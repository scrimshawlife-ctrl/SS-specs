# Implementation Tasks

Status: READY_FOR_REVIEW  
Feature: SS-001

Tasks are ordered. Runtime implementation belongs in the future runtime repository.

## Phase 0 — Specification and repository boundary

- [x] T000 Record iPhone-only, iOS 18, landscape, touch, and device-matrix decisions.
- [x] T001 Record 60 Hz simulation and physical-device frame-time thresholds.
- [x] T002 Reserve `scrimshawlife-ctrl/SS` as the future runtime repository identity.
- [x] T003 Define visual, animation, arena, production, and accessibility baselines.
- [ ] T004 Resolve the immutable legacy head and create annotated tag `legacy-multicity-2026-08-23`.
- [ ] T005 Complete cross-artifact consistency and specification-quality review.
- [ ] T006 Create the runtime repository and link its first commit to the accepted specification SHA.
- [ ] T007 Establish ruleset, level, replay-schema, asset-schema, arena-schema, and save-schema version policies.

## Phase 1 — Legacy admission

- [ ] T100 Inventory exact source paths for LC-001 through LC-010.
- [ ] T101 Recover tests and dependency boundaries for deterministic kernel candidates.
- [ ] T102 Classify campaign, procedural district, challenge, and non-SF content as excluded.
- [ ] T103 Classify SF assets individually with provenance and runtime relevance.
- [ ] T104 Record ADMIT, ADAPT, REWRITE, or REJECT for every candidate.
- [ ] T105 Stop legacy migration when any copied source lacks an approved record.

## Phase 2 — Deterministic kernel

- [ ] T200 Implement fixed-step SimulationClock.
- [ ] T201 Implement seeded random generator with golden sequence tests.
- [ ] T202 Define stable entity IDs and ordered iteration rules.
- [ ] T203 Define normalized tick-indexed player commands.
- [ ] T204 Implement replay envelope loading and incompatibility errors.
- [ ] T205 Implement final state digest and first golden replay fixture.
- [ ] T206 Verify restart restores the initial authoritative state.

## Phase 3 — Grayscale arena blockout

- [ ] T300 Define arena, zone, collision, Camera, navigation, and spawn schemas.
- [ ] T301 Build the 36 × 24-cell baseline arena with seven canonical zones.
- [ ] T302 Validate reachability, minimum widths, viewport margins, and Spawn Alley protection.
- [ ] T303 Implement collision, Camera, spawn, safe-area, and density debug overlays.
- [ ] T304 Build SE-class and standard-iPhone HUD blockouts for both handedness modes.
- [ ] T305 Run first-run and competent-run pacing probes.
- [ ] T306 Freeze the accepted blockout before final environment production.
- [ ] T307 Establish diagonal spine, three-grid collision, wedge parcels, and landmark sightlines.
- [ ] T308 Validate Civic Seam identity without labels or literal map reproduction.

## Phase 4 — Surveillance and combat blockout

- [ ] T400 Implement Camera data, deterministic LOS, and occlusion.
- [ ] T401 Implement Exposure, recovery, thresholds, state cues, and Lockdown latch.
- [ ] T402 Render Camera fields from authoritative data.
- [ ] T403 Implement deterministic target selection, base attack, damage, and death.
- [ ] T404 Implement projectile pooling with complete lifecycle reset.
- [ ] T405 Implement Guard and Interceptor blockouts with distinct silhouettes.
- [ ] T406 Profile peak density on iPhone 12 and decide D-021 ceilings.
- [ ] T407 Validate spawn fairness and visual escape corridors.

## Phase 5 — Visual language and asset pipeline

- [ ] T500 Establish role palette, shape language, contact points, and salience hierarchy.
- [ ] T501 Implement asset manifest and provenance validation.
- [ ] T502 Implement deterministic naming, dimensions, alpha, sRGB, content, duplicate, and atlas checks.
- [ ] T503 Produce Player, Guard, Interceptor, Captain, Camera, objective, and upgrade silhouette sheets.
- [ ] T504 Produce grayscale, color-vision, dense-combat, and reduced-presentation review plates.
- [ ] T505 Establish bounded atlases and preload measurements.
- [ ] T506 Approve the minimum asset inventory before polish assets.
- [ ] T507 Produce the six Civic Seam Camera housing families.
- [ ] T508 Produce architectural module sheets and recombination tests.
- [ ] T509 Produce the original phoenix, repair, human-counter-signal, and broadcast-glyph motif sheets.

## Phase 6 — Animation and VFX

- [ ] T600 Implement clip metadata and authoritative event markers.
- [ ] T601 Produce minimum Player clips.
- [ ] T602 Produce Guard and Interceptor clip families.
- [ ] T603 Produce the finite Captain animation and telegraph vocabulary.
- [ ] T604 Implement bounded procedural VFX and reduced variants.
- [ ] T605 Verify anchors, mirroring, interruption, cancellation, and event alignment.
- [ ] T607 Implement bounded Civic Seam ambient motion with seeded cosmetic scheduling.
- [ ] T606 Measure animation, VFX, draw, and transient-node budgets on iPhone 12.

## Phase 7 — Upgrades, Captain, and Extraction

- [ ] T700 Implement protected upgrade selection.
- [ ] T701 Implement Signal Jammer, Ricochet Pulse, and Ghost Step.
- [ ] T702 Implement Captain phases and defeat.
- [ ] T703 Implement Extraction locking, countdown, reset-on-exit, and completion.
- [ ] T704 Implement terminal precedence and immutable result records.
- [ ] T705 Add complete-run golden vectors for every upgrade.
- [ ] T706 Verify every upgrade completes the level without exploits.

## Phase 8 — Final San Francisco production

- [ ] T800 Produce approved Civic Seam P0 modular environment families.
- [ ] T801 Integrate only runtime-reachable SS-001 assets.
- [ ] T802 Perform Civic Seam P1 identity pass without weakening affordances.
- [ ] T806 Add P2 polish only after P0/P1 device acceptance.
- [ ] T807 Verify no prohibited landmark, seal, logo, copied artwork, or geographically incoherent shorthand ships.
- [ ] T803 Complete audio, haptic, HUD, and objective presentation.
- [ ] T804 Pass asset provenance and device acceptance.
- [ ] T805 Remove unreachable, duplicate, source, and non-SF assets from the bundle.

## Phase 9 — Acceptance

- [ ] T900 Instrument frame time, memory, thermal state, entities, particles, Exposure, damage, and outcomes.
- [ ] T901 Pass deterministic replays across the supported matrix.
- [ ] T902 Pass functional, visual, arena, animation, accessibility, and edge-case gates.
- [ ] T903 Run onboarding comprehension playtests.
- [ ] T904 Run voluntary-replay playtests with at least five external participants.
- [ ] T905 Run three consecutive physical-device complete runs on the performance floor.
- [ ] T906 Fix all severity-one and severity-two defects.
- [ ] T907 Record release-candidate evidence.
- [ ] T908 Decide whether the expansion gate passes.

## Traceability rule

Every runtime pull request MUST cite task IDs and affected requirement or gate IDs. A task closes only when its verification evidence is linked.
