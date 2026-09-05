#!/usr/bin/env python3
"""
Problem Registry — tracks all identified problems, their status, and links to experiments.

Each problem has:
- statement (what's wrong)
- severity (0-1)
- status (diagnosing, experimenting, resolved, killed)
- hypotheses (what might fix it)
- experiments (what we're testing)
- linked decisions
- linked actions
- first detected / last updated
"""
import json
import os
import sys
import uuid
from datetime import datetime
from pathlib import Path

PROBLEMS_FILE = Path("/root/StallSpy/dogcasso-ops/problems.jsonl")

def uid(prefix="prob"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def add_problem(statement, severity=0.5, category="general", context=""):
    """Add a problem to the registry."""
    problem = {
        "problem_id": uid("prob"),
        "statement": statement,
        "severity": severity,
        "category": category,  # technical, business, product, process, external
        "context": context,
        "status": "diagnosing",
        "hypotheses": [],
        "experiments": [],
        "decisions": [],
        "actions": [],
        "first_detected": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
        "resolved_at": None,
        "resolution": None,
    }
    
    os.makedirs(PROBLEMS_FILE.parent, exist_ok=True)
    with open(PROBLEMS_FILE, "a") as f:
        f.write(json.dumps(problem, default=str) + "\n")
    
    return problem

def list_problems(status=None, category=None, min_severity=0.0):
    """List problems with optional filters."""
    if not PROBLEMS_FILE.exists():
        return []
    
    problems = []
    with open(PROBLEMS_FILE) as f:
        for line in f:
            try:
                p = json.loads(line.strip())
                if status and p.get("status") != status:
                    continue
                if category and p.get("category") != category:
                    continue
                if p.get("severity", 0) < min_severity:
                    continue
                problems.append(p)
            except:
                continue
    
    return sorted(problems, key=lambda x: x.get("severity", 0), reverse=True)

def update_problem(problem_id, **kwargs):
    """Update a problem's fields."""
    if not PROBLEMS_FILE.exists():
        return None
    
    lines = []
    updated = None
    with open(PROBLEMS_FILE) as f:
        for line in f:
            try:
                p = json.loads(line.strip())
                if p.get("problem_id") == problem_id:
                    p.update(kwargs)
                    p["last_updated"] = datetime.now().isoformat()
                    updated = p
                lines.append(json.dumps(p, default=str))
            except:
                lines.append(line.strip())
    
    with open(PROBLEMS_FILE, "w") as f:
        f.write("\n".join(lines) + "\n")
    
    return updated

def get_problem(problem_id):
    """Get a specific problem."""
    if not PROBLEMS_FILE.exists():
        return None
    with open(PROBLEMS_FILE) as f:
        for line in f:
            try:
                p = json.loads(line.strip())
                if p.get("problem_id") == problem_id:
                    return p
            except:
                continue
    return None

def print_registry():
    """Pretty print the problem registry."""
    problems = list_problems()
    
    print(f"\n{'='*70}")
    print(f"PROBLEM REGISTRY — {len(problems)} problems")
    print(f"{'='*70}")
    
    for p in problems:
        status_icon = {
            "diagnosing": "?",
            "experimenting": "⚡",
            "resolved": "✓",
            "killed": "✗",
        }.get(p.get("status", "?"), "?")
        
        sev = p.get("severity", 0)
        sev_bar = "█" * int(sev * 10) + "░" * (10 - int(sev * 10))
        
        print(f"\n  [{status_icon}] {p['problem_id']}")
        print(f"     {p['statement'][:80]}")
        print(f"     Severity: {sev_bar} ({sev:.1f})")
        print(f"     Category: {p.get('category', '?')}")
        print(f"     Status: {p.get('status', '?')}")
        if p.get("hypotheses"):
            print(f"     Hypotheses: {len(p['hypotheses'])}")
        if p.get("experiments"):
            print(f"     Experiments: {len(p['experiments'])}")
        if p.get("resolution"):
            print(f"     Resolution: {p['resolution'][:60]}")
    
    print(f"\n{'='*70}\n")

# ── Bootstrap: Populate from session data ─────────────────────────────────

def bootstrap():
    """Populate with problems identified during this session."""
    
    # P0: Revenue problems
    add_problem(
        "Zero revenue after 5 days of development",
        severity=0.95, category="business",
        context="Day 5: $88.37 cash, 0 listings, 0 sales. All time spent on specs and tools."
    )
    
    add_problem(
        "No Etsy listings live — nothing to sell",
        severity=0.9, category="business",
        context="Etsy API works, scraper works, but no actual product listed."
    )
    
    add_problem(
        "Dogcasso has no customer-facing products",
        severity=0.85, category="product",
        context="Engine specs exist but no templates rendered, no demos created."
    )
    
    # P0: Technical problems
    add_problem(
        "HydraDB Cypher parser rejects valid queries from Python neo4j driver",
        severity=0.7, category="technical",
        context="neo4j 5.28 driver sends metadata HydraDB interprets as property values. HTTP API also fails. Bolt protocol version mismatch."
    )
    
    add_problem(
        "OpenCode API returns plain text not structured JSON",
        severity=0.6, category="technical",
        context="opencode run works but returns unstructured text. PydanticAI needs structured outputs. opencode_llm.py adapter works around this."
    )
    
    add_problem(
        "Test model produces empty outputs — no real agent intelligence",
        severity=0.5, category="technical",
        context="When no API key configured, all agents return defaults. Real model needs OPENAI_API_KEY or ANTHROPIC_API_KEY."
    )
    
    # P1: Process problems
    add_problem(
        "Endgame architecture eating the experiment",
        severity=0.8, category="process",
        context="Spent more time building frameworks than selling products. Need to focus on DOGCASSO OPS first."
    )
    
    add_problem(
        "No daily cron automation running",
        severity=0.5, category="process",
        context="Scraper, content engine exist but not scheduled. No time series accumulating."
    )
    
    add_problem(
        "No listing version registry",
        severity=0.6, category="process",
        context="When we change a listing, we don't track what changed or why."
    )
    
    # P1: Product problems
    add_problem(
        "No video renders completed for any product",
        severity=0.7, category="product",
        context="Platinum renderers imported but none actually run on Dogcasso products."
    )
    
    add_problem(
        "No QA pipeline for generated content",
        severity=0.6, category="product",
        context="No automated quality checks for video/audio/identity consistency."
    )
    
    # P2: Research problems
    add_problem(
        "No Etsy developer API authorization for analytics",
        severity=0.4, category="external",
        context="Etsy API Terms restrict ML/AI training on API data. Need written permission."
    )
    
    add_problem(
        "Competitor data not systematically collected",
        severity=0.3, category="research",
        context="EverBee/eRank exist but we haven't set up systematic competitor tracking."
    )

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "bootstrap":
        bootstrap()
        print("Problem registry bootstrapped with session data.")
    elif len(sys.argv) > 1 and sys.argv[1] == "list":
        print_registry()
    elif len(sys.argv) > 1 and sys.argv[1] == "add":
        # stallspy problem add "statement" severity category
        statement = sys.argv[2] if len(sys.argv) > 2 else "new problem"
        severity = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
        category = sys.argv[4] if len(sys.argv) > 4 else "general"
        p = add_problem(statement, severity, category)
        print(f"Added: {p['problem_id']} — {p['statement'][:60]}")
    else:
        print("Usage:")
        print("  stallspy problem bootstrap    # populate from session")
        print("  stallspy problem list          # show all problems")
        print("  stallspy problem add '...' severity category")
