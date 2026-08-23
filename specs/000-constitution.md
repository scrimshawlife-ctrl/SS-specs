# Surveillance Survivor Constitution

Version: 1.0.0  
Ratified: 2026-08-23

## Article I — One complete level

The product MUST deliver one polished San Francisco level before work begins on another level. The target complete run MUST last approximately 8–12 minutes for a competent player. Breadth MUST NOT substitute for completion, clarity, stability, or replay value.

## Article II — Surveillance is systemic

Surveillance MUST affect play through the Exposure system. Cameras MUST NOT be decorative hazards. Detection, escalation, enemy pressure, Lockdown, and scoring MUST have explicit relationships to Exposure.

## Article III — Deterministic authority

Authoritative gameplay MUST be reproducible from:

`rulesetVersion + levelVersion + seed + ordered player inputs`

Rendering, audio, animation, and wall-clock timing MUST NOT own authoritative rules. Equivalent authoritative inputs MUST produce equivalent authoritative outcomes.

## Article IV — Legible causality

The player MUST be able to understand why detection, damage, escalation, upgrades, failure, and extraction occurred. Visual indicators MUST match authoritative geometry and state. Invisible damage and undisclosed state transitions are defects.

## Article V — Minimal meaningful content

The first slice is limited to one player, one map, two standard enemy roles, one Response Captain, one base weapon, three upgrades, one Exposure system, one extraction objective, and one result screen. New content MUST replace or materially improve an existing responsibility unless the constitution is amended.

## Article VI — Legacy code is evidence, not authority

The legacy project is a source quarry. A component may enter the reboot only after its behavior, dependencies, deterministic properties, tests, and ownership are documented. Copying a component because it appears to work is prohibited.

## Article VII — Contract before implementation

Observable behavior MUST be specified before implementation. Technical work MUST trace to a requirement and acceptance criterion. Decisions that change scope, determinism, player-facing rules, or expansion gates MUST be recorded.

## Article VIII — Quality gates control expansion

Additional levels are forbidden until all functional, deterministic, performance, usability, and playtest gates in the canonical acceptance artifact pass with recorded evidence.

## Governance

Constitution changes require:

1. A recorded rationale.
2. Identification of affected specifications and runtime contracts.
3. A version increment.
4. Migration or compatibility guidance.
5. Explicit owner approval.

Principles may not be silently weakened through plan or task changes.
