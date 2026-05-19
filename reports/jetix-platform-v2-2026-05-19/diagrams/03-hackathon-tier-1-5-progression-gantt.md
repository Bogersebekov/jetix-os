---
type: mermaid-diagram
date: 2026-05-19
session: jetix-platform-v2-description-2026-05-19
phase: 9
diagram_subject: Phase 3 — Hackathon Tier 1-5 progression Q3 2026 → Q3 2027
---

# Diagram 3 — Hackathon Tier 1-5 Progression Gantt (Q3 2026 → Q3 2027)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
gantt
    title Hackathon Tier-Progression Cadence Q3 2026 → Q3 2027
    dateFormat YYYY-MM-DD
    axisFormat %b %Y

    section Tier 1 Online Micro (bi-weekly)
    T1 Q3 2026 — 6 events       :a1, 2026-07-01, 90d
    T1 Q4 2026 — 6 events       :a2, after a1, 90d
    T1 Q1 2027 — 6 events       :a3, after a2, 90d
    T1 Q2 2027 — 6 events       :a4, after a3, 90d
    T1 Q3 2027 — 6 events       :a5, after a4, 90d

    section Tier 2 Online Standard (monthly)
    T2 Q3 2026 — 3 events       :b1, 2026-08-01, 90d
    T2 Q4 2026 — 3 events       :b2, after b1, 90d
    T2 Q1 2027 — 3 events       :b3, after b2, 90d
    T2 Q2 2027 — 3 events       :b4, after b3, 90d
    T2 Q3 2027 — 3 events       :b5, after b4, 90d

    section Tier 3 Hybrid (quarterly)
    T3 Q4 2026 — 1 event Berlin :c1, 2026-10-15, 14d
    T3 Q2 2027 — 1 event Berlin :c2, 2027-04-15, 14d
    T3 Q3 2027 — 1 event Berlin :c3, 2027-07-15, 14d

    section Tier 4 Workshop Berlin (bi-annual)
    T4 Q1 2027 — 1 event 3-4 wk :d1, 2027-02-01, 30d

    section Tier 5 Offline Major (annual)
    T5 Q3 2027 — 1 project       :e1, 2027-08-01, 180d
```

## Compound annual throughput

| Tier | Events / year | Participants / year |
|------|---------------|----------------------|
| T1 | 25-30 | 250-500 |
| T2 | 12-15 | 250-1200 |
| T3 | 3-4 | 80-300 |
| T4 | 1-2 | 20-100 |
| T5 | 1 | 100-1000+ |

**Cumulative: ~1000+ unique humans engaged annually.**

## Cohort flow (compound effect)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    POOL[Recruiting pool<br/>Phase 1 22 categories]
    POOL --> T1[T1 cohort<br/>250-500/yr]
    T1 -->|>30% progress| T2[T2 cohort<br/>250-1200/yr]
    T2 -->|>20% progress| T3[T3 cohort<br/>80-300/yr]
    T3 -->|>10% progress| T4[T4 cohort<br/>20-100/yr]
    T4 -->|>5% progress| T5[T5 cohort<br/>100-1000/yr]

    T5 -.->|alumni| T4M[T4 mentors-in-residence]
    T4 -.->|alumni| T3M[T3 mentor/judges]
    T3 -.->|alumni| T2M[T2 mentor/judges]
    T2 -.->|alumni| T1M[T1 mentors]
    T1 -.->|alumni| COMM[Community stewards]

    T5 -.->|substrate| FOUND[Foundation governance]
    T5 -.->|methodology| METH[R26 Methodology library]

    classDef cohort fill:#FFD700
    classDef flow fill:#90EE90

    class T1,T2,T3,T4,T5 cohort
    class T4M,T3M,T2M,T1M,COMM,FOUND,METH flow
```

## Per-Tier P&L baseline (Phase 3 §8)

| Tier | Sponsor revenue / event | Cost / event | Annual margin |
|------|--------------------------|---------------|---------------|
| T1 | €1K-5K | €0.5K-2K | €15K-90K |
| T2 | €10K-50K | €5K-20K | €60K-360K |
| T3 | €50K-250K | €30K-150K | €80K-400K |
| T4 | €250K-1M | €150K-700K | €200K-600K |
| T5 | €1M-10M | €500K-5M (mlti-yr) | strategic |

**Q3 2026 → Q3 2027 net positive substrate** if Tier T2-T4 sponsorship hits mid-range (~€1-3M revenue / ~€0.5-2M cost / margin €0.5-1M).

**Cross-link:** Phase 3 §0-§11 detailed; Phase 7 V1 sponsorship variant.

---

*Mermaid Diagram 3 of 7. Phase 3 visualisation. Gantt cadence Q3 2026 → Q3 2027 + cohort flow compound + per-Tier P&L.*
