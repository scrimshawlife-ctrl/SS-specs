# Run Shell — Terminal Surface

Status: PROPOSED
Feature: SS-001
Contract version: `run-shell-001` (proposed)

> **This document is not canonical.** It records behaviour already shipped in
> the runtime so the specification stops trailing the implementation, and it
> isolates the decisions still owed. `intent/run-shell-surfaces.md` is merged but
> still `Status: draft`; a human accepts that intent, then this document, before
> either binds. Sections marked **OPEN** are unanswered and MUST NOT be
> implemented from this file.

## 1. Why this exists

`FR-004` requires that a restart restore the complete initial authoritative
state for the selected Replay Identity, and gate `B003` verifies it. Until
recently the only way to reach that restart was a touch anywhere once the run
stopped, and no surface told the player the run had ended.

That blocks `T903`/`T904`. Playtest evidence asks humans to play runs and
report; a tester who cannot tell that a run ended, cannot tell whether it was
won, and restarts by reaching for a screenshot cannot produce clean evidence.

## 2. Scope

This document covers the **terminal surface only** — what the game presents once
a run is over. The launch and title half of the run shell is **OPEN** and is not
specified here. See section 7.

The terminal surface is not a HUD element. `hud-tutorial-001` owns the layout
table for HUD present *during play*; a surface shown after the run has ended
does not belong in it, on the same footing as the upgrade selection overlay.

## 3. Terminal outcomes

A run is over when its outcome is terminal. `RunOutcome` distinguishes:

| Outcome | Terminal | Meaning |
|---|---|---|
| `playing` | no | run in progress |
| `upgradeSelectionPending` | **no** | paused for a choice; the run continues |
| `success` | yes | Extraction held |
| `failure` | yes | Player Integrity exhausted |
| `invalid` | yes | run cannot be scored |

`upgradeSelectionPending` being non-terminal is load-bearing rather than
incidental. Treating "not playing" as "finished" made the first touch at the
upgrade gate restart the run, with the card-selection path unreachable behind
it. Any consumer MUST test for a terminal outcome, never for the absence of
`playing`.

## 4. Presentation

While the outcome is terminal:

- A single centred panel is presented over a scrim.
- The panel states the outcome, using the copy in section 5.
- The panel carries exactly one control, which restarts the run.
- No tutorial card is presented. A finished run has nothing left to teach.
- The panel is centred on the safe rectangle and is unaffected by handedness,
  which reflects only the movement stick and Dodge.
- The control is at least 44 × 44 points, consistent with every other
  interactive rectangle.

Presentation only. No simulation tick occurs while the run is terminal, the
state digest is unaffected, and no authoritative field is introduced.

## 5. Exact copy

| Outcome | Primary copy |
|---|---|
| `success` | `RUN COMPLETE` |
| `failure` | `PLAYER DOWN` |
| `invalid` | `RUN INVALID` |
| restart control | `RESTART` **(OPEN — see 7.1)** |

`RUN COMPLETE` and `PLAYER DOWN` are the words `audio-haptics-001` already uses
for these events in its accessibility captions ("Run complete", "Player down"),
uppercased per the `hud-tutorial-001` presentation rule. They are reused rather
than authored, so caption and panel cannot drift apart.

## 6. Restart

Restart is reachable **only** from the control on this panel. A touch elsewhere
on a terminal screen does nothing.

This is a deliberate narrowing. Restart-on-any-touch always worked, but it fired
without the player having been told the run was over, and a tester reaching for
a screenshot would trigger it. The trade is that a broken control would strand
the player, so the control's geometry is required to satisfy section 4 at every
supported safe rectangle.

Restart behaviour itself is unchanged and continues to satisfy `FR-004` and
gate `B003`.

## 7. OPEN — decisions still owed

Nothing in this section may be implemented from this document.

### 7.1 Restart control copy

`RESTART` borrows `FR-004`'s own noun, but no contract authorises it. It is the
only string on this surface that is not already specified elsewhere, and it
needs a row in an owning contract or a replacement.

### 7.2 What else, if anything, the surface reports

The run receipt carries seed, elapsed ticks, damage dealt and taken, exposure
peak, cameras destroyed, Network Blackout, boss phases, and more. The surface
currently reports none of it. Whether any is player-facing — as opposed to
evidence-only — is undecided. Testers need the seed for `T903`/`T904` evidence;
a player arguably does not.

### 7.3 Whether a launch or title surface exists at all

The app presents a running simulation on launch. Whether it should instead
present a title surface, and what that surface offers, is undecided and is the
substantive open question in `intent/run-shell-surfaces.md`. The terminal half
was specified first because `FR-004` already required restart; the launch half
has no such anchor.

### 7.4 Whether Settings is reachable outside a run

`SettingsView` is currently reached only from Pause, during a run. If a launch
surface exists it is the natural second entry point; if it does not, settings
remain unreachable before the first run begins.

### 7.5 The lethal-warning copy row

Unrelated to this surface but adjacent, and still outstanding:
`hud-tutorial-001` names a lethal warning as one of three higher safety messages
that preempt the tutorial card, and `audio-haptics-001` and
`camera-destruction.md` both give it audio priority 1 — but no contract gives it
HUD copy and the `## Exact copy` table has no row for it. The Lockdown and
Extraction preemptors are implemented; this one cannot be until it has a string.

## 8. Acceptance vectors

Proposed, pending acceptance of this document.

| ID | Scenario | Expected |
|---|---|---|
| RS-001 | run reaches `success` | panel presents `RUN COMPLETE` and one control |
| RS-002 | run reaches `failure` | panel presents `PLAYER DOWN` and one control |
| RS-003 | touch away from the control on a terminal screen | nothing happens; run stays terminal |
| RS-004 | touch on the control | run restarts and satisfies `B003` |
| RS-005 | upgrade selection open | no terminal panel; the touch selects a card |
| RS-006 | terminal screen at the smallest supported safe rectangle | panel and control fully on screen; control at least 44 × 44 |
| RS-007 | tutorial card active when the run ends | card is not presented |
