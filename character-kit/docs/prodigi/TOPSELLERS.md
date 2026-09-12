# Top-seller evidence in-repo — what exists, what transfers to MogMug

No stallshark repo exists; all of this is StallSpy. No pet-niche scrape exists yet — flagged as next run below.

## Seller-level data that exists

- `tool/data/personalized_football_gift/*.csv` — 200 listings, full funnel fields
  (price, favorers, views, tags, reviews, shop sales). Football niche, Sept 2026.
- `tool/data/scored_winning_goal_gift/*.csv` — 4 listings, same schema.
- `tool/etsy_snapshot.py` — live snapshot runner (needs ETSY_API_KEY/SECRET env).
- `intel/z2m-strategy/etsy-strat.md` — 100 shops w/ 100K+ sales study.
- `research/archive/MARKET_RESEARCH.md` — pet-niche demand + competitor tables.
- `tools/aserper-etsy-mcp` + 6 other Etsy MCP servers — scrape paths.

## Transferable patterns (from the 200-listing scrape + 100-shop study)

- Median price ~$20; ~half of listings under $20. Matches repo sweet spot $15–35.
- Top-favored items are cheap personalised goods (£6.99 name sign, 1124 favorers) — low price + name = favor magnet.
- Top shops concentrate: 82 shops across 200 listings, leaders hold 8–14 slots. Niching down wins slots.
- 100-shop tactics: 93% run 25%+ sales, 59% use low-price variants to look cheap in search,
  81% charge shipping (median $5.70, under $6 prioritised), 91% pro photos (flatlays win),
  median 1,611 listings, 96% use all 13 tags (our scrape avg 11.7 — gap to close).

## What this means for THE TEN

- Holds: cheap entry (stickers, self-send card) as favor/search bait; $15–35 bundle core
  (mug + video + card); run shop-wide ~25% sales; all 13 tags; flatlay mockups (Prodigi has 3D renders).
- Watch: our catalogue has no sub-£5 search-bait variant and no shipping-under-$6 plan yet.
- Memorial/breed angles stay art packs, per EVIDENCE.md.

## Next run (blocked on plumbing, not data)

Scrape pet keywords with the same schema: `custom pet portrait mug`, `personalized pet ornament`,
`dog bandana personalized`, `pet memorial gift`, `funny dog mug`. Runner exists
(`etsy_snapshot.py` keywords list); keys live in agent-vault `etsy` and must be wired via the
vault proxy, never pasted into env. Until then, no new-SKU claims beyond THE TEN.
