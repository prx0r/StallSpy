# @mythicbee/hive-activity

A modular activity-theatre engine for MythicBee.

It turns genuine latency into character and narrative:

```txt
Consulting the hive…
Reconsidering the Wembley incident…
Stinging the elves…
Packing the satchel…
Making it mythical…
```

The engine is deliberately split into **policy**, **content**, and **presentation** so that it can evolve without coupling MythicBee to a single UI framework.

## What it does

- Selects activity phrases based on the **real operation phase**
- Applies **bee personality bias** without changing core application logic
- Injects safe contextual hooks from the current `GiftState`
- Applies **seasonal overlays** (Christmas, Halloween, Valentine's, Father's Day, Mother's Day)
- Avoids repetition with recency windows and cooldowns
- Supports rare/nonsense phrases so the experience does not become a wall of bee puns
- Emits exposure metadata for analytics / experimentation
- Supports deterministic seeded playback for tests and session continuity
- Respects `prefers-reduced-motion`
- Includes a React adapter with a fluid text glimmer
- Can be used without React through the core TypeScript engine

## Core rule

**The engine never invents application progress.**

It decorates real states. `generate-video` phrases are only eligible while video generation is actually running; fulfilment phrases are only eligible during fulfilment. This keeps the theatre trustworthy.

## Installation

Internal package:

```bash
npm install
npm run build
```

## Basic React usage

```tsx
import { HiveActivity } from "@mythicbee/hive-activity/react";
import { DEFAULT_BEES } from "@mythicbee/hive-activity";

<HiveActivity
  seed={beeMission.id}
  context={{
    phase: "generate-world",
    bee: DEFAULT_BEES.find(b => b.id === "bartholomew-iii"),
    season: "christmas",
    missionTags: ["sport"],
    hooks: {
      hook: "the Wembley incident",
    },
  }}
/>
```

## Architecture

```txt
REAL APPLICATION STATE
        │
        ▼
     HivePhase
        │
        ├──────── Mission tags
        ├──────── Bee profile
        ├──────── Season theme
        └──────── Contextual hooks
                  │
                  ▼
          ELIGIBILITY FILTER
                  │
                  ▼
           WEIGHTED POLICY
                  │
      recency / cooldown / rarity
                  │
                  ▼
            RENDER PHRASE
                  │
       seasonal transformation
                  │
                  ▼
             SNAPSHOT
          text + motion cue
                  │
         ┌────────┴────────┐
         ▼                 ▼
      React UI         Analytics
```

See `docs/architecture.md` and `docs/authoring-guide.md`.
