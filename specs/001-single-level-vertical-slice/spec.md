# Feature Specification: San Francisco Vertical Slice

Status: BASELINE  
Feature ID: SS-001  
Ruleset version: `ruleset-001`  
Level version: `sf-001`

## 1. Product intent

Create a small, complete survival action game whose distinctive pressure comes from being observed. The player crosses a surveillance-heavy San Francisco district, develops one of three tactical strengths, survives a Lockdown, defeats the Response Captain, and reaches extraction.

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
| Camera | Static observer with visible line-of-sight geometry. |
| Guard | Standard pursuer that responds to current authoritative state. |
| Interceptor | Faster pressure enemy introduced after escalation. |
| Response Captain | The single boss whose defeat unlocks final extraction. |
| Lockdown | Maximum escalation phase triggered by the specified Exposure threshold or encounter progression. |
| Extraction | Final objective that completes a successful run after its prerequisites and survival countdown. |
| Upgrade | One of exactly three run-local choices that visibly alters play. |
| Replay Identity | Tuple of ruleset version, level version, seed, and ordered player inputs. |

## 4. Core journey

1. **Spawn Alley** teaches movement without damage pressure.
2. **Camera Corridor** introduces visible detection geometry and breaking line of sight.
3. **Civic Plaza** combines cameras and Guards.
4. **Pressure Route** permits a stealth-favored or combat-favored approach without branching the ending.
5. **Lockdown** raises pressure and introduces Interceptors.
6. **Captain Encounter** tests movement, exposure control, and combat.
7. **Extraction Platform** requires a final survival countdown and ends the run.

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

### Combat and enemies

- **FR-020:** The player MUST have one automatic base attack whose target-selection rule is deterministic.
- **FR-021:** Damage MUST identify its visible source or communicated hazard.
- **FR-022:** Guards MUST not spawn inside blocking geometry or within the protected spawn area.
- **FR-023:** Interceptors MUST appear only after their documented escalation condition.
- **FR-024:** Projectiles MUST be safely reusable without retaining state from a prior lifecycle.
- **FR-025:** Enemy removal, player damage, and death MUST occur at deterministic simulation boundaries.
- **FR-026:** The Response Captain MUST use a readable, finite attack vocabulary and MUST be defeatable with every valid upgrade path.

### Upgrades

- **FR-030:** Each run MUST offer exactly three upgrade identities: Signal Jammer, Ricochet Pulse, and Ghost Step.
- **FR-031:** Signal Jammer MUST materially reduce Exposure pressure.
- **FR-032:** Ricochet Pulse MUST materially improve crowd control.
- **FR-033:** Ghost Step MUST grant a brief, communicated detection immunity tied to a movement action.
- **FR-034:** Upgrade selection MUST pause or otherwise protect authoritative gameplay from uncommanded damage.
- **FR-035:** Each upgrade MUST visibly and measurably change player capability.

### Objective and completion

- **FR-040:** Extraction MUST remain locked until the Captain is defeated.
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
- Captain defeat and player death on the same tick MUST resolve deterministically. Baseline: player death ends the run.
- A pooled projectile returned twice MUST not corrupt the pool.
- A target removed between selection and attack resolution MUST be handled without retargeting inside the same resolution unless specified.
- Application suspension and resumption MUST not advance authoritative simulation by wall-clock elapsed time.
- Invalid or incompatible replay versions MUST fail clearly rather than approximate playback.

## 9. Success outcomes

- A new player understands movement, surveillance, upgrades, and extraction from in-game communication.
- A full run is stable and meets the target performance budget.
- Identical Replay Identities produce identical authoritative results.
- Playtest evidence shows voluntary replay rather than completion alone.
