# MythicBee — Bartholomew III Character Kit

A production-starting kit for turning the canonical MythicBee bee into an on-site conversational character.

## What is already done

- `assets/canonical/bartholomew.webp` — transparent canonical character, ready for web use.
- `assets/layers/` — **13 transparent lossless WebP slices** extracted from the generated rig sheet.
- `assets/expressions/` — neutral/blink/happy/determined/surprised eyes plus six mouth shapes and an extra cape piece.
- `assets/poses/` — 12 transparent pose/emote sprites for immediate state swapping.
- `assets/animations/` — lightweight animated-WebP hover and celebrate fallbacks.
- `src/BartholomewController.ts` — real Motion.js controller: idle hover, listen, think, speak, audio-reactive movement, fly-to-element, point, return-home, celebrate, reduced-motion support.
- `src/InworldVoiceClient.ts` — browser voice transport for the included proxy, with microphone PCM streaming, output playback, agent-state animation hooks and tool-event forwarding.
- `server/inworld-proxy.ts` — server-side Inworld Realtime WebSocket proxy so the API key never ships to the browser.
- `schemas/gift-brief.schema.json` — canonical structured customer brief.
- `schemas/tools.inworld.json` — function/tool definitions suitable for Inworld Realtime `session.update`.
- `schemas/tool-policy.json` — explicit boundary between automatic UI actions and operations requiring confirmation.
- `docs/bartholomew-system-prompt.md` — the character/persona prompt.
- `demo/` — working Motion.js interaction demo once dependencies are installed.

## Core 13 layer files

1. `01_body_head_thorax.webp`
2. `02_abdomen_tail.webp`
3. `03_eyes_neutral.webp`
4. `04_mouth_closed.webp`
5. `05_wing_left_front.webp`
6. `06_wing_left_back.webp`
7. `07_wing_right_front.webp`
8. `08_wing_right_back.webp`
9. `09_antenna_left.webp`
10. `10_antenna_right.webp`
11. `11_arm_left.webp`
12. `12_arm_right.webp`
13. `13_cape_trailing.webp`

See `docs/core-layers-contact-sheet.jpg`.

### Important rig note

The 13 pieces are clean transparent exports from the generated rig sheet, but they are **not yet a pixel-registered skeletal rig cut directly from one neutral master pose**. The source generator drew some overlapping elements into the body slice. Therefore:

- the canonical full-character image + Motion controller is usable immediately;
- pose swapping is usable immediately;
- these slices are a strong starting point for a Rive/Spine/Live2D-style rig;
- for perfect independent eye/mouth/arm deformation, the final production pass should repaint one neutral body master with those overlapping features removed and register every layer against that one canvas.

Do not let that block the site MVP. Use full-character motion first, then upgrade the rig once the interaction proves valuable.

## Run the animation demo

```bash
npm install
npm run dev
```

The demo shows:

- continuous hover
- listening / thinking / speaking states
- fake audio-reactive speaking
- fly to a specific DOM element
- celebrate
- return home
- a sample GiftBrief

Motion is deliberately responsible for **movement**, while the language model only emits high-level semantic actions such as `fly_to` and `set_expression`.

## Voice hookup with Inworld

Create `.env` from `.env.example`:

```bash
cp .env.example .env
```

Set your Inworld API key, model and voice, then run:

```bash
npm run voice
```

The included proxy listens on `ws://localhost:8787`.

In your site client:

```ts
import { InworldVoiceClient } from "./src/InworldVoiceClient";
import { routeClientTool } from "./src/toolRouter";

const voice = new InworldVoiceClient({
  controller,
  onTool: async (name, args) => {
    await routeClientTool(name, args, toolContext);
  }
});

await voice.start(); // must happen from a user click/tap because microphone permission is required
```

The voice client maps realtime events to mascot state:

```text
user starts speaking  -> listening
user stops            -> thinking
agent audio arrives   -> speaking
response finishes     -> idle
function call         -> site action / mascot action
```

## GiftBrief design

The conversation is a natural-language interface around one canonical state object. Do not keep critical customer facts only in chat history.

Example progression:

```text
"It's Father's Day"
        ↓
update_gift_brief({ occasion: ... })

"He's turning 60 and loves Liverpool"
        ↓
update_gift_brief({ recipient: ..., interests: ... })

"He's always taking the piss out of everyone"
        ↓
update_gift_brief({ personality: ... })

Bartholomew now has enough context to ask a higher-value creative question
instead of restarting a questionnaire.
```

`src/giftBrief.ts` also contains a deterministic readiness score and fallback next-question function.

## Tool philosophy

### Automatic

- update/read GiftBrief
- fly/point/animate Bartholomew
- show products/examples
- open upload UI
- create non-expensive concepts

### Requires explicit UI confirmation

- paid preview generation
- purchase/charge
- email/send/publish
- irreversible external actions

The LLM should never control raw animation frames. It should say *what it wants Bartholomew to do*, and the controller decides how that looks.

## Recommended production path

### V0 — ship now

Canonical transparent sprite + Motion.js + Inworld + GiftBrief + tool router.

### V1 — improve character expressiveness

Repaint/register a single neutral layered master and animate wings, eyes, mouth, antennae and cape independently using the same controller API.

### V2 — premium animation

Import the cleaned layer set into Rive or Spine. Keep the same `BartholomewController` public methods so the rest of the site does not care which renderer is underneath.

### V3 — 3D / AR

Create a separate 3D incarnation only if the product needs it. Keep 2D Bartholomew as the website concierge.

## Source artwork

The original generated source sheets are retained under `assets/source/` so a designer or animation agent can reproduce or improve the rig without losing provenance.
