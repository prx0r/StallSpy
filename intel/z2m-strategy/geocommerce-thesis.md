# GeoDrop — GeoCommerce Operating System

Build one operating system that repeatedly compiles narrowly coherent premium consultant stores.

---

## The Thesis

> **proven evergreen product + confusing-enough purchase + strong gross contribution + beautiful visual merchandising + verified supplier + local-country experience + AI buying advisor + human escalation**

Not "AmazingPremiumProducts.fi".

Instead:
- **Home Barista Finland**
- **Premium Pet Mobility Finland**
- **Ergonomic Workspace Belgium**
- **Workshop Systems Norway**

The engine is reusable. The customer's perceived expertise is vertical.

---

## Transaction Bands

| Band | Approach |
|------|----------|
| $250–$2,500 | Direct checkout sweet spot |
| $2,500–$5,000 | Assisted checkout; advisor builds confidence, human available |
| $5,000+ | Quote/callback/deposit (unless category proves self-checkout works) |

Enough contribution to buy Google clicks and provide meaningful service without six-week enterprise sales cycles.

---

## The Autonomous Loop

```
Merchant Best Sellers
    ↓
proven category/product/GTIN
    ↓
supplier resolution
    ↓
supplier quality audit
    ↓
country × keyword research
    ↓
Google CPC/competition/search demand
    ↓
local Shopping prices + seller count
    ↓
currency normalization
    ↓
true landed contribution
    ↓
country opportunity score
    ↓
FREE LISTINGS / REJECT / PAID TEST
    ↓
localized consultant storefront
    ↓
actual CTR/CVR/orders
    ↓
learning loop
```

---

## Supplier Layer (Not AliExpress Forever)

Real European supply structures exist:

| Supplier | What | Model |
|----------|------|-------|
| Smoasters | 500+ coffee SKUs, 4 EU warehouses | Zero-stock dropshipping under retailer branding |
| WPM | Espresso equipment wholesale/dealer | Dealer route |
| AOKE | Ergonomic desks | Reseller program, ships from Netherlands |
| Empets | Premium pet products (Poland) | Retailer/private-label |
| Bodyfriend | Massage chairs | European dealer program |

The long-term system:

```
public supplier to test
    → prove demand
    → authorized dealer
    → negotiate margin
    → perhaps exclusive territory/private label
    → local 3PL for winners
```

AliExpress/CJ/AutoDS = discovery infrastructure, not the final moat.

---

## Finland/Norway Market Data

**Finland:**
- 80% bought cross-border in last year (PostNord 2026)
- Online-bank payments preferred
- Delivery choice matters unusually strongly
- Parcel lockers most used/preferred

**Norway:**
- 78% bought abroad
- Vipps = most-used AND preferred payment
- 6/10 abandoned checkout in last 3 months
- Shipping price = #1 abandonment cause

**Key insight: AI translation isn't enough.**

Country compiler needs:
```
language
currency
search vocabulary
Google feed
pricing
payment methods
delivery choices
returns
tax/customs presentation
support language
local FAQs
local imagery/use cases
```

---

## EU Rules Changed July 1, 2026

Duties now apply to low-value non-EU parcels that previously benefited from the €150 exemption.

This further strengthens the EU-warehouse/distributor route.

For non-local customs markets (Norway/Switzerland): reject offers where duties/taxes aren't handled. A €1,500 order with surprise customs bill = incompatible with the brand.

---

## Media Strategy

### Factual Inspection Media (MUST be real)
- Packshots, ports, controls, dimensions
- 360° inspection from real photographs
- Sirv-compatible real-frame pipeline

### Emotional Merchandising Media (AI-powered)
- Runway: product-ad/UGC workflows
- Veo 3.1: multiple reference images, preserve appearance
- Photoroom API: catalog normalization, background replacement, shadows, relighting

```
Supplier photos
    ↓
Photoroom
clean standardized product packshots
    ↓
REAL SAMPLE
24/36 frame 360° inspection
    ↓
Runway / Veo
beautiful lifestyle/demo/UGC variants
    ↓
visual QA against canonical SKU
    ↓
PDP + Google + Meta + AI content
```

---

## AI Sales/Support

Gorgias Shopping Assistant already does conceptually what we need.

Our version: **assistant is subordinate to canonical product truth.**

If spec not verified:
> "I don't have that specification verified."

Then:
```
supplier question → support ticket → human callback → answer recorded → canonical product knowledge improves
```

After 500 conversations we learn: Finnish buyers care about X, Norwegians ask about Y.

PDPs → feeds → comparison pages → ads → supplier requirements all improve.

**That's the moat.**

---

## Tool Architecture

### Core System (We Own)
- Canonical catalog
- Product truth + provenance
- Country configuration
- Economics engine
- Opportunity ranking
- Supplier QA
- Experimentation + outcomes

### External APIs
| Layer | Tool |
|-------|------|
| Google | Ads API, Merchant Reports, Shopping/free listings |
| Supplier | CJ API, AutoDS, direct distributors |
| Store | Shopify Admin/Markets or custom frontend |
| SERP | SerpApi |
| Keywords | DataForSEO (fallback) |
| Imagery | Photoroom API |
| Video | Runway + Veo |
| 360° | Sirv-compatible pipeline |
| Support | Gorgias or internal advisor |
| Callbacks | Twilio |
| FX | ECB reference-rate adapter |
| LLM | OpenAI-compatible |

---

## Implemented Codebase

```
Google Ads API
Merchant Reports API
SerpApi Shopping
DataForSEO
CJ
Shopify
Kopy handoff
Runway
Veo
Photoroom
Sirv 360 manifests
Twilio
ECB FX
OpenAI-compatible LLMs

canonical catalog DB
provenance ledger
market configs
economics engine
opportunity scorer
live market scanner
supplier audit
supplier FX normalization
trade/customs logic
best-seller candidate normalization
fact-bounded localization
Merchant feed generation
premium storefront
advisor
support/handoff
experiment ledger
Docker/VPS deployment
```

### Supplier Auditor Scores
```
authorized reseller path
EU/local warehouse
tracked shipping
delivery speed
warranty
local return address
live stock
GTIN/MPN identity
complete specifications
sample order
replacement parts
human supplier support
```

A supplier can have amazing price and **still fail**.

---

## Category Shortlist

| Category | Why |
|----------|-----|
| Premium pet mobility/furniture | Visual, emotional, low complexity, EU manufacturing |
| Home-barista equipment | Huge consultation value + beautiful content + distributors |
| Ergonomic workspace systems | Strong Google intent, high AOV, dealer structures |
| Workshop/storage systems | Boring evergreen, search-led, spec advice |
| Prosumer craft/hobby equipment | Enthusiasts spend, novices need guidance |
| Premium outdoor-living accessories | Visual + evergreen/search-led |
| Non-medical recovery/wellness | High visual/AOV potential, avoid medical claims |

Massage chairs = phase two (freight, servicing, warranty complexity).

Espresso: not every SKU survives economics. The engine correctly rejects thin-margin fixtures.

---

## The Bigger Vision

GeoCommerce becomes an **allocation engine for commercial demand**:

```
SKU A → Finland
SKU B → Norway
SKU C → Belgium
SKU D → don't sell
SKU E → free listing only
SKU F → €20/day
SKU G → €500/day
```

Suppliers compete for access to **our demand**.

> "We have 3,700 Finnish monthly searches, 2.8× CPC headroom, 42 purchases, €31k demand. Your landed price is €128. Another factory offered €109 DDP with 2-year warranty. Match it and we route volume to you."

No longer dropshippers.

**Programmatically allocating consumer demand across suppliers and countries.**

---

## Sources

- Smoasters: 500+ coffee SKUs, EU dropshipping
- PostNord 2026: Finland 80% cross-border, Norway 78%
- EU customs rule change July 1, 2026
- Google Merchant Reports API
- Photoroom API docs
- Runway Dev API
- Gorgias Shopping Assistant
- Sirv 360° spin
- Twilio Programmable Voice
