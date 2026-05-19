---
type: mermaid-diagram
date: 2026-05-19
session: jetix-platform-v2-description-2026-05-19
phase: 9
diagram_subject: Phase 7 — 15 monetization variants × 3 horizons + R12 flow
---

# Diagram 7 — Monetization Variants × Horizon × Revenue Flow

## 15 variants × 3 horizons (breadth NOT selection)

```mermaid
graph TD
    JETIX[Jetix Substrate<br/>15 monetization variants surfaced]

    JETIX --> SHORT[Short-term Q3-Q4 2026<br/>V1-V5]
    JETIX --> MID[Mid-term 2026-2027<br/>V6-V10]
    JETIX --> LONG[Long-term 2027+<br/>V11-V15]

    SHORT --> V1[V1 Hackathon sponsorship]
    SHORT --> V2[V2 Workshop training fees]
    SHORT --> V3[V3 Consulting]
    SHORT --> V4[V4 Quick-money P1 AI]
    SHORT --> V5[V5 AI Grant non-dilutive]

    MID --> V6[V6 SaaS Platform fees]
    MID --> V7[V7 Tokenized governance]
    MID --> V8[V8 SBT issuance]
    MID --> V9[V9 M&A advisory]
    MID --> V10[V10 Curriculum licensing]

    LONG --> V11[V11 Network State residency]
    LONG --> V12[V12 QF revenue pool]
    LONG --> V13[V13 Royalty derived products]
    LONG --> V14[V14 Foundation endowment]
    LONG --> V15[V15 Self-sustaining compound]

    classDef now fill:#90EE90,stroke:#006400
    classDef mid fill:#FFD700,stroke:#B8860B
    classDef future fill:#87CEEB,stroke:#1E3A5F

    class V1,V2,V3,V4,V5 now
    class V6,V7,V8,V9,V10 mid
    class V11,V12,V13,V14,V15 future
```

## Revenue flow + R12 enforcement

```mermaid
graph LR
    SPONSORS[Sponsors Cat 8/16/17/19]
    PARTICIPANTS[Participants Cat 1-22]
    REVENUE[Revenue streams V1-V15]

    SPONSORS -.->|sponsorship| V1F[V1 Hackathon fees]
    SPONSORS -.->|grants| V5F[V5 AI Grants]
    PARTICIPANTS -.->|fees| V2F[V2 Workshop fees]
    PARTICIPANTS -.->|fees| V6F[V6 SaaS fees]

    V1F --> POOL[Aggregate revenue pool]
    V2F --> POOL
    V5F --> POOL
    V6F --> POOL

    POOL --> R12CHK[R12 audit gate]
    R12CHK -->|Pass: Mondragón ratio cap| DISTR[QF distribution]
    R12CHK -->|Pass: fork-and-leave| DISTR
    R12CHK -->|Pass: no extraction| DISTR
    R12CHK -->|Fail| HALT[Halt-Log-Alert]

    DISTR --> OPS[Operations 60-70%]
    DISTR --> ENDOW[Foundation endowment 15-25%]
    DISTR --> COHORT[Cohort distribution 10-20%<br/>QF-weighted]

    OPS --> SUBSTRATE[Substrate maintenance]
    ENDOW --> LONG_HORIZON[Long-horizon sustainability]
    COHORT --> CONTRIB[Per-contribution compensation]

    classDef revenue fill:#FFD700,stroke:#B8860B
    classDef audit fill:#FFB6C1,stroke:#8B0000
    classDef positive fill:#90EE90,stroke:#006400

    class V1F,V2F,V5F,V6F,POOL revenue
    class R12CHK,HALT audit
    class OPS,ENDOW,COHORT,SUBSTRATE,LONG_HORIZON,CONTRIB positive
```

## Annual revenue trajectory Y1-Y5+ (illustrative)

```mermaid
gantt
    title Annual revenue trajectory Y1-Y5+ (€ illustrative)
    dateFormat YYYY-MM-DD
    axisFormat %Y

    section Y1 2026-2027
    V1-V5 short-term €500K-2M  :a1, 2026-07-01, 365d

    section Y2 2027-2028
    V1-V5 €1M-3M + V6-V10 €100K-500K :a2, 2027-07-01, 365d

    section Y3 2028-2029
    V1-V5 €1.5M-5M + V6-V10 €500K-2M + V11-V15 €100K-500K :a3, 2028-07-01, 365d

    section Y4 2029-2030
    V1-V5 €2M-7M + V6-V10 €1M-5M + V11-V15 €500K-2M :a4, 2029-07-01, 365d

    section Y5+ 2030+
    Self-sustaining V15 compound €5M-40M+ :a5, 2030-07-01, 1095d
```

## 2-tier value framing (per Ruslan text_010)

```mermaid
graph LR
    PARTNERS[Partners + Participants]

    PARTNERS -.->|Tier 1 NOW| THEIR[For their project]
    PARTNERS -.->|Tier 2 LATER| HUMAN[For humanity]

    THEIR --> N1[Network connection FREE]
    THEIR --> N2[Substrate access FREE baseline]
    THEIR --> N3[Mentor matching FREE]
    THEIR --> N4[Sponsor intros FREE]
    THEIR --> N5[Co-funding revenue-share]

    HUMAN --> H1[Methodology contribution]
    HUMAN --> H2[Public-good substrate]
    HUMAN --> H3[Open-source artifacts]
    HUMAN --> H4[Trust infrastructure H8]
    HUMAN --> H5[Trained cohort 1000+/yr]
```

**Cross-link:** Phase 7 §1-§10 detailed; Phase 4 L8 R12 enforcement substrate; Phase 5 IP-1 (Ruslan selects mix); breadth NOT selection.

---

*Mermaid Diagram 7 of 7. Phase 7 visualisation. 15 variants × 3 horizons + revenue flow + R12 audit + Y1-Y5+ trajectory + 2-tier value.*
