# Fulfilment and Supplier Strategy

## The central supply-chain decision

### Personalised / made-to-order
Use **local POD**.

### Generic seasonal goods
Use **preseason wholesale + local 3PL** only after demand validation.

AliExpress-style per-order international delivery is usually structurally bad for Christmas/birthday urgency.

## Prodigi — strong UK-first default

Useful current characteristics:
- UK-rooted;
- API;
- Shopify/Etsy integrations;
- white-label/direct fulfilment;
- manufacturing in multiple regions;
- routing to facilities;
- product/status/tracking APIs.

Selected current starting production prices (before tax/shipping):
- classic card £1.10;
- photo print £0.19;
- wrapping paper £3;
- mug £3.64;
- gallery board £3.50;
- magazine £3.75;
- calendar £5.96;
- photo book £6.50;
- T-shirt £8;
- cushion £9;
- puzzle £10;
- aluminium ornament £6.

Production times vary by SKU; cards are advertised around 24h and many other products in multi-day ranges.

**Use it first for the UK MVP because integration and domestic production matter more than shaving pennies.**

## Gelato — global routing alternative

Useful characteristics:
- large local production network;
- Shopify/Etsy/WooCommerce/API;
- personalisation tooling;
- local routing;
- broad country coverage.

Use it as:
- second supplier;
- country expansion;
- failover;
- SKU coverage.

## Gooten / Printify
Useful for broader catalogues and supplier comparisons.
Avoid turning the storefront into an uncurated 500-SKU POD catalogue.

## Fulfilment router

Every order should resolve:

```
destination
→ product spec
→ candidate providers
→ cost
→ estimated production time
→ shipping SLA
→ quality score
→ failure rate
→ margin
→ chosen provider
```

### Routing objective

Minimise:
`landed_cost + late_delivery_penalty + quality_risk`

Not simply production price.

## Supplier scorecard

Maintain per provider × SKU × country:
- base production cost;
- shipping cost;
- tax;
- median production hours;
- p90 production hours;
- median delivery;
- p90 delivery;
- damaged rate;
- reprint rate;
- cancellation success;
- tracking quality;
- packaging quality;
- colour consistency;
- print-area accuracy;
- customer-reported NPS.

## Q4 rule

In peak weeks, reliability beats a 30p saving.

Show the customer an estimated arrival date generated from real performance, not supplier marketing text.

## Hybrid wholesale model

For generic, non-personalised seasonal products:
1. discover with trends;
2. test with affiliate/marketplace/POD-like low-risk equivalent;
3. sample manufacturer;
4. small MOQ;
5. sea/rail/air freight well before Q4;
6. store in domestic 3PL;
7. use as add-on to personalised hero products.

Netherlands is particularly interesting as an EU distribution hub: official Dutch statistics have shown very large Christmas-decoration import/re-export flows, with China the dominant source.

## Packaging opportunity

The customer does not see your API stack. They see:
- envelope/box;
- print;
- gift note;
- arrival date;
- unboxing.

Invest in:
- white-label;
- no invoice pricing;
- gift-ready packaging;
- tasteful inserts;
- QR/digital reveal where useful.

A £1 cheaper product that looks dropshipped destroys the premium story.
