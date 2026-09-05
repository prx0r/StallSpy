# The Etsy Data Cooperative — Build Thesis

**Date:** 5 September 2026

---

Yes — **the EverBee competitor is potentially the more interesting business than the Etsy shops themselves.** The shops become the laboratory and customer-acquisition story for the tool.

And your objection to Etsy Plus is correct: **30 days alone is not enough for serious product selection**, especially when Q4 seasonality is the entire point.

### Etsy Plus is useful, but mainly as a truth calibrator

Marketplace Insights currently gives real Etsy search counts and listing counts for the previous 30 days. That's valuable because essentially every third-party tool is estimating at least some of its numbers. ([Etsy Help][1])

But Etsy has now started testing an expanded Marketplace Insights product with:

* 30 days
* 90 days
* **12 months**
* purchased-listing price ranges
* **search conversion rate**

That expanded version isn't guaranteed to be available to every seller yet, but Etsy has officially announced the test. ([Etsy Help][2])

If 12-month search + conversion data becomes broadly available, Etsy Plus becomes enormously more useful.

But even then, we can build something far better around it.

---

## There is already historical Etsy data

Just not one clean authoritative database.

| Source                        |                                  Historical depth | What it actually knows                       |
| ----------------------------- | ------------------------------------------------: | -------------------------------------------- |
| **Etsy Marketplace Insights** |                 30d currently; 90d/12m in testing | **Real Etsy searches + competition**         |
| **eRank**                     |                                        ~15 months | estimated historical search/click behaviour  |
| **Marmalead**                        |                        >12 months + 3-mo forecast | estimated search/engagement seasonality      |
| **EverBee**                   |                                 3/6/12/24 months+ | estimated listing sales/revenue/trends       |
| **Alura**                     |                                12 months/all time | estimated listing sales/revenue              |
| **Koalanda**                  | continuous tracking; 30-day listing history shown | independently detected/estimated sales       |
| **Bright Data**                    |                    snapshots you purchase/collect | raw marketplace listing/catalog observations |

eRank explicitly advertises **15 months of historical search data**. ([eRank][3])

Marmalead has over a year's keyword seasonality and produces a three-month forecast from it. ([Marmalead][4])

Alura gives 12-month historical sales/revenue estimates for listings and shops. It openly says those sales numbers are estimates based on signals including views, favorites, category and listing age. ([Alura Help Center][5])

EverBee now goes to **24 months and beyond**. ([EverBee][6])

And then there's Koalanda, which I hadn't paid enough attention to before.

It claims to track **more than 125 million Etsy listings**, detects millions of sales daily, updates daily, and claims 89% average accuracy for its listing-sales history. Those are Koalanda's own claims, not independently verified, but the methodology is interesting. ([Koalanda][7])

So yes:

> **Historical Etsy intelligence absolutely exists.**

What's missing is an obvious **open/cheap high-quality Etsy data platform**.

---

## The important EverBee revelation

EverBee itself says:

> Etsy doesn't give it marketplace-wide sales/revenue history.

It estimates them.

EverBee says its model uses things Etsy makes observable such as:

* views
* favorites
* listing date
* price
* other listing characteristics

and then predicts sales. ([EverBee Help Center][8])

Alura describes essentially the same situation. ([Alura Help Center][5])

EtsyHunt explicitly says Etsy does not permit them to collect actual listing sales, so they estimate sales using proprietary ML. ([EHunt Knowledge Base][9])

This changes the problem enormously.

We don't need to discover EverBee's secret database.

### There isn't a secret exact-sales database.

We're competing on:

**observation + longitudinal snapshots + inference + first-party calibration + UX.**

That is buildable.

---

## And I think I see how to beat them

Instead of:

> Another EverBee clone with a prettier keyword table.

Build:

# **The Etsy Data Cooperative**

The most valuable piece Etsy sellers can give us is something EverBee can't normally see:

**their actual sales.**

Etsy lets sellers download an entire **year of real sold transactions** as CSV. It includes things such as item title, price, orders and payment information. ([Etsy Help][10])

And Shop Stats themselves go back to **November 2017**, including visits, orders, conversion and revenue. ([Etsy Help][11])

Imagine the onboarding:

> **Upload your Etsy history.**
>
> We'll analyse your shop for free.

Seller drops:

`EtsySoldOrders2024.csv`
`EtsySoldOrders2025.csv`
`EtsySoldOrders2026.csv`

We give them an excellent free dashboard.

In return, with explicit informed consent and appropriate terms/privacy controls, we can potentially build anonymized aggregate models from participating shops. The exact legal/data-rights design should be reviewed before doing aggregated commercialization, especially because Etsy's API terms are restrictive.

But technically this is vastly more interesting.

Now we'd have:

**actual sales**

versus

**what our public-market model predicted.**

That lets us train/calibrate:

`public signals → probable actual sales`

on millions of seller/listing-month observations over time.

That is a real data moat.

---

## Example

Suppose our public observation says:

### Listing A

Age: 153 days
Price: £24
Favorites: +682
Reviews: +57
Shop sales change: +1,480
Search rank: #4 → #8
Badge: Bestseller
Category: personalized sports gifts
Reviews mentioning listing: 44
Visible stock/renewal events: etc.

Our prediction:

**~290 sales/month**

And then one participating seller's real historical CSV tells us:

**Actual: 317**

Great.

Listing B prediction:

**242**

Actual:

**93**

Now we can ask:

Why?

That's exactly the weakness EverBee acknowledges in its own estimation model: listings with lots of views/favorites but poor conversion can cause estimates to be wrong. ([EverBee Help Center][8])

With enough opted-in actual seller data, we can learn what reduces that error.

---

## This is more valuable than collecting historical keywords alone

The database I'd ultimately want looks like:

```text
listing_daily
-------------
listing_id
shop_id
date

title
price
discount_price
favorites
reviews
shop_total_sales
shop_review_count

position_keyword_1
position_keyword_2
position_keyword_3

bestseller_badge
etsy_pick
ad_visible

image_embedding
title_embedding
tags
category

estimated_sales
estimated_revenue
```

Then:

```text
keyword_daily
-------------
keyword
date

etsy_real_search_30d
etsy_competition
median_price
top100_listing_ids

google_search_volume
google_trends_score
pinterest_signal
tiktok_signal
```

Then the magical table:

```text
seller_ground_truth
-------------------
listing_id
month

actual_units
actual_revenue
actual_orders
actual_conversion
actual_views
actual_ad_spend
actual_profit
```

That last table transforms the business.

---

## We can also build history ourselves from today forward

This is the fundamental insight.

You don't necessarily buy a historical database.

You create one.

Day one:

```text
6 September 2026

"personalised football gift"

Results:
1. listing 83829
2. listing 92018
...
100. listing 18838
```

Tomorrow:

```text
7 September

listing 83829 → #4
listing 92018 → #1
new listing → #7
```

Repeat.

Now we know:

* rankings
* listing entrances/exits
* price changes
* discounts
* thumbnail changes
* favorites growth
* review growth
* shop sales growth
* listing ages
* title changes
* category changes
* bestseller badges

At Christmas 2027 we own a dataset that nobody beginning in 2027 can recreate retroactively.

**Time itself becomes the moat.**

---

## There are commercial raw-data providers too

Bright Data currently advertises an Etsy dataset with **21M+ records** and lets customers buy filtered Etsy snapshots by field/timeframe/category. ([Bright Data][12])

It also sells Etsy scraping infrastructure.

That doesn't automatically mean every downstream use complies with Etsy's terms, but it shows the raw catalogue acquisition problem is not technically difficult. ([Bright Data][13])

So technically we could bootstrap rather than spending six months crawling the world.

But I would be cautious here.

---

## The big issue is Etsy's current API policy

This is where we need to build correctly.

Etsy's public Open API can search active marketplace listings by keyword and return fields including listing ID, shop ID, title, description, creation timestamps, price-related data, favorites, personalization status, tags and more. ([Etsy Developers][14])

That sounds perfect.

Unfortunately, Etsy's current API terms explicitly say you may not use automated systems/browser extensions to scrape/analyse Etsy data **unless Etsy gives written permission**, and separately prohibit API collection for analytics/ML without express written authorization. ([Etsy][15])

So I would **not** quietly build a 200-million-listing crawler on a standard Etsy API key.

I'd approach Etsy.

And here's the pitch:

> We're building a free analytics platform helping Etsy sellers understand demand, profitability, seasonality and shop performance.
>
> Sellers voluntarily connect their shops.
>
> We want commercial API access and explicit analytics authorization.

Etsy now has an explicit **Commercial Access** route for applications serving Etsy sellers. ([Etsy Developers][16])

That's the professional way to build this.

---

## What can we organize right now?

Yes.

I'd buy one month of:

**EverBee Business** — $69
**eRank Pro**
**Marmalead**
**Alura**
**Etsy Plus**

Not because we intend to resell their databases.

Instead, reverse-engineer the **product surface**.

Make a canonical comparison dataset:

```text
keyword:
personalized football gift

                     Sep 2026
Etsy actual 30d       8,123
eRank                  X
EverBee                Y
Alura                  Z
Marmalead              W

competition
Etsy                    X
eRank                   Y
...

listing:
123456789

EverBee estimated sales
Alura estimated sales
Koalanda estimated sales
Our estimate
```

Then compare all estimates against **our own shops' actual sales**.

That alone would make a fantastic blog series.

> **We tested EverBee, Alura, eRank and Marmalead against real Etsy sales. Here's who was actually closest.**

People would absolutely search for that.

Recent Reddit posts demonstrate why: sellers routinely see wildly different search-volume numbers between eRank, Alura and EverBee and don't know which one to believe. ([Reddit][17])

That's our opening.

---

## Don't compete on "keyword score"

Everyone already has this.

The killer product is:

### **What should I sell next?**

User enters:

> I have £100.
> UK.
> Can use AI.
> Can do POD.
> Want Christmas products.

We scan the universe.

Return:

### #1 Personalized football fantasy films

Demand trajectory
`█████████ +61% YoY`

Competition quality
`███░░░░░░ LOW`

Median selling price
`£22`

Estimated gross margin
`73%`

Seasonality
`Oct ↑ → Nov ↑↑ → Dec ↑↑↑`

Emerging keywords

* football gift dad
* football 50th birthday
* personalized football video
* football retirement gift

Competitor concentration

Top 10 shops capture X%.

Opportunity diagnosis:

> Searches are increasing faster than quality supply. Most competitors sell static prints. Video personalization is nearly absent.

**CREATE SHOP**

And then the software generates the listings.

That's not EverBee.

That's an **Etsy Bloomberg Terminal + agent**.

---

## And there's an even bigger wedge

Instead of charging broke beginners $30/month:

### Free.

That matches your thesis.

Make money through:

* premium automation
* supplier/POD affiliate revenue
* optional managed setup
* store audits
* consulting
* fulfillment margins
* advanced API/MCP
* later professional seller tier

Someone unemployed who needs £300/month is exactly the person who doesn't want another $30 subscription before their first sale.

So:

> **The best Etsy research software should be free until Etsy is making you money.**

That's an extremely good positioning wedge against EverBee.

---

## The journey becomes the acquisition engine

This now fits your original idea even better:

### `£0 → £1,000,000 Etsy Experiment`

But every experiment contributes to the dataset.

```text
DAY 1
£0 revenue
8 listings
3 hypotheses

DAY 14
£417 revenue
Winner: Game Winner Football

DAY 38
£2,911
We discovered 50th Birthday converts 2.4× Dad Birthday

DATASET
1.7m marketplace observations
42,881 keywords
12,418 historical listing snapshots
```

Then:

> **Download the exact tool I'm using free.**

That's extremely different from Etsy gurus.

You're simultaneously:

**seller + researcher + software builder + public case study.**

---

## What I would build first

Not the frontend.

**The data warehouse.**

Start accumulating irreversible history **now**:

1. canonical taxonomy of Etsy niches/categories;
2. keyword universe;
3. daily/weekly marketplace snapshots from permitted/licensed sources;
4. competitor estimate comparison layer;
5. Etsy Marketplace Insights ground-truth observations;
6. Google Trends/search history;
7. seller CSV importer;
8. our own shop ground truth;
9. prediction model;
10. opportunity ranker.

Then build the nice UI over it.

The significant realization is:

> **EverBee's defensibility isn't that it has Etsy's secret database. It has years of accumulated observations and models.**

We can start accumulating ours **September 2026**, calibrate it against real seller data, make the tool dramatically more agentic, and use our own Etsy portfolio to prove whether the recommendations actually make money.

That is considerably more interesting to me than merely building another Etsy shop.

---

## References

[1]: https://help.etsy.com/hc/en-us/articles/35122361353239-How-Do-I-Use-Etsy-s-Marketplace-Insights-Tool "How Do I Use Etsy's Marketplace Insights Tool? – Etsy Help"
[2]: https://help.etsy.com/hc/en-in/articles/10603291042967-Newly-Crafted-Etsy-Updates-for-Your-Shop "Newly Crafted: Etsy Updates for Your Shop – Etsy Help"
[3]: https://erank.com/keyword-research "Keyword Research Tools for Etsy Sellers — eRank"
[4]: https://marmalead.com/ "Marmalead"
[5]: https://help.alura.io/en/articles/8650440-getting-started-with-alura-chrome-extension "Getting started with Alura Chrome Extension | Alura Help Center"
[6]: https://www.everbee.io/product-analytics "Etsy Product Analytics - Real Sales & Revenue Data | EverBee"
[7]: https://koalanda.pro/etsy-product-research "Etsy Product Research | Koalanda"
[8]: https://help.everbee.io/en/article/6-how-does-everbee-work "How does EverBee work?"
[9]: https://help.etsyhunt.com/en-us/article/about-keywords-parameters-meaning-15p9d9b "About Keywords & Parameters Meaning | EHunt Knowledge Base"
[10]: https://help.etsy.com/hc/en-gb/articles/360000343328-How-to-Download-a-Spreadsheet-of-Your-Sold-Transactions "How to Download a Spreadsheet of Your Sold Transactions – Etsy"
[11]: https://help.etsy.com/hc/en-us/articles/115015774268-How-to-Use-Etsy-Stats-for-Your-Shop "How to Use Etsy Stats for Your Shop – Etsy Help"
[12]: https://brightdata.com/products/datasets/etsy "Buy Etsy Datasets - 21M+ Records Available"
[13]: https://brightdata.com/products/web-scraper/etsy "Etsy Scraper API - 5K records/Month for Free"
[14]: https://developers.etsy.com/documentation/reference "Reference | Etsy Open API v3"
[15]: https://www.etsy.com/legal/api/ "API Terms of Use - Our House Rules | Etsy"
[16]: https://developers.etsy.com/ "Etsy Open API v3 | Etsy Open API v3"
[17]: https://www.reddit.com/r/EtsyCommunity/comments/1uoo2sm/which_one_is_correct_searching_the_same_word_it "Which one is correct, searching the same word it gives me different results?"
