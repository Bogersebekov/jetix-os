---
title: IWE vs competitors — positioning landscape
date: 2026-05-17
type: mermaid-diagram
source: reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md §1 + README.en.md FAQ
F: F4
G: distillation-3
R: refuted_if_comparative_C5b_falsified_by_benchmark
---

# IWE vs competitors — positioning landscape

> Reposition по 2 осям: (X) breadth of tool surface vs (Y) intelligence-amplification depth.
> «Exoskeleton vs prosthesis» distinction is FPF-derived; «work environment vs note storage» distinction is Tseren-canonical.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'11px'}}}%%
quadrantChart
    title IWE vs competitors — depth × breadth
    x-axis "Surface breadth (single tool) →" --> "Workflow integration"
    y-axis "Note storage" --> "Intelligence amplification"
    quadrant-1 "Workflow + amplification"
    quadrant-2 "Note + amplification"
    quadrant-3 "Note storage only"
    quadrant-4 "Workflow without amplification"
    "Obsidian": [0.2, 0.3]
    "Notion": [0.5, 0.25]
    "Logseq": [0.25, 0.35]
    "Roam Research": [0.3, 0.4]
    "Vanilla Claude Code": [0.55, 0.45]
    "GitHub Copilot": [0.4, 0.35]
    "IWE template (FMT)": [0.75, 0.70]
    "IWE platform AI guide (paid)": [0.85, 0.85]
    "FPF (raw spec)": [0.1, 0.95]
```

**Tseren's explicit anti-positioning** (`README.en.md:219-220`):
> «Obsidian is a note storage. IWE is a **work environment** with protocols, AI agents, and knowledge formalization. You can use Obsidian inside IWE for notes, but IWE provides structure, planning, and competence accumulation.»

**The exoskeleton claim** (`README.en.md:41`):
> «**Key principle: exoskeleton, not prosthesis.** IWE amplifies your thinking, not replaces it. After each session you become more competent, not just get a result.»

**Falsifier (per phil × critic).** «Exoskeleton ≠ prosthesis» — test: «можешь объяснить без «ИИ подсказал»?» Operational test, not yet validated comparatively against vanilla Claude Code.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'12px'}}}%%
flowchart LR
    User["User<br>intellectual worker"]:::user

    subgraph Note["Note storage (low amplification)"]
        Ob["Obsidian / Logseq"]:::note
        Nt["Notion"]:::note
    end

    subgraph Vanilla["Vanilla AI (single-turn)"]
        Cl["Claude Code (vanilla)"]:::ai
        Cp["GitHub Copilot"]:::ai
    end

    subgraph IWE["IWE (template + platform)"]
        T["FMT-exocortex-template<br>(free, public, ver 0.31.0)"]:::iwe
        P["Aisystant AI guide<br>(paid platform)"]:::iwepaid
    end

    subgraph Pure["FPF Spec (raw)"]
        F["FPF-Spec.md<br>72 800 lines"]:::fpf
    end

    User -- "notes" --> Note
    User -- "single-shot" --> Vanilla
    User -- "full work culture" --> IWE
    User -- "research-grade" --> Pure

    T -- "imports A.7 Role-Method-Work" --> F
    P -- "C5a: structurally on FPF" --> F
    P -. "C5b: «умнее конкурентов» — unverified" .-> Vanilla

    classDef user fill:#fff8e1,stroke:#f57c00,stroke-width:2px
    classDef note fill:#eee,stroke:#999,stroke-width:1px
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef iwe fill:#fce4ec,stroke:#ad1457,stroke-width:2px
    classDef iwepaid fill:#f3e5f5,stroke:#6a1b9a,stroke-width:3px
    classDef fpf fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```

**Critical reading.** Both diagrams reflect **C5a verified / C5b not-verifiable** decomposition from `02-iwe-deep-v2.md §2.1`. The «умнее конкурентов» claim positions IWE-platform against vanilla AI but no published benchmark; falsifier = C4 Arm comparison (Phase B blocked on Ruslan IWE subscription).
