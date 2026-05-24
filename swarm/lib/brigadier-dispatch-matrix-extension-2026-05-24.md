---
title: Brigadier Dispatch Matrix Extension (Book-Driven Agents 2026-05-24)
date: 2026-05-24
type: dispatch-matrix-extension
parent_doc: .claude/agents/brigadier.md (read-only reference — NOT modified)
parent_routing_table: swarm/lib/routing-table.yaml (29 role entries + 4 R12 auto-pair rules)
ack_record: decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md (MAX-8)
parent_packet: swarm/awaiting-approval/book-driven-agents-2026-05-24.md
created_by: brigadier-scribe (server CC autonomous, Stage 6)
constitutional_posture: R2 packet-gated (Ruslan ack obtained 24.05) + IP-1 strict + R6 + R12 paired-frame + append-only
F: F2
G: brigadier-dispatch-matrix-extension
R: refuted_if_brigadier_md_modified_OR_executor_instance_named
language: russian primary
---

# Brigadier Dispatch Matrix Extension — Book-Driven Agents (2026-05-24)

> **Authority:** brigadier reads this file как dynamic dispatch matrix supplement BEFORE every dispatch decision involving any of 8 new ROY agents.
> Existing brigadier.md is NOT modified (preserved per Stage 2-6 halt rule).

## §1 8 NEW ROY agents — dispatch criteria

### propaganda-expert
- **Dispatch when:** mass-communication design / public-messaging strategy / content-strategy at scale / propaganda critique / historical case study
- **Auto-pair:** influence-ethics-expert MANDATORY (receiver direction)
- **NOT dispatch when:** pure NLP-pattern (→ nlp-expert) / cult-mechanics diagnosis (→ recruitment-dynamics-expert) / pure-marketing copy без strategic lens

### recruitment-dynamics-expert
- **Dispatch when:** Jetix-Clan / Network-State substrate design / cohort recruitment strategy / community-formation review / cult-mechanic defensive audit
- **Auto-pair:** influence-ethics-expert MANDATORY (CRITICAL — R12)
- **Additional checks:** mondragon-wage-ratio + fork-and-leave-clause
- **NOT dispatch when:** pure narrative propaganda (→ propaganda-expert) / pure NLP (→ nlp-expert) / pure engagement-loop (→ gamification-engagement-expert)

### nlp-expert
- **Dispatch when:** verbal-reframing for Ruslan's prose / communication-pattern audit / NLP-pattern consultation
- **Auto-pair:** influence-ethics-expert MANDATORY (STRICT)
- **Additional checks:** witkowski-critical-review-attached + milton-model-bite-cross-ref
- **NOT dispatch when:** mass-propaganda design / cult-mechanic diagnostic / hypnosis-deployment (Default-Deny F4 → escalate to Ruslan)

### sota-tracker-expert
- **Dispatch when:** weekly arxiv intake / SOTA digest request / paradigm-shift candidate review / field-state mapping for research project
- **Auto-pair:** none (pure epistemic surface)
- **NOT dispatch when:** single-claim epistemic audit (→ philosophy-expert evaluative) / production ML engineering (→ ml-ai-foundations-expert + engineering-expert)

### methodology-engineer
- **Dispatch when:** method-card production / Essence alpha-state binding / method-exchange protocol design / reflective-practice substrate / Russian methodology canon consultation
- **Auto-pair:** none (meta-discipline)
- **NOT dispatch when:** pure SE practice review (→ engineering-expert) / pure delivery planning (→ mgmt-expert) / pure systems-thinking analysis (→ systems-expert)

### ml-ai-foundations-expert
- **Dispatch when:** ML/AI literature review / MAS scaling analysis for Jetix swarm / MAS failure-mode audit / DL curriculum consultation
- **Auto-pair:** none (technical surface)
- **NOT dispatch when:** production ML engineering code review (→ engineering-expert) / pure paradigm-shift epistemic audit (→ philosophy-expert + sota-tracker) / ML product strategy (→ Ruslan + investor-expert)

### influence-ethics-expert (R12 ENFORCEMENT CELL)
- **Dispatch direction:** RECEIVER ONLY — fires WHEN propaganda / recruitment-dynamics / nlp / gamification-engagement dispatches
- **NEVER dispatch standalone** — no independent tactic surfacing
- **AUTHORITY:** VETO power on any unpaired dispatch — brigadier MUST halt-log-alert + re-dispatch with paired-frame
- **Halt-Log-Alert F4 ≤5s** on missing pairing; emit to swarm/approvals/log.jsonl per Part 6b §I.2

### gamification-engagement-expert
- **Dispatch when:** gamification design (product or community) / virtual-economy substrate (Jetix-Clan tokenomics) / Network-State sub-economy modeling / engagement-loop critique
- **Auto-pair:** influence-ethics-expert MANDATORY
- **Additional checks:** hook-model-manipulation-matrix-pair + rentier-anti-pattern-check
- **NOT dispatch when:** pure narrative propaganda / pure NLP / pure cult-recruitment

## §2 R12 paired-frame enforcement protocol

```
1. brigadier receives task
2. brigadier identifies primary agent(s) needed
3. IF primary agent ∈ {propaganda, recruitment-dynamics, nlp, gamification-engagement}:
   3a. brigadier MUST also dispatch influence-ethics-expert (receiver direction)
   3b. influence-ethics-expert provides paired-frame annotations attached to primary outputs
   3c. brigadier verifies pairing complete BEFORE promoting any output
4. IF pairing skipped → Halt-Log-Alert F4 → swarm/approvals/log.jsonl
5. r12-paired-frame-check.sh hook (swarm/lib/hooks/) runs at session-end to verify
```

## §3 IP-1 split clarifications (preserved)

- **philosophy-expert** = evaluative rationality (single claim epistemic audit)
- **sota-tracker-expert** = instrumental rationality of staying current (field-state operations)
- Both consult Popper-Kuhn-Lakatos-Feyerabend canon but for DIFFERENT modes

- **engineering-expert** = SE practice code review + architecture
- **methodology-engineer** = method-as-discipline + alpha-state framing
- **systems-expert** = cybernetics + VSM + Senge
- All three orthogonal; cross-consult via brigadier

## §4 Cycle hook integration

New hook: `swarm/lib/hooks/r12-paired-frame-check.sh`
- Cycle-2 mode: log-only (warns, does not fail)
- Scans recent drafts for paired-frame discipline
- Emits F4 alert records to swarm/approvals/log.jsonl
- Authority: Part 6b §I.2 LOCKED Halt-Log-Alert framework

## §5 What this extension does NOT do

- ❌ NOT modify `.claude/agents/brigadier.md` (existing 9 ROY agents UNTOUCHED per Stage 2-6 halt rule)
- ❌ NOT modify LOCKED Foundation content
- ❌ NOT name executor instances (IP-1 strict — slugs only)
- ❌ NOT auto-deploy on dispatch (cycle-2 log-only)

## §6 Authority trail

- Ruslan ack 2026-05-24: `decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md` MAX-8
- Parent packet: `swarm/awaiting-approval/book-driven-agents-2026-05-24.md`
- Phase 4 drafts: `reports/book-driven-agents-2026-05-24/04-per-agent-substrate-drafts.md`
- Phase 5 wikis: `reports/book-driven-agents-2026-05-24/05-wiki-auto-creation-proposals.md`
- Execution prompt: `prompts/execute-book-driven-agents-stage-2-6-2026-05-24.md`
- Routing table: `swarm/lib/routing-table.yaml` (29 role entries + 4 R12 auto-pair rules)

[src: prompts/execute-book-driven-agents-stage-2-6-2026-05-24.md Stage 6 + decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md MAX-8 ack + reports/book-driven-agents-2026-05-24/04-per-agent-substrate-drafts.md §4.10 + swarm/awaiting-approval/book-driven-agents-2026-05-24.md §6]
