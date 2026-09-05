# StallSpy

**Commerce Trajectory Corpus v1** — a replayable, machine-readable record of taking AI-native commerce businesses from hypothesis → launch → optimization → scale.

---

## Structure

```text
StallSpy/
├── corpus/                  # Corpus architecture (the primary asset)
│   ├── CORPUS_THESIS.md     # Business case, licensing, killer demo
│   ├── machinecourse.md     # 18 schemas, architecture, directory
│   ├── TRAJECTORY_CAPTURE.md # Lossless pyramid, step labels
│   ├── DAILY_RITUAL.md      # Morning belief → work → evening → extraction
│   ├── HUMAN_NOTE.md        # Operator state, 6 missing variables
│   └── DAILY_QUESTIONS.md   # 12 evidence-based daily questions
│
├── brands/                  # Brand/store strategy
│   ├── dogcasso/            # Pet studio (core brand)
│   ├── gamewinner/          # Sports fantasy (challenger)
│   ├── greatest_hits/       # Album studio (planned)
│   ├── storystar/           # Kids books (planned)
│   └── cover_story/         # Magazine covers (planned)
│
├── product/                 # Product architecture
│   ├── PRODUCT_ARCHITECTURE.md
│   ├── TECH_STACK.md
│   ├── FULFILLMENT.md
│   └── ... (UX, pricing, flow)
│
├── content/                 # Content strategy
│   ├── MASTER_PLAN.md       # £0 → £1M experiment
│   ├── CONTENT_SPEC.md      # YouTube/blog automation
│   ├── PORTFOLIO_SPEC.md    # 20-store strategy
│   └── ... (ads, customers, retention)
│
├── research/                # Market research & tools
│   ├── CANONICAL_RESOURCE.md # Etsy tooling landscape
│   ├── MARKET_RESEARCH.md
│   └── tool_registry.json
│
├── operations/              # Daily operations
│   ├── logs/                # Daily generated content
│   ├── voice_notes/         # Human reflections
│   ├── expenses.jsonl       # Financial tracking
│   └── ledger.jsonl         # Machine-readable daily entries
│
├── tool/                    # Automation scripts
│   ├── daily_content.py     # Git + Etsy → log, video, TL;DR
│   ├── auto_content.py      # Full pipeline + R2 backup
│   ├── morning_record.py    # Daily belief state
│   ├── log_expense.py       # Expense tracker
│   ├── scrape.py            # Etsy API scraper
│   ├── ml/                  # ML repos + models
│   └── r2_imports/          # 49 platinum video renderers
│
└── tools/                   # Cloned MCP servers (7 Etsy APIs)
```

---

## Quick Start

```bash
# Day 1: Morning record
python3 tool/morning_record.py 1 "Get listing live" "Birthday converts" "Test 50th variant" "2x favorites" "0 after 48h"

# Log expenses
python3 tool/log_expense.py 8.13 gpu "H3 generation test"

# End of day: generate content + backup
python3 tool/auto_content.py --day 1 --backup

# View today
cat operations/logs/2026-09-05_tldr.md
```

---

## What This Is

Not an Etsy course. Not a dropshipping guide.

A **machine-readable operating history** of building AI-native consumer brands from scratch. The corpus is the product. The stores are the environment that generates it.

**The key insight:** Noise is a retrieval problem, not a storage problem. Store everything. Let future agents find the signal.
