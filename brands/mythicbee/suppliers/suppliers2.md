# MythicBee — Supplier Investigation v2
**Date:** 2026-09-06
**Status:** CANONICAL — product strategy update

---

The supplier investigation changes the product strategy quite a bit.

We were still thinking too much in terms of **"20 themes, then print the output on something."** The more interesting model is:

**MythicBee story engine × physical magic mechanic.**

The physical object should *do something*: reveal, transform, move, glow, assemble, get worn, get opened, or become playable.

---

## The biggest discovery: Merchize jumps way up the list

Merchize is almost absurdly aligned with GameWinnerz. It has a literal **Acrylic Football Card Sign**: 5mm acrylic, wood stand, 4×6 or 8×12, MOQ 1. It also has custom acrylic cards, metal wallet cards, holographic spinning standees and custom-shape signs. ([Print on Demand & Fulfillment Service][1])

Even better, it has fully sublimated football/soccer jerseys where we can personalize the **entire design, name, number, fictional badge and colors**. Current base pricing shown is around $12.50 for the soccer jersey, $16.25 for the football jersey and $20.50 for a full soccer shirt-and-shorts set, all MOQ 1. ([Print on Demand & Fulfillment Service][2])

And it isn't merely a manual POD catalog. Merchize exposes API access, while its Order Desk integration can ingest dynamic `print_url` artwork, automatically push the order to manufacturing, then sync tracking back. ([OrderDesk Help][3])

That means **GameWinnerz should probably have a wearable tier.**

### GameWinnerz: The Pro Contract

Customer tells Bartholomew about Dad.

We invent his fictional club:

**Prior Athletic FC**
Founded 1966
#60
Captain
"ONE CLUB MAN"

Then automatically generate:

| Item | Product |
|------|---------|
| Collectible | Acrylic football card |
| Wearable | Full personalized football shirt |
| Pocket collectible | Metal GameWinnerz card |
| Digital | Stadium cinematic |
| Reveal | QR linking everything together |

The killer bit is that the jersey seen **in the AI film can be the exact jersey we manufacture**.

So Dad watches himself score the winner wearing:

> PRIOR
> 60

…and the physical shirt in the package is that shirt.

That's much stronger than a personalized card alone.

---

## The physical mechanics we're missing

Seven reusable product mechanics:

| Mechanic | Physical experience | Example |
|----------|-------------------|---------|
| **Reveal** | Something hidden appears | heat mug, puzzle, QR |
| **Transform** | Object visually changes | lenticular card, hologram |
| **Animate** | Object moves | spinning acrylic |
| **Illuminate** | Object changes when lit | night light, suncatcher |
| **Play** | Recipient interacts with rules | custom board game/deck/dice |
| **Wear** | Recipient becomes the character | fictional jersey, patch, jewelry |
| **Artifact** | Feels like a precious object from their story | sprayed-edge biography, woven tapestry |

Those mechanics can be shared across the existing 20 themes.

---

## The Living GameWinnerz Card

MakePlayingCards produces **lenticular cards** where two completely different images occupy the same physical card and switch as you tilt it. MOQ 1. ([MakePlayingCards][4])

**angle 1** → ordinary photo of Dad
**angle 2** → Dad in full stadium kit, arms out, confetti, OVR 99.

Premium end state: **sealed GAMEWINNERZ foil packet → rip it open → lenticular transformation card → scan → film.**

---

## The Game of You

The Game Crafter exposes APIs for cards + decks + custom dice + custom printed meeples + acrylic shapes + dials + score pads + booklets + tuck boxes. ([The Game Crafter][5])

Bartholomew interviews the buyer and creates an **actual personalized tabletop game**.

### "THE GAME OF DAVE"

Characters with special abilities. Board events from real life. Custom game box + cards + dice + meeples + rulebook.

**£50–100 personalized gift category.**

---

## The Puzzle That Lies To You

Gooten has **Gag Jigsaw Puzzles** with **two different printed images**: one on box, another on puzzle. ([Gooten][6])

Box: elegant family portrait.
Actual puzzle: the entire family rendered as medieval degenerates.

Put the final **QR into the completed image** — digital reveal can't be seen until puzzle is assembled.

---

## The Family Tapestry

Gooten's **woven** products: physically woven from colored cotton yarn, 195 color combinations, fringed edges.

### House of Prior

Bartholomew invents a family mythology / heraldic artwork. Woven into an actual tapestry.

**House of Us** for couples. **The Pack** for pets.

---

## The Heat-Reveal Product

merchOne's "magic mug": thermochromic coating conceals artwork, hot liquid reveals it. API permits different artwork URL per order.

Cold: **completely black**
Pour coffee: **Dad as OVR 99 GameWinnerz hero**

---

## Portal Lights

Merchize has custom-shape photo night lights, two-sided versions, holographic variants.

Daytime: transparent acrylic silhouette.
Turn light on: entire illustrated magical world appears.

**MythicLight** — reusable product class.

---

## The spinning holographic character

Merchize custom-shape hologram spinning standee ~$4.20. Laser-cut around their body → physical desktop character.

---

## The metal "access key"

Merchize credit-card-sized aluminum wallet card. Double-sided full-color. Optional hologram effects.

**Legend Pass / Love Licence / Official Dog Ownership Certificate**

---

## The Secret Edge Book

Bookvault: holographic/gold/silver foiling, custom sprayed page edges, custom endpapers, ribbon bookmarks, slipcases. From one copy.

Edge of book reads: **DAVE 1966—2026**

---

## "Your Future Biography"

Lulu: fully unique book-of-one API. 3,000+ print configurations. 200+ countries.

**The Authorized Biography From The Year 2086** — first half true, second half glorious fictional future.

---

## Storyworld Room

Contrado: 500+ premium products, 140+ printable fabrics.

Child's universe feeds: storybook, wall mural, cushion, fabric, blanket, curtains, framed hero image.

**Their bedroom becomes the book.**

---

## Mythic Sigils

Printify: engravable jewelry, headless personalization API.

Bartholomew generates a **symbol** from the GiftBrief → pendant + date/coordinates.

**"Your Symbol"** — standalone MythicBee product.

---

## Quest patches / achievement badges

Printful: no-MOQ custom embroidered patches.

**DRAGON TAMER — LEVEL I** / **CERTIFIED ELF WRANGLER** / **GOOD BOY HANDLER**

---

## Growth Quest

merchOne 120cm child's measuring bar.

**70cm — HATCHLING → 120cm — MYTHIC LEGEND** with avatar evolving.

---

## Memory Mosaic

merchOne MIXPIX: modular wall pieces. Nine moments → nine physical tiles. Gift that accumulates.

---

## Provider priority

| Provider | Capability | New idea | Priority |
|----------|-----------|----------|----------|
| **Merchize** | acrylic, holo, metal, sportswear, lights | GameWinnerz Pro Kit | **10/10** |
| **Game Crafter** | programmable cards/dice/meeples | The Game of You | **10/10** |
| **Gooten** | gag puzzle + woven goods | Reveal Puzzle / Tapestry | **9.5/10** |
| **MPC** | lenticular + foil booster | Living Card | 10/10 product, 4/10 automation |
| **Bookvault** | sprayed edge + foil | Artifact Biography | **9/10** |
| **Lulu** | book-of-one API | Future Biography | **9/10** |
| **merchOne** | thermochromic mug + MIXPIX | Heat Reveal / Memory Mosaic | **8.5/10** |
| **Contrado** | fabric/wallpaper/leather | Storyworld Room | **8/10** |
| **Printify** | engravable jewelry | Mythic Sigil | **8/10** |
| **Prodigi** | huge API + acrylic + paper | Glass Relic | **8/10 backbone** |
| **Cloudprinter** | multi-card/page sets | Party Kit | **7/10** |
| **Printful** | embroidered patches | Quest Badges | **6.5/10** |

---

## 8 new products/engines

| New product | Why exceptional |
|-------------|-----------------|
| **The Game of You** | Entire personalized tabletop game |
| **Living Card** | physical before/after transformation |
| **Reveal Puzzle** | completing the object unlocks the gift |
| **GameWinnerz Pro Contract** | video avatar's actual shirt arrives physically |
| **MythicLight** | glowing custom-shaped story artifact |
| **House of Us** | family mythology woven as tapestry |
| **Mythic Sigil** | AI converts relationship into symbol + jewelry |
| **Artifact Biography** | collector-edition publishing |

---

## Architecture

```
GIFTBRIEF → STORYWORLD → CANONICAL ASSET SET → CARD/VIDEO/BOOK/GAME/OBJECT
```

GiftBrief and story intelligence do the hard work once. Everything downstream is merchandising.

### The three to build first

1. **Merchize** — GameWinnerz Pro Kit (acrylic, jerseys, metal cards)
2. **Gooten** — Reveal Puzzle (two-image mechanic already exists)
3. **Game Crafter** — The Game of You (personalized tabletop game)

[1]: https://merchize.com/product/acrylic-football-card-sign/
[2]: https://merchize.com/product/all-over-print-football-jersey/
[3]: https://help.orderdesk.com/integration-setup-guides/print-on-demand/merchize-integration/
[4]: https://www.makeplayingcards.com/promotional/lenticular-playing-cards.html
[5]: https://www.thegamecrafter.com/developer/
[6]: https://www.gooten.com/products/
[7]: https://www.gooten.com/api-documentation/products/
[8]: https://www.gooten.com/print-on-demand/woven-blankets/
[9]: https://docs.merchone.com/api-reference/api-v1/orders
[10]: https://merchize.com/product-category/collection/valentine/
[11]: https://merchize.com/product/metal-wallet-card/
[12]: https://merchize.com/product-category/collection/mothers-day/
[13]: https://bookvault.app/special-edition-book-printing/
[14]: https://www.lulu.com/personalized-books
[15]: https://www.contrado.com/
[16]: https://www.contrado.com/custom-wallets
[17]: https://developers.printify.com/
[18]: https://developers.printful.com/docs/
[19]: https://www.printful.com/custom-patches
[20]: https://merchone.com/wall-decoration/kids-measuring-bar/
[21]: https://merchone.com/products/
[22]: https://www.prodigi.com/products/cards-and-stationery/
[23]: https://www.prodigi.com/products/home-and-living/tabletops/acrylic-prism/
[24]: https://www.cloudprinter.com/products/card-set
[25]: https://merchize.com/product-category/accessories/
[26]: https://www.gelato.com/products/photo-books
[27]: https://scalablepress.com/api
