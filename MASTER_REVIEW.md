# StallShark — Master Review & Research Synthesis

**Date:** 5 September 2026
**Session:** Day 0 — Architecture, Research, Integration

---

## Executive Summary

This session produced:

1. **A corpus architecture** for recording AI-native commerce from $0 to £1M
2. **An adaptive metamanagement protocol** with 18 question objectives
3. **A dual-model operator twin** (human prediction + economic critic)
4. **Integration with WorkerKit** (BATS budgets, cost tracking, capabilities)
5. **49 platinum video renderers** imported from Cloudflare R2
6. **Live Etsy API data** confirming zero competition in personalized video gifts
7. **12 evidence-based daily questions** from entrepreneurship research
8. **A meta-protocol** with 15 daily phases including blind fresh-agent review

---

## Part 1: The Business Thesis

### Core Concept

> Can one person use AI, public data and automation to repeatedly discover, build and scale profitable microbrands from almost no starting capital?

**Key file:** `corpus/CORPUS_THESIS.md`

### The Flywheel

```
Build stores → Content → Audience → Sales → Validation → More content → More audience
```

**Key file:** `content/MASTER_PLAN.md`

### 20-Store Portfolio

| Tier | Studios | Strategy |
|------|---------|----------|
| Build now | GameWinnerz, MythicBee, Greatest Hits, StoryStar, Cover Story | Dedicated shops |
| Graduate if validated | Arcana, Legend Cards, Wanted, TrailerMade, etc. | Shared engine |
| Viral laboratories | MemeMint, Cerealized, Natural Habitat | Experiment |

**Key file:** `content/PORTFOLIO_SPEC.md`

### The Promotion System

```
Idea → Validated Template → Commercial Mockup → Specialist Store → Data-Driven Promote/Kill
```

**Key file:** `content/PORTFOLIO_SPEC.md` (Section: The Promotion System)

### Economics (Prodigi Manufacturing Costs)

| Product | Cost | Retail | Margin |
|---------|------|--------|--------|
| Sticker | £0.80 | £4.99 | ~84% |
| Greeting card | £1.10 | £5.99 | ~82% |
| Budget poster | £3.00 | £14.99 | ~80% |
| Photo mug | £3.64 | £17.99 | ~80% |
| Magazine | £3.75 | £19.99 | ~81% |
| Softcover book | £6.50 | £24.99 | ~74% |

**Key file:** `content/PORTFOLIO_SPEC.md` (Section: Physical Economics)

---

## Part 2: Etsy SEO Research

### Live API Findings

**Key file:** `brands/gamewinner/GAMEWINNER_SEO_STRATEGY.md`

| Search Query | Results | Actual Video Gifts? | Gap |
|-------------|---------|-------------------|-----|
| `personalized football video gift` | 339 | **ZERO** | HUGE |
| `scored winning goal gift` | 4 | **ZERO** | HUGE |
| `personalized birthday video gift for dad` | 642 | **ZERO** | HUGE |
| `custom football movie gift` | 146 | **ZERO** | HUGE |

**Conclusion:** Game Winner enters a category with ZERO direct competition on Etsy.

### 13-Tag Strategy (Refined from Live Data)

```
1. personalized football
2. custom video gift
3. football gift for dad
4. birthday movie for him
5. sports video gift
6. funny football gift
7. gift for husband
8. scored the winning
9. personalized sports
10. fathers day football
11. custom birthday movie
12. football present for
13. soccer gift for dad
```

Uses both `football` (UK) + `soccer` (US) in same listing.

### Title Formula

```
Product Type + Personalization + Occasion + Recipient
```

Example: `Personalized Football Video Gift | Dad Scores The Winning Goal | Custom Birthday Movie`

### Seasonal Calendar

| Period | Focus | Tags |
|--------|-------|------|
| Apr-May | Father's Day | `fathers day gift`, `graduation gift` |
| Oct-Dec | Christmas | `christmas gift for dad`, `xmas football gift` |
| Year-round | Birthdays | `birthday gift`, `birthday present for dad` |

**Key file:** `brands/gamewinner/GAMEWINNER_SEO_STRATEGY.md` (Section: Seasonal Calendar)

---

## Part 3: The Corpus Architecture

### The Lossless Experience Pyramid

```
L5  Transfer Packs    — "Launch a jewellery brand"
L4  Principles         — "Occasion intent beats novelty"
L3  Episodes           — state → belief → action → result
L2  Semantic Session   — goals / decisions / discoveries
L1  Agent Trace        — turns / tool calls / diffs
L0  Raw Evidence       — complete OpenCode JSON, never deleted
```

**Key file:** `corpus/TRAJECTORY_CAPTURE.md`

### 18 Record Schemas

| Schema | Purpose |
|--------|---------|
| `episode` | STATE → GOAL → BELIEF → ACTION → OUTCOME → UPDATED BELIEF |
| `business_state_snapshot` | Daily state for time-travel |
| `hypothesis` | Never retrospectively invented |
| `decision` | With `information_cutoff_at` |
| `action` | Every meaningful intervention |
| `experiment` | A/B tests + smoke tests + qualitative |
| `metric_definition` + `metric_point` | Never silently change definitions |
| `financial_transaction` | Track cash, not influencer maths |
| `generation_run` | Production IP for the factory |
| `listing_revision` | Every revision, not just current |
| `product_template` | Actual production IP |
| `customer_feedback` | PII-safe |
| `observation` | Not everything is a metric |
| `lesson` | Derived, with invalidation conditions |
| `playbook` | Actionable distilled procedures |
| `brand_candidate` | Promotion strategy becomes learnable |
| `agent_run` | StallShark logs its own behavior |
| `eval_case` | Benchmark agents against historical operator |

**Key file:** `corpus/machinecourse.md`

### The Record Envelope

Every record gets: `id`, `schema`, `occurred_at`, `observed_at`, `recorded_at`, `project_id`, `actor`, `correlation_id`, `source`, `provenance`, `rights`, `quality`, `data`.

**Never modify historical events.** Corrections: new event → supersedes_id → old event.

**Key file:** `corpus/machinecourse.md` (Section: The Record Envelope)

---

## Part 4: The Metamanagement Protocol

### 18 Question Objectives

| # | Question Objective | Purpose |
|---|-------------------|---------|
| 1 | Objective Hierarchy | What are we optimizing across horizons? |
| 2 | Bottleneck Identification | What constrains progress most? |
| 3 | Uncertainty | Highest expected value of information? |
| 4 | Belief State | What claims does operator believe? |
| 5 | Evidence Update | What observation should modify beliefs? |
| 6 | Action Selection | Highest expected value action now? |
| 7 | Counterfactual | Strongest alternative action? |
| 8 | Opportunity Cost | What are we sacrificing? |
| 9 | Affordable Loss | How much can we lose while learning? |
| 10 | Falsification | What evidence would make us stop? |
| 11 | Risk / Premortem | How is this most likely to fail? |
| 12 | Hidden Signal | What human notices not in metrics? |
| 13 | Strategy Validity | Are we solving the correct problem? |
| 14 | Automation Boundary | What requires human judgment? |
| 15 | Portfolio Allocation | Which brand gets next unit of time/capital? |
| 16 | Recurring Problems | Something structurally similar before? |
| 17 | Reversibility | Cheap to undo or high evidence bar? |
| 18 | Exploit vs Explore | Improve winner or test something new? |

### Scoring Formula

```
Question value =
    uncertainty × decision_relevance × human_informational_advantage
    × consequence_magnitude × temporal_urgency ÷ interview_burden
```

**Key file:** `corpus/METAMANAGEMENT.md`

---

## Part 5: The Human Note

### Six Missing Variables

| # | Variable | Why It Matters |
|---|----------|---------------|
| 1 | Belief state | Prediction → result, not hindsight |
| 2 | Uncertainty | Where uncertainty existed and how it resolved |
| 3 | Motivation | Why this action over alternatives |
| 4 | Constraints | What wasn't available |
| 5 | Counterfactuals | The branch you didn't take |
| 6 | Intuition | Weak signals before quantification |

**Voice > typing.** Hesitations are information. "I dunno, this feels weird because…" captures preference signals that never appear in Git or metrics.

**Key file:** `corpus/HUMAN_NOTE.md`

---

## Part 6: The Operator Twin

### Dual Model Architecture

```
OPERATOR_MODEL    — predicts what Tom would do
ECONOMIC_CRITIC   — predicts what the business needs
```

Otherwise you merely manufacture an AI that faithfully reproduces all your mistakes.

### Three Answers Per Question

```
P — Predicted Human: "What I think Tom will say"
A — Agent's Own Judgment: "What I think should be done"
H — Actual Human: "What Tom actually says"
```

**P ↔ H** = operator-model accuracy
**A ↔ outcome** = agent decision quality
**H ↔ outcome** = human decision quality

### Six Operational Levels

| Level | Name | What It Can Do |
|-------|------|---------------|
| L0 | Recorder | Only observes |
| L1 | Shadow Twin | Predicts everything, never acts |
| L2 | Adviser | Independent recommendation, human decides |
| L3 | Delegated Reversible | Research, drafts, experiments |
| L4 | Bounded Operator | Update listings, spend under caps |
| L5 | Brand Manager | Grow brand subject to budget |

### Autonomy Passport

Earn autonomy per decision class, not globally. Track: twin accuracy, outcome quality, risk, override rate, rollback rate.

**Key file:** `corpus/OPERATOR_TWIN.md`

---

## Part 7: The 15-Phase Daily Protocol

| Phase | Artifact | Purpose |
|-------|----------|---------|
| 00 | BusinessSnapshot | Exact world before decisions |
| 01 | OperatorState | Human latent policy |
| 02 | AgentState | Independent agent judgment |
| 03 | OperatorPrediction | Predict human before reveal |
| 04 | DecisionManifest | Resolve divergence |
| 05 | WorkOrders + BudgetEnvelopes | Commit objectives/resources |
| 06 | WorkerRuns | Agents do actual work |
| 07 | RunReceipts | Actions, tools, tokens, cash, time |
| 08 | WorkerDebrief | Same-context reflection |
| 09 | OperatorReflection | Same-day human interpretation |
| 10 | ColdReview | Blind independent review |
| 11 | DayReview | Three perspectives reconciled |
| 12 | HydraCandidates | Candidate lessons/skills |
| 13 | Publish | Blog + Short |
| 14 | OutcomeReceipt | 1d/7d/30d reality grades |
| 15 | PromotionReceipt | Validated knowledge enters memory |

**Key file:** `corpus/MOLTWORK_INTEGRATION.md`

---

## Part 8: The ColdReview Protocol

The freshness is the feature.

**Pass A — Evidence only:** Agent gets trajectories, actions, metrics. Does NOT see human reflection or worker debrief. Forms own assessment.

**Pass B — Reconciliation:** Reveal human + worker reflections. Ask: where do they agree? Where disagree? What experiment resolves?

**Result:** Three minds observing the same business:
- Human — taste, intuition, fear
- Working agent — contemporaneous beliefs
- Cold reviewer — independent interpretation
- Market — external reward

**Key file:** `corpus/MOLTWORK_INTEGRATION.md` (Section: ColdReview)

---

## Part 9: The Feelings Dataset

### The Pipeline

```
"worried about conversion" (feelings)
     ↓
BATS: $0 on marketing today (activity)
     ↓
Outcome: 0 sales, 0 reviews (result)
     ↓
Hypothesis → Experiment → Protocol stored
```

### Tunable Aggression

```
operator_risk_preference: 0.42
low_sales_week → pushes to 0.55 (more aggressive)
recent_failure → pushes to 0.30 (more cautious)
```

### Problem → Experiment → Protocol

```
IDENTIFY → RESEARCH → HYPOTHESIZE → EXPERIMENT → MEASURE → STORE
```

Stored protocols become the company's operating manual, written by its own experience.

**Key file:** `corpus/FEELINGS_DATASET.md`

---

## Part 10: WorkerKit Integration

### What Works Today

| Component | Status | Can Use |
|-----------|--------|:-------:|
| Event Ledger | SQLite, hash chain | Yes |
| BATS | Free→cheap→strong routing | Yes |
| Cost Model | Historical benchmarking | Yes |
| Decision Engine | Marginal economics | Yes |
| Capabilities | Multi-dimensional evidence | Yes |
| WorkerAsset | 9 valuation dimensions | Yes |
| Metaculus Venue | Full API (discover/submit/status) | Yes |
| SDK | start→verify→gate→close | Yes |
| CG Evolution | 14 recipes, 33 reasoning styles | Yes |
| CGE Scoring | Peer review, MAP-Elites | Yes |

### Key WorkerKit Files

| File | Lines | What |
|------|------:|------|
| `core/schema.py` | 312 | 12 frozen dataclasses (canonical records) |
| `core/events.py` | 101 | Append-only SQLite event ledger |
| `core/hashing.py` | 97 | RFC 8785 JCS + SHA-256 |
| `core/worker_asset.py` | 287 | Complete business asset primitive |
| `economics/budgets.py` | 17 | BATS budget enforcement |
| `economics/costs.py` | 48 | CostModel + RunMeter |
| `economics/decisions.py` | 36 | Continue/abort marginal economics |
| `providers/bats.py` | 112 | Budget-aware model routing |
| `providers/broker.py` | 139 | Inference routing (3 policies) |
| `capabilities.py` | 220 | Multi-dimensional capability evidence |
| `lab_kernel.py` | 508 | Full orchestration (needs Letta) |
| `venues/metaculus.py` | 224 | Full Metaculus API adapter |
| `flywheel/__init__.py` | 349 | Complete opportunity→submit loop |
| `cg/evolve.py` | 241 | Evolution lab with WorldPack |
| `evidence/log.py` | 141 | Append-only Merkle log |

### CG/CGE Status

| Repo | Tests | Status |
|------|-------|--------|
| `/root/cg` | 20/21 passing | 1 bug: missing import in toy.py |
| `/root/cge` | 54/54 passing | Fully functional |

### Key Integration Points

```
WorkerKit BATS → Corpus budget tracking
WorkerKit CostModel → Token spend per task
WorkerKit DecisionEngine → Episode decisions
WorkerKit Capabilities → Operator twin calibration
WorkerKit MetaculusVenue → First live commerce test
CG Evolution → Worker version comparison
CGE Scoring → Peer review of agent outputs
```

**Key file:** `corpus/INTEGRATION.md`

---

## Part 11: Research Findings

### What Predicts Venture Success

| Factor | Evidence | Source |
|--------|----------|--------|
| Lean startup practices | Strong predictor of seed valuation | Eisenmann HBS survey |
| Organizational effort | Strong predictor of survival | PSED longitudinal |
| Subjective startup probability | Strong predictor of survival | PSED longitudinal |
| Financial metrics confidence | Strong predictor of growth | Eisenmann HBS survey |
| Self-efficacy | +8% income, +8.8% employees | Caliendo et al. 2019 |
| Conscientiousness | Positive for funding, negative for exit | Freiberg & Matz 2023 |
| Neuroticism | Negative for all outcomes | Freiberg & Matz 2023 |
| Founder personality | Weak predictor vs business factors | Eisenmann HBS survey |

### Decision Journal Research

| Finding | Source |
|---------|--------|
| Record at decision time, not after | Duke, Dalio, Tetlock |
| Quantify confidence (70% not "pretty sure") | Tetlock superforecasters |
| "What would change my mind" is highest-value field | Tetlock, Duke |
| Review at 3+ months, not 3 days | Decision journal practitioners |
| Grade process, not outcome | Annie Duke |
| Keep entries <5 minutes | Journal practitioners |
| Same questions daily = calibration data | Longitudinal studies |

### Agent Trajectory Research

| Finding | Source |
|---------|--------|
| Failed runs contain useful steps | JetBrains Step Rejection 2026 |
| Critical failure step identification | Microsoft AgentRx |
| Failed trajectories valid for different goals | AgentHER |
| Memory/modules not always worth tokens | Budget-constrained web agents study |
| Episodic→semantic consolidation without identity drift | 2026 research |
| Personalized agents from human feedback | Meta AI 2026 |
| PersonaAgent: memory + action separation | ACL Anthology 2026 |
| Active preference-learning via uncertainty | ScienceDirect 2026 |

### BATS Research

| Finding | Source |
|---------|--------|
| Budget awareness changes explore/exploit behavior | arXiv 2511.17006 |
| More tool calls ≠ better performance | BATS study |
| Free→cheap→strong routing works | Our implementation |
| Token budget is a policy input, not just a constraint | BATS research |

---

## Part 12: Tools & Infrastructure

### Cloned & Working

| Tool | Path | Purpose |
|------|------|---------|
| aserper/etsy-mcp | `tools/aserper-etsy-mcp/` | 37 Etsy API tools |
| avlihachev/etsy-mcp-server | `tools/avlihachev-etsy-mcp-server/` | 2026 API tracking |
| alveyautomation/etsy-mcp | `tools/alveyautomation-etsy-mcp/` | Read-only, safest |
| etsy-oracle | `tool/ml/etsy-oracle/` | Open-source sales estimator |
| iscale-etsy | `tool/ml/iscale-etsy/` | Chrome extension, ranking history |
| etsy-sales-prediction | `tool/ml/etsy-sales-prediction/` | 10K shops dataset |
| etsy-Analysis-ML | `tool/ml/etsy-Analysis-ML/` | Random Forest + GB |

### Platinum Renderers (49 files)

All in `tool/r2_imports/platinum/`. Full PIL-based video generators, 30-50KB each, 40-59 functions. Create animated videos from Python code.

### Automation Scripts

| Script | Purpose |
|--------|---------|
| `tool/daily_content.py` | Git + Etsy API → log, video, TL;DR |
| `tool/auto_content.py` | Full pipeline + R2 backup |
| `tool/morning_record.py` | Daily belief state |
| `tool/log_expense.py` | Expense tracker |
| `tool/scrape.py` | Etsy API scraper |

### R2 Backup

All content backed up to `blog-video-assets/experiments/£0to1M/`

---

## Part 13: The Auto-Protocol

### Daily Loop

```
MORNING → belief + goal + planned experiment
DAY     → raw work / OpenCode / Git / commerce
EVENING → metrics + money + 60-sec reflection
NIGHTLY → structured corpus extraction
PUBLIC  → blog + Short + scoreboard
LATER   → 1d/7d/30d outcomes attached
```

### Weekly Synthesis

- One longer YouTube video
- Weekly research report
- Experiment leaderboard
- P&L
- Hypotheses supported/rejected
- Next week's bets

### The Key Operating Rule

> **The business comes first. Content records the business. Content must never become the business's main source of busywork.**

**Key file:** `corpus/DAILY_RITUAL.md`

---

## Part 14: What to Build First

### This Week

1. Set up cron job — run `scrape.py` daily
2. Wire token tracking into `daily_content.py`
3. Add budget readout to morning record
4. Create `agent_session_reflection` schema
5. Wire RunMeter to corpus events
6. First 5 Game Winner listings on Etsy

### Next Week

7. Meta-protocol agent — fresh agent reviews previous day
8. BATS↔corpus bridge — budget decisions reference historical ROI
9. First 14 days of P/A/H data for operator twin v0.1

### Month 2

10. HydraDB corpus graph
11. Competence map (human vs agent strengths)
12. Autonomy passport (earn per decision class)

---

## Part 15: The Endgame

```
WATCH ME
↓
PREDICT ME
↓
ADVISE ME
↓
DISAGREE WITH ME
↓
LEARN WHEN I'M RIGHT
↓
LEARN WHEN I'M WRONG
↓
ACT FOR ME IN FAMILIAR STATES
↓
ESCALATE NOVEL STATES
↓
EVENTUALLY OUTPERFORM ME
```

The system asks nightly:

> **What did today teach us about how to operate tomorrow, and is that lesson worth the tokens required to remember it?**

That turns the Etsy experiment into: **a longitudinal economic laboratory for learning how human–AI organizations should allocate cognition, memory, capital and autonomy.**

---

## File Index

### Corpus Specs (`corpus/`)

| File | Lines | Topic |
|------|------:|-------|
| `CORPUS_THESIS.md` | 354 | Business case, licensing, killer demo |
| `machinecourse.md` | 780 | 18 schemas, architecture, directory |
| `TRAJECTORY_CAPTURE.md` | 362 | Lossless pyramid, step labels |
| `DAILY_RITUAL.md` | 215 | Morning → work → evening → extraction |
| `HUMAN_NOTE.md` | 226 | 6 missing variables, voice > typing |
| `DAILY_QUESTIONS.md` | 314 | 12 evidence-based questions |
| `METAMANAGEMENT.md` | 353 | 18 question objectives, adaptive interview |
| `OPERATOR_TWIN.md` | 1,030 | Dual model, autonomy passport, RL environment |
| `INTEGRATION.md` | 579 | WorkerKit ↔ corpus bridge |
| `MOLTWORK_INTEGRATION.md` | 828 | CompanyDay, BATS, ColdReview |
| `FEELINGS_DATASET.md` | 406 | Feelings → protocols → corporation |

### Brand Specs (`brands/`)

| File | Topic |
|------|-------|
| `mythicbee/STRATEGY.md` | Moonpig thesis, flywheel |
| `mythicbee/BRAND.md` | Brand positioning |
| `mythicbee/ENGINES.md` | 8 generation engines |
| `gamewinner/GAMEWINNER_SEO_STRATEGY.md` | Live API SEO research |
| `gamewinners.md` | Store strategy, economics |

### Content & Product

| File | Topic |
|------|-------|
| `content/MASTER_PLAN.md` | £0 → £1M experiment |
| `content/CONTENT_SPEC.md` | YouTube/blog automation |
| `content/PORTFOLIO_SPEC.md` | 20-store strategy |
| `product/PRODUCT_ARCHITECTURE.md` | Tech stack, engines |
| `product/TECH_STACK.md` | Models, GPUs, costs |

### Tools & Data

| Path | What |
|------|------|
| `tool/daily_content.py` | Content engine |
| `tool/auto_content.py` | Full automation |
| `tool/scrape.py` | Etsy API scraper |
| `tool/r2_imports/platinum/` | 49 video renderers |
| `tool/ml/` | 7 ML repos + datasets |
| `tools/` | 7 Etsy MCP servers |

---

*This document is the single source of truth for what was researched, built, and decided on Day 0 of the £0 → £1M experiment.*
