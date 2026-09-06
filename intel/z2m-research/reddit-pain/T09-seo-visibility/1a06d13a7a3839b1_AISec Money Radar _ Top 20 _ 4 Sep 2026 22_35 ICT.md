# AISec Money Radar — Top 20 — 4 Sep 2026 22:35 ICT

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Fri, 4 Sep 2026 08:39:59 -0700
**Message ID:** 1a06d13a7a3839b1

---

# AISec Money Radar — Top 20

Fresh scan: 4 September 2026. Ranked by expected value per scarce human hour, with training/reuse value for AISec + /bitt + /mw weighted heavily.

## Executive summary

**Biggest NEW item:** Immunefi’s **Sky (formerly MakerDAO)** bounty was updated **today, Sep 4**, and advertises a **$10M maximum**. It is a huge but hard target; the actionable angle is to diff exactly what changed today before the wider hunter crowd adapts.

**Biggest strategy correction:** **Trishool SN23 is now explorer-labelled abandoned (health 23/100)**. Do not spend TAO there until activity clearly recovers. **RedTeam SN61** is much stronger right now: health 88/100, 45 active miners, ~40.65 TAO/day aggregate miner distribution, no GPU requirement, and challenges directly overlap our security worker.

**Best immediate paid training loop remains 0DIN + Intigriti PWN.** 0DIN pays $500–$15,000 and offers abstract sign-off before the full report; Intigriti’s own program pays up to €13,337 and explicitly provides a PWN test environment with multiple self-created test accounts.

**Best Bittensor adjacent loop:** Ridges SN62 + Gittensor SN74 + RedTeam SN61 + BitSec SN60. Ridges has a 0.0005 TAO burn and local evaluation; Gittensor pays 90% of its OSS contribution pool for merged PRs; RedTeam has strong current emissions; BitSec remains the canonical security-agent benchmark.

**Best product angle this run:** sell the intelligence and regression layer we need internally anyway: (1) x402 `/agent-risk-report`, (2) paid `/attack/latest` machine-readable feed, (3) continuous agent-security regression service. Intigriti’s newly launched CrowdRecon strongly validates that reconnaissance itself has saleable value even before a vulnerability exists.

---

## Top 20

### 1. STILL-HIGH-VALUE — 0DIN GenAI bounty
- Source: https://0din.ai/policy
- Payout: **$500–$15,000**; Low up to $500, Medium $2,500, High $5,000, Severe $15,000.
- Status: ongoing/global.
- Work: model/agent security-boundary violations; current models only.
- Human effort: low–medium. Agent effort: high.
- Upfront cost: low/API usage.
- Constraints: authorized scope, test accounts, confidentiality; ID/tax paperwork for payment.
- Payout probability: **medium** relative to other bounty markets because abstract sign-off reduces wasted effort.
- Reuse/training: **10/10**.
- Next: submit high-level abstracts for our best candidate classes before spending heavily; 0DIN says it responds within 3 business days with scope + likely bounty range.

### 2. STILL-HIGH-VALUE — Intigriti’s own PWN bounty
- Source: https://app.intigriti.com/programs/intigriti/intigriti
- Payout: **€50–€13,337** depending on asset/severity.
- Status: live.
- Work: exploit the platform’s PWN test environment; focus on submission-data access, PII, vertical/horizontal privilege escalation.
- Human effort: low–medium. Agent effort: high.
- Upfront cost: ~zero.
- Constraints: max automated tooling 10 req/s; no DoS/social engineering; follow scope.
- Payout probability: **medium**.
- Reuse/training: **10/10** — unusually good safe end-to-end exploit→report target.
- Next: make this our first autonomous worker acceptance benchmark.

### 3. STILL-HIGH-VALUE — OpenAI Safety Bug Bounty
- Source: https://openai.com/index/safety-bug-bounty/
- Payout: program rewards vary by issue; verify live Bugcrowd award table before hunting.
- Status: public/ongoing.
- Work: reproducible agent hijacking, third-party prompt injection/data exfiltration, harmful agent actions, platform-integrity issues.
- Human effort: medium. Agent effort: high.
- Cost: API/product test cost.
- Constraints: must be in scope; third-party MCP testing must respect third-party ToS; prompt-injection behavior must be reproducible ≥50% for that listed category.
- Payout probability: **medium-low**.
- Reuse/training: **10/10**.
- Next: convert our agent-injection corpus into repeatability tests specifically for Browser/Agent/MCP chains.

### 4. STILL-HIGH-VALUE — Anthropic Model Safety Bug Bounty
- Source: https://support.anthropic.com/en/articles/12119250-model-safety-bug-bounty-program
- Payout: **up to $35,000 per novel universal jailbreak**.
- Status: ongoing; rolling applications via HackerOne.
- Work: universal jailbreaks against Constitutional Classifiers, primarily detailed harmful biological-query set.
- Human effort: medium. Agent effort: high.
- Cost: low after acceptance; Anthropic provides a free model alias for authorized testing.
- Constraints: invite/acceptance + NDA.
- Payout probability: **low–medium**.
- Reuse/training: **9/10**.
- Next: apply and reuse the same adversarial-search engine we use for 0DIN.

### 5. STILL-HIGH-VALUE — OpenAI Bio Bounty
- Source: https://openai.com/index/bio-bug-bounty/
- Payout: **$50,000** for a qualifying universal jailbreak; smaller awards may be given.
- Status: ongoing private program for GPT-5.6 and future frontier models; application route is live on current page.
- Human effort: medium. Agent effort: high.
- Cost: low after access.
- Constraints: application, NDA, tightly scoped challenge.
- Payout probability: **low**, but unusually high leverage if accepted.
- Reuse/training: **9/10**.
- Next: maintain one universal-jailbreak search architecture shared with Anthropic/0DIN.

### 6. STILL-HIGH-VALUE — RedTeam SN61
- Source: https://bittensor.ai/subnets/61
- Payout: current aggregate miner distribution **~40.65 TAO/day**; individual earnings performance-dependent.
- Status: active; health 88/100; 45 active miners; emission rank #7 at scan time.
- Work: bot detection, anti-detect browser detection, humanized bot behaviour, VPN-flow classification, device fingerprinting.
- Human effort: low after setup. Agent effort: high.
- Upfront cost: current burn **~0.07588 TAO** + Docker/inference/dev cost; no GPU required.
- Constraints: originality/similarity thresholds; submissions decay in ~10–15 days; ~24h commit cooldown.
- Payout probability: **medium if locally competitive**.
- Reuse/training: **9/10**.
- Next: reproduce one challenge locally and benchmark before registration.

### 7. STILL-HIGH-VALUE — Ridges SN62
- Source: https://bittensor.ai/subnets/62
- Payout: aggregate miner distribution **~35.51 TAO/day** at scan time.
- Status: active, health 83/100.
- Work: submit a single software-engineering `agent.py`, evaluated on Harbor tasks.
- Human effort: low. Agent effort: very high.
- Upfront cost: burn **0.0005 TAO** + inference; local evaluation supported.
- Constraints: strict task timeout/cost budget and sandbox.
- Payout probability: **medium if benchmark competitive**.
- Reuse/training: **10/10** for exploit→patch worker.
- Next: run our existing coding worker through `ridges miner run-local` before spending anything meaningful.

### 8. STILL-HIGH-VALUE — Gittensor SN74
- Sources: https://docs.gittensor.io/miner.html and https://bittensor.ai/subnets/74
- Payout: aggregate miner distribution **~12.74 TAO/day**; official docs say **90% of OSS contribution emission pool** is for merged PRs.
- Status: active; explorer shows 9 miners; burn about **0.15 TAO**.
- Work: useful merged PRs to recognized OSS repositories; optional GPU serving.
- Human effort: low–medium. Agent effort: very high.
- Upfront cost: registration + GitHub work; no server needed for OSS path.
- Constraints: maintainer acceptance; do not spam PRs; identity/PAT setup.
- Payout probability: **medium if worker can get merges**.
- Reuse/training: **10/10**.
- Next: rank eligible repos by issue clarity, maintainer responsiveness and worker competence; get 3 real merged PRs before optimizing subnet economics.

### 9. STILL-HIGH-VALUE — BitSec SN60
- Source: https://bittensor.ai/subnets/60
- Payout: TAO emissions, performance dependent.
- Status: active; health 54/100; current explorer shows the network itself but 0 active miners in the summarized participation snapshot, so verify exact miner enrollment path before spending.
- Work: agents analyze codebases and output vulnerability reports scored against ground truth.
- Human effort: low. Agent effort: extremely high.
- Cost: Bittensor registration/inference.
- Constraints: benchmark scoring and false-positive quality.
- Payout probability: **unknown until miner path tested**.
- Reuse/training: **10/10**.
- Next: continue treating BitSec as the lab benchmark even if direct mining economics are temporarily awkward.

### 10. NEW TODAY — Sky / MakerDAO Immunefi scope update
- Source: https://immunefi.com/bug-bounty/sky/information/
- Payout: **up to $10,000,000**.
- Status: **updated Sep 4, 2026**.
- Work: DeFi/smart-contract security.
- Human effort: high. Agent effort: high.
- Cost: local fork/test tooling.
- Constraints: Immunefi/program scope; never risk real funds without explicit authorization.
- Payout probability: **low**.
- Reuse/training: **8/10**.
- Next: do not broad-hunt. Diff the Sep 4 scope/code/resource changes and only pursue new attack surface.

### 11. NEW/STRONG-FIT — Aikido Zen security-engine bounty
- Source: https://app.intigriti.com/programs/aikido/aikidoruntime/detail
- Payout: **€150–€3,500** Tier 1.
- Status: live.
- Work: break an embedded runtime security engine designed to block shell injection, SQL injection and related attacks.
- Human effort: low–medium. Agent effort: high.
- Cost: low.
- Constraints: max automated tooling 5 req/s; follow scope.
- Payout probability: **medium**.
- Reuse/training: **9/10** because attacks on security controls improve our red-team worker directly.
- Next: add Aikido as a second controlled web-security curriculum after Intigriti PWN.

### 12. STILL-HIGH-VALUE — Adobe on Intigriti
- Source: https://app.intigriti.com/programs/adobe/adobepublic/updates
- Payout: current program has rewards up to **$15,000** (verify per current asset tier).
- Status: newly migrated Sep 1; ColdFusion submissions temporarily paused Sep 3, other scoped products open.
- Work: Adobe web/product security, including AI-enabled products wher
