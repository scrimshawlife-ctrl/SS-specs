# Global Simulation Order

Status: CANONICAL  
Contract version: `simulation-order-001`

Every authoritative tick executes these phases exactly once and in this order:

| Phase | Operation |
|---:|---|
| 1 | Reject completed/invalid run; increment tick |
| 2 | Consume normalized Player command and upgrade choice |
| 3 | Advance cooldowns, durations, and encounter timers |
| 4 | Resolve Player dodge/ground movement and solid collision |
| 5 | Resolve enemy intentions, movement, and collision |
| 6 | Sample fixed Camera detection contacts |
| 7 | Evaluate automatic attacks; allocate projectiles |
| 8 | Move projectiles; collect world/entity intersections |
| 9 | Resolve ordered damage and Camera Integrity transitions |
| 10 | Resolve destruction/deaths and invalidate dead targets |
| 11 | Remove contacts from Cameras destroyed this tick |
| 12 | Resolve threat contact damage; resolve Player death |
| 13 | Resolve continuous Exposure/recovery, then ordered Tamper Spikes |
| 14 | Resolve Detection State and one-time Lockdown entry |
| 15 | Resolve encounter completion, director decisions, and spawns |
| 16 | Resolve boss phase/defeat and arm Extraction if eligible |
| 17 | Resolve Extraction occupancy/countdown/completion |
| 18 | Emit sorted events, update receipt, compute state digest |

## Terminal precedence

Player death outranks every success on the same tick. Camera destruction and enemy/boss deaths still appear in the terminal receipt, but no objective, boss defeat, or Extraction event may convert failure to success. Once terminal, future `step` calls return no events and do not increment tick.

## Stable ordering

Unless a narrower contract says otherwise:

1. phase number;
2. event type ordinal from the event schema;
3. primary entity ID;
4. secondary entity ID;
5. insertion sequence.

Collections may use any storage structure, but iteration affecting authority must materialize this order. Floating display time, hash-map order, SpriteKit node order, audio, haptics, particles, animation callbacks, and render refresh rate are forbidden inputs.

## Numeric and RNG rules

- Positions, velocities, time counters, Exposure, Integrity, and damage use integers/fixed-point as their contracts specify.
- No authoritative branch compares platform `Float`, `Double`, wall clock, locale, or random framework APIs.
- RNG is `xoshiro256**`, seeded from SplitMix64 expansion of the unsigned 64-bit run seed.
- Each call returns one UInt64 and advances exactly once.
- Content choices use rejection sampling, never modulo reduction, when the range is not a power of two.
- Cosmetic RNG uses a separate seed/stream and is excluded from digest and receipt authority.

## State digest

At phase 18, serialize authoritative state as canonical JSON: UTF-8, sorted keys, no insignificant whitespace, decimal integers only, arrays already in stable-ID/order sequence. Hash with SHA-256 lowercase hex. Exclude presentation, device, elapsed wall time, audio/haptic settings, and cosmetic seeds.

The digest input includes contract versions, seed, tick, Player state, live authoritative entities, Camera state, Exposure state, encounter/objective state, upgrade state, timers, allocator next ID, and authoritative RNG state.

## Version identity

A replay is executable only when all identities exactly match:

- `rulesetVersion`
- `contentVersion`
- `arenaVersion`
- `schemaVersion`

Unknown/mismatched versions fail closed before tick 1. Golden results may change only with an explicit version bump and decision-register rationale.
