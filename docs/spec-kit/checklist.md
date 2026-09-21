# Spec Kit checklist — SS-001 requirements quality

**Phase:** optional Spec Kit `checklist` (“unit tests for English”).  
**Canonical product audit:** [`specs/001-single-level-vertical-slice/completeness-audit.md`](../../specs/001-single-level-vertical-slice/completeness-audit.md) (`completeness-audit-001`, 2026-08-24).  
**Kind:** reviewer-owned requirements-quality index. `[x]` means the **specification** already answers the question. It does not mean runtime work is done.

Do not add gameplay requirements here. If a row fails, tighten `spec.md` or the owning contract. Do not invent Exposure, Detection State, Lockdown, Algorithmic Moderate, or Extraction synonyms.

Contributor Workflows stay in [`AGENTS.md`](../../AGENTS.md). A missing pointer in `spec.md` fails this checklist.

| ID | Requirements-quality question | Result | Lands on |
|---|---|---|---|
| Q-01 | Is the one-level scope and non-goal list explicit? | [x] | `spec.md` §2; constitution I/V/VIII |
| Q-02 | Is ubiquitous language defined and used without harvest synonyms? | [x] | `spec.md` §3; AGENTS.md |
| Q-03 | Are user-facing journeys and user stories present? | [x] | `spec.md` §4, §7 (US-001–US-005) |
| Q-04 | Are functional requirements observable and testable? | [x] | `spec.md` §5 FR-001–FR-056 |
| Q-05 | Are Detection State order and Lockdown latch specified? | [x] | `spec.md` §6; `exposure.md` |
| Q-06 | Are edge cases and terminal precedence specified? | [x] | `spec.md` §8 |
| Q-07 | Are success outcomes distinct from implementation tasks? | [x] | `spec.md` §9; `acceptance.md` |
| Q-08 | Does specify bind Workflows by pointer, not by pasting skill tables? | [x] | `spec.md` Workflows pointer; D-064 |
| Q-09 | Does plan keep stack/architecture out of the product what/why? | [x] | `plan.md` |
| Q-10 | Do tasks trace to requirements or gates, with open items reconciled? | [x] | `tasks.md`; `validate_specs.py` |
| Q-11 | Is the expansion gate recorded and closed to new cities? | [x] | `acceptance.md`; constitution VIII |
| Q-12 | Is implement correctly out of this repository? | [x] | README; `plan.md` runtime boundary |

**Stale-but-folded (do not re-verdict here):** `completeness-audit.md` is dated 2026-08-24. Later accepted decisions D-060–D-066, the run-shell stub, and the 2026-09-21 extension-points audit are not restated in that file. That is a dated snapshot, not a license to invent a new completeness verdict.

**Not in this checklist:** playtest Gates G-001–G-007, device ceilings D-020/D-021, and the 30 open tasks. Those are evidence or production, not English-completeness.
