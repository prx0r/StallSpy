# Bartholomew 3D — The Canonical Character Build
**Date:** 2026-09-06
**Status:** BUILD THIS NOW

---

## The diagnosis

Current implementation: PNG + CSS wobble + PNG swapping. No real animation.

**Stop polishing 2D. Build the real 3D character.**

---

## The canonical stack

```
BARTHOLOMEW SOURCE ART
        │
        ▼
CUSTOM 3D CHARACTER MODEL (Blender/Maya)
        │
   ┌────┴────┐
   │         │
skeleton   morph targets
wings/arms  eyes/mouth
cape/antennae expressions
   │         │
   └────┬────┘
        │
        ▼
   bartholomew.glb
   embedded animation clips
        │
        ▼
THREE.JS WEB RUNTIME
transparent full-page canvas
        │
   ┌────┼────────┐
   │    │        │
AnimationMixer  procedural  flight
expressions    micro-motion  planner
   │    │        │
   └────┼────────┘
        │
   BEE STATE
   idle/listen/think/talk/fly/etc
        │
   ┌────┴────┐
   │         │
Inworld    site events
Realtime   DOM/cart/uploads
```

---

## Three animation layers

**Layer 1 — Authored animation:**
idle_hover, takeoff, flight, bank_left, bank_right, land, listen, think, talk, wave, point, present, celebrate, sleep

**Layer 2 — Procedural living motion:**
body breathing, head follows cursor, eyes track target, antennae spring, cape lags, wing speed responds to velocity, subtle body bank, tiny inertia

**Layer 3 — Semantic behavior:**
AI decides WHY he moves. "It's for my dad" → flies to creation panel.

---

## The rig

```
BartholomewRoot
├── Body
│   ├── Abdomen
│   ├── Head
│   └── Neck/Thorax
├── Arm.L → Forearm.L → Claw.L
├── Arm.R → Forearm.R → Claw.R
├── Wing.Top.L / Wing.Bottom.L
├── Wing.Top.R / Wing.Bottom.R
├── Antenna.L.01 → .02 → .03
├── Antenna.R.01 → .02 → .03
├── Cape.Center → Cape.L.01-03 / Cape.R.01-03
```

Morph targets: blink_L/R, eyes_happy/surprised/determined, mouth_A/E/O/smile/closed

---

## How he exists on the page

One transparent WebGL canvas over entire page:
```css
#bartholomew-world {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 900;
}
```

Orthographic camera → world coords = screen coords.

Semantic API survives:
```javascript
bee.flyTo("#photo-upload")
bee.pointAt("#generate-button")
bee.inspect("#uploaded-image")
bee.returnHome()
```

---

## Production brief for 3D artist

```
PROJECT: Bartholomew III — permanent 3D brand mascot

REFERENCE: Gold armored bee, large purple eyes, black/gold abdomen,
four pale faceted wings, red flowing cape, black antennae.

STYLE: Premium stylized animation-film character. Not photorealistic.
Preserve graphic/anime proportions of source artwork.

OUTPUT: Canonical Blender file + web-optimized GLB + transparent-background compatible

RIG: Root/body/head/abdomen, 2 arms+claws, 4 wings, 2 multi-joint antennae,
cape bone chain, eye aim controls, jaw/mouth control

MORPH TARGETS: blink L/R, happy/surprised/determined eyes, smile, A/E/O mouth, closed

ANIMATION CLIPS: idle_hover, listen, think, talk_idle, takeoff, flight,
bank_left/right, land, wave, point, inspect, present, celebrate,
magic_cast, surprised, sleep

CRITICAL: Flight must feel insect-like. Wings independently controllable at runtime.
Cape and antennae support secondary spring motion. Under 15 MB web asset.
```

---

## The experience

Page loads. Buzz enters from outside viewport. Shadow sweeps hero. Bartholomew rockets in, banks around logo, loops, decelerates, settles into hover.

> "Ah. There you are."

Click → mic activates.

> "Bartholomew the Third, Keeper of MythicBee. Who are we making mythical today?"

You: "It's Father's Day."

Wings slow. Head tilts.

> "Your father. Excellent. Tell me what makes the man himself."

You: "He's turning sixty, supports Liverpool..."

Eyes drift toward catalogue. Turns. Wings accelerate.

**zzzzzzzzzz—**

Flies across page, lands beside GameWinners.

> "I may have something rather perfect."

**That is the product.**

---

## three.ws role

Use for: hosting, viewer, easy embed, AI agent UI, voice, lip-sync, AR, experimentation

Our own clips for: wing motion, bee flight, cape motion, antennae, custom gestures

Hybrid approach — design Bartholomew's rig correctly for Bartholomew, not for generic humanoid.

---

## 8th Wall role

Not for website. For later:

```
physical MythicBee card → phone camera → card recognized →
Bartholomew lands ON THE CARD → "Ah. You've found it." → portal opens
```

---

## What to do now

1. Commission the 3D model (AI blockout + human hero asset)
2. Set up Three.js runtime with transparent canvas
3. Implement Layer 2 procedural motion
4. Wire Inworld voice
5. Connect semantic behavior to site events
