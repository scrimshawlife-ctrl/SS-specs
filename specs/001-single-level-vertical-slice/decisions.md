# Decision Register

## Accepted baseline decisions

| ID | Decision | Status | Rationale |
|---|---|---|---|
| D-001 | Build one San Francisco level before any additional city. | ACCEPTED | Concentrates validation and polish. |
| D-002 | Target an 8–12 minute competent complete run. | ACCEPTED | Supports replay and bounded playtesting. |
| D-003 | Make Exposure the defining systemic mechanic. | ACCEPTED | Aligns theme with gameplay. |
| D-004 | Use exactly three run-local upgrades. | ACCEPTED | Creates choice without content sprawl. |
| D-005 | Reset extraction countdown when the player leaves the zone. | ACCEPTED | Clear and testable risk rule. |
| D-006 | Resolve lethal damage before extraction completion on the same tick. | ACCEPTED | Removes ambiguous simultaneous success. |
| D-007 | Player death ends the run when Captain defeat occurs on the same tick. | ACCEPTED | Establishes deterministic terminal precedence. |
| D-008 | Keep implementation in a separate runtime repository. | ACCEPTED | Preserves the specification/runtime boundary. |

## Owner decisions required before runtime foundation closes

| ID | Question | Status |
|---|---|---|
| D-010 | Which Apple platforms, minimum OS versions, orientations, and input methods are supported? | DECISION_PENDING |
| D-011 | Which target devices define the performance matrix? | DECISION_PENDING |
| D-012 | What exact frame-rate and frame-time thresholds must pass? | DECISION_PENDING |
| D-013 | What legacy repository commit is the immutable migration source? | DECISION_PENDING |
| D-014 | What name and ownership will the runtime repository use? | DECISION_PENDING |
| D-015 | Which accessibility baseline is mandatory for the first release? | DECISION_PENDING |

## Rule

A pending decision may block an implementation task or final gate, but it MUST NOT be replaced with an invented answer. Record new decisions here and update every affected artifact.
