# Bartholomew 3D — The Actual Build
**Date:** 2026-09-06
**Status:** CANONICAL — this is what we're building

---

I checked the actual MythicBee implementation in `prx0r/StallSpy`, and you are not imagining it: **right now Bartholomew is literally a PNG being translated/rotated/scaled with CSS. There is no real character animation system on the deployed implementation.**

The page creates:

```html
<div id="mythic-bee" class="bee-character">
  <img src="assets/bartholomew.png" ...>
</div>
```

and its "hover" is just `translateY(-8px)`. The controller then rotates that whole image toward the mouse, translates the whole container toward DOM elements, and swaps between four static PNGs for different states. There are comments claiming wing flutter, eye tracking, mouth movement etc., but those are not actually implemented as articulated animation.

There is another bug worth fixing: `bee-controller.js` auto-initializes itself, and then `index.html` imports it and initializes another controller again. So you're potentially running two Bartholomew controllers against the same DOM node.

And your Inworld code is presently a scaffold rather than a working integration—the connection method sets `connected = true` around a placeholder `YOUR_INWORLD_API_KEY`; it isn't actually establishing the WebRTC session yet.

So: **we should stop polishing this 2D implementation. You now have a character good enough to justify building a real 3D brand asset.**

# What I would build now

The canonical stack I recommend has changed slightly because you explicitly want **the best possible living Bartholomew**, not merely the fastest MVP:

```text
             BARTHOLOMEW SOURCE ART
                      │
                      ▼
          CUSTOM 3D CHARACTER MODEL
              Blender / Maya
                      │
          ┌───────────┴───────────┐
          │                       │
       skeleton               morph targets
     wings / arms            eyes / mouth
    cape / antennae           expressions
          │                       │
          └───────────┬───────────┘
                      ▼
              bartholomew.glb
          embedded animation clips
                      │
                      ▼
             THREE.JS WEB RUNTIME
          transparent full-page canvas
                      │
        ┌─────────────┼──────────────┐
        │             │              │
   AnimationMixer   procedural      flight
   expressions      micro-motion    planner
        │             │              │
        └─────────────┼──────────────┘
                      │
                 BEE STATE
                      │
       idle/listen/think/talk/fly/etc
                      │
            ┌─────────┴─────────┐
            │                   │
       Inworld Realtime     site events
      STT / LLM / TTS       DOM / cart /
        tool calls           uploads
```

**That is the premium solution.**

Not Rive. Not animated PNGs. Not a GIF. Not a video masquerading as an avatar.

A proper **rigged 3D character rendered live in WebGL**.

Three.js natively supports bones, skinned meshes, morph targets and multiple animation clips, including fading/crossfading between them. ([Three.js][1]) Blender's glTF exporter supports exactly the things we need—armature animation, object transforms and shape-key/morph-target animation—and can export multiple animation actions into the GLB. ([Blender Documentation][2])

## The most important part: commission the final model

I would absolutely use AI 3D generation to experiment, but **I would not make an automatically generated Meshy/three.ws model the permanent MythicBee mascot**.

This character is becoming a brand asset analogous to Duo for Duolingo.

Pay a good 3D character artist/technical animator to make **one canonical Bartholomew** from our source artwork.

They should receive the hero image plus the turnaround sheets we've already generated and recreate it accurately in 3D.

AI can get surprisingly far now—Meshy offers reference-image → 3D, auto-rigging and hundreds of motion presets, and can export animated GLB. ([Meshy Help Center][3]) Three.ws can also generate creatures from references and output rigged GLBs. ([three.ws][4])

But the final 10–20%—the silhouette, face, cape, eye proportions, topology, wing construction and deformation—is exactly the 10–20% users will associate with **MythicBee forever**.

Use AI for the blockout.

Use a human for the hero asset.

# How I would rig him

The model should not simply have "an armature." It should be deliberately designed around his personality.

```text
BartholomewRoot

├── Body
│   ├── Abdomen
│   ├── Head
│   └── Neck/Thorax
│
├── Arm.L
│   ├── Forearm.L
│   └── Claw.L
├── Arm.R
│   ├── Forearm.R
│   └── Claw.R
│
├── Wing.Top.L
├── Wing.Bottom.L
├── Wing.Top.R
├── Wing.Bottom.R
│
├── Antenna.L.01 → .02 → .03
├── Antenna.R.01 → .02 → .03
│
├── Cape.Center
├── Cape.L.01 → .02 → .03
└── Cape.R.01 → .02 → .03
```

Then use morph targets/shape keys for:

```text
blink_L
blink_R
eyes_happy
eyes_suspicious
eyes_surprised

mouth_closed
mouth_A
mouth_E
mouth_O
mouth_smile
mouth_grin
```

glTF supports both skinned animation and animated morph-target weights, which is exactly why GLB is the correct runtime format here. ([Khronos Registry][5])

The wings should **not merely be part of a prerecorded animation**.

Give them independent bones.

Then runtime code can alter wing speed continuously.

That is how he starts feeling alive.

# The difference between "animated" and "alive"

This is the crucial distinction.

If we make fifteen Blender animations and loop `idle.glb`, he will still feel like an animated model.

I want three animation systems running simultaneously.

**Layer 1 — authored character animation.**

Things like:

```text
idle_hover
takeoff
flight
bank_left
bank_right
land
listen
think
talk
wave
point_left
point_right
inspect
present
celebrate
magic_cast
sleep
startled
```

These are hand-animated clips and blend into each other.

**Layer 2 — procedural living motion.**

The browser adds tiny continuously changing movement:

```text
body breathing/hover noise
head follows cursor
eyes track target
antennae spring slightly
cape lags behind movement
wing speed responds to velocity
subtle body bank follows flight direction
tiny inertia after stopping
```

That means he never repeats exactly the same five-second animation.

**Layer 3 — semantic behavior.**

The AI decides *why* he moves.

User says:

> "It's for my dad."

Bartholomew turns toward the creation panel.

> "Splendid. Tell me about the gentleman."

He flies beside the recipient field.

User says:

> "He's sixty and obsessed with Liverpool."

Bartholomew pauses in mid-air, hand under chin.

Thinking pose.

Then:

> "Oh, this has possibilities."

He flies toward the GameWinners concept.

That's where this becomes a character rather than a chatbot.

# How he should physically exist on the webpage

This is an important architectural improvement over your current fixed PNG.

I'd put **one transparent WebGL canvas over the entire page**:

```css
#bartholomew-world {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 900;
}
```

Inside that canvas is Bartholomew.

Use an **orthographic camera whose world coordinates correspond to screen coordinates**.

That sounds technical, but it gives you something extremely useful.

If this element:

```javascript
document.querySelector("#photo-upload")
```

is at:

```text
x = 823
y = 511
```

Bartholomew can literally fly to the corresponding location in his 3D world.

So your existing semantic API survives:

```javascript
bee.flyTo("#photo-upload")
bee.pointAt("#generate-button")
bee.inspect("#uploaded-image")
bee.returnHome()
```

Except instead of translating a PNG, we are moving an actual 3D character.

For the flight trajectory, GSAP's MotionPath is excellent: it can follow arbitrary Bézier/SVG paths and automatically orient along the curve. ([GreenSock][6])

So:

```text
bottom right

        ╭──────────────╮
       ╱                ╲
      ╱                  ╲
     🐝 ─────────────────→ upload
```

isn't a linear CSS transition anymore.

He curves upward, banks into the turn, accelerates, overshoots slightly, brakes, stabilizes and starts hovering.

That will look enormously better.

# three.ws: yes, definitely use it — but in the right role

My research here changed my view somewhat because **three.ws has progressed a lot**.

It now supports uploading arbitrary custom GLB avatars, with up to 16 MB for an agent body. ([three.ws][7]) It has a one-tag 3D viewer, talking agents, a floating Walk Companion and a site concierge that can use your own GLB. ([three.ws][8])

There is even now a page-tour system where a 3D character literally **walks to real interface elements, points at them and talks about them**. That is almost exactly the behavioral idea we've been designing for Bartholomew. ([three.ws][9])

And this is hilariously close to a no-code prototype of our idea:

```html
<script
  src="https://three.ws/walk-embed-sdk.js"
  data-avatar="YOUR-BARTHOLOMEW-ID"
  data-position="bottom-right">
</script>
```

Their Walk docs say that one script injects a transparent floating 3D avatar, and there is a JavaScript SDK for runtime control. ([three.ws][10])

So **I would absolutely test Bartholomew in three.ws**.

But there is a caveat.

Their global animation-retargeting system is designed around a **52-joint canonical humanoid skeleton**. Their own Rig Doctor explains that their animation clips target those joints; it explicitly has a non-humanoid test case because nonstandard rigs don't automatically map onto those animations. ([three.ws][11])

Our bee has:

* four wings
* antennae
* no human legs
* weird abdomen
* cape
* claws.

Therefore don't design Bartholomew around compatibility with their generic humanoid animation library.

Design **Bartholomew's rig correctly for Bartholomew**.

Use three.ws for:

```text
hosting
viewer
easy embed
AI agent UI
voice
lip-sync
AR
experimentation
```

and our own clips/runtime for:

```text
wing motion
bee flight
cape motion
antennae
custom gestures
MythicBee-specific choreography
```

That's the hybrid I trust most.

# three.ws is also extremely useful for speech

Another piece I found is excellent for us.

Three.ws now has browser-side TTS lip synchronization. It analyzes the actual speech audio and drives visemes/morphs; it even has fallback jaw animation where facial morphs are absent. ([three.ws][12])

Their current implementation uses `wawa-lipsync` in-browser to derive visemes from the audio signal. ([three.ws][13])

That means we can potentially steal/adapt the same conceptual layer:

```text
TTS AUDIO
    │
    ▼
audio analyser
    │
    ▼
viseme detector
    │
 ┌──┼────────┐
 A  E  O  mouthClosed
 │  │  │
 ▼  ▼  ▼
GLB morph targets
```

For a little bee, this will look excellent without needing Pixar-level facial capture.

# Voice layer

I would retain the architectural decision you already made:

**Inworld owns conversation.**

Your repo actually documents that intended stack correctly: Inworld Realtime + GiftBrief + page tools + character state.

The implementation just hasn't caught up yet.

So:

```text
microphone
    ↓
Inworld
    ↓
STT
    ↓
LLM / Bartholomew personality
    ↓
tool calls ───────→ fly_to("#foo")
    ↓               point_at("#bar")
TTS                 celebrate()
    ↓
audio
    ↓
lip-sync + speaking animations
```

If eventually you prefer ElevenLabs' voice, that's fine too. ElevenLabs' streaming APIs can return character-level alignment/timing with the audio, and their Agent WebSocket exposes audio events plus alignment. ([ElevenLabs][14])

The key is to make **VoiceProvider** an abstraction. Don't couple Bartholomew's body to Inworld's audio API.

# Where 8th Wall fits

Not here.

8th Wall does **not** make Bartholomew animate better on your homepage.

It's an XR layer.

It has now transitioned to 8thwall.org: the open-source framework includes Image Targets, Face Effects and Sky Effects under MIT; SLAM remains distributed as a binary, and the tools are free to use commercially under their respective licenses. ([8th Wall][15])

Use it later for:

```text
physical MythicBee card
        ↓
phone camera
        ↓
card recognized
        ↓
Bartholomew lands ON THE CARD
        ↓
"Ah. You've found it."
        ↓
portal opens
```

That's where 8th Wall is killer.

For the website itself: **Three.js / three.ws**.

# What I'd change in StallSpy immediately

Your own architecture docs currently explicitly say "Not generic 3D" and prescribe 2D Motion as the MVP. The older avatar spec similarly says 3D should come later.

That was sensible before we decided Bartholomew was important enough to become the interface to the entire studio.

I would now promote him from:

> animated page decoration

to:

> **canonical 3D interactive character**

and retire this current runtime:

```text
PNG
 + CSS wobble
 + PNG swapping
```

as soon as the GLB exists.

The current `package.json` doesn't even contain Three.js—only Motion—so nothing about the current implementation is genuinely 3D.

# The production brief I'd give the 3D artist

This is what I would send, essentially verbatim:

```text
PROJECT
Bartholomew III — permanent 3D brand mascot for MythicBee.

REFERENCE
Match supplied 2D anime character exactly:
gold armored bee, large purple eyes, black/gold abdomen,
four pale faceted wings, red flowing cape, black antennae.

STYLE
Premium stylized animation-film character.
Not photorealistic.
Not generic Pixar.
Preserve the graphic/anime proportions of the source artwork.

OUTPUT
Canonical Blender source file.
Web-optimized GLB.
Transparent-background compatible.
PBR materials.
Clean topology.
Proper UVs.
LOD-friendly topology.

RIG
Root/body/head/abdomen
2 articulated arms + claws
4 independent wings
2 multi-joint antennae
cape bone chain
eye aim controls
jaw/mouth control

MORPH TARGETS
blink L/R
happy eyes
surprised eyes
determined eyes
smile
A / E / O mouth
closed mouth

ANIMATION CLIPS
idle_hover
listen
think
talk_idle
takeoff
flight
bank_left
bank_right
land
wave
point_left
point_right
inspect
present
celebrate
magic_cast
surprised
sleep

CRITICAL
Flight must feel insect-like rather than humanoid.
Wing flutter should be independently controllable at runtime.
Cape and antennae must support secondary spring motion.
Animations must loop cleanly where appropriate.

TARGET
Modern mobile + desktop WebGL.
GLB intended for Three.js.
Keep final web asset comfortably under ~15 MB,
with compressed web textures.
```

That is the asset I would pay for.

Once you own that file, **everything else becomes software**.

And we never have to redraw Bartholomew again.

# The resulting experience

Page loads.

Nothing.

A buzz enters from somewhere outside the viewport.

A tiny shadow sweeps across the hero.

Bartholomew rockets in from above the navigation, banks around the MythicBee logo, loops once, decelerates, wings beating, cape trailing behind him, and settles into a hover beside:

> **Make something for someone.**

He looks toward the user.

Eyes blink.

Antennae twitch.

Cape settles.

Then:

> "Ah. There you are."

Click him.

Microphone activates.

> **"Bartholomew the Third, Keeper of MythicBee. Who are we making mythical today?"**

You:

> "It's Father's Day."

His wings slow.

Head tilts.

> **"Your father. Excellent. Tell me what makes the man himself."**

You:

> "He's turning sixty, supports Liverpool, loves his Labrador..."

He pauses.

Eyes drift toward the catalogue.

Turns.

Wings accelerate.

**zzzzzzzzzz—**

He physically flies across the page and lands beside GameWinners.

> **"I may have something rather perfect."**

That is the product.

And I think it's worth doing **properly in 3D now**, because Bartholomew is no longer garnish. He's potentially the thing people remember about MythicBee.

[1]: https://threejs.org/manual/en/animation-system.html?utm_source=chatgpt.com "Animation System"
[2]: https://docs.blender.org/manual/en/dev/addons/scene_gltf2.html?utm_source=chatgpt.com "glTF 2.0 - Blender 5.3 Manual"
[3]: https://help.meshy.ai/en/articles/16231707-how-to-create-3d-animation-with-auto-rigging?utm_source=chatgpt.com "How to Create 3D Animation with Auto Rigging | Meshy Help Center"
[4]: https://three.ws/forge-studio?utm_source=chatgpt.com "Studio · Object + Avatar from text · three.ws"
[5]: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.pdf?utm_source=chatgpt.com "glTF™ 2.0 Specification"
[6]: https://gsap.com/docs/v3/Plugins/MotionPathPlugin/?utm_source=chatgpt.com "MotionPath | GSAP | Docs & Learning"
[7]: https://www.three.ws/create-agent?utm_source=chatgpt.com "Create an agent · three.ws"
[8]: https://www.three.ws/integrations?utm_source=chatgpt.com "Integrations — three.ws"
[9]: https://www.three.ws/tour?utm_source=chatgpt.com "Guided Tour: a 3D guide walks you through three.ws · three.ws"
[10]: https://three.ws/docs/walk/getting-started?utm_source=chatgpt.com "Getting started — Walk docs — three.ws"
[11]: https://three.ws/rig-doctor?utm_source=chatgpt.com "Rig Doctor · Will your GLB animate? · three.ws"
[12]: https://three.ws/changelog/2026-07-07-give-your-assistant-a-living-3d-body-that-lip-syncs-and-emotes-in-the-chat?utm_source=chatgpt.com "Changelog · three.ws"
[13]: https://three.ws/lipsync?utm_source=chatgpt.com "TTS-driven lipsync · three.ws"
[14]: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input?utm_source=chatgpt.com "WebSocket | ElevenLabs Documentation"
[15]: https://8thwall.org/?utm_source=chatgpt.com "8th Wall - Open Source AR & 3D"
