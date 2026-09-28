# T305 evidence — scripted pacing probes (partial)

**Status asked:** record as **PARTIAL**. T305 stays open. These are bot probes, not a person playing. The reconciliation row requires "recorded pacing probes compared against the `E-011` 8–12-minute target" run by a designer or player, and nobody has played yet.

**Runtime:** SS-runtime `evidence/t305-t901-pacing-replay-probes` (`06561a9`), on `main` `59e5e4b`, spec pin `cd77770`. Tooling is test-target only. No file under `Sources/` or `App/` changed.

## What was run

A headless pilot drives `Simulation.step` with the same `PlayerCommand` a touch controller produces. It reads only `PresentationSnapshot`. It follows the authoritative objective node, navigates by grid search over live solids, moves to get a line of fire, backs away from contacts, leaves receipt-mine reach, and sidesteps projected telegraphs and hostile bolts.

| Profile | What it is | What it is not |
|---|---|---|
| `competent` | Perfect route knowledge, zero reaction latency, Dodge as a hit lands | A skilled human. It never reads, hesitates, explores, or learns |
| `firstRun` | The same route knowledge, 250 ms (15-tick) perception latency, never Dodges | A first run. It already knows where every objective is, has read no tutorial, and cannot be confused. At most a lower bound on first-run time |
| `sustained` (diagnostic) | Either profile with Integrity restored to full after every tick, through the test-only hook | A legal run. It measures how long the content takes to clear when survival is not the limit |

The sweep ran seeds 1–20 × three upgrades × two profiles, legal and sustained: 240 runs in total. Raw data is one JSON line per run in [`pacing-sweep-seeds-1-20.jsonl`](pacing-sweep-seeds-1-20.jsonl). To reproduce it:

```
SS_PACING_SEEDS=20 SS_PACING_REPORT=report.jsonl \
  swift test -c release -Xswiftc -enable-testing --filter pacingT305ProbeMatrix
```

Times are simulation ticks at 60 Hz. The upgrade overlay freezes the clock, so time spent choosing a card never appears.

## Results (OBSERVED)

### Outcomes, legal runs

| Profile | Runs | Success | Died at M-C | Died at elite | Died at boss | Stalled |
|---|---:|---:|---:|---:|---:|---:|
| `competent` | 60 | 7 (SJ 1, RP 4, GS 2) | 4 | 30 | 17 | 2 (M-C) |
| `firstRun` | 60 | 0 | 30 | 15 | 15 | 0 |

The pilot's survival is limited by its skill. A 12 % success rate says nothing reliable about difficulty. Damage taken by the `competent` pilot came mostly from the Improper Search Daemon (2304 total), Signal Witch bolts (2080), and Victorian Vendor mines and contact (724). The `firstRun` pilot, which never Dodges, took most of its damage from Vendors (3361).

### Pacing against `arena.md` §5

Median time with range, in m:ss. The segment start is the first entry into the segment's zone for segments 1–5. Captain Court starts at `BossActivated` and Extraction at `ExtractionArmed`. That mapping is INFERRED from `arena.md` §2 and `enemies-and-encounters.md`, because §5 does not name start events.

| Segment (start event) | Target start | competent, legal, successful (n=7) | competent, sustained, successful (n=49) | firstRun, sustained, successful (n=60) |
|---|---:|---:|---:|---:|
| Spawn Alley | 0:00 | 0:00 | 0:00 | 0:00 |
| Camera Corridor | 0:45 | 0:01 | 0:01 | 0:01 |
| Civic Plaza | 2:00 | 0:03 | 0:03 | 0:05 (0:04–0:05) |
| Pressure Route | 4:00 | 0:28 (0:27–0:32) | 0:30 (0:27–0:32) | 0:42 (0:37–0:47) |
| Lockdown Ring | 6:00 | 0:55 (0:43–1:00) | 0:51 (0:19–1:14) | 1:11 (0:51–1:54) |
| Captain Court | 7:30 | 2:14 (1:55–3:26) | 2:43 (1:56–5:28) | 3:16 (2:28–3:46) |
| Extraction | 10:00 | 3:32 (2:54–4:34) | 3:49 (2:52–6:31) | 4:04 (3:12–4:28) |
| **Run complete** | **8:00–12:00** | **3:43 (3:06–4:43)** | **3:57 (3:02–6:40)** | **4:14 (3:24–4:50)** |

Other measured times:

- **Time to first encounter** (`WaveStarted`, M-A): 0:03 competent, 0:06 firstRun.
- **Time to first damage:** median 0:39 competent, 0:53 firstRun.
- **Lockdown:** every run, all 240, entered Lockdown. The median is 1:05 competent and 1:30 firstRun. M-C forces it by design (EN-007).
- **Elite fight:** a median of 0:19–0:20 from `EliteActivated` to `EliteDefeated`.
- **Boss fight:** a median of 0:48–1:04 from `BossActivated` to `BossDefeated`.
- **Extraction:** a median of 0:09–0:14 from `ExtractionArmed` to success. That is travel plus the 300-tick hold.
- **Cameras destroyed:** 0–8 per run, mostly 4–6. The automatic weapon prefers a detecting Camera over a farther enemy (D-031), so a pilot that ignores Cameras still destroys about half of them. Two sustained runs reached Network Blackout.

### Content-bound floor (INFERRED from `combat-content-001`)

Total hostile HP is 2800: M-A 330, M-B 530, M-C 840, elite 300, boss 800. Civic Pulse deals 10 damage every 30 ticks, which is 20 DPS. So the kill time alone is at least **2:20**, before travel, spawn intervals, wave delays, boss transitions, or shots spent on Cameras. Ricochet Pulse lowers the floor. The fastest measured completion was 3:02.

## What this shows

- **OBSERVED:** For both pilots, a completed run lasts about 3–5 minutes, and no run of the 116 completions exceeded 6:40. Every segment starts far earlier than `arena.md` §5 targets. The gap is largest early: Civic Plaza is reached in 3–5 s against a 2:00 target.
- **INFERRED:** A competent human reaching 8–12 minutes needs to spend roughly 2–3 times as long as these pilots. The weapon fires automatically at a fixed rate, so a player can add time only by being slower to reach a line of fire, by retreating, or by losing shots to Cameras. Whether real players do that is exactly what this probe cannot show.

## What this cannot show

- How long a person spends learning movement, reading tutorial copy, looking at Camera fields, hesitating, getting lost, or backtracking. These dominate `arena.md`'s early segments ("Learn movement", "Learn observation and recovery"). The pilots have none of it.
- First-run comprehension, including F-001 through F-004 and G-001 through G-003.
- Real difficulty. The pilots die from their own skill limits. Their death rate is not a balance signal.
- Anything on a device. All runs are headless, in the macOS test process.

T305 closes when a designer or player records first-run and competent-run probes, with durations per segment, compared against these targets. G-005 needs the median over at least five external participants.

## Spec observations

1. **Extraction segment vs. Extraction rule.** `arena.md` §5 gives Extraction 10:00–12:00, which is 2 minutes. `arena.md` §3 and E-019 fix the hold at 300 ticks, which is 5 s, and no new pressure appears (E-010). Measured Extraction took 5–24 s. The segment cannot fill 2 minutes unless the player is repeatedly pushed out.
2. **Segment names vs. zone names.** §5 uses Spawn Alley … Captain Court. The manifest, the runtime, and `arena-layout.md` use Residential Wedge … Authority Court. The mapping exists only in the §2 headings and `civic-seam-visual-direction.md`. §5 also names no start or end events, although it says segment boundaries are "event-based".
3. **Spawn Alley geometry vs. its 45 s budget.** The Player spawns at (160, 192), and Z-02 begins at x = 320, so walking straight crosses Spawn Alley in 0.7 s. The 45 s exists only if the player lingers to learn.
4. **Competent-run target vs. content volume.** D-002 and E-011 target 8–12 minutes. `combat-content-001` supports a 2:20 kill-time floor, and two pilots finish in 3–5 minutes. If playtests confirm this, either the target or the content needs a recorded decision. This document does not propose one.
