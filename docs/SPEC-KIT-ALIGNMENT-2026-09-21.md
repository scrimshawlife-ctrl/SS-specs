# Spec Kit alignment — SS-specs

**Repo:** `scrimshawlife-ctrl/SS-specs` at `81c29b18` (main) plus this change.  
**Date:** 2026-09-21.  
**Kind:** docs/process alignment. No gameplay rules, store copy, SIGN, or HANDOFF invented here.

**Canonical Spec Kit:** [github/spec-kit](https://github.com/github/spec-kit) and [Agentic SDD](https://github.github.io/spec-kit/reference/agentic-sdd.html).  
**This-repo locks win** when they conflict with generic Spec Kit defaults. See [`AGENTS.md`](../AGENTS.md) and D-062–D-064, D-067.

**Labels:** **OBSERVED** = in this repository or the cited Spec Kit page. **INFERRED** = mapping judgment.

---

## 0. Language and process locks (read first)

Canonical SS-001 terms stay: **Exposure**, **Detection State**, **Camera**, **Lockdown**, **Algorithmic Moderate**, **Extraction**.

Do not import SS-MAP harvest verbs as product vocabulary (Suspicion, LPR, Blind Spot). Harvest remains a mapping aid. See [`EXTENSION-POINTS-AUDIT-2026-09-21.md`](EXTENSION-POINTS-AUDIT-2026-09-21.md).

Product-true process locks that override generic Spec Kit:

| Lock | Source | What it changes vs generic Spec Kit |
|---|---|---|
| Intent before specify | D-063, `intent/README.md` | Spec Kit has no `intent/` phase. This repo requires `intent.md` for non-trivial work. |
| Workflows live in AGENTS.md | D-064 | Spec Kit wants a Workflows table inside `spec.md`. This repo binds by **pointer only**. |
| One Civic Seam level | Constitution I/VIII | No second city until `EXPANSION_GATE_PASSED` and a constitution amendment. |
| No HANDOFF.md | Owner hold; extension audit G-14 | Spec Kit converge does not authorize a HANDOFF document. |
| Markdown artifacts, not `.specify` | This alignment | Do not install the Specify CLI or a `.specify/` tree unless the owner names that work. |
| Existing CI only | D-062 | Keep `.github/workflows/validate.yml` → `scripts/validate_specs.py`. Do not add a Spec Kit Action. |

---

## 1. Spec Kit phase order

**OBSERVED** from Spec Kit Agentic SDD:

`constitution → specify → [clarify] → plan → [checklist] → tasks → [analyze] → implement → converge`

**This repo** inserts `intent/` after constitution and before specify, and keeps implement in `scrimshawlife-ctrl/SS-runtime`.

```text
constitution → intent → specify → [clarify] → plan → [checklist] → tasks → [analyze] → implement (SS-runtime) → [converge]
```

Only specify is strictly required before plan in Spec Kit. This repo additionally requires intent for feature- or RFC-sized work.

---

## 2. Gap table

| Spec Kit phase | Expected artifact | SS-specs today | Verdict | This PR |
|---|---|---|---|---|
| constitution | Project principles | `specs/000-constitution.md` v1.1.0 | **Present.** Named `000-constitution.md`, not root `constitution.md`. | Map only. |
| intent | (not in Spec Kit) | `intent/` + `_TEMPLATE.md` + D-063 | **Present.** This-repo gate. Template and practice drifted on one historical file. | Document the gate; keep the template as the copy source. |
| specify | `spec.md` what/why + Workflows | `specs/001-single-level-vertical-slice/spec.md` | **Present.** No Workflows *pointer* (**OBSERVED**). Skill tables correctly absent (D-064). | Add a short pointer section. |
| clarify | Optional; answers encoded into spec/decisions | `decisions.md`, intent Open questions | **Folded.** No standalone `clarify.md`. Civic Seam baseline is already specified. | Defer a dedicated file. |
| plan | How / stack / architecture | `plan.md` | **Present.** Three stale identity lines (**OBSERVED**). | Correct constitution version, runtime repo, legacy tag date. |
| checklist | Requirements-quality (“unit tests for English”) | `completeness-audit.md` (2026-08-24) | **Folded, dated.** Audit is a completeness pass, not a Spec Kit-shaped checklist. | Thin stub at `docs/spec-kit/checklist.md`. |
| tasks | Dependency-ordered work | `tasks.md` + open-task reconciliation | **Present.** Phases are delivery slices, not Spec Kit Setup/Foundational/user-story/Polish. Validate enforces reconciliation. | Map only. Do not rewrite the task list. |
| analyze | Read-only spec/plan/tasks coverage | No named analyze report | **Missing.** Completeness audit is the nearest historical pass. | Thin stub at `docs/spec-kit/analyze.md`. |
| implement | Execute tasks | `scrimshawlife-ctrl/SS-runtime` | **Out of this repo.** README already says so. | Map only. |
| converge | Compare runtime to spec/plan/tasks; append remaining work | `acceptance.md` + `tasks.md` reconciliation | **Folded, not named.** Gates A–G unchecked; 30 open tasks. | Thin stub at `docs/spec-kit/converge.md`. Do not invent tasks. |
| taskstoissues | Optional GitHub issues from tasks | Absent | **Deferred.** Owner did not name a new Action or issue mill. | Follow-up only. |
| `.specify` CLI / templates | `specify init` toolchain | Absent (**OBSERVED**: no `.specify/`) | **Deferred on purpose.** | Follow-up note only. |

---

## 3. Gaps closed in this change

1. README states the Spec Kit phase map and indexes the process docs, including the extension-points audit.
2. `spec.md` has a Workflows **pointer** to `AGENTS.md`. No skill table was copied into the product specification.
3. `AGENTS.md` Method lists optional Spec Kit gates without moving Workflows into `spec.md`.
4. `intent/README.md` and `_TEMPLATE.md` state the specify gate and Status values used in practice.
5. Thin Spec Kit-shaped stubs exist for checklist, analyze, and converge. They fold existing artifacts and do not add FRs.
6. `plan.md` identity lines match constitution 1.1.0, `SS-runtime`, and D-013’s legacy tag date.
7. D-067 records this alignment.

---

## 4. Gaps deferred

| Item | Why deferred |
|---|---|
| Install Specify CLI / `.specify/` | Owner has not named a toolchain refresh. Markdown artifacts already match the phase split. |
| Dedicated `clarify.md` | Optional gate. Open questions already live in intents and `decisions.md`. A new file would invent a questionnaire. |
| Rewrite `tasks.md` into Spec Kit user-story phases | Would churn a validate-locked reconciliation table without changing work. |
| Refresh `completeness-audit.md` to 2026-09-21 | That audit is a dated evidence snapshot. Re-authoring it here would invent a new completeness verdict. |
| Close acceptance gates / open tasks | Evidence-owned. Harnesses are not evidence. |
| `taskstoissues` | Would create GitHub issues. Not requested. |
| HANDOFF.md | Owner hold. Converge does not authorize it. |
| Wire `docs/` into `validate_specs.py` as a required index | Not needed for CI green. The script still requires every `specs/`, `contracts/`, and `fixtures/` file in README. |

---

## 5. How new work should run

For typo or index-only edits: skip intent.

For non-trivial, feature, or RFC-sized work:

1. Copy `intent/_TEMPLATE.md`. Stop after intent until it is `accepted`.
2. Specify observable what/why. Add or keep the Workflows pointer. Do not paste the skill table.
3. Clarify only if an area is still underspecified; encode answers into `spec.md` or `decisions.md`.
4. Plan the how. Carry the same Workflows pointer.
5. Optionally walk `docs/spec-kit/checklist.md` before tasks.
6. Update `tasks.md` and its reconciliation table together (validate fails closed on drift).
7. Optionally walk `docs/spec-kit/analyze.md` before runtime work.
8. Implement in `SS-runtime`, citing task and requirement IDs.
9. Converge against `acceptance.md` and the open-task table. Append tasks only for OBSERVED gaps. Do not write HANDOFF.md.

---

## 6. What this alignment is not

- Not a constitution amendment.
- Not a new feature slice and not a product `intent.md`.
- Not permission to add cities, meta-progression, shop, gacha, a second meter, SIGN, or store subtitle.
- Not permission to install `.specify` or add a GitHub Action.
- Not a claim that Civic Seam has converged.
