# Extension-points audit — SS-specs

**Repo:** `scrimshawlife-ctrl/SS-specs` at `fb60046` (main).  
**Date:** 2026-09-21.  
**Kind:** docs-only audit. No gameplay rules, store copy, SIGN, or HANDOFF invented here.

**Lens:** attached SS-MAP / DISTILL / TEACH-LUDUS harvest (KEEP 10 / ADAPT 8 / REJECT 9). The harvest is a mapping aid, not a license to add product verbs.

**Labels:** **OBSERVED** = in this repository. **INFERRED** = harvest-to-spec mapping judgment.

---

## 0. Language lock (read first)

Canonical SS-001 terms stay: **Exposure**, **Detection State**, **Camera**, **Lockdown**, **Algorithmic Moderate**, **Extraction**, **Upgrade**, **Network Blackout**, **Civic Seam**.

SS-MAP harvest language is **not** imported as product vocabulary:

| Harvest phrase (SS-MAP) | Civic Seam analog (OBSERVED) | Do not do |
|---|---|---|
| Suspicion 0–5 | Five Detection States: `hidden`, `observed`, `tracked`, `hunted`, `lockdown` | Add a second Suspicion meter |
| LPR poles | Standard Cameras; `trafficReader` is one housing family | Rename Cameras to LPR, or ship rejected legacy `lpr_*` frames as the mechanic |
| Blind Spot extract | Extraction at Phoenix Steps after Combat Authority; field absence after Camera destruction | Create a Blind Spot entity (D-033 and camera-destruction §8 forbid it) |
| Ten-city Wichita→Atlanta | Explicitly deferred / REJECTED for SS-001 | Import campaign cities before the expansion gate |
| SIGN / store subtitle | **Absent** from this repo | Author SIGN or a store subtitle here |

**OBSERVED:** `Stay untrackable. Break the grid.` does not appear in SS-specs. Bundle id `com.zer0state.surveillancesurvivor` does not appear either. This audit does not add them.

---

## 1. Repo map

Top-level layout **OBSERVED**:

```text
SS-specs/
  README.md                         Canonical product index (must list every specs/contracts/fixtures file)
  AGENTS.md                         Contributor Workflows (skills, owner, CI) — not product spec
  CLAUDE.md                         Adapter → AGENTS.md
  intent/                           Specify gate (D-063). Template + three intents
  specs/000-constitution.md         Governing locks (v1.1.0)
  specs/001-single-level-vertical-slice/   The only feature slice
  contracts/                        Versioned machine artifacts
  fixtures/                         Golden vectors / replay corpus
  scripts/validate_specs.py         Fail-closed index + schema checks
  .github/workflows/validate.yml    "Validate specification"
```

**Absent (OBSERVED):** `rfc/`, `docs/` (until this file), `adr/` folder. Decisions live in `specs/001-single-level-vertical-slice/decisions.md`. No pull-request template.

### 1.1 Constitution and product index

| Artifact | Role |
|---|---|
| `specs/000-constitution.md` | One SF level; Exposure is systemic; determinism; legible causality; Article V content cap; Article VIII expansion gate |
| `README.md` | Civic Seam thesis, 40-item sequence, one-level baseline YAML |
| `AGENTS.md` | intent → spec → plan/tasks → implement; ubiquitous-language lock; one-level scope discipline |

### 1.2 Feature slice (SS-001)

All under `specs/001-single-level-vertical-slice/`:

| File | Role |
|---|---|
| `spec.md` | Product intent, non-goals, ubiquitous language, FR-001–FR-056 |
| `plan.md` | Runtime modules, determinism, delivery slices |
| `tasks.md` | Implementation checklist + open-task reconciliation |
| `decisions.md` | Decision register D-001–D-066 (the ADR surface) |
| `acceptance.md` | Gates A–G and expansion decision |
| `completeness-audit.md` | Closed surfaces + expansion seal |
| `exposure.md` | Exposure 0–1000, five Detection States, Tamper, recovery |
| `camera-destruction.md` | Integrity 3, Tamper +100, no Blind Spot entity, Network Blackout |
| `camera-placement.md` | Seeded 8-of-authored-sockets; ≥18 enabled |
| `upgrades.md` | One protected 3-offer after M-A |
| `enemies-and-encounters.md` | Five archetypes; M-A/M-B/M-C = 14/17/25 |
| `bosses.md` | Improper Search Daemon + Algorithmic Moderate |
| `encounter-objectives.md` | Combat Authority vs Network Blackout; Extraction predicate |
| `combat.md` | Civic Pulse auto-attack |
| `player-controller.md` | Analog move + 12-tick Dodge |
| `arena.md` / `arena-layout.md` | Seven zones; Pressure Route dual path; Phoenix Steps |
| `hud-tutorial.md` | HUD table, exact copy, T0–T4 tutorial |
| `run-shell.md` | **PROPOSED** title/terminal surfaces; OPEN copy and receipt questions |
| `events-receipts-replays.md` | Append-only events; result-screen fields |
| `audio-haptics.md` | Event projection, 8-voice cap, music states |
| `civic-seam-visual-direction.md` | Civic (not neon) identity; housing families; fog |
| `visual-assets.md` / `animation.md` / `visual-production.md` | Art inventory and intake |
| `legacy-admission.md` | LC-001–LC-010; bounded ADAPT; ten-city REJECT |

### 1.3 Intents (specify gate, not RFCs)

| Path | Status (OBSERVED) | Next |
|---|---|---|
| `intent/README.md` + `_TEMPLATE.md` | Process | — |
| `intent/run-shell-surfaces.md` | accepted | `run-shell.md` still PROPOSED |
| `intent/2026-09-04-legacy-art-admission.md` | accepted | LC-009/LC-010 amended |
| `intent/2026-09-07-fog-layers.md` | draft | IDs already in `presentation-assets-001`; zone-density still open |

**OBSERVED:** there is no RFC file. D-063 names RFC-sized work as a reason to write intent first. A new slice starts at `intent/<name>.md`, not as a free-standing RFC folder.

### 1.4 Contracts and fixtures

Identities live in the contract registry: ruleset `ss-rules-001`, content `civic-seam-content-001`, arena `civic-seam-arena-001`.

Notable machine hooks: `combat-content-001.json` (tuning tables), `event-catalog-001.json` (append-only ordinals), `visual-language-001.json` (salience + palette), `procedural-vfx-001.json` (hit / telegraph recipes), `camera-placement-001.json` (18 sockets), `civic-seam-arena-001.json` (geometry), `asset-catalog-001.json` (intake).

### 1.5 Decision register (ADR surface)

`decisions.md` is the only ADR log. Load-bearing for this audit:

- D-001 / D-017: one authored Civic Seam, no procedural maps.
- D-003 / D-038 / D-039: Exposure 0–1000; Lockdown latches at 1000.
- D-004 / D-048: exactly three run-local upgrades; choose one after M-A.
- D-025: no generic neon cyberpunk.
- D-033: no loot, no Blind Spot entity, no chain explosion, no Camera respawn.
- D-037: keep Algorithmic Moderate phases **without importing the ten-city campaign**.
- D-059: local receipts only; no cloud sync or analytics.
- D-063: intent before specify for feature/RFC-sized work.

Pending evidence only: D-020 (device equivalents), D-021 (profiled ceilings).

---

## 2. How this repo already invites extension

**OBSERVED** Article V: new content must replace or materially improve an existing responsibility unless the constitution is amended. Article VIII: additional levels wait for Gates A–G.

So a true extension point is a place the current contracts already allow variety, presentation, or authored content **without** adding a city, a second meter, a new verb, or a meta tree.

---

## 3. Extension-points inventory

Status key: **exists** = specified and versioned; **stub** = draft/proposed/OPEN or IDs without owning canonical copy; **absent** = no slice, and a new intent would be required.

### 3.1 Systemic / run-structure

| ID | Path | What it extends | Status | SS-MAP KEEP/ADAPT landing | REJECT risk |
|---|---|---|---|---|---|
| EP-01 | `exposure.md`; HUD Detection table in `hud-tutorial.md` | Five Detection States already teach pressure literacy | exists | KEEP systems-first + “Suspicion should teach.” **INFERRED:** harvest Suspicion maps onto these five states; do not add a sixth scale | Inventing Suspicion 0–5 as a second meter; curse-without-reward (thresholds that grief without teaching) |
| EP-02 | `encounter-objectives.md`; `arena.md` Z-07; D-053 | Timed Extraction after Combat Authority (300 ticks, reset on exit) | exists | ADAPT “endless timer survive” → Phoenix Steps coda. KEEP Blind Spot *timing* only as Extraction | Reintroducing a Blind Spot **entity** (D-033, LC-008 REWRITE). Gating extract on Camera count |
| EP-03 | `encounter-objectives.md` Combat Authority lane | Required graph M-A → M-B → M-C → elite → boss → Extraction armed | exists | ADAPT boss set-pieces / run coda onto Algorithmic Moderate + Improper Search Daemon | Extra bosses, HP-sponge phases, or a second wincon (body-count) |
| EP-04 | `encounter-objectives.md` Network Blackout lane | Optional 8/8 Camera mastery; receipt accolade only; no power | exists | ADAPT “untrackable storm” / screen-clear fantasy as **optional geometry mastery**, not DPS | Turning Blackout into loot, multiplier, or Extraction gate (explicitly forbidden) |
| EP-05 | `upgrades.md`; FR-030–035; D-048 | Exactly one protected 3-card offer after M-A | exists | KEEP 3-offer grammar, dual audience, no forced-upgrade softlock (every upgrade must beat every required fight) | Second offer mid-run, evolutions, luck-gated rerolls, numeric-only cards — needs constitution amendment |
| EP-06 | `enemies-and-encounters.md` EN-010 | No XP gems, health, currency, or upgrade drops | exists (as a negative) | ADAPT “kill-horde XP” → existing Exposure / encounter pressure only | Sneaking collectible gems via `visual-language-001` `collectible` / `dropsAndUpgrades` ranks |
| EP-07 | `run-shell.md`; `intent/run-shell-surfaces.md` | Title + terminal surfaces; OPEN control copy, player-facing receipt subset, title return, lethal-warning HUD row | stub (PROPOSED; 7.1, 7.2, 7.5 OPEN) | KEEP buy-once / systems-first / dual audience. Result literacy without a meta lobby | Run history, unlocks, difficulty select, shop — `run-shell.md` §8 already forbids these |

### 3.2 Space / Cameras / movement

| ID | Path | What it extends | Status | SS-MAP KEEP/ADAPT landing | REJECT risk |
|---|---|---|---|---|---|
| EP-08 | `camera-destruction.md`; `camera-placement.md`; schema housing enum | Destructible stationary Cameras; honest fields; 5 appearance-only housings including `trafficReader` | exists | KEEP honest cones + readable silhouettes. **INFERRED:** harvest “LPR poles” land as Camera housings, not a new pole verb | Dishonest/hidden fields; panning/patrol Cameras (non-goals); shipping classified `lpr_*` frames as the system; Blind Spot bubbles |
| EP-09 | `camera-placement-001` schema `minItems: 18` | More **authored** sockets (still select 8; still fairness CI) | exists | ADAPT “pole fields as boss-like pressure” via legal layouts, not mid-run spawn | Procedural coordinates; difficulty-based Camera count; mid-run rerolls |
| EP-10 | `arena.md` Z-04 Pressure Route | Stealth-favored vs combat-favored paths; same ending; no exclusive upgrade | exists | KEEP move-as-primary; ADAPT dual audience as **routes**, not skins | Branching endings, exclusive power, or a second map |
| EP-11 | `player-controller.md`; Ghost Step in `upgrades.md` | Analog move + Dodge; Ghost Step is the only detection-immunity upgrade | exists | KEEP “you do not stop moving”; TEACH-LUDUS move-as-verb | Stand-still AFK win; Ghost Step damage immunity (explicitly 0); AFK extract |
| EP-12 | `bosses.md` Captain Camera / Temporary Order | Boss-owned emitter, not a standard Camera | exists | ADAPT authority-spike as boss pressure | Making Captain Camera Network-Blackout-countable or independently destructible |

### 3.3 Presentation / juice / identity

| ID | Path | What it extends | Status | SS-MAP KEEP/ADAPT landing | REJECT risk |
|---|---|---|---|---|---|
| EP-13 | `visual-language-001.json` salience ranks 1–9; D-016, D-025 | Readability-first hierarchy; civic palette; no neon cyberpunk | exists | KEEP readable silhouettes under chaos; REJECT cyberpunk-ghost poster | Visual mush; juice that hides cones; full-neon skin |
| EP-14 | `procedural-vfx-001.json` recipes (`enemyHit` = compactSpark, not a number) | Bounded hit-stop / particles / telegraphs | exists | KEEP damage-number / juice **feel**. Numeric pops are **absent** | Clutter deaths; full-screen flash (already forbidden); juice that outranks Camera fields |
| EP-15 | `hud-tutorial.md` exact copy + visibility rules | Minimal, named HUD; Camera counter hidden until first damage unless pinned | exists | KEEP minimal HUD / action-first | Extra meters, XP bar, shop HUD |
| EP-16 | `hud-tutorial.md` lethal-warning gap (called out in `run-shell.md` §7.5) | Safety preemptor named, **no copy row** | stub | KEEP causality / “if you die to clutter, design failed” | Invented panic copy that does not match audio priority 1 |
| EP-17 | `audio-haptics.md` event map + 8-voice cap | Juice that does not own rules | exists | KEEP systems-first feel; coalescence already fights mush | Always-on online stingers; music that implies other cities on screen (Atlanta **beds** are a recorded exception in LC-010, IDs must stay city-nameless) |
| EP-18 | `civic-seam-visual-direction.md` §7; `intent/2026-09-07-fog-layers.md`; `env_fog_low` / `env_fog_high` | Two presentation fog layers; no volumetrics | stub (IDs exist; intent draft; zone-density OPEN) | KEEP readable grid; civic atmosphere | Fog that conceals cones/collision (Article IV defect) |
| EP-19 | `visual-assets.md` §14 P1/P2 lists | Authored civic dressing after P0 | exists (production, not mechanics) | KEEP slapstick-readable city | Tourist collage, real seals, other-city packs (T102 EXCLUDED) |
| EP-20 | `legacy-admission.md` LC-009/LC-010 | Bounded ADAPT of role-identical SF assets | exists | KEEP systems-first over spectacle; ADAPT only where role matches | Admitting legacy guards/Shift Manager as Civic Seam cast; wholesale city packs; Blind Spot decal (`blind_spot_decal.png` classified REJECT) |

### 3.4 Contracts that look like content frameworks (they are not)

| ID | Path | What it extends | Status | SS-MAP KEEP/ADAPT landing | REJECT risk |
|---|---|---|---|---|---|
| EP-21 | `combat-content-001.json` | Versioned **tuning** of the existing five enemies, three upgrades, two bosses | exists | KEEP systems-first. Tune; do not grow the roster | Treating the JSON as a generalized content framework (expansion seal) |
| EP-22 | `event-catalog-001.json` | Append-only event ordinals | exists | KEEP receipts / replay identity | New verbs smuggled as new event types without intent |
| EP-23 | `visual-language-001.json` `collectible` gold + salience rank 7 `dropsAndUpgrades` | Presentation roles with **no SS-001 drop entities** | exists (trap) | — | KEEP “no loot” is the rule. This palette slot is the easiest REJECT sneak |
| EP-24 | `acceptance.md` expansion decision | Second level only after Gates A–G + D-013/D-021 + sev-1/2 closed | exists (gate, not content) | ADAPT persistent talent tree / ten-city **only after** this gate, and only with owner + constitution | Shipping Wichita→Atlanta, shops, or meta now |

### 3.5 Explicitly not extension points

These are specified **closed** for SS-001. Harvest ADAPT items that need them must wait.

| Closed lock | Where | Harvest item that does **not** land here |
|---|---|---|
| Exactly 3 upgrades, choose 1 | Article V, D-004, D-048 | Layered weapon/mod trees; multiple 3-offers |
| Exactly 5 standard enemies | Article V, D-046 | New bullet-heaven threat verbs |
| No persistent meta-progression | `spec.md` §2, completeness-audit expansion seal, run-shell §8 | Between-run talent tree; unlocks that add verbs |
| No shop / chests / gold | EN-010, D-033, monetization non-goal | Brotato shop synergies |
| No Blind Spot entity | D-033, camera-destruction §8, LC-008 | Harvest “Blind Spot extract” as a place/entity |
| No ten-city campaign | D-001, D-037, LC default exclusions, Article I/VIII | Wichita→Atlanta roster |
| No online / accounts / MTX | README baseline; D-059 | Gacha / always-online retention |
| Camera fields honest and fixed | FR-010, FR-017, placement non-goals | Hidden telegraphs; AFK-safe dishonest cones |

---

## 4. Priority shortlist (next SS design work)

Ordered for **this** repo’s current slice, using the harvest as a lens. Each item improves an existing responsibility (Article V). None invents a verb.

### P0 — specify or finish what is already open

| Rank | Extension point | Why now | Harvest map | First honest next artifact |
|---|---|---|---|---|
| P0-1 | **EP-07 Run-shell OPEN items** | Title/terminal already shipped in runtime ahead of a canonical spec. Testers need outcome literacy for T903/T904. Smallest product-facing hole | KEEP systems-first, buy-once clarity, dual audience. ADAPT run coda as “what the player is told,” not a lobby | Accept `run-shell.md`; close 7.1 copy rows; decide 7.2 player-facing receipt subset. Do **not** add history/unlocks |
| P0-2 | **EP-16 Lethal-warning copy** | Named preemptor with audio priority 1 and no HUD string | KEEP causality / readable deaths | One exact-copy row in `hud-tutorial.md` (after a tiny intent if treated as specify-sized) |
| P0-3 | **EP-08 Camera housing + honest fields** | T507 still `NOT_PRODUCED`. `trafficReader` is the existing LPR-shaped **skin**, not a new pole | KEEP readable silhouettes, honest cones. ADAPT pole-field pressure | Produce five standard families + Captain Camera presentation; keep fields procedural and authoritative |
| P0-4 | **EP-13 / EP-14 Readable juice** | Salience + VFX recipes exist; floating damage **numbers** do not. Peak-density readability is Gate D | KEEP juice + chunky silhouettes. ADAPT “screen storm” as untrackable/Lockdown theater with cones still honest | Presentation-only: tighten VFX/HUD pops on existing `entityDamaged` / Tamper / Detection events. If numeric pops are wanted, that is a named gap (G-03), not a silent add |

### P1 — deepen existing loops without new verbs

| Rank | Extension point | Why next | Harvest map | Guardrail |
|---|---|---|---|---|
| P1-1 | **EP-01 Detection State literacy** | The defining system is already fully specified; remaining work is teaching and juice, not a new meter | KEEP “Suspicion teaches.” REJECT curse-without-reward | Do not rename Exposure. Thresholds stay D-038 unless a versioned retune is accepted |
| P1-2 | **EP-05 Three-card upgrade presentation** | Mechanics locked; cards can get clearer roles/numbers (already required) without a second pick | KEEP 3-offer, dual audience, no softlock | No fourth identity, no reroll, no evolution pair |
| P1-3 | **EP-02 / EP-03 Extraction + authority coda** | 8–12 minute run already ends in a timed hold after the Captain | ADAPT endless-timer and boss set-piece | Extraction predicate must stay combat-only |
| P1-4 | **EP-04 Network Blackout accolade on the terminal** | OPEN in run-shell 7.2 / intent question. Accolade already specified in-run | ADAPT untrackable fantasy without power | Receipt/terminal only; no combat reward |

### P2 — authored variety after P0 readability

| Rank | Extension point | Why later | Harvest map | Guardrail |
|---|---|---|---|---|
| P2-1 | **EP-18 Fog layers** | IDs exist; intent still draft; zone-density unanswered | KEEP civic readable grid | Presentation only; no concealment |
| P2-2 | **EP-09 Extra authored Camera sockets** | Schema already allows a larger reviewed pool | ADAPT pole-field variety per seed | Still eight selected; still exhaustive fairness |
| P2-3 | **EP-19 Visual P1/P2 civic kit** | Production list already exists | KEEP slapstick-readable city; REJECT cyberpunk mush | No other-city assets; no landmark collage |
| P2-4 | **EP-10 Pressure Route mastery** | Dual path is specified; playtest (G-006) still pending | KEEP move-as-skill; ADAPT stealth/combat as routes | Neither path may grant exclusive power |

**Not on this shortlist (harvest ADAPT that would break SS-001):** persistent talent tree, shop synergies, weapon-evolution pairs, XP-gem loop, ten-city meta. Those are **EP-24 / constitution** work after `EXPANSION_GATE_PASSED`, not silent extensions.

---

## 5. Gaps (names only)

Where specs are silent or only stubbed. **Do not treat these as written RFCs.**

| Gap | Kind | Notes |
|---|---|---|
| G-01 Run-shell canonicalization | stub exists | `run-shell.md` PROPOSED; intent accepted |
| G-02 Shell control copy (`START` / `SETTINGS` / `RESTART`) | OPEN 7.1 | No owning exact-copy rows |
| G-03 Hit-pop / numeric damage presentation | absent | VFX recipes are sparks, not numbers |
| G-04 Lethal-warning HUD copy | stub | `run-shell.md` §7.5 |
| G-05 Terminal player-facing receipt subset | OPEN 7.2 | Receipt exists; surface shows almost none of it |
| G-06 Title-return from terminal | OPEN §8.1 | Second control vs one-control restart |
| G-07 Fog zone-density | intent OPEN | IDs exist; “Transit Cut foggier?” unanswered |
| G-08 Housing-count hygiene | inconsistency | Destruction/schema: 5 standard families. Visual P0 / T507: “six” (5 + Captain). Not a new mechanic |
| G-09 Mid-run additional upgrade offers | absent | Would need constitution amendment + new intent |
| G-10 Between-run unlocks that add routes | absent | Expansion-gated; `spec.md` non-goal |
| G-11 Shop / chest / gold synergy layer | absent | Conflicts with EN-010 and Article V |
| G-12 Ten-city / district-authority campaign | absent | D-037, Article I/VIII, LC exclusions |
| G-13 SIGN / store subtitle | absent | Out of scope for this repo’s product spec |
| G-14 HANDOFF document | absent | Do not invent one |

---

## 6. Non-goals — do not extend

Hard locks for this audit and for next SS-specs work unless the owner amends the constitution and the expansion gate passes:

1. **One Civic Seam level.** No Wichita, Atlanta, or other city as playable content. Atlanta boss **music beds** are a recorded LC-010 exception, not a city unlock.
2. **Ubiquitous language.** Do not synonymize Exposure, Detection State, Lockdown, Algorithmic Moderate, or Extraction. Do not add Suspicion, LPR-as-verb, or Blind Spot-as-entity.
3. **Article V roster.** One player, one map, five standard enemies, one elite, one boss, one base weapon, three upgrades, one Exposure system, one Extraction, one result screen.
4. **Honest stationary Cameras.** No hidden fields, no mid-run pan/patrol/respawn, no Camera loot, no magical safe bubble.
5. **Extraction independence.** Network Blackout never gates Extraction. Combat Authority never marks Blackout complete.
6. **No meta-progression, shop, inventory, extra characters, or campaign framework** until `acceptance.md` records `EXPANSION_GATE_PASSED`.
7. **Offline premium.** No accounts, networking, gacha, MTX, or analytics upload (D-059).
8. **No cyberpunk ghost / neon poster fantasy** (D-025, visual prohibitions). Player is a readable grid runner.
9. **No stand-still AFK win.** Movement and Dodge remain the skill; Ghost Step is not damage immunity.
10. **Deterministic replay identity.** Presentation juice must not own rules (Article III).
11. **SIGN and store identity.** Do not author SIGN, a store subtitle, or change bundle/org identity. `com.zer0state.surveillancesurvivor` may exist elsewhere; this audit does not touch it.
12. **No invented HANDOFF** and no new Grok Bot skill or GitHub Action (D-062 / D-064).

---

## 7. Harvest crosswalk (KEEP / ADAPT / REJECT)

### KEEP (10) → existing SS-001 surface

| KEEP lesson | Lands on | Status |
|---|---|---|
| Move-as-primary skill | EP-11, EP-10, spawn-alley teaching | exists |
| Readable silhouettes under chaos | EP-13, Gate D, visual-production grayscale-first | exists |
| Minimal HUD / action-first | EP-15 | exists |
| 3-offer upgrade choices | EP-05 (once per run, not every level-up) | exists |
| Dual audience: simple + deep | EP-05 roles + EP-10 routes | exists |
| Buy-once / no gacha | spec non-goals, D-059, run-shell §8 | exists |
| Systems-first over spectacle | EP-01 Exposure, Article II | exists |
| Damage-number / juice feedback | EP-14 / G-03 | exists (sparks); numbers absent |
| No forced-upgrade softlock | `upgrades.md` balance invariants | exists |
| Between-run unlocks add verbs/routes | **Cannot land in SS-001** | absent / expansion-gated |

### ADAPT (8) → translate or defer

| Genre default | SS-001 landing | Verdict |
|---|---|---|
| Kill-horde XP gems | Exposure contact, Tamper, encounter graphs (EP-01, EP-06) | Adapt via existing loops only |
| Weapon evolution pairs | Three fixed upgrades; Ricochet already changes cone/pole interaction | Do **not** add evolution slots |
| Screen-clear power fantasy | Ghost Step + field removal + Lockdown theater; cones stay honest | Adapt presentation, not a wipe button |
| Endless timer survive | EP-02 Phoenix Steps 300-tick hold | Already the coda |
| Persistent talent tree | EP-24 only | Defer |
| Boss set-pieces | EP-03 / EP-12 Algorithmic Moderate + Captain Camera | Already specified |
| Shop synergies | — | Reject for SS-001 (G-11) |
| Genre inversion (save-horde) | Wincon is Extraction, not body count (FR-040) | Already the foil |

### REJECT (9) → existing fail-closed language

| REJECT pattern | Already blocked by |
|---|---|
| Stand-still AFK win | Dodge/Ghost Step contracts; spawn-alley teaching; Article IV |
| Dishonest / hidden threat telegraphs | FR-010, FR-011, Article IV |
| Cyberpunk ghost / poster fantasy | D-025, visual-assets §15 |
| Visual mush / unfair clutter deaths | Gate D, VFX bounds, 8-voice audio cap |
| Always-online / gacha / MTX | README networking/accounts none; D-059 |
| Luck-only power | Protected upgrade order; no reroll; deterministic targeting |
| Easy-mode gold efficiency | No gold (EN-010) |
| Numeric-only meta | No meta; upgrades change roles, not +% only |
| Curse difficulty without readable reward | Exposure recovery, tutorial copy, G-002 playtest |

---

## 8. What this audit is not

- Not a constitution amendment.
- Not a new feature slice and not an `intent.md` (no product intent invented).
- Not store copy, SIGN, subtitle, or bundle-id work.
- Not permission to open a ten-city or HANDOFF document.

**OBSERVED** next design work that stays inside the locks: finish run-shell (P0-1), lethal-warning copy (P0-2), Camera housing readability (P0-3), and honest juice (P0-4). Everything else on the harvest that needs new verbs waits for the expansion gate.
