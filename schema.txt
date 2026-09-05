The clean theoretical framing is: **StallShark’s interview layer is a budgeted active-learning system over three evolving models—business state, operator state, and human–agent comparative advantage.** Session reviews are event-contingent momentary measurements; questions are selected by expected decision value; forecasts make beliefs falsifiable; independent perspectives prevent anchoring; and later economic outcomes supervise which judgments, questions, memories, and delegation decisions were actually useful.

That gives us something much more rigorous than a journal.

# StallShark Meta-Enquiry Protocol v1.0

## 1. Scientific basis

The protocol combines seven established ideas.

| Theory                                                    | StallShark implication                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ecological Momentary Assessment / Experience Sampling** | Capture human beliefs immediately after work rather than reconstructing them days later. EMA exists specifically to reduce retrospective bias and preserve cognition in context. ([PubMed][1])                                                                                                               |
| **Metacognitive monitoring/control**                      | Separate “what state do you think we're in?” from “what should we do about it?” Nelson–Narens distinguishes monitoring from control/allocation. ([Socsci UCI][2])                                                                                                                                            |
| **Value of Information / active learning**                | Ask questions only when obtaining the answer could reduce meaningful decision loss. VOI explicitly values information by how much better it could make a decision; information-theoretic active learning selects observations to reduce uncertainty efficiently. ([PubMed][3])                               |
| **Optimal preference elicitation**                        | Human attention is an annotation budget. Select questions that discriminate among competing models/preferences rather than asking everything. ([arXiv][4])                                                                                                                                                   |
| **Scientific entrepreneurship**                           | Encode causal theories, predictions and falsification criteria before experiments. RCT evidence finds hypothesis-driven scientific approaches improve entrepreneurial decision quality; a 2025 field experiment additionally found value from explicit causal “theory-of-value” reasoning. ([PubsOnline][5]) |
| **Forecasting/calibration**                               | Turn uncertain beliefs into resolvable probability forecasts and score them. Proper scoring rules such as Brier reward calibrated probabilities, while forecasting-tournament research shows training, tracking and aggregation improve calibration and resolution. ([NOAA Institutional Repository][6])     |
| **Double-loop learning**                                  | Sometimes fix the action; sometimes question the policy/objective producing the action. Argyris distinguishes correcting errors under existing goals from revising the underlying governing variables themselves. ([Harvard Business Review][7])                                                             |
| **Human–AI complementarity / learning to defer**          | Learn where humans outperform agents and vice versa rather than optimizing for blanket autonomy. Information/capability asymmetries create complementarity, and learning-to-defer formalizes routing decisions to humans. ([arXiv][8])                                                                       |
| **Continual personalization**                             | Current intent, stable preferences, routines and intervention-derived rules must remain separable. PAHF, PersonalAlign and PPL provide concrete mechanisms for this. ([arXiv][9])                                                                                                                            |

The protocol therefore optimizes:

> **Decision-relevant uncertainty reduction per unit of human attention.**

Not introspection quantity.

---

# 2. What the system is estimating

Maintain four separate latent models.

```text
BUSINESS MODEL
What is happening in the world?
What causes what?
What will happen next?

OPERATOR MODEL
What does this human value?
What would they choose?
What contextual rules guide their behavior?

ECONOMIC POLICY MODEL
What choices actually produce good outcomes?

COMPLEMENTARITY MODEL
Where does human involvement add value over agent-only execution?
```

Never collapse them.

Thus the system can simultaneously represent:

```text
Human prefers A.
Agent independently recommends B.
Operator model predicted Human would prefer A.
Historical economic evidence currently favors B.
Human historically outperforms agents on this decision class.
```

That disagreement is training data.

---

# 3. Fixed 10 information objectives

These identifiers are permanent.

Actual wording is dynamically generated.

## `QO_01_GOAL_HIERARCHY`

**Unknown being estimated:** desired objective and priority across horizons.

Capture:

```text
NOW
TODAY
7D
30D
MISSION
```

Core question:

> What outcome currently matters most, and has that changed?

This supports metacognitive **control**.

---

## `QO_02_STATE_BOTTLENECK`

**Unknown:** perceived binding constraint.

Capture:

```text
primary bottleneck
confidence
evidence
alternative bottleneck
```

Distinguishes:

> something annoying

from:

> something constraining progress.

---

## `QO_03_CAUSAL_MODEL`

**Unknown:** operator's causal explanation of the business.

Capture propositions such as:

```text
Low sales
BECAUSE
low qualified traffic

rather than:

Low sales
BECAUSE
bad product
```

Every important causal belief should eventually become testable.

This is the entrepreneurship **theory-of-value** layer supported by recent field experiments. ([PubsOnline][10])

---

## `QO_04_UNCERTAINTY_VOI`

**Unknown:** highest-value missing information.

Question class:

> What, if we learned it today, would most change what we do?

This is the explicit VOI/active-learning objective. ([PubMed][11])

---

## `QO_05_FORECAST`

**Unknown:** prospective expectation.

Questions create resolvable predictions:

```text
P(first sale before 100 visits) = .55

P(recorder fails to capture a session this week) = .10

Expected GameWinner conversion after 250 visits:
1.5%–4%, median 2.6%
```

Never create the prediction retrospectively.

---

## `QO_06_RESOURCE_POLICY`

**Unknown:** appropriate expenditure of scarce resources.

Capture separately:

```text
cash aggressiveness
compute aggressiveness
human time allocation
exploration fraction
exploitation fraction
verification intensity
parallelism
```

This links directly to BATS: agents perform better when remaining resources are visible and planning responds to budget rather than merely receiving a larger budget. ([arXiv][12])

---

## `QO_07_TEST_COUNTERFACTUAL`

Combines falsification and opportunity cost.

**Unknowns:**

```text
What evidence would change this belief?
What alternative are we rejecting?
What are we giving up by choosing this action?
```

Required for significant business hypotheses.

---

## `QO_08_RISK_PREMORTEM`

**Unknown:** failure modes not represented in current plan.

For substantial decisions:

> Assume this failed. What probably caused the failure?

Premortems are specifically designed to surface reservations before execution rather than after failure. ([Harvard Business Review][13])

---

## `QO_09_HUMAN_SIGNAL`

**Unknown:** information visible internally to the human but absent from machine telemetry.

Examples:

```text
"This output feels cheap."

"This market suddenly feels much more promising."

"I think we're solving the wrong problem."

"The numbers look fine but something about this offer is confusing."
```

This is why contemporaneous measurement matters. EMA research exists precisely because retrospective summaries lose contextual cognition and introduce recall distortion. ([PubMed][1])

These statements are hypotheses, not facts.

Track whether they later predict anything.

---

## `QO_10_META_POLICY_DELEGATION`

**Unknown:** whether the operating policy itself should change.

Questions include:

```text
Should we still be optimizing this objective?

Is this process itself wrong?

Should this class of decision remain human-led?

Did asking the human add value here?

Should this worker receive more or less autonomy?
```

This implements double-loop learning and learning-to-defer. ([Harvard Business Review Store][14])

---

# 4. Sampling schedule

Do not administer ten questions repeatedly.

EMA research supports repeated real-world sampling but also makes burden/compliance an explicit design concern; a large meta-analysis across 477 studies found repeated assessments practical but emphasizes the need to manage sampling intensity. ([PubMed][15])

Use this rigid cadence.

```text
MORNING
5 questions

mandatory:
QO_01 GOAL
QO_02 BOTTLENECK
QO_06 RESOURCE POLICY

+ 2 highest-value adaptive questions
```

```text
MAJOR SESSION CLOSE
1 mandatory alignment question
+ 0–2 adaptive questions

target human time:
60–180 seconds
```

```text
EVENING
5 questions

mandatory:
QO_03 CAUSAL UPDATE
QO_09 HUMAN SIGNAL
QO_10 META POLICY

+ 2 adaptive
```

```text
WEEKLY
5–8 questions

focus:
patterns invisible at daily scale
forecast performance
persistent enquiry threads
delegation
resource policy
strategy changes
```

No question should be asked merely because its category has not appeared recently unless a minimum cadence rule specifically requires it.

---

# 5. Adaptive question selection

## Step A — construct `KnowledgeGap`s

Before asking anything, derive unresolved uncertainties.

```python
class KnowledgeGap:
    gap_id: UUID

    target_type: Literal[
        "goal",
        "state",
        "causal_belief",
        "forecast",
        "operator_preference",
        "risk",
        "delegation",
        "resource_policy",
    ]

    target_ref: str | None

    description: str

    uncertainty: float       # 0–1
    decision_impact: float   # 0–1
    urgency: float           # 0–1

    human_information_advantage: float  # 0–1
    agent_information_advantage: float  # 0–1

    current_evidence_refs: list[UUID]

    next_decision_ids: list[UUID]
```

---

## Step B — generate candidate questions

For every relevant objective:

```python
class QuestionCandidate:
    candidate_id: UUID

    objective_id: str
    gap_ids: list[UUID]

    wording: str
    timescale: str

    action_hook: str

    estimated_probability_answer_changes_decision: float
    estimated_uncertainty_reduction: float
    decision_impact: float
    human_information_advantage: float

    estimated_burden_seconds: int

    redundancy_with_recent_questions: float

    why_now: str

    generator_model: str
    generator_version: str
```

Hard rule:

```text
action_hook == null
→ reject candidate
```

---

# 6. VOI-inspired ranking

True Bayesian EVSI is computationally demanding and generally requires a formal decision model; therefore StallShark should **not pretend its heuristic is exact EVSI**. VOI literature explicitly frames information value as the expected reduction in decision loss after obtaining additional information. ([PubMed][3])

Use a clearly named proxy:

```text
QuestionValueProxy =
    P(answer changes decision)
  × decision impact
  × expected uncertainty reduction
  × human information advantage
  × urgency
```

Then apply:

```text
net_priority =
QuestionValueProxy
÷ expected human burden
```

Redundancy reduces priority.

Persist every component.

Do not store only the final score.

Future models can learn better selection functions from actual outcomes.

---

# 7. `QuestionInstance`

Once selected, candidate becomes immutable.

```python
class QuestionInstance:
    question_id: UUID
    company_day_id: UUID
    session_id: UUID | None

    objective_id: str

    knowledge_gap_ids: list[UUID]

    exact_wording: str

    asked_at: datetime

    cadence: Literal[
        "morning",
        "session_close",
        "evening",
        "weekly",
        "event_triggered",
    ]

    action_hook: str

    selection_features: QuestionSelectionFeatures
    selection_policy_version: str

    context_manifest_id: UUID

    answer_due_from: list[
        Literal[
            "predicted_human",
            "independent_agent",
            "human",
            "worker",
            "cold_reviewer",
        ]
    ]
```

---

# 8. `PerspectiveAnswer`

All actors answer the same canonical object.

```python
class PerspectiveAnswer:
    answer_id: UUID
    question_id: UUID

    actor_type: Literal[
        "human",
        "predicted_human",
        "independent_agent",
        "worker",
        "cold_reviewer",
    ]

    actor_version: str

    context_manifest_id: UUID

    committed_at: datetime

    raw_text_artifact_id: UUID

    structured_answer: str

    confidence: float | None

    claim_ids: list[UUID]
    forecast_ids: list[UUID]

    suggested_action_ids: list[UUID]

    unknowns: list[str]
```

Raw language is permanent.

Structured extraction is replaceable.

---

# 9. Independence protocol

Research on selective prediction shows that information disclosed by AI can alter the human's judgment itself; one study found benefit from telling humans that the system had deferred while withholding the AI's prediction. ([arXiv][16])

Therefore perspective isolation is not cosmetic.

## Morning

```text
STATE FREEZE

↓ parallel

P = Operator model predicts H
A = Independent agent answers for itself
H = Human answers

↓ only after all committed

REVEAL
```

`A` must not receive operator preference memory.

`P` may.

`H` sees neither before committing.

---

## Session close

```text
FACTUAL SESSION TRACE
       ├─────────────┐
       ↓             ↓
WORKER DEBRIEF     HUMAN QUESTIONS
       │             │
       commit        commit
       └──────┬──────┘
              ↓
        SESSION RECONCILIATION
```

The question generator should use **factual session evidence + open enquiry threads**, not the worker's debrief.

That prevents the worker from framing the human's assessment.

---

## Evening

```text
HUMAN EVENING VIEW
        commit

WORKER VIEW
        commit

COLD REVIEW
facts only
        commit

↓
RECONCILIATION
```

---

# 10. `ContextManifest`

Every independent judgment must prove what information it was allowed to see.

```python
class ContextManifest:
    context_manifest_id: UUID

    purpose: str

    information_cutoff_at: datetime

    included_record_ids: list[UUID]
    included_artifact_ids: list[UUID]

    excluded_record_ids: list[UUID]
    excluded_memory_banks: list[str]

    explicitly_hidden_categories: list[str]

    model: str
    worker_version: str
    axioms_version: str

    context_sha256: str
```

This makes historical replay possible without future leakage.

---

# 11. `Belief`

Beliefs must be versioned rather than silently edited.

```python
class Belief:
    belief_id: UUID
    revision: int

    holder_type: Literal["human", "agent", "joint"]

    proposition: str

    belief_type: Literal[
        "causal",
        "market",
        "operator",
        "strategic",
        "operational",
    ]

    confidence: float

    scope: dict

    evidence_for: list[UUID]
    evidence_against: list[UUID]

    created_at: datetime

    supersedes: UUID | None

    falsification_condition: str | None

    status: Literal[
        "active",
        "supported",
        "weakened",
        "rejected",
        "retired",
    ]
```

This gives us **belief half-life**:

```text
time from contradictory evidence
→ meaningful confidence update
```

for both human and agents.

---

# 12. `CausalHypothesis`

This is more rigorous than a generic belief.

```python
class CausalHypothesis:
    hypothesis_id: UUID

    problem_id: UUID

    cause: str
    effect: str
    mechanism: str

    boundary_conditions: list[str]

    confidence_before: float

    predictions: list[UUID]

    falsification_conditions: list[str]

    candidate_experiment_ids: list[UUID]

    status: Literal[
        "proposed",
        "testing",
        "supported",
        "rejected",
        "inconclusive",
    ]
```

This explicitly operationalizes the scientific-entrepreneurship evidence. ([PubsOnline][5])

---

# 13. `Forecast`

Every important uncertain claim should become resolvable where practical.

```python
class Forecast:
    forecast_id: UUID

    actor_answer_id: UUID

    question: str

    probability: float

    resolution_condition: str
    resolution_deadline: datetime

    information_cutoff_at: datetime

    reference_class: str | None

    resolved: bool = False
    outcome: bool | None = None

    brier_score: float | None = None
```

For binary outcome:

```text
Brier = (forecast_probability - outcome)^2
```

Aggregate separately by:

```text
human
independent agent
operator model

and by:

product decisions
marketing
engineering effort
cost estimates
strategic pivots
creative choices
```

Forecasting tournaments show that tracking performance by domain can reveal persistent differences in judgment quality rather than relying on reputation or confidence. ([Sage Journals][17])

---

# 14. Persistent `EnquiryThread`

This is essential.

Questions should accumulate into ongoing investigations.

```python
class EnquiryThread:
    thread_id: UUID

    title: str

    originating_objective_id: str

    opened_at: datetime

    central_question: str

    target_gap_ids: list[UUID]

    linked_belief_ids: list[UUID]
    linked_problem_ids: list[UUID]
    linked_decision_ids: list[UUID]
    linked_experiment_ids: list[UUID]

    human_current_view: str | None
    agent_current_view: str | None

    evidence_refs: list[UUID]

    resolution_rule: str

    revisit_triggers: list[str]

    status: Literal[
        "open",
        "waiting_for_evidence",
        "resolved",
        "retired",
    ]
```

Example:

```text
ET-003

Are we investing in infrastructure because it is genuinely
high-leverage, or because it delays uncomfortable market validation?

Day 1:
Human: necessary foundation.

Agent: opportunity cost becoming high.

Day 3:
Recorder prevents loss of useful session evidence.

Day 5:
No listing live.

Day 7:
Revisit automatically.
```

Now the enquiry develops as evidence develops.

---

# 15. Session-close human review

Every meaningful work session gets one mandatory human question:

> **Did this session move in the direction you intended? If not, what did the agent misunderstand?**

Structured:

```python
class HumanSessionReview:
    review_id: UUID
    session_id: UUID

    intent_alignment: float

    main_misunderstanding: str | None

    strongest_positive_signal: str | None
    strongest_negative_signal: str | None

    decision_you_would_change: str | None

    agent_missed_signal: str | None

    adaptive_answer_ids: list[UUID]

    raw_voice_artifact_id: UUID | None
```

Maximum 1–3 minutes.

The contemporaneous timing is important because repeated real-world assessment reduces reliance on distorted retrospective reconstruction. ([PubMed][1])

---

# 16. Human interventions

A human correcting an agent is especially valuable.

PAHF shows the utility of both pre-action clarification and post-action feedback; PPL shows that an intervention can indicate preferences relevant to future states rather than only the exact corrected action. ([arXiv][9])

```python
class HumanIntervention:
    intervention_id: UUID

    session_id: UUID
    trajectory_step_id: UUID

    agent_intended_action: str

    exact_human_message_artifact_id: UUID

    corrective_action: str

    inferred_reason: str
    inference_confidence: float

    scope: Literal[
        "single_action",
        "session",
        "until_condition",
        "decision_class",
        "candidate_persistent",
    ]

    termination_condition: dict | None

    candidate_operator_memory_id: UUID | None

    eventual_outcome_ids: list[UUID]
```

Example:

```text
"Stop doing the AR stuff and launch."

scope:
until_condition

termination:
listing_count >= 1
```

Not:

```text
Tom hates AR.
```

---

# 17. Operator memory

PersonalAlign specifically separates persistent preferences from recurring routines; PAHF explicitly handles preference drift. ([arXiv][18])

Use:

```python
class OperatorMemory:
    memory_id: UUID

    memory_type: Literal[
        "explicit_preference",
        "contextual_preference",
        "routine",
        "inferred_rule",
    ]

    claim: str

    context_conditions: dict

    evidence_refs: list[UUID]
    contradiction_refs: list[UUID]

    confidence: float

    status: Literal[
        "candidate",
        "validated",
        "weakened",
        "retired",
    ]

    created_at: datetime
    last_validated_at: datetime | None
```

Precedence:

```text
CURRENT EXPLICIT INTENT
>
CURRENT CONTEXTUAL INSTRUCTION
>
VALIDATED RECENT OPERATOR MEMORY
>
OLDER OPERATOR MEMORY
```

Candidate memories never silently control behavior.

---

# 18. `DelegationDecision`

This is the bridge to learning optimal human involvement.

```python
class DelegationDecision:
    delegation_id: UUID

    task_id: UUID
    task_class: str

    state_snapshot_id: UUID

    agent_confidence: float

    novelty_score: float
    reversibility: float
    consequence: float

    historical_agent_success: float | None
    historical_human_advantage: float | None

    selected_mode: Literal[
        "agent_autonomous",
        "agent_then_human_review",
        "joint",
        "human_lead",
    ]

    estimated_human_minutes: int

    actual_human_minutes: int | None

    human_changed_decision: bool | None

    outcome_ids: list[UUID]
```

Do **not** initially calculate fictional:

```text
human_value_usd = 43.87
```

Collect the observable inputs first.

Later estimate:

```text
E[outcome | human consulted]
-
E[outcome | agent alone]
-
human attention cost
```

Learning-to-defer literature gives the appropriate eventual modeling framework. ([arXiv][19])

---

# 19. Question outcomes

Crucially, evaluate the interviewer itself.

```python
class QuestionOutcome:
    question_id: UUID

    human_answered: bool

    immediate:
        changed_plan: bool
        changed_decision: bool
        created_problem: bool
        created_hypothesis: bool
        created_experiment: bool
        exposed_human_agent_divergence: bool
        changed_belief_confidence: bool

    delayed:
        forecast_resolved: bool
        answer_was_predictive: bool | None
        cited_in_future_decision_count: int
        enquiry_thread_resolved: bool
        economic_relevance_detected: bool | None

    actual_human_seconds: int
```

Initially keep this vector.

Do not invent arbitrary weights.

Later this becomes the reward signal for learning the **question-selection policy**.

---

# 20. Complete data pipeline

```text
                    ┌──────────────────────────────┐
                    │      OBJECTIVE REALITY       │
                    │ money / Git / sessions /     │
                    │ products / actions / metrics │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                         STATE SNAPSHOT S_t
                                  │
                   derive KnowledgeGaps
                                  │
                                  ▼
                      QUESTION CANDIDATES
                                  │
                          VOI proxy rank
                                  │
                                  ▼
                         SELECT QUESTIONS
                                  │
                 ┌────────────────┼────────────────┐
                 ▼                ▼                ▼
        PREDICTED HUMAN      AGENT VIEW       HUMAN VIEW
             P_t                A_t               H_t
                 │                │                │
                 └────────────────┼────────────────┘
                                  ▼
                             DIVERGENCE
                                  │
                                  ▼
          beliefs / problems / hypotheses / forecasts
                                  │
                                  ▼
                              DECISION
                                  │
                                  ▼
                         RESOURCE ALLOCATION
                                  │
                                  ▼
                              EXECUTION
                                  │
             ┌────────────────────┴──────────────────┐
             ▼                                       ▼
       OPENCODE TRACE                          MARKET OUTCOME
             │                                       │
             ▼                                       │
       SESSION FACTS                                 │
      ┌──────┴──────┐                                │
      ▼             ▼                                │
WORKER VIEW     HUMAN REVIEW                         │
      └──────┬──────┘                                │
             ▼                                       │
        SESSION DELTA                                │
                                                     │
DAY END                                               │
      ┌──────────────────────────────────────────────┘
      ▼
HUMAN EVENING
WORKER DEBRIEF
BLIND REVIEW
      │
      ▼
RECONCILIATION
      │
      ▼
candidate memories / enquiry updates
      │
      ▼
1D / 7D / 30D OUTCOMES
      │
      ▼
calibration / question utility /
human-v-agent competence /
economic evidence
```

---

# 21. Data levels

## L0 — immutable raw evidence

```text
OpenCode messages
human exact prompts
agent exact responses
voice
tool calls
Git
files/diffs
receipts
economic events
```

## L1 — canonical structured observations

```text
QuestionInstance
PerspectiveAnswer
Belief
Forecast
HumanIntervention
Decision
Action
Budget
Outcome
```

## L2 — derived interpretations

```text
operator memories
knowledge gaps
enquiry threads
session interpretations
competence estimates
question utility
```

## L3 — outcome-linked episodes

```text
state
belief
question
decision
action
resources
outcome
```

## L4 — trainable exports

Generated deterministically from L0–L3.

Never hand-edit training datasets.

---

# 22. Model-training datasets this creates

## A. Operator prediction model

Goal:

> What would this human say/choose in this exact context?

Training:

```text
INPUT
business state
question
allowed historical operator context
recent relevant raw language

TARGET
actual prospective human response
```

Dataset:

```text
(state, question, operator_context)
→ H
```

Evaluation:

```text
semantic agreement
preference ranking accuracy
numeric calibration
```

This is your actual **Operator Twin**.

---

# 23. Operator preference model

Decisions naturally create pairwise/listwise preferences.

```text
STATE

OPTIONS:
A
B
C

HUMAN CHOICE:
B

RATIONALE:
...

LATER OUTCOME:
...
```

This can support:

```text
preference classifier
ranking model
DPO-style preference data
reward model
```

But importantly:

> human preference reward ≠ economic reward.

Maintain separate targets.

---

# 24. Intervention/PPL dataset

```text
STATE
agent proposed action
human intervention
correction
future state sequence
preference horizon
termination condition
later outcome
```

Potential future use:

> Predict when an agent trajectory is approaching a region where this human is likely to intervene.

PPL provides a concrete framework for propagating intervention signals beyond one immediate action. ([arXiv][20])

---

# 25. Question-policy dataset

This is particularly novel.

For every candidate set:

```text
STATE
KNOWLEDGE GAPS
QUESTION CANDIDATES
SELECTION FEATURES
SELECTED QUESTION
ANSWER
QUESTION OUTCOME
HUMAN COST
```

Eventually train:

```text
QuestionPolicy(state, uncertainties)
→ question
```

Possible methods progress from:

```text
heuristic VOI ranking

→ supervised utility predictor

→ contextual bandit

→ offline policy learning
```

The reward becomes:

```text
decision improvement
uncertainty resolved
forecast value
downstream use
-
human attention
```

This is essentially **active preference elicitation specialized to entrepreneurship/management**. ([arXiv][4])

---

# 26. Economic critic

Dataset:

```text
state_t
action_t
resource allocation
market context
1d outcome
7d outcome
30d outcome
```

Potential training:

```text
OutcomeModel(state, action)
→ distribution(outcome)
```

or:

```text
ActionRanker(state, A, B)
→ better expected action
```

This is different from the Operator model.

One predicts Tom.

One predicts reality.

---

# 27. Learning-to-defer model

Dataset:

```text
task state

agent answer
agent confidence

human answer where requested

whether human changed action

human minutes consumed

agent-only historical performance

human-assisted performance

economic result
```

Train:

```text
DeferPolicy(task, state)
→ autonomous
   human_review
   human_lead
```

Human-AI complementarity research argues that the key benefit comes from differences in available information and capability, not merely combining two opinions indiscriminately. ([arXiv][8])

Eventually the system discovers:

```text
Tom:
excellent at product positioning
good at visual taste
poor at effort estimation

Agent:
excellent at bookkeeping
excellent at API operations
better at experiment hygiene
worse at emotionally resonant brand judgments
```

based on outcomes rather than assumptions.

---

# 28. Forecasting model / calibration layer

Every prospective forecast produces:

```text
state
actor
probability
resolution
```

Train or calibrate:

```text
raw forecast
→ calibrated probability
```

More importantly, build competence maps:

```text
Human forecasting:
brand concepts       strong
engineering time     weak
paid acquisition     unknown

Economic Critic:
cost                 strong
taste                weak
conversion           improving
```

Delegation can consume this directly before any fine-tuning.

---

# 29. Belief-update model

An unusually useful future dataset:

```text
prior belief
confidence_before

new evidence

human confidence_after
agent confidence_after

eventual truth/outcome
```

Potential model:

```text
BeliefUpdate(prior, evidence)
→ posterior
```

Then compare:

> Which actor updates too slowly?

> Which overreacts to noisy observations?

> When does human intuition update before formal metrics?

This makes metacognitive **monitoring quality** measurable rather than philosophical. ([Socsci UCI][2])

---

# 30. Memory retrieval model

Every retrieval should log:

```text
query
candidate memories
selected memories
tokens consumed
decision changed?
result
```

Dataset:

```text
(state, task, candidate_memory)
→ future usefulness
```

Train a reranker:

```text
MemoryValue(state, task, memory)
```

This matters because current 2026 evidence shows memory/skill modules can lose their apparent advantage once compared against token-matched vanilla agents. ([arXiv][21])

Therefore:

```text
memory retrieval
```

must economically justify its context cost.

---

# 31. Semantic memory must remain a projection

Do not mutate historical evidence into “what the agent knows.”

Use:

```text
episodic evidence
       ↓
deterministic/versioned consolidation
       ↓
semantic knowledge
```

The recent episodic-to-semantic consolidation work makes essentially the same architectural distinction: knowledge can be consolidated into a separately addressable layer without mutating the underlying identity/evidence. ([arXiv][22])

Thus a model in 2030 can rebuild the semantic layer from the original 2026 evidence.

---

# 32. The interviewer improves itself

After enough CompanyDays:

```text
QO_BOTTLENECK questions:
83% produce actionable corrections

QO_RISK:
14% alter anything

QO_HUMAN_SIGNAL:
only 22% immediately actionable
BUT
highly predictive of later product-quality problems

QO_RESOURCE_POLICY:
strongly predicts infrastructure rabbit holes
```

Now the system stops asking generic questions.

It learns:

> In this operator/company/state, which question is worth asking?

That is a legitimate learned management policy.

---

# 33. The enquiry system should create interventions automatically

Example after 30 days:

```text
FACTS

Last 3 days:
market_contact = 0

Infrastructure time:
74%

Open problems:
5

No new listings.

Historical pattern:
similar state preceded 4 human corrections.

Operator memory:
human opposes optional infrastructure
when market hypothesis remains unvalidated.
```

The interviewer generates:

> “You've spent 74% of the last three days on infrastructure and received no new customer evidence. Is that still an intentional allocation, or has infrastructure become avoidance?”

That is not a canned coaching question.

It is an **active query generated from longitudinal evidence**.

---

# 34. Meta-enquiry then becomes recursive

```text
DAY 1

AI asks:
What is the bottleneck?
```

```text
DAY 30

AI asks:
You've identified production reliability as the bottleneck
six times, but only two experiments attacked it.
Is diagnosis failing to translate into resource allocation?
```

```text
DAY 180

AI asks:
Historically your strongest product decisions occur
when you override the agent on emotional positioning,
while your engineering overrides reduce performance.
Should we formally change the delegation policy?
```

That is the endgame.

The agent is no longer simply remembering the human.

It is using empirical history to **improve the conversation through which the organization governs itself**.

---

# 35. Rights boundary for training

This is critical.

Etsy's current API Terms prohibit using automated systems to analyze Etsy API/site data and explicitly prohibit collecting Etsy API content for analytics, machine learning or AI training unless Etsy provides written authorization. ([Etsy][23])

Therefore the training-export layer must have a hard rights filter.

Safe first-party corpus candidates include:

```text
human prompts
human voice/transcripts
agent responses
code
Git actions
first-party decisions
budgets
generated product-process metrics
your own experiments
your own abstracted economic outcomes
your own operator-memory structures
```

Restricted by default:

```text
raw Etsy API content
competitor listing content
Etsy member/customer content
customer PII
customer photos
customer messages
```

Do not allow a future `train.py` to simply read the whole ledger.

Every canonical record needs:

```python
training_rights: Literal[
    "allowed",
    "internal_only",
    "prohibited",
    "unknown",
]
```

`unknown` must fail closed.

---

# 36. Minimal implementation for today

Do **not** train anything yet.

Implement only the machinery that makes future training possible.

```text
1. QuestionObjective registry — 10 fixed IDs

2. KnowledgeGap generation

3. QuestionCandidate generation + VOI-proxy ranking

4. QuestionInstance

5. PerspectiveAnswer with P/A/H isolation

6. Belief + Forecast

7. EnquiryThread

8. HumanSessionReview

9. HumanIntervention

10. ContextManifest

11. QuestionOutcome

12. DelegationDecision

13. Immutable raw OpenCode + voice storage

14. 1d/7d/30d OutcomeReceipts
```

Everything else is derived.

---

# 37. Immediate agent usefulness without training

Even with zero fine-tuning, tomorrow's agent can already use this data meaningfully.

Before working:

```text
retrieve:
current intent
relevant validated operator preferences
similar resolved problems
open enquiry threads
relevant failed experiments
```

Before asking the human:

```text
estimate:
Do I already know this?
Is this decision consequential?
Is the human historically better here?
Would an answer change what I do?
```

Before spending:

```text
read:
resource policy
remaining BATS budget
```

Before acting autonomously:

```text
read:
delegation history
novelty
reversibility
human comparative advantage
```

At session end:

```text
identify:
what changed
what remains unclear
what requires human-only information
```

At day end:

```text
fresh reviewer:
facts only

reconciliation:
compare independent interpretations
```

So the corpus delivers value long before there is enough data to train a specialized model.

---

# 38. Training progression

```text
DAYS 1–14
No custom model training.

Use:
structured retrieval
question utility
forecast scoring
operator-memory candidates
```

```text
~50–200 meaningful human judgments
Operator prediction evaluator
simple preference/ranking models
retrieval tuning
```

```text
hundreds of comparable decisions
Operator-model SFT / preference model
question-utility predictor
delegation classifier
forecast calibration
```

```text
hundreds/thousands of outcome-linked episodes
Economic action ranker
state-conditioned delegation
contextual question policy
memory reranker
```

```text
large repeated state/action corpus
Carefully evaluate:
offline policy learning
operator-policy fine-tuning
economic critic fine-tuning
bounded autonomous management
```

Do not advance because a dataset merely becomes large.

Advance when it contains enough **comparable states with resolved outcomes**.

---

# 39. The canonical learning unit

Ultimately the most valuable row is:

```text
COMPANY STATE

WHAT WAS KNOWABLE

QUESTION ASKED

PREDICTED HUMAN VIEW

INDEPENDENT AGENT VIEW

ACTUAL HUMAN VIEW

BELIEFS / FORECASTS

DECISION

RESOURCE ALLOCATION

FULL EXECUTION TRAJECTORY

HUMAN INTERVENTIONS

IMMEDIATE OUTCOME

1D OUTCOME

7D OUTCOME

30D OUTCOME

WHO WAS RIGHT

WHAT QUESTION WAS USEFUL

WHETHER HUMAN INVOLVEMENT HELPED
```

Call that:

```text
DecisionEpisode
```

After a year, StallShark is not just a log of an Etsy business.

It is a longitudinal dataset of:

> **how a human–AI organization perceived uncertain states, asked for information, disagreed, allocated cognition and capital, acted, learned, and was subsequently graded by economic reality.**

That is the dataset from which the Operator model, Economic Critic, Question Policy, Memory Policy and Delegation Policy can all emerge.

---

# 40. Core axioms for this subsystem

```text
1. Ask for information, not introspection.

2. No question without an action hook.

3. Capture beliefs before outcomes.

4. Preserve probability, not merely confidence prose.

5. Preserve raw language before extracting structure.

6. Monitoring and control are separate variables.

7. Human preference and economic correctness are separate rewards.

8. Independent judgments commit before reveal.

9. Interventions are contextual evidence, not universal preferences.

10. Questions themselves are experiments.

11. Memory must justify its token cost.

12. Human attention is a scarce budget.

13. Outcomes never rewrite prior beliefs.

14. Single-loop fixes and double-loop policy changes are different events.

15. The best future question is learned from what previous questions actually changed.
```

This is the rigid core I would now freeze into StallShark.

The most important change from our earlier version is that the interview is no longer “ten good categories.” It is formally a **query policy**: stable measurement objectives generate candidate questions against current knowledge gaps; a VOI-inspired selector spends scarce human attention on the most decision-relevant gaps; every answer is prospectively timestamped; and `QuestionOutcome` later tells us whether asking was actually worth it. That creates a direct path from daily management practice to a learnable **QuestionPolicy**, just as the human/agent comparisons create learnable Operator and Delegation policies.

[1]: https://pubmed.ncbi.nlm.nih.gov/18509902/?utm_source=chatgpt.com "Ecological momentary assessment - PubMed"
[2]: https://sites.socsci.uci.edu/~lnarens/1994/Nelson%26Narens_Book%20Chapter_1994.pdf?utm_source=chatgpt.com "Untitled.PDF"
[3]: https://pubmed.ncbi.nlm.nih.gov/32165869/?utm_source=chatgpt.com "Value of Information: Sensitivity Analysis and Research Design in Bayesian Evidence Synthesis."
[4]: https://arxiv.org/abs/2404.13895?utm_source=chatgpt.com "Optimal Design for Human Preference Elicitation"
[5]: https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2018.3249?utm_source=chatgpt.com "A Scientific Approach to Entrepreneurial Decision Making: Evidence from a Randomized Control Trial | Management Science"
[6]: https://repository.library.noaa.gov/view/noaa/33728?utm_source=chatgpt.com "Why the Brier Score is a \"proper\" scoring system"
[7]: https://hbr.org/1977/09/double-loop-learning-in-organizations?utm_source=chatgpt.com "Double Loop Learning in Organizations"
[8]: https://arxiv.org/abs/2404.00029?utm_source=chatgpt.com "Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence"
[9]: https://arxiv.org/abs/2602.16173?utm_source=chatgpt.com "Learning Personalized Agents from Human Feedback"
[10]: https://pubsonline.informs.org/doi/10.1287/orsc.2023.17590?utm_source=chatgpt.com "Does a Theory-of-Value Add Value? Evidence from a Randomized Control Trial with Tanzanian Entrepreneurs | Organization Science"
[11]: https://pubmed.ncbi.nlm.nih.gov/32197720/?utm_source=chatgpt.com "Value of Information Analytical Methods: Report 2 of the ISPOR Value of Information Analysis Emerging Good Practices Task Force."
[12]: https://arxiv.org/abs/2511.17006?utm_source=chatgpt.com "Budget-Aware Tool-Use Enables Effective Agent Scaling"
[13]: https://hbr.org/2007/09/performing-a-project-premortem?utm_source=chatgpt.com "Performing a Project Premortem"
[14]: https://store.hbr.org/product/double-loop-learning-in-organizations/77502?utm_source=chatgpt.com "Double Loop Learning in Organizations"
[15]: https://pubmed.ncbi.nlm.nih.gov/35016567/?utm_source=chatgpt.com "Ecological Momentary Assessment: A Meta-Analysis on Designs, Samples, and Compliance Across Research Fields - PubMed"
[16]: https://arxiv.org/abs/2112.06751?utm_source=chatgpt.com "Role of Human-AI Interaction in Selective Prediction"
[17]: https://journals.sagepub.com/doi/pdf/10.1177/0963721414534257?utm_source=chatgpt.com "Forecasting Tournaments - Philip E. Tetlock, Barbara A. Mellers, Nick Rohrbaugh, Eva Chen, 2014"
[18]: https://arxiv.org/abs/2601.09636?utm_source=chatgpt.com "PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records"
[19]: https://arxiv.org/abs/2006.01862?utm_source=chatgpt.com "Consistent Estimators for Learning to Defer to an Expert"
[20]: https://arxiv.org/abs/2510.01545?utm_source=chatgpt.com "Predictive Preference Learning from Human Interventions"
[21]: https://arxiv.org/abs/2606.15017?utm_source=chatgpt.com "Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents"
[22]: https://arxiv.org/abs/2607.01988?utm_source=chatgpt.com "Episodic-to-Semantic Consolidation Without Identity Drift"
[23]: https://www.etsy.com/legal/api/?utm_source=chatgpt.com "API Terms of Use - Our House Rules | Etsy"
