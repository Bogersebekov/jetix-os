---
title: EXPLAIN — DR-26 Unit-economics Deep-Dive (20-25% take rate validation)
date: 2026-05-21
type: prompt-explanation
parent_prompt: prompts/dr-26-unit-econ-deep-dive-2026-05-21.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
target_audience: Ruslan (≤3-min read)
constitutional_posture: R1 + R6 + R11 + R12 + EP-5 + append-only + research-pool pattern + IP-1 STRICT
ack_source: Ruslan voice 2026-05-21 day post-batch-9 explicit «ack всё»
F: F2
G: dr-26-explain
---

# EXPLAIN — DR-26 Unit-economics Deep-Dive

> **TL;DR.** Глубокий research для validation 20-25% take rate (O-108 audio_710) — math + scenarios + comparable substrate. **Gates публичный lock этой цифры в one-pager / pitch / Distribution Plan §5 monetization.** Ruslan ack D9-3 explicit; runs autonomously ~8-12h на server CC; <€2 cost.

---

## §1 Why

Audio_710 voiced explicit 20-25% take rate. Но Ruslan сам сказал «надо математику просчитать» — провизорно ОК для substrate, но публично lock'ать нельзя без validation. DR-26 = math + scenarios → memo с recommended take rate (либо 20-25% confirmed, либо adjusted range, либо piecewise schedule).

**Что gates DR-26:**
- O-108 Tier B promotion (или Tier A standalone if validated)
- C.2 Pitch deck monetization section
- Distribution Plan §5 (was placeholder)
- One-pager R12 paired-frame ask language ("optional первый cohort partnership с N% take rate")

---

## §2 Scope (что покрывает research)

1. **Mondragón ratio analysis** — historical cooperative wage ratio + take rate analogue
2. **QF (Quadratic Funding)** revenue distribution mechanics + cooperative variant
3. **Comparable cooperative DAOs** unit-econ baselines (e.g., Gitcoin / RaidGuild / DXdao / etc.)
4. **Traditional SaaS / consulting** take rate comparables (Uber 25% / Etsy 6.5% / Stripe 2.9% / consulting markup 30-40%)
5. **Member-incentive math** — at what take rate first-cohort joiners feel «win-win» vs «extracted»?
6. **R12 anti-extraction edges** — what threshold = «extraction beyond agreed share»?
7. **Sensitivity scenarios** — 15% / 20% / 25% / 30% take rate impact on cohort growth + revenue per partner + reinvestment loop
8. **Reinvestment loop dynamics** — N% take → re-invested в community → compound growth modeling

---

## §3 Что НЕ делает

- ❌ Не lock'ает финальный publicly committed take rate — surfaces options + recommendation; Ruslan = R1 final decision
- ❌ Не модифицирует Foundation / Pillar C R12 LOCKED text
- ❌ Не запускает A/B tests (those = Phase 2-3 cascade, post Дмитрий/Левенчук feedback)
- ❌ Не violates research-pool-pattern (это explicit ack D9-3 launch, не auto)

---

## §4 9 phases

| # | Phase | Time | Commit |
|---|---|---|---|
| 0 | FPF lens + substrate inventory (R12 + Mondragón + Distribution Plan §5) | 15m | `[dr-26] Phase 0 FPF + substrate` |
| 1 | Mondragón ratio + cooperative DAO unit-econ comparables | 1-2h | `[dr-26] Phase 1 Mondragón + DAOs` |
| 2 | QF + revenue distribution mechanics | 1-2h | `[dr-26] Phase 2 QF mechanics` |
| 3 | Traditional comparables (SaaS / consulting / marketplace) | 1h | `[dr-26] Phase 3 traditional comparables` |
| 4 | Member-incentive math + R12 anti-extraction edges | 1-2h | `[dr-26] Phase 4 member-incentive + R12` |
| 5 | Sensitivity scenarios (15/20/25/30%) + reinvestment loop modeling | 2h | `[dr-26] Phase 5 sensitivity + reinvestment` |
| 6 | Recommendation memo + 3 scenarios | 1h | `[dr-26] Phase 6 recommendation memo` |
| 7 | Cross-link к Distribution Plan + C.2 pitch substrate | 30m | `[dr-26] Phase 7 cross-link + substrate` |
| 8 | Summary + final push | 30m | `[dr-26] Phase 8 Summary + final push` |

**Total: ~8-12h server CC autonomous; <€2.**

---

## §5 Outputs

| Type | Path |
|---|---|
| Phase 0-7 research artifacts | `research/unit-econ-deep-dive-2026-05-21/01..07-*.md` |
| ⭐ Recommendation memo | `research/unit-econ-deep-dive-2026-05-21/_RECOMMENDATION-MEMO.md` |
| Summary for Ruslan | `research/unit-econ-deep-dive-2026-05-21/00-SUMMARY-FOR-RUSLAN.md` (≤1500w) |
| §APPEND к Distribution Plan §5 | `decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md` (or new §APPEND file) |

---

## §6 Acceptance

- ✅ Mondragón + 3+ cooperative DAOs analysed
- ✅ ≥3 traditional comparables (SaaS / consulting / marketplace)
- ✅ Sensitivity 4 scenarios (15/20/25/30%) с math + outcomes
- ✅ R12 anti-extraction edge analysis explicit
- ✅ Recommendation memo с 3 options (conservative / Ruslan-voiced 20-25% / aggressive) — Ruslan picks
- ✅ Cross-link substrate ready для one-pager + C.2 pitch deck monetization
- ✅ Constitutional posture preserved

---

## §7 Cost / runtime

- Server CC autonomous ~8-12h (Opus / 1M context / cache-warm)
- Cost: <€2 (built-in tools + Claude Max sub bundled)
- 9 commits per-phase atomic

---

*EXPLAIN closure 2026-05-21. Per memory `feedback_prompt_explanation_required.md`.*
