# EasyEtsy Demo Flow — Dog Roast V1

## 1. Exact Etsy buyer flow

For Dogcasso, each product should be a **made-to-order digital listing**, not an instant download. Etsy explicitly supports custom digital files made after purchase. ([Etsy Help][1])

The buyer journey is:

**1. Buyer lands on listing**
They see our title, images, example videos and price.

**2. Before checkout, Etsy shows our Custom Options fields.** Etsy now supports up to **5 personalization questions** per listing: text boxes, dropdowns and one file-upload field. ([Etsy Help][2])

**3. They upload the photo(s) on the listing itself.** One upload field can accept up to **10 files**, each up to **100 MB**, including JPG, PNG and HEIC. If we mark it required, they cannot check out without supplying the required file(s). ([Etsy Help][2])

**4. They fill in name/facts/tone.**

**5. They click Add to Cart / Buy Now and pay.**

**6. Order appears in our Etsy Orders page with their personalization information.** ([Etsy Help][2])

**7. We generate + QA the film.**

**8. We complete the order and upload the finished digital file.** For made-to-order digital orders Etsy lets the seller attach up to **5 finished files, max 20 MB each** and then mark the order complete. Etsy emails the buyer that the files are ready. ([Etsy Help][1])

So yes:

> **upload photo → fill details → pay → we produce it → Etsy sends finished film**

No need for Google Forms or manually messaging buyers.

---

## 2. Important Etsy annoyance: MP4 delivery

Current Etsy digital-download supported file types include `.mov`, `.mpeg` and `.zip`, but their published list **doesn't include `.mp4`**. ([Etsy Help][3])

So initially I would produce:

**`Birthday_Dave.mov`** — H.264/AAC encoded and under 20 MB

and perhaps optionally:

**`Birthday_Dave_MP4.zip`**

containing the normal MP4.

Don't make buyers jump through external forms/sites yet.

Another quirk: Etsy says digital purchases currently **can't be downloaded directly through the Etsy app**; buyers need Etsy in a mobile browser or desktop. ([Etsy Help][4])

This strengthens the case for Dogcasso.com later, but it isn't a reason to delay Etsy.

---

## 3. Etsy listing previews need special treatment

Our Etsy listing demo video can be **3–15 seconds**, MP4 is accepted for listing media, and Etsy currently allows up to two listing videos.

But:

> **Etsy strips the audio from listing videos.**

([Etsy Help][5])

That matters a lot for Dog Roast / Breaking News.

Therefore every Etsy demo needs **burned-in captions**.

Example:

dog sitting on talk show:

**INTERVIEWER:**
"So what do you think of Dave?"

**DOG:**
"Yeah, I think he's weird too…"

beat

**"…but somebody has to love him."**

Audience reaction visually.

Then:

**MAKE YOUR DOG ROAST YOU — £4.99**

The actual purchased film has audio.

TikTok/Instagram gets the full audio version.

---

## 4. Exact `DOG_ROAST_V1` Etsy listing

I would make the first product simpler than we originally discussed.

Don't require owner + dog.

Require **only the dog**.

### Custom Option 1 — File Upload

**Upload your dog**

Required: YES
Files: 1

Instructions:

> Clear photo showing your dog's face. Good lighting, no filters. Front or 3/4 view works best.

### Custom Option 2 — Text

**Owner's first name**

Required.

Example:

> Dave

### Custom Option 3 — Text

**What's funny about them?**

Required.

Example:

> He talks to the dog like it's a human and always steals the dog's side of the sofa.

### Custom Option 4 — Dropdown

**Roast level**

* Cute
* Cheeky
* Savage

### Custom Option 5 — Text

**Anything we must include or avoid?**

Optional.

That's it.

Etsy actually recommends fewer, clearly defined questions rather than making personalization cumbersome. ([Etsy Help][2])

The buyer should **not approve a script**.

---

## 5. Breaking News is even simpler

### `BREAKING_NEWS_BIRTHDAY_V1`

**Upload:** 1 clear face photo.

Then:

**Name**
Dave

**Age**
30

**Funny fact / running joke**
Still tells everyone he's 25.

**Tone**
Friendly / Roast / Savage

Done.

Then our template turns that structured data into the script automatically.

---

## 6. Meet Tom

This is where Etsy's new upload field becomes excellent.

### Upload

> Upload 3–5 clear photos of Tom.

We can allow up to five.

Then:

**Name**

**Occasion**

**Tell us three things about them**

**Tone**

No script.

No storyboard selection.

No "prompt your movie."

We're selling:

> **You tell us about them. Dogcasso makes the film.**

---

## 7. The H3 endpoint selection is now very clear

This is important.

fal currently exposes three H3 Max modes we care about.

### `text-to-video`

Use when there is **no customer's subject**.

Perfect for:

* generic Dogcasso advertisements;
* testing meme formats;
* creating background shots;
* market-testing concepts before building personalization.

H3 Max supports 5-second default generation, 480P/768P, seeds and prompt expansion. ([Fal][6])

---

### `image-to-video`

Use when the customer's image should literally define the **opening frame**.

Perfect for:

> Santa Was In Your Room.

fal explicitly treats `image_url` as the first frame and can additionally accept `end_image_url` as the final frame. ([Fal][7])

That gives us a very good production trick.

Instead of asking:

> "Here's a room. Somehow make Santa appear."

we can create:

**FRAME A:** untouched customer living room.

**FRAME B:** image-edited version of exact same room with our canonical Santa crouched beneath tree.

Then H3 does:

> **first frame → controlled motion → last frame**

MiniMax explicitly recommends first-frame state → observable intermediate changes → convergence on final frame for this mode. ([Hugging Face][8])

Much more deterministic.

---

### `reference-to-video`

Use when customer images define **who the characters are**, rather than the opening composition.

Perfect for:

* customer's dog;
* birthday person;
* Mum;
* partner;
* multiple friends;
* Dogcasso mascot;
* recurring Santa.

fal lets prompts refer explicitly to:

**Image 1**
**Image 2**
**Video 1**
**Audio 1**

and currently supports up to **12 reference assets total**. ([Fal][9])

So:

> Image 1 = Dave's dog
> Image 2 = canonical talk-show set reference
> Image 3 = visual style reference

Then generate.

---

## 8. MiniMax's own prompt documentation is much more structured than normal prompting

This was the biggest useful research result.

Their preferred prompt isn't:

> "cute realistic dog on funny talk show, cinematic"

It's essentially a production document.

MiniMax recommends explicitly describing:

**style → composition → subject → action → camera → dialogue → sound → music → shot transitions.**

([Hugging Face][8])

And for reference generation, they recommend defining what every reference actually contributes and whether its characteristics are fully preserved or merely used as loose guidance. ([Hugging Face][10])

So Dogcasso's backend should compile simple buyer inputs into something like this.

---

## 9. Example: properly structured Dog Roast prompt

Not necessarily the literal final production prompt yet, but this is the architecture.

```text
Image 1 defines the dog's identity.

Preserve Image 1's breed, facial proportions, fur colour,
fur pattern, ear shape, eye colour, muzzle, nose and distinctive
facial features throughout the entire target video.

[Shot 1]
Live-action cinematic television comedy panel show.

A medium close shot frames the dog from Image 1 seated behind
a polished dark desk in a warm studio. The dog looks completely
real and naturally integrated into the environment.

The camera holds almost static.

The dog looks slightly off-camera toward the interviewer, then
slowly turns its eyes toward camera with a dry, intelligent expression.

The dog's speaking voice (S1) is dry, calm and slightly amused.

(S1) says:
"Yeah, I also think Dave's weird."

The dog pauses for approximately half a second.

The dog's mouth pulls into a tiny smug smile.

(S1) continues:
"But someone has to love him, am I right?"

Immediately after the punchline, an off-camera studio audience
bursts into natural laughter.

The dog holds the camera's gaze for one beat without moving.

overall_soundscape:
Quiet television studio ambience beneath the dialogue.
Natural audience laughter begins immediately after the punchline.

non_diegetic_music:
N/A
```

Notice what we're **not** asking it to do:

* render DOGCASSO.COM;
* render subtitles;
* generate title cards;
* generate our logo;
* make complicated transitions.

Those happen afterward deterministically.

---

## 10. Camera instructions should be literal

MiniMax's own vocabulary includes:

**Push In**
**Pull Out**
**Pan Left/Right**
**Truck Left/Right**
**Tilt**
**Arc Shot**
**Tracking Shot**
**Static Shot**

and says camera instructions should include range/speed when meaningful. ([Hugging Face][8])

So don't write:

> dramatic camera.

Write:

> The camera pushes in with small amplitude at slow speed toward the dog's face.

This is exactly the sort of thing we should encode in templates.

---

## 11. Dialogue should have stable speaker IDs

For multiple-character scenes MiniMax explicitly recommends:

```text
(S1)
(S2)
(S3)
```

with the ID remaining attached to the same character across shots. ([Hugging Face][8])

So our future family roast becomes:

```text
Image 1 = Mum = S1
Image 2 = Dad = S2
Image 3 = dog = S3
Image 4 = birthday person
```

Then the compiler never loses track.

---

## 12. We should deliberately separate AI generation from normal editing

The model should generate only the hard part:

> **convincing moving footage.**

Then our deterministic compositor handles:

* titles;
* captions;
* logo;
* Dogcasso.com sting;
* freeze frames;
* meme labels;
* music;
* sound effects;
* aspect ratios;
* final compression;
* QR graphics;
* card still.

This dramatically increases consistency.

Example:

```text
H3 output
   ↓
trim best 7.8 sec
   ↓
audio cleanup
   ↓
caption template
   ↓
audience sting
   ↓
DOGCASSO.COM 0.8 sec
   ↓
MOV + MP4
```

---

## 13. fal settings I'd use during development

### Cheap exploration

```text
resolution: 480P
prompt_expansion_mode: balanced
seed: saved
```

### Candidate winner

```text
resolution: 768P
prompt_expansion_mode: quality
seed: saved
```

fal says `balanced` does quick prompt rewriting, while `quality` can spend up to roughly 30 seconds producing a richer expanded prompt. It also returns the `expanded_prompt`, so we can record exactly what ultimately went into the generation. ([Fal][7])

**Save that expanded prompt.**

It is incredibly useful for learning why a render worked.

Our experiment database should be:

```text
template
version
buyer-like inputs
source images
raw prompt
expanded prompt
endpoint
seed
resolution
output
human score
identity score
motion score
audio score
reroll?
cost
```

That becomes the real Dogcasso recipe library.

---

## 14. Etsy V1 operational pipeline

I'd implement **manual orchestration first**:

```text
ETSY LISTING
      ↓
customer uploads photo(s)
customer enters details
      ↓
PAYS
      ↓
ETSY ORDER
      ↓
we inspect inputs
      ↓
normalize photo
      ↓
template compiler
      ↓
H3 MAX
      ↓
QA
      ↓
reroll if needed
      ↓
FFmpeg deterministic edit
      ↓
MOV under 20 MB
      ↓
upload to Etsy order
      ↓
COMPLETE ORDER
      ↓
buyer receives Etsy email
```

That is enough to sell.

---

## 15. Then automate everything except one Etsy step

Etsy's Open API became substantially better for us this year: the API now officially supports creating/reading those multiple personalization fields, including file-upload questions. ([Etsy Developers][11])

So eventually:

```text
Etsy order
    ↓
Dogcasso worker sees order
    ↓
parses personalization
    ↓
downloads/intakes assets
    ↓
generates
    ↓
QA agent
    ↓
renders finished product
```

However, there is currently an important API hole:

**Etsy does not expose an official API operation to attach a unique finished made-to-order digital file to a specific order and complete that custom digital order.**

That limitation was still being discussed by Etsy Open API users in late 2025/2026. ([GitHub][12])

So initially the final step may remain:

> **human opens completed order → Upload File → Complete Order**

That's like 20 seconds.

Everything expensive and tedious can still be automated.

And we should **not** hack around Etsy with browser automation just to save those 20 seconds.

---

## Therefore I would freeze our first Etsy flow at this

## Listing #1

### **My Dog Roasts Me — Personalised Birthday Video**

£4.99.

Inputs:

**1 photo**
**owner's name**
**funny fact**
**roast intensity**
**optional avoid/include**

Output:

**8–10 sec film**

Production target:

> **customer does 30 seconds of work; Dogcasso does everything else.**

And before we even publish it, we generate perhaps **10–20 controlled test cases using different dog breeds/photos**.

The key R&D question isn't "can H3 make a talking dog?"

It's:

> **Can `DOG_ROAST_V1` successfully produce a recognizably identical customer dog, deliver the punchline naturally and look good enough in at least ~80% of first renders?**

If yes, that's a product.

If only 40% of renders work, we keep refining the recipe before selling it.

That should be the Dogcasso methodology for every subsequent template.

---

[1]: https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings "How to Manage Your Digital Listings – Etsy Help"
[2]: https://help.etsy.com/hc/en-us/articles/360000344528-How-to-Offer-Personalized-Listings "How to Offer Personalized Listings – Etsy Help"
[3]: https://help.etsy.com/hc/en-gb/articles/115015628347-How-to-Manage-Your-Digital-Listings "How to Manage Your Digital Listings – Etsy"
[4]: https://help.etsy.com/hc/en-us/articles/115013328108-How-to-Download-a-Digital-Item "How to Download a Digital Item – Etsy Help"
[5]: https://help.etsy.com/hc/en-us/articles/360053206073-How-to-Add-Listing-Videos "How to Add Listing Videos – Etsy Help"
[6]: https://fal.ai/models/minimax/h3-max/text-to-video/api "MiniMax H3 Max Text to Video API Docs | fal"
[7]: https://fal.ai/models/minimax/h3-max/image-to-video/api "H3 Max Image to Video API Docs | fal"
[8]: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md "docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md · MiniMaxAI/MiniMax-H3 at main"
[9]: https://fal.ai/models/minimax/h3-max/reference-to-video/api "H3 Max Reference to Video Image to Video API Docs | fal"
[10]: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md "docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md · MiniMaxAI/MiniMax-H3 at main"
[11]: https://developers.etsy.com/documentation/tutorials/personalization-migration/ "Personalization Migration Guide | Etsy Open API v3"
[12]: https://github.com/etsy/open-api/discussions/1514 "API for complete Order digital with mode Make to order · etsy open-api · Discussion #1514 · GitHub"
