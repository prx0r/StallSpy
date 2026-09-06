# Bartholomew 3D — The Canonical Build
**Date:** 2026-09-06
**Status:** CANONICAL — this is the path

---

## Current state

| Area | Quality |
|------|---------|
| 3D architecture | 7/10 |
| Browser rendering proof | 8/10 |
| Character likeness | ~5/10 |
| Rigging | 1/10 |
| Character animation | 2/10 |
| "Alive" feeling | 2/10 |
| Production integration | 2/10 |
| Potential | 10/10 |

---

## The canonical S-tier route

```
OUR BARTHOLOMEW ART
        │
        ▼
Rodin Gen-2.5 multi-view
   high-quality blockout
        │
        ▼
human creature artist
cleanup / proportions / topology
        │
        ▼
CUSTOM BLENDER RIG
4 wings + arms + eyes +
antennae + cape + mouth
        │
        ▼
bartholomew-v1.blend
        │
        ▼
optimized GLB
        │
        ▼
THREE.JS
        │
 ┌──────┼─────────────────┐
 │      │                 │
clips procedural         page flight
 │      │                 │
 └──────┼─────────────────┘
        │
   character brain
        │
 Inworld + GiftBrief
```

---

## Don't auto-rig the final bee

Commission:

> **Stylized creature model cleanup + custom game/web rig + facial morphs + 12–18 animation clips.**

Current Upwork: $1k–$3k for canonical asset.

---

## The rig

```
Root
 ├─ body
 │   ├─ abdomen
 │   └─ head
 ├─ arm_L → forearm → claw
 ├─ arm_R → forearm → claw
 ├─ wing_upper_L
 ├─ wing_lower_L
 ├─ wing_upper_R
 ├─ wing_lower_R
 ├─ antenna_L_01 → 02 → 03
 ├─ antenna_R_01 → 02 → 03
 └─ cape_root
      ├─ cape_L_01 → 02 → 03
      ├─ cape_C_01 → 02 → 03
      └─ cape_R_01 → 02 → 03
```

Morphs: blink, happy/determined/surprised eyes, jaw, visemes, smile.

---

## Three animation layers

1. **Authored animation** — Blender clips, AnimationMixer crossfades
2. **Procedural animation** — wing frequency, eye target, head target, cape inertia
3. **Semantic animation** — AI says `fly_to("#upload")`, `point_at("#gamewinners")`

---

## Speech

wawa-lipsync → visemes → morph targets. No GPU needed.

---

## Performance targets

| Asset | Target |
|-------|--------|
| GLB download | < 6–8 MB |
| triangles | 30k–60k |
| textures | 2K |
| skeleton | <50 bones |
| morph targets | 10–20 |
| animation clips | 12–18 |
| desktop | 60 fps |
| mobile | 30–60 fps adaptive |

---

## Next steps

1. Generate via Rodin Gen-2.5 + Tripo + three.ws challengers
2. Pick best shape
3. Hire creature artist for bartholomew-v1.blend
4. Work via Vagon/RunPod for Blender
5. Replace production <img> with Three.js canvas
6. Build BartholomewRuntime
7. Connect Inworld
