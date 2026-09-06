# GameWinnerz Automated Fulfilment Architecture
**Date:** 2026-09-06 03:45 UTC
**Status:** CANONICAL — zero human-in-the-loop

---

## The rule

**customer pays → assets generated → print file rendered → supplier API receives order → supplier manufactures → supplier ships to recipient → tracking comes back automatically.**

No Canva. No uploading orders. No packing. No post office. No touching anything.

---

## Product catalog

| Tier | Physical item | Price | Prodigi cost |
|------|---------------|-------|--------------|
| Digital | reveal + digital card | £7–12 | £0 |
| Reveal | 4×6 premium postcard + QR | £14–20 | ~£0.40 |
| Gift | folded card + envelope + reveal | £18–25 | ~£0.75 |
| Legend | 1" acrylic collectible + reveal | £39–59 | ~£7 |

Same GiftBrief. Same video. Same card design. Only ProductRenderer changes.

---

## The pipeline

```
Payment
   ↓
GiftBrief validation
   ↓
image generation
   ↓
automated visual QA
   ↓
card template render
   ↓
QR validation
   ↓
print dimensions validation
   ↓
address validation
   ↓
supplier quote
   ↓
supplier submit
   ↓
production
   ↓
tracking webhook
   ↓
customer notifications
```

Failure = retry generation → alternate model → alternate provider → refund if impossible.

---

## Template system

We create deterministic templates:

```
gamewinnerz/
  football/
    legend-v1.svg
    captain-v1.svg
    icon-v1.svg
    gamewinner-v1.svg
  rugby/
  cricket/
  golf/
  basketball/
```

Variables:

```json
{
  "name": "DAVE",
  "number": "60",
  "rating": "99",
  "position": "ST",
  "title": "THE GAME WINNER",
  "stat1": "LOYALTY 99",
  "stat2": "BANTER 97",
  "stat3": "DAD JOKES 100",
  "portrait": "...",
  "qr": "https://gamewinnerz.com/r/abc123"
}
```

Our renderer produces the exact final 300dpi file.

---

## Supplier abstraction

```ts
interface FulfilmentProvider {
  quote(order): Promise<Quote>
  validate(order): Promise<Validation>
  submit(order): Promise<SupplierOrder>
  status(id): Promise<OrderStatus>
  cancel?(id): Promise<void>
}
```

Then: ProdigiProvider, GelatoProvider, MPCProvider, FutureLocalPrinterProvider.

Our business isn't built *on* Prodigi. Prodigi is merely `fulfilment_provider = prodigi`.

---

## Phase 0 — now

**Prodigi.**

- Reveal Card: 4×6, 350gsm glossy, ~£0.40
- Legend Block: 4×6 × 1" acrylic, ~£7
- Both fully automated through one API

## Phase 1 — getting orders

**MakePlayingCards** for real 2.5×3.5 holographic cards + foil packets + DTC fulfilment.

Require programmatic order feed agreement. No private API = no deal.

## Phase 2 — volume

Negotiate dedicated GameWinnerz SKU with Prodigi/MPC:
- unit cost, foil, packaging, shipping, SLA, branding, API, tracking

---

## Key Prodigi products

| Product | Cost | Production | Use |
|---------|------|------------|-----|
| Classic postcard 4×6 | £0.40 | 24h | Reveal Card |
| Fine-art greeting card | £0.75 | 24–72h | Gift Card |
| Acrylic prism 4×6 | £7 | 72h | Legend Block |
| Magic heat-reveal mug | £9 | 72h | Magic Pack |
| Metallic foil print | £2.57 | 72h | Hall of Fame |
| Glow-in-dark print | £2.57 | 72h | Little Legend |

---

## The canonical end-state

```
                    GAMEWINNERZ
                         │
                  PRODUCT ENGINE
                         │
       ┌─────────────────┼──────────────────┐
       │                 │                  │
       ▼                 ▼                  ▼
    DIGITAL          REVEAL CARD        LEGEND
      £9                £19               £49
       │                 │                  │
       │              Prodigi           Prodigi
       │             initially          acrylic
       │                 │                  │
       │                 ▼                  │
       │          MPC/custom SKU            │
       │            at volume               │
       │                 │                  │
       └─────────────────┴──────────────────┘
                         │
                         ▼
                RECIPIENT REVEAL
```

We own: design system, personalization engine, QR/reveal layer, StorySpec, customer relationship.

The printer is replaceable infrastructure.

---

## References

- Prodigi Print API: https://www.prodigi.com/print-api/docs/reference/
- Prodigi Postcards: https://www.prodigi.com/products/cards-and-stationery/postcards/classic-postcards/
- Prodigi Fine Art Cards: https://www.prodigi.com/products/cards-and-stationery/greetings-cards/fine-art-greetings-cards/
- Prodigi Acrylic: https://www.prodigi.com/products/home-and-living/tabletops/acrylic-prism/
- Prodigi Enterprise: https://www.prodigi.com/enterprise-sales/
- Prodigi Branded Inserts: https://www.prodigi.com/branded-packaging-inserts/
- MakePlayingCards: https://www.makeplayingcards.com/design/custom-trading-game-cards.html
- MPC Fulfilment: https://www.makeplayingcards.com/mpc-fulfillment-services.aspx
- Gelato: https://www.gelato.com/products
