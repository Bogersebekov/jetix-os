---
title: "D1 — нарративная дуга презентации (5 актов, 20 слайдов)"
date: 2026-05-30
type: diagram
theme: light (white bg)
parent: partner-package/presentation/PRESENTATION-MASTER-2026-05-30.md
---

# D1 — Нарративная дуга (WHY-first → recursive-close)

> Светлая тема. Жёлтый = вход/выход (зацепить/закрыть) · красный = кульминация/гарантии · синий = «как».

```mermaid
%%{init: {'theme':'base','themeVariables':{'background':'#ffffff','mainBkg':'#eef2f7','primaryColor':'#eef2f7','primaryTextColor':'#000','primaryBorderColor':'#555','secondaryColor':'#f5f5f5','tertiaryColor':'#ffffff','textColor':'#000','lineColor':'#333','edgeLabelBackground':'#ffffff','noteBkgColor':'#fff8d5','noteTextColor':'#000','clusterBkg':'#f5f5f5','clusterBorder':'#999','titleColor':'#000'}}}%%
graph TB
    classDef default fill:#eef2f7,stroke:#555,stroke-width:1px,color:#000;
    subgraph A1[🎯 АКТ 1 · ЗАЧЕМ]
        S1[1 с тренером лучше<br/>benefit-stack ×7]
        S2[2 почему сейчас<br/>AI=электричество]
    end
    subgraph A2[🧱 АКТ 2 · ЧТО ЭТО]
        S3[3 база] --> S4[4 3P] --> S5[5 проблема] --> S6[6 суть] --> S7[7 усилитель]
    end
    subgraph A3[⚙️ АКТ 3 · КАК РАБОТАЕТ]
        S8[8 метод+интеллект] --> S9[9 two-sided] --> S10[10 карта 16]
        S10 --> S11[11 кланы 7 фаз] --> S12[12 правила] --> S13[⭐13 кооперация-moat<br/>4 концепта = 1 контур]
    end
    subgraph A4[💎 АКТ 4 · ГАРАНТИИ+ЧИСЛА]
        S14[14 ценности R12] --> S15[⭐15 числа<br/>иллюстрация] --> S16[16 таймлайн]
    end
    subgraph A5[🤝 АКТ 5 · ТЫ+ЗАКРЫТИЕ]
        S17[17 когорта] --> S18[18 чем помочь] --> S19[19 участие+кто я<br/>🚧 Ruslan] --> S20[20 recursive close]
    end
    A1 --> A2 --> A3 --> A4 --> A5
    S20 --> END([💬 созвон ИЛИ «спасибо, не моё»])
    style A1 fill:#fff8d5,color:#000
    style S13 fill:#ffd6d6,color:#000
    style S15 fill:#ffd6d6,color:#000
    style A4 fill:#f5f5f5,color:#000
    style S20 fill:#fff8d5,color:#000
    style END fill:#d6f0d6,color:#000
```

**Чтение.** Сдвиг vs пакета: ведём «зачем» (S1-2) ПЕРВЫМ, потом «что это» (S3-7). Кульминация «как» =
S13 (moat). Числа (S15) идут после того, как партнёр поверил в идею. Закрытие = рекурсивная петля +
просьба об обратной связи (не подписи).
