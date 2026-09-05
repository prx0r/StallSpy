# Metamanagement — Adaptive Interview Protocol

**Date:** 5 September 2026
**Core insight:** Don't build a fixed daily founder journal. Build an adaptive metamanagement interview protocol whose stable unit is the *decision variable*, not the wording of the question.

---

## The Mistake to Avoid

Treating the interview as a questionnaire.

The valuable object is a set of **information requirements**. The agent decides what questions best extract those variables from the human **given the exact state of the business right now**.

Don't hard-code: "What is the single most important outcome right now?"

Hard-code the underlying measurement:

> **Identify the operator's current objective function at multiple timescales and detect conflicts between them.**

Then generate the actual question dynamically.

---

## Question Objectives (Not Fixed Questions)

Each interview question comes from a `question_objective`:

```json
{
  "id": "QO_OBJECTIVE_PRIORITY",
  "principle": "Goal hierarchy / resource allocation",
  "purpose": "Determine what outcome the operator is optimizing and on what timescale.",
  "information_needed": [
    "immediate objective",
    "7-day objective",
    "30-day objective",
    "long-term objective",
    "conflicts between objectives"
  ],
  "why_valuable": "Actions cannot be evaluated without knowing the objective they were intended to serve.",
  "action_relevance": "Used to rank today's candidate actions.",
  "trigger_conditions": ["multiple active projects", "resource conflict", "strategy change"]
}
```

Same theory, different question each day:

**Day 1 (multiple projects):**
> "You have Dogcasso, StallSpy and Game Winner competing for attention. What outcome matters most by end of today, by Sunday, and by end of September? If those conflict, which wins?"

**Day 15 (one project live):**
> "Dogcasso is live but has no sales. Are you optimizing the next 24 hours for first revenue, learning, or getting Game Winner live? Rank those three."

---

## Five Timescale Horizons

```text
NOW       next action / next 1–3 hours
TODAY     end of workday
WEEK      ~7 days
SPRINT    ~30 days
MISSION   long-term objective
```

Detect **local/global objective conflict**:

```
NOW:      improve Dogcasso video quality
TODAY:    publish first listing
WEEK:     achieve first sale
30 DAYS:  determine whether Dogcasso is commercially viable
MISSION:  build reusable autonomous commerce infrastructure
```

Six hours improving animation quality optimizes `NOW` while actively harming `TODAY`, `WEEK`, and potentially `MISSION`.

---

## The 18 Question Objectives

### Objective Hierarchy
What are we optimizing across different horizons?

### Bottleneck Identification
What currently constrains progress most?

### Uncertainty
What unknown has the highest expected value of information?

### Belief State
What important claims does the operator currently believe and how strongly?

### Evidence Update
What new observation should modify those beliefs?

### Action Selection
What action has the highest expected value now?

### Counterfactual
What is the strongest alternative action?

### Opportunity Cost
What are we sacrificing by doing this?

### Affordable Loss
How much can we lose while learning?

### Falsification
What evidence would make us stop?

### Risk / Premortem
How is this most likely to fail?

### Hidden Signal
What does the human notice that isn't represented in the metrics?

### Strategy Validity
Are we solving the correct problem?

### Automation Boundary
What currently requires human judgment and why?

### Portfolio Allocation
Which brand/project deserves the next unit of time/capital?

### Recurring Problems
Have we encountered something structurally similar before?

### Reversibility
Is this action cheap to undo or should the evidence bar be higher?

### Exploit vs Explore
Should we improve a proven winner or test something new?

---

## The Interviewer Optimizes Information Gain

Before questioning, the interviewer reads:

```text
latest Git state
OpenCode sessions
open TODOs
yesterday's operator state
active hypotheses
unresolved problems
shop metrics
cash
sales
experiments
time spent
agent recommendations
upcoming deadlines
```

Then determines:

> What do I already know?
> What can I infer with high confidence?
> What remains uncertain?
> Which missing human information could materially change today's actions?

Then asks only the questions with the highest **expected information value**.

### Scoring formula

```text
Question value =
    uncertainty
  × decision relevance
  × expected human informational advantage
  × consequence magnitude
  × temporal urgency
  ÷ interview burden
```

Don't ask: "What do you think the current conversion bottleneck is?"
if there is no traffic yet.

Instead ask: "You've spent most of today implementing the corpus recorder, but the stated goal this week is getting Dogcasso's first sale. Is the recorder blocking launch, or are you intentionally prioritizing infrastructure over validation?"

That question could immediately alter behavior.

---

## Agent-Human Parallel Interview

The same dynamically generated questions go to both:

```json
{
  "question_id": "...",
  "measurement_objective": "portfolio_allocation",
  "generated_question": "You have 4 hours left today. Allocate them between Dogcasso launch, Game Winner prototype and StallSpy infrastructure.",
  "state_snapshot": "snap_...",
  "information_cutoff": "...",
  "why_this_question_now": "Three projects are competing for limited operator time."
}
```

### Human answer
> 3h Dogcasso, 1h StallSpy, 0h Game Winner.
> Need something actually selling before starting another brand.

### Agent answer
> 2h Dogcasso, 2h Game Winner.
> Game Winner has higher expected commercial value and Dogcasso is suffering diminishing returns.

### Divergence analysis
```
Human values: first revenue / focus / psychological momentum
Agent values: expected monetary value / diversification
Missing: operator believes another failed launch will damage motivation
```

Follow-up: "Would your allocation change if Game Winner had an estimated 2× expected conversion probability?"

---

## Revisit Old Answers

Suppose Day 12:
> "I think AI generation cost is the main threat." Confidence: 82%.

Day 44:
> Generation cost is trivial; acquisition is the problem.

Interviewer asks:
> "On Day 12 you assigned 82% confidence to generation cost being the primary constraint. It is now 7% of COGS and customer acquisition appears dominant. What did your original mental model miss?"

Captures **how operator models change**.

---

## Problem-Informed Question Generation

Problem registry:
```
P-018: Game Winner facial consistency failing on older male photos.
P-019: Dogcasso getting clicks but no checkout.
P-020: Too much operator time on infrastructure.
```

Interviewer searches:
```
current problem → similar historical problems → past solutions/outcomes
→ missing distinguishing information → ask human + agent
```

> "Problem P-019 resembles Dogcasso P-004 where trust was the issue, but unlike that case favorites are also low. Do you think this is still a trust problem or an offer problem?"

The interview does active diagnosis.

---

## Self-Improving Protocol

For every generated question:

```json
{
  "question_objective": "QO_HIGHEST_VALUE_UNCERTAINTY",
  "question": "...",
  "human_answer": "...",
  "agent_answer": "...",
  "changed_plan": true,
  "action_changed": "act_...",
  "eventual_economic_impact": 83.20,
  "retrospective_information_value": 0.88
}
```

After 1,000 days:

> Which questions historically caused valuable plan changes?

- Premortem questions: moderately useful
- "What aren't we doing?" questions: extremely useful
- Generic emotional questions: low direct economic value
- Portfolio allocation questions: massive value at scaling stages

**The metamanagement protocol improves from data.**

---

## Three-Level Schema

### Level 1 — Theory
Why do we need this information?
```
principle
decision-science rationale
business relevance
```

### Level 2 — Information Objective
What variable are we trying to estimate?
```
current objective, bottleneck, uncertainty, risk, belief, counterfactual...
```

### Level 3 — Generated Question
What's the best way to extract that variable **right now**?

Changes every day. That's the architecture.

### Level 4 — Action Hook
Every question must answer: **What decision could this answer alter today?**

If the answer is "nothing" — don't ask it.

```json
{
  "question_objective": "QO_BOTTLENECK",
  "generated_question": "What is currently preventing Dogcasso from getting its first order?",
  "action_hook": {
    "decision": "choose_next_4_hours",
    "possible_actions": ["improve_product", "publish_more_listings", "work_on_traffic", "lower_price"]
  }
}
```

---

## The Daily Control Loop

```
CURRENT STATE
      ↓
question-objective selector
      ↓
dynamic interview (highest information value)
      ↓
HUMAN answers + AGENT answers (parallel)
      ↓
divergence analysis
      ↓
updated beliefs + today's plan
      ↓
execution
      ↓
economic reality scores everything
      ↓
future agents inherit the entire trajectory
```

The corpus isn't a tax for future value. It actively makes today's business run better.

---

*Don't build a fixed daily founder journal. Build an adaptive metamanagement interview protocol. The stable unit is not the wording of the question but the decision variable it is trying to reveal.*
