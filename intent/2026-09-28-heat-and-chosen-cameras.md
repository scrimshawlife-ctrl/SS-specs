# Intent: surveillance with teeth (heat) and Cameras as a choice

**Author:** prabu-openclaw  
**Date:** 2026-09-28  
**Status:** accepted (owner direction, 2026-09-28: "do a and c")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

Exposure changes nothing in play: no simulation system reads it, and Lockdown is forced at M-C. The weapon auto-targets Cameras, so Camera kills and their Tamper Spikes happen by accident. The game's premise, surviving surveillance, has no mechanical stake.

## Proposed outcome

- **Heat:** being seen costs something, as more enemies.
- **Cameras:** destroying one is a decision.
- **Styles:** a careful run and a loud run play measurably differently.

## Affected users/systems

- **Player:** targeting, wave sizes, and HUD captions change.
- **Specification:** `camera-destruction.md` § 6, `combat.md`, `enemies-and-encounters.md`, `hud-tutorial.md`, `combat-content-002`, `versions.json`, `runtime-kernel-001` constants, fixtures, D-082/D-083.
- **Runtime:** targeting, the encounter director, the HUD caption, the probes (stealth and loud pilots), and regenerated goldens.

## Constraints/non-goals

- No new archetypes or content types (constitution Article V).
- M-C and forced Lockdown are unchanged.
- No awareness AI: that is option B, deferred.

## Open questions

- The reinforcement counts are a first cut. Probes and playtests tune them.

## Verified claims

- No simulation system reads `exposure` or `detectionState` except tutorial pre-emption.
- T305: 240 of 240 runs hit Lockdown at M-C, and 4–6 of 8 Cameras were destroyed per run.

## Assumed claims

- A careful player can reach M-C mostly `hidden` or `observed` under the new targeting. The stealth-pilot probe must show this.
