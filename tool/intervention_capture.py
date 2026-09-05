"""
Intervention Capture — HumanIntervention + PPL horizon transform.

Every human override of agent behavior is a training signal.
PPL teaches us that interventions contain information about future trajectories.
"""
from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

def uid(prefix="intv"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def now_iso():
    return datetime.now().isoformat()


# ── HumanIntervention ────────────────────────────────────────────────────

def make_human_intervention(
    agent_intended_action: str,
    human_override: str,
    reason: str,
    session_id: str = "",
    decision_id: str = "",
    agent_prediction_of_why: str = "",
) -> dict:
    """Every time human overrides agent — it's a training signal."""
    return {
        "schema": "human_intervention",
        "intervention_id": uid("intv"),
        "timestamp": now_iso(),
        "agent_intended_action": agent_intended_action,
        "human_override": human_override,
        "reason": reason,
        "agent_prediction_of_why": agent_prediction_of_why,
        "session_id": session_id,
        "decision_id": decision_id,
        "downstream_outcome_ids": [],
    }


# ── PPL Horizon Transform ───────────────────────────────────────────────

def make_ppl_horizon(
    intervention_id: str,
    implied_trajectory_concern: str,
    preference_horizon: str,  # "until_first_sale", "until_q4", "until_validation"
    inferred_temporary_policy: str,
    confidence: float = 0.5,
) -> dict:
    """PPL: interventions contain info about future trajectories to prevent."""
    return {
        "schema": "ppl_horizon",
        "horizon_id": uid("horizon"),
        "intervention_id": intervention_id,
        "implied_trajectory_concern": implied_trajectory_concern,
        "preference_horizon": preference_horizon,
        "inferred_temporary_policy": inferred_temporary_policy,
        "confidence": confidence,
        "created_at": now_iso(),
    }


# ── Human Value Estimate ────────────────────────────────────────────────

def make_human_value_estimate(
    task_class: str,
    expected_outcome_with_human: float,
    expected_outcome_without_human: float,
    expected_human_minutes: int,
    expected_delay_minutes: int,
    expected_economic_difference: float,
) -> dict:
    """Marginal human value = E[outcome|human] - E[outcome|no_human] - interruption_cost."""
    marginal_value = expected_outcome_with_human - expected_outcome_without_human - (expected_delay_minutes * 0.01)  # $0.01/min opportunity cost
    
    return {
        "schema": "human_value_estimate",
        "estimate_id": uid("hve"),
        "task_class": task_class,
        "expected_outcome_with_human": expected_outcome_with_human,
        "expected_outcome_without_human": expected_outcome_without_human,
        "expected_human_minutes": expected_human_minutes,
        "expected_delay_minutes": expected_delay_minutes,
        "expected_economic_difference": expected_economic_difference,
        "marginal_human_value_usd": marginal_value,
        "created_at": now_iso(),
    }


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Intervention Capture Test ===\n")
    
    # 1. Human intervention
    intv = make_human_intervention(
        agent_intended_action="publish listing with default thumbnail",
        human_override="use before/after proof image instead",
        reason="Face legibility stronger at thumbnail size",
        agent_prediction_of_why="agent predicted human would want speed over quality",
    )
    print(f"Intervention: {intv['intervention_id']}")
    print(f"  Agent wanted: {intv['agent_intended_action'][:50]}")
    print(f"  Human chose: {intv['human_override'][:50]}")
    print(f"  Reason: {intv['reason']}")
    
    # 2. PPL horizon
    horizon = make_ppl_horizon(
        intervention_id=intv["intervention_id"],
        implied_trajectory_concern="continued infrastructure work will delay market validation",
        preference_horizon="until_first_sale",
        inferred_temporary_policy="prioritize launch-blocking work over optional capability development",
    )
    print(f"\nPPL Horizon: {horizon['horizon_id']}")
    print(f"  Concern: {horizon['implied_trajectory_concern']}")
    print(f"  Policy: {horizon['inferred_temporary_policy']}")
    
    # 3. Human value estimate
    hve = make_human_value_estimate(
        task_class="thumbnail_selection",
        expected_outcome_with_human=0.042,
        expected_outcome_without_human=0.031,
        expected_human_minutes=12,
        expected_delay_minutes=5,
        expected_economic_difference=0.011,
    )
    print(f"\nHuman Value: ${hve['marginal_human_value_usd']:.3f}")
    print(f"  Task: {hve['task_class']}")
    print(f"  With human: {hve['expected_outcome_with_human']}")
    print(f"  Without: {hve['expected_outcome_without_human']}")
    
    print("\n=== ALL WORKING ===")
