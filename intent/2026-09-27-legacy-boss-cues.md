# Intent — Legacy boss cues

**Author:** prabu-openclaw  
**Date:** 2026-09-27  
**Status:** accepted  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

The boss fight is the loudest moment of the run, yet it is the quietest part of
the cue set. `audio-haptics.md` names `boss_phase_<id>` and
`boss_telegraph_<attack>`, and the runtime emits both. But
`presentation-assets-001` registers neither, so no file can reach the bundle. A
phase change or a major telegraph gives only a haptic and a caption. The boss
beds are already legacy (legacy-admission.md § Boss phase beds), so the gap is
cues, not music.

## Proposed outcome

- The eight boss cue IDs are registered in `presentation-assets-002`, bumped
  from `-001` as D-060 requires.
- Each ID is either an admitted legacy sound, matched on exact gameplay meaning
  with its authoring intent quoted, or a planned original.
- No cue takes an approximate sound; approximate substitution stays closed.

## Affected users/systems

- Player: boss phase changes and Temporary Order become audible.
- Specification: `presentation-assets-002`, `versions.json`, and
  `asset-catalog-001` (8 records added, 72 `ownerContract` values moved to
  `-002`), plus `legacy-admission.md` and `decisions.md` (D-075).
- Runtime: adopts `presentation-assets-002` and re-pins. Both source files are
  already bundled (`lockdown_enter` and `camera_hit_02`), so no new audio is
  delivered.

## Constraints/non-goals

- No change to AudioProjector priority, coalescence, captions, or haptics.
- No change to authoritative state, events, or digests.
- No city identity: both sources are non-city `Runtime`/`Shared` assets.

## Open questions

- Should originals for the three unmatched telegraphs join the T602 art pass's
  audio sibling, or wait for a dedicated audio pass? Not decided here.

## Verified claims

- Frozen `AUDIO_ASSET_MANIFEST.json` delivery digests match the files at
  `3b20d88d`: `sfx_boss_activated` `c724600a…` and `sfx_camera_scan_sweep`
  `b156b001…`.
- The runtime emits `bossPhaseChanged` with `before: null, after: publicSafety`
  on the activation tick (Simulation.swift), so all four phase IDs fire.
- `AudioProjector` builds `boss_telegraph_\(attackId)` and
  `boss_phase_\(after)`.

## Assumed claims

- None.
