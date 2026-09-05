#!/usr/bin/env python3
"""
Daily Content Engine — distills actions into log, video script, and TL;DR.

Sources:
  - git commits (what we did)
  - Etsy API (store metrics)
  - expense log (what we spent)
  - manual notes (optional)

Outputs:
  - logs/YYYY-MM-DD_full.md      (granular agent-readable log)
  - logs/YYYY-MM-DD_video.md     (YouTube short script)
  - logs/YYYY-MM-DD_tldr.md      (human summary)
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# ── Config ──────────────────────────────────────────────────────────────

REPO = "/root/StallSpy"
LOG_DIR = os.path.join(REPO, "logs")
EXPENSE_FILE = os.path.join(REPO, "expenses.jsonl")

ETSY_API_KEY = os.environ.get("ETSY_API_KEY", "")
ETSY_SHARED_SECRET = os.environ.get("ETSY_SHARED_SECRET", "mbb9u861jg")
ETSY_BASE = "https://openapi.etsy.com/v3/application"


# ── Git Collection ──────────────────────────────────────────────────────

def get_git_log(date_str=None):
    """Get git commits for a given date (YYYY-MM-DD)."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    try:
        result = subprocess.run(
            ["git", "log", f"--after={date_str} 00:00", f"--before={date_str} 23:59",
             "--pretty=format:%H|%s|%ai", "--all"],
            capture_output=True, text=True, cwd=REPO, timeout=10
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if "|" in line:
                parts = line.split("|", 2)
                commits.append({
                    "hash": parts[0][:8],
                    "message": parts[1],
                    "timestamp": parts[2] if len(parts) > 2 else ""
                })
        return commits
    except Exception as e:
        return [{"hash": "?", "message": f"Git error: {e}", "timestamp": ""}]


def get_git_diff_stat(date_str=None):
    """Get files changed today."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    try:
        result = subprocess.run(
            ["git", "diff", "--stat", f"HEAD~20..HEAD"],
            capture_output=True, text=True, cwd=REPO, timeout=10
        )
        return result.stdout.strip()
    except:
        return ""


# ── Etsy API Collection ────────────────────────────────────────────────

def etsy_get(path, params=None):
    """Call Etsy API."""
    from urllib.parse import urlencode
    url = f"{ETSY_BASE}{path}"
    if params:
        url += "?" + urlencode(params)
    req = Request(url, headers={"x-api-key": f"{ETSY_API_KEY}:{ETSY_SHARED_SECRET}"})
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        return {"error": str(e)}


def get_etsy_store_metrics():
    """Pull current store metrics from Etsy API."""
    # Search for our listings to get basic metrics
    metrics = {"queries": {}}
    
    keywords = [
        "personalized football gift",
        "dogcasso",
        "personalized birthday video",
    ]
    
    for kw in keywords:
        data = etsy_get("/listings/active", {
            "keywords": kw,
            "limit": 5,
            "fields": "listing_id,title,price,num_favorers,views,url"
        })
        if "results" in data:
            metrics["queries"][kw] = {
                "total_results": data.get("count", 0),
                "top_listings": [{
                    "id": r["listing_id"],
                    "title": r["title"][:60],
                    "price": r["price"]["amount"] / r["price"]["divisor"],
                    "favorites": r.get("num_favorers", 0),
                    "views": r.get("views", 0),
                } for r in data["results"][:3]]
            }
    
    return metrics


# ── Expense Collection ─────────────────────────────────────────────────

def get_today_expenses(date_str=None):
    """Read expenses from JSONL log."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if entry.get("date") == date_str:
                        expenses.append(entry)
                except:
                    continue
    return expenses


def log_expense(amount, category, description, project="general"):
    """Log an expense."""
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "timestamp": datetime.now().isoformat(),
        "amount": amount,
        "category": category,
        "description": description,
        "project": project,
    }
    with open(EXPENSE_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


# ── Content Generation ─────────────────────────────────────────────────

def generate_full_log(commits, metrics, expenses, day_number, notes=""):
    """Generate granular agent-readable log using 6-part structure."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    total_expenses = sum(e.get("amount", 0) for e in expenses)
    
    lines = []
    lines.append(f"# Day {day_number} — {date_str}")
    lines.append("")
    
    # 6-part structure (from corpus thesis)
    lines.append("## STATE")
    lines.append("")
    lines.append(f"- Expenses today: ${total_expenses:.2f}")
    lines.append(f"- Commits: {len(commits)}")
    for kw, data in metrics.get("queries", {}).items():
        lines.append(f"- \"{kw}\": {data['total_results']} results on Etsy")
    lines.append("")
    
    lines.append("## BELIEF")
    lines.append("")
    lines.append("- (what did we think was true today?)")
    lines.append("")
    
    lines.append("## ACTION")
    lines.append("")
    if commits:
        for c in commits:
            lines.append(f"- `{c['hash']}` {c['message']}")
    else:
        lines.append("- No commits today")
    for e in expenses:
        lines.append(f"- Spent ${e['amount']:.2f} on {e.get('category', '?')}: {e.get('description', '?')}")
    lines.append("")
    
    lines.append("## COST")
    lines.append("")
    lines.append(f"- Total: ${total_expenses:.2f}")
    for e in expenses:
        lines.append(f"  - ${e['amount']:.2f} — {e.get('description', '?')} ({e.get('category', '?')})")
    lines.append("")
    
    lines.append("## OUTCOME")
    lines.append("")
    lines.append("- (what happened as a result?)")
    lines.append("")
    
    lines.append("## UPDATE")
    lines.append("")
    lines.append("- (what do we now believe?)")
    lines.append("")
    
    # Manual notes
    if notes:
        lines.append("## Notes")
        lines.append("")
        lines.append(notes)
        lines.append("")
    
    # Event classification (for agent ingestion)
    lines.append("---")
    lines.append("")
    lines.append("## Event Classification (machine-readable)")
    lines.append("")
    lines.append("### Money events")
    for e in expenses:
        lines.append(f"- expense: ${e['amount']:.2f} {e.get('category', '?')}")
    lines.append("")
    
    lines.append("### Development events")
    for c in commits:
        msg = c["message"].lower()
        if "listing" in msg or "etsy" in msg:
            lines.append(f"- listing_action: {c['message']}")
        elif "scrape" in msg or "data" in msg:
            lines.append(f"- data_collection: {c['message']}")
        elif "fix" in msg or "bug" in msg:
            lines.append(f"- bug_fix: {c['message']}")
        elif "feat" in msg or "add" in msg:
            lines.append(f"- feature: {c['message']}")
        else:
            lines.append(f"- general: {c['message']}")
    lines.append("")
    
    lines.append("### Hypothesis updates")
    lines.append("- (none logged today)")
    lines.append("")
    
    # Etsy metrics (detailed)
    lines.append("## Etsy Metrics (detailed)")
    lines.append("")
    for kw, data in metrics.get("queries", {}).items():
        lines.append(f"### \"{kw}\"")
        lines.append(f"- Total results: {data['total_results']}")
        for listing in data.get("top_listings", []):
            lines.append(f"  - #{listing['id']}: {listing['title']} — ${listing['price']:.2f}, {listing['favorites']} favs, {listing['views']} views")
    lines.append("")
    
    return "\n".join(lines)


def generate_video_script(commits, metrics, expenses, day_number):
    """Generate YouTube short script (30-90 sec)."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    total_expenses = sum(e.get("amount", 0) for e in expenses)
    
    # Find most interesting commit
    interesting = ""
    for c in commits:
        msg = c["message"].lower()
        if any(w in msg for w in ["listing", "sale", "launch", "fix", "breakthrough", "first", "new"]):
            interesting = c["message"]
            break
    if not interesting and commits:
        interesting = commits[0]["message"]
    
    # Find top market signal
    market_signal = ""
    for kw, data in metrics.get("queries", {}).items():
        if data.get("total_results"):
            market_signal = f"\"{kw}\" has {data['total_results']} results — that's the market we're entering"
            break
    
    script = f"""# Day {day_number} — {date_str}

## HOOK (3 sec)
"""
    
    if total_expenses > 0:
        script += f'"Day {day_number}. I spent ${total_expenses:.2f} today."\n'
    else:
        script += f'"Day {day_number} of the £0 to £1M experiment."\n'
    
    script += f"""
## MONEY
- Spent today: ${total_expenses:.2f}
- Revenue today: $0
- Days in: {day_number}

## WHAT I DID
"""
    
    if commits:
        for c in commits[:3]:
            script += f"- {c['message']}\n"
    else:
        script += "- Planning day\n"
    
    script += f"""
## MARKET
"""
    if market_signal:
        script += f"- {market_signal}\n"
    
    script += f"""
## INSIGHT
"""
    
    if commits:
        script += f'"Every commit is a hypothesis. {len(commits)} hypotheses tested today."\n'
    else:
        script += '"Some days you plan. Planning is testing."\n'
    
    script += f"""
## TOMORROW
- Continue building
- Day {day_number + 1} drops tomorrow

#£0to1M #Etsy #AIBusiness #BuildInPublic
"""
    
    return script


def generate_tldr(commits, metrics, expenses, day_number):
    """Generate human-readable TL;DR."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    total_expenses = sum(e.get("amount", 0) for e in expenses)
    
    # Count commits by type
    types = {"listing": 0, "data": 0, "fix": 0, "feature": 0, "other": 0}
    for c in commits:
        msg = c["message"].lower()
        if "listing" in msg or "etsy" in msg:
            types["listing"] += 1
        elif "scrape" in msg or "data" in msg:
            types["data"] += 1
        elif "fix" in msg:
            types["fix"] += 1
        elif "feat" in msg or "add" in msg:
            types["feature"] += 1
        else:
            types["other"] += 1
    
    tldr = f"""# Day {day_number} TL;DR — {date_str}

**Spent:** ${total_expenses:.2f} | **Revenue:** $0 | **Commits:** {len(commits)}

**What happened:**
"""
    
    if commits:
        for c in commits[:3]:
            tldr += f"- {c['message']}\n"
        if len(commits) > 3:
            tldr += f"- ...and {len(commits)-3} more\n"
    else:
        tldr += "- Planning day (no commits)\n"
    
    # Top market signal
    for kw, data in metrics.get("queries", {}).items():
        if data.get("total_results"):
            tldr += f"\n**Market:** \"{kw}\" has {data['total_results']} results on Etsy\n"
            break
    
    tldr += f"\n**Lesson:** Building in public. Day {day_number} of the £0 → £1M experiment.\n"
    
    return tldr


# ── Main ────────────────────────────────────────────────────────────────

def run(date_str=None, day_number=None, notes="", morning_record=None):
    """Generate all content for a given day."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    if not day_number:
        day_number = 1
    
    print(f"Collecting data for Day {day_number} ({date_str})...")
    
    # Collect
    commits = get_git_log(date_str)
    metrics = get_etsy_store_metrics()
    expenses = get_today_expenses(date_str)
    
    print(f"  Git: {len(commits)} commits")
    print(f"  Etsy: {len(metrics.get('queries', {}))} keyword queries")
    print(f"  Expenses: {len(expenses)} entries")
    
    # Generate
    os.makedirs(LOG_DIR, exist_ok=True)
    
    full_log = generate_full_log(commits, metrics, expenses, day_number, notes)
    video_script = generate_video_script(commits, metrics, expenses, day_number)
    tldr = generate_tldr(commits, metrics, expenses, day_number)
    
    # Write
    prefix = os.path.join(LOG_DIR, date_str)
    
    with open(f"{prefix}_full.md", "w") as f:
        f.write(full_log)
    print(f"  Wrote: {prefix}_full.md")
    
    with open(f"{prefix}_video.md", "w") as f:
        f.write(video_script)
    print(f"  Wrote: {prefix}_video.md")
    
    with open(f"{prefix}_tldr.md", "w") as f:
        f.write(tldr)
    print(f"  Wrote: {prefix}_tldr.md")
    
    # Also write a combined daily ledger entry (JSON)
    ledger_entry = {
        "date": date_str,
        "day_number": day_number,
        "timestamp": datetime.now().isoformat(),
        "commits": commits,
        "expenses": expenses,
        "etsy_metrics": metrics,
        "expense_total": sum(e.get("amount", 0) for e in expenses),
    }
    
    ledger_path = os.path.join(REPO, "ledger.jsonl")
    with open(ledger_path, "a") as f:
        f.write(json.dumps(ledger_entry) + "\n")
    print(f"  Wrote: ledger.jsonl")
    
    print(f"\nDone. Generated 3 files + 1 ledger entry.")
    return full_log, video_script, tldr


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Daily Content Engine")
    parser.add_argument("--date", help="Date to generate for (YYYY-MM-DD)")
    parser.add_argument("--day", type=int, default=1, help="Day number in experiment")
    parser.add_argument("--notes", default="", help="Manual notes for the day")
    parser.add_argument("--morning", default="", help="Morning record: goal, belief, bet, success, kill conditions")
    parser.add_argument("--expense", nargs=3, metavar=("AMOUNT", "CATEGORY", "DESC"),
                        help="Log an expense before generating")
    
    args = parser.parse_args()
    
    if args.expense:
        amount = float(args.expense[0])
        category = args.expense[1]
        desc = args.expense[2]
        log_expense(amount, category, desc)
        print(f"Logged expense: ${amount:.2f} ({category}: {desc})")
    
    run(date_str=args.date, day_number=args.day, notes=args.notes, morning_record=args.morning)
