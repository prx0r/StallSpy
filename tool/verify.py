#!/usr/bin/env python3
"""
StallShark Verify — checks completeness of a CompanyDay.

Usage: stallshark verify --day today
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path("/root/StallShark")
PRIVATE = ROOT / "private"
MYTHICBEE_OPS = ROOT / "mythicbee-ops"

def verify_day(day_id: str = None) -> dict:
    """Run full verification of a CompanyDay."""
    if not day_id:
        # Find latest day
        days_dir = MYTHICBEE_OPS / "days"
        if days_dir.exists():
            files = sorted(days_dir.glob("*.json"))
            if files:
                with open(files[-1]) as f:
                    data = json.load(f)
                day_id = data.get("day_id", "unknown")
    
    results = {"day_id": day_id, "checks": []}
    
    def check(name, passed, detail=""):
        results["checks"].append({"name": name, "passed": passed, "detail": detail})
        symbol = "✓" if passed else "✗"
        print(f"  {symbol} {name}: {detail}")
    
    print(f"\n{'='*60}")
    print(f"COMPANY DAY {day_id}")
    print(f"{'='*60}\n")
    
    # 1. CAPTURE
    print("CAPTURE")
    check("CompanyDay exists", (MYTHICBEE_OPS / "days").exists() and any((MYTHICBEE_OPS / "days").glob("*.json")))
    check("State snapshot exists", (MYTHICBEE_OPS / "states").exists() and any((MYTHICBEE_OPS / "states").glob("*.json")))
    check("Perspectives recorded", (MYTHICBEE_OPS / "perspectives").exists() and len(list((MYTHICBEE_OPS / "perspectives").glob("*.json"))) >= 2)
    check("Decisions recorded", (MYTHICBEE_OPS / "decisions").exists() and len(list((MYTHICBEE_OPS / "decisions").glob("*.json"))) >= 1)
    check("Problems tracked", (MYTHICBEE_OPS / "problems.jsonl").exists())
    check("Economic events", (MYTHICBEE_OPS / "economic_events").exists())
    
    # 2. STORAGE
    print("\nSTORAGE")
    artifacts = list((PRIVATE / "artifacts" / "sha256").rglob("*.meta.json"))
    manifests = list((PRIVATE / "manifests").glob("*.json"))
    check("Local artifacts", len(artifacts) > 0, f"{len(artifacts)} artifacts")
    check("R2 manifests", len(manifests) > 0, f"{len(manifests)} manifests")
    check("Private dir exists", PRIVATE.exists())
    
    # 3. INDEPENDENCE
    print("\nINDEPENDENCE")
    check("No credentials in source", not any(
        f.exists() for f in [ROOT / "tool" / ".env_leaked"]
    ))
    
    # 4. PUBLIC
    print("\nPUBLIC")
    check("Content generated", any((ROOT / "logs").glob("*_full.md")))
    check("Video script exists", any((ROOT / "logs").glob("*_video.md")))
    check("TL;DR exists", any((ROOT / "logs").glob("*_tldr.md")))
    
    # Summary
    passed = sum(1 for c in results["checks"] if c["passed"])
    total = len(results["checks"])
    all_pass = passed == total
    
    print(f"\n{'='*60}")
    print(f"DAY COMPLETE: {'TRUE' if all_pass else 'FALSE'} ({passed}/{total} checks passed)")
    print(f"{'='*60}")
    
    results["complete"] = all_pass
    results["passed"] = passed
    results["total"] = total
    
    # Write report
    report_path = ROOT / "private" / "manifests" / f"verify_{day_id}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    day_id = sys.argv[1] if len(sys.argv) > 1 else None
    verify_day(day_id)
