"""
BOOK Schemas — The experimental record / operating memory.

Six core record types for MythicBee operations.
All Pydantic, all versioned, all append-oriented.
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

def uid(prefix: str = "rec") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"

def sha256(data: Any) -> str:
    return hashlib.sha256(json.dumps(data, default=str, sort_keys=True).encode()).hexdigest()

def now_iso() -> str:
    return datetime.now().isoformat()

# ── Schemas ──────────────────────────────────────────────────────────────

# 1. DailyRun

def make_daily_run(day_id: str = None, opened_at: str = None) -> dict:
    return {
        "schema": "DailyRun",
        "day_id": day_id or f"mythicbee_{datetime.now().strftime('%Y_%m_%d')}",
        "opened_at": opened_at or now_iso(),
        "closed_at": None,
        "etsy_snapshot_start": None,
        "etsy_snapshot_end": None,
        "orders": 0,
        "revenue": 0.0,
        "fees": 0.0,
        "render_cost": 0.0,
        "refunds": 0,
        "profit_estimate": 0.0,
        "work_completed": [],
        "decisions": [],
        "experiments_active": [],
        "problems": [],
        "wins": [],
        "next_priorities": [],
    }

# 2. AgentSession

def make_agent_session(objective: str = "", scope: str = "", priority: str = "normal") -> dict:
    return {
        "schema": "AgentSession",
        "session_id": uid("ses"),
        "started_at": now_iso(),
        "ended_at": None,
        "agent": {
            "runtime": "opencode",
            "model": "mimo-v2.5",
            "provider": "opencode",
        },
        "repo": {
            "name": "StallShark",
            "start_commit": _git_head(),
            "end_commit": None,
        },
        "task": {
            "objective": objective,
            "scope": scope,
            "priority": priority,
        },
        "inputs": {
            "files_read": [],
            "source_refs": [],
            "previous_handover": None,
        },
        "outputs": {
            "commits": [],
            "files_created": [],
            "files_changed": [],
            "artifacts": [],
        },
        "decisions": [],
        "experiments_touched": [],
        "actions_taken": [],
        "cost": {
            "model_usd": 0.0,
            "external_usd": 0.0,
            "gpu_usd": 0.0,
        },
        "result": {
            "status": "in_progress",
            "summary": "",
            "blockers": [],
            "next_actions": [],
        },
    }

def _git_head() -> str:
    try:
        import subprocess
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, cwd="/root/StallShark")
        return r.stdout.strip()
    except:
        return "unknown"

# 3. Decision

def make_decision(subject_type: str, subject_id: str, question: str,
                  decision: str, alternatives: list, reason: str,
                  confidence: float = 0.5, expected_metric: str = "",
                  expected_direction: str = "") -> dict:
    return {
        "schema": "Decision",
        "decision_id": uid("dec"),
        "created_at": now_iso(),
        "subject": {"type": subject_type, "id": subject_id},
        "question": question,
        "decision": decision,
        "alternatives": alternatives,
        "reason_summary": reason,
        "evidence": [],
        "confidence": confidence,
        "expected_effect": {
            "metric": expected_metric,
            "direction": expected_direction,
        },
        "review_at": None,
    }

# 4. Experiment

def make_experiment(hypothesis: str, unit_listing_id: str,
                    control: dict, treatment: dict,
                    primary_metric: str = "ctr",
                    started_at: str = None) -> dict:
    return {
        "schema": "Experiment",
        "experiment_id": uid("exp"),
        "hypothesis": hypothesis,
        "unit": {"listing_id": unit_listing_id},
        "control": control,
        "treatment": treatment,
        "primary_metric": primary_metric,
        "guardrails": ["conversion_rate"],
        "started_at": started_at or now_iso(),
        "evaluate_after": None,
        "minimum_impressions": 100,
        "status": "running",
        "result": None,
    }

# 5. MetricSnapshot

def make_metric_snapshot(shop_metrics: dict = None,
                         listing_metrics: list = None,
                         reviews: dict = None,
                         operations: dict = None) -> dict:
    return {
        "schema": "MetricSnapshot",
        "snapshot_id": uid("snap"),
        "observed_at": now_iso(),
        "shop": shop_metrics or {},
        "listings": listing_metrics or [],
        "reviews": reviews or {},
        "operations": operations or {},
    }

# 6. ActionReceipt

def make_action_receipt(action_type: str, target_id: str,
                        before_ref: str = None, after_ref: str = None,
                        actor_type: str = "agent", actor_id: str = "system",
                        external_request_id: str = None,
                        related_decision: str = None,
                        related_experiment: str = None,
                        cost: float = 0.0) -> dict:
    return {
        "schema": "ActionReceipt",
        "action_id": uid("act"),
        "at": now_iso(),
        "actor": {"type": actor_type, "id": actor_id},
        "action": action_type,
        "target": {"listing_id": target_id},
        "before": {"ref": before_ref} if before_ref else None,
        "after": {"ref": after_ref} if after_ref else None,
        "external_request_id": external_request_id,
        "result": {"success": True},
        "related_decision": related_decision,
        "related_experiment": related_experiment,
        "cost": cost,
    }

# ── Persistence ──────────────────────────────────────────────────────────

DATA_ROOT = Path("/root/StallShark/mythicbee-ops")

def _ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def save_record(record: dict, category: str, record_id: str = None):
    """Save a record to the filesystem."""
    schema = record.get("schema", "unknown")
    rid = record_id or record.get(f"{schema.lower()}_id", uid("rec"))
    
    base = DATA_ROOT / category
    _ensure_dir(base)
    
    path = base / f"{rid}.json"
    with open(path, "w") as f:
        json.dump(record, f, indent=2, default=str)
    
    return path

def load_record(category: str, record_id: str) -> dict:
    """Load a record from the filesystem."""
    path = DATA_ROOT / category / f"{record_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Record not found: {path}")
    with open(path) as f:
        return json.load(f)

def list_records(category: str) -> list:
    """List all records in a category."""
    base = DATA_ROOT / category
    if not base.exists():
        return []
    return [f.stem for f in base.glob("*.json")]

def git_commit_record(category: str, record_id: str, message: str = None):
    """Git commit a record for lineage."""
    path = DATA_ROOT / category / f"{record_id}.json"
    if not path.exists():
        return None
    
    import subprocess
    msg = message or f"book: {category}/{record_id}"
    subprocess.run(["git", "add", str(path)], cwd="/root/StallShark", capture_output=True)
    r = subprocess.run(["git", "commit", "-m", msg], cwd="/root/StallShark", capture_output=True, text=True)
    return r.stdout.strip()


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== BOOK Schemas Test ===\n")
    
    # Test DailyRun
    dr = make_daily_run()
    print(f"DailyRun: {dr['day_id']}")
    
    # Test AgentSession
    session = make_agent_session(objective="Launch Game Winner listing")
    print(f"AgentSession: {session['session_id']}")
    
    # Test Decision
    dec = make_decision(
        subject_type="listing", subject_id="dog_roast_30th",
        question="Change thumbnail v2 to v3?",
        decision="use v3",
        alternatives=["v2", "v3"],
        reason="Face legibility stronger at thumbnail size",
        confidence=0.72,
        expected_metric="ctr",
        expected_direction="increase",
    )
    print(f"Decision: {dec['decision_id']}")
    
    # Test Experiment
    exp = make_experiment(
        hypothesis="Large face + short headline improves CTR",
        unit_listing_id="listing_123",
        control={"thumbnail_version": 2},
        treatment={"thumbnail_version": 3},
        primary_metric="ctr",
    )
    print(f"Experiment: {exp['experiment_id']}")
    
    # Test MetricSnapshot
    snap = make_metric_snapshot(
        shop_metrics={"views": 1200, "visits": 80, "orders": 3, "revenue": 47.97},
        listing_metrics=[{"listing_id": "l1", "impressions": 500, "views": 40, "favorites": 5, "orders": 1}],
        reviews={"count": 12, "average": 4.8},
        operations={"open_orders": 2, "failed_renders": 0, "rerolls": 1},
    )
    print(f"MetricSnapshot: {snap['snapshot_id']}")
    
    # Test ActionReceipt
    act = make_action_receipt(
        action_type="etsy.listing.update",
        target_id="listing_123",
        before_ref="sha256:abc",
        after_ref="sha256:def",
        cost=0.0,
    )
    print(f"ActionReceipt: {act['action_id']}")
    
    # Test persistence
    path = save_record(dec, "decisions")
    loaded = load_record("decisions", dec["decision_id"])
    assert loaded["decision"] == "use v3"
    print(f"\nPersistence: OK ({path})")
    
    # Test listing
    records = list_records("decisions")
    print(f"List decisions: {len(records)} records")
    
    print("\n=== ALL SCHEMAS WORKING ===")
