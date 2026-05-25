---
title: Phase 13 — Architecture mermaid suite ARCH-1..ARCH-10 (Notion 4-Layers Architecture)
date: 2026-05-25
type: phase-report-mermaid-suite
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 13
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + append-only
language: russian primary
mermaid: [ARCH-1, ARCH-2, ARCH-3, ARCH-4, ARCH-5, ARCH-6, ARCH-7, ARCH-8, ARCH-9, ARCH-10]
---

# Phase 13 — 📐 Architecture mermaid suite (ARCH-1..ARCH-10)

> **Что в этой фазе.** Консолидированный каталог 10 схем. ARCH-1..ARCH-6 встроены в Phase 1/6/7/8/11
> (ссылки ниже); ARCH-7..ARCH-10 авторизованы здесь. Каждая ≥10-15 nodes, light bg theme.

---

## Каталог 10 схем

| # | Схема | Где тело | Тип |
|---|---|---|---|
| ARCH-1 | 4 layers stack | Phase 1 (02-overview) | graph TB |
| ARCH-2 | cross-layer dependencies + inheritance | Phase 1 (02-overview) | graph LR |
| ARCH-3 | cross-layer data flows | Phase 6 (07-data-flows) | graph TB |
| ARCH-4 | permissions heat matrix | Phase 7 (08-permissions) | graph TB |
| ARCH-5 | sync mechanics | Phase 8 (09-sync) | sequenceDiagram |
| ARCH-6 | implementation timeline | Phase 11 (12-roadmap) | gantt |
| ARCH-7 | Layer 4 executive dashboard layout | **здесь** | graph TB |
| ARCH-8 | R12 risk heat overlay per layer | **здесь** | graph LR |
| ARCH-9 | fork-and-leave preservation flow | **здесь** | graph TD |
| ARCH-10 | master synthesis diagram | **здесь** | graph TB |

---

## ARCH-7 — Layer 4 Executive Dashboard layout

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    CC([⭐ Executive Command Center<br/>«весь бизнес на одной странице»])
    CC --> BRIEF[📊 §5.11 Daily/Weekly Briefing<br/>5 секций · DRAFT-only]
    BRIEF --> CRIT[🚨 Critical attention ≤5]
    BRIEF --> HEALTH[📈 Health snapshot]
    BRIEF --> PROG[🎯 Progress]
    BRIEF --> PPL[🤝 People movement]
    BRIEF --> STR[💡 Strategic threads]

    CC --> STRAT[🎯 §5.1 Strategy/Goals]
    CC --> FIN[💰 §5.2 Financial · runway gauge]
    CC --> PROJ[🚀 §5.4 Projects portfolio]
    CC --> STK[🤝 §5.5 Stakeholders pipeline]
    CC --> DEC[⚖️ §5.6 Decisions awaiting]
    CC --> RISK[🛡️ §5.7 Top risks]

    FIN -.runway<3 → 🔴.-> CRIT
    RISK -.high score.-> CRIT
    STK -.expiring contract.-> CRIT
    STRAT -.at-risk goal.-> CRIT
    PROJ -.rollup health.-> HEALTH
    FIN -.revenue delta.-> HEALTH

    CC --- OVR[(🟧 Jetix overlay §5.X<br/>R12 · Mondragón · Charter · 10 ролей<br/>= optional)]
    style CC fill:#ffe0a0,color:#000
    style BRIEF fill:#fff4cc,color:#000
    style CRIT fill:#ffd6d6,color:#000
    style FIN fill:#d6f0d6,color:#000
    style OVR fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```
**ARCH-7.** Executive Command Center: 6 групп + брифинг (5 секций); критичные сигналы (runway/risk/contract/goal) текут в Critical attention; Jetix-overlay опционален.

---

## ARCH-8 — R12 risk heat overlay per layer

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    L1[🟢 Layer 1<br/>НИЗКИЙ<br/>privacy/lock-in]
    L2[🟢🟡 Layer 2<br/>НИЗ-СРЕДН<br/>self-surveillance]
    L3[🟡🔴 Layer 3<br/>СРЕДН-ВЫС<br/>монетизация/cohort]
    L4[🔴 Layer 4<br/>ВЫСОКИЙ<br/>концентрация контроля]

    L1 -->|защита растёт| L2 -->|быстрее системы| L3 -->|⚖️ закон| L4

    L1 --- M1[файлы=правда<br/>export · нет имён]
    L2 --- M2[тон уроки-не-суд<br/>DRAFT-only · не наверх]
    L3 --- M3[8-Q · 4 classes · 5:1<br/>анти-секта · Steward HALT]
    L4 --- M4[VOTE guard · auditor<br/>нейтр.base · overlay opt-in]

    L3 -.primary R12 surface.-> STW[⚖️ Steward enforcement]
    L4 -.authoritarian drift.-> STW
    STW --> HALT[🛑 HALT F2/F4/F8 ≤5с]
    FORK[🚪 fork-and-leave preserved ВСЕ слои]
    L1 -.-> FORK
    L4 -.-> FORK
    style L1 fill:#d6f0d6,color:#000
    style L2 fill:#eaf6c8,color:#000
    style L3 fill:#ffd9b3,color:#000
    style L4 fill:#ffd6d6,color:#000
    style STW fill:#fff4cc,color:#000
    style HALT fill:#ffcccc,color:#000
    style FORK fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```
**ARCH-8.** R12-риск растёт L1→L4; защита растёт быстрее; L3+L4 = primary surfaces → Steward HALT; fork-and-leave сквозной.

---

## ARCH-9 — Fork-and-leave preservation flow

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    USER([👤 Участник решает уйти])
    USER --> Q{С какого слоя?}
    Q -->|Layer 1/2| L12[🟢 личный воркспейс<br/>остаётся полностью<br/>= его собственность]
    Q -->|Layer 3 cohort| L3FLOW[🔵 fork-and-leave процедура]
    L3FLOW --> ANN[1 объявление выхода<br/>Decisions Queue]
    ANN --> WIN[2 30-day window<br/>при изменении Charter]
    WIN --> ASSET[3 asset retrieval<br/>Ledger строка + доля]
    ASSET --> SHARE[4 proportional share<br/>БЕЗ штрафа]
    SHARE --> NEUTRAL[5 не-punitive язык]
    Q -->|Layer 4 founder| L4[⭐ бизнес продолжается<br/>Scale: founder=1 из многих]

    L12 -.не трогается.-> SAFE[💾 данные сохранены]
    NEUTRAL --> SAFE
    L4 --> SAFE
    ATTEMPT[🚫 fork_prevention_attempt<br/>«теперь не уйдёшь»] --> HALT[🛑 HALT F4 ≤5с<br/>Steward + лог]
    SAFE -.архитектурно: раздельные воркспейсы.-> GUARANTEE[✅ leak/lock невозможен<br/>= структура, не обещание]
    style USER fill:#d6e0f0,color:#000
    style L12 fill:#d6f0d6,color:#000
    style SHARE fill:#fff4cc,color:#000
    style HALT fill:#ffcccc,color:#000
    style GUARANTEE fill:#d6f0d6,color:#000
    style ATTEMPT fill:#ffd6d6,color:#000
```
**ARCH-9.** Fork-and-leave: L1/2 данные остаются; L3 = 5-шаговая процедура (объявление→30day→asset→доля→нейтрально); L4 founder exit = бизнес продолжается; fork_prevention → HALT; гарантия архитектурна.

---

## ARCH-10 — Master synthesis (вся архитектура одной схемой)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph PERSONAL["🟢🟡 Личное (приватный воркспейс)"]
        L1[🟢 L1 Personal Core<br/>5-8 баз · ≤30мин fork]
        L2[🟡 L2 Expanded<br/>Reviews · гипотезы · аналитика]
        L1 -->|апгрейд| L2
    end
    subgraph TEAM["🔵 Командное (shared Teamspace)"]
        L3[🔵 L3 Team Collab<br/>10 ролей · биржа · Charter<br/>4 монетизации · Daily Brief]
    end
    subgraph BIZ["⭐ Бизнес (executive)"]
        L4[⭐ L4 Universal Business<br/>12 групп · framework-agnostic<br/>standalone-capable]
        OVR[(🟧 overlay §5.X opt:<br/>Jetix/VC/agency/none)]
        L4 --- OVR
    end

    L1 -.у каждого участника.-> L3
    L1 ==>|⬆️ opt-in publish| L3
    L3 ==>|⬆️ rollup агрегация| L4
    L4 -.⬇️ контроль/направление.-> L3
    L3 -.⬇️ сигнал/уведомление.-> L1
    PRIV[🔐 NEVER up:<br/>Daily Log·Pulse·Finances] -.🚫.-> X[не течёт]

    DISC[📐 Сквозное:<br/>файлы=правда · DRAFT-only<br/>роль≠человек IP-1 · fork-and-leave]
    DISC -.-> PERSONAL
    DISC -.-> TEAM
    DISC -.-> BIZ
    R12[⚖️ R12 risk 🟢→🔴<br/>защита растёт быстрее] -.-> TEAM
    R12 -.-> BIZ
    FND[🧍 founder-одиночка] -->|standalone start| L4

    style L1 fill:#d6f0d6,color:#000
    style L2 fill:#fff4cc,color:#000
    style L3 fill:#cce6ff,color:#000
    style L4 fill:#ffe0a0,color:#000
    style OVR fill:#eeeeee,color:#000,stroke-dasharray: 5 5
    style PRIV fill:#ffd6d6,color:#000
    style DISC fill:#d6e0f0,color:#000
    style R12 fill:#ffd6d6,color:#000
```
**ARCH-10 — master synthesis.** 4 слоя × 2 оси (личное/командное/бизнес); потоки ⬆️opt-in/rollup ⬇️контроль/сигнал; privacy core не течёт; сквозные дисциплины (файлы=правда / DRAFT / IP-1 / fork-leave); R12 растёт; overlay опционален; founder может стартовать с L4.

---

## §1 Mermaid theme (для всех 10)

```
{'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000',
'lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}
```
Light bg, чёрный текст, читаемо в Notion light mode + при экспорте.

---

*Phase 13 closure. 10 схем ARCH-1..ARCH-10: 1-6 встроены в фазы, 7-10 авторизованы здесь
(executive dashboard / R12 heat / fork-leave flow / master synthesis). Каждая ≥10-15 nodes, light
theme. Дальше Phase 14 — Main consolidated + 00-SUMMARY + per-layer matrix + INDEX (final push).*
