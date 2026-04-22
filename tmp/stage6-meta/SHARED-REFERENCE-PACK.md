---
id: stage6-shared-reference-pack
purpose: Shared context for 6 subagents writing variant prompts — extracted from D4, CLAUDE.md, approvals
date: 2026-04-21
---

# Stage 6 Shared Reference Pack (for subagents writing variant prompts)

This is a working-memory pack distilled from D4 + D1/D2/D3 + approvals. Subagents writing
variant prompts MUST reference these authoritatively (not reinvent).

## 24 Locks — authoritative list

| # | Lock ID | Title (short) | Source |
|---|---|---|---|
| 1 | D1 (pre) | Gentleman inside / Predator outside | TENSIONS-PRE-RESOLVED |
| 2 | D2 (pre) | Solo-now-team-ready scaffolding | TENSIONS-PRE-RESOLVED |
| 3 | D3 (pre) | Closed outside / open inside (team) | TENSIONS-PRE-RESOLVED |
| 4 | D4 (pre) | Name = Jetix (Jackson/Джек → Jetix canon) | TENSIONS-PRE-RESOLVED |
| 5 | D5 (pre) | Consulting-first → Secure Network Phase 2+ | TENSIONS-PRE-RESOLVED |
| 6 | D6 (pre) | Anton/Vladislav/Rodion — not key (no advisor layer) | TENSIONS-PRE-RESOLVED |
| 7 | D7 (pre) | Union of 11 archetypes (10 base + 1 bloggers Stage 3) | TENSIONS-PRE-RESOLVED |
| 8 | D8 (pre) | Layered identity (multiple faces per observer) | TENSIONS-PRE-RESOLVED |
| 9 | D9/T1 | Pain primary + Opportunity secondary | TENSIONS-RESOLVED |
| 10 | D10/T2 | English + US first, Germany Phase 2+ | TENSIONS-RESOLVED |
| 11 | D11/T3 | Consulting + Продюс-центр + Investment-fund | TENSIONS-RESOLVED |
| 12 | D12/T4 | Smart audience + site primary + social max-TOF | TENSIONS-RESOLVED |
| 13 | D13/T5 | Open surface / closed core | TENSIONS-RESOLVED |
| 14 | D14/T6 | Research = revenue-instrumental (Phase 1) | TENSIONS-RESOLVED |
| 15 | D15/T7 | Revenue-gated spend ($20-30K → €50K → €200K → €1M) | TENSIONS-RESOLVED |
| 16 | D16/T8 | Phase 1 simple chat / formal Phase 2+/3+ | TENSIONS-RESOLVED |
| 17 | D17/T9 | Filesystem = single source of truth | TENSIONS-RESOLVED |
| 18 | D18/T10 | Productization over hours | TENSIONS-RESOLVED |
| 19 | D19 | Holding-Scale $1T ambition ($100M → $100B → $1T) | TENSIONS-RESOLVED-STAGE-2B |
| 20 | D20 | USB-C positioning + Enterprise-Fast | TENSIONS-RESOLVED-STAGE-2B |
| 21 | D21 | Partnership-Matchmaker + Roy-Replication | TENSIONS-RESOLVED-STAGE-2B |
| 22 | D22 | ICP 5-criteria + direction-of-life axis (11 × 5 + direction) | TENSIONS-RESOLVED-STAGE-2B |
| 23 | D23 | Token economy Option B (internal P2 → limited public P3+) | TENSIONS-RESOLVED-STAGE-2B |
| 24 | D24 | Open-source research Phase 2+ (closed methodology) | TENSIONS-RESOLVED-STAGE-2B |

## 21 Hard Constraints (C1-C21) from D4 §6

- **C1** — Solo-now-team-ready (Lock 2)
- **C2** — Revenue-gated spend (Lock 15)
- **C3** — Closed outside / open inside (Locks 3, 13)
- **C4** — Filesystem source of truth (Lock 17)
- **C5** — Consulting-first Phase 1 (Lock 5)
- **C6** — Productization over hours (Lock 18)
- **C7** — Investment-fund philosophy (Lock 11)
- **C8** — Layered identity (Lock 8)
- **C9** — Universality (D2 §10, D-test)
- **C10** — English+US primary Phase 1 (Lock 10)
- **C11** — JETIX-FPF mandatory (D6)
- **C12** — Role ≠ Executor strict (IP-1, P2)
- **C13** — F-G-R trust calculus mandatory
- **C14** — 11-agent canonical roster (D6 §2.2, NOT 12)
- **C15** — Physical Life-OS ≠ Jetix separation
- **C16** — Continuous (not periodic) quality (D2 §6)
- **C17** — Gentleman/Predator membrane bifurcation (Lock 1)
- **C18** — $1T no-rewrite trajectory (Lock 19)
- **C19** — USB-C positioning + enterprise-fast (Lock 20)
- **C20** — ICP 5-criteria + direction-of-life axis (Lock 22)
- **C21** — Token Option B membrane preservation (Lock 23)

## 16 Anti-Patterns (AP-1 through AP-16)

- **AP-1** — Notion-as-primary-store (violates Lock 17)
- **AP-2** — Hour-billing-only architecture (violates Lock 18)
- **AP-3** — Mass-market / attention-economy features (violates Locks 12, 16, 22)
- **AP-4** — Public open-source Phase 1/2 of core (violates Locks 3, 13)
- **AP-5** — Hard-coded Jetix-specific features in base (violates D2 §10)
- **AP-6** — One-person-company assumptions (violates Lock 2)
- **AP-7** — Slow-corporate governance (violates Lock 20)
- **AP-8** — Chaotic-startup governance (violates Lock 20)
- **AP-9** — Motivational-circle community (violates Lock 22)
- **AP-10** — Attention-extraction mechanics (violates Locks 12, 16, 22)
- **AP-11** — Single-provider AI architecture (violates §4.8, Lock 20)
- **AP-12** — Pure-research institution Phase 1 (violates Lock 14)
- **AP-13** — Public token with governance / community-access rights (violates Lock 23)
- **AP-14** — Equal-weight distribution across channels (violates Lock 12)
- **AP-15** — Monolithic brand identity (violates Lock 8)
- **AP-16** — Boutique-scale shortcuts (violates Lock 19)

## 15 Architect Questions (Q1-Q15) from D4 §10

1. **Q1** — Repository structure (base / overlay separation)
2. **Q2** — Agent roster reconciliation (11 canonical + 5 Ruslan sub-roles + 2 Phase-2a stubs)
3. **Q3** — Integration points inventory (Stripe/Wise/Claude/Notion/Telegram/etc + fallback)
4. **Q4** — Scaling mechanism ($0 → $1T without rewrite, 10× per gate <30% LOC refactor)
5. **Q5** — Data architecture (wiki 9 entity types + atoms + provenance + F-G-R)
6. **Q6** — Privacy / security membrane (tier ACL + GDPR Art.22 + EU AI Act)
7. **Q7** — API architecture (multi-provider + compute-ledger + €300-800/mo Phase 1)
8. **Q8** — Token economy Option B (Phase 2 internal / Phase 3+ limited public)
9. **Q9** — Matchmaker algorithm (4 modules: algorithm / quality-gate / contract / metrics)
10. **Q10** — Roy-replication formalization (methodology-as-system kit export)
11. **Q11** — Content pipeline TOF/mid/deep (frame-tag + archetype-keyed rendering)
12. **Q12** — Dashboard implementation (v1 Phase 1 / v2 Phase 2+ / v3 Phase 3+)
13. **Q13** — Escalation routing (6 non-delegatable + 4-class FPF + CP-5 gate)
14. **Q14** — Onboarding architecture (2nd pilot ≤7 days cold-start)
15. **Q15** — USB-C protocol layer (Jetix-defined standards + verification harness)

## 10 Quality Axes (D4 §8.1) + weights (§8.2)

1. Phase-1 readiness — 20%
2. Scale trajectory — 15%
3. Foundation quality — 15%
4. Locks compliance — 18%
5. Universality — 10%
6. Operational simplicity — 10%
7. Cost efficiency — 0% (gate-based disqualifier §8.3)
8. Resilience — 5%
9. Security posture — 5%
10. Innovation — 2%

Total max = 100. Hard floor = axis<3 disqualifies variant.

## 6 Ruslan Non-Delegatable Functions (OME L2 + D1 §3 + D2 §14)

Стратегия / Вкус / Ответственность / Утверждение / Эскалация / Отношения

## 4 FPF Escalation Classes (atom-2558)

dept-internal → Dept Lead; cross-dept → manager (≤20 active); strategic → Ruslan strategy-lead;
safety → meta-agent + Ruslan immediately (halts current task).

## 11 Canonical Agents (D6 §2.2 — NOT 12)

1. manager (MGMT/Phase 1)
2. personal-assistant (OPS/Phase 1)
3. system-admin (OPS/Phase 1)
4. sales-lead (Sales/Phase 2)
5. sales-research (Sales/Phase 2) — renamed from sales-researcher
6. sales-outreach (Sales/Phase 2)
7. inbox-processor (Brain/Phase 2)
8. crazy-agent (Meta/Phase 2)
9. knowledge-synth (Brain/Phase 3)
10. strategy-support-analyst (MGMT/Phase 3) — renamed from strategist
11. meta-agent (Meta/Phase 4, FPF-Steward sub-role until Phase 2b trigger)

Plus 5 Ruslan atomic sub-roles (role-manifests, NOT separate agents):
strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations

Plus 2 Phase-2a stubs: dpo (external-executor) + customer-success (J2).

life-coach → migrates to Life-OS (per Lock 15 C15).

## Revenue Gates (Lock 15)

- $20-30K → essentials
- €50K → GmbH + Stripe + legal basic
- €200K → patents EU + 1-2 hires
- €1M → revenue-share × 3-5 + team 5-10
- €1M+ → Phase 3+

## Phase 2a Triple-AND Trigger (C15, MHT-1)

≥€20K MRR × 3 months AND Ruslan >40% L1/L2 time AND ≥1 GDPR DPA client.

## Foundation Layer 8 Elements (§4)

1. wiki + ATOM-REGISTRY
2. agent contracts
3. handoff protocols
4. escalation protocols
5. continuous quality metrics
6. dashboard
7. reserve routes (failover)
8. F-G-R tagging

## 8 Alphas (FPF)

Past-participle states for wiki: (configured / specified / implemented / tested / deployed / operated / archived / deprecated — per FPF §B).

## Membrane Tiers (C3, Q6)

public / member / partner / core (4 tiers).

## F-G-R Tagging (C13)

- Formality F0-F9 (F0 raw cue → F9 formally proven)
- Reliability R-low / R-medium / R-high / R-certified / R-formally-proven
- Claim-scope: bounded context name

## Dashboard 5 Mandatory Metrics (§3.1.11, §4.7)

1. Architect-hours/week (declining, OME 18h baseline)
2. Founder-dependency % (<30% by €200K)
3. Monthly revenue (trend + gates)
4. Failure rate + MTTR (≤3/mo, p50 ≤42min)
5. Cash runway (≥6mo Phase 1)

Plus Deep Hours (25-30h/wk), Productized revenue % (≥40% @ €200K, ≥70% @ €1M).

## Compute Budget Phase 1

€300-800/mo run rate (hard limit per §5.6 / §8.3 disqualifier).

## 25K Exocortex Budget (MC3)

Hard model-agnostic: FPF 7-10K + role 2-3K + alpha states 3-5K + Steward 3-5K;
remainder flexible (950K on Opus 4.7 1M as reference).

## Ruslan Voice Quotes (for prompts to preserve)

- *"Foundation = главный актив"* — D2 §14
- *"Continuous, every iteration — NOT periodic"* — D2 §6
- *"AI = electricity"* — D2 §7
- *"Gentleman inside / Predator outside"* — Lock 1
- *"это фиксируй. Нам это не сильно важно"* — Stage 4 approval voice
- *"самый глубокий вариант… на максималку"* — Stage 5 directive
- *"Notion loss recoverable in 1 day, wiki loss = Jetix loss"* — D2 §14

---

*END OF SHARED REFERENCE PACK*
