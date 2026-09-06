# Legal / Risk Notes

Not legal advice. Treat this as an implementation checklist for counsel review.

## 1. Personalised-goods cancellation rights

UK and EU consumer rules generally distinguish made-to-order / clearly personalised goods from ordinary distance-sale goods.

The UK government guidance states that personalised/custom-made items are generally outside the normal change-of-mind cancellation/refund requirement, while faulty goods remain protected.

EU consumer guidance similarly lists made-to-order / clearly personalised goods as an exception to the general 14-day withdrawal right, while legal guarantees for defective/non-conforming goods still apply.

**Implementation**
- state clearly when production begins;
- make customer approve the proof;
- preserve exact approved file;
- retain supplier/job IDs;
- have a fair reprint policy for defects.

## 2. AI + copyright / trademarks

Highest operational risk:
customers asking for:
- Disney/Marvel/etc characters;
- football club logos;
- celebrity likeness;
- luxury logos;
- living artists’ styles;
- copied Etsy designs.

Do not assume “AI generated” makes it lawful.

**Build**
- prompt moderation;
- protected-mark keyword list;
- image/logo detection where practical;
- takedown process;
- rights declaration for customer uploads;
- safe house-style library.

Ideogram's current API documentation even exposes optional copyright-detection functionality on certain generation endpoints; use provider safety signals where helpful, but do not outsource policy entirely.

## 3. Customer photo privacy

You will process family/child/pet photos, names, dates and relationships.

Design for:
- encryption;
- limited retention;
- private-by-default assets;
- signed URLs;
- deletion;
- no model-training reuse unless explicitly permitted;
- child-photo safeguards;
- clear privacy notice.

## 4. Marketplace rules

Etsy's Creativity Standards allow seller-prompted AI creations but require AI disclosure; production partners should also be disclosed where required.

Do not build a business model that depends on hiding POD/AI.

## 5. Product safety

Some products introduce special obligations:
- children's goods;
- drinkware/food-contact;
- candles;
- toys;
- electronics.

Start with low-regulatory-complexity paper/print/decor goods from reputable suppliers.

## 6. Delivery claims

Never claim “guaranteed by Christmas” unless the operational system supports it.

Compute cutoff from:
- provider p90 production;
- carrier p90 delivery;
- destination;
- current backlog;
- buffer.

## 7. Discount claims

Avoid fake perpetual “was £62, now £32” patterns unless you meet applicable pricing/advertising rules.
Long-term trust matters more than conversion hacks.

## 8. AI text correctness

A misspelled dead relative’s name on a memorial product is not a minor UI bug.

Exact user strings must bypass generative uncertainty and be rendered deterministically.
