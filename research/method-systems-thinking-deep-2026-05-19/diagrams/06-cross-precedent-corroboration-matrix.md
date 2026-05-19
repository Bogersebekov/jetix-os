---
title: Diagram 06 — Cross-precedent corroboration matrix
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../06-31-method-components-synthesis.md
source: Phase 5 §3
---

# Cross-precedent corroboration matrix (10 thinkers × selected K-6 components)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    subgraph THINKERS[10 primary thinkers]
        MEAD[Meadows]
        ASHB[Ashby]
        WIEN[Wiener]
        BEER[Beer VSM]
        SENG[Senge]
        STER[Sterman]
        BERT[Bertalanffy]
        BOYD[Boyd]
        BATE[Bateson]
        HOFS[Hofstadter]
    end

    subgraph COMPS[Selected K-6 components]
        C1[ALL=systems]
        C2[ALL=information]
        C6[Rules]
        C9["⭐ Sense of Measure"]
        C10[Intellect cycle]
        C11[Self-knowledge]
        C16[Gradient view]
        C18[Recursive lifecycle]
        C25[Reconnaissance]
        C28["⭐⭐ Exokortex"]
    end

    MEAD --- C1 & C6 & C16 & C18
    ASHB --- C9 & C11 & C18 & C25
    WIEN --- C2 & C10 & C25
    BEER --- C6 & C9 & C25 & C10
    SENG --- C9 & C10 & C11 & C16 & C18
    STER --- C2 & C16 & C18 & C25
    BERT --- C1 & C18 & C28
    BOYD --- C9 & C10 & C25 & C18
    BATE --- C1 & C2 & C11 & C28
    HOFS --- C11 & C18 & C28

    classDef thinker fill:#dbeafe,stroke:#3b82f6
    classDef comp fill:#fef3c7,stroke:#f59e0b
    class MEAD,ASHB,WIEN,BEER,SENG,STER,BERT,BOYD,BATE,HOFS thinker
    class C1,C2,C6,C9,C10,C11,C16,C18,C25,C28 comp
```

**Reading:** 168 corroboration touches across 31 components × 10 thinkers (5.4 thinkers/component avg). Cross-cultural / cross-discipline convergence. Breadth-NOT-selection preserved.
