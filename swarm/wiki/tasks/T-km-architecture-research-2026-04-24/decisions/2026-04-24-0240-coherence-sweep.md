---
title: Inter-expert coherence sweep — Phase 4 brigadier integration
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
type: decision
layer: tasks
niche: meta
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: brigadier-integration-from-20-cell-drafts
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-scalability-ingest-retrieval-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-scalability-pm-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-scalability-both-layers-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-scalability-epistemic-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-integrator-moat-synthesis.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-scalability-investment-horizon.md"}
binding_scope: km-architecture-phase-4-integration
---

# Phase-4 Inter-Expert Coherence Sweep

## §1 Convergent Findings (>=4 of 5 experts agree)

**C-1 — UC-9 + UC-10 are architecturally absent from current substrate.**
All 5 critics surfaced this as a structural gap requiring closure. Engineering H-3/H-4/H-8 NO; mgmt H-4 NO; systems H-3 NO peer-vs-containment; philosophy H-4 NO UC-7×UC-9 tension; investor H-1 GM-margin-of-safety. **Drives every variant must add proof-by-construction or be dropped.**

**C-2 — UC-9 proof = defense-in-depth STACK (Lakatos protective-belt endorsed).** Three layers stack:
- Phase-A session-level: env-var `WIKI_ROOT_CLIENT_ID` (engineering Δ1)
- Phase-A graph-level: directory namespace `operations/clients/<slug>/<project>/` + `granularity:client:<slug>` frontmatter (mgmt Δ4 + systems E-16 ext)
- Phase-B graph-level: 13th edge `holon-ref` with hard `/lint` cross-holon rejection (systems Δ1; AWAITING-APPROVAL per D3 §3.5)
- Phase-B OS-level: separate git repository per client + OS filesystem permissions

Philosophy-integrator §3 endorses defense-in-depth STACK over single-mechanism (Lakatos protective belt — multiple thin layers > single thick layer for strategic moat preservation). All 5 experts converge.

**C-3 — UC-10 proof = ollama + Mistral-7B-Q4_K_M default (or Llama-3.1-8B alt, pending DACH golden-set eval).** Engineering Δ4 + investor §4 converge on stack: ollama (single-binary; pure-Go) + GGUF model files + 16GB GPU floor. Apache 2.0 (Mistral) cleanest license; Llama Community License OK ≤700M MAU. Phase-A T-Offline = `/ask` `OFFLINE_MODE=1` structured-excerpt path (zero cloud LLM call); Phase-B = full local LLM synthesis.

**C-4 — A2+B2 (federated peer-holons + per-client per-project federated) is the only antifragile-to-G4 pairing.** Engineering-scalability §3, mgmt-scalability §2, systems-scalability §4 all concur. A1+B1 fragile at G3 (single-brigadier attention-budget breaks; grep ceiling at 8K+ pages). Implies migration path A1→A2 / B1→B2 between G2 and G3.

**C-5 — Path B (€3K onboarding + €15K/yr recurring) clears 70% GM in Phase A.** Investor-optimizer Δ-H3 + investor-scalability §4. RESOLVES the Wave-1 investor-vs-Strategic-Insight Path-C dissent. Path C (Hybrid) viable from G2+ post-contractor-#1.

**C-6 — Popperian falsification IS UC-9-compatible** via outcome-level vs content-level distinction (philosophy-scalability §6). Methodology claims testable across isolated client deployments using anonymized acceptance-predicate telemetry; per-client KB content never crosses holon boundary. **Dissolves the apparent UC-7×UC-9 tension.**

## §2 Divergent Positions (preserved as dissents)

**D-1 — Engineering env-var vs Systems 13th-edge for UC-9 architectural mechanism.** Both preserved as defense-in-depth layers per philosophy meta-decision.

**D-2 — Llama 3.1-8B vs Mistral 7B as offline-LLM default.** Resolution path: 20-query German-language golden-set evaluation before Phase-B commit.

**D-3 — Path C (Hybrid) timing: investor-critic says Phase-A 54% GM disqualifies; Strategic Insight §5 says recommended for Enterprise.** Resolution: Path B Phase-A; Path C from G2+ post-contractor-#1.

**D-4 — B1 may survive G3 with portfolio-brigadier aggregation (mgmt-scalability) vs forced sub-roy split at G3 (mgmt-integrator).** Both preserved; brigadier flags as Ruslan-decision-point.

**D-5 — Buffett concentrated A1+B1 (max-focus) vs Taleb barbell 70/30 (investor-integrator).** Resolution: Phase-A barbell default; G3+ revisit Buffett concentration if hurdle-clearance data supports.

**D-6 — FPAR floor 80% (investor) vs 90% (engineering).** Resolution: 80% internal floor; 90% client-deployment gate.

**D-7 — Network-effect formula √N (investor-scalability) vs N² Metcalfe (preserved as upside dissent).** Resolution: √N conservative default; revisit if Alliance governance systematized at G4 removes HITL bottleneck.

**D-8 — Alliance methodology-licensing pilot timing G2 (investor) vs wait-for-G3 (systems).** Resolution: pilot at G2 with explicit disclosure that full EISA-isolation is Phase B.

**D-9 — Cross-client contradiction detection scope: Phase-A absent-by-design (philosophy) vs Phase-B+ slug-normalised federation may enable it (systems).** Resolution: Phase-A adopts safe absolute (no cross-client); Phase-B+ evaluates after Alliance legal structure settled.

(All 9 dissents preserved with F-G-R triples per integrator drafts; full list in §12 of consolidated doc.)

## §3 The 6 Variants (axis-of-differentiation confirmed)

### Layer-A — KM substrate

**A1 — "Karpathy++" (filesystem-resident, retrieval-lean, write-heavy)**
- Source: engineering-integrator
- Axis: filesystem-native + grep+typed-BFS retrieval + W-5 strategies write-back; per-client isolation via env-var + directory-namespace
- Differentiation: low infra complexity; retrieval-lean (Q1 Tier-A/B/C) + on-demand T-Offline synthesis; appropriate G1-G2; fragile at G3 (forces migration to A2)

**A2 — "Federated peer-holons" (per-client autonomous holons + Jetix-methodology-holon)**
- Source: systems-integrator A2 view + supplementary engineering Δ
- Axis: ontological-layered with peer-holon topology + 13th `holon-ref` edge + per-client JSONL shards; isolation by construction at OS-level + graph-level
- Differentiation: structural isolation + Ashby-balanced at G2-G4; antifragile through G4; requires more setup overhead at G1

**A3 — "GraphRAG community-summaries + HippoRAG PPR hybrid" (pre-compiled-heavy)**
- Source: engineering-scalability A3 axis-design proposal
- Axis: pre-compiled retrieval atlas (community detection + PPR index nightly cron) + per-client community pages
- Differentiation: high-quality cross-document synthesis at G2-G5; requires daily-cron infrastructure; over-engineering at G1; activates at G2 (≥3K pages per client)

### Layer-B — Project-Mgmt substrate

**B1 — "Layer-6 namespaces" (thin-scaffold, high-autonomy single-brigadier)**
- Source: systems-integrator B1 view
- Axis: existing D1 Layer-6 `operations/<slug>/` + minimal frontmatter state machine; single Jetix brigadier with on-demand expert dispatch
- Differentiation: minimal overhead; supports 8 active projects today; Agency-trigger fires hard at G3 (≤20 active tasks rule); forces migration to B2 at G3

**B2 — "Federated per-client per-project mini-swarm" (rich-scaffold + per-client brigadier instances)**
- Source: mgmt-integrator + systems-integrator B2 view
- Axis: per-client directory namespace + per-client brigadier instance + 5-file scaffold (consulting type adds offline-inference-spec.md) + lifecycle frontmatter state machine + weekly digest cadence
- Differentiation: structural per-client isolation; antifragile through G4; engineering investment in CI methodology-push fan-out is the G2-G3 critical engineering bet

**B3 — "Adaptive-scaffold phase-gated autonomy" (biological morphogenesis: thin→rich on evidence)**
- Source: engineering-scalability B3 axis-design proposal + mgmt-optimizer Δ6 project-type templates
- Axis: minimal scaffold at bootstrap; auto-extends sections (icp.md / pipeline.md / contracts/ / leads/) when stage-gate predicates fire (e.g., ≥3 leads → leads/ activated; ≥1 contract → contracts/ activated)
- Differentiation: scaffold-cost matches project-stage; risk = stage-gate predicate must be Hamel-binary or B3 collapses to ad-hoc; activates at G1 with rigorous predicates

## §4 Canonical Pairings (3 + cross-pair discussion)

**Pair-1: A1↔B1 (Phase-A solo-founder, conservative, filesystem-native).** 18-month lifespan; migration path defined: A1→A2 + B1→B2 between G2 and G3. Recommended for Phase-A bootstrap (1-3 clients).

**Pair-2: A2↔B2 (Phase-B federated multi-client production).** Antifragile to G4. Activated at G2 first paying client; mature by G3 (50 clients).

**Pair-3: A3↔B2 (high-scale production with pre-computed retrieval atlas).** Activated at G3 (≥3K pages per client + ≥10 clients). A3 augments A2 substrate via nightly community-summaries cron; B2 unchanged. The €1M-and-beyond config.

**Cross-pair note 1: A1↔B2.** Premature B2 federation atop A1 retrieval-lean substrate — works at G1-G2 if first paying client lands early; awkward but functional.

**Cross-pair note 2: A2↔B1.** Federated A but flat Layer-6 B — INCONSISTENT isolation level (per systems-integrator §7 disqualification). NOT RECOMMENDED.

**Cross-pair note 3: A3↔B1.** Pre-compiled atlas with thin Phase-A scaffold — low-value pairing; A3's value is in multi-client cross-document synthesis which requires B2's per-client isolation.

## §5 Brigadier Recommendation Posture (preview for §11 of consolidated doc)

Recommend **Pair-1 (A1↔B1) for Phase-A** with explicit migration plan to **Pair-2 (A2↔B2) at G2 first paying client onset**, and **A3 augmentation at G3 (≥3K pages per client)**. This is the **antifragile trajectory** that respects Phase-A solo-founder constraints, preserves UC-9 + UC-10 by-construction at every gate (Phase-A policy+directory; Phase-B graph+OS), and aligns with investor's barbell 70/30 + Path B €3K+€15K pricing structure.

Philosophy × integrator's defense-in-depth UC-9 endorsement + Systems × scalability's Ashby-mandatory G2 sharding + Investor × scalability's $10M crossover at G3 all support this trajectory. NOT a single-variant pick — a sequenced migration path with explicit gate triggers.

## §6 Phase-5 plan

Brigadier proceeds to:
1. Compose 6 intermediate variant drafts under `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-{A1,A2,A3,B1,B2,B3}-<slug>.md` (each ~4500-5500w per §5.1 template floors).
2. Compose consolidated decision document at `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` (~17-22K words).
3. Compose AWAITING-APPROVAL gate file at `swarm/gates/AWAITING-APPROVAL-km-architecture-variants-2026-04-24.md` (~3K words; 6 variant summaries + recommendation + 9 dissents + 4-response template).
4. Run §13 verification checks.
5. HALT pending Ruslan ack.

— brigadier, 2026-04-24 02:40 CET
