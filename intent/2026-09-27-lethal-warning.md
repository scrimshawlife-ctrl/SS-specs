# Intent — Lethal warning

**Author:** prabu  
**Date:** 2026-09-27  
**Status:** accepted  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

The specification names a lethal warning in four places and never says when it happens. It is audio priority 1 (`audio-haptics.md`), a Captain-camera priority (`camera-destruction.md`), a magenta-red chevron carrier (`visual-assets.md`), and a safety message that preempts tutorial cards (`hud-tutorial.md`). It has no trigger, no audio ID, and no HUD copy, so SS-runtime correctly shows nothing (SS-specs#31). Article IV requires that a player can understand why damage and failure occurred; the one warning meant to say "this can kill you" is the part that does not exist.

## Proposed outcome

- A player about to die is told so before it happens, through a non-colour carrier, audio, a haptic, and a caption.
- The trigger is exact, deterministic, and testable from authoritative state alone.
- It does not fire so often that it becomes noise, and it never contradicts what the telegraphs show.

## Affected users/systems

- Player: a new warning state in the HUD, audio, and haptics.
- Specification: `hud-tutorial.md` (copy row), `audio-haptics.md` (audio ID), `presentation-assets` (declared ID), and possibly `event-catalog` (only under option 3 below).
- Runtime: presentation layer only under options 1 and 2.

## Constraints/non-goals

- One level; no new meter, stat, or difficulty setting (Article V).
- The warning MUST NOT change damage, timing, or any rule; it only reports state.
- Colour is never its sole carrier (F-005); reduced-flash compliant (D-009).
- Not a low-health regeneration or a second chance.

## Open questions

The trigger. Three candidates, for the owner to choose:

1. **Integrity threshold.** Warn while Player Integrity ≤ *N* (for example 25). Simple, cheap, conventional. It says "you are fragile", not what will kill you, and in a long boss fight it may stay on for a long time.
2. **Lethal threat.** Warn while any active hostile telegraph that contains the Player would deal damage ≥ current Integrity, or while summed contact damage would exhaust Integrity within *T* ticks. It names the actual killer, which is what Article IV asks for, and it stays silent when the Player is merely low but safe. It is more work: each telegraph's damage must be available to presentation, and all of them are already authored integers.
3. **Authoritative event.** Either rule above, emitted by the simulation as a new `lethalWarning` event. Only needed if receipts or replays must record the warning. It changes every golden event stream, so it carries a version decision.

**Recommendation (assumed, owner decides):** option 2, derived in presentation, with option 1's threshold as a floor if playtests show players want a standing cue.

**Owner decision (2026-09-27):** accepted, option 2. A lethal threat triggers the lethal warning.

Also open: the HUD copy (one exact string, like the other safety messages), the audio ID and haptic for the priority-1 slot, and whether the warning outranks the Lockdown and Extraction safety messages when they coincide (the audio priority says yes).

## Verified claims

- Spawn Integrity is 100 and clamps to 0…100 (`player-controller.md`).
- Contact damage is continuous with no invulnerability window, capped to the three highest simultaneous threat rates (`player-controller.md`); the highest three are 16 (Moderate), 14 (Daemon), and 12 (Correlator), so at most 42 per second.
- The largest single hits are Safety Rationale 18 (`bosses.md`) and the Daemon's query resolution 14; Narrow Tailoring fires three 9-damage projectiles.
- Presentation already derives HUD state from authoritative state without events (Detection State, Camera Integrity notches), so options 1 and 2 need no event.
- No event, audio ID, or HUD row for the lethal warning exists in any artifact (SS-specs#31).

## Assumed claims

- A threshold near 25 would read as "one heavy hit from death" given the 18-damage maximum hit. Assumed; tune in playtest.
- Option 2's contact-damage horizon *T* should be about one second. Assumed.
