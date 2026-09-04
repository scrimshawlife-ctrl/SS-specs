# Feature Specification: The Civic Seam

Status: BASELINE  
Feature ID: SS-001  
Ruleset version: `ss-rules-001`  
Arena version: `civic-seam-arena-001`

## 1. Product intent

Create a small, complete survival action game whose distinctive pressure comes from being observed. The player crosses **The Civic Seam**, a compressed fictional San Francisco district organized around a diagonal transit spine where civic, residential, and service grids collide, develops one of three tactical strengths, survives a Lockdown, defeats the Algorithmic Moderate, and reaches extraction.

## 2. Non-goals

This feature does not include:

- Other cities or selectable levels
- Procedural map generation
- Multiple characters or weapons
- Inventory or crafting
- Narrative branches
- Persistent meta-progression
- Online multiplayer
- General-purpose campaign or content frameworks
- Monetization systems

## 3. Ubiquitous language

| Term | Definition |
|---|---|
| Exposure | Bounded authoritative value representing accumulated surveillance pressure. |
| Detection State | `hidden`, `observed`, `tracked`, `hunted`, or `lockdown`. |
| Camera | Static destructible infrastructure observer with visible line-of-sight geometry. |
| Standard enemy | One of the five canonical archetypes in `enemies-and-encounters.md`. |
| Improper Search Daemon | Required elite/sub-boss after the three mob encounters. |
| Algorithmic Moderate | The single boss whose defeat completes Combat Authority. |
| Lockdown | Maximum escalation phase triggered by the specified Exposure threshold or encounter progression. |
| Extraction | Final objective that completes a successful run after its prerequisites and survival countdown. |
| Upgrade | One of exactly three run-local choices that visibly alters play. |
| Replay Identity | Tuple of ruleset version, level version, seed, and ordered player inputs. |
| Civic Seam | The fictional Level 1 district and its canonical visual identity. |

## 4. Core journey

1. **Spawn Alley / Residential Wedge** teaches movement without damage pressure.
2. **Camera Corridor / Transit Cut** introduces visible detection geometry and breaking line of sight.
3. **Civic Plaza** combines Cameras with the first standard-enemy roles.
4. **Pressure Route / Service Seam** permits a stealth-favored or combat-favored approach without branching the ending.
5. **Lockdown / Grid Junction** forces Lockdown and tests the full standard-enemy roster.
6. **Algorithmic Moderate / Deco Authority Court** tests movement, Exposure control, and combat.
7. **Extraction Platform / Phoenix Steps** requires a final survival countdown and ends the run.

## 5. Functional requirements

### Movement and world

- **FR-001:** The player MUST move responsively within traversable level bounds.
- **FR-002:** Collision MUST prevent traversal through blocking geometry.
- **FR-003:** The introductory area MUST teach movement through layout and feedback without requiring external instructions.
- **FR-004:** A restart MUST restore the complete initial authoritative state for the selected Replay Identity.

### Detection and Exposure

- **FR-010:** Every Camera MUST display a detection region consistent with its authoritative line-of-sight test.
- **FR-011:** Blocking geometry MUST interrupt Camera detection.
- **FR-012:** Exposure MUST increase only through specified observable causes.
- **FR-013:** Exposure MUST decrease under specified recovery conditions after the player breaks surveillance contact.
- **FR-014:** Detection State transitions MUST be deterministic and communicated to the player.
- **FR-015:** Re-entering detection MUST follow documented grace-period and accumulation rules; these values belong to the versioned tuning contract.
- **FR-016:** Maximum escalation MUST enter Lockdown exactly once per run.
- **FR-017:** Level 1 MUST deterministically select exactly eight standard Cameras per run from versioned authored sockets using `camera-placement.md`; after initialization their positions, headings, ranges, and field angles are immutable, and they never pan, relocate, spawn, activate, or respawn during the run.
- **FR-017A:** A standard Camera MUST require exactly three valid Player projectile impacts to destroy.
- **FR-018:** Destroying a Camera MUST permanently remove only that Camera field for the current run and apply exactly +100 Tamper Exposure.
- **FR-018A:** Destroying all eight Cameras MUST complete optional objective Network Blackout exactly once and MUST NOT alter Extraction eligibility.
- **FR-019:** Damaged and Critical Cameras MUST retain full detection capability until destroyed.

### Combat and enemies

- **FR-020:** The player MUST have one automatic base attack whose target-selection rule is deterministic.
- **FR-021:** Damage MUST identify its visible source or communicated hazard.
- **FR-022:** Standard enemies MUST spawn only from valid authored sockets outside blocking geometry and the protected spawn area.
- **FR-023:** Every standard enemy, elite, and boss behavior MUST conform to the exact activation and state-machine contracts.
- **FR-024:** Projectiles MUST be safely reusable without retaining state from a prior lifecycle.
- **FR-025:** Enemy removal, player damage, and death MUST occur at deterministic simulation boundaries.
- **FR-026:** The Algorithmic Moderate MUST use a readable, finite attack vocabulary and MUST be defeatable with every valid upgrade path.
- **FR-027:** Automatic targeting, Ricochet interaction, damage eligibility, tick order, persistence, and Camera destruction receipts MUST conform to `camera-destruction.md`.
- **FR-028:** The Captain Camera is an attack emitter and MUST NOT be treated as independently destructible standard infrastructure.

### Upgrades

- **FR-030:** Each run MUST offer exactly three upgrade identities: Signal Jammer, Ricochet Pulse, and Ghost Step.
- **FR-031:** Signal Jammer MUST materially reduce Exposure pressure.
- **FR-032:** Ricochet Pulse MUST materially improve crowd control.
- **FR-033:** Ghost Step MUST grant a brief, communicated detection immunity tied to a movement action.
- **FR-034:** Upgrade selection MUST pause or otherwise protect authoritative gameplay from uncommanded damage.
- **FR-035:** Each upgrade MUST visibly and measurably change player capability.

### World identity

- **FR-050:** The diagonal transit spine MUST remain a readable navigation landmark and a surveillance-risk axis.
- **FR-051:** The seven zones MUST use the visual identities defined by `civic-seam-visual-direction.md` without changing their mechanical responsibilities.
- **FR-052:** Fog, grade, rooftop depth, and architectural massing MUST NOT conceal required gameplay information.
- **FR-053:** Historic, civic, industrial, and surveillance elements MUST use modular recombination rather than a tourist-landmark collage.
- **FR-054:** Fictional phoenix, signage, and broadcast glyphs MUST remain original and MUST NOT reproduce municipal seals, real logos, protected art, or film/game assets.
- **FR-055:** Ambient motion MUST remain cosmetic, bounded, accessible, and non-authoritative.
- **FR-056:** Every visual landmark MUST support navigation, threat communication, cover, or progression.

### Objective and completion

- **FR-040:** Extraction MUST remain locked until the three required mob encounters, The Improper Search Daemon elite/sub-boss, and The Algorithmic Moderate boss are complete as defined by `encounter-objectives.md`.
- **FR-040A:** Camera destruction count and Network Blackout MUST NOT appear in the Extraction unlock predicate.
- **FR-041:** Entering the extraction zone before it unlocks MUST communicate the unmet prerequisite.
- **FR-042:** Unlocked Extraction MUST require a visible survival countdown.
- **FR-043:** Leaving the zone MUST follow one documented countdown rule: pause, reset, or continue. The baseline decision is **reset**.
- **FR-044:** Completion MUST occur once and freeze further authoritative combat outcomes.
- **FR-045:** The result screen MUST report outcome, duration, final Exposure or peak Exposure, damage taken, enemies defeated, upgrade identity, seed, ruleset version, and level version.

## 6. Detection state contract

The tuning artifact MUST define integer thresholds and rates. State ordering is fixed:

`hidden → observed → tracked → hunted → lockdown`

Exposure may fall and reverse among hidden, observed, tracked, and hunted. Lockdown is latched for the remainder of the run. Threshold comparisons MUST define inclusive/exclusive behavior and occur on deterministic simulation ticks.

## 7. User stories

### US-001 — Understand surveillance

As a new player, I can see when a Camera can observe me, recognize that Exposure is increasing, break line of sight, and observe recovery without reading external documentation.

### US-002 — Choose a play style

As a player, I can select one of three upgrades and feel a meaningful difference in stealth, crowd control, or mobility.

### US-003 — Attribute failure

As a player who loses, I can identify the damage source or escalation condition that caused the failure.

### US-004 — Complete a run

As a player, I can defeat the Captain, survive the extraction countdown, and receive a complete result record.

### US-005 — Reproduce a run

As a developer, I can replay the same authoritative inputs under the same Replay Identity and receive the same authoritative outcome.

## 8. Edge cases

- Simultaneous detection by multiple Cameras MUST use one documented aggregation rule.
- Simultaneous lethal damage and extraction completion MUST have a deterministic precedence rule. Baseline: lethal damage resolves before completion on the same tick.
- The Algorithmic Moderate defeat and player death on the same tick MUST resolve deterministically. Baseline: player death ends the run.
- A pooled projectile returned twice MUST not corrupt the pool.
- A target removed between selection and attack resolution MUST be handled without retargeting inside the same resolution unless specified.
- Application suspension and resumption MUST not advance authoritative simulation by wall-clock elapsed time.
- Invalid or incompatible replay versions MUST fail clearly rather than approximate playback.

## 9. Success outcomes

- A new player understands movement, surveillance, upgrades, and extraction from in-game communication.
- A full run is stable and meets the target performance budget.
- Identical Replay Identities produce identical authoritative results.
- Playtest evidence shows voluntary replay rather than completion alone.
