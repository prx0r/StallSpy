# Synthesis — Where Everything Converges

**Date:** 5 September 2026

---

## The Three Repositories

```text
private-lab (qdw-workbench)
    = canonical company kernel
    = ledger, artifacts, contracts, experiments, budgets, capabilities
    = the "operating system" for any economic agent

StallSpy (this repo)
    = Etsy/Dogcasso domain implementation
    = the first "world" running on private-lab
    = the corpus that trains operator models

finalbuilds2
    = donor + product-building intelligence
    = receipts, attribution, reconciliation, autonomy policy
    = concepts to port, not code to fork
```

The non-negotiable rule:

> **Domain-specific facts belong in StallSpy. Universal company machinery belongs in private-lab.**

Do not create a second ledger, second experiment framework, second worker registry, or second memory store inside StallSpy.

---

## What StallSpy Has Built (September 5, 2026)

### The Corpus Architecture (13 specs, 6,408+ lines)

| Spec | Lines | Purpose |
|------|------:|---------|
| `CORPUS_THESIS.md` | 354 | Business case, licensing, killer demo |
| `machinecourse.md` | 780 | 18 schemas, full architecture |
| `TRAJECTORY_CAPTURE.md` | 362 | Lossless experience pyramid |
| `DAILY_RITUAL.md` | 215 | Morning → work → evening → extraction |
| `HUMAN_NOTE.md` | 226 | 6 missing variables, voice > typing |
| `DAILY_QUESTIONS.md` | 314 | 12 evidence-based questions |
| `METAMANAGEMENT.md` | 353 | 18 question objectives, adaptive interview |
| `OPERATOR_TWIN.md` | 1,030 | Dual model, autonomy passport, RL environment |
| `INTEGRATION.md` | 579 | WorkerKit ↔ corpus bridge |
| `MOLTWORK_INTEGRATION.md` | 828 | CompanyDay, BATS, ColdReview, token telemetry |
| `FEELINGS_DATASET.md` | 406 | Feelings → protocols → corporation |
| `FRONTIER_RESEARCH.md` | 307 | CEO-Bench, AI Co-Scientist, ForecastBook |
| `PROMPT_ARCHIVE.md` | 284 | Human language as operator model training data |
| `OPERATING_SYSTEM.md` | 307 | Human–Agent Operating System |
| `ENDGAME.md` | 434 | $5/day agent, operator twin buildable now |

### The Working System (16/16 E2E PASS)

| Component | Status | Evidence |
|-----------|--------|----------|
| Event ledger | ✓ | SQLite, append-only, hash chain, 53+ events |
| SubjectiveState | ✓ | 25 fields, Pydantic validated |
| PydanticAI agents | ✓ | Agent + output_type validated |
| Operator Twin | ✓ | mimo-v2.5 produces real predictions |
| Economic Critic | ✓ | Independent recommendations |
| Cold Reviewer | ✓ | Blind protocol, interpretations hidden |
| Interview Agent | ✓ | Generates high-value questions |
| Memory extraction | ✓ | PAHF-style, SQLite storage |
| Token tracking | ✓ | Per model, per task, per day |
| Problem registry | ✓ | 18 problems registered |
| Divergence calculator | ✓ | P/A/H comparison |
| Content engine | ✓ | Git + Etsy API → daily log/video/TL;DR |
| Etsy API | ✓ | Live, 584K results |
| R2 backup | ✓ | Connected, 4 files |
| Morning record | ✓ | Belief state capture |
| Ledger integrity | ✓ | Hash chain verified |

### The Endgame Architecture

| Doc | What It Defines |
|-----|----------------|
| `DEVPLAN.md` | StallShark rename, eBay as primary gym, UCI/Olist/Retailrocket, 15 weekly actions |
| `COMMERCE_LABORATORY.md` | Multi-marketplace agent benchmark, cross-market transfer |
| `moredev.txt` | Full implementation brief (43 sections) from private-lab integration |

---

## What private-lab Has

| Component | Status | Lines |
|-----------|--------|------:|
| Contracts (41 types) | Working | 585 |
| Event Ledger | Working | 366 |
| Artifact Store | Working | 153 |
| Context Compiler | Working | 186 |
| Budget Allocator (Thompson) | Working | 149 |
| Worker Registry | Working | 212 |
| Pool Matcher | Working | 180 |
| Evaluation (multi-dim) | Working | 247 |
| Curriculum Engine | Working | 246 |
| Lab Controller | Working | 242 |
| Hydra Projector | Working | 225 |
| Metaculus Studio | Working | 175 |
| Rust qdw-node | Working | Git, sessions, handover |

### What private-lab needs (from the implementation brief)

1. **Ledger: make append transactional** (BEGIN IMMEDIATE)
2. **Fix event ID semantics** (UUIDv7 or explicit time-sortable)
3. **Make Hydra projection pure** (never creates ledger events)
4. **All state changes ledger-first**
5. **Preserve published contract compatibility** (v2 adapters, not destructive renames)
6. **Add universal Company contracts** (CompanyDay, ActorAssessment, etc.)
7. **WorldExperiment** (separate from CapabilityExperiment)
8. **Information-boundary contracts** (blind review enforcement)
9. **Reconciliation abstraction** (drift detection → Problem)
10. **Autonomy policy** (R0-R3 risk classes)

---

## The Convergence Map

```text
                    PRIVATE-LAB
               Canonical Company Kernel
                         │
         ┌───────────────┼────────────────────┐
         │               │                    │
       Truth          Cognition            Learning
         │               │                    │
      Ledger          PydanticAI         Experiments
      Artifacts        Workers            Attribution
      Git              Context            Reconciliation
      Receipts         Capabilities       Allocation
         │               │                    │
         └───────────────┼────────────────────┘
                         │
                    STALLSPY WORLD
                         │
            ┌────────────┼─────────────────┐
            │            │                 │
         Etsy API     Research         Dogcasso
         Webhooks     EverBee          Templates
         Orders       Signals          Renders
         Reviews                       Fulfillment
            │            │                 │
            └────────────┼─────────────────┘
                         │
                  ECONOMIC OUTCOMES
                         │
                         ▼
                    PRIVATE-LAB
                    (evaluates)
                         │
                         ▼
                    MWGYM / ARENAV2
                    (historical replay / tournaments)
                         │
                         ▼
                    OPERATOR MEMORY
                    (improves Moltwork)
```

---

## The Daily Operating Loop (StallSpy-specific)

```text
00  FREEZE STATE        → BusinessSnapshot
01  MORNING RECORD      → OperatorState (human)
02  AGENT PREDICTION    → OperatorTwin (mimo-v2.5)
03  ECONOMIC CRITIQUE   → EconomicCritic (mimo-v2.5)
04  DIVERGENCE          → Compare P/A/H
05  PROBLEM SELECTION   → Highest-value unresolved problem
06  HYPOTHESIS          → What would fix it
07  BATS ALLOCATION     → Budget envelope
08  EXECUTION           → WorkerKit / OpenCode
09  WORKER DEBRIEF      → Same-context reflection
10  HUMAN CLOSE         → Evening voice/note
11  COLD REVIEW         → Blind fresh agent
12  RECONCILE           → Three perspectives
13  LEARN               → Hydra candidates
14  PUBLISH             → Blog + Short
15  OUTCOMES            → 1d/7d/30d results attached
16  PROMOTE             → Validated knowledge enters memory
```

---

## The Key Technical Decisions Made

1. **PydanticAI + opencode mimo-v2.5** for agent execution (not Letta)
2. **SQLite ledger** for event storage (not Postgres as canonical)
3. **Test model fallback** when API unavailable
4. **Dict-based agent outputs** (not Pydantic models) for opencode compatibility
5. **Separate CapabilityExperiment vs WorldExperiment** (not overloaded)
6. **Information-boundary enforcement** via context compilation, not prompting
7. **Etsy as live world, eBay as historical gym** (not interchangeable)
8. **MarketWorld schema** as the universal abstraction
9. **StallShark > StallSpy** (brand rename, StallSpy becomes feature name)
10. **$5/day agent budget** with smart routing

---

## What Blocks Progress

| Blocker | Impact | Solution |
|---------|--------|----------|
| OpenCode API returns plain text | Agents produce test defaults | Use opencode run adapter (working) |
| private-lab kernel not hardened | Ledger/contract bugs | Fix 5 invariants per implementation brief |
| No real Etsy shop live | Zero market feedback | Launch Game Winner first 5 listings |
| No eBay world | No historical gym | Build ebay-world against Product Research |
| No daily cron | No time series accumulation | Set up midnight scraper |
| TokenWise not integrated | No task decomposition | Wire into BATS |

---

## The Immediate Priority

From the implementation brief, the **highest-value first coding pass** is:

> Fix the three private-lab kernel invariants — transactional ledger append, pure Hydra rebuild, ledger-first controller — then implementing the replay-mode CompanyDay vertical slice.

Once that passes, plugging the real Etsy API becomes mechanical.

---

## The Dataset That Matters

After 1 year:

```text
365 CompanyDays
1,000+ ActorAssessments (human + agent + cold reviewer)
500+ Problems
200+ Hypotheses
100+ Experiments
50+ validated Lessons
10,000+ token usage records
50+ MarketplaceDecisionTrajectories
complete prompt archive
complete operator model training data
```

This is not an Etsy analytics tool.

This is **a longitudinal record of AI-assisted entrepreneurship from Day 0** — what was believed, what was tried, what it cost, what happened, and what was learned.

That dataset is the product.

---

*The repos are separate. The contracts are shared. The learning compounds. The company is the experiment.*
