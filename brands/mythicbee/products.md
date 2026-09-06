# MythicBee — Strategic Architecture v3
**Date:** 2026-09-06 02:28 UTC
**Status:** CANONICAL — build from this

---

## Core Thesis (refined)

> **Talk about someone you love for five minutes. MythicBee figures out what would delight them, creates it, and routes it to the fastest physical form that can actually reach them in time.**

---

## The Architecture (frozen)

```
                  HUMAN RAMBLE
                       │
                       ▼
                    GiftBrief
                       │
                       ▼
               GIFT INTELLIGENCE
          "what would actually delight them?"
                       │
                       ▼
              ExperienceManifest
                       │
        ┌──────────────┼───────────────┐
        ▼              ▼               ▼
      WORLD          MEDIA          PHYSICAL
   Atlas/Marble     image/video      Prodigi
   /next model       voice           Express
        │              │               │
        └──────────────┼───────────────┘
                       ▼
              PERSISTENT PORTAL
             mythicbee.com/r/...
                       │
       phone today / glasses tomorrow /
          holographic frame later
```

---

## World Generation = Replaceable Backend

Not MythicBee R&D. Use whatever is best this month:
- World Labs Atlas (text/image/video/3D → world)
- Marble World API (splats, colliders, panoramas)
- Genie 3 (navigable 720p worlds at 20-24fps)
- GPT-6 Astra (world/game author in Unity/Godot)

---

## The 20 Product Families

| #  | Family | Best Physical | Digital/Spatial |
|----|--------|---------------|-----------------|
| 1  | Dogcasso | fine-art/foil print, card, acrylic, mug | pet paints portrait; AR pet |
| 2  | GameWinners | foil sports card/poster, acrylic | stadium entrance/world |
| 3  | Legendary Card | specialist holo collectible | summoned person/pet creature |
| 4  | CoverStar | personalized magazine/print | animated cover / interview |
| 5  | Hall of Fame | foil certificate/poster/acrylic | awards ceremony world |
| 6  | MovieStar | movie poster/card | generated trailer/world |
| 7  | The Legend of Dad | hardcover/softcover book | documentary / memory world |
| 8  | Breaking News | card/magazine/newspaper | personalized broadcast |
| 9  | Birthday Roast | card/magazine | comedian/news-show reveal |
| 10 | Dogumentary | book/card | pet documentary |
| 11 | First Edition | book | childhood/nostalgia storyworld |
| 12 | Little Legend | glow poster/storybook | child enters fantasy world |
| 13 | Our Story | photo book/acrylic | couple/family memory world |
| 14 | VowFrame | foil print/acrylic | vows animate in spatial scene |
| 15 | Remembered | fine-art print/book/acrylic | sensitive memorial world |
| 16 | Christmas Story | glow print/book/card | Santa/fantasy storyworld |
| 17 | Personalized Comic | magazine/softcover | animated/comic world |
| 18 | Recipe Legacy | book/notebook | voice/audio family recipes |
| 19 | Private Puzzle | jigsaw/crossword booklet | clues reveal memories |
| 20 | Star Map | foil or glow print | reconstructed night-sky world |

---

## Physical Vessels (collapsed)

```text
CARD           → greeting cards, collectibles
PRINT          → posters, foil, glow, art
ACRYLIC        → premium desk/mantelpiece
BOOK/MAGAZINE  → stories, biographies, comics
MUG            → Dogcasso, comedy
PUZZLE         → jigsaws, crosswords
SPECIALIST     → holo trading cards, custom hardware
```

Twenty creative families → seven manufacturing pipelines.

---

## Prodigi as Canonical Supplier

| Product | Wholesale | Production | Use |
|---------|-----------|------------|-----|
| Fine-art greeting card | £0.75 | 24-72h | Default occasion gift |
| Classic glossy card | £1.10 | 24h | Fast UK card |
| Art print | £2.57 | 24-72h | Portraits/posters |
| Gold/silver foil print | £2.57 | 72h | GameWinners, awards, vows |
| Glow-in-dark print | £2.57 | 72h | Kids, fantasy, stars, Christmas |
| Magazine | £3.75 | 96-144h | Birthday newspaper |
| Mug | £3.64 | 48-72h | Dogcasso / comedy |
| Softcover book | £6.50 | 96h | Stories/comics/yearbooks |
| 1-inch acrylic prism | £7 | 72h | Premium desk gift |
| Framed foil print | £21 | 72h | Premium upgrade |

---

## Same-Day Delivery

```text
MYTHICBEE STANDARD
Prodigi
global
premium formats
1-5 days

MYTHICBEE EXPRESS
local retail printing (Walgreens/Boots)
+ last-mile courier (Uber Direct)
hours
limited formats (card, print, poster)
```

---

## The UX: Ramble → Perfect Gift

1. **Ramble.** Speech-to-speech Bartholomew. Photos dropped in.
2. **Structure silently.** Extract GiftBrief.
3. **Find giftable hooks.** Not keywords — insights.
4. **Generate three pitches.** Genuinely different concepts.
5. **Select vessel based on person + deadline.**
6. **Show idea before design.** Cover/mockup + 5-10s teaser.
7. **Compile ExperienceManifest.**
8. **Render against Prodigi template.**
9. **Quote fulfilment before checkout.**
10. **Digital gift available immediately.** Physical starts async.

> **The customer contributes memories, not design labor.**

---

## "Late Gift Panic" as Product

```
birthday gift for dad today
        ↓
Forgot? Good. Tell us about them.
        ↓
RAMBLE 5 MINUTES
        ↓
PERFECT CONCEPT
        ↓
DIGITAL GIFT READY IN 10 MINUTES
        ↓
choose:
INSTANT DIGITAL
SAME-DAY LOCAL
NEXT-DAY PREMIUM
```

Deadline is a first-class input to the recommendation agent.

---

## Holographic Future (design for, don't manufacture)

| Hardware | Cost | Relevance |
|----------|------|-----------|
| Looking Glass Go | $99 | Development/premium experiment |
| Looking Glass musubi | $149 | Consumer MythicFrame candidate |
| Spinning LED fans | $47-65 | Retail signage, not gifts |

Design content pipeline for holographic output now. Don't manufacture hardware now.

---

## The Moat

Not the world model. Not a printing factory. Not an AR engine.

**Gift Intelligence:** the structured understanding of the loved person + the creative interpretation + the persistent world attached to their object.

Everything beneath that is swappable infrastructure.

---

## 30-Day Priority

1. Build Gift Intelligence layer (ramble → insights → recommendations)
2. Wire Prodigi API for real orders
3. Complete one end-to-end GameWinners order
4. Build recipient reveal page with AR activation
5. Order Prodigi samples (foil, glow, acrylic, mug)
6. Prototype holo collectible with Looking Glass
