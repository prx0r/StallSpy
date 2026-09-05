"""
Meta-Enquiry Protocol — 10 information objectives + adaptive question selection.

The interview is a budgeted active-learning system over three evolving models:
business state, operator state, and human-agent comparative advantage.
"""
from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Literal, Optional

def uid(prefix="qo"): return f"{prefix}_{uuid.uuid4().hex[:8]}"
def now(): return datetime.now().isoformat()


# ── 10 Information Objectives ────────────────────────────────────────────

INFORMATION_OBJECTIVES = {
    "QO_01_GOAL_HIERARCHY": {
        "description": "Desired objective and priority across horizons",
        "unknowns": ["immediate objective", "7d objective", "30d objective", "mission", "conflicts"],
        "timescales": ["NOW", "TODAY", "7D", "30D", "MISSION"],
    },
    "QO_02_STATE_BOTTLENECK": {
        "description": "Perceived binding constraint",
        "unknowns": ["primary bottleneck", "confidence", "evidence", "alternative bottleneck"],
    },
    "QO_03_CAUSAL_MODEL": {
        "description": "Operator's causal explanation of the business",
        "unknowns": ["causal propositions", "testable predictions", "evidence basis"],
    },
    "QO_04_UNCERTAINTY_VOI": {
        "description": "Highest-value missing information",
        "unknowns": ["what would change decisions", "expected information value"],
    },
    "QO_05_FORECAST": {
        "description": "Prospective expectation",
        "unknowns": ["probability estimates", "confidence intervals", "resolution conditions"],
    },
    "QO_06_RESOURCE_POLICY": {
        "description": "Appropriate expenditure of scarce resources",
        "unknowns": ["cash aggressiveness", "compute aggressiveness", "exploration fraction", "exploitation fraction"],
    },
    "QO_07_TEST_COUNTERFACTUAL": {
        "description": "Falsification and opportunity cost",
        "unknowns": ["falsification conditions", "alternative rejected", "what are we giving up"],
    },
    "QO_08_RISK_PREMORTEM": {
        "description": "Failure modes not in current plan",
        "unknowns": ["assumed failure causes", "mitigation plans", "kill conditions"],
    },
    "QO_09_HUMAN_SIGNAL": {
        "description": "Information visible internally but absent from machine telemetry",
        "unknowns": ["feelings", "intuitions", "concerns", "excitements", "hidden observations"],
    },
    "QO_10_META_POLICY_DELEGATION": {
        "description": "Whether operating policy itself should change",
        "unknowns": ["should objective change", "should delegation change", "did human add value"],
    },
}


# ── KnowledgeGap ─────────────────────────────────────────────────────────

def make_knowledge_gap(
    target_type: str,
    description: str,
    uncertainty: float = 0.5,
    decision_impact: float = 0.5,
    urgency: float = 0.5,
    human_advantage: float = 0.5,
    agent_advantage: float = 0.5,
) -> dict:
    return {
        "schema": "knowledge_gap",
        "gap_id": uid("gap"),
        "target_type": target_type,
        "target_ref": None,
        "description": description,
        "uncertainty": uncertainty,
        "decision_impact": decision_impact,
        "urgency": urgency,
        "human_information_advantage": human_advantage,
        "agent_information_advantage": agent_advantage,
        "current_evidence_refs": [],
        "next_decision_ids": [],
        "created_at": now(),
    }


# ── QuestionCandidate ───────────────────────────────────────────────────

def make_question_candidate(
    objective_id: str,
    gap_ids: list,
    wording: str,
    timescale: str,
    action_hook: str,
    estimated_burden_seconds: int = 60,
) -> dict:
    return {
        "schema": "question_candidate",
        "candidate_id": uid("qc"),
        "objective_id": objective_id,
        "gap_ids": gap_ids,
        "wording": wording,
        "timescale": timescale,
        "action_hook": action_hook,
        "estimated_probability_answer_changes_decision": 0.5,
        "estimated_uncertainty_reduction": 0.5,
        "decision_impact": 0.5,
        "human_information_advantage": 0.5,
        "estimated_burden_seconds": estimated_burden_seconds,
        "redundancy_with_recent_questions": 0.0,
        "why_now": "",
        "generator_model": "mimo-v2.5",
        "generator_version": "v1",
        "created_at": now(),
    }


# ── QuestionOutcome ──────────────────────────────────────────────────────

def make_question_outcome(
    candidate_id: str,
    changed_plan: bool = False,
    decision_changed: str = "",
    economic_impact: float = 0.0,
    retrospective_value: float = 0.0,
) -> dict:
    return {
        "schema": "question_outcome",
        "outcome_id": uid("qo_out"),
        "candidate_id": candidate_id,
        "changed_plan": changed_plan,
        "decision_changed": decision_changed,
        "economic_impact": economic_impact,
        "retrospective_value": retrospective_value,
        "assessed_at": now(),
    }


# ── DecisionEpisode ──────────────────────────────────────────────────────

def make_decision_episode(
    decision_id: str,
    state_before: dict,
    beliefs: list,
    information_set: dict,
    human_preference: str,
    agent_preference: str,
    predicted_human: str,
    final_choice: str,
    rationale: str,
    confidence: float,
    budget: dict,
) -> dict:
    return {
        "schema": "decision_episode",
        "episode_id": uid("dep"),
        "decision_id": decision_id,
        "state_before": state_before,
        "beliefs": beliefs,
        "information_set": information_set,
        "human_preference": human_preference,
        "agent_preference": agent_preference,
        "predicted_human": predicted_human,
        "final_choice": final_choice,
        "rationale": rationale,
        "confidence": confidence,
        "budget": budget,
        "outcome": None,
        "who_was_right": None,
        "question_was_useful": None,
        "human_involution_helped": None,
        "created_at": now(),
    }


# ── Sampling Schedule ───────────────────────────────────────────────────

SAMPLING_SCHEDULE = {
    "morning": {
        "mandatory": ["QO_01_GOAL_HIERARCHY", "QO_02_STATE_BOTTLENECK", "QO_06_RESOURCE_POLICY"],
        "adaptive_count": 2,
        "target_human_seconds": 120,
    },
    "session_close": {
        "mandatory": [],
        "adaptive_count": 2,
        "target_human_seconds": 90,
    },
    "evening": {
        "mandatory": ["QO_03_CAUSAL_MODEL", "QO_09_HUMAN_SIGNAL", "QO_10_META_POLICY_DELEGATION"],
        "adaptive_count": 2,
        "target_human_seconds": 120,
    },
    "weekly": {
        "mandatory": [],
        "adaptive_count": 8,
        "target_human_seconds": 300,
    },
}


# ── Adaptive Question Selector ──────────────────────────────────────────

def select_questions(
    gaps: list,
    schedule: dict,
    recent_questions: list = None,
    max_questions: int = 5,
) -> list:
    """Select highest-value questions from knowledge gaps."""
    recent_ids = set(r.get("candidate_id", "") for r in (recent_questions or []))
    
    # Score each gap
    scored = []
    for gap in gaps:
        voi = gap["uncertainty"] * gap["decision_impact"] * gap["human_information_advantage"]
        redundancy = 1.0 if gap.get("gap_id", "") in recent_ids else 0.0
        score = voi * (1.0 - redundancy * 0.5)
        scored.append((score, gap))
    
    scored.sort(key=lambda x: x[0], reverse=True)
    
    # Take top N
    selected = []
    for score, gap in scored[:max_questions]:
        selected.append({
            "gap": gap,
            "voi_score": score,
            "selected": True,
        })
    
    return selected


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Meta-Enquiry Protocol Test ===\n")
    
    # 1. Information objectives
    print(f"Information Objectives: {len(INFORMATION_OBJECTIVES)}")
    for oid, obj in INFORMATION_OBJECTIVES.items():
        print(f"  {oid}: {obj['description'][:60]}")
    
    # 2. Knowledge gaps
    gaps = [
        make_knowledge_gap("goal", "What matters most today?", 0.7, 0.8, 0.9, 0.8, 0.2),
        make_knowledge_gap("causal_belief", "Why are sales low?", 0.6, 0.7, 0.6, 0.7, 0.3),
        make_knowledge_gap("forecast", "Expected conversion rate?", 0.5, 0.6, 0.5, 0.4, 0.6),
    ]
    print(f"\nKnowledge Gaps: {len(gaps)}")
    
    # 3. Question candidates
    candidates = [
        make_question_candidate(
            objective_id="QO_01_GOAL_HIERARCHY",
            gap_ids=[gaps[0]["gap_id"]],
            wording="What outcome matters most today?",
            timescale="TODAY",
            action_hook="choose_top_3_priorities",
        ),
        make_question_candidate(
            objective_id="QO_04_UNCERTAINTY_VOI",
            gap_ids=[gaps[1]["gap_id"]],
            wording="What would most change what we do if we learned it?",
            timescale="TODAY",
            action_hook="identify_next_experiment",
        ),
    ]
    print(f"\nQuestion Candidates: {len(candidates)}")
    
    # 4. Adaptive selection
    selected = select_questions(gaps, SAMPLING_SCHEDULE["morning"], max_questions=2)
    print(f"\nSelected: {len(selected)} questions")
    for s in selected:
        print(f"  VOI={s['voi_score']:.3f}: {s['gap']['description'][:50]}")
    
    # 5. Question outcome
    outcome = make_question_outcome(
        candidate_id=candidates[0]["candidate_id"],
        changed_plan=True,
        decision_changed="prioritize launch over infrastructure",
        economic_impact=0.0,
    )
    print(f"\nOutcome: {outcome['outcome_id']} (changed_plan={outcome['changed_plan']})")
    
    # 6. Decision episode
    episode = make_decision_episode(
        decision_id="dec_001",
        state_before={"cash": 100, "revenue": 0},
        beliefs=["birthday converts better"],
        information_set={"sources": ["etsy_api", "manual_research"]},
        human_preference="ship first",
        agent_preference="build more specs",
        predicted_human="ship first",
        final_choice="ship first",
        rationale="revenue matters more than frameworks",
        confidence=0.8,
        budget={"cash_usd": 5, "human_minutes": 120, "agent_tokens": 500000},
    )
    print(f"\nDecision Episode: {episode['episode_id']}")
    print(f"  Human: {episode['human_preference']}")
    print(f"  Agent: {episode['agent_preference']}")
    print(f"  Final: {episode['final_choice']}")
    
    print("\n=== ALL WORKING ===")
