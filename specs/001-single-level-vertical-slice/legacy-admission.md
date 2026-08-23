# Legacy Component Admission

Status: INVENTORY_PENDING

## Purpose

This artifact prevents accidental architectural inheritance. The legacy runtime is evidence and a source of candidates. It is not the canonical design.

## Immutable source requirement

Before analysis, record:

- Repository URL
- Commit SHA or release tag
- Build environment
- Test command and result
- Known runtime defects
- Provenance date

Until these fields are populated, all candidate statuses are `NOT_EVALUATED`.

## Admission schema

| Field | Required content |
|---|---|
| Candidate ID | Stable identifier |
| Source | Exact legacy path and commit |
| Responsibility | One bounded behavior |
| Dependencies | Imports, globals, assets, runtime assumptions |
| Evidence | Tests, observed output, or reproducible probe |
| Determinism risks | Time, randomness, ordering, floating point, scene graph authority |
| Contract fit | Requirement IDs satisfied or violated |
| Decision | ADMIT, ADAPT, REWRITE, or REJECT |
| Destination | New module and ownership |
| Verification | New tests and acceptance evidence |

## Initial candidate queue

| ID | Candidate | Initial state | Intended evaluation |
|---|---|---|---|
| LC-001 | Seeded randomness | NOT_EVALUATED | Sequence stability and injection |
| LC-002 | Simulation timing | NOT_EVALUATED | Fixed-step fitness |
| LC-003 | Player movement | NOT_EVALUATED | Input separation and collision |
| LC-004 | Camera line-of-sight | NOT_EVALUATED | Geometry truth and occlusion |
| LC-005 | Projectile pool | NOT_EVALUATED | Complete lifecycle reset |
| LC-006 | Combat resolution | NOT_EVALUATED | Ordering and attribution |
| LC-007 | Enemy behaviors | NOT_EVALUATED | Scene coupling and determinism |
| LC-008 | Extraction logic | NOT_EVALUATED | Preconditions and single completion |
| LC-009 | Visual assets | NOT_EVALUATED | License, performance, and style |
| LC-010 | Audio assets | NOT_EVALUATED | License, mixing, and event coupling |

## Default exclusions

The following are rejected unless a later specification creates a proven need:

- City selection
- Multi-level coordinators
- Campaign progression
- Procedural map generation
- Generalized content abstractions
- Multiple player characters
- Inventory and crafting
- Legacy global state containers

## Decision meanings

- **ADMIT:** Behavior and architecture fit; port with tests.
- **ADAPT:** Useful bounded logic exists but must be separated or corrected.
- **REWRITE:** Requirement remains, implementation is unsuitable.
- **REJECT:** Neither implementation nor responsibility belongs in SS-001.

No source file may be copied before its row contains an evidence-backed decision.
