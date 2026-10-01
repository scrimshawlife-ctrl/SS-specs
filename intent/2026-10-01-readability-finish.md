# Intent: readability and finish pass

**Author:** prabu-openclaw  
**Date:** 2026-10-01  
**Status:** accepted (owner direction, 2026-10-01: "start with 0 then do them all")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

A self-review of full runs found:
- the action hard to read (small dark actors, grey fog);
- a cluttered HUD (a constant caption scroll);
- unfinished pieces (blockout gates);
- a flat Lockdown.

## Proposed outcome

- **Readable:** action is clear at a glance on an iPhone.
- **Clean HUD:** it carries what matters.
- **No placeholders:** nothing on screen looks unfinished.
- **Lockdown:** feels like a city on alert.

## Affected users/systems

- **Player:** presentation and settings.
- **Specification:** `animation.md` § 8b, `audio-haptics.md`, `arena-layout.md`, `civic-seam-arena-004` (viewport), and D-094.
- **Runtime:** renderer, HUD, settings, and arena adoption.

## Constraints/non-goals

- Presentation only, plus the viewport values; no rules change.
- Accessibility guarantees hold (D-015): safety events always have a visual carrier, and nothing is carried by colour alone.

## Open questions

- None.

## Verified claims

- The viewport is used by audio sectoring and reachability, not by rules.
- Spawn fairness requires spawns outside the view, which a smaller view only eases.
- Closed gates render through the solid blockout path (no art).

## Assumed claims

- A 704-unit-wide view still shows enough of the arena for telegraph reading. The self-review re-capture checks this.
