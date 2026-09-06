# TODAY.md — 2026-09-06

## Session Notes

### What we built
- 3D Bartholomew GLB from three.ws Forge (4.2MB)
- Three.js runtime with procedural animations
- Hive Activity Engine (186 entries)
- Gift Intelligence (adaptive question bank)
- Worker proxy for Cloudflare AI (token secure)
- Product Language, Supplier docs, GiftGraph architecture
- Honey currency system, BeeSession system
- Rig mapper web tool, barth-rig.json manifest

### What's working
- 3D GLB renders in browser
- Procedural wing flutter, eye tracking, cape physics
- LLM responses via worker proxy
- Gift Brief extraction
- Concept generation

### What's broken
- Site still shows 2D poses (not 3D runtime)
- Duplicate response bug (async timing)
- Three.js runtime not in main site
- Inworld voice not started
- edge-tts browser fallback only

### Key decisions
- Worker proxy for Cloudflare AI (token stays server-side)
- No Blender — use three.ws Forge + procedural animations
- Product Language frozen: "Make it mythical"
- GiftGraph as data moat
- Honey as AI credits, not money-off

### Files created/modified
- bartholomew-ai.glb, bartholomew-v2.glb
- barth-rig.json, puppet.html, rig-mapper.html
- THE-REAL-PATH.md, CANONICAL-BUILD.md
- worker/index.js (token server-side)
- OPEN-THREADS.md, HANDOVER.md
- All supplier docs

### Disk: 547M total, 138M Mythicbee, 69M 3D assets
