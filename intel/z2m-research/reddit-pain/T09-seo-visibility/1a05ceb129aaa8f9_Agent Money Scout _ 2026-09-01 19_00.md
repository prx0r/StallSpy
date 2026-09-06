# Agent Money Scout — 2026-09-01 19:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Tue, 1 Sep 2026 08:21:44 -0400
**Message ID:** 1a05ceb129aaa8f9

---

Agent Money Scout — 2026-09-01 19:00

NEW THIS RUN

1) BTNOMB Bounty Board — https://bounty.btnomb.com/
What the agent does: Builds agent/devtools products from posted briefs, including MCP servers, AI code review, meeting-to-CRM, synthetic user testing, API-key rotation, voice-to-Jira, LLM observability, changelog generation, and email triage.
Who pays: Bounty posters; advertised settlement is USDC on Base.
Verified economics: Primary board currently shows 11 open bounties and $3,000 total bounty value. Three open listings already show public bids: MCP/Postgres server lowest bid $200; AI code reviewer lowest bid $200; LLM observability dashboard lowest bid $200; AI changelog writer lowest bid $5. BTNOMB charges 5% on payouts and $0.10 USDC to unlock a full brief.
Important caveat: the board explicitly says no payout has yet been executed on the board, and several submitted/negotiating listings are marked NOT FUNDED / DO NOT START. Treat only escrow-backed OPEN listings as executable.
Tools/account: Base wallet, USDC for brief unlock, GitHub/deployment stack, REST/API or wallet-signature support.
Autonomy: 10/10. The API supports free listing/preview, x402 brief unlock, claim, submit, counter-offer and webhook subscriptions.
Exact first action: GET /api/bounties, batch-preview the 11 open listings, check which are actually escrow-funded, then bid/claim the smallest clearly testable product. The changelog writer is the lowest-risk visible entry point; the $200 MCP/Postgres and observability jobs are the higher-value targets.
Constraints: 72-hour claim TTL; wallet signatures required; only work funded listings.
Ease first $5: 7/10. Repeatability: 9/10 if first payouts validate.

2) BotBounty.ai — https://www.botbounty.ai/
What the agent does: Code, research, writing, scraping/ETL and automation bounties.
Who pays: Bounty posters through smart-contract escrow; payout advertised in ETH on Base L2.
Verified economics: Site states a $10 minimum bounty for solvers, secure escrow and 90% auto-verification. Current public bounty page presently shows 0 live / 0 completed, so there is no executable inventory at this exact check.
Tools/account: No signup required for agent API; curl skill.md then GET /api/agent/bounties.
Autonomy: 10/10.
Exact first action: Add the endpoint to the hourly scanner and trigger only when a live bounty >= $10 appears.
Constraints: Competition model means best solution wins; do not spend compute when the board is empty.
Ease first $5 today: 0/10. Repeatability potential: 9/10.

3) Project Hunter — https://projecthunter.ai/
What the agent does: Build custom business AI agents and automations—sales outreach, support, enrichment, research bots, data pipelines.
Who pays: Businesses posting competitive bounties.
Verified economics: Primary page currently advertises an active AI Sales Outreach Agent bounty with reward 750 and 8 developers competing. It also claims DataMaster_AI won $750, 500+ agents built, 200+ developers and $500K+ bounties paid. Those aggregate numbers are first-party claims, so treat them as unverified until a withdrawal is demonstrated.
Tools/account: Project Hunter developer account, coding/automation agent, deployment and integration tools.
Autonomy: 7/10 because delivery/approval is project-style rather than pure machine settlement.
Exact first action: Open the active AI Sales Outreach Agent brief, verify whether the reward is USD and escrow-funded, then decide if the CRM/outreach integration can be completed within the contest economics. Avoid ToS-violating bulk LinkedIn automation; keep any outreach compliant and human-approved.
Constraints: Competitive bounty; platform/client acceptance; outreach platform rules.
Ease first $5: 5/10. Repeatability: 8/10 if payout claims validate.

4) BaseBounty — https://www.basebounty.app/
What the agent does: x402-native coding, design and data bounties on Base, with MCP/SDK/REST support and ERC-8183 escrow / ERC-8004 reputation.
Who pays: Bounty posters.
Verified economics: Six total posted. Current visible jobs are only $1 each: Twitter/X banner, TypeScript Pinata snippet, and 200-row ETH job-posting CSV. Discovery transactions are about $0.01.
Tools/account: Base wallet with USDC and a little ETH for gas; npx basebounty-mcp available.
Autonomy: 10/10.
Exact first action: Integrate discovery but hard-reject reward < $5.
Constraints: Some jobs require bonds; Base gas; do not violate target-site scraping/ToS.
Ease today: 1/10. Repeatability: 9/10 if bounty budgets rise.

5) ClawFreelance — https://www.clawfreelance.com/en
What the agent does: Aggregated open-source issues, paid bounties and project work; code agents claim, submit PRs and get verified.
Who pays: Direct posters / external bounty sources; crypto settlement advertised as USDC, ETH or platform tokens.
Verified economics: Primary page currently displays TASK-042 Fix auth bug $500 USDC and TASK-044 Optimize DB $250 USDC, alongside claimed 2,847 agents, $1.2M earned, 12,453 completed tasks and 847 open bounties. The headline figures are first-party claims, so independently verify the underlying task and escrow before execution.
Tools/account: @clawfreelance CLI, agent registration, wallet, GitHub.
Autonomy: 10/10.
Exact first action: claw tasks search --min-reward 100 --status open; inspect TASK-042/TASK-044 and verify they correspond to real funded tasks rather than illustrative UI.
Constraints: Reward type may vary; only accept USDC/ETH with verifiable funding; respect repo contribution rules.
Ease first $5: 6/10 if tasks verify. Repeatability: 9/10.

6) AI Agent Marketplace — https://ai-agentmarketplace.ai/
What the agent does: List specialized agents for content, leads, research, code and document/data tasks; jobs dispatch via webhook.
Who pays: Marketplace customers via Stripe Connect escrow.
Verified economics: Provider keeps 88%, but provider plan costs $45/month. Current primary page says “No agents listed yet.” There is no buyer-liquidity evidence strong enough to justify paying the listing fee now.
Tools/account: Provider subscription, Stripe Connect, hosted webhook agent.
Autonomy: 9/10 after setup.
Exact first action: Do not pay $45/month yet. Watch until there is visible independent buyer activity or list only if you already have a profitable external service and can treat it as another channel.
Constraints: Stripe/KYC/geography.
Ease today: 0/10. Repeatability potential: 7/10.

STILL ACTIVE FROM PRIOR RUNS

7) MoltJobs — https://moltjobs.io/open-jobs
Current primary listing: 5 USDC to turn three live external job postings into ready-to-fund MoltJobs specs and contact the buyer. Every job is funded in Base-USDC escrow; platform fee 5%; 72-hour review window; agent API/CLI/MCP/webhooks are live.
What the agent does: Research, coding/data jobs and verifiable artifacts.
Who pays: Job poster via Base-USDC escrow.
Tools/account: MoltJobs agent/API key; some jobs require machine-graded certification.
Autonomy: 9/10.
First action: Poll GET /v1/jobs?status=OPEN and prefer the next >=$5 pure research/code/data task rather than outreach-heavy work.
Constraints: Certification may gate bids; contact/outreach tasks must remain targeted and compliant.
Ease: 8/10. Repeatability: 9/10.

8) Complete Codes — https://www.complete.codes/en/agents
Agent does: Finds funded GitHub repos, solves reactive issues or proposes allowed proactive improvements, submits PRs and earns Base-USDC automatically on merge.
Who pays: Repo sponsor/maintainer funding the Sprint.
Verified economics: Paid sprint payout = remaining pool x slider; examples on primary site show roughly $20/$100/$400 per merge from a $1,000 pool depending on slider. Public discovery requires no auth and supports min_payout filters.
Tools/account: GitHub/coding agent. Wallet created automatically through Web3Auth.
Autonomy: 10/10 discovery/execution; maintainer controls merge.
First action: GET https://api.complete.codes/v1/sprints?status=active&min_payout=5&sort=payout, then choose a repo with reproducible issues, good CI and active maintainers.
Constraints: No self-merges; anti-gaming limits; only merged work pays.
Ease: 8/10. Repeatability: 10/10.

9) AgentGigs — https://www.agentgigs.io/
Agent does: Browse, apply, quote, deliver and receive payouts entirely via REST after two one-time human steps.
Who pays: Job posters through Stripe Connect escrow.
Verified current architecture: API returns jobs with budget/match score; independent proofers can verify work. Prior live runs surfaced $300–$750 research work and a completed $465 agent payout.
Tools/account: One email confirmation, Stripe Connect KYC/bank connection, API key.
Autonomy: 9/10.
First action: GET /api/agent/jobs/available and filter budget >=$5, high match score, objective acceptance.
Constraints: Stripe geography/KYC; confidentiality.
Ease: 8/10. Repeatability: 9/10.

10) dealwork.ai — https://dealwork.ai/
Agent does: General digital contract work with escrow and AI-to-AI contracting.
Who pays: Human or AI requester.
Recent verified primary state: 2.6K workers, 162 open tasks, 264 completed and 83 verified reviews; prior documented examples include an $80 AI-delivered API and $5 autonomous AI-to-AI contract. AI-to-AI fee 3%.
Tools/account: dealwork worker integration/account.
Autonomy: 9/10.
First action: Ingest all open tasks and rank by acceptance test, competition and execution cost.
Constraints: Follow task-specific platform/identity rules.
Ease: 9/10. Repeatability: 9/10.

11) AgentPact — https://agentpact.xyz/
Agent does: Post offers/needs, match, negotiate milestones, deliver and settle Base-USDC deals through MCP/Python/npm.
Who pays: Other agents or humans.
Verified indexed state: 153 active offers, 206 open needs, 19 live deals, 638 agents.
Tools/account: Free API registration; wallet only needed for paid settlement.
Autonomy: 10/10.
First action: Post a tightly scoped $5 offer such as API smoke testing, CSV/data validation or source-backed research while 
