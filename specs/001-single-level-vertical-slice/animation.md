# Animation and Motion Specification

Status: BASELINE  
Feature: SS-001  
Animation version: `animation-sf-001`

## 1. Principle

Animation communicates authoritative state. It may anticipate, emphasize, and settle an event, but it MUST NOT invent timing, collision, immunity, damage, or movement.

Every gameplay clip maps to an authoritative state or event. Cosmetic loops remain explicitly non-authoritative.

## 2. Motion grammar

Use three phases where the event benefits from warning:

1. **Anticipation** — communicates what will happen.
2. **Commit** — aligns with the authoritative event tick.
3. **Recovery** — communicates temporary vulnerability or completion.

The authoritative event marker belongs in clip metadata. Runtime code MUST NOT infer the event from a frame filename.

## 3. Actor state machines

### Player

`idle ↔ move → dodge → recover`  
`idle/move → hurt → prior locomotion`  
`any living → defeat`  
`eligible → extraction → complete`

Rules:

- Defeat and extraction are terminal presentation states.
- Hurt may interrupt cosmetic locomotion but not authoritative input unless the simulation says so.
- Ghost Step immunity begins and ends from simulation events, not afterimage visibility.
- Movement animation speed may follow speed bands, but animation must not change authoritative velocity.

### Standard enemy

`idle → acquire → move → anticipate → commit → recover → move`  
`living → hurt`  
`living → defeat`

Enemy roles MUST have different anticipation silhouettes and cadences. A Guard attack and Interceptor attack must be distinguishable before commit.

### Response Captain

The Captain uses a finite vocabulary:

- command pulse;
- sweep;
- targeted strike;
- reinforcement call;
- phase transition;
- stagger;
- defeat.

Each damaging action requires a telegraph record containing shape, minimum readable duration, authoritative commit tick, cancellation rule, and reduced-motion equivalent.

## 4. Clip metadata

Each clip MUST declare:

```yaml
clip_id:
actor_role:
state:
directions:
frame_ids:
frames_per_second:
loop:
anchor:
authoritative_event_marker:
cancel_windows:
blend_or_transition:
reduced_motion_clip:
audio_cue:
vfx_cue:
```

Missing required metadata fails intake.

## 5. Frame and timing guidance

| Clip | Target frames | Target duration |
|---|---:|---:|
| Idle | 4 | 600–1000 ms loop |
| Standard move | 6 | 400–650 ms loop |
| Interceptor move | 6 | 280–450 ms loop |
| Dodge/Ghost Step | 4 | 180–300 ms |
| Hurt | 2–3 | 100–220 ms |
| Standard attack anticipation | 2–4 | ≥ 250 ms |
| Standard attack commit | 1–2 | event-aligned |
| Standard defeat | 4–6 | 300–600 ms |
| Captain basic anticipation | 4–8 | ≥ 450 ms |
| Captain major anticipation | 6–12 | ≥ 700 ms |
| Captain phase change | 6–10 | 600–1000 ms |
| Extraction | 6–10 | countdown-aligned |

These are production ranges, not simulation rules. Playtest evidence may tune them while preserving required warning windows.

## 6. Direction and mirroring

- Player, Guard, and Interceptor require four-direction readability.
- Eight-direction movement may be projected from four authored directions.
- Mirroring is allowed only when asymmetrical equipment, text, insignia, lighting, or attack handedness remains correct.
- Captain attacks that depend on handedness require authored or procedurally correct direction variants.
- Anchors must remain stable across mirrored clips.

## 7. Telegraph contract

A telegraph MUST:

- appear before the damage or control event;
- use ground geometry consistent with the authoritative affected area;
- remain visible against every floor material;
- identify event class by shape, not color alone;
- avoid spawning underneath opaque HUD;
- have a reduced-motion equivalent;
- retain enough warning at maximum enemy density.

Shape language:

| Shape | Meaning |
|---|---|
| Narrow line | sweep or shot |
| Circle | local area impact |
| Cone | directional surveillance or attack |
| Broken ring | expanding or delayed area |
| Chevrons | pursuit or charge |
| Brackets | target lock |
| Segmented boundary | safe or interruptible region |

Camera fields must remain visually distinct from Captain attack cones through boundary pattern and iconography.

## 8. Hit feedback

- Hit-stop is presentation-only and capped at 50 ms for standard impacts and 90 ms for major Captain impacts.
- Screen shake is capped, user-adjustable, and disabled under Reduced Motion.
- Player damage uses directional feedback.
- Repeated low-damage events coalesce presentation to avoid flashing.
- Invulnerability feedback must remain visible without relying on rapid blinking.
- Damage numbers are optional and default off; the health/state response remains sufficient without them.

## 9. Camera motion

- Normal camera follows with bounded smoothing and a dead zone.
- Camera motion never alters authoritative coordinates.
- No combat zoom pulsing.
- Major encounter framing may use one short bounded transition before control pressure begins.
- Reduced Motion replaces travel/zoom transitions with a cut or short dissolve.
- Camera shake must not displace UI, Camera field truth, or objective markers.

## 10. Reduced Motion and Reduced Flash

When system Reduce Motion is enabled:

- disable parallax and multi-speed fog;
- replace repeated scaling with opacity or outline changes;
- remove continuous screen shake;
- replace long afterimage trails with a static echo;
- replace sliding full-screen transitions with dissolve/cut;
- preserve meaningful telegraph timing and state change.

Reduced presentation MUST remain mechanically equivalent and must not make a hazard harder to read.

## 11. Animation performance

- Animation changes textures; it does not recreate nodes each frame.
- Frame arrays are cached by clip ID.
- Encounter-critical atlases are preloaded.
- Offscreen cosmetic animation may pause or lower frequency.
- Particle counts and transient nodes remain bounded.
- No animation completion callback may mutate authoritative gameplay.
- Reused nodes reset texture, alpha, scale, rotation, blend mode, actions, shader state, and child effects.

## 12. Acceptance

Each clip family requires:

- contact-sheet review;
- anchor-drift test;
- gameplay-speed capture;
- dense-frame readability capture;
- event-marker alignment test;
- cancellation and interruption tests;
- mirroring review;
- reduced-motion capture;
- performance-floor device measurement.

A clip passes only when its purpose is recognizable before its label is shown.


## 13. Civic Seam ambient motion

Ambient motion is cosmetic and seeded separately from authoritative replay state.

Persistent candidates:

- two-height fog drift;
- slight trolley-wire sway;
- asynchronous rooftop fans;
- traffic-signal cycles;
- distinct Camera status patterns;
- occasional blinds;
- bounded paper/plastic wind channels;
- transit-display refresh;
- pigeons scattering from nearby combat.

Rare candidates:

- green parrot crossing;
- fictional autonomous vehicle hesitation;
- passing streetcar shadow;
- tower-light synchronization;
- phoenix-relief apparent blink during a beam crossing;
- occupant closing blinds;
- fog reveal of the wider network.

Rules:

- rare events must not imply collision, reward, enemy, or objective state;
- events pause or simplify under Reduced Motion where appropriate;
- events may not begin during a high-priority Captain telegraph;
- movement remains below gameplay salience;
- seeded cosmetic events do not enter authoritative state digests;
- density and device budgets may disable P1/P2 ambience before critical presentation.


## 14. Camera destruction motion

Camera motion clips/events:

- `camera_operational_idle` — emissive/status animation only; no translation or rotation
- `camera_hit` — crack/outline response only; no translation or rotation; detection uninterrupted
- `camera_critical_enter`
- `camera_destroy` — ≤ 350 ms
- `camera_field_off`
- `camera_destroyed_idle`

The field-off presentation begins from the authoritative destruction event and cannot wait for the destruction clip to finish. No animation callback changes Integrity or Camera functionality. Reduced Motion uses immediate state swaps, short outline changes, and labeled Tamper feedback.


Standard Camera position, heading, range, and field angle are immutable. Any housing animation is texture/emissive-only. The renderer must never rotate a Camera field from animation state.
