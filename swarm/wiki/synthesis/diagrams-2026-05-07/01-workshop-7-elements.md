---
title: Workshop — 7 базовых элементов мастерской
date: 2026-05-07
type: visual
diagram_engine: mermaid
source: BASE-MANAGEMENT-SYSTEM-2026-05-04.md §1.3 + JETIX-WORKSHOP-CONCEPT-2026-04-30.md §3
audience: Цэрэн / Левенчук / Mittelstand partners / future Jetix members
purpose: визуализация архитектуры мастерской — 7 функциональных элементов + информационный поток INPUT → WORKSHOP → OUTPUT
---

# 🏭 Мастерская — 7 базовых элементов

> Скелет любой мастерской. Каждый мастер обвешивает скелет своими специфическими станками и процессами.
> Главный принцип — **всё, с чем работаем, это информация**.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fff8e1', 'primaryTextColor':'#000', 'primaryBorderColor':'#f57c00', 'lineColor':'#555', 'fontFamily':'Inter, sans-serif', 'fontSize':'14px'}}}%%
flowchart TB
    INPUT(["📥 <b>INPUT</b><br/><i>информация о мире</i>"]):::cloud

    subgraph WORKSHOP ["🏭 МАСТЕРСКАЯ"]
        direction TB

        GUARD{{"🛡️ Охрана<br/><small>фильтр входа</small>"}}:::guard
        FOUNDATION["🏗 Фундамент<br/><small>substrate / git / naming</small>"]:::foundation
        STORAGE[("📦 Склад<br/><small>knowledge base</small>")]:::storage

        MASTER(("👤 <b>МАСТЕР</b><br/><small>+ AI-агенты<br/>+ collaborators</small>")):::master

        TOOLS["🔧 Станки<br/><small>D2 / MCP / Voice<br/>adaptable за день</small>"]:::tools
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

    classDef cloud fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    classDef guard fill:#ffebee,stroke:#c62828,stroke-width:3px,color:#000
    classDef foundation fill:#e8eaf6,stroke:#283593,stroke-width:3px,color:#000
    classDef storage fill:#e0f2f1,stroke:#00695c,stroke-width:3px,color:#000
    classDef master fill:#fce4ec,stroke:#ad1457,stroke-width:4px,color:#000
    classDef tools fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#000
    classDef auto fill:#f3e5f5,stroke:#6a1b9a,stroke-width:3px,color:#000
    classDef phone fill:#e1f5fe,stroke:#01579b,stroke-width:3px,color:#000

    style WORKSHOP fill:#fff8e1,stroke:#f57c00,stroke-width:4px
```

---

## 📖 7 элементов — что каждый делает

| # | Элемент | Функция в системе |
|---|---------|-------------------|
| 1 | 🏗 **Фундамент** | substrate — где живут данные, единый язык (даты / naming / тэги). Без него мастерская развалится за неделю |
| 2 | 🛡️ **Охрана** | фильтр на входе — спам, низкокачественные источники, отвлечения отсекаются |
| 3 | 📦 **Склад** | сырьё (источники) + полуфабрикаты (drafts) + готовые изделия. Структурированный, найти за секунды |
| 4 | 🔧 **Станки** | adaptable инструменты под конкретные операции. Главное свойство — добавляются за день, удаляются без боли |
| 5 | 👤 **Мастера** | владелец + AI-агенты + human collaborators. Многостаночник по ролям |
| 6 | 🤖 **Автоматизация** | sync pipelines / cron jobs / scheduled reviews. Мастер занимается мастерством, рутина платится минимально |
| 7 | 📞 **Телефон** | связь с другими мастерами. Не строй с нуля — запроси у того, у кого уже есть |

---

## 🔗 Source

- [decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md §1.3](../../../../decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md) — Документ 1A LOCKED v1.0
- [decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md §3](../../../../decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md) — Workshop concept LOCKED canonical
