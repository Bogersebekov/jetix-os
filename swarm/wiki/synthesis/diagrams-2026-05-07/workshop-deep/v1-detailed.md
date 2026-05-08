---
title: Workshop Information Flow — Deep v1 Detailed
date: 2026-05-08
type: visual
diagram_engine: mermaid
palette: Variant B (Pastel Warm Set2)
parent_TZ: TZ.md
purpose: max detail — все nodes explicit, full information flow + cycles
status: variant-for-comparison
---

# 🏭 Workshop Information Flow — v1 Detailed

> **Версия 1 — Detailed.** Все nodes explicit, full LR layout, максимум detail.
> INPUT источники — каждый отдельной нодой. People / Tools — отдельные ноды.
> Network sidecar + feedback loop bottom.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fc8d62', 'primaryTextColor':'#000', 'primaryBorderColor':'#a35332', 'lineColor':'#555', 'fontFamily':'Inter, system-ui, sans-serif', 'fontSize':'13px'}}}%%
flowchart LR

    %% ═══ INPUT cluster (left) ═══
    INFO["📥 <b>Информация<br/>о мире</b>"]:::cloud
    ARTICLES["📰 Статьи"]:::cloud
    VIDEOS["📺 Видео"]:::cloud
    TALKS["💬 Разговоры"]:::cloud
    HYPO["💡 Гипотезы<br/>/ опыт"]:::cloud

    INFO --- ARTICLES
    INFO --- VIDEOS
    INFO --- TALKS
    INFO --- HYPO

    %% ═══ GUARD ═══
    GUARD{{"🛡️ <b>Охрана</b><br/><small>фильтр входа</small>"}}:::guard

    ARTICLES ==> GUARD
    VIDEOS ==> GUARD
    TALKS ==> GUARD
    HYPO ==> GUARD

    %% ═══ Substrate ═══
    FOUNDATION["🏗 <b>Фундамент</b><br/><small>substrate / git<br/>Foundation v1.0</small>"]:::foundation
    STORAGE[("📦 <b>Склад</b><br/><small>knowledge<br/>base</small>")]:::foundation

    GUARD --> FOUNDATION
    FOUNDATION --> STORAGE

    %% ═══ People cluster ═══
    MASTER(("👤 <b>МАСТЕР</b><br/><small>multi-роль</small>")):::master
    AGENTS["🤖 AI-агенты<br/><small>12 ролей</small>"]:::agent
    COLLAB["👥 Коллабораторы<br/><small>partners / mentors</small>"]:::agent

    STORAGE --> MASTER
    MASTER <--> AGENTS
    MASTER <--> COLLAB

    %% ═══ Tools (несколько станков) ═══
    T_MERMAID["🔧 Mermaid"]:::tools
    T_MCP["🔧 MCP"]:::tools
    T_VOICE["🔧 Voice"]:::tools
    T_PLAN["🔧 Plan Mode"]:::tools

    MASTER --> T_MERMAID
    MASTER --> T_MCP
    MASTER --> T_VOICE
    MASTER --> T_PLAN

    %% ═══ Automation ═══
    AUTO["🤖 <b>Auto pipelines</b><br/><small>cron / sync</small>"]:::auto

    T_MERMAID --> AUTO
    T_MCP --> AUTO
    T_VOICE --> AUTO
    T_PLAN --> AUTO
    AUTO -.->|updates| STORAGE

    %% ═══ Network sidecar ═══
    PHONE["📞 <b>Телефон</b>"]:::phone
    OW1["🏭 Workshop A"]:::other_workshop
    OW2["🏭 Workshop B"]:::other_workshop
    OW3["🏭 Workshop C"]:::other_workshop

    MASTER <--> PHONE
    PHONE <--> OW1
    PHONE <--> OW2
    PHONE <--> OW3
    OW1 -.->|external info| GUARD
    OW2 -.->|external info| GUARD

    %% ═══ Output cluster (right) ═══
    OUTPUT["📤 <b>OUTPUT</b>"]:::cloud
    O_DECISIONS["✅ Решения"]:::cloud
    O_ARTIFACTS["📄 Артефакты<br/><small>статьи / видео<br/>посты</small>"]:::cloud
    O_ACTIONS["⚡ Действия<br/><small>transfers / hires<br/>outreach</small>"]:::cloud

    MASTER ==> OUTPUT
    OUTPUT --- O_DECISIONS
    OUTPUT --- O_ARTIFACTS
    OUTPUT --- O_ACTIONS

    %% ═══ External world ═══
    WORLD["🌍 <b>Внешний мир</b><br/><small>business / жизнь<br/>отношения / health</small>"]:::cloud

    O_DECISIONS ==> WORLD
    O_ARTIFACTS ==> WORLD
    O_ACTIONS ==> WORLD

    %% ═══ Feedback loop ═══
    WORLD -.->|"⟲ feedback /<br/>новая инфа"| INFO

    %% ═══ Style ═══
    classDef cloud fill:#f5f5f5,stroke:#999,stroke-width:2px,color:#000
    classDef guard fill:#e41a1c,stroke:#a00,stroke-width:3px,color:#fff
    classDef foundation fill:#66c2a5,stroke:#2c7a5e,stroke-width:3px,color:#000
    classDef master fill:#fc8d62,stroke:#a35332,stroke-width:4px,color:#000
    classDef agent fill:#fdb18b,stroke:#a35332,stroke-width:2px,color:#000
    classDef tools fill:#fdb18b,stroke:#a35332,stroke-width:2px,color:#000
    classDef auto fill:#e78ac3,stroke:#a64a87,stroke-width:3px,color:#000
    classDef phone fill:#8da0cb,stroke:#4d5a8a,stroke-width:3px,color:#000
    classDef other_workshop fill:#b0bedd,stroke:#4d5a8a,stroke-width:2px,color:#000
```

---

## v1 — что показывает

- **Полный flow:** info sources (4 типа) → GUARD → Substrate → People + Tools + Auto → Output (3 типа) → World
- **Network sidecar:** Phone + 3 Other workshops, info from external workshops back through GUARD
- **Feedback loop:** World → новая инфа → INFO (closing circle)
- **Subgraph не используется** — все nodes на одном уровне

**Pros:** видно всё что в системе. Полная картина.
**Cons:** density — много nodes, может перегружать. Layout LR может вытянуться wide.
