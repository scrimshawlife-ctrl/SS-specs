# Agent Instructions

Read `README.md` and `specs/000-constitution.md` before changing any artifact.

## Method

Use Spec-Driven Development in this order:

1. Constitution: governing constraints.
2. Intent: `intent.md` for why the change is worth specifying. Required before specify for non-trivial, feature, or RFC-sized work. Copy `intent/_TEMPLATE.md`. Do not skip.
3. Specification: observable what and why in `spec.md`. Bind Workflows from this file at specify time. Do not put skills, owner, or CI policy in the product specification.
4. Plan: technical how.
5. Tasks: ordered implementation work.
6. Runtime implementation in the separate runtime repository.
7. Verification evidence against acceptance gates.

Sequence for non-trivial changes: `intent.md` → `spec.md` → plan/tasks → implement. Bind Workflows (below) when specifying. Do not skip intent for feature- or RFC-sized work.

Do not place implementation details in the product specification unless they are externally observable constraints.

## Workflows

Locked 2026-08-31 by Danny. This section names existing Grok Bot skills, the owner specialist, and GitHub Actions already in use. Do not invent skills, bots, or Actions.

This is contributor policy. It is not part of the product specification.

### Product-work defaults

Use these existing Grok Bot skills on specification and product work:

| Skill | Role on this slice |
|---|---|
| `anti-slop-code` | Keep scripts and any later runtime change small, testable, and free of dead paths. Cite `FM-AS-01`–`FM-AS-07`. |
| `production-systems` | Fail closed on secrets, ambiguous authority, and unproven scale. Cite `FM-PS-04`, `FM-PS-06`; treat `FM-PS-01`–`FM-PS-03`, `FM-PS-05`, `FM-PS-07`–`FM-PS-10` as runtime constraints when implementation touches them. `FM-PS-11` remains SPECULATIVE. |
| `google-developer-style` | Write contracts and agent docs in plain, specific language. Cite `FM-DOC-01`. |

`FM-DOC-02` is a Zero State / SUAS copy lock and does not apply to this product.

### Owner specialist

The owner specialist is Danny (`scrimshawlife-ctrl`). Constitution changes, expansion-gate exceptions, and any new skill or bot require that owner. This is not a new bot.

### GitHub Actions

Reuse the Actions that already exist. Do not add another workflow unless the owner specialist names one.

| Action | Repository | Reuse |
|---|---|---|
| `Validate specification` (`.github/workflows/validate.yml`) | `scrimshawlife-ctrl/SS-specs` | Required on every pull request and push to `main`. Runs `scripts/validate_specs.py`. |
| `CI` (`.github/workflows/ci.yml`) | `scrimshawlife-ctrl/SS-runtime` | Runtime tests and iOS simulator build. Spec work does not replace or duplicate it. |

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
