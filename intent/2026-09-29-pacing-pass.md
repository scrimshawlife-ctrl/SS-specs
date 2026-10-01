# Intent: pacing pass

**Author:** prabu-openclaw  
**Date:** 2026-09-29  
**Status:** accepted (owner direction, 2026-09-29: "yes merge and do pacing pass"; "do a and b")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

Winning runs take about 2:56 against the 5–8 minute target, and D-089 sight never alerts anyone. The § 5 opening windows (75 s before the first fight) cannot exist on a map crossed in about 10 s.

## Proposed outcome

- **Run length:** competent winning runs inside 5–8 minutes.
- **Balance:** win rates held.
- **Sight:** it alerts a meaningful share of enemies.
- **Stealth:** keeps its ambush advantage.
- **Windows:** § 5 matches the map.

## Affected users/systems

- **Player:** enemy toughness, damage taken, awareness behaviour, and the pacing targets.
- **Specification:** `combat-content-004`, `enemies-and-encounters.md`, `combat.md`, `bosses.md`, `player-controller.md`, `arena.md` § 5, and D-090.
- **Runtime:** content adoption, the drift and damage-remainder rules, `PacingSegment` targets, probes, and goldens.

## Constraints/non-goals

- Existing content types only (Article V).
- Values only, plus two small rules (drift, the damage remainder).

## Open questions

- Whether Player Integrity 200 can replace the 50% damage rule. It is being measured; if equivalent, D-090 is amended before merge.

## Verified claims

- The search results are recorded in D-090 (seeds 1–20).

## Assumed claims

- The runtime re-probe reproduces the search's figures within noise.
