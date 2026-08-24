# Upgrade Contract

Status: CANONICAL  
Contract version: `upgrades-001`

## Selection

Immediately after M-A completes, offer exactly these three choices in this order:

0. Signal Jammer
1. Ricochet Pulse
2. Ghost Step

The game enters `upgradeSelectionPending`. No simulation tick, cooldown, Exposure, spawn, or damage advances while the selection interface is open. The next accepted tick command must contain one index 0–2 and neutral movement; the upgrade applies in simulation phase 2 and that tick then proceeds. Invalid or missing choice leaves the game protected and does not consume a tick.

Only one upgrade may be selected per run. It is active immediately, cannot be replaced, and is recorded by ID and contract version.

## Signal Jammer

Role: surveillance control.

- Reduce positive continuous Camera contact delta by 1 point/tick, minimum 1.
- Reduce Fog Analytics Cloud Exposure pulses and Algorithmic Moderate Observation pulses by 25%, rounded half away from zero.
- Do not affect Tamper Spikes, M-C forced Lockdown, thresholds, recovery, Camera Integrity, field presentation, enemy speed, or damage.
- Required presentation: cyan interference contour around Player while an affected contact/pulse is being modified.

Examples: contact +2 becomes +1; +5 becomes +4; Fog pulse +20 becomes +15.

## Ricochet Pulse

Role: crowd control.

- Each Civic Pulse hit may create one continuation.
- Continuation range: 160 world units from the first target anchor.
- Valid continuation classes are living enemies and damageable Cameras, excluding the original target.
- Sort by squared distance from first target, then stable entity ID.
- Require unobstructed line of fire.
- Continuation deals full Civic Pulse damage: 10 enemy Integrity or 1 Camera Integrity.
- No third hit, recursive chain, duplicated target, or bonus projectile.
- Continuation resolves after the first hit in the same damage phase and records the original projectile ID.
- If no candidate exists, nothing happens.

## Ghost Step

Role: mobility and surveillance evasion.

| Property | Baseline | Ghost Step |
|---|---:|---:|
| Dodge speed | 480 | 540 units/second |
| Dodge duration | 12 | 12 ticks |
| Dodge cooldown | 120 | 90 ticks |
| Camera detection immunity | 0 | active dodge + 18 ticks |
| Damage immunity | 0 | 0 |

On accepted dodge start, set `cameraInvisibleUntilTick = startTick + 29`, inclusive of the 12 active ticks and 18 following ticks. Camera contact sampling ignores the Player through that tick. Fog/boss pulses are not Cameras and remain effective. Tamper remains effective. Enemy collision/contact and projectiles remain damaging.

## Balance invariants

- Every upgrade must defeat every required enemy and boss phase without exploiting Camera destruction.
- Every upgrade must succeed with zero Cameras destroyed.
- Signal Jammer cannot prevent forced Lockdown.
- Ricochet cannot hit one target twice from one projectile.
- Ghost Step cannot cross solids or provide damage immunity.
- No upgrade changes base Player HP, base enemy HP, spawn count, boss HP, or objective predicates.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| UP-001 | selection UI open 600 wall-clock ticks | zero authoritative ticks pass |
| UP-002 | select index 0 | only Signal Jammer active |
| UP-003 | invalid index | protected state remains; no tick |
| UP-004 | Jammer with one/two/eight Cameras | deltas +1/+2/+4 |
| UP-005 | Jammer plus +100 Tamper | Tamper remains +100 |
| UP-006 | Ricochet equal-distance candidates | lower stable ID continuation |
| UP-007 | Ricochet first hit destroys Camera | destroyed Camera excluded |
| UP-008 | Ghost Step starts tick 100 | Camera immune through tick 129 |
| UP-009 | Ghost Step during hostile projectile hit | projectile still damages |
| UP-010 | restart | no selected upgrade before M-A completion |
