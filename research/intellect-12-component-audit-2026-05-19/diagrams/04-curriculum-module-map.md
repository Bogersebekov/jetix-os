---
type: mermaid-diagram
session: k-4-intellect-12-component-audit-2026-05-19
diagram_n: 4
---

# Diagram 04 — Curriculum Module Map (12 Components → 12 Modules)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fafafa','primaryTextColor':'#000000','lineColor':'#333','primaryBorderColor':'#333'}}}%%
graph TB
    subgraph "M1-M4 Foundations (weeks 1-4)"
        M1[M1 Direction<br/>C1 — vision exercise<br/>North Star]
        M2[M2 Safety→Dev<br/>C2 — backup discipline<br/>Default-Deny]
        M3[M3 Relevance<br/>C3 — JIT learning<br/>info diet]
        M4[M4 Attention<br/>C4 — deep work<br/>+ MC-1 Gwm fold]
    end

    subgraph "M5-M9 Core practice (weeks 4-9)"
        M5[M5 Tool-use<br/>C5 — Git/Docker/Python<br/>Karpathy dev env]
        M6[M6 Tool-create<br/>C6 — build-from-scratch<br/>nanoGPT model + MC-5 creativity]
        M7[M7 Questions<br/>C7 — Socratic<br/>quality rubric]
        M8[M8 Observation<br/>C8 — field notes<br/>VSM operative]
        M9[M9 Reasoning<br/>C9 — first principles<br/>chain-of-thought]
    end

    subgraph "M10-M12 Meta + Executive (weeks 9-12+)"
        M10[M10 Proportion<br/>C10 — MVP/sufficiency<br/>+ MC-10 calibration]
        M11[M11 Goals<br/>C11 — OKR cascade<br/>SMART critique]
        M12[M12 Decompose<br/>C12 — WBS/GTD<br/>tree-search]
    end

    M1 --> M3
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M4 --> M7
    M4 --> M8
    M5 --> M6
    M7 --> M9
    M8 --> M9
    M1 --> M11
    M2 --> M11
    M11 --> M12
    M9 --> M10
    M1 --> M10

    style M9 fill:#d6f0d6
    style M6 fill:#d6f0d6
    style M2 fill:#fff4e6
    style M10 fill:#fff4e6
```

## Cohort time-to-Stage-3 (per module)

| Module | Weeks | Karpathy parallel |
|---|---|---|
| M1 Direction | 1-2 | «Why X» framing |
| M2 Safety→Dev | 1-2 | baseline running + commit |
| M3 Relevance | 2-3 | JIT learning |
| M4 Attention | 3-4 | deep work blocks |
| M5 Tool-use | 4-6 | second brain |
| M6 Tool-create | 6-9 | nanoGPT model |
| M7 Questions | 4-6 | simplest model |
| M8 Observation | 4-6 | look at data |
| M9 Reasoning | 6-9 | first principles |
| M10 Proportion | 8-12 | nanoGPT NOT GPT-4 |
| M11 Goals | 9-12 | per-module objectives |
| M12 Decompose | 9-12 | per-module structure |

---

*Diagram 04 — 12-module curriculum map.*
