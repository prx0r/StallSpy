#!/usr/bin/env python3
"""Q4 commerce intelligence ranker.

Static pack utility: filters and reranks the opportunity seed file.
It intentionally does NOT pretend to fetch live marketplace competition.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

WEIGHTS = {
    "capital_efficiency": 1.6,
    "q4_fit": 1.3,
    "organic_distribution": 1.5,
    "ai_quality_moat": 1.4,
    "margin_potential": 1.2,
    "operational_simplicity": 1.0,
    "competition_whitespace_hypothesis": 1.0,
}

def score(scores: dict, weights: dict = WEIGHTS) -> float:
    denom = sum(weights.values())
    if denom <= 0:
        raise ValueError("weights must sum to >0")
    total = sum(float(scores.get(k, 0)) * w for k, w in weights.items())
    return round((total / denom) * 10, 1)

def rank(items: list[dict], *, zero_capital=False, q4=False) -> list[dict]:
    out = []
    for item in items:
        if zero_capital and item.get("capital_band") not in {"$0-10"}:
            continue
        if q4 and float(item["scores"].get("q4_fit", 0)) < 8:
            continue
        row = dict(item)
        row["runtime_score_100"] = score(row["scores"])
        out.append(row)
    return sorted(out, key=lambda x: (-x["runtime_score_100"], x["id"]))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/opportunities.json")
    p.add_argument("--top", type=int, default=15)
    p.add_argument("--zero-capital", action="store_true")
    p.add_argument("--q4", action="store_true")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    items = json.loads(Path(args.data).read_text())
    ranked = rank(items, zero_capital=args.zero_capital, q4=args.q4)[:args.top]

    if args.json:
        print(json.dumps(ranked, indent=2))
        return
    print(f"{'RANK':>4} {'SCORE':>6} {'CAPITAL':>9}  OPPORTUNITY")
    for i, item in enumerate(ranked, 1):
        print(f"{i:>4} {item['runtime_score_100']:>6.1f} {item['capital_band']:>9}  {item['name']}")

if __name__ == "__main__":
    main()
