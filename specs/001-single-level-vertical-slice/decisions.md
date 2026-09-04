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
| D-014 | Use `scrimshawlife-ctrl/SS-runtime` as the runtime repository. | AMENDED | Amended 2026-09-01: the repository was created as `SS-runtime`, not `SS`; the specification records the identity that exists rather than the one that was reserved. |
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
| D-034 | Deterministically select eight Cameras per run from versioned authored sockets; once selected, each remains stationary with immutable position, heading, range, and field angle. | AMENDED | Adds seeded replay variety while keeping surveillance geometry fair, inspectable, and fixed during play. |
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
| D-046 | Use exactly five standard enemy archetypes with finite state machines and exact M-A/M-B/M-C wave totals of 14/17/25. | ACCEPTED | Creates readable role combinations without runtime-authored content. |
| D-047 | Force and latch Lockdown when M-C activates. | ACCEPTED | Guarantees the promised Lockdown mastery segment without relying on player mistakes. |
| D-048 | Offer Signal Jammer, Ricochet Pulse, and Ghost Step once after M-A; choose exactly one while simulation is protected. | ACCEPTED | Gives the run one legible tactical identity and deterministic selection timing. |
| D-049 | Give the Improper Search Daemon one fixed six-state cycle with no summons, immunity, Camera control, or Exposure effect. | ACCEPTED | Keeps the sub-boss distinct and bounded. |
| D-050 | Give the Algorithmic Moderate 800 HP, the four verified legacy policy phases, and four finite telegraphed attacks. | ACCEPTED | Preserves canon while making the final fight directly implementable. |
| D-051 | Freeze Level 1 at 2304 × 1536 world units using a 64-unit, 36 × 24 authoring grid. | ACCEPTED | Makes collision, sockets, camera framing, and asset scale directly implementable. |
| D-052 | Use exactly 14 permanent solids, five encounter gates, and the versioned spawn/trigger sockets in the arena manifest. | ACCEPTED | Replaces design stubs with executable geometry. |
| D-053 | Require 300 consecutive ticks inside Phoenix Steps for Extraction and reset immediately on exit. | ACCEPTED | Defines the final survival test without ambiguous timing. |
| D-054 | Use three fixed, cyclic Captain Camera emitter anchors independent of the 18 standard Camera sockets. | ACCEPTED | Keeps boss attack geometry deterministic and outside Network Blackout. |
| D-055 | Author HUD against an 844 × 390 safe reference canvas with uniform scaling and mirrored movement/Dodge controls. | ACCEPTED | Makes iPhone layout adaptation explicit without coupling UI points to simulation. |
| D-056 | Use the five-state tutorial sequence and exact safety copy in `hud-tutorial.md`. | ACCEPTED | Makes onboarding deterministic, bounded, and accessible. |
| D-057 | Cap simultaneous effects voices at eight and resolve contention by event priority then age. | ACCEPTED | Prevents audio overload and unbounded presentation work. |
| D-058 | Use append-only event ordinals under event schema version 001 and decimal-string UInt64 entity IDs in JSON. | ACCEPTED | Preserves stable ordering and lossless cross-environment serialization. |
| D-059 | Store canonical local receipts atomically, retain the newest 50, and perform no cloud sync or analytics upload. | ACCEPTED | Provides reproducible evidence with a bounded privacy-preserving footprint. |
| D-060 | Amend `presentation-assets-001` in place to add the `camera_field_off` audio event (T610), and add it to the audio event map. | ACCEPTED | The runtime shipped field-off audio (SS-runtime #20) against a contract that did not list it; both repositories carried `presentation-assets-001` with different content under one version ID. Pre-acceptance amendment recorded once here; any further change to this contract bumps to `-002`. |
| D-061 | Adopt the runtime-authored presentation contracts `clip-metadata-001`, `procedural-vfx-001`, `ambient-motion-001`, `visual-language-001`, and `asset-catalog-001`, plus golden fixtures `complete-run-vectors-001` and `replay-matrix-001`, as specification-owned under their existing IDs. | ACCEPTED | Article VII requires contract before implementation. These were introduced in SS-runtime (#16, #17, #22, T500, T801, T705, T901) without a specification commit and were unregistered in `contracts/versions.json`. Adopting them restores the specification as authority; from this commit the runtime bundle must byte-match `contracts/` and `fixtures/`. |
| D-062 | Record the 2026-08-31 multi-agent Workflows lock on the live product specification: existing Grok Bot skills `anti-slop-code`, `production-systems`, and `google-developer-style`; owner specialist Danny; reuse `Validate specification` here and `CI` in SS-runtime; do not invent skills or bots. | ACCEPTED | The lock was owner-authorized and memory-only. Writing it into `spec.md` makes the binding inspectable. |
| D-063 | Require `intent.md` before specify for non-trivial, feature, or RFC-sized work. Sequence: intent → `spec.md` Workflows → plan/tasks → implement. Template only; no invented product intents. | ACCEPTED | Makes the specify gate inspectable. The Civic Seam baseline is already specified. |

## Pending evidence decisions

| ID | Question | Status |
|---|---|---|
| D-013 | Freeze legacy evidence at `3b20d88d6a6e1fe8f07f45f581359d371fa65d98` under reference label `legacy-multicity-2026-08-24`. | ACCEPTED | Establishes immutable migration provenance. Annotated tag `legacy-multicity-2026-08-24` created 2026-09-01 (`e085ea8` → `3b20d88`). |
| D-020 | Which available physical devices will serve as approved equivalents for the four device classes? | DECISION_PENDING |
| D-021 | What exact profiled enemy, projectile, particle, atlas-memory, and resident-memory ceilings pass on iPhone 12? | DECISION_PENDING |

D-013 requires an exact head lookup immediately before the legacy freeze. D-021 must be derived from the playable grayscale blockout; it must not be guessed in advance.

## Rule

A pending decision may block an implementation task or final gate, but it MUST NOT be replaced with an invented answer. Record new decisions here and update every affected artifact.
