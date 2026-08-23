# Surveillance Survivor — Specifications

Canonical specifications for the one-level reboot of **Surveillance Survivor**.

## Product thesis

Surveillance Survivor is a deterministic, top-down survival action game in which surveillance is an active systemic threat. The first release contains one polished San Francisco level. The player must manage exposure, survive escalating enforcement, defeat the response captain, and reach extraction.

## Canonical sequence

1. [Constitution](specs/000-constitution.md)
2. [Product specification](specs/001-single-level-vertical-slice/spec.md)
3. [Technical plan](specs/001-single-level-vertical-slice/plan.md)
4. [Implementation tasks](specs/001-single-level-vertical-slice/tasks.md)
5. [Legacy admission inventory](specs/001-single-level-vertical-slice/legacy-admission.md)
6. [Acceptance and playtest gates](specs/001-single-level-vertical-slice/acceptance.md)

Implementation belongs in a separate runtime repository. This repository defines product intent, contracts, decisions, and acceptance evidence.

## Current status

- Scope: one level
- Canonical location: San Francisco
- Target experience: 8–12 minute complete run
- Specification state: baseline
- Runtime state: not yet authorized by this repository
- Additional cities: deferred

## Core loop

`evade surveillance → manage exposure → gain power → survive lockdown → defeat captain → extract`

## Change rule

A change to product behavior must update the specification before or with runtime implementation. A proposal that introduces another city, generalized campaign infrastructure, or speculative content before the acceptance gates pass is non-conforming.
