---
task_id: phase-0-fpf-scope-2026-05-17-task-5-diagram-05
produced_by: engineering-expert × scalability
mode: scalability
status: draft
date: 2026-05-17
diagram_title: Top-level L1-friendly Architecture (Foundation → ROY → Hexagon → outreach; honest gaps)
source: reports/phase-0-fpf-scope/01-jetix-objects-inventory.md §QR-CARD; 02-objects §0; 03-comparison-matrix §6-§7
---

# Diagram 05 — Master TL;DR Architecture (L1-friendly)

Честное представление Jetix для L1 аудитории: что работает, что STUB, что vapor.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TD
    subgraph ExternalLoop["External Loop [GAP: not yet closed; revenue = 0]"]
        direction LR
        CLIENT["First client\nO-04 working product\n[adjacent-possible]"]
        L1PARTNER["L1 partners\nLevenchuk + Tseren\n[6 outreach files; sent=?]"]
    end

    subgraph S5["S5 Identity / Policy\n[RICHEST in Jetix]"]
        direction LR
        FUNDAMENTAL["O-03 Vision / FUNDAMENTAL\nU.WorkPlan + U.MethodDescription\nF8 artefact / F2 system\nB.5.1 Explore state"]
        PILLARC["O-08 Pillar C\n12 Tier-2 rules\nU.Commitment (A.2.8)\nF8 text / F4 enforcement\n[Rule 11 only machine-enforced]"]
        R12["O-11 R12 Anti-extraction\n[J-U2 UNIQUE]\nF5 text / F2 enforcement\nAWAITING-APPROVAL"]
    end

    subgraph S4["S4 Intelligence / Futures\n[partial]"]
        direction LR
        HEXAGON["O-09 Hexagon\n6 LOCKED insights H1-H7\nB.5.2 partial (output; process informal)\nF-G-R + 1A+1B views\n[D-3: closest FPF intel-amp]"]
        PART11["Part 11 Strategic Direction\nB.5.2 partial + E.17 partial"]
    end

    subgraph S3["S3 Audit / Control\n[SECOND-RICHEST in Jetix]"]
        direction LR
        FOUNDATION["O-07 Foundation v1.0\n11 Parts + Pillar A/C\nF8-artefact [EP-5 disclosure]\n[D-2: U.System vs U.Episteme]\nRuntime enforcement = STUB Phase-B"]
        FGR["Part 6a F-G-R\nB.3 per-artefact\n[per-claim = inconsistent]"]
        HITL["Part 6b Human Gate\nE.5 Guard-Rails analog\nDefault-Deny (Rule 11)\nHalt-Log-Alert = STUB"]
    end

    subgraph S2["S2 Coordination\n[operational but under-specified]"]
        direction LR
        ROY["ROY Swarm\nbrigadier + 5 experts × 4 modes\nU.RoleAssignment (A.2.1)\nO-06b functioning"]
        SHAREDPROTO["shared-protocols.md\nPart 4 Role Taxonomy\n[RSG A.2.5 = STUB]"]
    end

    subgraph S1["S1 Operations\n[WEAKEST in Jetix; zero external closure]"]
        direction LR
        VOICE["Voice pipeline\ntranscribe→extract→filter→review\n11 reviews active\n[auto-KB = GAP distribute.py.bak]"]
        WIKI["Wiki v2\n551 records\ngit-native"]
        CRM["CRM\n84/90 draft suffix\n0 closed_won"]
    end

    %% Vertical VSM flows
    S5 -->|"constrains"| S3
    S3 -->|"governs"| S2
    S2 -->|"orchestrates"| S1
    S4 -->|"informs"| S3

    %% Intelligence loop
    S1 -->|"raw data"| HEXAGON
    HEXAGON -->|"strategic insights"| PART11
    PART11 -->|"direction"| FOUNDATION

    %% External loop (currently broken)
    S1 -.->|"[GAP: auto-distribution absent]"| CLIENT
    CLIENT -.->|"[GAP: revenue=0; loop not closed]"| S1

    %% Outreach
    S1 -->|"outreach artefacts"| L1PARTNER
    L1PARTNER -.->|"[pending: send confirmation absent]"| CLIENT

    %% LIVE FLAG
    LIVEFLAG["⚠ LIVE-FLAG\nDoc 1B §7 Mittelstand\nvs ACTION-PLAN Online-first\nUnresolved 7+ days\nBoth в outreach pack"]
    LIVEFLAG -.->|"affects"| L1PARTNER

    classDef s5node fill:#cce5ff,stroke:#004085
    classDef s4node fill:#e2d9f3,stroke:#6f42c1
    classDef s3node fill:#d4edda,stroke:#28a745
    classDef s2node fill:#fff3cd,stroke:#856404
    classDef s1node fill:#f8d7da,stroke:#721c24
    classDef gapnode fill:#dee2e6,stroke:#6c757d,stroke-dasharray:5 5
    classDef liveflag fill:#ffe5b4,stroke:#e65c00

    class FUNDAMENTAL,PILLARC,R12 s5node
    class HEXAGON,PART11 s4node
    class FOUNDATION,FGR,HITL s3node
    class ROY,SHAREDPROTO s2node
    class VOICE,WIKI,CRM s1node
    class CLIENT,L1PARTNER gapnode
    class LIVEFLAG liveflag
```

**Honest gaps annotated:**

| Gap | Location | Impact | Adjacent-possible? |
|---|---|---|---|
| Auto-KB distribution | S1 (distribute.py.bak archived) | voice loop не closes | YES (one automation step) |
| External loop closure | S1 → Client | revenue = 0; Loop B (internal complexity) dominates | YES (O-04 first client) |
| Halt-Log-Alert | S3 Part 6b | F8/F4/F2 violations not halted within SLA | Phase B stub |
| RoleStateGraph A.2.5 | S2 Part 4 | brigadier sees 2 states per role at 10× dispatch | Phase B stub |
| NQD-CAL in Hexagon | S4 | echo chamber risk at 10× decisions | YES (one process step) |
| LIVE-FLAG ICP | S3/outreach | contradiction reaches L1 partners today | Ruslan decision |
| Runtime enforcement 11/12 Pillar C rules | S5 | S5 richness = spec-only without S3 blocking | Phase B materialization |

**VSM verdict:** S5/S3 richest; S1 weakest = inversion. Pre-operations = hazard. Post-operations (first client) = advantage. [src: 03-comparison-matrix §6 F-6 D-SYS-NEW-1]

**Scalability at 10× (fragile threshold):**

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
xychart-beta
    title "Structural change required at scale gates (%)"
    x-axis ["€50K current","€200K first-hire","€1M managed team","$100M ARR","$1T Clan 100y"]
    y-axis "Restructure required (%)" 0 --> 60
    line [10, 25, 40, 50, 0]
    bar [10, 25, 40, 50, 0]
```

30% = antifragility threshold. Gates €1M and $100M both above threshold = FRAGILE. [src: 03-comparison-matrix §7 F-7]

**5 adjacent-possible activations (one step each):**
- O-01 auto-KB: close voice→wiki loop
- O-04 first client: highest variety impact, closes ALL loops
- O-09 NQD-CAL: add alternatives portfolio to Hexagon
- O-10 ICP fix: resolve Doc 1B vs ACTION-PLAN contradiction
- O-11 R12 ack: AWAITING-APPROVAL packet resolution

[src: 03-comparison-matrix §7 F-8 + SYS-OQ-1]
