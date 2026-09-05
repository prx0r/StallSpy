"""
CapabilityExperiment — structured comparison of frontier mechanisms.

Every imported capability must pass:
1. upstream reference + version
2. minimal adapter
3. fixture
4. baseline
5. feature treatment
6. evaluator
7. Cost/UsageReceipt
8. result in CapabilityExperiment
"""
from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

def uid(prefix="cap"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def now_iso():
    return datetime.now().isoformat()


# ── Upstream Registry Entry ──────────────────────────────────────────────

def make_upstream_entry(
    id: str,
    paper: str = "",
    repo: str = "",
    commit: str = "HEAD",
    license: str = "",
    mechanisms: list = None,
    mini_test: str = "",
) -> dict:
    return {
        "id": id,
        "paper": paper,
        "repo": repo,
        "commit": commit,
        "license": license,
        "integration_status": "candidate",
        "mechanisms": mechanisms or [],
        "mini_test": mini_test,
    }


# ── CapabilityExperiment ────────────────────────────────────────────────

def make_capability_experiment(
    upstream_id: str,
    hypothesis: str,
    mechanism: str,
    description: str = "",
) -> dict:
    """Structured comparison: baseline vs feature treatment."""
    return {
        "schema": "capability_experiment",
        "experiment_id": uid("capexp"),
        "upstream_id": upstream_id,
        "hypothesis": hypothesis,
        "mechanism": mechanism,
        "description": description,
        "baseline": {
            "description": "current system without this mechanism",
            "implementation": "none",
        },
        "treatment": {
            "description": "current system + this mechanism",
            "implementation": "adapter",
        },
        "metrics": {
            "primary": "outcome_quality",
            "secondary": ["token_cost", "cash_cost", "latency", "human_intervention_rate"],
        },
        "status": "designed",
        "result": None,
        "created_at": now_iso(),
    }


# ── Feature Flag ────────────────────────────────────────────────────────

def make_feature_flag(
    name: str,
    enabled: bool = False,
    upstream_id: str = "",
    description: str = "",
) -> dict:
    return {
        "schema": "feature_flag",
        "flag_id": uid("flag"),
        "name": name,
        "enabled": enabled,
        "upstream_id": upstream_id,
        "description": description,
        "created_at": now_iso(),
    }


# ── Persistence ──────────────────────────────────────────────────────────

PROTOCOL_DIR = Path("/root/StallShark/protocol")

def save_json(data: Any, path: str):
    full_path = PROTOCOL_DIR / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    return full_path

def load_json(path: str) -> Any:
    with open(PROTOCOL_DIR / path) as f:
        return json.load(f)


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== CapabilityExperiment Test ===\n")
    
    # 1. Upstream entry
    entry = make_upstream_entry(
        id="pahf",
        paper="arxiv:2602.16173",
        repo="https://github.com/facebookresearch/PAHF",
        mechanisms=["pre_action_feedback", "post_action_feedback", "explicit_user_memory"],
        mini_test="ft-001",
    )
    print(f"Upstream: {entry['id']} ({len(entry['mechanisms'])} mechanisms)")
    
    # 2. Capability experiment
    exp = make_capability_experiment(
        upstream_id="pahf",
        hypothesis="Pre-action clarification reduces unnecessary human interventions",
        mechanism="pre_action_feedback",
        description="Ask clarifying questions before executing ambiguous tasks",
    )
    print(f"Experiment: {exp['experiment_id']}")
    print(f"  Hypothesis: {exp['hypothesis']}")
    print(f"  Baseline: {exp['baseline']['description']}")
    print(f"  Treatment: {exp['treatment']['description']}")
    
    # 3. Feature flag
    flag = make_feature_flag(
        name="pahf_pre_action_feedback",
        enabled=False,
        upstream_id="pahf",
        description="PAHF pre-action clarification before task execution",
    )
    print(f"Flag: {flag['name']} (enabled={flag['enabled']})")
    
    # 4. Save
    save_json(entry, "upstreams/pahf.json")
    save_json(exp, "experiments/capexp_pahf.json")
    save_json(flag, "flags/pahf_pre_action_feedback.json")
    
    print("\nSaved to protocol/")
    print("=== ALL WORKING ===")
