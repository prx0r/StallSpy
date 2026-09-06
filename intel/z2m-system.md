# The Integrated System — What We Built

---

## The Full Picture

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE MACHINE                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│  │   z2m        │    │ finalbuilds2 │    │  AISec       │     │
│  │  RESEARCH    │    │   FACTORY    │    │  SECURITY    │     │
│  │              │    │              │    │              │     │
│  │ Pain themes  │    │ Idea bank    │    │ Attack corpus│     │
│  │ Market data  │    │ Hypotheses   │    │ Bounty adapt │     │
│  │ Competitors  │    │ Experiments  │    │ UK regulation│     │
│  │ Strategy     │    │ Attribution  │    │ Worker kit   │     │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘     │
│         │                   │                   │              │
│         └───────────────────┼───────────────────┘              │
│                             │                                  │
│                    ┌────────▼────────┐                         │
│                    │   ORACLE (MW)   │                         │
│                    │   Opportunity   │                         │
│                    │   Scanner       │                         │
│                    └────────┬────────┘                         │
│                             │                                  │
│                    ┌────────▼────────┐                         │
│                    │   WORKER (bitt) │                         │
│                    │   Execute       │                         │
│                    └────────┬────────┘                         │
│                             │                                  │
│                    ┌────────▼────────┐                         │
│                    │   HydraDB       │                         │
│                    │   Learn         │                         │
│                    └─────────────────┘                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## What Each Repo Does

### z2m — The Scientist
**Location:** `/root/z2m`

| Component | What It Does | Files |
|-----------|-------------|-------|
| Strategy | Business positioning, thesis, execution plans | `strategy/` (8 docs) |
| Research | Pain analysis, competitor intel, market data | `research/` (159 reports, 12 themes) |
| Products | Product ideas, personalization, founder tools | `products/` (3 categories) |
| Data | Scanners, databases, feeds, calculators | `data/` (370 opportunities) |
| Imports | 18 imported codebases and research packs | `imports/` (18 ZIPs) |

### finalbuilds2 — The Factory
**Location:** `/root/finalbuilds2`

| Component | What It Does | Files |
|-----------|-------------|-------|
| Ideabank | 100+ generated ideas | `ideabank/` (hourly reports) |
| Hypotheses | Track which ideas work | `hypotheses/` |
| Factory | Build products from ideas | `src/` (full codebase) |
| Experiments | A/B testing, attribution | `src/experiments/` |
| Standards | Version registry, drift detection | `standards/` |
| Registry | Idea → build → product → site | `registry/` |

### AISec — The Security Lab
**Location:** `/root/aisec`

| Component | What It Does |
|-----------|-------------|
| Schemas | Incident, claim, regulation, obligation models |
| Bounties | 14 platform adapters, submission workflows |
| UK Regulation | NCSC, ICO, DUA Act tracker |
| Sources | ATLAS, garak, PyRIT, Inspect repos |

---

## The Hypothesis Hierarchy

```
H1: Personalization Arbitrage (0.80)
├── H1a: Gift engines (ornaments, puzzles, photo books)
├── H1b: Decision engines (kitchen audit, moving blueprint)
└── H1c: Visualization (room render, product mockup)

H2: Pain-Attached Digital Products (0.85)
├── H2a: Moving abroad
├── H2b: Golf improvement
├── H2c: Home renovation
└── H2d: Wedding planning

H3: Voice AI Collapses Commerce Cost (0.75)
├── H3a: Voice concierge
├── H3b: Warranty claims
├── H3c: Delivery exceptions
├── H3d: Return rescue
└── H3e: B2B reorder

H4: Geographic Arbitrage (0.70)
├── H4a: Nordic markets
├── H4b: DACH markets
└── H4c: Benelux markets

H5: Free Distribution First (0.85)
├── H5a: Etsy free listings
├── H5b: Google free Shopping
├── H5c: Pinterest organic
└── H5d: YouTube Shorts

H6: Factory Is The Product (0.90)
├── H6a: Ideabank
├── H6b: Hypothesis tracking
├── H6c: Scoring
└── H6d: Experiments

H7: AI Gifting Is Strongest Single Product (0.85)
├── H7a: Christmas ornaments
├── H7b: Personalized puzzles
├── H7c: Photo magazines
└── H7d: Card bundles
```

---

## The Data Flow

```
RESEARCH (z2m)
│ 159 reports → 12 pain themes
│ 370 opportunities → scored
│ 7 market scanners → demand signals
│ Etsy/Google/Pinterest → trends
▼
HYPOTHESIS GENERATION (finalbuilds2)
│ Pain themes → ideas
│ Market data → hypotheses
│ Competitor gaps → opportunities
▼
SCORING (q4 oracle pack)
│ Capital requirements
│ Margin potential
│ Competition whitespace
│ Channel economics
▼
FACTORY (finalbuilds2)
│ Build MVP
│ Deploy to free channels
│ Track outcomes
▼
WORKER (bitt)
│ Execute against targets
│ Submit to bounties
│ Generate revenue
▼
LEARNING (HydraDB)
│ What worked
│ What failed
│ Attribution
│ Hypothesis confidence update
▼
back to RESEARCH
```

---

## The Product Portfolio

### Tier S — Build First (AI Gifting)
| Product | Capital | AOV | Moat |
|---------|---------|-----|------|
| Christmas ornaments | $0-10 | $15-25 | Recipient memory |
| Personalized puzzle | $0-10 | $25-40 | Photo transformation |
| Photo magazine | $0-10 | $30-60 | Story + layout |
| Card bundle | $0-10 | $10-15 | Reminder loop |

### Tier A — Build Second (Pain Solutions)
| Product | Capital | AOV | Moat |
|---------|---------|-----|------|
| Kitchen quote auditor | $0-10 | $49 | Deterministic comparison |
| Moving abroad blueprint | $0-10 | $39 | Personalized plan |
| Golf break-90 plan | $0-10 | $39 | Training data |
| Voice commerce concierge | $0-10 | $60/mo | Vertical playbook |

### Tier B — Build Third (Voice AI)
| Product | Capital | AOV | Moat |
|---------|---------|-----|------|
| Warranty claims agent | $0-10 | $49-199/mo | Parts history |
| Delivery exception guard | $0-10 | $99/mo | Carrier outcomes |
| Return rescue agent | $0-10 | % saved | Pre-return data |
| B2B reorder agent | $0-10 | $149/mo | Account context |

### Tier C — Experiment (Geographic)
| Product | Capital | AOV | Moat |
|---------|---------|-----|------|
| Home barista Finland | $0-10 | €150-500 | Compatibility + localization |
| Winter gear Norway | $0-10 | NOK 200-500 | Search intent + localization |
| Dog travel Denmark | $0-10 | DKK 300-600 | Fitting + safety content |

---

## The Execution Timeline

### Week 1: Prove Fulfilment
- Prodigi/Gelato accounts
- Order samples
- Build creation flow
- Test 50 recipient briefs

### Week 2: Launch Demand Lab
- 20 hypothesis pages
- Pinterest + Etsy + Google Merchant
- First £20 ad test

### Week 3-4: Find Winning Wedge
- Track metrics
- Kill losers, scale winners
- 3-5 product types

### Month 2: Scale + Cross-Sell
- Bundle offers
- Email capture + reminders
- Pinterest organic
- Google Shopping expansion

### Month 3: Q4 Ramp
- Gift framing
- Black Friday prep
- Multi-country expansion
- Voice AI layer

---

## The Revenue Model

### Phase 1: Digital/POD (Month 1-2)
- Cards: £3-5 (acquisition)
- Ornaments: £15-25 (margin)
- Puzzles: £25-40 (AOV)
- Photo books: £30-60 (premium)

### Phase 2: Subscriptions (Month 2-3)
- Annual ornament subscription: £20/year
- Birthday reminder service: £5/month
- Family collection updates: £10/quarter

### Phase 3: Voice AI (Month 3+)
- Voice concierge: $60-120/mo per merchant
- Warranty claims: $49-199/mo
- Delivery guard: $99/mo

### Target Path
```
Month 1: £500 (proof of concept)
Month 2: £3,000 (winning wedge found)
Month 3: £10,000 (scaling + subscriptions)
Month 6: £30,000 (multi-country + voice)
Month 12: £100,000 (compound growth)
```

---

## The Key Insight

> **The factory is the product. The products are the experiments.**

We don't build one store. We build a system that:
1. Research finds pain
2. Hypothesis formed
3. Factory builds MVP
4. Deploy to free channels
5. Measure real outcomes
6. Hypothesis confirmed/rejected
7. Scale winners, kill losers

The system that does this is worth more than any single store it produces.

**z2m provides the research. finalbuilds2 provides the factory. The gifting pack provides the first product. The voice AI pack provides the execution layer. AISec provides the security moat.**

**All connected. All compounding. All autonomous.**
