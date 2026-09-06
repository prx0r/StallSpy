# Agent Money Scout — 2026-09-03 08:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Wed, 2 Sep 2026 18:25:17 -0700
**Message ID:** 1a064decb9e1f0ae

---

Agent Money Scout — 2026-09-03 08:00

NEW THIS RUN

1) BTNOMB Bounty Board — 11 open bounties / $3,000 total listed bounty value
URL: https://bounty.btnomb.com/
What the agent does: builds concrete developer/agent tools from posted briefs. Current open ideas include a guarded Postgres MCP server, AI contract redliner, agent spending-limit wallet, meeting-to-CRM sync, code reviewer, synthetic-user testing, API-key rotation, Voice-to-Jira, LLM observability, changelog writer, and email triage.
Who pays: bounty posters in USDC on Base. BTNOMB takes 5% on payout.
Payout: the board reports $3,000 total bounty value. Some listings show competing bids (e.g. $200 lowest bids on Postgres MCP/code-review/observability; $5 lowest bid on changelog writer), but the brief unlock costs $0.10 and funding must be individually verified. The board explicitly marks some submitted/negotiating listings as NOT FUNDED; do not start those.
Required: Base wallet, coding/agent-tooling skill, API/backend experience depending on bounty.
Autonomy: 9/10.
First action: inspect the open bounty’s funding/escrow state before paying the $0.10 brief unlock; prioritize objectively testable devtools such as Postgres MCP or changelog writer.
Constraints: only execute funded bounties; avoid sensitive-email/contract workflows without privacy safeguards.
Ease first $5: 6/10. Repeatability: 9/10.

2) BaseBounty — 6 real-USDC bounties on Base, autonomous payout proven
URL: https://www.basebounty.app/
What the agent does: browse, take, submit and get paid for small bounties through MCP/SDK/REST. Current visible examples include a $1 BaseBounty X banner, $1 TypeScript/Pinata snippet, and $1 scrape+dedupe ETH job-postings CSV.
Who pays: bounty posters who lock USDC in ERC-8183 escrow.
Payout: current tasks are mostly $1–$2. The official walkthrough documents an agent autonomously receiving 0.99 USDC from a 1-USDC bounty after the 1% protocol fee.
Required: Base USDC + small ETH gas balance, ERC-8004 identity for agent-only listings; MCP/SDK/REST supported.
Autonomy: 10/10.
First action: run npx basebounty-mcp or query the REST board, then take one low-risk $1 task to validate the full earn loop.
Constraints: some tasks require a worker bond; missed deadlines can forfeit it. Silent posters can be bypassed after 14 days.
Ease first $5: 4/10 at current $1 pricing. Repeatability: 9/10.

3) Upwork — 4-workflow business automation project
URL: https://www.upwork.com/freelance-jobs/apply/Automation-Expert-Needed-Workflow-Automations-Slack-Gmail-Google-Drive-Meet_~022095150095333313585/
What the agent does: eliminate four repetitive marketing tasks using Slack, Gmail, Drive, Meet/Gemini and Wispr Flow, with n8n/Make/Zapier.
Who pays: Upwork client.
Payout: not reliably exposed in the public crawl; no invented number.
Required: SaaS APIs, OAuth, workflow automation, reliability/error handling.
Autonomy: 9/10.
First action: apply with a 4-workflow map showing triggers, state, human checkpoints, retries and outputs.
Constraints: operate only on authorized business accounts/data.
Ease first $5: 7/10. Repeatability: 10/10.

4) Freelancer — Conversational AI / multi-agent jewelry business system — $750–$1,500
URL: https://www.freelancer.com/projects/ai-agent-swarms/conversational-agent-development
What the agent does: build an orchestrator coordinating sales/customer management, inventory/pricing, suppliers, quotes/orders, communications, invoices, prospecting and scheduling.
Who pays: Freelancer client.
Payout: $750–$1,500 advertised.
Required: Python, APIs, agent orchestration, business-state design, likely CRM/inventory integrations.
Autonomy: 8/10.
First action: propose a staged v1 around quote/order/inventory state rather than trying to automate the whole company at once.
Constraints: customer communications and pricing changes should have explicit policy/human gates.
Ease first $5: 7/10. Repeatability: 9/10.

5) Freelancer — Northquill AI slide/narration alignment — $25–$50/hour
URL: https://www.freelancer.com/projects/ai-model-development/refine-alignment-northquill-platform
What the agent does: improve an existing SaaS that takes a PowerPoint plus one continuous narration recording and automatically determines slide-advance timing.
Who pays: Freelancer client.
Payout: $25–$50/hour advertised.
Required: audio alignment, ML/LLM evaluation, Python/media pipeline skills.
Autonomy: 9/10.
First action: propose a measurable benchmark: timestamp-alignment error, slide-boundary precision/recall and failure categories.
Constraints: use client-authorized media only.
Ease first $5: 7/10. Repeatability: 8/10.

6) Freelancer — LiveKit/Asterisk course beta review — $30–$250
URL: https://www.freelancer.com/projects/ai-voice-agents/livekit-asterisk-course-beta-review
What the agent does: execute voice-agent labs end-to-end, record exact errors/version/config issues and provide a structured beta review.
Who pays: Freelancer client.
Payout: $30–$250 advertised.
Required: LiveKit, Asterisk/SIP, Python, Linux/VPS.
Autonomy: 9/10.
First action: apply only if the environment can actually reproduce Asterisk/LiveKit labs; offer trace-backed issue reports.
Constraints: do not claim telephony expertise you cannot demonstrate.
Ease first $5: 6/10. Repeatability: 8/10.

7) Freelancer — AI business-management platform — $1,500–$3,000
URL: https://www.freelancer.com/projects/python/build-custom-powered-business-management
What the agent does: build backend/API/dashboard/auth/data/reporting integrations plus AI/RAG/embeddings, background jobs, monitoring and CI/CD.
Who pays: Freelancer client.
Payout: $1,500–$3,000 advertised.
Required: Python/Go, PostgreSQL, Redis, Docker, RAG, APIs, cloud ops.
Autonomy: 8/10.
First action: bid around a vertical slice: auth + canonical data model + one core workflow + observability.
Constraints: secure credential handling and role-based access are essential.
Ease first $5: 5/10. Repeatability: 9/10.

8) Upwork — n8n multi-app approvals/reporting suite — $550
URL: https://www.upwork.com/freelance-jobs/apply/n8n-Engineer-Multi-App-Business-Suite-Paid-Ads-Content-Approval-Daily-Reporting_~022095096776384726086/
What the agent does: connect 12 platforms, generate rich approval previews, audit Asana tasks, use Slack/Telegram approval buttons + SMS fallback, aggregate ad metrics and generate daily reporting.
Who pays: Upwork client.
Payout: $550 fixed.
Required: n8n, Asana, Slack/Telegram, Twilio, ad APIs, Excel/OneDrive, Google Drive/YouTube.
Autonomy: 9/10.
First action: apply with an architecture separating read-only aggregation from side-effecting actions and manual approval.
Constraints: client joined Sep 2; require a funded milestone before substantial work.
Ease first $5: 6/10. Repeatability: 10/10.

STILL ACTIVE FROM PRIOR RUNS

9) MoltJobs — six 5-USDC jobs still open
URL: https://moltjobs.io/open-jobs
Current primary board shows six 5-USDC jobs with about 17 hours remaining: freelance-task research, durable-hosting guide, delivery-verification benchmark, translation, agent-community mapping and a MoltJobs integration walkthrough. Each is described as funded in USDC on-chain escrow.
Who pays: Parsa Barati via MoltJobs escrow.
Required: API/agent account + research/writing/translation skill depending on task.
Autonomy: 10/10.
First action: claim the simplest task that still says OPEN.
Constraints: deadline is short; verify status before execution.
Ease first $5: 10/10. Repeatability: 9/10.

10) GH Bounty — 5 / 29 / 39 SOL open-source bounties
URL: https://www.ghbounty.com/
Current live feed: solana-labs/web3.js retry logic 5 SOL OPEN; vercel/next.js async generators 29 SOL OPEN; denoland/deno WebGPU texture compression 39 SOL OPEN. LangChain 14 SOL and Supabase 9.8 SOL are reviewing; Tauri 3.5 SOL is paid. Every displayed feed row is described as real Solana-mainnet escrow.
Who pays: maintainers/bounty funders via smart-contract escrow.
Required: GitHub OAuth once, coding skill, Solana wallet; MCP/SDK supported.
Autonomy: 10/10.
First action: reproduce the 5-SOL issue locally and inspect competing PRs before coding.
Constraints: 2.5% protocol fee; contribution must satisfy validator/maintainer criteria.
Ease first $5: 8/10 when technically matched. Repeatability: 10/10.

11) DataBazaar — seven open funded-data opportunities
URL: https://www.databazaar.io/bounties
Current board: $42 MENA cybersecurity leads (0 submissions), $500 clinical-trial outcomes (4), $200 labeled support conversations (2), $400 cross-retailer SKU/pricing (1), $250 EV chargers (11), $300 small-cap fundamentals (5), $100 robotics FMEAs (13).
Who pays: data bounty buyers.
Required: legal/licensed data acquisition, normalization, provenance, QA; API/MCP available.
Autonomy: 9/10.
First action: feasibility-check the $400 SKU/pricing bounty and the $42 zero-submission leads bounty against permitted sources.
Constraints: clinical-trial bounty explicitly requires publicly licensed commercial-use sources; support data must remove/redact PII.
Ease first $5: 7/10. Repeatability: 10/10.

12) AgentGigs — autonomous job API with escrow + Stripe
URL: https://www.agentgigs.io/
What the agent does: browse jobs, apply, deliver and get paid after two one-time human steps (email verification and Stripe Connect KYC). Optional proofers can verify results.
Who pays: job posters funding escrow.
Payout: current public API example shows a $300 budget research-style job; prior runs also surfaced a $300–$750 competitor-landscape listing and a visible $465 completed transfer. Recheck live inventory before assuming availability.
Required: AgentGigs API + Stripe Connect.
Autonomy: 9/10.
First action: query /api/agent/jobs/available and rank by payout × acceptance probability / runtime.
Constraints: KYC/bank connection is a one-time human step.
Ease first $5: 8/10. Repeatability: 9/10.

13) BaseBounty / x402 autonomous work rail — now worth permanent polling
URL: https://www.basebounty.app/start
The platform support
