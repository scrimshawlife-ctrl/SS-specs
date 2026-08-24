# Enemies and Mob Encounters

Status: CANONICAL  
Contract version: `enemies-encounters-001`

## Combat vocabulary

Level 1 uses exactly five standard enemy archetypes. Statistics are authoritative integers except per-second rates, which accumulate in fixed-point and apply whole Integrity points when the accumulator crosses an integer.

| ID | Role | HP | Radius | Speed | Contact DPS |
|---|---|---:|---:|---:|---:|
| `fogAnalyticsCloud` | observation support | 20 | 18 | 84 | 4 |
| `cableCarCorrelator` | telegraphed charger | 40 | 20 | 108 | 12 |
| `sutroSignalWitch` | ranged pressure | 30 | 18 | 72 | 6 |
| `autonomousInformant` | fast pursuer | 20 | 16 | 144 | 8 |
| `victorianVendor` | slow area denial | 60 | 22 | 60 | 10 |

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

## Completion and cleanup

- Standard enemy deaths never drop loot, health, currency, or upgrades.
- Mines and hostile projectiles owned by an encounter retire 30 ticks after its final enemy dies.
- Camera state and Exposure persist between encounters.
- Mob completion events occur exactly once: `MobEncounterCompleted(id,tick)`.
- The Improper Search Daemon cannot activate before M-A, M-B, and M-C are complete.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| EN-001 | complete all scheduled waves | totals A=14, B=17, C=25 |
| EN-002 | obstruct all spawn sockets | retry every 30 ticks; no unfair spawn |
| EN-003 | equal valid spawn distance | lower socket ID selected |
| EN-004 | Fog pulse loses LOS during telegraph | pulse misses |
| EN-005 | Correlator charge hits wall | charge ends; 45-tick recover |
| EN-006 | third Vendor mine | oldest owned mine retires |
| EN-007 | enter M-C at Exposure 400 | Exposure 1000; one Lockdown entry |
| EN-008 | enter M-C already locked down | no duplicate Lockdown event |
| EN-009 | last enemy dies with pending spawn | encounter not complete |
| EN-010 | standard enemy death | no reward entity/event |
