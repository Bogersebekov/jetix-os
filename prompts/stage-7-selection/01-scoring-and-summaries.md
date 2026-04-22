---
id: stage-7-scoring-and-summaries
title: Stage 7 Scoring Matrix + Executive Summaries — 5 Architecture Variants
author: cloud-cowork
date: 2026-04-22
audience: server-cc (Opus 4.7 1M, extended thinking max)
expected-duration: 2-4h
status: active
---

# Stage 7 Scoring + Executive Summaries — Task for Server CC

## Role

Ты — **independent cross-auditor** для Stage 7 variant selection. 5 архитекторов уже
написали свои variants (Stage 6) со **self-scores**. Твоя задача — **cross-audit**
(не self-score автора): применить D4 §8.1 rubric + §8.2 weights на каждый variant,
сравнить с авторским self-score, flag'нуть discrepancies, и дать Ruslan'у **одну
навигационную таблицу + 5 executive summaries** для выбора на Stage 7.

**Critical:** ты НЕ выбираешь variant. Ты готовишь selection-ready data. Ruslan +
Cloud Cowork читают твой output и принимают решение.

## Context

- **24 LOCKED decisions** (non-negotiable) в 3 файлах:
  - `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` (Locks 1-8)
  - `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` (Locks 9-18 / T1-T10)
  - `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` (Locks 19-24)
- **D1-D4 APPROVED** foundation: `decisions/JETIX-VISION.md`, `JETIX-PHILOSOPHY.md`,
  `JETIX-PLAN.md`, `JETIX-ARCHITECTURE-BRIEF.md`
- **Scoring rubric** в `decisions/JETIX-ARCHITECTURE-BRIEF.md` §8.1 (10 axes), §8.2
  (weights), §8.3 (hard disqualifiers), §9 (selection procedure)

## Inputs (обязательно прочитать целиком)

1. `decisions/JETIX-ARCHITECTURE-BRIEF.md` — §6 hard constraints, §7 anti-patterns,
   §8 rubric, §9 selection procedure, §10 16 architect questions
2. `decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md` (1699 lines)
3. `decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md` (1684 lines)
4. `decisions/variants/JETIX-ARCH-V3-DEEPTECH.md` (1809 lines)
5. `decisions/variants/JETIX-ARCH-V4-HYBRID.md` (1608 lines)
6. `decisions/variants/JETIX-ARCH-V5-EMERGENT.md` (1499 lines)
7. `decisions/variants/_CRITIC-NOTES.md` (только для V2, но прочитать — шаблон для твоих
   own critic observations)
8. 3 Locks файла (см. Context выше) — для §8.1 axis 4 cross-audit

**V6 WILDCARD не доставлен** — работаем с 5 variants. Не упоминай V6 как вариант.

## Deliverables

Один файл: `decisions/variants/_STAGE-7-SCORING-AND-SUMMARIES.md`

Структура:

### Part 1 — Scoring Matrix (master table)

Одна таблица 10 axes × 5 variants + 2 columns справа (max, weighted):

```
| Axis (weight)           | V1 Con | V2 Max | V3 DT | V4 Hyb | V5 Em | Best | Notes |
| 1 Phase-1 ready (20%)   | 9      | 6      | 5     | 8      | 6     | V1   | ...   |
| 2 Scale trajectory (15%)| 6      | 9      | 9     | 9      | 7     | V2/3/4 | ... |
...
| TOTAL (weighted 100)    | 74     | 72     | 78    | 77     | 71    | V3   |       |
```

**Правила:**

1. Для каждой ячейки 1-10 — **cross-audit score** (не копировать self-score автора).
   Обоснование в колонке `Notes` **коротко** (15-25 слов), с цитатой §.
2. Если cross-audit разошёлся с self-score ≥2 балла — явно пометить `(self: X, my: Y)`
   в Notes и объяснить почему.
3. Axis 7 (Cost efficiency) — per §8.3 это **gate-based** (€800/mo disqualifier), 0%
   weight в §8.2. Всё же дай score 1-10 как proxy-signal, но в totals не считай.
4. **Disqualifier check** (§8.3) сначала: если variant нарушает §6 hard constraint
   ИЛИ присутствует §7 anti-pattern ИЛИ Phase-1 run-rate > €800/mo без justification —
   вариант `DISQUALIFIED` в таблице с указанием нарушенного правила. Scoring пропусти.
5. **Alternative weightings** (§8.2 allows): если ты считаешь что Lock 19 ($1T
   ambition) требует перевеса Scale vs Phase-1 — предложи alternative weights
   OTDEL'nym sub-table'ом с цитатой Lock. Оба scorings в output (default + alt).

### Part 2 — Executive Summaries (5 × compact, 2-page each)

Для каждого variant — фиксированная структура:

```
## V[N] [Name]

**Self-score:** X/100 | **My weighted score:** Y/100 | **Status:** ELIGIBLE / DISQUALIFIED

**Thesis (1 sentence)**: ...

**Top 3 strengths:**
1. ...
2. ...
3. ...

**Top 3 weaknesses/risks:**
1. ...
2. ...
3. ...

**Phase-1 cost estimate:** €X-Y/mo (evidence: §Z)

**Phase-3 scalability:** ... (evidence: §Z)

**Critical assumptions** (если variant ломается — что именно не сработает):
- Assumption 1: ...
- Assumption 2: ...

**Non-negotiable elements** (что ДОЛЖНО выжить в hybrid composition если этот variant
НЕ выбран basic'ом):
- Element 1: ... (цитата §Z)
- Element 2: ... (цитата §Z)

**Red flags** (что заставило меня снизить score):
- Flag 1: ...

**Compatibility with 24 locks:**
- ✅ Full compliance OR ⚠️ Tension with Lock N (...) OR ❌ Violation of Lock N (stop)
```

Каждый summary — ~400-600 слов. Total Part 2 = ~2500-3000 слов.

### Part 3 — Cross-Variant Analysis

Секция 500-800 слов с анализом:

1. **Orthogonal pairs** (какие variants — real alternatives, а какие почти дубли)
2. **Hybrid composability** (V4 уже hybrid — что ещё можно компоновать? V3+V1? V5+V2?)
3. **Lock-driven filter**: какой Lock/принцип наиболее жёстко разделяет variants?
4. **€50K Q2 feasibility ranking** (Phase-1 gate): top-3 по реалистичности
5. **Swarm/роя-паттерн readiness**: какой variant лучше accommodates
   capability-capsules + agent-bidding (V5-style) при необходимости layer'а сверху?
   Это важно для Stage 7 discussion.

### Part 4 — Flagged Questions for Ruslan

5-10 конкретных вопросов где твой cross-audit выявил ambiguity или tension и нужно
Ruslan'у решить перед selection. Пример:
- «V2 Maximalist scaffold-rot risk при медленном revenue growth — acceptable tradeoff
  за Phase-3 readiness Day 1?»
- «V3 Deep-Tech formalism learning cliff — Ruslan готов вложить ~7 architect-weeks в
  FPF-formalism Phase 1 ради лучшего $1T defense?»

Каждый вопрос — контекст + tradeoff + что решение открывает/закрывает.

## Success criteria

- **Taxonomy fidelity**: используешь ТОЛЬКО axes из §8.1 (10 штук). Не изобретай
  новые axes.
- **Citation discipline**: каждая non-trivial claim ссылается на §X.Y в variant doc
  или на Lock N. NO hand-waving.
- **Cross-audit honesty**: если author self-score слишком оптимистичен — обосновать
  снижение. Если self-score занижен — повысить.
- **No new decisions**: ты не предлагаешь новые Locks / new anti-patterns / new
  principles. Ты scoring'уешь existing.
- **Length**: ~4000-6000 слов total. Concise, dense, table-heavy где возможно.
- **Honest tradeoffs**: для каждого variant должны быть настоящие weaknesses, не
  marketing. Axis < 5 должен быть хотя бы у одного variant где это честно.

## Anti-patterns (НЕ делай)

- ❌ НЕ выбирай «best variant» в output — только scoring + summaries
- ❌ НЕ меняй §8 weights без явного alt-weighting sub-table с Lock citation
- ❌ НЕ добавляй V6 в scoring (не существует)
- ❌ НЕ копируй self-scores без верификации — это cross-audit, не aggregation
- ❌ НЕ пиши >6000 слов — compact
- ❌ НЕ пропускай disqualifier check (§8.3) — первый шаг всегда

## Extended thinking

Используй **extended thinking max** для этой задачи. Особенно на:
- Cross-audit scoring (где дискреционный judgment)
- Lock-compliance matrix (24 × 5 = 120 ячеек верификации)
- Hybrid composability analysis

## Workflow

1. Read all 6 inputs (Architecture-Brief + 5 variants + 3 Locks files). ~45min.
2. Disqualifier pass (§8.3) для каждого variant. ~15min.
3. Scoring matrix fill (10 axes × 5 variants + Notes). ~60-90min.
4. Executive summaries (5 × 400-600 words). ~60-90min.
5. Cross-variant analysis + flagged questions. ~30-45min.
6. Self-review pass: проверь disqualifier check не пропущен; все claims с citation;
   total word count 4000-6000. ~15min.
7. Commit + push.

## Commit template

```
git add decisions/variants/_STAGE-7-SCORING-AND-SUMMARIES.md
git commit -m "[decisions] Stage 7 scoring matrix + executive summaries (cross-audit 5 variants)"
git push origin claude/jolly-margulis-915d34
```

## After completion

Сообщи в commit message что готово. Cloud Cowork увидит через git fetch и начнёт
Stage 7 discussion with Ruslan.

**Не пиши selection decision.** Это работа Ruslan + Cloud Cowork на следующем шаге.

---

*END PROMPT*
