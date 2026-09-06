# Agent Money Scout — 2026-09-04 11:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Thu, 3 Sep 2026 21:21:05 -0700
**Message ID:** 1a06aa61ac40a3ed

---

# Agent Money Scout — 2026-09-04 11:00

## NEW THIS RUN

### 1) BTNOMB Bounty Board — 11 open Base-USDC bounties
URL: https://bounty.btnomb.com/
What the agent does: Browse bounties by API, unlock the full brief for $0.10 USDC via x402, claim with an EIP-191 wallet signature, build the requested product, submit a GitHub URL, negotiate/counter-offer, and receive Base USDC if approved.
Who pays: bounty posters.
Payout/pricing: Board currently reports 11 open bounties and $3,000 total bounty value. Visible examples include a Postgres MCP server with one bid at $200; an AI code reviewer with one bid at $200; an LLM observability dashboard with one bid at $200; and an AI changelog writer with one bid at $5. These are bids, not guaranteed bounty amounts. BTNOMB charges 5% on payout; unlocking a full brief costs $0.10 USDC.
Required: Base wallet, USDC, coding/agent skills, GitHub.
Autonomy: 10/10.
First action: GET /api/bounties, batch-preview the open listings, then unlock only the most testable one.
Constraints: Important caveat: BTNOMB states that no payout has yet been executed on this board, and some submitted/negotiating listings are explicitly unfunded/demo listings. Do not start work unless the selected listing is actually funded/claimable.
Ease first $5: 5/10. Repeatability: 9/10.

### 2) Upwork — Google Workspace Scheduling System — $2,500 fixed
URL: https://www.upwork.com/freelance-jobs/apply/Google-Workspace-Scheduling-System_~022095644377205296653/
What the agent does: Convert an existing Excel/VBA scheduling prototype for a home-visit healthcare practice into a cloud multi-user system supporting office scheduling, doctor mobile view, patient eligibility rules, and future route planning.
Who pays: Upwork client.
Payout: $2,500 fixed.
Required: Google Apps Script, Google Workspace, JavaScript; ability to handle healthcare workflow data appropriately.
Autonomy: 8/10.
First action: Apply with a migration plan: current workbook/state model → canonical data model → Apps Script/API layer → multi-user UI → eligibility assertions → scheduling tests.
Constraints: Worldwide. Do not expose real patient data to unapproved AI services; use approved/synthetic samples until data-handling terms are clear.
Ease first $5: 6/10. Repeatability: 9/10.

### 3) BotBounty.ai — API-native ETH bounty marketplace
URL: https://www.botbounty.ai/
What the agent does: GET /api/agent/bounties, claim a code/research/data/automation task, execute it, submit the output and get paid in ETH on Base.
Who pays: bounty posters.
Payout: Platform advertises a $10 minimum bounty and funded smart-contract escrow; no specific current bounty amount was sufficiently exposed in the public page, so I am not inventing one.
Required: HTTP/API-capable agent, Base wallet, relevant task skills.
Autonomy: 10/10.
First action: curl https://botbounty.ai/skill.md and inspect the current /api/agent/bounties feed.
Constraints: Only spend compute after confirming the bounty is live and funded.
Ease first $5: 5/10. Repeatability: 9/10.

### 4) Hober — scored Base-USDC job marketplace
URL: https://www.hober.dev/
What the agent does: Register as a merchant, discover open jobs through MCP/SDK, bid, deliver, receive an evaluator score and settle from escrow.
Who pays: job posters.
Payout: Job-specific. Hober’s mechanism example shows a 250-USDC settlement, but that is an example lifecycle, not a verified open job. Current platform fee is 5%, hard-capped on-chain at 10%.
Required: API key, MCP/SDK integration; no transaction signing is required in agent code because the gateway settles with its own keys.
Autonomy: 10/10.
First action: Register one narrowly defined worker and inspect the Open Jobs feed before spending compute.
Constraints: Base mainnet escrow is live; Solana escrow is still devnet.
Ease first $5: 4/10. Repeatability: 10/10 potential.

### 5) Upwork — AI Automation Specialist for Recruitment Workflow
URL: https://www.upwork.com/freelance-jobs/apply/Automation-Specialist-for-Recruitment-Workflow_~022095117861253926413/
What the agent does: Build an automated incoming-lead/recruitment workflow: ingest → classify → route → update system-of-record → follow-up → exceptions.
Who pays: Upwork client.
Payout: Not reliably exposed in the live crawl, so none invented.
Required: workflow automation, APIs, likely n8n/Make/Zapier/LLM tooling depending on client stack.
Autonomy: 9/10.
First action: Apply around a small working vertical slice with clear failure handling and human review where appropriate.
Constraints: Use client-authorized candidate data only; avoid automated high-impact employment decisions without human review.
Ease first $5: 6/10. Repeatability: 10/10.

### 6) Upwork — Claude Code API Integration Debugging / Python Automation
URL: https://www.upwork.com/freelance-jobs/apply/Claude-Code-API-Integration-Debugging-Python-Automation-Script-Fix_~022095210022877776945/
What the agent does: Debug an existing Python automation that uses Claude for data processing and is failing at backend API integration.
Who pays: Upwork client.
Payout: Not reliably exposed.
Required: Python, API debugging, Anthropic/Claude integration, logs/tests.
Autonomy: 9/10.
First action: Ask for the failing trace/repro inside the platform, then run: reproduce → isolate contract mismatch → patch → regression test → delivery evidence.
Constraints: Never request raw secrets in chat; use Upwork/client-approved credential handling.
Ease first $5: 8/10. Repeatability: 9/10.

### 7) Upwork — Automation of Report Creation — $500 fixed
URL: https://www.upwork.com/freelance-jobs/apply/Automation-Report-Creation_~022094695697305215555/
What the agent does: Automate 10–15 monthly material-consumption reports currently maintained in Excel/Google Sheets.
Who pays: Upwork client.
Payout: $500 fixed.
Required: Excel/Google Sheets, data normalization, formulas/scripts, report QA.
Autonomy: 10/10 once inputs/outputs are specified.
First action: Propose one report as a paid/acceptance-tested template, then generalize across the remaining reports.
Constraints: Preserve source data and make outputs auditable; no need for LLMs unless unstructured text exists.
Ease first $5: 8/10. Repeatability: 10/10.

### 8) Upwork — AI Video Generation for YouTube Channel
URL: https://www.upwork.com/freelance-jobs/apply/Video-Generation-for-YouTube-Channel_~022095280017792984843/
What the agent does: Generate/edit recurring videos for an AI/tech/productivity YouTube channel from topic → research → script → voice/visuals → edit → QA.
Who pays: Upwork client.
Payout: Not reliably exposed.
Required: AI-video tooling, editing, script/research pipeline, copyright-safe assets.
Autonomy: 8/10.
First action: Produce a short sample workflow and a cost-per-video estimate, with human approval before publishing.
Constraints: Use licensed/generated assets and comply with YouTube disclosure/content rules.
Ease first $5: 6/10. Repeatability: 9/10.

### 9) Upwork — 87 short vertical explainer videos
URL: https://www.upwork.com/freelance-jobs/apply/Editor-for-series-short-vertical-explainer-videos-talking-head-captions_~022095138698004253745/
What the agent does: Repeatedly process talking-head footage into 9:16 financial explainers with consistent captions, pacing, cleanup and exports.
Who pays: Upwork client.
Payout: Not reliably exposed.
Required: video editing, transcription/captioning, batch templates and QC.
Autonomy: 9/10 after style lock.
First action: Offer one representative edit, then automate transcript/cut/caption/export while retaining human QC.
Constraints: Financial content should not be altered in meaning by automated editing.
Ease first $5: 7/10. Repeatability: 10/10.

### 10) Upwork — GoHighLevel CRM setup — $5 paid wedge
URL: https://www.upwork.com/freelance-jobs/apply/Google-Ads-Manager-Google-Ads-PPC-Campaign-Setup-Management_~022095455009997339523/
What the agent does: Despite the misleading job title, the live description asks for GoHighLevel CRM configuration: pipelines, automations, workflows, lead routing and process improvements.
Who pays: Upwork client with $3K prior spend and 170 hires.
Payout: $5 fixed; ongoing project.
Required: GoHighLevel/CRM automation.
Autonomy: 9/10.
First action: Only accept if the $5 milestone is genuinely a tiny paid test; propose one pipeline/automation, not a full CRM rebuild.
Constraints: Avoid scope creep at this price.
Ease first $5: 10/10. Repeatability: 6/10 unless converted.

## STILL ACTIVE FROM PRIOR RUNS

### 11) AgentGigs — SaaS competitor research — $300–$750
URL: https://www.agentgigs.io/
Still active: Fresh primary verification still shows “Analyze competitor landscape for SaaS product” OPEN at $300–$750 with only 3 applicants. AgentGigs also shows a separate delivered job independently scored 87/100 followed by a $465 transfer to an agent.
Agent work: competitor discovery → primary-source pricing/features → structured comparison → uncertainty/evidence → deliver.
Who pays: job poster through escrow.
Required: one-time email verification + Stripe Connect KYC, then pure API.
Autonomy: 9/10.
First action: Apply through the API with a primary-evidence-first methodology and a competitive proposed price.
Constraints: Stripe/KYC availability by jurisdiction.
Ease first $5: 9/10. Repeatability: 9/10.

### 12) Superteam Earn — hidden AGENT_ONLY work + $200 Agentic Engineering grant
URL: https://superteam.fun/earn/agents
Grant URL: https://superteam.fun/earn/grants/agentic-engineering
Still active: Official agent API returns AGENT_ALLOWED and AGENT_ONLY listings; AGENT_ONLY listings are hidden from normal feeds. Separately, the Agentic Engineering grant offers $200 USDG to build a working Solana product, 50% upfront and 50% after shipping; page reports $60.8K approved so far across 304 recipients.
Agent work: discover eligible listing → build/submit artifact. For grant: propose Solana product → ship with AI coding tools.
Who pays: Superteam/sponsors.
Required: agent registra
