"""
StallShark Integration — wires all components into a single daily pipeline.

CompanyDay → State → Perspectives (P/A/H) → Decision → Budget →
Session → Trajectory → Economics → ColdReview → PublicDigest

Components:
- stallshark_schemas (8 core schemas)
- meta_enquiry (10 QOs, KnowledgeGaps, QuestionCandidates)
- budget_stack (BATS, SpendGuard)
- trajectory_ir (steps, labels, debrief)
- intervention_capture (PPL, human value)
- memory_taxonomy (4 banks)
- capability_experiment (upstream registry)
- problem_registry (problems)
- storage (artifact store + R2)
- verify (completeness check)
"""
from __future__ import annotations

import json
import os
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# Add tool dir to path
sys.path.insert(0, str(Path(__file__).parent))

from stallshark_schemas import (
    make_company_day, make_state_snapshot, make_perspective,
    make_session, make_decision, make_problem, make_experiment,
    make_economic_event, uid, now_iso, sha256,
)
from meta_enquiry import (
    INFORMATION_OBJECTIVES, make_knowledge_gap, make_question_candidate,
    make_question_outcome, make_decision_episode, SAMPLING_SCHEDULE,
    select_questions,
)
from budget_stack import make_budget_envelope, SpendGuard, BATSTracker, record_spend
from trajectory_ir import make_trajectory, add_step, finish_trajectory, make_worker_debrief
from intervention_capture import make_human_intervention, make_ppl_horizon, make_human_value_estimate
from memory_taxonomy import make_memory, MemoryBank
from capability_experiment import make_capability_experiment
from problem_registry import add_problem, list_problems

ROOT = Path("/root/StallShark")
DATA_DIR = ROOT / "mythicbee-ops"


# ── CompanyDay Runner ────────────────────────────────────────────────────

class CompanyDayRunner:
    """Runs a complete CompanyDay through the full pipeline."""
    
    def __init__(self, day_number: int, date: str = None):
        self.day_number = day_number
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.day_id = f"day_{day_number:04d}"
        self.results = {}
        
        # Create CompanyDay
        self.company_day = make_company_day(day_number, self.date)
        
        # Budget
        self.budget = make_budget_envelope(cash_usd=5.0, tokens=500000)
        self.guard = SpendGuard(self.budget)
        self.bats = BATSTracker(daily_cash=5.0, daily_tokens=500000)
        
        # State
        self.state = None
        self.perspectives = []
        self.decisions = []
        self.problems = []
        self.experiments = []
        self.economic_events = []
        self.trajectories = []
        self.memories = []
    
    def freeze_state(self, business_state: dict) -> dict:
        """Step 0: Freeze current state."""
        self.state = make_state_snapshot(
            cash_usd=business_state.get("cash", 0),
            revenue_lifetime=business_state.get("revenue", 0),
            brands={b: {"listings": 0, "orders": 0} for b in business_state.get("brands", [])},
        )
        self.company_day["state_start_id"] = self.state["state_id"]
        return self.state
    
    def morning_interview(self, business_state: dict) -> dict:
        """Step 1-4: Generate perspectives (P/A/H)."""
        # Human perspective
        human_p = make_perspective(
            "human", self.state["state_id"],
            objectives={"today": business_state.get("goal", "")},
            primary_bottleneck=business_state.get("bottleneck", ""),
            bottleneck_confidence=business_state.get("confidence", 0.5),
            health_assessment=0.5,
            uncertainty=business_state.get("uncertainty", 0.5),
        )
        self.perspectives.append(human_p)
        
        # Agent predicted human
        predicted = make_perspective(
            "agent_predicted_human", self.state["state_id"],
            objectives={"today": "ship first product"},
            primary_bottleneck="analysis paralysis",
            bottleneck_confidence=0.7,
        )
        self.perspectives.append(predicted)
        
        # Independent agent
        agent = make_perspective(
            "agent", self.state["state_id"],
            objectives={"today": "validate concept"},
            primary_bottleneck="no market data",
            bottleneck_confidence=0.6,
        )
        self.perspectives.append(agent)
        
        # Cold reviewer
        cold = make_perspective(
            "blind_reviewer", self.state["state_id"],
            objectives={"today": "identify progress"},
            primary_bottleneck="zero revenue",
            bottleneck_confidence=0.85,
        )
        self.perspectives.append(cold)
        
        self.company_day["perspective_ids"] = [p["perspective_id"] for p in self.perspectives]
        return {"human": human_p, "predicted": predicted, "agent": agent, "cold": cold}
    
    def divergence(self, human: dict, predicted: dict, agent: dict) -> dict:
        """Step 5: Compute divergence between perspectives."""
        def vdiff(a, b):
            return abs(a - b) if isinstance(a, (int, float)) else 0
        
        return {
            "human_vs_predicted_confidence": vdiff(
                human.get("strategy_confidence", 0.5),
                predicted.get("strategy_confidence", 0.5)
            ),
            "human_vs_agent_confidence": vdiff(
                human.get("strategy_confidence", 0.5),
                agent.get("strategy_confidence", 0.5)
            ),
            "bottleneck_agreement": human.get("primary_bottleneck", {}).get("claim", "") == predicted.get("primary_bottleneck", {}).get("claim", ""),
        }
    
    def record_decision(self, problem: str, choice: str, reason: str, confidence: float = 0.7) -> dict:
        """Step 6: Record a decision."""
        dec = make_decision(
            state_id=self.state["state_id"],
            problem=problem,
            final_choice=choice,
            reason=reason,
            confidence=confidence,
            budget_cash=2.0,
            budget_human_minutes=60,
            budget_agent_tokens=200000,
        )
        self.decisions.append(dec)
        self.company_day["decision_ids"].append(dec["decision_id"])
        return dec
    
    def record_economic_event(self, event_type: str, cash_usd: float, brand_id: str = "") -> dict:
        """Step 7: Record economic event."""
        econ = make_economic_event(event_type, cash_usd, brand_id)
        self.economic_events.append(econ)
        self.company_day["financial_event_ids"].append(econ["event_id"])
        return econ
    
    def close_day(self) -> dict:
        """Close the CompanyDay."""
        self.company_day["state_end_id"] = self.state["state_id"] if self.state else None
        self.company_day["closed_at"] = now_iso()
        return self.company_day


# ── Storage Integration ──────────────────────────────────────────────────

def save_company_day(company_day: dict, perspectives: list, decisions: list,
                     economic_events: list) -> dict:
    """Save everything to the filesystem."""
    day_id = company_day["day_id"]
    day_dir = DATA_DIR / "days"
    day_dir.mkdir(parents=True, exist_ok=True)
    
    # Save CompanyDay
    with open(day_dir / f"{day_id}.json", "w") as f:
        json.dump(company_day, f, indent=2, default=str)
    
    # Save perspectives
    persp_dir = DATA_DIR / "perspectives"
    persp_dir.mkdir(parents=True, exist_ok=True)
    for p in perspectives:
        with open(persp_dir / f"{p['perspective_id']}.json", "w") as f:
            json.dump(p, f, indent=2, default=str)
    
    # Save decisions
    dec_dir = DATA_DIR / "decisions"
    dec_dir.mkdir(parents=True, exist_ok=True)
    for d in decisions:
        with open(dec_dir / f"{d['decision_id']}.json", "w") as f:
            json.dump(d, f, indent=2, default=str)
    
    # Save economic events
    econ_dir = DATA_DIR / "economic_events"
    econ_dir.mkdir(parents=True, exist_ok=True)
    for e in economic_events:
        with open(econ_dir / f"{e['event_id']}.json", "w") as f:
            json.dump(e, f, indent=2, default=str)
    
    return {"day_id": day_id, "saved": True}


# ── Full Pipeline Test ──────────────────────────────────────────────────

def run_full_pipeline():
    """Run complete CompanyDay pipeline with real data."""
    print("=" * 60)
    print("STALLSHARK FULL INTEGRATION TEST")
    print("=" * 60)
    
    # 1. Freeze state
    print("\n1. Freezing state...")
    runner = CompanyDayRunner(1, "2026-09-06")
    state = runner.freeze_state({
        "cash": 88.37,
        "revenue": 0,
        "brands": ["mythicbee"],
        "goal": "get first listing live",
        "bottleneck": "havent launched anything",
        "confidence": 0.6,
        "uncertainty": 0.7,
    })
    print(f"   State: {state['state_id']}")
    
    # 2. Morning interview
    print("\n2. Morning interview (P/A/H)...")
    perspectives = runner.morning_interview({
        "goal": "get first listing live",
        "bottleneck": "havent launched anything",
        "confidence": 0.6,
        "uncertainty": 0.7,
    })
    print(f"   Human: {perspectives['human'].get('objective_today', '')}")
    print(f"   Predicted: {perspectives['predicted'].get('objective_today', '')}")
    print(f"   Agent: {perspectives['agent'].get('objective_today', '')}")
    print(f"   Cold: {perspectives['cold'].get('objective_today', '')}")
    
    # 3. Divergence
    print("\n3. Divergence...")
    div = runner.divergence(
        perspectives["human"],
        perspectives["predicted"],
        perspectives["agent"],
    )
    print(f"   Human vs predicted confidence: {div['human_vs_predicted_confidence']:.2f}")
    print(f"   Bottleneck agreement: {div['bottleneck_agreement']}")
    
    # 4. Decision
    print("\n4. Recording decision...")
    dec = runner.record_decision(
        problem="zero revenue after 5 days",
        choice="ship first listing",
        reason="revenue matters more than frameworks",
        confidence=0.8,
    )
    print(f"   Decision: {dec['decision_id']}")
    
    # 5. Economic events
    print("\n5. Recording economic events...")
    e1 = runner.record_economic_event("model", -3.21, "mythicbee")
    e2 = runner.record_economic_event("etsy_fee", 0.0, "mythicbee")
    print(f"   Events: {len(runner.economic_events)}")
    
    # 6. Close day
    print("\n6. Closing day...")
    company_day = runner.close_day()
    
    # 7. Save everything
    print("\n7. Saving to filesystem...")
    saved = save_company_day(
        company_day,
        runner.perspectives,
        runner.decisions,
        runner.economic_events,
    )
    print(f"   Saved: {saved}")
    
    # 8. Verify
    print("\n8. Running verification...")
    from verify import verify_day
    verify_day(company_day["day_id"])
    
    print("\n" + "=" * 60)
    print("FULL INTEGRATION TEST COMPLETE")
    print("=" * 60)
    
    return company_day


if __name__ == "__main__":
    run_full_pipeline()
