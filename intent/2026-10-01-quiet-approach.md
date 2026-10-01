# Intent: Quiet approach (the stealth reward)

**Author:** prabu-openclaw  
**Date:** 2026-10-01  
**Status:** accepted (owner direction, 2026-10-01: "spec the stealth reward")  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

Stealth pays nothing. In the D-096 final probe, stealth wins 52% of legal runs and loud wins 53%. The quiet route takes longer to play, and the `GHOST` medal is only cosmetic. D-093 set the target that stealth should win more than loud and left it to playtests. No rule exists that could make that happen.

## Proposed outcome

- **A real reward for staying quiet:** a Player who reaches M-C without ever being `tracked` enters the Captain fight stronger.
- **Legible:** the Player can see the reward is in reach, see when it is lost, and see it paid.
- **Stealth wins more:** stealth's win rate rises measurably above loud's, and nobody else's changes.

## Affected users/systems

- **Player:** a `QUIET` tag under the Exposure bar, a caption when it is lost, and a bigger court restore when it is kept.
- **Specification:** `exposure.md` (the latch and EX-013 to EX-016), `bosses.md` (the restore and BO-022 to BO-024), `hud-tutorial.md` (copy and UI-009 to UI-011), `run-shell.md` (RS-024), `combat-content-006`, `versions.json`, the `runtime-kernel-001` constants, fixtures, and D-101.
- **Runtime:** the latch, the restore branch, the HUD tag and captions, probes, and goldens.

## Constraints/non-goals

- No new content (Article V). The reward pays through the existing D-096 restore.
- The reward is tied to Exposure (Article II): its condition is the Detection State.
- No drops from enemy deaths (enemies-and-encounters.md).
- Loud and competent play must not change.
- The patrol slip-past target (D-093) stays a playtest question.

## Open questions

- Whether 60% is the right size. The probe decides, and `courtQuietRestorePercent` is the lever (55–70).
- Whether a human stealth player keeps the quiet approach as often as the pilot does. That is for the playtest.

## Verified claims

- D-096 final probe (SS-runtime #108 `17ef51f`, legal seeds 1–40):
  - win rates 56/52/53% (competent/stealth/loud).
  - Before M-C, 93 of 120 stealth runs stay at `observed` or below. 0 of 120 loud runs do, and 104 reach `hunted`.
  - Win rate by Integrity at the start of the boss fight: 75–84 wins 49% (n=247), 85–94 67% (n=53), 95–104 70% (n=27), 105–114 83% (n=12).

## Assumed claims

- At 90 Integrity, quiet stealth runs win about 65%, which puts stealth near 62% overall, against loud's 53%. The probe confirms.
