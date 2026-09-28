# Intent: close the P0 environment definitions

**Author:** prabu-openclaw  
**Date:** 2026-09-28  
**Status:** accepted  
**Next stage:** `spec.md`

`draft` until the owner accepts. `accepted` authorizes specify. `superseded` replaces this intent. Do not list Grok Bot skills or CI policy here; bind those from `AGENTS.md` in `spec.md` by pointer only.

## Problem

The T800 review named three P0 gaps with no asset ID: the trolley wires, the basic rooftop kit, and the Captain Camera housing. Art cannot be produced for an ID that does not exist, and the runtime has nowhere to draw it. Meanwhile a firing Captain Camera emitter is drawn as a standard Camera in its critical state, which tells the player it is a damaged Camera they can finish off. It cannot be damaged.

## Proposed outcome

- **Captain Camera:** two declared IDs (idle and active), drawn at every emitter.
- **Trolley wires:** delivered without breaking the decoration overlap rules.
- **Rooftop kit:** resolved against the art that already exists.

## Affected users/systems

- **Player:** sees which emitter owns the field, and is no longer invited to shoot something indestructible.
- **Specification:** `presentation-assets-003`, `asset-catalog-001`, `arena-layout.md`, D-078, and the T507/T800 rows.
- **Runtime:** adopt `-003`, draw the Captain Camera housings, and drop the standard critical sprite at the emitter.

## Constraints/non-goals

- No arena, geometry, or digest change.
- No new decoration placements.

## Open questions

- None.

## Verified claims

- `PresentationSnapshot` builds the firing emitter as a `CameraSprite` in `.critical` with the standard critical clip.
- The rail strip's railbed occupies rows 32–95 of 512x128, so the rows above it are free for wires.
- The delivered solids' roofs show HVAC units, a water tank, chimneys, and vents.

## Assumed claims

- None.
