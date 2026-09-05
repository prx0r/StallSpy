# StallShark

**Commerce Trajectory Corpus** — a machine-readable record of building AI-native commerce businesses from hypothesis through real economic outcomes.

---

## What This Repo Is

StallShark is the operating record for an experiment: can one person use AI, public data and automation to repeatedly discover, build and scale profitable microbrands?

Dogcasso is Experiment 001. Game Winner is Experiment 002. The corpus is the primary asset.

---

## Directory Structure

```
StallShark/
│
├── AGENTS.md                    ← START HERE
├── README.md                    ← this file
│
├── dogcasso-ops/                ← LIVE BUSINESS DATA
│   ├── days/                    ← CompanyDay records
│   ├── states/                  ← StateSnapshots
│   ├── perspectives/            ← Human/Agent/Blind reviews
│   ├── sessions/                ← OpenCode session metadata
│   ├── decisions/               ← Decision records
│   ├── problems/                ← Problem registry
│   ├── experiments/             ← Active experiments
│   ├── economic_events/         ← Financial transactions
│   └── snapshots/               ← Market snapshots
│
├── corpus/                      ← ARCHITECTURE SPECS
│   ├── machinecourse.md         ← 18 schemas (reference)
│   ├── CORPUS_THESIS.md         ← Business case
│   ├── OPERATOR_TWIN.md         ← Dual model (human + critic)
│   ├── METAMANAGEMENT.md        ← Adaptive interview protocol
│   ├── TRAJECTORY_CAPTURE.md    ← Lossless experience pyramid
│   ├── DAILY_RITUAL.md          ← Daily operating loop
│   ├── HUMAN_NOTE.md            ← 6 missing variables
│   ├── FEELINGS_DATASET.md      ← Agent-human meta-signals
│   ├── INTEGRATION.md           ← WorkerKit ↔ corpus bridge
│   ├── MOLTWORK_INTEGRATION.md  ← CompanyDay + BATS + ColdReview
│   ├── OPERATING_SYSTEM.md      ← Human–Agent OS
│   ├── PROMPT_ARCHIVE.md        ← Language as training data
│   ├── FRONTIER_RESEARCH.md     ← CEO-Bench, AI Co-Scientist
│   ├── ENDGAME.md               ← $5/day agent, operator twin
│   ├── ADAPTIVE_PROTOCOL.md     ← 18 question objectives
│   ├── DAILY_QUESTIONS.md       ← 12 evidence-based questions
│   └── DAILY_RITUAL.md          ← Morning → work → evening
│
├── endgame/                     ← PLANNING DOCS
│   ├── PROJECT_SEPARATION.md    ← Stop endgame eating experiment
│   ├── OPERATIONAL_PLAN.md      ← 8 schemas, daily process
│   ├── DEVPLAN.md               ← Full implementation brief
│   ├── COMMERCE_LABORATORY.md   ← Multi-marketplace benchmark
│   └── metaplan.md              ← What actually matters
│
├── tool/                        ← AUTOMATION + SCHEMAS
│   ├── stallshark_schemas.py    ← 8 core schemas (Pydantic)
│   ├── stallspy_cli.py          ← CLI (day/decision/experiment)
│   ├── problem_registry.py      ← Problem tracking
│   ├── etsy_snapshot.py         ← Live Etsy API scraper
│   ├── daily_content.py         ← Git + Etsy → content
│   ├── auto_content.py          ← Full pipeline + R2 backup
│   ├── morning_record.py        ← Morning belief state
│   ├── log_expense.py           ← Expense tracker
│   ├── cold_review.py           ← Blind review protocol
│   ├── opencode_llm.py          ← mimo-v2.5 adapter
│   ├── kernel.py                ← Hardened ledger + CompanyDay
│   ├── book_schemas.py          ← Full schema library
│   ├── stallspy_system.py       ← PydanticAI integration
│   ├── ml/                      ← ML repos (12 cloned)
│   └── r2_imports/              ← 49 platinum renderers
│
├── brands/                      ← BRAND STRATEGY
│   ├── dogcasso/                ← Pet studio (16 docs)
│   └── gamewinner/              ← Sports fantasy (2 docs)
│
├── content/                     ← CONTENT STRATEGY
│   ├── MASTER_PLAN.md           ← £0 → £1M experiment
│   ├── CONTENT_SPEC.md          ← YouTube/blog automation
│   ├── PORTFOLIO_SPEC.md        ← 20-store strategy
│   └── ... (9 docs)
│
├── product/                     ← PRODUCT ARCHITECTURE
│   ├── PRODUCT_ARCHITECTURE.md
│   ├── TECH_STACK.md
│   └── ... (8 docs)
│
├── research/                    ← MARKET RESEARCH
│   ├── CANONICAL_RESOURCE.md    ← Etsy tooling landscape
│   ├── GOLD_IDEAS.md            ← Strategic insights
│   └── ... (5 docs)
│
├── tools/                       ← CLONED MCP SERVERS (7)
│
└── data/                        ← LOCAL DATABASES
    └── ledger.db               ← SQLite event ledger
```

---

## Quick Start for a New Agent

### 1. Read these first

```bash
cat AGENTS.md              # Operating rules
cat endgame/OPERATIONAL_PLAN.md  # What we're building
cat endgame/PROJECT_SEPARATION.md  # What NOT to build
```

### 2. Check current state

```bash
python3 tool/stallspy_cli.py day status     # What's happening
python3 tool/problem_registry.py list       # What's broken
ls dogcasso-ops/days/                        # Day records
```

### 3. Understand the schemas

```bash
python3 tool/stallshark_schemas.py          # Test all 8 schemas
cat corpus/machinecourse.md                  # Full 18-schema reference
```

### 4. Export OpenCode session

```bash
opencode session list                       # See sessions
opencode export <sessionID> --sanitize      # Export as JSON
```

### 5. Run daily workflow

```bash
python3 tool/stallspy_cli.py day start      # Start day
# ... work ...
python3 tool/stallspy_cli.py day report     # Daily summary
python3 tool/stallspy_cli.py day close      # Close + handover
```

---

## What NOT to Build

Read `endgame/PROJECT_SEPARATION.md`.

The freeze list until 20 paid orders or 30 days data:
- New generalized databases
- New graph abstractions
- New agent runtimes
- Amazon/eBay
- Complex Arenav2 work
- Fine-tuning
- Multi-company hierarchies

**Priority: DOGCASSO > OPS/BOOK > RADAR > LAB/GYM.**

---

## File Count

| Area | Files | Purpose |
|------|------:|---------|
| dogcasso-ops/ | 18 | Live business data (8 schemas) |
| corpus/ | 17 | Architecture specs |
| endgame/ | 5 | Planning docs |
| tool/ | 17 scripts + 12 ML repos + 49 renderers | Automation |
| brands/ | 21 | Brand strategy |
| content/ | 9 | Content strategy |
| product/ | 8 | Product architecture |
| research/ | 5 | Market research |
| tools/ | 7 | Cloned MCP servers |
| **Total** | **~100 authored + 9K cloned** | |
