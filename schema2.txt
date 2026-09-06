Yes. **Keep Pydantic. Add binary validation, but only for things that are objectively valid/invalid. Keep “skills” extremely small. And stop adding parallel schema files.**

The repo is at the exact point where consolidation matters more than invention. `AGENTS.md` already has the correct doctrine—build businesses, preserve cognition, simplest thing that works, no big new abstractions before meaningful commerce data.  The new meta-enquiry implementation has the right concepts, but it is still prototype code using unvalidated dict factories rather than Pydantic contracts. It also currently has a few important implementation bugs: the selector accepts a schedule but does not enforce it, candidate-question objects are generated but selection actually ranks `KnowledgeGap`s, the redundancy comparison mixes candidate IDs with gap IDs, and `DecisionEpisode` contains a typo (`human_involution_helped`).

Pydantic is still a very good fit because current Pydantic supports strict validation and can emit JSON Schema Draft 2020-12 automatically, letting Python remain the implementation while every agent/tool can consume a language-independent schema. ([Pydantic Docs][1]) JSON Schema 2020-12 remains the current published JSON Schema dialect. ([JSON Schema][2])

The key design decision is:

> **Don't build an autonomous framework. Build an immutable, typed operating record that an increasingly autonomous agent can safely act through.**

W3C PROV is useful conceptually here because its basic model is exactly what we need: entities, activities, agents and derivations, with provenance supporting reproducibility, trust, versioning and reconstruction. We do not need to implement RDF/PROV itself; just copy those primitives. ([W3C][3])

# StallShark Canonical Corpus Architecture v1

## End goal

After 500 real operating days, the primary asset is:

```text
500 CompanyDays

containing:

raw human language
raw agent trajectories
state snapshots
human beliefs
agent beliefs
predicted-human beliefs
questions asked
forecasts
decisions
rejected alternatives
budgets
actions
model/tool usage
human interventions
experiments
economic outcomes
blind reviews
belief updates
public narratives
```

The core research/training unit is:

```text
STATE
→ WHAT WAS KNOWABLE
→ WHAT HUMAN THOUGHT
→ WHAT AGENT THOUGHT
→ WHAT AGENT THOUGHT HUMAN WOULD THINK
→ QUESTIONS ASKED
→ DECISION
→ RESOURCE ALLOCATION
→ ACTION TRAJECTORY
→ HUMAN INTERVENTIONS
→ OUTCOME
→ LATER INTERPRETATION
```

Everything in the repo should support creating or using that record.

---

# 1. Four layers only

```text
L0 RAW EVIDENCE
       ↓
L1 CANONICAL RECORDS
       ↓
L2 DERIVED VIEWS
       ↓
L3 TRAINING / PUBLIC EXPORTS
```

### L0 — never transformed destructively

Examples:

```text
OpenCode exports
exact human prompts
agent messages
voice recordings
Git diffs
generated assets
API responses
tool outputs
receipts
```

Store by SHA-256.

### L1 — canonical typed history

Pydantic-validated immutable records.

### L2 — rebuildable interpretations

Examples:

```text
TrajectoryIR
DecisionEpisode
EnquiryThread
OperatorMemory
Skill
DailyDigest
weekly analysis
competence maps
```

Delete L2 and rebuild it from L0/L1.

### L3 — consumers

```text
blog
YouTube/TikTok package
Parquet research dataset
operator-model dataset
economic-policy dataset
question-policy dataset
delegation dataset
```

No L3 object is canonical.

---

# 2. One base record

Every canonical object inherits this.

```python
class Record(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        frozen=True,
    )

    id: UUID
    kind: RecordKind
    schema_version: Literal["1.0"]

    company_day_id: UUID | None

    occurred_at: AwareDatetime
    recorded_at: AwareDatetime

    actor: ActorRef

    provenance: ProvenanceRef
    rights: RightsPolicy

    correlation_id: UUID | None = None
    causation_id: UUID | None = None
    supersedes_id: UUID | None = None
```

Use normal UUIDs.

Chronological ordering comes from timestamps, not IDs.

Do not add another ID package merely to get UUIDv7 unless already available.

---

# 3. Core enums

Replace loose strings.

```python
class ActorType(StrEnum):
    HUMAN = "human"
    AGENT = "agent"
    SYSTEM = "system"
    MARKET = "market"

class PerspectiveKind(StrEnum):
    HUMAN_ACTUAL = "human_actual"
    PREDICTED_HUMAN = "predicted_human"
    INDEPENDENT_AGENT = "independent_agent"
    WORKER_DEBRIEF = "worker_debrief"
    COLD_REVIEW = "cold_review"

class RightsClass(StrEnum):
    FIRST_PARTY_PRIVATE = "first_party_private"
    FIRST_PARTY_TRAINABLE = "first_party_trainable"
    CUSTOMER_PRIVATE = "customer_private"
    PLATFORM_RESTRICTED = "platform_restricted"
    PUBLIC_SAFE = "public_safe"

class ActionRisk(StrEnum):
    READ_ONLY = "read_only"
    REVERSIBLE_WRITE = "reversible_write"
    SPEND_CAPPED = "spend_capped"
    IRREVERSIBLE = "irreversible"

class ValidationStatus(StrEnum):
    PASS = "pass"
    FAIL = "fail"
```

Avoid arbitrary labels where a finite vocabulary exists.

---

# 4. Canonical record types

Keep the canonical set relatively small.

## 4.1 `CompanyDay`

One per real day.

```python
class CompanyDay(Record):
    kind: Literal["company_day"]

    day_number: int
    local_date: date
    timezone: str

    started_at: AwareDatetime
    closed_at: AwareDatetime | None

    primary_brand: str | None

    status: Literal[
        "open",
        "closed",
        "incomplete",
    ]
```

Do not embed all the day's content.

Everything references `company_day_id`.

---

## 4.2 `Artifact`

Pointer to raw evidence.

```python
class Artifact(Record):
    kind: Literal["artifact"]

    sha256: str
    byte_size: int
    media_type: str

    artifact_type: Literal[
        "opencode_export",
        "human_voice",
        "transcript",
        "git_diff",
        "image",
        "video",
        "api_response",
        "tool_output",
        "document",
    ]

    storage_uri: str

    sanitized_artifact_id: UUID | None

    contains_secrets: bool
    contains_pii: bool
```

---

## 4.3 `StateSnapshot`

Facts only.

```python
class StateSnapshot(Record):
    kind: Literal["state_snapshot"]

    phase: Literal["start", "checkpoint", "end"]

    cash: Money | None
    cumulative_revenue: Money | None
    cumulative_profit: Money | None

    brand_states: list[BrandState]

    active_problem_ids: list[UUID]
    active_experiment_ids: list[UUID]

    git_commit: str
    git_dirty: bool

    metrics: list[MetricValue]
```

Unknown = `None`.

Never make unavailable values zero.

---

## 4.4 `Session`

One actual work session.

```python
class Session(Record):
    kind: Literal["session"]

    runtime: str
    external_session_id: str

    objective: str

    started_at: AwareDatetime
    ended_at: AwareDatetime | None

    repo_commit_before: str
    repo_commit_after: str | None

    raw_trace_artifact_id: UUID
    sanitized_trace_artifact_id: UUID | None
    git_diff_artifact_id: UUID | None

    result: Literal[
        "success",
        "partial",
        "failure",
        "unknown",
    ]
```

Token/tool/cost information stays in `ResourceReceipt`, not duplicated here.

---

## 4.5 `QuestionInstance`

What was actually asked.

```python
class QuestionInstance(Record):
    kind: Literal["question"]

    objective_id: QuestionObjective

    exact_wording: str

    knowledge_gap_ids: list[UUID]

    cadence: Literal[
        "morning",
        "session_close",
        "evening",
        "weekly",
        "event_triggered",
    ]

    action_hook: str

    estimated_burden_seconds: int

    selection_features: QuestionSelectionFeatures
    selection_policy_version: str

    context_manifest_id: UUID
```

This replaces storing merely “question candidates”.

---

## 4.6 `Perspective`

One actor's prospective view.

```python
class Perspective(Record):
    kind: Literal["perspective"]

    perspective_kind: PerspectiveKind

    state_snapshot_id: UUID
    context_manifest_id: UUID

    question_answers: list[QuestionAnswer]

    objectives: ObjectiveHierarchy

    bottleneck: Claim | None

    beliefs: list[Claim]

    opportunities: list[Claim]
    risks: list[Claim]
    unknowns: list[str]

    preferred_action: str | None

    operating_stance: OperatingStance | None

    raw_artifact_id: UUID | None
```

This single schema covers:

```text
H
P
A
worker debrief
cold review
evening human view
```

---

## 4.7 `Forecast`

Do not hide forecasts inside prose.

```python
class Forecast(Record):
    kind: Literal["forecast"]

    perspective_id: UUID

    proposition: str
    probability: float

    resolution_condition: str
    resolution_deadline: AwareDatetime

    information_cutoff_at: AwareDatetime

    resolved_outcome_id: UUID | None
```

Validate:

```text
0 <= probability <= 1
resolution deadline > forecast timestamp
```

---

## 4.8 `Decision`

```python
class Decision(Record):
    kind: Literal["decision"]

    state_snapshot_id: UUID

    question: str

    options: list[DecisionOption]

    selected_option_id: str

    owner: Literal[
        "human",
        "agent",
        "joint",
    ]

    human_perspective_id: UUID | None
    agent_perspective_id: UUID | None
    predicted_human_perspective_id: UUID | None

    reversible: bool

    expected_downside: Money | None

    budget_id: UUID | None

    review_after: AwareDatetime | None
```

The rejected options matter.

Never store only the winning action.

---

## 4.9 `ActionIntent`

Before an external side effect.

This is important for future autonomy.

```python
class ActionIntent(Record):
    kind: Literal["action_intent"]

    decision_id: UUID | None

    action_type: str
    target: str

    risk_class: ActionRisk

    parameters: dict[str, JsonValue]

    budget_id: UUID | None

    requires_human_approval: bool

    idempotency_key: str | None
```

---

## 4.10 `ActionReceipt`

Reality after the attempt.

```python
class ActionReceipt(Record):
    kind: Literal["action_receipt"]

    intent_id: UUID

    status: Literal[
        "success",
        "partial",
        "failure",
    ]

    started_at: AwareDatetime
    completed_at: AwareDatetime

    external_reference: str | None

    before_artifact_id: UUID | None
    after_artifact_id: UUID | None

    rollback_possible: bool
    rollback_receipt_id: UUID | None
```

This gives:

```text
intention
vs
actual result
```

which is crucial training data.

---

## 4.11 `ResourceReceipt`

Unified cognition/resources accounting.

```python
class ResourceReceipt(Record):
    kind: Literal["resource_receipt"]

    session_id: UUID | None
    action_intent_id: UUID | None

    provider: str | None
    model: str | None

    input_tokens: int | None
    cached_input_tokens: int | None
    output_tokens: int | None
    reasoning_tokens: int | None

    tool_calls: int | None

    human_seconds: int | None

    inference_cost_usd: Decimal | None
    external_cost_usd: Decimal | None

    measurement_quality: Literal[
        "exact",
        "provider_reported",
        "estimated",
    ]
```

OpenTelemetry's current GenAI conventions already standardize model and input/output token telemetry and trace trees around agent/model/tool calls, so mirror those names where practical rather than inventing conflicting semantics. ([OpenTelemetry][4])

---

## 4.12 `EconomicEvent`

Actual money.

```python
class EconomicEvent(Record):
    kind: Literal["economic_event"]

    category: Literal[
        "sale",
        "refund",
        "platform_fee",
        "advertising",
        "generation",
        "supplier",
        "shipping",
        "software",
        "domain",
        "other",
    ]

    amount: Decimal
    currency: str

    direction: Literal["inflow", "outflow"]

    brand_id: str | None

    external_reference: str | None
```

Do not estimate human time in dollars here.

---

## 4.13 `HumanIntervention`

```python
class HumanIntervention(Record):
    kind: Literal["human_intervention"]

    session_id: UUID
    trajectory_step_ref: str | None

    agent_intended_action: str

    human_message_artifact_id: UUID

    corrective_action: str

    inferred_reason: str | None
    inference_confidence: float | None

    scope: Literal[
        "single_action",
        "session",
        "until_condition",
        "decision_class",
        "persistent_candidate",
    ]

    termination_condition: Condition | None
```

Raw message is evidence.

Interpretation is explicitly marked inference.

---

## 4.14 `ScientificRecord`

Use a discriminated union rather than three completely separate persistence systems.

```python
ScientificRecord =
    Problem
    | Hypothesis
    | Experiment
```

### Problem

```python
class Problem(Record):
    problem_id: UUID

    statement: str
    severity: float

    evidence_refs: list[UUID]

    status: Literal[
        "open",
        "diagnosing",
        "testing",
        "resolved",
        "abandoned",
    ]
```

### Hypothesis

```python
class Hypothesis(Record):
    problem_id: UUID

    claim: str
    mechanism: str

    confidence_before: float

    falsification_conditions: list[str]
```

### Experiment

```python
class Experiment(Record):
    problem_id: UUID
    hypothesis_id: UUID

    preregistered_at: AwareDatetime

    intervention: str
    control: str | None

    primary_metric_id: str

    evaluation_at: AwareDatetime

    success_rule: str
```

No experiment result lives here.

---

## 4.15 `OutcomeReceipt`

Later reality.

```python
class OutcomeReceipt(Record):
    kind: Literal["outcome"]

    target_type: Literal[
        "forecast",
        "decision",
        "action",
        "experiment",
        "question",
        "intervention",
    ]

    target_id: UUID

    horizon: Literal[
        "immediate",
        "1d",
        "7d",
        "30d",
        "final",
        "custom",
    ]

    metric_changes: list[MetricDelta]

    economic_effect: Money | None

    conclusion: Literal[
        "positive",
        "negative",
        "neutral",
        "inconclusive",
    ]

    causal_confidence: Literal[
        "none",
        "weak",
        "moderate",
        "strong",
    ]
```

Original records remain untouched.

---

# 5. Two supporting records

These matter enough to formalize.

## `ContextManifest`

```python
class ContextManifest(Record):
    information_cutoff_at: AwareDatetime

    included_record_ids: list[UUID]
    included_artifact_ids: list[UUID]

    excluded_record_ids: list[UUID]
    excluded_memory_banks: list[str]

    model: str
    worker_version: str

    context_sha256: str
```

This proves:

```text
P did not see H
A did not see operator memory
cold reviewer did not see interpretations
historic replay did not see future outcomes
```

---

## `TransformReceipt`

Every derived transformation emits one.

```python
class TransformReceipt(Record):
    transform_name: str
    transform_version: str

    input_refs: list[ContentRef]
    output_refs: list[ContentRef]

    code_commit: str

    model: str | None
    prompt_version: str | None

    deterministic: bool

    resource_receipt_ids: list[UUID]
```

This is how future models can reprocess old data safely.

Conceptually this follows the useful W3C PROV distinction between entities, activities, agents and derivations without requiring the full PROV technology stack. ([W3C][3])

---

# 6. Yes: binary validations

But only for **objective invariants**.

Do not ask an LLM:

> Is this record valid?

for hard integrity conditions.

## Binary gate 1 — `SCHEMA_VALID`

```text
PASS:
Pydantic strict parse succeeds.

FAIL:
record rejected.
```

---

## Binary gate 2 — `REFERENCES_VALID`

```text
all referenced canonical IDs exist

all referenced artifacts exist

no dangling relationship
```

---

## Binary gate 3 — `TEMPORAL_VALID`

Examples:

```text
forecast occurred before outcome
experiment preregistered before intervention
end snapshot after start snapshot
human response committed before reveal
information cutoff not in future
```

---

## Binary gate 4 — `PROVENANCE_VALID`

```text
artifact SHA matches bytes
TransformReceipt inputs exist
output hash matches
event chain valid
```

---

## Binary gate 5 — `RIGHTS_VALID`

```text
public export contains no non-public record

training export contains only training-allowed records
```

---

## Binary gate 6 — `INDEPENDENCE_VALID`

```text
Predicted Human context excludes actual Human answer

Independent Agent excludes operator preference memory

ColdReview Pass A excludes human/worker interpretations

historical replay excludes later outcomes
```

---

## Binary gate 7 — `BUDGET_VALID`

```text
actual resource usage <= hard approved limits
```

where a hard limit exists.

---

## Binary gate 8 — `ACTION_POLICY_VALID`

Before any side effect:

```text
ActionIntent exists

risk category recognized

required approval exists

budget exists where needed

idempotency key present where appropriate
```

---

# 7. What should NOT be binary

Do not turn uncertain concepts into fake passes.

These remain scores/observations:

```text
Was this a good decision?
Was this question useful?
Did this session create value?
Is this memory useful?
Who was more correct?
Did human involvement help?
Was this strategy coherent?
```

Store:

```text
score
confidence
evidence
evaluator version
later outcomes
```

Do not mark them PASS merely because an agent says so.

---

# 8. CompanyDay completion gates

Separate corpus integrity from publishing.

## `CORPUS_COMPLETE`

Mechanical PASS requires:

```text
CompanyDay exists

start StateSnapshot

morning:
    P
    A
    H
    ContextManifests

all detected OpenCode sessions archived

all raw artifacts hashed

resource receipts reconciled

economic events reconciled where available

human session reviews captured for major sessions

worker debriefs captured

end StateSnapshot

human evening Perspective

cold review with blindness proof

all binary integrity gates pass
```

## `PUBLIC_PROJECTION_COMPLETE`

```text
rights-filtered DailyDigest exists
blog artifact generated
video script/package generated
```

## `DISTRIBUTION_COMPLETE`

Separate and optional:

```text
blog deployed
YouTube posted
TikTok posted
```

A TikTok API failure must never cause the corpus to become incomplete.

---

# 9. Fix the current `verify` semantics

The current repo says CompanyDay 0001 passes 13/13 checks, which is useful progress, but this should become substantially stricter.

Do not count:

```text
"perspectives >= 2"
```

as success.

Require:

```text
exactly required perspective roles exist

their ContextManifests prove separation

timestamps prove commit order
```

Similarly:

```text
"local artifacts = 2"
```

is not enough.

Require:

```text
every required artifact referenced by canonical records exists
SHA matches
backup receipt exists
```

Validation should establish **properties**, not counts.

---

# 10. Meta-enquiry transformation

Current prototype:

```text
KnowledgeGap
→ question
```

should become:

```text
StateSnapshot
+ open Problems
+ unresolved Forecasts
+ recent Decisions
+ prior QuestionOutcomes
+ EnquiryThreads

↓ GAP EXTRACTOR

KnowledgeGap[]

↓ CANDIDATE GENERATOR

QuestionCandidate[]

↓ SELECTOR

QuestionInstance[]

↓ P / A / H

Perspective[]

↓ later

QuestionOutcome[]
```

Current `meta_enquiry.py` should become a derived subsystem, not another source of truth.

Specific fixes:

```text
enforce sampling schedule

rank QuestionCandidates, not gaps

include urgency

divide by burden

fix redundancy matching

store exact QuestionInstance

remove free-form economic_impact unless unit/source defined

remove retrospective_value scalar for now

fix human_involution_helped typo

use timezone-aware timestamps

replace dict factories with Pydantic
```

---

# 11. Skills: yes, but only five initially

A Skill is **not memory**.

It is a typed executable operation.

Define:

```python
class SkillContract(BaseModel):
    name: str
    version: str

    input_schema_ref: str
    output_schema_ref: str

    permissions: set[Permission]

    side_effects: bool

    risk_class: ActionRisk

    preconditions: list[str]

    evaluator: str

    rollback_supported: bool

    evidence_refs: list[UUID]
```

Only create skills for stable repeated operations.

Start with:

```text
capture_opencode_session

snapshot_company_state

run_meta_enquiry

close_company_day

build_public_daily_digest
```

Potential sixth:

```text
archive_artifact
```

That is enough.

Do NOT yet make:

```text
SEO skill
marketing manager skill
CEO skill
brand strategist skill
```

Those come from actual repeated evidence.

---

# 12. Skill execution rule

Agent:

```text
selects Skill
       ↓
validates typed Input
       ↓
PolicyGate
       ↓
executes
       ↓
validates typed Output
       ↓
writes ActionReceipt
       ↓
runs evaluator
```

The skill itself cannot write arbitrary historical data.

All canonical writes go through one service:

```text
CorpusWriter.append(record)
```

---

# 13. One canonical writer

This is probably the most important repo simplification.

Everything currently writing:

```text
random JSON files
SQLite directly
ledger.jsonl
dogcasso/mythicbee-ops
protocol JSON
memory files
```

should eventually go through:

```python
CorpusWriter.append(record)
```

Internally:

```text
Pydantic strict validation
↓
invariant validation
↓
canonical serialization
↓
hash
↓
append ledger
↓
artifact backup if needed
```

No agent gets raw unrestricted database access.

---

# 14. Canonical persistence

Keep it boring.

```text
SQLite:
canonical event/index store

R2:
large content-addressed raw artifacts

JSON Schema:
public machine contract

Parquet:
analytics/training projection
```

No Hydra dependency.

No graph database dependency.

No vector database dependency.

Those can index the corpus later.

---

# 15. Export JSON schemas automatically

Pydantic can emit JSON Schema Draft 2020-12 directly.

Generate on CI:

```text
schemas/
├── record.schema.json
├── company_day.schema.json
├── perspective.schema.json
├── decision.schema.json
├── action_intent.schema.json
├── action_receipt.schema.json
├── experiment.schema.json
└── ...
```

Then:

```bash
stallshark schemas generate
stallshark schemas verify-clean
```

fails if generated schemas differ from committed schemas.

This gives every future:

```text
Python agent
TypeScript agent
Rust worker
external research tool
```

the same contract.

---

# 16. Canonical transformation graph

```text
RAW OPENCODE
   ↓
Session
   ↓
TrajectoryIR          DERIVED
   ↓
DecisionEpisode       DERIVED

VOICE
   ↓
Artifact
   ↓
Transcript            DERIVED
   ↓
Perspective extraction

MARKET / BUSINESS FACTS
   ↓
StateSnapshot

STATE + HISTORY
   ↓
KnowledgeGap          DERIVED
   ↓
QuestionInstance
   ↓
P/A/H Perspectives

Decision
   ↓
ActionIntent
   ↓
ActionReceipt
   ↓
OutcomeReceipt

ALL COMPANYDAY RECORDS
   ↓
CompanyDayManifest    DERIVED
   ↓
rights filter
   ↓
PublicDailyDigest
   ↓
blog / short / social

500 CompanyDays
   ↓
Parquet
   ↓
DecisionEpisodes
   ↓
training/eval datasets
```

---

# 17. Final 500-day analytical tables

After 500 days, projections should trivially produce:

```text
company_days.parquet

sessions.parquet
resource_usage.parquet

questions.parquet
question_answers.parquet
question_outcomes.parquet

perspectives.parquet
beliefs.parquet
forecasts.parquet

decisions.parquet
decision_options.parquet

actions.parquet
interventions.parquet

problems.parquet
hypotheses.parquet
experiments.parquet

economic_events.parquet
outcomes.parquet
```

These are analytical tables.

They are not sources of truth.

---

# 18. The truly valuable derived table

`decision_episodes.parquet`

One row per consequential decision.

Columns conceptually:

```text
company_day
business_state

information_available

human_view
agent_view
predicted_human_view

questions_that_preceded_decision

options
human_preference
agent_preference
chosen_action

budget

human_interventions

execution_summary

immediate_outcome
1d_outcome
7d_outcome
30d_outcome

human_forecast_accuracy
agent_forecast_accuracy

human_involvement
```

This is arguably the highest-value asset.

---

# 19. Model-training paths

The corpus naturally creates several different training problems.

## Operator model

```text
(state, question, historical operator context)
→ human answer
```

Learns:

> what would the operator probably think?

---

## Preference/ranking model

```text
(state, options)
→ human ranking
```

Learns human taste/management preferences.

---

## Economic critic

```text
(state, chosen action, budget)
→ later outcome
```

Learns:

> what appears economically effective?

Separate from operator preference.

---

## Question policy

```text
(state, knowledge gaps, candidate question)
→ later QuestionOutcome
```

Learns:

> is this human worth interrupting with this question?

---

## Delegation policy

```text
(task, state, agent confidence, historical competence)
→ human involvement benefit
```

Learns:

```text
agent autonomous
human review
joint
human lead
```

---

## Intervention predictor

```text
trajectory state
→ probability human intervenes
```

Useful for PPL-style preference learning.

---

## Forecast calibrator

```text
actor + domain + raw probability
→ calibrated probability
```

---

## Memory reranker

```text
current task + candidate memory
→ downstream usefulness
```

Allows future agent to retrieve only memories that justify their token cost.

---

# 20. Public dataset lineage

The public story:

```text
Day 147 — £X revenue
```

must trace back to:

```text
PublicDailyDigest
↓
CompanyDay
↓
EconomicEvents
↓
receipts
```

Likewise:

> “The human wanted A and the agent wanted B.”

must trace to prospectively committed Perspectives.

No narrative should be the only record of an event.

---

# 21. Repo cleanup

Do not delete research immediately.

Classify every current module as:

```text
CANONICAL
DERIVED
ADAPTER
EXPERIMENTAL
ARCHIVE
```

Target:

```text
src/stallshark/
├── schemas/
├── corpus/
├── capture/
├── transforms/
├── validation/
├── skills/
└── cli/
```

Old:

```text
tool/book_schemas.py
tool/meta_enquiry.py
tool/kernel.py
tool/dp2_final.py
...
```

become temporary adapters or archived prototypes once functionality moves.

Do not maintain two implementations indefinitely.

---

# 22. `AGENTS.md`

Keep it.

It should be extremely small.

It defines:

```text
mission
axioms
permissions
canonical write rule
daily workflow
scope boundaries
```

It should not become accumulated company memory.

The existing version is already close.

Add:

```text
All historical writes MUST pass CorpusWriter.

Never mutate a canonical record.

Never infer unavailable metrics as zero.

Derived interpretations MUST reference source evidence.

Hard validation failures halt autonomous writes.

LLM judgments cannot satisfy hard validation gates.

Current explicit human intent outranks operator memory.

No irreversible or uncapped monetary action without explicit permission.
```

---

# 23. What not to implement now

Do not build:

```text
full autonomous CEO

complex skill marketplace

graph database

new memory DB

offline RL

fine-tuning

automatic organizational spawning

general marketplace simulator

advanced HumanValue dollar model

complex question-policy ML
```

Capture the fields that make those possible.

---

# 24. Immediate migration sprint

## Step 1

Create:

```text
src/stallshark/schemas/
```

and convert the canonical records above to Pydantic.

---

## Step 2

Implement:

```text
CorpusWriter
```

with strict validation.

---

## Step 3

Implement eight hard validators:

```text
schema
references
temporal
provenance
rights
independence
budget
action policy
```

All return mechanical PASS/FAIL plus evidence.

---

## Step 4

Make:

```text
stallshark verify --day today
```

use those validators.

---

## Step 5

Convert:

```text
OpenCode capture
meta enquiry
daily close
```

to canonical writer.

---

## Step 6

Build one deterministic synthetic CompanyDay.

Prove:

```text
raw inputs
→ canonical records
→ validations
→ DailyDigest
→ decision episode
→ Parquet export
```

---

## Step 7

Run one real CompanyDay.

Then freeze architecture.

---

# 25. Final principle

The system should optimize for one question:

> **If StallShark disappeared on Day 501, could a researcher or future agent reconstruct exactly what the human and agents knew, believed, chose, spent, did and learned across the entire $0→$1M trajectory?**

If yes, the corpus worked.

The system does not need to know today how the future model will learn from it.

It needs to ensure future models have **clean, prospective, provenance-preserving evidence rather than retrospective stories**.

The immediate code change I would make is therefore **not another agent capability**. It is to turn the current excellent-but-loose objects—especially the new meta-enquiry models—into strict Pydantic records behind one `CorpusWriter`, and make the current 13/13 day verification become genuine invariant checks rather than existence/count checks.

After that, the schema substrate is stable enough to start accumulating the 500 days.

[1]: https://docs.pydantic.dev/latest/concepts/strict_mode/ "Strict Mode | Pydantic Docs"
[2]: https://json-schema.org/specification?utm_source=chatgpt.com "JSON Schema - Specification [#section]"
[3]: https://www.w3.org/TR/prov-primer/?utm_source=chatgpt.com "PROV Model Primer"
[4]: https://opentelemetry.io/blog/2026/genai-observability/?utm_source=chatgpt.com "Inside the LLM Call: GenAI Observability with OpenTelemetry | OpenTelemetry"
