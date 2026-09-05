#!/usr/bin/env python3
"""Morning record — log your belief, goal, and planned experiment before starting work."""

import json
import os
import sys
from datetime import datetime

MORNING_DIR = "/root/StallSpy/morning"

def record(day_number, goal, belief, bet, success, kill):
    """Record the morning belief state."""
    os.makedirs(MORNING_DIR, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    record = {
        "date": date_str,
        "day_number": day_number,
        "timestamp": datetime.now().isoformat(),
        "goal": goal,
        "belief": belief,
        "bet": bet,
        "success_condition": success,
        "kill_condition": kill,
    }
    
    path = os.path.join(MORNING_DIR, f"{date_str}.json")
    with open(path, "w") as f:
        json.dump(record, f, indent=2)
    
    print(f"Morning record saved: {path}")
    print(f"  Goal: {goal}")
    print(f"  Belief: {belief}")
    print(f"  Bet: {bet}")
    print(f"  Success: {success}")
    print(f"  Kill: {kill}")
    
    return record

def show_today():
    """Show today's morning record if it exists."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(MORNING_DIR, f"{date_str}.json")
    
    if os.path.exists(path):
        with open(path) as f:
            record = json.load(f)
        print(f"Morning record for {date_str}:")
        print(f"  Goal: {record['goal']}")
        print(f"  Belief: {record['belief']}")
        print(f"  Bet: {record['bet']}")
        print(f"  Success: {record['success_condition']}")
        print(f"  Kill: {record['kill_condition']}")
    else:
        print(f"No morning record for {date_str}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "today":
        show_today()
    elif sys.argv[1] == "help":
        print("Usage:")
        print("  python3 morning_record.py 1 \\")
        print("    \"Get Birthday V1 listing live\" \\")
        print("    \"Football birthday gifts convert better than generic\" \\")
        print("    \"Test 50th birthday variant against generic dad\" \\")
        print("    \"50th birthday gets 2x more favorites\" \\")
        print("    \"Zero favorites after 48 hours\"")
        print()
        print("  python3 morning_record.py today  # show today's record")
    else:
        day = int(sys.argv[1])
        goal = sys.argv[2] if len(sys.argv) > 2 else input("Goal: ")
        belief = sys.argv[3] if len(sys.argv) > 3 else input("Belief: ")
        bet = sys.argv[4] if len(sys.argv) > 4 else input("Bet: ")
        success = sys.argv[5] if len(sys.argv) > 5 else input("Success condition: ")
        kill = sys.argv[6] if len(sys.argv) > 6 else input("Kill condition: ")
        record(day, goal, belief, bet, success, kill)
