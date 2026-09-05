# MiniMax H3 — Full-Reference Mode Prompt Writing Guide

Source: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md

---

## 1. Overall Structure

A complete rewrite output consists of six sections:

| Section | Purpose |
|---------|---------|
| `subject_definitions` | Defines referenced content and its reference labels |
| `summary` | Summarizes the task type, target video, and main reference relationships |
| `retention_analysis` | Describes how referenced content is preserved, transferred, or reused |
| `detailed_description` | Describes visuals, actions, shots, sound, and dialogue in playback order |
| `overall_soundscape` | Summarizes ambience and physical sounds |
| `non_diegetic_music` | Describes background music audible only to the audience |

---

## 2. Reference Labels

| Label | Meaning |
|-------|---------|
| `<Subject N>` | Visible content abstracted from reference assets that can be reused or modified |
| `<Picture N>` | A reference image used as a concrete target frame or shot-planning anchor |
| `<Video N>` | A reference video that provides an editing source, continuation starting point, or temporal structure |
| `<Audio N>` | An audio signal that is copied or referenced |

---

## 3. Retention Relationship Markers

### Visible Content

| Marker | Meaning |
|--------|---------|
| `fully_preserved` | The defined role of the referenced content is fully preserved |
| `partially_preserved` | The referenced content is still used, but some defined characteristics are changed |
| `attribute_transfer` | Referenced characteristics are transferred to a different identifiable target subject |
| `weak_reference` | Only broad similarity in style, category, composition, or atmosphere is retained |

### Audio

| Marker | Meaning |
|--------|---------|
| `fully_copy` | The complete source audio serves as the target video's complete final audio track |
| `partially_copy` | Only part of the timeline or selected audio layers are copied |
| `reference` | The signal is not copied directly; only timbre, rhythm, music style, dialogue content, or sound texture is referenced |
| `weak_reference` | Only broad similarity in category or atmosphere is retained |

---

## 4. Task Types

| Task Type | When to Use |
|-----------|-------------|
| `keyframe completion` | An image serves as the target video's first frame, keyframe, last frame, or another concrete frame anchor |
| `reference generation` | An image, video, or audio asset provides generation guidance without serving as a concrete frame |
| `video editing` | An existing source video is directly modified |
| `video continuation` | New content continues, extends, resumes, or transitions from an existing source video |
| `audio reuse` | The same audio signal is reused in full or in part |
| `audio reference` | The audio signal is not copied directly; only its music style, timbre, dialogue or lyric content, sound-effect texture, beat, or continuity is referenced |

---

## 5. Key Rules

### 5.1 Subject Definitions

Give each item its own line and explain what its label denotes, its reference role, and the main features to follow:

```text
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue cardigan, and a thin silver necklace.
```

When the same subject comes from multiple assets:
```text
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose walking motion comes from <Video 1>.
```

### 5.2 Picture as Frame Anchor

When an image serves as a concrete frame:
```text
<Picture 2> is the first frame of [Shot 1], showing a woman seated beside a café window.
```

When an image is only a storyboard reference:
```text
<Picture 3> is a storyboard reference for [Shot 1] and [Shot 2], defining their viewpoint, subject placement, and shot order.
```

### 5.3 Speaker IDs with References

When a referenced subject physically speaks, retain both the visual reference label and the speaker ID:

```text
<Subject 2> (S1) turns toward the woman and says, <d>[English] Last summer, I went to my grandfather's house. He talked about you.</d>
```

### 5.4 Audio as Voice Reference

```text
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

---

## 6. Complete Example

```text
subject_definitions:
<Subject 1> is the coffee-shop environment in <Picture 1>, featuring an exposed brick wall, an orange tufted sofa with patterned pillows, a neon sign, and a wooden coffee table.
<Subject 2> is the fluffy white Samoyed in <Picture 2>, <Picture 3>, and <Picture 4>, with thick white fur, pointed ears, a dark nose, and a curved tail.
<Subject 3> is the young blonde woman in <Video 1>, with long blonde hair and a light-pink button-down shirt with rolled-up sleeves.
<Subject 4> is the young man in <Video 2>, with short wavy brown hair and a dark-grey hoodie with drawstrings.
<Audio 1> is the voice-timbre reference for <Subject 3> (S1), containing a spoken English vocal layer.

summary:
[reference generation + audio reference] The target video shows <Subject 3> eating a cookie in <Subject 1>. <Subject 4> enters with <Subject 2>, which lunges toward the cookie. The three-shot exchange uses <Audio 1> as the voice-timbre reference for <Subject 3> and ends with a canned audience laugh.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table are retained.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the Samoyed's thick white fur, pointed ears, dark nose, and curved tail are retained.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the blonde woman's identity, long hair, and light-pink shirt are retained.
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the young man's short wavy brown hair and dark-grey hoodie are retained.
<Audio 1>: reference - its vocal timbre guides the dialogue delivery of <Subject 3> without copying the original signal.

detailed_description:
The target video uses a realistic multi-camera sitcom style with warm indoor lighting.
[Shot 1] A medium shot establishes <Subject 1>, the coffee shop with its exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table. <Subject 3> (S1), the young woman with long blonde hair and a light-pink button-down shirt with rolled-up sleeves, sits on the sofa holding a chocolate-chip cookie. From the left, <Subject 4>, the young man with short wavy brown hair and a dark-grey hoodie with drawstrings, enters holding the leash of <Subject 2>, the thick-furred white Samoyed with pointed ears, a dark nose, and a curved tail. The dog lunges toward the cookie and pulls the leash taut. <Subject 3> (S1) jerks her hand back and, using the clear youthful voice timbre referenced from <Audio 1>, exclaims with light annoyance, <d>[English] Hey! Watch your dog!</d> She closes her lips and guards the cookie while <Subject 4> pulls the dog back.
[Shot 2] At 00:03.000, the shot cuts to a close-up of <Subject 4> (S2), the young man in the dark-grey hoodie from Shot 1, sitting beside <Subject 3> on the sofa and holding <Subject 2> securely in his arms. <Subject 4> (S2) says in a casual young male voice with a playful tone and an easy conversational pace, <d>[English] He just likes cookies more than me.</d> He closes his mouth into an apologetic smile and strokes the dog's thick white fur.
[Shot 3] At 00:05.000, the shot cuts to a close-up of <Subject 3> (S1), the blonde woman in the light-pink shirt from Shot 1. Her annoyance softens as she looks toward the Samoyed. <Subject 3> (S1) replies in the same clear youthful voice referenced from <Audio 1> with an amused cadence, <d>[English] Well, he has good taste at least.</d> She smiles and raises the cookie in a small toast-like gesture. A classic canned audience laugh begins immediately after the line and continues through the final frame.

overall_soundscape:
Soft indoor coffee-shop room tone continues throughout the scene.

non_diegetic_music:
N/A
```
