# HiveActivity v1 product specification

## Experience target

Claude Code proved that a tiny shifting activity phrase can make latency feel alive. MythicBee should use the same underlying idea but make it diegetic:

- the bee appears to be working
- the Hive appears to have departments
- status wording reacts to the mission
- seasonality alters the Hive naturally
- the animation is fluid enough to feel premium
- real progress remains honest

The result should feel closer to an animated storybook / Club Penguin ambient world than a SaaS loading spinner.

## First-frame design

One line:
- small living glyph
- glimmering status text
- no progress percentage unless the underlying API provides a meaningful one
- no fake step checklist

The component should fit:
- under a conversational bubble
- inside a product card
- full-screen Hive transition
- checkout/status screens

## Fluidity

There are two independent timescales:

1. **continuous** — shimmer/glyph/bee idle motion
2. **semantic** — phrase swaps every ~2–5 seconds

This is important. If the entire UI only changes when the phrase changes, it feels like a slideshow. If the phrase changes constantly, it becomes unreadable.

## Phase-specific latency theatre

### Listening
The UI should barely move. Avoid stealing attention from the user's story.

### Understanding
Subtle note-taking/inspection.

### Ideation / Council
More social movement: bees peek in, argue, vote.

### Generation
The visual focus may move toward the generated artifact while the bee performs small related motions.

### Package
Satchel choreography.

### Fulfilment
Bee physically leaves for the Hive.

## Seasonal inheritance

Season is a composable overlay:
- status additions
- optional phrase transforms
- CSS variables/classes
- ambient scene hook

The same core status bank remains intact.

## Accessibility

- `aria-live="polite"`
- reduced-motion fallback
- never rely on animation alone to communicate completion/failure
- maintain readable contrast
- avoid rapid flashing
- allow application to provide explicit factual status when necessary

## Error states

Do not make errors whimsical to the point of ambiguity.

Good:
> Bartholomew couldn't get the video through. Nothing has been charged. Try again.

Then optionally:
> “The hive has embarrassed itself.”

Bad:
> Fluffernectaring failed!

Errors need ordinary-language recovery first, character second.
