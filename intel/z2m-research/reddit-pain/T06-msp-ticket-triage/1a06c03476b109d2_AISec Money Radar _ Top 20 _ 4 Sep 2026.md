# AISec Money Radar — Top 20 — 4 Sep 2026

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Fri, 4 Sep 2026 03:42:29 -0700
**Message ID:** 1a06c03476b109d2

---

# AISec Money Radar — Top 20

## Executive summary

The best immediate economic loop is now clear: **0DIN + OpenAI Safety + Anthropic Safety + Bittensor SN60/SN61/SN62/SN74**. These all pay for work that directly trains the same security/coding worker.

Two genuinely new discoveries deserve attention today:

- **SN61 RedTeam** pays miners in TAO for successful bypasses against bot-detection systems. This is almost a direct Bittensor version of our adversarial-security lab.
- **SN62 Ridges** pays competing software-engineering agents evaluated in sandboxes under fixed inference budgets; it is a strong adjacent training/economic loop for the same coding worker.

Also new: OpenAI announced **Daybreak for Frontline Defenders on Sep 3**, committing $1B in subsidized cyber-model access, training, technical support and partnerships. This is not a cash bounty, but could dramatically lower our model/compute cost and create a future partnership/sales channel if AISec qualifies as a supporting organization.

I rank below by expected value per scarce human hour, with payout probability kept qualitative because exact probability cannot be responsibly estimated before we have our own submission history.

---

## 1. STILL-HIGH-VALUE — Mozilla 0DIN AI Bug Bounty
Source: https://www.0din.ai/scope
Payout: $500 low / $2,500 medium / $5,000 high / up to $15,000 severe.
Status: Live; 44 model targets + 11 app targets shown today.
Work: Novel GenAI/agent security boundary breaks: prompt injection, tool abuse, sandbox/interpreter failures, data/context exfiltration, etc.
Human effort: Low–medium once worker harness exists.
Agent effort: High, ideal for automated mutation/reproduction.
Upfront cost: Mostly inference/test accounts; unknown by target.
Constraints: Must obey 0DIN scope; original/unreported; latest model; KYC/ID for payment.
Payout probability: Medium relative to frontier bounties; 0DIN says most submissions are rejected, but publishes researcher payout/validation histories.
Training value: Extremely high.
Fit: 10/10 AISec.
Next action: Build a dedicated 0DIN adapter and run the lab against the currently listed app/model security boundaries.

## 2. STILL-HIGH-VALUE — OpenAI Safety Bug Bounty
Source: https://openai.com/index/safety-bug-bounty/
Payout: Program-specific; verify the current Bugcrowd reward table immediately before testing.
Status: Ongoing public program.
Work: Third-party prompt injection + data exfiltration, agentic harmful actions, MCP risks, account/platform integrity and proprietary-information exposures.
Human effort: Low–medium.
Agent effort: High.
Upfront cost: Low/moderate model usage.
Constraints: Reproducibility requirement for relevant agentic findings; third-party MCP testing must comply with third-party terms; generic harmless jailbreaks are out of scope.
Payout probability: Medium if impact is real and reproducible; low for generic jailbreaks.
Training value: Maximum.
Fit: 10/10.
Next action: Turn every relevant AISec prompt-injection primitive into a reproducibility campaign against explicitly authorized OpenAI surfaces.

## 3. STILL-HIGH-VALUE — Anthropic Model Safety Bug Bounty
Source: https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program
Payout: Up to **$35,000 per novel universal jailbreak**.
Status: Ongoing; rolling applications; HackerOne invite after acceptance.
Work: Universal jailbreaks against Anthropic Constitutional Classifiers, especially detailed harmful-information extraction in the program’s supplied test set.
Human effort: Medium.
Agent effort: High; excellent adversarial-search problem.
Upfront cost: Anthropic provides accepted participants a free model alias for authorized red teaming.
Constraints: Application + NDA; strict confidentiality; supplied question set and details cannot be disclosed.
Payout probability: Low–medium because universality bar is high.
Training value: Extremely high for attack search/evaluation.
Fit: 9.5/10.
Next action: Apply and prepare automated universal-jailbreak search + reproducibility scoring.

## 4. STILL-HIGH-VALUE — Bittensor SN60 BitSec
Source: https://github.com/Bitsec-AI/subnet
Payout: TAO/alpha emissions; exact realized payout depends on rank/emissions and must be read live.
Status: Active; BitSec explicitly incentivizes agents that find/fix high/critical code vulnerabilities and lists a future “Bitsec Hunter” bug-bounty application.
Work: Submit the strongest vulnerability-finding worker we can build.
Human effort: Medium during initial architecture iteration; then low.
Agent effort: Continuous.
Upfront cost: Subnet registration + inference/compute.
Constraints: Follow current validator/sandbox rules; avoid benchmark gaming/spam.
Payout probability: Medium only if we become competitive; objective scoring gives us rapid signal.
Training value: Maximum.
Fit: 10/10.
Next action: Keep BitSec as the canonical worker benchmark; feed bounty/cybergym/real audit lessons back into it.

## 5. NEW — Bittensor SN61 RedTeam
Sources: https://www.theredteam.io ; https://github.com/RedTeamSubnet/RedTeam
Payout: TAO/alpha emissions; live value depends on subnet economics/rank.
Status: Active; current docs describe challenge submission and reward monitoring.
Work: Ethical adversarial solutions that bypass bot-detection systems; successful exploits feed defensive improvements.
Human effort: Medium initial reverse engineering.
Agent effort: High and automatable.
Upfront cost: Registration + API/compute costs; quantify from current miner guide before joining.
Constraints: Exact challenge authorization only; use official container/current dependency instructions.
Payout probability: Unknown until we reproduce a challenge locally.
Training value: Very high — adversarial search, evidence, bypass generation.
Fit: 10/10.
Next action: Clone official miner/challenge stack and benchmark our worker against the current challenge before paying registration cost.

## 6. NEW — Bittensor SN62 Ridges
Source: https://bittensor.ai/subnets/62
Payout: Live subnet currently distributes roughly 35.5 TAO/day equivalent to miners in aggregate; individual reward is rank-dependent, not guaranteed.
Status: Active; only ~11 miners visible on the explorer today despite 256 registered neurons.
Work: Submit one `agent.py` software-engineering agent; validators run it on Harbor tasks in sandboxes with cost/time budgets.
Human effort: Medium to adapt our coding/security worker.
Agent effort: High.
Upfront cost: Current explorer shows very low burn cost plus inference; per-evaluation budgets are enforced.
Constraints: Sandbox/cost/time limits.
Payout probability: Potentially attractive but must test score before assuming revenue.
Training value: Extremely high for general coding worker.
Fit: 9/10.
Next action: Run `ridges miner run-local` using our current agent and compare to leaderboard before registering.

## 7. CHANGED — Bittensor SN74 Gittensor
Source: https://bittensor.ai/subnets/74
Payout: TAO/alpha emissions for eligible merged OSS contributions.
Status: Active. Current explorer shows ~12.7 TAO/day miner pool aggregate and a **0.15 TAO burn cost** today; this is dynamic and should be rechecked immediately before registration.
Work: Produce genuinely useful merged PRs to recognized repositories.
Human effort: Low if `/mw` chooses high-probability issues well.
Agent effort: Medium/high.
Upfront cost: Registration + negligible GitHub costs; inference.
Constraints: GitHub identity/hotkey rules; maintainer acceptance; no PR spam.
Payout probability: Medium once we prove merge rate.
Training value: High.
Fit: 9/10.
Next action: Use the Gittensor Hub/registry to rank open issues by merge probability × score × worker skill match.

## 8. NEW — Immunefi: Sky
Source: https://immunefi.com/bug-bounty/sky/information/
Payout: Smart-contract critical $150k minimum to $10M maximum; high up to $100k; website/app critical up to $100k.
Status: Live; updated Sep 1, 2026; PoC required.
Work: Solidity/DeFi + web/app security within exact scope.
Human effort: High today due to domain skill gap.
Agent effort: High.
Upfront cost: Mostly compute/reproduction environment.
Constraints: Exact Immunefi scope and PoC rules; never risk real funds/mainnet outside explicit authorization.
Payout probability: Low now; could rise as smart-contract worker improves.
Training value: Exceptional economically weighted corpus.
Fit: 8/10.
Next action: Use historical Sky/Maker findings as curriculum first; do not spend human days blind-hunting yet.

## 9. NEW — Immunefi: USDT0
Source: https://immunefi.com/bug-bounty/usdt0/information/
Payout: Critical smart-contract findings $50k minimum to $6M maximum; medium $5k.
Status: Live; updated Sep 1; PoC + KYC required.
Work: LayerZero/cross-chain/Stablecoin Solidity auditing.
Human effort: High.
Agent effort: High.
Upfront cost: Low–medium compute.
Constraints: Exact scope, PoC, KYC, no unauthorized mainnet actions.
Payout probability: Low currently.
Training value: Very high for cross-chain exploit reasoning.
Fit: 8/10.
Next action: Add as a benchmark corpus, then hunt only if our worker scores on analogous historical cross-chain bugs.

## 10. NEW — Immunefi: Optimism
Source: https://immunefi.com/bug-bounty/optimism/information/
Payout: Blockchain critical up to $2,000,042; high $15k–$50k; medium $1k–$15k.
Status: Live; updated Sep 1; PoC + KYC required.
Work: OP Stack / Go / Solidity / infrastructure vulnerability research.
Human effort: High, but excellent overlap with software-security worker.
Agent effort: High.
Upfront cost: Compute/test environment.
Constraints: Program scope and safe PoC rules.
Payout probability: Low until specialized.
Training value: Very high.
Fit: 8.5/10.
Next action: Benchmark worker on historical OP Stack vulnerabilities before allocating real hunting time.

## 11. NEW — Immunefi: RootstockLabs
Source: https://immunefi.com/bug-bounty/rootstocklabs/information/
Payout: Blockchain critical $10k–$200k; high $5k–$10k; medium $2.5
