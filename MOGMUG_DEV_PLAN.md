# MogMug → Pogtown: Implementation Brief (canonical dev plan)

Source: consolidated brief 2026-09-11. Repo: StallSpy (`/stallspy`). Worlds: `~/pogtown`, `~/freaktown`, `~/mogmug` docs.

## 0. Product thesis

Not a generic gift site or bee shop. **MogMug: pay to bring your pet to life.** Customer buys via Etsy/MogMug; fulfillment creates a persistent digital identity that can do videos, costumes, stand-up, voice, puppeting, AR, portal triggers, games, friend interactions, eventually Pogtown. Do NOT build full virtual world now — minimal reusable identity + commerce primitives.

## 1. Conversion language — no "Buy"

Avoid "Buy" and "mint" (crypto). Hierarchy:

```text
CREATE = generate the Pog / concept
BRING TO LIFE = commit to finished paid version
SUMMON = open it in AR
SEND = share/gift
MAKE PHYSICAL = card/mug/poster/ornament
```

Example: "Bring Royal Buster to life — £12" → "Royal Buster is alive." → "Give Buster a physical portal? [Card][Mug][Poster]". Flow: ramble → design → preview → BRING TO LIFE → Pog exists → optionally GIVE IT A PORTAL. Physical = bind Pog to object ("Scan it anytime to summon him").

## 2. Brand architecture

- `mogmug.com`: shop/creation funnel (Etsy landings, onboarding, products, videos, AR, share, management). Tagline: "Bring your pet to life."
- `pog.town`: persistent identity/world (`pog.town/buster`, `pog://character/<uuid>`). Never expose complexity at checkout.
- StallSpy/StallShark: business operating system.
- MythicBee: first archived theme pack (`themes/mythicbee/`), NOT deleted. Refactor: bartholomew-kit→character-kit, bee-session→character-session, hive-activity→world-activity, honey→credits/rewards (Treats, no crypto), tts-worker→character-voice, site→mogmug-site. Bartholomew becomes early NPC.

## 3. Character cast + loading engine

Replace one bee mascot with cast (Buster, Bartholomew, Kevin, Pickles, Mog…). Generic data-driven loading-copy engine:

```ts
type LoadingPhrase = { text: string; themes?: string[]; seasons?: string[]; characters?: string[]; weight?: number }
```

Seasonal packs (Christmas/Halloween). Eventually `generate_loading_pack(character)` from identity (e.g. "Hiding from Dave next door…").

## 4. Canonical Character schema

Cheap creation: references + identity + 1 portrait. Expensive assets later. Fields: id/slug/ownerId/origin(source/order/listing/referral)/identity(name/species/breed/traits/likes/dislikes/enemies/habits/nicknames/jokes/story)/references(primary+images)/assets(portrait/transparent/GLB/USDZ/voice/animations)/state(outfit/mood/level/xp)/permissions(public/remixable/messages)/timestamps. See full type in brief.

## 5. Etsy personalization (typed, with file upload)

Up to 5 questions, 1 upload field ≤10 files (JPG/PNG/HEIC/SVG/PDF ≤100MB). Refs: personalization migration guide, Etsy personalization help.
- F1 required upload "Photos of your pet": 4 ideal (face/front, full body, side, favourite), accept 6–8, minimum 1 excellent still works. Grade A(4+)/B(2–3)/C(1)/REJECT. Don't block sale.
- F2 required text: pet name.
- F3 optional text: "what makes them THEM" (identity conditioning).
- F4 optional dropdown: adventure (Surprise/Wizard/Royal/Astronaut/Pirate/Superhero-original/Movie-star/Christmas/Birthday, no copyrighted universes).
- F5 optional: recipient/message OR personality (Sweet/Chaotic/Serious/Dramatic/Tiny menace/Surprise).

## 6. MogMug onboarding + photo pipeline + asset layers

Etsy fulfills item; `mogmug.com/create/<signed-order-token>` builds identity (no account before fun). 30-sec ramble interview → extraction into Character.identity. Photo validator (detect/count/face/body/occlusion/blur/lighting/resolution/duplicates/angle) auto-selects primary_face/full_body/side/style; UX "These are perfect" vs "one more photo". Layers: L0 free identity, L1 paid product asset, L2 character pack (transparent/turnaround/GLB), L3 interactive (anim/voice/persona/AR).

## 7. Products, Prodigi, portals, triggers, pages, sharing, free tier

One pipeline, ProductRecipe config (inputs/steps/physical+prodigi SKU/credits/unlocks). Catalogue: video x3, talking message, card, AR card, mug, AR mug, ornament, character pack. Prodigi: JPG/PNG/PDF via URL at exact SKU pixel dims, prefer exact templates over fillPrintArea. Rule: object→trigger_id→character→experience resolver (`mogmug.com/x/<short-id>`), never ephemeral URLs; mug printed today can behave differently at Christmas. MVP trigger = QR → great mobile page; later markers/NFC/WebXR. Character page `mogmug.com/p/<slug>`: hero + MAKE/PERFORM/TALK/PLAY/SHARE. Every output gets `mogmug.com/v/<id>` with "Make yours" (camera→photo→free Character), track source_character/share/owner/recipient. Free: identity+thumbnail. Paid: videos/premium/rig/GLB/voice/AR/physical/longer. Principle: identity = growth, actions = monetization.

## 8. Milestones + guardrails + metrics

M1: Etsy order → Character → video → share page → friend MAKE YOURS. M2: physical mug/card via Prodigi + QR resolver scan. M3: "Buster in your room" simplest reliable web path. M4: Perform (record → character performs → share → recipient creates). DON'T build: blockchain/$POG, MMO, marketplace, hunger sim, native apps, perfect 3D, 10 games, multiplayer, NFTs, social graph — honor "no generalized systems before 20 paid orders/30d". Metrics: full funnel etsy_view→…→second_purchase/trigger_scan; CHARACTER VIRAL COEFFICIENT + revenue/character. Design principle: customer thinks "£7 to make Buster hilarious", we think "paid Pogtown identity onboarded" — never expose second at expense of first.
