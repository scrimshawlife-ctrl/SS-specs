# Surveillance Survivor — Specifications

Canonical specifications for the one-level reboot of **Surveillance Survivor**.

## Product thesis

Surveillance Survivor is a deterministic, top-down survival action game in which surveillance is an active systemic threat. The first release contains one polished San Francisco level. The player must manage Exposure, survive escalating enforcement, defeat the Response Captain, and reach Extraction.

## Canonical sequence

1. [Constitution](specs/000-constitution.md)
2. [Product specification](specs/001-single-level-vertical-slice/spec.md)
3. [Technical plan](specs/001-single-level-vertical-slice/plan.md)
4. [Civic Seam visual direction](specs/001-single-level-vertical-slice/civic-seam-visual-direction.md)
5. [Visual asset specification](specs/001-single-level-vertical-slice/visual-assets.md)
6. [Animation specification](specs/001-single-level-vertical-slice/animation.md)
7. [Arena specification](specs/001-single-level-vertical-slice/arena.md)
8. [Visual production plan](specs/001-single-level-vertical-slice/visual-production.md)
9. [Camera destruction contract](specs/001-single-level-vertical-slice/camera-destruction.md)
10. [Exposure contract](specs/001-single-level-vertical-slice/exposure.md)
11. [Player controller contract](specs/001-single-level-vertical-slice/player-controller.md)
12. [Base combat contract](specs/001-single-level-vertical-slice/combat.md)
13. [Global simulation order](specs/001-single-level-vertical-slice/simulation-order.md)
14. [Encounter objectives and Extraction gate](specs/001-single-level-vertical-slice/encounter-objectives.md)
15. [Runtime kernel schema](contracts/runtime-kernel-001.json)
16. [Contract version registry](contracts/versions.json)
17. [Implementation tasks](specs/001-single-level-vertical-slice/tasks.md)
18. [Legacy admission inventory](specs/001-single-level-vertical-slice/legacy-admission.md)
19. [Acceptance and playtest gates](specs/001-single-level-vertical-slice/acceptance.md)
20. [Decision register](specs/001-single-level-vertical-slice/decisions.md)

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
runtime_repository: scrimshawlife-ctrl/SS
additional_cities: deferred
```

## Core loop

`evade surveillance → manage Exposure → gain power → survive Lockdown → defeat Captain → extract`

## Change rule

A change to product behavior must update the specification before or with runtime implementation. A proposal that introduces another city, generalized campaign infrastructure, or speculative content before the acceptance gates pass is non-conforming.
