# HUD, Controls, and Tutorial Contract

Status: CANONICAL  
Contract version: `hud-tutorial-001`

## Reference canvas and adaptation

HUD authoring uses an 844 × 390-point landscape reference canvas after safe-area insets. Runtime scales uniformly by:

`scale = min(safeWidth / 844, safeHeight / 390)`

The scaled canvas is centered inside the safe rectangle. HUD scale setting multiplies non-control HUD by 1.0, 1.15, or 1.30; controls remain at least their baseline size. No gameplay state depends on points, scale, safe area, or handedness.

## Default right-handed layout

| Element | Reference anchor | Size |
|---|---|---|
| Movement stick | (104, 286) | 144 × 144 |
| Dodge button | (760, 286) | 88 × 88 |
| Pause | (806, 36) | 44 × 44 |
| Player Integrity | (24, 24), top-left | 220 × 20 |
| Exposure bar | (422, 26), top-center | 300 × 24 |
| Detection label | (422, 54), top-center | 180 × 24 |
| Combat objective | (24, 58), top-left | 300 × 48 |
| Camera objective | (24, 110), top-left | 180 × 28 |
| Boss Integrity | (422, 82), top-center | 360 × 24 |
| Extraction countdown | (422, 134), center | 220 × 56 |
| Upgrade badge | (760, 88), top-right | 64 × 64 |
| Context tutorial | (422, 318), bottom-center | max 520 × 56 |

Left-handed mode reflects movement stick and Dodge across x=422. Pause and informational HUD do not move. Every interactive rectangle is at least 44 × 44 points and remains inside the safe canvas.

## Visibility rules

- Player Integrity: always during gameplay.
- Exposure and Detection State: appear before first possible Camera contact and remain.
- Combat objective: always, using current graph node.
- Camera counter: hidden until first Camera damage, unless pinned in settings.
- Boss bar: only while boss active or during a phase-transition cue.
- Extraction countdown: only while armed and Player is inside; locked contact instead shows prerequisite.
- Upgrade badge: after selection.
- Integrity notches: exactly three, adjacent to current Camera target while damageable and in range; persist for 90 ticks after a Camera hit.

## Exact copy

| Event/state | Primary copy |
|---|---|
| First movement | `MOVE` |
| First visible field | `CAMERA FIELDS RAISE EXPOSURE` |
| First contact | `BREAK LINE OF SIGHT TO RECOVER` |
| First damageable Camera | `CAMERAS: 3 HITS • DESTRUCTION ADDS EXPOSURE` |
| Camera destruction | `+100 TAMPER` |
| M-A complete | `CHOOSE ONE COUNTERMEASURE` |
| M-C activation | `LOCKDOWN` |
| Locked Extraction contact | `DEFEAT THE CURRENT AUTHORITY` |
| Extraction armed | `PHOENIX STEPS OPEN` |
| Network Blackout | `NETWORK BLACKOUT 8/8` |

Copy is uppercase in visual presentation but exposed to VoiceOver in sentence case. Captions use the same semantic message without requiring uppercase pronunciation.

## Tutorial state machine

`T0_MOVE → T1_FIELD → T2_CONTACT → T3_CAMERA_DAMAGE → T4_UPGRADE → COMPLETE`

- T0 completes after cumulative Player displacement reaches 96 units.
- T1 becomes eligible on first selected Camera entering the inner viewport; completes after 60 presented ticks.
- T2 activates on first Camera contact; completes when contact becomes zero for 30 consecutive ticks.
- T3 activates when a damageable Camera first becomes a valid target; completes on its first valid impact or after 300 eligible ticks.
- T4 activates on M-A completion and completes on accepted upgrade choice.
- Only one tutorial card is visible. Higher safety messages (lethal warning, Lockdown, Extraction) temporarily replace it without changing tutorial progress.
- Each card has a maximum visual duration of 300 ticks, but its completion condition remains authoritative where specified.
- Tutorial completion is a local setting. A replay receipt records whether tutorials were enabled, but tutorial state is excluded from gameplay digest.

## Upgrade selection

Use a protected SwiftUI overlay with three equal cards in canonical order. Each card contains name, one-line role, non-color icon, exact numeric summary, and VoiceOver label. Gameplay commands stop while open as defined by `upgrades.md`. No default choice, timeout, swipe-only action, or randomized order is permitted.

## Exposure presentation

The bar is a 0–1000 projection with threshold notches at 200, 450, 700, and 1000. State uses label, icon shape, bar pattern, and color:

| State | Shape/pattern |
|---|---|
| Hidden | open eye/slack dotted fill |
| Observed | half eye/diagonal fill |
| Tracked | bracket eye/cross fill |
| Hunted | boxed eye/dense chevron |
| Lockdown | sealed eye/solid segmented fill |

Transitions use a 180-ms outline emphasis. Reduced Motion uses an immediate swap. Reduced Flash forbids full-screen luminance changes.

## Extraction display

Render `ceil(remainingTicks / 60)` as 5, 4, 3, 2, 1. The ring uses exact tick progress. Leaving the zone immediately hides the active ring and shows `RESET` for 45 presented ticks. Presentation does not drive completion.

## Acceptance vectors

| ID | Scenario | Expected |
|---|---|---|
| UI-001 | 844 × 390 safe canvas | anchors match table |
| UI-002 | handedness toggle | only stick/Dodge reflect |
| UI-003 | HUD scale 130% on smallest target | no clipping; controls remain usable |
| UI-004 | Camera target damaged | three notches show authoritative state |
| UI-005 | tutorial plus Lockdown | Lockdown preempts; tutorial progress preserved |
| UI-006 | leave Extraction at one tick remaining | resets to 300; RESET cue |
| UI-007 | VoiceOver upgrade selection | three ordered complete labels |
| UI-008 | grayscale/reduced presentation | all critical states remain distinct |
