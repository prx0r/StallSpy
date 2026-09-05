# The Feelings Dataset — Agent-Human Meta-Signals as Training Data

**Date:** 5 September 2026
**Context:** Etsy API reference confirms agent-operability. Blind reviewers independently arriving at the same conclusions = validated knowledge. The "feelings" dataset (agent + human assessments of state/progress/future) becomes the primary training signal for operator models and the foundation for corporate structure.

---

## The Core Insight

Every day, both human and agent produce assessments about:

- **Current state** — "how are things going?"
- **Progress** — "are we moving forward?"
- **Future state** — "what should happen next?"
- **Emotional/strategic signal** — "I feel X about Y"

These assessments are not just journal entries. They are **labeled training data** for:

1. Operator models (what would this human think/do?)
2. Economic models (what actually produces value?)
3. Meta-management models (when to ask, when to act, when to escalate)

The key: **linking "feelings" to BATS economic activity and economic outcomes** creates a tunable system.

---

## The Feelings-Activity-Outcome Linkage

```text
FEELINGS (daily)
├── "I'm worried about conversion"
├── "Game Winner feels stronger than MythicBee"
├── "I'm spending too much time on infrastructure"
└── "Customers aren't leaving reviews"

     ↓ linked to

BATS ACTIVITY (same day)
├── $8.13 spent on H3 generation
├── 4h on MythicBee, 2h on StallShark
├── 0h on marketing
└── 0h on customer outreach

     ↓ linked to

ECONOMIC OUTCOMES (1d/7d/30d later)
├── 0 sales
├── 12 impressions
├── 0 reviews
└── $0 revenue
```

Now you can ask:

> "When the operator reports worry about conversion, does increased ad spend actually improve conversion?"

> "When the agent reports confidence about a concept, does it convert better than when the agent reports uncertainty?"

> "When the operator feels 'stuck,' is the optimal response more spending or more research?"

---

## Tunable Aggression

The operator model learns a **risk preference parameter** from the feelings-activity-outcome data:

```json
{
  "operator_id": "tom_v1",
  "risk_preference": {
    "value": 0.42,
    "scale": "0=ultra_conservative ... 1=ultra_aggressive",
    "calibrated_from": 847_decisions,
    "confidence": 0.78
  },
  "current_context_adjustment": {
    "low_sales_week": "pushes toward 0.55 (more aggressive)",
    "high_cash_reserve": "pushes toward 0.60",
    "recent_failure": "pushes toward 0.30 (more cautious)"
  }
}
```

The economic critic can then say:

> "Operator's current risk preference is 0.42. Given 3 consecutive weeks of declining sales, the optimal response per historical data is 0.55. Shall I propose a more aggressive posture?"

And the human decides.

---

## The Problem → Hypothesis → Experiment Pipeline

This is the meta-protocol that makes the system self-improving.

### Stage 1: Problem Detection

Agent identifies problems from multiple signals:

```json
{
  "problem_id": "P-047",
  "detected_by": "economic_critic",
  "detection_method": "metric_anomaly",
  "description": "Conversion rate dropped from 4.2% to 2.1% over 14 days",
  "severity": "high",
  "first_observed": "2026-10-15",
  "affected_brands": ["gamewinner"],
  "candidate_causes": [
    "seasonal_decline",
    "competitor_entry",
    "listing_quality_degradation",
    "price_sensitivity",
    "trust_signal_missing"
  ]
}
```

Sources of problem detection:

| Source | What it detects |
|--------|----------------|
| Economic Critic | Metric anomalies, declining trends |
| Operator Twin | When human reports frustration/uncertainty |
| Cold Reviewer | When actions don't match stated priorities |
| BATS | When cost-per-acquisition exceeds threshold |
| Customer feedback | Review themes, refund reasons |
| Market signals | Competitor changes, seasonality |

### Stage 2: Research

Agent searches for relevant knowledge:

```json
{
  "research_id": "res-047",
  "problem_id": "P-047",
  "sources_searched": [
    "corpus_history",
    "external_literature",
    "competitor_analysis",
    "customer_feedback"
  ],
  "findings": [
    {
      "source": "corpus_history",
      "finding": "P-019 (MythicBee trust issue) was resolved by before/after proof",
      "relevance": 0.72,
      "applicability": "moderate — different product but similar trust friction"
    },
    {
      "source": "external_literature",
      "finding": "Etsy SEO research shows review velocity is #1 predictor of conversion",
      "relevance": 0.85,
      "applicability": "high — directly addresses missing reviews"
    },
    {
      "source": "customer_feedback",
      "finding": "3 buyers asked 'will this look like my dog?' before purchasing",
      "relevance": 0.91,
      "applicability": "high — confirms trust/uncertainty as root cause"
    }
  ]
}
```

### Stage 3: Hypothesis Formation

```json
{
  "hypothesis_id": "H-047",
  "problem_id": "P-047",
  "claim": "Adding before/after proof images to Game Winner listings will increase conversion from 2.1% back to 4%+",
  "mechanism": "Reduces buyer uncertainty about AI-generated output quality",
  "confidence_before": 0.65,
  "falsification": "Conversion does not improve within 14 days of implementation",
  "estimated_cost": "$0 (only requires rephotographing existing outputs)",
  "estimated_timeline": "3 days to implement, 14 days to measure"
}
```

### Stage 4: Experiment Design

```json
{
  "experiment_id": "exp-047",
  "hypothesis_id": "H-047",
  "design": "before_after",
  "control": {
    "description": "Current listing with AI-generated hero image only",
    "listings": ["listing_gw_001", "listing_gw_002"]
  },
  "treatment": {
    "description": "Same listing with before/after proof image added",
    "listings": ["listing_gw_003", "listing_gw_004"]
  },
  "primary_metric": "conversion_rate",
  "secondary_metrics": ["favorite_rate", "click_through_rate", "refund_rate"],
  "minimum_sample": 100_visits_per_variant,
  "measurement_window": "14_days",
  "success_rule": {
    "metric": "conversion_rate",
    "minimum_relative_change": 0.20,
    "direction": "increase"
  },
  "budget": {
    "cash": 0,
    "tokens": 50000,
    "human_minutes": 30
  }
}
```

### Stage 5: Execution

BATS allocates resources:

```json
{
  "work_orders": [
    {
      "work_order_id": "wo-047a",
      "objective": "Create before/after proof images for 4 Game Winner listings",
      "budget": {"human_minutes": 20, "tokens": 20000, "cash": 0}
    },
    {
      "work_order_id": "wo-047b",
      "objective": "Update listing hero images with proof variants",
      "budget": {"human_minutes": 10, "tokens": 10000, "cash": 0}
    }
  ]
}
```

### Stage 6: Measurement

After 14 days:

```json
{
  "experiment_result": {
    "experiment_id": "exp-047",
    "status": "complete",
    "duration_days": 14,
    "control": {
      "visits": 187,
      "conversions": 4,
      "conversion_rate": 0.0214
    },
    "treatment": {
      "visits": 203,
      "conversions": 11,
      "conversion_rate": 0.0542
    },
    "effect": {
      "relative_change": 1.53,
      "p_value": 0.023,
      "confidence": "moderate"
    },
    "decision": "adopt",
    "revenue_impact": "+$67.40 over 14 days"
  }
}
```

### Stage 7: Protocol Storage

The validated solution becomes a reusable protocol:

```json
{
  "protocol_id": "proto_trust_proof_v1",
  "name": "Before/After Proof for Generative Products",
  "derived_from": ["exp-047", "P-019", "corpus_observation_22"],
  "claim": "Showing source-to-output proof reduces trust friction for AI personalization",
  "applicable_when": [
    "generative_product",
    "customer_uploads_photo",
    "output_quality_uncertain"
  ],
  "implementation_steps": [
    "Generate 3-5 example outputs from reference photos",
    "Place source photo directly beside generated result in hero image",
    "Include text: 'This is what [Name] looked like → This is what we made'"
  ],
  "evidence_strength": 0.78,
  "estimated_conversion_lift": "50-150%",
  "estimated_cost": "$0",
  "applicable_brands": ["gamewinner", "mythicbee", "greatest_hits", "cover_story"]
}
```

Now the next brand that launches gets this protocol automatically.

---

## From Protocols to Corporate Structure

As protocols accumulate, the system naturally generates organizational structure:

### Phase 1: Solo Operator (Day 1-90)

```text
Human does everything
Agent advises
1 brand active
```

### Phase 2: Operator + Assistant (Day 90-180)

```text
Agent handles: research, drafting, SEO, content
Human handles: product taste, strategy, customer relationships
2-3 brands active
Agent has L3 autonomy (reversible actions)
```

### Phase 3: Operator + Departments (Day 180-365)

```text
Agent team:
├── Research Agent (market intelligence)
├── Content Agent (blog, social, SEO)
├── Operations Agent (listings, inventory, orders)
├── Creative Agent (generation, QA, iteration)
└── Finance Agent (budgets, pricing, P&L)

Human: strategic decisions, brand vision, relationship management
5+ brands active
Agent has L4 autonomy (bounded operations)
```

### Phase 4: Delegated Agency (Year 2+)

```text
Each brand gets its own agent team
Corporate layer coordinates resource allocation
Human: CEO — sets vision, allocates capital, evaluates brand performance
External agents (marketing agency, fulfillment) integrated via protocols
Agent has L5 autonomy (brand management within budget)
```

The corporate structure **emerges from the protocol stack**, not from org-chart thinking.

---

## The Agent Research → Fix → Track Cycle

Each problem goes through:

```
IDENTIFY → RESEARCH → HYPOTHESIZE → EXPERIMENT → MEASURE → STORE
    ↑                                                      │
    └──────────────────────────────────────────────────────┘
```

The stored protocols become the company's **operating manual** — written by its own experience.

After 100 experiments:

- Which interventions reliably improve conversion?
- Which are waste?
- What's the base rate for each type of problem?
- Which problems recur and need systemic solutions?
- When is the right time to invest in infrastructure vs validation?

That's institutional knowledge. Normally it lives in a founder's head. Here it's in the corpus.

---

## The Natural Progression

```
FEELINGS → PROBLEMS → PROTOCOLS → DEPARTMENTS → CORPORATION
```

Not planned. Emergent.

Day 1: "I'm worried about conversion" → one experiment

Day 30: "Conversion protocol v3 works reliably" → stored knowledge

Day 90: "We have 12 protocols covering the main failure modes" → operating manual

Day 180: "The research protocol can be delegated to an agent" → first department

Day 365: "Each brand has its own agent team following validated protocols" → corporation

**The company builds itself from experiments.**

---

## What Makes This Work

1. **Etsy API is agent-operable** — good API design means agents can actually execute
2. **Blind reviewers validate independently** — knowledge is tested, not assumed
3. **Feelings are labeled training data** — human + agent assessments linked to outcomes
4. **BATS makes economics explicit** — every action has a cost, every outcome has a return
5. **Protocols compound** — each solved problem becomes reusable institutional knowledge
6. **Structure emerges from protocols** — departments form around protocol clusters
7. **The system is tunable** — aggression/conservatism adjusts to economic context
8. **Everything is recorded** — the corpus grows richer with every day

---

*The Etsy API is the perfect agent-operable marketplace. The feelings dataset is the training signal. The problem→protocol pipeline is the growth engine. The corporate structure is the emergent outcome.*
