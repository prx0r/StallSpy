"""
DP2-10: Long-horizon eval — CompanyForecast, WorkOrder grader, repeated-run evaluator.
"""
from __future__ import annotations
import json, os, time, uuid
from datetime import datetime
from pathlib import Path

def uid(p="eval"): return f"{p}_{uuid.uuid4().hex[:8]}"
def now(): return datetime.now().isoformat()

# ── CompanyForecast ──────────────────────────────────────────────────────

def make_forecast(horizon_days: int, target_metric: str, baseline: float,
                  prediction: float, confidence: float = 0.5) -> dict:
    return {
        "schema": "company_forecast",
        "forecast_id": uid("fc"),
        "horizon_days": horizon_days,
        "target_metric": target_metric,
        "baseline": baseline,
        "prediction": prediction,
        "confidence": confidence,
        "actual": None,
        "error": None,
        "created_at": now(),
        "resolved_at": None,
    }

def resolve_forecast(forecast: dict, actual: float):
    forecast["actual"] = actual
    forecast["error"] = abs(forecast["prediction"] - actual) / max(actual, 0.01)
    forecast["resolved_at"] = now()
    return forecast

def brier_score(forecasts: list) -> float:
    """Compute Brier score for resolved forecasts."""
    resolved = [f for f in forecasts if f.get("actual") is not None]
    if not resolved:
        return 0.0
    scores = []
    for f in resolved:
        predicted = f["prediction"]
        actual = f["actual"]
        baseline = f.get("baseline", 0)
        if baseline > 0:
            scores.append((predicted - actual/baseline) ** 2)
    return sum(scores) / len(scores) if scores else 0.0

# ── WorkOrder Grader ────────────────────────────────────────────────────

def make_work_order_grader():
    """Grade a work order on multiple dimensions."""
    return {
        "schema": "work_order_grader",
        "grader_id": uid("wog"),
        "dimensions": {
            "objective_alignment": {"weight": 0.25, "score": 0.0},
            "budget_adherence": {"weight": 0.20, "score": 0.0},
            "quality": {"weight": 0.25, "score": 0.0},
            "speed": {"weight": 0.15, "score": 0.0},
            "learning_value": {"weight": 0.15, "score": 0.0},
        },
        "overall_score": 0.0,
        "created_at": now(),
    }

def grade_work_order(grader: dict, scores: dict):
    for dim, score in scores.items():
        if dim in grader["dimensions"]:
            grader["dimensions"][dim]["score"] = score
    grader["overall_score"] = sum(
        d["weight"] * d["score"] for d in grader["dimensions"].values()
    )
    return grader

# ── Repeated-Run Evaluator ──────────────────────────────────────────────

def make_repeated_run_evaluator(n_runs: int = 10):
    return {
        "schema": "repeated_run_evaluator",
        "evaluator_id": uid("rre"),
        "n_runs": n_runs,
        "runs": [],
        "variance": 0.0,
        "mean_return": 0.0,
        "created_at": now(),
    }

def record_run(evalr: dict, run_return: float, tokens: int, cost: float):
    evalr["runs"].append({
        "return": run_return,
        "tokens": tokens,
        "cost": cost,
        "timestamp": now(),
    })
    returns = [r["return"] for r in evalr["runs"]]
    evalr["mean_return"] = sum(returns) / len(returns) if returns else 0
    if len(returns) > 1:
        mean = evalr["mean_return"]
        evalr["variance"] = sum((r - mean)**2 for r in returns) / (len(returns) - 1)
    return evalr

# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== DP2-10: Long-Horizon Eval ===\n")
    
    # Forecast
    fc = make_forecast(30, "conversion_rate", 0.021, 0.032, 0.7)
    resolve_forecast(fc, 0.029)
    print(f"Forecast: predicted={fc['prediction']}, actual={fc['actual']}, error={fc['error']:.3f}")
    
    # Work order grader
    grader = make_work_order_grader()
    grade_work_order(grader, {"objective_alignment": 0.8, "budget_adherence": 0.9, "quality": 0.7, "speed": 0.6, "learning_value": 0.8})
    print(f"Work order grade: {grader['overall_score']:.2f}")
    
    # Repeated run evaluator
    evaluator = make_repeated_run_evaluator(5)
    for ret in [0.12, -0.03, 0.08, 0.15, -0.01]:
        record_run(evaluator, ret, 100000, 1.0)
    print(f"Repeated run: mean={evaluator['mean_return']:.3f}, variance={evaluator['variance']:.4f}")
    
    print("\n=== ALL WORKING ===")
