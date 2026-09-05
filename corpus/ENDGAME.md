# The Endgame — What to Build Now

**Date:** 5 September 2026

---

## The $5/Day Agent

Allocate $5/day. Agent operates the business with smart controls:

```
TOTAL DAILY BUDGET: $5.00

├── Free tier (mimo-v2.5): unlimited
│   └── Low-value tasks: research, drafting, summarization, routine queries
│
├── Cheap tier (groq/llama-3.3): $1.50/day
│   └── Medium tasks: SEO analysis, listing optimization, competitor research
│
├── Strong tier (claude/gpt-4o): $2.00/day
│   └── High-value tasks: strategy decisions, complex reasoning, creative generation
│
├── GPU/Generation: $1.50/day
│   └── H3 video generation, image processing
│
└── Reserve: $0.00 (buffer)
```

### Smart Routing (from existing tools)

| Tool | What It Does | Relevance |
|------|-------------|-----------|
| **Tidus** | 5-stage model selection: constraints → guardrails → tier → budget → scoring | We can adopt this routing logic |
| **agent-budget** | Complexity classifier routes BEFORE expensive call | Exactly what BATS does |
| **TokenWise** | Task decomposition + per-step model assignment + escalation | Good for multi-step workflows |
| **Treasury** | Pre-flight cost forecasting, cheapest-first cascade | Good for budget planning |
| **TokSuan** | Context compression + routing + budget enforcement | Good for long sessions |

### What We Can Build Today

```python
# stallsypy/tool/smart_router.py

class StallSpyRouter:
    """Routes tasks to cheapest capable model within daily budget."""
    
    TIERS = {
        "free": {"models": ["mimo-v2.5"], "cost_per_1k": 0.0},
        "cheap": {"models": ["groq/llama-3.3-70b"], "cost_per_1k": 0.00059},
        "strong": {"models": ["claude-3.5-sonnet"], "cost_per_1k": 0.003},
    }
    
    TASK_COMPLEXITY = {
        "research": "free",
        "draft": "free",
        "summarize": "free",
        "seo_analysis": "cheap",
        "listing_optimization": "cheap",
        "competitor_analysis": "cheap",
        "strategy_decision": "strong",
        "creative_generation": "strong",
        "complex_reasoning": "strong",
    }
    
    def route(self, task_type: str, daily_budget_remaining: float) -> str:
        preferred = self.TASK_COMPLEXITY.get(task_type, "free")
        
        if daily_budget_remaining < 0.50:
            return "free"  # Emergency: only free tier
        elif daily_budget_remaining < 2.00:
            return "free" if preferred == "strong" else preferred
        else:
            return preferred
```

---

## The Operator Twin — Buildable Now

### Architecture

```text
Day 1-7:   L0 Recorder (observe only)
Day 8-14:  L1 Shadow Twin (predict, never act)
Day 15-30: L2 Adviser (recommend, human decides)
Day 31+:   L3 Delegated Reversible (cheap actions)
```

### The P/A/H System

Every interview produces three answers:

```
P — Predicted Human (agent predicts what human will say)
A — Agent's Own Judgment (independent recommendation)
H — Actual Human (what human actually says)
```

### Implementation

```python
# stallsypy/tool/operator_twin.py

class OperatorTwin:
    def __init__(self):
        self.preferences = {}  # learned from P/A/H data
        self.risk_preference = 0.5  # starts neutral
        self.calibration = []  # history of predictions
    
    def predict(self, question_objective: str, business_state: dict) -> dict:
        """Predict what the human would say."""
        # Start with simple heuristics
        # Upgrade to ML model after 14+ days of data
        
        prediction = {
            "goal_priority": self._predict_goals(business_state),
            "risk_tolerance": self._predict_risk(business_state),
            "time_allocation": self._predict_allocation(business_state),
            "confidence": self._estimate_confidence(business_state),
        }
        
        self.calibration.append({
            "question_objective": question_objective,
            "prediction": prediction,
            "timestamp": time.time(),
        })
        
        return prediction
    
    def update(self, prediction: dict, actual: dict):
        """Update model after human answers."""
        error = self._compute_error(prediction, actual)
        self._adjust_weights(error)
    
    def _predict_goals(self, state: dict) -> dict:
        """Simple heuristic: predict based on current business state."""
        if state.get("sales", 0) == 0:
            return {"primary": "first_sale", "confidence": 0.7}
        elif state.get("days_since_launch", 0) > 30:
            return {"primary": "scale_success", "confidence": 0.6}
        else:
            return {"primary": "validate_concept", "confidence": 0.5}
```

### Key Research Repos for This

| Repo | What It Does | Can We Use |
|------|-------------|:----------:|
| **facebookresearch/PAHF** | Personalized Agent from Human Feedback — SQL/FAISS memory, pre-action clarification, post-action learning | Yes — adapt memory system |
| **metadriverse/PPL** | Predictive Preference Learning — learns preferences from interventions, not just comparisons | Yes — adapt preference model |
| **PatrickG1014/HPL** | Hierarchical Preference Learning — trajectory + step level preferences for long-horizon agents | Yes — for multi-day planning |
| **iLearn-Lab/ACL26-PersonalAlign** | Hierarchical implicit intent alignment — Preference Intent Memory + Routine Intent Memory | Yes — best memory architecture |
| **zzh237/AgentBake** | Drop-in personalization layer — 103/110 agents showed positive uplift, 1.4ms/round overhead | Yes — lightweight integration |
| **Avinandan22/PEP** | Cold-start preference elicitation — 80.8% alignment with 3-5x fewer interactions | Yes — for Day 1 bootstrapping |

### The PAHF Memory System (from Meta)

```python
# Adapted from facebookresearch/PAHF

class OperatorMemory:
    """Stores operator preferences with temporal awareness."""
    
    def __init__(self, backend="sqlite"):
        self.backend = backend  # sqlite or faiss
        self.preferences = []
    
    def store_preference(self, context: str, preference: str, timestamp: float):
        """Store a preference observation."""
        self.preferences.append({
            "context": context,
            "preference": preference,
            "timestamp": timestamp,
        })
    
    def retrieve_similar(self, current_context: str, k: int = 5) -> list:
        """Find similar past contexts."""
        # Use embedding similarity or keyword matching
        return sorted(
            self.preferences,
            key=lambda p: self._similarity(current_context, p["context"]),
            reverse=True
        )[:k]
    
    def predict_preference(self, current_context: str) -> str:
        """Predict preference based on similar past contexts."""
        similar = self.retrieve_similar(current_context)
        if not similar:
            return "unknown"
        # Weight by recency and similarity
        return self._aggregate(similar)
```

---

## The Problem → Experiment → Protocol Pipeline

### Buildable Now

```python
# stallsypy/tool/experiment_pipeline.py

class ExperimentPipeline:
    def __init__(self, corpus, bats, operator_twin):
        self.corpus = corpus
        self.bats = bats
        self.operator_twin = operator_twin
    
    def detect_problem(self, metrics: dict, human_signal: str = None) -> dict:
        """Detect problems from metrics and human input."""
        problems = []
        
        # Metric-based detection
        if metrics.get("conversion_rate", 0) < 0.02:
            problems.append({
                "type": "low_conversion",
                "severity": "high",
                "source": "metric"
            })
        
        # Human signal detection
        if human_signal:
            if "worried" in human_signal.lower() or "stuck" in human_signal.lower():
                problems.append({
                    "type": "operator_uncertainty",
                    "severity": "medium",
                    "source": "human"
                })
        
        return problems
    
    def design_experiment(self, problem: dict) -> dict:
        """Design experiment to address problem."""
        return {
            "problem_id": problem["type"],
            "hypothesis": f"Addressing {problem['type']} will improve metrics",
            "design": "before_after",
            "budget": self.bats.allocate(2.0),  # $2 for this experiment
            "timeline": "14_days",
            "success_metric": "conversion_rate",
            "minimum_effect": 0.20,
        }
    
    def measure_result(self, experiment: dict, before: dict, after: dict) -> dict:
        """Measure experiment results."""
        effect = {}
        for metric in experiment.get("metrics", []):
            b = before.get(metric, 0)
            a = after.get(metric, 0)
            if b > 0:
                effect[metric] = (a - b) / b
            else:
                effect[metric] = a
        
        return {
            "experiment": experiment,
            "effect": effect,
            "status": "win" if effect.get("conversion_rate", 0) > 0.15 else "loss",
        }
    
    def store_protocol(self, experiment: dict, result: dict):
        """Store validated protocol for reuse."""
        if result["status"] == "win":
            self.corpus.store_lesson({
                "claim": experiment["hypothesis"],
                "evidence": [result],
                "confidence": 0.7,
                "applicable_when": experiment.get("conditions", []),
            })
```

---

## Token Tracking — Buildable Now

```python
# stallsypy/tool/token_tracker.py

import json
from datetime import datetime
from pathlib import Path

class TokenTracker:
    def __init__(self, log_path="operations/token_usage.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
    
    def record(self, model: str, input_tokens: int, output_tokens: int, 
               cost: float, task: str, agent: str = ""):
        """Record a model call."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "cost_usd": cost,
            "task": task,
            "agent": agent,
        }
        
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
        
        return entry
    
    def daily_summary(self, date: str = None) -> dict:
        """Get daily token usage summary."""
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        summary = {"total_cost": 0, "total_tokens": 0, "by_model": {}, "by_task": {}}
        
        if self.log_path.exists():
            with open(self.log_path) as f:
                for line in f:
                    entry = json.loads(line.strip())
                    if entry.get("date") == date:
                        summary["total_cost"] += entry["cost_usd"]
                        summary["total_tokens"] += entry["total_tokens"]
                        
                        model = entry["model"]
                        summary["by_model"][model] = summary["by_model"].get(model, 0) + entry["total_tokens"]
                        
                        task = entry["task"]
                        summary["by_task"][task] = summary["by_task"].get(task, 0) + entry["total_tokens"]
        
        return summary
    
    def efficiency_report(self, days: int = 7) -> dict:
        """Report on token efficiency over time."""
        # Analyze cost per outcome, ROI per task type, etc.
        pass
```

---

## The Daily $5 Agent Budget — Concrete Plan

### Day 1-7: Calibration Phase

```
Budget: $5/day total
├── Free model: unlimited (all tasks)
├── Cheap model: $1.50/day (SEO, research)
├── Strong model: $2.00/day (strategy, creative)
├── GPU: $1.50/day (generation)

Daily tasks:
├── Morning interview (operator twin predicts → human answers)
├── Etsy research (free model)
├── Listing creation (free model)
├── Content generation (free model)
├── Experiment tracking (free model)
├── Evening reflection (free model)
└── Weekly synthesis (cheap model)
```

### Day 8-14: Shadow Twin Phase

```
Same budget but:
├── Agent predicts every human answer
├── Divergence tracked
├── Accuracy measured
├── Model confidence calibrated
└── Human interaction optimized
```

### Day 15-30: Adviser Phase

```
Budget reallocates based on learned value:
├── If human outperforms agent on concept selection:
│   └── Agent does research, human picks concepts
├── If agent outperforms on SEO:
│   └── Agent handles all SEO autonomously
├── If human is bottleneck on speed:
│   └── Agent gets L3 for reversible actions
└── Budget shifts toward high-value tasks
```

### Day 31+: Bounded Operator Phase

```
Agent earns autonomy per decision class:
├── Research: AUTO (free model)
├── Draft creation: AUTO (free model)
├── Listing updates: AUTO (cheap model)
├── Price changes: PROPOSE (strong model)
├── New products: APPROVE (human)
└── Budget: $5/day → $10/day if ROI positive
```

---

## What We Build This Week

| Task | Tool | Time |
|------|------|------|
| Token tracker | `tool/token_tracker.py` | 2h |
| Smart router | `tool/smart_router.py` | 3h |
| Operator twin v0.1 | `tool/operator_twin.py` | 4h |
| Morning record with budget | `tool/morning_record.py` (update) | 1h |
| Expense logger with token tracking | `tool/log_expense.py` (update) | 1h |
| First 5 Game Winner listings | Etsy API | 4h |
| Daily content pipeline test | `tool/auto_content.py` | 2h |

**Total: ~17h**

---

## The Endgame Vision

```
YEAR 1: $5/day agent, 1 brand, learning
YEAR 2: $15/day agent, 3 brands, protocols emerging
YEAR 3: $50/day agent, 5 brands, delegated departments
YEAR 4: $200/day agent, 10+ brands, autonomous operation
YEAR 5: $500/day agent, portfolio, corporate structure
```

The corpus grows every day. The operator twin gets more accurate. The economic critic gets better predictions. The protocols compound. The corporate structure emerges from protocols, not org charts.

**The question is not "can AI run a business?"**

**The question is "how much budget does the AI need to run a business at each stage of growth?"**

And we're about to find out.

---

*Start with $5/day. Track everything. Let the data tell us when to scale.*
