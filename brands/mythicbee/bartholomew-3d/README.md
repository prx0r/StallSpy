# Bartholomew 3D — The Character Package

**Status:** Asset collection complete. 3D model commission pending.

---

## What's here

### Assets
- **poses/** — 12 transparent pose sprites (neutral, happy, wink, listening, thinking, surprised, confident, talking, presenting, celebrate, sleeping)
- **animations/** — 2 animated WebP fallbacks (hover, celebrate)
- **canonical/** — Hero character art (PNG + WebP)
- **rig/** — 13 transparent rig layers (body, abdomen, eyes, mouth, 4 wings, 2 antennae, 2 arms, cape)
- **source/** — Original source sheets (turnaround, rig, emote, source)

### Code
- **src/bartholomew3d.js** — Three.js character controller (unused, replaced by CSS approach)
- **src/bee-controller.js** — CSS-based state machine (current implementation)
- **src/hive-activity.js** — Status text engine (186 entries)

### Docs
- **3dactual.md** — The canonical 3D build spec
- **bartholomew-system-prompt.md** — Character personality
- **interaction-contract.md** — How Bartholomew interacts
- **production-rig-next-step.md** — What the 3D artist needs to do
- **voice-architecture.md** — Voice integration plan

---

## The current state

**What exists:** 12 high-quality pose sprites + 2 animated WebP + 13 rig layers + source art

**What's missing:** A proper 3D GLB model with bones, morph targets, and animation clips

**The 3D build spec:** See `docs/3dactual.md`

---

## What the 3D artist needs

### Reference images
- `assets/source/bartholomew-source.png` — Hero character
- `assets/source/turnaround-source-sheet.png` — 360° turnaround
- `assets/source/rig-source-sheet.png` — Component breakdown
- `assets/source/emote-source-sheet.png` — Expression sheet

### Rig requirements
- Root/body/head/abdomen
- 2 articulated arms + claws
- 4 independent wings
- 2 multi-joint antennae
- Cape bone chain
- Eye aim controls
- Jaw/mouth control

### Morph targets
- blink_L/R
- eyes_happy/surprised/determined
- mouth_A/E/O/smile/closed

### Animation clips
idle_hover, listen, think, talk_idle, takeoff, flight, bank_left/right, land, wave, point, inspect, present, celebrate, magic_cast, surprised, sleep

### Target format
- Blender source + web-optimized GLB
- Under 15 MB
- Transparent background compatible
- PBR materials
- Clean topology

---

## The production brief

```
PROJECT: Bartholomew III — permanent 3D brand mascot

REFERENCE: Match supplied 2D anime character exactly.
Gold armored bee, large purple eyes, black/gold abdomen,
four pale faceted wings, red flowing cape, black antennae.

STYLE: Premium stylized animation-film character.
Not photorealistic. Not generic Pixar.

OUTPUT: Blender source + GLB + transparent-background compatible

RIG: Root/body/head/abdomen, 2 arms+claws, 4 wings,
2 multi-joint antennae, cape bone chain, eye aim, jaw control

MORPH TARGETS: blink L/R, happy/surprised/determined eyes,
smile, A/E/O mouth, closed

ANIMATION CLIPS: idle_hover, listen, think, talk_idle, takeoff,
flight, bank_left/right, land, wave, point, inspect, present,
celebrate, magic_cast, surprised, sleep

CRITICAL: Flight must feel insect-like. Wings independently
controllable at runtime. Cape and antennae support secondary
spring motion. Under 15 MB web asset.
```

---

## Next steps

1. Commission 3D model from production brief
2. Set up Three.js runtime with transparent canvas
3. Implement Layer 2 procedural motion
4. Wire Inworld voice
5. Connect semantic behavior to site events
