# MythicBee — Internal Template Format

Production YAML schema for every scene.

---

## Template Schema

```yaml
id: ROOM_SANTA_001
version: 1
engine: IN_YOUR_ROOM

product:
  title: Santa Was In Your Living Room
  price: 4.99
  category: christmas
  tags: [santa, room, christmas, kids]

inputs:
  room_photo:
    required: true
    type: environment
    description: Clean photo of the room where Santa will appear
  child_name:
    required: false
    type: string
  present_description:
    required: false
    type: string

render:
  endpoint: minimax/h3-max/image-to-video
  duration: 5
  resolution: 768P
  aspect_ratios:
    - 9:16
    - 16:9
  quality: high

storyboard:
  - time: "00:00.000"
    action: "Static camera. Christmas lights flicker in customer's room."
    camera: static
    sound: room ambience, gentle Christmas music
  - time: "00:01.000"
    action: "Santa quietly enters from frame left carrying sack. Walks toward tree."
    camera: static
    sound: footsteps on carpet
  - time: "00:03.000"
    action: "Santa places present beneath tree. Suddenly notices camera."
    camera: push in slowly
    sound: paper rustling
  - time: "00:04.000"
    action: "Finger to lips. Shhh gesture."
    camera: static closeup
    sound: "Shhh" dialogue
  - time: "00:05.000"
    action: "Cut to black."
    camera: none
    sound: music sting

references:
  - id: santa_canonical_v1
    role: character identity
    preserve: [facial features, costume, proportions]
  - id: room_customer
    role: environment
    preserve: [room layout, furniture, lighting]

prompts:
  visual_style: "Cinematic, warm Christmas lighting, photorealistic"
  scene_setting: "Customer's living room with Christmas decorations"
  character: "Santa Claus, traditional red suit, white beard, carrying brown sack"
  dialogue: "(S1) Shhh."
  music: "Gentle Christmas orchestral, building to whimsical sting"
  negative: "extra people, deformed hands, blurry, text overlays"

qa:
  preserve_room: true
  normal_hands: true
  no_extra_people: true
  santa_identity: canonical_santa_v1
  audio_clear: true
  no_artifacts: true

metrics:
  generations: 0
  rerolls: 0
  orders: 0
  conversion_rate: null
  avg_rating: null
  total_revenue: 0

variants:
  - id: ROOM_MONSTER_001
    title: Monster In Your Bedroom
    price: 4.99
    category: halloween
  - id: ROOM_GHOST_001
    title: Ghost In Your Hallway
    price: 4.99
    category: halloween
  - id: ROOM_DINOSAUR_001
    title: Dinosaur In Your Garden
    price: 4.99
    category: kids
```

---

## Fields Explained

| Field | Purpose |
|-------|---------|
| `id` | Unique template identifier |
| `version` | Iteration number (improves with generations) |
| `engine` | Which of the 8 canonical engines |
| `product` | Customer-facing metadata |
| `inputs` | What the customer must provide |
| `render` | GPU endpoint, duration, resolution |
| `storyboard` | Shot-by-shot with timestamps |
| `references` | Identity/role/preservation rules |
| `prompts` | H3 prompt components |
| `qa` | Automated quality checks |
| `metrics` | Performance tracking |
| `variants` | Related templates (same engine, different skin) |

---

## Prompt Compiler Input

The template YAML gets compiled into H3's verbose production prompt:

```text
[Visual Style]
{prompts.visual_style}

[Scene Setting]
{prompts.scene_setting}

[Characters]
{prompts.character}

References:
{references[0].id} defines {references[0].role}.
Preserve: {references[0].preserve}

[Storyboard]
{storyboard entries compiled with timestamps}

[Sound]
Dialogue: {prompts.dialogue}
Music: {prompts.music}

[Negative]
{prompts.negative}
```

---

## Production Pipeline

```text
Customer data
    ↓
Template manifest (YAML)
    ↓
Prompt compiler (YAML → H3 prompt)
    ↓
fal API (H3 render)
    ↓
Automated QA (face check, audio check, artifact check)
    ↓
FFmpeg (text overlays, color grading, aspect ratios)
    ↓
Delivery (MP4 + gift page)
```

---

## Experiment Log Format

For every generation, save:

```yaml
experiment:
  template_id: ROOM_SANTA_001
  version: 1
  input_prompt: "..."
  expanded_prompt: "..."  # fal returns this
  seed: 42
  output_url: "..."
  human_score: 4  # 1-5
  generation_time: 45s
  gpu_cost: $0.08
  reroll_count: 0
  timestamp: "2026-09-05T14:30:00Z"
```

**That's how we learn which recipes reliably make good films.**
