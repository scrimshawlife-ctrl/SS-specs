# Spec Kit analyze — SS-001 cross-artifact coverage

**Phase:** optional Spec Kit `analyze` (read-only coverage of spec / plan / tasks).  
**Date:** 2026-09-21.  
**Kind:** process report. This file does not edit product contracts and does not invent FRs.

Spec Kit analyze never writes code. Findings below are labeled **OBSERVED** or **INFERRED**.

## Consistent (**OBSERVED**)

- Constitution 1.1.0 Article V roster matches `spec.md` non-goals and the Civic Seam one-level lock.
- Ubiquitous language in `spec.md` §3 matches AGENTS.md. Harvest verbs (Suspicion, LPR, Blind Spot) are not product terms.
- D-062/D-064 keep Workflows in AGENTS.md. `spec.md` now points there instead of pasting the skill table.
- `tasks.md` open IDs match the reconciliation table. `scripts/validate_specs.py` fails closed on drift.
- Implement is scoped to `scrimshawlife-ctrl/SS-runtime`. This repo does not claim runtime CI.
- No `.specify/` toolchain is present. Phase artifacts are Markdown.

## Corrected in the alignment change (**OBSERVED**)

These were identity drift, not new design:

| Finding | Was | Now |
|---|---|---|
| `plan.md` constitution pin | 1.0.0 | 1.1.0 (amendment already recorded in `completeness-audit.md`) |
| `plan.md` runtime repository | `scrimshawlife-ctrl/SS` (“will be”) | `scrimshawlife-ctrl/SS-runtime` (README baseline) |
| `plan.md` legacy tag date | `legacy-multicity-2026-08-23` | `legacy-multicity-2026-08-24` (D-013) |

## Remaining coverage notes (not closed here)

| Finding | Label | Owner |
|---|---|---|
| `completeness-audit.md` date is 2026-08-24; D-060–D-066, run-shell, and the extension-points audit are later | **OBSERVED** | Do not invent a new audit verdict in this file |
| `acceptance.md` A-006 names “Guards and Interceptors”; the canonical five archetypes live in `enemies-and-encounters.md` | **OBSERVED** naming leftover | Fold on a spec pass; do not add enemies |
| `tasks.md` T002 still says reserve `scrimshawlife-ctrl/SS` | **OBSERVED** historical checked task | Leave the checked row; the live name is `SS-runtime` |
| `run-shell.md` is `PROPOSED`; title/terminal copy remains OPEN | **OBSERVED** | Existing stub; no HANDOFF |
| `intent/2026-09-07-fog-layers.md` is still `draft` | **OBSERVED** | Specify only after acceptance |
| Gates A–G unchecked; 30 open tasks; D-020/D-021 pending | **OBSERVED** | Evidence / owner specialist |
| Historical `intent/2026-09-04-legacy-art-admission.md` does not copy `_TEMPLATE.md` headings exactly | **OBSERVED** | New intents copy the template; do not rewrite accepted history |

## Remediation rule

Fix requirement problems in `spec.md` or the owning contract. Fix design problems in `plan.md`. Fix task drift in `tasks.md` together with the reconciliation table. Do not silently mark analyze findings done.
