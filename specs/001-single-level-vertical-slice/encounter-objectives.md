# Encounter Objectives and Extraction Gate

Status: CANONICAL BASELINE  
Feature: SS-001  
Contract version: `encounter-objectives-001`

## 1. Provenance

**OBSERVED legacy canon:**

- San Francisco level title: **Fog of Probable Cause**
- Standard enemies:
  - Fog Analytics Cloud
  - Cable-Car Correlator
  - Sutro Signal Witch
  - Autonomous Informant
  - Victorian Vendor
- Elite/sub-boss: **The Improper Search Daemon**
- Boss: **The Algorithmic Moderate**
- Boss policy phases:
  1. Public Safety
  2. Civil Liberties
  3. Temporary Safeguard
  4. Independent Review

The reboot location is **The Civic Seam**. It preserves this enemy and authority lore while replacing the old ten-city campaign structure.

## 2. Objective separation

Level 1 has two independent objective lanes:

| Lane | Required for Extraction | Completion |
|---|---:|---|
| Combat Authority | Yes | required mobs + sub-boss + boss defeated |
| Network Blackout | No | all 8 stationary Cameras destroyed |

Network Blackout never substitutes for combat completion. Combat completion never marks Network Blackout complete.

## 3. Required combat graph

```text
Mob Encounter A
      ↓
Mob Encounter B
      ↓
Mob Encounter C
      ↓
The Improper Search Daemon
      ↓
The Algorithmic Moderate
      ↓
Extraction Armed
```

All five standard enemy identities must appear across the three mob encounters. Exact composition, counts, statistics, and spawn cadence require the dedicated enemy/encounter tuning contract; they cannot be inferred from Camera progress.

## 4. Boss requirement

The Algorithmic Moderate is the single Level 1 boss. It progresses through the four canonical policy phases in order. A phase change is not a separate boss defeat.

Extraction cannot arm until:

- all three required mob encounter IDs are COMPLETE;
- The Improper Search Daemon is DEFEATED;
- The Algorithmic Moderate is DEFEATED;
- the Player is alive;
- no terminal failure has been recorded.

## 5. Extraction predicate

```text
extractionArmed =
  mobA.complete
  AND mobB.complete
  AND mobC.complete
  AND improperSearchDaemon.defeated
  AND algorithmicModerate.defeated
  AND player.alive
  AND NOT run.failed
```

The predicate MUST NOT reference:

- Cameras destroyed;
- Network Blackout completion;
- Exposure value;
- upgrade identity;
- optional ambience or collectibles.

After arming, the Player must still enter Phoenix Steps and complete the specified Extraction survival countdown.

## 6. Receipt

```json
{
  "combatAuthority": {
    "mobEncountersComplete": 0,
    "mobEncountersRequired": 3,
    "elite": {
      "id": "improper-search-daemon",
      "defeated": false
    },
    "boss": {
      "id": "algorithmic-moderate",
      "defeated": false,
      "phasesReached": []
    },
    "complete": false
  },
  "networkBlackout": {
    "camerasDestroyed": 0,
    "camerasTotal": 8,
    "complete": false
  },
  "extractionArmed": false
}
```

## 7. Non-goals

This contract does not yet define enemy statistics, wave counts within each mob encounter, spawn cadence, loot, or exact boss attacks. Those require a separate contract before runtime implementation.
