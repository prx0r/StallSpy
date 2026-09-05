# The £0 → £1M Journey — Content Spec

**Date:** 5 September 2026
**Core thesis:** Document the experiment. The documentation IS the business.

---

## The Flywheel

```
Build stores → Content → Audience → Sales → Validation → More content → More audience
     ↑                                                                        |
     └────────────────────────────────────────────────────────────────────────┘
```

Even failure is content. Even failure is data. The only way to lose is to stop publishing.

---

## Why This Works

### The meta-thesis

> Unemployment grows from AI. People need ways to make money. A person documenting their journey building Etsy stores with AI is exactly what thousands of people want to watch — because they're asking their own agents "what works?" and there's no real-world timestamped log of someone actually doing it.

### The content economics

Best-performing content on YouTube = "how to make money."

We don't need to fake it. We're literally doing it.

### The compounding loop

| Stage | What happens | What it produces |
|-------|-------------|-----------------|
| Day 1 | First video + first listing | 0 views, 0 sales |
| Week 2 | Daily recaps stacking | Search index finds "etsy money" content |
| Month 1 | "Etsy Money Week 1: +$12" | People subscribe for the journey |
| Month 3 | Real revenue numbers | Credibility → audience grows |
| Month 6 | Tool launches | Audience → tool users |
| Month 12 | £100K+ revenue | Authority → consulting, speaking, book |
| Month 24 | £1M run rate | Case study → everything compounds |

### Even if it fails

A granular, timestamped log of someone trying to start an Etsy store — tracking actions daily on what works and what doesn't — is valuable data. When someone asks their agent "what works on Etsy?", this dataset is the answer.

---

## Content Formats

### Daily YouTube Short (30-60 seconds)

What happened today. No production value needed. Literally a phone recording or screen capture.

```text
"Day 14. Made $417 today. Here's what happened.
I listed 3 new football gift variations.
The 50th birthday one converted 2.4x better than the generic dad one.
I spent $0 on ads. All organic.
Here's what I learned..."
```

### Weekly Stitch ("Etsy Money Week X")

All 7 daily shorts stitched together + summary stats.

```text
Etsy Money Week 3
Revenue: +$2,911
Expenses: -$89 (Prodigi cards)
Profit: $2,822
Listings: 14 active
Best seller: 50th Birthday Football
Worst seller: Generic "Sports Gift"
Key insight: Age milestones convert 3x better than generic
```

### Monthly Deep Dive (5-10 minutes)

Full analysis of the month. Revenue breakdown, what worked, what failed, what's next.

### Quarterly Paper / Blog Post

```text
"The Etsy AI Gift Experiment: Q4 2026 Results"
- Revenue: £X
- Lessons: X
- Data points: X
- What I'd do differently
- Open-source dataset release
```

---

## Automation Pipeline

### From git history → content

```text
Git commits (timestamped)
     │
     ▼
commit_parser.py
     │  Extracts: what files changed, commit messages, timestamps
     │  Infers: actions taken, decisions made, progress
     ▼
daily_summary.py
     │  Groups commits by day
     │  Identifies key actions (new listing, price change, SEO update)
     │  Pulls Etsy API data (sales, views, favorites)
     │  Generates natural language summary
     ▼
video_generator.py
     │  Takes daily summary
     │  Adds TTS narration (free AI voice)
     │  Pairs with relevant screen captures / mockups
     │  Outputs 30-60 second short
     ▼
weekly_stitcher.py
     │  Combines 7 daily shorts
     │  Adds intro/outro with stats
     │  Outputs "Etsy Money Week X"
     ▼
youtube_upload.py
     │  Uploads with SEO-optimized titles/descriptions
     │  Adds to playlist
     │  Posts to community tab
     ▼
blog_publisher.py
     │  Converts summary to markdown
     │  Posts to blog (substack / ghost / github pages)
     │  Cross-posts key insights to Twitter/X
```

### Key data sources

| Source | What it provides |
|--------|-----------------|
| Git log | Timestamped actions, file changes, decisions |
| Etsy API | Sales, views, favorites, search terms, conversion |
| Prodigi API | Orders, shipping status, costs |
| Our scraper | Market data, competitor movements |
| Koalanda (free) | 30-day sales spot checks |

### Content is generated, not performed

The videos don't need:
- A face
- A studio
- Editing skills
- A script

They need:
- A screen recording of the dashboard
- A voice summarizing what happened
- Stats on screen

AI generates the script from git + API data. AI generates the voice. We stitch and upload.

---

## Blog / Newsletter

### Platform: Substack or Ghost (free tier to start)

### Format: "The £0 → £1M Etsy Experiment"

```text
Weekly posts:
- Revenue report
- What I launched
- What worked / didn't
- Key insight of the week
- Open questions

Monthly posts:
- Full P&L breakdown
- Tool progress update
- Market analysis
- What's next

Quarterly posts:
- Paper-style analysis
- Dataset release
- Model accuracy update
- Strategic pivots
```

### The transparency advantage

> "We're completely upfront about this as a thesis. Here's the plan. Here's the data. Here's what's working. Here's what's failing. Watch us do it in real time."

Nobody does this. Everyone shows the highlight reel. We show the raw log.

---

## The Mini-Paper

### Title: "Building an Etsy Business with AI: A Real-Time Experiment"

```text
Abstract:
We document a 24-month experiment building personalized gift businesses
on Etsy using AI video generation, starting from £0. Daily timestamped
logs track actions, decisions, revenue, and failures. We release the
complete dataset as an open resource for researchers studying
entrepreneurship, marketplace dynamics, and AI-assisted commerce.

Key findings (preliminary):
- AI video personalization creates a new product category on Etsy
- Review velocity is the strongest predictor of sales (5.1x difference)
- Age milestone gifts convert 3x better than generic occasions
- The content flywheel (document → audience → sales) compounds
- Even failed experiments produce valuable timestamped data

Dataset:
- Daily git commits (timestamped actions)
- Etsy API snapshots (listings, sales, views, favorites)
- Market snapshots (competitor data, keyword trends)
- Revenue data (actual P&L per listing)
- Content performance (views, engagement, conversion)
```

This paper doesn't need to be published in a journal. It needs to be:
1. Searchable (Google-indexed)
2. Citable (other creators reference it)
3. Useful (people actually learn from it)

---

## The Audience Flywheel

### Who watches

| Segment | What they want | What we give them |
|---------|---------------|-------------------|
| Aspiring Etsy sellers | "How do I start?" | Real daily log of someone doing it |
| AI/tech enthusiasts | "Can AI actually make money?" | Hard numbers, no hype |
| Side-hustle seekers | "What actually works?" | Timestamped evidence, not guru BS |
| Content creators | "How do I build in public?" | Blueprint for automated content |
| Researchers | "What are marketplace dynamics?" | Open dataset |

### What the audience produces

| Audience size | What it enables |
|--------------|-----------------|
| 100 subscribers | Feedback loop, early testers |
| 1,000 subscribers | First tool beta users |
| 10,000 subscribers | Consulting inbound, sponsor interest |
| 100,000 subscribers | Tool becomes the default Etsy research platform |
| 1,000,000 subscribers | Book deal, speaking, the whole thing |

### Content → revenue paths

| Path | When | Revenue |
|------|------|---------|
| Etsy store sales | Month 1+ | Direct revenue |
| Tool subscriptions | Month 3+ | SaaS revenue |
| Consulting | Month 6+ | £150/hour |
| Course | Month 9+ | £299 "How to Build a £100K Etsy Shop" |
| Sponsorships | Month 6+ | AI tools, POD services, Etsy apps |
| Book | Month 12+ | "The AI Etsy Experiment" |
| Speaking | Month 12+ | conferences, podcasts |

---

## Daily Workflow

```text
Morning (30 min):
  1. Check overnight Etsy sales (API)
  2. Review git log from yesterday
  3. AI generates daily summary
  4. Record 30-sec video (phone/screen)
  5. Upload YouTube Short + blog post

During day (real work):
  - Build listings
  - Run scraper
  - Iterate on tool
  - Respond to comments

Evening (15 min):
  1. Commit what I did today
  2. Update dashboard
  3. Schedule tomorrow's content
```

**Total content creation time: ~45 minutes/day.**

Everything else is automated or is the actual work being documented.

---

## Naming

### YouTube channel

Options:
- "£0 to £1M" — clear, searchable, aspirational
- "The Etsy Experiment" — clear, but generic
- "AI Etsy" — too narrow
- "Build in Public: Etsy" — good for community

**Recommendation:** "£0 to £1M" — it's the journey people follow.

### Blog / Newsletter

**"The £0 → £1M Etsy Experiment"** — matches the YouTube.

### The paper

**"Building an Etsy Business with AI: A Real-Time Experiment"** — academic enough to be taken seriously, specific enough to be found.

---

## Risk: What if people copy us?

They should.

The point isn't to hoard the strategy. The point is:
1. We do it first → we have the data first
2. We publish the data → we become the authority
3. We build the tool → we capture the value
4. Copying us validates our thesis → more audience

The best moat is being the source of truth, not the only player.

---

## Success Metrics

| Metric | Month 1 | Month 6 | Month 12 | Month 24 |
|--------|---------|---------|----------|----------|
| YouTube subscribers | 50 | 5,000 | 50,000 | 500,000 |
| Blog subscribers | 20 | 2,000 | 20,000 | 200,000 |
| Daily views (combined) | 100 | 5,000 | 50,000 | 500,000 |
| Etsy store revenue | £200 | £5,000 | £50,000 | £200,000 |
| Tool users | 0 | 100 | 1,000 | 10,000 |
| Content-related revenue | £0 | £500 | £10,000 | £100,000 |
| Total revenue | £200 | £5,500 | £60,000 | £300,000 |

---

*The experiment is the content. The content is the business. The business validates the content. Even if the Etsy stores fail, the timestamped dataset of someone trying — with all the failures documented — is itself valuable. There is no way to lose by publishing honestly.*
