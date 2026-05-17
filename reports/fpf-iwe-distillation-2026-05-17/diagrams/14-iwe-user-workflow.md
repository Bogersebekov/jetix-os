---
title: IWE user workflow — OWC fractal end-to-end UX
date: 2026-05-17
type: mermaid-diagram
source: reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md §3 + CLAUDE.md §2
F: F6
G: distillation-3
---

# IWE — user workflow (OWC fractal at 4 scales)

> Каждый scale: Открытие → Работа → Закрытие. Triggers + skills + persisted artefacts.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'12px'}}}%%
flowchart TB
    subgraph Month["МЕСЯЦ (Month) — первый Пн месяца"]
        direction LR
        MO["[не определено]"]:::dim
        MW["Между Month Close<br>предыдущего и текущего"]:::work
        MC["/month-close<br>→ stage 7 ВДВ v9"]:::close
        MO --> MW --> MC
    end

    subgraph Week["НЕДЕЛЯ (Week)"]
        direction LR
        WO["[не определено]"]:::dim
        WW["Между Week Close<br>+ Strategy Session"]:::work
        WC["/run-protocol week-close<br>→ WeekReport<br>+ promote staging<br>+ archive proposals"]:::close
        WO --> WW --> WC
    end

    subgraph Day["ДЕНЬ (Day)"]
        direction LR
        DO["/day-open<br>«открывай»<br>→ commits + issues<br>+ Scout + DayPlan"]:::open
        DW["Между Day Open<br>и Day Close"]:::work
        DC["/run-protocol day-close<br>→ R23 Verifier checklist<br>+ updates MEMORY.md<br>+ commit + push"]:::close
        DO --> DW --> DC
    end

    subgraph Session["СЕССИЯ (Session)"]
        direction LR
        SO["protocol-open<br>Любое задание:<br>WP Gate ритуал<br>(Роль/Метод/Артефакт)"]:::open
        SW["protocol-work<br>+ Capture-to-Pack на рубежах<br>+ Self-correction<br>+ Pre-action Gates"]:::work
        SC["/run-protocol close<br>→ R23 Quick Close<br>(>15 min OR file changes)"]:::close
        SO --> SW --> SC
    end

    SC -.->|all sessions of day| DC
    DC -.->|7 days| WC
    WC -.->|~4 weeks| MC

    classDef open fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
    classDef work fill:#fff9c4,stroke:#f9a825,stroke-width:2px
    classDef close fill:#ffccbc,stroke:#bf360c,stroke-width:2px
    classDef dim fill:#eee,stroke:#999,stroke-width:1px,color:#666
```

**Critical gates** (per CLAUDE.md §2):
- **WP Gate** (БЛОКИРУЮЩЕЕ): любое задание → register РП в 4 places (REGISTRY/WeekPlan/context/Linear)
- **Pull-on-Touch**: первое обращение к репо → `git pull --rebase` (lazy)
- **АрхГейт**: любое архитектурное решение → 7-factor ЭМОГССБ profile
- **IntegrationGate**: новый инструмент → 4 фазы (Обещание → Сценарии → Роль → Реализация)

**Artefacts produced per scale.**

| Scale | Artefacts |
|---|---|
| Session | WP-context/<NNN>.md, capture-reports, MEMORY.md updates |
| Day | DayPlan + DayReport + commits + Telegram notifications |
| Week | WeekPlan (next) + WeekReport (last) + staging promotions |
| Month | Month-Close report + Strategy session prep |
