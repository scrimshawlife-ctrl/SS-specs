# Visual Production and Intake Plan

Status: BASELINE  
Feature: SS-001

## 1. Production sequence

1. Gameplay blockout
2. Collision and Camera truth
3. Grayscale readability
4. Silhouette kit
5. Palette and material plates
6. Minimum viable animations
7. VFX and state language
8. Environment modules
9. San Francisco identity pass
10. Dense-combat validation
11. Performance-floor device intake
12. Polish

Final art MUST NOT precede a playable grayscale blockout.

## 2. Approval stages

| Stage | Meaning |
|---|---|
| CONCEPT | Direction only; not runtime eligible |
| BLOCKOUT | Correct footprint and function |
| READABILITY_APPROVED | Passes silhouette and dense-frame tests |
| DELIVERY_CANDIDATE | Correct export, provenance, metadata |
| RUNTIME_INTEGRATED | Referenced by runtime catalog and exercised |
| DEVICE_ACCEPTED | Verified on target physical devices |
| REJECTED | Must not ship |

No asset may jump directly from CONCEPT to RUNTIME_INTEGRATED.

## 3. Source and delivery separation

```text
ArtSources/
  Characters/
  Environment/
  UI/
  VFX/
  Marketing/

RuntimeAssets/
  Atlases/
  Procedural/
  Manifests/
```

Source masters, prompts, layered files, alternates, and rejected exports stay out of the app bundle. Runtime delivery contains only approved assets referenced by the SS-001 catalog.

## 4. Provenance

Every asset requires:

- creator or generator;
- creation date;
- source inputs or prompt when applicable;
- model/tool and version when generated;
- license and commercial-use basis;
- edits and editor;
- source hash;
- delivery hash;
- approval record;
- prohibited-reference confirmation.

Unknown provenance is `NOT_COMPUTABLE` and blocks shipping.

## 5. Generation rules

Generated assets may accelerate exploration but do not bypass production contracts.

- Generate isolated subjects on simple backgrounds where possible.
- Do not ask the generator to bake labels, UI, Camera cones, collision guides, or sprite sheets whose frames must align.
- Use one approved character turnaround as the identity reference.
- Derive animation frames through controlled frame production and manual cleanup.
- Remove stray opaque pixels, inconsistent lighting, changing equipment, and anchor drift.
- Rebuild tile edges manually when seamlessness is required.
- Validate each output at actual gameplay scale.

## 6. Intake automation

The runtime repository MUST provide checks for:

- expected inventory;
- file naming;
- dimensions;
- sRGB;
- alpha;
- opaque-content floor;
- duplicate hashes;
- manifest/catalog parity;
- atlas membership;
- missing frames;
- sequential frame IDs;
- stable anchors;
- runtime reachability;
- bundle exclusion for sources;
- provenance completeness.

## 7. Review plates

Each batch produces:

1. source/contact sheet;
2. actual-scale light background;
3. actual-scale dark background;
4. grayscale plate;
5. simulated color-vision plate;
6. dense-combat composite;
7. reduced-motion composite;
8. collision/anchor overlay;
9. device screenshot;
10. manifest receipt.

Reviewers approve batches by stable asset IDs, not filenames alone.

## 8. Asset budgets

Budgets are measured after the grayscale blockout and then frozen for the release candidate:

- decoded atlas memory;
- application bundle bytes;
- atlas count loaded per segment;
- draw count at median and peak density;
- particle count;
- transient-node count;
- preload latency;
- peak resident memory.

A new asset that breaks a budget requires replacement, consolidation, or an explicit decision—not an undocumented budget increase.

## 9. Sources informing this contract

- Apple, [Maximizing Texture Performance](https://developer.apple.com/documentation/spritekit/maximizing-texture-performance)
- Apple, [About Texture Atlases](https://developer.apple.com/documentation/spritekit/about-texture-atlases)
- Apple, [Loading and Using Textures](https://developer.apple.com/documentation/spritekit/loading-and-using-textures)
- Apple, [SpriteKit Best Practices](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/DesigningGameswithSpriteKit/DesigningGameswithSpriteKit.html)
- Apple, [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- Apple, [Reduced Motion evaluation](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria/)
- Apple, [Differentiate Without Color Alone](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria/)
- Apple, [Sufficient Contrast evaluation](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria/)

Similar survivor games inform the high-level pattern—short legible loops, rising density, strong silhouettes, build expression, and boss punctuation—but this specification does not copy their assets, layouts, timings, names, or content.
