---
title: Diagram 04 — IWE = production-applied FPF
date: 2026-05-17
type: mermaid
parent: 02-u-episteme-and-iwe.md §2-3
F: F4
G: distillation-diagrams
R: refuted_if_iwe_role_misencoded
---

# Diagram 04 — IWE = Production-applied FPF

> Per Левенчуковский TG 2026-05-17 C5: «У Церена IWE … внутри там интеллект опирается
> на тот же FPF — и понятно, за счёт чего его IWE умнее конкурентов.»
>
> Empirical IWE behavior pending Ruslan subscription per blockers.md B2; this diagram
> = CONCEPTUAL layer based on R-A + LJ + Tseren corpus.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'13px'}}}%%
flowchart TB
    subgraph FPF_LAYER["<b>FPF spec (substrate)</b><br><small>raw/external/ailev-FPF/FPF-Spec.md · 62K lines</small>"]
        FPF_K["U.Holon · U.BoundedContext · U.Role<br>U.Method · U.RoleStateGraph · U.Episteme<br>F-G-R trust · Abductive Loop · DRR · UTS · MVPK"]:::fpf
    end

    subgraph IWE_LAYER["<b>IWE — Intelligent Workflow Engine</b><br><small>aisystant.system-school.ru · paid platform<br>per Левенчук TG 2026-05-17 C5</small>"]
        direction TB
        IWE_AGENT["AI agent core<br><small>(LLM with FPF in context)</small>"]:::iwe
        IWE_TRACK["Learner progress tracker<br><small>past-participle alpha-states per learner</small>"]:::iwe
        IWE_GUIDE["Personal guide<br><small>route recommendations<br>per current method+role</small>"]:::iwe
        IWE_QA["Q&A interface<br><small>cite FPF patterns<br>surface alternatives (abductive)</small>"]:::iwe
    end

    subgraph CORPUS_LAYER["<b>Knowledge corpus</b>"]
        BOOK_ST["Сис. мышление 2024<br><small>(2 vol)</small>"]:::book
        BOOK_M["Методология 2025"]:::book
        BOOK_SE["Сис. инженерия 2022"]:::book
        BOOK_SM["Сис. менеджмент 2023"]:::book
        BOOK_IL["Инженерия личности 2023"]:::book
        BOOK_IS["Интеллект-стек 2023"]:::book
        BOOK_R["Рациональная работа"]:::book
    end

    subgraph LEARNER["<b>МИМ learner / resident</b>"]
        L_PROJECT["learner's actual work project<br><small>e.g. agricultural consulting<br>(per Sergeev case study)</small>"]:::learner
        L_DISCS["target transdisciplines<br><small>per residency tier R0/R1/R2</small>"]:::learner
    end

    subgraph MENTOR["<b>Mentor (human)</b><br><small>weekly разборы 2hr</small>"]
        M_REVIEW["mentor-led structured review<br><small>NOT lectures</small>"]:::mentor
    end

    FPF_K -->|loaded as context| IWE_AGENT
    CORPUS_LAYER -->|indexed reference| IWE_AGENT
    IWE_AGENT --> IWE_TRACK
    IWE_AGENT --> IWE_GUIDE
    IWE_AGENT --> IWE_QA
    L_PROJECT -->|task descriptions| IWE_QA
    L_DISCS -->|learning targets| IWE_GUIDE
    IWE_TRACK -->|alpha states progress| L_PROJECT
    IWE_GUIDE -->|route recommendations| L_PROJECT
    M_REVIEW -->|qualitative review| L_PROJECT
    L_PROJECT -->|brought to разбор| M_REVIEW

    DELTA["<b>Why IWE > vanilla AI</b><br><small>(per Левенчуковский C5)</small><br><br>FPF bounded contexts → no semantic drift<br>Role-method signatures → executor-agnostic<br>Past-participle alpha tracking → machine-progress<br>F-G-R per claim → audit-able trust<br>Abductive loop → portfolio of routes<br>MVPK → learner-facing + mentor-facing views<br>DRR → reasoning durability</small>"]:::delta
    IWE_LAYER -.->|empirically demonstrates| DELTA

    classDef fpf fill:#e3f2fd,stroke:#1565c0,stroke-width:4px
    classDef iwe fill:#e8eaf6,stroke:#283593,stroke-width:3px
    classDef book fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef learner fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef mentor fill:#fce4ec,stroke:#ad1457,stroke-width:3px
    classDef delta fill:#fff8e1,stroke:#f57c00,stroke-width:3px
```

**Provenance.** Левенчуковский C5 verbatim (inbox/levenchuk-tg-2026-05-17.md:28) +
R-A §5.1 IWE description + 10th MIM conf 2026 talk list (LJ 1798285: Tserenov +
Sergeev IWE talks) + R-A §5.3 quality-control framing + Tseren TG corpus
analysis 2026-04-28 (Цэрэн personally building IWE).
