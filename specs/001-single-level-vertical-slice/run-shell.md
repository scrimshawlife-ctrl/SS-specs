# Run Shell — Title and Terminal Surfaces

Status: PROPOSED
Feature: SS-001
Contract version: `run-shell-001` (proposed)

> **This document is not canonical.** It records behaviour already shipped in
> the runtime so the specification stops trailing the implementation, and it
> isolates the decisions still owed. `intent/run-shell-surfaces.md` is `accepted`
> and authorizes specify; this document remains `PROPOSED` until a human accepts
> it. Sections marked **OPEN** are unanswered and MUST NOT be implemented from
> this file.

## 1. Why this exists

`FR-004` requires that a restart restore the complete initial authoritative
state for the selected Replay Identity, and gate `B003` verifies it. Until
recently the only way to reach that restart was a touch anywhere once the run
stopped, and no surface told the player the run had ended.

That blocks `T903`/`T904`. Playtest evidence asks humans to play runs and
report; a tester who cannot tell that a run ended, cannot tell whether it was
won, and restarts by reaching for a screenshot cannot produce clean evidence.

## 2. Scope

This document covers both shell surfaces: the **title surface** the app presents
on launch, and the **terminal surface** it presents once a run is over.

Neither shell surface is a HUD element. `hud-tutorial-001` owns the layout
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
- The panel carries two controls: Restart, the primary control, and Share (§ 11).
- Under the outcome it shows the run card (§ 11).
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
| title, start control | `START` **(OPEN — see 7.1)** |
| title, settings control | `SETTINGS` **(OPEN — see 7.1)** |
| title, daily label | `DAILY RUN · <YYYY-MM-DD>` (UTC date of the seed) |
| share control | `SHARE` |

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

### 7.1 Shell control copy

`RESTART`, `START`, and `SETTINGS` are the only strings on either shell surface
that no contract authorises. `RESTART` borrows `FR-004`'s own noun; the other two
are the plainest available words for what they do. All three need rows in an
owning contract, or replacements.

### 7.2 RESOLVED (D-081) — What else, if anything, the surface reports

The run receipt carries seed, elapsed ticks, damage dealt and taken, exposure
peak, cameras destroyed, Network Blackout, boss phases, and more. The surface
currently reports none of it. Whether any is player-facing — as opposed to
evidence-only — is undecided. Testers need the seed for `T903`/`T904` evidence;
a player arguably does not.

Resolved by D-081: the terminal surface shows the run card in § 11. The seed
itself stays evidence-only; the player sees the date it came from.

### 7.3 RESOLVED — a title surface exists

Decided 2026-09-06. See section 8.

The deciding argument was not presentation. `SettingsView` was reachable only
from Pause, during a run, so a player could not set handedness before playing.
A left-handed `T903`/`T904` participant would have had to begin a run, pause,
change handedness and restart — contaminating the onboarding-comprehension data
those playtests exist to collect. A launch surface is the natural place to fix
that, and section 7.4 is resolved with it.

### 7.4 RESOLVED — Settings is reachable from the title surface

Decided 2026-09-06. See section 8. Pause remains the in-run entry point; the
title surface is the second, and the only one available before a first run.

### 7.5 The lethal-warning copy row

Unrelated to this surface but adjacent, and still outstanding:
`hud-tutorial-001` names a lethal warning as one of three higher safety messages
that preempt the tutorial card, and `audio-haptics-001` and
`camera-destruction.md` both give it audio priority 1 — but no contract gives it
HUD copy and the `## Exact copy` table has no row for it. The Lockdown and
Extraction preemptors are implemented; this one cannot be until it has a string.

## 8. Title surface

The app presents the title surface on launch. No simulation tick occurs while it
is presented, on the same principle as `PC-008` for pause.

It offers exactly two actions:

| Control | Effect |
|---|---|
| Start | begins today's Daily Run (§ 10) |
| Settings | presents the existing settings surface |

Nothing else. No run history screen, no statistics, no continue, no difficulty
choice, no meta-progression of any kind — those are the expansion this level
defers. The one stored run the app keeps is today's best, which exists only to
drive the ghost (§ 10) and is never listed. The title shows the Daily Run label
from § 5 under the wordmark.

- The wordmark identifies the product.
- Controls are at least 44 x 44 points, consistent with every interactive
  rectangle, and horizontally centred so neither handedness is favoured.
- The surface is presentation only: it introduces no authoritative state and
  cannot affect the state digest or a run receipt.
- Settings reached from the title surface governs the run that follows it,
  through the same `PresentationSettings` path Pause already uses. `ER-007`
  continues to hold — a settings change moves nothing but the declared
  presentation metadata.

### 8.1 Returning to the title

A run reaching a terminal outcome presents the terminal surface (section 4),
**not** the title surface. Restart from there begins a new run directly, as
specified in section 6.

Whether the terminal surface should additionally offer a route back to the title
is **OPEN**. It is not required by anything, and adding a second control to that
panel trades against the deliberate narrowness of section 6.

## 10. Daily Run and ghost (D-081)

### 10.1 The daily seed

Every run started from the title uses the seed for the current UTC calendar
date, so every player sees the same Camera layout that day.

```text
dayKey    = year * 10000 + month * 100 + day          (UTC, as UInt64)
candidate = SplitMix64.mix(dayKey ^ 0x5353_4441_494C_5900 ^ salt),  salt = 0, 1, 2, …
seed      = the first candidate whose camera placement selects and passes its runtime asserts
```

The date is read once, when Start is pressed. Restart keeps the run's seed, so a
run started before midnight UTC restarts on the same layout. The seed is an input
to the Replay Identity like any other: the simulation never reads a clock.

### 10.2 The ghost

The ghost is the player's best successful run on the same seed and the same
Replay Identity. Best means success in the fewest ticks. It is replayed from
its recorded commands, one tick for each tick of the live run, and drawn as a
translucent Player silhouette.

- **Presentation only.** It has no collision, damage, audio, haptics, targeting,
  or effect on any authoritative field, digest, or receipt.
- It stops at its own terminal tick and fades out.
- It is discarded when the Replay Identity (ruleset, content, arena, replay
  schema) differs from the live run's, or when its replay fails to reproduce
  its stored digest.
- It is on by default and can be turned off in Settings (`PresentationSettings`).
  `ER-007` holds.

### 10.3 Daily city flavour (D-099)

Presentation only. Each Daily Run takes a look from its UTC day key, through
the same SplitMix64 mix as § 10.1 (salt 0), one field per byte of the mix:

| Field | Values |
|---|---|
| Grade (world colour grade) | `CLEAR`, `OVERCAST`, `GOLDEN HOUR`, `NIGHT SHIFT` (bits 0–7, mod 4) |
| Fog density | 80%, 100%, 120% of authored opacity (bits 8–15, mod 3) |
| Headline | one of 12 authored lines (bits 16–23, mod 12) |

- **Headlines:**
  1. `FOG ADVISORY IN EFFECT`
  2. `NEW CAMERAS APPROVED OVERNIGHT`
  3. `CIVIC SEAM REOPENS AFTER REVIEW`
  4. `TEMPORARY ORDER EXTENDED`
  5. `QUIET HOURS ENFORCED`
  6. `TRANSIT PATROL DOUBLED`
  7. `INDEPENDENT REVIEW SCHEDULED`
  8. `PUBLIC SAFETY NOTICE POSTED`
  9. `NETWORK MAINTENANCE TONIGHT`
  10. `PHOENIX STEPS LIGHTS RESTORED`
  11. `CURFEW RUMOURS DENIED`
  12. `OBSERVATION WEEK BEGINS`

  None is a real organization, place outside the level, or person.
- **Where it shows:** the title shows the headline under the Daily Run label,
  and the grade and fog apply to the world layer for every run that day.
- **Limits:**
  - fog density never exceeds what § 8b and the readability floor allow
    (fog still thins in a fight);
  - `NIGHT SHIFT` darkens the ground, never actors, telegraphs, or Camera
    fields, and actor outlines (§ 8b) keep contrast;
  - nothing here enters the digest or the receipt.

## 11. Run card and Share (D-081)

Under the outcome, the terminal surface shows:

| Row | Source |
|---|---|
| date | the Daily Run's UTC date |
| time | elapsed ticks as `m:ss` |
| cameras | `destroyed / 8`, plus `NETWORK BLACKOUT` when all eight fell |
| peak detection | the highest Detection State reached |
| ghost | success only: `NEW BEST` when this run replaced the stored best, otherwise the time behind it as `+m:ss`. Omitted on failure, and when no best exists |

Share opens the system share sheet with a plain-text summary of the same rows
and the game's name. It shares nothing else: no seed, no receipt, no identifier.

## 12. Medals (D-095)

One level needs more than one way to win. A successful run can earn any of
five medals. Each is derived from the run's own authoritative event stream and
terminal state, so a replay of the run earns the same medals. None is
authoritative state, and none changes rules, the digest, or the receipt.

| Medal | Earned when the run succeeds and |
|---|---|
| `GHOST` | the Detection State never reached `tracked` before M-C's first `waveStarted` |
| `SHADOW` | no Transit Patrol member was alerted before M-A's first `waveStarted` (slipped past) |
| `BLACKOUT` | Network Blackout (all eight Cameras destroyed) |
| `SURGICAL` | the Player ends with at least half of `player.integrity` |
| `SWIFT` | elapsed time is under 5:30 (19,800 ticks) |

- **On the run card:** a `MEDALS` row lists the medals earned, each marked
  `NEW` if this is the first time today. A failed run shows no medal row, and neither does a successful run that
  earned no medal.
- **On the title:** under the Daily Run label, the five medals for today's
  seed show as earned or not yet earned, by shape (filled or outlined) as well
  as colour. This is today's goal list, and the only run history shown.
- **Storage:** medals earned today are stored locally with the day's best run
  (§ 10.2), keyed by seed and Replay Identity. A new day starts empty.
- **Share** (§ 11) appends the earned medal names.
- `GHOST` and `BLACKOUT` pull in opposite directions by design: stealth and
  loud each have a medal of their own.

## 9. Acceptance vectors

Proposed, pending acceptance of this document.

| ID | Scenario | Expected |
|---|---|---|
| RS-001 | run reaches `success` | panel presents `RUN COMPLETE`, the run card, Restart, and Share |
| RS-002 | run reaches `failure` | panel presents `PLAYER DOWN`, the run card, Restart, and Share |
| RS-003 | touch away from the control on a terminal screen | nothing happens; run stays terminal |
| RS-004 | touch on the control | run restarts and satisfies `B003` |
| RS-005 | upgrade selection open | no terminal panel; the touch selects a card |
| RS-006 | terminal screen at the smallest supported safe rectangle | panel and control fully on screen; control at least 44 × 44 |
| RS-007 | tutorial card active when the run ends | card is not presented |
| RS-008 | cold launch | title surface presented; no simulation tick occurs |
| RS-009 | Start | a run begins from the authored initial state on the § 10.1 daily seed |
| RS-010 | Settings from the title, handedness changed, then Start | the run honours the changed handedness |
| RS-011 | Settings from the title | digest and receipt unchanged but for declared presentation metadata (`ER-007`) |
| RS-012 | run reaches a terminal outcome | terminal surface presented, not the title surface |
| RS-013 | the same UTC date on two devices | the same seed and Camera layout |
| RS-014 | a ghost is present | the live digest and receipt are identical to a run without the ghost |
| RS-015 | a stored best from a different Replay Identity | no ghost |
| RS-016 | Share | the summary contains the § 11 rows and no seed or identifier |
| RS-017 | run ends in failure with a stored best | no ghost row (a failed run is never "faster") |
| RS-018 | a success that stayed below `tracked` until M-C | `GHOST` earned |
| RS-019 | a success where a patrol member was alerted before M-A | no `SHADOW` |
| RS-020 | a success at 74 of 150 Integrity / at 75 | no `SURGICAL` / `SURGICAL` |
| RS-021 | a failed run that would otherwise qualify | no medals |
| RS-022 | a replay of a medal run | the same medals |
| RS-023 | a second run today earns `GHOST` again | `GHOST` shown, not marked `NEW` |
