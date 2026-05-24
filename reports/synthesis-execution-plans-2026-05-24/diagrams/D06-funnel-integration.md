---
title: D06 — PoD Шаг 2 Conversion Funnel + plan integration (Stages 0-7 × substrate × R12)
date: 2026-05-24
type: mermaid-diagram
parent: prompts/synthesis-execution-plans-2026-05-24.md
F: F2
---

# D06 — Funnel Integration

> PoD 24.05 Шаг 2 Conversion Funnel (Stranger → Cohort Member) с substrate mapping per batch-13 Phase 4 + Propaganda P4 R12-compatible pipeline + cohort-target-ontology O-161/O-162. Per Phase 2 §6.5 + batch-13 Phase 4 integration mapping.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TD
    Stage0[Stage 0<br/>Stranger]
    Stage1[Stage 1<br/>Awareness<br/>видел content / прочитал страницу]
    Stage2[Stage 2<br/>Interest<br/>запросил materials / посмотрел video]
    Stage3[Stage 3<br/>Engagement<br/>read substrate / contact request]
    Stage4[Stage 4<br/>Discovery call<br/>30-60 min]
    Stage5[Stage 5<br/>Trial<br/>template / Notion tool — Дмитрий-style]
    Stage6[Stage 6<br/>Partner / Cohort member<br/>Charter signed]
    Stage7[Stage 7<br/>Advocate<br/>active spreader]

    Stage0 --> Stage1 --> Stage2 --> Stage3 --> Stage4 --> Stage5 --> Stage6 --> Stage7

    subgraph Substrate0_1[Stage 0-1 Substrate]
        S01a[O-166 library positioning]
        S01b[O-167 world-wide frame]
        S01c[O-174 founder persona]
    end
    Stage1 -.feeds.- Substrate0_1

    subgraph Substrate1_2[Stage 1-2 Substrate]
        S12a[O-169 web-сайт 6 sections]
        S12b[O-170 axiom-chain anchor]
        S12c[P2 Welcome-frame 9-section]
    end
    Stage2 -.feeds.- Substrate1_2

    subgraph Substrate2_3[Stage 2-3 Substrate]
        S23a[O-170 cascade deepen]
        S23b[O-173 embedded-development]
        S23c[O-171 mechanism intro]
    end
    Stage3 -.feeds.- Substrate2_3

    subgraph Substrate3_5[Stage 3-5 Substrate]
        S35a[O-171 ⭐⭐⭐ point-A→B template HEART]
        S35b[O-173 embedded-development deepen]
        S35c[P3 cohort target ontology<br/>Hungry/Disciplined/Ready]
        S35d[O-175 testing-posture]
    end
    Stage4 -.feeds.- Substrate3_5
    Stage5 -.feeds.- Substrate3_5

    subgraph Substrate6_7[Stage 6-7 Substrate]
        S67a[O-168 tier-structure<br/>free / Corp / Кланы]
        S67b[O-172 ⚠️R12 civilizational vision<br/>R12 audit pending]
        S67c[Charter draft + onboarding kit]
    end
    Stage6 -.feeds.- Substrate6_7
    Stage7 -.feeds.- Substrate6_7

    subgraph R12disc[🚦 R12-compatible pipeline disciplines]
        R12a[Pull-not-push: opt-in only]
        R12b[Self-selection]
        R12c[24h cooldown System-2]
        R12d[Reversibility]
        R12e[Member-portable artifacts]
        R12f[Alumni-respect]
        R12g[Fork-and-leave preserved]
    end
    Stage4 -.discipline.- R12disc
    Stage5 -.discipline.- R12disc
    Stage6 -.discipline.- R12disc

    PoD([🎯 PoD Шаг 2 §A-E<br/>Conversion Funnel central doc])
    PoD --> Stage0

    style Stage0 fill:#fafafa
    style Stage5 fill:#ffd6d6
    style Stage6 fill:#ffd6d6
    style S35a fill:#ffd6d6
    style S67a fill:#ffe0a0
    style S67b fill:#ffe0a0
    style PoD fill:#d6e0f0
```

## Per-stage 4-cell (per audio_732+733 + Propaganda P3 + P4)

| Stage | Делать | Уметь | Принести | Зачем им это |
|---|---|---|---|---|
| 0-1 Stranger/Awareness | Прочитать положение | Различить «работающее» | – | Доступ к «только работающему» |
| 1-2 Interest | Запросить materials | Self-onboard через сайт | – | Clarity «как можно быстрее» |
| 2-3 Engagement | Принять axiom | Применить «ответственная info-переработка» | – | «Эффективное развитие в 10 раз» |
| 3-5 Discovery/Trial | Описать точку А → Б | Адопт template (point-A→B + daily reporting + time tracking) | Свой intellect + responsibility + дисциплина | Освобождение intellect/attention → 10x efficiency |
| 5-6 Partner/Кланы | Pay membership / Sign Charter | Создать платформу improved | %-share revenue + audience + skill + time | Free=life / Corp=monetization / Кланы=co-create + ownership |
| 7 Advocate | Spread world-wide regardless of locality | – | – | Mutual benefit: лучше система → лучше работает он |

## Plan A/B/C/D × Funnel coverage

| Plan | Stages covered immediately |
|---|---|
| Plan A Video-first | Stages 0-3 (video distribution) + Stage 4 (discovery call follow-up) |
| Plan B Doc-first | Stages 0-7 (full funnel doc + per-stage docs) |
| Plan C Notion-hybrid | Stages 3-7 deep test (Дмитрий-Сева actual trial) |
| Plan D Path A МИМ | Stages 6-7 partnership-tier (long-term Wave 1 institutional) |
