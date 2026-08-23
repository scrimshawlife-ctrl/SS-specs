# Technical Plan: San Francisco Vertical Slice

Status: PROPOSED  
Depends on: `spec.md`, constitution 1.0.0

## 1. Runtime boundary

The runtime SHOULD use Swift and SpriteKit unless an explicit architecture decision replaces the existing platform direction. SpriteKit owns presentation, input sampling, audio, and animation. A platform-independent deterministic simulation module owns authoritative gameplay.

## 2. Module model

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
| Renderer | Projection of authoritative state | Rule mutation |

## 3. Determinism

- Use a fixed simulation step.
- Use an injected seeded random generator.
- Do not iterate unordered collections when order affects results.
- Give every authoritative entity a stable identifier.
- Define tie-breakers for targeting, spawning, collision, damage, and simultaneous terminal events.
- Quantize or otherwise control floating-point behavior where cross-device equivalence requires it.
- Record normalized input commands by tick.
- Compute a final authoritative state digest for test comparison.

Replay envelope:

```text
rulesetVersion
levelVersion
seed
inputSchemaVersion
ordered { tick, command }[]
```

A replay with an unknown version MUST be rejected with a typed incompatibility result.

## 4. Simulation state

Minimum authoritative state:

- tick
- run phase
- player position, velocity intent, health, cooldowns, upgrade
- entity registry with stable IDs
- Camera definitions and active status
- current Exposure and Detection State
- Lockdown latch
- Captain state
- Extraction lock and countdown
- seeded generator state
- terminal result, if any

## 5. Data contracts

Versioned data SHOULD define:

- Level geometry and spawn regions
- Camera transforms, fields of view, range, and occlusion masks
- Exposure thresholds, rates, grace periods, and recovery
- Enemy attributes and escalation eligibility
- Weapon and upgrade parameters
- Captain phases and attack vocabulary
- Extraction duration
- Performance budgets

Data loading MUST validate invariants and fail before starting a run when configuration is invalid.

## 6. Test strategy

### Unit

- Seeded generator sequences
- Fixed-step advancement
- Collision and occlusion
- Exposure accumulation, recovery, thresholds, and latch
- Target tie-breaking
- Damage and terminal precedence
- Projectile lifecycle reset
- Extraction reset rule

### Golden vectors

Commit canonical fixtures containing Replay Identity, ordered inputs, expected result, expected critical events, and final state digest. Golden changes require an explained ruleset or level-version change.

### Integration

- Complete successful run
- Player death in each encounter phase
- Restart from every phase
- Suspend/resume
- Upgrade paths
- Captain defeat and extraction
- Invalid replay version

### Presentation contract

Automated or recorded checks MUST compare visible Camera regions with authoritative geometry and confirm that player-facing state cues follow the authoritative event stream.

## 7. Performance

The runtime plan MUST declare target devices before implementation acceptance. Initial budgets:

- Stable target frame rate under worst supported encounter
- No unbounded entity growth
- Bounded projectile and enemy pools
- No authoritative allocations inside hot loops where avoidable
- Frame-time and entity-count instrumentation available in development builds

Exact device and frame-time thresholds remain an owner decision and block final performance acceptance, not specification work.

## 8. Legacy migration procedure

For each candidate:

1. Inventory source path and behavior.
2. Identify dependencies and global state.
3. Write or recover behavioral tests.
4. Evaluate deterministic fitness.
5. Decide ADMIT, ADAPT, REWRITE, or REJECT.
6. Port only the smallest admitted responsibility.
7. Verify against the new contract without referencing legacy success as acceptance.

Recommended order: seeded randomness, simulation clock, movement/collision, Camera LOS, projectile pooling, combat, enemies, extraction, approved assets.

## 9. Delivery slices

1. Deterministic kernel and replay harness
2. Movement sandbox
3. Camera and Exposure sandbox
4. Combat sandbox
5. Enemy escalation
6. Upgrades
7. Captain encounter
8. Extraction and results
9. Level assembly
10. Performance, accessibility, playtest, and polish

Each slice must remain executable and testable.
