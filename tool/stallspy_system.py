#!/usr/bin/env python3
"""
StallSpy Agent — PydanticAI integration with private-lab contracts.

This is the working harness that replaces Letta.
It uses PydanticAI for orchestration, our contracts for types,
and the event ledger for persistence.
"""
from __future__ import annotations

import json
import os
import sqlite3
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field
from pydantic_ai import Agent

# ── Paths ───────────────────────────────────────────────────────────────

STALLSPY = Path("/root/StallSpy")
LEDGER_DB = STALLSPY / "data" / "ledger.db"
CORPUS_DIR = STALLSPY / "corpus"

# ── Contracts (Pydantic models matching private-lab) ─────────────────────

class SubjectiveState(BaseModel):
    """What an actor believes about the business right now."""
    snapshot_id: str = Field(default_factory=lambda: f"S_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    actor_type: str  # "human", "agent", "fresh_agent"
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

    objective_next_hours: str = ""
    objective_today: str = ""
    objective_7d: str = ""
    objective_30d: str = ""
    objective_mission: str = ""

    momentum: float = 0.5
    business_health: float = 0.5
    strategy_confidence: float = 0.5
    uncertainty: float = 0.5
    urgency: float = 0.5

    bottleneck: str = ""
    bottleneck_confidence: float = 0.5

    top_opportunities: list[str] = []
    top_risks: list[str] = []
    active_problems: list[str] = []
    beliefs: list[str] = []
    unknowns: list[str] = []

    preferred_actions: list[str] = []
    actions_to_avoid: list[str] = []

    what_would_change_my_mind: str = ""
    biggest_concern: str = ""
    biggest_excitement: str = ""

    def to_dict(self) -> dict:
        return self.model_dump()


class RunReceipt(BaseModel):
    """Immutable record of what happened."""
    run_id: str = Field(default_factory=lambda: f"run_{uuid.uuid4().hex[:12]}")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    task: str = ""
    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    success: bool = True
    artifacts: list[str] = []
    notes: str = ""


class ForecastEntry(BaseModel):
    """Prospective prediction before outcome is known."""
    forecast_id: str = Field(default_factory=lambda: f"F_{uuid.uuid4().hex[:8]}")
    question: str = ""
    human_probability: float = 0.5
    agent_probability: float = 0.5
    resolution_condition: str = ""
    resolution_deadline: str = ""
    outcome: Optional[bool] = None


class Problem(BaseModel):
    """Persistent problem registry entry."""
    problem_id: str = Field(default_factory=lambda: f"P_{uuid.uuid4().hex[:8]}")
    statement: str = ""
    detected_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    severity: float = 0.5
    status: str = "diagnosing"  # diagnosing, experimenting, resolved, killed
    hypotheses: list[str] = []
    experiments: list[str] = []


# ── Event Ledger (SQLite append-only) ────────────────────────────────────

class EventLedger:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or str(LEDGER_DB)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                event_type TEXT NOT NULL,
                entity_id TEXT,
                payload_json TEXT NOT NULL,
                payload_sha256 TEXT,
                previous_event_hash TEXT,
                event_hash TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS subjective_states (
                snapshot_id TEXT PRIMARY KEY,
                actor_type TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                data_json TEXT NOT NULL
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS forecasts (
                forecast_id TEXT PRIMARY KEY,
                question TEXT,
                human_prob REAL,
                agent_prob REAL,
                resolution_condition TEXT,
                resolution_deadline TEXT,
                outcome INTEGER,
                created_at TEXT NOT NULL
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS token_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                model TEXT,
                input_tokens INTEGER,
                output_tokens INTEGER,
                cost_usd REAL,
                task TEXT,
                agent TEXT
            )
        """)
        self.conn.commit()

    def append_event(self, event_type: str, entity_id: str, payload: dict) -> str:
        import hashlib
        event_id = f"evt_{uuid.uuid4().hex[:12]}"
        payload_json = json.dumps(payload, default=str)
        payload_hash = hashlib.sha256(payload_json.encode()).hexdigest()

        # Get previous hash
        cursor = self.conn.execute("SELECT event_hash FROM events ORDER BY rowid DESC LIMIT 1")
        prev_hash = cursor.fetchone()
        prev_hash = prev_hash[0] if prev_hash else "genesis"

        # Compute event hash
        event_data = f"{event_id}{event_type}{entity_id}{payload_json}{prev_hash}"
        event_hash = hashlib.sha256(event_data.encode()).hexdigest()

        self.conn.execute(
            "INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (event_id, event_type, entity_id, payload_json, payload_hash,
             prev_hash, event_hash, datetime.now().isoformat())
        )
        self.conn.commit()
        return event_id

    def record_subjective_state(self, state: SubjectiveState):
        self.conn.execute(
            "INSERT OR REPLACE INTO subjective_states VALUES (?, ?, ?, ?)",
            (state.snapshot_id, state.actor_type, state.timestamp,
             json.dumps(state.to_dict()))
        )
        self.conn.commit()
        self.append_event("subjective_state.recorded", state.snapshot_id, state.to_dict())

    def record_token_usage(self, model: str, input_tokens: int, output_tokens: int,
                           cost: float, task: str, agent: str = ""):
        self.conn.execute(
            "INSERT INTO token_usage (timestamp, model, input_tokens, output_tokens, cost_usd, task, agent) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (datetime.now().isoformat(), model, input_tokens, output_tokens, cost, task, agent)
        )
        self.conn.commit()
        self.append_event("token_usage.recorded", "", {
            "model": model, "input_tokens": input_tokens,
            "output_tokens": output_tokens, "cost_usd": cost, "task": task
        })

    def get_token_summary(self, date: str = None) -> dict:
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        cursor = self.conn.execute(
            "SELECT model, SUM(input_tokens+output_tokens), SUM(cost_usd) FROM token_usage WHERE timestamp LIKE ? GROUP BY model",
            (f"{date}%",)
        )
        return {row[0]: {"tokens": row[1], "cost": row[2]} for row in cursor.fetchall()}

    def get_state_count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM subjective_states").fetchone()[0]

    def get_event_count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]


# ── Model Selection ──────────────────────────────────────────────────────
# Use test model if no API key, real model if key available.
# Set OPENAI_API_KEY or ANTHROPIC_API_KEY to use real models.

import os
MODEL = "test"  # Default to test model for architecture validation
if os.environ.get("OPENAI_API_KEY") or os.environ.get("ANTHROPIC_API_KEY"):
    MODEL = "openai:gpt-4o-mini"  # Or whichever provider is configured
print(f"Using model: {MODEL}")

# ── The Operator Twin Agent ──────────────────────────────────────────────

OPERATOR_TWIN_SYSTEM = """You are the Operator Twin — a model that predicts what the human operator would decide in a given business state.

You have observed the operator's past decisions, preferences, and reasoning patterns.

Given the current business state, predict:
1. What the operator's primary objective would be
2. What action they would choose
3. Their confidence level
4. What they would be worried about
5. What they'd be excited about

Be specific. Reference past patterns when possible. Assign probabilities."""

operator_twin = Agent(
    MODEL,
    system_prompt=OPERATOR_TWIN_SYSTEM,
    output_type=SubjectiveState,
)

# ── The Economic Critic Agent ────────────────────────────────────────────

ECONOMIC_CRITIC_SYSTEM = """You are the Economic Critic — a model that predicts what action would best serve the business objective, regardless of what the human wants.

You analyze:
1. Current metrics (sales, conversion, traffic, costs)
2. Market conditions
3. Resource constraints
4. Historical what-has-worked data

Recommend the action with highest expected economic value. Be quantitative where possible."""

economic_critic = Agent(
    MODEL,
    system_prompt=ECONOMIC_CRITIC_SYSTEM,
    output_type=SubjectiveState,
)

# ── The Cold Review Agent ────────────────────────────────────────────────

COLD_REVIEW_SYSTEM = """You are the Cold Reviewer — a fresh agent reviewing a day's business activity WITHOUT seeing any previous interpretations.

You receive ONLY:
- Business state metrics
- Actions taken (from git/ledger)
- Costs incurred
- Outcomes observed

You do NOT see:
- What the human thought about the day
- What the working agent thought about the day

Form your own independent assessment:
1. What actually happened?
2. Which actions were useful?
3. Which were waste?
4. Did work match stated priorities?
5. What should tomorrow's agent know?

Be brutally honest. Your independence is the feature."""

cold_reviewer = Agent(
    MODEL,
    system_prompt=COLD_REVIEW_SYSTEM,
    output_type=SubjectiveState,
)


# ── The Interview System ────────────────────────────────────────────────

INTERVIEW_SYSTEM = """You are the Interview Agent. Given the current business state and recent activity,
generate the 3-5 most valuable questions to ask the human operator right now.

Focus on:
- Highest information value questions
- Questions the human can uniquely answer
- Decisions that need human judgment
- Divergence between what was planned vs what happened

Output a list of questions, each with:
- The question
- Why this question now (what makes it high-value)
- What decision it could alter today"""

interview_agent = Agent(
    MODEL,
    system_prompt=INTERVIEW_SYSTEM,
)


# ── Wire It All Together ────────────────────────────────────────────────

class StallSpySystem:
    """The integrated system: contracts + ledger + agents."""

    def __init__(self):
        self.ledger = EventLedger()
        self.today_states: list[SubjectiveState] = []

    def morning_interview(self, business_state: dict) -> dict:
        """Generate interview questions based on business state."""
        result = interview_agent.run_sync(
            f"Current business state: {json.dumps(business_state, default=str)}"
        )
        return {"questions": result.output}

    def predict_human(self, business_state: dict) -> SubjectiveState:
        """Agent predicts what the human would say."""
        result = operator_twin.run_sync(
            f"Current business state: {json.dumps(business_state, default=str)}"
        )
        state = result.output
        state.actor_type = "agent_predicted_human"
        self.ledger.record_subjective_state(state)
        return state

    def economic_critique(self, business_state: dict) -> SubjectiveState:
        """Agent's independent economic recommendation."""
        result = economic_critic.run_sync(
            f"Current business state: {json.dumps(business_state, default=str)}"
        )
        state = result.output
        state.actor_type = "agent_critic"
        self.ledger.record_subjective_state(state)
        return state

    def cold_review(self, day_data: dict) -> SubjectiveState:
        """Fresh agent reviews the day blind."""
        result = cold_reviewer.run_sync(
            f"Day's data: {json.dumps(day_data, default=str)}"
        )
        state = result.output
        state.actor_type = "fresh_agent"
        self.ledger.record_subjective_state(state)
        return state

    def record_human_state(self, state: SubjectiveState):
        """Record the human's actual subjective state."""
        state.actor_type = "human"
        self.ledger.record_subjective_state(state)

    def divergence(self, human: SubjectiveState, predicted: SubjectiveState,
                   critic: SubjectiveState) -> dict:
        """Compute divergence between three perspectives."""
        def vdiff(a, b):
            return abs(a - b) if isinstance(a, (int, float)) else 0

        return {
            "objective_alignment": 1.0 - vdiff(
                hash(human.objective_today) % 100 / 100,
                hash(predicted.objective_today) % 100 / 100
            ),
            "confidence_delta_human_predicted": vdiff(
                human.strategy_confidence, predicted.strategy_confidence
            ),
            "confidence_delta_human_critic": vdiff(
                human.strategy_confidence, critic.strategy_confidence
            ),
            "bottleneck_agreement": human.bottleneck == predicted.bottleneck,
            "risk_delta": vdiff(human.uncertainty, critic.uncertainty),
        }

    def status(self) -> dict:
        return {
            "events": self.ledger.get_event_count(),
            "states": self.ledger.get_state_count(),
            "token_summary": self.ledger.get_token_summary(),
        }


# ── Quick Test ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== StallSpy System Test ===\n")

    system = StallSpySystem()

    # Simulate a business state
    business_state = {
        "day": 5,
        "cash": 88.37,
        "revenue": 0,
        "listings": 0,
        "active_brands": ["dogcasso"],
        "top_problem": "nothing launched yet",
        "yesterday_actions": ["wrote specs", "cloned repos", "built scraper"],
    }

    print("1. Morning interview...")
    interview = system.morning_interview(business_state)
    print(f"   Questions: {interview.get('questions', 'generated')[:200]}")

    print("\n2. Agent predicts human...")
    predicted = system.predict_human(business_state)
    print(f"   Predicted objective: {predicted.objective_today}")
    print(f"   Predicted bottleneck: {predicted.bottleneck}")

    print("\n3. Economic critic...")
    critic = system.economic_critique(business_state)
    print(f"   Critic objective: {critic.objective_today}")
    print(f"   Critic bottleneck: {critic.bottleneck}")

    print("\n4. Cold review (simulated day data)...")
    day_data = {
        "actions": ["wrote 12 spec docs", "cloned 7 repos", "built scraper"],
        "costs": {"tokens": 50000, "cash": 0},
        "outcomes": {"listings": 0, "revenue": 0},
    }
    cold = system.cold_review(day_data)
    print(f"   Cold assessment: {cold.biggest_concern}")

    # Record human state (simulated)
    human = SubjectiveState(
        actor_type="human",
        objective_today="get first listing live",
        bottleneck="haven't launched anything",
        strategy_confidence=0.6,
        uncertainty=0.7,
        biggest_concern="spending too much time on infrastructure",
        biggest_excitement="the concept is strong",
    )
    system.record_human_state(human)

    print("\n5. Divergence analysis...")
    div = system.divergence(human, predicted, critic)
    print(f"   Human vs predicted confidence delta: {div['confidence_delta_human_predicted']:.2f}")
    print(f"   Human vs critic confidence delta: {div['confidence_delta_human_critic']:.2f}")
    print(f"   Bottleneck agreement: {div['bottleneck_agreement']}")

    print("\n6. System status...")
    status = system.status()
    print(f"   Events: {status['events']}")
    print(f"   States: {status['states']}")

    print("\n=== All working ===")
