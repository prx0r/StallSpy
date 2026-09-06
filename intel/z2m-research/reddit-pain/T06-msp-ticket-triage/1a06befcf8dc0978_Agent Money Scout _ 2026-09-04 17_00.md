# Agent Money Scout — 2026-09-04 17:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Fri, 4 Sep 2026 03:21:13 -0700
**Message ID:** 1a06befcf8dc0978

---

# Agent Money Scout — Security-Only — 2026-09-04 17:00

## NEW THIS RUN

### 1. Veda — Immunefi bug bounty — up to $1,000,000
URL: https://immunefi.com/bug-bounty/veda/information/

Live since Jan 21, 2026; updated Aug 18, 2026. Critical smart-contract bugs pay 10% of directly affected funds up to $1M, with a $100,000 critical minimum; high pays $10,000–$25,000. PoC and KYC required. Agent role: ingest scoped contracts/docs/audits, build call/state graph, run static/fuzz/invariant checks, rank suspicious paths, construct reproducible PoC in a forked/test environment, then human-review before submission. Who pays: Veda via Immunefi, in USDC on Ethereum. First action: clone the scoped code and build a known-issue exclusion corpus before hunting. Autonomy 8/10. Ease first $5: 2/10. Repeatability 9/10.

### 2. 1inch Smart Contracts — Immunefi — $100 to $500,000
URL: https://immunefi.com/bug-bounty/1inch-SmartContracts/information/

Live since Jun 11, 2026; updated Aug 14, 2026. Critical: $30,000–$500,000; high: $10,000–$30,000; medium: $2,000–$10,000; low: $100–$2,000. Scope includes Limit Order Protocol, Settlement, token plugins, farming, delegating and cross-chain components. PoC + KYC required. Agent fit is strong because the low/medium bands make smaller validated findings economically meaningful. First action: map each scoped repository/commit to attack-surface tests and search for cross-contract authorization/accounting inconsistencies. Autonomy 8/10. Ease 4/10. Repeatability 9/10.

### 3. Ether.fi — Immunefi — websites/apps + contracts, up to $500,000
URL: https://immunefi.com/bug-bounty/etherfi/information/

Updated Sep 1, 2026. Smart contracts: critical $10,000–$500,000; high $5,000–$15,000; medium $1,000–$5,000; low $1,000. Websites/apps: critical $5,000–$25,000, high $5,000, medium $3,000, low $1,500. This is especially suitable for a mixed agent pipeline because it supports web-app attack-surface work in addition to Solidity. PoC + KYC required. First action: separate web and contract scopes, then run evidence-preserving passive recon and source-assisted checks before any active testing. Autonomy 8/10. Ease 5/10. Repeatability 9/10.

### 4. Babylon Labs — Immunefi — up to $500,000
URL: https://immunefi.com/bug-bounty/babylon-labs/information/

Updated Sep 3, 2026. Blockchain/DLT critical: $20,000–$500,000; high: $5,000–$15,000. Stack includes Go, TypeScript, JavaScript and Rust, giving a coding agent more leverage than Solidity-only hunting. PoC, KYC and arbitration rules apply. First action: diff recent releases and prioritize consensus/state-transition and staking/slashing boundaries. Autonomy 8/10. Ease 3/10. Repeatability 9/10.

### 5. CapyFi — Immunefi — $1,000 to $1,000,000
URL: https://immunefi.com/bug-bounty/capyfi/information/

Updated Aug 19, 2026. Critical $50,000–$1M; high $10,000–$50,000; medium $5,001–$10,000; low $1,000–$5,000. The lower-severity floor is attractive: even a valid low can clear $1K. PoC + KYC required. First action: build Compound-v2-derived invariant tests and concentrate on protocol-specific changes rather than re-auditing inherited code blindly. Autonomy 8/10. Ease 4/10. Repeatability 9/10.

### 6. Wormhole — Immunefi — up to $1,000,000
URL: https://immunefi.com/bug-bounty/wormhole/information/

Updated Aug 12, 2026. Blockchain/DLT and smart-contract critical findings pay $100,000–$1M; high $10,000–$100,000; medium $2,000–$10,000; low up to $2,000. Stack spans Go, Move, Python, Rust and Solidity. PoC + KYC required. Agent value: cross-language static analysis, message/state-machine modeling, serialization and verification-path differential testing. First action: focus on one narrow subsystem and its trust boundary rather than the whole bridge. Autonomy 7/10. Ease 2/10. Repeatability 10/10.

### 7. Sei — Immunefi — $1,000 to $500,000
URL: https://immunefi.com/bug-bounty/sei/information/

Updated Aug 31, 2026. Critical $50,000–$500,000; high $25,000; medium $5,000; low $1,000. Go/Rust chain scope. PoC, KYC and arbitration enabled. First action: construct deterministic state-transition/property tests against scoped components and diff recent security-relevant changes. Autonomy 8/10. Ease 3/10. Repeatability 9/10.

### 8. Upwork — Pen Tester Wanted for Complex SaaS Platform — $500
URL: https://www.upwork.com/freelance-jobs/apply/Pen-Tester-Wanted-for-Complex-SaaS-Platform_~022094333789026655904/

Active worldwide job. Buyer wants authentication, authorization, tenant isolation, privilege escalation, API security, data exposure and business-logic abuse tested on a complex multi-tenant SaaS. Client has $24K prior spend and 84 hires; 50+ proposals but 0 interviews at crawl. Agent workflow: supplied scope/test accounts -> endpoint/role matrix -> automated checks -> targeted human-approved active tests -> reproductions -> remediation report. First action: submit a scope-driven methodology emphasizing tenant-boundary and authz testing. Only test explicitly authorized assets. Autonomy 7/10. Ease 6/10. Repeatability 10/10.

### 9. Upwork — Independent B2B SaaS Audit + Remediation Plan — $15–$45/hr
URL: https://www.upwork.com/freelance-jobs/apply/Independent-Audit-Remediation-Plan-for-live-B2B-SaaS-Platform_~022094433098558907637/

Active worldwide job; safe preview/test environment only, no production credentials. Scope includes role separation/IDOR, injection/input handling, PII/media handling, destructive-operation safety, rate limiting, Postgres/object storage and a retest. Client has $104K spend. Strong agent fit because every finding needs severity, reproduction, root cause and fix order. OSCP strongly preferred and case studies/sample report requested. First action: only apply if you can truthfully satisfy the credentials/evidence requirement. Autonomy 8/10. Ease 5/10. Repeatability 10/10.

### 10. Upwork — Security Check for Vibe-Coded App — $40–$120/hr
URL: https://www.upwork.com/freelance-jobs/apply/Security-Check-for-Vibe-Coded-App_~022094796360849919732/

Active worldwide security review for an AI/vibe-coded application. This is a rapidly growing niche and is highly agentable: stack fingerprint -> auth/access review -> public data/secrets -> dependency/SAST -> API abuse cases -> prioritized fixes. 50+ proposals, 7 interviews. First action: pitch a bounded launch-readiness audit with explicit read-only/default-safe testing. Autonomy 9/10. Ease 7/10. Repeatability 10/10.

### 11. Upwork — Cybersecurity audit of two new website platforms — $35–$50/hr
URL: https://www.upwork.com/freelance-jobs/apply/Cyber-security-audit-new-website-platform_~022094748073735058079/

Active UK buyer wants external testing of Next.js and Laravel raffle platforms, plus payment-flow testing and abuse cases such as leaked winning numbers, credit/checkout manipulation, privacy leaks and claim exploitation. Client has $27K prior spend. This is semi-autonomous only: agent can enumerate/test in authorized staging and produce evidence, but payment/competition-flow abuse tests need strict human-controlled scope. First action: propose test matrix + explicit rules of engagement. Autonomy 6/10. Ease 5/10. Repeatability 9/10.

### 12. Upwork — Ethical Hacking Technical Editor — $150
URL: https://www.upwork.com/freelance-jobs/apply/Ethical-Hacking-Technical-Editor-required_~022094698961332493342/

Active worldwide $150 fixed job to technically review/refine an ethical-hacking book. Client has $171K historical spend and 840 hires. This is one of the easiest security-adjacent agent jobs: verify commands/claims against authoritative references, identify unsafe/inaccurate sections, tighten terminology and flag unsupported claims. Requires genuine ethical-hacking expertise; do not pretend credentials. First action: offer a sample technical-accuracy pass on one chapter. Autonomy 9/10. Ease 9/10. Repeatability 7/10.

### 13. Cantina — 46 active bug-bounty opportunities
URL: https://cantina.xyz/competitions

Cantina's current opportunity page shows 46 bounties and 1 competition in the active/all interface; its researcher docs confirm ongoing bounties and competitions expose payout/status/start-date information. Total platform-reported payouts are in the tens of millions. Specific current bounty amounts were not sufficiently exposed in the crawl, so none are invented. First action: create a researcher account, filter only currently active bounties and rank by language familiarity, scope size and payout. Autonomy 8/10. Ease 4/10. Repeatability 10/10.

### 14. Sherlock — paid security referrals — $500–$1,000 per qualified sale
URL: https://sherlock.xyz/post/introducing-the-2026-sherlock-referral-program

A different security monetization channel: Sherlock pays $1,000 for a qualified Sherlock AI referral, $1,000 for a qualified audit referral and $500 for a bug-bounty referral. No barrier to entry, but the team must not already be in Sherlock's active sales process, the referral must be recorded correctly, and purchase must happen within the 180-day attribution window. No cold-spam referrals: Sherlock explicitly says the team should be expecting the introduction. Agent workflow: identify genuinely relevant protocol teams -> evidence-based security-gap research -> human-approved warm introduction -> attribution tracking. Autonomy 5/10. Ease 5/10. Repeatability 8/10.

## STILL ACTIVE FROM PRIOR RUNS

### 15. Freelancer — AI Vulnerability Scanning Harness — $250–$300
URL: https://www.fi.freelancer.com/projects/ai-automation/vulnerability-scanning-harness

Still indexed as active this week. Buyer wants a defensive CI/CD security harness for an authorized codebase, internal/exposed APIs and cloud configuration, with actionable findings. Best implementation is orchestration rather than inventing scanners: established SAST/SCA/secrets/cloud scanners -> normalize -> dedupe -> confidence/evidence -> AI triage -> remediation report. First action: pitch a scanner-orchestration MVP with a false-positive benchmark. Autonomy 10/10
