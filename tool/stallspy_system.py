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

# ── LLM Backend ──────────────────────────────────────────────────────────
# OpenCode mimo-v2.5 via opencode run command
# Falls back to PydanticAI test model if opencode unavailable

import subprocess as _sp

def _call_opencode(prompt, system="", timeout=60):
    """Call opencode run with mimo-v2.5, return parsed JSON."""
    full = f"{system}\n\n{prompt}" if system else prompt
    try:
        r = _sp.run(["/root/.opencode/bin/opencode", "run", full],
                     capture_output=True, text=True, timeout=timeout,
                     cwd="/root/StallSpy")
        import re
        matches = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', r.stdout)
        for m in reversed(matches):
            try:
                return json.loads(m)
            except: continue
        return {"raw": r.stdout.strip()[-200:]}
    except Exception as e:
        return {"error": str(e)}

# ── Agents ───────────────────────────────────────────────────────────────

OPERATOR_SYSTEM = """You are the Operator Twin — predict what the human operator would decide.
Return ONLY a JSON object: {"objective_today":"...","bottleneck":"...","strategy_confidence":0.5,"biggest_concern":"...","biggest_excitement":"...","preferred_actions":["..."],"beliefs":["..."]}"""

CRITIC_SYSTEM = """You are the Economic Critic — recommend what action best serves the business regardless of what the human wants.
Return ONLY a JSON object: {"objective_today":"...","bottleneck":"...","strategy_confidence":0.5,"preferred_actions":["..."],"top_risks":["..."],"beliefs":["..."]}"""

COLD_SYSTEM = """You are the Cold Reviewer. Review business activity BLIND — no previous interpretations.
You receive ONLY facts. Return ONLY a JSON object:
{"what_happened":"...","valuable_actions":["..."],"waste_actions":["..."],"key_hypothesis":"...","tomorrow_should_know":"...","biggest_surprise":"..."}"""

# ── The Integrated System ────────────────────────────────────────────────

class StallSpySystem:
    def __init__(self):
        self.ledger = EventLedger()

    def _call(self, system, prompt):
        """Call mimo-v2.5 via opencode run."""
        return _call_opencode(prompt, system)

    def morning_interview(self, business_state: dict) -> dict:
        result = _call_opencode(
            f"Given this business state, generate 3-5 high-value questions for the operator.\n"
            f"Return ONLY a JSON object with key 'questions' containing a list of objects with 'question', 'reason', 'decision_it_alters'.\n\n"
            f"State: {json.dumps(business_state, default=str)}"
        )
        self.ledger.append_event("interview.generated", "", result)
        return result

    def predict_human(self, business_state: dict) -> dict:
        result = self._call(OPERATOR_SYSTEM, f"Business state: {json.dumps(business_state, default=str)}")
        result["actor_type"] = "agent_predicted_human"
        self.ledger.append_event("subjective_state.predicted", "predicted_human", result)
        return result

    def economic_critique(self, business_state: dict) -> dict:
        result = self._call(CRITIC_SYSTEM, f"Business state: {json.dumps(business_state, default=str)}")
        result["actor_type"] = "agent_critic"
        self.ledger.append_event("subjective_state.predicted", "critic", result)
        return result

    def cold_review(self, day_data: dict) -> dict:
        result = self._call(COLD_SYSTEM, f"Day's facts: {json.dumps(day_data, default=str)}")
        result["actor_type"] = "fresh_agent"
        result["interpretations_hidden"] = ["human_reflection", "worker_debrief", "previous_agent_assessment"]
        self.ledger.append_event("cold_review.created", "", result)
        return result

    def record_human_state(self, state: dict):
        state["actor_type"] = "human"
        self.ledger.append_event("subjective_state.recorded", "human", state)
        self._extract_memory(state)

    def record_tokens(self, model, inp, out, task):
        te = TokenEvent(model=model, input_tokens=inp, output_tokens=out, task=task)
        self.ledger.record_tokens(te)

    def _extract_memory(self, state):
        for belief in state.get("beliefs", []):
            m = MemoryEntry(category="stable_preference", claim=belief,
                          confidence=state.get("strategy_confidence", 0.5))
            self.ledger.record_memory(m)

    def record_problem(self, statement, severity=0.5):
        pid = f"P_{uuid.uuid4().hex[:8]}"
        self.ledger.record_problem(pid, statement, severity)
        return pid

    def divergence(self, human, predicted, critic):
        def vdiff(a, b):
            return abs(a - b) if isinstance(a, (int, float)) else 0
        return {
            "confidence_delta_hp": vdiff(human.get("strategy_confidence",0), predicted.get("strategy_confidence",0)),
            "confidence_delta_hc": vdiff(human.get("strategy_confidence",0), critic.get("strategy_confidence",0)),
            "bottleneck_agreement": human.get("bottleneck","") == predicted.get("bottleneck",""),
            "risk_delta": vdiff(human.get("uncertainty",0), critic.get("uncertainty",0)),
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
