---
title: "Diagram 04 — DAO multi-Clan governance flow"
date: 2026-05-18
type: architecture-diagram
F: F3
G: jetix-dao-multi-clan-governance-diagram
parent: ../00-MASTER-ARCHITECTURE.md
---

# Diagram 04 — DAO multi-Clan governance flow

## §1 Multi-Clan Federation architecture

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
  subgraph Federation ["Multi-Clan FEDERATION DAO (Phase 3+)"]
    Fed_Treasury[Federation Treasury<br/>shared infrastructure funds]
    Fed_Vote[Federation Vote Mechanism<br/>Quadratic Voting + reliability-weighted]
    Fed_Scope[Federation Scope:<br/>- cross-Clan disputes<br/>- shared infrastructure<br/>- cross-Clan SBT recognition<br/>NOT internal Clan affairs]
  end
  
  subgraph Clan_A ["CLAN A (Aragon OSx DAO)"]
    A_Members[10-100 members<br/>SBT-gated]
    A_Treasury[Clan A Treasury<br/>Workshop revenue + grants]
    A_Vote[Clan A Vote<br/>QV per SBT holder]
    A_Delegate[Clan A Delegate<br/>elected via QV rotation]
  end
  
  subgraph Clan_B ["CLAN B (Aragon OSx DAO)"]
    B_Members[10-100 members<br/>SBT-gated]
    B_Treasury[Clan B Treasury]
    B_Vote[Clan B Vote]
    B_Delegate[Clan B Delegate]
  end
  
  subgraph Clan_C ["CLAN C (Aragon OSx DAO)"]
    C_Members[10-100 members<br/>SBT-gated]
    C_Treasury[Clan C Treasury]
    C_Vote[Clan C Vote]
    C_Delegate[Clan C Delegate]
  end
  
  subgraph FoundationLayer ["Foundation Layer 1 (off-DAO scope)"]
    Found[Foundation v1.0 LOCKED<br/>Pillar C R12 substrate-agnostic<br/>NOT subject to DAO governance]
    Ruslan[Ruslan ack-authority<br/>strategist (Tier 2 R1)<br/>Constitutional steward]
  end
  
  A_Members -->|elect via QV| A_Delegate
  B_Members -->|elect via QV| B_Delegate
  C_Members -->|elect via QV| C_Delegate
  
  A_Delegate -->|seat in Federation| Fed_Vote
  B_Delegate -->|seat in Federation| Fed_Vote
  C_Delegate -->|seat in Federation| Fed_Vote
  
  Fed_Vote -->|governs| Fed_Treasury
  Fed_Vote -->|governs| Fed_Scope
  
  A_Vote -->|governs| A_Treasury
  B_Vote -->|governs| B_Treasury
  C_Vote -->|governs| C_Treasury
  
  Found -.constitutional anchor.-> A_Vote
  Found -.constitutional anchor.-> B_Vote
  Found -.constitutional anchor.-> C_Vote
  Found -.constitutional anchor.-> Fed_Vote
  
  Ruslan -.ack-authority.-> Found
  Ruslan -.ack-authority.-> Fed_Scope
  
  Fed_Scope -->|escalates contradictions| Ruslan
  
  style Federation fill:#fef3c7,color:#1a202c
  style Clan_A fill:#dbeafe,color:#1a202c
  style Clan_B fill:#dbeafe,color:#1a202c
  style Clan_C fill:#dbeafe,color:#1a202c
  style FoundationLayer fill:#fce7f3,color:#1a202c
```

## §2 Reading guide

**3 levels:**

1. **Clan level (blue)** — each Clan = independent Aragon OSx DAO. Internal governance: Workshop curriculum, revenue distribution, new member admissions, project priorities. **Sovereign в его scope.**

2. **Federation level (yellow)** — meta-DAO; each Clan = 1 delegate (elected via QV per-Clan). Federation **only** governs:
   - Cross-Clan disputes (e.g., Clan A member claims R12 violation by Clan B)
   - Shared infrastructure costs (Foundation maintenance, Workshop platform)
   - Cross-Clan SBT recognition (Clan A graduate SBT accepted by Clan B?)

   Federation does NOT govern individual Clan internal affairs.

3. **Foundation level (pink) — OFF-DAO** — Foundation v1.0 LOCKED + Pillar C R12 + IP-1 + constitutional principles. **NOT subject to DAO governance.** Federation must operate within Foundation principles. Constitutional contradictions escalate к **Ruslan ack-authority** (Tier 2 R1 sole strategist).

## §3 Decision routing matrix

| Decision type | Authority |
|---|---|
| Workshop curriculum within Clan | Clan DAO vote (QV) |
| Workshop revenue distribution within Clan | Clan DAO + QF + Mondragón cap |
| New member admission within Clan | Clan DAO vote |
| Clan delegate election | Clan members via QV |
| Cross-Clan dispute | Federation vote OR escalate Ruslan ack |
| Shared infrastructure costs | Federation vote |
| Cross-Clan SBT recognition | Federation vote (per-source-Clan or general policy) |
| Foundation Part amendment | Ruslan ack via AWAITING-APPROVAL packet (NOT DAO) |
| Pillar C Tier 2 amendment | Ruslan ack via AWAITING-APPROVAL packet (NOT DAO) |
| Constitutional principle adoption | Ruslan ack via AWAITING-APPROVAL packet (NOT DAO) |

## §4 Constitutional preservation

**Critical invariants:**

- **Pillar C R7 (no autonomous contradiction arbitration):** DAO vote = «registered decision»; if contradicts Foundation → escalate Ruslan
- **Pillar C R9 (no AI self-modification):** AI agents = advisory; cannot vote
- **IP-1 (Role≠Executor):** Foundation Parts name abstract roles; specific DAO addresses live in RUSLAN-LAYER overlay
- **R12 anti-extraction:** Federation cannot extract value from member Clans beyond agreed share; per-Clan fork-and-leave preserved

**Failure modes mitigated:**

| Failure mode | Mitigation |
|---|---|
| Federation 51% attack against minority Clan | QV anti-concentration + Foundation scope limitation + Ruslan ack escalation |
| Clan internal R12 violation | Member can fork-and-leave (RageQuit) + Federation arbitration available |
| AI agent voting in DAO | Forbidden by Pillar C R9; DAO smart contract requires human-Soul signature |
| Foundation amendment via DAO majority | NOT allowed; AWAITING-APPROVAL packet к Ruslan only |

## §5 Phase progression

- **Phase 1 (now):** 1 Clan only (Charter v0; 10 signatories target); no Federation needed
- **Phase 2 (Q4 2026+):** Single Clan governance; Federation conceptual only
- **Phase 2+ Ethereum overlay:** First Clan DAO deployed; Federation not yet
- **Phase 3 (2028+):** 3+ Clan; Federation DAO deployed; multi-Clan governance operational

## §6 Source

`../05-dao-governance-multi-clan.md` §2 + `../00-MASTER-ARCHITECTURE.md` §4 constitutional preservation
