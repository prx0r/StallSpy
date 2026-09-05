"""
StallShark Core Schemas — 8 schemas for V0 company operation.

CompanyDay, StateSnapshot, Perspective, Session, Decision,
Problem, Experiment, EconomicEvent.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# ── Helpers ──────────────────────────────────────────────────────────────

def uid(prefix: str = "id") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"

def sha256(data: Any) -> str:
    return hashlib.sha256(json.dumps(data, default=str, sort_keys=True).encode()).hexdigest()

def now_iso() -> str:
    return datetime.now().isoformat()

# ── 1. CompanyDay ────────────────────────────────────────────────────────

def make_company_day(day_number: int = 1, date: str = None) -> dict:
    return {
        "schema": "company_day",
        "day_id": f"day_{day_number:04d}",
        "date": date or datetime.now().strftime("%Y-%m-%d"),
        "day_number": day_number,
        "state_start_id": None,
        "state_end_id": None,
        "perspective_ids": [],
        "session_ids": [],
        "decision_ids": [],
        "problem_ids": [],
        "experiment_ids": [],
        "financial_event_ids": [],
        "public_content_ids": [],
    }

# ── 2. StateSnapshot ─────────────────────────────────────────────────────

def make_state_snapshot(
    cash_usd: float = 0,
    revenue_lifetime: float = 0,
    profit_lifetime: float = 0,
    brands: dict = None,
    active_problems: list = None,
    active_experiments: list = None,
    git_heads: dict = None,
    open_work: list = None,
) -> dict:
    return {
        "schema": "state_snapshot",
        "state_id": uid("state"),
        "as_of": now_iso(),
        "cash_usd": cash_usd,
        "revenue_lifetime": revenue_lifetime,
        "profit_lifetime": profit_lifetime,
        "brands": brands or {},
        "active_problems": active_problems or [],
        "active_experiments": active_experiments or [],
        "git_heads": git_heads or {},
        "open_work": open_work or [],
    }

# ── 3. Perspective ──────────────────────────────────────────────────────

def make_perspective(
    actor_type: str,  # human|agent|predicted_human|blind_reviewer
    state_id: str,
    objectives: dict = None,
    primary_bottleneck: str = "",
    bottleneck_confidence: float = 0.5,
    health_assessment: float = 0.5,
    momentum: float = 0.5,
    uncertainty: float = 0.5,
    top_beliefs: list = None,
    top_opportunities: list = None,
    top_risks: list = None,
    best_action: str = "",
    best_action_reason: str = "",
    best_action_confidence: float = 0.5,
    best_alternative: str = "",
    highest_value_unknown: str = "",
    resource_stance: dict = None,
    forecasts: list = None,
    what_metrics_miss: str = "",
    freeform: str = "",
) -> dict:
    return {
        "schema": "perspective",
        "perspective_id": uid("persp"),
        "state_id": state_id,
        "actor": {"type": actor_type, "id": f"{actor_type}_default"},
        "information_cutoff": now_iso(),
        "context_manifest": [],
        "objectives": objectives or {
            "next_3_hours": "",
            "today": "",
            "7_days": "",
            "30_days": "",
        },
        "health_assessment": health_assessment,
        "momentum": momentum,
        "uncertainty": uncertainty,
        "primary_bottleneck": {
            "claim": primary_bottleneck,
            "confidence": bottleneck_confidence,
        },
        "top_beliefs": top_beliefs or [],
        "top_opportunities": top_opportunities or [],
        "top_risks": top_risks or [],
        "best_action_now": {
            "action": best_action,
            "reason": best_action_reason,
            "confidence": best_action_confidence,
        },
        "best_alternative": best_alternative,
        "highest_value_unknown": highest_value_unknown,
        "resource_stance": resource_stance or {
            "cash_aggressiveness": 0.3,
            "exploration": 0.5,
            "quality_vs_speed": 0.5,
        },
        "forecasts": forecasts or [],
        "what_metrics_miss": what_metrics_miss,
        "freeform": freeform,
    }

# ── 4. Session ──────────────────────────────────────────────────────────

def make_session(
    day_id: str,
    objective: str = "",
    commit_before: str = "",
) -> dict:
    return {
        "schema": "session",
        "session_id": uid("ses"),
        "day_id": day_id,
        "started_at": now_iso(),
        "ended_at": None,
        "objective": objective,
        "repo": "StallSpy",
        "commit_before": commit_before,
        "commit_after": None,
        "raw_trace_sha256": None,
        "raw_trace_path": None,
        "human_prompt_count": 0,
        "tool_calls": 0,
        "usage": {
            "input_tokens": 0,
            "cached_tokens": 0,
            "output_tokens": 0,
            "reasoning_tokens": 0,
            "estimated_usd": 0.0,
        },
        "worker_debrief": {
            "most_important_discovery": "",
            "biggest_concern": "",
            "what_logs_do_not_reveal": "",
            "what_i_learned_about_operator": "",
            "next_action": "",
        },
    }

# ── 5. Decision ─────────────────────────────────────────────────────────

def make_decision(
    state_id: str,
    problem: str,
    options: list = None,
    human_preference: str = "",
    agent_preference: str = "",
    final_choice: str = "",
    reason: str = "",
    confidence: float = 0.5,
    budget_cash: float = 0,
    budget_human_minutes: int = 0,
    budget_agent_tokens: int = 0,
    expected_result: str = "",
) -> dict:
    return {
        "schema": "decision",
        "decision_id": uid("dec"),
        "state_id": state_id,
        "problem": problem,
        "options": options or [],
        "human_preference": human_preference,
        "agent_preference": agent_preference,
        "final_choice": final_choice,
        "reason": reason,
        "confidence": confidence,
        "budget": {
            "cash_usd": budget_cash,
            "human_minutes": budget_human_minutes,
            "agent_tokens": budget_agent_tokens,
        },
        "expected_result": expected_result,
        "outcome_ids": [],
    }

# ── 6. Problem ──────────────────────────────────────────────────────────

def make_problem(
    statement: str,
    severity: float = 0.5,
    evidence: list = None,
    candidate_causes: list = None,
) -> dict:
    return {
        "schema": "problem",
        "problem_id": uid("prob"),
        "detected_at": now_iso(),
        "statement": statement,
        "evidence": evidence or [],
        "severity": severity,
        "candidate_causes": candidate_causes or [],
        "status": "open",
        "related_experiments": [],
    }

# ── 7. Experiment ───────────────────────────────────────────────────────

def make_experiment(
    problem_id: str,
    hypothesis: str,
    intervention: str,
    primary_metric: str = "conversion_rate",
    baseline: float = 0.0,
    prediction_human: float = 0.0,
    prediction_agent: float = 0.0,
    cash_budget: float = 0,
    token_budget: int = 0,
    success_condition: str = "",
) -> dict:
    return {
        "schema": "experiment",
        "experiment_id": uid("exp"),
        "problem_id": problem_id,
        "hypothesis": hypothesis,
        "intervention": intervention,
        "primary_metric": primary_metric,
        "baseline": baseline,
        "prediction": {
            "human": prediction_human,
            "agent": prediction_agent,
        },
        "start_at": now_iso(),
        "resolution_at": None,
        "cash_budget": cash_budget,
        "token_budget": token_budget,
        "success_condition": success_condition,
        "result": None,
    }

# ── 8. EconomicEvent ────────────────────────────────────────────────────

def make_economic_event(
    event_type: str,  # revenue|etsy_fee|ad|model|gpu|pod|domain|software|refund
    cash_usd: float,
    brand_id: str = "",
    tokens: int = 0,
    human_minutes: float = 0,
    session_id: str = "",
    experiment_id: str = "",
) -> dict:
    return {
        "schema": "economic_event",
        "event_id": uid("econ"),
        "occurred_at": now_iso(),
        "type": event_type,
        "brand_id": brand_id,
        "cash_usd": cash_usd,
        "tokens": tokens,
        "human_minutes": human_minutes,
        "session_id": session_id,
        "experiment_id": experiment_id,
    }

# ── Persistence ──────────────────────────────────────────────────────────

DATA_ROOT = Path("/root/StallSpy/dogcasso-ops")

def save(schema: dict, category: str):
    os.makedirs(DATA_ROOT / category, exist_ok=True)
    rid = schema.get(f"{schema['schema'].replace(' ', '_')}_id",
                     schema.get("id", uid("rec")))
    path = DATA_ROOT / category / f"{rid}.json"
    with open(path, "w") as f:
        json.dump(schema, f, indent=2, default=str)
    return path

def load(category: str, record_id: str) -> dict:
    path = DATA_ROOT / category / f"{record_id}.json"
    with open(path) as f:
        return json.load(f)

def list_all(category: str) -> list:
    base = DATA_ROOT / category
    if not base.exists():
        return []
    return [f.stem for f in base.glob("*.json")]


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== StallShark 8 Schemas Test ===\n")
    
    # 1. CompanyDay
    cd = make_company_day(1, "2026-09-06")
    print(f"1. CompanyDay: {cd['day_id']}")
    
    # 2. StateSnapshot
    state = make_state_snapshot(
        cash_usd=88.37, brands={"dogcasso": {"listings": 0, "orders": 0}}
    )
    print(f"2. StateSnapshot: {state['state_id']}")
    
    # 3. Perspectives
    human_p = make_perspective("human", state["state_id"],
        objectives={"today": "launch first listing"},
        primary_bottleneck="no listings live", bottleneck_confidence=0.8,
        health_assessment=0.4, uncertainty=0.7)
    agent_p = make_perspective("agent", state["state_id"],
        objectives={"today": "ship first product"},
        primary_bottleneck="analysis paralysis", bottleneck_confidence=0.9)
    predicted_p = make_perspective("predicted_human", state["state_id"],
        objectives={"today": "launch listing"},
        primary_bottleneck="havent launched", bottleneck_confidence=0.7)
    blind_p = make_perspective("blind_reviewer", state["state_id"],
        objectives={"today": "identify progress"},
        primary_bottleneck="zero revenue", bottleneck_confidence=0.85)
    print(f"3. Perspectives: {len([human_p, agent_p, predicted_p, blind_p])} created")
    
    # 4. Session
    sess = make_session(cd["day_id"], objective="Build corpus + schemas")
    print(f"4. Session: {sess['session_id']}")
    
    # 5. Decision
    dec = make_decision(
        state_id=state["state_id"],
        problem="Endgame architecture eating the experiment",
        options=["continue building schemas", "ship a product"],
        human_preference="ship a product",
        agent_preference="continue building schemas",
        final_choice="ship a product",
        reason="Revenue matters more than frameworks",
        confidence=0.8,
        budget_cash=5.0,
        budget_human_minutes=120,
        budget_agent_tokens=500000,
    )
    print(f"5. Decision: {dec['decision_id']}")
    
    # 6. Problem
    prob = make_problem(
        statement="Zero revenue after 5 days of development",
        severity=0.95,
        candidate_causes=[
            {"claim": "no listings exist", "confidence": 0.9},
            {"claim": "no product renders completed", "confidence": 0.7},
        ],
    )
    print(f"6. Problem: {prob['problem_id']}")
    
    # 7. Experiment
    exp = make_experiment(
        problem_id=prob["problem_id"],
        hypothesis="Listing with before/after proof increases conversion",
        intervention="Replace gallery image 2 with before/after",
        prediction_human=0.032,
        prediction_agent=0.028,
        success_condition=">=20% relative conversion increase",
    )
    print(f"7. Experiment: {exp['experiment_id']}")
    
    # 8. EconomicEvent
    econ = make_economic_event(
        event_type="model",
        cash_usd=-3.21,
        tokens=721992,
        human_minutes=0,
        session_id=sess["session_id"],
    )
    print(f"8. EconomicEvent: {econ['event_id']}")
    
    # Save all
    for s, cat in [(cd, "days"), (state, "states"), (human_p, "perspectives"),
                    (agent_p, "perspectives"), (predicted_p, "perspectives"),
                    (blind_p, "perspectives"), (sess, "sessions"),
                    (dec, "decisions"), (prob, "problems"),
                    (exp, "experiments"), (econ, "economic_events")]:
        path = save(s, cat)
    
    print(f"\nAll saved to dogcasso-ops/")
    print(f"Days: {len(list_all('days'))}")
    print(f"States: {len(list_all('states'))}")
    print(f"Perspectives: {len(list_all('perspectives'))}")
    print(f"Sessions: {len(list_all('sessions'))}")
    print(f"Decisions: {len(list_all('decisions'))}")
    print(f"Problems: {len(list_all('problems'))}")
    print(f"Experiments: {len(list_all('experiments'))}")
    print(f"Economic events: {len(list_all('economic_events'))}")
    
    print("\n=== ALL 8 SCHEMAS WORKING ===")
