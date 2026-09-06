# Trend Radar: Low-Cost Seasonal Demand Intelligence

## Goal

Continuously discover **recipient × occasion × product × aesthetic** combinations whose demand is rising before competitors fully price it into ads.

## Data stack

### 1. Google Trends
Google launched an official Trends API alpha in 2025.
Current documented features include:
- rolling five years;
- daily/weekly/monthly/yearly aggregations;
- region/sub-region;
- consistently scaled data across requests;
- data close to current time.

Access remains alpha/limited, so also use:

### 2. Google Trends BigQuery public dataset
Google documents a BigQuery Trends dataset exposing:
- Top 25;
- Top 25 Rising;
- U.S. DMAs;
- international country/sub-region data.

This is a very useful free/cheap radar even without alpha API access.

### 3. Etsy Marketplace Insights
Use:
- rising searches;
- buyer phrases;
- category attributes;
- recipient/occasion language.

Etsy's own 2026 trend guidance explicitly recommends timing inventory/listings ahead of search upticks and using exact phrases buyers use.

### 4. Pinterest
Pinterest is unusually valuable because planning begins early.
2026 Pinterest holiday material says:
- users are already planning before conventional retail peaks;
- visual search grew much faster than text search last holiday season;
- early/always-on presence matters.

Use Pinterest for:
- aesthetic names;
- colour palettes;
- decor motifs;
- recipient inspiration;
- early seasonal slope.

### 5. TikTok Creative Center
TikTok says Creative Center Trends provides:
- trending hashtags by industry;
- trendline;
- related videos;
- audience insights;
- regional popularity;
- related hashtags.

Use it for:
- creative framing;
- viral product demos;
- language;
- novelty formats.

### 6. Google Ads Keyword Planner
Use exact commercial validation:
- monthly search bands;
- geography;
- CPC;
- competition.

A trend with no purchasable query may be content, not commerce.

### 7. Merchant / Shopping SERPs
Daily sample:
- number of advertisers;
- price distribution;
- delivery promises;
- dominant marketplaces;
- visual sameness.

### 8. Reddit
Use for problem/recipient language, not volume:
- “what do I buy my…”
- “gift for someone who…”
- “I want something personalised but…”
- “Secret Santa…”
- “first Christmas…”

### 9. Amazon/Etsy autocomplete
Capture long-tail recipient and occasion phrases.

## Scoring formula

For each hypothesis `h`:

```
score =
  0.20 * seasonal_repeatability
+ 0.15 * current_growth_slope
+ 0.15 * commercial_intent
+ 0.10 * low_competition
+ 0.10 * gross_margin_potential
+ 0.10 * personalization_gain
+ 0.08 * organic_visual_shareability
+ 0.07 * local_fulfillment_fit
+ 0.05 * repeat_recipient_value
```

Do not allow a high trend slope to rescue awful fulfilment or zero margin.

## Seasonal anomaly detection

For a query:
- compute median interest by day-of-year across 3–5 previous years;
- compare current year to seasonal baseline;
- calculate:
  - current percentile;
  - 7d/28d slope;
  - YoY same-week ratio;
  - “days earlier than normal peak ramp”;
  - geographic concentration.

This separates:
**normal Christmas rise** from **unusually strong 2026 rise**.

## “Buzzword × evergreen” transmutation

The most valuable approach is not selling random viral junk.

Combine a transient aesthetic with an evergreen gift need.

Examples:
- “Gothmas” × family ornament;
- “Vamp Romantic” × couple portrait;
- “Cool Blue” × minimalist Christmas card;
- “Pen Pals” × personalised stationery;
- “Glitchy Glam” × party invite/card;
- novelty food motif × ornament.

The *occasion* is stable.
The *skin* changes.

That lets one product engine exploit many trends without rebuilding fulfilment.

## Daily radar output

For each country, output:

| Field | Meaning |
|---|---|
| Query | exact phrase |
| Occasion | Christmas / birthday / etc |
| Recipient | dad / pet owner / couple |
| Product | ornament / puzzle / book |
| Aesthetic | trend skin |
| 7d slope | current acceleration |
| YoY | same-period change |
| CPC | ad pressure |
| SERP competitors | saturation |
| POD fit | supplier availability |
| Margin | modeled |
| Deadline risk | fulfilment |
| Score | 0–100 |
| Action | ignore / landing page / sample / ad test |

## Highest-value automation

Automate **candidate discovery and scoring**.
Do not automate large inventory purchases.

The engine should produce 10–20 hypotheses/day.
A human approves physical samples and meaningful spend.
