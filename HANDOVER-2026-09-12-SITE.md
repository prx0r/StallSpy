# Handover — 2026-09-12 (website slice)

Follows HANDOVER-2026-09-12-MOGMUG.md. All pushed to `prx0r/StallSpy@master`, tree clean.

## Built this slice (`92a8eb1`)

- Title → MogMug, console + AI system prompt rebranded (bee infra untouched underneath).
- Host cast: Buster / Bartholomew III (OG resident) / Kevin / Pickles / Mog, random per session.
- Product tiles → canonical offers + real prices (video £6.99, bundle £12.99, mug £19.99, cushion £29.99).
- order-pipeline.js catalog → canonical names/prices/verified SKUs; portal `mogmug.com/x/`; order prefix `MM-`.
- New `js/pog-pack.js`: 12 pet loading lines in hive-engine schema (wire-in documented, engine adopts later).

## State of the world

- StallSpy master: site rebranded at surface, Bartholomew art + bee-session + hive engine intact for theme-pack archiving.
- Vaults: `prodigi` = PRODIGI_API_KEY (live, verified 200); `etsy` = KEYSTRING + SHARED_SECRET.
- MogMug notes indexed (`~/mogmug/00-INDEX.md`); canonical products/costs/listings in `character-kit/docs/prodigi/`.
- No Etsy listings live (explicitly deferred). No stallshark repo exists — everything is StallSpy.
- Tokens: GitHub + Etsy keys have passed through chat — rotate when convenient.

## Next (see todo board)

Site reskin + phrase-pack wiring → sample pack → listings live → memorial/breed packs → Xmas art by early Nov.
