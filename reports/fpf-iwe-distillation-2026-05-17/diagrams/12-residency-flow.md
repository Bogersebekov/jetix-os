---
title: Diagram 12 — МИМ residency flow (R0 → R1 → R2 → masters)
date: 2026-05-17
type: mermaid
parent: 05-residencies-format.md
F: F4
G: distillation-diagrams
R: refuted_if_track_progression_misordered
---

# Diagram 12 — МИМ Residency Flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'13px'}}}%%
flowchart TB
    ENTRY["<b>Entry: no prerequisites</b><br><small>Free registration aisystant.system-school.ru<br>«Бесконечное развитие» subscription для homework</small>"]:::entry

    subgraph R0_TRACK["<b>R0 — Рациональная работа / Собранность</b><br><small>~10 weeks · Tuesdays 18:00 + Saturdays 11:30<br>min 10-15 hrs/week · Autumn 2025 sample</small>"]
        R0_GUIDE["Online guide:<br>attention management, lean working,<br>anti-procrastination"]:::guide
        R0_IWE["IWE assistance<br>(personal progress tracking)"]:::iwe
        R0_RAZBOR["Weekly разбор<br>(mentor + cohort<br>review of own projects)"]:::razbor
        R0_OUTCOME["<b>Outcome:</b> Собранность practice +<br>method-tuned working habits"]:::outcome
        R0_GUIDE --> R0_RAZBOR
        R0_IWE --> R0_RAZBOR
        R0_RAZBOR --> R0_OUTCOME
    end

    subgraph R1_TRACK["<b>R1 — Системное мышление + Методология</b><br><small>~19 sessions · Tuesdays 18:00-20:00 · Spring 2026 sample</small>"]
        R1_GUIDE["Online guides:<br>Сис.мышление 2024 (2 vol) +<br>Методология 2025 +<br>Интеллект-стек 2023"]:::guide
        R1_IWE["IWE assistance"]:::iwe
        R1_RAZBOR["Weekly разбор<br>(ontological modeling of own project)"]:::razbor
        R1_OUTCOME["<b>Outcome:</b> apply 5 ШСМ primitives к own project +<br>graf создания + альфа state-graphs"]:::outcome
        R1_GUIDE --> R1_RAZBOR
        R1_IWE --> R1_RAZBOR
        R1_RAZBOR --> R1_OUTCOME
    end

    subgraph R2_TRACK["<b>R2 — Системный менеджмент + Системная инженерия</b><br><small>~19 sessions · Wednesdays 18:00-20:00</small>"]
        R2_GUIDE["Online guides:<br>Сис.менеджмент 2023 +<br>Сис.инженерия 2022 +<br>Инженерия личности 2023"]:::guide
        R2_IWE["IWE assistance"]:::iwe
        R2_RAZBOR["Weekly разбор<br>(enterprise architecture of own project)"]:::razbor
        R2_OUTCOME["<b>Outcome:</b> «инженер-менеджер» identity +<br>enterprise systems design capacity"]:::outcome
        R2_GUIDE --> R2_RAZBOR
        R2_IWE --> R2_RAZBOR
        R2_RAZBOR --> R2_OUTCOME
    end

    subgraph ADVANCED["<b>R3+ Advanced / Masters / Reformers</b><br><small>per R-A §5.2 + 10th MIM conf 2026 Section 1<br>«Развитие для развитых» (Левенчуковский talk)</small>"]
        AD_MASTER["МИМ Masters<br><small>e.g. Mizgulin · Agroskin · Lubchenko · Medvedeva · Nedbailov</small>"]:::master
        AD_REF["МИМ Reformers<br><small>contribute к method development itself</small>"]:::master
    end

    SEMINARS["<b>Applied seminars + Annual conference</b><br><small>events.system-school.ru · 10th conf April 2026</small>"]:::seminar
    AISYSTANT["<b>aisystant.system-school.ru</b><br><small>Курсы + IWE persistent across residencies</small>"]:::platform

    ENTRY --> R0_TRACK
    R0_OUTCOME --> R1_TRACK
    R1_OUTCOME --> R2_TRACK
    R2_OUTCOME --> ADVANCED
    AISYSTANT -.->|substrate| R0_TRACK
    AISYSTANT -.->|substrate| R1_TRACK
    AISYSTANT -.->|substrate| R2_TRACK
    ADVANCED --> SEMINARS

    LEVCHALL["<b>Ruslan path per §0.0 ack 2026-05-17</b><br><small>Apply for nearest R0 cohort<br>Activate aisystant subscription<br>Phase B = inside experience captured</small>"]:::ruslan
    ENTRY -.->|invite per Левенчук C7 2026-05-17| LEVCHALL

    classDef entry fill:#fff8e1,stroke:#f57c00,stroke-width:4px
    classDef guide fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef iwe fill:#e8eaf6,stroke:#283593,stroke-width:2px
    classDef razbor fill:#fce4ec,stroke:#ad1457,stroke-width:3px
    classDef outcome fill:#e0f2f1,stroke:#00695c,stroke-width:3px
    classDef master fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    classDef seminar fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef platform fill:#bbdefb,stroke:#0d47a1,stroke-width:2px
    classDef ruslan fill:#ffebee,stroke:#c62828,stroke-width:4px
```

**Provenance.** R-A §2.2 residency tracks + LJ 1777145 Autumn 2025 cohort dates +
R-A §5.1 IWE role + R-A §5.2 advanced tracks + system-school.ru/team mentor list +
LJ 1798285 10th MIM conf Section 1 Левенчуковский talk title.
