# Camera Destruction Mechanic

Status: CANONICAL  
Feature: SS-001  
Contract version: `camera-destruction-001`

## 1. Intent

Camera destruction gives the Player a permanent, local way to reshape surveillance geometry during a run. It is a tactical trade:

- benefit: remove one Camera field for the rest of the run;
- cost: remain in attack range long enough to land three impacts and receive a network-visible Tamper Spike;
- limit: destroying a Camera does not erase existing Exposure, create a magical safe bubble, produce loot, or remove other Cameras.

Cameras are infrastructure, not ordinary enemies.

## 2. Scope

This contract applies to standard Level 1 Camera entities:

- Municipal Dome
- Storefront Camera
- Traffic Reader
- Ornamental Civic Camera
- Temporary Sensor Mast

Housing family changes appearance only. All five use the same destruction rules.

The **Captain Camera** is an attack emitter owned by the Response Captain. It is not a standard Camera entity and is not independently destructible in SS-001.

## 3. Canonical constants

```yaml
camera_integrity_max: 3
integrity_damage_per_valid_impact: 1
exposure_scale:
  min: 0
  max: 1000
tamper_spike_per_destroyed_camera: 100
destroyed_camera_respawns_during_run: false
camera_drops_loot: false
camera_destruction_creates_area_effect: false
standard_camera_count: 8
camera_position_changes_during_run: false
camera_heading_changes_during_run: false
camera_field_geometry_changes_during_run: false
```

Tuning these values changes `camera-destruction-001` and requires golden-vector review.

## 4. State machine

```text
OPERATIONAL(3) ──impact──> DAMAGED(2)
DAMAGED(2) ──impact──> CRITICAL(1)
CRITICAL(1) ──impact──> DESTROYED(0)
```

### OPERATIONAL, DAMAGED, and CRITICAL

- Remain fully functional Cameras.
- Use identical fixed field angle, fixed range, fixed heading, detection contribution, and network behavior.
- Damage does not shorten range, interrupt detection, rotate the field, or reduce Exposure.
- Visual damage state MUST NOT imply mechanical impairment.

### DESTROYED

- Is not targetable.
- Produces no Camera field or detection contact.
- Never returns to another state during the run.
- Keeps only the collision footprint of its permanent mount/base.
- Adds no new blocking debris.
- Returns to its authored initial state only on a complete restart/new run.

## 5. Valid damage

A valid Camera impact requires:

1. source is the Player base projectile or an eligible Ricochet continuation;
2. target Camera is OPERATIONAL, DAMAGED, or CRITICAL;
3. projectile collision occurs against the authoritative Camera hit shape;
4. projectile has not already damaged that Camera;
5. no blocking geometry invalidated the projectile path before collision.

Every valid impact removes exactly one Integrity point. Player damage statistics, critical-hit rules, enemy damage modifiers, and Camera housing family do not alter Integrity damage.

The following cannot damage Cameras:

- contact with the Player;
- Guard, Interceptor, or Captain attacks;
- Camera fields;
- Ghost Step;
- Signal Jammer;
- VFX, debris, fog, or ambient events.

Friendly or enemy attacks never destroy Cameras in SS-001.

## 6. Auto-targeting

Cameras participate in the deterministic automatic-target candidate set when they are:

- damageable;
- inside the current weapon's authoritative attack range;
- reachable by the weapon's authoritative line-of-fire rule.

Candidate priority is:

| Priority | Candidate class |
|---:|---|
| 1 | Enemy within 96 world units of the Player |
| 2 | Camera currently detecting the Player |
| 3 | Other enemy |
| 4 | Other damageable Camera |

Within the same class, select:

1. smallest squared distance from Player to target anchor;
2. then lowest stable entity ID.

Target selection occurs only at an authoritative attack opportunity. A target is not continuously locked between attacks. If the chosen target becomes invalid before projectile creation, that attack opportunity produces no projectile; it does not retarget inside the same tick.

A Camera behind blocking geometry is not a valid candidate even when its field can reach the Player by a different path.

## 7. Ricochet Pulse

Ricochet Pulse may damage Cameras.

- A projectile may damage a given Camera at most once.
- A ricochet candidate uses the same damageable and line-of-fire validation.
- Ricochet candidate ordering is nearest valid target, then stable entity ID.
- A Camera destroyed by the first impact is excluded from continuation candidates immediately.
- One projectile may destroy multiple Cameras in one tick if every continuation is valid.
- Each destroyed Camera produces its own Tamper Spike.

Signal Jammer and Ghost Step change their specified systems only; they do not modify Camera Integrity.

## 8. Destruction resolution and Exposure

Destroying a Camera produces:

```text
CameraDestroyed(cameraID, tick, sourceProjectileID, priorDetectionContact)
ExposureDelta(reason: cameraTamper, amount: +100, cameraID)
```

Rules:

- Tamper Spike is applied exactly once when Integrity crosses from 1 to 0.
- It is applied even when the Camera was not detecting the Player.
- It stacks additively when multiple Cameras are destroyed on one tick.
- Exposure clamps at 1000.
- Tamper Spike may cross any Detection State threshold and may trigger Lockdown.
- Destruction does not directly lower Exposure.
- If no surviving Camera detects the Player, normal recovery eligibility begins on the next simulation tick under the Exposure contract.
- Destroying a Camera does not create an explicit Blind Spot entity. The safe space is only the geometric absence of that field.

A repeated damage event against an already destroyed Camera is ignored and produces no Tamper Spike.

## 9. Tick order

The authoritative tick order relevant to Camera destruction is:

1. consume normalized Player command;
2. resolve movement and collision;
3. read each Camera's immutable authored position, heading, range, and field angle;
4. sample Camera detection contacts;
5. select automatic-attack target and create eligible projectiles;
6. advance projectiles and collect collisions;
7. resolve ordered damage, Integrity transitions, destruction, and Player/enemy death;
8. remove contacts belonging to Cameras destroyed on this tick;
9. apply surviving Camera contact Exposure deltas;
10. apply ordered Tamper Spikes by Camera stable ID;
11. clamp Exposure and resolve Detection State/Lockdown transitions;
12. resolve spawns and objectives;
13. publish ordered events and receipt data.

Consequences:

- A Camera destroyed on a tick contributes no continuous detection Exposure on that same tick.
- Its +100 Tamper Spike still applies.
- Other Camera contacts still contribute.
- If destruction and Player death occur on the same tick, both are recorded; Player death remains terminal.
- If multiple Cameras are destroyed, events are ordered by stable Camera ID.

## 10. Collision and navigation

Each Camera definition has separate shapes:

- `mountCollisionShape`: permanent world obstruction, if any;
- `cameraHitShape`: projectile target;
- `fieldOrigin`: line-of-sight origin;
- `targetAnchor`: targeting and distance anchor.

On destruction:

- authored position, heading, and mount remain unchanged;
- `cameraHitShape` is disabled;
- `fieldOrigin` is disabled;
- `mountCollisionShape` remains unchanged;
- transient debris has no collision;
- no navigation path opens or closes unless explicitly authored as a separate arena event.

Visual bounds never define any authoritative shape.

## 11. Presentation

### Integrity states

| Integrity | State | Required presentation |
|---:|---|---|
| 3 | Operational | intact housing, stable status pattern |
| 2 | Damaged | one visible crack/dent plus single-notch integrity marker |
| 1 | Critical | exposed/sparking detail plus double-notch marker |
| 0 | Destroyed | collapsed/dark head, broken-lens silhouette, no active field |

Damage state must remain distinguishable in grayscale and without rapid blinking.

### Valid impact

- compact directional spark;
- one distinct hard-material impact sound;
- a crack/outline response that does not translate or rotate the housing;
- optional light haptic, subject to user settings;
- no detection interruption.

### Destruction

- mechanical break event no longer than 350 ms;
- 4–8 bounded particles;
- field retracts or collapses immediately from the authoritative event;
- short network-disconnect audio cue;
- +100 Tamper Spike shown as a labeled Exposure increment;
- destroyed housing settles into a stable non-emissive state.

Reduced Motion replaces recoil, field collapse, and debris motion with:

- immediate broken-state swap;
- short outline change;
- labeled Tamper Spike;
- audio/haptic equivalents when enabled.

No full-screen flash or camera shake is required.

## 12. HUD and player communication

On the first damageable Camera encounter, teach once:

`CAMERAS: 3 HITS • DESTRUCTION ADDS EXPOSURE`

Requirements:

- The optional objective HUD shows `CAMERAS destroyed/8`; Camera Integrity is shown by three compact notches when the Camera is targeted, damaged, or within attack range.
- The Tamper Spike displays `+100 TAMPER` adjacent to the Exposure HUD.
- The Camera field disappears immediately at destruction.
- No loot icon or pickup sound is used.
- Destroyed Cameras remain visually identifiable on return traversal.
- Tutorial communication is available through VoiceOver and captions.

## 13. Audio

Required event IDs:

- `camera_hit_01`
- `camera_hit_02`
- `camera_critical`
- `camera_destroy`
- `camera_network_tamper`
- `camera_field_off`

Audio priority:

1. Player lethal warning;
2. Camera destruction/Tamper confirmation;
3. Camera impact;
4. ambient machinery.

Repeated impacts coalesce to prevent mix overload. Audio is supportive and never the sole state carrier.

## 14. Optional objective: Network Blackout

Level 1 contains exactly eight standard Cameras. All eight are authored at run start, operational, stationary, and accessible before Extraction.

Objective state:

```text
INCOMPLETE: camerasDestroyed < 8
COMPLETE: camerasDestroyed == 8
```

On the eighth distinct destruction, publish exactly once:

```text
AllCamerasDestroyed(tick, destroyedCount: 8, totalCount: 8)
```

Rules:

- Network Blackout is an optional secondary objective.
- It is never an Extraction prerequisite.
- Extraction remains valid with 0–7 Cameras destroyed.
- No Camera spawns, activates, repairs, relocates, rotates, or respawns during the run.
- Completion grants a result-screen accolade and receipt field only; it grants no combat power, loot, score multiplier, or progression in SS-001.
- The HUD counter is visible after the first Camera is damaged and may be pinned through settings.
- If the Player extracts without completing it, the receipt reports partial progress.

## 15. Extraction independence

The Extraction unlock predicate contains no Camera condition. It depends on the required combat objective graph in `encounter-objectives.md`: required mob encounters, the canonical elite sub-boss, and the canonical boss.

Camera destruction may make traversal safer, but neither a specific Camera nor Network Blackout may gate the boss, elite, or Extraction.

## 16. Receipt and telemetry

Run receipt summary:

```json
{
  "camerasDamaged": 0,
  "camerasDestroyed": 0,
  "tamperExposureApplied": 0,
  "cameraObjective": { "destroyed": 0, "total": 8, "complete": false },
  "cameraDestructions": [
    {
      "cameraId": "string",
      "tick": 0,
      "housingFamily": "municipalDome",
      "wasDetectingPlayer": false,
      "source": "baseProjectile|ricochet",
      "exposureBefore": 0,
      "exposureAfter": 100,
      "triggeredLockdown": false
    }
  ]
}
```

Telemetry is local receipt data only. No external analytics or network submission is added.

## 17. Edge cases

- Two projectiles hit an Integrity-1 Camera on one tick: first ordered hit destroys it; later hits are ignored.
- Ricochet destroys two Cameras on one tick: both events and +200 total Tamper apply in stable-ID order.
- Camera is destroyed while detecting: its continuous contribution is removed before Exposure accumulation; Tamper remains.
- Camera is destroyed at Exposure 950: Exposure becomes 1000 and Lockdown triggers.
- Camera is destroyed at Exposure 1000: Exposure remains 1000; destruction is still recorded.
- Restart after destruction: all eight Cameras restore Operational state at their immutable authored transforms.
- Player dies on the destruction tick: failure outcome stands; destruction remains in the terminal receipt.
- Destroyed Camera mount blocks a path: mount collision remains exactly as before destruction.
- Camera field VFX lingers from interpolation: renderer must clear it within the same presented authoritative update; lingering field is a presentation defect.

- Eighth Camera destruction: Network Blackout completes exactly once; Extraction predicate is unchanged.
- Extraction with zero Cameras destroyed: valid when all required combat objectives are complete.
- Extraction with seven Cameras destroyed: valid and receipt reports 7/8 incomplete.

## 18. Golden vectors

Minimum canonical vectors:

| ID | Scenario | Expected outcome |
|---|---|---|
| CD-001 | Three sequential base impacts | states 3→2→1→0; one +100 Tamper |
| CD-002 | Two impacts only | CRITICAL; field remains fully active |
| CD-003 | Destroy while detecting | no same-tick contact delta; +100 Tamper |
| CD-004 | Destroy while not detecting | +100 Tamper; no field |
| CD-005 | Two simultaneous final impacts | one destruction; one Tamper |
| CD-006 | Ricochet destroys two Cameras | two ordered destructions; +200 Tamper |
| CD-007 | Destroy at Exposure 950 | clamp 1000; Lockdown |
| CD-008 | Hit destroyed Camera | ignored |
| CD-009 | Restart | all eight Operational at fixed transforms |
| CD-010 | Camera destruction plus Player death | failure plus destruction receipt |
| CD-011 | Equal-distance target tie | lowest stable entity ID selected |
| CD-012 | Eighth destruction | one Network Blackout event; 8/8 complete |
| CD-013 | Extract at 0/8 | succeeds when combat graph complete |
| CD-014 | Extract at 7/8 | succeeds; objective remains incomplete |

## 19. Non-goals

SS-001 does not include:

- hacking or converting Cameras;
- Camera loot or salvage;
- variable Camera armor;
- critical damage against Cameras;
- enemy-friendly fire against Cameras;
- repair or respawn;
- chain explosions;
- permanent progression from Camera destruction;
- achievements that encourage farming;
- a separate infrastructure-alarm meter;
- manual aiming or tap-to-target solely for Cameras;
- rotating, panning, patrolling, relocating, spawning, or dynamically activated Cameras.
