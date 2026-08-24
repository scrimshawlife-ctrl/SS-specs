# Acceptance and Expansion Gates

Status: BASELINE  
Feature: SS-001

## Evidence rule

Each criterion requires a linked test, replay fixture, measurement, review plate, device capture, or recorded playtest result. A verbal assertion is not evidence.

## Gate A — Functional completion

- [ ] A-001 A clean install can start, complete, restart, and complete another run.
- [ ] A-002 All seven journey spaces are present and connected.
- [ ] A-003 Camera regions match authoritative detection.
- [ ] A-004 Blocking geometry reliably interrupts Camera detection.
- [ ] A-005 Exposure and every Detection State transition are communicated.
- [ ] A-006 Guards and Interceptors never spawn inside blocking geometry or protected Spawn Alley.
- [ ] A-007 Damage always has a visible or communicated source.
- [ ] A-008 All three upgrades materially change play and complete the level.
- [ ] A-009 Captain defeat reliably unlocks Extraction.
- [ ] A-010 Extraction countdown visibly resets when the Player leaves.
- [ ] A-011 Terminal events occur once and obey documented precedence.
- [ ] A-012 Result records contain all fields required by FR-045.
- [ ] A-013 Exactly eight standard Cameras exist at fixed authored transforms and fields for the full run.
- [ ] A-013A Every standard Camera transitions 3→2→1→0 from exactly three valid impacts.
- [ ] A-014 Camera damage does not impair detection before destruction.
- [ ] A-015 Destruction removes only the destroyed Camera field, persists for the run, and restores on restart.
- [ ] A-016 Each destruction applies one +100 Tamper Spike and no loot or area effect.
- [ ] A-017 Automatic targeting and Ricochet follow the exact Camera candidate and tie-break rules.
- [ ] A-018 Captain Camera remains outside the standard Camera destruction system.
- [ ] A-019 Eighth Camera destruction completes Network Blackout exactly once; 0–7 remains partial.
- [ ] A-020 Extraction succeeds at 0/8 or 7/8 Cameras when the required combat graph is complete.
- [ ] A-021 Extraction remains locked at 8/8 Cameras when any required mob, elite/sub-boss, or boss objective is incomplete.
- [ ] A-022 Required combat order is three mob encounters, The Improper Search Daemon, then The Algorithmic Moderate.

## Gate B — Determinism

- [ ] B-001 Three executions of every golden replay produce identical critical events and state digests.
- [ ] B-002 Golden replays pass on every supported architecture and target device.
- [ ] B-003 Restart restores the same initial state for the same Replay Identity.
- [ ] B-004 Suspend/resume does not advance authoritative state from wall-clock time.
- [ ] B-005 Unknown replay versions fail with a typed incompatibility result.
- [ ] B-006 Collection order, targeting ties, spawn ties, and terminal ties have tests.
- [ ] B-007 A rules-affecting change cannot alter a golden result without an explicit version change and rationale.
- [ ] B-008 Animation, VFX, audio, haptics, camera, and refresh rate do not mutate authoritative results.
- [ ] B-009 CD-001 through CD-014 pass with identical ordered events and state digests.
- [ ] B-010 Same-tick Camera destruction removes that Camera contact before continuous Exposure and applies Tamper afterward.
- [ ] B-011 Simultaneous hits and multi-Camera destruction resolve by stable entity ID without duplicate Tamper.

## Gate C — Stability and performance

Run three consecutive complete runs on a physical iPhone 12 or approved no-better equivalent.

- [ ] C-001 No crash, soft lock, memory warning, or unbounded growth.
- [ ] C-002 Frame-time p50 ≤ 16.67 ms.
- [ ] C-003 Frame-time p95 ≤ 16.67 ms.
- [ ] C-004 Frame-time p99 ≤ 25 ms.
- [ ] C-005 No gameplay frame exceeds 50 ms.
- [ ] C-006 No sustained presentation interval falls below 55 fps.
- [ ] C-007 No serious or critical thermal state occurs.
- [ ] C-008 Pools remain bounded and contain no stale lifecycle state.
- [ ] C-009 Ten consecutive automated complete-run simulations pass.
- [ ] C-010 Twenty manual restarts across all phases pass.
- [ ] C-011 Atlas, resident-memory, entity, projectile, particle, and transient ceilings match D-021.

## Gate D — Visual assets and animation

- [ ] D-001 Player remains identifiable at peak density and 50% gameplay scale.
- [ ] D-002 Lethal telegraphs and projectiles outrank decoration in every capture.
- [ ] D-003 Guard, Interceptor, and Captain silhouettes are distinguishable without color.
- [ ] D-004 Sprite contact points remain stable across clips.
- [ ] D-005 Camera fields and attack cones remain distinguishable.
- [ ] D-006 Every damaging animation provides its required anticipation.
- [ ] D-007 Animation commit markers align with authoritative event ticks.
- [ ] D-008 Reduced Motion preserves timing, meaning, and difficulty.
- [ ] D-009 No uncontrolled full-screen flash or unbounded emitter exists.
- [ ] D-010 Every shipped asset passes provenance, manifest, atlas, dimension, color-space, alpha, content, and reachability checks.
- [ ] D-011 No source master, rejected asset, other-city asset, or unreachable asset ships.
- [ ] D-012 Visual review plates pass on light, dark, grayscale, color-vision, dense-combat, and reduced-presentation variants.
- [ ] D-013 The Civic Seam is recognizable through grid, architecture, transit, repair, and surveillance language without labels.
- [ ] D-014 P0 inventory is complete before P1/P2 polish is admitted.
- [ ] D-015 No exact seal, real logo, copied street art, film/game asset, tourist collage, arbitrary cable car, or full-neon skin ships.
- [ ] D-016 Fog and ambient motion never conceal or outrank required gameplay information.
- [ ] D-017 Each landmark supports navigation, threat, cover, or progression.
- [ ] D-018 Operational, Damaged, Critical, and Destroyed Camera states are distinguishable without color or rapid blinking.
- [ ] D-019 Camera field presentation clears on the authoritative destruction update.
- [ ] D-020 Impact/destruction VFX remain bounded and reduced presentation preserves all state information.
- [ ] D-021 No Camera idle, hit, or ambient animation translates or rotates its authoritative housing or field.

## Gate E — Arena design and fairness

- [ ] E-001 All seven zones are reachable and preserve minimum path widths.
- [ ] E-002 No false wall, false opening, unexplained invisible boundary, or collision trap remains.
- [ ] E-003 The first Camera is seen before it can detect the Player.
- [ ] E-004 The Player escapes one isolated observation event before combined combat pressure.
- [ ] E-005 Civic Plaza and Lockdown retain at least one readable circulation loop.
- [ ] E-006 Pressure Route provides stealth-favored and combat-favored paths that reconnect.
- [ ] E-007 Every hostile spawn satisfies region, geometry, viewport, distance, reachability, and telegraph rules.
- [ ] E-008 When no valid spawn exists, spawning delays or skips without weakening constraints.
- [ ] E-009 Every upgrade retains viable Captain positioning.
- [ ] E-010 Extraction uses only previously taught pressure systems.
- [ ] E-011 Competent segment and complete-run pacing falls within the arena targets.
- [ ] E-012 Debug overlays and heatmaps show no invalid geometry, unreachable area, or spawn leak.
- [ ] E-013 The diagonal transit spine remains readable from at least four major landmarks.
- [ ] E-014 All seven zones are distinguishable by massing and material language.
- [ ] E-015 Apparent grade, stairs, and pitched vehicles do not create false movement or ballistic expectations.
- [ ] E-016 Phoenix Steps are visually unique and readable as the final destination.

## Gate F — Accessibility and comprehension

- [ ] F-001 New players learn movement without external explanation.
- [ ] F-002 New players identify Camera fields and explain how to reduce Exposure.
- [ ] F-003 Players understand why Lockdown began.
- [ ] F-004 Players attribute each recorded death to an observable cause.
- [ ] F-005 Color is not the sole carrier of Detection State, damage, objective, or telegraph class.
- [ ] F-006 Critical non-text state contrast reaches 3:1 and normal text reaches 4.5:1.
- [ ] F-007 Menus, upgrades, pause, and results work with VoiceOver.
- [ ] F-008 Dynamic Type up to 200% reflows or scrolls without loss of function.
- [ ] F-009 Touch targets are at least 44 × 44 points.
- [ ] F-010 Both handedness modes pass on the SE-class screen.
- [ ] F-011 Reduced Flash, Reduced Motion, captions, HUD scale, and separate audio/haptic controls pass.
- [ ] F-012 Every upgrade defeats the Captain without undocumented exploits.
- [ ] F-013 First Camera encounter communicates `3 HITS` and `DESTRUCTION ADDS EXPOSURE` visually, through captions, and through VoiceOver.
- [ ] F-014 Integrity notches and `+100 TAMPER` remain readable on the SE-class screen.

## Gate G — Playtest signal

Test with at least five people who did not implement the feature.

- [ ] G-001 At least four of five complete onboarding without instruction.
- [ ] G-002 At least four of five correctly describe Exposure after one run.
- [ ] G-003 No repeated confusion pattern remains unresolved.
- [ ] G-004 At least three of five voluntarily begin another run.
- [ ] G-005 Median competent successful run duration is 8–12 minutes after onboarding.
- [ ] G-006 Feedback identifies surveillance pressure—not generic combat—as a defining feature.
- [ ] G-007 At least four of five can distinguish Guard, Interceptor, Camera field, enemy projectile, and objective without a legend after one run.

## Expansion decision

A second level is authorized only when Gates A–G pass, D-013 and D-021 are settled, and all severity-one and severity-two defects are closed.

Possible decisions:

- `EXPANSION_GATE_PASSED`
- `EXPANSION_GATE_FAILED`
- `EXPANSION_GATE_NOT_COMPUTABLE`

Failure does not authorize undocumented exceptions. Correct the slice, update the specification through governance, or record why evidence is insufficient.
