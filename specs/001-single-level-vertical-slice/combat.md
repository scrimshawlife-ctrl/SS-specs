# Base Combat Contract

Status: CANONICAL  
Contract version: `combat-001`

## Base weapon: Civic Pulse

The Player always starts with one automatic `civicPulse` weapon.

| Property | Value |
|---|---:|
| Damage to enemies | 10 Integrity |
| Camera damage | 1 Camera Integrity per valid impact |
| Cadence | every 30 ticks |
| First opportunity | tick 30 |
| Target range | 512 world units |
| Projectile speed | 720 world units/second (12/tick) |
| Projectile radius | 4 world units |
| Lifetime | 45 ticks |
| Maximum travel | 540 world units |
| Pierce | 0 |
| Critical hits | none |
| Active projectile ceiling | 32 |

An attack opportunity with no valid target produces no projectile and does not shift later cadence. The active-projectile ceiling rejects the shot without replacement or cadence change.

## Automatic targeting

Use the classes in `camera-destruction.md`: enemy within 96 units; detecting Camera; other enemy; other Camera. Within class, sort by squared distance to target anchor, then stable entity ID. Range is inclusive. Static solid geometry blocks line of fire; actors and destroyed Camera housings do not, except permanent mount solids.

Target selection happens at the attack opportunity. If the selected target is invalid before spawn in the same phase, no projectile is created and there is no retarget.

## Aim and spawn

Projectiles spawn at the Player weapon anchor. Aim uses the earliest positive constant-velocity intercept. If no positive intercept exists, aim directly at the target’s sampled position. All calculations use the deterministic numeric layer; final direction is quantized before velocity is stored.

## Projectile lifecycle and collision

- A projectile moves on its spawn tick after creation.
- Collision is swept from previous to new position against compatible circular hit shapes.
- Earliest intersection wins; exact intersection ties use lowest target stable ID.
- Blocking world geometry is tested on the same sweep and wins exact ties over entities.
- On a valid base hit, apply damage once and retire the projectile.
- At age 45 ticks, retire after that tick’s sweep.
- Leaving world bounds retires before any out-of-bounds hit.

Damage is collected then resolved by target stable ID, projectile stable ID. A target reaching zero is dead immediately for later ordered hits and continuation selection. Overkill is allowed in computation but receipt damage counts only Integrity actually removed.

## Entity identifiers

Stable IDs are unsigned 64-bit integers allocated monotonically from 1 within a run. Authored entities receive IDs first in manifest order; spawned entities then consume the next ID. IDs are never reused, random, or derived from collection indices.

## Pooling rule

Object pooling is presentation/runtime storage only. Every checkout resets all fields. The authoritative entity ID is newly allocated. Double return is a debug failure and release diagnostic; it must not mutate another projectile.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| CB-001 | one enemy, 300 ticks | 10 opportunities/projectiles if target remains valid |
| CB-002 | equal-distance enemies | lower stable ID targeted |
| CB-003 | fast lateral target with valid intercept | predictive direction used |
| CB-004 | target at/above projectile speed | direct aim fallback |
| CB-005 | two targets on sweep | earliest intersection hit |
| CB-006 | equal intersection time | lower target ID hit |
| CB-007 | wall/entity exact tie | wall consumes projectile |
| CB-008 | Camera hit | −1 Camera Integrity regardless of 10 enemy damage |
| CB-009 | 32 live projectiles | opportunity rejected, count remains 32 |
| CB-010 | target dies before later ordered hit | later hit cannot damage/retarget it |
