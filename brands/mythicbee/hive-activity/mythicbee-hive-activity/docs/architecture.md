# Architecture

## Design goals

HiveActivity exists for a specific job: convert otherwise dead latency into a small piece of MythicBee theatre without lying about what the system is doing.

It must remain:

1. **Truthful** — phrases decorate real states.
2. **Fast** — no LLM call is required for ordinary status rotation.
3. **Contextual** — the best moments reference what the customer actually said.
4. **Seasonal** — the Hive should visibly inherit the gifting calendar.
5. **Characterful** — Bartholomew and Martin should not sound identical.
6. **Non-annoying** — repetition, constant bee puns, and hyperactive status swaps are aggressively controlled.
7. **Observable** — every exposure is loggable for later tuning.
8. **Extensible** — new phases, bees, seasons and phrase packs should be data additions, not rewrites.

## Three layers

### 1. Activity policy

`HiveActivityEngine` selects an eligible phrase.

It considers:

- actual `phase`
- explicit status overrides
- active season
- bee archetype
- mission tags
- contextual hook availability
- cooldowns
- recent exposure
- rarity
- bee phrase biases

### 2. Content packs

Phrase banks are JSON.

The base bank should contain the durable MythicBee voice. Seasonal packs only add/transform a fraction of phrases.

This prevents Christmas from turning every status into a Christmas joke.

### 3. Presentation adapters

The core engine has no DOM dependency.

React is merely the first adapter. Other future surfaces can consume the same snapshot:

- Web/React
- mobile app
- recipient reveal
- email animation/gif generation
- Three.js bee choreography
- in-store holographic display
- smart-glasses UI

## Motion cues

Phrase content may emit a tiny semantic `motionCue`:

- `hover`
- `fly-out`
- `fly-in`
- `peek`
- `scribble`
- `argue`
- `pack`
- `inspect`
- `celebrate`

The status engine never manipulates transforms directly.

A separate character controller maps `pack` to the current bee rig/sprite implementation.

That is the same semantic-control principle used elsewhere in MythicBee.

## Context hooks

Do not pass arbitrary raw transcript text directly to the display.

Upstream Gift Intelligence should provide a small list of display-safe hooks:

```json
{
  "hook": "the Wembley incident",
  "pet": "Dave",
  "place": "Mallorca",
  "catchphrase": "we'll see"
}
```

The status bank can then use controlled templates:

```txt
Reconsidering {hook}…
Putting {pet} in goal…
Rebuilding {place}…
```

This creates the feeling that the Hive listened without exposing sensitive or inappropriate transcript fragments.

## Session determinism

Use `BeeMission.id` as the default seed.

Benefits:

- a resumed mission feels stable rather than random
- screenshots are reproducible
- bugs can be replayed
- A/B tests can cleanly control phrase variance

## Do not call an LLM every status tick

Normal status rotation is a local policy over curated text.

LLMs may enrich a session once by producing safe `loader_hooks`, but those outputs should then be inserted into curated templates.

This keeps latency, cost and moderation risk low.

## Truthfulness

Bad:

```txt
"Three bees unanimously chose this…"
```

when no multi-agent vote happened.

Good:

```txt
"Consulting the hive…"
```

during a recommendation process.

If the actual Hive Council runs, the application may set:

```ts
context.explicitStatus = "Three bees are voting…"
```

This module is theatre, not deception.
