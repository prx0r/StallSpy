# MythicBee — Technical Stack

## Production Pipeline

```text
Customer inputs
    │
    ├── room/photo
    ├── child/pet name
    ├── message
    └── occasion
          ↓
Prompt Recipe
          ↓
Generate first frame
          ↓
MINIMAX H3
I2V / Ref2V
          ↓
QA
          ↓
optional reroll
          ↓
FFmpeg template
          ↓
music/subtitles/title
          ↓
16:9 TV
9:16 phone
          ↓
DELIVER
```

---

## Primary Model: MiniMax H3

**Why H3:**
- #1 open-weight model for text-to-video + audio (Artificial Analysis leaderboard)
- I2V + audio: Elo ~1187 (vs LTX-2.5 Fast ~1044)
- Native stereo audio generation alongside video
- Reference-to-video for character consistency (Santa, recurring characters)
- 4-15 seconds at 768p
- First/last-frame I2V, reference-to-video

**Key capability:** H3 generates audio alongside the video. Santa can say "Hello Oliver! I've heard you've been doing brilliantly at swimming…" — performance, facial movement, ambient fireplace, room audio and voice in one pass.

**Reference mode:** Multiple images/video/audio references — essential for keeping Santa/pets/characters consistent across products.

### GPU Requirements

| Config | VRAM | System RAM | Quality |
|--------|------|------------|---------|
| NVFP4 quantized | ~12.5 GB | Moderate | Good |
| INT8 | ~16.4 GB peak (T2V), ~18.2 GB (Ref2V) | ~75 GB+ (offload) | Very good |
| BF16 full | 96 GB+ | Minimal | Best |

---

## GPU Infrastructure

### Primary: Vast.ai RTX 5090

- **Price:** $0.36-0.51/hr
- **Filter:** RTX 5090 + ≥96GB host RAM + decent NVMe + good reliability
- **At ~$0.40/hr:** $5 buys ~12.5 GPU-hours → 100+ Santa prompts
- **Best for:** Production runs, batch generation, experimentation

### Secondary: RunPod

| GPU | Price/hr | Use case |
|-----|----------|----------|
| RTX 5090 | ~$0.99 | Faster setup, less config |
| RTX Pro 6000 96GB | ~$1.99-2.09 | Full BF16, zero compromise |

**RunPod advantage:** ComfyUI template exists for H3 (boots with workflows for H3 video+audio). Recommends ~85GB storage quantized, ~180-200GB full BF16.

---

## Secondary Model: LTX-2.5

**Role:** Fast drafts, rapid iteration, recipe engineering

**Advantages:**
- Faster iteration cycle
- Good multishot/control
- Excellent ComfyUI ecosystem
- First/middle/last-frame workflows
- Easier recipe engineering

**Keep installed alongside H3. Use for:**
- Rapid prototyping new templates
- Testing storyboard ideas before committing to H3 render
- Budget-conscious batch runs

---

## Workflow Orchestration: ComfyUI

- Visual node-based workflow editor
- Community templates for H3 and LTX
- Custom nodes for face insertion, character consistency
- API mode for programmatic execution

---

## Final Composition: FFmpeg

- Titles and text overlays
- Subtitles (timed to speech)
- Music bed mixing
- Sound design layering
- Aspect ratio conversion (16:9 TV ↔ 9:16 phone)
- Color grading
- Transition effects
- Final render and encoding

---

## Template Schema

Each template stores:

```text
SANTA_ROOM_V001
├── model: minimax-h3-int8
├── seed: 42
├── workflow_json: {comfyui workflow}
├── prompt: "Santa sits beside fireplace..."
├── negative_prompt: ""
├── reference_images: [santa_ref_01.png, santa_ref_02.png]
├── generation_time: 45s
├── gpu_cost: $0.08
├── customer_conversion: 7.2%
├── reroll_rate: 12%
├── rating: 4.7
├── qa_criteria: {face visible, audio clear, no artifacts}
├── fallback_model: ltx-2.5-fast
├── aspect_ratios: [16:9, 9:16]
└── card_artwork: santa_card_template_v3.png
```

---

## What Improves Over Time

| Today | Next quarter | Next year |
|-------|-------------|-----------|
| 5-sec clips | 15 seconds | 60-second coherent films |
| Basic face insert | Consistent characters | Perfect dialogue |
| Single shot | Multi-scene | Pixar-level production value |
| Manual QA | Auto QA | Self-improving templates |

**Our catalogue doesn't become obsolete. `SANTA_IN_YOUR_ROOM` just becomes more convincing.**

---

## Cost Per Unit (Estimated)

| Product | GPU time | GPU cost | Platform | Total COGS |
|---------|----------|----------|----------|------------|
| £4.99 Magic Clip | 15-30s | $0.02-0.05 | £0.50 | ~£0.55 |
| £9.99 Magic Pack | 30-60s | $0.05-0.10 | £0.75 | ~£0.90 |
| £19.99 Studio Perfect | 60-120s | $0.10-0.20 | £1.50 | ~£1.75 |
| £29.99 Mini Movie | 120-300s | $0.20-0.50 | £2.00 | ~£2.50 |
| £7.99 Movie Card | 15-30s + print | $0.05 + £1.00 | £0.75 | ~£1.85 |

**Gross margins: 65-90% depending on tier.**
