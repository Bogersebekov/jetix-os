---
type: diagram
title: ML engineer 7-step workflow (image 2 reproduced)
date: 2026-05-18
source: Ruslan-shared infographic «Чем занимается ML-инженер»
---

# Diagram 02 — ML workflow 7 steps

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    S1[Шаг 1<br/>Постановка задачи<br/>метрики<br/>общение с заказчиком]
    S2[Шаг 2<br/>Сбор данных<br/>аналитика<br/>выборка + валидация]
    S3[Шаг 3<br/>Обучение модели<br/>baseline → advanced]
    S4[Шаг 4<br/>Улучшение качества<br/>гипотезы<br/>feature generation]
    S5[Шаг 5<br/>Тестирование<br/>A/B tests]
    S6[Шаг 6<br/>Развертывание модели]
    S7[Шаг 7<br/>Дообучение<br/>поддержка<br/>улучшения]

    S1 -->|defines problem| S2
    S2 -->|provides substrate| S3
    S3 -->|baseline established| S4
    S4 -->|improved candidate| S5
    S5 -->|validated| S6
    S6 -->|in production| S7
    S7 -.drift detected.-> S3
    S7 -.major change.-> S1
    S7 -.compound learning.-> CL[Methodology evolution]
    CL -.feedback.-> S1

    subgraph "Strategic bookends"
        direction LR
        S1
        S7
    end

    subgraph "Tactical execution"
        direction LR
        S2
        S3
        S4
        S5
        S6
    end

    style S1 fill:#ffd6f0
    style S7 fill:#ffd6f0
    style S2 fill:#d6f0d6
    style S3 fill:#d6f0d6
    style S4 fill:#d6f0d6
    style S5 fill:#d6f0d6
    style S6 fill:#d6f0d6
    style CL fill:#fff4e6
```

**Цветовая легенда:**
- 🟣 Strategic bookends: Step 1 (framing) + Step 7 (compound learning)
- 🟢 Tactical execution: Steps 2-6
- 🟡 Methodology evolution: compound learning feedback loop

**Cross-link:** doc 06 (per-step analysis) + doc 07 (universal pattern claim).
