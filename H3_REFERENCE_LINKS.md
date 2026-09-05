# Dogcasso — H3 Prompting Reference Links

Canonical sources for MiniMax H3 prompt engineering.

---

## Official MiniMax Guides

### Base Video Prompt Writing Guide
**URL:** https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md

Covers:
- Shot-by-shot structure with timestamps
- Camera terminology (push in, pull out, pan, tracking, arc)
- Speaker IDs for dialogue (S1, S2, etc.)
- Sound design layers (dialogue, ambience, foley, music)
- Observable motion descriptions
- Multi-shot clip formatting

### Reference-Mode Prompt Writing Guide
**URL:** https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md

Covers:
- Reference image roles (identity, environment, motion, voice, style)
- Preservation rules for uploaded subjects
- How to assign explicit jobs to each reference
- Identity retention across shots
- Multiple reference composition

---

## fal AI Guides

### H3 Max API Documentation
**URL:** https://fal.ai/models/minimax/h3-max/reference-to-video/api

Covers:
- Three modes: text-to-video, image-to-video, reference-to-video
- Up to 12 image/video/audio references
- Seed control for reproducibility
- Quality prompt-expansion mode
- 5-15 second clips at 480p/768p
- 16:9 and 9:16 support
- Native audio generation
- Expanded prompt returned (save for experiment logs)

### 44-Example H3 Prompting Collection
**URL:** https://fal.ai/learn/devs

Best practical corpus: prompts alongside actual generated videos.

---

## Key Rules (Summary)

### 1. References Have Jobs
> Image 1 defines Tom's facial identity and hairstyle.
> Image 2 defines Tom's clothing.
> Image 3 defines the dog.
> Preserve their identities throughout.

### 2. Describe Observable Motion
Bad: "Santa looks magical."
Good: "Santa enters from frame left, walks three steps toward the tree, crouches, places one wrapped parcel beneath it, then turns his head toward the camera."

### 3. Camera Direction Is Literal
Use: push in, pull out, pan, tracking shot, arc shot, static, dolly, crane.

### 4. Use Timed Shots
```text
[Shot 1] ...
[Shot 2] At 00:03.500, the camera cuts to...
[Shot 3] At 00:07.000...
```

### 5. Treat Sound Like Production
Specify separately: dialogue, room ambience, foley, music.

### 6. Preserve Identities Explicitly
> Facial proportions, eye colour, hairstyle, skin tone and distinctive features remain unchanged.

---

## Experiment Logging

Save for every generation:
- input prompt
- expanded prompt (fal returns this)
- seed
- output video
- human score (1-5)
- generation time
- GPU cost
- reroll count

**That's how we learn which recipes reliably make good films.**
