"""Simple hypothesis score; replace manual inputs with live radar data."""

WEIGHTS = {
    "seasonal_repeatability": 0.20,
    "current_growth_slope": 0.15,
    "commercial_intent": 0.15,
    "low_competition": 0.10,
    "gross_margin_potential": 0.10,
    "personalization_gain": 0.10,
    "visual_shareability": 0.08,
    "local_fulfillment_fit": 0.07,
    "repeat_recipient_value": 0.05,
}

def score(metrics: dict[str, float]) -> float:
    """Inputs are 0..100. Output is 0..100."""
    missing = set(WEIGHTS) - set(metrics)
    if missing:
        raise ValueError(f"Missing metrics: {sorted(missing)}")
    return round(sum(metrics[k] * w for k, w in WEIGHTS.items()), 2)

if __name__ == "__main__":
    example = {
        "seasonal_repeatability": 100,
        "current_growth_slope": 80,
        "commercial_intent": 95,
        "low_competition": 55,
        "gross_margin_potential": 75,
        "personalization_gain": 100,
        "visual_shareability": 95,
        "local_fulfillment_fit": 90,
        "repeat_recipient_value": 95,
    }
    print("Annual family ornament:", score(example))
