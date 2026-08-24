# Visual Asset Specification

Status: BASELINE  
Feature: SS-001  
Visual version: `visual-civic-seam-001`

## 1. Visual thesis

Surveillance Survivor uses readable 2.5D top-down pixel art with a dark urban base and high-salience systemic signals. The image must communicate:

1. player location;
2. immediate collision and escape space;
3. surveillance geometry;
4. incoming damage;
5. enemy role;
6. objective direction;
7. atmosphere and satire.

Decoration must never compete with these signals.

The tone is **paranoid slapstick**: privatized authority appears officious, over-equipped, and slightly absurd. The presentation is tense but not horror-realistic. San Francisco identity comes from geometry, grade, fog, transit, hills, civic materials, and selected landmarks—not labels pasted onto scenery.

## 2. Readability hierarchy

When the frame becomes dense, salience MUST resolve in this order:

| Priority | Surface | Required distinction |
|---:|---|---|
| 1 | Player | Unique silhouette, persistent grounding ring, unobscured core |
| 2 | Lethal telegraph and projectile | Shape, motion, outline, and high local contrast |
| 3 | Extraction and critical objective | Stable icon plus directional cue |
| 4 | Camera field and current detection | Procedural geometry plus boundary pattern |
| 5 | Algorithmic Moderate | Scale, silhouette, persistent boss marker |
| 6 | Standard enemies | Role-readable silhouettes |
| 7 | Drops and upgrade affordances | Compact pulse and icon |
| 8 | Environment interactables | Contextual rim or icon |
| 9 | Decoration | Lowest contrast and motion budget |

No lower-priority surface may obscure a higher-priority surface for more than two presentation frames.

## 3. Palette contract

The palette is role-based, not merely aesthetic.

| Role | Baseline family | Non-color carrier |
|---|---|---|
| Player | warm ivory / amber core | circular grounding ring and four-notch marker |
| Safe or recoverable space | cool cyan | dashed boundary |
| Camera observation | cyan-white at low state | scan-line pattern and wedge boundary |
| Tracked state | amber | double boundary and TRACKED glyph |
| Hunted / lethal warning | magenta-red | triangular chevrons and pulse cadence |
| Enemy body | desaturated civic/navy/gray | silhouette and role marker |
| Player attack | warm white | round projectile and short trail |
| Enemy attack | magenta/red | diamond projectile and segmented trail |
| Extraction | green-cyan | portal brackets and EXTRACT icon |
| Neutral environment | blue-gray, asphalt, concrete | material texture |
| Collectible | gold | diamond/star icon |

Color MUST NOT be the only state carrier. Critical adjacent UI contrast MUST target at least 3:1; normal text MUST target at least 4.5:1.

## 4. Perspective and world scale

- Projection: top-down 2.5D, approximately 3/4 presentation, with collision defined separately.
- Authoring grid: 64 logical world units.
- One traversal cell: 64 × 64 units.
- Canonical actor footprint: 28–36 units in diameter.
- Canonical visual sprite box: 64 × 64 pixels for Player and standard enemies.
- Improper Search Daemon visual box: 80 × 80 pixels. Algorithmic Moderate visual box: 96 × 96 pixels.
- Camera pole box: 64 × 96 pixels.
- Large environment modules: multiples of 64 pixels.
- Texture filtering: nearest-neighbor for pixel assets.
- Camera and collision MUST never infer geometry from opaque sprite bounds.

Sprites may exceed their collision footprint for hats, coats, weapons, or antennas. The ground-contact point MUST remain stable across every animation frame.

## 5. Required asset inventory

### Player

| Asset group | Minimum |
|---|---:|
| Idle | 4 frames × 4 directions |
| Move | 6 frames × 4 directions |
| Dodge/Ghost Step | 4 frames × 4 directions |
| Hurt | 3 frames × 4 directions |
| Defeat | 6 frames |
| Extraction | 6 frames |
| Grounding ring | procedural or 1 reusable texture |
| Aim/attack | procedural weapon orientation or 2–4 frame overlay |

### Enemies

Each standard enemy requires idle, move, attack/commit, hurt, and defeat presentation. All five canonical archetypes MUST have different silhouettes at thumbnail scale.

| Role | Visual identity |
|---|---|
| Fog Analytics Cloud | suspended clustered mass, soft perimeter, obvious pulse aperture |
| Cable-Car Correlator | long forward chassis, rail/route motif, committed charge axis |
| Sutro Signal Witch | tall narrow mast silhouette, cast antenna, ranged posture |
| Autonomous Informant | forward lean, narrow body, high-frequency leg silhouette |
| Victorian Vendor | broad loaded torso, receipt/projector appendage, deliberate stride |
| Improper Search Daemon | 1.25× mass, query apertures, dash-axis silhouette |
| Algorithmic Moderate | at least 1.5× mass, official geometric insignia, unique head/shoulder profile |

### Surveillance and objectives

- Camera pole base, mast, head, damaged state, destroyed state
- Procedural Camera field with state variants
- Camera acquisition reticle
- Exposure state glyphs
- Extraction locked, armed, active, interrupted, and complete states
- Boss health frame and phase markers
- Directional objective arrow
- Upgrade icons: Signal Jammer, Ricochet Pulse, Ghost Step

### San Francisco environment

Required modular families:

- asphalt and lane-marking tiles;
- concrete sidewalk and curb transitions;
- civic plaza paving;
- service alley walls, doors, dumpsters, and utility fixtures;
- transit platform edge and shelter components;
- hill/stair/ramp visual language;
- fog overlays;
- bollards, planters, barriers, kiosks, and street furniture;
- cable/transit motifs used sparingly;
- one distant landmark silhouette layer;
- surveillance retrofit variants for civic objects.

Text embedded in world textures is prohibited except for approved fictional diegetic signage that remains legible and non-essential.

## 6. Materials and collision legibility

Every blocking object MUST have:

- a stable ground contact;
- a boundary readable against every adjacent floor family;
- no transparent visual invitation into blocked space;
- a collision footprint that is smaller than or equal to the perceived solid base.

Every traversable transition MUST avoid false walls caused by high-contrast seams. Decorative shadows MUST NOT resemble Camera fields, projectiles, hazards, or navigable openings.

## 7. Procedural visual systems

The following MUST be procedural or data-driven:

- Camera fields and occlusion clipping;
- detection boundary patterns;
- target reticles;
- health and state rings;
- projectile trails;
- objective arrows;
- Extraction countdown;
- Exposure meter;
- fog density response;
- damage flash and hit-stop presentation;
- debug collision and line-of-sight overlays.

Baking Camera wedges, collision guides, captions, or state labels into environment art is prohibited.

## 8. VFX budget and language

| Event | Default presentation | Reduced presentation |
|---|---|---|
| Camera acquire | contracting reticle + short scan | static reticle + opacity step |
| Exposure threshold | HUD pulse + edge brackets | icon swap + short highlight |
| Player hit | 1–2 frame impact, directional arc | directional arc without screen flash |
| Enemy hit | compact spark, ≤ 120 ms | outline change |
| Enemy defeat | 4–8 particles, ≤ 350 ms | dissolve or 2-particle cue |
| Ghost Step | afterimage trail, ≤ 300 ms | single outline echo |
| Ricochet | segmented path trace | impact markers only |
| Lockdown | one controlled scene pulse + barriers | static perimeter change |
| Captain telegraph | ground shape + body anticipation | ground shape + phase icon |
| Extraction | inward particles + stable brackets | brackets + progress fill |

No gameplay VFX may use uncontrolled full-screen white flashes. Particle emitters MUST be pooled or bounded, use finite lifetimes, and stop emission when offscreen or irrelevant.

## 9. HUD and safe-area contract

- Support landscape left and landscape right.
- All critical controls and text MUST remain inside the current safe area.
- Virtual stick placement MUST support left- and right-handed modes.
- Critical gameplay HUD MUST occupy no more than 18% of the unobstructed play area during normal play.
- The center 60% of the viewport SHOULD remain free of persistent opaque UI.
- Player health, Exposure, current state, upgrade identity, and objective MUST be readable without opening a menu.
- Upgrade selection and result screens MUST support VoiceOver and Dynamic Type up to 200% through reflow or scrolling.
- Touch targets MUST be at least 44 × 44 points.

## 10. Texture and atlas contract

Atlas groups follow simultaneous use rather than directory convenience:

- `player.atlas`
- `enemies_standard.atlas`
- `captain.atlas`
- `sf_environment_core.atlas`
- `sf_environment_props.atlas`
- `surveillance_ui.atlas`
- `combat_vfx.atlas`
- `hud.atlas`

Rules:

- Preload the next encounter's required atlases before the encounter admits entities.
- Do not place all art in one atlas.
- Do not split every frame into separate runtime loads.
- Record decoded memory estimates per atlas.
- Reject duplicate content hashes under different names unless documented.
- Use opaque/replace blending where visual output permits.
- Assets not reachable in SS-001 MUST NOT ship in the application bundle.

Apple recommends texture atlases for textures rendered together and warns that overly large atlases increase memory use. The atlas layout therefore requires measurement rather than a fixed universal maximum.

## 11. File contract

Naming:

`{domain}_{role}_{state}_{direction}_{frame}@{scale}.png`

Example:

`actor_autonomous_informant_move_ne_03@1x.png`

Each source asset record MUST include:

- stable asset ID;
- role;
- source file;
- delivery file;
- pixel dimensions;
- color space;
- alpha requirement;
- anchor;
- visual bounds;
- intended atlas;
- animation clip IDs;
- content hash;
- license/provenance;
- authoring tool and export version;
- approval state.

Delivery PNGs MUST use sRGB, clean alpha, deterministic names, and exact approved dimensions. Masters remain outside the runtime bundle.

## 12. Visual validation

Every asset family MUST pass:

- dimension and color-space validation;
- non-empty opaque-content validation;
- alpha-edge inspection;
- nearest-neighbor scale inspection;
- contact-point stability;
- silhouette test at 50% gameplay scale;
- grayscale and color-vision simulation;
- light/dark background contrast plates;
- dense-combat occlusion plate;
- reduced-motion presentation plate;
- license and provenance check;
- runtime atlas lookup test.

A beautiful asset that weakens gameplay readability fails.


## 13. Civic Seam environment authority

The canonical location-specific direction is `civic-seam-visual-direction.md`. When a general visual rule conflicts with that artifact, gameplay readability remains supreme and the conflict requires a recorded decision.

The environment MUST use:

- a southwest–northeast diagonal transit spine;
- Victorian/Edwardian Residential Wedge;
- rail, trolley-wire, island, and ventilation infrastructure in Transit Cut;
- formal Classical massing in Civic Plaza and Phoenix Steps;
- brick, steel-sash, fire-escape, loading, and rooftop-service language in Service Seam;
- temporary sensor infrastructure at Grid Junction;
- restrained Art Deco authority language at Captain Court.

The approved environment palette extends the role palette with the exact material colors in the Civic Seam direction. Surveillance cyan and Detection red remain active-system colors, not general decoration.

## 14. Location-specific production inventory

P0:

- diagonal road/rail modules;
- Victorian, Edwardian, and Classical façade families;
- Civic Plaza landmark kit;
- six Camera housing families;
- trolley-wire system;
- two-layer fog;
- core street furniture;
- Detection State materials;
- original phoenix relief;
- basic rooftop kit.

P1:

- fire escapes;
- Art Deco corner/court kit;
- transit shelter and island;
- parklet;
- original protest-poster decals;
- seismic retrofit kit;
- signs/signals;
- pigeon and parrot animation;
- fictional autonomous vehicle;
- distant three-pronged tower glyph.

P2:

- window-interior cards;
- rare environmental events;
- rooftop narrative props;
- fictional historic plaques;
- repair variations;
- rain-darkened material state;
- storefront dressing;
- architectural Camera disguises.

P1 and P2 assets may not delay P0 gameplay acceptance.

## 15. Location-specific prohibitions

No Golden Gate Bridge, arbitrary cable car, exact civic seal, real logo, copied street art, full-neon cyberpunk skin, geographically incoherent neighborhood mixture, or dense fog that weakens gameplay truth may ship.


## 16. Camera destruction assets

The normative behavior is `camera-destruction.md`.

Every standard housing family requires:

- Operational Integrity 3 state;
- Damaged Integrity 2 state with one non-color damage marker;
- Critical Integrity 1 state with two-notch/non-color damage marker;
- Destroyed Integrity 0 state with broken-lens silhouette and no emissive field;
- compact hit VFX;
- bounded destruction VFX;
- field-off transition;
- three-notch targeting/Integrity HUD.

Housing damage art MUST NOT imply reduced detection before destruction. Destroyed debris has no collision and may not resemble loot.


All eight standard Cameras use stationary housings. No Camera animation may imply panning, tracking rotation, patrol, relocation, or changing field geometry. Housing families distinguish institutional provenance, not mechanics.


## Runtime presentation identity

The required HUD, control, telegraph, objective, and audio IDs are enumerated by `contracts/presentation-assets-001.json`. Shipped asset records must resolve every required ID exactly once. Missing, duplicate, unreachable, or undeclared runtime-facing IDs fail asset validation before release.
