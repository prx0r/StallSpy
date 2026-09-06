# Telemetry

Every phrase exposure can emit a `SelectionMeta` event.

Recommended event:

```json
{
  "event": "hive_activity_exposure",
  "bee_mission_id": "mission_123",
  "bee_id": "martin",
  "phase": "package",
  "season": "christmas",
  "entry_id": "package_004",
  "source": "bank",
  "weight": 1.8,
  "selection_probability_approx": 0.11,
  "rendered_text": "Finding the smarter bundle…",
  "policy_version": "hive-activity-v1"
}
```

## Why log this?

Later you can answer:

- Which phrases reduce abandonment during 15-second video generation?
- Does contextual loader copy improve patience?
- Do Christmas-specific lines increase session continuation or simply annoy people?
- Does Martin's dry language correlate with higher value-bundle acceptance?
- Which rare lines get screenshotted/shared?

## Do not optimize purely for dwell time

A phrase engine that maximizes time-on-loader will learn to delay people.

Primary application metrics should remain:
- successful operation completion
- abandonment
- purchase
- recipient outcome
- support contacts

HiveActivity is supportive UX.

## Privacy

Do not log raw private transcript content in these events.

Prefer stable hook categories / IDs or redacted display-safe hook text.
