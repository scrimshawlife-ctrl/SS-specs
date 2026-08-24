# Exposure Contract

Status: CANONICAL  
Contract version: `exposure-001`

## Purpose

Exposure is the one authoritative surveillance-pressure value. It is deterministic, integer-valued, bounded, and independent of rendering.

## Constants

| Constant | Value |
|---|---:|
| Scale | 0–1000 integer points |
| Starting Exposure | 0 |
| First detecting Camera | +2 points/tick |
| Each additional detecting Camera | +1 point/tick |
| Contact gain cap | +5 points/tick |
| Recovery delay after last contact | 60 ticks |
| Recovery | −2 points/tick |
| Camera Tamper Spike | +100 points/destruction |

At 60 ticks/second, one Camera adds 120 points/second. Recovery begins only after 60 complete no-contact ticks and removes 120 points/second. Tamper is instantaneous and is not modified by contact count.

## Detection states

| State | Exposure |
|---|---:|
| `hidden` | 0–199 |
| `observed` | 200–449 |
| `tracked` | 450–699 |
| `hunted` | 700–999 |
| `lockdown` | 1000 |

There is no threshold hysteresis. State is a pure projection of Exposure after all deltas for the tick. `lockdown` is entered once, latched for the run, and fixes Exposure at 1000 thereafter. Recovery never exits Lockdown.

## Contact aggregation

After same-tick destruction removes dead Cameras, collect distinct surviving Camera IDs detecting the Player. Sort IDs ascending. For count `n`:

```text
contactDelta = n == 0 ? 0 : min(5, 2 + n - 1)
```

Overlapping fields add pressure; multiple samples from one Camera never do. Occlusion, range, and fixed field-angle tests belong to the arena/camera geometry contract.

## No-contact clock

- A contact tick sets `noContactTicks` to 0.
- A no-contact tick increments it by 1.
- Recovery applies when the incremented value is greater than 60.
- Therefore, the first recovery delta occurs on the 61st consecutive no-contact tick.
- Any new contact resets the clock before recovery is considered.

## Tick resolution

1. Camera contact is sampled.
2. Projectile damage and destruction resolve.
3. Contacts from Cameras destroyed this tick are removed.
4. Surviving-contact delta or no-contact recovery is calculated.
5. Ordered Tamper Spikes are added by Camera stable ID.
6. Clamp to 0–1000.
7. Project Detection State and emit upward transition events.
8. If 1000 is first reached, emit `LockdownEntered` once and latch.

Tamper and continuous contact may cross several thresholds in one tick. Emit one `DetectionStateChanged` event containing old and final state, not an event for every skipped state.

## Upgrade hook

`Signal Jammer` may reduce only continuous contact delta. Its modifier is applied after aggregation and before Tamper, using integer arithmetic. It cannot reduce a positive contact delta below 1 and never changes Tamper, recovery, thresholds, or Lockdown latching. Its exact value belongs to the upgrade contract.

## Required state

```json
{
  "exposure": 0,
  "detectionState": "hidden",
  "noContactTicks": 0,
  "lockdownEntered": false
}
```

## Golden vectors

| ID | Input | Expected |
|---|---|---|
| EX-001 | 100 ticks, one Camera | 200, `observed` |
| EX-002 | one tick, three Cameras | +4 |
| EX-003 | one tick, eight Cameras | +5 cap |
| EX-004 | 60 no-contact ticks from 300 | remains 300 |
| EX-005 | 61 no-contact ticks from 300 | 298 |
| EX-006 | contact on no-contact tick 60 | clock resets; contact gain; no recovery |
| EX-007 | destroy sole detecting Camera at 190 | no contact delta; +100 Tamper = 290, `observed` |
| EX-008 | destroy two detecting Cameras at 850 | +200 clamps 1000; one Lockdown event |
| EX-009 | no contact after Lockdown | remains 1000/`lockdown` |
| EX-010 | delta jumps `hidden` to `hunted` | one old→final transition event |

## Failure rules

Unknown Camera IDs, duplicate contacts, non-integer deltas, invalid thresholds, or values outside the scale are content/runtime errors. Debug builds fail fast; release builds reject the affected run and produce a diagnostic receipt rather than silently repairing authoritative state.
