"""
Trajectory IR — OpenCode session → structured trajectory.

Every coding session becomes a machine-readable trajectory.
Raw transcript always preserved. Structured extraction layered on top.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

def uid(prefix="traj"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def now_iso():
    return datetime.now().isoformat()

def git_head():
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, cwd="/root/StallShark")
        return r.stdout.strip()
    except:
        return "unknown"


# ── Trajectory IR ────────────────────────────────────────────────────────

def make_trajectory(
    session_id: str = "",
    day_id: str = "",
    objective: str = "",
) -> dict:
    return {
        "schema": "trajectory",
        "trajectory_id": uid("traj"),
        "session_id": session_id,
        "day_id": day_id,
        "started_at": now_iso(),
        "ended_at": None,
        "objective": objective,
        "repo": "StallShark",
        "commit_start": git_head(),
        "commit_end": None,
        "steps": [],
        "decisions": [],
        "artifacts_created": [],
        "artifacts_changed": [],
        "cost": {
            "input_tokens": 0,
            "output_tokens": 0,
            "cached_tokens": 0,
            "reasoning_tokens": 0,
            "estimated_usd": 0.0,
            "tool_calls": 0,
            "human_prompts": 0,
        },
        "result": {
            "status": "in_progress",
            "summary": "",
        },
    }


def add_step(trajectory: dict, step_type: str, description: str,
             label: str = "neutral", cost_usd: float = 0.0) -> dict:
    """Add a step to the trajectory with a quality label."""
    step = {
        "step_id": uid("step"),
        "type": step_type,
        "description": description,
        "label": label,  # productive, neutral, unnecessary, mistake, recovery, discovery, blocked, exploration
        "cost_usd": cost_usd,
        "timestamp": now_iso(),
    }
    trajectory["steps"].append(step)
    return step


def finish_trajectory(trajectory: dict, summary: str = ""):
    """Close the trajectory."""
    trajectory["ended_at"] = now_iso()
    trajectory["commit_end"] = git_head()
    trajectory["result"]["summary"] = summary
    return trajectory


# ── Worker Debrief ───────────────────────────────────────────────────────

def make_worker_debrief(
    trajectory_id: str = "",
    objective: str = "",
    what_changed: str = "",
    discovery: str = "",
    concern: str = "",
    logs_dont_reveal: str = "",
    learned_about_operator: str = "",
    next_action: str = "",
) -> dict:
    return {
        "schema": "worker_debrief",
        "debrief_id": uid("debrief"),
        "trajectory_id": trajectory_id,
        "objective": objective,
        "what_changed": what_changed,
        "discovery": discovery,
        "concern": concern,
        "logs_dont_reveal": logs_dont_reveal,
        "learned_about_operator": learned_about_operator,
        "next_action": next_action,
        "timestamp": now_iso(),
    }


# ── Failure Diagnosis (AgentRx) ────────────────────────────────────────

def make_failure_diagnosis(
    trajectory_id: str = "",
    failure_type: str = "",  # incorrect_action, wrong_tool, budget_exceeded, timeout, logic_error
    root_cause: str = "",
    step_id: str = "",
    severity: str = "medium",
    suggested_fix: str = "",
) -> dict:
    return {
        "schema": "failure_diagnosis",
        "diagnosis_id": uid("fdiag"),
        "trajectory_id": trajectory_id,
        "failure_type": failure_type,
        "root_cause": root_cause,
        "step_id": step_id,
        "severity": severity,
        "suggested_fix": suggested_fix,
        "timestamp": now_iso(),
    }


# ── Step Label (SRFT) ──────────────────────────────────────────────────

STEP_LABELS = ["productive", "neutral", "unnecessary", "mistake", "recovery", "discovery", "blocked", "exploration"]

def label_step(step: dict, label: str, reason: str = ""):
    """Label a step with quality assessment."""
    if label not in STEP_LABELS:
        raise ValueError(f"Invalid label: {label}. Must be one of {STEP_LABELS}")
    step["label"] = label
    step["label_reason"] = reason
    return step


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Trajectory IR Test ===\n")
    
    # 1. Create trajectory
    traj = make_trajectory(objective="Build BOOK schemas")
    print(f"Trajectory: {traj['trajectory_id']}")
    print(f"  Objective: {traj['objective']}")
    
    # 2. Add steps with labels
    s1 = add_step(traj, "code", "Created book_schemas.py", "productive")
    s2 = add_step(traj, "research", "Searched for OpenCode export docs", "neutral")
    s3 = add_step(traj, "code", "Attempted HydraDB connection (failed)", "mistake")
    s4 = add_step(traj, "code", "Fixed by patching neo4j driver", "recovery")
    print(f"\nSteps: {len(traj['steps'])}")
    for s in traj['steps']:
        print(f"  [{s['label']:12s}] {s['description'][:50]}")
    
    # 3. Add decision
    traj["decisions"].append({
        "decision_id": uid("dec"),
        "problem": "HydraDB won't connect from Python",
        "choice": "patch driver instead of switching to HTTP API",
        "confidence": 0.7,
    })
    
    # 4. Finish
    finish_trajectory(traj, summary="BOOK schemas working, HydraDB connection patched")
    print(f"\nTrajectory complete: {traj['result']['summary']}")
    
    # 5. Worker debrief
    debrief = make_worker_debrief(
        trajectory_id=traj["trajectory_id"],
        objective="Build BOOK schemas",
        what_changed="8 core schemas working, persistence layer tested",
        discovery="OpenCode API returns plain text, not structured JSON",
        concern="HydraDB Cypher parser incompatible with Python driver",
        logs_dont_reveal="Human was frustrated with HydraDB for 20 minutes before switching approach",
        learned_about_operator="Operator values getting things working over understanding why they're broken",
        next_action="Wire schemas into daily workflow",
    )
    print(f"\nDebrief: {debrief['debrief_id']}")
    print(f"  Discovery: {debrief['discovery'][:60]}")
    print(f"  Concern: {debrief['concern'][:60]}")
    print(f"  Logs don't reveal: {debrief['logs_dont_reveal'][:60]}")
    
    # 6. Failure diagnosis
    fd = make_failure_diagnosis(
        trajectory_id=traj["trajectory_id"],
        failure_type="wrong_tool",
        root_cause="neo4j 5.28 driver rejects HydraDB as unsupported product",
        severity="medium",
        suggested_fix="patch driver or use HTTP API",
    )
    print(f"\nFailure: {fd['diagnosis_id']}")
    print(f"  Type: {fd['failure_type']}")
    print(f"  Fix: {fd['suggested_fix']}")
    
    print("\n=== ALL WORKING ===")
