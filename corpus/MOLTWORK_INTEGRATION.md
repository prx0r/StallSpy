# Moltwork × StallSpy — The Integration

**Date:** 5 September 2026

---

Yes. This is where the earlier Moltwork ideas suddenly become concrete.

The commerce experiment can be the **first real WorkerKit world with an external economic reward function**. Git stores what changed; WorkerKit records what happened and what it cost; Hydra learns across runs; BATS governs scarce resources; Pydantic gives you typed immutable records; the human and agents supply competing policies; Etsy/customer behavior supplies reality.

And yes: **tokens are absolutely an economic input worth recording.** Current agent tooling already treats input/output/cached/reasoning tokens and requests as first-class usage telemetry, and OpenTelemetry's GenAI conventions similarly support model, token, latency and tool-call instrumentation. ([OpenAI GitHub Pages][1])

## The key conceptual change

Don't record only:

> agent did X → business made Y.

Record:

```text
STATE
↓
HUMAN PLAN
AGENT PLAN
↓
PLANNED BUDGETS
↓
EXECUTION TRAJECTORIES
↓
ACTUAL RESOURCE USE
↓
CONTEMPORANEOUS HUMAN REFLECTION
CONTEMPORANEOUS WORKER REFLECTION
INDEPENDENT FRESH-AGENT REVIEW
↓
REAL ECONOMIC OUTCOMES
↓
HYDRA LEARNING
↓
NEXT DAY
```

That gives you **three minds observing the same business**:

| Perspective         | What it contributes                                                          |
| ------------------- | ---------------------------------------------------------------------------- |
| Human operator      | taste, intuition, priorities, fear, conviction, hidden constraints           |
| Working agent       | what it believed while actually interacting with the problem                 |
| Fresh auditor agent | independent interpretation without being anchored by the session's narrative |
| Market              | external reward signal that eventually tells you which judgments mattered    |

The working agent doesn't literally "feel," but its **contemporaneous assessment, uncertainty, expectations and concerns** are valuable for exactly the same reason your contemporaneous human reflection is valuable: they're recorded before later outcomes contaminate the narrative.

---

# This maps perfectly onto WorkerKit

Previously the architecture was roughly:

```text
WorkOrder
+
WorkerVersion
+
ContextPack
+
BudgetEnvelope
        ↓
WorkerRun
        ↓
trajectory + artifacts + costs
        ↓
RunReceipt
        ↓
evaluation/outcome
        ↓
Hydra
        ↓
candidate memory / skill / process change
        ↓
promote or reject
```

That is exactly what I would use here.

But now `evaluation/outcome` isn't merely:

> tests passed 17/20.

It can be:

```text
listing launched
$8.21 spent
4,921 impressions
291 visits
17 sales
$226 revenue
$119 contribution
human time 74 min
AI tokens 418,231
AI cost $3.81
refunds 1
7-day conversion 5.84%
```

That's an unusually strong learning signal.

---

# Add BATS at the WorkOrder level

This part could become genuinely valuable.

Before the agent begins:

```json
{
  "work_order": "improve_gamewinner_listing_conversion",

  "objective": "identify and test highest-EV conversion intervention",

  "budget": {
    "human_minutes": 45,
    "agent_input_tokens": 250000,
    "agent_output_tokens": 50000,
    "reasoning_tokens": 30000,
    "tool_calls": 30,
    "web_searches": 8,
    "generation_usd": 5.00,
    "total_cash_usd": 7.00
  },

  "stop_conditions": [
    "credible answer found",
    "budget exhausted",
    "marginal information value falls below threshold"
  ]
}
```

Now you have **intended resource allocation**.

At completion:

```json
{
  "actual": {
    "human_minutes": 31,
    "input_tokens": 181293,
    "output_tokens": 21844,
    "reasoning_tokens": 11892,
    "tool_calls": 19,
    "generation_usd": 2.40,
    "cash_usd": 3.12
  },

  "budget_variance": {
    "human_minutes": -14,
    "cash_usd": -3.88
  }
}
```

And later:

```text
7-day incremental profit: +$48.21
```

Now you can derive:

> **$15.45 incremental profit / $1 agent cash spend**

or:

> **$0 despite 1.8M tokens consumed**

That is incredibly useful.

---

# BATS becomes more than a spending cap

The current BATS research you were referring to is especially relevant: it explicitly gives agents awareness of remaining token/tool budget and changes their behavior between exploring new paths and exploiting promising ones. Simply giving an agent more tool calls does not necessarily improve performance. ([arXiv][2])

We can apply the same idea economically.

At 100% remaining budget:

> Explore several plausible causes.

At 50%:

> Concentrate resources on the strongest two.

At 20%:

> Stop broad research. Verify the best option and execute.

At 5%:

> Either commit or escalate.

So every WorkerRun gets:

```text
remaining_cash_ratio
remaining_token_ratio
remaining_tool_ratio
remaining_time_ratio
```

continuously available.

That makes `budget awareness` part of the policy.

---

# Record tokens all the way down

Not merely:

> September 7 AI spend = $8.20.

Capture at:

```text
MODEL CALL
↓
TURN
↓
AGENT RUN
↓
SESSION
↓
WORK ORDER
↓
EXPERIMENT
↓
DAY
↓
BRAND
↓
BUSINESS
```

For every model call I'd preserve:

```json
{
  "model": "model-x",
  "provider": "...",

  "input_tokens": 18291,
  "cached_input_tokens": 14822,
  "cache_write_tokens": 0,
  "output_tokens": 1822,
  "reasoning_tokens": 711,

  "latency_ms": 8211,
  "cost_usd": 0.0412,

  "tool_calls": 3,

  "parent_work_order": "...",
  "parent_experiment": "...",
  "outcome_role": "research"
}
```

Those categories map cleanly onto what contemporary agent telemetry already exposes. ([OpenAI GitHub Pages][1])

Eventually you can ask fascinating questions:

> Which model produces the most profit per million tokens?

> Does spending another 100k reasoning tokens materially improve product decisions?

> Which task types justify expensive models?

> Does retrieval of Hydra memories save tokens?

> Does the human use fewer resources than the agent for brand-selection judgments?

> At what stage did automation actually reduce total operating cost?

That's a **business-level benchmark of intelligence cost**.

---

# Your end-of-session agent reflection is absolutely worth storing

But I would make it a formal artifact:

## `WorkerDebrief`

Before the OpenCode session ends or gets compacted, the **same worker with full active context** answers something like:

```json
{
  "objective": "...",

  "what_i_think_happened": "...",

  "most_important_discovery": "...",

  "most_important_unresolved_problem": "...",

  "decision_i_am_least_confident_about": "...",

  "assumption_that_may_be_wrong": "...",

  "what_the_raw_logs_will_not_make_obvious": "...",

  "what_i_noticed_about_operator_preferences": "...",

  "what_i_would_do_next": "...",

  "what_i_would_warn_tom_about": "...",

  "information_i_wish_i_had": "...",

  "candidate_memory": [],
  "candidate_skill": [],
  "confidence": {}
}
```

That field—

> **What will the raw logs not make obvious?**

—is particularly good.

Because the worker might say:

> "We spent most of the session debugging rendering, but I don't think rendering is actually the strategic bottleneck. Tom repeatedly diverted back to it because it was concrete and solvable."

That's not necessarily *true*.

But it's a valuable **contemporaneous agent hypothesis**.

---

# Then deliberately DON'T trust that reflection

This is where Hydra matters.

Reflection research shows that linguistic self-reflection can improve subsequent agent performance; Reflexion, for example, stores verbal feedback in episodic memory rather than requiring weight updates, and later web-agent work finds useful transfer from reflecting on both successes and failures. ([arXiv][3])

But there is an important 2026 warning: memory/skill modules themselves consume tokens, and under equal total inference budgets they do **not automatically outperform simply giving the base agent more useful reasoning budget**. ([arXiv][4])

Therefore:

> **Worker reflection does not become memory automatically.**

It becomes:

```text
CandidateMemory
```

with provenance:

```text
claimed by WorkerVersion 0.17
based on Session X
confidence 0.67
not yet validated
```

Hydra later discovers whether it was actually useful.

That's exactly consistent with the prior Moltwork rule that empirical evidence—not the worker merely asserting something—governs promotion.

---

# Then have a fresh agent review the day

Yes. I think this is worth doing.

But the **freshness is the feature**.

Call it:

# `ColdReview`

The day's working agent has inherited the entire messy narrative:

> tried A → failed → debugged B → discovered C → got emotionally/narratively anchored on C.

The fresh reviewer gets:

* morning state;
* WorkOrders;
* budgets;
* raw traces;
* Git diffs;
* artifacts;
* metrics;
* human interview;
* WorkerDebriefs;

but **none of the worker's hidden accumulated context beyond recorded evidence**.

It asks:

> What actually happened?

> Which actions were useful?

> Which were waste?

> Did actual work match stated priorities?

> What important hypothesis emerged?

> What appears to be a local fix rather than a structural solution?

> Which worker conclusions aren't adequately supported?

> What should tomorrow's agent know?

Now you have:

```text
INSIDE VIEW
WorkerDebrief

OUTSIDE VIEW
ColdReview
```

That difference itself becomes data.

---

# Even better: blind the fresh reviewer initially

I'd run it in two passes.

### Pass A — Evidence only

It gets trajectories, actions, metrics, artifacts.

It does **not** see:

* your evening reflection;
* working agent's debrief.

It forms its own assessment.

### Pass B — Reconciliation

Reveal:

**Human reflection**

**Worker reflection**

Then ask:

> Where do the three accounts agree?

> Where do they disagree?

> Which claims are observable fact vs interpretation?

> What experiment could resolve the disagreement?

This prevents the fresh agent merely parroting the previous two.

---

# That gives you an insane daily comparison object

Imagine:

### Human

> "I think today was great. Game Winner finally feels real."

### Working Agent

> "The most important result was solving identity consistency."

### Cold Reviewer

> "Commercially the highest-value event was actually discovering customers responded to the simple before/after still image. The video work consumed 74% of tokens but has no evidence of affecting demand."

### Seven days later

Sales confirm the fresh review.

Now you learn something about:

* human judgment;
* worker judgment;
* independent review;
* allocation efficiency.

Or perhaps the human was right.

**Reality grades all three.**

---

# This also gives you `ContextRetention` empirically

We've talked before about persistent workers and context packs.

Now you can actually test whether persistent context is worth its cost.

Run paired experiments:

```text
A:
tomorrow's worker gets raw previous session + full memory

B:
fresh worker gets only ColdReview + promoted Hydra memories
```

Measure:

* tokens;
* task success;
* repeated mistakes;
* time;
* cash;
* quality;
* business outcome.

Perhaps full context is useful.

Perhaps a 1,500-token distilled context pack performs identically at 20% the cost.

You don't have to theorize.

**The business itself can evaluate context retention.**

That's exactly the sort of paired experiment the earlier WorkerKit/Hydra design was meant to support.

---

# The daily meta-protocol I would freeze

| Phase                   | Artifact                       | Purpose                                    |
| ----------------------- | ------------------------------ | ------------------------------------------ |
| **00: State Freeze**    | `BusinessSnapshot`             | Exact world before decisions               |
| **01: Human Interview** | `OperatorState`                | Human latent policy                        |
| **02: Agent Interview** | `AgentState`                   | Independent agent judgment                 |
| **03: Twin Prediction** | `OperatorPrediction`           | Predict human before reveal                |
| **04: Reconciliation**  | `DecisionManifest`             | Resolve divergence                         |
| **05: Allocate**        | `WorkOrders + BudgetEnvelopes` | Commit objectives/resources                |
| **06: Execute**         | `WorkerRuns`                   | OpenCode/agents do actual work             |
| **07: Instrument**      | `RunReceipts`                  | Actions, tools, tokens, cash, time         |
| **08: Worker Close**    | `WorkerDebrief`                | Same-context contemporaneous reflection    |
| **09: Human Close**     | `OperatorReflection`           | Same-day human interpretation              |
| **10: Blind Review**    | `ColdReview`                   | Independent evidence interpretation        |
| **11: Reconcile**       | `DayReview`                    | Agreements/divergences/problems            |
| **12: Consolidate**     | `HydraCandidates`              | Candidate lessons/skills/memories          |
| **13: Publish**         | blog + Short                   | Human/public view                          |
| **14: Later Outcome**   | `OutcomeReceipt_1d/7d/30d`     | Reality grades decisions                   |
| **15: Promote**         | `PromotionReceipt`             | Validated knowledge enters reusable memory |

This is the protocol.

---

# Budgeting itself becomes a learning problem

This may be one of the best extensions.

The morning agent doesn't merely say:

> Today we should improve Game Winner.

It says:

> **I would allocate the day's resources as follows.**

For example:

```text
TOTAL CASH RISK       $10
TOTAL HUMAN TIME      6h
TOTAL MODEL BUDGET    2M tokens

Dogcasso launch       3h / 600k / $3
Corpus recorder       1h / 300k / $0
Game Winner research  2h / 1.1M / $7
```

You independently do the same.

Now:

```text
HUMAN RESOURCE ALLOCATION
vs
AGENT RESOURCE ALLOCATION
vs
ACTUAL RESOURCE ALLOCATION
vs
ECONOMIC RETURN
```

after hundreds of days.

This lets the system learn **capital allocation**, not merely task completion.

That is CEO-level data.

---

# And you get a really interesting quantity: `Regret`

Suppose:

```text
planned Game Winner: 2h
actual Game Winner: 0h

planned corpus infra: 1h
actual corpus infra: 5h
```

At evening you say:

> "I got sucked into infrastructure."

The agent agrees.

Seven days later no product launched.

Now:

```text
allocation_regret = HIGH
```

But another time you spend five unplanned hours on infrastructure and that saves 200 hours later.

Then:

```text
allocation_regret = NEGATIVE
```

Over time Hydra can discover:

> When is infrastructure work actually leverage, and when is it avoidance?

That's precisely the kind of abstract principle a generic entrepreneur course cannot give you.

---

# Worker versions also become economically measurable

Imagine:

```text
WorkerVersion v12
Model: cheap model
Context: generic

WorkerVersion v17
Model: same model
Context: Hydra memory + budget tracking

WorkerVersion v21
Different model
```

Now compare:

```text
successful actions / $1
profit generated / 1M tokens
human interventions / run
rollback rate
problem recurrence
new useful skills / 100 runs
```

This is a **live economic fitness function for WorkerKit**.

Voyager demonstrated the general principle that continuously accumulating reusable skills can compound agent ability without model fine-tuning. ([arXiv][5])

We'd be attempting a commerce analogue, but with much stronger accounting.

---

# And Hydra should remain a projection, not the source of truth

This is important from the earlier design.

Don't let:

> "Hydra thinks we learned X"

become canonical history.

Canonical:

```text
raw trajectories
Git
receipts
budgets
human statements
agent statements
economic outcomes
```

Hydra is:

```text
current best empirical interpretation of those records
```

So when GPT-whatever-2028 becomes dramatically smarter, rebuild Hydra from the original evidence.

Recent work on episodic-to-semantic consolidation makes a similar distinction: retain episodic evidence and produce a separately addressable semantic knowledge layer rather than mutating the underlying agent identity/history. ([arXiv][6])

That's exactly what we want.

---

# Eventually every day is a little company experiment

The thing I'd call the entire unit is:

# `CompanyDay`

A `CompanyDay` contains:

```text
world state
human policy prediction
human actual policy
agent policy
joint policy
resource allocation
WorkOrders
WorkerRuns
full trajectories
token/tool/cash/time receipts
Git/artifacts
human reflection
worker reflections
cold review
problems
belief updates
1d/7d/30d rewards
```

After 365 days:

**365 complete company trajectories.**

Inside them:

potentially thousands of WorkOrders and tens of thousands of agent/tool decisions.

Then you can replay Day 82 with:

> Moltwork Worker v2028

and ask:

> Given only what was knowable that morning, run the company for this day.

Compare it against:

**2026 human**

**2026 agents**

**actual decision**

**actual outcome**

That is a serious evaluation environment.

---

## The strongest meta-protocol

The system should eventually ask itself nightly:

> **What did today teach us about how to operate tomorrow, and is that lesson worth the tokens required to remember it?**

That second clause matters.

Because memory, reflection, context and intelligence themselves have economic costs. Current research is already showing that more memory/modules aren't automatically better under equal inference budgets. ([arXiv][4])

So Hydra/WorkerKit/BATS together let you learn not only:

> **How do we build profitable stores?**

but also:

> **What information is worth retaining?**

> **What should be forgotten?**

> **When is a cheap worker sufficient?**

> **When should an expensive worker be invoked?**

> **How much reasoning should a $5 commercial decision consume?**

> **When should an agent ask the human?**

> **When is historical context valuable enough to justify its token cost?**

That turns the Etsy experiment into something substantially bigger: **a longitudinal economic laboratory for learning how human–AI organizations should allocate cognition, memory, capital and autonomy.**

[1]: https://openai.github.io/openai-agents-python/usage/ "Usage - OpenAI Agents SDK"
[2]: https://arxiv.org/abs/2511.17006 "Budget-Aware Tool-Use Enables Effective Agent Scaling"
[3]: https://arxiv.org/abs/2303.11366 "Reflexion: Language Agents with Verbal Reinforcement Learning"
[4]: https://arxiv.org/abs/2606.15017 "Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents"
[5]: https://arxiv.org/abs/2305.16291 "Voyager: An Open-Ended Embodied Agent with Large Language Models"
[6]: https://arxiv.org/abs/2607.01988 "Episodic-to-Semantic Consolidation Without Identity Drift"
