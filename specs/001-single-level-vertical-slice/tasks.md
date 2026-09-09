# Implementation Tasks

Status: READY_FOR_REVIEW  
Feature: SS-001

Tasks are ordered. Runtime implementation belongs in the future runtime repository.

## Phase 0 — Specification and repository boundary

- [x] T000 Record iPhone-only, iOS 18, landscape, touch, and device-matrix decisions.
- [x] T001 Record 60 Hz simulation and physical-device frame-time thresholds.
- [x] T002 Reserve `scrimshawlife-ctrl/SS` as the future runtime repository identity.
- [x] T003 Define visual, animation, arena, production, and accessibility baselines.
- [x] T004 Create annotated legacy-repository tag `legacy-multicity-2026-08-24` at accepted SHA `3b20d88d6a6e1fe8f07f45f581359d371fa65d98`.
- [x] T005 Complete cross-artifact consistency and specification-quality review.
- [x] T006 Create the runtime repository and link its first commit to the accepted specification SHA.
- [x] T007 Establish ruleset, level, replay-schema, asset-schema, arena-schema, and save-schema version policies.

- [x] T008 Lock Exposure, controller, base combat, simulation order, and version identities.
- [x] T009 Lock Camera socket randomization, enemy/encounter tables, bosses, and upgrades.
- [x] T010 Lock exact arena coordinates, solids, gates, triggers, sockets, emitters, viewport, and Extraction geometry.
- [x] T011 Lock HUD/tutorial, audio/haptics, event catalog, replay, receipt, and presentation asset identities.

## Phase 1 — Legacy admission

- [x] T100 Record observed immutable legacy paths and evidence limits for LC-001 through LC-010.
- [ ] T101 Recover tests and dependency boundaries for deterministic kernel candidates.
- [x] T102 Classify campaign, procedural district, challenge, and non-SF content as excluded.
- [x] T103 Classify SF assets individually with provenance and runtime relevance.
- [x] T104 Record ADMIT, ADAPT, REWRITE, or REJECT for every candidate.
- [ ] T105 Stop legacy migration when any copied source lacks an approved record.

## Phase 2 — Deterministic kernel

- [x] T200 Implement fixed-step SimulationClock.
- [x] T201 Implement seeded random generator with golden sequence tests.
- [x] T202 Define stable entity IDs and ordered iteration rules.
- [x] T203 Define normalized tick-indexed player commands.
- [x] T204 Implement replay envelope loading and incompatibility errors.
- [x] T205 Implement final state digest and first golden replay fixture.
- [x] T206 Verify restart restores the initial authoritative state.

## Phase 3 — Grayscale arena blockout

- [x] T300 Define arena, zone, collision, Camera, navigation, and spawn schemas.
- [ ] T301 Build the 36 × 24-cell baseline arena with seven canonical zones.
- [x] T302 Validate reachability, minimum widths, viewport margins, and Spawn Alley protection.
- [x] T303 Implement collision, Camera, spawn, safe-area, and density debug overlays.
- [x] T304 Build SE-class and standard-iPhone HUD blockouts for both handedness modes.
- [ ] T305 Run first-run and competent-run pacing probes.
- [ ] T306 Freeze the accepted blockout before final environment production.
- [x] T307 Establish diagonal spine, three-grid collision, wedge parcels, and landmark sightlines.
- [x] T308 Validate Civic Seam identity without labels or literal map reproduction.

## Phase 4 — Surveillance and combat blockout

- [x] T400 Implement Camera data, deterministic LOS, and occlusion.
- [x] T401 Implement Exposure, recovery, thresholds, state cues, and Lockdown latch.
- [x] T402 Render Camera fields from authoritative data.
- [x] T403 Implement deterministic target selection, base attack, damage, and death.
- [x] T404 Implement projectile pooling with complete lifecycle reset.
- [x] T405 Implement Guard and Interceptor blockouts with distinct silhouettes.
- [ ] T406 Profile peak density on iPhone 12 and decide D-021 ceilings.
- [x] T407 Validate spawn fairness and visual escape corridors.
- [x] T408 Author at least 18 Camera sockets; deterministically select exactly eight by seed/quota and assert selected transforms/fields remain immutable.
- [x] T408B Exhaustively validate every legal Camera selection and implement CP-001 through CP-010.
- [ ] T408A Implement Camera Integrity 3→2→1→0 and exact damage eligibility.
- [x] T409 Implement Camera-aware automatic-target priority and stable tie-breaking.
- [x] T410 Implement destruction contact removal, +100 Tamper, and Lockdown transition order.
- [x] T411 Implement permanent per-run Camera destruction with complete restart restoration.
- [x] T413 Implement Network Blackout counter, eighth-destruction event, partial receipt, and accolade.
- [x] T414 Prove Camera state never enters the Extraction predicate.
- [x] T412 Implement CD-001 through CD-012 golden vectors.

## Phase 5 — Visual language and asset pipeline

- [x] T500 Establish role palette, shape language, contact points, and salience hierarchy.
- [x] T501 Implement asset manifest and provenance validation.
- [x] T502 Implement deterministic naming, dimensions, alpha, sRGB, content, duplicate, and atlas checks.
- [ ] T503 Produce Player, Guard, Interceptor, Captain, Camera, objective, and upgrade silhouette sheets.
- [ ] T504 Produce grayscale, color-vision, dense-combat, and reduced-presentation review plates.
- [ ] T505 Establish bounded atlases and preload measurements.
- [ ] T506 Approve the minimum asset inventory before polish assets.
- [ ] T507 Produce the six Civic Seam Camera housing families.
- [ ] T508 Produce architectural module sheets and recombination tests.
- [ ] T509 Produce the original phoenix, repair, human-counter-signal, and broadcast-glyph motif sheets.

## Phase 6 — Animation and VFX

- [x] T600 Implement clip metadata and authoritative event markers.
- [ ] T601 Produce minimum Player clips.
- [ ] T602 Produce Guard and Interceptor clip families.
- [ ] T603 Produce the finite Captain animation and telegraph vocabulary.
- [x] T604 Implement bounded procedural VFX and reduced variants.
- [x] T608 Produce Camera operational, damaged, critical, destroyed, dormant, hit, and field-off presentation.
- [x] T609 Implement first-encounter Camera tutorial, Integrity notches, and +100 TAMPER feedback.
- [x] T610 Integrate Camera hit, critical, destruction, network-tamper, and field-off audio events.
- [x] T605 Verify anchors, mirroring, interruption, cancellation, and event alignment.
- [x] T607 Implement bounded Civic Seam ambient motion with seeded cosmetic scheduling.
- [ ] T606 Measure animation, VFX, draw, and transient-node budgets on iPhone 12.

## Phase 7 — Upgrades, Captain, and Extraction

- [ ] T700 Implement protected upgrade selection.
- [x] T701 Implement Signal Jammer, Ricochet Pulse, and Ghost Step.
- [x] T702 Implement Captain phases and defeat.
- [x] T703 Implement the three-mob → Improper Search Daemon → Algorithmic Moderate → Extraction objective graph.
- [x] T703A Implement Extraction locking, countdown, reset-on-exit, and completion.
- [x] T704 Implement terminal precedence and immutable result records.
- [x] T707 Add Camera destruction/Network Blackout receipt summary and ordered destruction entries.
- [x] T708 Add canonical combat-authority and boss-phase receipt fields.
- [x] T705 Add complete-run golden vectors for every upgrade.
- [x] T706 Verify every upgrade completes the level without exploits.

## Phase 8 — Final San Francisco production

- [ ] T800 Produce approved Civic Seam P0 modular environment families.
- [x] T801 Integrate only runtime-reachable SS-001 assets.
- [ ] T802 Perform Civic Seam P1 identity pass without weakening affordances.
- [ ] T806 Add P2 polish only after P0/P1 device acceptance.
- [x] T807 Verify no prohibited landmark, seal, logo, copied artwork, or geographically incoherent shorthand ships.
- [x] T803 Complete audio, haptic, HUD, and objective presentation.
- [ ] T804 Pass asset provenance and device acceptance.
- [x] T805 Remove unreachable, duplicate, source, and non-SF assets from the bundle.

## Phase 9 — Acceptance

- [x] T900 Instrument frame time, memory, thermal state, entities, particles, Exposure, damage, and outcomes.
- [ ] T901 Pass deterministic replays across the supported matrix.
- [ ] T902 Pass functional, visual, arena, animation, accessibility, and edge-case gates.
- [ ] T903 Run onboarding comprehension playtests.
- [ ] T904 Run voluntary-replay playtests with at least five external participants.
- [ ] T905 Run three consecutive physical-device complete runs on the performance floor.
- [ ] T906 Fix all severity-one and severity-two defects.
- [ ] T907 Record release-candidate evidence.
- [ ] T908 Decide whether the expansion gate passes.

## Evidence (2026-09-01 reconciliation)

Checked tasks link to the runtime pull request or commit that carries their verification. Tasks whose text is *run*, *record*, *measure*, *pass*, or *decide* stay open until the artifact exists; harnesses for them (T901–T908) exist in SS-runtime #34–#41 but are not evidence.

| Task | Evidence |
|---|---|
| T004 | tag `legacy-multicity-2026-08-24` (`e085ea8`) |
| T006 | SS-runtime `7e04ef1` |
| T007 | SS-runtime `SPEC_BASELINE.md`, `ContractVersions.swift` (`7e04ef1`) |
| T103 | SS-runtime `b8d3467` |
| T200 | SS-runtime `913b62a` |
| T201 | SS-runtime `913b62a` |
| T202 | SS-runtime `913b62a` |
| T203 | SS-runtime `913b62a` |
| T204 | SS-runtime `913b62a` |
| T205 | SS-runtime `913b62a` |
| T206 | SS-runtime `913b62a` |
| T300 | SS-runtime `913b62a` |
| T302 | SS-runtime `11d69ff` |
| T303 | SS-runtime `92fff69` |
| T304 | SS-runtime `92fff69` |
| T307 | SS-runtime `9a937b1` |
| T308 | SS-runtime `9a937b1` |
| T400 | SS-runtime `913b62a` |
| T401 | SS-runtime `92fff69` |
| T402 | SS-runtime `92fff69` |
| T403 | SS-runtime `92fff69` |
| T404 | SS-runtime `92fff69` |
| T405 | SS-runtime #6 |
| T407 | SS-runtime #8, #11 |
| T408 | SS-runtime #7 (`CameraPlacementTests`) |
| T408B | SS-runtime #7 |
| T409 | SS-runtime #9 |
| T410 | SS-runtime #10 |
| T411 | SS-runtime #12 |
| T412 | SS-runtime #15 |
| T413 | SS-runtime #13 |
| T414 | SS-runtime #14 |
| T500 | SS-runtime `11d69ff` |
| T501 | SS-runtime `b8d3467`, `11d69ff` |
| T502 | SS-runtime `11d69ff` |
| T600 | SS-runtime #16 |
| T604 | SS-runtime #17 |
| T605 | SS-runtime #21 |
| T607 | SS-runtime #22 |
| T608 | SS-runtime #18 |
| T609 | SS-runtime #19 |
| T610 | SS-runtime #20 |
| T701 | SS-runtime #23 |
| T702 | SS-runtime #24 |
| T703 | SS-runtime #25 |
| T703A | SS-runtime #26 |
| T704 | SS-runtime #27 |
| T705 | SS-runtime #30 |
| T706 | SS-runtime #30 |
| T707 | SS-runtime #28 |
| T708 | SS-runtime #29 |
| T801 | SS-runtime #33 |
| T803 | SS-runtime #31 |
| T805 | SS-runtime #32 |
| T807 | SS-runtime #32 |
| T900 | SS-runtime #34 |

Implemented in the runtime but **not cited** by any pull request, left unchecked pending citation: T301, T408A, T700. Range citation `T303-T404` (`92fff69`) is not accepted for T305/T306, which have no pacing or freeze artifact.

## Open task reconciliation (honest gap)

The 31 unchecked tasks above are **not agent-closable**. Each is a *run*, *record*, *measure*, *decide*, or *produce* item whose closure needs an input this specification does not own, and none of them may be closed on the strength of a harness. They group into six kinds, each with its required owner or input:

- **Device (iPhone 12 performance floor / supported matrix)** — T406, T606, T901, T905.
- **Human judgment / decision** — T306, T506, T802, T804, T806, T907, T908 (the expansion gate and any D-register decision require the owner specialist, Danny).
- **Artist / production** — T503, T504, T505, T507, T508, T509, T601, T602, T603, T800.
- **Runtime-implemented, awaiting a citing PR** — T301, T408A, T700.
- **Legacy archaeology** — T101, T105.
- **Developer (defect closure)** — T906.

A harness is a collector of evidence, not evidence. SS-runtime #34–#41 ship the peak-density profiler, replay matrix, playtest loader, gate registry, defect registry, release-evidence store, and expansion-gate report; each stays a collector until it has captured a real device run, a named participant, or a recorded decision. The pending decisions **D-020** (which physical devices are approved equivalents for the four device classes) and **D-021** (the exact measured ceilings) remain `DECISION_PENDING` and MUST NOT be replaced with invented answers; they block the device-class tasks until the owner records them.

**What counts as evidence:** a linked device capture or profile, a recorded playtest naming its participants, a recorded decision, a delivered asset carrying `asset-record-001` provenance, or a runtime PR that cites the task ID and links its verification. Until one of these exists and is linked, the task stays open.

| Task | Status | Blocker | Required owner / input | Evidence required |
|---|---|---|---|---|
| T101 | NOT_RUN | Legacy test suite and build environment at the frozen SHA `3b20d88` are NOT_COMPUTABLE; deterministic-kernel tests are unrecovered | Developer with legacy-repo access performs the recovery; owner specialist approves | A recovered, runnable deterministic-kernel test suite with recorded results at the frozen SHA |
| T105 | STANDING_GATE | Legacy migration is not complete; the gate is active until every copied source is approved | Every copied source carries an approved record before migration closes (owner specialist Danny) | An approved record per copied source (asset-record / admission decision) plus a migration-close note |
| T301 | PENDING_CITATION | The arena is implemented in SS-runtime but no PR cites T301 | Runtime team opens a PR citing T301 | A PR citing T301 that links the arena-geometry verification |
| T305 | NOT_RUN | No first-run or competent-run pacing probe has been run; the `T303-T404` range citation is not accepted | Designer / player runs the probes on a device (owner specialist Danny) | Recorded pacing probes compared against the `E-011` 8–12-minute target |
| T306 | NOT_DECIDED | The blockout freeze is a human judgment, pending pacing (T305) and density ceilings (T406) | Designer accepts the freeze (owner specialist Danny) | A recorded freeze decision referencing the pacing and density evidence |
| T406 | NOT_RUN | Peak-density profiling on an iPhone 12 (performance floor, D-011) is not run; D-021 ceilings are DECISION_PENDING | iPhone 12 device plus a human owner who settles D-021 | A device profile (resident memory, atlas memory, frame time) and a D-021 decision record |
| T408A | PENDING_CITATION | Camera Integrity is implemented in SS-runtime but no PR cites T408A | Runtime team opens a PR citing T408A | A PR citing T408A that links the Integrity / damage-eligibility verification |
| T503 | NOT_PRODUCED | The silhouette sheets are not produced | Artist delivers the sheets; intake records `asset-record-001` provenance | Delivered Player, Guard, Interceptor, Captain, Camera, objective, and upgrade silhouette sheets with provenance |
| T504 | NOT_PRODUCED | The review plates are not produced | Artist produces the plates | Delivered grayscale, color-vision, dense-combat, and reduced-presentation review plates with provenance |
| T505 | NOT_MEASURED | Bounded atlases and preload measurements are not recorded | Runtime builds the atlases and measures preload on a device | Bounded atlases plus a recorded preload measurement |
| T506 | NOT_DECIDED | Approving the minimum asset inventory is a human judgment | Designer / owner approves the inventory (owner specialist Danny) | A recorded approval decision for the minimum asset inventory |
| T507 | NOT_PRODUCED | The six Civic Seam Camera housing families are not produced | Artist delivers the families | Delivered housing families with provenance |
| T508 | NOT_PRODUCED | The architectural module sheets and recombination tests are not produced | Artist produces the sheets; runtime adds the recombination tests | Delivered module sheets plus passing recombination tests |
| T509 | NOT_PRODUCED | The motif sheets are not produced | Artist delivers the sheets | Delivered phoenix, repair, human-counter-signal, and broadcast-glyph motif sheets with provenance |
| T601 | NOT_PRODUCED | The minimum Player clips are not produced | Artist / animation production delivers the clips | Delivered minimum Player clips with provenance |
| T602 | NOT_PRODUCED | The Guard and Interceptor clip families are not produced | Artist delivers the families | Delivered Guard and Interceptor clip families with provenance |
| T603 | NOT_PRODUCED | The finite Captain animation and telegraph vocabulary are not produced | Artist delivers the set | Delivered Captain animation and telegraph vocabulary with provenance |
| T606 | NOT_MEASURED | Animation, VFX, draw, and transient-node budgets are not measured on an iPhone 12 | iPhone 12 device | Recorded budget measurements on an iPhone 12 |
| T700 | PENDING_CITATION | Protected upgrade selection is implemented in SS-runtime but no PR cites T700 | Runtime team opens a PR citing T700 | A PR citing T700 that links the selection verification |
| T800 | NOT_PRODUCED | The approved Civic Seam P0 modular environment families are not produced | Artist delivers the families; owner approves | Delivered P0 families with an approval decision and provenance |
| T802 | NOT_PERFORMED | The P1 identity pass is not performed and must not weaken affordances | Artist performs the pass; human confirms affordances hold | A completed P1 pass plus a human judgment record |
| T804 | NOT_PASSED | Asset provenance and device acceptance have not passed | Device plus a human acceptance decision | Recorded device-acceptance results plus a provenance check |
| T806 | BLOCKED | P2 polish is allowed only after P0/P1 device acceptance (T804) | P0/P1 device acceptance lands first, then artist adds P2 | P0/P1 device-acceptance evidence before any P2 polish |
| T901 | NOT_PASSED | Deterministic replay has not passed across the supported device matrix; the harness is not evidence | The supported device matrix | Linked device replay results across the matrix (B-002) |
| T902 | NOT_PASSED | Functional, visual, arena, animation, accessibility, and edge-case gates have not passed; `GateRegistry` maps gates to evidence but the evidence is not linked | Human plus device, per gate | Linked evidence for each acceptance gate (A–G) |
| T903 | NOT_RUN | The onboarding comprehension playtest is not run | Named participants plus a designer who records comprehension | A recorded playtest with a comprehension outcome |
| T904 | NOT_RUN | The voluntary-replay playtest with at least five external participants is not run | At least five named external participants | A recorded playtest from at least five external participants |
| T905 | NOT_RUN | Three consecutive physical-device complete runs on the performance floor (iPhone 12) are not run | iPhone 12 device | Three recorded consecutive complete runs on the performance floor |
| T906 | STANDING_GATE | Severity-one and -two defects are not fixed; the defect list must be found through device / playtest evidence first | Developer fixes; evidence discovers the defects | A defect registry with no open severity-one or -two defects |
| T907 | NOT_RECORDED | Release-candidate evidence is not recorded; `ReleaseEvidenceStore` is a harness, not evidence | The release owner records the evidence | A recorded release-candidate evidence bundle |
| T908 | NOT_DECIDED | The expansion-gate decision is a human judgment, gated on D-020, D-021, and Gates A–G | The owner specialist (Danny) decides | A recorded expansion-gate decision referencing D-020/D-021 and the gate evidence |

## Traceability rule

Every runtime pull request MUST cite task IDs and affected requirement or gate IDs. A task closes only when its verification evidence is linked.
