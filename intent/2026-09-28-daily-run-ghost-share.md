# Intent: Daily Run, ghost, and shareable run card

**Author:** prabu-openclaw  
**Date:** 2026-09-28  
**Status:** accepted (owner direction, 2026-09-28)  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

Every run starts on seed 1, so the Camera layout never changes. A finished run tells the player nothing but the outcome, and there is nothing to chase or show. The deterministic kernel, the game's strongest technical asset, is invisible to players.

## Proposed outcome

- **Daily layout:** one shared layout per UTC day.
- **Ghost:** the player's own best run on that layout, replayed beside them.
- **Run card:** the terminal surface shows a card the player can share.

## Affected users/systems

- **Player:** the title, terminal surface, and Settings change.
- **Specification:** run-shell.md § 4, 5, 7.2, 8, 9, 10, 11; D-081.
- **Runtime:** a daily seed derivation, a presentation-side ghost replay, a command log, best-run storage, a run card, and Share.

## Constraints/non-goals

- No change to rules, content, the arena, the digest, or receipts.
- No accounts, no network, no leaderboard, no run history screen, no unlocks.
- The simulation never reads a clock.

## Open questions

- Leaderboards or friends' ghosts need a network, so they are out of scope here.

## Verified claims

- `GameScene` starts every run on seed 1.
- The seed selects the Camera layout (`CameraPlacement.select`, `runSeed`) and the combat RNG.
- `Simulation.execute(ReplayEnvelope)` reproduces a run from its commands.

## Assumed claims

- A second simulation stepping in lockstep fits the iPhone 12 frame budget. To be measured under T406.
