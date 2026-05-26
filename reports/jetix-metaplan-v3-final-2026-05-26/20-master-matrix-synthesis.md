---
title: "MetaPlan V3 — Phase 19: Master matrix synthesis (14 × 12 × 6 × 3 + implementation roadmap)"
date: 2026-05-26
type: phase-report-metaplan-v3
phase: 19
F: F2-F3
G: prompt-jetix-metaplan-v3-final-integration-2026-05-26
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 paired-frame STRICT
language: russian
status: draft-report (pool — feeds main v3)
mermaid: V3-6, V3-7, V3-12 (Phase 20)
---

# 🧮 Phase 19 — Master Matrix Synthesis

> **Назначение фазы.** 14 directions × 12 artefacts = **168 потенциальных документов.** Невозможно (и не
> нужно) строить всё сразу. Phase 19 = 4-мерная матрица приоритезации (**direction × artefact × audience ×
> Build/Run/Scale**) → каждая ячейка получает приоритет P0-P3 → из P0/P1 выводится **implementation
> roadmap (4 волны)** + оценка усилия per P0 artefact = surfacing quick wins. Это превращает огромную
> карту в исполнимую очередь.

---

## §0 4 измерения матрицы

1. **Direction (14):** #1..#14 — какая полка.
2. **Artefact (12):** §A..§L — какой тип документа (главный / видео / курс / книга / SOP / шаблоны /
   презентация / FAQ / worked examples / R12 / AI tooling / partner-extension).
3. **Audience (5+1):** 👁️ Любопытный (A) · 🤔 Кандидат T1-T4 (B) · 🔬 Методолог (C) · 🟢 Cohort/масса ·
   ⚖️ R12-критик.
4. **Stage (3):** 🏗️ Build · ▶️ Run · 📡 Scale (per Platform Lifecycle маховик).

**Полная развёртка = 14 × 12 × 6 × 3 = 3024 ячейки.** Очевидно, не все актуальны. Приоритезация сжимает
до исполнимого ядра: **P0 ≈ 20-25 артефактов** (Wave 1-2 Build).

---

## §1 Логика приоритета (P0-P3)

| Приоритет | Критерий | Когда |
|---|---|---|
| **P0** | Блокер выхода наружу ИЛИ ✅ substrate готов + нужен на Build | Wave 1 (Build нед 1-2) |
| **P1** | Нужен для двери B (кандидат) + средняя готовность | Wave 2 (Build нед 3-4) |
| **P2** | Углубление / дверь C / cohort delivery | Wave 3 (Run prep) |
| **P3** | Scale-only / nice-to-have / partner-generated | Wave 4+ (Run/Scale) |

**Правило (из v2 + Phase 17):** P0 = ✅-готовые направления (#4/#5) первыми + 🟢-стоимость форматы (MD/
диаграмма/FAQ) + блокеры параллельно (видео A = критический путь Ruslan).

---

## §2 Master priority matrix (14 directions × 12 artefacts)

Приоритет primary-артефакта каждой ячейки (P0/P1/P2/P3; «—» = не applicable для этого direction).

| Dir \ Art | A Глав | B Видео | C Курс | D Книга | E SOP | F Шабл | G През | H FAQ | I Worked | J R12 | K AI | L Partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 Метод | P0 | P1🎬A | P2 | P3 | P1 | P1 | P2 | P1 | P1 | P1 | P1 | P2 |
| 2 Платформа | P0 | P2 | P3 | — | P1 | P0 | P2 | P1 | P1 | P1 | P1 | P2 |
| 3 Бизнес | P1 | P3 | — | P3 | P2 | P2 | P1 | P1 | P2 | P1 | P2 | P3 |
| 4 Заработок | **P0** | P1 | P3 | — | P2 | P1 | P1 | P0 | P1 | **P0** | P2 | P2 |
| 5 Партнёры | **P0** | P1🎬C | — | — | P0 | P0 | P1 | P0 | P1 | **P0** | P2 | P2 |
| 6 Видение | P0 | P1 | — | P3 | — | P2 | P1 | P1 | P1 | P1 | P3 | P3 |
| 7 Образование | P1 | P2🎬B | P1 | P3 | P2 | P2 | P2 | P1 | P2 | P1 | P2 | P2 |
| 8 R12 | **P0** | P2 | P3 | — | P1 | P1 | P2 | P0 | P1 | **P0** | P2 | P1 |
| 9 Правила | P1 | — | P3 | — | P1 | P1 | P2 | P2 | P2 | P1 | P2 | P2 |
| 10 Ценности | P0 | P2 | — | P3 | — | P2 | P2 | P1 | P1 | P1 | P3 | P3 |
| 11 Master Plan | P1 | P2 | — | P3 | — | P2 | P1 | P1 | P2 | P1 | P3 | P3 |
| 12 Мастерская | P1 | P2🎬тур | P3 | — | P2 | P2 | P1 | P1 | P1 | P1 | P2 | P2 |
| 13 Мастерство | P1 | P2🎬B | P2 | P3 | P2 | P2 | P2 | P1 | P1 | P1 | P1 | P2 |
| 14 Сеть | P1 | P2🎬C | P3 | — | P2 | P2 | P2 | P1 | P2 | **P0** | P2 | P1 |

**P0-ядро (Wave 1) — ~12 артефактов:**
- #4 Заработок: A (Partner Offering polish ✅) + H FAQ + J R12
- #5 Партнёры: A + E SOP (discovery) + F templates + H FAQ + J R12
- #8 R12: A («Наше обещание» якорь) + H FAQ + J R12
- #2 Платформа: A + F templates (Notion базы)
- #6 Видение: A (витрина) · #10 Ценности: A (триада)
- #14 Сеть: J R12 (primary surface)

**Блокеры (параллельный критический путь, Ruslan):** видео A (#1) · видео B (#7/#13) · видео C (#5/#14).

---

## §3 Audience × stage filter (когда какая дверь наполняется)

Из v2: на Build активны T1+T3 (двери C+B); масса/T4 — позже. → двери наполняются по этапам.

| Audience | Build (сейчас) | Run | Scale |
|---|---|---|---|
| 👁️ Любопытный (A) | one-pager + витрина (минимум) | полнее | полная воронка witness |
| 🤔 Кандидат T1-T4 (B) | **главный фокус** (маршрут B) | углубление | partner-generated |
| 🔬 Методолог (C) | deep по запросу (#1 §J, #8) | курсы | книги |
| 🟢 Cohort/масса | — (нет cohort) | **курс + workshop** | сеть cells |
| ⚖️ R12-критик | GitHub + Charter + R12-checklist (всегда) | смарт-контракты | внешний аудит |

**Вывод:** Build = дверь B (кандидат T1-T4) primary + дверь C по запросу + R12-критик всегда. Cohort/масса
(дверь A полная + курсы) = Run+. Это совпадает с P0-ядром §2 (партнёр-facing артефакты).

---

## §4 Implementation roadmap (4 волны — derived из P0/P1)

```
Wave 1 (Build нед 1-2) — P0 only [~12 артефактов + видео A старт]
  ├─ #4 Заработок: Partner Offering polish (✅ готов) + FAQ + R12
  ├─ #5 Партнёры: «кого зовём» + discovery SOP + templates + FAQ + R12
  ├─ #8 R12: «Наше обещание» якорь + FAQ + R12-checklist
  ├─ #6 Видение витрина + #10 Ценности триада (one-pagers)
  ├─ #2 Платформа: главный + Notion templates
  └─ 🎬 видео A старт (Ruslan, критический путь)

Wave 2 (Build нед 3-4) — P1 [главные + презентации кандидата]
  ├─ #1 Метод главный + #6 Видение видео + #3 Бизнес презентация
  ├─ #7/#9/#11/#12/#13/#14 главные документы
  ├─ worked examples + AI tooling specs (P1 directions)
  └─ 🎬 видео A финал + видео C старт

Wave 3 (Run prep / Build exit ≥80%) — P2 [углубление + cohort]
  ├─ #7 Образование курс + #13 Мастерство курс (cohort delivery)
  ├─ SOP + шаблоны (P2) + дверь C deep-материалы
  ├─ #3 Бизнес governance SOP + #9 Правила enforcement
  └─ 🎬 видео B + видео-тур #12

Wave 4+ (Run / Scale) — P3 [книги + Scale + partner-generated]
  ├─ книги (#1/#11/#13 long-arc) — Scale-этап
  ├─ Master Plan Part 3+4 (gated) + смарт-контракты #8/#14
  ├─ partner-extension L3/L4 (co-create / spawn) активируется
  └─ дверь A полная воронка (witness, масса)
```

**Build exit gate (≥80%):** Wave 1+2 P0/P1 + видео A/C готовы + Notion внедрён → переход к Run (дверь C
глубина + первый cohort). Per Platform Lifecycle: переключатель = «кто крутит маховик», не объём контента.

---

## §5 Per-direction effort estimate (P0 artefacts — quick win surfacing)

Оценка усилия на **P0-артефакт** каждого direction (порядок величины; R1 — финал за Ruslan; зависит от
substrate-готовности и формата per Phase 17):

| Direction | P0 artefact | Substrate | Усилие (порядок) | Quick win? |
|---|---|---|---|---|
| #4 Заработок | A Partner Offering polish | ✅ готов | 🟢 ~3-5 ч (polish) | ⭐ ДА |
| #5 Партнёры | A «кого зовём» + E discovery | ✅ EXECUTION §5 | 🟢 ~5-8 ч | ⭐ ДА |
| #8 R12 | A «Наше обещание» якорь | ⚠️ EXECUTION §4 | 🟡 ~5-8 ч (ФРАЗА = Ruslan) | средне |
| #2 Платформа | A + F Notion templates | ⚠️ PLATFORM-LIFECYCLE | 🟡 ~8-12 ч | средне |
| #6 Видение | A витрина | ⚠️ workshop §4 | 🟡 ~4-6 ч (one-liner = Ruslan) | средне |
| #10 Ценности | A триада | ⚠️ O-числа | 🟡 ~5-8 ч (триада = Ruslan) | средне |
| #1 Метод | A главный | ⚠️ §J | 🟡 ~6-10 ч (+ видео A блокер) | средне |
| #3 Бизнес | A «Как устроен» | ❌ create | 🔴 ~10-15 ч (жанр с нуля) | нет |
| #11 Master Plan | A 4 части | ❌ create | 🔴 ~12-20 ч (жанр + anti-hype) | нет |
| #12 Мастерская | A 8 зон | ❌ create | 🔴 ~10-15 ч (+ видео-тур позже) | нет |
| #14 Сеть | J R12 + A | ❌ create | 🔴 ~12-18 ч (R12-плотность) | нет |
| #7 Образование | A + C курс | ⚠️ 7 ступ | 🔴 ~15-20 ч (курс) | нет (Run) |
| #13 Мастерство | A + C курс | ⚠️ substrate готов | 🟡 ~10-15 ч | средне |
| #9 Правила | A свод 10 углов | ⚠️ Pillar C | 🟡 ~8-12 ч (public/internal = R1) | средне |

**Quick wins (⭐):** #4 Заработок (polish готового) + #5 Партнёры (substrate ✅). Это подтверждает v2 §13.1
рекомендацию: Wave 1 = ✅-готовые первыми, тяжёлые ❌-манифесты (#3/#11/#12/#14) параллельно/позже.

**Рычажные CREATE-GAP (❌, высокое усилие но высокий рычаг):** #3 Бизнес · #11 Master Plan · #12 Мастерская
· #14 Сеть + видео A/B/C. Это «тело» (новые directions) — дорого, но без них Foundation не материализуется.

→ Визуализации — **V3-6** (synthesis tree) + **V3-7** (roadmap timeline) + **V3-12** (build readiness) — Phase 20.

---

## §6 Что Phase 19 разблокирует

- 168 потенциальных документов сжаты до **~12 P0-ядра (Wave 1)** + чёткой 4-волновой очереди.
- Per-direction P0 effort estimate → Ruslan видит quick wins (#4/#5) vs рычажные (#3/#11/#12/#14).
- Audience × stage filter → знаем, какая дверь наполняется на каком этапе (Build = дверь B + C по запросу).
- Partner-extension layer (Phase 18) накладывается: L1-L2 = Build/Run, L3-L4 = Run/Scale.
- Это THE очередь для следующих iterations (per-direction × per-artefact filling prompts — 168 potential).

**Phase 19 complete.** 4-мерная матрица (14×12×6×3 = 3024 ячейки) приоритезирована до ~12 P0-ядра. Master
priority matrix 14×12. Audience × stage filter. Implementation roadmap 4 волны (Build P0/P1 → Run prep P2 →
Scale P3). Per-direction P0 effort estimate (quick wins #4/#5; рычажные #3/#11/#12/#14). Feeds V3-6/7/12.

---

*Phase 19 closure. Master matrix synthesis: 4 измерения (direction × artefact × audience × stage). 168
docs → ~12 P0-ядро. Priority matrix 14×12 (P0-P3 per cell). Implementation roadmap 4 волны (P0 Wave1 →
P1 Wave2 → P2 Wave3 Run-prep → P3 Wave4 Scale). Per-direction P0 effort estimate (quick wins #4/#5 ⭐;
рычажные ❌ #3/#11/#12/#14). Build exit gate ≥80%. Feeds V3-6/V3-7/V3-12 (Phase 20). R12 paired-frame STRICT.*
