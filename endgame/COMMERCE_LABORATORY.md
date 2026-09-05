# The Commerce Laboratory — Endgame Architecture

**Date:** 5 September 2026

---

## The Convergence

StallSpy becomes the commerce laboratory for Moltwork. Etsy/eBay/Amazon become different economic environments in which we train and evaluate operator agents.

The key realization:

> **We are not trying to predict what products sell. We are trying to train agents to make good capital-allocation decisions from imperfect information, then measure whether those decisions actually made money.**

That changes the architecture.

---

## 1. Build a commerce equivalent of Atari environments

An `mwgym` marketplace world should be a timestamped snapshot:

```text
WORLD: EBAY_US_2024_Q4
DECISION DATE: 2024-09-01
CAPITAL: £500

VISIBLE INFORMATION
───────────────────
eBay market state up to 2024-09-01
Google search trends up to 2024-09-01
Pinterest trends available at that date
macro / retail reports available at that date
supplier prices available at that date
seasonality
historical sales
competition
fees
shipping
agent's existing capabilities

TASK
───────────────────
Allocate £500.
Choose what to sell.
Choose quantities.
Choose prices.
Choose listing strategies.
Choose advertising allocation.

HIDDEN
───────────────────
Sep-Dec 2024 actual marketplace outcomes
```

Agent commits its portfolio. Then reveal future. Score: return on capital, prediction calibration, drawdown, inventory risk, capital efficiency, time to feedback, forecast accuracy, opportunity cost.

**Critical rule: temporal isolation.** Every datum needs `observed_at`, `published_at`, `available_at`, provenance and world-version metadata.

---

## 2. Train on the Past, Deploy into September 2026

```text
2019 ───────────────────── 2025 │ 2026
                                 │
     HISTORICAL WORLDS           │ LIVE WORLD
                                 │
train / evaluate / compare       │ deploy
                                 │
Etsy Q4 2023                     │ Etsy Q4 2026
Etsy Q4 2024            ────────►│
Etsy Q4 2025                     │
eBay Q4 2023                     │
eBay Q4 2024                     │
eBay Q4 2025                     │
Amazon Q4 2023                   │
Amazon Q4 2024                   │
Amazon Q4 2025                   │
```

Run tournaments:

```
GPT-5.6 baseline
vs DeepSeek baseline
vs Oracle-enhanced operator
vs Oracle + memory
vs Oracle + memory + reviewers
vs aggressive policy
vs conservative policy
vs cross-market Moltwork operator
```

Every agent gets identical information at identical timestamps. Answer:

> Does Moltwork actually make agents economically smarter?

Not SWE-bench. Not vibes. **Return on capital under unseen future market conditions.**

---

## 3. The Marketplaces Are Beautifully Different

| Property | Etsy | eBay | Amazon |
|----------|------|------|--------|
| Core advantage | differentiation | price/inventory discovery | operational scale |
| Product identity | unique/custom | existing/used/rare | standardized catalog |
| Strong product types | personalized, designed, handmade, vintage, digital | used, collectible, parts, pre-loved | repeatable new goods, private label |
| Main question | **What desirable thing can I create?** | **What is mispriced/undersupplied?** | **What repeatable demand can I supply?** |
| Moat | creativity / personalization | sourcing / information | supply chain / brand / ranking |
| Inventory | can be zero/POD | frequently opportunistic | generally much more important |
| Pricing | differentiated | highly market-driven | intensely competitive |
| Scale path | more designs/niches | more sourcing throughput | inventory + FBA + brand |

Transfer coefficients become data:

```
trend detection:         Etsy → Amazon strong
personalization:         Etsy → Amazon Custom only
price arbitrage:         eBay strong, Amazon moderate, Etsy weak
creative differentiation: critical Etsy, useful Amazon, less eBay commodities
inventory allocation:    minor Etsy POD, important eBay, critical Amazon
```

---

## 4. eBay = Incredible Historical Gym

eBay Product Research provides **up to three years of actual sales data**, including actual accepted Best Offer prices, sales trends, sold price ranges, shipping costs, seller counts and sell-through rate.

```text
STATE(t)
   ↓
agent decides inventory
   ↓
advance 30/60/90 days
   ↓
observe real historic market
   ↓
score agent
```

**Etsy = first live experiment. eBay = first serious retrospective benchmark.**

---

## 5. Amazon = Advanced Level

Product Opportunity Explorer: current Amazon-derived signals around searches, purchases, reviews, pricing, niche saturation.

SP-API: catalog lookup, listing creation/update, sales/traffic reporting, Brand Analytics, Search Query Performance.

Keepa API: historical product prices, sales rank, historical monthly bestseller lists.

```text
£10,000 capital
Choose: SKU, supplier, order quantity, price, FBA/FBM, launch timing, ad budget, restocking point
↓ 90 days
Did you: stock out? over-order? lose Buy Box? misread demand? destroy margin with ads?
```

---

## 6. Oracle = Universal Sensory System

```
                EXOGENOUS WORLD

Google Trends (5yr rolling, geo, scaled)
Pinterest Trends (growing keywords, WoW/MoM/YoY)
TikTok Creative Center (ads, keywords, trends)
fashion/design reports
retail calendars
holidays
macro conditions
supplier movements
social signals
search signals
                     │
                     ▼
                  ORACLE
                     │
          normalized opportunity graph
                     │
        ┌────────────┼─────────────┐
        ▼            ▼             ▼
      Etsy          eBay         Amazon
```

Oracle learns:

```
External signal: "bow aesthetic" accelerating

ETSY: personalized/hand-designed accessory opportunity
EBAY: vintage/pre-loved fashion pricing opportunity
AMAZON: standardized accessory demand, needs volume evidence
```

That's an **economic world model**.

---

## 7. Etsy Historical Signals

Etsy has years of archived Seller Trend Reports (Holiday 2023, 2024, 2025, 2026).

Benchmark:

```
RAW DATA BENCHMARK    — agent sees metrics
vs
ANALYST BENCHMARK     — agent sees human industry reports
vs
ORACLE BENCHMARK      — agent sees fused signal graph
```

Measure whether Oracle adds value.

---

## 8. StallSpy Architecture

```text
stallspy-core
stallspy/etsy
stallspy/ebay
stallspy/amazon
```

Same conceptual interface per marketplace:

```
observe_market()          get_impressions()
discover_opportunities()  get_clicks()
estimate_demand()         get_orders()
estimate_competition()    get_returns()
estimate_unit_economics() get_fees()
create_listing()          get_profit()
update_listing()
set_price()
set_inventory()
advertise()
```

All three have serious programmatic surfaces. Not speculative browser automation.

---

## 9. QDW = Control Tower

```
                         QDW
              GLOBAL ECONOMIC IDENTITY
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
    Etsy Shop         eBay Store       Amazon Store
        │                │                 │
        └────────────────┼─────────────────┘
                         │
                    Cost Ledger
                   Revenue Ledger
                  Experiment Ledger
                   Evidence / Proof
                    Profit / L

Marketplace says: order = £29.99
QDW says:
  revenue             £29.99
  POD                  -8.12
  marketplace fees     -3.41
  ad attribution       -4.80
  generation cost      -0.19
  refund reserve       -0.62
  ──────────────────────────
  economic reward      £12.85
```

---

## 10. MarketDecisionTrajectory

First-class Moltwork primitive:

```yaml
world:
  marketplace: etsy
  market: UK
  timestamp: 2026-09-06

observation:
  oracle_snapshot: ...
  marketplace_snapshot: ...
  trend_snapshot: ...

belief:
  hypothesis: "X will outperform"
  expected_sales_30d: 17
  expected_profit: 214
  confidence: 0.71

decision:
  products: [...]
  capital_allocated: 48
  reasoning_features: [...]

execution:
  artifacts: [...]
  listings: [...]
  ads: [...]

outcome:
  actual_sales: 13
  actual_profit: 181
  elapsed_days: 30

review:
  forecast_error: ...
  independent_reviews: [...]
  lessons_promoted: [...]

policy:
  operator_version: 18
```

**State → belief → allocation → action → economic consequence.**

---

## 11. Cross-Market Transfer

Etsy operator completes 5,000 historical worlds. Throw it into eBay with no eBay training. Measure. Give it 50 eBay worlds. Measure again. Then Amazon.

Derive transfer coefficients:

```
                     ETSY     EBAY     AMAZON
trend reasoning       █████████████████
pricing reasoning       ███████████████
creative selection    ████████
inventory reasoning             █████████████
sourcing                        ███████████████
capital allocation    █████████████████████████
seasonality           █████████████████████████
```

Some skills universal. Some marketplace-specific. **Moltwork discovers the difference automatically.**

---

## 12. StallSpy Chooses the Marketplace

User provides:

```
I have £1,000.
I can use POD.
I'm in the UK.
I can spend 10 hours/week.
I want something live before Christmas.
```

StallSpy/Oracle answers:

```
Opportunity A: Personalised pet memorial print
  Best market: Etsy
  Amazon Custom: secondary
  eBay: don't bother

Opportunity B: Vintage discontinued Christmas ornaments
  Best market: eBay
  Etsy: viable if vintage-qualified
  Amazon: poor fit

Opportunity C: Reusable gift-storage organizer
  Best market: Amazon
  eBay: secondary
  Etsy: weak differentiation
```

**Marketplace selection itself becomes an agent decision.**

---

## 13. The Mega-System Loop

```
                  GLOBAL SIGNALS
                       │
                       ▼
                    ORACLE
            "where is opportunity?"
                       │
                       ▼
                    MOLTWORK
             "what should we do?"
                       │
                       ▼
                CAPITAL ALLOCATOR
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        ETSY          EBAY        AMAZON
          │            │            │
          └────── STALLSPY ─────────┘
                       │
                    actions
                       │
                       ▼
                 QDW-WORKBENCH
             canonical economic truth
                       │
                       ▼
                    OUTCOME
                       │
               ┌───────┴────────┐
               ▼                ▼
          reviewers          mwgym
               │          historical replay
               └───────┬────────┘
                       ▼
                   ARENAV2
                policy comparison
                       │
                       ▼
                OPERATOR MEMORY
                       │
                       ▼
                 BETTER MOLTWORK
                       │
                       └──────────────► ORACLE
```

FinalBuilds2 sits inside execution, manufacturing storefronts, imagery, personalization UIs, landing pages, ads.

---

## The Critical Architectural Decision

Create **one canonical marketplace-world schema now**:

```
MarketWorld
MarketSnapshot
Opportunity
DecisionTrajectory
EconomicOutcome
```

Then:

```
EtsyWorld implements MarketWorld
EbayWorld implements MarketWorld
AmazonWorld implements MarketWorld
```

Force every experiment — historical or live — to use the same trajectory format.

The first Etsy store isn't merely a store.

**It's experiment #1 in a dataset that could eventually contain millions of economically grounded agent decisions across multiple real marketplaces.**

That's when Moltwork becomes exactly what we've been reaching toward: **a system for teaching agents not merely how to work, but how to decide what work is worth doing.**
