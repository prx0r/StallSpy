# MythicBee — Supplier Reference
**Date:** 2026-09-06
**Status:** CANONICAL — supplier architecture

---

Yes. I recovered the earlier MythicBee catalogue. Nineteen themes were explicitly named; **Children's Adventure** was the additional STORYWORLD product implied in the same spec, so I'm using that as #20 rather than inventing a new category.

The key supplier rule should now be:

> **MythicBee generates the complete print-ready artifact. The supplier is a dumb manufacturing API.**

We should not depend on a supplier's personalization UI. For every order we generate a unique PNG/PDF/SVG and send it with the recipient address. That gives us replaceable suppliers and completely automated fulfillment.

---

## Supplier universe

| Supplier | Zero-touch status | Strongest at | Customization | Main limitation |
|----------|-------------------|--------------|---------------|-----------------|
| **Prodigi** | ✅ Excellent public Print API | Cards, postcards, photo books, framed art, acrylic blocks, calendars, mugs, cushions, puzzles, stationery | Per-order artwork, front/back cards, inside/outside greeting cards, printable book spines, transparent-background acrylic prisms, inserts at supported facilities | No true trading-card/holo SKU today |
| **Gelato** | ✅ REST API + webhooks | Global/localized cards, posters, acrylic, photo books, calendars, mugs, apparel | Multi-page PDFs, separate print areas, nearby production in 32 countries | Less exotic collectible finishing |
| **Lulu** | ✅ Excellent Print API | **Dynamically personalized books**, comics, magazines, children's books, workbooks, calendars | Completely unique interior + cover PDF per customer; 3,000+ format combinations; global network | Not a general gift/POD catalogue |
| **Bookvault** | ⚠️ Very interesting | Premium books and collector editions | Foiling, **holographic foil**, custom sprayed edges, endpapers, ribbons, slipcases | Personalized transient API orders currently UK-only |
| **Cloudprinter** | ✅ API/global network | Commercial print, posters, books and **card sets** | Each card in a set can have its own personalized design | No holo/foil collectible-card finishing |
| **Gooten** | ✅ Open API | Weird/general gifts: puzzles, blankets, candles, ornaments, acrylic, stationery, mugs, wall art | Huge gift catalogue through one API | Production varies across network partners |
| **Printify** | ✅ API | Massive long-tail catalogue | Unique print file with placement/scale/rotation | Quality depends on individual print provider |
| **Printful** | ✅ API | Reliable apparel/home merchandise | Labels, packing-slip branding, stickers, branded pack-ins | Pack-ins require stocked materials beforehand |
| **Contrado** | ✅ New white-label API | Premium/weird homeware, accessories, fabric, fashion and art | 500+ premium products, in-house manufacturing, white-label | More expensive; use for premium SKUs |
| **merchOne** | ✅ API | Wall art/home décor at scale | Personalized print files, US/EU in-house production | Less useful for books/cards |
| **CustomCat** | ✅ API | General merch/apparel/homeware | Direct/API fulfillment | More of a merch provider |
| **Scalable Press** | ✅ Very clean REST API | Cheap mugs, posters, phone cases, garments | Programmatic designs, quotes and orders; no MOQ | Catalogue mostly apparel/mugs/cases/posters |
| **The Game Crafter** | ✅ Surprisingly programmable | Card decks, tuck boxes, game components | API can create games/cards/decks/boxes, construct carts, attach addresses and checkout | More complicated integration |
| **MakePlayingCards / MPC** | ❌ No public API | **Best physical collectible product** | Real 2.5×3.5 sports cards; full holographic foil; spot holo/gold/silver foil; booster packs | No proper public order API |
| **Merchize** | ⚠️ Secondary | Huge gift/apparel catalogue and branded packaging | API/integration support, custom packaging | Some workflows still contain payment/approval step |

---

## Product × Supplier Matrix

| # | Product | Primary | Alternate | Notes |
|---|---------|---------|-----------|-------|
| 1 | GameWinners | Prodigi | Cloudprinter / TGC / MPC | MPC for holo eventually |
| 2 | Legendary Card | Cloudprinter or TGC | Prodigi → MPC | True holo = MPC |
| 3 | Dogcasso | Prodigi | Gelato / Contrado | Overlay text ourselves |
| 4 | Birthday Roast | Prodigi | Gelato | Mail4Me UK-produced |
| 5 | Breaking News | Prodigi | Cloudprinter / Lulu | Don't imitate real trademarks |
| 6 | Dogumentary | Prodigi | Lulu | Premium photo-book |
| 7 | Movie Trailer | Prodigi | Gelato / merchOne | Own movie universe |
| 8 | The Boss | Prodigi | Gooten / Contrado | Photo-block style acrylic |
| 9 | Best Man / Wedding | Prodigi | Lulu | Layflat premium |
| 10 | Romantic Film | Prodigi | Gelato | Own movie universe |
| 11 | Christmas Story | Lulu | Bookvault / Prodigi | Full unique PDF |
| 12 | Personalized Comic | Lulu | Prodigi magazine | Deterministic lettering |
| 13 | Birthday Newspaper | Prodigi | Lulu / Cloudprinter | Magazine format |
| 14 | Yearbook | Prodigi | Lulu | Hardcover/layflat |
| 15 | Recipe Book | Lulu | Bookvault | Coil binding |
| 16 | Biography | Lulu | Bookvault premium | Gold/holo foil possible |
| 17 | Private Crossword | Lulu | Bookvault | Wire-bound puzzle book |
| 18 | Star Map | Prodigi | Gelato / merchOne | Transparent acrylic |
| 19 | Mythic Portrait | Prodigi | Contrado / merchOne | Fictional universe |
| 20 | Children's Adventure | Lulu | Bookvault / Prodigi | Full unique PDF |

---

## Supplier hierarchy

**Prodigi = default physical API.**
**Lulu = default personalized-book API.**
**Gooten = unusual-gift catalogue.**
**The Game Crafter = programmable collectible/card lab.**
**Gelato = geographic/availability fallback.**
**Contrado = premium weird products.**
**Cloudprinter = commercial print/card-set fallback.**
**Printify/Printful = commodity long-tail fallback.**
**Bookvault = premium book upgrade once bespoke automation is verified.**
**MPC = ultimate GameWinnerz card manufacturer once we secure programmatic ordering.**

---

## The architecture

```
GiftBrief
    │
    ▼
ExperienceManifest
    │
    ▼
PhysicalProductSpec
    │
    ▼
SupplierRouter
    │
    ├─ Prodigi (general)
    ├─ Lulu (books)
    ├─ Gooten (weird gifts)
    ├─ The Game Crafter (collectibles)
    └─ [fallback chain]
```

**One GiftBrief → multiple physical formats → replaceable suppliers.**

---

## The product strategy

```
6 experience engines
×
5-10 physical formats
×
occasions
×
seasonal skins
= hundreds of SKUs from small codebase
```

One customer conversation produces multiple manufacturing routes from a single GiftBrief.
