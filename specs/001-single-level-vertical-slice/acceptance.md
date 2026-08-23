# Acceptance and Expansion Gates

Status: BASELINE  
Feature: SS-001

## Evidence rule

Each criterion requires a linked test, replay fixture, measurement, or recorded playtest result. A verbal assertion is not evidence.

## Gate A — Functional completion

- [ ] A-001 A clean install can start, complete, restart, and complete another run.
- [ ] A-002 All seven journey spaces are present and connected.
- [ ] A-003 Camera regions match authoritative detection.
- [ ] A-004 Blocking geometry reliably interrupts Camera detection.
- [ ] A-005 Exposure and every Detection State transition are communicated.
- [ ] A-006 Guards and Interceptors never spawn inside blocking geometry or the protected spawn area.
- [ ] A-007 Damage always has a visible or communicated source.
- [ ] A-008 All three upgrades materially change play and can complete the level.
- [ ] A-009 Captain defeat reliably unlocks Extraction.
- [ ] A-010 Extraction countdown visibly resets when the player leaves.
- [ ] A-011 Terminal events occur once and obey documented precedence.
- [ ] A-012 Result records contain all fields required by FR-045.

## Gate B — Determinism

- [ ] B-001 Three executions of every golden replay produce identical critical events and state digests.
- [ ] B-002 Golden replays pass on every supported architecture and target device.
- [ ] B-003 Restart restores the same initial state for the same Replay Identity.
- [ ] B-004 Suspend/resume does not advance authoritative state from wall-clock time.
- [ ] B-005 Unknown replay versions fail with a typed incompatibility result.
- [ ] B-006 Collection order, targeting ties, spawn ties, and terminal ties have tests.
- [ ] B-007 A rules-affecting change cannot alter a golden result without an explicit version change and rationale.

## Gate C — Stability and performance

Owner decisions T000 and T001 must set exact thresholds.

- [ ] C-001 Full runs complete without crash, soft lock, or unbounded memory growth.
- [ ] C-002 Worst-case encounters maintain the declared frame-time budget.
- [ ] C-003 Pools remain bounded and contain no stale lifecycle state.
- [ ] C-004 Development instrumentation confirms entity counts remain within declared limits.
- [ ] C-005 Ten consecutive automated complete-run simulations pass.
- [ ] C-006 Twenty manual restarts across all phases pass.

## Gate D — Comprehension and fairness

- [ ] D-001 New players learn movement without external explanation.
- [ ] D-002 New players correctly identify Camera detection regions.
- [ ] D-003 New players can explain how to reduce Exposure.
- [ ] D-004 Players understand why Lockdown began.
- [ ] D-005 Players can attribute each recorded death to an observable cause.
- [ ] D-006 Color is not the sole carrier of Detection State or damage information.
- [ ] D-007 Text and critical indicators are readable on every supported display size.
- [ ] D-008 Every upgrade path can defeat the Captain without requiring undocumented exploits.

## Gate E — Playtest signal

Test with at least five people who did not implement the feature.

- [ ] E-001 At least four of five complete the onboarding sequence without instruction.
- [ ] E-002 At least four of five correctly describe Exposure after one run.
- [ ] E-003 No repeated confusion pattern remains unresolved.
- [ ] E-004 At least three of five voluntarily begin another run.
- [ ] E-005 Median competent successful run duration is within 8–12 minutes after onboarding.
- [ ] E-006 Qualitative feedback identifies surveillance pressure—not generic combat—as a defining feature.

## Expansion decision

A second level is authorized only when Gates A–E pass and all severity-one and severity-two defects are closed.

Possible decisions:

- `EXPANSION_GATE_PASSED`
- `EXPANSION_GATE_FAILED`
- `EXPANSION_GATE_NOT_COMPUTABLE`

Failure does not authorize scope reduction through undocumented exceptions. Correct the slice, update the specification through governance, or record why evidence is insufficient.
