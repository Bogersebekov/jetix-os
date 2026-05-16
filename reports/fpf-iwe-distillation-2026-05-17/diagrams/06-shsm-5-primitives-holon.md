---
title: Diagram 06 — ШСМ 5 primitives + their interrelations (R-B §2 graph)
date: 2026-05-17
type: mermaid
parent: 03-intellect-stack-and-transdisciplines.md + R-B §6
F: F4
G: distillation-diagrams
R: refuted_if_relations_misordered
---

# Diagram 06 — ШСМ 5 primitives holon

> Per R-B §6.1 (verbatim graph):
> ГРАФ СОЗДАНИЯ → задаёт контекст → РОЛИ ↔ СТРАТЕГИРОВАНИЕ
> РОЛИ → работают с → АЛЬФЫ
> АЛЬФЫ → переходы фиксируются → МЫШЛЕНИЕ ПИСЬМОМ
> МЫШЛЕНИЕ ПИСЬМОМ → создаёт контекст → экзокортекс

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'14px'}}}%%
flowchart TB
    GRAF["<b>1. ГРАФ СОЗДАНИЯ</b><br><small>three-level mereology<br>Надсистема ↔ Целевая система ↔ Системы создания<br>(5 typed edges)</small>"]:::root

    ROLE["<b>2. РОЛИ</b><br><small>= сигнатура метода × интерес к системе × набор мастерства<br>(R-B §1.1)<br>NEVER dynamic self-assignment</small>"]:::role

    ALPHA["<b>3. АЛЬФЫ</b><br><small>'предмет метода…<br>может быть и физическим объектом и абстрактным<br>(описанием)'<br>past-participle state graph + checklists</small>"]:::alpha

    STRAT["<b>4. СТРАТЕГИРОВАНИЕ</b><br><small>'метод выбора метода'<br>trigger-driven NOT scheduled<br>3 modes: 1:1 / Adapt / Invent<br>(Invent = human only — NOT AI)</small>"]:::strat

    PISMOM["<b>5. МЫШЛЕНИЕ ПИСЬМОМ</b><br><small>writing-as-thinking<br>cognitive process + onto-tracked text<br>NOT documentation</small>"]:::pismom

    EXO["<b>EXOCORTEX</b><br><small>context input для next AI session<br>'theory death' prevention (Naur)</small>"]:::exo

    GRAF -->|задаёт контекст| ROLE
    GRAF -->|holonic basis| ALPHA
    STRAT -->|chooses what method| ROLE
    STRAT -->|chooses what alphas| ALPHA
    STRAT -.->|may revise| GRAF
    ROLE -->|работают с| ALPHA
    ALPHA -->|state transitions| PISMOM
    PISMOM -->|externalizes| STRAT
    PISMOM -->|produces| EXO

    REFLECT["<b>READING per R-B §6.2:</b><br>• Граф frames<br>• Стратегирование rewrites<br>• Operational order: Strategize → Plan → Work<br>• Continuous: Мышление письмом (cross-cutting)"]:::reflect
    GRAF -.->|reading note| REFLECT

    classDef root fill:#e8eaf6,stroke:#283593,stroke-width:4px
    classDef role fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    classDef alpha fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    classDef strat fill:#fce4ec,stroke:#ad1457,stroke-width:4px
    classDef pismom fill:#e0f2f1,stroke:#00695c,stroke-width:3px
    classDef exo fill:#fff3e0,stroke:#e65100,stroke-width:3px
    classDef reflect fill:#fff8e1,stroke:#f57c00,stroke-width:2px
```

**Provenance.** R-B §6.1 verbatim graph (L700-720) + §6.2 feed-direction table
(L724-736). Cross-cite: A-fpf-spec-5-primitives.md Part 2.
