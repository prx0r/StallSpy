# The Integration — Moltwork × StallSpy Corpus

**Date:** 5 September 2026
**Core insight:** WorkerKit already solved execution, budgeting, and receipts. The corpus architecture already solved experience capture. The operator twin already solved preference learning. This document connects them into one coherent system.

---

## What Already Exists

### WorkerKit (execution kernel)

| Component | What it does |
|-----------|-------------|
| `lab_kernel.py` | WorkerVersion, WorldVersion, RunSpec, RunReceipt |
| `economics/budgets.py` | BATS — daily_cap, per_run_cap, lifetime_cap |
| `economics/costs.py` | CostModel, RunMeter — tracks costs by category |
| `economics/decisions.py` | Continue/abort based on marginal economics |
| `capabilities.py` | Multi-dimensional capability evidence |
| `hydra_projectors.py` | Derived experience graph |
| `git_primitives.py` | Content-addressed everything |

### MWGym (training + evolution)

| Component | What it does |
|-----------|-------------|
| `worlds/` | CGE worlds with hidden truth, observable state |
| `harnesses/` | PydanticBATS, Letta, forecast harnesses |
| `evolution/` | CG deterministic evolution |
| `budgets/` | Budget tracking per experiment |

### HydraDB (empirical memory)

| Component | What it does |
|-----------|-------------|
| Graph database | Nodes + relationships, derived from receipts |
| Cypher queries | `MATCH (n:Run) RETURN n.id` |
| Content-addressed | Rebuilt from canonical receipts |

### StallSpy Corpus (experience capture)

| Component | What it does |
|-----------|-------------|
| `machinecourse.md` | 18 schemas for the corpus |
| `OPERATOR_TWIN.md` | Dual model: operator + economic critic |
| `METAMANAGEMENT.md` | Adaptive interview protocol |
| `TRAJECTORY_CAPTURE.md` | Lossless experience pyramid |

---

## The Connection

The WorkerKit already models the world as:

```
WorkerVersion × WorldVersion → RunSpec → RunReceipt → CapabilityEvidence
```

The corpus adds:

```
OperatorState × BusinessState → Decision → Action → Outcome → Episode
```

They're the same loop viewed from different angles:

```
                    ┌─────────────────────────────┐
                    │      MOLTWORK LAB            │
                    │  WorkerKit + MWGym + HydraDB │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │      STALLSPY CORPUS         │
                    │  Episodes + Operator Twin    │
                    │  + Economic Critic            │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │      DAILY OPERATIONS        │
                    │  Content + Interview + Logs   │
                    └─────────────────────────────┘
```

---

## 1. Budget Tracking Integration

### What WorkerKit already has

```python
# economics/budgets.py
class Budget:
    daily_cap: float = 5.0
    per_run_cap: float = 2.0
    lifetime_cap: float = 5.0

# economics/costs.py
class RunMeter:
    def record(self, category: str, cost: float, **kwargs):
        self.total_cost += cost
        self.events.append({"category": category, "cost": cost, **kwargs})
```

### What the corpus needs

Extend `RunMeter` to also track:

```python
class CorpusRunMeter(RunMeter):
    def record(self, category: str, cost: float, **kwargs):
        super().record(category, cost, **kwargs)
        # Also emit corpus event
        emit_corpus_event({
            "type": "financial_transaction",
            "category": category,
            "amount": cost,
            "run_id": kwargs.get("run_id"),
            "agent": kwargs.get("agent"),
            "model": kwargs.get("model"),
            "tokens": kwargs.get("tokens", 0),
        })
```

### Token tracking (new)

```python
@dataclass
class TokenUsage:
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    timestamp: float

class TokenMeter:
    def __init__(self):
        self.daily: dict[str, int] = {}  # model → tokens
        self.history: list[TokenUsage] = []
    
    def record(self, model: str, input_tokens: int, output_tokens: int, cost: float):
        usage = TokenUsage(model, input_tokens, output_tokens, cost, time.time())
        self.history.append(usage)
        key = f"{model}:{datetime.now().strftime('%Y-%m-%d')}"
        self.daily[key] = self.daily.get(key, 0) + input_tokens + output_tokens
    
    def daily_summary(self) -> dict:
        today = datetime.now().strftime('%Y-%m-%d')
        return {k: v for k, v in self.daily.items() if today in k}
```

### Budget becomes the BATS bridge

The corpus `question_objective: QO_BOTTLENECK` can now check:

```python
# "Can I afford to run this experiment today?"
budget = lab_kernel.get_budget("gamewinner")
meter = lab_kernel.get_meter("gamewinner")

remaining = budget.daily_cap - meter.total_cost
if remaining < estimated_cost:
    # Cannot afford this experiment today
    emit_question_objective("QO_BUDGET_CONSTRAINT", {
        "remaining_budget": remaining,
        "estimated_cost": estimated_cost,
        "alternative": "use cheaper model or defer to tomorrow"
    })
```

**The budget isn't just a constraint. It's a question objective.**

---

## 2. Decision Points Integration

### What WorkerKit already has

Decision points in `lab_kernel.py`:

```python
@dataclass
class DecisionPoint:
    """Atomic unit of agent choice."""
    options: list[str]
    chosen: str
    exploration_budget: float
    reasoning: str
```

### What the corpus adds

```python
@dataclass
class CorpusDecisionPoint(DecisionPoint):
    """Extended with operator twin + economic critic."""
    operator_prediction: str  # P — what human would choose
    agent_recommendation: str  # A — what agent recommends
    human_actual: str = ""  # H — what human actually chose
    divergence_score: float = 0.0
    belief_before: dict = field(default_factory=dict)
    belief_after: dict = field(default_factory=dict)
    outcome_linked: bool = False
```

Now every WorkerKit decision point gets the full P/A/H triple.

---

## 3. Capability Evidence → Operator Twin

### What WorkerKit already has

```python
@dataclass
class CapabilityEvidence:
    capability: str
    worker_version: str
    evaluator_score: float
    outcome: str  # won / lost
    payout: float
    cost: float
```

### What the corpus adds

```python
@dataclass
class OperatorCapabilityEvidence(CapabilityEvidence):
    """Extends with operator judgment tracking."""
    human_judgment_quality: float = 0.0  # how well did human predict this?
    agent_judgment_quality: float = 0.0  # how well did agent predict this?
    operator_model_confidence: float = 0.0
    economic_model_confidence: float = 0.0
```

Over time: which capabilities does the human judge well vs the agent?

---

## 4. The Daily Budget-Corpus Loop

```text
MORNING
├── Operator answers adaptive interview (METAMANAGEMENT.md)
├── Agent predicts operator answers (OPERATOR_TWIN.md)
├── Divergence calculated
├── BATS budget allocated for today
│   ├── Dogcasso: $X
│   ├── Game Winner: $Y
│   └── StallSpy: $Z
├── Token budget allocated
│   ├── Free model (mimo-v2.5): unlimited
│   ├── Cheap model (groq): $X
│   └── Strong model: $Y (high-stakes only)
└── Today's plan generated

WORK
├── Each action tracked by RunMeter
│   ├── category: "generation" / "research" / "listing" / "content"
│   ├── cost: $actual
│   ├── tokens: N
│   └── model: which model used
├── Budget enforcement (BATS)
│   ├── daily_cap check
│   ├── per_run_cap check
│   └── can_spend() → yes/no
├── Decision points recorded
│   ├── P: operator prediction
│   ├── A: agent recommendation
│   ├── chosen: what actually happened
│   └── cost: what it consumed
└── Git commits + OpenCode sessions captured

EVENING
├── Business state snapshot
├── Human evening answers (6 questions)
├── Token usage summary
├── Cost summary
├── RunMeter totals
└── Workday.json created

NIGHTLY (META-PROTOCOL)
├── Fresh agent reviews previous day's full context
├── Distills high-signal takeaways
├── Identifies agent worries/observations
├── Updates operator model
├── Updates economic model
├── Generates next day's interview questions
└── Backs up to R2
```

---

## 5. The Meta-Protocol: Agent Reflection

This is the piece you identified. At end of day, a **fresh agent** with no context reads:

- All OpenCode session transcripts
- Git diffs
- Financial data
- Operator interview answers
- Previous day's state
- Active hypotheses

And produces:

### Session Distillation

```json
{
  "session_id": "meta_day_014",
  "reviewed_day": "2026-09-19",

  "high_signal_takeaways": [
    "Operator spent 3h on infrastructure but stated goal was first sale",
    "Generation quality improved but operator didn't test with real customer photos",
    "Budget allocated 60% to Dogcasso but Game Winner has higher EV per the economic model"
  ],

  "things_logs_dont_reveal": [
    "Operator seems to be avoiding the launch moment — possible fear of rejection",
    "Infrastructure work feels productive but doesn't generate revenue",
    "Operator's confidence dropped after seeing competitor listings"
  ],

  "agent_worries": [
    "Dogcasso may be over-optimized for perfection before validation",
    "Budget is being consumed by learning, not by selling",
    "StallSpy infrastructure is becoming a躲避 from the uncomfortable work"
  ],

  "operator_observations": [
    "Operator is most energized when discussing product concepts",
    "Operator is least energized when discussing marketing/SEO",
    "Operator made 3 scope expansions after seeing successful competitor"
  ],

  "context_retention": {
    "beliefs_changed": ["trust hypothesis strengthened"],
    "new_hypotheses": ["physical bundle may convert better than digital-only"],
    "unresolved_tensions": ["infrastructure vs validation"]
  },

  "recommendations_for_tomorrow": [
    "Test one listing with real customer photo — no more generation optimization",
    "Set a hard 2h limit on infrastructure work",
    "Review competitor listing that operator found threatening — understand why"
  ]
}
```

This becomes a new corpus schema:

### `agent_session_reflection`

```json
{
  "reflection_id": "...",
  "day": 14,
  "reviewed_by": "fresh_agent",
  "context_available": ["git", "opencode_traces", "metrics", "interviews", "previous_reflections"],
  "high_signal_takeaways": [],
  "latent_observations": [],
  "agent_worries": [],
  "operator_observations": [],
  "context_retention": {},
  "recommendations": [],
  "timestamp": "..."
}
```

Over time: agent reflections become a dataset about **what agents think and feel during sessions**.

Compare agent reflections to human reflections:

```
AGENT: "Operator seems to be avoiding the launch moment"
HUMAN: "I'm scared it won't work"

AGENT: "Infrastructure is becoming an escape"
HUMAN: "I know, I just like building things"

AGENT: "Confidence dropped after seeing competitors"
HUMAN: "Those competitors look way more professional than us"
```

That divergence is itself a training signal.

---

## 6. HydraDB as the Experience Graph

### Current HydraDB structure

```
(Run) -[:DEPENDS_ON]-> (Run)
(Run) -[:USES_CAPABILITY]-> (Capability)
(Run) -[:PRODUCES]-> (Artifact)
```

### Extended for corpus

```
(Run) -[:INFORMED_BY]-> (Episode)
(Episode) -[:TRIGGERED_BY]-> (Decision)
(Decision) -[:BASED_ON]-> (Hypothesis)
(Hypothesis) -[:VALIDATED_BY]-> (Experiment)
(Experiment) -[:PRODUCED]-> (Outcome)
(Outcome) -[:UPDATED]-> (Belief)
(Belief) -[:SHARED_BY]-> (OperatorModel)
(Belief) -[:SHARED_BY]-> (EconomicModel)
```

Now HydraDB can answer:

> "Show me all episodes where the operator and agent disagreed, and the economic outcome favored the agent's choice."

---

## 7. The BATS→Corpus Budget Bridge

### BATS today

```python
budget.can_spend(amount, daily_spent, lifetime_spent, run_spent)
# Returns: True/False
```

### BATS with corpus awareness

```python
class CorpusBudget:
    def __init__(self, budget: Budget, meter: RunMeter, corpus: Corpus):
        self.budget = budget
        self.meter = meter
        self.corpus = corpus
    
    def can_spend(self, amount: float, category: str, purpose: str) -> dict:
        # Check BATS limits
        allowed = self.budget.can_spend(
            amount,
            self.meter.daily_total(),
            self.meter.lifetime_total()
        )
        
        # Check corpus: is this spend aligned with current objectives?
        alignment = self.corpus.check_alignment(category, purpose)
        
        # Check historical: has similar spend produced value?
        historical_roi = self.corpus.historical_roi(category)
        
        return {
            "allowed_by_budget": allowed,
            "alignment_score": alignment,
            "historical_roi": historical_roi,
            "recommendation": "proceed" if (allowed and alignment > 0.6) else "review"
        }
```

---

## 8. Token Spend as a Data Point

### What to track

```python
@dataclass
class TokenEvent:
    timestamp: float
    model: str  # "mimo-v2.5", "groq/llama-3.3", "claude-3.5"
    input_tokens: int
    output_tokens: int
    cost_usd: float
    session_id: str
    task: str  # "interview_generation", "code_generation", "reflection"
    agent: str  # "operator_twin", "economic_critic", "meta_reviewer"
```

### What it reveals

After 30 days:
- Which tasks consume the most tokens?
- Which models are cost-effective for which tasks?
- Is the meta-protocol worth its token cost?
- Does the operator twin prediction cost more or less than it saves?

### The meta-question

> "Is the daily agent reflection worth its token cost?"

Track:
```
reflection_cost: $0.12 (15K tokens × $0.008/1K)
value_of_insight: ??? (harder to measure)
plan_changes_caused: 2
action_changes_caused: 1
```

If plan changes → positive ROI. If no changes → wasteful overhead.

---

## 9. The Full Integration Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MOLTWORK LAB                              │
│  WorkerKit (execution) + MWGym (training) + HydraDB (memory) │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ BATS     │  │ RunMeter │  │ CostModel│  │Capability│   │
│  │ Budgets  │  │ Tokens   │  │ History  │  │ Evidence │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       └──────────────┴──────────────┴──────────────┘         │
│                          │                                   │
│                    ┌─────┴─────┐                             │
│                    │RunReceipts│ ← canonical, immutable      │
│                    └─────┬─────┘                             │
└──────────────────────────┼──────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    │  CORPUS     │
                    │  Events     │
                    │  Episodes   │
                    │  Decisions  │
                    │  Beliefs    │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
     ┌──────────────┐ ┌────────┐ ┌──────────┐
     │OPERATOR TWIN │ │ECONOMIC│ │META-     │
     │ predicts H   │ │CRITIC  │ │PROTOCOL  │
     │              │ │predicts│ │reviews   │
     │              │ │outcomes│ │sessions  │
     └──────┬───────┘ └───┬────┘ └────┬─────┘
            └──────────────┴───────────┘
                           │
                    ┌──────┴──────┐
                    │  DAILY      │
                    │  Plan       │
                    │  Execution  │
                    │  Reflection │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  CONTENT    │
                    │  Blog       │
                    │  YouTube    │
                    │  Scoreboard │
                    └─────────────┘
```

---

## 10. What to Build First

### This week

1. **Token tracking in daily_content.py** — add `TokenMeter` to every API call
2. **Budget readout in morning record** — show remaining daily budget
3. **Agent reflection schema** — add `agent_session_reflection` to corpus
4. **Wire RunMeter to corpus events** — every cost emits a corpus event

### Next week

5. **Meta-protocol agent** — fresh agent reads previous day, distills takeaways
6. **BATS↔corpus bridge** — budget decisions reference historical ROI
7. **Operator twin v0.1** — after 14 days of P/A/H data

### Month 2

8. **HydraDB corpus graph** — episodes, decisions, beliefs as nodes
9. **Competence map** — human vs agent strengths
10. **Autonomy passport** — earn per decision class

---

*The WorkerKit already solved execution and budgeting. The corpus already solved experience capture. The operator twin already solved preference learning. This integration makes them one system: the autonomous $0 → £1M operating protocol.*
