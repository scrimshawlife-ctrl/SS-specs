# Player Controller Contract

Status: CANONICAL  
Contract version: `player-controller-001`

## Coordinate and timing model

- Simulation: fixed 60 Hz.
- World unit: 1/64 authored arena cell.
- Authoritative position and velocity: signed fixed-point integers with 1/256-world-unit precision.
- Player collision: circle, radius 18 world units.
- Spawn health: 100 Integrity.
- Presentation interpolation never feeds simulation state.

## Normalized command

The platform layer samples touch input and submits one command per tick:

```json
{"tick":1,"moveX":0,"moveY":0,"dodgePressed":false}
```

`moveX` and `moveY` are integers in −32767…32767. The platform applies a radial 0.15 dead zone, linearly remaps the remaining magnitude to 0…1, clamps the vector to the unit circle, quantizes half-away-from-zero, and then records it. Replays contain normalized commands, never touch coordinates.

Missing command for a running tick means neutral movement and no button edges. Duplicate, late, or future commands invalidate the run. Pause and app suspension create no simulation ticks.

## Ground movement

| Constant | Value |
|---|---:|
| Maximum speed | 240 world units/second |
| Maximum displacement | 4 world units/tick |
| Acceleration | none; direct analog velocity |
| Facing threshold | input magnitude > 0 |

Velocity is normalized direction × quantized magnitude × 240. Diagonal input cannot exceed maximum speed. The last non-zero movement heading persists while idle.

## Collision

The Player is a circle against authored axis-aligned solid rectangles and arena bounds. For each tick:

1. integrate X displacement and clamp to bounds;
2. if X overlaps a solid, restore previous X;
3. integrate Y from the X-resolved position and clamp;
4. if Y overlaps a solid, restore previous Y.

Solids are checked by ascending stable obstacle ID. Touching is allowed; penetration is not. This produces deterministic wall sliding. Cameras retain their permanent mount collision after destruction. Actors do not block one another.

## Dodge

| Constant | Value |
|---|---:|
| Cooldown | 120 ticks |
| Active duration | 12 ticks |
| Speed | 480 world units/second (8/tick) |
| Direction | current non-zero input, else stored facing |
| Charges | 1 |

`dodgePressed` is a rising-edge command. If ready, dodge begins before movement for that tick and active tick 1 is immediate. Active ticks replace normal movement but use the same collision rules. Collision may shorten the dodge. Baseline dodge grants no damage immunity and no surveillance immunity; `Ghost Step` may add only its specified immunity window. A press while unavailable is ignored and recorded as rejected; it is not buffered.

Cooldown begins on the first active tick. Dodge becomes ready when the current tick is at least `startedAtTick + 120`.

## Damage response

Contact damage is continuous and has no invulnerability window. The sum is capped to the three highest simultaneous threat rates, ordered by rate descending then stable entity ID. Integrity clamps to 0…100. Player death resolves before objectives or Extraction on the same tick.

## Accessibility and layout

Default is left virtual stick, right dodge button, top-corner pause; handedness mirrors stick and dodge. Control placement may change, but normalized commands and mechanics may not. Touch targets are at least 44×44 points and remain inside safe areas on every target device.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| PC-001 | full right for 60 ticks, no collision | +240 X |
| PC-002 | full diagonal for 60 ticks | distance 240, not 339.4 |
| PC-003 | half magnitude for 60 ticks | distance 120 |
| PC-004 | diagonal into vertical wall | X stops, Y slides |
| PC-005 | dodge full right | at most +96 X over 12 ticks |
| PC-006 | dodge into wall | no penetration; shortened distance |
| PC-007 | dodge press during cooldown | no dodge and one rejection record |
| PC-008 | suspend for ten seconds | zero added ticks/displacement |
