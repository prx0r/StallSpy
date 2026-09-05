# The Adaptive Company Operating Protocol

**Date:** 5 September 2026

---

## The Core Object: SubjectiveState

Every company-state freeze generates three independently written `SubjectiveState` records:

```
                         FROZEN STATE S_t
                               │
                ┌──────────────┼──────────────┐
                ↓              ↓              ↓
             HUMAN          AGENT          FRESH AGENT
                │              │              │
             H_t            A_t             F_t
                └──────────────┼──────────────┘
                               ↓
                         compare only now
                               ↓
                        DECISION / PLAN
                               ↓
                           ACTIONS
                               ↓
                       ECONOMIC STATE S_t+1
```

The fresh agent does NOT see yesterday's agent interpretation before committing its own.

It can see facts: code, Git history, transactions, product state, executed actions, costs, outcomes.

But NOT: "Yesterday's agent thinks the main problem is trust."

Only after `F_t` is committed do we reveal that.

### The SubjectiveState Schema

```json
{
  "snapshot_id": "S_2026_09_06_0900",
  "actor_type": "human|agent|fresh_agent",
  "actor_version": "tom_2026_09",

  "objective": {
    "next_hours": "...",
    "today": "...",
    "seven_days": "...",
    "thirty_days": "...",
    "mission": "..."
  },

  "state_assessment": {
    "momentum": 0.61,
    "business_health": 0.54,
    "strategy_confidence": 0.72,
    "uncertainty": 0.66,
    "urgency": 0.81
  },

  "bottleneck": {"primary": "...", "confidence": 0.74, "evidence": []},
  "top_opportunities": [],
  "top_risks": [],
  "active_problems": [],
  "beliefs": [],
  "unknowns": [],

  "forecast": {"next_1d": [], "next_7d": [], "next_30d": []},

  "resource_stance": {
    "exploration": 0.40,
    "exploitation": 0.60,
    "cash_aggressiveness": 0.31,
    "compute_aggressiveness": 0.67,
    "willingness_to_pivot": 0.54
  },

  "preferred_actions": [],
  "actions_to_avoid": [],
  "what_would_change_my_mind": [],
  "what_metrics_miss": "...",
  "biggest_concern": "...",
  "biggest_excitement": "..."
}
```

After one year: 1,095 contemporaneous high-level assessments. Each later attached to reality.

---

## The Problem Registry

The company's agents shouldn't wake up thinking "what random thing should we work on?"

They maintain a persistent **Problem Registry**:

```
OBSERVATION → PROBLEM → CAUSE HYPOTHESES → RESEARCH →
DISCRIMINATING EXPERIMENT → BATS RESOURCE BUDGET →
INTERVENTION → PRE-COMMITTED OBSERVATION WINDOW →
RESULT → DECISION → LESSON / POLICY UPDATE
```

A Problem persists until resolved. Six months later an agent can ask:

> "Show me every recurring acquisition problem we've failed to solve permanently."

---

## Two Experiment Systems

### Market experiments
Testing the world: price, thumbnail, offer, product, ad, customer experience

### Meta experiments
Testing the company operating system:
- Model A vs Model B
- Fresh context vs persistent context
- Hydra retrieval vs no retrieval
- 200k vs 1M token budget
- Human approval vs autonomous action
- Aggressive vs conservative BATS policy

---

## The 17-Phase Daily Protocol

| Phase | What |
|-------|------|
| 00 | Freeze state S_t |
| 01 | Fresh blind diagnosis F_t |
| 02 | Human subjective state H_t |
| 03 | Operator model predicts H_t + provides A_t |
| 04 | Reveal / divergence |
| 05 | Problem prioritization |
| 06 | Hypothesis + experiment design |
| 07 | BATS allocation |
| 08 | WorkerKit execution |
| 09 | Worker debrief |
| 10 | Human close |
| 11 | Blind evidence review |
| 12 | Reconciliation |
| 13 | Hydra candidates |
| 14 | Blog + YouTube Short |
| 15 | Future outcomes (1d/7d/30d) |
| 16 | Reality scores everyone |

---

## Four Simultaneously Learning Systems

1. **Market Model** — what do customers respond to?
2. **Operator Model** — what would the human decide and why?
3. **Economic Policy** — what actually produces returns?
4. **Organization Model** — what mixture of humans, agents, memory, budgets and teams produces returns efficiently?

---

## Corporate Structure Emerges from Problems

Not: "We need a marketing department."

But:

> 37% of unresolved problems belong to acquisition/creative testing.
> $4,300/month potential impact.
> 14 WorkOrders/week.
> Specialist Growth Worker outperforms generalist by 23%.

Then: **Spawn Growth Unit.**

Same with CX, production, finance. Organization emerges from measured problem structure.

---

## Viable System Model Mapping

| VSM Function | Our System |
|-------------|-----------|
| Operations | MythicBee, Game Winner, individual brands |
| Coordination | WorkerKit scheduler, shared production |
| Control | BATS, finance, permissions, QA, risk |
| Intelligence | StallShark, research, problem detection, fresh reviewers |
| Policy | Human + operator model + governance |

Recursive — every level uses the same protocols.

---

## Risk Appetite as Experiment

Not "make the AI more reckless." But:

```
increase exploration_fraction 0.25 → 0.40
increase max_test_loss $10 → $25
decrease min_action_confidence .75 → .60
increase ad_scaling_rate 1.2x → 1.5x
```

Run controlled period. Measure economic consequences. Risk appetite itself is experimental.

---

## The Dataset

> A machine-readable developmental history of the company's mind — what its human and artificial operators independently believed at every stage, which problems they noticed, how they allocated thought and capital, which interventions they tried, and how the outside economy rewarded or punished those beliefs.

---

## Etsy API Constraint

Etsy's API Terms prohibit using API content for analytics/ML training without written authorization. Build a rights firewall into the corpus. Contact `developer@etsy.com` early.

Operation (running your own shops) is clearly intended use. Analytics/training on API-derived content needs permission.

---

*The Etsy stores are almost incidental. They give us a real, low-capital, high-frequency economic environment in which actions can be taken, money can be won or lost, hypotheses can resolve fairly quickly, and the whole human-agent organization's cognition can be instrumented from Day 0.*
