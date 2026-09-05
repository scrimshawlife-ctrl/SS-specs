# Intent — Legacy art and audio admission

Author: prabu
Date: 2026-09-04
Status: draft
Product: Surveillance Survivor (`scrimshawlife-ctrl/SS-specs`)

## Problem / why now

The runtime has no shippable art or audio at all, and the specification as
written offers no path to any.

[verified: `asset-catalog-001.json` carries all 52 required IDs as
`plannedOriginal` with no files; nothing in the catalog is `accepted`;
`SS-runtime` renders `SKShapeNode` primitives and plays nothing.]

`legacy-admission.md` LC-009 and LC-010 both say REJECT. LC-009 leaves a door
open — "An individual asset may return only through the new asset-record
process" — but names no such admission, so nothing has come back through it.
LC-010 names no return path at all.

Meanwhile the frozen legacy commit holds 389 sprites and 68 audio deliveries,
and a meaningful subset of them is **role-identical** to the reboot: a player
is still a player, a surveillance camera is still a surveillance camera, a
weapon projectile is still a weapon projectile.

Measured coverage of that subset against the current contracts:

| Contract surface | Required | Backed by frozen legacy | Coverage |
|---|---:|---:|---:|
| `clip-metadata-001` frame IDs | 408 | 112 | 27% |
| — player clips | 144 | 96 | 67% |
| — camera clips | 16 | 16 | **100%** |
| — five standard enemies | 100 | 0 | 0% |
| — Algorithmic Moderate | 148 | 0 | 0% |
| `presentation-assets-001` audio event IDs | 24 | 13 | 54% |
| `presentation-assets-001` visual asset IDs (HUD/control) | 28 | 0 | 0% |

[verified: mapping computed against `scrimshawlife-ctrl/Surveillance-Survivor@3b20d88`,
the commit this document already freezes.]

The two zero rows are not an oversight. They are a **casting** fact: the legacy
enemies are seven generic guards (`guard_clipboard_enforcer`,
`guard_radio_guy`, `guard_segway_sentinel`, …) and the legacy boss is a Shift
Manager. Neither is the canonical Civic Seam cast, which is exactly why LC-007
says REWRITE. Admitting them would put the wrong characters on screen.

So the honest shape of the decision is: admit where the role matches, keep
REJECT where the cast differs, and name the remainder as production work.

### Provenance note

`Zero-State-LLC/Surveillance-Survivor` also holds this art, and is where a
reader is likely to look for it. It is a **separate history**: the frozen
commit `3b20d88` does not exist there, and six San Francisco files have been
re-authored since the freeze.

[verified: `GET /repos/Zero-State-LLC/Surveillance-Survivor/commits/3b20d88…`
returns 422 "No commit found"; 11 of the 17 files recorded in
`SS-runtime/ArtSources/legacy-evidence/README.md` hash-match that repository
and 6 do not. All 17 hash-match `scrimshawlife-ctrl@3b20d88`.]

This document keeps `scrimshawlife-ctrl@3b20d88` as the sole admission source,
because it is the immutable evidence the specification already pins and the
only source whose hashes match the recorded evidence. Moving the pin to the
Zero State line would be a separate, deliberate change.

## Proposed outcome

Observable done (a stranger can check this without reading the chat):

- LC-009 and LC-010 state an explicit, bounded ADAPT set instead of a blanket
  REJECT, and name the conditions every admitted asset must satisfy.
- The legacy enemy cast, the legacy boss, non-San-Francisco packs, and literal
  landmark shorthand stay REJECTED, with the reason recorded.
- Every admitted asset carries an `asset-record-001` record whose `sha256`
  matches the frozen commit, so admission is verifiable and reversible.
- The specification states that partial clip coverage is legal and what the
  runtime must do for an unbacked frame, so a 27%-covered bundle is a defined
  state rather than an undefined one.
- The remaining production work is enumerated, not implied.

## Affected users / systems

- Users: players (the game currently renders untextured primitives and is silent).
- Systems: `legacy-admission.md`, `visual-assets.md`, `audio-haptics.md`;
  downstream `asset-catalog-001.json` and the runtime asset pipeline.

## Constraints

Product-true locks (do not reopen in implement):

- The canonical cast is unchanged. Admission may not rename, re-role, or
  substitute a legacy character for a Civic Seam one.
- `scrimshawlife-ctrl/Surveillance-Survivor@3b20d88` remains the only admission
  source; the commit stays immutable evidence.
- Collision, targeting, and Camera fields are never inferred from sprites.
- Admitted audio still owes the `audio-haptics-001` priority, coalescence, and
  caption obligations. Admission supplies a file, not an exemption.
- No second level, campaign framework, additional weapon, meta-progression, or
  online system.

Non-goals:

- Moving the legacy pin to the Zero State repository
- Admitting the legacy enemy or boss cast
- Producing the 28 HUD, control, telegraph, and objective asset IDs, which have
  no legacy counterpart and stay `projectOriginal`

## Open questions

- **Placeholder cast.** The seven legacy guards and the Shift Manager could
  stand in for the canonical cast at low fidelity (6 frames each rather than
  20). That trades Civic Seam identity for a screen that reads as a game
  sooner. Recommend no; flagging because it is a product call, not a technical
  one.
- Should `explore` and `terminal` music states map onto the admitted
  `music_san_francisco_run_loop` and a silence-with-caption state, or wait for
  original material? Three of six states have no admitted source.

## Claims

| Claim | Label |
|---|---|
| All 17 recorded evidence hashes match `scrimshawlife-ctrl@3b20d88` | `[verified: sha256 over the sparse checkout at that commit]` |
| The Zero State repository is a separate history missing `3b20d88` | `[verified: GitHub API 422 for that SHA; 6 of 17 files differ]` |
| Camera clip coverage is complete at 16/16 frames | `[verified: lpr_scan_loop, lpr_damaged, fx_camera_disabled, lpr_destroy_sequence, fx_camera_destroyed, lpr_destroyed cover every camera clip]` |
| `player_move` maps exactly, 24/24 | `[verified: player_walk_{up,right,down,left} × 6 frames]` |
| The enemy and boss gap is a casting difference, not a copying gap | `[verified: legacy roster is seven generic guards plus a Shift Manager; LC-007 already says REWRITE]` |

## Next

A human accepts this file (`Status: accepted`). Then the amendment lands in
`legacy-admission.md`, and the runtime produces the records and the pipeline.
