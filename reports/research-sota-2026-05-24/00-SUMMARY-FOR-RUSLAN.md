---
title: SUMMARY for Ruslan — Research SOTA 2026-05-24
date: 2026-05-24
type: summary-for-ack
parent_research: decisions/strategic/RESEARCH-SOTA-2026-05-24.md
target_word_count: ≤1500
actual_word_count: ~1450
audience: Ruslan (R1 pre-ack)
language: russian primary
---

# 📋 Summary — Research SOTA 2026-05-24

> **TL;DR:** Decoded SOTA-concept через 16 источников + Jetix lens. **3 главных вывода + 7 решений для тебя.** Если 5 минут на чтение — читай §1 и §3.

---

## §1 Что мы узнали (3 главных вывода)

### 1️⃣ **SOTA — не «лучшее», а «лучшее на сегодня, для domain X, по criteria Y»**

Каждая честная SOTA-claim должна specify **7 axes**: WHAT (объект) / WHEN (год) / WHERE (domain) / WHO (community) / WHY-better (предсказательное преимущество) / HOW-validated (механизм) / HOW-LONG (lifespan).

Без любого = vague (потенциально dishonest) claim. Это **applicable немедленно** к нашим partner-facing materials.

**Левенчук source:** «SoTA всегда имеет дату» [Метод 2025 :6485]. **МИМ implementation:** каждая квалификация year-stamped — «мастер 2018» visible publicly.

### 2️⃣ **У Jetix уже есть ~70% МИМ SOTA-pattern implicitly**

После deep decode Master Q article (`ailev.livejournal.com/1794653`) — **сравнил 10-layer МИМ stack с Jetix:**

- ✅ **5 strong:** continuous measurement (cycle-hooks) / JSONL mailbox = «все слова записаны» / HITL stage gate = group qual / multi-niche memory / sota-tracker-expert = reformator role / F-G-R = anti-charisma
- 🟡 **4 medium:** quantified 3-axis profiles / 7-step ladder / year-of-qualification (partial) / cohort-specific recognition
- 🔴 **1 weak:** explicit per-agent qualification ladder

**Implication:** Jetix substrate уже эволюционировал в МИМ-direction, **просто без явного признания**. Phase 7 предлагает formalisation.

### 3️⃣ **8 paradigms philosophy-of-science все одновременно живы — Jetix должен держать все**

EP-5 / AP-6 preservation: ни Popper, ни Kuhn, ни Lakatos, ни Feyerabend, ни Laudan не «победил». **8 paradigms = 8 lenses для разных situations** (Phase 3 §7 decision matrix).

Что Jetix уже использует implicitly:
- **F-G-R discipline** = Popper + Longino operational
- **R12 LOCK** = Lakatos hard core
- **AP-6** = Feyerabend minimal
- **Method V2 §J meta-method** = Lakatosian operational
- **HITL stage gate** = Longino 4 norms (3 из 4 operational)

---

## §2 Что особенно важно знать

### Huyen «Avoid the SOTA trap» — самое практичное чтение

Если читать **одну главу** из всего corpus — это **Huyen Designing ML Systems Ch.6 «Avoid the state-of-the-art trap»**:

- SoTA-model на static benchmark ≠ SoTA на your data
- Business «appear cutting edge» = bullshit motivator, не engineering
- Simple baseline first; complex SoTA только if beats baseline
- Melis 2018: weak model + tuned hyperparameters > strong model + default tuning

**Прямо применимо к нашим sales conversations.** Подавляющее большинство клиентов хочет «cutting edge AI». Discipline: «cutting edge что именно, для какой задачи, vs какие baselines».

### Master Q article = best operational case ever published

Master Q article — это **самый плотный operational SOTA-discipline applied к human qualification, что я нашёл в literature**. 5K слов, март 2026, formalised:
- 3-axis quality measurement
- EQF + EPA international calibration
- Year-of-update mechanism
- «осетрина первой свежести» binary purity rule на старшем уровне
- Continuous measurement vs discrete exam
- Group + public Longino-style validation
- «У нас все слова записаны» — direct video recording discipline (явно включая AI-agents!)

**Это direct precedent + evidence material для нашего Wave 1 outreach к МИМ.**

### Левенчук «foundational > SoTA-chasing» — критический совет

Из всех Левенчуковских claims самый strategic:

> «Не гонись за SoTA инструментов — инвестируй в SoTA трансдисциплин (медленно меняются), это позволит быстро отслеживать SoTA прикладных методов.» [Метод 2025 :3055]

**Application к Jetix:** Pillar C Tier 2 12 rules = stable foundation; experts pull SoTA on-demand. **НЕ chasing latest ML framework eachweek**. Foundation-first approach защищает от SoTA-chase exhaustion.

---

## §3 7 решений для тебя (ack/defer matrix)

| # | Решение | Investment | Моя R1-surface recommendation | Твой ack |
|---|---|---|---|---|
| 1 | `wiki/experiments/replication-log.md` — log каждое methodology application + outcome | **low** | **adopt — closes critical gap** | __ |
| 2 | `wiki/comparisons/` expanded — Method V2 vs OMG Essence + FPF vs ISO 24744 | medium | Q3 2026 | __ |
| 3 | `sota_revalidate_by:` frontmatter field в Foundation/canonical docs | **low** | **adopt — schema-level fix** | __ |
| 4 | `wiki/foundations/sota-claim-discipline.md` — codify partner-facing discipline | **low** | **adopt — sales-impact direct** | __ |
| 5 | FPF cross-paradigm translation docs (Левенчук-to-McКинзи / СМД-to-Agile / Jetix-to-Cooperative-Governance) | medium | Q3-Q4 2026 | __ |
| 6 | `agents/<id>/qualification.yaml` — МИМ-style 3-axis agent quals | medium | Q3-Q4 2026 | __ |
| 7 | `wiki/dissent/` cluster — AP-6 operationalised | **low** | **adopt** | __ |

**Net recommendation:** 4 low-investment immediate (1, 3, 4, 7) + 3 medium-investment Q3-Q4 2026 (2, 5, 6).

**Total adoption cost:** ~10-15 hours dev work + schema updates + 2-3 wiki docs за следующие 2 weeks if all low-investment adopted.

---

## §4 Wave 1 outreach implication

**Этот research bundle сам — evidence material для Wave 1 outreach к Левенчуку / Цэрэн / МИМ:**

- Phase 6 (МИМ deep decode) + Phase 7 (Jetix Lens) — direct evidence что мы понимаем their work + умеем translate to AI-substrate
- Honest framings (Phase 7 §7) preserve cohort-specific recognition — НЕ «we replace МИМ», но «AI-substrate complement that preserves your work + adds new capabilities»
- R12-compliant — НЕ extracting МИМ insights, а surfacing how AI-substrate can recognise + amplify them

**После твоего ack** — Phase 7 §7 templates готовы для adaptation к partner-specific messaging.

---

## §5 Что в substrate (быстрый browse)

```
reports/research-sota-2026-05-24/
├── 00-SUMMARY-FOR-RUSLAN.md  ← this file
├── phase-0-fpf-lens-scope.md  (162 lines — preflight)
├── 01-levenchuk-sota-concept.md  (401 lines — Левенчук deep)
├── 02-philosophy-of-science.md  (398 lines — Popper-Kuhn-Lakatos-Feyerabend-Laudan)
├── 03-modern-epistemology.md  (292 lines — Hacking-Longino-Chalmers)
├── 04-sota-modern-ai.md  (367 lines — Goodfellow-Huyen-Karpathy-PWC)
├── 05-sota-tracking-mechanisms.md  (518 lines — 9 mechanisms)
├── 06-sota-mim-operational.md  (448 lines — МИМ Master Q deep)
├── 07-jetix-lens-sota.md  (474 lines — gaps + extensions)
└── diagrams/
    ├── _INDEX.md
    ├── 01-sota-concept-multi-tradition-decomposition.mmd
    ├── 02-levenchuk-sota-time-decay-curve.mmd
    ├── 03-popper-kuhn-lakatos-feyerabend-laudan-comparison.mmd
    ├── 04-sota-tracking-mechanisms-flow.mmd
    ├── 05-ml-sota-leaderboard-pattern.mmd
    ├── 06-mim-sota-mastery-spectrum.mmd
    ├── 07-jetix-sota-tracking-inventory.mmd
    ├── 08-jetix-sota-gaps-and-extensions.mmd
    ├── 09-sota-claim-honesty-discipline.mmd
    └── 10-sota-vs-foundational-trade-off.mmd

decisions/strategic/RESEARCH-SOTA-2026-05-24.md  ← master strategic doc (~18K words)
```

**Если только browsing — read это Summary + Phase 7 (Jetix Lens) + master strategic doc §1, §7, §10.**

**Если deep — read also Phase 6 (МИМ deep) + Phase 4 §3 (Huyen anti-SOTA-trap).**

---

## §6 Метрики run

- ✅ 8 phases done
- ✅ 30+ sources cited (target 25+)
- ✅ 10 mermaid diagrams (target 8-12)
- ✅ 8 per-phase commits + pushes
- ✅ 0 LOCK modifications
- ✅ 0 API key leaks
- ✅ 0 SKIP-list violations
- ✅ 0 R1 strategic prose authored by agent
- ✅ R12 paired-frame discipline preserved
- ✅ Master Q cross-cite (ailev.livejournal.com/1794653)
- ✅ Jetix Lens (Phase 7) concrete

---

*Summary closure 2026-05-24. Ready для твоего review + ack/defer matrix decisions §3.*
