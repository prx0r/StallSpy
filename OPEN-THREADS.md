# Open Threads — Session Review
**Date:** 2026-09-06
**Status:** NEEDS RESOLUTION

---

## Critical Issues

### 1. Duplicate response when typing "hey"
**Status:** UNRESOLVED
**What happens:** User types "hey", gets "Something went wrong" immediately, then sees greeting
**Root cause:** Likely timing issue with async functions or module loading
**Fix needed:** Test actual browser execution, check console errors

### 2. Site still shows 2D poses
**Status:** UNRESOLVED
**What happens:** Production site (`master.mythicbee.pages.dev`) shows 2D pose images
**Root cause:** `index.html` still uses `<img src="assets/poses/01_neutral.webp">`
**Fix needed:** Replace with Three.js canvas integration

### 3. Three.js runtime not integrated
**Status:** UNRESOLVED
**What happens:** Runtime files exist in `examples/` but aren't in main site
**Root cause:** Separate demo files, not wired into production
**Fix needed:** Integrate `definitive.html` or `puppet.html` into main `index.html`

### 4. barth-rig.json not connected
**Status:** UNRESOLVED
**What happens:** Rig manifest exists but runtime doesn't use it
**Root cause:** Runtime uses hardcoded mesh name matching
**Fix needed:** Update runtime to load `barth-rig.json`

### 5. Inworld voice still scaffold
**Status:** NOT STARTED
**What happens:** Voice integration placeholder only
**Root cause:** No API key, no WebRTC setup
**Fix needed:** Get Inworld API key, wire WebRTC

### 6. edge-tts not wired to browser
**Status:** PARTIAL
**What happens:** Server-side TTS works, browser uses Web Speech API
**Root cause:** Cloudflare Workers can't run Python
**Fix needed:** Set up proper TTS backend

---

## What Works

| Component | Status |
|-----------|--------|
| 3D GLB file | ✅ |
| Three.js rendering | ✅ |
| Procedural animations | ✅ |
| Hive Activity Engine | ✅ |
| Gift Intelligence | ✅ |
| Product Language | ✅ |
| Supplier docs | ✅ |
| GiftGraph architecture | ✅ |
| edge-tts (server) | ✅ |
| Cloudflare LLM | ✅ |
| Cloudflare Flux | ✅ |

---

## Priority Order

1. Fix duplicate response (critical UX bug)
2. Integrate 3D runtime into main site
3. Wire barth-rig.json to runtime
4. Test on mobile + desktop
5. Commit all fixes

---

## Files to Update

| File | Issue |
|------|-------|
| `site/index.html` | Still uses 2D poses |
| `site/js/bee-controller.js` | Needs 3D integration |
| `bartholomew-3d/examples/` | Too many duplicates |
