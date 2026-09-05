#!/usr/bin/env python3
"""
StallShark CLI — day management, decisions, experiments, snapshots, handovers.

Usage:
    stallshark day start              Start a new day
    stallshark day status             Show current day status
    stallshark day close              Close day, print summary
    stallshark decision add           Add a decision
    stallshark experiment add         Add an experiment
    stallshark experiment list        List active experiments
    stallshark experiment status ID   Check experiment status
    stallshark snapshot add           Add metric snapshot
    stallshark session record         Record agent session
    stallshark handover create        Create handover document
    stallshark etsy snapshot          Capture Etsy metrics
    stallshark render receipt         Record a render
"""
import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

# Add book_schemas to path
sys.path.insert(0, str(Path(__file__).parent))
from book_schemas import (
    make_daily_run, make_agent_session, make_decision,
    make_experiment, make_metric_snapshot, make_action_receipt,
    save_record, load_record, list_records, now_iso, _git_head,
    DATA_ROOT
)

# ── Day Management ───────────────────────────────────────────────────────

def day_start():
    """Start a new day."""
    day = make_daily_run()
    path = save_record(day, "days", day["day_id"])
    
    # Write TODAY.md
    today_md = f"""# {day['day_id']}

## Top 3 Priorities
1. 
2. 
3. 

## Notes
"""
    today_path = Path("/root/StallShark/TODAY.md")
    with open(today_path, "w") as f:
        f.write(today_md)
    
    print(f"Day started: {day['day_id']}")
    print(f"  Run: {path}")
    print(f"  TODAY.md written")
    return day

def day_status():
    """Show current day status."""
    days = list_records("days")
    if not days:
        print("No active day. Run: stallshark day start")
        return
    
    latest = sorted(days)[-1]
    day = load_record("days", latest)
    
    decisions = len(list_records("decisions"))
    experiments = len(list_records("experiments"))
    sessions = len(list_records("sessions"))
    
    print(f"Day: {day['day_id']}")
    print(f"  Opened: {day.get('opened_at', day.get('date', 'unknown'))}")
    print(f"  Closed: {day.get('closed_at', 'NO')}")
    print(f"  Orders: {day.get('orders', 0)}")
    print(f"  Revenue: ${day.get('revenue', 0):.2f}")
    print(f"  Decisions: {decisions}")
    print(f"  Experiments: {experiments}")
    print(f"  Sessions: {sessions}")

def day_close():
    """Close day, print summary, create handover."""
    days = list_records("days")
    if not days:
        print("No active day.")
        return
    
    latest = sorted(days)[-1]
    day = load_record("days", latest)
    day["closed_at"] = now_iso()
    save_record(day, "days", day["day_id"])
    
    # Collect day's records
    decisions = list_records("decisions")
    experiments = list_records("experiments")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"DAY CLOSE: {day['day_id']}")
    print(f"{'='*60}")
    print(f"Opened: {day['opened_at']}")
    print(f"Closed: {day['closed_at']}")
    print(f"\nOrders: {day.get('orders', 0)}")
    print(f"Revenue: ${day.get('revenue', 0):.2f}")
    print(f"Fees: ${day.get('fees', 0):.2f}")
    print(f"Render cost: ${day.get('render_cost', 0):.2f}")
    print(f"Estimated profit: ${day.get('profit_estimate', 0):.2f}")
    print(f"\nDecisions today: {len(decisions)}")
    print(f"Active experiments: {len(experiments)}")
    print(f"Work completed: {len(day.get('work_completed', []))}")
    
    # Print next priorities
    print(f"\nTomorrow's priorities:")
    for i, p in enumerate(day.get("next_priorities", [])[:3], 1):
        print(f"  {i}. {p}")
    
    # Create handover
    handover = f"""# HANDOVER — {day['day_id']}

## What I Was Trying To Do
{chr(10).join(f'- {w}' for w in day.get('work_completed', ['(none recorded)']))}

## What Changed
{len(day.get('decisions', []))} decisions made
{len(experiments)} experiments active

## What I Verified
- Day closed at {day.get('closed_at', 'unknown')}

## What Is Currently Broken
(assess from problems)

## What I Did Not Do
{chr(10).join(f'- {p}' for p in day.get('next_priorities', ['(none recorded)']))}

## Next Three Actions
{chr(10).join(f'{i+1}. {p}' for i, p in enumerate(day.get('next_priorities', ['assess state', 'prioritize', 'execute'])[:3]))}

## Relevant Commits
{_git_head()}

## Open Experiments
{chr(10).join(f'- {e}' for e in experiments)}
"""
    
    handover_path = DATA_ROOT / "handovers" / f"handover_{day['day_id']}.md"
    handover_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handover_path, "w") as f:
        f.write(handover)
    
    print(f"\nHandover: {handover_path}")

# ── Commands ──────────────────────────────────────────────────────────────

def render_receipt():
    """Record a render."""
    args = sys.argv[2:]
    receipt = make_action_receipt(
        action_type="render.complete",
        target_id=args[0] if args else "unknown",
        cost=float(args[1]) if len(args) > 1 else 0.0,
    )
    path = save_record(receipt, "actions")
    print(f"Render receipt: {receipt['action_id']}")
    print(f"  Target: {receipt['target']['listing_id']}")
    print(f"  Cost: ${receipt['cost']:.2f}")
    print(f"  Saved: {path}")

def etsy_snap():
    """Run Etsy snapshot."""
    from etsy_snapshot import run_snapshot
    run_snapshot()

def session_record():
    """Record current agent session."""
    session = make_agent_session(
        objective=sys.argv[2] if len(sys.argv) > 2 else "session work",
        scope=sys.argv[3] if len(sys.argv) > 3 else "general",
    )
    path = save_record(session, "sessions")
    print(f"Session: {session['session_id']}")
    print(f"  Objective: {session['task']['objective']}")
    print(f"  Saved: {path}")

def handover_create():
    """Create handover from current state."""
    days = list_records("days")
    if not days:
        print("No active day. Run: stallshark day start")
        return
    
    latest = sorted(days)[-1]
    day = load_record("days", latest)
    decisions = list_records("decisions")
    experiments = list_records("experiments")
    
    handover = f"""# HANDOVER — {latest}

## What I Was Trying To Do
{chr(10).join(f'- {w}' for w in day.get('work_completed', ['(none recorded)']))}

## What Changed
{len(day.get('decisions', []))} decisions made
{len(experiments)} experiments active

## What I Verified
- Git head: {_git_head()}

## What Is Currently Broken
(check from problems)

## What I Did Not Do
{chr(10).join(f'- {p}' for p in day.get('next_priorities', []))}

## Next Three Actions
{chr(10).join(f'{i+1}. {p}' for i, p in enumerate(day.get('next_priorities', ['assess state', 'prioritize', 'execute'])[:3]))}

## Relevant Commits
{_git_head()}

## Open Experiments
{chr(10).join(f'- {e}' for e in experiments)}
"""
    
    path = DATA_ROOT / "handovers" / f"handover_{latest}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(handover)
    
    print(f"Handover created: {path}")

def day_report():
    """Print daily report."""
    days = list_records("days")
    if not days:
        print("No active day.")
        return
    
    latest = sorted(days)[-1]
    day = load_record("days", latest)
    decisions = list_records("decisions")
    experiments = list_records("experiments")
    
    # Count today's expenses
    expenses_path = Path("/root/StallShark/expenses.jsonl")
    today_expenses = []
    if expenses_path.exists():
        with open(expenses_path) as f:
            for line in f:
                try:
                    e = json.loads(line.strip())
                    if e.get("date") == datetime.now().strftime("%Y-%m-%d"):
                        today_expenses.append(e)
                except:
                    continue
    
    total_expenses = sum(e.get("amount", 0) for e in today_expenses)
    
    print(f"""
{'='*60}
DAY REPORT: {day['day_id']}
{'='*60}

ORDERS:     {day.get('orders', 0)}
REVENUE:    ${day.get('revenue', 0):.2f}
FEES:       ${day.get('fees', 0):.2f}
RENDER:     ${day.get('render_cost', 0):.2f}
EXPENSES:   ${total_expenses:.2f}
PROFIT:     ${day.get('profit_estimate', 0) - total_expenses:.2f}

CHANGES:    {len(day.get('work_completed', []))} items
DECISIONS:  {len(decisions)}
SESSIONS:   {len(list_records('sessions'))}
SNAPSHOTS:  {len(list_records('snapshots'))}

EXPERIMENTS:
{chr(10).join(f'  - {e}' for e in experiments) if experiments else '  (none)'}

TOMORROW:
{chr(10).join(f'  {i+1}. {p}' for i, p in enumerate(day.get('next_priorities', ['assess state', 'prioritize', 'execute'])[:3]))}
{'='*60}
""")

def decision_add():
    """Add a decision interactively."""
    args = sys.argv[2:]
    dec = make_decision(
        subject_type=args[0] if len(args) > 0 else "general",
        subject_id=args[1] if len(args) > 1 else "none",
        question=args[2] if len(args) > 2 else "no question",
        decision=args[3] if len(args) > 3 else "no decision",
        alternatives=[],
        reason=args[4] if len(args) > 4 else "no reason",
        confidence=0.5,
    )
    path = save_record(dec, "decisions")
    print(f"Decision: {dec['decision_id']}")
    print(f"  {dec['question']}")
    print(f"  → {dec['decision']}")
    print(f"  Saved: {path}")

def experiment_add():
    """Add an experiment."""
    args = sys.argv[2:]
    exp = make_experiment(
        hypothesis=args[0] if args else "test hypothesis",
        unit_listing_id=args[1] if len(args) > 1 else "listing_001",
        control={"version": "control"},
        treatment={"version": "treatment"},
    )
    path = save_record(exp, "experiments")
    print(f"Experiment: {exp['experiment_id']}")
    print(f"  Hypothesis: {exp['hypothesis']}")
    print(f"  Saved: {path}")

def experiment_list():
    """List active experiments."""
    exps = list_records("experiments")
    print(f"Active experiments: {len(exps)}")
    for e in exps:
        exp = load_record("experiments", e)
        print(f"  {e}: {exp.get('hypothesis', '?')[:60]} [{exp.get('status', '?')}]")

COMMANDS = {
    "day": {"start": day_start, "status": day_status, "close": day_close, "report": day_report},
    "decision": {"add": decision_add},
    "experiment": {"add": experiment_add, "list": experiment_list},
    "render": {"receipt": render_receipt},
    "etsy": {"snapshot": etsy_snap},
    "session": {"record": session_record},
    "handover": {"create": handover_create},
}

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    sub = sys.argv[2] if len(sys.argv) > 2 else "status"
    
    if cmd in COMMANDS and sub in COMMANDS[cmd]:
        COMMANDS[cmd][sub]()
    else:
        print(f"Unknown command: {cmd} {sub}")
        print(__doc__)

if __name__ == "__main__":
    main()
