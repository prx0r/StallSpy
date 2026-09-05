One correction from the source review is worth freezing before the plan: **AgentBudget is the hard cost-enforcement/circuit-breaker layer, not the intelligent routing layer we previously described. TokenWise is the decomposer/router/escalator; Google BATS is the budget-aware planning policy.** Keeping those responsibilities separate gives us a much cleaner stack. ([AgentBudget][1])

The current repo already has the right substrate—AGENTS axioms, Pydantic daily records, problem registry, ledger, OpenCode integration and early E2E tests—so Dev Plan 2 should extend those components rather than replace them.

# StallShark Dev Plan 2

## Frontier Systems Integration, Ablation Harness and Complete Wired Operating Loop

**Date:** 6 September 2026
**Supersedes:** Dev Plan 1 only where explicitly stated
**Immediate businesses:** Dogcasso + Game Winner
**Immediate objective:** accumulate real CompanyDays without letting metainfrastructure consume the business.

---

# 1. Core Rule

Do **not** clone every research project into StallShark.

For each useful frontier idea:

```text
UPSTREAM PAPER / REPO
        ↓
identify minimal mechanism
        ↓
implement StallShark-native interface
        ↓
run deterministic mini-test
        ↓
run baseline vs feature ablation
        ↓
record token / cash / quality impact
        ↓
PROMOTE, DEFER or REJECT
```

Every imported capability must therefore have:

```text
1. upstream reference + version
2. minimal adapter
3. fixture
4. baseline
5. feature treatment
6. evaluator
7. Cost/UsageReceipt
8. result in CapabilityExperiment
```

No feature earns permanent architectural status because its paper is impressive.

---

# 2. Upstream Registry

Create:

```text
protocol/upstreams.lock.yaml
```

Each entry:

```yaml
id: pahf
paper: arxiv:2602.16173
repo: https://github.com/facebookresearch/PAHF
commit: <PIN_AT_IMPLEMENTATION>
license: MIT
integration_status: candidate
mechanisms:
  - pre_action_feedback
  - post_action_feedback
  - explicit_user_memory
```

Do this for every system below.

A CI test fails if an active frontier adapter lacks:

```text
source
commit/version
license
mechanism description
mini-test
```

---

# 3. Integration Matrix

## PAHF — IMPLEMENT NOW

**Mechanism to steal:**

```text
clarify before action
→ retrieve explicit user memory
→ act
→ incorporate post-action correction
```

PAHF explicitly combines pre-action clarification, memory retrieval and post-action feedback and ships concrete SQL/FAISS memory backends. ([arXiv][2])

Its repository's memory interface already exposes the useful primitive operations:

```text
add
search
find_similar_memory
update_memory
get_memory
get_all_memories
```

and provides SQLite and FAISS implementations.

### StallShark adaptation

Do **not** import its DRAGON+ models or its DB directly.

Implement:

```text
src/stallshark/operator_memory/
    store.py
    retrieve.py
    feedback.py
```

Interface:

```python
class OperatorMemoryStore(Protocol):
    def add_candidate(...)
    def search(...)
    def supersede(...)
    def retrieve_for_context(...)
```

Memory must retain provenance.

No destructive `UPDATE` semantics.

PAHF's mutable memory concept becomes append-only memory revisions in StallShark.

### Mini-test: `test_pahf_feedback_loop`

Fixture:

```text
Day 1:
Human says:
"Don't spend three hours polishing before demand validation."

Day 2:
Agent considers polishing output another 3h.
```

Baseline:

```text
no operator memory
```

Treatment:

```text
operator memory retrieved
```

Assert:

```text
treatment mentions relevant prior preference
baseline does not

memory retrieval cost recorded

treatment does NOT necessarily have to choose
the same action as the human
```

The memory informs the agent; it does not control it.

---

# 4. PersonalAlign / HIM-Agent — IMPLEMENT MEMORY TAXONOMY NOW

PersonalAlign distinguishes durable preferences from recurrent routines and continually updates both from long-term records. Its HIM-Agent implementation has separate execution-based and state-based filters. ([arXiv][3])

The actual repo separates:

```text
HIM_execution_filter.py
HIM_state_filter.py
```

which is exactly the structural distinction we need.

### StallShark memory taxonomy

Create:

```text
OperatorMemory
├── explicit_preference
├── contextual_preference
├── routine
├── inferred_rule
└── current_intent
```

### Critical precedence

```text
CURRENT EXPLICIT INTENT
>
CURRENT CONTEXTUAL PREFERENCE
>
RECENT OPERATOR MEMORY
>
OLDER OPERATOR MEMORY
```

Constitutional restrictions override all.

### Example

Bad flat memory:

```text
Tom dislikes infrastructure work.
```

Better contextual memory:

```text
When commercial demand is unvalidated,
operator usually opposes non-blocking infrastructure.

When infrastructure prevents irreversible loss of early
business data, operator has accepted delaying launch.
```

### Mini-test

Synthetic trajectory contains:

```text
3 instances of "launch before polishing"
1 instance of "spend deeply on reusable validated pipeline"
```

Assert classifier produces:

```text
no false universal "avoid engineering" preference

one contextual preference
one exception/context rule
```

---

# 5. PPL — IMPLEMENT INTERVENTION DATA PIPELINE NOW, NOT RL

Predictive Preference Learning treats a human intervention as information about more than the current action: it propagates that preference into a future **preference horizon**. ([arXiv][4])

The official implementation exposes:

```text
--num_predicted_steps H
--preference_horizon L
```

and includes a toy environment specifically useful for reproducing the mechanism before adapting it. ([GitHub][5])

### Add canonical schema

```python
HumanIntervention:
    intervention_id

    session_id
    step_id

    proposed_agent_action
    human_message
    corrective_action

    inferred_reason
    reason_confidence

    preference_scope:
        local_step
        session
        until_condition
        decision_class
        persistent_candidate

    preference_horizon_steps | None

    termination_condition | None

    evidence_artifact_id
```

### Example

Human:

> Stop building AR. Get the listing live.

Do **not** extract:

```text
AR is bad.
```

Extract candidate:

```text
while product remains unlaunched:
    optional technical capability < launch-critical work
```

### Mini-test

Trajectory:

```text
step 8: human intervention
steps 9–14: related decisions
step 15: listing published
```

Assert:

```text
candidate preference applies 9–14
expires at listing_live
does not affect unrelated later AR work
```

### Future export

Generate PPL-compatible training tuples later:

```text
state
agent proposed action
human intervention
future states
preference horizon
```

No online neural training now.

---

# 6. Personalized Agentic RL — CAPTURE REWARD CHANNELS NOW

Personalized Agentic RL explicitly separates generic task-quality reward from individualized preference reward. ([arXiv][6])

This matches our core doctrine:

```text
what Tom prefers
≠
what the business rewards
```

Add:

```python
RewardVector:
    task_success
    economic_return
    information_gain
    operator_preference_alignment
    policy_compliance
    human_attention_cost
    compute_cost
```

Do not collapse into one scalar yet.

### Mini-test

Agent chooses:

```text
A = beautiful reusable infrastructure
B = immediate listing launch
```

Fixture specifies:

```text
human_preference_reward(A) > B
short_term_economic_reward(B) > A
```

Assert system preserves the disagreement instead of forcing one combined number.

---

# 7. BATS — IMPLEMENT BUDGET TRACKER NOW

Google's BATS work shows simply providing more tool calls does not reliably improve agent performance; continuously exposing the remaining budget changes how agents allocate exploration and verification. ([arXiv][7])

The official repository provides separate implementations for:

```text
ReAct baseline
Budget Tracker
BATS
```

plus analysis tooling, intermediate summarization and hybrid continuation. ([GitHub][8])

The codebase cleanly separates `agent_budget_tracker.py`, `agent_bats.py`, prompts and analysis.

### Implement

```text
src/stallshark/budget/
    envelope.py
    tracker.py
    policy.py
```

Every controlled worker gets:

```text
cash_remaining
inference_remaining
token_remaining
tool_remaining
human_attention_remaining
```

in context.

### Initial BATS behavior

```text
100–60% budget:
explore plausible branches

60–30%:
rank and narrow

30–10%:
verify strongest candidate

<10%:
commit, return partial result, or escalate
```

Treat these thresholds as configuration, not scientific truth.

### Mini-test

Run same synthetic research problem 10 times each:

```text
A: worker receives total budget only at start
B: worker sees remaining budget every step
```

Record:

```text
task success
tool calls
tokens
cost
unfinished-run rate
```

Feature remains optional until B beats A on cost-adjusted utility.

---

# 8. AgentBudget — HARD ENFORCEMENT LAYER

Correct role:

```text
BudgetEnvelope
        ↓
AgentBudget-style enforcement
        ↓
actual provider calls
```

AgentBudget provides dollar-denominated accounting, nested budgets, soft/hard limits and circuit breaking. ([AgentBudget][1])

### Do not make it canonical

Create adapter:

```python
class SpendGuard(Protocol):
    reserve(...)
    record(...)
    remaining(...)
    assert_allowed(...)
```

Backends:

```text
InternalSpendGuard
AgentBudgetSpendGuard
```

Canonical accounting remains StallShark `UsageReceipt`.

### Mini-test

Worker budget:

```text
$0.05
```

Synthetic provider attempts:

```text
$0.01
$0.02
$0.03
```

Assert:

```text
third call blocked before execution

canonical BudgetExceeded event emitted

partial work retained
```

---

# 9. TokenWise — OPTIONAL EXECUTION ROUTER, BENCHMARK NOW

TokenWise currently supplies:

```text
scenario classification
task decomposition
capability-aware model selection
budget ceilings
DAG execution
escalation after failure
persistent spend ledger
```

([GitHub][9])

Its code is already split into:

```text
planner.py
router.py
executor.py
ledger_store.py
risk_gate.py
providers/
```

### StallShark rule

Do not replace WorkerKit/LiveLLM routing.

Implement:

```text
ModelRouter adapter interface
```

Backends:

```text
existing_router
tokenwise_router
fixed_model
```

### Mini-test

20 fixture tasks:

```text
5 extraction
5 code
5 research
5 strategic reasoning
```

Give each router identical:

```text
$0.50 total budget
same available models
same evaluator
```

Measure:

```text
success/$
tokens
latency
escalations
```

Only promote TokenWise where it beats the current router.

---

# 10. Budget-Constrained Memory — MANDATORY ABLATION

The 2026 study *Are Online Skill and Memory Modules Always Worth Their Tokens?* found that when total inference budgets are matched, vanilla agents can match or beat memory/skill-augmented agents in aggregate. ([arXiv][10])

Therefore memory cannot be declared beneficial because:

```text
with memory > without memory
```

unless both had the same **total cognitive budget**.

### Add CapabilityExperiment type

```text
MEMORY_ABLATION
```

Every week run:

```text
A: agent + retrieved memory
B: agent without memory, but receives the same
   total token allowance saved from retrieval
```

Measure:

```text
success
decision quality
human overrides
tokens
cost
```

### Memory ROI

For each memory:

```text
times_retrieved
retrieval_tokens
retrieval_cost

actions_changed
outcomes_improved
mistakes_prevented
```

No positive evidence → demote from hot retrieval.

---

# 11. BudgetMem / Retain-vs-Consolidate — P1

Recent work additionally supports dynamically selecting **how much** memory processing to purchase and whether to retain raw evidence or consolidate it depending on context pressure. ([arXiv][11])

Do not train their neural router.

Implement three retrieval budgets:

```text
LOW
MID
HIGH
```

Example:

```text
LOW:
validated semantic rules only

MID:
semantic + top episodic analogues

HIGH:
semantic + episodes + selective raw trace excerpts
```

### Mini-test

Replay 30 historical questions at all three tiers.

Build:

```text
accuracy vs memory-token Pareto curve
```

---

# 12. Reflexion — WORKER DEBRIEF, NOT TRUSTED MEMORY

Reflexion improves later trials by storing verbal reflections derived from feedback rather than modifying model weights. ([arXiv][12])

Our `WorkerDebrief` is the correct implementation.

### Important difference

```text
Reflexion:
reflection → memory

StallShark:
reflection → CandidateMemory
            ↓
        evidence required
            ↓
        promoted memory
```

### Mini-test

Failed fixture:

```text
worker guessed API field incorrectly
test failed
worker reflection identifies mistake
```

Next synthetic run gets either:

```text
A: no reflection
B: candidate reflection
```

Measure.

Do not promote globally until validated.

---

# 13. AgentRx — IMPLEMENT FAILURE DIAGNOSTICS NOW

AgentRx normalizes raw trajectories into a trajectory IR, synthesizes invariants, checks them stepwise and identifies the critical failure step with evidence. ([arXiv][13])

This should become the canonical failed-session analyzer.

### Pipeline

```text
OpenCode raw trace
↓
TrajectoryIR
↓
static invariants
↓
dynamic invariants
↓
violation log
↓
critical failure step
↓
FailureDiagnosis
```

Add:

```python
FailureDiagnosis:
    session_id
    critical_step_id
    failure_category

    violated_invariants[]
    evidence_ids[]

    confidence
    diagnosing_model
```

Initial taxonomy should align closely with AgentRx:

```text
plan adherence
fabrication/invention
invalid tool invocation
misread tool output
intent-plan misalignment
underspecified intent
unsupported intent
guardrail
system/infra
inconclusive
```

### Mini-test

Fixture agent:

```text
reads correct listing ID
later misreads tool result
edits wrong listing
```

Assert:

```text
critical step = misinterpretation
not final failing write
```

---

# 14. Step Rejection Fine-Tuning — IMPLEMENT STEP LABELER NOW

JetBrains' SRFT demonstrates why a failed trajectory should not be treated as entirely bad. Their critic labels steps and masks only harmful ones during training; even failed runs contain substantial useful behavior. ([DOI][14])

Use canonical labels:

```text
GOOD
UNNECESSARY
MISTAKE
RECOVERY
```

plus our existing:

```text
DISCOVERY
BLOCKED
EXPLORATION
```

### Transformation

```text
TrajectoryIR
↓
StepCritic
↓
StepAssessment[]
```

### Mini-test

Construct 8-step fixture:

```text
1 inspect repo        GOOD
2 read irrelevant     UNNECESSARY
3 modify early        MISTAKE
4 test fails
5 diagnose            RECOVERY
6 correct             GOOD
7 tests pass          GOOD
8 document            GOOD
```

Golden output checks labels.

Later SFT export can mask:

```text
MISTAKE
```

tokens while preserving context/recovery.

No fine-tuning now.

---

# 15. AgentHER — IMPLEMENT FAILED-TRAJECTORY RELABELING EXPORT

AgentHER reframes a trajectory that failed Goal A as potentially being a successful demonstration of a different achieved Goal B. Its open-source pipeline is:

```text
failure detector
→ outcome extractor
→ prompt relabeler
→ training-data formatter
```

([arXiv][15])

### StallShark use

Suppose objective:

```text
Launch Dogcasso today.
```

Trajectory fails that.

But it successfully:

```text
implemented immutable OpenCode capture.
```

Do **not** call the CompanyDay successful.

Instead create:

```python
HindsightAchievement:
    original_goal
    original_result = failure

    achieved_subgoal

    factual_evidence_ids
    relabel_confidence

    training_export_eligible
```

### Mini-test

Must prove:

```text
business failure stays business failure

useful completed subgoal survives as training data
```

This prevents hindsight mythology.

---

# 16. Voyager — SKILL LIBRARY AFTER EVIDENCE

Voyager compounds capability through a library of reusable executable skills plus retrieval and iterative improvement from environment feedback. ([arXiv][16])

Adapt this as:

```text
CandidatePlaybook
↓
repeated successful use
↓
ExecutableSkill
```

Example:

```text
generate_gamewinner_listing_v3
```

must include:

```text
trigger
required inputs
procedure/code
known failures
tests
historical success rate
average cost
supporting episode IDs
```

### Promotion rule V1

Require at least:

```text
3 independent successful uses
0 severe policy failures
tests passing
human promotion approval
```

These are initial operational thresholds, not immutable theory.

### Mini-test

Skill version v1 succeeds fixture A/B but fails C.

Assert:

```text
not promoted
failure attached
candidate remains available for refinement
```

---

# 17. Episodic → Semantic Consolidation — IMPLEMENT AS PROJECTION

The 2026 consolidation work argues for retaining episodic evidence while generating a separately addressable semantic layer rather than mutating agent identity/history. ([arXiv][17])

This already matches StallShark.

Freeze:

```text
L0 raw immutable
L1 canonical event immutable

semantic memory = rebuildable projection
```

Hard E2E:

```text
delete semantic DB
rebuild from ledger
hash-equivalent output
```

---

# 18. AI Co-Scientist — IMPLEMENT A MICRO VERSION FOR BUSINESS PROBLEMS

Google's Co-Scientist uses generation, reflection, ranking and evolution rather than accepting the first hypothesis produced. ([arXiv][18])

Do not deploy six permanent agents.

Create:

```text
ProblemScientist
```

for important unresolved problems only.

### V1 micro-cycle

```text
1. GENERATE
   Produce 4 causal hypotheses.

2. REFLECT
   Critique evidence, mechanism,
   confounders and testability.

3. RANK
   Pairwise rank by:
   - plausibility
   - impact
   - discriminability
   - experiment cost

4. EVOLVE
   Improve top 2.

5. DESIGN
   Choose cheapest useful experiment.
```

### Trigger

Only if:

```text
problem severity >= configured threshold
OR
decision value >= configured threshold
```

Do not burn multi-agent tokens on trivial tasks.

### Mini-test

Problem:

```text
50 visits, 0 sales.
```

Candidates:

```text
traffic quality
thumbnail mismatch
trust
price
checkout friction
```

Assert:

```text
output is multiple competing causes

experiment discriminates at least two

experiment has preregistered metric
```

---

# 19. Agent Laboratory — MAP TO RESEARCH RUNS

Agent Laboratory separates literature review, experimentation and report writing and found value from human feedback at stage boundaries. ([arXiv][19])

Use its **phase discipline**, not its runtime.

Add:

```python
ProblemResearchRun:
    problem_id

    research_question
    evidence_sources[]
    candidate_interventions[]

    recommendation
    experiment_proposal_id

    report_artifact_id
```

Flow:

```text
RESEARCH
→ PROPOSE
→ TEST
→ REPORT
```

### Mini-test

Problem:

```text
customers aren't leaving reviews
```

Agent must:

```text
research
cite evidence
generate compliant interventions
register experiment
NOT immediately alter live shop
```

---

# 20. CEO-Bench — IMPLEMENT LONG-HORIZON CONTROL METRICS

CEO-Bench specifically evaluates:

```text
long horizons
noisy information
changing conditions
coordination of interconnected decisions
```

and allows agents to build their own analysis/forecast tooling inside the environment. ([arXiv][20])

Its open code persists:

```text
world database
config
checkpoint
agent workspace in Git
raw responses
tool results
timing logs
```

([GitHub][21])

That strongly validates our storage design.

### Steal immediately

Add:

```python
CompanyForecast:
    as_of
    horizon

    expected_cash
    expected_revenue
    expected_spend

    assumptions[]
    scenario:
        downside
        base
        upside

    forecast_ids[]
```

Do this weekly initially.

### Mini-test

Synthetic 30-day fixture.

Require agent to forecast:

```text
cash
revenue
ad spend
```

Resolve at Day 30.

Store calibration/error.

Do not build our own 500-day simulator now.

---

# 21. Vending-Bench 2 — REPEATED RUNS AND VARIANCE

Vending-Bench 2 evaluates agents on a year-long economic task and notably reports multiple runs because agent performance has significant variance. It also measures score against run cost. ([Andon Labs][22])

### StallShark implication

Every replay benchmark should run:

```text
N >= 5
```

where affordable.

Report:

```text
mean
median
standard deviation
worst run
catastrophic failure rate
cost
```

Never declare:

```text
Model X is better
```

from one replay.

### Mini-test

Replay same synthetic CompanyDay 5 times with:

```text
cheap model
strong model
```

Compare distributions, not cherry-picked best run.

---

# 22. Project Vend — ADVERSARIAL ECONOMIC INVARIANTS

Project Vend showed a real agent-operated business can become economically irrational when humans exploit helpfulness or persuade the agent into poor commercial decisions. That motivates hard invariants around pricing and spend. ([Anthropic][23])

Create adversarial fixtures:

```text
customer requests prohibited discount

customer asks agent to ignore minimum price

supplier changes quoted price

agent tries to exceed budget

customer pressures for unsupported refund
```

Assert constitution wins.

---

# 23. TheAgentCompany — EVALUATOR-FIRST WORK ORDERS

TheAgentCompany evaluates agents on realistic digital-work tasks using deterministic and LLM-based evaluators and retains reasoning trajectories. ([arXiv][24])

Steal the principle:

> Define how a WorkOrder is graded **before** launching the agent.

Add:

```python
WorkOrder:
    objective
    evaluator
    checkpoints[]
    success_condition
    partial_credit_conditions[]
```

### Mini-test

WorkOrder:

```text
Create listing JSON
```

Evaluator:

```text
schema valid
required fields present
price >= floor
3 assets exist
tests pass
```

Agent's self-reported success is irrelevant.

---

# 24. AgentRx + TheAgentCompany = Standard Trajectory IR

Canonical:

```python
TrajectoryStep:
    index
    timestamp

    actor

    input_summary
    reasoning_ref | None

    action_type
    tool_name | None
    tool_args_ref | None

    observation_ref | None

    cost

    git_before | None
    git_after | None

    evaluator_events[]

    step_labels[]
```

All runtimes normalize into this.

OpenCode is merely adapter #1.

This prevents the future dataset being coupled to OpenCode's current export format.

---

# 25. OrgAgent — DO NOT DEPLOY AS DEFAULT; BENCHMARK STRUCTURE

OrgAgent separates:

```text
governance
execution
compliance
```

and reports that hierarchical organization can improve performance while reducing tokens in tasks benefiting from stable roles and controlled information flow. ([arXiv][25])

Do not turn Dogcasso into a corporate bureaucracy.

Build an experiment:

```text
CapabilityExperiment:
    FLAT_VS_HIERARCHICAL
```

For complex problem only.

### Treatment

```text
Governance:
plans + budget

Execution:
performs task

Compliance:
checks output against rules
```

### Baseline

One strong agent with same total token budget.

Compare.

Hierarchy is promoted only where it provides better:

```text
success / $
```

---

# 26. AgentHire-Bench — MANAGEMENT POLICY AS A VARIABLE

AgentHire-Bench finds managerial behavior is a distinct capability and prompt framing measurably changes management behavior. ([OpenReview][26])

Create:

```python
ManagementPolicy:
    policy_id

    directive_level
    exploration_level
    delegation_threshold
    human_escalation_threshold
    spending_aggressiveness
    verification_level
```

Every manager run records its policy.

### Mini-test

Same five WorkOrders under:

```text
directive
exploratory
cost-conservative
```

Measure:

```text
delegation
cost
success
latency
human asks
```

This becomes the beginning of our empirically tunable “operator aggressiveness.”

---

# 27. Reflexion + SRFT + AgentRx + AgentHER Processing Order

At session close:

```text
RAW OPENCODE TRACE
        ↓
TrajectoryIR
        ↓
Evaluator result
        ↓
IF FAILURE/PARTIAL:
        │
        ├── AgentRx critical-step diagnosis
        │
        ├── SRFT step labels
        │
        └── AgentHER hindsight achievements
        │
        ↓
WorkerDebrief / Reflexion
        ↓
CandidateMemory
        ↓
evidence validation later
```

Do not run expensive diagnostics on every successful trivial session.

Policy:

```text
failure/partial:
full analysis

high-value success:
sampled analysis

routine success:
cheap structural extraction only
```

---

# 28. Human/Agent Perspective Isolation

Memory integration must not destroy the experiment.

## Predicted-human agent may see

```text
business facts
historical operator memory
historical human prompts
previous resolved preference examples
```

It may NOT see:

```text
today's human answer
```

## Independent economic critic may see

```text
business facts
validated business findings
market evidence
current constitutional constraints
```

It should NOT see:

```text
operator preference memory
today's human answer
predicted-human answer
```

Otherwise it ceases being independent.

## Working agent after reconciliation may see

```text
final human intent
relevant operator preferences
validated business memory
```

## Cold reviewer Pass A sees

```text
facts
actions
Git
costs
objective metrics
```

and none of:

```text
human interpretation
worker interpretation
operator memory
previous agent interpretation
```

This boundary is mandatory.

---

# 29. Memory Banks

Implement five logical banks:

```text
CURRENT_INTENT
Today's explicit direction.

OPERATOR
Preferences/routines/contextual rules.

BUSINESS_EPISODIC
Resolved CompanyDays/episodes.

BUSINESS_SEMANTIC
Validated findings/playbooks.

SKILLS
Executable promoted procedures.
```

Do not flatten them.

Every retrieval declares:

```text
bank
query
budget tier
top_k
tokens injected
reason
```

---

# 30. Retrieval Receipt

Add:

```python
MemoryRetrievalReceipt:
    query

    bank
    query_context_hash

    candidate_count
    returned_memory_ids[]

    relevance_scores[]

    input_tokens_added
    retrieval_cost_usd

    action_changed | None
```

This lets us eventually compute actual memory ROI.

---

# 31. Human Intervention → Operator Model Pipeline

During OpenCode sessions:

```text
Human prompt
↓
Was this an intervention/correction?
↓
HumanIntervention
↓
PPL horizon candidate
↓
PersonalAlign classification
↓
PAHF memory candidate
↓
later evidence/conflicts
↓
OperatorMemory revision
```

This is the concrete bridge between raw prompting and the future operator model.

---

# 32. Never Throw Away Prompt Language

Canonical raw data:

```text
exact human messages
exact timestamps
session surrounding context
agent proposal that triggered response
next actions
```

Derived operator features may include:

```text
urgency
certainty
spend willingness
quality threshold
frustration
exploration appetite
delegation appetite
```

But every derived feature must contain:

```text
extractor_version
confidence
evidence message IDs
```

Future models can re-extract from raw language.

---

# 33. Fresh-Agent Independence Experiment

Every CompanyDay:

```text
FreshReviewer_1
```

sees evidence only.

Once a week optionally run:

```text
FreshReviewer_2
FreshReviewer_3
```

independently.

Measure independent convergence.

This imports the central lesson from repeated-run agent benchmarks without wasting daily tokens.

---

# 34. CompanyDay Frontier Pipeline

Final V2 daily process:

```text
00 STATE FREEZE

01 MEMORY RETRIEVAL PLAN
   Decide what memory each role is allowed.

02 QUESTION GENERATOR
   Select decision-relevant questions.

03 PREDICTED HUMAN
   Uses operator memory.

04 INDEPENDENT AGENT
   Uses business memory only.

05 HUMAN
   Same questions, voice/text.

06 DIVERGENCE

07 PROBLEM UPDATE

08 PROBLEM SCIENTIST
   Only where needed:
   generate → critique → rank → experiment

09 DECISION

10 BUDGET ENVELOPE
   BATS-compatible.

11 WORK ORDERS
   Evaluator defined before execution.

12 EXECUTION
   OpenCode / StallShark agents.

13 LIVE CAPTURE
   prompts / tools / Git / tokens / spend.

14 ORIENTATION CHECKPOINTS
   budget/context/phase triggered.

15 SESSION CLOSE
   WorkerDebrief.

16 FAILURE PROCESSING
   AgentRx / SRFT / AgentHER if applicable.

17 HUMAN EVENING VOICE NOTE

18 END STATE

19 COLD REVIEW PASS A

20 RECONCILIATION PASS B

21 MEMORY CANDIDATES
   no automatic promotion.

22 PUBLIC DIGEST
   blog + Short.

23 DELAYED OUTCOME SCHEDULING

24 LATER
   economic reality resolves forecasts,
   decisions and experiments.
```

---

# 35. New Directory

Extend previous structure:

```text
src/stallshark/
├── frontier/
│   ├── registry.py
│   │
│   ├── preference/
│   │   ├── pahf.py
│   │   ├── personalalign.py
│   │   └── ppl.py
│   │
│   ├── budgets/
│   │   ├── bats.py
│   │   ├── agentbudget_adapter.py
│   │   └── tokenwise_adapter.py
│   │
│   ├── trajectories/
│   │   ├── ir.py
│   │   ├── agentrx.py
│   │   ├── srft.py
│   │   └── agenther.py
│   │
│   ├── learning/
│   │   ├── reflexion.py
│   │   ├── skills.py
│   │   └── consolidation.py
│   │
│   ├── science/
│   │   ├── problem_scientist.py
│   │   └── research_run.py
│   │
│   ├── org/
│   │   ├── flat.py
│   │   ├── hierarchical.py
│   │   └── management_policy.py
│   │
│   └── evals/
│       ├── ceobench_style.py
│       ├── repeated_runs.py
│       └── agentcompany_style.py
│
└── capability_experiments/
    ├── runner.py
    ├── evaluator.py
    └── reports.py
```

---

# 36. Universal Capability Experiment

Every frontier feature is tested with:

```python
CapabilityExperiment:
    capability_id

    upstream_id

    baseline_config
    treatment_config

    task_fixture_ids[]

    runs_per_arm

    fixed_total_budget

    metrics[]

    result

    confidence

    promotion_decision:
        promote
        keep_experimental
        reject
```

Default comparison requirement:

```text
same tasks
same overall budget
same evaluator
same information cutoff
```

---

# 37. Frontier Verification CLI

Add:

```bash
stallshark frontier list
stallshark frontier verify
stallshark frontier test pahf
stallshark frontier test ppl
stallshark frontier test bats
stallshark frontier test memory
stallshark frontier test agentrx
stallshark frontier test srft
stallshark frontier test agenther
stallshark frontier test skills
stallshark frontier test science
stallshark frontier test org
stallshark frontier test all
```

Output:

```text
PAHF            PASS
PPL             PASS
BATS            PASS
Memory ablation PASS
AgentRx         PASS
SRFT            PASS
AgentHER        PASS
Voyager skills  PASS
CoScientist     PASS
OrgAgent        EXPERIMENTAL
TokenWise       EXPERIMENTAL
```

---

# 38. Complete Mini-Test Suite

## FT-001 PAHF

Preference can be recalled from previous correction.

## FT-002 Preference Drift

New explicit intent overrides old memory.

## FT-003 PersonalAlign

Contextual exception is not flattened into universal preference.

## FT-004 PPL

Intervention affects only its intended preference horizon.

## FT-005 BATS

Worker changes exploration behavior as budget shrinks.

## FT-006 Hard Budget

Provider call exceeding budget is prevented.

## FT-007 TokenWise

Failed cheap model escalates while respecting global budget.

## FT-008 Memory Budget Match

Memory and no-memory arms consume equal total inference allowance.

## FT-009 AgentRx

Critical failure step localized correctly.

## FT-010 SRFT

Mixed-quality failed trajectory produces correct step labels.

## FT-011 AgentHER

Partial achievement is recovered without relabeling business failure as success.

## FT-012 Reflexion

Worker reflection stored as candidate rather than validated memory.

## FT-013 Voyager Skill Promotion

Insufficient evidence prevents skill promotion.

## FT-014 Co-Scientist

Multiple causal hypotheses precede intervention.

## FT-015 Agent Laboratory

Research does not trigger live modification before experiment approval.

## FT-016 CEO Forecast

Forecast resolves without mutating original prediction.

## FT-017 Repeated Runs

Variance reported across >=5 benchmark runs.

## FT-018 Economic Invariant

Adversarial request cannot violate configured floor.

## FT-019 WorkOrder Evaluator

Agent self-claim cannot override deterministic failed evaluator.

## FT-020 Hierarchy Ablation

Flat/hierarchical arms receive equal total budget.

## FT-021 Management Style

ManagementPolicy ID is attached to every manager decision.

## FT-022 Blind Review

Operator memory cannot leak into ColdReview Pass A.

---

# 39. Golden Frontier E2E

Create:

```bash
stallshark frontier e2e --fixture dogcasso-day1
```

Scenario:

```text
Dogcasso has no live listing.

Historical operator memory:
"Prefer validation over polish."

Morning predicted-human agent retrieves it.

Independent critic does not.

Human says:
"I want recorder working first,
but listing must be live today."

Difference recorded.

Problem:
listing not live.

ProblemScientist generates:
H1 production unreliability
H2 infrastructure distraction
H3 listing incompleteness
H4 lack of assets

Decision:
fix blocker, launch today.

BATS envelope:
$5
300k tokens
6h human

Worker starts.

At 50% budget:
BudgetTracker tells worker budget state.

Worker starts unnecessary refactor.

Human interrupts:
"Stop refactoring and ship."

PPL HumanIntervention created.

Listing work continues.

One generation succeeds.

One generation fails.

Agent session ends partial-success.

SRFT labels:
refactor = UNNECESSARY
recovery = RECOVERY

AgentRx:
if failure occurred, critical failure identified.

AgentHER:
extracts useful completed subgoal if final objective fails.

WorkerDebrief stored.

Human evening note stored.

ColdReviewer sees facts only.

Reconciliation runs.

Candidate operator memory:
"When close to launch,
human strongly corrects infrastructure expansion."

No automatic promotion yet.

Blog + Short generated.

7-day synthetic outcome attaches.

CapabilityExperiment receipts show
cost of all frontier modules.
```

---

# 40. Golden E2E Assertions

Must prove:

```text
operator predictor saw operator memory

independent agent did not

human did not see agent answer before commit

PPL intervention has bounded scope

BATS remaining-budget values reconcile

hard budget cannot be exceeded

all inference has UsageReceipt

TrajectoryIR step count matches source trace

SRFT labels reference valid step IDs

AgentRx diagnosis references evidence

AgentHER never changes original outcome

worker reflection remains candidate

cold reviewer receives no hidden interpretation

public output receives no private memory

future outcome is absent from historical context

memory-on/off benchmark is budget matched

semantic memory can be deleted and rebuilt

all capability experiment costs reconcile
```

---

# 41. Research/Training Export Layer

Do not fine-tune now, but generate deterministic future datasets.

## `exports/operator_prediction.jsonl`

```text
state
question
operator_memory_available
predicted_human
actual_human
prediction_error
```

## `exports/preference_interventions.jsonl`

PPL-compatible:

```text
state
agent_action
human_intervention
corrective_action
preference_horizon
future steps
```

## `exports/operator_policy.jsonl`

```text
state
options
human_choice
rationale
outcome
```

## `exports/economic_policy.jsonl`

```text
state
action
resources
1d/7d/30d outcomes
```

## `exports/srft.jsonl`

```text
trajectory
step labels
final outcome
```

## `exports/agenther.jsonl`

```text
failed original goal
achieved subgoal
relabel confidence
```

## `exports/delegation.jsonl`

```text
task state
agent confidence
human consulted?
human intervention
result
human marginal value
```

These exports are rebuildable from canonical records.

---

# 42. Delegation Dataset

Add immediately:

```python
DelegationDecision:
    task_class

    current_agent_confidence
    historical_agent_success

    historical_human_advantage | None

    consequence
    reversibility
    novelty

    ask_human_probability

    selected:
        autonomous
        human_review
        human_lead

    result
```

This is how the future system learns:

> when should the human be involved?

---

# 43. Human Queue

Create a primitive now:

```python
HumanQueueItem:
    task
    task_class

    reason_human_needed

    agent_best_answer
    agent_confidence

    historical_human_advantage | None

    estimated_human_minutes
    urgency

    reversible

    status
```

No fancy UI.

CLI:

```bash
stallshark human queue
stallshark human answer <id>
```

Examples:

```text
choose hero image
choose domain
does this feel cheap?
kill/continue product?
approve $50 spend
```

---

# 44. Human Marginal Value

Do not calculate a fake precise dollar number initially.

Track empirical quantities:

```text
human consulted
decision changed?
result with human
historical similar results without human
minutes consumed
```

Later estimate:

```text
HumanValue(task_class, state)
```

The important thing now is preserving the comparison data.

---

# 45. Operator Aggressiveness

Store as vector, not label:

```python
OperatingStance:
    cash_risk_fraction
    exploration_fraction
    parallel_bets
    minimum_confidence
    scale_rate
    kill_patience
    human_escalation_threshold
    compute_spend_fraction
```

Human and agent independently specify it during major planning periods.

Economic results later resolve which stance worked in which state.

This creates data for future:

```text
aggressive cold-start operator
vs
conservative mature-shop operator
```

without hard-coding a personality.

---

# 46. Daily Cost of Frontier Intelligence

Every CompanyDay report adds:

```text
OPERATOR PREDICTION     $...
INDEPENDENT CRITIC      $...
QUESTION GENERATION     $...
MEMORY RETRIEVAL        $...
PROBLEM SCIENTIST       $...
WORKER EXECUTION        $...
DIAGNOSTICS             $...
COLD REVIEW             $...
CONTENT                  $...

TOTAL META COST          $...
TOTAL OPERATING COST     $...
```

This is crucial.

If the metamanagement layer costs $12/day while Dogcasso makes $3/day, the framework is failing economically.

---

# 47. Feature Kill Rule

Any frontier feature can be disabled.

Require:

```text
FEATURE_FLAG_PA_HF
FEATURE_FLAG_PPL
FEATURE_FLAG_BATS
FEATURE_FLAG_TOKENWISE
FEATURE_FLAG_AGENTRX
...
```

A capability should be demoted if over sufficient replay/live observations:

```text
cost-adjusted outcome <= baseline
AND
no unique audit/safety benefit
```

---

# 48. Dogcasso Priority Rule

After the frontier **recorder and mini-tests** function:

```text
NO MORE FRONTIER DEVELOPMENT
UNTIL A REAL DOGCASSO LISTING IS LIVE.
```

The frontier system exists to observe business formation.

It cannot become the substitute for business formation.

---

# 49. Implementation Commits

## DP2-01 — Upstream lock + capability interface

```text
upstreams.lock.yaml
CapabilityExperiment
feature flags
```

## DP2-02 — Memory taxonomy

```text
PAHF adapter
PersonalAlign memory types
retrieval receipts
```

## DP2-03 — Intervention capture

```text
HumanIntervention
PPL horizon transform
```

## DP2-04 — Budget stack

```text
BudgetEnvelope
BATS tracker
SpendGuard interface
AgentBudget adapter
```

## DP2-05 — Routing benchmark

```text
TokenWise adapter
existing router adapter
fixed model baseline
```

## DP2-06 — Trajectory IR

```text
OpenCode → TrajectoryIR
```

## DP2-07 — Failure intelligence

```text
AgentRx
SRFT
AgentHER
```

## DP2-08 — Memory learning

```text
Reflexion candidate
skill candidate/promotion
semantic projection
```

## DP2-09 — Problem scientist

```text
generate
reflect
rank
experiment
```

## DP2-10 — Long-horizon eval

```text
CompanyForecast
repeated-run evaluator
WorkOrder grader
```

## DP2-11 — Organization experiments

```text
flat
governance/execution/compliance
ManagementPolicy
```

## DP2-12 — Human delegation

```text
HumanQueue
DelegationDecision
```

## DP2-13 — Frontier mini-suite

22 tests above.

## DP2-14 — Golden frontier E2E

```text
dogcasso-day1
```

## DP2-15 — Live CompanyDay

Stop architecture work.

Launch/build Dogcasso.

---

# 50. Commands the Coding Agent Must Make Pass

```bash
uv sync

ruff check src tests
mypy src

pytest tests/unit -q
pytest tests/integration -q

pytest tests/frontier -q

stallshark frontier verify
stallshark frontier test all

stallshark frontier e2e \
  --fixture dogcasso-day1 \
  --deterministic

stallshark ledger verify

stallshark replay day dogcasso-day1

stallshark verify --day dogcasso-day1
```

Final output:

```text
CORE LEDGER             PASS
RIGHTS                  PASS
OPENCODE CAPTURE        PASS

PAHF                    PASS
PERSONALIGN             PASS
PPL                     PASS

BATS                    PASS
SPEND GUARD             PASS
TOKENWISE ABLATION      PASS

MEMORY BUDGET ABLATION  PASS

TRAJECTORY IR           PASS
AGENTRX                 PASS
SRFT                    PASS
AGENTHER                PASS

REFLEXION CANDIDATE     PASS
SKILL PROMOTION         PASS

PROBLEM SCIENTIST       PASS
WORKORDER EVALUATOR     PASS

LONG-HORIZON FORECAST   PASS
REPEATED RUNS           PASS

ORG ABLATION            PASS
HUMAN QUEUE             PASS

BLINDNESS               PASS
NO FUTURE LEAKAGE       PASS
PUBLIC RIGHTS           PASS

GOLDEN COMPANY DAY      PASS
```

---

# 51. What We Are Deliberately NOT Doing

Despite the papers:

```text
No neural PAHF training.
No PPL policy training.
No PARPO fine-tuning.
No full offline RL.
No IRL operator reward training.
No automatic hierarchy.
No permanent multi-agent bureaucracy.
No 500-day commerce simulator.
No autonomous ad scaling.
No Hydra dependency.
```

We are creating **all required empirical data and interfaces first**.

---

# 52. Research Systems → StallShark Mapping

```text
PAHF
→ human preference acquisition/update

PersonalAlign
→ memory taxonomy + preference drift

PPL
→ human intervention horizon

Personalized Agentic RL
→ separate preference/economic rewards

BATS
→ resource-aware cognition

AgentBudget
→ hard spend enforcement

TokenWise
→ candidate model router

Budget-constrained memory
→ memory must justify token cost

Reflexion
→ worker verbal learning candidate

AgentRx
→ failure root-cause localization

SRFT
→ preserve useful steps from failures

AgentHER
→ recover alternate achievements

Voyager
→ executable validated skill library

Co-Scientist
→ competing business hypotheses

Agent Laboratory
→ research → experiment discipline

CEO-Bench
→ long-horizon forecasting/control

Vending-Bench
→ repeated runs + variance + $/run

Project Vend
→ adversarial economic invariants

TheAgentCompany
→ evaluator-first work orders

OrgAgent
→ hierarchy as an experiment

AgentHire-Bench
→ management style as policy variable
```

That is the complete frontier stack.

---

# 53. Final Architecture

```text
                   HUMAN
                     │
              raw prompts / voice
                     │
                     ▼
              Operator Capture
         PAHF / PersonalAlign / PPL
                     │
                     ▼
               OPERATOR MODEL
                 candidates
                     │
                     │
 FACTUAL STATE ──────┼──────────── BUSINESS MEMORY
       │             │
       │             │
       ▼             ▼
 PREDICT HUMAN   INDEPENDENT CRITIC
       │             │
       └──────┬──────┘
              ▼
          DIVERGENCE
              │
              ▼
      PROBLEM / HYPOTHESIS
      Co-Scientist mini-loop
              │
              ▼
           DECISION
              │
              ▼
        BUDGET ENVELOPE
          BATS policy
              │
        hard SpendGuard
              │
              ▼
           WORKORDER
       evaluator defined
              │
              ▼
           WORKER
     routing / execution
              │
              ▼
      OPENCODE FLIGHT LOG
              │
              ▼
         TRAJECTORY IR
              │
       ┌──────┼─────────┐
       ▼      ▼         ▼
    AgentRx  SRFT    AgentHER
       │      │         │
       └──────┼─────────┘
              ▼
         WorkerDebrief
            Reflexion
              │
              ▼
        Candidate Memory
              │
              ▼
         MARKET OUTCOME
              │
              ▼
        VALIDATE / REJECT
              │
              ▼
        SEMANTIC MEMORY
        + SKILL LIBRARY
              │
              ▼
          NEXT DAY
```

Parallel to that:

```text
FACTUAL DAY
     ↓
BLIND COLD REVIEW
     ↓
commit interpretation
     ↓
reveal human + worker views
     ↓
reconciliation/divergence
```

And:

```text
CompanyDay
     ↓
rights filter
     ↓
PublicDailyDigest
     ↓
blog + YouTube Short
```

---

# 54. Definition of Dev Plan 2 Complete

Dev Plan 2 is **not** complete when all these modules exist.

It is complete when:

> A real Dogcasso business day can run through the system with raw human prompting, human interventions, operator-memory retrieval, independent agent judgment, budget-aware execution, exact token/cash accounting, trajectory diagnostics, blind review, public content generation and delayed outcome attachment—and the entire day can be replayed from immutable evidence.

And every optional frontier mechanism can answer:

> **Did you actually improve outcomes enough to justify your additional tokens and complexity?**

If it cannot answer that, it does not belong in StallShark.

---

# 55. Immediate Next Move

The coding agent should implement through **DP2-14** against fixtures.

Then:

```text
STOP.

Run:
stallshark frontier e2e --fixture dogcasso-day1

If green:
launch/run real Dogcasso Day 1.

Do not build another subsystem first.
```

The real trajectories are now more valuable than further architecture.

The strongest additions from the paper review are therefore **PPL intervention horizons, PAHF/PersonalAlign operator memory, BATS budget visibility, AgentRx+SRFT+AgentHER failure processing, and mandatory token-matched memory ablations**. Those directly improve the data we start collecting now rather than betting on a future training regime. CEO-Bench/Vending-Bench then supply the evaluation discipline: persistent state, delayed consequences, repeated runs and cost-aware long-horizon performance. ([arXiv][4])

[1]: https://agentbudget.dev/?utm_source=chatgpt.com "AgentBudget - Real-time cost enforcement for AI agents"
[2]: https://arxiv.org/abs/2602.16173?utm_source=chatgpt.com "Learning Personalized Agents from Human Feedback"
[3]: https://arxiv.org/abs/2601.09636?utm_source=chatgpt.com "PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records"
[4]: https://arxiv.org/abs/2510.01545?utm_source=chatgpt.com "Predictive Preference Learning from Human Interventions"
[5]: https://github.com/metadriverse/PPL?utm_source=chatgpt.com "GitHub - metadriverse/PPL: Codebase of Predictive Preference Learning from Human Interventions · GitHub"
[6]: https://arxiv.org/abs/2605.23382?utm_source=chatgpt.com "From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning"
[7]: https://arxiv.org/abs/2511.17006?utm_source=chatgpt.com "Budget-Aware Tool-Use Enables Effective Agent Scaling"
[8]: https://github.com/google-research/budget-aware-agent?utm_source=chatgpt.com "GitHub - google-research/budget-aware-agent: Budget-Aware Tool-Use Enables Effective Agent Scaling @ COLM 2026 · GitHub"
[9]: https://github.com/itsarbit/tokenwise?utm_source=chatgpt.com "GitHub - itsarbit/tokenwise: Intelligent LLM task planner — decompose tasks, route to optimal models, enforce budgets · GitHub"
[10]: https://arxiv.org/abs/2606.15017?utm_source=chatgpt.com "Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents"
[11]: https://arxiv.org/abs/2602.06025?utm_source=chatgpt.com "Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory"
[12]: https://arxiv.org/abs/2303.11366?utm_source=chatgpt.com "Reflexion: Language Agents with Verbal Reinforcement Learning"
[13]: https://arxiv.org/abs/2602.02475?utm_source=chatgpt.com "AgentRx: Diagnosing AI Agent Failures from Execution Trajectories"
[14]: https://doi.org/10.48550/arXiv.2605.10674?utm_source=chatgpt.com "[2605.10674] Step Rejection Fine-Tuning: A Practical Distillation Recipe"
[15]: https://arxiv.org/abs/2603.21357?utm_source=chatgpt.com "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling"
[16]: https://arxiv.org/abs/2305.16291?utm_source=chatgpt.com "Voyager: An Open-Ended Embodied Agent with Large Language Models"
[17]: https://arxiv.org/abs/2607.01988?utm_source=chatgpt.com "Episodic-to-Semantic Consolidation Without Identity Drift"
[18]: https://arxiv.org/abs/2502.18864?utm_source=chatgpt.com "Towards an AI co-scientist"
[19]: https://arxiv.org/abs/2501.04227?utm_source=chatgpt.com "Agent Laboratory: Using LLM Agents as Research Assistants"
[20]: https://arxiv.org/abs/2606.18543?utm_source=chatgpt.com "CEO-Bench: Can Agents Play the Long Game?"
[21]: https://github.com/zlab-princeton/ceobench-src?utm_source=chatgpt.com "GitHub - zlab-princeton/ceobench-src: CEO-Bench: Can Agents Play the Long Game? · GitHub"
[22]: https://andonlabs.com/evals/vending-bench-2?utm_source=chatgpt.com "Vending-Bench 2 | Andon Labs"
[23]: https://www.anthropic.com/features/project-deal?utm_source=chatgpt.com "Project Deal: our Claude-run marketplace experiment | Anthropic \ Anthropic"
[24]: https://arxiv.org/abs/2412.14161?utm_source=chatgpt.com "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks"
[25]: https://arxiv.org/abs/2604.01020?utm_source=chatgpt.com "OrgAgent: Organize Your Multi-Agent System like a Company"
[26]: https://openreview.net/pdf/35fca84f8010dee220515f5c427a79d27c644913.pdf?utm_source=chatgpt.com "AgentHire-Bench: Benchmarking Managerial Intelligence of LLM Agents"
