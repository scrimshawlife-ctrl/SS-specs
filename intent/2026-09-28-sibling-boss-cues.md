# Intent — Boss telegraph cues from a sibling title

**Author:** prabu-openclaw  
**Date:** 2026-09-28  
**Status:** accepted  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

D-075 left three boss telegraphs silent: `safetyRationale`, `narrowTailoring`, and `independentReview`. The frozen legacy library has no enemy attack sounds, and approximate substitution is closed.

## Proposed outcome

Each of the three has a sound whose role in its source game is the same meaning. It is recorded with commit, digest, and licence basis. After this, no audio ID stays planned.

## Affected users/systems

- **Player:** every boss telegraph is audible.
- **Specification:** `asset-catalog-001` (3 records), `legacy-admission.md`, D-077.
- **Runtime:** three AAC files and a re-pin.

## Constraints/non-goals

- Sound effects only. Eleven Music carries a platform condition and is excluded.
- No change to AudioProjector priority, coalescence, captions, or haptics.
- No new source class for visuals.

## Open questions

- The Hexwire audio rights ledger still needs plan-on-generation-date evidence, the same gap as the legacy ElevenLabs cues. Evidence is owner work (Hexwire `OWNER_EVIDENCE_PACKET.md`).

## Verified claims

- Hexwire plays `mech_autocannon` for the boss mech's attack and `agi_attack_burst` for the AGI boss's attack (`Game/SFXManager.swift`). It plays `trace_warning` when the player is being traced (`UI/PacketRouterMiniGame.swift`).
- The digests of all three files at Hexwire `19e12b6` are recorded on their catalog records.
- Hexwire's licence determination rates paid-plan ElevenLabs Sound Effects output as cleared for commercial use, owned, with no attribution required.

## Assumed claims

- None.
