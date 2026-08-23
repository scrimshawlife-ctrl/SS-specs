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

## Pending evidence decisions

| ID | Question | Status |
|---|---|---|
| D-013 | What exact legacy `main` commit and annotated tag define the immutable migration source? | DECISION_PENDING |
| D-020 | Which available physical devices will serve as approved equivalents for the four device classes? | DECISION_PENDING |
| D-021 | What exact profiled enemy, projectile, particle, atlas-memory, and resident-memory ceilings pass on iPhone 12? | DECISION_PENDING |

D-013 requires an exact head lookup immediately before the legacy freeze. D-021 must be derived from the playable grayscale blockout; it must not be guessed in advance.

## Rule

A pending decision may block an implementation task or final gate, but it MUST NOT be replaced with an invented answer. Record new decisions here and update every affected artifact.
