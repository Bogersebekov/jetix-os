---
title: Diagram 09 — FPF mechanisms ↔ Jetix presence (Phase B audit prep)
date: 2026-05-17
type: mermaid
parent: 06-honest-self-audit.md (companion in same dir)
F: F4
G: distillation-diagrams
R: refuted_if_jetix_presence_overstated
note: |
  This diagram prepares for Phase B detailed FPF presence audit
  across all Jetix LOCKED documents. Phase A shows broad-strokes mapping.
---

# Diagram 09 — FPF mechanisms ↔ Jetix presence

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'12px'}}}%%
flowchart LR
    subgraph FPF_MECH["<b>FPF mechanism</b>"]
        M1["U.Holon (A.1)"]:::fpf
        M2["U.BoundedContext (A.1.1)"]:::fpf
        M3["U.Role/RoleAssignment (A.2)"]:::fpf
        M4["U.Method/MethodDescription (A.3)"]:::fpf
        M5["U.RoleStateGraph (A.2.5) +<br>U.Work (A.15.1)<br>past-participle alpha-states"]:::fpf
        M6["U.Episteme + EpistemeSlotGraph (C.2.1)"]:::fpf
        M7["F-G-R (B.3) Trust+Assurance"]:::fpf
        M8["A.6.B Claim Register"]:::fpf
        M9["A.14 Advanced Mereology"]:::fpf
        M10["B.5.2 Abductive Loop"]:::fpf
        M11["C.17-C.19 NQD / E-E-LOG"]:::fpf
        M12["E.9 DRR"]:::fpf
        M13["E.17 MVPK multi-view"]:::fpf
        M14["F.9 Bridges"]:::fpf
        M15["F.17 UTS"]:::fpf
        M16["E.5.2 Notational Independence"]:::fpf
        M17["E.2 Pillars (P-2 Didactic etc.)"]:::fpf
    end

    subgraph JETIX["<b>Jetix presence (Phase A surface-level)</b>"]
        J1["<b>Foundation 11 Parts</b><br><small>swarm/wiki/foundations/<br>Parts 1-11 + Strategic Layer</small>"]:::jetix
        J2["<b>F-G-R schema</b><br><small>shared/schemas/f-g-r.json<br>DOGFOOD per CLAUDE.md §4.1</small>"]:::jetix
        J3["<b>Pillar C Tier-2 12 rules</b><br><small>principles/tier-2-system/foundation-generic/</small>"]:::jetix
        J4["<b>IP-1 Role≠Executor</b><br><small>shared/schemas/executor-binding.yaml.template<br>Bundle 1 RUSLAN-ACK</small>"]:::jetix
        J5["<b>Default-Deny table</b><br><small>.claude/config/default-deny-table.yaml<br>11 entries via constitutional_never_list</small>"]:::jetix
        J6["<b>Wiki v2</b><br><small>concepts/ entities/ sources/<br>topics/ ideas/ claims/ summaries/<br>foundations/ + niches/</small>"]:::jetix
        J7["<b>Decisions D-Lock entries</b><br><small>decisions/strategic/<br>~29 entries</small>"]:::jetix
        J8["<b>Strategic Insights H1-H7</b><br><small>reports/strategic-decisions-2026-05-12.md<br>Hexagon → Heptagon</small>"]:::jetix
        J9["<b>archive/design/JETIX-FPF.md</b><br><small>3762-line derivative (archived 2026-05-06)</small>"]:::jetix
        J10["<b>swarm/lib/routing-table.yaml</b><br><small>shared protocols</small>"]:::jetix
        J11["<b>Mailbox schema</b><br><small>shared/schemas/message.schema.json v2.0.0</small>"]:::jetix
        J12["<b>Approvals log</b><br><small>swarm/approvals/log.jsonl</small>"]:::jetix
        J13["<b>swarm/wiki/cycles/</b><br><small>per-cycle synthesis</small>"]:::jetix
        J14["<b>CRM 14-section schema</b><br><small>crm/people/ crm/orgs/</small>"]:::jetix
    end

    M1 -->|adopted broadly| J1
    M2 -->|partially via Bounded contexts in F-G-R G:| J2
    M3 -->|directly| J4
    M4 -->|partial via routing-table| J10
    M5 -->|partial via state-flags in alphas| J6
    M6 -.->|conceptual only — not enforced| J6
    M7 -->|direct adoption| J2
    M8 -.->|not adopted| FUTURE["future audit Phase B"]:::future
    M9 -->|via holonic Foundation| J1
    M10 -.->|conceptual в Strategic Insights| J8
    M11 -.->|via NQD-style Strategic Insights surfacing| J8
    M12 -->|D-Lock entries are DRR-shaped| J7
    M13 -.->|partial via multi-Layer F2/F4/F6/F8| J3
    M14 -.->|not formal — informal cross-niche| J6
    M15 -.->|not formal UTS — informal glossary in CLAUDE.md| J9
    M16 -->|aligned (multiple notations)| J11
    M17 -->|enforced в reviews / audits| J3

    subgraph SUMMARY["<b>Phase A summary count</b>"]
        S1["<b>Direct adoptions</b> (4):<br>F-G-R · IP-1 Role≠Executor ·<br>Notational Independence · Pillars discipline"]:::sum_yes
        S2["<b>Partial / conceptual</b> (8):<br>Holon · BoundedContext · Method ·<br>RoleStateGraph · Episteme · MHT · Abductive · MVPK"]:::sum_part
        S3["<b>Not adopted</b> (4):<br>A.6.B Claim Register · Bridges (formal) ·<br>UTS (formal) · DRR-as-canonical-shape"]:::sum_no
    end

    JETIX -.->|tally| SUMMARY

    classDef fpf fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    classDef jetix fill:#fce4ec,stroke:#ad1457,stroke-width:2px
    classDef future fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef sum_yes fill:#e0f2f1,stroke:#00695c,stroke-width:3px
    classDef sum_part fill:#fff8e1,stroke:#f57c00,stroke-width:3px
    classDef sum_no fill:#ffebee,stroke:#c62828,stroke-width:3px
```

**Phase A surface only — Phase B detailed audit pending per prompt §11.**

**Provenance.** Mapping table derived from CLAUDE.md §4 + Foundation v1.0 LOCKED
section + shared/schemas/ inspection + decisions/strategic/ inventory +
archive/design/JETIX-FPF.md (existing derivative). Inline `[src]` для each row
in companion `06-honest-self-audit.md`.
