# Intent

**Author:** prabu-openclaw
**Date:** 2026-09-05
**Status:** draft
**Next stage:** `spec.md`

## Problem

The game has no way in and no way out.

`SSRuntimeApp` presents `GameContainerView`, which presents a `SpriteView` whose
scene is already running. Launching the app drops the player into a live
simulation mid-stride: no title, no start, no seed shown, no way to decline.

The exit is worse, because it is specified and unreachable. **FR-004** requires
that "A restart MUST restore the complete initial authoritative state for the
selected Replay Identity", the runtime implements it, and gate B003 verifies it.
But the only surface that reaches it is `GameScene.touchesBegan`, which restarts
when the player taps anywhere once `outcome != .playing`. There is no terminal
panel. When a run ends the screen simply stops responding to the stick, shows no
statement of outcome, and any touch silently starts a new run.

This matters now because every other blocker has cleared. The asset inventory is
complete, audio and music are wired, the build is green, and the remaining
acceptance work is **T903/T904 playtest evidence** — which asks humans to play
runs and report. A tester who cannot tell that a run ended, cannot tell whether
it was won or lost, and restarts by accident cannot produce clean evidence.

Nothing in `specs/` describes a title screen, main menu, launch screen, splash,
or terminal surface. This is a genuine specification gap, not an implementation
oversight.

## Update — 2026-09-05, after merge

The **terminal half has since shipped** in the runtime (SS-runtime #65), at the
user's direction and ahead of this intent's acceptance. That changes this
document's Problem section in one respect: a finished run now states its outcome
and restarts only from a named control, so the "no way out" half is addressed in
code even though it was never specified.

`specs/001-single-level-vertical-slice/run-shell.md` records that shipped
behaviour as `PROPOSED`, so the specification stops trailing the implementation.
It deliberately specifies nothing about launch or title surfaces, which remain
the substantive open question below.

Building it also surfaced a defect this intent did not anticipate: because
completing M-A sets `outcome = .upgradeSelectionPending`, the touch handler's
"not playing means finished" test made the first tap at the upgrade gate restart
the whole run. Every hand-played run would have ended at M-A. That is now fixed,
and the terminal/non-terminal distinction is recorded in the proposed spec
because it is a contract consumers must not get wrong.

## Proposed outcome

- Launching the app presents a surface that does not simulate, from which the
  player chooses to begin a run.
- A run that reaches a terminal outcome says so, names the outcome, and does not
  restart except by a deliberate act.
- Restart from that surface satisfies FR-004 exactly as the existing path does —
  same restored state, same gate.
- A tester can complete a T903/T904 session without ambiguity about when one run
  ended and the next began.
- Presentation only: no simulation tick occurs while a shell surface is
  presented, and the state digest and receipt are unchanged by any of it.

## Affected users/systems

- **Player:** gains a start and an end.
- **Operator/tester:** can run T903/T904 sessions with unambiguous run boundaries.
- **Specification artifacts:** a new spec document; `hud-tutorial.md` may need a
  cross-reference, since a shell surface is not a HUD element and should not
  enter its layout table.
- **Runtime:** `SSRuntimeApp`, `GameContainerView`, `GameScene.touchesBegan`
  (whose incidental restart-on-any-touch is superseded).
- **CI:** no change expected; B003 continues to cover restart.

## Constraints/non-goals

- **One-level scope discipline holds.** This adds no city, campaign system,
  procedural map, content framework, inventory, character, or meta-progression.
  It is the shell around the existing single level, and nothing behind it.
- **No meta-progression of any kind.** No unlocks, no persistent profile, no
  run history, no statistics surface. A leaderboard or a "best run" is exactly
  the expansion this defers.
- **No new gameplay state.** Shell surfaces read the existing outcome and
  Replay Identity; they introduce no authoritative field.
- **Replay identity is untouched.** Nothing here may enter the state digest.
- **PC-008 already governs the pause case** — a paused run creates no simulation
  ticks — and the same rule should hold for any shell surface.
- Not a settings surface. `SettingsView` exists and is reached from Pause.
- Not a tutorial. `hud-tutorial-001` owns first-run teaching, and its T0 card
  already reads `MOVE`.

## Open questions

Do not treat any of these as decided.

- Does launch go to a title surface, or straight to a run with only the terminal
  surface added? The second is a smaller change and may be sufficient for
  T903/T904.
- What exactly does a terminal surface state? The runtime distinguishes
  `success` and `failure`, and receipts carry more (`outcome`, phases reached,
  cameras destroyed, Network Blackout). How much of that is product-visible
  rather than evidence-only?
- Is the seed or Replay Identity shown to the player? Testers need it for
  evidence; a player arguably does not.
- Does a title surface offer anything besides Start — Settings, for instance —
  given Settings is currently reachable only from Pause *during* a run?
- Is there an app icon and launch image requirement to specify alongside this?
  `visual-assets.md` does not currently name one.
- Should `NETWORK BLACKOUT 8/8`, already specified as an accolade, appear on the
  terminal surface or remain purely in-run?

## Verified claims

- No specification names a title screen, main menu, launch screen, splash, or
  terminal surface. `grep -rn -iE "title screen|main menu|launch screen|start
  screen|splash" specs/` returns nothing.
- FR-004 requires restart to restore complete initial authoritative state
  (`specs/001-single-level-vertical-slice/spec.md:59`).
- The runtime implements restart and gate B003 verifies it
  (`gateB003RestartRestoresInitialAuthoritativeState`).
- The only surface reaching restart is a bare touch once the run is not playing
  (`App/GameScene.swift:353`), and no terminal panel is drawn — `HUDRenderer`
  contains no outcome copy.
- The app boots directly into a running scene: `SSRuntimeApp` → `WindowGroup` →
  `GameContainerView` → `SpriteView(scene:)`.
- PC-008 already establishes that a presented surface can hold the simulation
  without ticking, and `GameContainerView` implements it for Pause.
- T903/T904 remain the outstanding acceptance gates.

## Assumed claims

- *Assumed:* a terminal surface is the higher-value half. Run boundaries are
  what T903/T904 evidence depends on; a title screen is polish by comparison.
- *Assumed:* accidental restart has already cost evidence. Any touch after a
  terminal outcome starts a fresh run, and a tester reaching for a screenshot
  would trigger it. Not yet observed in a real session — no human has played.
- *Assumed:* the shell is presentation and needs no authoritative state, on the
  evidence that outcome and Replay Identity are already projected.
