---
type: mermaid-diagram
date: 2026-05-19
session: jetix-platform-v2-description-2026-05-19
phase: 9
diagram_subject: Phase 5 — Jetix organisational role + IP-1 28-entry boundary
---

# Diagram 5 — Jetix Organisational Role (Substrate + IP-1 STRICT)

## 7-role substrate spec

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    JETIX[Jetix Substrate]

    JETIX --> R1_ROLE[1. Substrate Provider<br/>infra/tools/protocols]
    JETIX --> R2_ROLE[2. Values Anchor<br/>humanity-dev + R12]
    JETIX --> R3_ROLE[3. Facilitator<br/>matching/convening/hosting]
    JETIX --> R4_ROLE[4. Quality Steward<br/>FPF + F-G-R discipline]
    JETIX --> R5_ROLE[5. Coordination Layer<br/>comm/scheduling/flow]

    JETIX -.-> R6_NOT[6. NOT Decider<br/>IP-1 STRICT]
    JETIX -.-> R7_NOT[7. NOT Extractor<br/>R12 Constitutional]

    classDef positive fill:#90EE90,stroke:#006400
    classDef negative fill:#FFB6C1,stroke:#8B0000

    class R1_ROLE,R2_ROLE,R3_ROLE,R4_ROLE,R5_ROLE positive
    class R6_NOT,R7_NOT negative
```

## IP-1 28-Entry Boundary — decision-tree

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    ACT[Proposed action]
    ACT --> CLAS{Action class?}

    CLAS -->|Per published rules| PRE[Pre-authorized 10 entries<br/>Substrate executes]
    CLAS -->|Novel action| DD[Default-Deny<br/>14 entries → escalate]
    CLAS -->|Boundary unclear| EDGE[Edge cases<br/>4 entries → escalate-log]

    DD --> ESC1[Ruslan + cohort gov ack required]
    EDGE --> ESC2[Foundation governance review]

    ESC1 --> HUMAN[Human decision<br/>Recursive Engine pattern]
    ESC2 --> HUMAN

    HUMAN -->|Approved| EXEC[Execute]
    HUMAN -->|Denied| LOG[Audit-trail log]

    PRE --> EXEC
    EXEC --> AUDIT[L6 audit-trail emission]

    classDef preauthd fill:#90EE90,stroke:#006400
    classDef denyd fill:#FFD700,stroke:#B8860B
    classDef edgec fill:#FFB6C1,stroke:#8B0000

    class PRE preauthd
    class DD denyd
    class EDGE edgec
```

## Pre-authorized examples (10 entries — substrate decisions OK)

1. Provision compute / hosting per published quota
2. Register new participant per L1 protocol
3. Publish offer / ask per L2 protocol
4. Execute matching algorithm per L3 protocol
5. Emit audit-trail entry per L6 protocol
6. Trigger Halt-Log-Alert per Pillar C Tier 2 R11
7. Send communication per published templates
8. Schedule Tier-1/2 hackathon per cohort governance pre-approval
9. Issue commitment-completion-receipt per L4
10. Update reputation per L6 audit per published rules

## Default-Deny examples (14 entries — Ruslan + cohort gov ack)

11. Add new participant category to taxonomy
12. Add new resource type to taxonomy
13. Modify Tier-progression criteria
14. Accept new corporate sponsor (Cat 16)
15. Accept government partnership (Cat 17)
16. Select Tier-1 hackathon theme
17. Select Tier-4/5 cohort participants
18. Allocate prize-pool per hackathon
19. Modify matching algorithm logic
20. Add new R12 enforcement mechanism
21. Adjust Mondragón ratio cap
22. Spend Foundation endowment
23. Engage M&A target (System Merger Protocol)
24. Issue SBT (Phase 7 variant)

## Edge cases (4 entries — escalate-and-log)

25. Resource-allocation conflict between cohorts
26. Mode negotiation (full-FPF / partial / opaque)
27. Saturation control (outreach quality cap)
28. Goal-divergence handling (partner values diverge)

## Decision rights compact matrix

| Decision class | Substrate | Cohort gov | Foundation gov | Ruslan |
|----------------|-----------|------------|-----------------|--------|
| Infrastructure | ✓ | — | — | (override) |
| Matching | ✓ | (acceptance) | (algo changes) | (override) |
| Audit trail | ✓ | (interpretation) | — | — |
| R12 enforcement | ✓ | (audit) | (parameter tuning) | (severe) |
| Strategic direction | — | (input) | (input) | ✓ |
| Values articulation | — | (input) | (input) | ✓ |
| Monetization mix | — | (input) | (input) | ✓ |
| Partner selection | (R12 check) | (input) | (Tier 4-5) | ✓ |

**Cross-link:** Phase 5 §0-§14 detailed; Phase 4 protocol layer IP-1 mapping; Phase 6 values + framing handled by Ruslan strategic prose.

---

*Mermaid Diagram 5 of 7. Phase 5 visualisation. 7-role substrate + IP-1 decision tree + 28-entry boundary + decision-rights matrix.*
