"""
StallShark Canonical Pydantic Schemas

Canonical record types for the Commerce Trajectory Corpus.
All records inherit from Record base.
Binary validation for objective invariants.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from enum import StrEnum
from typing import Literal, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


# ── Enums ────────────────────────────────────────────────────────────────

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


# ── Base Record ──────────────────────────────────────────────────────────

class Record(BaseModel):
    """Base for all canonical records."""
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    id: UUID = Field(default_factory=uuid4)
    kind: str
    schema_version: Literal["1.0"] = "1.0"
    company_day_id: Optional[UUID] = None
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    recorded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    actor_type: ActorType = ActorType.SYSTEM
    provenance: Optional[str] = None
    rights: RightsClass = RightsClass.FIRST_PARTY_PRIVATE
    correlation_id: Optional[UUID] = None
    causation_id: Optional[UUID] = None
    supersedes_id: Optional[UUID] = None


# ── Core Records ─────────────────────────────────────────────────────────

class CompanyDay(Record):
    kind: Literal["company_day"] = "company_day"
    day_number: int = 0
    local_date: date = Field(default_factory=date.today)
    timezone: str = "UTC"
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    closed_at: Optional[datetime] = None
    primary_brand: Optional[str] = None
    status: Literal["open", "closed", "incomplete"] = "open"

class StateSnapshot(Record):
    kind: Literal["state_snapshot"] = "state_snapshot"
    phase: Literal["start", "checkpoint", "end"] = "start"
    cash: Optional[float] = None
    cumulative_revenue: Optional[float] = None
    cumulative_profit: Optional[float] = None
    brand_states: list[dict] = []
    active_problem_ids: list[UUID] = []
    active_experiment_ids: list[UUID] = []
    git_commit: Optional[str] = None
    git_dirty: bool = False

class Session(Record):
    kind: Literal["session"] = "session"
    runtime: str = "opencode"
    external_session_id: str = ""
    objective: str = ""
    ended_at: Optional[datetime] = None
    repo_commit_before: Optional[str] = None
    repo_commit_after: Optional[str] = None
    raw_trace_artifact_id: Optional[UUID] = None
    sanitized_trace_artifact_id: Optional[UUID] = None
    result: Literal["success", "partial", "failure", "unknown"] = "unknown"

class Perspective(Record):
    kind: Literal["perspective"] = "perspective"
    perspective_kind: PerspectiveKind = PerspectiveKind.HUMAN_ACTUAL
    state_snapshot_id: Optional[UUID] = None
    objectives: dict = {}
    bottleneck_claim: str = ""
    bottleneck_confidence: float = 0.5
    beliefs: list[str] = []
    opportunities: list[str] = []
    risks: list[str] = []
    preferred_action: str = ""
    strategy_confidence: float = 0.5

class Decision(Record):
    kind: Literal["decision"] = "decision"
    state_snapshot_id: Optional[UUID] = None
    question: str = ""
    options: list[str] = []
    selected_option: str = ""
    owner: Literal["human", "agent", "joint"] = "human"
    reversible: bool = True
    confidence: float = 0.5
    rationale: str = ""
    budget_cash: float = 0.0
    budget_human_minutes: int = 0
    budget_agent_tokens: int = 0

class Problem(Record):
    kind: Literal["problem"] = "problem"
    statement: str = ""
    severity: float = 0.5
    evidence_refs: list[UUID] = []
    status: Literal["open", "diagnosing", "testing", "resolved", "abandoned"] = "open"

class Hypothesis(Record):
    kind: Literal["hypothesis"] = "hypothesis"
    problem_id: Optional[UUID] = None
    claim: str = ""
    mechanism: str = ""
    confidence_before: float = 0.5
    falsification_conditions: list[str] = []

class Experiment(Record):
    kind: Literal["experiment"] = "experiment"
    problem_id: Optional[UUID] = None
    hypothesis_id: Optional[UUID] = None
    intervention: str = ""
    control: Optional[str] = None
    primary_metric: str = "conversion_rate"
    success_rule: str = ""
    status: Literal["designed", "running", "evaluating", "concluded"] = "designed"
    result: Optional[dict] = None

class EconomicEvent(Record):
    kind: Literal["economic_event"] = "economic_event"
    category: Literal["sale", "refund", "platform_fee", "advertising", "generation",
                       "supplier", "shipping", "software", "domain", "model", "other"] = "other"
    amount: float = 0.0
    currency: str = "USD"
    direction: Literal["inflow", "outflow"] = "outflow"
    brand_id: Optional[str] = None

class HumanIntervention(Record):
    kind: Literal["human_intervention"] = "human_intervention"
    session_id: Optional[UUID] = None
    agent_intended_action: str = ""
    human_override: str = ""
    reason: str = ""
    inferred_reason: Optional[str] = None
    scope: Literal["single_action", "session", "until_condition", "decision_class"] = "single_action"

class KnowledgeGap(Record):
    kind: Literal["knowledge_gap"] = "knowledge_gap"
    target_type: str = ""
    description: str = ""
    uncertainty: float = 0.5
    decision_impact: float = 0.5
    human_advantage: float = 0.5
    agent_advantage: float = 0.5

class QuestionInstance(Record):
    kind: Literal["question"] = "question"
    objective_id: str = ""
    exact_wording: str = ""
    cadence: Literal["morning", "session_close", "evening", "weekly"] = "morning"
    action_hook: str = ""
    estimated_burden_seconds: int = 60

class Forecast(Record):
    kind: Literal["forecast"] = "forecast"
    proposition: str = ""
    probability: float = 0.5
    resolution_condition: str = ""
    resolution_deadline: Optional[datetime] = None
    resolved_outcome: Optional[bool] = None

class OutcomeReceipt(Record):
    kind: Literal["outcome"] = "outcome"
    target_type: Literal["forecast", "decision", "action", "experiment"] = "decision"
    target_id: Optional[UUID] = None
    horizon: Literal["immediate", "1d", "7d", "30d", "final"] = "immediate"
    economic_effect: Optional[float] = None
    conclusion: Literal["positive", "negative", "neutral", "inconclusive"] = "neutral"

class ContextManifest(Record):
    kind: Literal["context_manifest"] = "context_manifest"
    information_cutoff_at: Optional[datetime] = None
    included_record_ids: list[UUID] = []
    excluded_record_ids: list[UUID] = []
    excluded_memory_banks: list[str] = []
    model: str = ""
    context_sha256: str = ""


# ── Binary Validators ────────────────────────────────────────────────────

class ValidationResult(BaseModel):
    gate: str
    status: ValidationStatus
    details: str = ""

def validate_schema(record: Record) -> ValidationResult:
    """Gate 1: Pydantic strict parse."""
    try:
        record.__class__.model_validate(record.model_dump())
        return ValidationResult(gate="SCHEMA_VALID", status=ValidationStatus.PASS)
    except Exception as e:
        return ValidationResult(gate="SCHEMA_VALID", status=ValidationStatus.FAIL, details=str(e))

def validate_temporal(record: Record) -> ValidationResult:
    """Gate 3: Temporal ordering."""
    if hasattr(record, 'closed_at') and record.closed_at:
        if record.closed_at < record.occurred_at:
            return ValidationResult(gate="TEMPORAL_VALID", status=ValidationStatus.FAIL,
                                   details="closed_at before occurred_at")
    return ValidationResult(gate="TEMPORAL_VALID", status=ValidationStatus.PASS)

def validate_independence(perspective_kind: PerspectiveKind,
                          has_human_answer: bool,
                          has_interpretations: bool) -> ValidationResult:
    """Gate 6: Independence proof."""
    if perspective_kind == PerspectiveKind.COLD_REVIEW and has_interpretations:
        return ValidationResult(gate="INDEPENDENCE_VALID", status=ValidationStatus.FAIL,
                               details="ColdReview saw interpretations")
    if perspective_kind == PerspectiveKind.PREDICTED_HUMAN and has_human_answer:
        return ValidationResult(gate="INDEPENDENCE_VALID", status=ValidationStatus.FAIL,
                               details="Predicted human saw actual answer")
    return ValidationResult(gate="INDEPENDENCE_VALID", status=ValidationStatus.PASS)
