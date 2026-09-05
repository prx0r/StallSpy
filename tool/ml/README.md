# Cloned ML Repos — Quick Reference

## What We Have

| Repo | Path | Use |
|------|------|-----|
| **PAHF** | `tool/ml/PAHF/` | Personalized Agent from Human Feedback (Meta) — memory, pre/post feedback |
| **PPL** | `tool/ml/PPL/` | Predictive Preference Learning (NeurIPS 2025 Spotlight) — learn preferences from interventions |
| **ACL26-PersonalAlign** | `tool/ml/ACL26-PersonalAlign/` | Preference Intent Memory + Routine Intent Memory (ACL 2026) |
| **agent-budget** | `tool/ml/agent-budget/` | Complexity-based model routing BEFORE expensive call |
| **tokenwise** | `tool/ml/tokenwise/` | Task decomposition + per-step model assignment + escalation |

## How to Use Each

### PAHF (Meta) — Operator Twin Memory

```bash
cd tool/ml/PAHF
pip install -r requirements.txt

# Run shopping agent with memory
python run_agent.py --agent shopping --mem_style sql

# Run with FAISS backend
python run_agent.py --agent shopping --mem_style faiss
```

**What to adapt:** The `memory/banks.py` (SQLiteMemoryBank, FAISSMemoryBank) becomes our operator preference memory. The pre-action feedback loop (ask clarifying questions before acting) maps directly to our interview protocol.

**Key file:** `memory/banks.py` — SQL/FAISS memory backends
**Key file:** `agents/base.py` — BasePersonalAgent with memory + feedback loop

### PPL (NeurIPS 2025 Spotlight) — Preference Model

```bash
cd tool/ml/PPL
conda create -n ppl python=3.7
pip install -r requirements.txt
pip install -e .

# Run toy experiment
python ppl/experiments/metadrive/train_ppl_metadrive.py --toy_env
```

**What to adapt:** The trajectory predictor learns to predict human preference outcomes from interventions. Maps to our "feelings → activity → outcome" pipeline. The DPO-like preference loss is the key innovation.

**Key file:** `ppl/experiments/metadrive/train_ppl_metadrive.py` — training script

### ACL26-PersonalAlign — Hierarchical Memory

```bash
cd tool/ml/ACL26-PersonalAlign
conda create -n personal python=3.10
pip install -r requirements.txt

# Evaluate
sh scripts/execution/eval_qwen3vl.sh
```

**What to adapt:** The HIM-Agent (Hierarchical Intent Memory) separates:
- **Preference Intent Memory** — stable preferences (what the human values)
- **Routine Intent Memory** — recurring patterns (what the human typically does)

This is exactly our operator twin's structure: stable preferences + current objectives + belief graph.

**Key file:** `src/` — HIM-Agent implementation
**Key file:** `skills/` — reusable skill extraction

### agent-budget — Smart Model Routing

```bash
cd tool/ml/agent-budget
pip install agent-budget

# Quick test
python -c "
from agent_budget import BudgetTracker, ModelRouter
tracker = BudgetTracker(budget_usd=5.0)
router = ModelRouter(tracker=tracker)
decision = router.route('What is 2+2?')
print(f'→ {decision.complexity.value} → {decision.resolved_model.model_id}')
"
```

**What to adapt:** The complexity classifier (LOW/MEDIUM/HIGH) routes before the expensive call. 7 heuristic signals: token count, keywords, tools, conversation history, code blocks, questions.

**Key file:** `agent_budget/router.py` — ModelRouter with complexity classification
**Key file:** `agent_budget/tracker.py` — BudgetTracker with warning/pause states

### tokenwise — Task Decomposition + Escalation

```bash
cd tool/ml/tokenwise
pip install tokenwise-llm

# Route a query
tokenwise route "Write a haiku about Python"

# Route with budget
tokenwise route "Debug this segfault" --strategy best_quality --budget 0.05

# Plan and execute
tokenwise plan "Build a REST API" --budget 0.50 --execute
```

**What to adapt:** Task decomposition into subtasks with per-step model assignment. Auto-downgrades expensive steps if over budget. Escalates to stronger models on failure.

**Key file:** `tokenwise/planner.py` — task decomposition
**Key file:** `tokenwise/router.py` — tiered escalation

## Integration Plan

| Week | Action |
|------|--------|
| 1 | Wire `agent-budget` into `tool/smart_router.py` — replace our simple router |
| 2 | Adapt PAHF memory system for operator twin preference storage |
| 3 | Use PPL trajectory predictor for "feelings → outcome" modeling |
| 4 | Use PersonalAlign HIM-Agent for operator memory architecture |
| 5 | Use tokenwise for multi-step task planning with budget enforcement |
