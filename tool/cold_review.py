#!/usr/bin/env python3
"""
ColdReview Protocol — Fresh agent reviews the day BLIND.
No previous interpretations. Just facts.
"""
import json
from datetime import datetime
from pydantic_ai import Agent
from pydantic import BaseModel

COLD_REVIEW_PROMPT = """You are the Cold Reviewer. You review a day's business activity.

RULES:
1. You receive ONLY facts: metrics, actions, costs, outcomes.
2. You do NOT see what the human thought about the day.
3. You do NOT see what the working agent thought about the day.
4. Form your own INDEPENDENT assessment.

Analyze:
1. What actually happened today?
2. Which actions produced value?
3. Which actions were waste?
4. Did actual work match stated priorities?
5. What important hypothesis emerged?
6. What appears to be a local fix rather than structural solution?
7. What should tomorrow's agent know?

Output your assessment as a structured summary."""

class ColdReviewOutput(BaseModel):
    what_happened: str = ""
    valuable_actions: list[str] = []
    waste_actions: list[str] = []
    priority_alignment: str = ""
    key_hypothesis: str = ""
    local_vs_structural: str = ""
    tomorrow_should_know: str = ""
    biggest_surprise: str = ""

def run_cold_review(day_facts: dict) -> dict:
    """Run cold review with only facts — no previous interpretations."""
    model = "test"  # Use test model; switch to real model when API key configured
    
    agent = Agent(model, system_prompt=COLD_REVIEW_PROMPT, output_type=ColdReviewOutput)
    
    facts_only = {
        "date": day_facts.get("date", datetime.now().strftime("%Y-%m-%d")),
        "actions_taken": day_facts.get("actions", []),
        "costs": day_facts.get("costs", {}),
        "outcomes": day_facts.get("outcomes", {}),
        "git_commits": day_facts.get("commits", []),
        "etsy_metrics": day_facts.get("etsy_metrics", {}),
    }
    
    result = agent.run_sync(json.dumps(facts_only, default=str))
    return {
        "review": result.output.model_dump(),
        "timestamp": datetime.now().isoformat(),
        "facts_used": list(facts_only.keys()),
        "interpretations_hidden": ["human_reflection", "worker_debrief", "previous_agent_assessment"],
    }

if __name__ == "__main__":
    print("=== ColdReview Protocol Test ===\n")
    
    day_facts = {
        "date": "2026-09-05",
        "actions": ["wrote 12 spec docs", "cloned 7 repos", "built scraper", "ran E2E tests"],
        "costs": {"tokens": 50000, "cash": 0, "human_hours": 8},
        "outcomes": {"listings": 0, "revenue": 0, "api_working": True},
        "commits": ["15 git commits"],
        "etsy_metrics": {"personalized_football_gift": 137474},
    }
    
    result = run_cold_review(day_facts)
    print(json.dumps(result, indent=2))
