---
title: Wave A Split Note — Part 6 → Part 6a + Part 6b (post-Bundle 1)
date: 2026-04-28
phase: C-1-post-finalize
expert: brigadier
mode: integrator
cycle: cyc-foundation-build-2026-04-28
applied_to:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md
F: F4
ClaimScope: "Holds for cycle cyc-foundation-build-2026-04-28 onward. Prior cycle artefacts that referenced 'Part 6' are unchanged in the historical record (per Reversal Transactions discipline — no edit of past); future references should distinguish 6a vs 6b."
R:
  refuted_if: "Bundle 2/3/4 work surfaces a structural function that should be neither 6a nor 6b, requiring Part 6c"
  accepted_if: "Bundles 2/3/4 reference Part 6a or Part 6b explicitly; no further re-split needed"
sources:
  - prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md §1.1 OQ-MERGED-1 OVERRIDE
  - decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md (Ruslan walkthrough ack)
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md
---

# Wave A Split Note — Part 6 → Part 6a + Part 6b

> **Per Ruslan walkthrough OQ-MERGED-1 OVERRIDE (2026-04-27):** former Part 6 (Governance, Provenance & Human Gate) is split into two parts in Wave C Bundle 1.

## Split rationale

1. **Scale-readiness Phase B/C/D** — Part 6a (provenance officer, periodic audit cadence) and Part 6b (human gate, real-time per-artefact cadence) operate on fundamentally different cadences. Phase B partner integration, Phase C product scale, Phase D org scale all require independent change cadence on these two functions.

2. **Fork-friendly portable provenance standard** — Part 6a's F-G-R schema + citation lint + approval log + quarterly audit framework is GENERIC and portable to any Phase B partner fork. Part 6b's Default-Deny rules, blast-radius assignments, and SLA values include RUSLAN-LAYER bindings that partners replace.

3. **Independent change cadence** — Part 6a evolves as F-G-R discipline matures (rare); Part 6b evolves as new action classes / blast-radius assignments are added (frequent).

## Part 6a — Provenance Officer

**Owns:** F-G-R schema (`shared/schemas/f-g-r.json`); citation enforcement scanner (`/lint --check-citations`); approval log structure (`swarm/approvals/log.jsonl`); quarterly immune audit framework (`swarm/audits/quarterly-template.md`).

**Cadence:** quarterly audit + per-commit citation lint.

**Authoritative architecture document:** `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (16,448 words, finalized 2026-04-28).

## Part 6b — Human Gate

**Owns:** stage-gate predicates registry (`shared/schemas/stage-gates.yaml`); Default-Deny classifier (`.claude/config/default-deny-table.yaml`); blast-radius classification table (`.claude/config/blast-radius-table.yaml`); AWAITING-APPROVAL packet schema (`shared/schemas/awaiting-approval-packet.json` — with `gate_class` UND-4 enum); HITL escalation taxonomy (`.claude/config/escalation-taxonomy.yaml`).

**Cadence:** real-time per-artefact gate enforcement.

**Authoritative architecture document:** `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (15,015 words, finalized 2026-04-28).

## Updates to Wave A artefacts

### MASTER-PLAN-DRAFT.md

10 → 11 parts. The "Part 6 (Governance, Provenance & Human Gate)" row is split into:
- **Part 6a — Provenance Officer** (governance cluster — periodic audit)
- **Part 6b — Human Gate** (governance cluster — real-time gate enforcement)

Both parts are MemberOf the Part 6 governance cluster (parent role, conceptual). The original Part 6 interface card at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md` is SUPERSEDED for Wave C onward — historical record preserved per Reversal Transactions discipline (Young 2010 — "There is no Delete").

### dependency-graph.md

The dependency edges originally pointing to Part 6 are now distinguished:
- Edges relating to F-G-R / citation lint / approval log / quarterly audit → point to Part 6a
- Edges relating to AWAITING-APPROVAL packet / Default-Deny / blast-radius / escalation taxonomy → point to Part 6b
- Reciprocal edge between 6a ↔ 6b: `Part 6a methodologically-uses Part 6b` (consume gate_class enum); `Part 6b methodologically-uses Part 6a` (consume F-G-R schema)
- Per C4 fix: `Part 9 PhaseOf Part 6` corrected to `Part 9 methodologically-uses Part 6b` (Bundle 4 work)
- Per OQ-1 / TRADEOFF-01: Part 8 = audit lead; Part 6a = audit support (provenance enforcement); Part 6b = enforcement arm (real-time)

### Wave B Manifest §2 matrix

Row 6 (former "Part 6 application table") is split. Card #1 Левенчук + Card #13 CAI + Card #14 Mereology now apply primarily to Part 6a. Card #13 CAI Default-Deny + Card #1 IP-4 + Card #6 SRE fail-loud + Card #10 Capital margin + Card #14 Stoic now apply primarily to Part 6b. Cross-mapping table available in each part architecture document §M Wisdom Application Findings.

## Forward direction

- Bundle 2 (Parts 2 + 7): references Part 6b as the gate consumer; references Part 6a indirectly via citation lint applied to Bundle 2 outputs.
- Bundle 3 (Parts 5 + 8): Part 8 references Part 6a as audit framework service (`methodologically-uses`); Part 5 references both 6a (compliance) and 6b (gate decisions on methodology promotions).
- Bundle 4 (Parts 9 + 10): Part 9 references Part 6b (methodologically-uses per C4 fix); Part 10 closes D27 cross-fork approvals reconciliation gap (HARD GAP from Bundle 1 Scenario 4).

## §X Foundation vs RUSLAN-LAYER

This split note itself is GENERIC — Phase B partners encountering a former-Part-6-style artefact import this note's structure (the rationale + the cadence-distinction logic). Specific architecture document paths (`swarm/wiki/foundations/part-6a-*` and `part-6b-*`) are RUSLAN-LAYER instance bindings for the Jetix mono-repo; partners create their own equivalent paths in their fork.
