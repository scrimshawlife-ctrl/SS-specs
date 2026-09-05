# Legacy Component Admission

Status: EVALUATED_WITH_LIMITS  
Provenance date: 2026-08-24  
Amended: 2026-09-04 (LC-009, LC-010 bounded ADAPT; see §Bounded visual and audio admission)

## Immutable source

- Repository: `scrimshawlife-ctrl/Surveillance-Survivor`
- Source commit: `3b20d88d6a6e1fe8f07f45f581359d371fa65d98`
- Reference label: `legacy-multicity-2026-08-24` (annotated repository tag created 2026-09-01, tag object `e085ea8`)
- Observed core path: `Sources/SurveillanceCore/Simulation.swift`
- Observed policy path: `Sources/SurveillanceCore/SanFranciscoPolicyPhase.swift`
- Observed content path: `Sources/SurveillanceCore/Resources/bosses.json`
- Build environment and complete test result at this SHA: NOT_COMPUTABLE from available evidence
- Known product defect: legacy scope and systems are too broad and internally coupled for the one-level reboot

No legacy file may be copied wholesale. The commit is evidence only.

## Decisions

| ID | Candidate | Decision | Evidence and boundary | Runtime destination |
|---|---|---|---|---|
| LC-001 | Seeded randomness | REWRITE | Legacy injects deterministic RNG, but SS-001 fixes xoshiro256**/SplitMix64 and isolated streams. Algorithm compatibility is not established. | Determinism/RNG |
| LC-002 | Simulation timing | ADAPT | `Simulation.swift` has validated 1/60 fixed step and prevents wall-clock stepping. Retain behavior, replace surrounding state. | SimulationClock |
| LC-003 | Player movement | ADAPT | Legacy direct analog throttle and X-then-Y obstacle slide are observed and match `player-controller-001`; replace floating numeric authority. | MovementSystem |
| LC-004 | Camera LOS | REWRITE | Legacy sensor geometry is useful evidence, but rotating/multiple sensor archetypes conflict with stationary seeded sockets and exact Exposure. | DetectionSystem |
| LC-005 | Projectile pool/lifecycle | ADAPT | Legacy lifecycle reset and projectile-origin handling are useful patterns; authoritative IDs and storage must follow new contracts. | CombatSystem/ProjectileStore |
| LC-006 | Combat resolution | ADAPT | Swept-circle earliest-hit and stable-ID tie behavior are observed and fit; rewrite numeric layer, target classes, damage tables, and event emission. | CombatSystem |
| LC-007 | Enemy behaviors | REWRITE | Legacy generalized guard/boss catalogs do not implement the five exact Level 1 state machines. | EnemySystem |
| LC-008 | Extraction logic | REWRITE | Legacy boss/Blind Spot flow does not implement the required three mobs → elite → boss → 300-tick Phoenix Steps predicate. | ObjectiveSystem |
| LC-009 | Visual assets | ADAPT (bounded) | Wholesale admission is still rejected. An individual asset returns only through the asset-record process, only where its runtime role is unchanged, and only under §Bounded visual and audio admission. The legacy enemy and boss cast, non-San-Francisco packs, and literal landmark shorthand remain REJECTED. | VisualCatalog |
| LC-010 | Audio assets | ADAPT (bounded) | Wholesale admission is still rejected. A clip returns only where it carries the same gameplay meaning as a named `audio-haptics-001` event, and admission supplies a file, not an exemption from priority, coalescence, caption, or license obligations. | AudioProjector |

## Verified legacy behavior retained as specification evidence

- fixed 60 Hz simulation;
- direct analog movement throttle;
- X-then-Y solid collision slide;
- predictive projectile intercept with direct-aim fallback;
- swept projectile collision with earliest-hit and stable-ID ties;
- additive simultaneous Camera pressure;
- four Algorithmic Moderate policy-phase identities and verified ratios.

These are design provenance, not permission to copy code.

## Default exclusions

City selection, ten-city campaign authority, district procedural generation, challenge systems, generalized city profiles, legacy upgrade catalog, multiple characters, inventory/crafting, global state containers, store-launch scope, and non-SF runtime assets are REJECTED for SS-001.

## Bounded visual and audio admission

Added 2026-09-04. This section is the only route by which a legacy file may
enter the runtime bundle.

### Source of truth

`scrimshawlife-ctrl/Surveillance-Survivor@3b20d88d6a6e1fe8f07f45f581359d371fa65d98`
is the sole admission source and remains immutable evidence.

`Zero-State-LLC/Surveillance-Survivor` holds the same art and is where a reader
is likely to look for it, but it is a **separate history**: the frozen commit
does not exist there, and six San Francisco files have been re-authored since
the freeze. It is not an admission source. Moving the pin is a separate change.

### Admission test

A legacy asset may be admitted only when every line holds:

1. **Role identity.** Its runtime role in SS-001 is the same role it had in the
   legacy build. A player frame may back a player clip; a surveillance-camera
   frame may back a Camera clip. A guard frame may not back a Civic Seam enemy,
   because LC-007 already records that the legacy enemies are not this cast.
2. **Per-asset record.** An `asset-record-001` entry exists whose `sha256` is
   the digest of the file at the frozen commit, with real `dimensions`,
   `colorSpace`, and `alpha`, and a `source` naming the frozen commit.
3. **Authored geometry.** The delivered frame is resampled to the
   `visual-language-001` sprite box for its role. Legacy pixel dimensions carry
   no authority.
4. **No inference.** Collision, targeting, Camera fields, and anchors come from
   the authored contracts, never from the admitted image.
5. **Audio obligations survive.** An admitted clip still owes its
   `audio-haptics-001` priority, coalescence, caption, and license duties.

### Admitted set

| Legacy family | Backs | Note |
|---|---|---|
| `player_walk_{up,right,down,left}` | `player_move` | exact, 24 frames |
| `player_idle_{up,right,down,left}` | `player_idle` | partial, 8 of 16 |
| `player_damage` | `player_hurt` | 12 frames |
| `player_defeat` | `player_defeat` | 20 frames |
| `player_extract` | `player_extraction` | 32 frames |
| `lpr_scan_loop`, `lpr_damaged`, `lpr_destroyed`, `lpr_destroy_sequence`, `fx_camera_disabled`, `fx_camera_destroyed` | every `camera_*` clip | complete, 16 frames |
| `projectile_kinetic` | Civic Pulse projectile presentation | — |
| `suspicion_tier_0…5` | Detection state icons | non-colour carrier only |
| San Francisco `terrain`, `decal`, `overlay`, `prop`, `skyline`, `landmark_cable_track`, `landmark_victorian_midground`, `landmark_comms_tower` | Civic Seam environment | `landmark_bridge_distant` stays REJECTED under T807 |
| `sfx_weapon_fire`, `sfx_countermeasure_hit`, `sfx_player_damaged`, `sfx_player_defeated`, `sfx_lpr_destroyed`, `sfx_suspicion_tier_up`, `sfx_extraction_opened`, `sfx_extraction_completed`, `sfx_upgrade_selected`, `sfx_camera_scan_sweep`, `sfx_blind_spot_field_loop` | 13 of the 24 `audio-haptics-001` event IDs | one clip may back several IDs |
| `music_san_francisco_run_loop`, `music_san_francisco_boss_loop`, `amb_san_francisco_city_identity_loop` | music and ambience buses | 3 of 6 music states |

### Individually admissible non-San-Francisco cues

Amended 2026-09-05. T102 excludes non-San-Francisco content because SS-001 is
one San Francisco level, not a ten-city campaign. That purpose is served by
excluding **city identity** — packs, profiles, districts, campaign authority,
and any asset that would make another city legible on screen.

A single sound effect carries no city identity. It is heard once, names nothing,
and shows nothing. Excluding one whose gameplay meaning exactly matches a named
`audio-haptics-001` event costs the player a warning and buys no protection.

So an **individual** non-San-Francisco cue may be admitted when all hold:

1. it is a single `sfx_` or `stinger_` asset, never a pack, profile, or set;
2. its recorded authoring intent in the frozen `AUDIO_ASSET_MANIFEST.json` is
   the same gameplay meaning as a named `audio-haptics-001` event, and the
   record quotes that intent;
3. it names no city, landmark, or district in anything the player can hear or
   read, and its admitted asset ID carries no city name;
4. it satisfies the § Admission test above in full.

Music, ambience, and city packs stay excluded by default. The one exception is
named below.

### Boss phase beds

Amended 2026-09-05, and this one is a real trade rather than a clean case.

The Algorithmic Moderate has four canonical phases. The frozen commit holds four
Atlanta final-boss phase loops written for exactly that structure, escalating in
the same direction: institutional certainty, unification, relentless
optimisation, then collapse. No other source in the library has per-phase boss
music, and the alternative is one loop repeating across the whole encounter.

These four beds are admitted:

| Boss phase | Source |
|---|---|
| Public Safety | `music_atlanta_boss_phase_1_loop` |
| Civil Liberties | `music_atlanta_boss_phase_2_loop` |
| Temporary Safeguard | `music_atlanta_boss_phase_3_loop` |
| Independent Review | `music_atlanta_boss_phase_4_loop` |

**What this trades.** A music bed colours a whole state, so it carries more
identity than a one-shot cue does, and phase two's authoring intent explicitly
interlocks motifs from ten cities. A listener cannot name a city from an
instrumental loop, and no city name reaches an asset ID, a caption, or the
screen — but this is admitted on judgement, not on the clean "a one-shot names
nothing" argument that governs the cues above. It is recorded that way on
purpose.

No other city music is admitted. Run loops, city ambience, and city identity
beds stay excluded.

### Approximate substitution

Amended 2026-09-05. Two events have no legacy sound that carries their meaning,
because the legacy build never had them: it had no Dodge, and no countdown
metronome. Silence is a worse default than an imperfect sound for both — a
Dodge with no feedback reads as a dropped input, and a countdown the player
cannot hear cannot be timed.

So a cue may take the **nearest applicable** legacy sound when all hold:

1. no asset carries the event's meaning, and the search is recorded;
2. the record says plainly that the substitution is approximate, so the catalog
   never claims a precision it does not have;
3. the substitution introduces no confusion — it does not reuse a sound already
   carrying a different event the player can hear in the same run;
4. it is marked for replacement. These are the first two cues an original-audio
   pass should replace.

| Event | Source | Why it is the nearest, and what is imperfect |
|---|---|---|
| `player_dodge` | `sfx_san_francisco_hidden_sensor_fog` | "moist air shifts … sensor itself remains acoustically obscured" is the only moving-air sound in the library, and becoming unseen is what a Dodge does. Imperfect: it is authored as a sensor activating, and at 0.9–2s it is long for a 12-tick Dodge |
| `extraction_tick` | `sfx_interactable_activate` | "transformer pad clunk … brief electrical stress pop" is the shortest unused discrete mechanical step, and nothing else is unused and dry enough to repeat once a second. Imperfect: it is authored as an environmental activation, not a metronome |

Both are San Francisco or non-city assets, so neither widens the city boundary.
No further approximate substitution is authorised: every other event either has
an exact match or stays a project original.

| Event | Source | Why the meaning matches |
|---|---|---|
| `daemon_dash` | `sfx_louisville_map_redaction` | "black paper strip slides across glass … camera relay disappears behind an opaque mechanical shutter" — the elite's attack is a Redaction Dash |
| `boss_defeated` | `stinger_atlanta_final_blind_spot` | "network links snap and fall silent from the edges inward … server cathedral powers down" — the final authority collapsing |
| `extraction_reset` | `sfx_los_angeles_private_network_persist` | "municipal relay powers off, then nodes wake independently and reconnect" — a system reasserting itself after it looked beaten |

### Still REJECTED

- The legacy enemy cast (seven generic guards) and the legacy boss (Shift
  Manager). LC-007 REWRITE stands: these are not the Civic Seam five, the
  Improper Search Daemon, or the Algorithmic Moderate.
- Every non-San-Francisco city **pack** — music, ambience, environment, and
  profile — under T102. Only the individual cues named above return, and only
  under the conditions above.
- `san_francisco_landmark_bridge_distant_01` and any literal landmark, seal, or
  logo shorthand (T807).

### Partial coverage is a defined state

The admitted set backs 112 of the 408 `clip-metadata-001` frame IDs and 13 of
the 24 audio event IDs. Partial coverage is legal. For any frame ID with no
accepted asset the runtime MUST fall back to the authored grayscale silhouette
or shape for that role, and MUST NOT substitute a frame from another role,
another direction, or another clip. A missing audio ID plays nothing and its
caption still appears.

Coverage is therefore observable: what is backed is drawn from the atlas, what
is not is drawn as blockout, and neither state is silent about itself.

## Copy gate

A runtime pull request that copies or ports legacy source must cite the candidate ID, exact source lines at the frozen commit, destination contract, and new tests. REWRITE and REJECT decisions prohibit source copying. ADAPT permits bounded reimplementation after review, not file transfer.
