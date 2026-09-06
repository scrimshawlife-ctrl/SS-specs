# The Civic Seam — Level 1 Visual Direction

Status: CANONICAL  
Feature: SS-001  
Direction version: `civic-seam-001`

## 1. Thesis

**A rebuilt civic city whose historic layers remain visible beneath an expanding machine of observation.**

Level 1 is a compressed, fictionalized district where the visual grammar of Market Street, Civic Center, and eastern SoMa collide. It is not a literal map and MUST NOT claim geographic fidelity. It uses real urban patterns to create a legible authored arena.

The central contrast is:

`historic civic order ↔ invisible algorithmic order`

Civic architecture promises permanence and public legibility. Ordinary networked sensors quietly overlay it with classification, tracking, and private control. Human counter-signals—posters, murals, birds, patched buildings, improvised street furniture, and closed blinds—prevent the city from becoming a sterile machine.

## 2. Provenance classification

### OBSERVED

The supplied research identifies:

- a diagonal boulevard crossing differently aligned street grids;
- triangular parcels and irregular intersections;
- dense street walls and visible rooftop layers;
- Classical civic buildings adjacent to Victorian, Edwardian, Art Deco, and industrial fabric;
- streetcar rails, overhead wires, transit islands, utility infrastructure, and modest grade changes;
- fog, long shadows, and ordinary cameras as recognizable visual systems;
- repair, retrofit, and rebuilding as recurring material history.

These observations derive from the linked planning, museum, archive, municipal, and cultural sources in section 13.

### INFERRED

The project translates those observations into:

- one strong southwest–northeast diagonal transit spine;
- a near-orthogonal civic/residential grid;
- a service grid rotated approximately 30–45 degrees;
- wedge-shaped combat spaces;
- long exposed sightlines crossed by short protected lanes;
- a phoenix-like reconstruction motif;
- a distant fictional three-pronged broadcast glyph;
- fog that reveals surveillance fields while softening distant noncritical detail.

### PROHIBITED INFERENCE

The level MUST NOT present the compressed district as a factual reconstruction, reproduce protected artwork or identities, or imply that fictional surveillance events occur at a real location.

## 3. Arena identity

The seven canonical gameplay zones keep their mechanical names and gain these visual identities:

| Gameplay zone | Civic Seam identity | Primary signal |
|---|---|---|
| Spawn Alley | Residential Wedge | Edwardian/Victorian façades, bay shadows, small trees |
| Camera Corridor | Transit Cut | diagonal rails, wires, island, first long Camera sweep |
| Civic Plaza | Civic Plaza | formal symmetry, stone massing, open exposure |
| Pressure Route | Service Seam | fire escapes, loading doors, conduits, rooftop network |
| Lockdown Ring | Grid Junction | three-grid collision, temporary sensor masts and barriers |
| Captain Court | Deco Authority Court | stepped Art Deco/civic façade and mechanical iris system |
| Extraction Platform | Phoenix Steps | raised civic/transit portal with fictional phoenix relief |

The diagonal transit spine MUST remain readable from at least four major arena landmarks. It supplies navigation, sightline risk, and visual continuity.

## 4. Architectural kit

Build the city from approximately 20–25 reusable modules. Unique buildings are exceptions.

| Family | Character | Arena use |
|---|---|---|
| Victorian commercial | cornices, vertical windows, projecting bays, painted trim | Residential Wedge perimeter |
| Edwardian apartment | pale stucco, restrained ornament, rounded bays, flat roof | repeatable mid-height fabric |
| Classical civic | rusticated base, columns, deep steps, symmetry, bronze doors | Civic Plaza and Phoenix Steps |
| Art Deco office | terracotta geometry, stepped crown, vertical fins, brass detail | Captain Court |
| SoMa industrial | brick, loading bays, steel sash, ducts and tanks | Service Seam |
| Mission fragment | curved parapet, stucco, tile inset | one minor landmark only |

Minimum module inventory:

- three bay-window projections;
- two cornice families;
- four storefronts;
- columns and pilasters;
- civic stairs and balustrades;
- fire escapes;
- rooftop HVAC, vents, tank, antenna clusters;
- brick loading dock;
- Mission-shaped parapet;
- Art Deco doorway and relief panels;
- recessed residential entries;
- flat roofs with varied parapets.

## 5. Street and infrastructure kit

P0 infrastructure:

- diagonal embedded rails, switches, and crossings;
- trolley poles, suspended wires, and junctions;
- transit-lane fragments and concrete boarding island;
- ventilation grates;
- traffic-signal mast;
- parking meters, hydrants, utility covers, bollards, barricades;
- newspaper boxes with fictional brands;
- bike racks/docks;
- parklet platform;
- bus shelter with surveillance display;
- curb ramps, retaining edges, sidewalk trees, curb markings;
- seismic braces and façade anchors.

Grade is visually modest:

- boulevard: 0–3% apparent;
- side street: 6–10%;
- one short service incline: 12–15%;
- level building foundations step with grade;
- parked vehicles pitch with the street;
- stairs provide nonmandatory shortcuts.

Elevation presentation MUST NOT change authoritative movement speed or projectile physics unless separately specified.

## 5b. Ground tiles carry no linear infrastructure

A ground tile repeats across a whole zone, so it may carry **surface** — paving,
wear, joints, stains — and must not carry a **linear feature**. Rails, kerbs,
lane markings and conduit runs are directional and continuous: tiling them
produces a visible lattice, because the eye follows the line and finds it
restarting on a fixed interval.

This was learned the direct way. The first Transit Cut tile embedded diagonal
rails, and at play scale the rails read as a repeating grid rather than as track.
The rails belong to the **infrastructure kit** in section 5, which is placed,
not to the ground kit, which is tiled.

So `env_ground_railbed` carries setts and ballast alone, and the rails are
`env_prop_rail_strip`: a 512-unit section placed end to end, whose rails meet
both short edges at the same height so a run reads as continuous track.

The run is laid **axis-aligned**, not on the diagonal this document describes as
the transit spine. A 45-degree run through the Transit Cut fouls the transit
kiosk and the civic massing and leaves the arena at its southwest end — the
authored arena is axis-aligned, and the diagonal spine is a compositional
intent that `civic-seam-arena-001` does not yet implement. Rails that cut
through a building would suggest a route where none exists, which matters more
than the angle. Aligning the spine is arena work, not art work.

Two rendering measures reduce tile repetition generally, and neither is a
substitute for the rule above:

- **Per-cell variation.** Tiles are drawn with a small deterministic brightness
  offset derived from cell coordinates, so identical tiles do not read as an
  identical lattice. It shifts no pixels, so a continuous feature stays
  continuous. Presentation only, derived from position rather than any RNG
  stream, and therefore invisible to the digest.
- **A kerb at zone boundaries.** Where two surfaces meet, an edge is drawn. Real
  paving changes at a kerb, so the boundary reads as a civic detail rather than
  as an artifact of rectangular zones.

## 5a. Decoration placement

Props and motifs are **non-collidable** and are placed by `decorations` in
`civic-seam-arena-001`: an asset ID, a centre in units, and an optional
`scalePermille`. They are presentation only and introduce no authoritative
state — a decoration cannot block, damage, or conceal anything.

Two placement rules are load-bearing:

- **A decoration may not overlap a permanent solid.** It would read as clutter
  inside a wall, and worse, it would suggest cover where none exists.
- **Authority Court stays sparse.** It is the boss arena and the busiest screen
  in the game; architecture and dressing must recede there.

Motif assets are landmarks rather than tiling material, so a placed one is
placed once and scaled down.

**Only a motif drawn in the arena's own projection may be placed.** The delivered
motifs are frontal elevations — drawn as though hung on a wall and viewed
head-on — and on a ground plane a frontal elevation reads as a picture pasted
flat on the floor rather than as part of the city. Verified on device: the
phoenix relief floats.

So the ground plane carries the phoenix alone, and only once it is redrawn as a
**floor inlay seen from directly above** — a civic medallion set flush into
paving, not a sculpture.

`env_motif_counter_signal` and `env_motif_repair` are **unplaced**. They are wall
pieces: good art in the wrong place rather than bad art, and they are retained as
reference for façade work, where a frontal elevation is exactly right.

**The broadcast glyph is unplaced for a different reason.** It is specified as a
*distant* skyline element, and a top-down arena has no skyline — placing it on
the ground plane would contradict what it is. It belongs on the title surface,
which already carries it.

## 6. Surveillance families

Ordinary devices are more important than futuristic spectacle.

| Family | Visual identity | Meaning |
|---|---|---|
| Municipal dome | off-white dome, cool status point | normalized observation |
| Storefront Camera | black rectangular body, exposed cable | fragmented private observation |
| Traffic reader | dual lens, infrared pulse | identification/tracking |
| Ornamental civic Camera | brass eye within fictional stone rosette | surveillance disguised as tradition |
| Mobile sensor mast | temporary battery/solar platform | emergency expansion |
| Captain Camera | Art Deco searchlight with mechanical iris | centralized control |

Camera fields remain procedural and share authoritative geometry. Camera housings may disguise purpose, but the active field and acquisition state MUST remain legible.

## 7. Symbolic vocabulary

### Fictional phoenix

Use a novel phoenix-like reconstruction glyph, not the municipal seal.

Approved applications:

- cracked relief at Phoenix Steps;
- wing-shaped paving or street geometry;
- gold feather-like collectible marker;
- repaired fire damage with visible metal seams;
- fragmented-pixel Extraction assembly;
- corrupted drone-like echo in surveillance UI.

The phoenix means: rebuilding can heal the city while also creating an opportunity to install new control.

### Fog

Fog is layered presentation with bounded gameplay effects:

- low layer reveals beams and tires/feet;
- high layer softens distant architecture;
- required hazards and objective cues remain above the readability floor;
- no fog state may conceal authoritative collision, lethal telegraphs, or required Camera boundaries;
- any gameplay visibility change is simulation-authored and versioned separately.

### Seismic repair

Use patched pavement, bolted braces, façade frames, misaligned curbs, repair plaques, and subtle wave patterns. Avoid disaster spectacle.

### Broadcast glyph

A distant fictional three-pronged tower acts as orientation and network symbolism. It MUST NOT reproduce Sutro Tower exactly.

## 8. Human counter-signal

The environment must contain signs of life and resistance:

- handmade privacy and organizing posters;
- murals with original abstract forms;
- pigeons and rare green parrots;
- repaired storefronts;
- blinds that close during detection;
- improvised parklets and street furniture;
- ordinary clutter placed below gameplay salience.

No real campaign art, movement logo, street-art reproduction, or political endorsement may appear without clearance.

## 9. Influence routing

References guide qualities, not assets or direct imitation:

| Reference | Extractable quality | Prohibited copying |
|---|---|---|
| *Bullitt* | grade momentum, compressed streets, cool urban palette | vehicles, chase, likenesses |
| *Vertigo* | elevation anxiety, watched framing, controlled color shift | Saul Bass work, costumes, exact scenes |
| *The Conversation* | rooftop observation, fragmented audio, surveillance tension | plot, characters, exact setup |
| *Dirty Harry* | telephoto sightlines and hard civic massing | character, dialogue, weapon poses |
| *Invasion of the Body Snatchers* | familiar city becoming subtly untrustworthy | pods and character design |
| *Watch Dogs 2* | playful resistance and visible networks | UI, logos, DedSec language |
| *The Matrix Resurrections* | technology overlay on familiar streets | glyphs, imagery, grading |
| *Milk* | street organizing and community presence | campaign artwork |
| *Wild Parrots of Telegraph Hill* | living color resisting rigid systems | documentary imagery |

Synthesis:

- spatial language: grade and diagonal momentum;
- psychological language: elevation and observation;
- surveillance language: fragmentation and distant listening;
- antagonist: cooperating ordinary sensors;
- counter-signal: community traces and living movement.

## 10. Palette and materials

| Role | Color |
|---|---|
| Fog light | `#CBD1CF` |
| Civic limestone | `#BDB39F` |
| Weathered stucco | `#A79C8B` |
| Asphalt blue-gray | `#343D43` |
| Brick shadow | `#594541` |
| Bay-window teal | `#406C6A` |
| Transit red | `#A83D39` |
| Aged brass | `#A68449` |
| Phoenix gold | `#D29A37` |
| Surveillance cyan | `#39C8D8` |
| Detection red | `#EF4B47` |

Historic materials are matte, repaired, and irregular. Civic stone has clear massing with stained joints and dark recesses. Sensor housings are sealed industrial polymer. Bright emissive color is reserved for active information and threat.

The level MUST NOT use generic full-neon cyberpunk treatment.

## 11. Ambient motion

### Persistent, low-cost candidates

- two-height fog drift;
- slight trolley-wire sway;
- asynchronous rooftop fans;
- traffic-signal cycle;
- distinct Camera idle patterns;
- occasional blind movement;
- paper/plastic in bounded wind channels;
- transit display refresh;
- pigeons scattering from combat.

### Rare, deterministic cosmetic events

- green parrot flock crossing;
- fictional autonomous vehicle hesitation;
- passing streetcar shadow without a full vehicle;
- distant tower light synchronization;
- phoenix relief apparent blink during a beam crossing;
- occupant closing blinds;
- fog reveal of the wider network.

Rare events MUST use seeded cosmetic scheduling, remain non-authoritative, and respect motion, density, and performance budgets.

## 12. Signage

Approved fictional phrases include:

- CIVIC SAFETY NODE 01
- OBSERVATION IMPROVES SERVICE
- PUBLIC SPACE / PRIVATE SIGNAL
- REBUILD AUTHORITY
- THE CITY SEES FOR YOU
- OPT OUT REQUEST RECEIVED
- TRANSIT CONTINUES DURING ALERT
- GOLD IN PEACE / DATA IN WAR

Signage styles may reference Victorian paint, theater blades, Art Deco lettering, municipal enamel, venture-backed sans serif, and handmade posters. Text remains sparse and nonessential at gameplay distance.

## 13. Constraints

- No tourist-landmark collage.
- No Golden Gate Bridge inside the arena.
- No arbitrary cable car shorthand.
- No exact corporate, transit, political, street-art, film, or game logo.
- No exact municipal seal.
- No geographically incoherent neighborhood mixture.
- No Chinatown visual language without a future Chinatown-specific level.
- No procedural clutter that obscures Player, projectiles, telegraphs, or Camera fields.
- No fog dense enough to conceal required information.
- Every landmark supports navigation, threat communication, cover, or progression.
- “Karl” is not a canonical fog name.

## 14. Research sources

- [SF General Plan — Market and Octavia](https://generalplan.sfplanning.org/Market_Octavia.htm)
- [SFO Museum — David Rumsey map collection](https://www.sfomuseum.org/exhibitions/san-francisco-david-rumsey-map-collection/gallery)
- [Library of Congress — 1864 bird’s-eye view](https://www.loc.gov/resource/g4364s.pm000343/?st=image)
- [SF Planning — Architectural periods and styles](https://default.sfplanning.org/Preservation/bulletins/HistPres_Bulletin_18.PDF)
- [SF General Plan — Civic Center](https://generalplan.sfplanning.org/Civic_Center.htm)
- [San Francisco Public Works — Better Market Street](https://sfpublicworks.org/bettermarketstreet)
- [EFF — camera concentration analysis](https://www.eff.org/deeplinks/2019/02/san-francisco-district-attorneys-10-most-surveilled-places)
- [San Francisco Administrative Code — civic flag](https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-19)
- [KQED — fog naming](https://www.kqed.org/news/11682057/how-the-bay-areas-fog-came-to-be-named-karl)
- [SF Travel — San Francisco on screen](https://www.sftravel.com/article/san-francisco-screen-where-famous-films-and-tv-shows-were-shot-around-city)

The attached research note is the synthesis source. These links retain external provenance; this specification is the project’s canonical design translation.
