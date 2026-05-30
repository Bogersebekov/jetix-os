---
title: "D2 — покрытие audit-picks (4 таблицы → слайды + P-доки)"
date: 2026-05-30
type: diagram
theme: light (white bg)
parent: decisions/strategic/PRESENTATION-ADDITIONS-AND-GAPS-AUDIT-2026-05-30.md
---

# D2 — Покрытие picks (ничего не потеряно)

> Светлая тема. Зелёный = P0 (несущее) · жёлтый = gap-доки · синий = P1/P2.

```mermaid
%%{init: {'theme':'base','themeVariables':{'background':'#ffffff','mainBkg':'#eef2f7','primaryColor':'#eef2f7','primaryTextColor':'#000','primaryBorderColor':'#555','secondaryColor':'#f5f5f5','tertiaryColor':'#ffffff','textColor':'#000','lineColor':'#333','edgeLabelBackground':'#ffffff','noteBkgColor':'#fff8d5','noteTextColor':'#000','clusterBkg':'#f5f5f5','clusterBorder':'#999','titleColor':'#000'}}}%%
graph LR
    classDef default fill:#eef2f7,stroke:#555,stroke-width:1px,color:#000;
    subgraph T[📋 4 таблицы аудита]
        T1[Таблица 1<br/>ADD to directions]
        T2[Таблица 2<br/>ADD to presentation]
        T3[Таблица 3<br/>TO PROCESS]
        T4[Таблица 4<br/>new dir candidates]
        CC[4 концепта<br/>один R12-контур]
    end
    subgraph P0[🟢 P0 несущее]
        WHY[WHY-opener → S1+P-1]
        NUM[числа → S15+A1+P-6]
        REC[recursive → S20+P-1]
    end
    subgraph GAP[🟡 gap-доки]
        P9[кланы → S11+P-9]
        P10[правила → S12+P-10]
        P11[мастерская → S6+P-11]
    end
    subgraph P12[🔵 P1/P2]
        TIM[timing → S2+P-7]
        MOAT[moat+коины → S13+P-4]
        INTEL[intelligence → S8+P-2]
        TWO[two-sided → S9+P-2]
        COH[когорта → S17+P-5]
        BEN[benefit-stack → S1/S18]
        FND[founder → S19+P-8 Ruslan]
    end
    T2 --> WHY
    T2 --> NUM
    T2 --> REC
    T3 --> NUM
    T1 --> P9
    T1 --> P10
    T2 --> TIM
    T2 --> MOAT
    CC --> MOAT
    T2 --> INTEL
    T2 --> TWO
    T2 --> COH
    T2 --> BEN
    T2 --> FND
    T4 -.инвест-фонд = суб-грань #4 НЕ #18.-> MOAT
    style P0 fill:#d6f0d6,color:#000
    style GAP fill:#fff8d5,color:#000
    style WHY fill:#d6f0d6,color:#000
    style NUM fill:#d6f0d6,color:#000
    style REC fill:#d6f0d6,color:#000
```

**Чтение.** Все P0 (WHY/числа/recursive) → несущие слайды. gap-доки (P-9/10/11) закрывают «невидимые»
направления #14/#9/#12. 4 концепта = один R12-контур → S13 (не 4 разрозненных). Таблица 4: инвест-фонд =
**суб-грань #4**, НЕ новое #18 в V4 (R2 STRICT). Ничего не потеряно.
