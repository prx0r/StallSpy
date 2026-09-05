# Commerce Trajectory Corpus v1 — Machine Course

**Date:** 5 September 2026
**Status:** Architecture spec — the primary asset is the corpus, not the stores

---

## The Insight

The future product is not "Tom's Etsy logs."

It is:

> **Commerce Trajectory Corpus v1 — a replayable, machine-readable record of taking AI-native commerce businesses from hypothesis → launch → optimization → scale, including every state, action, cost, outcome, failed belief and validated playbook.**

The killer property is that an agent can use it as **experience**.

Not: "Here are some tips about Etsy."

But: "Here are 14,832 historical situations where an operator faced a particular state, chose an action, and observed what happened next."

---

## Canonical Architecture

Don't make the blog the database.

```text
IMMUTABLE EVENTS
      ↓
CURRENT STATE / DAILY SNAPSHIPS
      ↓
EXPERIMENTS + EPISODES
      ↓
LESSONS / PLAYBOOKS
      ↓
AGENT EVALS
      ↓
BLOG / YOUTUBE / PUBLIC DATA
```

### Standards

- **Croissant 1.1** — overall dataset manifest, provenance and usage policies
- **JSON Schema 2020-12** — validation of every record type
- **UUIDv7** — sortable unique identifiers
- **JSONL** — canonical append-only streams
- **Parquet** — analytics/large metric tables
- **SQLite/DuckDB** — turnkey querying for agents
- **W3C PROV** — entity/activity/agent lineage
- **ODRL** — machine-readable allowed/prohibited uses

---

## The Record Envelope (Mandatory)

Every record gets this envelope:

```json
{
  "id": "019c...",
  "schema": "decision",
  "schema_version": "1.0.0",
  "occurred_at": "2026-09-06T10:31:12Z",
  "observed_at": "2026-09-06T10:31:14Z",
  "recorded_at": "2026-09-06T10:31:15Z",
  "project_id": "proj_mythicbee",
  "brand_id": "brand_mythicbee",
  "store_id": "store_etsy_mythicbee",
  "actor": {
    "type": "human|agent|automation|customer|platform",
    "id": "actor_tom"
  },
  "correlation_id": "019c...",
  "parent_ids": [],
  "supersedes_id": null,
  "source": {
    "type": "manual|system|git|etsy_export|analytics|api|model|supplier",
    "source_ref": null
  },
  "provenance": {
    "derived_from": [],
    "content_sha256": "..."
  },
  "rights": {
    "classification": "first_party|licensed|platform_restricted|derived|public_reference",
    "agent_internal_use": true,
    "commercial_redistribution": true,
    "public_release": false,
    "contains_personal_data": false
  },
  "quality": {
    "confidence": 0.95,
    "verified": true
  },
  "data": {}
}
```

**Never modify a historical event.** If something was wrong: new event → correction_of / supersedes_id → old event.

---

## Schema: `episode`

The single most important schema. STATE → GOAL → BELIEF → ACTION → OUTCOME → UPDATED BELIEF.

```json
{
  "episode_id": "ep_...",
  "started_at": "...",
  "ended_at": "...",
  "situation": {
    "business_age_days": 19,
    "brand": "GameWinner",
    "channel": "etsy",
    "market": "US",
    "cash_available_usd": 82.40,
    "cumulative_revenue_usd": 114.00,
    "cumulative_profit_usd": 31.82
  },
  "goal": {
    "primary": "increase conversion",
    "target_metric": "listing_conversion_rate",
    "target_change": 0.20
  },
  "constraints": ["budget_under_10_usd", "no_new_template", "24_hours"],
  "belief_before": {
    "claim": "Showing source photo beside generated result will increase buyer trust",
    "confidence": 0.68
  },
  "evidence_available_at_decision": ["obs_123", "review_theme_88", "experiment_21"],
  "options_considered": ["reduce_price", "change_thumbnail", "show_before_after", "add_more_examples"],
  "decision": "show_before_after",
  "action_ids": ["act_91"],
  "expected_outcome": {
    "metric": "listing_conversion_rate",
    "direction": "increase",
    "minimum_effect": 0.10
  },
  "observation_window": {"start": "...", "end": "..."},
  "outcome": {
    "before": 0.031,
    "after": 0.042,
    "relative_change": 0.354,
    "revenue_change_usd": 41.20
  },
  "causal_assessment": {
    "strength": "weak|moderate|strong",
    "confounders": [],
    "confidence": 0.73
  },
  "belief_after": {
    "claim": "Before/after proof materially reduces trust friction for AI personalization",
    "confidence": 0.81
  },
  "transfer": {
    "likely_generalizable_to": ["custom_portraits", "personalized_video", "generative_gifts"],
    "unlikely_generalizable_to": []
  },
  "reward": {
    "profit_delta": 12.43,
    "conversion_delta": 0.011,
    "human_minutes": 18,
    "compute_cost_usd": 0.00
  }
}
```

**This is the $10k data.**

---

## Schema: `business_state_snapshot`

Daily + before significant decisions.

```json
{
  "snapshot_id": "...",
  "as_of": "...",
  "cash": {"available": 117.32, "currency": "USD"},
  "lifetime": {
    "revenue": 822.11,
    "gross_profit": 501.84,
    "net_profit": 391.22,
    "orders": 94,
    "refunds": 3
  },
  "last_1d": {},
  "last_7d": {},
  "last_30d": {},
  "funnel": {
    "impressions": 12203,
    "visits": 808,
    "favorites": 57,
    "carts": 32,
    "orders": 19,
    "conversion_rate": 0.0235
  },
  "operations": {
    "active_listings": 12,
    "open_orders": 3,
    "human_minutes_7d": 420,
    "generation_failure_rate": 0.09
  },
  "portfolio": {
    "active_experiments": ["exp_1", "exp_2"],
    "active_templates": ["sports_hero_v3"]
  }
}
```

---

## Schema: `hypothesis`

Never retrospectively invent these.

```json
{
  "hypothesis_id": "...",
  "created_at": "...",
  "claim": "Recipient-and-occasion listings outperform generic style listings",
  "scope": {"marketplace": "etsy", "category": "personalized_gifts"},
  "mechanism": "Existing purchase intent reduces education required",
  "confidence_before": 0.61,
  "predictions": [{"metric": "conversion_rate", "expected_direction": "increase"}],
  "falsification_conditions": ["generic listings outperform across 3 comparable experiments"],
  "status": "untested|testing|supported|rejected|inconclusive",
  "supporting_experiments": [],
  "contradicting_experiments": []
}
```

---

## Schema: `decision`

Keep reasoning short and explicit.

```json
{
  "decision_id": "...",
  "decision_at": "...",
  "information_cutoff_at": "...",
  "problem": "Birthday listing gets traffic but low conversion",
  "objective": "Increase conversion without lowering price",
  "options": [
    {"id": "A", "action": "lower price", "expected_value": 0.42},
    {"id": "B", "action": "add before-after proof", "expected_value": 0.73}
  ],
  "chosen": "B",
  "rationale_summary": "Reviews suggest likeness uncertainty is primary friction",
  "confidence": 0.69,
  "risk": {"max_cost_usd": 5, "reversible": true},
  "evidence_ids": ["obs_...", "feedback_..."]
}
```

`information_cutoff_at` prevents future agents from training on information that wasn't available when the decision was made.

---

## Schema: `action`

```json
{
  "action_id": "...",
  "type": "create_listing|edit_listing|change_price|change_thumbnail|generate_asset|launch_ad|stop_ad|change_supplier|launch_brand|kill_brand",
  "target_ids": ["listing_44"],
  "parameters": {"old_price": 7.99, "new_price": 9.99},
  "started_at": "...",
  "completed_at": "...",
  "human_minutes": 4,
  "compute_cost_usd": 0,
  "cash_cost_usd": 0,
  "decision_id": "...",
  "experiment_id": "..."
}
```

---

## Schema: `experiment`

```json
{
  "experiment_id": "...",
  "name": "before_after_listing_proof_v1",
  "design": "ab_test|sequential|before_after|smoke_test|qualitative|multivariate",
  "hypothesis_id": "...",
  "started_at": "...",
  "ended_at": "...",
  "control": {},
  "treatment": {},
  "primary_metric": "conversion_rate",
  "secondary_metrics": ["favorite_rate", "refund_rate", "profit_per_visit"],
  "success_rule": {"type": "threshold", "minimum_relative_change": 0.15},
  "result": {"status": "win|loss|neutral|inconclusive", "effect": 0.31},
  "causal_strength": "weak|moderate|strong",
  "confounders": ["weekend_traffic"],
  "decision_after": "adopt"
}
```

---

## Schema: `metric_definition` + `metric_point`

Never allow "conversion" to silently change definition.

```json
{
  "metric_id": "listing_conversion_rate",
  "name": "Listing conversion rate",
  "formula": "orders / visits",
  "unit": "ratio",
  "aggregation": "sum_orders / sum_visits",
  "version": "1.0.0"
}
```

```json
{
  "metric_point_id": "...",
  "metric_id": "listing_conversion_rate",
  "entity_type": "listing",
  "entity_id": "listing_123",
  "window_start": "...",
  "window_end": "...",
  "value": 0.0418,
  "numerator": 13,
  "denominator": 311,
  "source": "operator_record"
}
```

---

## Schema: `financial_transaction`

Track cash, not influencer maths.

```json
{
  "transaction_id": "...",
  "occurred_at": "...",
  "type": "revenue|refund|fee|compute|ad|supplier|shipping|software|domain|tax",
  "amount": 4.50,
  "currency": "USD",
  "brand_id": "...",
  "listing_id": null,
  "order_id": null,
  "experiment_id": null,
  "vendor": "fal",
  "cash_flow": "outflow",
  "fixed_or_variable": "variable"
}
```

---

## Schema: `generation_run`

Makes the personalization factory incredibly valuable.

```json
{
  "generation_run_id": "...",
  "template_id": "sports_hero_v3",
  "provider": "fal",
  "model": "minimax-h3-max",
  "model_version": "...",
  "task": "image_to_video",
  "input_artifact_ids": ["asset_customer_reference"],
  "prompt_version": "sportshero_prompt_17",
  "parameters": {},
  "duration_seconds": 15,
  "resolution": "768p",
  "cost_usd": 1.20,
  "runtime_seconds": 14.8,
  "qa": {
    "identity": 0.94,
    "anatomy": 0.98,
    "motion": 0.91,
    "prompt_adherence": 0.89,
    "audio": 0.86,
    "overall": 0.92
  },
  "accepted": true,
  "failure_codes": [],
  "retry_of": null,
  "output_artifact_ids": ["asset_..."]
}
```

After 5,000 of these, an agent can predict which model/settings pass QA at lowest cost.

---

## Schema: `listing_revision`

Every revision, not merely current state.

```json
{
  "listing_revision_id": "...",
  "listing_id": "...",
  "revision_number": 14,
  "effective_at": "...",
  "title": "...",
  "price": 9.99,
  "currency": "USD",
  "tags": [],
  "description_version": "...",
  "hero_asset_id": "...",
  "gallery_asset_ids": [],
  "offer": {
    "package": "digital",
    "occasion": "birthday",
    "recipient": "dad",
    "sport": "football"
  },
  "change_reason": "...",
  "experiment_id": "..."
}
```

---

## Schema: `product_template`

Actual production IP.

```json
{
  "template_id": "sports_hero_v3",
  "name": "Game Winner",
  "version": "3.2.1",
  "promise": "Put the recipient into the winning sporting moment",
  "inputs_required": {
    "photos_min": 1,
    "photos_preferred": 3,
    "recipient_name": true,
    "sport": true,
    "inside_joke": false
  },
  "pipeline": ["reference_normalization", "hero_frame", "video_generation", "commentary", "qa", "upscale", "delivery"],
  "expected_metrics": {
    "generation_cost_usd": 1.18,
    "pass_rate": 0.91,
    "human_minutes": 4.2
  },
  "known_failure_modes": ["extreme_profile_photo", "multiple_people"],
  "fallback_template_id": "...",
  "status": "experimental|production|deprecated"
}
```

---

## Schema: `customer_feedback`

Don't make the corpus a PII leak.

```json
{
  "feedback_id": "...",
  "order_id_hash": "...",
  "received_at": "...",
  "type": "review|message|refund_reason|survey",
  "rating": 5,
  "themes": ["likeness", "gift_reaction", "fast_delivery"],
  "sentiment": 0.94,
  "product_issue": null,
  "raw_text_retained": false,
  "anonymized_summary": "Buyer said recipient was surprised by likeness and shared video",
  "permission": {"public_quote": false, "training_internal": true}
}
```

---

## Schema: `observation`

Not everything is a metric.

```json
{
  "observation_id": "...",
  "observed_at": "...",
  "claim": "Customers repeatedly ask whether the final portrait will resemble their actual dog",
  "category": "buyer_friction",
  "evidence_ids": ["feedback_1", "feedback_7", "feedback_19"],
  "confidence": 0.84,
  "actionability": 0.91
}
```

---

## Schema: `lesson`

Derived knowledge object, not automatically treated as truth.

```json
{
  "lesson_id": "...",
  "claim": "For personalized generative products, visible source-to-output examples reduce likeness uncertainty",
  "scope": {"channel": "etsy", "categories": ["pet_portraits", "personalized_video"]},
  "supporting_episode_ids": ["ep_12", "ep_45", "ep_81"],
  "contradicting_episode_ids": [],
  "confidence": 0.86,
  "transferability": "high",
  "first_observed_at": "...",
  "last_validated_at": "...",
  "invalidation_condition": "Three comparable experiments produce no conversion improvement"
}
```

---

## Schema: `playbook`

Actionable distilled procedure backed by episodes.

```json
{
  "playbook_id": "pb_validate_personalized_product",
  "name": "Validate a personalized gift product",
  "version": "2.1",
  "trigger": {"business_stage": "pre_launch"},
  "required_inputs": ["recipient", "occasion", "artifact", "production_cost"],
  "steps": [
    {"order": 1, "action": "Create five representative outputs", "evidence": ["ep_17", "ep_61"]},
    {"order": 2, "action": "Require >=80% acceptable-generation rate", "evidence": ["ep_72"]}
  ],
  "stop_conditions": ["expected margin below threshold", "generation reliability below threshold"],
  "evidence_strength": 0.79
}
```

---

## Schema: `brand_candidate`

Lets the promotion strategy become learnable.

```json
{
  "candidate_id": "...",
  "concept": "personalized_sports_fantasy",
  "working_brand": "Game Winner",
  "scores": {
    "buyer_comprehension": 0.95,
    "existing_demand": 0.91,
    "production_reliability": 0.86,
    "gross_margin": 0.88,
    "shareability": 0.96,
    "repeatability": 0.83
  },
  "stage": "idea|prototype|validated|store_candidate|launched|core|maintain|killed",
  "promotion_rule": {"minimum_score": 0.80},
  "decision_history": []
}
```

---

## Schema: `time_entry`

Record human labour.

```json
{
  "time_entry_id": "...",
  "started_at": "...",
  "ended_at": "...",
  "minutes": 37,
  "activity": "template_development",
  "brand_id": "...",
  "experiment_id": "...",
  "automation_potential": 0.82
}
```

---

## Schema: `content`

Record the content flywheel.

```json
{
  "content_id": "...",
  "channel": "youtube",
  "format": "short",
  "published_at": "...",
  "topics": ["gamewinner", "etsy", "ai_video"],
  "source_episode_ids": [],
  "metrics": {
    "views_24h": 12044,
    "views_7d": 51102,
    "watch_time_seconds": 182211,
    "subscribers_gained": 132
  },
  "commerce_attribution": {
    "store_visits": 81,
    "orders": 6,
    "revenue": 71.94
  }
}
```

---

## Schema: `agent_run`

When StallShark operates autonomously, log its own behavior.

```json
{
  "agent_run_id": "...",
  "agent": "stallshark_operator",
  "agent_version": "0.8.2",
  "model": "...",
  "started_at": "...",
  "ended_at": "...",
  "objective": "Choose today's highest-value action for Game Winner",
  "context_snapshot_id": "...",
  "retrieved_episode_ids": ["ep_12", "ep_89"],
  "plan_summary": "Change listing proof image rather than price",
  "actions_proposed": [],
  "actions_executed": [],
  "human_intervention": {"required": false},
  "outcome_episode_id": "...",
  "cost_usd": 0.12
}
```

---

## Schema: `eval_case`

Build evals from reality.

```json
{
  "eval_case_id": "...",
  "snapshot_id": "snapshot_day_87",
  "question": "What is the highest-EV action available today?",
  "available_evidence_ids": [],
  "forbidden_future_evidence_after": "...",
  "historical_action_id": "...",
  "actual_outcome": {},
  "scoring": {
    "profit": 0.4,
    "risk": 0.2,
    "reasoning_quality": 0.2,
    "policy_compliance": 0.2
  }
}
```

---

## Corpus Directory

```text
commerce-corpus/
├── README.md
├── README_AGENT.md
├── CHANGELOG.md
├── croissant.json
├── manifest.json
├── LICENSE
├── schemas/           (18 JSON schemas)
├── ontology/          (actions, metrics, failure codes, etc.)
├── events/YYYY/MM/DD/events.jsonl
├── entities/          (brands, stores, listings, templates as Parquet)
├── snapshots/daily/
├── experiments/
├── episodes/episodes.jsonl
├── lessons/lessons.jsonl
├── playbooks/
├── evals/
├── agent_runs/
├── public/blog/
├── public/youtube/
├── restricted/pii/
├── artifacts/sha256/  (content-addressed)
└── indexes/corpus.sqlite + corpus.duckdb
```

---

## Agent-Facing Layer

Don't sell a ZIP. Sell:

```text
10 GB corpus + query database + schemas + playbooks + evals + read-only MCP server
```

MCP tools:

```
search_episodes(query, filters)
get_business_state(timestamp)
find_similar_state(snapshot_id)
compare_experiments(ids)
get_evidence(id)
get_playbook(goal, constraints)
trace_lesson(lesson_id)
get_template_performance(template_id)
find_failure_modes(template_id)
simulate_budget(strategy, budget)
get_policy_constraints(channel, timestamp)
```

Buyer says: "Use Commerce Corpus as a source. I have $10,000 and want to enter personalized fishing gifts."

Agent interrogates twenty thousand historical episodes selectively.

---

## What to Log Starting Day 1

Seven things to get perfect immediately:

1. **Every financial transaction**
2. **Every meaningful action**
3. **State snapshot every day**
4. **Hypothesis before experiments**
5. **Decision before action**
6. **Outcome after sufficient observation**
7. **Human time spent**

The irrecoverable information is: **what you thought and knew before seeing the outcome.**

---

## The Critical Rule: Preserve Failed Predictions

Day 11 belief: Natural Habitat wins. 74% confidence.

Day 19 evidence: Birthday 4.2%, Habitat 0.8%.

Day 20 update: hypothesis rejected.

The corpus must preserve this. It contains **error gradients**.

Most business writing destroys them.

---

## The Real Long-Term Loop

Initially: YOU → make decision → STORE → outcome → CORPUS

Then: YOU + STALLSHARK → CORPUS retrieval → decision → outcome → CORPUS improves

Eventually: AUTONOMOUS COMMERCE AGENT → retrieve analogous episodes → plan → execute → measure → update → improve

The highest-value use may simply be:

> **Seed every new commercial agent with all the experience accumulated by every previous store.**

MythicBee learns something about personalization. Game Winner inherits it.

The tenth business starts with the accumulated experience of the first nine.

The stronger eventual claim:

> **Give your agent a machine-readable record of how real stores were built, what failed, what worked, and the evidence behind every major operating rule — so it starts with years of empirical experience instead of a blank context window.**

---

*The business comes first. Content records the business. The corpus outlasts both. The corpus is the product.*
