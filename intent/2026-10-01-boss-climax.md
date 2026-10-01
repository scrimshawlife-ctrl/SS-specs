# Intent: Captain Court climax

**Author:** prabu-openclaw  
**Date:** 2026-10-01  
**Status:** accepted (owner direction, 2026-10-01: "do them all")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

Almost every death happens at the boss, and it comes from attrition (contact, and damage carried in from earlier), not from misreading the boss's attacks. The climax is a grind.

## Proposed outcome

- **Decided by attacks:** the boss fight is won or lost on its readable attacks.
- **Each phase an event:** every phase looks and sounds distinct.

## Affected users/systems

- **Player:** a threshold restore, lower contact damage, phase lighting, and telegraph rings.
- **Specification:** `bosses.md`, `combat-content-005`, `versions.json`, the `runtime-kernel-001` constants, fixtures, and D-096.
- **Runtime:** the restore rule, the content value, presentation, probes, and goldens.

## Constraints/non-goals

- No new attacks or content types.
- Presentation follows the Reduced Motion and Flash rules.

## Open questions

- Whether the boss stays challenging. The probe re-measures, and boss Integrity or the restore percent are the tuning levers.

## Verified claims

- D-093 probe: 198 of 203 deaths were at the boss; damage share was boss contact 32%, Daemon 22%, Witch bolts 21%, boss projectiles 12%.

## Assumed claims

- Win rates stay within the owner's targets. The probe confirms.
