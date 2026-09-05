# EasyEtsy Build Blueprint

## Repo layout

```text
easyetsy/
  apps/
    operator-web/
    api/
  packages/
    etsy-openapi/
    etsy-gateway/
    product-schema/
    listing-compiler/
    policy-engine/
    market-signals/
    creative-manifest/
    fulfillment/
    audit/
  workers/
    webhook-consumer/
    listing-research/
    performance-review/
    fulfillment-dispatch/
  db/
    migrations/
  evals/
    listing-compiler/
    tool-safety/
    webhook-idempotency/
  docs/
    etsy/
```

## Suggested services

- Postgres: canonical own-shop and experiment state
- Redis/Valkey or durable queue: webhook/jobs
- Object storage: original assets, generated mockups, production files
- Secret manager: Etsy OAuth client/refresh data and POD credentials
- OpenTelemetry: request/tool traces

## Data objects

### ProductFamily
Own this; do not make Etsy listing JSON your domain model.

### ChannelProjection
Maps a ProductFamily into Etsy-specific listing fields.

### MarketSignal
Provider + query + timestamp + metric + confidence + raw reference.

### ListingExperiment
Hypothesis, listing version, creative version, price, launch date and outcomes.

### Approval
Who approved what tool call, when, and the exact input hash.

### FulfillmentJob
One durable record that prevents double-submit to a POD provider.

## Agent tool contract principles

1. Small semantic tools, not arbitrary HTTP.
2. JSON Schema validation before every write.
3. Read/write scope separation.
4. Deterministic fee/margin math outside the LLM.
5. Human approval for publish/destructive/financial actions.
6. Evidence/source IDs for market claims.
7. Idempotency keys on all external side effects.
8. Capture Etsy request IDs and response codes for support/debugging.

## First 12 implementation tickets

1. Pull and pin Etsy OpenAPI in CI.
2. Generate internal typed API client.
3. Implement PKCE OAuth callback and refresh-token vault.
4. Add rate-limit broker.
5. `shop_get_state`.
6. `listing_get` + `listing_get_inventory`.
7. `listing_prepare_draft` compiler.
8. `listing_create_draft` with approval gate.
9. Webhook receiver/signature verifier.
10. Webhook durable queue + idempotent consumer.
11. EverBee MCP research adapter normalized to `MarketSignal`.
12. Printify/Customily proof-of-concept for one personalized Q4 gift.

## Kill criteria

Do not add a SaaS/tool when:
- it duplicates two existing signals,
- it cannot export/API its data,
- it relies on unauthorized Etsy scraping,
- its metric cannot be validated,
- its sync creates multiple sources of truth,
- it requires the agent to hold unrestricted shop credentials.
