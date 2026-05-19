---
title: "Diagram 07 — State Map (LOCKED / ACKED / SURFACE / VAPOR / GAPS)"
date: 2026-05-19
type: mermaid-diagram
parent_doc: 03-state-map-gaps.md
diagram_id: 07
---

# Diagram 07 — 5-Tier State Map

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    subgraph LOCKED[" LOCKED F8 / F5+ — UNTOUCHABLE "]
        F[Foundation v1.0<br/>11 Parts + Pillar A/C<br/>tag 2026-04-28]:::locked
        PC[Pillar C Tier 2<br/>12 rules + R12]:::locked
        OCT[8 Octagon LOCKs<br/>H1-H8]:::locked
        VF[VISION-FUNDAMENTAL<br/>35 UC × 12 cat]:::locked
        WS[Workshop Concept<br/>+ First Clan Charter<br/>+ Action Plan Phase 1]:::locked
        SC[shared/schemas<br/>F8 contracts]:::locked
    end

    subgraph ACKED[" ACKED F2-F3 — Confirmed но не LOCKED "]
        CD[5 concept docs F2<br/>Hackathon/Recursive/Merger/Outreach/Education]:::acked
        ETH[H8 Option A Ethereum +<br/>R12 Option D programmable]:::acked
        VC[9 vision/ companions 01-13]:::acked
        NC[12 NC candidates O-30-41<br/>+ 5 Tier B этим run]:::acked
        WA[6 Tier A wiki + 5 Tier B wiki]:::acked
    end

    subgraph SURFACE[" SURFACE only — require ack/research "]
        DR[5 deep concept research<br/>outputs]:::surface
        HB[200+ H bank across<br/>6 banks]:::surface
        AAP[3 AWAITING-APPROVAL<br/>packets pending]:::surface
        PP[6 promotion docs<br/>NOT YET AUTHORED]:::surface
        OS[4 operational specs<br/>candidates]:::surface
    end

    subgraph VAPOR[" VAPOR — not yet specified (9 critical) "]
        V1[Monetization model<br/>BL CRITICAL]:::vapor
        V2[First hackathon Q3 2026<br/>date/venue/sponsor]:::vapor
        V3[First merger partners]:::vapor
        V4[6-resource 6th category<br/>GAP]:::vapor
        V5[Berlin Grundstück]:::vapor
        V6[Outreach queue v1]:::vapor
        V7[Engineer cohort<br/>recruitment]:::vapor
        V8[L1→L2 fallback<br/>(10% assumption)]:::vapor
        V9[Quality-of-engagement<br/>metric]:::vapor
    end

    subgraph GAPS[" GAPS — что надо проработать "]
        G1[Critical: G-1/2/3<br/>Monetization / Engineer / 6th resource]:::gap-crit
        G2[High: G-4/5/6<br/>Q3 spec / Sponsor / Promotion docs]:::gap-high
        G3[Medium: G-7/8/9<br/>L1→L2 / All-in / Humility]:::gap-med
        G4[Strategic Q: G-10/11/12<br/>Merger Option C / partners / taxonomy]:::gap-strategic
        G5[Foundation candidates: G-13/14<br/>Recursive 5-tuple / Engelbart]:::gap-foundation
        G6[Phase 0 next batch: G-15<br/>12 NCs Tier promotion]:::gap-phase0
    end

    LOCKED -.foundation for.-> ACKED
    ACKED -.evidence for.-> SURFACE
    SURFACE -.path to LOCK if acked.-> LOCKED
    VAPOR -.target to specify.-> SURFACE
    GAPS -.identifies.-> VAPOR
    GAPS -.identifies.-> SURFACE

    classDef locked fill:#9f9,stroke:#000,stroke-width:2px
    classDef acked fill:#cf9
    classDef surface fill:#fff,stroke:#888
    classDef vapor fill:#fcc,stroke:#000
    classDef gap-crit fill:#f66,stroke:#000,stroke-width:2px
    classDef gap-high fill:#fc9,stroke:#000,stroke-width:2px
    classDef gap-med fill:#ffc
    classDef gap-strategic fill:#cef
    classDef gap-foundation fill:#cdf
    classDef gap-phase0 fill:#ecf
```

---

## Count summary

| Tier | Count | Auth/source examples |
|---|---|---|
| LOCKED F8/F5+ | 25+ artefacts | Foundation v1.0 + Pillar C + 8 Octagon + 3 canonical + shared/schemas |
| ACKED F2-F3 | 35+ artefacts | 5 concept docs + 9 vision + 12 NC + 6 Tier A + 5 Tier B wiki + H8 overlay + R12 programmable |
| SURFACE | 200+ items | 5 deep research + ~200 H bank + 3 AAP + 6 promotion docs + 4 ops specs |
| VAPOR | 9 critical | Monetization + Q3 hackathon + merger partners + 6th resource + Grundstück + outreach queue + engineer cohort + L1→L2 + quality metric |
| GAPS | 6 categories × multiple items | Critical 3 + High 3 + Medium 3 + Strategic Q 3 + Foundation 2 + Phase 0 1 |

---

*Mermaid diagram 07 for Doc 3 §8 sprint-synthesis-2026-05-19.*
