# Technical Plan: San Francisco Vertical Slice

Status: BASELINE  
Depends on: `spec.md`, constitution 1.0.0

## 1. Platform baseline

```yaml
platform: iPhone
orientation: landscape-left-and-right
minimum_os: iOS 18.0
language: Swift 6
renderer: SpriteKit
application_shell: SwiftUI
simulation_step: 60Hz
presentation_target: 60fps
networking: none
accounts: none
persistence: settings-and-local-run-receipts
```

The runtime repository will be `scrimshawlife-ctrl/SS` after the specifications pass their completeness review.

## 2. Runtime boundary

SpriteKit owns presentation, input sampling, audio, and animation. A platform-independent deterministic simulation module owns authoritative gameplay. SwiftUI owns application lifecycle, menus, settings, protected overlays, and accessible non-gameplay controls.

## 3. Module model

| Module | Responsibility | Prohibited ownership |
|---|---|---|
| SimulationClock | Fixed-step tick progression | Wall-clock gameplay authority |
| WorldState | Canonical entities and run state | Render nodes |
| InputBuffer | Ordered normalized commands | Device-specific event objects |
| MovementSystem | Movement and collision resolution | Animation decisions |
| DetectionSystem | LOS, Camera contacts, Exposure, Detection State | Cone rendering |
| CombatSystem | Target selection, attacks, damage, death | Particle effects |
| EnemySystem | Spawn eligibility and enemy behavior decisions | Scene graph queries |
| ExposureDirector | Escalation schedule and Lockdown latch | Audio cues |
| ObjectiveSystem | Captain and Extraction prerequisites | UI navigation |
| ResultBuilder | Immutable run result | Persistence policy |
| ArenaLoader | Validated arena data | Sprite bounds as collision |
| VisualCatalog | Asset IDs, atlases, clips, provenance receipts | Gameplay rules |
| AnimationProjector | Authoritative event-to-clip projection | Rule mutation |
| Renderer | Projection of authoritative state | Rule mutation |

## 4. Determinism

- Use a fixed 60 Hz simulation step.
- Use an injected seeded random generator.
- Do not iterate unordered collections when order affects results.
- Give every authoritative entity a stable identifier.
- Define tie-breakers for targeting, spawning, collision, damage, and simultaneous terminal events.
- Quantize or otherwise control floating-point behavior where cross-device equivalence requires it.
- Record normalized input commands by tick.
- Compute a final authoritative state digest for test comparison.
- Keep camera, animation, VFX, audio, haptics, and display refresh outside gameplay authority.

Replay envelope:

```text
rulesetVersion
levelVersion
seed
inputSchemaVersion
ordered { tick, command }[]
```

A replay with an unknown version MUST be rejected with a typed incompatibility result.

## 5. Simulation state

Minimum authoritative state:

- tick and run phase;
- Player position, velocity intent, health, cooldowns, and upgrade;
- entity registry with stable IDs;
- Camera definitions and active status;
- current Exposure and Detection State;
- Lockdown latch;
- Captain state;
- Extraction lock and countdown;
- seeded generator state;
- terminal result, if any.

## 6. Versioned data contracts

Versioned data defines:

- Arena geometry, zones, navigation, and spawn regions
- Camera transforms, fields of view, range, and occlusion masks
- Exposure thresholds, rates, grace periods, and recovery
- Enemy attributes and escalation eligibility
- Weapon and upgrade parameters
- Captain phases, telegraphs, and attack vocabulary
- Extraction duration
- Visual asset records, atlases, anchors, and provenance
- Animation clips and authoritative event markers
- Performance budgets

Data loading MUST validate invariants and fail before starting a run when configuration is invalid.

## 7. Visual and arena contracts

The following artifacts are normative:

- `visual-assets.md`: art direction, inventory, palette roles, VFX, HUD, atlases, and validation
- `animation.md`: state machines, clip metadata, telegraphs, event alignment, and reduced motion
- `arena.md`: 36 × 24-cell baseline arena, seven zones, pacing, navigation, surveillance, and spawn fairness
- `camera-destruction.md`: per-run fixed Camera behavior, Integrity, targeting, optional Network Blackout, Tamper Exposure, tick order, presentation, receipts, and golden vectors
- `camera-placement.md`: seeded authored-socket selection, zone quotas, fairness invariants, RNG isolation, schema, receipts, and golden vectors
- `encounter-objectives.md`: canonical mob, elite/sub-boss, boss, and Extraction objective graph
- `visual-production.md`: blockout-first workflow, provenance, intake, review plates, and budgets

Final art begins only after grayscale blockout, collision truth, Camera truth, and dense-frame readability pass.

## 8. Test strategy

### Unit and contract tests

- Seeded generator sequences
- Fixed-step advancement
- Collision, reachability, and occlusion
- Exposure accumulation, recovery, thresholds, and latch
- Target and spawn tie-breaking
- Damage and terminal precedence
- Projectile lifecycle reset
- Extraction reset rule
- Arena-schema invariants
- Asset manifest, atlas, frame, anchor, and provenance invariants
- Camera Integrity, target priority, simultaneous-hit, Tamper, dormant-state, restart, and Ricochet vectors
- Animation event-marker alignment

### Golden vectors

Commit canonical fixtures containing Replay Identity, ordered inputs, expected result, expected critical events, and final state digest. Golden changes require an explained ruleset or level-version change.

### Integration

- Complete successful run
- Player death in each encounter phase
- Restart from every phase
- Suspend/resume
- All upgrade paths
- Captain defeat and Extraction
- Invalid replay version
- Small-screen and both handedness layouts
- Reduced Motion and Differentiate Without Color

### Presentation contract

Automated or recorded checks compare:

- visible Camera regions with authoritative geometry;
- telegraphs with authoritative affected areas and commit ticks;
- sprite contact points with authoritative transforms;
- HUD and objective cues with state events;
- reduced presentation with mechanical equivalence.

## 9. Performance

Measure on physical iPhone 12 during three consecutive complete runs.

| Metric | Threshold |
|---|---:|
| Frame-time p50 | ≤ 16.67 ms |
| Frame-time p95 | ≤ 16.67 ms |
| Frame-time p99 | ≤ 25 ms |
| Worst gameplay frame | ≤ 50 ms |
| Sustained presentation | no sustained interval below 55 fps |
| Memory warnings | 0 |
| Serious/critical thermal state | 0 |
| Unbounded entity or transient growth | 0 |

Application/loading transitions are reported separately. Profiled blockout evidence sets exact entity, projectile, particle, atlas-memory, and resident-memory ceilings in D-021.

Textures used together are grouped into bounded atlases and preloaded before their encounter. Offscreen cosmetic animation may reduce frequency. Particle and transient-node counts remain bounded.

## 10. Device matrix

Physical acceptance classes:

1. iPhone SE, 3rd generation — small-screen layout
2. iPhone 12 — performance floor
3. current standard iPhone — primary acceptance
4. current iPhone Pro — high-refresh behavior

Equivalent devices require a recorded equivalence rationale. Routine CI uses SE-class and current-standard simulators. Physical devices remain mandatory for performance, thermal, audio, haptics, and touch acceptance.

## 11. Legacy migration procedure

1. Resolve and tag the exact legacy `main` head as `legacy-multicity-2026-08-23`.
2. Stop active legacy development.
3. Inventory each bounded candidate.
4. Identify dependencies and global state.
5. Write or recover behavioral tests.
6. Decide ADMIT, ADAPT, REWRITE, or REJECT.
7. Port only the smallest admitted responsibility.
8. Verify against the new contract.
9. Archive the legacy repository only after every candidate has a disposition.

Recommended migration order: seeded randomness, simulation clock, movement/collision, Camera LOS, projectile pooling, combat, accessibility/settings shell, audio infrastructure, approved SF assets. Campaign authority, other cities, procedural districts, challenges, and generalized city profiles are excluded.

## 12. Delivery slices

1. Specification closure and legacy freeze
2. Deterministic kernel and replay harness
3. Grayscale movement/arena blockout
4. Camera and Exposure blockout
5. Combat and density blockout
6. Visual language and minimum animation set
7. Enemy escalation
8. Upgrades
9. Captain encounter
10. Extraction and results
11. Final SF art, audio, and polish
12. Performance, accessibility, playtest, and release evidence

Each slice remains executable and testable.
