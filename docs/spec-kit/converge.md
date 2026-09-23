# Spec Kit converge — SS-001 implementation vs artifacts

**Phase:** Spec Kit `converge` (compare runtime evidence to spec / plan / tasks).  
**Date:** 2026-09-21.  
**Status:** `NOT_CONVERGED`  
**Kind:** process pointer. This file does not append tasks and does not invent remaining work.

Implement lives in `scrimshawlife-ctrl/SS-runtime`. Spec Kit converge is append-only on `tasks.md`. This stub **does not write tasks**. The honest remaining work is already listed.

## Folded artifacts

| Converge question | Canonical answer |
|---|---|
| What must be true for the player? | `spec.md` FR/US rows; ubiquitous language |
| How is it built? | `plan.md` |
| What work remains? | `tasks.md` open-task reconciliation (28 unchecked rows) |
| What evidence closes a gate? | `acceptance.md` Gates A–G |
| What is still a dated design-complete snapshot? | `completeness-audit.md` verdict `RUNTIME_CONTRACT_COMPLETE_EVIDENCE_PENDING` |

## Current result (**OBSERVED**)

Not converged. `tasks.md` already records the gap without a second list:

- Device / matrix evidence: T406, T606, T901, T905.
- Owner decisions: T306, T506, T802, T804, T806, T907, T908; D-020, D-021.
- Art / production: T503–T509, T601–T603, T800.
- Legacy archaeology: T101, T105.
- Defect closure after evidence: T906.

Acceptance checkboxes in `acceptance.md` remain unchecked. A harness is not evidence.

## Rules for a later converge pass

1. Run it only after runtime work against the current `tasks.md`.
2. Append a task only for an **OBSERVED** gap that is not already in the open-task table.
3. Do not close a *run* / *record* / *measure* / *decide* / *produce* task on a harness.
4. Do not write `HANDOFF.md` (owner hold; extension audit G-14).
5. Do not treat `NOT_CONVERGED` as permission for a second city, SIGN, store subtitle, or a new meter.
