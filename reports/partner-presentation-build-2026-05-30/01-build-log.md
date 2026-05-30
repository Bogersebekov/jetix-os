---
title: "01 · Build log — как строилась презентация + gap-доки + финмодель (фазы)"
date: 2026-05-30
type: phase-report
parent_prompt: prompts/partner-presentation-build-full-2026-05-30.md
language: russian
---

# 01 · Build log — фазы full presentation build

> Хронология построения (что читалось, что писалось, какие решения). ROY-lens: brigadier-scribe +
> investor-expert (A1) + systems/methodology/philosophy/mgmt + influence-ethics (RECEIVER R12).

## Фаза 0 — substrate read (всё загружено)

Прочитано перед сборкой:
- **Audit doc** (`PRESENTATION-ADDITIONS-AND-GAPS-AUDIT-2026-05-30`) — 4 таблицы picks (все ack'нуты).
- **P-1..P-8 + README** (существующий пакет — тон, структура, mermaid-стиль).
- **4 концепта** (`02-four-concepts.md`) — один R12-контур + 4 guards.
- **Economic V10 LOCKED** — 75/25, 5:1, T_inst=0.25R, recursion (8.33% Ruslan), break-even Y5,
  ~100 партнёров, K≥1.0 Y4, bridge ~€245K, Caja Laboral.
- **METAPLAN-V4** — кланы 7 фаз (§4), правила (§9), хакатоны (§6, ≥$30K/event), мастерская (§1).
- **coach-thesis wiki** — benefit-stack ×7 (WHY).
- **AI-Market LOCKED** — electricity analogy (timing).

## Фаза 1 — финмодель A1 (investor-expert lens)

Построена ПЕРВОЙ (питает слайд 15). 4 блока: unit-econ (3 единицы) · 3 монетизации · treasury/фонд
арифметика (Caja-Laboral, 4 guards) · resource-pooling proof (6 ресурсов, считаемо O-271). **Все числа
= derivation из V10 LOCKED (verbatim recursion/75-25/5:1) + явные допущения (§6, 14 штук).** R12: numbers
no-promise; фонд = реинвест-петля не доходность. 6 mermaid светлых.

## Фаза 2 — gap-доки (добор фундамента)

- **P-9 Кланы** — клан vs команда; Jetix=качалка/склад; 7 фаз lifecycle; пол vs свобода; worked scenario.
- **P-10 Правила** — 2-уровневый Charter (floor 3 + inner-freedom); anti-dark-patterns (#15 gate);
  governance flow (Steward → peer-check → Foundation dispute).
- **P-11 Мастерская** — почему «мастерская» (не курс); 3 грани Foundation; «станки»; online→offline.

Все три = из METAPLAN-V4 §4/§9/§1 + WORKSHOP-CONCEPT, partner-facing, R12-floor, DRAFT R1.

## Фаза 3 — PRESENTATION-MASTER (20 слайдов)

Каркас из §1 промпта (20 слайдов, 5 актов). WHY-first (S1 coach-thesis) → recursive-close (S20 O-281).
Каждый слайд: № · заголовок · сообщение · буллеты · визуал/mermaid · источник · audit-pick. 8 inline
mermaid светлых + reuse-ссылки на P-doc диаграммы (не дублировать). Кульминация акта 3 = S13 (4 концепта
= один R12-контур). Mapping-таблица в конце (полнота picks).

**Решение по структуре:** 20 слайдов (верх диапазона 15-20) — чтобы вместить ВСЕ picks без потери, но
держать каждый слайд тугим (глубина в смыслах, не в объёме — не academic monster).

## Фаза 4 — INDEX-AND-ORDER

Что в презентации (строка/слайд) + порядок рассказа (5 актов + логика переходов) + тайминг (полный
~31 мин / короткий ~12 мин) + 3 альтернативных порядка (founder-first / investor-first / short) + связь
слайд↔P-doc + чеклист для Ruslan. 3 mermaid светлых.

## Фаза 5 — встраивание picks в P-1..P-8

Маркированные блоки «🔖 ... (встроено 2026-05-30, DRAFT R1)» — additive, не переписывая прозу Ruslan'а
(append-only spirit):
- P-1: WHY-opener + recursive-close + ссылки на P-9/10/11/A1.
- P-2: §3.5 intelligence-frame + §6 two-sided.
- P-3: раскрытие #9/#12/#14 → P-9/P-10/P-11.
- P-4: ч.4 cooperation-moat + crypto-enforcement + 4-guards замок.
- P-5: full-stack когорта + resource-pooling + no-false-scarcity.
- P-6: экономика вклада (числа/фонд → A1) + no-promise.
- P-7: «почему сейчас» (AI=электричество).
- P-8: ссылка на Слайд 19 (founder slot = Ruslan, IP-1).

## Фаза 6 — meta-docs + reports

README (новый состав + presentation/ + статус-таблица) · PARTNER-PACKAGE overview (§1.6 append) ·
SUMMARY (≤1200w) · этот build-log · 2 диаграммы.

## Constitutional чек (на каждой фазе)

- **R2 STRICT:** Foundation / 4 LOCKED / V4 — read-only. Invest-fund = суб-грань #4 (НЕ #18). ✅
- **R12 STRICT:** influence-ethics RECEIVER fired на финмодель (numbers) + S13 (moat/коины) + S1/S18
  (benefit-stack) + S10/S12 (#15 gate). Guards видимы. No wealth-promise. ✅
- **R6:** provenance per claim (audit table / P-doc / LOCKED / O-item / Концепт). ✅
- **IP-1:** P-8 / S19 founder = Ruslan only. ✅
- **append-only:** picks = additive блоки; overview = §1.6 append. ✅
