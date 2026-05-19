---
type: diagram
phase: 8
diagram_id: 05
title: USB-C порт translation flow (3 modes)
parent_doc: 04-two-sub-protocols-formalised.md §B
---

# Diagram 05 — USB-C порт Translation Flow

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    subgraph Incoming_System["Incoming System (native model)"]
        IN_DATA[Native data: User, Project, ...]
        IN_LOGIC[Native business logic]
    end

    subgraph ACL["Anti-Corruption Layer (per Evans DDD)"]
        ACL_RULES[Translation rules<br/>per entity class]
        ACL_AUDIT[Audit hooks<br/>append-only log]
    end

    subgraph FPF_BRIDGE["FPF Bridge Layer (A.6.B)"]
        FPF_LANG[FPF U.* primitives<br/>Performer, MethodDescription,<br/>BoundedContext, ...]
        MODE{Mode}
    end

    subgraph Host_System["Host System (Jetix-FPF)"]
        HOST_DATA[FPF-native data]
        HOST_LOGIC[Constitutional posture<br/>+ R12 enforcement]
    end

    IN_DATA -->|attempt cross-boundary| ACL_RULES
    ACL_RULES --> MODE
    
    MODE -->|FULL-FPF| FPF_LANG
    MODE -->|PARTIAL-FPF<br/>5-15% overhead| FPF_LANG
    MODE -->|OPAQUE-BRIDGE<br/>0-2% overhead<br/>HIGH drift risk| FPF_LANG
    
    FPF_LANG --> HOST_DATA
    
    ACL_RULES -.->|every event| ACL_AUDIT
    ACL_AUDIT -.->|Merkle-anchor| CHAIN[On-chain audit anchor]
    
    HOST_LOGIC -.->|response| ACL_RULES
    ACL_RULES -.->|reverse translate| IN_DATA

    style MODE fill:#9cf,stroke:#333,stroke-width:2px
    style ACL_AUDIT fill:#ffc,stroke:#333,stroke-width:1px
```

## Mode characteristics (Phase 3 §B.4)

| Mode | Use case | Overhead | Maintenance | Drift risk |
|---|---|---|---|---|
| FULL-FPF | Incoming small / greenfield / FPF-curious | ~0% | High initial, low later | Low |
| PARTIAL-FPF | Mid-size with legacy; pragmatic | 5-15% | Medium ongoing | Medium |
| OPAQUE-BRIDGE | Highly proprietary / regulated | 0-2% | Low | High |

**Hypothesis H-SM-12:** PARTIAL-FPF overhead <15% acceptable; >20% requires redesign.

**Hypothesis H-SM-18:** OPAQUE-BRIDGE without upgrade в 24 months shows 3× drift vs PARTIAL/FULL.
