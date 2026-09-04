# Agent Instructions

Read `README.md` and `specs/000-constitution.md` before changing any artifact.

## Method

Use Spec-Driven Development in this order:

1. Constitution: governing constraints.
2. Intent: `intent.md` for why the change is worth specifying. Required before specify for non-trivial, feature, or RFC-sized work. Copy `intent/_TEMPLATE.md`. Do not skip.
3. Specification: observable what and why, including the `spec.md` Workflows binding.
4. Plan: technical how.
5. Tasks: ordered implementation work.
6. Runtime implementation in the separate runtime repository.
7. Verification evidence against acceptance gates.

Sequence for non-trivial changes: `intent.md` → `spec.md` Workflows → plan/tasks → implement.

Do not place implementation details in the product specification unless they are externally observable constraints.

## Ubiquitous language

Use the terms defined in `specs/001-single-level-vertical-slice/spec.md`. Do not create synonyms for Exposure, Detection State, Lockdown, Algorithmic Moderate, or Extraction.

## Evidence

Label uncertain statements as one of:

- **OBSERVED**: directly verified in code, runtime output, or test evidence.
- **INFERRED**: supported by evidence but not directly verified.
- **PROPOSED**: a design choice awaiting acceptance.
- **NOT_COMPUTABLE**: insufficient evidence.

Never claim that a legacy component works until its admission evidence is recorded.

## Scope discipline

The canonical product has one level. Reject or defer additional cities, campaign systems, procedural maps, generalized content frameworks, inventories, multiple characters, and meta-progression until the expansion gate passes.

## Change discipline

Every behavior change must update all affected artifacts. A specification change is incomplete if its plan, tasks, acceptance criteria, or decision record conflicts with it. Preserve deterministic replay identity and version every ruleset-affecting change.

## Escalation

Broken CI or failing tests are a labeled `defect`. File or update that issue. Do not skip, weaken, or rewrite tests to manufacture a green run.
