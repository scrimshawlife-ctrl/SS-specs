# Civic Seam Arena Layout

Status: CANONICAL  
Contract version: `civic-seam-arena-001`

The machine-readable source of truth is `contracts/civic-seam-arena-001.json`. This document defines interpretation and validation.

## Coordinate system

- Arena: 36 × 24 cells.
- Cell: 64 × 64 world units.
- Bounds: x 0–2304, y 0–1536.
- Origin: southwest/bottom-left.
- Positive X: east/right. Positive Y: north/up.
- Every authored coordinate is an integer world unit.
- Rectangles use center and half-size; boundaries are inclusive for containment and exclusive for penetration.
- Angles use millidegrees clockwise from positive X and normalize to 0–359999.

The diagonal transit spine is the navigable band from southwest Z-01 through Z-03 and northeast Z-04. Mechanical grade is flat; slope is presentation only.

## Zone progression

| Zone | Trigger rectangle | Responsibility |
|---|---|---|
| Z-01 Residential Wedge | center (224,256), half (160,192) | protected spawn/tutorial |
| Z-02 Transit Cut | center (576,448), half (256,256) | Camera tutorial |
| Z-03 Civic Plaza | center (1024,640), half (256,256) | M-A and upgrade |
| Z-04 Service Seam | center (1376,1088), half (288,320) | M-B and route choice |
| Z-05 Grid Junction | center (1728,832), half (256,256) | M-C and elite |
| Z-06 Authority Court | center (2048,640), half (192,256) | boss |
| Z-07 Phoenix Steps | center (2048,224), half (192,128) | Extraction |

Zone rectangles may overlap only at transitions. They are progression/telemetry regions, not collision.

## Critical route and gates

The route visits zones in numeric order. Five encounter gates are non-solid until their owner activates:

- `gate-ma-forward` closes M-A’s east exit;
- `gate-mb-forward` closes M-B’s southeast exit;
- `gate-mc-forward` closes the Authority Court approach;
- `gate-elite-forward` remains closed until the Daemon is defeated;
- `gate-boss-extraction` remains closed until the Algorithmic Moderate is defeated.

Encounter gates use authored rectangles but cannot overlap Player or enemy spawn sockets. Gate changes occur only in simulation phase 15 or 16. Closing a gate while the Player intersects its rectangle is delayed until the rectangle is clear.

## Collision

Arena bounds and 14 permanent axis-aligned rectangles define solid geometry. Decorative geometry never adds collision. Every solid has a stable ID; simulation tests them in ascending UTF-8 ID order.

Minimum navigable widths:

- critical traversal: 128 units;
- combat circulation: 160 units;
- boss safe corridor: 192 units;
- Camera firing stand: 64-unit-radius clear region.

## Spawn sockets

The manifest contains:

- one Player spawn;
- six M-A sockets in Z-03;
- eight M-B sockets in Z-04;
- eight M-C sockets in Z-05;
- one elite socket;
- one boss socket;
- six boss-projectile/emitter anchors;
- four extraction-pressure sockets.

Enemy spawning applies the filtering/order rules in `enemies-and-encounters.md`. A socket is a point, not a region; the spawned circle must be clear for its archetype radius.

## Camera sockets

The manifest contains exactly 18 enabled sockets:

- Z-02: 4, select 2;
- Z-03: 3, select 1;
- Z-04: 4, select 2;
- Z-05: 4, select 2;
- Z-06: 3, select 1.

All socket fields are fixed authored geometry. `camera-placement.md` selects eight deterministically. Socket incompatibilities prevent unfair overlapping combinations. The socket manifest includes target anchors and hit/field offsets; Camera housing art does not change them.

## Captain Camera emitters

Z-06 contains three fixed emitter anchors. Temporary Order chooses them cyclically by phase-local attack ordinal. Emitters are boss attack geometry, not standard Camera sockets. Their field is 70 degrees, range 320 units, and active only during Temporary Order.

## Extraction

Phoenix Steps Extraction is the rectangle centered at (2048,192) with half-size (96,64).

- Locked contact displays the remaining combat prerequisite and starts no timer.
- Armed contact starts a 300-tick countdown.
- The Player must be alive and inside on every countdown tick.
- Leaving resets progress to 0 immediately.
- Re-entry restarts at 300.
- Boss projectiles and Captain fields are already retired before arming.
- Standard Cameras, Exposure, and Network Blackout do not alter the predicate or countdown.
- Lethal damage on countdown tick 300 produces failure, not extraction.

## Camera and viewport framing

- Logical reference viewport: 844 × 390 points in landscape.
- World camera baseline visible size: 896 × 414 world units.
- Follow dead zone: 96 × 64 world units.
- Maximum look-ahead: 96 units along movement heading.
- Look-ahead smoothing is presentation-only.
- World view clamps to arena bounds.
- Gameplay HUD safe rectangle is provided by the platform after iOS safe-area insets; no arena coordinate depends on device points.

## Validation requirements

Content CI must reject the manifest unless:

1. all IDs are unique within their namespace;
2. all rectangles and points are within bounds;
3. permanent solids do not overlap required trigger centers, Player spawn, Extraction, or required spawn points;
4. every consecutive zone pair has a 128-unit-clear path;
5. all enemy sockets are reachable from their encounter trigger;
6. all Camera sockets satisfy `camera-placement.md`;
7. every legal Camera selection is completable at 0/8 and 8/8 destroyed;
8. no required choke has more than two selected fields;
9. the Z-06 boss safe corridor survives every legal Camera selection and Temporary Order emitter;
10. the Extraction rectangle is reachable only after the boss gate opens;
11. gate closure never seals the encounter’s escape aperture;
12. all socket and rectangle coordinates are integer and stable under JSON round-trip.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| AR-001 | manifest dimensions | 2304 × 1536; 36 × 24 cells |
| AR-002 | count namespaces | 7 zones, 14 solids, 5 gates, 18 Camera sockets |
| AR-003 | Camera quota | selected 2/1/2/2/1 |
| AR-004 | Player spawn | inside Z-01, outside all solids and Camera fields |
| AR-005 | closed M-A gate | escape aperture remains reachable |
| AR-006 | all permanent solids | no critical path below 128 units |
| AR-007 | boss safe corridor | 192-unit route remains clear |
| AR-008 | Extraction enter/leave/re-enter | start/reset/restart 300 ticks |
| AR-009 | lethal damage at final countdown | failure precedence |
| AR-010 | same manifest JSON round-trip | identical canonical digest |
