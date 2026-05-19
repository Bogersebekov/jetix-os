---
title: Diagram 5 — Cross-link Levenchuk topics × Jetix substrate
phase: 6
parent: research/levenchuk-corpus-inventory-v2-2026-05-19-evening/
---

# Diagram 5 — Cross-link к Jetix substrate ⭐

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph "LEVENCHUK CORPUS — 13 topic clusters"
        L1[Системное мышление]
        L2[Методология]
        L3[Системная инженерия]
        L4[Системный менеджмент]
        L5[Инженерия личности]
        L6[Интеллект-стек 16 trans]
        L7[Рациональная работа / R1]
        L8[FPF 73K lines]
        L9[IWE Workbench]
        L10[Essence Kernel OMG]
        L11[Holon mereology]
        L12[Master-Apprentice 4-role]
        L13[Sense-of-measure / Системный фитнес]
    end

    subgraph "JETIX SUBSTRATE — 8 sources"
        J1[5 concept docs 2026-05-18]
        J2[Platform v2 2026-05-19]
        J3[K-1 InfoSub]
        J4[K-2 AGI Reception]
        J5[K-3 Society-Code]
        J6[K-4 Intellect-12]
        J7[K-5 Safety-Develop]
        J8[K-6 Method 31-comp ⭐⭐]
        J9[3 Tier A wikis]
    end

    L1 ==>|deep| J8
    L1 ==>|deep| J9
    L2 ==>|deep| J8
    L2 ==>|deep| J9
    L2 -->|medium| J3
    L3 -->|medium| J1
    L3 -->|medium| J2
    L3 -->|medium| J7
    L4 -->|medium| J2
    L4 -->|medium| J8
    L5 ==>|deep| J1
    L5 ==>|deep| J6
    L5 -->|medium| J9
    L6 ==>|deep| J6
    L6 -->|medium| J1
    L7 ==>|deep| J6
    L7 -->|medium| J7
    L8 ==>|deep| J1
    L8 ==>|deep| J2
    L8 ==>|deep| J7
    L9 -.->|ABSENT GAP| J9
    L10 -.->|ABSENT GAP| J9
    L11 -->|medium| J8
    L12 ==>|deep| J1
    L12 ==>|deep| J2
    L13 ==>|deep| J9
    L13 ==>|deep| J8

    style L8 fill:#d6f0d6,color:#000
    style L9 fill:#ffd6d6,color:#000
    style L10 fill:#ffd6d6,color:#000
    style L13 fill:#fff4e6,color:#000
    style J8 fill:#fff4e6,color:#000
    style J9 fill:#fff4e6,color:#000

    classDef deep stroke:#000,stroke-width:3px
    classDef absent stroke:#a00,stroke-width:2px,stroke-dasharray: 5 5
```

**Legend:**
- `==>` deep overlap (verbatim or near-verbatim cross-citation present)
- `-->` medium / partial overlap
- `-.->` absent / GAP candidate
- Red nodes = topic absent from substrate (IWE / Essence Kernel)
- Light yellow = K-6 + Sense-of-measure = highest-density cross-link cluster
- Green = FPF = wholesale already integrated

---

## Top-5 cross-link clusters by density

1. **K-6 Method × Системное мышление + Методология + Sense-of-measure** ⭐⭐ — direct lineage; K-6 31-component synthesis structurally mirrors Levenchuk's Системное мышление 2024 (1200pp Ridero)
2. **3 Tier A wikis × Method + Sense-of-measure + Personal Engineering** ⭐ — already-acked wiki concepts deeply latent с Levenchuk parallels
3. **FPF × ALL Jetix substrate** ⭐ — wholesale integration (Platform v2 §5 8-layer + concept docs reference + K-5 R13 packet cites)
4. **5 concept docs × Master-Apprentice + Personal Engineering** — Workshop / EDU-LAYER strong overlap
5. **K-4 × Интеллект-стек 16 transdisciplines** ⭐ — 12-component framework parallels 16-transdiscipline structure

## Top-2 absent gaps (red)

- **IWE** (Intelligence Workbench Engine) — absent ALL 8 sources despite Levenchuk's central concept = exokortex precursor
- **Essence Kernel** (OMG SEMAT 7-alpha) — absent despite Levenchuk's 2015 arXiv direct contribution
