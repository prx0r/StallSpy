# z2m — Zero to Million

**$0 → $1,000,000 in 90 days.**

---

## Structure

```
z2m/
├── README.md                 ← you are here
├── TRACKER.md                ← daily progress
│
├── strategy/                 ← business strategy & positioning
│   ├── STRATEGY.md           ← AI-native premium commerce thesis
│   ├── gameplan.md           ← Google Ads dropshipping gameplan
│   ├── AUTONOMOUS-PIPELINE.md ← workerkit integration
│   ├── geocommerce-thesis.md ← GeoCommerce OS
│   └── etsy-strat.md         ← 100-shop Etsy analysis
│
├── research/                 ← market intelligence & analysis
│   ├── reddit-pain/          ← 12 themes, 159 reports
│   ├── pain-points-analysis.json ← structured pain data
│   ├── ecom-strategists.md   ← 10 sharp channels
│   ├── the-angles.md         ← 7 money angles
│   ├── free-tools.md         ← zero-cost tool stack
│   └── ... (intel reports)
│
├── products/                 ← product ideas & implementations
│   ├── selling-to-idiots/    ← personalized digital products
│   ├── one-click-personalization.md
│   ├── products-for-founders.md
│   └── digital-product-opportunities.md
│
├── data/                     ← databases, tools, scanners
│   ├── opportunities.db      ← unified SQLite (370 opps)
│   ├── daily_scanner.py      ← runs all engines
│   ├── pricing_calculator.py ← full economics
│   ├── merchant_feeds.py     ← Google Merchant XML
│   └── ... (more tools)
│
├── imports/                  ← raw imports from email (18 ZIPs)
│   ├── INVENTORY.md
│   ├── LAB-RESULTS.md
│   └── ... (engines, codebases)
│
├── tools/                    ← cloned repos
│   ├── global-ecommerce-intelligence/
│   ├── ecommerce-dtc-skills/
│   └── dropshipping-product-scout/
│
└── transcripts/              ← video transcripts
```

---

## What We Have

| Category | Count | Key Items |
|----------|:-----:|-----------|
| Strategy docs | 5 | GeoCommerce, gameplan, etsy, pipeline |
| Research reports | 159 | Reddit pain, money radar, agent scout |
| Pain themes | 12 | Lead speed, missed calls, invoices, etc. |
| Product ideas | 3 | Personalization, founders, digital products |
| Imported ZIPs | 18 | Full codebases, engines, research |
| Scanners | 3 | Q4 Radar, Gift Engine, Nordic Scanner |
| Databases | 370 | Unified opportunities in SQLite |
| Free tools | 10+ | eRank, PPSPY, Google, MCP servers |
| Market analysis | 7 | Etsy, Google, Nordic, Pinterest |

---

## The Flywheel

```
REDDIT PAIN (what people complain about)
    ↓
THEMES (recurring patterns)
    ↓
PRODUCTS (solutions)
    ↓
IMPORTS (codebases to build from)
    ↓
STRATEGY (positioning & pricing)
    ↓
DATA (scanners, economics, feeds)
    ↓
EXECUTION (stores, ads, revenue)
    ↓
RESEARCH (what worked, what failed)
    ↓
back to REDDIT PAIN
```

---

## Quick Commands

```bash
# Run all scanners
python3 data/daily_scanner.py

# Generate specs
python3 data/generate_specs.py

# Generate merchant feeds
python3 data/merchant_feeds.py

# Calculate pricing
python3 data/pricing_calculator.py

# Query opportunities
sqlite3 data/opportunities.db "SELECT product_name, market, score FROM opportunities WHERE score > 80 ORDER BY score DESC LIMIT 10;"
```
