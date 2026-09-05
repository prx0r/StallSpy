# The £0 → £1M Experiment — Master Plan

**Date:** 5 September 2026
**Core thesis:** Can one person use AI, public data and automation to repeatedly discover, build and scale profitable microbrands from almost no starting capital?

**Context:** Unemployment grows from AI. People need ways to make money. A person documenting their journey building Etsy stores with AI is exactly what thousands of people want to watch — because they're asking their own agents "what works?" and there's no real-world timestamped log of someone actually doing it.

**Tool:** stallspy.com — the agent control plane for the stores.

**Even if it fails:** A granular, timestamped log of someone trying to start an Etsy store — tracking actions daily on what works and what doesn't — is valuable data. When someone asks their agent "what works on Etsy?", this dataset is the answer.

---

## The Flywheel

```text
                    PUBLIC JOURNEY
              YouTube / Blog / X / Shorts
                       ↑       ↓
                    audience
                       ↑       ↓
   ┌─────────── STALLSPY / RESEARCH ENGINE ───────────┐
   │                                                   │
   │ demand → hypotheses → products → measurement      │
   │    ↑                                  ↓           │
   │    └────────── learning / corpus ─────┘           │
   └───────────────────────────────────────────────────┘
                        ↓
              PERSONALIZATION FACTORY
         images / video / audio / POD / QA
                        ↓
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
      Dogcasso      Game Winner     Brand #3
          ↓             ↓             ↓
       revenue        revenue       revenue
          └─────────────┼─────────────┘
                        ↓
                 REAL PERFORMANCE DATA
```

Four outputs reinforce each other:

1. **Stores make money.**
2. **Real store performance makes the content credible.**
3. **Content creates audience/distribution.**
4. **Operating the stores produces the data that makes StallSpy useful.**
5. **StallSpy improves the next store.**
6. **Successful stores validate StallSpy to future customers.**

StallSpy becomes:

> **The Etsy/ecommerce tool built by actually running the businesses it's advising you about.**

---

## The Public Project Is Bigger Than Dogcasso

YouTube channel = personal builder channel.

Eventually talking about:
- Dogcasso
- Game Winner
- StallSpy
- Failed ideas
- AI models
- Etsy experiments
- POD
- Marketing
- Revenue
- Building software
- New marketplaces
- Eventually businesses beyond Etsy

The recurring series: **$0 → $1,000,000**

People are dying for authentic money-making content. Not guru BS. Not "I made $10k last month." Real numbers, real failures, real timestamps.

Define what the number means on Day 1. Track separately:

| Metric | Definition |
|--------|-----------|
| Gross revenue | Total money in |
| Gross profit | Revenue minus COGS |
| Net profit | Gross minus all expenses |
| Cash balance | What's in the bank |
| Total invested | Everything spent so far |

Truthfully say:

> Day 36
> Revenue: $1,238
> Net profit: $294
> Cash invested: $73

That honesty itself becomes the brand.

---

## Daily Content: Deliberately Primitive

**30–90 seconds per day.** That's the required human action.

### Daily Short Structure

```
HOOK — 3 sec
"I spent $8 today trying to make someone's Dad score the World Cup winner."

MONEY
Spent: $8.13
Revenue: $0
Cumulative P&L: -$24.71

WHAT I DID
2–3 visual clips/screenshots.

RESULT
Good/bad/interesting.

ONE INSIGHT
The highest-alpha lesson.

TOMORROW
One concrete experiment.
```

Done. Total content creation time: ~45 minutes/day. Everything else is automated or is the actual work being documented.

### Content Automation Pipeline

```text
Git commits (timestamped actions)
     +
Etsy API data (sales, views, favorites)
     +
StallSpy actions (hypotheses, tests, results)
     +
AI/GPU spend logs
     +
Manual voice note (30-90 sec)
     +
Screenshots / photos
        ↓
   commit_parser.py → daily_summary.py
        ↓
   Significance scorer (rewards: money change, hypothesis changed,
   unexpected result, failed assumption, customer feedback)
        ↓
   ┌─────────────┬──────────────┬─────────────┐
   ↓             ↓              ↓
Short script  Blog draft     Dataset entry
   ↓             ↓              ↓
TTS voice     Markdown        SQLite
   ↓             ↓              ↓
Video edit    Publish         StallSpy
   ↓             ↓              ↓
YouTube       Substack/blog   Training data
```

### Weekly becomes the compelling long-form

# **Etsy Money — Week 1: -$12.43**

Then:

- Week 2: I Finally Made a Sale — +$6.21
- Week 3: I Built a Second Store
- Week 4: This Product Beat Everything Else
- Week 7: My $5 AI Gift Made $327
- Week 11: I Killed a Store

**Important:** Do NOT literally concatenate Shorts and upload untouched. YouTube's monetization rules care about repetitive/reused content. Add fresh weekly narration, charts, conclusions and retrospective so the weekly episode is genuinely new editorial content.

Weekly pipeline:

```text
7 daily Shorts
+
Git activity
+
store metrics
+
expenses
+
screenshots
+
decisions
        ↓
AI timeline extraction
        ↓
rank events by significance
        ↓
weekly narrative
        ↓
8–15 minute video
```

---

## The Experiment Ledger

Every meaningful action creates an event. One source of truth.

### Production events

```json
{
  "timestamp": "2026-09-06T14:32:17+07:00",
  "project": "gamewinner",
  "store": "gamewinner-etsy",
  "experiment": "SPORTS_HERO_V1",
  "hypothesis": "Football fantasy converts as a birthday gift for dads",
  "action": "generated_video",
  "model": "minimax-h3-max",
  "cost_usd": 0.82,
  "input_variant": "older_male_glasses",
  "output_score": 8.7,
  "passed_qa": true,
  "time_minutes": 6,
  "git_commit": "...",
  "notes": "Face remained consistent; crowd audio excellent"
}
```

### Commerce events

```
listing_view, listing_click, favorite, cart, checkout,
order, refund, review, repeat_order, upsell
```

### Development events

```
idea_created, hypothesis_created, template_tested,
generation_failed, generation_passed, listing_created,
listing_changed, price_changed, thumbnail_changed,
seo_changed, supplier_changed
```

### Financial events

```
AI_spend, GPU_spend, listing_fees, ad_spend, POD_cost,
shipping, domain, software, revenue, refund, net_contribution
```

---

## The Canonical Daily Record

Every day ends with this automatically:

```text
DAY 18

STARTING CASH:     $___
REVENUE TODAY:     $___
EXPENSE TODAY:     $___
NET TODAY:         $___
CUMULATIVE NET:    $___

STORE METRICS:
  Dogcasso:
    impressions:
    visits:
    sales:
    conversion:
  Game Winner:
    ...

SHIPPED:    ...
TESTED:     ...
FAILED:     ...

KEY DECISION:      ...
BEST INSIGHT:      ...
HYPOTHESIS UPDATE: ...
TOMORROW:          ...
```

This document simultaneously becomes:
- Your journal
- The Short script
- The blog source
- Weekly video source
- StallSpy training/eval data
- The eventual research corpus

---

## Blog / Newsletter

### Daily post (300–700 words)

```text
## Day 17 — Finally Got Game Winner Reliable

### Money
Spend: $4.72
Revenue: $8.99
Profit: $2.84

### What I did
Three bullets.

### What happened
Actual metrics.

### What surprised me
One real observation.

### Decision
What you're changing.

### Tomorrow
Experiment.
```

### Weekly Research Report (Sunday)

- Cumulative P&L
- Traffic
- Listings
- Conversion
- AI generation costs
- Production reliability
- What worked / what failed
- Hypotheses accepted/rejected
- Next week's experiments

These become **SEO assets** and later chapters of the larger project.

---

## Live Scoreboard (Website)

```text
# $0 → $1M

Day 43

Revenue:         $1,842
Net Profit:      $614
Stores Launched: 2
Products:        17
Sales:           126
Failures:        9
AI Spend:        $81
Ad Spend:        $42
Hours:           127
```

Charts: revenue by day, profit by day, store leaderboard, experiments launched/killed.

Timeline:
> Sep 6 — Dogcasso started
> Sep 12 — first sale
> Sep 19 — Natural Habitat killed
> Sep 23 — Game Winner launched
> Oct 2 — first physical bundle sale

People come back just to see whether you're succeeding.

---

## StallSpy (stallspy.com): The Agent Control Plane

StallSpy consumes the ledger and becomes the store management agent. It is simultaneously:
- The research engine that finds opportunities
- The production system that generates products
- The analytics dashboard that tracks performance
- The learning system that improves with each experiment

The key differentiator: StallSpy's recommendations can be compared against actual outcomes from our own stores. No other Etsy tool has this calibration loop.

```text
MARKET       → What are people searching for?
COMPETITION  → What already sells?
HYPOTHESIS   → What opportunity might exist?
BUILD        → What should we make?
LAUNCH       → How should it be positioned?
OBSERVE      → What happened?
DIAGNOSE     → Why?
ACT          → What should change?
LEARN        → Did the change work?
```

Critical: StallSpy's recommendations can be compared against actual outcomes.

**StallSpy prediction:** Game Winner has 74/100 opportunity score.

**Actual result after 30 days:** 417 visits, 19 sales, 4.6% conversion, £173 revenue, £102 contribution.

Now you can calibrate StallSpy. Far more valuable than another tool showing estimated Etsy revenue.

---

## The Mini-Paper

### Title: AI-Native Microenterprise: A Longitudinal Public Experiment in One-Person Business Formation

**Do NOT frame as "AI is causing mass unemployment."** Evidence isn't strong enough. ILO June 2026 review says large-scale displacement remains limited.

**Better thesis:**

> AI is rapidly reducing the cost of capabilities previously requiring teams—design, software development, marketing, media production, customer support and analysis. Can these falling coordination and production costs enable individuals to create economically viable microenterprises with very little starting capital?

### Research Questions

| Hypothesis | Question |
|-----------|----------|
| H1 — Cost compression | Can AI materially reduce the cash required to launch differentiated consumer products? |
| H2 — Speed | Can one operator test substantially more commercial hypotheses per month? |
| H3 — Specialization | Do narrowly positioned specialist brands outperform general stores? |
| H4 — Personalization | Can AI personalization command greater conversion/AOV than generic alternatives? |
| H5 — Learning | Does performance improve as the experiment corpus grows? |
| H6 — Distribution | Can transparent build-in-public content lower customer-acquisition costs? |
| H7 — Tooling | Can models trained on the experiment ledger predict better opportunities than generic marketplace research? |

That's a legitimate longitudinal study.

---

## Failure Is Valuable

Most make-money creators have survivorship bias. We publish:

> **Here are the 43 things I tried. Seven worked. Here are the exact numbers for all 43.**

A failed experiment becomes:
- **Content value:** "I lost $37 trying this Etsy idea."
- **Research value:** labeled negative example.
- **Tool value:** StallSpy learns what not to recommend.
- **Audience value:** demonstrates you're not hiding losses.
- **Business value:** prevents repeating the mistake.

The project continues even through periods of poor sales.

---

## Transparency Boundary

### Publish immediately
- Revenue, expenses, failed experiments
- Broad strategy, lessons, marketplace observations
- Finished products, model comparisons
- Things already launched

### Delay 30 days
- Exact unreleased product ideas
- Exact profitable prompts/workflows
- Supplier negotiations
- Winning unpublished keywords
- Conversion optimizations being A/B tested

### Private
- Customer PII, secrets, API keys
- Proprietary production recipes

---

## Etsy Is a Good Laboratory

- ~87 million trailing-12-month active buyers (Q2 2026)
- Solid YoY growth around Mother's Day, Father's Day, graduation
- Birthdays and weddings both grew double digits
- Etsy explicitly investing in occasion-led discovery and gifting
- Etsy says showing buyers the maker's process is one of its strongest trust drivers

> "Watch me actually build your product and business from scratch" is unusually compatible with the marketplace itself.

---

## First 30 Days

### Days 1–7: Dogcasso only
- Ledger, financial tracking
- Daily Short system, daily blog
- Public dashboard
- Birthday V1
- First Etsy listings
- Content begins: **"Day 1: I Have $0 Revenue and an Idea About Dogs"**

### Days 8–14: Dogcasso live
- Capture impressions, CTR, favorites, conversion
- Production costs, generation reliability
- Build initial StallSpy ingestion

### Days 15–21: Game Winner prototype
- Do not launch five other ideas
- Show the process
- Potential video: **"Day 17: I Think I Found a Better Business Than My First One"**

### Days 22–30: Game Winner launch
- If production validation passes
- Public scoreboard now has: Brand 1 vs Brand 2

---

## The Portfolio Becomes a Game

| Brand | Revenue | Profit | Growth | Conversion | Reliability | Content Pull | Status |
|-------|--------:|-------:|-------:|-----------:|------------:|-------------:|--------|
| Dogcasso | $820 | $441 | ↑ | 4.2% | 92% | High | CORE |
| Game Winner | $1,420 | $802 | ↑↑ | 6.1% | 87% | Very high | PROMOTE |
| Tarot test | $63 | $41 | → | 1.4% | 96% | Medium | WATCH |
| Cereal | $0 | -$18 | ↓ | 0% | 81% | High | KILL |

The audience gets invested: **"Which brand survives this month?"**

A public venture studio where starting bets cost tens of dollars rather than millions.

---

## StallSpy Launch Story

> "For the last year I used StallSpy to launch 14 Etsy brands. Eight failed. Three made a little money. Three became real businesses. Every recommendation in the software is informed by the actual experiment data."

StallSpy monetizes via:
- Research, opportunity discovery, competitor tracking
- Listing diagnostics, portfolio monitoring
- Experimentation, product briefs, production workflows
- Eventually semi-autonomous store management

YouTube audience is exactly the audience StallSpy needs. Much stronger than buying Google ads.

---

## The Key Operating Rule

Write this at the top of the repo:

> **The business comes first. Content records the business. Content must never become the business's main source of busywork.**

You spend the day:

**making offers → publishing → measuring → improving.**

The machine watches.

At the end of the day, you talk for a minute.

Everything else gets manufactured from the evidence.

That keeps the channel authentic, gives StallSpy a uniquely valuable dataset, and forces the actual experiment to remain measurable rather than disappearing into another huge build.

---

*Dogcasso is Experiment 001. Game Winner is potentially Experiment 002. StallSpy (stallspy.com) becomes the instrumentation/control plane. YouTube + the blog are the public research log and distribution engine. That is a coherent project.*

*Even if every store fails, the timestamped dataset of someone trying — with all the failures documented — is itself valuable. There is no way to lose by publishing honestly.*

---

## Appendix: Content That Works

The best-performing content on YouTube = "how to make money."

We don't need to fake it. We're literally doing it.

### The compounding loop

| Stage | What happens | What it produces |
|-------|-------------|-----------------|
| Day 1 | First video + first listing | 0 views, 0 sales |
| Week 2 | Daily recaps stacking | Search index finds "etsy money" content |
| Month 1 | "Etsy Money Week 1: +$12" | People subscribe for the journey |
| Month 3 | Real revenue numbers | Credibility → audience grows |
| Month 6 | Tool launches | Audience → tool users |
| Month 12 | £100K+ revenue | Authority → consulting, speaking, book |
| Month 24 | £1M run rate | Case study → everything compounds |

### Audience segments

| Segment | What they want | What we give them |
|---------|---------------|-------------------|
| Aspiring Etsy sellers | "How do I start?" | Real daily log of someone doing it |
| AI/tech enthusiasts | "Can AI actually make money?" | Hard numbers, no hype |
| Side-hustle seekers | "What actually works?" | Timestamped evidence, not guru BS |
| Content creators | "How do I build in public?" | Blueprint for automated content |
| Researchers | "What are marketplace dynamics?" | Open dataset |

### Even failure is content

A failed experiment becomes:
- **Content value:** "I lost $37 trying this Etsy idea."
- **Research value:** labeled negative example.
- **Tool value:** StallSpy learns what not to recommend.
- **Audience value:** demonstrates you're not hiding losses.
- **Business value:** prevents repeating the mistake.
