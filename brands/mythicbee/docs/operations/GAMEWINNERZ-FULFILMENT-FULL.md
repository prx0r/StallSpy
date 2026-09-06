# GameWinnerz Automated Fulfilment — Full Spec
**Date:** 2026-09-06 03:50 UTC
**Status:** CANONICAL

---

Yes. **We should remove every manual-fulfilment assumption from GameWinnerz.** Your location does not matter. The canonical system should be:

**customer pays → assets generated → print file rendered → supplier API receives order → supplier manufactures → supplier ships to recipient → tracking comes back automatically.**

Prodigi can already do essentially all of that.

### What Prodigi can do now

Prodigi's Print API is explicitly designed for recurring automated flows with **no manual intervention**. A live API order is validated, charged and routed into production automatically; artwork is supplied by a public URL, and the API exposes order/shipment status. ([Prodigi][1])

It's also fully white-label: Prodigi says neither it nor its production partners appear on the product or ordinary packaging. ([Prodigi][2])

So our architecture becomes:

```text
CUSTOMER
   │
   ▼
GameWinnerz conversation
   │
   ▼
GiftBrief
   │
   ├──► video/reveal generation
   │
   └──► physical ProductSpec
              │
              ▼
        deterministic SVG
        card renderer
              │
              ▼
      300dpi JPG/PDF + QR
              │
              ▼
        object storage URL
              │
              ▼
       PRODIGI PRINT API
              │
              ▼
      manufacture / pack
              │
              ▼
          CUSTOMER
```

No Canva. No uploading orders. No packing. No post office. No touching anything.

---

# The particularly good discovery: GameWinnerz can have 3 physical tiers immediately

## 1. GameWinnerz Reveal Card — cheapest

Prodigi's **4×6 classic postcard** is unusually good for this.

It's:

* 350gsm card
* gloss laminated on both sides
* 4×6"
* ~24-hour production
* API enabled
* ships worldwide
* explicitly designed to be sent directly to the recipient
* **from £0.40 before shipping**

([Prodigi][3])

Don't think of it as a postcard.

We design it like this:

```text
╭──────────────────────────╮
│                          │
│          99              │
│                          │
│        DAVE              │
│                          │
│     [HERO IMAGE]         │
│                          │
│     GAMEWINNERZ          │
│       LEGEND             │
│                          │
╰──────────────────────────╯
```

Back:

```text
HE THOUGHT HIS PLAYING DAYS
WERE OVER.

THEY WEREN'T.

[ QR ]

SCAN TO WITNESS THE MOMENT
```

The customer perceives it as a **large premium collectible**, not a postcard.

At £0.40 manufacturing cost, the economics are absurdly forgiving.

---

# 2. GameWinnerz Gift Card — better presentation

Prodigi's fine-art greeting cards are probably even better for gifting.

They start around **£0.75**, can be personalized inside and outside, and the Mail4Me option puts the finished personalized card into a kraft envelope and sends it **directly to the recipient**. Production is roughly 24–72 hours. ([Prodigi][4])

Important distinction:

**Mail4Me production is currently UK-based, but it ships worldwide.**

That doesn't mean *you* need to be in the UK. You're just calling an API.

This might actually be our canonical entry product:

```text
envelope
   ↓
beautiful GameWinnerz cover
   ↓
"Dave Prior
THE 60TH SEASON"
   ↓
open
   ↓
hero image + personalized message
   ↓
"There's one more thing."
   ↓
QR
   ↓
cinematic reveal
```

That is much more obviously a birthday/Father's Day/Christmas **gift** than a naked sports card.

---

# 3. GameWinnerz Legend — this is excellent

Prodigi has a **4×6 acrylic prism**.

This is a one-inch-thick freestanding acrylic photo block with diamond-polished edges. It starts around **£7**, is fulfilled in UK/EU/US facilities, ships worldwide and is available through the API. ([Prodigi][5])

This thing maps extremely well onto our concept.

Imagine:

```text
     ╭─────────────╮
     │             │
     │     99      │
     │             │
     │    DAVE     │
     │   [IMAGE]   │
     │             │
     │   LEGEND    │
     │             │
     ╰─────────────╯
         █████
         █████  ← 1" thick acrylic
```

It becomes a **little trophy**.

Retail:

**£39–59**

Production:

~£7 + shipping + our generated media.

That is far stronger than a £3 Etsy JPEG.

---

# So I would make the catalog

| Tier       | Physical item                                | Likely positioning |
| ---------- | -------------------------------------------- | ------------------ |
| Digital    | reveal + digital card                        | £7–12              |
| **Reveal** | 4×6 premium card/postcard + QR               | £14–20             |
| **Gift**   | folded personalized card + envelope + reveal | £18–25             |
| **Legend** | 1" acrylic collectible + reveal              | £39–59             |

Same underlying `GiftBrief`.

Same video.

Same card design.

Only:

```text
ProductRenderer
```

changes.

That is exactly how MythicBee/GameWinnerz should work.

---

# And yes: WE create the templates

We don't need Prodigi to support personalization logic.

This is important.

Prodigi doesn't need to know that Dave is 60, supports Arsenal, likes Thierry Henry and is being portrayed scoring a bicycle kick.

Our application handles all of that.

We make deterministic templates like:

```text
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

And variables:

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

Our renderer produces the **exact final 300dpi file**.

Prodigi's API simply gets:

```text
SKU
recipient address
copies = 1
print-ready artwork URL
```

Prodigi explicitly supports remotely hosted print-ready asset URLs in its order schema. ([Prodigi][6])

This means the physical personalization engine is completely supplier-neutral.

---

# The supplier abstraction is important

I'd build:

```ts
interface FulfilmentProvider {
  quote(order): Promise<Quote>
  validate(order): Promise<Validation>
  submit(order): Promise<SupplierOrder>
  status(id): Promise<OrderStatus>
  cancel?(id): Promise<void>
}
```

Then:

```text
ProdigiProvider
GelatoProvider
MPCProvider
FutureLocalPrinterProvider
```

Our business isn't built *on Prodigi*.

Prodigi is merely:

> `fulfilment_provider = prodigi`

---

# Gelato should be our backup rather than primary

Gelato has an even larger local-production footprint: it currently advertises **250+ production partners across 32 countries**, supports cards, an API, ecommerce integrations and automated routing to a nearby production facility. ([Gelato][7])

That's useful.

Especially if we eventually sell heavily into:

```text
US
Canada
Australia
Europe
Asia
```

we can dynamically select:

```text
UK recipient
    → Prodigi

Germany
    → whichever quotes faster/cheaper

US
    → Gelato / Prodigi local SKU

Australia
    → Gelato / Prodigi

unsupported
    → fallback
```

Eventually our checkout could calculate this invisibly.

---

# But I found a MUCH more interesting specialist partner

## MakePlayingCards

This is basically the manufacturing partner we'd want once we insist upon a **real collectible trading card**.

They already manufacture standard:

**2.5 × 3.5-inch trading cards.**

They specifically advertise **custom football cards**. ([MakePlayingCards][8])

And they can do:

* 300gsm+ stocks
* black-core card
* linen
* plastic
* holographic foil
* gold foil
* silver foil
* embossing
* debossing
* spot effects
* custom boxes
* **custom foil booster packs**

([MakePlayingCards][9])

Look at how good that is for GameWinnerz.

Instead of receiving an envelope:

```text
┌─────────────────┐
│  GAMEWINNERZ    │
│                 │
│  LEGEND SERIES  │
│                 │
│   DAVE PRIOR    │
│                 │
│  ★ ONE OF ONE ★ │
└─────────────────┘
```

**sealed foil booster pack**

Recipient tears it open.

Inside:

```text
holographic personalized
GameWinnerz card
```

Back:

```text
SCAN TO REVEAL
[QR]
```

That is an actual product.

Not a greeting card pretending to be a collectible.

---

# MPC will even fulfil internationally for you

Their fulfillment service explicitly says:

* no setup cost
* no MOQ
* worldwide shipment
* manufacturing
* packaging
* labeling
* tracking/recorded delivery
* **from $1 extra per parcel dispatch**, plus normal shipping

([MakePlayingCards][10])

They also say their fulfillment center can ship orders directly from their factory to end recipients. ([MakePlayingCards][11])

### BUT.

I cannot find a documented public ordering API comparable to Prodigi.

That is the problem.

Their existing workflow appears much more builder/checkout/fulfillment oriented. ([MakePlayingCards][12])

So I would **not** build V0 against MPC.

Because you specifically don't want:

```text
order comes in
→ Tom logs in
→ uploads Dave.png
→ changes address
→ submits order
```

Absolutely not.

---

# However, MPC is exactly who I'd approach for our first supplier agreement

Not:

> "Hi, can you print some cards?"

Instead:

> **We're building a personalized gifting platform generating unique sports trading cards per customer. We require automated one-unit manufacturing and direct-to-consumer fulfillment. Every order has unique front/back print files and recipient data. We expect to begin at low volume but need an integration capable of scaling. We require either REST API, SFTP/structured order feed, or another fully programmatic submission mechanism.**

Then specify:

```text
63.5 × 89mm
rounded corners
350gsm+ premium stock
front unique
back unique
holographic finish
1 card / order
custom GameWinnerz foil sleeve
direct recipient shipping
neutral or GameWinnerz branding
tracking callbacks
no invoice showing manufacturing cost
```

That is a genuine manufacturing specification.

MPC has been manufacturing cards for 40+ years and explicitly invites customers with custom requirements to contact them. ([MakePlayingCards][11])

---

# Prodigi may eventually custom-build the SKU too

This was another interesting finding.

Prodigi Enterprise explicitly supports bespoke pricing and custom personalization programs, including things like:

* branded boxes/tubes
* branded tape
* branded tissue
* external stickers
* hand numbering
* certificates of authenticity
* specialist substrates
* special visual effects

subject to volume. ([Prodigi][13])

Prodigi also offers custom-branded packaging at Enterprise level. ([Prodigi][2])

So once GameWinnerz proves demand, I'd ask them:

> Can you add a custom 63.5 × 89mm GameWinnerz collectible SKU to our account?

Something like:

```text
GAMEWINNERZ-HOLO-63X89

350gsm black-core
rounded
full-colour front/back
holo laminate
branded protective sleeve
optional foil packet
single-unit POD
UK/EU/US production where available
```

I **cannot say that Prodigi will agree to that exact SKU**—their public pages don't promise bespoke card formats—but their enterprise operation explicitly supports specialist substrates/special effects/custom personalization, so it is a credible conversation once there's volume. ([Prodigi][13])

---

# There's also a very clever Prodigi packaging hack

They support branded inserts:

* A6 postcards
* flyers
* stickers
* packing slips

and the API can specify print-ready URLs for those inserts too. ([Prodigi][14])

So imagine the acrylic premium order:

```text
BOX

   GameWinnerz sticker
          ↓

   acrylic GAMEWINNERZ trophy
          +

   small personalized card:

   "THE MATCH ISN'T OVER."

        [QR]

   "SCAN TO CONTINUE"
```

Everything generated specifically for that recipient.

Still completely automatic.

---

# I would now make this a hard architectural rule

## Absolutely zero human-in-the-loop fulfillment.

Even artwork QA should ultimately be automated.

```text
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

Failure doesn't mean:

> email Tom.

It means:

```text
retry generation
→ alternate model
→ alternate fulfillment provider
→ refund automatically if impossible
```

There can obviously be an admin dashboard for exceptional failures, but the product should be designed assuming **nobody operates it**.

---

# Therefore I'd change our plan slightly

### Phase 0 — immediately

Use Prodigi.

**Hero product:**

**GameWinnerz Reveal Card**

4×6, 350gsm glossy physical collectible, permanent QR → cinematic reveal.

Supplier cost begins around £0.40 + delivery. ([Prodigi][3])

### Premium:

**GameWinnerz Legend Block**

4×6 × 1-inch acrylic trophy.

Supplier cost begins around £7 + delivery. ([Prodigi][5])

Both fully automated through one API.

---

### Phase 1 — when we're getting orders

Talk to:

**MakePlayingCards**

for:

**real 2.5×3.5 holographic single-card + GameWinnerz foil packet + DTC fulfillment.**

They already manufacture exactly this class of collectible and already run international fulfillment. ([MakePlayingCards][15])

But require a **programmatic order feed agreement** before we integrate them.

No private API = no deal.

---

### Phase 2 — volume

Take our real numbers to Prodigi/MPC/other manufacturers:

> 1,500 personalized cards/month.
> Every card unique.
> Here are our exact files.
> Here are our destination percentages.
> Here is our acceptable SLA.
> Quote us a dedicated GameWinnerz SKU.

Now we negotiate:

```text
unit cost
foil
packaging
shipping
reprints
SLA
branding
API
tracking
```

That's when we stop buying a generic POD product and essentially have **our own virtual factory SKU**.

---

## The canonical end-state is therefore

```text
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

And importantly:

**we own the design system, personalization engine, QR/reveal layer, StorySpec and customer relationship.**

The printer is replaceable infrastructure.

That is exactly the way I'd build this given your requirement: **you should be able to run GameWinnerz from Cambodia, India, Thailand or anywhere else without ever seeing or touching a product.**

[1]: https://www.prodigi.com/faq/print-api/?utm_source=chatgpt.com "Print API | FAQ | Prodigi"
[2]: https://www.prodigi.com/faq/packaging/?utm_source=chatgpt.com "Packaging | FAQ | Prodigi"
[3]: https://www.prodigi.com/products/cards-and-stationery/postcards/classic-postcards/?utm_source=chatgpt.com "Print on Demand Classic Postcards - Print API, Dropshipping"
[4]: https://www.prodigi.com/products/cards-and-stationery/greetings-cards/fine-art-greetings-cards/?utm_source=chatgpt.com "Print on Demand Fine Art Greetings Cards - Print API, Dropshipping"
[5]: https://www.prodigi.com/products/home-and-living/tabletops/acrylic-prism/?utm_source=chatgpt.com "Print on Demand Acrylic Prism Prints - Print API, Dropshipping"
[6]: https://www.prodigi.com/print-api/docs/reference/?utm_source=chatgpt.com "Prodigi API Documentation"
[7]: https://www.gelato.com/products?utm_source=chatgpt.com "Print on Demand Products | Gelato"
[8]: https://www.makeplayingcards.com/design/custom-trading-game-cards.html?utm_source=chatgpt.com "Custom Trading Game Cards"
[9]: https://www.makeplayingcards.com/design/custom-square-corner-game-cards.html?utm_source=chatgpt.com "Custom Square Corner Game Cards"
[10]: https://www.makeplayingcards.com/mpc-fulfillment-services.aspx?utm_source=chatgpt.com "MPC Order Fulfillment Services"
[11]: https://www.makeplayingcards.com/faq-kickstarter.aspx?utm_source=chatgpt.com "Running Playing Cards Projects on Kickstarter"
[12]: https://www.makeplayingcards.com/faq-order.aspx?utm_source=chatgpt.com "FAQ on placing an online order - MakePlayingCards.com"
[13]: https://www.prodigi.com/enterprise-sales/?utm_source=chatgpt.com "Enterprise Sales | Prodigi"
[14]: https://www.prodigi.com/branded-packaging-inserts/?utm_source=chatgpt.com "Custom Packaging Inserts | Prodigi"
[15]: https://www.makeplayingcards.com/promotional/custom-booster-pack.html?utm_source=chatgpt.com "Custom Booster Packs for TCG Cards and Sports Cards"
