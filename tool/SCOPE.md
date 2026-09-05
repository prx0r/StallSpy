# Etsy Data Cooperative — Build Spec

**Date:** 5 September 2026
**Status:** Thesis + initial data pipeline live
**Goal:** Build the free, open-source Etsy research tool that beats EverBee by using actual sales data.

---

## The Insight

Every Etsy sales estimator (EverBee, Alura, eRank, Marmalead) works the same way:

> Observable signals (views, favorites, reviews, listing age) → ML model → estimated sales

They all admit it's estimation. EverBee literally says "we don't have actual sales data."

**The moat isn't the algorithm. It's the calibration data.**

Only sellers have their own real sales. If we build the tool AND become a seller, we can calibrate estimates against ground truth. Then sellers who upload their CSVs make it better for everyone.

---

## What Exists Today

### Data We Already Have

| Asset | Source | What | Records |
|-------|--------|------|---------|
| `Etsy_top10000shops.csv` | Kaggle/Barkingdata | **Actual sold_count** per shop + reviews, favorites, ratings, active listings | 10,000 shops |
| `raw_shop_reviews.csv` | EtsyAnalysis repo | Scraped review dates + item details per shop | 1,485 shops |
| Live API scraper output | Our `scrape.py` | Listings, prices, reviews, favorites, shop sales, tags — timestamped | 200 listings (growing daily) |
| Etsy API credentials | User-provided | 10K requests/day, listings + reviews + shops + taxonomy | Unlimited |

### Tools We've Cloned

| Tool | Path | Use |
|------|------|-----|
| `aserper/etsy-mcp` | `tool/ml/` | 37 Etsy API tools — listings, orders, reviews, shop management |
| `avlihachev/etsy-mcp-server` | `tool/ml/` | Fresh implementation tracking 2026 API changes |
| `alveyautomation/etsy-mcp` | `tool/ml/` | Read-only, safest for competitor research |
| `etsy-oracle` | `tool/ml/etsy-oracle` | Open-source sales estimator (early stage, extend this) |
| `iscale-etsy` | `tool/ml/iscale-etsy` | Chrome extension — ranking history per keyword with timestamps |
| `etsy-sales-prediction` | `tool/ml/etsy-sales-prediction` | GBM model on 10K shops, R²=0.515 |
| `etsy-Analysis-ML` | `tool/ml/etsy-Analysis-ML` | Random Forest + GB analysis |
| `EtsyAnalysis` | `tool/ml/EtsyAnalysis` | Review timing → seasonality prediction |
| `Analyzing-Etsy-Shops` | `tool/ml/Analyzing-Etsy-Shops` | OLS/logistic regression on shop success |
| 7 Etsy MCP servers | `tools/` | Shop management, listing CRUD, taxonomy |

### Key ML Findings (from cloned repos)

| Finding | Source | Implication |
|---------|--------|-------------|
| Reviews = 5.1x sales difference (top vs bottom decile) | Our analysis of 10K shops | Reviews are THE signal |
| Top 25% by favorites have 23.7x more reviews | Live scraped data | Favorites predict reviews, reviews predict sales |
| Shop age > listing count as predictor | Vertex AI Medium article | New shops can grow fast |
| Star seller badge = 1256 more sales | Analyzing-Etsy-Shops | Badge is a real signal |
| Review date predicts seasonality | EtsyAnalysis | Timing matters — Q4 is everything |
| R²=0.515 with reviews + favorites + rating + listings | etsy-sales-prediction | ~50% of sales variance explainable from public signals |

---

## The Gap

| What We Have | What We're Missing |
|-------------|-------------------|
| 10K shops with actual sales (snapshot) | Time series of the same shops over months/years |
| Live listing data (point-in-time) | Historical tracking — how listings move over time |
| Review counts | Review velocity — reviews per week/month |
| Shop sales | Listing-level sales (only estimable, not actual) |
| 30-day Koalanda spot checks | Continuous daily tracking of keyword rankings |
| ML models trained on static data | Models calibrated against our own actual sales |

**The core gap: no time series.** We need daily/weekly snapshots of the same keywords and listings to see how rankings, favorites, reviews, and estimated sales change.

---

## What We Build

### Phase 1: The Data Warehouse (Week 1-2)

**Objective:** Start accumulating irreversible history from Day 1.

```text
keyword_daily
-------------
keyword             TEXT
date                DATE
total_results       INT          -- how many listings match
top100_listing_ids  JSON         -- which listings are ranking
median_price        FLOAT
avg_reviews         FLOAT
avg_favorites       FLOAT
new_listings        INT          -- listings that appeared since yesterday
exited_listings     INT          -- listings that disappeared

listing_daily
-------------
listing_id          INT
date                DATE
title               TEXT
price               FLOAT
favorites           INT
reviews             INT
views               INT
shop_id             INT
shop_total_sales    INT
tags                JSON
position_in_search  INT          -- what rank for which keyword
```

**Implementation:**
- Run `scrape.py` daily via cron for 20 core keywords
- Store to SQLite (simple, portable, fast enough)
- Add a `daily_snapshot` table with timestamp

**Keywords to track daily (Game Winner focus):**

| Keyword | Why |
|---------|-----|
| `personalized football gift` | Our primary market |
| `personalized birthday video` | Exact product match |
| `scored winning goal gift` | Our unique niche |
| `football birthday gift dad` | High-intent long-tail |
| `personalized sports gift` | Category |
| `custom birthday movie` | Product type |
| `fathers day football gift` | Seasonal peak |
| `50th birthday football gift` | Age milestone |
| `personalized cricket gift` | UK market |
| `baseball birthday gift` | Sport variation |
| `personalized basketball gift` | Sport variation |
| `funny football gift` | Tone variant |
| `gift for husband birthday` | Recipient variant |
| `retirement sports gift` | Evergreen occasion |
| `personalized hockey gift` | Sport variation |

### Phase 2: Sales Estimation Engine (Week 2-3)

**Objective:** Build a transparent, calibratable sales estimator.

Extend `etsy-oracle` with:

```python
def estimate_sales(listing):
    """
    Transparent sales estimation from public signals.
    Returns estimate + confidence band.
    """
    reviews = listing["review_count"]
    favorites = listing["num_favorers"]
    views = listing.get("views", 0)
    age_days = listing["age_days"]
    price = listing["price"]
    
    # Base estimate from review velocity
    # Assumes ~1-3% of buyers leave reviews
    review_rate = 0.02  # conservative
    base_estimate = reviews / review_rate
    
    # Adjust for favorites (people who favorite often buy later)
    fav_multiplier = 1 + (favorites / 1000) * 0.1
    
    # Adjust for age (older listings with same reviews = slower seller)
    age_factor = max(0.5, 1 - (age_days / 730) * 0.3)
    
    # Adjust for views (if available)
    view_factor = 1.0
    if views > 0:
        conversion_est = 0.02  # 2% view-to-sale
        view_estimate = views * conversion_est
        # Blend review-based and view-based
        base_estimate = (base_estimate + view_estimate) / 2
    
    estimate = base_estimate * fav_multiplier * age_factor * view_factor
    
    # Confidence band (wider for older/less-reviewed listings)
    confidence = min(0.9, 0.3 + (reviews / 100) * 0.1 + (favorites / 500) * 0.05)
    
    return {
        "estimated_sales": round(estimate),
        "confidence": round(confidence, 2),
        "method": "review_velocity + favorites + age_adjustment",
        "review_rate_assumed": review_rate,
    }
```

**Calibration loop:**
1. Our shop listings → actual sales (from Etsy CSV)
2. Our estimates vs actuals → compute error
3. Adjust review_rate and multipliers
4. Repeat monthly

### Phase 3: Niche Opportunity Scorer (Week 3-4)

**Objective:** Answer "What should I sell next?"

```text
For each keyword/category:

  demand_score = search_volume × growth_rate
  competition_score = listing_count × avg_reviews × top10_concentration
  margin_score = median_price - estimated_cogs
  seasonality = Q4_factor × occasion_factor
  
  opportunity = demand_score / competition_score × margin_score × seasonality
```

Output:

```text
#1 Personalized football video gift
  Demand:    ████████░░ 8/10  (+61% YoY)
  Competition: ███░░░░░░░ 3/10  (low quality supply)
  Margin:    ████████░░ 8/10  (£7.99-£24.99, ~80% gross)
  Season:    ██████████ 10/10 (Q4 peak)
  Score:     9.2/10
  
  Diagnosis: Searches growing faster than quality supply.
             Most competitors sell static prints.
             Video personalization is nearly absent.
```

### Phase 4: Seller CSV Importer (Week 4-5)

**Objective:** Let sellers upload their Etsy data for calibration.

Sellers download:
- `EtsySoldOrders.csv` (full year of transactions)
- `EtsyStats.csv` (visits, orders, conversion, revenue since 2017)

We give them:
- Free dashboard showing their shop performance
- Benchmarking against category averages
- SEO recommendations

In return (with consent):
- Anonymized aggregate data improves our models
- `seller_ground_truth` table for calibration

### Phase 5: The Tool (Week 5-8)

**Objective:** Free, self-hosted web app.

```text
easyetsy-tool/
├── data/
│   ├── keyword_daily.db      -- SQLite time series
│   ├── listings.db           -- listing snapshots
│   └── calibration.db        -- seller ground truth
├── api/
│   ├── etsy_client.py        -- rate-limited API wrapper
│   ├── scraper.py            -- daily snapshot runner
│   ├── estimator.py          -- sales estimation engine
│   └── scorer.py             -- niche opportunity scorer
├── web/
│   ├── dashboard.py          -- Streamlit or Flask
│   └── templates/
├── ml/
│   ├── train.py              -- model training
│   ├── evaluate.py           -- estimate vs actual
│   └── models/               -- saved models
└── cli/
    └── etsytool.py           -- command line interface
```

**Features:**
1. **Keyword Explorer** — search volume, competition, trends, opportunity score
2. **Listing Inspector** — estimated sales, revenue, review velocity, tag analysis
3. **Niche Finder** — "what should I sell next" with scoring
4. **Shop Benchmark** — compare your shop to category averages
5. **Trend Tracker** — keyword ranking history over time
6. **Competitor Monitor** — track specific shops/listings

---

## Revenue Model

| Tier | Price | What |
|------|-------|------|
| **Free** | £0 | Dashboard, 50 keyword lookups/day, basic estimation, shop benchmark (up to 3 shops) |
| **Pro** | £9.99/mo | Unlimited lookups, advanced estimation, niche scoring, competitor monitoring, CSV import for up to 10 shops |
| **Agency** | £49.99/mo | API access, bulk analysis, white-label reports, priority support |

**Additional revenue:**
- POD affiliate links (Printify, Prodigi) — earn commission on referrals
- Managed shop setup — £500-2000 one-time
- Consulting — £150/hour
- Course — "How to Build a £100K Etsy Shop" — £299

---

## The £0 → £1,000,000 Experiment

The tool proves itself by being a seller.

```text
MONTH 1 (Sep 2026)
├── 8 Game Winner listings live
├── Daily scraper running (15 keywords)
├── 10K shops dataset loaded
├── Sales estimator v1 built
└── Revenue: £0

MONTH 2 (Oct 2026)
├── 20 listings (Football, Baseball, Basketball, Cricket)
├── First sales from organic Etsy search
├── Tool dashboard live (self-hosted)
├── First blog post: "I tested EverBee vs real sales"
└── Revenue: £200-500

MONTH 3 (Nov 2026)
├── Q4 peak begins
├── 40+ listings across sports
├── Tool gains first 10 beta users
├── Time series: 60 days of data
└── Revenue: £1,000-3,000

MONTH 6 (Feb 2027)
├── Post-Christmas analysis complete
├── 120+ listings
├── Tool has 100+ users
├── 6 months of time series
├── First seller CSV uploads for calibration
└── Revenue: £5,000-10,000/mo

MONTH 12 (Sep 2027)
├── Full year of data — nobody else has this
├── 500+ listings across 5 brands
├── Tool has 1,000+ users
├── Models calibrated against 50+ seller shops
├── Blog: "1 Year of Etsy Data: What We Learned"
└── Revenue: £20,000-50,000/mo

MONTH 24 (Sep 2028)
├── 2 years of time series — irreplaceable dataset
├── Tool is the go-to free Etsy research platform
├── 5,000+ users
├── API/MCP for advanced users
├── Pro tier thriving
└── Revenue: £100,000+/mo
```

---

## Technical Architecture

### Data Pipeline

```text
Etsy API (10K req/day)
        │
        ▼
┌──────────────────┐
│  Daily Scraper   │  cron: 6am UTC daily
│  (scrape.py)     │  15 keywords × 100 listings = 1,500 API calls
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  SQLite Warehouse │  keyword_daily, listing_daily, shop_daily
│  (data/*.db)      │  append-only, never delete
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────────┐
│Estimate│ │  Scorer    │
│Engine  │ │  (niche    │
│        │ │  finder)   │
└───┬────┘ └─────┬──────┘
    │            │
    ▼            ▼
┌──────────────────┐
│  Web Dashboard   │  Streamlit or Flask
│  (tool/)         │  self-hosted, local
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────────┐
│  CLI   │ │  API/MCP   │
│        │ │  (later)   │
└────────┘ └────────────┘
```

### Sales Estimation Algorithm

```text
Input signals (from Etsy API):
  - review_count
  - num_favorers
  - views (if available)
  - creation_timestamp (listing age)
  - price
  - tags
  - shop.transaction_sold_count
  - shop.review_average
  - shop.review_count
  - shop.num_favorers
  - shop.listing_active_count

Estimation:
  1. Review velocity: reviews / age_days × 30 = monthly review rate
  2. Convert to sales: monthly_reviews / review_rate (calibrated, ~1-3%)
  3. Adjust for favorites: +10% per 1,000 favorites
  4. Adjust for age: older listings with same reviews = slower
  5. Blend with shop-level signals if listing data is sparse
  6. Output: estimated_monthly_sales + confidence_band

Calibration:
  - Compare estimates vs actual sales from opted-in sellers
  - Update review_rate and multipliers monthly
  - Track R², MAE, RMSE over time
  - Publish accuracy benchmarks publicly (transparency = trust)
```

### Database Schema

```sql
-- Core time series (append-only, never delete)
CREATE TABLE keyword_daily (
    keyword TEXT,
    date TEXT,
    total_results INT,
    top100_ids TEXT,  -- JSON array
    median_price REAL,
    avg_reviews REAL,
    avg_favorites REAL,
    new_count INT,
    exited_count INT,
    PRIMARY KEY (keyword, date)
);

CREATE TABLE listing_daily (
    listing_id INT,
    date TEXT,
    title TEXT,
    price REAL,
    favorites INT,
    reviews INT,
    views INT,
    shop_id INT,
    shop_sales INT,
    tags TEXT,  -- JSON
    position INT,
    keyword TEXT,
    PRIMARY KEY (listing_id, date, keyword)
);

CREATE TABLE shop_daily (
    shop_id INT,
    date TEXT,
    shop_name TEXT,
    total_sales INT,
    review_count INT,
    review_average REAL,
    favorers INT,
    active_listings INT,
    PRIMARY KEY (shop_id, date)
);

-- Seller ground truth (opted-in sellers only)
CREATE TABLE seller_ground_truth (
    listing_id INT,
    month TEXT,
    actual_units INT,
    actual_revenue REAL,
    actual_orders INT,
    actual_conversion REAL,
    seller_id TEXT,  -- anonymized
    PRIMARY KEY (listing_id, month)
);

-- Model predictions (for tracking accuracy over time)
CREATE TABLE estimates (
    listing_id INT,
    date TEXT,
    estimated_sales REAL,
    confidence REAL,
    method TEXT,
    PRIMARY KEY (listing_id, date)
);
```

---

## Dependencies

### Python (standard library only for v1)
- `json` — API responses
- `csv` — data export
- `sqlite3` — database
- `urllib` — HTTP requests (no requests library needed)
- `datetime` — timestamps
- `os`, `sys`, `time` — utilities

### Optional (for better ML later)
- `scikit-learn` — Gradient Boosting, Random Forest
- `numpy` — numerical operations
- `pandas` — data manipulation
- `streamlit` — web dashboard (later)

### Infrastructure
- This server (4 cores, 8GB RAM) — sufficient for SQLite + scraper
- Etsy API key — already have
- Cron job — daily scraper
- Git — version control for code + data

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| Etsy API rate limit changes | Scraper slows down | Already batch 100/call, only use 15% of daily budget |
| Etsy API terms restrict analytics | Can't use API for this purpose | Use Commercial Access route, be transparent about purpose |
| Koalanda/eRank improve free tier | Our tool less differentiated | Our edge is time series + calibration, not features |
| EverBee goes free | Competitive pressure | We're already free — our edge is the data |
| Seller CSV adoption is slow | Less calibration data | Make the free dashboard valuable enough that uploading is worth it |
| Time series takes 12+ months to be useful | Slow to demonstrate value | Use 10K dataset for immediate ML, time series compounds over time |

---

## Success Metrics

| Metric | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|----------|
| Daily snapshots | 450 | 900 | 1,800 |
| Tracked keywords | 15 | 50 | 200 |
| Estimated listings in DB | 50,000 | 200,000 | 1,000,000 |
| Tool users | 10 | 100 | 1,000 |
| Seller CSV uploads | 0 | 10 | 50 |
| Estimation R² | 0.50 | 0.65 | 0.75 |
| Etsy shop revenue | £500 | £5,000 | £50,000 |
| Tool revenue | £0 | £500 | £10,000 |

---

## Next Steps (This Week)

1. **Set up cron job** — run `scrape.py` daily at 6am UTC
2. **Extend etsy-oracle** — add our estimation algorithm
3. **Build the dashboard** — even a simple Streamlit one-page view
4. **Run the 10K model** — train GBM on the full dataset
5. **Start the blog** — "Building a Free Etsy Research Tool: Day 1"
6. **List Game Winner** — first 5-8 listings on Etsy

---

*The thesis is simple: EverBee built a $69/mo business on estimation. We build the same thing free, calibrate it against real data, and prove it works by being a profitable Etsy seller ourselves. Time is the moat. Start accumulating data today.*
