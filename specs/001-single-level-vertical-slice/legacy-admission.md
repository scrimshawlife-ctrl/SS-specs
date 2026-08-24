# Legacy Component Admission

Status: EVALUATED_WITH_LIMITS  
Provenance date: 2026-08-24

## Immutable source

- Repository: `scrimshawlife-ctrl/Surveillance-Survivor`
- Source commit: `3b20d88d6a6e1fe8f07f45f581359d371fa65d98`
- Reference label: `legacy-multicity-2026-08-24` (specification label; annotated repository tag not yet created)
- Observed core path: `Sources/SurveillanceCore/Simulation.swift`
- Observed policy path: `Sources/SurveillanceCore/SanFranciscoPolicyPhase.swift`
- Observed content path: `Sources/SurveillanceCore/Resources/bosses.json`
- Build environment and complete test result at this SHA: NOT_COMPUTABLE from available evidence
- Known product defect: legacy scope and systems are too broad and internally coupled for the one-level reboot

No legacy file may be copied wholesale. The commit is evidence only.

## Decisions

| ID | Candidate | Decision | Evidence and boundary | Runtime destination |
|---|---|---|---|---|
| LC-001 | Seeded randomness | REWRITE | Legacy injects deterministic RNG, but SS-001 fixes xoshiro256**/SplitMix64 and isolated streams. Algorithm compatibility is not established. | Determinism/RNG |
| LC-002 | Simulation timing | ADAPT | `Simulation.swift` has validated 1/60 fixed step and prevents wall-clock stepping. Retain behavior, replace surrounding state. | SimulationClock |
| LC-003 | Player movement | ADAPT | Legacy direct analog throttle and X-then-Y obstacle slide are observed and match `player-controller-001`; replace floating numeric authority. | MovementSystem |
| LC-004 | Camera LOS | REWRITE | Legacy sensor geometry is useful evidence, but rotating/multiple sensor archetypes conflict with stationary seeded sockets and exact Exposure. | DetectionSystem |
| LC-005 | Projectile pool/lifecycle | ADAPT | Legacy lifecycle reset and projectile-origin handling are useful patterns; authoritative IDs and storage must follow new contracts. | CombatSystem/ProjectileStore |
| LC-006 | Combat resolution | ADAPT | Swept-circle earliest-hit and stable-ID tie behavior are observed and fit; rewrite numeric layer, target classes, damage tables, and event emission. | CombatSystem |
| LC-007 | Enemy behaviors | REWRITE | Legacy generalized guard/boss catalogs do not implement the five exact Level 1 state machines. | EnemySystem |
| LC-008 | Extraction logic | REWRITE | Legacy boss/Blind Spot flow does not implement the required three mobs → elite → boss → 300-tick Phoenix Steps predicate. | ObjectiveSystem |
| LC-009 | Visual assets | REJECT | Wholesale admission lacks per-asset provenance and conflicts with the new Civic Seam inventory. An individual asset may return only through the new asset-record process. | VisualCatalog |
| LC-010 | Audio assets | REJECT | Legacy clips are not proven against the new event IDs, priority, coalescence, license, and accessibility contract. | AudioProjector |

## Verified legacy behavior retained as specification evidence

- fixed 60 Hz simulation;
- direct analog movement throttle;
- X-then-Y solid collision slide;
- predictive projectile intercept with direct-aim fallback;
- swept projectile collision with earliest-hit and stable-ID ties;
- additive simultaneous Camera pressure;
- four Algorithmic Moderate policy-phase identities and verified ratios.

These are design provenance, not permission to copy code.

## Default exclusions

City selection, ten-city campaign authority, district procedural generation, challenge systems, generalized city profiles, legacy upgrade catalog, multiple characters, inventory/crafting, global state containers, store-launch scope, and non-SF runtime assets are REJECTED for SS-001.

## Copy gate

A runtime pull request that copies or ports legacy source must cite the candidate ID, exact source lines at the frozen commit, destination contract, and new tests. REWRITE and REJECT decisions prohibit source copying. ADAPT permits bounded reimplementation after review, not file transfer.
