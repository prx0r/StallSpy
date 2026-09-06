# Product + Technical Architecture

## Product principle

The core object is not a SKU.
It is a **RecipientCreative**.

```
Recipient
  ├─ identity / relationship
  ├─ preferences
  ├─ important dates
  ├─ memories/photos
  └─ CreativeWorld
        ├─ art direction
        ├─ reusable assets
        ├─ copy
        └─ product renders
             ├─ card
             ├─ ornament
             ├─ mug
             ├─ puzzle
             └─ book
```

## Suggested stack

### Web
- Next.js / React
- mobile-first
- Stripe or equivalent checkout
- object storage (R2/S3)
- Postgres
- background job queue
- image/PDF rendering workers

### AI
Provider abstraction:
- OpenAI;
- Ideogram;
- Recraft;
- Google;
- Adobe.

### Fulfilment
Adapter abstraction:
- Prodigi;
- Gelato;
- later Gooten/Printify/specialist printers.

## Core API flow

### `POST /api/creative-brief`
Input:
- recipient;
- relation;
- occasion;
- tone;
- budget;
- memories;
- photo references.

Output:
- 4–8 creative concepts.

### `POST /api/generate-assets`
Creates:
- hero art;
- transparent cutout;
- optional vector;
- copy variants.

### `POST /api/render-product`
Input:
- creative ID;
- product SKU;
- template ID.

Output:
- exact print file;
- mockup;
- QA report.

### `POST /api/quote`
Queries providers and returns:
- production cost;
- shipping;
- ETA;
- margin;
- provider.

### `POST /api/order`
Creates payment + fulfilment order only after print QA/customer approval.

## Deterministic template system

Each product template defines:
- physical size;
- print pixels;
- bleed;
- safe zones;
- background;
- dynamic image slots;
- dynamic text slots;
- fonts;
- font fallback;
- min/max sizes;
- export format.

AI should decide **what goes where** within constraints.
The renderer ensures manufacturing correctness.

## QA checks

Automatic:
- image resolution;
- effective DPI;
- missing asset;
- text overflow;
- exact-string match;
- alpha issues;
- safe-zone collision;
- face crop;
- blank page;
- profanity;
- blocked IP terms;
- unsupported file size/type.

Visual:
- generate raster proof;
- customer approves;
- immutable approved render hash stored with order.

## Memory

Recipient memory should be explicit and editable:
- “Mum likes botanical illustrations”
- “Do not use sentimental copy”
- “Dog: Alfie, black lab”
- “Last gift: museum portrait mug”
- “Birthday 14 March”

Privacy:
- clear consent;
- easy delete/export;
- minimize sensitive data;
- do not infer protected/sensitive traits unnecessarily.

## Event model

Track:
- `recipient_created`
- `occasion_added`
- `concept_generated`
- `concept_saved`
- `regenerated`
- `product_previewed`
- `checkout_started`
- `ordered`
- `fulfilled`
- `delivered`
- `recipient_reused`
- `reminder_converted`

This is how you learn which creative recipes work.

## Trend → creative loop

```
Trend Radar
  → hypothesis
  → generated design set
  → landing page
  → organic impressions
  → click/save
  → sample order
  → paid micro-test
  → conversion
  → scale / kill
```

## Multi-country configuration

Country config should contain:
- language;
- currency;
- holidays;
- cultural copy;
- preferred provider;
- payment methods;
- return text;
- shipping cutoffs;
- SEO dictionary;
- taboo/risk words;
- VAT/tax behavior.

One engine; many native surfaces.
