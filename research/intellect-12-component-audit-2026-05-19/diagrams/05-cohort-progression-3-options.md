---
type: mermaid-diagram
session: k-4-intellect-12-component-audit-2026-05-19
diagram_n: 5
---

# Diagram 05 — Cohort Progression: 3 Sequencing Options (NO recommendation)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fafafa','primaryTextColor':'#000000','lineColor':'#333','primaryBorderColor':'#333'}}}%%
graph LR
    subgraph "Option A — Foundations-first (linear)"
        A1[M1→M2→M3→M4 weeks 1-4]
        A2[M5→M9 weeks 4-6]
        A3[M7→M8 weeks 6-8]
        A4[M6 weeks 8-10]
        A5[M10→M11→M12 weeks 10-12+]
        A1 --> A2 --> A3 --> A4 --> A5
    end

    subgraph "Option B — Project-based (demand-driven)"
        B1[Project 1 selected]
        B2[Activate needed modules]
        B3[Next project]
        B4[Activate more modules]
        B5[Stage-3 = portfolio]
        B1 --> B2 --> B3 --> B4 --> B5
    end

    subgraph "Option C — Hackathon-driven (12 hackathons over 6 mo)"
        C1[Hackathon 1 = M1]
        C2[Hackathon 2 = M2]
        Cdots[... 10 more hackathons]
        C3[Master-apprentice between events]
        C4[Portfolio = 12 hackathon projects]
        C1 --> C2 --> Cdots --> C4
        C3 -.-> Cdots
    end

    subgraph "Tradeoff matrix"
        T[Engagement: C > B > A<br/>Depth: A > B = C<br/>Engineer-attractive: B = C > A<br/>Cohort-scale: C > A > B<br/>R12-aligned: A = B = C ✅]
    end

    A5 -.-> T
    B5 -.-> T
    C4 -.-> T

    style A1 fill:#e6f0ff
    style B1 fill:#fff4e6
    style C1 fill:#d6f0d6
    style T fill:#fff8d5
```

## Hybrid options (Phase 7 H-IC-19 candidates)

- **Hybrid A+B:** M1-M4 foundations + project-based thereafter
- **Hybrid A+C:** M1-M4 foundations + hackathon-driven thereafter
- **Hybrid B+C:** project-based with hackathon punctuation

**Decision discipline:** Ruslan acks selection OR pilot 3-arm RCT (H-IC-16 + H-IC-19 + H-IC-24)

---

*Diagram 05 — 3 sequencing options surfaced parallel per R1.*
