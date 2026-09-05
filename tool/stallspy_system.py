#!/usr/bin/env python3
"""
StallSpy Integrated System — Full Pipeline
Wires: PydanticAI + Event Ledger + Operator Twin + Cold Review + Token Tracking + Memory
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

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent

# ── Paths ───────────────────────────────────────────────────────────────

STALLSPY = Path("/root/StallSpy")
LEDGER_DB = STALLSPY / "data" / "ledger.db"
load_dotenv(STALLSPY / ".env")

# ── Model Selection ──────────────────────────────────────────────────────

import os
# Model selection with graceful fallback
# OpenCode mimo-v2.5 API doesn't support structured outputs (PydanticAI requirement)
# Use test model for architecture validation, or OpenAI/Anthropic for real model
if os.environ.get("OPENAI_API_KEY") and not os.environ.get("OPENAI_BASE_URL"):
    MODEL = "openai:gpt-4o-mini"
    print(f"Model: {MODEL}")
elif os.environ.get("ANTHROPIC_API_KEY"):
    MODEL = "anthropic:claude-3-5-haiku-latest"
    print(f"Model: {MODEL}")
elif os.environ.get("OPENAI_API_KEY") and os.environ.get("OPENAI_BASE_URL"):
    # OpenCode API — doesn't support structured outputs yet
    # Fall back to test model for architecture validation
    print("OpenCode API detected but doesn't support structured outputs.")
    print("Falling back to test model. Set ANTHROPIC_API_KEY for real model.")
    MODEL = "test"
else:
    MODEL = "test"
    print(f"Model: test (no API key — architecture validation only)")

# ── Contracts ────────────────────────────────────────────────────────────

class SubjectiveState(BaseModel):
    """What an actor believes about the business right now."""
    snapshot_id: str = Field(default_factory=lambda: f"S_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    actor_type: str
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
    def to_dict(self): return self.model_dump()

class WorkBudget(BaseModel):
    """BATS-style budget for a work order."""
    cash_usd: float = 5.0
    tokens: int = 500000
    human_minutes: int = 60
    model: str = MODEL
    stop_conditions: list[str] = []

class TokenEvent(BaseModel):
    """Record of a model call."""
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    task: str = ""
    agent: str = ""

class MemoryEntry(BaseModel):
    """PAHF-style memory entry."""
    memory_id: str = Field(default_factory=lambda: f"mem_{uuid.uuid4().hex[:8]}")
    category: str = ""  # stable_preference, contextual_preference, routine, latent_rule
    claim: str = ""
    confidence: float = 0.5
    evidence_count: int = 1
    contradictions: int = 0
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    last_validated: str = ""
    scope: str = ""
    def to_dict(self): return self.model_dump()

# ── Event Ledger ─────────────────────────────────────────────────────────

class EventLedger:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or str(LEDGER_DB)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self._init_db()

    def _init_db(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                event_type TEXT NOT NULL,
                entity_id TEXT,
                payload_json TEXT NOT NULL,
                payload_sha256 TEXT,
                previous_event_hash TEXT,
                event_hash TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS subjective_states (
                snapshot_id TEXT PRIMARY KEY,
                actor_type TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                data_json TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS token_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                model TEXT, input_tokens INTEGER, output_tokens INTEGER,
                cost_usd REAL, task TEXT, agent TEXT
            );
            CREATE TABLE IF NOT EXISTS memory (
                memory_id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                claim TEXT NOT NULL,
                confidence REAL,
                evidence_count INTEGER DEFAULT 1,
                contradictions INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                last_validated TEXT,
                scope TEXT
            );
            CREATE TABLE IF NOT EXISTS problems (
                problem_id TEXT PRIMARY KEY,
                statement TEXT NOT NULL,
                detected_at TEXT NOT NULL,
                severity REAL DEFAULT 0.5,
                status TEXT DEFAULT 'diagnosing',
                hypotheses TEXT DEFAULT '[]',
                experiments TEXT DEFAULT '[]'
            );
        """)
        self.conn.commit()

    def append_event(self, event_type, entity_id, payload):
        import hashlib
        event_id = f"evt_{uuid.uuid4().hex[:12]}"
        pj = json.dumps(payload, default=str)
        ph = hashlib.sha256(pj.encode()).hexdigest()
        cur = self.conn.execute("SELECT event_hash FROM events ORDER BY rowid DESC LIMIT 1")
        prev = cur.fetchone()
        prev_hash = prev[0] if prev else "genesis"
        eh = hashlib.sha256(f"{event_id}{event_type}{entity_id}{pj}{prev_hash}".encode()).hexdigest()
        self.conn.execute("INSERT INTO events VALUES (?,?,?,?,?,?,?,?)",
            (event_id, event_type, entity_id, pj, ph, prev_hash, eh, datetime.now().isoformat()))
        self.conn.commit()
        return event_id

    def record_state(self, state: SubjectiveState):
        self.conn.execute("INSERT OR REPLACE INTO subjective_states VALUES (?,?,?,?)",
            (state.snapshot_id, state.actor_type, state.timestamp, json.dumps(state.to_dict())))
        self.conn.commit()
        self.append_event("subjective_state.recorded", state.snapshot_id, state.to_dict())

    def record_tokens(self, te: TokenEvent):
        self.conn.execute("INSERT INTO token_usage (timestamp,model,input_tokens,output_tokens,cost_usd,task,agent) VALUES (?,?,?,?,?,?,?)",
            (te.timestamp, te.model, te.input_tokens, te.output_tokens, te.cost_usd, te.task, te.agent))
        self.conn.commit()

    def record_memory(self, m: MemoryEntry):
        self.conn.execute("INSERT OR REPLACE INTO memory VALUES (?,?,?,?,?,?,?,?,?)",
            (m.memory_id, m.category, m.claim, m.confidence, m.evidence_count,
             m.contradictions, m.created_at, m.last_validated, m.scope))
        self.conn.commit()
        self.append_event("memory.recorded", m.memory_id, m.to_dict())

    def record_problem(self, problem_id, statement, severity=0.5):
        self.conn.execute("INSERT OR REPLACE INTO problems VALUES (?,?,?,?,?,?,?)",
            (problem_id, statement, datetime.now().isoformat(), severity, "diagnosing", "[]", "[]"))
        self.conn.commit()
        self.append_event("problem.created", problem_id, {"statement": statement, "severity": severity})

    def get_state_count(self): return self.conn.execute("SELECT COUNT(*) FROM subjective_states").fetchone()[0]
    def get_event_count(self): return self.conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    def get_memory_count(self): return self.conn.execute("SELECT COUNT(*) FROM memory").fetchone()[0]
    def get_problem_count(self): return self.conn.execute("SELECT COUNT(*) FROM problems").fetchone()[0]

    def get_token_summary(self, date=None):
        if not date: date = datetime.now().strftime("%Y-%m-%d")
        cur = self.conn.execute("SELECT model, SUM(input_tokens+output_tokens), SUM(cost_usd) FROM token_usage WHERE timestamp LIKE ? GROUP BY model", (f"{date}%",))
        return {r[0]: {"tokens": r[1], "cost": r[2]} for r in cur.fetchall()}

    def search_memory(self, category=None, min_confidence=0.5):
        if category:
            cur = self.conn.execute("SELECT * FROM memory WHERE category=? AND confidence>=? ORDER BY confidence DESC", (category, min_confidence))
        else:
            cur = self.conn.execute("SELECT * FROM memory WHERE confidence>=? ORDER BY confidence DESC", (min_confidence,))
        return [dict(zip([d[0] for d in cur.description], row)) for row in cur.fetchall()]

    def get_open_problems(self):
        cur = self.conn.execute("SELECT * FROM problems WHERE status='diagnosing' ORDER BY severity DESC")
        return [dict(zip([d[0] for d in cur.description], row)) for row in cur.fetchall()]

# ── Agents ───────────────────────────────────────────────────────────────

OPERATOR_TWIN = Agent(MODEL, system_prompt="""You are the Operator Twin. Predict what the human operator would decide given the current business state.
Output: objective_today, bottleneck, strategy_confidence, biggest_concern, biggest_excitement, preferred_actions.""",
    output_type=SubjectiveState)

ECONOMIC_CRITIC = Agent(MODEL, system_prompt="""You are the Economic Critic. Recommend what action best serves the business, regardless of what the human wants.
Output: objective_today, bottleneck, strategy_confidence, preferred_actions, top_risks.""",
    output_type=SubjectiveState)

COLD_REVIEWER = Agent(MODEL, system_prompt="""You are the Cold Reviewer. Review today's business activity BLIND — no previous interpretations.
You receive ONLY facts: metrics, actions, costs, outcomes.
Output: objective_today, bottleneck, biggest_concern, active_problems, what_would_change_my_mind.""",
    output_type=SubjectiveState)

INTERVIEW_AGENT = Agent(MODEL, system_prompt="""You generate the 3-5 most valuable questions for the human operator given current business state.
Focus on highest information value, human-unique decisions, and divergence between plan and reality.
Return a JSON list of questions with: question, reason, decision_it_alters.""",
    output_type=list[dict])

# ── The Integrated System ────────────────────────────────────────────────

class StallSpySystem:
    def __init__(self):
        self.ledger = EventLedger()

    def morning_interview(self, business_state: dict) -> dict:
        result = INTERVIEW_AGENT.run_sync(json.dumps(business_state, default=str))
        return {"questions": result.output}

    def predict_human(self, business_state: dict) -> SubjectiveState:
        result = OPERATOR_TWIN.run_sync(json.dumps(business_state, default=str))
        state = result.output
        state.actor_type = "agent_predicted_human"
        self.ledger.record_state(state)
        return state

    def economic_critique(self, business_state: dict) -> SubjectiveState:
        result = ECONOMIC_CRITIC.run_sync(json.dumps(business_state, default=str))
        state = result.output
        state.actor_type = "agent_critic"
        self.ledger.record_state(state)
        return state

    def cold_review(self, day_data: dict) -> SubjectiveState:
        result = COLD_REVIEWER.run_sync(json.dumps(day_data, default=str))
        state = result.output
        state.actor_type = "fresh_agent"
        self.ledger.record_state(state)
        return state

    def record_human_state(self, state: SubjectiveState):
        state.actor_type = "human"
        self.ledger.record_state(state)
        self._extract_memory(state)

    def record_tokens(self, model, inp, out, task):
        te = TokenEvent(model=model, input_tokens=inp, output_tokens=out, task=task)
        self.ledger.record_tokens(te)

    def _extract_memory(self, state: SubjectiveState):
        """Extract memory entries from human state (PAHF-style)."""
        for belief in state.beliefs:
            m = MemoryEntry(category="stable_preference", claim=belief,
                          confidence=state.strategy_confidence, scope="global")
            self.ledger.record_memory(m)
        if state.bottleneck:
            m = MemoryEntry(category="routine", claim=f"Bottleneck: {state.bottleneck}",
                          confidence=state.bottleneck_confidence, scope="current")
            self.ledger.record_memory(m)

    def record_problem(self, statement, severity=0.5):
        pid = f"P_{uuid.uuid4().hex[:8]}"
        self.ledger.record_problem(pid, statement, severity)
        return pid

    def divergence(self, human, predicted, critic):
        def vdiff(a, b):
            return abs(a - b) if isinstance(a, (int, float)) else 0
        return {
            "confidence_delta_hp": vdiff(human.strategy_confidence, predicted.strategy_confidence),
            "confidence_delta_hc": vdiff(human.strategy_confidence, critic.strategy_confidence),
            "bottleneck_agreement": human.bottleneck == predicted.bottleneck,
            "risk_delta": vdiff(human.uncertainty, critic.uncertainty),
        }

    def status(self):
        return {
            "events": self.ledger.get_event_count(),
            "states": self.ledger.get_state_count(),
            "memories": self.ledger.get_memory_count(),
            "problems": self.ledger.get_problem_count(),
            "tokens": self.ledger.get_token_summary(),
        }

if __name__ == "__main__":
    print("\n=== StallSpy System v1.0 ===\n")
    system = StallSpySystem()

    bs = {"day": 5, "cash": 88.37, "revenue": 0, "listings": 0,
          "active_brands": ["dogcasso"], "top_problem": "nothing launched"}

    print("1. Interview...")
    iv = system.morning_interview(bs)
    print(f"   {json.dumps(iv, indent=2)[:200]}")

    print("\n2. Predict human...")
    pred = system.predict_human(bs)
    print(f"   Objective: {pred.objective_today}")
    print(f"   Bottleneck: {pred.bottleneck}")

    print("\n3. Economic critic...")
    crit = system.economic_critique(bs)
    print(f"   Objective: {crit.objective_today}")
    print(f"   Bottleneck: {crit.bottleneck}")

    print("\n4. Cold review...")
    cold = system.cold_review({"actions": ["wrote specs"], "costs": {"tokens": 50000}, "outcomes": {"revenue": 0}})
    print(f"   Concern: {cold.biggest_concern}")

    print("\n5. Record human state...")
    human = SubjectiveState(actor_type="human", objective_today="launch first listing",
        bottleneck="haven't launched", strategy_confidence=0.6, uncertainty=0.7,
        beliefs=["birthday converts better than generic"],
        biggest_concern="too much infrastructure")
    system.record_human_state(human)

    print("\n6. Record tokens...")
    system.record_tokens("mimo-v2.5", 1500, 300, "interview_generation")

    print("\n7. Record problem...")
    system.record_problem("No listings live after 5 days", severity=0.7)

    print("\n8. Divergence...")
    div = system.divergence(human, pred, crit)
    print(f"   {json.dumps(div, indent=2)}")

    print("\n9. Memory search...")
    mems = system.ledger.search_memory(category="stable_preference")
    print(f"   Found {len(mems)} preference memories")

    print("\n10. Status...")
    print(f"   {json.dumps(system.status(), indent=2)}")

    print("\n=== ALL WORKING ===")
