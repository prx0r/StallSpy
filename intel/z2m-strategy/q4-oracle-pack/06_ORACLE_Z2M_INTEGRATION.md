# Oracle / Z2M Extension Spec

## Goal

Extend Oracle from machine-work economics into **commerce economics** without making Z2M a second control plane.

## New canonical entities

### `CommerceObservation`
```json
{
  "source": "etsy|google|pinterest|shopify_benchmark|supplier|competitor",
  "entity_key": "normalized product/category/query",
  "market": "GB",
  "observed_at": "...",
  "metrics": {},
  "raw_ref": "...",
  "confidence": "observed|reported|inferred"
}
```

### `CommerceOpportunity`
```json
{
  "id": "...",
  "product_family": "...",
  "market": "...",
  "distribution_surfaces": [],
  "capital_required": 0,
  "paid_media_dependency": 0.0,
  "contribution_estimate": 0,
  "demand_evidence": [],
  "competition_evidence": [],
  "supplier_evidence": [],
  "hypothesis_parents": [],
  "existing_capabilities": [],
  "missing_capabilities": [],
  "status": "HYPOTHESIS"
}
```

### `CommerceExperiment`
Stages:
```text
HYPOTHESIS
→ RESEARCHED
→ FREE_SIGNAL_TEST
→ TEST_READY
→ PAID_TEST
→ VALIDATED
→ SCALE
→ REJECTED
```

## Sensors to add

### Zero/low-cost
- Google Merchant free-listing performance
- Google Search Console queries
- Google Trends/manual export or approved connector
- Etsy Marketplace Insights/manual export
- Pinterest Trends / analytics export
- marketplace listing impressions/clicks
- supplier price/stock snapshots
- competitor price/stock snapshots
- organic social/post analytics
- affiliate outbound-click and conversion receipts

### Paid only when justified
- Google Ads Keyword Planner / Ads actuals
- Shopping/PMax actuals
- Pinterest Ads actuals

## Change events

```text
SEARCH_DEMAND_RISING
SEARCH_DEMAND_FALLING
CPC_RISING
CPC_FALLING
FREE_LISTING_IMPRESSIONS_RISING
COMPETITOR_COUNT_RISING
COMPETITOR_STOCKOUT
COMPETITOR_PRICE_RISING
SUPPLIER_COST_FALLING
SUPPLIER_STOCKOUT
LOCAL_WAREHOUSE_ADDED
SHIPPING_TIME_IMPROVED
MARKETPLACE_QUERY_RISING
PINTEREST_SAVE_RATE_BREAKOUT
Q4_GIFT_WINDOW_OPEN
DELIVERY_CUTOFF_APPROACHING
```

## Admission score

Use observable features, not arbitrary "winning product" scores.

```text
utility =
  demand_evidence
+ organic_distribution_fit
+ contribution_margin
+ personalization_differentiation
+ existing_capability_match
+ verifier_strength
+ q4_fit
+ asset_reusability

- capital_at_risk
- paid_media_dependency
- return_risk
- compliance_risk
- operational_complexity
- competition_density
```

## Critical rule

`competition_density` may not be an LLM guess.

It must be populated from a measurable source or marked `UNKNOWN`, and `UNKNOWN` blocks high-spend admission.
