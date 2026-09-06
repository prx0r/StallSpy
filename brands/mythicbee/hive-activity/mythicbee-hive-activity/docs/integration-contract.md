# Integration contract

HiveActivity should consume normalized state from the MythicBee application.

## Application → HiveActivity

```ts
{
  phase: "generate-video",
  bee,
  season,
  missionTags: ["sport", "dad", "funny"],
  hooks: {
    hook: "the Wembley incident"
  }
}
```

## HiveActivity → UI

```ts
{
  text: "Giving the Wembley incident a close-up…",
  motionCue: "inspect",
  seasonId: "christmas",
  beeId: "bartholomew-iii",
  meta: { ... }
}
```

## UI → Bee controller

Map semantic cues:

```ts
switch (snapshot.motionCue) {
  case "pack": beeController.pack();
  case "argue": beeController.react("argument");
  case "fly-out": beeController.flyTo("hive-door");
}
```

The phrase engine does not own choreography.

## Upstream hook contract

Gift Intelligence should provide display-safe hooks only.

Recommended hook object:

```ts
type LoaderHooks = {
  hook?: string;       // "the Wembley incident"
  pet?: string;        // "Dave"
  place?: string;      // "Mallorca"
  object?: string;     // "that 1998 mug"
  catchphrase?: string;// "we'll see"
};
```

Do not pass health, politics, sexuality, religion, financial distress, or other sensitive inferences into casual loader text.
