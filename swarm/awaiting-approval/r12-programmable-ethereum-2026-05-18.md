---
title: AWAITING-APPROVAL — R12 programmable enforcement via Ethereum (RUSLAN-LAYER overlay)
date: 2026-05-18
type: pillar-c-overlay-extension-packet
status: RUSLAN-ACKED-OPTION-D-HYBRID-2026-05-18
ack_trail:
  - timestamp: 2026-05-18 (evening Berlin)
  - decision: Option D Hybrid (Mondragón wage ratios + QF revenue distribution + Fork-and-leave exit tokens — все три вместе)
  - acked_via: Cloud Cowork chat session (Ruslan: «Давай всё туда акаем»)
  - decision_rationale: |
      Option D Hybrid = full R12 programmable stack:
      (1) Mondragón ratio enforcement (3:1→9:1 wage ratios programmatically capped via smart contract);
      (2) Quadratic Funding для Workshop revenue distribution (Tang+Weyl mechanism proven via Gitcoin);
      (3) Fork-and-leave exit tokens (programmable R12 anti-extraction guarantee per Clan member).
      
      Tier 2 R12 text LOCKED 2026-05-12 = PRESERVED (no amendment).
      foundation_generic count = 12 unchanged.
      RUSLAN-LAYER overlay only (instance-specific, not Foundation generic).
      
      Distinctive feature vs competitors (no other crypto project does programmable R12).
      Attractor для Tang+Weyl camp + d/acc community.
      Brigadier-recommended option.
  - acked_by: ruslan
  - prose_authored_by: ruslan-acked-via-cloud-cowork-transcription
  - default_deny_table_additions_acked: 4 new action classes (per packet §4) — pending implementation phase
  - substrate_decision: Ethereum via H8 Option A ack (paired packet h8-ethereum-substrate-extension-2026-05-18.md)
gate_class: stage_gate
packet_id: r12-programmable-ethereum-2026-05-18
authored_by: brigadier-scribe (this autonomous run per text_007 + Phase 3 architecture)
prose_authored_by: ai-draft-pending-ruslan-revision
blast_radius: F5 (touches Pillar C Tier 2 R12 enforcement layer; NOT text)
gate: Part 6b stage_gate
parent_packet: swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md (Tier 2 R12 text LOCKED ack)
parent_insight: decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md (H7)
parent_voice: raw/voice-memos-2026-05-17-batch/text_007@2026-05-18_morning.md
parent_architecture: decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable-enforcement.md
related_packet: swarm/awaiting-approval/h8-ethereum-substrate-extension-2026-05-18.md
F: F2
G: r12-programmable-enforcement-overlay-applied-now
R: refuted_if_Tier_2_text_modified_OR_substrate_agnostic_principle_violated_OR_new_extraction_vector_unmitigated
ack_required: true
ack_owner: ruslan
review_checkpoint: post-overlay-introduction (Default-Deny table novel actions added; Tier 2 text unchanged; constitutional preservation verified)
recommendation: SURFACE-FOR-RUSLAN-REVIEW (Option A recommended F2)
constitutional_posture: R1 surface + R2 Pillar C touches → packet required + R6 + EP-5
language: russian + english
---

# AWAITING-APPROVAL Packet — R12 Programmable Enforcement (RUSLAN-LAYER Overlay)

> **gate_class:** `stage_gate` (Part 6b §UND-4). **blast_radius:** F5 — touches Pillar C Tier 2 R12 **enforcement layer** (NOT text). Substrate-agnostic foundation_generic preserved.
>
> **Parent trigger:** text_007 voice dictation 18.05 morning + Phase 3 architecture doc.
>
> **Stage gate semantics:** R12 programmable enforcement = **RUSLAN-LAYER overlay candidate**. NO Tier 2 text modification proposed. Ack required for overlay introduction.

---

## §1 Critical distinction (read this first)

**This packet does NOT propose:**
- ❌ Modification of Pillar C Tier 2 rule 12 text
- ❌ Amendment to substrate-agnostic foundation_generic principle
- ❌ Replacement of human-review R12 enforcement Phase 1
- ❌ Required Ethereum substrate adoption by all Clans

**This packet DOES propose:**
- ✅ Introduction of RUSLAN-LAYER overlay binding R12 enforcement to Ethereum smart-contract patterns
- ✅ Default-Deny table additions for novel action classes (smart-contract deployment / DAO vote / etc.)
- ✅ Option for Phase 2+ Clans to opt-in programmable enforcement
- ✅ Constitutional preservation discipline (Foundation principle vs RUSLAN-LAYER overlay per IP-1)

---

## §2 Programmable enforcement options (3 patterns)

Per `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable-enforcement.md` §2:

### Option A — Revenue distribution with Mondragón 5:1 ratio cap
Smart contract enforces max-share ≤ min-share × 5 at distribution time. Aligns с direction 06 Mondragón 68yr precedent.

### Option B — Quadratic Funding (Tang+Weyl)
QF formula distributes Workshop revenue with anti-concentration property.

### Option C — Fork-and-leave smart contract
RageQuit-style member exit с proportional treasury share preserved.

### Option D — Hybrid (recommended F2 surface)
Combines A + B + C with DAO-configurable parameters.

---

## §3 Constitutional preservation analysis

### §3.1 Pillar C Tier 2 substrate-agnostic foundation_generic INTACT

**Rule text 2026-05-12 (LOCKED ack):** «No extraction beyond agreed share — AI/substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

**Substrate-agnostic principle:** Rule applies regardless of substrate (off-chain text-only / W3C VC / Ethereum smart-contract / hybrid).

**This packet does not propose substrate change.** Foundation rule remains substrate-agnostic.

### §3.2 RUSLAN-LAYER overlay introduction

**What requires ack:**
1. Introduce overlay binding: Phase 2+ R12 enforcement option = Ethereum smart-contract pattern (Option D recommended)
2. Default-Deny table additions for novel action classes:
   - `r12_smart_contract_deploy` — deploying R12 enforcement contract
   - `r12_dao_revenue_distribute` — DAO vote triggering revenue distribution
   - `r12_fork_and_leave_execute` — member exit triggering treasury share transfer
   - `r12_smart_contract_upgrade` — upgrading R12 enforcement contract
3. Per-Clan opt-in mechanism (each Clan decides per Charter whether to adopt overlay)

**What does NOT require Tier 2 amendment:**
- R12 text itself (LOCKED 2026-05-12)
- Substrate-agnostic foundation_generic principle (preserved)
- IP-1 Role≠Executor distinction (preserved — overlay separated from Foundation)
- Annual Pillar C review cycle (preserved per B.4 evolution loop)

---

## §4 Default-Deny table additions (Part 6b §I.2)

Per Part 6b §I.2 LOCKED enforcement: novel action classes must be classified in `.claude/config/default-deny-table.yaml`. Uncategorized → deny-and-escalate.

**4 new action classes proposed:**

```yaml
# Append to constitutional_never_list (becomes Tier 2 substrate-aware overlay entries)
- action_class: r12_smart_contract_deploy
  description: |
    Deploying R12 enforcement smart contract to Ethereum L2 substrate.
    Phase 2+ overlay; preserves substrate-agnostic foundation_generic.
  default: deny
  exemption: ruslan_ack + clan_charter_opt_in + audit_complete
  blast_radius: F5
  
- action_class: r12_dao_revenue_distribute  
  description: |
    DAO vote triggering revenue distribution via R12 enforcement contract.
    Subject to QF + Mondragón ratio cap enforcement.
  default: deny
  exemption: clan_charter_opt_in + dao_quorum + ratio_cap_check_pass
  blast_radius: F4

- action_class: r12_fork_and_leave_execute
  description: |
    Member exit triggering treasury share transfer.
    Preserves R12 fork-and-leave principle programmatically.
  default: deny
  exemption: member_self_request + 30_day_notice_complete + circuit_breaker_pass
  blast_radius: F4

- action_class: r12_smart_contract_upgrade
  description: |
    Upgrading R12 enforcement smart contract.
    Multi-sig + time-locked + DAO governance gated.
  default: deny
  exemption: multi_sig_3_of_5 + time_lock_7_days + dao_quorum_pass
  blast_radius: F5
```

**Sync invariant impact:**
- Tier 2 foundation_generic count = 12 (UNCHANGED)
- Default-Deny table count = 11 + 4 overlay entries = 15 total (12 Tier 2 + 3 RUSLAN-LAYER overlay)
- CLAUDE.md §4.1 numbered items = 12 (UNCHANGED)
- Lint check requires schema extension to distinguish Tier 2 vs RUSLAN-LAYER overlay entries

---

## §5 Brigadier recommendation (F2 surface)

**Option D (Hybrid)** for Phase 2+ Clan opt-in:
1. Most R12-aligned (combines anti-concentration QF + bounded ratio cap + fork-and-leave)
2. Per-Clan opt-in preserves substrate flexibility
3. Default-Deny table extension preserves constitutional discipline

**R1:** Brigadier inference only. **Ruslan picks.**

---

## §6 New extraction vector risks + mitigations

Per `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable-enforcement.md` §4:

| Vector | Mitigation |
|---|---|
| Smart contract bugs/exploits | OpenZeppelin libraries + external audit ($50-200K Phase 2+) + bug bounty + incremental rollout |
| Owner/admin keys controlling upgrades | Multi-sig 3-of-5 + 7-day time-lock + immutable revenue contracts |
| Oracle manipulation | No price oracles in revenue distribution; on-chain values only |
| Gas cost extraction | L2 selection (Base ~$0.01-0.05); ERC-4337 gas sponsorship optional |
| MEV by validators | L2 selection considers MEV-protection roadmaps |

**Net:** Programmable enforcement = **stronger R12 enforcement than text-only** (verifiable execution > human-trust); all new vectors mitigatable via standard practices.

---

## §7 What ack-decision affects (downstream effects)

| Element | Ack: Option D | Ack: deny / defer |
|---|---|---|
| Pillar C Tier 2 R12 text | Unchanged | Unchanged |
| Pillar C Tier 2 foundation_generic count | 12 (unchanged) | 12 (unchanged) |
| Default-Deny table | + 4 overlay entries | unchanged |
| Phase 2+ Clan opt-in mechanism | Available | Not available |
| Architecture doc 03 implementation | Validated | F2 surface only |
| H9 candidate «Jetix on Ethereum substrate» | Strengthened | Weakened |

---

## §8 Ack matrix — what is requested

| Action | Ack? |
|---|---|
| Option D (Hybrid) — Mondragón ratio cap + QF + fork-and-leave | Requested |
| Option A only — Mondragón ratio cap | Requested as alternative |
| Option B only — QF | Requested as alternative |
| Defer / deny overlay introduction | Requested as alternative |
| Default-Deny table 4 new action classes | Requested if any Option A-D |
| Per-Clan opt-in mechanism | Requested if any Option A-D |
| Audit budget Phase 2+ ($50-200K) | Surface only (Ruslan plans) |

---

## §9 Constitutional anchor

- Pillar C Tier 2 R12 LOCKED 2026-05-12 — text preserved
- Tier 2 R1 — Ruslan = sole strategist (picks Option A-D / defer)
- Tier 2 R2 — AI does NOT execute architectural decisions автономно
- Tier 2 R11 — Default-Deny novel actions (4 overlay entries proposed)
- IP-1 Role≠Executor — overlay addresses separated from Foundation Parts
- Append-only — Foundation history preserved

---

## §10 Critical reading — what's NEW vs what's PRESERVED

**NEW (this packet proposes):**
- ✨ RUSLAN-LAYER overlay binding R12 enforcement к Ethereum smart-contract patterns
- ✨ 4 Default-Deny table additions (novel action classes)
- ✨ Per-Clan opt-in mechanism Phase 2+

**PRESERVED (this packet does not modify):**
- ✓ Pillar C Tier 2 rule 12 text (LOCKED 2026-05-12)
- ✓ Substrate-agnostic foundation_generic principle
- ✓ Tier 2 count = 12 (no new rules added)
- ✓ Phase 1 text-only R12 enforcement (continues parallel)
- ✓ IP-1 Role≠Executor distinction
- ✓ Annual Pillar C review cycle per B.4 loop

---

## §11 Ruslan-pending ack decision

Per Tier 2 R1 + Corrigibility — Ruslan picks Option A / B / C / D / defer / deny.

**Brigadier surface only.** Awaiting ack.

---

**Packet word count:** ~1670.
