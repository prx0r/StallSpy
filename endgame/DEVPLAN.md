# StallShark — The Full Endgame

**Date:** 5 September 2026

---

After going through the data sources, platform APIs, historical reports and account rules, the project has snapped into a much stronger shape:

> **Build the Etsy business and the eBay business now, while simultaneously turning every decision into an mwgym training trajectory.**

And **eBay the primary historical/economic research world**, even if Etsy remains the easiest place to launch the personalized-gifting thesis.

The reason is simple: eBay is unusually observable. Its own Product Research gives sellers **three years of actual sold-item data**, including real accepted Best Offer prices, seller counts, sold-price ranges, shipping and sell-through. Its Sourcing Insights is explicitly designed to identify high-demand/low-supply categories. That is almost absurdly well aligned with what we're building. ([eBay][1])

---

# StallShark vs StallSpy

The thesis has evolved beyond **spying**.

`StallSpy` sounds like:

> research competitors → inspect listings → keyword analytics.

`StallShark` sounds like:

> finds opportunity → evaluates it → deploys capital → launches → hunts for profit.

And *that* is what the product is becoming.

Internal naming:

```text
STALLSHARK
Marketplace operating intelligence
│
├── Spy
│   competitor / listing intelligence
│
├── Radar
│   trends / emerging demand
│
├── Oracle
│   opportunity scoring
│
├── Lab
│   historical simulations
│
└── Operator
    actually launches/runs things
```

So **StallSpy** becomes a beautiful feature name within StallShark.

### Domain/name ranking

| Name               |   My score | Why                                                                                        |
| ------------------ | ---------: | ------------------------------------------------------------------------------------------ |
| **StallShark.com** | **9.4/10** | Active, memorable, money/opportunity connotation, mascotable                               |
| StallSpy.com       |        8.5 | Excellent intelligence product; slightly too passive                                       |
| StallRadar.com     |        8.0 | Very legible, weaker brand personality                                                     |
| StallSignal.com    |        7.8 | Serious analytics feel                                                                     |
| StallIQ.com        |        7.7 | Clean SaaS, generic                                                                        |
| StallScout.com     |        7.6 | Nice concept, but web results suggest the string is already floating around domain indexes |
| StallLab.com       |        7.4 | Perfect for mwgym feature, weaker business brand                                           |
| StallPilot.com     |        7.3 | Good agent operator meaning                                                                |
| Stalls.space        |        6.5 | Cool community/market feel, but doesn't sound like a profit tool                           |

Buy **StallShark.com** if available at sane price. Keep **StallSpy** for the research/intelligence subsystem.

Keep **Moltwork** completely intact. StallShark is the commerce company/product. Moltwork is the autonomous economic machine underneath.

---

# The research result: enough data sources to build this

mwgym data into four classes:

| Class             | What agent sees                        | What it teaches                 |
| ----------------- | -------------------------------------- | ------------------------------- |
| Marketplace state | listings, prices, sales, sellers, rank | What's happening?               |
| Exogenous signals | Google/Pinterest/TikTok trends         | What's about to happen?         |
| Analyst forecasts | Etsy/Pinterest/NRF/etc reports         | What did informed humans think? |
| Future outcomes   | later sales/ranks/prices               | Were we right?                  |

Much better benchmark than simply giving the model historical sales.

---

# 1. eBay is the gold-standard first marketplace gym

Official Product Research provides **three years of actual sold-item data**, including actual Best Offer prices, average sold price, shipping, seller counts and sell-through. ([eBay][1])

```text
EBAY_WORLD_2024_09_01

Everything known by: 2024-09-01
Capital: £500
Markets: eBay UK
Agent may select: 20 inventory positions

Agent predicts: 30d sales, 90d sales, price, margin, sell-through, competition, inventory risk

ADVANCE WORLD → 2024-12-01
Reveal actual market.
Score operator.
```

eBay Feed APIs can expose weekly complete category bootstrap + daily newly-listed inventory + hourly changed inventory. ([eBay Developers][2])

Plus **Marketplace Insights API** for historical sales of sold items (Limited Release — apply for access). ([eBay Developers][3])

```text
ACTIVE MARKET + SOLD MARKET + PRICE CHANGES + LISTING CREATION
+ SELLER COUNTS + TRAFFIC + AD RESULTS + OUR OWN ECONOMIC OUTCOMES
```

---

# 2. eBay is particularly attractive right now

eBay's 2025 Recommerce Report: fifth consecutive annual report, 27,000+ consumers/sellers, 89% expected to maintain/increase pre-loved spending. ([eBay Inc.][4])

eBay 2024 report: 28,000+ people surveyed. ([eBay Inc.][5])

Pre-loved/refurbished: $5.3B positive economic impact in 2025, up $300M YoY. ([eBay Inc.][6])

Initial economic worlds:

```text
collectibles / trading cards
replacement parts / vehicle parts
used electronics / refurbished electronics
vintage objects
pre-loved fashion
discontinued goods
rare/replacement components
bundles/lots
cross-market arbitrage
```

Especially appealing for agents because the job is often **information processing**, not superior creative taste.

Which listing is underpriced? What obscure part has persistent demand? Which objects have high sell-through but poor supply?

---

# 3. eBay gives perfect synthetic → real progression

eBay has a proper Sandbox with virtual seller/buyer accounts, fake money, mock transactions. ([developer.ebay.com][7])

```text
LEVEL 0  Historical replay
LEVEL 1  eBay Sandbox — test operational competence
LEVEL 2  Shadow trading — decisions against live eBay, £0 spent
LEVEL 3  £20 live portfolio
LEVEL 4  £100
LEVEL 5  £500
LEVEL 6  full autonomous store
```

Probably **mwgym's first genuinely excellent economic environment**.

---

# 4. Etsy has fantastic historical trend-document worlds

Etsy Seller Trend / Marketplace Insights archive going back through 2022. ([Etsy][8])

Reports combine **Etsy search data, industry forecasting, buyer research and social trends**. Fall 2023 report calculates YoY changes using Etsy search volumes Jan-Mar 2023 vs 2022. ([Etsy][9])

```text
DOCUMENT WORLD

DATE: 2023-08-09

DOCUMENTS AVAILABLE:
Etsy Holiday 2023
Pinterest trend state
Google trend state
TikTok What's Next information
macro consumer reports

QUESTION:
You're launching 10 Etsy products.
What do you build? Why? Allocate £300.

Reveal Q4.
```

Repeat for 2024, 2025. Then **2026 is the held-out live year**.

---

# 5. There is a particularly interesting opportunity today

September 6, 2026.

Latest Etsy seasonal report: Spring/Summer 2026, published March 17, 2026. Previous Fall/Winter: October 13, 2025. **Fall/Winter 2026 report not yet published.** ([Etsy][10])

Freeze today. Have agents make Q4 predictions. When Etsy publishes Fall/Winter 2026 report, ingest as **new observation**, not retrospectively available.

> Did StallShark predict themes BEFORE Etsy's own trend team published them?

---

# 6. Important Etsy restriction

Etsy API Terms restrict automated scraping/analysis without authorization. Prohibit collecting API content for analytics/ML/AI training without written permission. ([Etsy][11])

```text
SAFE CORE

official published trend reports
+
Marketplace Insights used normally
+
our own shop data
+
our own economic trajectories
+
properly licensed third-party datasets
```

Separately: approach Etsy/third-party providers for explicit commercial dataset rights.

---

# 7. eRank/EverBee become potential data suppliers

EverBee: ~206M listings, 75M keywords, 1M sellers, 24-month historical windows. Acknowledges estimates. ([EverBee][13])

EverBee launched research MCP August 2026. ([EverBee Help Center][14])

Acceptable-use restrictions mean: **don't bulk ingest without agreement.** ([EverBee][15])

> Ask EverBee and eRank for a commercial/research data license.

StallShark can eventually become their competitor at the *operator layer* while initially consuming licensed research data.

---

# 8. Google Trends is Oracle's most important neutral signal

Official Trends API alpha (2025): **five rolling years**, daily/weekly/monthly/yearly, geographic breakdowns, consistent scaling across requests. ([Google for Developers][16])

Extremely valuable for historical worlds:

```text
Google searches: "personalized dog portrait" / "Labubu" / "vintage camcorder"
2022 → 2026
```

Oracle estimates: velocity, acceleration, seasonality, geographic diffusion, repeatability, trend half-life.

Apply to Trends API alpha **now**.

---

# 9. Pinterest is nearly perfect for Etsy

Pinterest Trends API: WoW/MoM/YoY growth, weekly normalized interest, trailing year.

Important limitation: doesn't allow arbitrary historic-date queries. **Start snapshotting Pinterest now** to build proprietary historical dataset.

Pinterest Predicts 2026: 21 predicted emerging trends (Dec 9, 2025). ([Pinterest][17])

Evaluation:

```text
Pinterest predicted X.
Did Etsy react? eBay react? Amazon react?
How long was the lag?
Which platform monetized it best?
```

Learning **marketplace propagation dynamics**.

---

# 10. TikTok gives another annual forecast stream

What's Next 2024 (Dec 7, 2023). ([TikTok For Business][18])
What's Next 2025. ([TikTok For Business][19])
Next 2026: authenticity, discovery/curiosity, "Emotional ROI." ([TikTok For Business][20])

```text
TikTok cultural trend
        ↓
Pinterest visual/search adoption
        ↓
Google search adoption
        ↓
marketplace queries
        ↓
listings increase
        ↓
sales
        ↓
saturation
```

Moltwork learning typical lead/lag:

```text
TikTok leads Etsy by 21 days
Pinterest leads Etsy by 13
Google leads Amazon by 9
eBay reacts differently because supply is constrained
```

---

# 11. Annual macro reports

| Source | Recurrence/value |
|--------|-----------------|
| **NRF Winter Holidays** | Annual intent + actual spending, since 2003 ([NRF][22]) |
| **Deloitte Holiday Retail Survey** | 40-year annual survey ([Deloitte][23]) |
| **Adobe Holiday Shopping** | Digital commerce spend, categories ([Adobe][24]) |
| **eBay Recommerce Report** | Annual second-hand market |
| **Pinterest Predicts** | Annual trend forecasts |
| **TikTok What's Next** | Annual cultural/trend forecasts |
| **Etsy Seller Trend Reports** | Multiple seasonal/year |
| **Google Trends** | continuous quantitative search state |

```text
FORECAST DOCUMENTS → October 2025
          ↓
AGENT MAKES PORTFOLIO
          ↓
ACTUAL REPORT → January 2026
          ↓
score()
```

---

# 12. Amazon: replay route via Keepa

Keepa: historical Amazon Best Seller lists by month, **36 months**, across US/UK/Germany/France/Japan/Canada/Italy/Spain/India/Mexico. ([Keepa][25])

```text
AMAZON_UK
September 2023 bestseller state → December 2023
September 2024 → December 2024
September 2025 → December 2025
```

Plus Keepa price histories + Product Opportunity Explorer when live.

Amazon Reviews 2023 corpus: **571.54 million reviews**, May 1996–September 2023. ([Hugging Face][26])

Not a sales ledger. But exceptional for product evolution, category evolution, review velocity, consumer complaints, feature demand, quality signals.

---

# 13. Build mwgym before any marketplace data deal

Open/academic commerce datasets:

### UCI Online Retail II
**1,067,371 actual transactions**, UK online giftware retailer, Dec 2009–Dec 2011, time/product/quantity/price/customer/country. **CC BY 4.0.** ([UCI][27])

```text
You are the retailer on 1 September 2010.
Here's everything before today.
Stock £5,000 worth of goods for Q4.
What do you buy?
```

### Olist
~100,000 real orders, 2016–2018, Brazilian marketplaces. Price, freight, payment, customer, product, status, reviews. ([Kaggle][28])

### Retailrocket
2.75M events: views, carts, purchases, timestamped item properties. ([Kaggle][29])

Test: > Can the operator distinguish traffic from purchase intent?

Before touching Etsy/eBay:

```text
mwgym generic-commerce-v0 → UCI, Olist, Retailrocket, Amazon Reviews
```

Make Arenav2/model comparison work perfectly. Then attach real marketplaces.

---

# 14. Canonical world format — crucial engineering decision

```yaml
world:
  id: ebay_gb_2024_q4_v1
  world_time: 2024-09-01T00:00:00Z
  marketplace: ebay
  region: GB

capital:
  cash: 500
  inventory: 0

observations:
  marketplace_snapshot: ...
  google_snapshot: ...
  pinterest_snapshot: ...
  reports_available: ...

constraints:
  max_inventory_positions: 20
  horizon_days: 120

operator:
  id: moltwork_operator_014
  memory_cutoff: 2024-09-01

decision:
  hypotheses: ...
  confidence: ...
  products: ...
  quantities: ...
  prices: ...
  marketing_budget: ...

reveal:
  market_30d: ...
  market_90d: ...
  realised_outcomes: ...

score:
  pnl: ...
  roi: ...
  calibration: ...
  drawdown: ...
  turnover: ...
  inventory_age: ...
  forecast_error: ...
```

Every datum needs:

```text
event_time
observed_at
published_at
available_at
ingested_at
source
license
```

**`available_at` may be the most important field in the entire project.**

Without it, benchmark leakage destroys the experiment.

---

# 15. Give agents reports as documents, not just feature vectors

```text
September 2024

Documents:

[Google Trends snapshot]
[Etsy Holiday outlook]
[Pinterest Predicts]
[NRF consumer forecast]
[Deloitte retail forecast]
[TikTok What's Next]
[eBay market state]
```

> What do you believe?

Model returns structured hypotheses.

Evaluating something closer to an actual entrepreneur: > Can you read the world intelligently?

---

# 16. Oracle becomes absolutely central

```text
          SLOW SIGNALS
annual reports / demographics / macro / seasonality / historical categories
               +
          FAST SIGNALS
Google acceleration / Pinterest growth / TikTok trends / new eBay listings
sold/listed ratios / price movement / review velocity / competition
               ↓
             ORACLE
               ↓
opportunity:
  concept: "..."
  platform_fit: {etsy: .91, ebay: .34, amazon: .63}
  trend: {velocity: .82, acceleration: .61, durability: .70}
  economics: {expected_margin: 18.20, capital_required: 72, time_to_feedback_days: 11}
  evidence: [google, pinterest, ebay, annual_report]
  confidence: .73
```

Then mwgym measures whether Oracle's scores were calibrated historically.

---

# 17. Train Oracle itself

```text
World t → Oracle says A=0.91, B=0.72, C=0.18
Reveal t+90 → A=+37%, B=-8%, C=-21%
Repeat 100,000 times
```

Test:

```
Oracle alone
vs LLM alone
vs Oracle + LLM
vs Oracle + LLM + memory
vs Oracle + LLM + independent reviewer
```

That's Arenav2.

---

# 18. Three marketplace worlds are not interchangeable

```text
ETSY     "What new thing should exist?"     creative differentiation, personalization
EBAY     "What existing thing is mispriced?"  sourcing, price discovery, scarcity
AMAZON   "What repeatable demand to supply?"  unit economics, inventory forecasting
```

Three different economic IQ tests.

Central research question:

> **What does an Etsy-trained entrepreneur learn that helps on eBay?**

---

# 19. Transferable economic intelligence

```text
Operator A: trained only on Etsy
Operator B: trained only on eBay
Operator C: trained only on Amazon
Operator D: trained across everything
```

Throw into new market. Measure.

```text
trend identification       universal
seasonality                universal
EV reasoning               universal
capital allocation         universal
creative differentiation   Etsy-specific
scarcity sourcing           eBay-specific
inventory forecasting      Amazon-specific
```

Studying **transfer learning for entrepreneurship**.

---

# 20. Live-agent experiment design

Don't initially do separate accounts (account reputation/trust/age can swamp agent effect).

Instead:

```text
ONE REAL EBAY BUSINESS
              │
     randomized products
              │
   ┌──────────┼──────────┐
   ▼          ▼          ▼
Agent A     Agent B     Agent C
20 SKUs     20 SKUs     20 SKUs
£100        £100        £100
```

Same account. Same period. Same capital. Different agents.

**Actual randomized economic agent trial.**

---

# 21. Cold-start championship

```text
STALLSHARK ZERO → ONE

Starting assets: £500, zero products, zero customers, zero feedback
Goal: maximize 180-day economic value
Allowed: market research, sourcing, listing, pricing, marketing, support, reinvestment
```

eBay permits multiple accounts, but prohibits evading restrictions or manipulating feedback. **Real legitimate businesses, not Sybil accounts.** ([eBay][30])

No fake transactions, feedback exchange, shill bidding. Real buyers only.

---

# 22. Etsy same zero→one benchmark

Etsy permits multiple shops with separate accounts/profiles. ([Etsy Help][31])

First compare operators inside same real store via product cohorts. Then legitimate independent shop launches.

```text
ETSY ZERO→ONE    personalized products
EBAY ZERO→ONE    resale / sourcing
AMAZON ZERO→ONE  standard inventory
```

Actual longitudinal benchmark of AI entrepreneurship.

---

# 23. Amazon should come third

Multiple-account policies stricter: one Seller Central per region unless legitimate business need, with related-account enforcement risk. ([Amazon Seller Central][32])

```text
historical Amazon worlds → Keepa simulation → shadow decisions
→ one real Amazon business → product cohort experiments
```

---

# 24. QDW = economic laboratory notebook

Every decision gets one trajectory:

```text
OBSERVATION → BELIEF → CONFIDENCE → FORECAST → CAPITAL ALLOCATION
→ ACTION → MARKET RESPONSE → TRUE P&L → INDEPENDENT REVIEW → MEMORY UPDATE
```

Do not save hidden chain-of-thought. Save structured economic rationale:

```yaml
signals: [sell_through_high, competition_falling, google_trend_accelerating]
thesis: demand likely to exceed supply
risks: [seasonal, supplier concentration]
confidence: 0.68
```

---

# 25. Immediate architecture

```text
                           STALLSHARK
                    commerce-facing product
                            │
             ┌──────────────┼──────────────┐
             │              │              │
          Etsy           eBay           Amazon
        adapter         adapter          adapter
             │              │              │
             └──────────────┼──────────────┘
                            ↓
                          ORACLE
                   opportunity graph
                            │
                            ↓
                         MOLTWORK
                  operator / allocator
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
        FinalBuilds      WorkerKit       suppliers
             │              │
             └──────────────┘
                            ↓
                         ACTION
                            ↓
                     MARKETPLACE
                            ↓
                      QDW-WORKBENCH
                   canonical economics
                            ↓
                   DecisionTrajectory
                            ↓
              ┌─────────────┴────────────┐
              ▼                          ▼
            MWGYM                     ARENAV2
      historical replay          operator tournament
              │                          │
              └────────────┬─────────────┘
                           ↓
                      learned policy
                           ↓
                        MOLTWORK
```

---

# 26. What to do this week

1. **Try to secure StallShark.com.** Keep Moltwork.com. StallSpy = research module.
2. Build canonical `MarketWorld`, `MarketSnapshot`, `DecisionTrajectory`, `EconomicOutcome`, `SourceArtifact` schemas.
3. Build `mwgym-commerce-v0` against **UCI Online Retail II** first — real, temporal, CC BY 4.0. ([UCI][27])
4. Add Olist + Retailrocket as additional test worlds.
5. Build `ebay-world` using manually authorized Product Research data initially; apply for eBay's Limited Release Marketplace Insights/Feed access. ([eBay Developers][3])
6. Create eBay Developer Sandbox seller/buyer agents; wire WorkerKit through complete listing/order lifecycle. ([eBay Developers][7])
7. Start **daily/weekly snapshots now** of every legally accessible ephemeral signal — especially Pinterest; register for Google Trends API alpha. ([Google for Developers][16])
8. Ingest every historical Etsy Seller Trend Report, Pinterest Predicts, TikTok What's Next, NRF Holiday, Deloitte Holiday and eBay Recommerce report as timestamped `SourceArtifact`s.
9. Freeze a **2026-09-06 Q4 World Snapshot now.** It becomes extremely valuable once Q4 happens.
10. Have 5–10 operator configurations independently make **Q4 2026 Etsy + eBay predictions now**, before more future information arrives.
11. Run the real Etsy personalized-product store simultaneously. Every listing becomes a QDW experiment.
12. Start a small real eBay store simultaneously; first goal **£100→£300**, not £0→£1m. Preserve every signal and decision.
13. Randomize eBay/Etsy product opportunities across Moltwork operator policies for causal-ish comparisons.
14. After Q4, lock the dataset and benchmark which September operators actually understood the market.
15. Train/revise the operator and run the exact process again in 2027.

**Begin recording the benchmark before finishing the benchmark software.**

Reconstruct historical 2023–25 worlds later.

**Never reconstruct exactly what the world looked like to us on September 6, 2026** if we fail to snapshot it now.

---

# The Grand Thesis

**StallShark** asks: What should I sell, where should I sell it, and what should I do next?

**mwgym** asks: Would this decision have worked in previous markets?

**Arenav2** asks: Which operator makes the best economic decisions?

**Oracle** asks: What opportunities exist?

**QDW** asks: What actually happened?

**Moltwork** asks: Given everything I've learned, where should I deploy my next unit of money, time and intelligence?

Etsy, eBay and Amazon aren't merely integrations. They are **different worlds in a curriculum for training autonomous economic agents**.

eBay should move way up the priority list. It's the strongest bridge between "cool agent research" and "agent that demonstrably compounds £100 into more money" — historical sold-data, low-capital resale mechanics, Sandbox, APIs and live marketplace all line up unusually well.

And Etsy's Fall/Winter 2026 report and other Q4 reports haven't all landed yet. Freeze predictions now. Automatically ingest/compare as official reports appear.

[1]: https://www.ebay.com/help/selling/selling-tools/research?id=4853 "Product research | eBay"
[2]: https://developer.ebay.com/api-docs/buy/api-feed_beta.html "Feed API beta | eBay Developers Program"
[3]: https://developer.ebay.com/develop/get-started/get-started-on-a-buying-application "Get Started on a Buying Application | eBay Developers Program"
[4]: https://www.ebayinc.com/stories/news/2025-ebay-recommerce-report-publishes-today/ "Nearly Nine in Ten Consumers Plan to Maintain or Increase Spending on Pre-loved Goods"
[5]: https://www.ebayinc.com/stories/news/ebays-inaugural-recommerce-day-celebrates-pre-loved-shopping/ "eBay's Inaugural "Recommerce Day" Celebrates Pre-Loved Shopping"
[6]: https://www.ebayinc.com/stories/news/ebay-publishes-2025-impact-report/ "eBay Publishes 2025 Impact Report"
[7]: https://developer.ebay.com/api-docs/static/sandbox-test-users.html "Configuring Sandbox test users | eBay Developers Program"
[8]: https://www.etsy.com/in-en/seller-handbook/topic/seasonal-tips "Seller Handbook - Marketplace Insights"
[9]: https://www.etsy.com/seller-handbook/article/1148199715118 "Seller Trend Report: Fall 2023"
[10]: https://www.etsy.com/seller-handbook/search/marketplace%20insights "Seller Handbook - Search: marketplace insights"
[11]: https://www.etsy.com/legal/api/ "API Terms of Use - Our House Rules | Etsy"
[12]: https://developers.etsy.com/ "Etsy Open API v3"
[13]: https://everbee.io/ "Etsy Product Research & Sales Data Tool | EverBee"
[14]: https://help.everbee.io/en/article/211-everbee-research-mcp-ask-claude-for-etsy-market-research "EverBee Research MCP"
[15]: https://www.everbee.io/legal/acceptable-use "Acceptable Use Policy - EverBee"
[16]: https://developers.google.com/search/apis/trends "Google Trends API Alpha"
[17]: https://business.pinterest.com/en-ca/blog/pinterest-predicts-2026-turn-trends-into-unlimited-possibilities/ "Pinterest Predicts™ 2026"
[18]: https://ads.tiktok.com/business/en/blog/2024-whats-next-trend-report "What's Next 2024 Trend Report"
[19]: https://ads.tiktok.com/business/en-CA/blog/2025-whats-next-trend-report "What's Next 2025 Trend Report"
[20]: https://ads.tiktok.com/business/en-GB/next "TikTok Next 2026 Trend Report"
[21]: https://ads.tiktok.com/business/en/products/ecommerce "TikTok E-Commerce"
[22]: https://nrf.com/research-insights/holiday-data-and-trends/winter-holidays "Winter Holiday Data and Trends | NRF"
[23]: https://www.deloitte.com/us/en/insights/industry/retail-distribution/holiday-retail-sales-consumer-survey.html "2025 Deloitte Holiday Retail Survey"
[24]: https://business.adobe.com/resources/holiday-shopping-report.html "2025 Holiday Shopping Statistics"
[25]: https://keepa.com/api-docs/best-sellers.html "Best Sellers — Keepa API Documentation"
[26]: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023 "McAuley-Lab/Amazon-Reviews-2023"
[27]: https://archive-beta.ics.uci.edu/dataset/502/online%2Bretail%2Bii "Online Retail II - UCI Machine Learning Repository"
[28]: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce "Brazilian E-Commerce Public Dataset by Olist"
[29]: https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset "Retailrocket recommender system dataset"
[30]: https://www.ebay.com/help/Policy/-/Multiple_accounts_policy?id=4232 "Multiple account policy | eBay"
[31]: https://help.etsy.com/hc/en-us/articles/360017604474-How-to-Open-a-Second-Shop-on-Etsy "How to Open a Second Shop on Etsy"
[32]: https://sellercentral.amazon.com/seller-forums/discussions/t/6a7fbcfc-1ed4-42b0-a382-d2b8d61e1c47 "Account health tips for multiple selling accounts"
