# Intent: retarget the run length to what the content supports

**Author:** prabu-openclaw  
**Date:** 2026-09-28  
**Status:** accepted (owner, 2026-09-28; SS-specs #46)  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

The constitution, D-002, and G-005 target an 8–12 minute competent run. The T305 scripted probes measured 3:43 for a perfect-route run, and the content bounds the kill time alone at about 2:20. G-005 cannot pass without either more content, which Article V restricts, or a different target. The pacing table also names segments with no event boundaries, gives Extraction two minutes against a 5-second rule, and B-002/B-016 never define "supported architecture".

## Proposed outcome

- **Run length:** a competent run of about 5–8 minutes, with segment targets and event boundaries the runtime can measure.
- **Extraction:** its budget matches its rule.
- **Architecture:** "supported architecture" has one meaning.

## Affected users/systems

- **Player:** none directly; content is unchanged.
- **Specification:** constitution Article I (to 1.2.0), D-002 (superseded by D-079), D-080, arena.md § 5, acceptance G-005/B-002/B-016, README.
- **Runtime:** none.

## Constraints/non-goals

- No content, ruleset, or golden change.
- Playtests (T903/T904) remain the authority on the final number.

## Open questions

- Owner: retarget, as proposed, or keep 8–12 and tune existing content up under Article V?

## Verified claims

- The T305 figures are in `docs/review/T305`: a 3:43 median, a 3:02–6:40 range, and 2800 total enemy integrity at 20 damage per second.
- Extraction holds for `countdownTicks: 300` in `civic-seam-arena-001`.

## Assumed claims

- A human competent player after onboarding will land inside 5–8 minutes. This is assumed until the playtests.
