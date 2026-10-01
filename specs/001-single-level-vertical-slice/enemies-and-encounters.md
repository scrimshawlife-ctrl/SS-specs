# Enemies and Mob Encounters

Status: CANONICAL  
Contract version: `enemies-encounters-001`

## Combat vocabulary

Level 1 uses exactly five standard enemy archetypes. Statistics are authoritative integers except per-second rates, which accumulate in fixed-point and apply whole Integrity points when the accumulator crosses an integer.

| ID | Role | HP | Radius | Speed | Contact DPS |
|---|---|---:|---:|---:|---:|
| `fogAnalyticsCloud` | observation support | 30 | 18 | 84 | 4 |
| `cableCarCorrelator` | telegraphed charger | 60 | 20 | 108 | 12 |
| `sutroSignalWitch` | ranged pressure | 45 | 18 | 72 | 6 |
| `autonomousInformant` | fast pursuer | 30 | 16 | 144 | 8 |
| `victorianVendor` | slow area denial | 90 | 22 | 60 | 10 |

All target the Player, use circle collision, obey stable-ID ties, and stop acting immediately at zero HP. They never damage Cameras or one another.

## Archetype state machines

### Fog Analytics Cloud

`APPROACH → ORBIT → TELEGRAPH → PULSE → COOLDOWN`

- Approach until 210 units from Player.
- Orbit band: 170–230 units, clockwise for even entity ID and counterclockwise for odd.
- Pulse cooldown: 180 ticks, first eligible 120 ticks after spawn.
- Telegraph: 45 ticks with a visible 220-unit ring.
- Pulse: if Player is within 220 units and unobstructed, add +20 Exposure; otherwise miss.
- Signal Jammer modifies this pulse under its contract.
- Cooldown starts on pulse resolution.

### Cable-Car Correlator

`PURSUE → CHARGE_TELEGRAPH → CHARGE → RECOVER`

- Pursue until within 240 units.
- Cooldown: 180 ticks; first eligible 90 ticks after spawn.
- Telegraph: 30 ticks; lock the Player position on the final telegraph tick.
- Charge: 24 ticks at 300 units/second along the locked direction.
- Charge uses normal solid collision and ends on first solid impact.
- Recover stationary for 45 ticks, then pursue.
- Contact damage applies normally during charge.

### Sutro Signal Witch

`KEEP_RANGE → CAST_TELEGRAPH → FIRE → COOLDOWN`

- Maintain 220–300 units: approach outside 300, retreat inside 220, otherwise orbit.
- Fire cooldown: 120 ticks; first eligible 60 ticks after spawn.
- Telegraph: 30 ticks.
- Fire one `sutroBolt`: speed 360 units/second, radius 6, lifetime 90 ticks, 10 damage.
- Aim directly at the sampled Player position; no predictive lead.
- Solids consume the bolt. The bolt retires on Player hit.

### Autonomous Informant

`PURSUE`

- Always takes the shortest direct steering vector toward the Player.
- No special attack, leap, split, death spawn, or Exposure effect.
- Its purpose is to force movement while other roles telegraph.

### Victorian Vendor

`KEEP_RANGE → THROW_TELEGRAPH → THROW → COOLDOWN`

- Maintain 160–220 units.
- Throw cooldown: 180 ticks; first eligible 90 ticks after spawn.
- Telegraph: 36 ticks and mark the sampled Player position.
- Place one `receiptMine` at that position, clamped to the nearest valid point within 48 units.
- Mine arms after 30 ticks, persists 240 ticks, radius 42, and deals 12 damage once on Player entry.
- Maximum two live mines per Vendor; creating a third retires its oldest.
- Mines are hazards, not targetable entities, and never affect Cameras or enemies.

## Awareness (D-089)

Standard enemies can be **unaware**. Being hidden earns the first strike. The
elite and the boss are always aware.

**Spawning.** A standard enemy spawns **aware** when any of these holds;
otherwise it spawns unaware:
- the Detection State, resolved after the previous tick, is `tracked`,
  `hunted`, or `lockdown` (`awareness.surveillanceAlertState` or above);
- its encounter is listed in `awareness.awareEncounters` (M-C, the forced
  Lockdown set piece);
- it is a heat reinforcement (D-083), since it was sent because the Player was
  seen.

**Unaware behaviour.** No telegraph, attack, pulse, charge, throw, or mine; no
contact damage. It **drifts** toward its encounter's trigger centre at
`awareness.unawareDriftPercent` (25%) of its archetype speed, with normal
steering and solid collision, and stops within `awareness.unawareDriftStopUnits`
(48) of it (D-090). Patrol members patrol instead (§ Transit Patrol). It and presents its
idle clip with an unaware marker (animation.md § 8a).

**Becoming alerted.** Evaluated once per tick, at the start of the enemy phase
(simulation-order.md), in ascending entity ID, with each cause taking precedence
over the ones below it:
1. **surveillance**: the Detection State is `tracked` or above, which alerts
   every unaware standard enemy;
2. **damage**: the enemy took damage since its last enemy phase;
3. **sight**: the Player is within `awareness.sightRangeUnits` (320, D-090) with a
   clear line (the weapon line-of-fire rule against static solids);
4. **ally**: an unaware enemy within `awareness.allyAlertRadiusUnits` (128) of an
   enemy alerted this tick by damage or sight. This is one hop: an ally alert
   never propagates further.

An alerted enemy never returns to unaware. Each alert publishes
`enemyAlerted(entityId, cause)` once. An enemy alerted this tick begins its
normal state machine on the next tick.

**Ambush.** The first damage an unaware enemy takes is multiplied by
`awareness.ambushDamageMultiplier` (3, D-090) (combat.md). The enemy is aware
afterwards, so later hits in the same tick are normal.

## Transit Patrol (P-02, D-091)

The Camera Corridor holds a patrol: the Player's first stealth problem, and one
that moves. It is not an encounter. It has no trigger, no gate, no waves, no
upgrade, and no completion, and it never blocks the route. It is optional: sneak
past, ambush it, or be seen and fight.

**Members and routes.** `civic-seam-arena-004` `patrols` lists each member's
archetype and a closed loop of waypoints. Each member spawns **unaware** at its
first waypoint during the first tick's spawn phase, and follows its loop in
order, wrapping from last to first.

**Patrolling.** While unaware, a patrol member moves toward its next waypoint
at `patrol.speedPercent` (40%) of its archetype speed, with the same steering and
solid collision as any enemy. Within `patrol.arrivalUnits` it has arrived: it
holds for `patrol.dwellTicks` (30), then targets the next waypoint. Its
**facing** is its last non-zero travel direction, initially the direction from
the first waypoint to the second. It never attacks and deals no contact damage
while unaware (D-089).

**Vision cone.** An unaware patrol member does not use D-089 all-round sight.
It sees in a cone: range `patrol.sightUnits` (240), half-angle
`patrol.sightHalfAngleMilliDegrees` (45°) about its facing, with a clear line
under the weapon line-of-fire rule. The angle test is the integer test of the
D-082 chosen Camera, at this half-angle. The cone is shown on screen
(animation.md), because a threat the Player cannot read is not stealth
(constitution Article IV).

**Alerting.** D-089's causes apply, with the cone in place of sight:
surveillance, damage, cone sight, and one-hop ally. Once alerted, a member runs
its archetype's normal state machine and pursues the Player anywhere. It never
resumes patrol.

**Scope.**
- Patrol members are excluded from encounter totals, completion, heat, and the
  M-A–M-C graph.
- Their deaths count in the receipt like any standard enemy.
- The ambush multiplier applies to them, but a patrol member spawns with
  `patrol.integrityPercent` (200%, D-093) of its archetype Integrity: 60 for a
  Fog Analytics Cloud or an Autonomous Informant. One ambush (30) wounds it
  but does not kill it, and the hit alerts it (damage) and its neighbours
  within 128 units (ally). Picking a patrol off is a fight you start; slipping
  past is the quiet option.
- While unaware, a patrol member is an automatic target only within
  `patrol.sightUnits` (240) of the Player (D-092), and only while the Player
  moves toward it, by the chosen-Camera 30° test (D-093). Walking past holds
  fire, so slipping by is possible in a 512-unit corridor. The weapon's 512-unit reach
  would otherwise clear the patrol from outside every cone, and it would never
  be read or timed.

**Fairness.** Checked against the arena data by runtime tests (the spec validator does not model patrols):
- no waypoint lies inside a solid, outside its zone, or inside an encounter
  trigger;
- no cone ever reaches the Player spawn or zone Z-01;
- a walkable route from Z-01 into the M-A trigger that no cone covers exists
  at every tick of joint patrol simulation for at least the first hour
  (216,000 ticks), across every Camera subset a legal placement can produce.
  Members interact through separation, so the joint state has no short cycle,
  and a bounded horizon is the proof. The debug test covers the first 3,600
  ticks; an opt-in release test covers the hour.

The cone half-angle must be one with an exact integer cone test (30°, 45°, 60°).

## Shared steering and separation

Enemies compute desired velocity in ascending entity-ID order. A deterministic separation vector is added for living enemies within combined radii + 8 units, with the lower ID retaining priority. Final speed cannot exceed the archetype maximum. Enemies use the same X-then-Y solid collision order as the Player. Enemies do not block one another or the Player.

## Spawn validation

Every spawn uses an authored encounter socket and must satisfy `arena.md` fairness. Candidate sockets are filtered, then ordered by:

1. greatest squared distance from Player;
2. lowest socket ID.

The first valid socket is used. If none is valid, retry after 30 ticks. A wave cannot complete while it has deferred unspawned members. After 300 deferred ticks, fail the run as invalid content; never spawn unfairly.

## Required encounter table

An encounter activates once when the Player enters its trigger region. Entry closes the forward gate only after all pending entities have valid spawn routes. Backtracking remains possible only through the authored escape aperture.

### M-A — Civic Plaza Audit

Zone Z-03. Purpose: teach target priority and award the upgrade.

| Wave | Composition | Spawn interval | Next-wave delay |
|---:|---|---:|---:|
| A1 | 3 Autonomous Informants, 2 Fog Analytics Clouds | 30 ticks | 60 ticks after clear |
| A2 | 2 Cable-Car Correlators, 2 Autonomous Informants | 30 | 60 |
| A3 | 1 Sutro Signal Witch, 2 Fog Analytics Clouds, 2 Autonomous Informants | 24 | — |

Total: 14 enemies. Completion requires every member dead and no pending spawn. Completion enters protected upgrade selection before the next simulation tick.

### M-B — Service Seam Correlation

Zone Z-04. Purpose: combine ranged, charge, and area denial.

| Wave | Composition | Spawn interval | Next-wave delay |
|---:|---|---:|---:|
| B1 | 2 Correlators, 2 Informants, 1 Signal Witch | 24 | 60 |
| B2 | 2 Victorian Vendors, 2 Fog Clouds, 2 Informants | 24 | 75 |
| B3 | 2 Signal Witches, 2 Correlators, 2 Informants | 20 | — |

Total: 17 enemies.

### M-C — Grid Junction Lockdown

Zone Z-05. Purpose: mastery under full escalation.

On activation, set Exposure to 1000, enter and latch Lockdown if not already latched, then begin C1 after 60 ticks. This is the only encounter-forced Exposure assignment.

| Wave | Composition | Spawn interval | Next-wave delay |
|---:|---|---:|---:|
| C1 | 3 Informants, 2 Correlators | 20 | 45 |
| C2 | 2 Fog Clouds, 2 Signal Witches, 1 Vendor | 20 | 60 |
| C3 | 3 Correlators, 2 Vendors, 2 Informants | 18 | 75 |
| C4 | 2 Fog Clouds, 2 Signal Witches, 2 Vendors, 2 Informants | 18 | — |

Total: 25 enemies.

## Heat reinforcements (D-083)

Being seen raises the pressure. When a wave of **M-A or M-B** starts, read the
Detection State after the previous tick's Exposure resolution and append
Autonomous Informants to that wave's spawn list:

| Detection State | Added Informants |
|---|---:|
| `hidden` | 0 |
| `observed` | 0 |
| `tracked` | 1 |
| `hunted` | 2 |
| `lockdown` | 2 |

The values are data in `combat-content-002` (`heat`). Added members spawn after
the authored members, at the wave's own interval and under the same spawn
validation. The wave completes only when they are dead too. M-C is unaffected: it
is the forced Lockdown set piece and is already at full escalation.

The Player is told. The wave's HUD caption names the count and its cause
(hud-tutorial.md), so the pressure is never invisible (constitution Article IV).

## Completion and cleanup

- Standard enemy deaths never drop loot, health, currency, or upgrades.
- Mines and hostile projectiles owned by an encounter retire 30 ticks after its final enemy dies.
- Camera state and Exposure persist between encounters.
- Mob completion events occur exactly once: `MobEncounterCompleted(id,tick)`.
- The Improper Search Daemon cannot activate before M-A, M-B, and M-C are complete.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| EN-001 | complete all scheduled waves while `hidden` | totals A=14, B=17, C=25 |
| EN-002 | obstruct all spawn sockets | retry every 30 ticks; no unfair spawn |
| EN-003 | equal valid spawn distance | lower socket ID selected |
| EN-004 | Fog pulse loses LOS during telegraph | pulse misses |
| EN-005 | Correlator charge hits wall | charge ends; 45-tick recover |
| EN-006 | third Vendor mine | oldest owned mine retires |
| EN-007 | enter M-C at Exposure 400 | Exposure 1000; one Lockdown entry |
| EN-008 | enter M-C already locked down | no duplicate Lockdown event |
| EN-009 | last enemy dies with pending spawn | encounter not complete |
| EN-010 | standard enemy death | no reward entity/event |
| EN-011 | a wave of M-A starts while `hunted` | 2 Informants appended after the authored members |
| EN-012 | a wave of M-B starts while `tracked` | 1 Informant appended |
| EN-013 | a wave of M-C starts (always `lockdown`) | no Informants appended |
| EN-014 | an appended Informant alive, authored members dead | wave not complete |
| EN-015 | a wave of M-B starts after Lockdown latched early (before M-C) | 2 Informants appended |
| EN-016 | an M-A enemy spawns while `hidden` | unaware; zero velocity at spawn, then drifts (D-090); no attack |
| EN-017 | an M-A enemy spawns while `tracked` | aware |
| EN-018 | any M-C enemy, or a heat reinforcement | aware |
| EN-019 | the Player comes within 320 units with a clear line | `enemyAlerted` cause `sight`; acts next tick |
| EN-020 | the Player is at 150 units behind a solid | stays unaware |
| EN-021 | Exposure crosses into `tracked` | every unaware standard enemy alerted, cause `surveillance` |
| EN-022 | an unaware enemy is hit; another unaware enemy is 100 units away, a third 200 units | the hit one is alerted (`damage`), the second (`ally`), the third stays unaware |
| EN-023 | the elite or the boss | never unaware |
| EN-031 | an unaware M-A enemy 400 units from the trigger centre | drifts toward it at 25% speed; stops within 48 units |
| EN-024 | run start | every `patrols` member spawns unaware at its first waypoint |
| EN-025 | an unaware patrol member reaches a waypoint | holds 30 ticks, then heads for the next, wrapping at the end |
| EN-026 | the Player at 200 units, inside the 45° cone, clear line | alerted, cause `sight` |
| EN-027 | the Player at 200 units, 60° off facing | stays unaware |
| EN-028 | the Player at 300 units inside the cone | stays unaware (beyond 240) |
| EN-029 | a patrol member dies | counted in the receipt; no encounter completes; no heat |
| EN-030 | any tick in the first hour of joint patrol simulation, any legal Camera subset | an uncovered walkable route from Z-01 to the M-A trigger exists |
| EN-032 | an unaware patrol member 300 units away, nothing else in range | not targeted; no projectile |
| EN-033 | the same member at 230 units, Player moving toward it | targeted; the ambush applies |
| EN-035 | the same member at 230 units, Player moving perpendicular to it | not targeted; no projectile |
| EN-034 | an ambush hit on an unaware patrol Fog Cloud (60 Integrity) | 30 damage, survives at 30; alerted (`damage`) next enemy phase; unaware patrol members within 128 alerted (`ally`) |
