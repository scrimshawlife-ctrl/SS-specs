# The Civic Seam Arena Specification

Status: BASELINE  
Feature: SS-001  
Arena version: `sf-arena-001`

## 1. Arena thesis

The arena is one authored, interconnected fictional district called **The Civic Seam**. Its spatial grammar compresses the collision of Market Street, Civic Center, and eastern SoMa without reproducing a literal map. It combines the continuous movement pressure of survivor games with readable stealth geometry. It is not a random field and not a linear corridor. The player should form a mental map during the first run and exploit it during later runs.

A strong southwest–northeast diagonal transit spine crosses a near-orthogonal grid and a 30–45-degree service grid. This produces wedge spaces, exposed boulevard sightlines, protected rear lanes, and memorable irregular intersections.

The arena teaches through spatial sequence:

`Spawn Alley → Camera Corridor → Civic Plaza → Pressure Route → Lockdown Ring → Captain Court → Extraction Platform`

## 2. Coordinate and footprint contract

- Authoring grid: 64 world units.
- Baseline arena extent: 36 × 24 cells, or 2304 × 1536 world units.
- Final extent may vary by at most 15% after playtesting without a level-version change.
- Traversable primary paths: minimum 3 cells wide.
- Combat circulation loops: minimum 4 cells wide at pressure points.
- Protected Spawn Alley: no hostile spawn and no damaging Camera contact.
- Arena boundary: visually explained through architecture, fog, barriers, or grade—not invisible collision alone.
- Critical geometry MUST be data-authored and validated independently of art.

## 3. Spatial topology

### Z-01 Spawn Alley — Residential Wedge

Purpose: movement, camera follow, and safe-area comprehension.

- One obvious exit and one small optional loop.
- No damage for the initial teaching interval.
- Player can test every movement direction.
- First Camera is visible before its field can reach the player.
- No decorative motion that competes with the first surveillance cue.

### Z-02 Camera Corridor — Transit Cut

Purpose: line of sight, occlusion, Exposure accumulation, and recovery.

- Alternating cover creates at least two valid crossings.
- The shortest path crosses observation.
- The safer path teaches breaking line of sight.
- No enemy attack occurs before the player has received and escaped one readable observation event.
- Camera wedge boundaries remain visible across all floor materials.

### Z-03 Civic Plaza

Purpose: combine surveillance, Guards, auto-attack, and circulation.

- Central open pressure space with a perimeter loop.
- At least three exits remain visually distinguishable.
- Cover islands interrupt sight without creating collision traps.
- Guard spawn regions cannot enter the current viewport.
- Player must be able to circle the plaza without reversing through a dead end.

### Z-04 Pressure Route — Service Seam

Purpose: allow a stealth-favored or combat-favored approach.

- Two routes reconnect before Lockdown.
- Route A offers more cover and more Camera timing.
- Route B offers more enemy pressure and more open movement.
- Neither route grants an exclusive upgrade or irreversible advantage.
- Both routes teach mechanics used by the Captain.

### Z-05 Lockdown Ring — Grid Junction

Purpose: convert accumulated Exposure into explicit escalation.

- Boundary closure is communicated before it becomes authoritative.
- At least two circulation loops remain after barriers engage.
- Interceptor entry directions are telegraphed.
- The player is never locked into a space narrower than the minimum combat width.
- Lockdown does not erase the player's learned map.

### Z-06 Captain Court — Deco Authority Court

Purpose: readable boss arena with reusable cover and clear telegraphs.

- Baseline combat region: approximately 12 × 9 cells.
- No essential HUD overlaps the Captain or major telegraph origins.
- Four anchor landmarks provide orientation.
- Cover blocks may shape movement but must not invalidate attacks unpredictably.
- Spawn points remain outside immediate player collision and outside unavoidable telegraphs.
- Every upgrade path retains viable positioning.

### Z-07 Extraction Platform — Phoenix Steps

Purpose: final survival test and closure.

- Visible before it unlocks, but not safely campable during the Captain fight.
- One clear entrance plus one secondary escape route.
- Active boundary is distinguishable from Camera and damage geometry.
- Leaving resets the countdown.
- Final pressure comes from known systems; no new enemy type appears.
- Completion framing preserves player, countdown, and incoming threats.

## 4. Navigation grammar

- Major paths use strong floor or curb continuity.
- Blocking props do not create gaps that look passable.
- Dead ends are allowed only when they contain a clear reward or tactical reset and remain at least 3 cells deep.
- No corridor ends in unavoidable Camera contact.
- No collision throat is narrower than 1.5 player diameters.
- The player must always have at least one visible short-term movement option during non-terminal combat.
- Offscreen spawn routes must reach play without appearing to teleport.

## 5. Arena pacing

| Segment | Target elapsed time | Pressure purpose |
|---|---:|---|
| Spawn Alley | 0:00–0:45 | Learn movement |
| Camera Corridor | 0:45–2:00 | Learn observation and recovery |
| Civic Plaza | 2:00–4:00 | Combine combat and surveillance |
| Pressure Route | 4:00–6:00 | Express upgrade style |
| Lockdown Ring | 6:00–7:30 | Escalate and compress choices |
| Captain Court | 7:30–10:00 | Mastery test |
| Extraction | 10:00–12:00 | Final known-system pressure |

These are competent-run targets. First-run onboarding may be longer. Segment boundaries are event-based rather than wall-clock scripted where possible.

## 6. Encounter density

Density increases through composition, not uncontrolled entity count.

Each encounter configuration MUST declare:

- maximum active Guard count;
- maximum active Interceptor count;
- maximum active projectiles;
- maximum simultaneous telegraphs;
- spawn cadence;
- minimum player distance;
- offscreen margin;
- permitted spawn regions;
- Exposure-state modifiers;
- cleanup and pooling rules.

Baseline visual ceiling:

- no more than three simultaneous high-priority telegraph classes;
- no more than one Captain major telegraph;
- no more than two overlapping Camera fields at a required traversal choke;
- player silhouette visible in every acceptance capture;
- at least one escape corridor visually parseable at peak density.

Exact entity ceilings require runtime profiling on the iPhone 12 performance floor.

## 7. Surveillance geometry

Authored Camera sockets and every seeded selection follow this grammar:

1. **Teach** one isolated field.
2. **Test** with cover.
3. **Combine** with one enemy role.
4. **Cross-link** two fields with an escape route.
5. **Escalate** through timing or pressure, not invisible range changes.
6. **Master** through Captain interactions with known Camera behavior.

Camera socket position, range, field angle, heading, and occlusion are data. Eight sockets are selected at initialization under `camera-placement.md`; selected Cameras remain fixed. Visual fields render from the same data. Decorative lights may not use the same wedge language.

## 8. Spawn fairness

A hostile spawn is valid only when:

- inside an approved region;
- outside blocking geometry;
- outside the protected Spawn Alley;
- outside the player's collision safety radius;
- outside the current viewport plus declared margin, unless visibly delivered;
- reachable through navigation;
- not inside an active lethal telegraph;
- not positioned to guarantee damage before the minimum reaction window.

When no spawn satisfies all rules, the system skips or delays the spawn. It must not weaken the constraints silently.

## 9. Camera and viewport

- Landscape iPhone only.
- World projection respects safe areas.
- Player follow uses a dead zone so small corrections do not move the whole world.
- Look-ahead may bias toward movement by a bounded amount.
- Arena edges clamp the camera without exposing void.
- Objective arrows appear only when the objective is outside a defined inner viewport.
- The viewport must not reveal enemy pop-in inside its visible bounds.

## 10. Environmental storytelling

San Francisco identity uses compressed signals:

- civic concrete and transit infrastructure;
- steep-grade motifs represented without distorting authoritative movement;
- fog and marine color;
- retrofit cameras on familiar public objects;
- contradictory fictional public-safety signage;
- institutional maintenance clutter;
- distant landmark silhouettes.

Story details remain optional to notice. They do not conceal hazards, create false affordances, or require reading while moving.

## 11. Arena validation

Required tooling and evidence:

- collision overlay;
- Camera field and occlusion overlay;
- navigation reachability map;
- spawn-validity heatmap;
- safe-area and HUD overlay;
- encounter-density capture;
- critical-path traversal recording;
- all-upgrade Captain completion;
- left/right-handed control captures;
- small-screen capture;
- grayscale and reduced-motion capture.

Automated validation MUST reject unreachable zones, overlapping blocking geometry, invalid spawn regions, extraction without a route, and Camera definitions without a matching render projection.


## 12. Grid and landmark contract

- The diagonal spine crosses or visually connects at least four major landmarks.
- Triangular/wedge parcels create tactical identity without narrowing combat below minimum widths.
- Rooftops form a visible secondary city layer but never create false traversable space.
- Residential Wedge, Transit Cut, Civic Plaza, Service Seam, Grid Junction, Deco Authority Court, and Phoenix Steps must be identifiable in silhouette-only review plates.
- The fictional tower glyph provides distant orientation from at least three zones.
- The original phoenix relief marks Extraction and appears nowhere else at equal scale.

## 13. Grade contract

Apparent grade targets:

- diagonal boulevard: 0–3%;
- side street: 6–10%;
- one service incline: 12–15%.

Building bases step with grade; vehicles pitch with the street; stairs provide optional shortcuts. Presentation grade does not change authoritative movement or ballistics unless a later mechanics contract explicitly does so.

## 14. Place-identity validation

A passing arena must be recognizable as the Civic Seam without using a real landmark logo or explanatory label. Reviewers must identify:

- diagonal transit infrastructure;
- formal civic-to-worn-commercial contrast;
- residential bay/cornice rhythm;
- industrial service layer;
- seismic repair layer;
- ordinary Camera network;
- Phoenix Steps as the final destination.


## 15. Camera destruction placement contract

The arena declares exactly eight standard Camera placements. Each declares:

- stable Camera ID and housing family;
- immutable position, heading, range, and field angle;
- initial activation state;
- mount collision, hit shape, field origin, and target anchor;
- field orientation/range;
- return-traversal visibility after destruction.

Placement rules:

- The first damageable Camera provides room for three valid base-weapon impacts and teaches the Tamper trade.
- No required route assumes a Camera will be destroyed.
- Destroying a Camera may create a safer sightline but never a new collision route.
- Mount collision remains after destruction.
- Camera combinations must remain completable if the Player destroys none.
- The arena must remain completable if the Player destroys all eight standard Cameras.
- All eight are operational and damageable from run start, though geometry may delay access.
- Network Blackout is optional and never gates mobs, sub-boss, boss, or Extraction.
