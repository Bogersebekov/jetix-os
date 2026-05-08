---
title: Workshop 7 elements — Variant A (Cool Blues / YlGnBu sequential)
date: 2026-05-08
type: visual-variant
diagram_engine: mermaid
palette_source: ColorBrewer 2.0 — 4-class YlGnBu sequential + red accent
palette: "#ffffcc / #a1dab4 / #41b6c4 / #225ea8 + #e41a1c (guard accent)"
parent_diagram: 01-workshop-7-elements.md
audience: Цэрэн / Левенчук / Mittelstand partners
purpose: вариант A — cool sequential для visual depth (foundation deep → cloud lightest)
F: F4
status: variant-for-comparison
---

# 🏭 Variant A — Cool Blues (YlGnBu sequential)

> Палитра ColorBrewer YlGnBu — sequential от светло-жёлтого до тёмно-синего.
> Глубина = "глубже элемент → темнее цвет". Foundation самый темный (как фундамент дома), Cloud INPUT/OUTPUT самые светлые.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#ffffcc', 'primaryTextColor':'#000', 'primaryBorderColor':'#225ea8', 'lineColor':'#555', 'fontFamily':'Inter, system-ui, sans-serif', 'fontSize':'14px'}}}%%
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

    classDef cloud fill:#ffffcc,stroke:#888,stroke-width:2px,color:#000
    classDef guard fill:#e41a1c,stroke:#a00,stroke-width:3px,color:#fff
    classDef foundation fill:#225ea8,stroke:#0d2858,stroke-width:3px,color:#fff
    classDef storage fill:#41b6c4,stroke:#1a6e7d,stroke-width:3px,color:#000
    classDef master fill:#a1dab4,stroke:#225ea8,stroke-width:4px,color:#000
    classDef tools fill:#a1dab4,stroke:#41b6c4,stroke-width:3px,color:#000
    classDef auto fill:#41b6c4,stroke:#225ea8,stroke-width:3px,color:#000
    classDef phone fill:#225ea8,stroke:#0d2858,stroke-width:3px,color:#fff

    style WORKSHOP fill:#ffffcc,stroke:#225ea8,stroke-width:4px
```

---

## Цветовая семантика Variant A

| Элемент | Цвет | Значение |
|---|---|---|
| INPUT / OUTPUT | `#ffffcc` светло-жёлтый | граница системы, самый "лёгкий" слой |
| GUARD | `#e41a1c` red | accent — фильтр опасности (как roads на ColorBrewer maps) |
| FOUNDATION | `#225ea8` deep blue | глубочайший слой — substrate |
| STORAGE | `#41b6c4` turquoise | средняя глубина — knowledge layer |
| MASTER | `#a1dab4` light green | live центр — действующее лицо |
| TOOLS | `#a1dab4` light green (lighter stroke) | extension мастера |
| AUTO | `#41b6c4` turquoise | автоматический pipeline |
| PHONE | `#225ea8` deep blue | внешняя сеть, deep как foundation |

**Vibe:** профессиональный / спокойный / "data viz" / cool tones / good for B2B Mittelstand.
