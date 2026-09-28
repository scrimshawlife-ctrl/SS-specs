# T901 evidence — deterministic replay across host and simulator configurations (partial)

**Status asked:** record as **PARTIAL**. T901 stays open. Replays pass on every configuration available on this Mac, but the reconciliation row asks for "linked device replay results across the matrix (B-002)". No physical device has run them.

**Runtime:** SS-runtime `evidence/t305-t901-pacing-replay-probes` (`06561a9`), on `main` `59e5e4b`, spec pin `cd77770`. Nothing under `Sources/` changed, so every golden vector and digest is as pinned.

## What the matrix names

- `fixtures/replay-matrix-001.json` has one entry. `RM-001` is `replay-smoke-001`: 5 ticks, triple run required, expected digest `d0639d50…6de4`.
- `plan.md` §10 names four physical classes: iPhone SE (3rd generation), iPhone 12, the current standard iPhone, and the current iPhone Pro. It says "Routine CI uses SE-class and current-standard simulators."
- B-002 and B-016 require the golden replays and `kernel-vectors-001` to pass "on every supported architecture and target device".

RM-001 is 5 ticks and never reaches an encounter. Each configuration therefore also replayed a **piloted legal run**: seed 1, Ricochet Pulse, 9227 ticks through M-A, M-B, M-C, and the elite (defeated at tick 7389), then into the boss fight, ending in Player death at tick 9227. Its commands are re-executed three times and must reproduce the live digest `7e9e5ebc…73bb68`. That digest is not a spec fixture and is not pinned in a test. Each configuration prints it, and the prints are compared here.

## Results

| Configuration | How | RM-001 ×3 | Kernel, complete-run, and other vectors | Piloted run ×3 | Result |
|---|---|---|---|---|---|
| macOS 26, arm64, debug | `swift test` | pass | 471 tests: 470 pass, 1 opt-in skipped | `7e9e5ebc…` | **PASS** |
| macOS 26, arm64, release | `swift test -c release -Xswiftc -enable-testing`, determinism suites (31 tests) | pass | pass | `7e9e5ebc…` | **PASS** |
| macOS 26, x86_64 under Rosetta 2, release | standalone probe executable built `--arch x86_64` | pass | not run (see below) | `7e9e5ebc…`, and 30 piloted digests identical to arm64 | **PASS** (RM-001 and piloted replays only) |
| iOS Simulator 26.5, iPhone 17 profile, arm64 | `xcodebuild test`, package scheme | pass | 470 pass, 1 skipped | `7e9e5ebc…` | **PASS** |
| iOS Simulator 26.5, iPhone SE (3rd gen) profile, arm64 | `xcodebuild test` | pass | 470 pass, 1 skipped | `7e9e5ebc…` | **PASS** |
| iOS Simulator 26.5, iPhone 12 profile, arm64 | `xcodebuild test` | pass | 470 pass, 1 skipped | `7e9e5ebc…` | **PASS** |
| iPhone SE (3rd gen), physical | — | — | — | — | **NOT RUN** |
| iPhone 12, physical (performance floor) | — | — | — | — | **NOT RUN** |
| Current standard iPhone, physical | — | — | — | — | **NOT RUN** |
| Current iPhone Pro, physical | — | — | — | — | **NOT RUN** |

Cross-architecture detail is in [`archprobe-arm64.txt`](archprobe-arm64.txt) and [`archprobe-x86_64.txt`](archprobe-x86_64.txt). Each file holds RM-001 plus 30 piloted legal runs: seeds 1–5 × two pilot profiles × three upgrades, each replayed three times. Apart from the `ARCH` line, the two files are byte-identical, and all 30 runs report `replayx3=true`.

## Limits

- **A simulator is not a device.** On Apple silicon, the iOS Simulator runs arm64 code on the Mac's CPU, not on an A14 or A15. The device profile changes the screen, not the processor. The simulator rows show that the iOS SDK build and its runtime reproduce the digests. They say nothing about the physical classes.
- **x86_64 coverage is partial.** SwiftPM's `swift-testing` helper is arm64-only, so the x86_64 test bundle built but could not be launched. The x86_64 row comes from a standalone executable that uses the public `ReplayMatrix` and replay APIs plus the probe sources. The kernel and complete-run vector tests, which use `@testable` hooks, did not run on x86_64. No shipping iPhone is x86_64, so this row matters only if "supported architecture" includes Intel Macs running the package tests.
- **Physical devices were not run because none was available to this run.** D-020, which names the approved physical devices, is still `DECISION_PENDING`.

## What closes T901

T901 closes when a linked capture shows RM-001, the complete-run vectors, and `kernel-vectors-001` reproducing on each approved physical class. That needs D-020 first. Running the piloted replay on each device as well would cover a full encounter graph, but it is not required by the matrix as written.

## Spec observations

1. **"Supported architecture" is undefined.** B-002 and B-016 name it, but no artifact lists the architectures. Every iPhone class in `plan.md` §10 is arm64, and CI runs `swift test` on arm64 macOS. It is unclear whether x86_64 or simulator builds are in scope.
2. **The matrix fixture names no configurations.** `replay-matrix-001` lists fixtures, not devices or architectures, so "across the supported matrix" in T901 is defined only by `plan.md` §10 and the pending D-020.
3. **The golden replays are short.** RM-001 is 5 ticks, and the complete-run vectors (302 ticks) reach the upgrade and the terminal state through test hooks. No spec-owned replay exercises spawning, targeting, the elite, or the boss through `step`. Whether to adopt a piloted replay as a spec fixture is an open question, and adopting one would be a specification change.
