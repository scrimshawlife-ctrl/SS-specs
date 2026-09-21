# Intent

Write an `intent.md` **before specify**. Intent captures why a change is worth specifying. It is not a specification, plan, or task list.

This directory is this repository’s required gate between constitution and specify (D-063). GitHub Spec Kit has no `intent/` phase. Do not skip intent for feature- or RFC-sized work.

## When to write

Write intent for non-trivial work: a feature, RFC, or any change that would add or rewrite observable product behavior.

Skip intent only for typo, index, or other mechanical doc fixes that do not change product meaning.

## How

1. Copy [`_TEMPLATE.md`](_TEMPLATE.md) to `intent/<short-name>.md`.
2. Fill every section. Label claims as verified or assumed. Set **Status** to `draft`.
3. Stop. A human sets **Status** to `accepted` before specify. `superseded` replaces an earlier intent.
4. After acceptance, the next stage is `spec.md`. Bind Workflows from [`AGENTS.md`](../AGENTS.md) there by pointer only. Do not list skills, owner, or CI policy in the intent or in the product specification.

Do not invent product intents to populate this directory. The Civic Seam baseline is already specified; new feature-sized work starts here.

Accepted historical files may use older headings. New intents copy the template exactly.

## After specify

Optional Spec Kit gates — clarify, checklist, analyze, converge — are mapped in [`docs/SPEC-KIT-ALIGNMENT-2026-09-21.md`](../docs/SPEC-KIT-ALIGNMENT-2026-09-21.md). They do not replace this gate.
