---
title: Workshop 7 elements — Variant B (Pastel Warm / Set2 qualitative)
date: 2026-05-08
type: visual-variant
diagram_engine: mermaid
palette_source: ColorBrewer 2.0 — 4-class Set2 qualitative + red accent
palette: "#66c2a5 / #fc8d62 / #8da0cb / #e78ac3 + #e41a1c (guard) + #f5f5f5 (cloud)"
parent_diagram: 01-workshop-7-elements.md
audience: Цэрэн / Левенчук / Mittelstand partners
purpose: вариант B — pastel warm для category distinction (каждая группа уникальный цвет)
F: F4
status: variant-for-comparison
---

# 🏭 Variant B — Pastel Warm (Set2 qualitative)

> Палитра ColorBrewer Set2 — 4 distinct pastel category colors.
> Каждая функциональная группа имеет свой цвет: Substrate = green, Work = orange, Network = blue-lavender, Automation = pink.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fc8d62', 'primaryTextColor':'#000', 'primaryBorderColor':'#a35332', 'lineColor':'#555', 'fontFamily':'Inter, system-ui, sans-serif', 'fontSize':'14px'}}}%%
flowchart TB
    INPUT(["📥 <b>INPUT</b><br/><i>информация о мире</i>"]):::cloud

    subgraph WORKSHOP ["🏭 МАСТЕРСКАЯ"]
        direction TB

        GUARD{{"🛡️ Охрана<br/><small>фильтр входа</small>"}}:::guard
        FOUNDATION["🏗 Фундамент<br/><small>substrate / git / naming</small>"]:::foundation
        STORAGE[("📦 Склад<br/><small>knowledge base</small>")]:::storage

        MASTER(("👤 <b>МАСТЕР</b><br/><small>+ AI-агенты<br/>+ collaborators</small>")):::master

        TOOLS["🔧 Станки<br/><small>Mermaid / MCP / Voice<br/>adaptable за день</small>"]:::tools
        AUTO["🤖 Автоматизация<br/><small>cron / sync / pipelines</small>"]:::auto
        PHONE["📞 Телефон<br/><small>сеть других мастеров</small>"]:::phone

        GUARD --> FOUNDATION
        FOUNDATION --> STORAGE
        STORAGE --> MASTER
        MASTER <--> TOOLS
        TOOLS --> AUTO
        AUTO -.->|updates| STORAGE
        MASTER <--> PHONE
    end

    OUTPUT(["📤 <b>OUTPUT</b><br/><i>решения / артефакты / действия</i>"]):::cloud

    INPUT ==>|сырая информация| GUARD
    MASTER ==>|готовый результат| OUTPUT

    classDef cloud fill:#f5f5f5,stroke:#999,stroke-width:2px,color:#000
    classDef guard fill:#e41a1c,stroke:#a00,stroke-width:3px,color:#fff
    classDef foundation fill:#66c2a5,stroke:#2c7a5e,stroke-width:3px,color:#000
    classDef storage fill:#66c2a5,stroke:#2c7a5e,stroke-width:3px,color:#000
    classDef master fill:#fc8d62,stroke:#a35332,stroke-width:4px,color:#000
    classDef tools fill:#fc8d62,stroke:#a35332,stroke-width:3px,color:#000
    classDef auto fill:#e78ac3,stroke:#a64a87,stroke-width:3px,color:#000
    classDef phone fill:#8da0cb,stroke:#4d5a8a,stroke-width:3px,color:#000

    style WORKSHOP fill:#fff8f0,stroke:#fc8d62,stroke-width:4px
```

---

## Цветовая семантика Variant B

| Элемент | Цвет | Значение |
|---|---|---|
| INPUT / OUTPUT | `#f5f5f5` light grey | нейтральная граница системы |
| GUARD | `#e41a1c` red | accent — фильтр опасности (как roads на ColorBrewer maps) |
| FOUNDATION + STORAGE | `#66c2a5` green | базовый слой — substrate + knowledge |
| MASTER + TOOLS | `#fc8d62` orange | центр работы — live actor + extensions |
| AUTO | `#e78ac3` pink | автоматизация — non-human pipelines |
| PHONE | `#8da0cb` blue-lavender | внешняя сеть |

**Vibe:** тёплый / friendly / pastel / "people-first" / good for founder pitch / human storytelling.
