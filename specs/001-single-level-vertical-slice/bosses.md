# Elite and Boss Contract

Status: CANONICAL  
Contract version: `bosses-001`

## Improper Search Daemon

The elite activates in Z-05 after M-C cleanup.

| Property | Value |
|---|---:|
| HP | 300 |
| Radius | 26 |
| Base speed | 108 units/second |
| Contact damage | 14 DPS |
| Spawn delay after M-C | 90 ticks |

State sequence repeats until defeated:

1. `PURSUIT` for 120 ticks.
2. `QUERY_TELEGRAPH` for 45 ticks: display three 56-unit circles at Player position and ±96 units perpendicular to facing.
3. `QUERY_RESOLVE`: each circle still containing the Player deals 14 damage; circles do not overlap.
4. `REDACTION_DASH_TELEGRAPH` for 36 ticks: show one 72-unit-wide lane to the sampled Player position.
5. `REDACTION_DASH` for 30 ticks at 288 units/second; normal solid collision; contact remains active.
6. `RECOVER` stationary for 60 ticks.

The Daemon has no invulnerability, summons, random attack choice, Camera control, or Exposure effect. At zero HP, emit `EliteDefeated(improperSearchDaemon,tick)` once and open the route to Z-06 after 60 ticks.

## Algorithmic Moderate

The single boss activates when the living Player enters Z-06 after the elite is defeated.

| Property | Value |
|---|---:|
| HP | 800 |
| Radius | 30 |
| Base speed | 120 units/second |
| Base contact damage | 16 DPS |
| Initial attack delay | 90 ticks |
| Phase transition recovery | 45 ticks, movement only; not damage-immune |

### Canonical policy phases

Health bands use HP after the tick's ordered damage batch:

| Phase | HP after batch | Observation | Speed | Contact | Orbit |
|---|---:|---:|---:|---:|---:|
| Public Safety | 600–800 | 105/100 | 100/100 | 100/100 | 0/100 |
| Civil Liberties | 400–599 | 108/100 | 90/100 | 104/100 | 72/100 |
| Temporary Safeguard | 200–399 | 112/100 | 118/100 | 110/100 | 18/100 |
| Independent Review | 1–199 | 116/100 | 104/100 | 116/100 | −55/100 |

These ratios adapt verified legacy San Francisco policy values. A damage batch may cross multiple thresholds, but only the final resulting phase is entered and one transition event is emitted. Phase cannot move backward.

Orbit modifies normalized pursuit by adding the perpendicular direction × orbit ratio before normalization. Even entity parity chooses the initial perpendicular orientation; negative ratio reverses it.

### Attack vocabulary

The boss has exactly four attacks.

#### Safety Rationale

- Telegraph: 45 ticks, 70-degree cone, range 260.
- Lock cone heading on the final telegraph tick.
- Resolve: 18 damage once inside cone with solid-geometry occlusion.
- Cooldown contribution: 90 ticks.

#### Narrow Tailoring

- Telegraph: 30 ticks.
- Fire three projectiles at sampled Player heading −12°, 0°, +12°.
- Projectile: speed 420, radius 7, lifetime 72 ticks, 9 damage.
- Solids consume projectiles.
- Cooldown contribution: 75 ticks.

#### Temporary Order

- Telegraph: 48 ticks at one authored Captain Camera emitter.
- Activate its fixed field for 180 ticks.
- The Captain Camera is not a standard Camera, cannot be targeted or destroyed, and does not count toward Network Blackout.
- While Player is in its unobstructed field, apply an Observation pulse of base +10 Exposure every 30 ticks, multiplied by the current phase Observation ratio and then upgrade modifiers; round half away from zero.
- Only one Temporary Order field may be active.
- Cooldown contribution: 120 ticks.

#### Independent Review

- Telegraph: 60 ticks with six radial lanes.
- Resolve six projectiles at equal 60-degree spacing, speed 360, radius 7, lifetime 90 ticks, 8 damage.
- A deterministic safe gap is created by omitting the lane nearest the current vector from boss to Player; therefore five projectiles spawn.
- Exact angular ties omit the lower numbered lane.
- Cooldown contribution: 105 ticks.

### Phase schedules

Each phase begins its sequence at index 0. After an attack resolves, wait its cooldown contribution, then advance cyclically.

| Phase | Sequence |
|---|---|
| Public Safety | Safety Rationale → Narrow Tailoring |
| Civil Liberties | Narrow Tailoring → Safety Rationale → Temporary Order |
| Temporary Safeguard | Temporary Order → Narrow Tailoring → Safety Rationale |
| Independent Review | Independent Review → Narrow Tailoring → Temporary Order |

Phase transition cancels an unresolved telegraph and hostile projectiles owned by the prior attack, retires the active Captain Camera field, enters 45 ticks of transition recovery, and begins the new sequence. It does not clear standard enemies, standard Camera state, Exposure, mines, or Player projectiles.

## Defeat and Extraction

Boss defeat retires all boss projectiles and Captain Camera fields immediately. It emits `BossDefeated(algorithmicModerate,tick)` once. Extraction arms only under `encounter-objectives.md`. Player death on the same tick remains terminal failure even if boss HP reaches zero.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| BO-001 | Daemon uninterrupted cycle | exact 120/45/instant/36/30/60 timing |
| BO-002 | boss HP 800/600/599/400/399/200/199/1 | phases match table |
| BO-003 | one batch 610→390 | one transition to Temporary Safeguard |
| BO-004 | phase transition during telegraph | prior attack canceled; 45-tick recovery |
| BO-005 | Temporary Order pulse in Public Safety | +11 Exposure before upgrade |
| BO-006 | same pulse with Signal Jammer | +8 after 25% reduction |
| BO-007 | Independent Review lane tie | lower numbered lane omitted |
| BO-008 | boss defeat with active field/projectiles | all retire immediately |
| BO-009 | boss and Player die same tick | terminal failure; boss death recorded |
| BO-010 | zero Cameras destroyed | boss remains defeatable and Extraction can arm |
