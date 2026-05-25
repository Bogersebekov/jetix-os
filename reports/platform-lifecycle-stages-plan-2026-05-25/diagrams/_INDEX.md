---
title: Diagrams INDEX — Platform Lifecycle Stages Plan (PL-1..PL-5)
date: 2026-05-25
type: platform-lifecycle-diagrams-index
parent_main: decisions/strategic/PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md
schemes_file: reports/platform-lifecycle-stages-plan-2026-05-25/09-mermaid-schemes.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
language: russian primary
---

# 🎨 Diagrams INDEX — PL-1..PL-5

Все диаграммы: светлый фон, чёрный текст, ≥10 узлов, inline-ready. Полный код —
`09-mermaid-schemes.md`. Встроены также в main-документ.

| # | Диаграмма | Тип | Что показывает | Где в main | Source phase |
|---|---|---|---|---|---|
| **PL-1** | Три этапа Build→Run→Scale | graph LR (subgraphs) | входы/выходы/ловушки каждого этапа; маркер «кто крутит маховик» | §2 | Phase 2 §E |
| **PL-2** | Карта акторов по этапам | graph TB (subgraphs) | T1-T4 × stages + переходы (тестер→адвокат, методолог→клан); R12-градиент | §4 | Phase 3 §E |
| **PL-3** | Матрица обмена + R12-риск | graph LR (subgraphs) | даём × просим per stage + защита + соблазн; цвет = R12 🟢🟡🔴 | §5 | Phase 4 §E |
| **PL-4** | Жизненный цикл документов | graph LR (subgraphs) | docs перетекают: мы→партнёр→органика; LOCKED reference сквозь все | §6 | Phase 5 §F |
| **PL-5** | Таймлайн А→B→C→D | graph LR | где сейчас (А=факты) → куда идём (B/C/D=направление); наложено на этапы | §3 | Phase 6 §F |

**Дополнительные (не PL-номерные, поддерживающие):**

| Диаграмма | Тип | Где |
|---|---|---|
| Build stage state diagram | stateDiagram-v2 | Phase 2 §A |
| Run stage state diagram | stateDiagram-v2 | Phase 2 §B |
| Scale stage state diagram + защиты | stateDiagram-v2 | Phase 2 §C |
| Build 4-week zoom + transition gate | graph TB | Phase 7 §H + main §8 |

**Итого:** 5 канонических PL-схем + 4 поддерживающих = 9 диаграмм. Все ≥10 узлов, светлый фон.

**Дисциплина рендера:** `%%{init theme:base, primaryTextColor:#000, ...}%%` шапка в каждой
схеме — чёрный текст на светлом фоне, читаемо для шаринга / лендинга / звонков.
