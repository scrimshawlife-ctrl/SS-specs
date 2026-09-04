# Intent

Write an `intent.md` **before specify**. Intent captures why a change is worth specifying. It is not a specification, plan, or task list.

## When to write

Write intent for non-trivial work: a feature, RFC, or any change that would add or rewrite observable product behavior.

Do not skip intent for feature- or RFC-sized work.

Skip intent only for typo, index, or other mechanical doc fixes that do not change product meaning.

## How

1. Copy [`_TEMPLATE.md`](_TEMPLATE.md) to `intent/<short-name>.md`.
2. Fill every section. Label claims as verified or assumed.
3. Stop. The next stage is `spec.md`, not implementation.

Do not invent product intents to populate this directory. The Civic Seam baseline is already specified; new feature-sized work starts here.
