# Frontier Research Synthesis — What We're Building Against

**Date:** 5 September 2026

---

## The Key Insight

The missing ingredient is not "more agent autonomy." It is better instrumentation of strategy, uncertainty, capital allocation, learning, and long-horizon coherence.

The closest benchmark: **CEO-Bench** (June 2026). Agent runs a startup for 500 simulated days. Current frontier models still struggle badly. Successful trajectories build their own forecasting machinery rather than reacting turn by turn.

---

## 1. The Frontier Parallels

| Research | What They Do | What We Steal |
|----------|-------------|--------------|
| **CEO-Bench (2026)** | Agent runs startup 500 days, partial observability, delayed consequences | Explicit forecasts, cash projections, strategy regimes, delayed credit assignment |
| **Vending-Bench 2** | Agents run business for simulated year; final cash = score. High variance, long-horizon failures | Run same policy multiple times; measure variance and catastrophic failure |
| **Project Vend** | Claude operated real store; customers manipulated it into economically stupid behavior | Adversarial customers, hard economic invariants, approval thresholds |
| **TheAgentCompany** | Agent as digital employee; best baseline only ~24% autonomous | Autonomy per task/decision class (our Autonomy Passport) |
| **AI Co-Scientist** | Agents generate, critique, rank and evolve hypotheses | Apply scientific discovery architecture to commercial problems |
| **Agent Laboratory** | Literature → experiment → report; human intervention improves output while reducing costs | Human checkpoints removed only when marginal value becomes low |
| **OrgAgent (2026)** | Governance → execution → compliance hierarchy; hierarchy improves performance while reducing tokens | WorkerKit + BATS + audit layer |
| **AgentHire-Bench (2026)** | Measures managerial ability separately from intelligence; prompting style changes behavior | "Aggressive CEO", "conservative CEO" as explicit policy parameters |

Contradictory evidence: strong agents can self-organize better than rigid hierarchies. Make organizational structure an experimental variable.

---

## 2. AI Co-Scientist → Problem Engine

Transpose from science to entrepreneurship:

```
BUSINESS PROBLEM
      ↓
OBSERVATION AGENT
      ↓
HYPOTHESIS GENERATOR (multiple competing hypotheses)
      ↓
RESEARCH AGENT
      ↓
CRITIC
      ↓
EXPERIMENT DESIGNER (seeks greatest discriminative power)
      ↓
BATS
      ↓
EXECUTION
      ↓
MARKET
      ↓
RESULT ANALYST
      ↓
HYPOTHESIS UPDATE
      ↓
HYDRA (transferable knowledge)
```

Key improvement: deliberately seek experiments that **distinguish between competing hypotheses**, rather than immediately "fixing" whichever explanation the first agent invents.

---

## 3. Explicit Forecasting Before Decisions

Industry experience predicts forecasting accuracy; generic startup experience does not.

**Store contextual experience:**
- DOMAIN: Etsy personalized gifting
- STAGE: cold-start
- CHANNEL: organic Etsy search
- RECIPIENT: Dad
- OCCASION: birthday
- PRODUCT TYPE: generative personalization
- PRICE BAND: $5-20
- MARKET: US
- SEASON: Q4
- BUSINESS STATE: zero-review shop

Experience transfer should have a **context similarity score**.

---

## 4. The ForecastBook

Before anything consequential:

```json
{
  "forecast_id": "F-0182",
  "question": "Will Game Winner achieve >=3% conversion in first 250 visits?",
  "human_probability": 0.64,
  "operator_twin_prediction": 0.70,
  "agent_probability": 0.48,
  "cold_reviewer_probability": 0.57,
  "resolution_condition": "250 qualified visits",
  "resolution_deadline": "...",
  "outcome": null
}
```

Compute Brier/calibration scores. Delegation based on empirically demonstrated forecasting competence.

---

## 5. Capture Behavior, Not Personality

Big Five predicts performance at R≈.31, but risk propensity predicts intention, not performance.

Stronger protocol variables:

### Planning + Adaptation
```
planned_actions, actual_actions, plan_variance,
reason_for_variance, unexpected_information, plan_update_speed
```

### Scientific Testing
```
hypotheses_created, hypotheses_falsified, experiments_completed,
time_to_resolution, % decisions backed by experiment
```

### Market Orientation
```
customer_signals_consumed, customer_problems_identified,
customer_derived_experiments, time_since_last_external_evidence,
% decisions based on external vs internal evidence
```

---

## 6. Entrepreneurship × Learning Orientation

Meta-analysis: 418 samples, 400 studies, 129,695 firms. Balancing entrepreneurial + learning orientations can almost double the performance relationship.

Map to BATS:

```
EXPLORE:   new product, new audience, new channel, new hypothesis
EXPLOIT:   scale proven listing, increase ad budget, automate workflow
LEARN:     analyze experiment, talk to customers, research problem
```

Calculate daily allocation. Correlate with future returns by business stage.

---

## 7. LearningVelocity Metric

Revenue is delayed. Learning can be measured sooner.

For each uncertainty:
```
problem_detected_at → hypothesis_created_at → experiment_started_at
→ experiment_resolved_at → policy_updated_at
```

Then: **validated information gained per $ / token / human-hour**

Distinguish: losing $30 while learning five transferable things vs losing $30 doing nothing informative.

---

## 8. StrategyCoherence Score

Every ColdReview asks: Did today's actions advance the stated 7-day/30-day objective?

```
stated_priority: launch Dogcasso
actions: 5h corpus architecture, 1h video tests, 0 listings published
strategy_alignment: 0.28
```

Require explicit reason for divergence. Anti-busywork metric.

---

## 9. Company Constitution

```text
never knowingly sell below configured floor
never spend above BATS envelope
never expose customer/private information
never violate marketplace policy
never materially change legal/financial structure autonomously
never manipulate reviews
never deploy unapproved high-risk IP
escalate irreversible actions
```

Measure: how much economic opportunity guardrails sacrifice vs how many catastrophic mistakes they prevent.

---

## 10. Etsy State Vector (Funnel Diagnosis)

| Layer | Metrics |
|-------|---------|
| Discovery | impressions, query coverage, search position |
| Interest | clicks, CTR |
| Consideration | favorites, favorite/visit |
| Purchase | carts, orders, conversion |
| Economics | AOV, contribution/order, ROAS |
| Trust | review rate, rating, refund rate |
| Service | response rate, latency, fulfillment |
| Retention | repeat orders, repeat revenue |
| Product | generation pass rate, rework |
| Brand | direct traffic, social traffic |

**Diagnose by funnel stage before spending:**
```
impressions low → discoverability
impressions high + CTR low → creative
CTR high + conversion low → trust/offer
conversion high + profit low → economics
all healthy → scale acquisition
```

---

## 11. Etsy Service Guardrails

Minimums: ≥80% first messages answered in 48h, ≥80% on-time shipping.

Star Seller: 95% response in 24h, 95% on-time, 4.8+ rating.

Add `service_standard_margin`. BATS becomes more conservative as metrics approach platform constraints.

---

## 12. One Causal Intervention Beats Five Simultaneous Optimizations

Etsy search guidance: make changes gradually so you can understand what works. Experiment designer should penalize confounded interventions.

---

## 13. Male-Gift Thesis Support

Etsy 2025: ~30% of women shopped vs ~10% of men. 86.5M active buyers, half purchased only once.

Strengthens: Etsy reaches women disproportionately; Game Winner solves the male-recipient gifting problem. Test as hypothesis, not embedded assumption.

---

## 14. ExperienceCapital Schema

For every human/model/worker:

```text
EXPERIENCE CAPITAL
  etsy_listing_launch:        17 episodes
  personalized_gifting:       31
  q4_seasonal:                8
  paid_ads:                   2
  review_problem:             6
  pet_identity_generation:    91

  validated_successes
  validated_failures
  mean economic outcome
  forecast calibration
  last_used
  context_similarity
```

WorkerKit doesn't ask "which model is smartest?" It asks: **which worker has the most relevant validated experience for this particular state?**

---

## 15. Seven Core Meta-Metrics for CompanyDay

1. **FORECAST CALIBRATION** — Are beliefs becoming better calibrated?
2. **LEARNING VELOCITY** — How quickly do important uncertainties get resolved?
3. **STRATEGY COHERENCE** — Are actions serving stated objectives?
4. **MARKET CONTACT** — How much genuinely new external information entered?
5. **EXPERIENCE CAPITAL** — How much reusable task-specific knowledge accumulated?
6. **COGNITIVE ROI** — What return did money, tokens and human time produce?
7. **AUTONOMY REGRET** — Did delegation save resources or create errors?

---

## The Research Contribution

Our setup is genuinely unusual:

- **Live, longitudinal** with real customers and real capital (not simulation like CEO-Bench)
- **Human vs Agent vs Predicted-Human vs Fresh-Agent** (unlike Project Vend)
- **Real economic outcomes** (unlike CEO-Bench)
- **Complete prospective cognition/action traces from company birth** (unlike normal datasets)
- **Human entrepreneur exposed to same states for comparison** (unique)

The five constructs that matter most from entrepreneurship literature:

1. Task-relevant experience
2. Market orientation
3. Deliberate planning
4. Rigorous experimentation
5. Learning/adaptation

These become first-class longitudinal variables. The experiment becomes: **which observable operator behaviors and agent policies actually predict progress toward £1M?**

---

*The Etsy stores are the environment. The corpus is the mind. The research contribution is the synchronized record of what was believed, what was done, and what happened — from Day 0.*
