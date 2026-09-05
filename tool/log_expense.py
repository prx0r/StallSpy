#!/usr/bin/env python3
"""Quick expense logger. Usage: python3 log_expense.py 8.13 gpu "Ran H3 generation for Game Winner" """

import sys
import os
import json
from datetime import datetime

EXPENSE_FILE = "/root/StallSpy/expenses.jsonl"

CATEGORIES = {
    "gpu": "GPU rental (Vast.ai / RunPod)",
    "ai": "AI model API calls",
    "domain": "Domain registration",
    "pod": "Print-on-demand manufacturing",
    "shipping": "Shipping costs",
    "etsy": "Etsy listing fees / ads",
    "software": "Software subscriptions",
    "tool": "Tool development costs",
    "content": "Content creation costs",
    "other": "Other expenses",
}

def log(amount, category, description, project="general"):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "timestamp": datetime.now().isoformat(),
        "amount": float(amount),
        "category": category,
        "description": description,
        "project": project,
    }
    with open(EXPENSE_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    
    # Update daily total
    today = entry["date"]
    total = 0
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                try:
                    e = json.loads(line.strip())
                    if e.get("date") == today:
                        total += e.get("amount", 0)
                except:
                    continue
    
    print(f"Logged: ${float(amount):.2f} ({category}: {description})")
    print(f"Today's total: ${total:.2f}")

def show_today():
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0
    entries = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                try:
                    e = json.loads(line.strip())
                    if e.get("date") == today:
                        entries.append(e)
                        total += e.get("amount", 0)
                except:
                    continue
    
    print(f"Expenses for {today}:")
    for e in entries:
        print(f"  ${e['amount']:.2f} — {e.get('category', '?')}: {e.get('description', '?')}")
    print(f"  Total: ${total:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "today":
        show_today()
    elif sys.argv[1] == "help":
        print("Usage:")
        print("  python3 log_expense.py 8.13 gpu \"Ran H3 generation\"")
        print("  python3 log_expense.py 0.50 pod \"Ordered mug sample\"")
        print("  python3 log_expense.py today  # show today's expenses")
        print(f"\nCategories: {', '.join(CATEGORIES.keys())}")
    else:
        amount = float(sys.argv[1])
        category = sys.argv[2] if len(sys.argv) > 2 else "other"
        desc = sys.argv[3] if len(sys.argv) > 3 else "no description"
        project = sys.argv[4] if len(sys.argv) > 4 else "general"
        log(amount, category, desc, project)
