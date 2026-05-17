---
title: IWE → FPF mechanism map (what IWE imports from FPF)
date: 2026-05-17
type: mermaid-diagram
source: reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md §2.5
F: F4
G: distillation-3
---

# IWE — FPF mechanism map

> What FPF mechanisms IWE structurally adopts. Solid line = explicit declared mapping;
> dashed line = used-but-not-named; gap = not visible in template.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'12px'}}}%%
flowchart LR
    subgraph FPF["FPF Spec (canonical, c86eabd)"]
        direction TB
        A11["A.1.1<br>U.BoundedContext"]:::fpf
        A2["A.2 Role Taxonomy<br>+ A.13 Agential Role"]:::fpf
        A3["A.3 Method-Description<br>+ A.15 Role-Method-Work"]:::fpf
        A6B["A.6.B Claim Register"]:::fpf
        A6P["A.6.P Compression<br>Decompression"]:::fpfactive
        A14["A.14 Advanced Mereology"]:::fpf
        B3["B.3 F-G-R Trust"]:::fpf
        B5["B.5 Reasoning Cycle<br>Explore→Shape→Evidence→Operate"]:::fpf
        C21["C.2.1 U.EpistemeSlotGraph"]:::fpf
        C17["C.17-C.19 NQD / E-E-LOG"]:::fpf
        E9["E.9 DRR Design Rationale"]:::fpf
        E17["E.17 MVPK Multi-View"]:::fpf
    end

    subgraph IWE["IWE template (ver 0.31.0 @ 2026-05-17)"]
        direction TB
        Pack["Pack<br>(domain knowledge passport)"]:::iwe
        Roles["5 Roles: R1/R2/R8/R23/R24"]:::iwe
        WP["WP lifecycle<br>(Open→Work→Close)"]:::iwe
        Arch["ArchGate 7-factor<br>ЭМОГССБ checklist"]:::iwe
        Memory["Memory lifecycle (S-35)<br>HOT/WARM/COLD/ARCHIVE"]:::iwe
        BasePD["Base/Pack/DS<br>3-tier hierarchy"]:::iwe
        Fall["Fallback Chain<br>DS→Pack→SPF→FPF→ZP"]:::iwe
        OWC["OWC ritual<br>4 scales"]:::iwe
        WPGate["WP Gate<br>(register before work)"]:::iwe
        ServiceClause["Service Clauses<br>(DP.SC.NNN)"]:::iwe
        FpfRef["memory/fpf-reference.md<br>(navigation)"]:::iwe
    end

    A11 -->|bounded context| Pack
    A2 -->|5 roles mapping| Roles
    A3 -->|method-work quartet| WP
    A6B -.->|not directly used| Memory
    A6P -.->|implicit horizons| Memory
    A14 -->|3-tier mereology| BasePD
    B3 -.->|informal F-G-R| WP
    B5 -->|fractal at 4 scales| OWC
    C21 -.->|implicit slots| Pack
    C17 -.->|not visible| FpfRef
    E9 -->|WP-context + Strategy| Arch
    E17 -->|partial: per-role views| ServiceClause

    FPF -.->|"Fallback chain (CLAUDE.md §1)"| Fall
    Fall --> FpfRef

    classDef fpf fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#01579b
    classDef fpfactive fill:#ffe0b2,stroke:#f57c00,stroke-width:3px,color:#bf360c
    classDef iwe fill:#fce4ec,stroke:#ad1457,stroke-width:2px,color:#880e4f
```

**Legend.** Solid arrows = explicit mapping (verified in CLAUDE.md / docs/). Dashed arrows = used-but-not-named (functional similarity без declared discipline). Orange box (A.6.P) = active dev cluster May 2026, not yet stable in FPF Spec.

**Coverage.** 12 FPF mechanisms surveyed: 5 explicit, 5 implicit/partial, 2 not-visible-in-template.
