"""
Budget Stack — BATS tracker + SpendGuard + BudgetEnvelope.

BATS = Budget-Aware Task Selection (planning policy)
AgentBudget = hard enforcement / circuit breaker
SpendGuard = pre-flight cost check
"""
from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

def uid(prefix="bud"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def now_iso():
    return datetime.now().isoformat()


# ── BudgetEnvelope ───────────────────────────────────────────────────────

def make_budget_envelope(
    cash_usd: float = 5.0,
    tokens: int = 500000,
    human_minutes: int = 60,
    tool_calls: int = 50,
    model_calls: int = 20,
) -> dict:
    return {
        "schema": "budget_envelope",
        "envelope_id": uid("env"),
        "cash_usd": cash_usd,
        "tokens": tokens,
        "human_minutes": human_minutes,
        "tool_calls": tool_calls,
        "model_calls": model_calls,
        "spent": {
            "cash_usd": 0.0,
            "tokens": 0,
            "human_minutes": 0.0,
            "tool_calls": 0,
            "model_calls": 0,
        },
        "created_at": now_iso(),
    }

def can_spend(envelope: dict, category: str, amount: float) -> bool:
    """Check if we can spend within budget."""
    remaining = envelope[category] - envelope["spent"][category]
    return remaining >= amount

def record_spend(envelope: dict, category: str, amount: float):
    """Record spend against budget."""
    envelope["spent"][category] = envelope["spent"].get(category, 0) + amount

def budget_status(envelope: dict) -> dict:
    """Get remaining budget for all categories."""
    return {
        cat: envelope[cat] - envelope["spent"].get(cat, 0)
        for cat in ["cash_usd", "tokens", "human_minutes", "tool_calls", "model_calls"]
    }

def budget_utilization(envelope: dict) -> dict:
    """Get utilization percentage for all categories."""
    return {
        cat: (envelope["spent"].get(cat, 0) / envelope[cat] * 100) if envelope[cat] > 0 else 0
        for cat in ["cash_usd", "tokens", "human_minutes", "tool_calls", "model_calls"]
    }


# ── SpendGuard ──────────────────────────────────────────────────────────

class SpendGuard:
    """Pre-flight cost check. Returns approval/rejection."""
    
    def __init__(self, envelope: dict):
        self.envelope = envelope
    
    def check(self, category: str, amount: float, reason: str = "") -> dict:
        remaining = self.envelope[category] - self.envelope["spent"].get(category, 0)
        utilization = self.envelope["spent"].get(category, 0) / self.envelope[category] * 100 if self.envelope[category] > 0 else 0
        
        if remaining < amount:
            return {
                "approved": False,
                "reason": f"Budget exceeded: {category} remaining={remaining:.2f}, requested={amount:.2f}",
                "utilization": utilization,
            }
        
        if utilization > 80:
            return {
                "approved": True,
                "warning": f"Budget at {utilization:.0f}% — consider alternatives",
                "utilization": utilization,
            }
        
        return {"approved": True, "utilization": utilization}
    
    def record_and_check(self, category: str, amount: float, reason: str = "") -> dict:
        result = self.check(category, amount, reason)
        if result["approved"]:
            record_spend(self.envelope, category, amount)
        return result


# ── BATS Tracker ────────────────────────────────────────────────────────

class BATSTracker:
    """Budget-Aware Task Selection — plans resource allocation."""
    
    def __init__(self, daily_cash: float = 5.0, daily_tokens: int = 500000):
        self.daily_cash = daily_cash
        self.daily_tokens = daily_tokens
        self.spent_today = {"cash": 0.0, "tokens": 0}
    
    def plan(self, tasks: list) -> list:
        """Allocate budget across tasks."""
        remaining_cash = self.daily_cash - self.spent_today["cash"]
        remaining_tokens = self.daily_tokens - self.spent_today["tokens"]
        
        allocations = []
        for task in tasks:
            priority = task.get("priority", 1)
            estimated_cost = task.get("estimated_cash", 0.5)
            estimated_tokens = task.get("estimated_tokens", 50000)
            
            can_afford = (remaining_cash >= estimated_cost and remaining_tokens >= estimated_tokens)
            
            allocations.append({
                "task": task.get("name", "unknown"),
                "priority": priority,
                "estimated_cash": estimated_cost,
                "estimated_tokens": estimated_tokens,
                "approved": can_afford,
                "remaining_cash": remaining_cash,
                "remaining_tokens": remaining_tokens,
            })
            
            if can_afford:
                remaining_cash -= estimated_cost
                remaining_tokens -= estimated_tokens
        
        return allocations
    
    def record_spend(self, cash: float, tokens: int):
        self.spent_today["cash"] += cash
        self.spent_today["tokens"] += tokens
    
    def status(self) -> dict:
        return {
            "daily_cash": self.daily_cash,
            "daily_tokens": self.daily_tokens,
            "spent_cash": self.spent_today["cash"],
            "spent_tokens": self.spent_today["tokens"],
            "remaining_cash": self.daily_cash - self.spent_today["cash"],
            "remaining_tokens": self.daily_tokens - self.spent_today["tokens"],
        }


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Budget Stack Test ===\n")
    
    # 1. BudgetEnvelope
    env = make_budget_envelope(cash_usd=5.0, tokens=500000)
    print(f"Envelope: ${env['cash_usd']}, {env['tokens']} tokens")
    assert can_spend(env, "cash_usd", 3.0)
    assert not can_spend(env, "cash_usd", 6.0)
    record_spend(env, "cash_usd", 2.5)
    assert can_spend(env, "cash_usd", 2.0)
    assert not can_spend(env, "cash_usd", 3.0)
    print(f"After $2.50 spend: {budget_status(env)}")
    
    # 2. SpendGuard
    guard = SpendGuard(env)
    r1 = guard.check("cash_usd", 1.0)
    print(f"\nSpendGuard check $1: approved={r1['approved']}")
    r2 = guard.check("cash_usd", 3.0)
    print(f"SpendGuard check $3: approved={r2['approved']}, reason={r2.get('reason', 'ok')}")
    
    # 3. BATS Tracker
    bats = BATSTracker(daily_cash=10.0, daily_tokens=1000000)
    tasks = [
        {"name": "research", "priority": 1, "estimated_cash": 0.0, "estimated_tokens": 100000},
        {"name": "generation", "priority": 2, "estimated_cash": 2.0, "estimated_tokens": 200000},
        {"name": "strategy", "priority": 3, "estimated_cash": 0.0, "estimated_tokens": 50000},
    ]
    allocations = bats.plan(tasks)
    print(f"\nBATS plan:")
    for a in allocations:
        print(f"  {a['task']}: approved={a['approved']}, ${a['estimated_cash']}, {a['estimated_tokens']} tokens")
    
    print(f"\nBATS status: {bats.status()}")
    
    print("\n=== ALL WORKING ===")
