# Camera Placement Contract

Status: CANONICAL  
Contract version: `camera-placement-001`

## Rule

Level 1 selects eight Camera placements at run initialization. Selection changes between seeds but is deterministic for the same seed and version. After selection, every Camera remains stationary with an immutable heading, range, and field angle until the run ends.

Randomization chooses from authored, reviewed sockets. It never creates coordinates, angles, ranges, collision, or fields procedurally.

## Socket inventory

The arena manifest must provide at least 18 enabled sockets distributed as follows:

| Zone | Required selected | Minimum enabled sockets |
|---|---:|---:|
| Z-02 Camera Corridor / Transit Cut | 2 | 4 |
| Z-03 Civic Plaza | 1 | 3 |
| Z-04 Pressure Route / Service Seam | 2 | 4 |
| Z-05 Lockdown Ring / Grid Junction | 2 | 4 |
| Z-06 Captain Court | 1 | 3 |
| Z-01 Spawn Alley | 0 | 0 |
| Z-07 Phoenix Steps | 0 | 0 |

Each socket declares:

- stable `socketId` unique within the arena version;
- zone and position;
- fixed heading, range, and field angle;
- housing families allowed at that mount;
- mount collision, hit shape, field origin, and target anchor;
- `tutorialEligible`, `returnVisible`, and `enabled` flags;
- symmetric incompatibility list of socket IDs that may not coexist.

All enabled sockets and every legal eight-socket result must already pass reachability, line-of-fire, route, telegraph, and viewport review. Runtime randomization is not a substitute for authored validation.

## Deterministic selection

Placement owns a dedicated RNG stream and cannot consume or perturb combat, encounter, upgrade, or cosmetic RNG.

```text
streamConstant = 0x43414D4552413031  // ASCII CAMERA01
placementSeed = SplitMix64(runSeed XOR streamConstant)
rng = Xoshiro256StarStar(SplitMix64-expand placementSeed)
```

Selection algorithm:

1. Read enabled sockets sorted by UTF-8 byte order of `socketId`.
2. Validate minimum pool sizes, socket geometry, symmetric incompatibilities, and zone membership.
3. Process zones in order Z-02, Z-03, Z-04, Z-05, Z-06.
4. For each zone, Fisher–Yates shuffle its socket list using rejection-sampled RNG indices.
5. Depth-first select the required count, trying shuffled sockets in order.
6. Reject a candidate if incompatible with any already selected socket.
7. The selected Z-02 set must include at least one `tutorialEligible` socket.
8. The full set must include at least four distinct housing families and at least four `returnVisible` sockets.
9. Accept the first complete valid set. If none exists, fail arena validation and refuse to start the run.

The search order, not dictionary/set iteration, is authoritative. A rejected candidate consumes no extra RNG; all randomness is fixed by the five initial shuffles.

## Identity assignment

After selection, sort the eight sockets by `socketId`. Assign Camera entity IDs from the normal monotonic allocator in that order. Socket identity and Camera entity identity are both recorded. Housing family is the first allowed family after a per-socket Fisher–Yates shuffle using the same placement stream after all zone shuffles.

## Runtime immutability

Once initialized:

- no Camera or socket is added, removed, activated, relocated, rotated, rerolled, or replaced;
- damage and destruction do not change the mount transform;
- restarting the same seed and versions reproduces the same selection;
- starting a different seed may produce a different legal selection;
- restoring a replay uses the recorded seed and versions, never a saved list that bypasses validation.

## Fairness invariants

Every legal generated layout must satisfy:

- no Camera contact or hostile Camera field in protected Z-01;
- no required choke covered by more than two Camera fields;
- every Camera can be hit three times with Civic Pulse from at least one reachable standing region;
- at least one zero-contact route segment exists between consecutive encounter zones;
- neither branch of Z-04 is made impassable;
- Captain major-telegraph safe regions remain reachable;
- Extraction remains completable with zero Cameras destroyed;
- all eight Cameras are accessible before Extraction completion;
- no selected field origin begins inside solid geometry;
- no two selected mounts or hit shapes overlap.

These invariants are exhaustively evaluated against every legal result during content CI. Runtime performs the cheaper manifest and selected-set assertions before tick 1.

## Receipt

```json
{
  "cameraPlacementVersion": "camera-placement-001",
  "placementSeed": 0,
  "selectedSockets": [
    {
      "socketId": "cam-z02-a",
      "cameraEntityId": 1,
      "housingFamily": "municipalDome"
    }
  ]
}
```

Selected sockets are ordered by `socketId`. The receipt does not need to repeat geometry because `arenaVersion` identifies the immutable socket manifest.

## Golden vectors

| ID | Scenario | Expected |
|---|---|---|
| CP-001 | same seed and versions, ten restarts | identical sockets, housings, and entity IDs |
| CP-002 | placement generation | exactly 2/1/2/2/1 Cameras by zone |
| CP-003 | legal result | at least one tutorial socket, four housing families, four return-visible sockets |
| CP-004 | incompatible pair shuffled first | pair never coexists; deterministic next choice |
| CP-005 | insufficient zone pool | run rejected before tick 1 |
| CP-006 | no complete compatible set | arena validation failure; no fallback layout |
| CP-007 | different seeds across corpus | more than one legal layout observed |
| CP-008 | Camera destroyed then same-seed restart | original selected layout restored Operational |
| CP-009 | placement RNG consumption changes | combat RNG golden sequence unchanged |
| CP-010 | enumerate every legal result | every fairness invariant passes |

## Non-goals

- moving or rotating Cameras during play;
- random coordinates or fields;
- difficulty-based Camera count;
- mid-run rerolls;
- hidden fallback positions;
- random Camera statistics;
- Camera placement as an Extraction gate.
