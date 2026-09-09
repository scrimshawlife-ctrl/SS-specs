#!/usr/bin/env python3
"""Fail-closed consistency checks for the specification repository.

Every check here is a rule the specification already states in prose:
contracts are versioned and registered, machine artifacts conform to their
schemas, and the README is the canonical index. This script only makes the
rules executable so a pull request cannot silently drift.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


# 1. Every JSON artifact parses.
json_paths = sorted(p for p in ROOT.rglob("*.json") if ".git" not in p.parts)
documents = {}
for path in json_paths:
    try:
        documents[path] = load_json(path)
    except Exception as exc:  # noqa: BLE001 — report and continue
        err(f"{path.relative_to(ROOT)}: does not parse ({exc})")

# 2. Every schema is a valid Draft 2020-12 schema.
schema_paths = [p for p in documents if p.name.endswith(".schema.json") or p.name == "runtime-kernel-001.json"]
for path in schema_paths:
    try:
        Draft202012Validator.check_schema(documents[path])
    except Exception as exc:  # noqa: BLE001
        err(f"{path.relative_to(ROOT)}: invalid schema ({exc})")


def validate_instance(instance_rel: str, schema_rel: str, label: str | None = None) -> None:
    instance_path, schema_path = ROOT / instance_rel, ROOT / schema_rel
    if instance_path not in documents or schema_path not in documents:
        err(f"{label or instance_rel}: missing instance or schema")
        return
    validator = Draft202012Validator(documents[schema_path])
    for problem in sorted(validator.iter_errors(documents[instance_path]), key=lambda e: list(e.path)):
        where = "/".join(str(part) for part in problem.path) or "<root>"
        err(f"{label or instance_rel} !~ {schema_rel} at {where}: {problem.message[:160]}")


# 3. Machine artifacts conform to the schema that governs them.
validate_instance("contracts/civic-seam-arena-001.json", "contracts/civic-seam-arena-001.schema.json")
validate_instance("fixtures/replay-smoke-001.json", "contracts/runtime-kernel-001.json")
validate_instance("contracts/camera-placement-001.json", "contracts/camera-placement-001.schema.json")

# 3a. The placement instance is the arena's authored socket inventory wrapped
# in the placement identity fields (D-066). The schema proves each socket is
# well-formed; this proves the inventory did not drift from the arena
# manifest the runtime loads, and that the authored pool still meets the
# minimum enabled sizes camera-placement.md requires per zone.
placement = documents.get(ROOT / "contracts/camera-placement-001.json")
manifest = documents.get(ROOT / "contracts/civic-seam-arena-001.json")
if isinstance(placement, dict) and isinstance(manifest, dict):
    sockets = placement.get("sockets")
    if not isinstance(sockets, list):
        err("camera-placement-001 sockets is not an array")
    else:
        if sockets != manifest.get("cameraSockets"):
            err("camera-placement-001 sockets drifted from the arena manifest cameraSockets")
        enabled_by_zone: dict[str, int] = {}
        for socket in sockets:
            if not isinstance(socket, dict) or not socket.get("enabled"):
                continue
            zone = socket.get("zoneId")
            if isinstance(zone, str):
                enabled_by_zone[zone] = enabled_by_zone.get(zone, 0) + 1
        for zone, need in (("Z-02", 4), ("Z-03", 3), ("Z-04", 4), ("Z-05", 4), ("Z-06", 3)):
            have = enabled_by_zone.get(zone, 0)
            if have < need:
                err(f"camera-placement-001 {zone} has {have} enabled sockets; camera-placement.md requires at least {need}")

catalog_path = ROOT / "contracts/asset-catalog-001.json"
record_schema_path = ROOT / "contracts/asset-record-001.schema.json"
if catalog_path in documents and record_schema_path in documents:
    validator = Draft202012Validator(documents[record_schema_path])
    entries = documents[catalog_path].get("entries", [])
    for index, entry in enumerate(entries):
        # Catalog entries wrap the record with the admission decision that
        # accepted it; the schema governs the record.
        if not isinstance(entry, dict) or "record" not in entry or "admissionDecision" not in entry:
            err(f"asset-catalog-001 entries[{index}] is not an {{admissionDecision, record}} pair")
            continue
        for problem in validator.iter_errors(entry["record"]):
            where = "/".join(str(part) for part in problem.path) or "<root>"
            err(f"asset-catalog-001 entries[{index}] ({entry['record'].get('assetId', '?')}) !~ asset-record-001 at {where}: {problem.message[:140]}")
            break  # one problem per entry keeps the report readable

# 4. Every identity in contracts/versions.json resolves to a real artifact.
version_token = re.compile(r"\b[a-z][a-z0-9]*(?:-[a-z0-9]+)*-\d{3}\b")
declared: set[str] = set()
for path, doc in documents.items():
    declared.add(path.stem.removesuffix(".schema"))

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, str) and key.lower().endswith("version") or key in {"schemaVersion", "contract", "fixtureVersion"}:
                    if isinstance(value, str):
                        declared.add(value)
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(doc)
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    for match in re.finditer(r"version[^\n`]*`([^`]+)`", text, flags=re.I):
        declared.add(match.group(1))

versions = documents.get(ROOT / "contracts/versions.json", {})
for key in ("schemaVersion", "rulesetVersion", "contentVersion", "arenaVersion"):
    value = versions.get(key)
    if value not in declared:
        err(f"versions.json {key}={value!r} is not declared by any artifact")
for key, value in versions.get("componentContracts", {}).items():
    if value not in declared:
        err(f"versions.json componentContracts.{key}={value!r} is not declared by any artifact")

# 5. The README index is complete and every link resolves.
readme = (ROOT / "README.md").read_text(encoding="utf-8")
linked = {ROOT / target for target in re.findall(r"\]\(([^)#]+)\)", readme) if not target.startswith("http")}
for target in sorted(linked):
    if not target.exists():
        err(f"README links to missing file {target.relative_to(ROOT)}")
artifacts = [p for d in ("contracts", "fixtures", "specs") for p in (ROOT / d).rglob("*") if p.is_file()]
for path in sorted(artifacts):
    if path not in linked:
        err(f"README index does not list {path.relative_to(ROOT)}")

# 6. tasks.md reconciliation integrity.
# The "Open task reconciliation (honest gap)" table states, for every unchecked
# task, the status, blocker, required owner/input, and the evidence that would
# close it. Keep that table in lockstep with the checklist: every open task must
# be reconciled exactly once, no reconciled task may be already checked, and no
# ID may be reconciled twice. This is documentation integrity only — it fails
# closed on drift, it does not assert that any task's evidence exists.
tasks_path = ROOT / "specs" / "001-single-level-vertical-slice" / "tasks.md"
if not tasks_path.exists():
    err("tasks.md is missing; cannot check open-task reconciliation integrity")
else:
    tasks_text = tasks_path.read_text(encoding="utf-8")
    open_ids = {m.group(1) for m in re.finditer(r"^- \[ \] (T[0-9A-Z]+)", tasks_text, flags=re.M)}
    closed_ids = {m.group(1) for m in re.finditer(r"^- \[x\] (T[0-9A-Z]+)", tasks_text, flags=re.M)}
    head = "## Open task reconciliation"
    tail = "## Traceability rule"
    if head not in tasks_text or tail not in tasks_text:
        err("tasks.md is missing the open-task reconciliation section or the traceability rule")
    else:
        section = tasks_text.split(head, 1)[1].split(tail, 1)[0]
        reconciled = [m.group(1) for m in re.finditer(r"^\| (T[0-9A-Z]+) \|", section, flags=re.M)]
        if len(reconciled) != len(set(reconciled)):
            dupes = sorted({t for t in reconciled if reconciled.count(t) > 1})
            err(f"tasks.md reconciliation reconciles these task IDs more than once: {', '.join(dupes)}")
        reconciled_set = set(reconciled)
        for task_id in sorted(open_ids - reconciled_set):
            err(f"tasks.md task {task_id} is open but has no reconciliation row (status/blocker/owner/evidence)")
        for task_id in sorted(reconciled_set & closed_ids):
            err(f"tasks.md task {task_id} is checked but still carries a reconciliation row; reconcile it or drop the row")
        for task_id in sorted(reconciled_set - open_ids - closed_ids):
            err(f"tasks.md reconciliation references {task_id}, which is not present in the task checklist")

if errors:
    print(f"validate_specs: {len(errors)} problem(s)")
    for line in errors:
        print(f"  - {line}")
    sys.exit(1)
print(f"validate_specs: OK — {len(json_paths)} JSON artifacts, {len(schema_paths)} schemas, "
      f"{len(versions.get('componentContracts', {}))} registered contracts, {len(artifacts)} indexed files")
