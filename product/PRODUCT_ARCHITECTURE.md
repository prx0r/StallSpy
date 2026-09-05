# MythicBee — Product Architecture

**As of:** 5 September 2026
**Brand:** MythicBee Studios — tiny movies starring your people.
**Tagline:** Make someone the main character.
**Positioning:** Video-native Moonpig. Pick joke → Add people → Receive something hilarious.

---

## The Business

We are not selling "AI videos." We are selling personalized versions of internet culture.

The customer uploads a photo. We turn them into the meme, the movie, the magic.

**MythicBee = the place where you turn someone into a gift.**

---

## 5 Core Engines

| Engine | Input | Output | Price Range |
|--------|-------|--------|-------------|
| **Character Talks To You** | name + age + facts + photo | Character speaks to camera | £4.99-£9.99 |
| **Something Was In Your Room** | room photo | Entity placed in their space | £4.99-£9.99 |
| **Put Me In The Movie** | face/body photo | Cinematic scenario with them | £4.99-£19.99 |
| **Meet [Name]** | 6 questions + 5-10 photos | 30-60s mini film | £19.99-£29.99 |
| **Trend Drop** | trend format + personal info | Quick comedic clip | £4.99 |

See `ENGINES.md` for engine matrix.
See `STORYBOARDS.md` for shot-by-shot blueprints.
See `H3_PROMPT_RULES.md` for prompting rules.
See `TEMPLATE_FORMAT.md` for YAML schema.

---

## Three Catalogue Layers

| Layer | Purpose | Refresh |
|-------|---------|---------|
| **Classics** | Evergreen meme grammars | Permanent, improves with models |
| **Trending** | TikTok/internet formats | Weekly |
| **Occasions** | Santa, birthdays, weddings | Seasonal |

See `CATALOGUE.md` for full catalogue.

---

## Pricing

| Tier | Price | What it is |
|------|-------|------------|
| Magic Clip | £4.99 | 5-15 sec, 1 format, standard quality |
| Gift Pack | £9.99 | Video + custom song + e-card + both formats |
| Card Pack | £14.99 | Everything above + physical card + gift page |
| Movie Pack | £29.99 | 30-60 sec movie + song + card + page |
| Movie Card | £7.99 | Physical card + QR to movie |

**Early-bird schedule:** 21 days (40% off) → 14 days (25% off) → 7 days (normal) → 48hrs (+£4 rush)

See `PRICING.md` for full economics.

---

## Tech Stack

| Component | Choice | Cost |
|-----------|--------|------|
| Primary model | MiniMax H3 (quantized) | — |
| Secondary model | LTX-2.5 | — |
| Workflow | ComfyUI | — |
| Post-production | FFmpeg | — |
| GPU (cheap) | Vast.ai RTX 5090 | $0.40/hr |
| GPU (easy) | RunPod RTX 5090 | $0.99/hr |
| Physical cards | Prodigi API | ~£0.75-1.10/unit |
| Books (future) | Lulu Print API | TBD |

See `TECH_STACK.md` for full architecture.

---

## Fulfillment

- **Digital:** Gift page at mythicbee.com/[name]-[occasion]-[code]
- **Cards:** Prodigi prints + ships, QR inside links to movie
- **Books (future):** Lulu Print API
- **AR (future):** WebAR, card becomes tracking marker

See `FULFILLMENT.md` for full pipeline.

---

## Storefront

Browse-by-joke interface. Thumbnails show the joke, not the tech.

See `STOREFRONT_UX.md` for UX design.

---

## Chatbot-First Interface

Conversational UX: "Who is it for?" → 3 curated options → "Make this one."

60 seconds vs 20-45 minutes on traditional ecommerce.

See `CHATBOT_UX.md` for conversational flow.

---

## Partnerships & Affiliate Commerce

We own the personalization layer. Partners fulfil physical goods.

High-margin digital products subsidize physical/affiliate offering.

See `PARTNERSHIPS.md` for partner matrix and bundle architecture.

---

## Customer Strategy

Three buyer groups: parents (28-44), friend groups (18-34), couples/family (28-45).

Product test: Recognition (2 sec) + Projection (specific person) + Price irrelevance (£4.99 feels trivial).

Target AOV: £9-15 via upsells from £4.99 entry.

See `CUSTOMERS.md` for full customer strategy.

---

## Trend Monitoring

TikTok Creative Center + KnowYourMeme + Reddit + Google Trends + Etsy Marketplace Insights.

See `TREND_RADAR.md` for monitoring system.

---

## Retention Engine

**"Never forget a good gift again."**

Save recipient profiles with buyer consent: name, birthday, relationship, interests, pets, preferred tone, prior gifts.

Proactive reminders 21 days before occasions with pre-generated concepts.

Early-bird pricing rewards planning.

Gift CRM makes accounts more valuable over time.

Referral loop: recipients become buyers via gift pages.

See `RETENTION.md` for full system.

---

## File Index

| File | Contents |
|------|----------|
| `BRAND.md` | Brand proposition, positioning, voice |
| `ENGINES.md` | 8 core generation engines + matrix |
| `STORYBOARDS.md` | Shot-by-shot blueprints for all 8 engines |
| `H3_PROMPT_RULES.md` | 6 canonical prompting rules |
| `TEMPLATE_FORMAT.md` | YAML schema + prompt compiler + experiment logging |
| `CATALOGUE.md` | Product catalogue (Classics/Trending/Occasions) |
| `PRICING.md` | Tier structure, upsells, economics |
| `TECH_STACK.md` | Models, GPUs, workflow, cost per unit |
| `FULFILLMENT.md` | Digital delivery, physical cards, books, AR |
| `STOREFRONT_UX.md` | Browse-by-joke interface |
| `TREND_RADAR.md` | Trend monitoring system |
| `RETENTION.md` | Gift CRM, reminders, referral loop |
| `STRATEGY.md` | Moonpig thesis, competitive positioning, flywheel |
| `CHATBOT_UX.md` | Conversational interface design |
| `PARTNERSHIPS.md` | Affiliate commerce, bundle architecture |
| `CUSTOMERS.md` | Customer segments, ad channels, pricing psychology |
| `TEMPLATES.md` | Input contracts for each scene type |
| `PURCHASE_FLOW.md` | 9-step UX, upsells, product test rule |
| `GOLD_IDEAS.md` | All key strategic insights from founding conversation |
| `ADS.md` | Channel priority, creative rules, budget progression |
| `MEME_CATALOGUE.md` | 10 meme products ranked by difficulty + occasion matrix |
| `CONTENT_LANES.md` | 3 content lanes + 2 independent axes (scene × voice) |
| `MISIRECTION_SKITS.md` | 6 shot-by-shot tension/misdirection skits |
| `AD_TESTING.md` | Test slate, ad-testing loop, cost per test |
| `H3_REFERENCE_LINKS.md` | Official MiniMax + fal prompt guides |
| `CANONICAL_RESOURCE.md` | Etsy tooling landscape |
| `BUILD_BLUEPRINT.md` | Implementation tickets |
| `tool_registry.json` | Machine-readable tool registry |
