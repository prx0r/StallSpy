# Bartholomew 3D — The Real Path
**Date:** 2026-09-06
**Status:** CANONICAL — this is what we're building

---

## Current state

| Component | Status |
|-----------|--------|
| Canonical 2D art | ✅ |
| AI 3D interpretation | ✅ |
| GLB file | ✅ |
| Three.js loading | ✅ |
| Procedural animation idea | ✅ |
| Runtime | ⚠️ syntax errors |
| Part mapping | ❌ |
| Canonical 3D likeness | ⚠️ not locked |
| Live main-site 3D | ❌ |
| Voice → 3D body | ❌ |

---

## The blocker

**We need one faithful, part-addressable 3D Bartholomew asset.**

Everything else is code.

---

## The path (no Blender)

```
CANONICAL 2D BARTHOLOMEW
        │
        ▼
MULTI-VIEW REFERENCES
front / ¾ / side / back
        │
        ▼
THREE.WS / RODIN
image → 3D
        │
        ▼
candidate.glb
        │
        ▼
THREE.WS FORGE
Split into parts
        │
        ▼
bartholomew.glb
        │
   optional Meshy Smart Rig
        │
        ▼
BARTHOLOMEW RIG MANIFEST
(barth-rig.json)
        │
   ┌────┼────────┐
   │    │        │
rigid  soft    facial
parts  parts   parts
   │    │        │
JS     shaders  JS/morphs
pivots          │
   │    │        │
   └────┼────────┘
        ▼
BartholomewRuntime
   Three.js
        │
   ┌────┼────────┐
   │    │        │
  body flight  speech
 motion system  system
   │    │        │
   └────┼────────┘
        │
    INWORLD
```

---

## barth-rig.json

Explicitly map GLB parts to character components:

```json
{
  "version": 1,
  "root": "Bartholomew",
  "parts": {
    "body": "mesh_02",
    "head": "mesh_07",
    "eyeLeft": "mesh_11",
    "eyeRight": "mesh_12",
    "wingFrontLeft": "part_03",
    "wingRearLeft": "part_04",
    "wingFrontRight": "part_05",
    "wingRearRight": "part_06",
    "antennaLeft": "part_08",
    "antennaRight": "part_09",
    "armLeft": "part_13",
    "armRight": "part_14",
    "cape": "part_17"
  }
}
```

---

## Wing animation (no Blender)

```
idle       12 Hz
listening   8 Hz
thinking    6 Hz
talking    15 Hz
excited    21 Hz
flying     26 Hz
landing    26 → 4 Hz
sleeping    0 Hz
```

Flight velocity feeds wing frequency:
```
speed ↑ → wing frequency ↑
       → bank angle ↑
       → cape lag ↑
       → antenna deflection ↑
```

---

## Cape without Blender

Vertex shader:
- attachment edge = fixed
- distance from attachment increases → sine displacement
- cape waves more toward trailing edge
- amount depends on velocity

---

## Antennae

Two or three procedural pivot segments per antenna.
Tiny spring solver: head moves → base moves → tip lags → spring catches up.

---

## Face

- Pupil tracking (trivial if eyes are separate)
- Blinking (eyelid meshes or eye-scale)
- Talking (mouth closed/slight/open + audio amplitude)
- Later: wawa-lipsync → viseme → mouth state

---

## What to do next

1. Fix `bartholomew-runtime.html` — rename `anim` to `motion`, remove duplicate `t`, use `THREE.Clock`
2. Stop generating style variants — use only canonical art
3. Make 4 canonical reference views from character sheet
4. Run through three.ws Image→3D and Rodin
5. Run three.ws Split into parts
6. Create `barth-rig.json`
7. Animate as rigid articulated Three.js puppet
8. If arms/head need deformation → Meshy Smart Rig in-browser
9. Replace 2D `<img>` on production site

**No Blender required.**
