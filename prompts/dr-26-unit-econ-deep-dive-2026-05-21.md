---
title: DR-26 Unit-economics Deep-Dive — 20-25% take rate validation
date: 2026-05-21
type: autonomous-execution-prompt
phase_count: 9
parent_explain: prompts/explanations/_EXPLAIN-dr-26-unit-econ-deep-dive-2026-05-21.md
ack_source: Ruslan voice 2026-05-21 day post-batch-9 ack D9-3 explicit
gates:
  - O-108 take rate Tier B promotion
  - C.2 Pitch deck monetization section
  - Distribution Plan §5 monetization (was placeholder)
  - One-pager R12 paired-frame ask language
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: dr-26-unit-econ-deep-dive
R: refuted_if_LOCK_modified_OR_R12_violation_OR_take_rate_publicly_locked_without_Ruslan_R1
constitutional_posture: R1 + R2 + R6 + R11 + R12 + IP-1 STRICT + EP-5 + append-only + research-pool-pattern
estimated_runtime: 8-12h autonomous
estimated_cost: <€2
language: russian primary
---

# DR-26 Unit-economics Deep-Dive — Prompt

> **Trigger:** Ruslan voice 2026-05-21 day «ack всё» — D9-3 explicit. NOT plan mode — execute autonomously on launch. Per-phase commit + push.

---

## §0 Pre-flight (mandatory)

1. **EXPLAIN:** `prompts/explanations/_EXPLAIN-dr-26-unit-econ-deep-dive-2026-05-21.md`
2. **Memory:** `feedback_research_pool_pattern.md` + `feedback_constitutional.md` + `feedback_breadth_not_selection.md`
3. **Substrate read:**
   - `decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md` §5 (monetization placeholder)
   - `wiki/concepts/r12-charter.md` (or equivalent) — R12 anti-extraction text
   - `principles/tier-2-system/foundation-generic/` rule 12 (Pillar C R12 LOCKED)
   - `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` (Mondragón ratio + QF acked Option D Hybrid)
   - `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` (R12 LOCKED text + Game Theory M-C mechanism §11)
   - Audio_710 verbatim claim 1-3 (20-25% take rate + responsibility-pact reinvestment loop)
   - O-108 Tier B pool entry
   - All Левенчук distillation cross-link matrix §2.7 systemic ethics

---

## §1 Phase 0 — FPF lens + substrate inventory (15m)

**Output:** `research/unit-econ-deep-dive-2026-05-21/00-FPF-lens-scope.md`

- Object: unit-econ analysis для validate / refine / propose alternative take rate(s)
- FPF layer: F2 surfacing predominant; F2-F4 analysis
- Acceptance: 4 scenarios analysed (15/20/25/30%) + Mondragón + 3 cooperative DAOs + 3 traditional comparables + R12 edge analysis + recommendation memo

Commit: `[dr-26] Phase 0 FPF + substrate inventory`

---

## §2 Phase 1 — Mondragón ratio + cooperative DAOs unit-econ (1-2h)

**Output:** `research/unit-econ-deep-dive-2026-05-21/01-mondragon-cooperative-daos.md`

- **Mondragón Cooperative Corporation** — historical wage ratio (founder/avg ratio); membership economic structure; profit distribution mechanics; lessons applicable к Jetix
- **Gitcoin** — QF + grants distribution; take rate analogue (% community treasury)
- **RaidGuild** — coop development cooperative; member compensation structure
- **DXdao** — DAO governance + economic mechanics
- **Other:** scan 2-3 более comparables (Aragon / Colony / etc.) if relevant
- Cross-cite: ALL claims with [src: ...] verifiable references

Commit: `[dr-26] Phase 1 Mondragón + cooperative DAOs comparables`

---

## §3 Phase 2 — QF (Quadratic Funding) + revenue distribution mechanics (1-2h)

**Output:** `research/unit-econ-deep-dive-2026-05-21/02-qf-revenue-distribution.md`

- QF math basics (Vitalik / Glen Weyl original)
- QF в cooperative context (Gitcoin example)
- Revenue distribution model для Jetix:
  - Member contribution → revenue → take rate split → reinvestment
  - QF-style matching pool from take rate?
  - Cooperative ownership stake distribution
- Implementation considerations (on-chain vs off-chain)
- Compatibility с R12 programmable Ethereum substrate (acked 2026-05-18)

Commit: `[dr-26] Phase 2 QF + revenue distribution mechanics`

---

## §4 Phase 3 — Traditional comparables (1h)

**Output:** `research/unit-econ-deep-dive-2026-05-21/03-traditional-comparables.md`

| Type | Examples | Take rate | Notes |
|---|---|---|---|
| Marketplaces | Uber / Lyft / Etsy / eBay | 6.5-25% | reference points |
| SaaS | Stripe / Twilio / Notion | margin different metric | — |
| Consulting | Bain / McKinsey / boutique | 30-40% markup | service business |
| Cooperatives | REI / Mondragón / Ocean Spray | profit share to members | closer to Jetix |
| Education | Coursera / Udemy / Maven | 30-50% platform take | substrate analogue |

Identify Jetix-relevant pattern:
- Most apt analogy = cooperative + education + consulting hybrid
- Take rate в этом hybrid? — likely в 15-30% range, optimal depends on cohort dynamics

Commit: `[dr-26] Phase 3 traditional comparables`

---

## §5 Phase 4 — Member-incentive math + R12 anti-extraction edges (1-2h)

**Output:** `research/unit-econ-deep-dive-2026-05-21/04-member-incentive-r12-edges.md`

- **Member-incentive math:**
  - Per-partner unit econ: revenue / member / month
  - First-cohort joiners ROI calculation (their effort × take rate retained)
  - Compound growth: take rate → community pool → cohort expansion → revenue ↑
  - Break-even analysis: at what cohort size + take rate Jetix becomes self-sustaining?

- **R12 anti-extraction edges:**
  - R12 Pillar C Tier 2 rule 12: «cannot extract value from members beyond agreed share»
  - «Beyond agreed share» — что это в practice quantitatively?
  - 4 R12 RUSLAN-LAYER action classes (extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt)
  - Programmable enforcement (smart contracts) — Mondragón ratio cap + QF + fork-and-leave exit tokens (per Ethereum substrate acked Option D Hybrid)
  - Edge cases: at 30%+ take rate — есть R12 violation risk? Mondragón ratio threshold violation?

Commit: `[dr-26] Phase 4 member-incentive math + R12 edges`

---

## §6 Phase 5 — Sensitivity scenarios + reinvestment loop modeling (2h)

**Output:** `research/unit-econ-deep-dive-2026-05-21/05-sensitivity-scenarios.md`

### 4 scenarios

| Scenario | Take rate | Risk | Reinvest pool | Cohort growth model |
|---|---|---|---|---|
| **Conservative** | 15% | low R-1 | smaller pool | slower; sustainability primary |
| **Ruslan-voiced** | 20-25% | medium R-1 | balanced | matches audio_710 verbatim |
| **Aggressive** | 30% | high R-1 + R12 edge | larger pool faster | speed primary; R12 audit needed |
| **Piecewise** | 15% first year → 20% steady → 25% scale | adaptive | adaptive | gradient |

### Per scenario math model:
- Year-1 revenue (assume X partners @ Y eur/month)
- Take rate retained pool
- Community reinvestment loop dynamics
- Cohort growth function
- Break-even timing
- 5-year projection sensitivity

Commit: `[dr-26] Phase 5 sensitivity scenarios + reinvestment modeling`

---

## §7 Phase 6 — Recommendation memo (1h)

**Output:** `research/unit-econ-deep-dive-2026-05-21/_RECOMMENDATION-MEMO.md`

```markdown
# Recommendation Memo — Take Rate (DR-26)

## TL;DR (≤200w)
[Top-line recommendation: которая из 4 scenarios + почему]

## Options for Ruslan R1 decision
1. Conservative 15% — pros / cons / risk profile
2. Ruslan-voiced 20-25% — pros / cons / risk profile
3. Aggressive 30% — pros / cons / risk profile
4. Piecewise gradient — pros / cons / risk profile

## Recommended for one-pager + pitch
[Recommended option + rationale + R12 compliance + provisional language for pitch]

## What gates final lock
- A/B test data (Phase 2 cascade post-Дмитрий/Левенчук feedback)
- DR-31 governance R12 boundary audit (P3 deferred)
- Ruslan R1 strategic decision

## Substrate references
[All cross-cite [src: ...] inline]
```

Commit: `[dr-26] Phase 6 recommendation memo`

---

## §8 Phase 7 — Cross-link к Distribution Plan + C.2 pitch substrate (30m)

**Output:**
- `decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md` — §5 §APPEND-DR-26 unit-econ substrate added
- Note added к `_TIER-B-CANDIDATES-POOL-2026-05-20.md` O-108: «DR-26 ⭐⭐ validation done — recommendation memo at ...»

Commit: `[dr-26] Phase 7 cross-link + Distribution Plan §APPEND`

---

## §9 Phase 8 — Summary + final push (30m)

**Output:** `research/unit-econ-deep-dive-2026-05-21/00-SUMMARY-FOR-RUSLAN.md` (≤1500w)

Structure:
- §0 TL;DR (≤200w)
- §1 Что прочитал (substrate inventory)
- §2 Что сделал (8 phases + 9 commits)
- §3 Key findings (Mondragón / QF / traditional / R12 edges)
- §4 4 scenarios summary
- §5 Recommendation (top option + rationale)
- §6 What's gated / what's blocked still
- §7 Cross-link references
- §8 Cost + runtime

Final push:
```bash
git add research/unit-econ-deep-dive-2026-05-21/ decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md reports/voice-pipeline-2026-05-20-batch-7/_TIER-B-CANDIDATES-POOL-2026-05-20.md
git commit -m "[dr-26] Phase 8 Summary + final push"
git push origin main
```

Final echo:
```
DONE Phase 8 — 9 commits / N files / Recommendation memo ready / cost ~€X / runtime ~Y h
```

---

## §10 Operational rules

- **Per-phase commit + push** mandatory
- **NO LOCK modifications** (R12 Pillar C text untouched; Foundation read-only)
- **NO public take rate lock** — recommendation memo surfaces options; Ruslan R1 final
- **R12 paired-frame** discipline в recommendation language
- **Russian primary**; English для math/finance terms
- **R6 provenance per claim** — [src: ...] for every comparable / number
- **EP-5 F2** surface predominant; F4 explicit для analysis claims
- **Constitutional posture preserved** through all phases

---

## §11 If blocked

- Comparable data unavailable for specific DAO → flag + continue 3-4 others
- R12 edge analysis ambiguous → surface multiple readings AP-6
- Math model unclear → simpler placeholder + flag для Ruslan ack
- Git push race → rebase + retry

---

*Prompt closure 2026-05-21. Per memory `feedback_prompt_explanation_required.md` + `feedback_research_pool_pattern.md`. Ruslan ack D9-3 explicit launch authority.*
