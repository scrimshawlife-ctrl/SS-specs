# Decision Register

## Accepted baseline decisions

| ID | Decision | Status | Rationale |
|---|---|---|---|
| D-001 | Build one San Francisco level before any additional city. | ACCEPTED | Concentrates validation and polish. |
| D-002 | Target an 8–12 minute competent complete run. | ACCEPTED | Supports replay and bounded playtesting. |
| D-003 | Make Exposure the defining systemic mechanic. | ACCEPTED | Aligns theme with gameplay. |
| D-004 | Use exactly three run-local upgrades. | ACCEPTED | Creates choice without content sprawl. |
| D-005 | Reset Extraction countdown when the player leaves the zone. | ACCEPTED | Clear and testable risk rule. |
| D-006 | Resolve lethal damage before Extraction completion on the same tick. | ACCEPTED | Removes ambiguous simultaneous success. |
| D-007 | Player death ends the run when Captain defeat occurs on the same tick. | ACCEPTED | Establishes deterministic terminal precedence. |
| D-008 | Keep implementation in a separate runtime repository. | ACCEPTED | Preserves the specification/runtime boundary. |
| D-010 | Support iPhone only, landscape left/right, minimum iOS 18.0, touch input. | ACCEPTED | Reduces platform variance and matches the proven legacy baseline. |
| D-011 | Use SE 3rd generation, iPhone 12, current standard iPhone, and current Pro as physical device classes. | ACCEPTED | Covers small screen, performance floor, current standard, and ProMotion. |
| D-012 | Run authoritative simulation at 60 Hz and target stable 60 fps presentation. | ACCEPTED | Keeps timing deterministic and matches existing evidence. |
| D-014 | Use `scrimshawlife-ctrl/SS` for the new runtime repository after specification completion. | ACCEPTED | Short canonical runtime identity. |
| D-015 | Require VoiceOver-ready menus, non-color state carriers, Reduced Motion/Flash, scalable HUD, handedness, captions, and 44-point targets. | ACCEPTED | Establishes accessibility before art and UI harden. |
| D-016 | Use authored 2.5D top-down pixel art with a readability-first salience hierarchy. | ACCEPTED | Preserves atmosphere while protecting combat truth. |
| D-017 | Use one authored interconnected arena, not procedural generation. | ACCEPTED | Supports mastery, tuning, and controlled onboarding. |
| D-018 | Target four-direction actor art; project eight-direction movement when valid. | ACCEPTED | Bounds production while preserving directional clarity. |
| D-019 | Do not target 120 fps for SS-001. Request stable 60 Hz presentation on ProMotion devices. | ACCEPTED | Avoids a second presentation target before the core is proven. |
| D-022 | Name Level 1 **The Civic Seam** and use a compressed Market/Civic Center/eastern SoMa visual grammar. | ACCEPTED | Creates local identity through urban structure rather than landmark collage. |
| D-023 | Use one diagonal transit spine crossing civic/residential and rotated service grids. | ACCEPTED | Produces memorable sightlines, wedges, and cover transitions. |
| D-024 | Use an original phoenix-like reconstruction motif, ordinary cooperating Cameras, fog, and seismic repair as core symbols. | ACCEPTED | Connects rebuilding, civic order, and surveillance without copying protected identities. |
| D-025 | Use the supplied material palette and reserve emissive cyan/amber/red for active systems. | ACCEPTED | Protects threat readability and avoids generic neon cyberpunk. |
| D-026 | Route ambient city life through bounded cosmetic animation with reduced-motion and performance fallbacks. | ACCEPTED | Adds life without creating gameplay authority or density drift. |
| D-027 | Give each standard Camera exactly 3 Integrity; each valid Player projectile impact removes 1. | ACCEPTED | Creates a legible invariant independent of combat damage tuning. |
| D-028 | Keep Damaged and Critical Cameras fully operational until destruction. | ACCEPTED | Prevents ambiguous partial field behavior and stun-lock exploits. |
| D-029 | Apply exactly +100 Tamper Exposure once per destroyed Camera; do not directly reduce existing Exposure. | ACCEPTED | Makes destruction a permanent local benefit with a clear immediate cost. |
| D-030 | Remove the destroyed Camera contact before same-tick continuous Exposure, then apply Tamper. | ACCEPTED | Gives exact causal timing and matches the field visibly shutting off. |
| D-031 | Use Camera target priority: close enemy, detecting Camera, other enemy, other Camera; then distance and stable ID. | ACCEPTED | Protects the Player while making active surveillance destructible through auto-fire. |
| D-032 | Permit base projectiles and Ricochet to damage Cameras; exclude enemies, Ghost Step, Signal Jammer, and Captain Camera. | ACCEPTED | Keeps upgrade roles distinct and prevents environmental ambiguity. |
| D-033 | Camera destruction creates no loot, blind-spot entity, chain explosion, repair, or respawn during a run. | ACCEPTED | Preserves one bounded mechanic and avoids farming or hidden secondary systems. |
| D-034 | Level 1 contains exactly eight stationary Cameras with immutable position, heading, range, and field angle. | ACCEPTED | Makes surveillance geometry learnable and the destroy-all objective finite. |
| D-035 | Destroying all eight completes optional objective Network Blackout; it is never required for Extraction. | ACCEPTED | Separates surveillance mastery from mandatory combat progression. |
| D-036 | Extraction requires three mob encounters, The Improper Search Daemon, and The Algorithmic Moderate. | ACCEPTED | Preserves canonical San Francisco enemy lore and makes combat authority the primary gate. |
| D-037 | Preserve the Algorithmic Moderate phases: Public Safety, Civil Liberties, Temporary Safeguard, Independent Review. | ACCEPTED | Carries forward verified canonical boss identity without importing the ten-city campaign. |
| D-038 | Use integer Exposure 0–1000 with thresholds 200/450/700/1000, additive Camera contact capped at +5/tick, a 60-tick grace, and −2/tick recovery. | ACCEPTED | Makes the defining system directly implementable and golden-testable. |
| D-039 | Latch Lockdown at 1000 for the remainder of the run. | ACCEPTED | Preserves maximum escalation as a one-way run state. |
| D-040 | Use direct analog Player speed of 240 world units/second and deterministic axis-separated collision sliding. | ACCEPTED | Retains responsive proven legacy behavior with exact numeric rules. |
| D-041 | Include a baseline 12-tick dodge at 480 world units/second on a 120-tick cooldown, without default immunity. | ACCEPTED | Gives touch movement one explicit escape action while preserving Ghost Step's upgrade role. |
| D-042 | Start with Civic Pulse: 10 enemy damage, 30-tick cadence, 512 range, and a 720-unit/second swept projectile. | ACCEPTED | Locks the minimum viable combat loop before enemy tuning. |
| D-043 | Allocate monotonic UInt64 entity IDs, never reuse them, and use them for deterministic ties. | ACCEPTED | Removes collection and RNG dependence from ordering. |
| D-044 | Use xoshiro256** seeded through SplitMix64, canonical JSON, and SHA-256 for deterministic replay identity. | ACCEPTED | Defines portable RNG and digest behavior before runtime code. |
| D-045 | Treat the global 18-phase simulation order and four-part version identity as normative. | ACCEPTED | Prevents subsystem-local timing assumptions and incompatible replay execution. |

## Pending evidence decisions

| ID | Question | Status |
|---|---|---|
| D-013 | What exact legacy `main` commit and annotated tag define the immutable migration source? | DECISION_PENDING |
| D-020 | Which available physical devices will serve as approved equivalents for the four device classes? | DECISION_PENDING |
| D-021 | What exact profiled enemy, projectile, particle, atlas-memory, and resident-memory ceilings pass on iPhone 12? | DECISION_PENDING |

D-013 requires an exact head lookup immediately before the legacy freeze. D-021 must be derived from the playable grayscale blockout; it must not be guessed in advance.

## Rule

A pending decision may block an implementation task or final gate, but it MUST NOT be replaced with an invented answer. Record new decisions here and update every affected artifact.
