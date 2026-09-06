# Channel Economics — Q4 2026

## 1. Google free listings: default physical-product foundation

Google states that eligible products can appear for free across Search, Maps, Gemini, YouTube, Shopping, Images and Lens. This is unusually important for a low-capital factory because it lets a feed itself become a distribution experiment.

**Oracle fields to record**
- free impressions
- free clicks
- product-level CTR
- country
- query/product-type
- image variant
- price
- shipping speed
- return policy completeness
- subsequent paid-test result

**Hypothesis:** free-listing signal predicts paid Shopping winners.

## 2. Google paid Search / Shopping

Directional 2026 benchmarks:
- ecommerce Search CPC: about **$1.16–$1.42**
- ecommerce Shopping CPC: about **$0.66–$0.68**
- ecommerce Search CVR: about **2.8–3.2%**
- ecommerce Shopping CVR: roughly **1.4–1.9%**
- broad Search category Shopping/Collectibles/Gifts: **$4.14 CPC** in WordStream/LocaliQ's industry benchmark

Methodologies differ. Never hard-code these as expected performance.

### Admission rule

For any paid test:

```text
contribution_before_ads
× conservative_observed_CVR
>= target_CPC × safety_factor
```

Recommended safety factor: 1.5–2.0 for a small treasury.

### Practical strategy
- Prefer Standard Shopping / product-level isolation for early tests where possible.
- Do not run broad Search merely to “get data.”
- Use negative queries and exact product economics.
- Split SKUs by margin.
- Kill quickly if actual CPC makes break-even impossible.
- Do not scale because ROAS is high on tiny volume; require minimum conversions and stable fulfillment.

## 3. Etsy

Current fee structure:
- $0.20 listing fee
- 6.5% transaction fee
- country-dependent payment processing
- Offsite Ads can add 12%/15% on attributed orders

Why use it anyway: marketplace-native intent and gifting discovery can substitute for ad spend.

Best role for our system:
- validation marketplace
- exact keyword/recipient/occasion experiments
- personalization testing
- price elasticity
- proof before launching independent store

## 4. Pinterest

Use **organic first**.

Pinterest's 2026 holiday material says shoppers plan early, visual search is growing faster than text search, and platform materials report strong incremental ROAS for advertisers. The compelling bit for us is not the ad claim: it is that one product can generate dozens of high-quality visual contexts cheaply with AI.

**AI moat**
- room/recipient-specific mockups
- style variants
- gift-recipient boards
- before/after or assembly visuals
- motion from still product assets
- local-language variants

Measure:
- saves / impression
- outbound CTR
- product click-through
- assisted conversion
- winner concentration by creative template

## 5. SEO / AI discovery

Generic “best gifts” is saturated. Specialist sites can still compound if they provide something chat alone cannot reliably do:
- current price/stock
- compatibility
- shipping cutoff
- exact product data
- exhaustive comparison
- deterministic filters
- personalization
- country-specific taxes/returns/warranty

This directly matches FinalBuilds' existing hypothesis that live data, verification, persistence and real-world side effects are defensible product classes.

## 6. Marketplace ladder

**Digital/POD validation**
1. Etsy
2. own lightweight site
3. Ko-fi/Fourthwall/Gumroad where audience/direct traffic exists

**Handmade physical**
1. Etsy
2. Amazon Handmade after proof
3. own specialist store

**Vintage/collectible**
1. eBay/Etsy
2. curated specialist property

The factory should rank *distribution surfaces* as well as products.
