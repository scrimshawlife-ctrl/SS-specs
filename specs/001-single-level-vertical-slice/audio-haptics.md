# Audio and Haptics Contract

Status: CANONICAL  
Contract version: `audio-haptics-001`

Audio and haptics project authoritative events. They never create, delay, cancel, or acknowledge gameplay state.

## Mix buses

| Bus | Default | Range |
|---|---:|---:|
| Master | 100% | 0–100 |
| Music | 70% | 0–100 |
| Effects | 85% | 0–100 |
| Voice/captions | 100% | 0–100 |
| Haptics | 80% | 0–100 |

Settings are local, independent, and excluded from replay authority.

## Priority

1. Player death and lethal warning
2. Boss major telegraph and Extraction completion
3. Lockdown and Detection State escalation
4. Camera destruction/Tamper and objective completion
5. Player damage and hostile projectile
6. Weapon/Civic Pulse and Camera impact
7. UI
8. ambience

At most eight effects voices play simultaneously. A higher-priority event steals the oldest lowest-priority voice; ties steal oldest sequence. Music and voice/captions do not consume effect voices.

## Event map

| Event | Audio ID | Haptic |
|---|---|---|
| Weapon fired | `weapon_civic_pulse` | none |
| Enemy hit | `impact_enemy` | none |
| Player damaged | `player_damage` | light |
| Dodge start | `player_dodge` | light |
| Camera hit | `camera_hit_01/02` alternating by Camera hit count | light |
| Camera critical | `camera_critical` | warning |
| Camera destroyed | `camera_destroy` then `camera_field_off` then `camera_network_tamper` (same tick; D-060) | rigid |
| Detection escalated | `exposure_state_up` | warning |
| Lockdown entered | `lockdown_enter` | heavy |
| Upgrade selected | `upgrade_selected_<id>` | success |
| Elite telegraph | `daemon_query` or `daemon_dash` | warning |
| Boss phase | `boss_phase_<id>` | heavy |
| Boss major telegraph | `boss_telegraph_<attack>` | warning |
| Boss defeated | `boss_defeated` | success |
| Extraction armed | `extraction_armed` | success |
| Countdown second | `extraction_tick` | light |
| Extraction reset | `extraction_reset` | warning |
| Run success | `run_success` | success |
| Player death | `player_death` | heavy |
| Network Blackout | `network_blackout` | success |

## Coalescence

- Weapon fire: maximum one voice per 6 ticks.
- Enemy impacts: maximum two voices per tick; use highest actual damage then lowest target ID.
- Player damage: maximum one voice/haptic per 15 ticks.
- Camera hits: one per Camera per tick.
- Multiple Camera destructions: play one destruction per Camera, but one Tamper cue whose pitch variant encodes count 1, 2, or 3+.
- Detection transitions: one old-to-final cue per tick.
- Countdown: one cue when displayed integer changes.

## Music states

`explore → observed → lockdown → boss → extraction → terminal`

Music crossfades over 1.0 seconds except terminal, which begins within 100 ms. Music state reads the authoritative run state; crossfade time is presentation-only. Reduced sensory settings may disable music layers without changing cues/captions.

Each state names one music asset, and ambience is a separate bus. These are asset identities, not event IDs — they are continuous beds, so they carry no priority, coalescence, or voice cost, and they never consume an effects voice.

| Music state | Asset ID |
|---|---|
| explore | `music_explore` |
| observed | `music_observed` |
| lockdown | `music_lockdown` |
| boss | `music_boss` |
| extraction | `music_extraction` |
| terminal | `music_terminal` |
| (ambience bed) | `ambience_civic_seam` |

`presentation-assets-001` registers them as `musicAssetIds` so the runtime bundle filter can reach them; without that registration a delivered music file is unreachable and cannot ship. A state whose asset is not accepted plays no music, and the run continues on the remaining beds.

### Boss phase beds

The `boss` state is one state, and the Algorithmic Moderate passes through four canonical phases inside it. The state machine does not change: the run is in `boss` throughout. What changes is which bed that state plays.

| Boss phase | Asset ID |
|---|---|
| Public Safety | `music_boss_publicSafety` |
| Civil Liberties | `music_boss_civilLiberties` |
| Temporary Safeguard | `music_boss_temporarySafeguard` |
| Independent Review | `music_boss_independentReview` |

Phase is authoritative run state, so selecting the bed from it introduces no new authority. A phase change crossfades over the same 1.0 seconds as any other music transition, and phase cannot move backward, so the beds only ever escalate.

A phase whose bed is not accepted falls back to `music_boss`. That keeps the encounter scored when the set is incomplete, which is the same partial-coverage rule the visual clips follow.

## Accessibility

Every safety-critical audio event has a visual caption/event equivalent. Haptics are never the only carrier. Captions identify source direction in eight sectors when the source is offscreen. Caption history retains the last eight messages and is cleared on restart.

## Acceptance vectors

| ID | Scenario | Expected |
|---|---|---|
| AH-001 | nine simultaneous effects | priority/age voice stealing; max eight |
| AH-002 | three Camera destructions same tick | three breaks, one 3+ Tamper cue |
| AH-003 | repeated contact damage | one cue per 15 ticks |
| AH-004 | audio/haptics disabled | gameplay digest unchanged |
| AH-005 | offscreen major telegraph | directional caption present |
| AH-006 | Reduced Flash/Motion | cue meaning unchanged |
