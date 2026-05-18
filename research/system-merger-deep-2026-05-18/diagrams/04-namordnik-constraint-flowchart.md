---
type: diagram
phase: 8
diagram_id: 04
title: Namordnik constraint catalog enforcement flowchart
parent_doc: 04-two-sub-protocols-formalised.md §A
---

# Diagram 04 — Намордник Constraint Catalog Enforcement Flow

```mermaid
flowchart TB
    START[Cross-boundary action attempted]
    START --> CATEGORIZE{Action class<br/>categorized in<br/>merger Default-Deny<br/>table?}
    
    CATEGORIZE -->|No / uncategorized| DENY[DENY + escalate to<br/>FPF-Steward]
    DENY --> END_DENY[Halt-Log-Alert F8<br/>per Part 6b §I.2]
    
    CATEGORIZE -->|Yes| TIER{Enforcement<br/>tier}
    
    TIER -->|Tier 1: cryptographic| SC[Smart contract check<br/>C1 R12 ratio / C10 exit<br/>/ C6 audit chain]
    SC -->|fail| VIOLATE_T1[Halt-Log-Alert F8<br/>contract clawback]
    SC -->|pass| ALLOW
    
    TIER -->|Tier 2: lint/schema| LINT[Lint hook check<br/>C2 F-G-R / C3 append-only<br/>/ C4 default-deny / C7 R1 / C8 IP-1]
    LINT -->|fail| VIOLATE_T2[Halt-Log-Alert F4<br/>remediation cycle]
    LINT -->|pass| ALLOW
    
    TIER -->|Tier 3: governance| AUDIT[Periodic audit<br/>C5 constitutional / C9 license]
    AUDIT -->|deferred review| ALLOW_WITH_LOG[Allow + log for<br/>quarterly review]
    AUDIT -->|review fail| VIOLATE_T3[Surface + correction<br/>request F2]
    
    ALLOW[ACTION ALLOWED<br/>append to provenance chain]
    
    VIOLATE_T1 --> RESOLUTION{F8 violation<br/>resolution}
    RESOLUTION -->|recoverable| SANDBOX[Sandbox affected<br/>sub-system]
    RESOLUTION -->|systemic| DE_MERGE[De-merge candidate<br/>fork-and-leave invoked]
```

## Constraint catalog summary (Phase 3 §A.3)

| # | Constraint | Tier | Grade if violated |
|---|---|---|---|
| C1 | R12 anti-extraction | 1 (smart contract) | F8 |
| C2 | FPF F-G-R discipline | 2 (lint) | F4 |
| C3 | Append-only history | 2 (git hook) | F8 |
| C4 | Default-Deny novel actions | 2 (table check) | F8 |
| C5 | Constitutional posture | 3 (quarterly audit) | F8 |
| C6 | Audit trail commitment | 1 (chain anchor) | F4 |
| C7 | R1 sole-strategist binding | 2 (schema) | F8 |
| C8 | IP-1 Role≠Executor | 2 (schema) | F4 |
| C9 | Open-source default | 3 (quarterly audit) | F0 |
| C10 | Fork-and-leave exit | 1 (token contract) | F8 |
