# Surveillance Survivor — Specifications

Canonical specifications for the one-level reboot of **Surveillance Survivor**.

## Product thesis

Surveillance Survivor is a deterministic, top-down survival action game in which surveillance is an active systemic threat. The first release contains one polished San Francisco level. The player must manage Exposure, survive escalating enforcement, defeat the Algorithmic Moderate, and reach Extraction.

## Canonical sequence

Non-trivial or feature-sized work starts with [`intent/`](intent/README.md) before specify. Contributor Workflows (skills, owner, CI) live in [`AGENTS.md`](AGENTS.md), not in the product specification. The Civic Seam baseline below is already specified.

1. [Constitution](specs/000-constitution.md)
2. [Product specification](specs/001-single-level-vertical-slice/spec.md)
3. [Technical plan](specs/001-single-level-vertical-slice/plan.md)
4. [Civic Seam visual direction](specs/001-single-level-vertical-slice/civic-seam-visual-direction.md)
5. [Visual asset specification](specs/001-single-level-vertical-slice/visual-assets.md)
6. [Animation specification](specs/001-single-level-vertical-slice/animation.md)
7. [Arena specification](specs/001-single-level-vertical-slice/arena.md)
8. [Exact arena layout](specs/001-single-level-vertical-slice/arena-layout.md)
9. [Arena manifest](contracts/civic-seam-arena-001.json)
10. [Arena schema](contracts/civic-seam-arena-001.schema.json)
11. [Visual production plan](specs/001-single-level-vertical-slice/visual-production.md)
12. [Camera destruction contract](specs/001-single-level-vertical-slice/camera-destruction.md)
13. [Camera placement contract](specs/001-single-level-vertical-slice/camera-placement.md)
13a. [Camera socket manifest schema](contracts/camera-placement-001.schema.json)
14. [Exposure contract](specs/001-single-level-vertical-slice/exposure.md)
15. [Player controller contract](specs/001-single-level-vertical-slice/player-controller.md)
16. [Base combat contract](specs/001-single-level-vertical-slice/combat.md)
17. [Enemies and mob encounters](specs/001-single-level-vertical-slice/enemies-and-encounters.md)
18. [Elite and boss contract](specs/001-single-level-vertical-slice/bosses.md)
19. [Upgrade contract](specs/001-single-level-vertical-slice/upgrades.md)
20. [HUD and tutorial contract](specs/001-single-level-vertical-slice/hud-tutorial.md)
21. [Audio and haptics contract](specs/001-single-level-vertical-slice/audio-haptics.md)
22. [Events, receipts, and replays](specs/001-single-level-vertical-slice/events-receipts-replays.md)
23. [Event schema](contracts/event-001.schema.json)
24. [Event catalog](contracts/event-catalog-001.json)
25. [Run receipt schema](contracts/run-receipt-001.schema.json)
26. [Asset record schema](contracts/asset-record-001.schema.json)
27. [Presentation asset manifest](contracts/presentation-assets-001.json)
27a. [Clip metadata](contracts/clip-metadata-001.json)
27b. [Procedural VFX](contracts/procedural-vfx-001.json)
27c. [Ambient motion](contracts/ambient-motion-001.json)
27d. [Visual language](contracts/visual-language-001.json)
27e. [Asset catalog (intake records)](contracts/asset-catalog-001.json)
28. [Combat content manifest](contracts/combat-content-001.json)
29. [Global simulation order](specs/001-single-level-vertical-slice/simulation-order.md)
30. [Encounter objectives and Extraction gate](specs/001-single-level-vertical-slice/encounter-objectives.md)
31. [Runtime kernel schema](contracts/runtime-kernel-001.json)
32. [Contract version registry](contracts/versions.json)
33. [Kernel vectors](fixtures/kernel-vectors-001.json)
34. [Smoke replay](fixtures/replay-smoke-001.json)
34a. [Complete-run golden vectors](fixtures/complete-run-vectors-001.json)
34b. [Replay matrix](fixtures/replay-matrix-001.json)
35. [Completeness audit](specs/001-single-level-vertical-slice/completeness-audit.md)
36. [Implementation tasks](specs/001-single-level-vertical-slice/tasks.md)
37. [Legacy admission inventory](specs/001-single-level-vertical-slice/legacy-admission.md)
38. [Acceptance and playtest gates](specs/001-single-level-vertical-slice/acceptance.md)
39. [Decision register](specs/001-single-level-vertical-slice/decisions.md)
40. [Run-shell terminal surface](specs/001-single-level-vertical-slice/run-shell.md)

Implementation belongs in a separate runtime repository. This repository defines product intent, contracts, decisions, and acceptance evidence.

## Current baseline

```yaml
scope: one authored San Francisco level — The Civic Seam
platform: iPhone
orientation: landscape-left-and-right
minimum_os: iOS 18.0
language: Swift 6
renderer: SpriteKit
shell: SwiftUI
simulation: deterministic-fixed-step-60Hz
presentation_target: 60fps
networking: none
accounts: none
target_run: 8-12 minutes
runtime_repository: scrimshawlife-ctrl/SS-runtime
additional_cities: deferred
```

## Core loop

`evade surveillance → manage Exposure → gain power → survive Lockdown → defeat Captain → extract`

## Change rule

A change to product behavior must update the specification before or with runtime implementation. A proposal that introduces another city, generalized campaign infrastructure, or speculative content before the acceptance gates pass is non-conforming.
