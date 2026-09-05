# StallSpy — The Commerce Corpus Thesis

**Date:** 5 September 2026
**Status:** Strategic thesis — the end product is the dataset, not the stores

---

## The Insight

A course says: "Here's what I think you should do."

The corpus says: **"Here are 1,000+ consecutive days of what was actually done, what it cost, what happened next, what we believed at the time, what turned out to be wrong, and the exact state of the business at every step."**

For an AI agent, the second is vastly more interesting.

---

## Think of It as an Operating Dataset, Not a Blog Archive

Every public blog post has a corresponding machine-readable record:

```text
/day/0047/
    summary.md
    day.json
    events.jsonl
    metrics.json
    hypotheses.json
    decisions.jsonl
    experiments.jsonl
    lessons.jsonl
    financials.json
    artifacts.json
```

And `day.json` contains things like:

```json
{
  "day": 47,
  "date": "2026-10-22",
  "business_state": {
    "revenue_cumulative": 1832.41,
    "profit_cumulative": 618.22,
    "active_shops": 2,
    "active_listings": 31
  },
  "goals_at_start": [
    "Improve Game Winner conversion",
    "Test birthday thumbnail V4"
  ],
  "key_actions": [
    "Changed hero thumbnail",
    "Raised digital package from 7.99 to 9.99",
    "Tested five H3 generations"
  ],
  "key_outcomes": [
    "CTR increased 2.8% -> 4.1%",
    "2 orders at new price"
  ],
  "highest_information_event": "Price increase did not reduce conversion",
  "belief_updates": [
    {
      "before": "£7.99 is important for conversion",
      "after": "Perceived quality may dominate price in £8-£12 range",
      "confidence": 0.72
    }
  ]
}
```

The **belief-before → action → outcome → belief-after** chain is enormously important.

Most business datasets only contain outcomes.

You'd be collecting the **decision trace**.

---

## The Really Valuable Dataset

It's not "how I made $1M."

It's:

### **What did I know at every point before I knew the answer?**

Example:

**Day 21:** We think Dogcasso Natural Habitat will outperform birthday.

**Day 34:** Birthday converted 4.8%; Natural Habitat 0.9%.

**Update:** Hypothesis rejected. Buyers respond more strongly to explicit occasion intent than novelty.

Later Game Winner independently confirms it.

Agent extracts generalized rule:

> **When entering a gifting marketplace, start with established occasion/search intent and use novelty as the differentiator rather than asking the customer to learn a new purchase category.**

That's substantially more useful than "Use good thumbnails."

And because the conclusion has experiments behind it, the agent knows **why and with what confidence**.

---

## The End Product: Agent Pack

# **$0 → $1M Commerce Corpus**

A complete machine-readable operating history of building AI-native consumer brands from scratch.

### What it contains

- Every daily operating record
- Hypotheses (accepted + rejected)
- Failed ideas (with reasons)
- Successful ideas (with evidence)
- Price changes + outcomes
- Listing changes + outcomes
- Thumbnails (before/after)
- Generation/model experiments
- Product economics per SKU
- Marketing experiments
- Store launches + kills
- Supplier decisions + costs
- AI costs per generation
- Advertising spend + ROAS
- Conversion changes over time
- Seasonality patterns
- Customer feedback themes
- Anonymized support problems
- Lessons (with confidence levels)
- Weekly retrospectives
- Monthly strategy updates
- Reusable playbooks
- Final post-mortems

### Derived assets for agents

```text
/corpus/
    days.jsonl                    # 1,000+ daily records
    experiments.jsonl             # every A/B test and hypothesis
    decisions.jsonl               # every decision with rationale
    lessons.jsonl                 # derived rules with confidence
    business_states.parquet       # daily snapshots for time series

/playbooks/
    launch_store.md               # step-by-step from experience
    validate_product.md           # how we test before launching
    price_personalization.md      # pricing psychology from data
    q4_launch.md                  # seasonal playbook
    kill_or_continue.md           # decision framework
    content_flywheel.md           # build-in-public playbook
    agent_calibration.md          # how to use the corpus

/evals/
    opportunity_selection.jsonl   # did our picks work?
    pricing_decisions.jsonl       # did our prices work?
    listing_diagnosis.jsonl       # did our SEO work?
    portfolio_decisions.jsonl     # did our brand choices work?

/agent/
    SYSTEM.md                     # agent instructions
    PLANNER.md                    # planning agent prompt
    STORE_OPERATOR.md             # store management agent prompt
    examples/                     # few-shot examples from history

/database/
    commerce-corpus.sqlite        # queryable historical database
```

### Agent query example

> "Find the five historical situations most similar to a new personalized fishing-gift store with a £500 starting budget."

Agent searches the corpus, finds comparable episodes, reasons from them.

**Case-based business intelligence.**

---

## The $10,000 Buyer

In three years, with meaningful success:

- 1,000 days documented
- 10–30 brand experiments
- Hundreds of listing experiments
- Thousands of generation tests
- Millions of marketplace impressions
- Real transaction history

A person with £100k wanting to build an Etsy/ecommerce portfolio could value a high-quality operational dataset more than a video course.

Their agent generates:

> Day 1: Research these three categories.
> Day 2: Produce these specific prototypes.
> Day 3: Test against this reliability suite.
> Day 4: Build five search-intent listings.

And crucially:

> "I'm recommending this because comparable Experiments #14, #27 and #31 behaved this way."

---

## Licensing Tiers

### Free — Public Research
Daily blog. Selected charts. Selected lessons. Some experiment records.
Builds trust and SEO.

### £99–299 — Research Edition
Clean historical summaries + playbooks.
Good for individual sellers.

### £500–1,500 — Agent Edition
Full structured corpus. SQLite/JSONL/Parquet. Agent prompts. Retrieval examples. Evaluations. Periodic updates.

### £5,000–10,000+ — Operator/Investor Edition
Complete historical corpus. Detailed decision records. Full experiment archive. Longer-delay proprietary information. Commercial/internal agent license. Planning agent built around corpus. Onboarding session / portfolio analysis.

---

## Public Pages as Teasers

Blog article shows:

### Day 143 (Public)

Revenue: £312
Profit: £167
Biggest change: Game Winner conversion rose 31%

> We discovered that showing the original customer photo immediately beside the generated result materially increased conversion.

### Agent Record Preview

```text
EXP-0093
hypothesis: Before/after proof increases trust in generative personalization.
control_conversion: 3.21%
variant_conversion: 4.19%
relative_change: +30.5%
sample_size: ...
decision: ADOPT
```

> **This is one of 2,481 experiment records in the Commerce Corpus.**

---

## Data Architecture

### Proprietary layer (safe to build around)

- Your decisions
- Your hypotheses
- Your own costs
- Your own generated assets
- Your own prompts/recipes
- Your business P&L
- Your experiments
- Your derived lessons
- Your manually authored observations
- Your own website analytics
- Your own production metrics

### Handle carefully / don't redistribute

- Customer names, addresses, emails
- Private messages
- Customer photographs (without permission)
- Other sellers' images/descriptions
- Raw Etsy-member datasets
- Raw API snapshots intended for ML/licensing

### The principle

> **We sell our experience and experimental results, not a scraped copy of Etsy.**

---

## Three Data Visibility Levels (From Day 1)

**PUBLIC_NOW** — Safe for today's blog/YouTube.

**PUBLIC_DELAYED** — Release after 30/90 days. Exact tactics still producing alpha.

**CORPUS_PRIVATE** — Future licensed material. Detailed experiment configs. Complete decision traces. Production economics. Proprietary template performance. Internal failure analysis.

Build in public without publishing the entire advantage while exploiting it.

---

## The Killer Demo

Landing page:

> "I have $5,000. I want to build personalized gifts for fishermen in the US. I have no existing audience. Produce my first 30-day plan."

Agent searches historical corpus and returns:

**Day 1–3: Validate intent**
Comparable evidence: GameWinner Experiments 14/21, Dogcasso Birthday 7/9.

**Day 4–6: Create one product primitive**
Historical evidence suggests focused occasion products beat broad novelty products during cold start.

**Day 7: Produce five proof examples**
Before→after images improved trust in Experiment 93.

**Day 8–10: Launch listings around recipient + occasion, not art style.**

Every recommendation links back into real historical evidence.

Miles beyond "Here are 25 Etsy tips."

---

## The Daily Journal Structure

Every day records six things:

| Field | Question |
|-------|----------|
| **STATE** | Where was the business? |
| **BELIEF** | What did we think was true? |
| **ACTION** | What did we actually change? |
| **COST** | What resources did that consume? |
| **OUTCOME** | What happened afterward? |
| **UPDATE** | What do we now believe? |

That six-part structure is the actual dataset.

The blog and YouTube are simply human-readable views of it.

---

## The Endgame

If you genuinely take one or more stores from **$0 to substantial revenue**, the resulting corpus becomes something quite rare:

**A dense longitudinal record of AI-assisted microenterprise formation from initial hypothesis through real market outcomes.**

That may eventually be more valuable than any single Etsy store.

---

*The business comes first. Content records the business. The corpus outlasts both.*
