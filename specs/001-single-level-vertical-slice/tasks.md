# Implementation Tasks

Status: READY_FOR_REVIEW  
Feature: SS-001

Tasks are ordered. Runtime implementation belongs in the future runtime repository.

## Phase 0 — Decisions and repository boundary

- [ ] T000 Record target Apple platforms, minimum OS, device matrix, orientation, and input methods.
- [ ] T001 Record frame-rate and frame-time acceptance thresholds.
- [ ] T002 Create the runtime repository and link it to this specification commit.
- [ ] T003 Establish ruleset, level, replay-schema, and save-schema version policies.
- [ ] T004 Identify the immutable legacy repository revision used for migration analysis.

## Phase 1 — Deterministic kernel

- [ ] T010 Implement fixed-step SimulationClock.
- [ ] T011 Implement seeded random generator with golden sequence tests.
- [ ] T012 Define stable entity IDs and ordered iteration rules.
- [ ] T013 Define normalized tick-indexed player commands.
- [ ] T014 Implement replay envelope loading and incompatibility errors.
- [ ] T015 Implement final state digest and first golden replay fixture.
- [ ] T016 Verify restart restores the initial authoritative state.

## Phase 2 — Movement sandbox

- [ ] T020 Implement authoritative movement and collision.
- [ ] T021 Define level geometry validation.
- [ ] T022 Build Spawn Alley teaching layout.
- [ ] T023 Project authoritative transforms into SpriteKit.
- [ ] T024 Add movement, collision, boundary, restart, and suspend/resume tests.

## Phase 3 — Surveillance sandbox

- [ ] T030 Define Camera data contract.
- [ ] T031 Implement deterministic line-of-sight and occlusion.
- [ ] T032 Implement Exposure accumulation, grace, recovery, and thresholds.
- [ ] T033 Implement Detection State transitions and Lockdown latch.
- [ ] T034 Render Camera regions from the same definitions used by detection.
- [ ] T035 Implement state cues and accessibility-safe alternatives.
- [ ] T036 Add single-camera, multi-camera, occlusion, boundary, and transition vectors.

## Phase 4 — Combat sandbox

- [ ] T040 Implement deterministic target selection and tie-breakers.
- [ ] T041 Implement base automatic attack.
- [ ] T042 Implement damage, death, and terminal-event precedence.
- [ ] T043 Implement safe projectile pooling with full lifecycle reset.
- [ ] T044 Add visible damage attribution.
- [ ] T045 Add combat and pooling stress tests.

## Phase 5 — Escalation and enemies

- [ ] T050 Implement Guard behavior.
- [ ] T051 Implement Interceptor behavior.
- [ ] T052 Implement validated spawn regions and protected Spawn Alley.
- [ ] T053 Implement ExposureDirector escalation schedule.
- [ ] T054 Assemble Camera Corridor, Civic Plaza, and Pressure Route.
- [ ] T055 Test spawn validity, escalation eligibility, and bounded entity counts.

## Phase 6 — Upgrades

- [ ] T060 Implement protected upgrade selection.
- [ ] T061 Implement Signal Jammer.
- [ ] T062 Implement Ricochet Pulse.
- [ ] T063 Implement Ghost Step.
- [ ] T064 Add quantitative and visual tests that each upgrade changes play.
- [ ] T065 Verify every upgrade can complete the level.

## Phase 7 — Captain and Extraction

- [ ] T070 Implement finite, readable Captain attack vocabulary.
- [ ] T071 Implement Captain phase rules and defeat event.
- [ ] T072 Lock Extraction until Captain defeat.
- [ ] T073 Implement visible extraction countdown with reset-on-exit.
- [ ] T074 Implement terminal precedence and single-completion guarantee.
- [ ] T075 Build immutable result record and result screen.
- [ ] T076 Add complete-run golden vectors for all upgrades.

## Phase 8 — Validation and polish

- [ ] T080 Instrument frame time, entity counts, spawns, Exposure, damage, and outcomes.
- [ ] T081 Pass the deterministic replay suite on the target device matrix.
- [ ] T082 Pass functional and edge-case acceptance criteria.
- [ ] T083 Run onboarding comprehension playtests.
- [ ] T084 Run voluntary-replay playtests with at least five external participants.
- [ ] T085 Fix all severity-one and severity-two defects.
- [ ] T086 Record acceptance evidence in the release candidate.
- [ ] T087 Decide whether the expansion gate passes.

## Traceability rule

Every runtime pull request MUST cite task IDs and affected requirement IDs. A task may close only when its verification evidence is linked.
