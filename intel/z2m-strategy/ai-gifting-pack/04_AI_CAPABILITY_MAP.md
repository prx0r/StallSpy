# AI Capability Map — What Changed by 2026

The thesis becomes materially better because image models and production APIs have moved from novelty generation into editable / structured creative workflows.

## Capability 1 — high-quality image generation + editing
Use cases:
- turn a pet into a specific visual world;
- restore or restyle a family photo;
- produce illustration assets;
- change clothing/background/setting;
- generate coherent visual directions.

Candidate adapters:
- GPT-Image-2
- Gemini image generation/editing
- Ideogram 4.0
- Recraft V4.1
- Adobe Firefly

**Rule:** maintain a provider abstraction. This market is moving too quickly to marry the product to one model.

## Capability 2 — typography is much better, but never trust it for critical customer text

Ideogram explicitly targets production typography and POD/design layouts.
Recraft V4.1 Vector targets illustrations/lettering.
Current models can produce attractive text.

But names, dates and messages are order-critical.

### Production rule
Let AI produce:
- visual style;
- decorative lettering concepts;
- illustration;
- texture;
- composition suggestions.

Then render exact customer text with deterministic:
- SVG;
- Canvas;
- CSS/HTML-to-image;
- PDF typography.

**Never ship a card because the image model appeared to spell “Christopher” correctly.**

## Capability 3 — vector output
Recraft exposes vector models.

This matters for:
- logos;
- line illustrations;
- scalable ornament graphics;
- apparel;
- print at arbitrary size;
- cutting/engraving downstream.

## Capability 4 — transparent assets
Ideogram 4.0 API supports transparent-background PNG output and high resolution tiers.
Background removal is also now commodity.

This is very useful for POD:
- isolate pet/person/art;
- layer over product templates;
- create reusable recipient assets once;
- reuse across card/mug/ornament/wrapping paper.

## Capability 5 — brand/style training
Adobe Firefly Custom Models and Recraft style systems can produce more repeatable art direction.

Moat idea:
- create 20–50 licensed house styles;
- validate which styles convert for recipient/occasion segments;
- train/fine-tune or reference-style them;
- expose friendly names rather than model names.

Example:
- “British storybook”
- “deadpan newspaper”
- “museum print”
- “90s school photo”
- “embroidered folk”
- “minimal Scandi”
- “Victorian naturalist”
- “retro ski poster”
- “medieval manuscript”

## Capability 6 — AI shopping itself is becoming mainstream
The consumer is increasingly comfortable expressing intent conversationally.
Amazon now has recipient/profile-aware shopping features and custom merch generation.
Microsoft's 2026 holiday work says AI usage in holiday shopping will be widespread.

This means the UI can skip traditional category browsing.

## Capability 7 — automatic ad/creative multiplication
One good product concept can become:
- hero image;
- 10 style variants;
- mockups;
- Pinterest pins;
- vertical video storyboards;
- localized text overlays;
- seasonal landing-page art.

This lowers creative-production cost dramatically.

## Recommended generation pipeline

1. **Intent model**
   transforms recipient facts into a structured creative brief.

2. **Concept model**
   generates 6 concept directions, each with:
   - title;
   - emotion;
   - visual motif;
   - exact copy;
   - product fit;
   - risk notes.

3. **Asset generator**
   produces illustration / portrait / transparent assets.

4. **Deterministic compositor**
   builds final product art with exact text and safe zones.

5. **Print QA**
   checks:
   - required pixels;
   - DPI;
   - bleed;
   - safe area;
   - text overflow;
   - face crop;
   - alpha;
   - colour-space warning;
   - profanity/IP moderation.

6. **Mockup generator**
   places finished art onto product scene.

7. **Human approval**
   customer sees exactly what will ship.

8. **Fulfilment**
   submit print-ready asset.

## Estimated AI cost intuition

Modern design APIs are cheap enough that several candidate generations per order can be economical relative to physical-gift margins. For example, Recraft currently lists several V4/V4.1 API generation tiers in the cents-per-image range, with higher-cost Pro/vector variants.

Do not optimize model pennies before conversion.
Optimize:
**preview speed + aesthetic hit rate + order confidence.**
