# Intent: awareness and ambush

**Author:** prabu-openclaw  
**Date:** 2026-09-29  
**Status:** accepted (owner direction, 2026-09-29: "do number 3")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

Staying hidden only lowers a cost (fewer reinforcements). It never earns anything, because every enemy always knows where the Player is. Stealth should be a way to play, not just damage control.

## Proposed outcome

- **Unaware enemies:** a hidden Player finds enemies that have not seen them.
- **Ambush:** striking first is decisive.
- **The link to bet 1:** being tracked by surveillance takes the ambush away.

## Affected users/systems

- **Player:** enemy behaviour, ambush damage, a `?`/`!` presentation, and tutorial copy.
- **Specification:** `enemies-and-encounters.md` § Awareness, `combat.md`, `animation.md`, `hud-tutorial.md`, `combat-content-003`, `procedural-vfx-003`, the event catalog (ordinal 290) and schema, `versions.json`, the `runtime-kernel-001` constants, fixtures, and D-089.
- **Runtime:** the enemy phase, damage resolution, events, presentation, probes, and goldens.

## Constraints/non-goals

- The elite and the boss are unchanged.
- Encounter gates are unchanged; no slipping past a fight.
- No new archetypes (constitution Article V).
- Deterministic: integer distance tests and a fixed evaluation order.

## Open questions

- The values (160 sight, 128 ally, ×2) are a first cut. Probes and playtests tune them.

## Verified claims

- Weapon range is 512 units, cadence 30 ticks, and damage 10 (`combat.md`).
- Standard enemy Integrity is 20/40/30/20/60 (`combat-content-002`).
- Encounter entry closes the forward gate (`enemies-and-encounters.md`).

## Assumed claims

- Unaware enemies holding position lengthens runs toward the 5–8 minute target. The probes must show it.
