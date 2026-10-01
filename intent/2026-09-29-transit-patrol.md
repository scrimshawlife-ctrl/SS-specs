# Intent: Transit Patrol

**Author:** prabu-openclaw  
**Date:** 2026-09-29  
**Status:** accepted (owner direction, 2026-09-29: "patrol is cool, sounds good")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

The Camera Corridor takes about 2 seconds to cross, so the run's opening has no stealth content. Cameras are stationary by rule, and Z-02 can hold at most two, so a camera gauntlet cannot supply tension. The first fight arrives 3.7 seconds after spawn.

## Proposed outcome

- **A moving stealth problem** in the corridor that a careful player reads and times: 20–40 seconds.
- **Optional:** sneak past, ambush, or fight.
- **Always fair:** an uncovered route always exists.

## Affected users/systems

- **Player:** the corridor gains a patrol with visible vision cones.
- **Specification:** `enemies-and-encounters.md` § Transit Patrol, `arena.md` Z-02, `animation.md`, `civic-seam-arena-003` (`patrols`), `combat-content-004` (`patrol`), D-091, and vectors EN-024–EN-030.
- **Runtime:** patrol movement, cone sight, presentation, fairness tests, probes, and goldens.

## Constraints/non-goals

- Existing archetypes only (constitution Article V).
- Cameras stay stationary.
- No gate. Excluded from the encounter graph and heat.

## Open questions

- The waypoints and values are a first cut. The runtime validates fairness and adjusts the data on the spec branch if a constraint fails (the D-087 precedent).

## Verified claims

- The Z-02 box is (320–832, 192–704), and its only solid edge is `solid-03-transit-kiosk`.
- Player speed is 240 units/s, and spawn to the M-A trigger is 887 units.

## Assumed claims

- A careful player spends 20–40 s in the corridor. The stealth-pilot probe must show it.
