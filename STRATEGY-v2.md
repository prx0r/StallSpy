# MythicBee — Strategic Architecture v2
**Date:** 2026-09-06 02:12 UTC
**Status:** CANONICAL — build from this

---

## Company Thesis (frozen)

> **MythicBee turns people, pets and memories into interactive worlds, delivered through beautiful physical gifts.**

The experience is the product. The card, poster, book, mug or collectible is its physical form.

---

## The Production System

```text
Human conversation
       ↓
GiftBrief
       ↓
ExperienceManifest
       ↓
creative assets
       ↓
┌───────────────┬────────────────┬────────────────┐
│ PHYSICAL      │ DIGITAL        │ SPATIAL        │
│ card          │ reveal page    │ 3D             │
│ holo card     │ video          │ room AR        │
│ poster        │ audio          │ target AR      │
│ book          │ mini-game      │ glasses later  │
│ acrylic       │ share link     │ hologram later │
└───────────────┴────────────────┴────────────────┘
```

---

## three.ws vs 8th Wall (complementary)

|                           | three.ws                     | 8th Wall                                 |
| ------------------------- | ---------------------------- | ---------------------------------------- |
| Core strength             | 3D objects/characters/agents | Computer-vision AR                       |
| Custom GLB                | Excellent                    | Can render one, but not its main purpose |
| 3D website mascot         | Excellent                    | Overkill                                 |
| Printed-card recognition  | Not its focus                | **Excellent**                            |
| Mug/packaging recognition | Not its focus                | **Yes**                                  |
| MythicBee role            | **Embodiment layer**         | **Portal/tracking layer**                |

---

## The Recipient Flow

```text
             QR
              │
              ▼
        Mythic Reveal
              │
   ┌──────────┼───────────┐
   │          │           │
 WATCH      PLAY       BRING ALIVE
 video    mini-scene        │
                             ▼
                   determine portal type
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
         CARD              MUG             ROOM
           │                 │                 │
      image target     cylinder target      surface
           │                 │                 │
           └────────── 8th Wall ──────┐   three.ws
                                       │
                                  interactive 3D
```

QR is the permanent addressing layer for the gift. Browsers change, QR stays.

---

## Physical Product Catalog (5 vessels)

| Vessel                 | Why                                            | Prodigi Price |
| ---------------------- | ---------------------------------------------- | ------------- |
| **Classic Card**       | Cheapest entry, occasions, QR, enormous market | ~£1.10        |
| **Mythic Collectible** | Holo card; best viral/AR object                | QPMN/MPC test |
| **Living Print**       | Foil/glow poster; premium wall gift            | ~£2.57        |
| **Mythic Block**       | Acrylic; premium mantel/desk gift              | ~£7           |
| **Legend Book**        | Documentary/story products                     | ~£6.50        |

Creative themes sit on top:
- GameWinners: card → holo collectible → print → acrylic
- Dogcasso: card → print → acrylic → mug
- Legendary Creature: card → holo collectible → poster
- The Legend of Dad: card → book → print

---

## Supplier Stack

| Need                   | UK                   | US                      | Role         |
| ---------------------- | -------------------- | ----------------------- | ------------ |
| Standard greeting card | **Prodigi**          | **Gelato/Prodigi test** | Core         |
| Posters/foil/glow      | **Prodigi**          | **Prodigi**             | Core         |
| Acrylic blocks         | **Prodigi**          | **Prodigi**             | Core premium |
| Photo books            | **Prodigi**          | **Prodigi**             | Core premium |
| Mugs                   | **Prodigi**          | **Prodigi**             | Secondary    |
| Holo trading cards     | QPMN/MPC test        | QPMN/MPC test           | Hero SKU     |
| Generic accessories    | Alibaba after volume | Alibaba after volume    | Later        |
| AliExpress             | Samples only         | Samples only            | Discovery    |

**Order same 6 test products to UK + US address before launch.**

---

## Product Rule: AR must enhance, never rescue

```text
LEVEL 0  beautiful physical gift
LEVEL 1  QR → instant personalized reveal
LEVEL 2  interactive browser experience
LEVEL 3  AR tied to object
LEVEL 4  room-scale spatial experience
LEVEL 5  glasses / holographic display
```

Every level is additive. Object must be good enough for the mantelpiece without scanning.

---

## Bartholomew: Both Sides

**Buyer side:** "Who are we making mythical?"
**Recipient side:** "Ah. You must be Peter. I have been expecting you."

Bartholomew is a narrative protocol. He introduces GameWinners, opens the Dogcasso studio, summons a creature, narrates the documentary, instructs someone to point their phone at the card.

---

## Experience Format (portable)

```json
{
  "portalId": "mb_7KQ2F9",
  "physical": {
    "type": "trading_card",
    "widthMm": 63,
    "heightMm": 88
  },
  "target": {
    "type": "image",
    "asset": "/targets/mb_7KQ2F9.webp"
  },
  "scene": {
    "model": "/models/dad-legend.glb",
    "animation": "summon",
    "audio": "/audio/commentary.mp3"
  },
  "surfaces": {
    "web": true,
    "video": true,
    "imageTargetAR": true,
    "roomAR": true,
    "smartGlasses": false,
    "lightField": false
  }
}
```

Never save `eightWallProject: "abc123"`. Save portable formats with adapters.

---

## Future Hardware

- **Looking Glass Go:** $99 light-field display, web workflows, WebXR library
- **Looking Glass musubi:** $149 consumer holographic photo/video frame
- **Meta Ray-Ban Display:** visual display, Web Apps on glasses
- **Snap SPECS:** consumer spatial AR glasses, September 2026
- **Android XR:** audio glasses fall 2026, display glasses following

The smartphone QR/AR version is the first interface to a spatial asset that survives the hardware transition.

---

## 30-Day Action Plan

1. Complete one GameWinners order: conversation → GiftBrief → ExperienceManifest → print PDF → QR → Prodigi/Gelato → recipient page
2. Build beautiful non-AR recipient reveal (commentary, animation, confetti, share/download)
3. Prototype premium holo collectible (order from QPMN, MPC, UK specialist)
4. Build one 8th Wall experiment (GameWinners card as image target)
5. Put three.ws Bartholomew GLB into recipient experience
6. Order weird Prodigi substrates (foil, glow, acrylic, mug)
7. Keep platform formats portable (GLB/glTF, USDZ, MP4, ExperienceManifest)

---

## Key Quotes

> "MythicBee should own the world attached to the object, not the printing technology and not the AR vendor."

> "A £1 card can contain a character. A mug can contain a scene. A poster can contain a world. A book can contain memories that move and speak."

> "The perceived value is almost completely decoupled from manufacturing cost."
