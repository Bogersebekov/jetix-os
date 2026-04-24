---
title: WBS — T-km-architecture-research-2026-04-24 (20-cell decomposition)
type: proposal
layer: proposals
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: brigadier-attested-from-prompt-§6
tier: tier-1
produced_by: brigadier
sources:
  - {path: "prompts/km-architecture-research-2026-04-24.md", range: "§6.1, §6.4"}
  - {path: ".claude/agents/brigadier.md", range: "§3.3 / §3.3.1 / §4.6"}
  - {path: "swarm/lib/shared-protocols.md", range: "§3 schema"}
related: []
binding_scope: km-pm-architecture-research
shape: design+combined-scale-project+review
chat_or_decompose: decompose
decompose_or_chat_predicates_fired: 4-of-4
  - complexity > simple (multi-domain synthesis required)
  - adversarial review required (critic-mode for each layer)
  - horizon projection required (all 5 gates, all 6 variants)
  - multi-domain synthesis required (engineering + mgmt + systems + philosophy + investor)
---

# 20-Cell Decomposition — KM + Project-Mgmt Architecture Research

## §0 Decompose-or-Chat gate (E-17 verbatim)

Per `.claude/agents/brigadier.md §3.0`: matrix invocation requires ≥1 of 4
predicates. **All 4 fire** for this task:

1. ✓ Complexity > simple — 6 variants × 10 use cases × 5 horizon gates =
   ≥300 distinct claims to derive; well beyond a single-cell brief.
2. ✓ Adversarial review required — critic-mode produces ≥5 binary
   Conformance Checks per draft; non-negotiable per execution prompt §1.4.
3. ✓ Horizon projection required — every variant projected through all 5
   gates per HD-01 5-gate propagation.
4. ✓ Multi-domain synthesis required — KM architecture spans engineering
   (ingest/retrieve), mgmt (project-mgmt), systems (ontology/holarchy),
   philosophy (epistemic), investor (capital/moat).

**Decision:** decompose into full 5×4 = 20 cells (cap 20 per §3.1
complexity-to-fan-out rule for "open-ended synthesis"). M-class slot
1-of-2 consumed per HD-02.

## §1 Wave dispatch plan (CE 40/10/40/10)

| Wave | Cells | Mode | Trigger | Duration target |
|---|---|---|---|---|
| W1 | #1, #5, #9, #13, #17 | critic | post-intake | 1 brigadier-message |
| W2 | #2, #6, #10, #14, #18 | optimizer | after W1 returns | 1 brigadier-message |
| W3 | #3, #7, #11, #15, #19 | integrator | after W2 returns | 1 brigadier-message |
| W4 | #4, #8, #12, #16, #20 | scalability | after W3 returns | 1 brigadier-message |

Each wave dispatched in parallel (single brigadier-message containing 5
`Task()` calls) per `.claude/agents/brigadier.md §4.3`. No cell calls
another cell directly; if a cell needs peer input it returns
`escalations[]{trigger: peer-input-needed}` and brigadier dispatches
the peer (none expected in this cycle — wave ordering pre-empts).

## §2 Cell table (OPP-04 cell_acceptance_predicate compliance, cycle-2 schema)

All cells: `class: M` (Method-development; per HD-02 each consumes the
1 structural M-slot's allocated cells; no rate-limit hit because they are
sub-decomposition cells of the single M-task, not separate M-tasks).

decomposition:
  - cell: engineering × critic
    cell_id: 1
    wave: 1
    class: M
    ap_cost: 25000
    ap_budget: 40000
    inputs:
      - prompts/km-architecture-research-2026-04-24.md
      - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1, D2, D3, D6, D7, D8)
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Parts A, B, F, G)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
      - swarm/lib/shared-protocols.md
      - .claude/agents/engineering-expert.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks against existing wiki v3 ingest/retrieval mechanics AND ≥2 Alternatives per check AND explicit Anti-scope AND each H-N row carries (F, ClaimScope, R) triple"
    primary_focus: "Audit wiki v3 D1-D12 for ingest/retrieval weaknesses; check Q1 4-tier ability to serve UC-1..UC-3 at G1-G3; identify what BREAKS for UC-9 isolation + UC-10 offline-first"

  - cell: engineering × optimizer
    cell_id: 2
    wave: 2
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
      - prompts/km-architecture-research-2026-04-24.md
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Parts B, F, H)
      - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§4.6, §5.5-5.10)
      - .claude/agents/engineering-expert.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md
    cell_acceptance_predicate: "Returns ingest+retrieval delta proposals each with WLNK/MONO/IDEM/COMM/LOC declared (apply or preserve) AND before/after table AND refuses on method-change with documented rationale"
    primary_focus: "Concrete ingest-skill + retrieval-skill edits; Unix-pipeline composition; pre-cache vs on-demand tradeoffs; offline-LLM stack engineering"

  - cell: engineering × integrator
    cell_id: 3
    wave: 3
    class: M
    ap_cost: 35000
    ap_budget: 55000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
      - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1, D2, D3, D6)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
      - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md (full)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md
    cell_acceptance_predicate: "Returns ≥1 Layer-A variant outline AND specifies skill+path+frontmatter+edge concretely AND UC-9 architectural-proof-by-construction (filesystem-namespaced/cryptographic-scoping) AND UC-10 offline-first inference path AND dissents[] non-empty if peer integrators contradicted"
    primary_focus: "Compose Layer-A Variant candidate from engineering perspective; Karpathy++ vs filesystem-pure axis"

  - cell: engineering × scalability
    cell_id: 4
    wave: 4
    class: M
    ap_cost: 28000
    ap_budget: 45000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Parts 4, 6, 8)
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Part G)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-scalability-ingest-retrieval-horizon.md
    cell_acceptance_predicate: "Projects ≥3 Layer-A variants through all 5 gates (€50K/€200K/€1M/$100M/$1T); each gate row names physical failure + upgrade path + MHT event + BOSC-A-T-X trigger + Janus risk; offline-LLM hardware curve named per gate"
    primary_focus: "Karpathy pattern vs GraphRAG preprocessing vs HippoRAG PPR persistent-graph thresholds; offline LLM hardware (7B Q4 → 70B Q4 → MoE) per gate"

  - cell: mgmt × critic
    cell_id: 5
    wave: 1
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - prompts/km-architecture-research-2026-04-24.md (§3 esp UC-5/UC-6)
      - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1 layer 6 operations/, D11)
      - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md (Pillar 3, C-2)
      - decisions/JETIX-ARCHITECTURE-BRIEF.md (§4.7 dashboard)
      - .claude/agents/mgmt-expert.md
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Part E)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks against existing project scaffold (D1 Layer-6 operations/) for UC-5/UC-6/UC-7 AND PMBOK lifecycle alignment check AND ≥2 alternatives AND Anti-scope"
    primary_focus: "PMBOK Work lifecycle alignment; cadence rhythm vs Jetix reality (8 active projects, ≤20 active tasks rule); per-client project scaffold isolation"

  - cell: mgmt × optimizer
    cell_id: 6
    wave: 2
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
      - decisions/JETIX-ARCHITECTURE-BRIEF.md (§4)
      - .claude/agents/mgmt-expert.md
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Part E, F)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md
    cell_acceptance_predicate: "Returns minimal-scaffold proposal hitting UC-5 in ≤30min AND GTD weekly-review rhythm AND BASB CODE distillation workflow AND each delta WLNK/MONO/IDEM/COMM/LOC checked"
    primary_focus: "Minimal scaffold; GTD weekly-review; Cagan problem-over-solution; ≤30min onboarding constraint"

  - cell: mgmt × integrator
    cell_id: 7
    wave: 3
    class: M
    ap_cost: 35000
    ap_budget: 55000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
      - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1, D11)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md
    cell_acceptance_predicate: "Returns ≥1 Layer-B variant outline AND specifies cadence+handoff+stakeholder model AND aligns to Ruslan's 6 non-delegatable functions AND UC-9 per-client project scaffold isolation traced AND dissents[] non-empty if peer integrators contradicted"
    primary_focus: "Layer-B Variant from mgmt perspective; cadence + handoff; ≤20 active tasks discipline; per-client project scaffold isolation"

  - cell: mgmt × scalability
    cell_id: 8
    wave: 4
    class: M
    ap_cost: 28000
    ap_budget: 45000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-scalability-pm-horizon.md
    cell_acceptance_predicate: "Projects ≥3 Layer-B variants through 5 gates with project-count + agent-count + Ruslan-attention-budget per gate; named MHT events; Janus INT-excess risk per gate"
    primary_focus: "8 → 50 → 100 → 500 projects; Ruslan attention budget (≤20 active tasks) as Agency trigger; Mittelstand AI Alliance federation per Strategic Insight §3-§4"

  - cell: systems × critic
    cell_id: 9
    wave: 1
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - prompts/km-architecture-research-2026-04-24.md
      - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1, D3, D5)
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Parts 4, 8)
      - .claude/agents/systems-expert.md
      - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md (skim)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks against ontology spine (9 layers + 12 edges + 5 alphas) for Janus risk + weak-supplementation + ontology drift AND ≥2 alternatives AND Anti-scope; identifies federated-holon boundary as candidate UC-9 proof"
    primary_focus: "Janus failure modes; weak-supplementation per R-E §1.2 P.4; ontology drift; client-holon boundary as UC-9 architectural option"

  - cell: systems × optimizer
    cell_id: 10
    wave: 2
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
      - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1, D3, D5)
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Parts 4, 8)
      - .claude/agents/systems-expert.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md
    cell_acceptance_predicate: "Returns minimal ontological-spine extensions (or zero with justification) AND each delta with feedback-loop named AND requisite-variety check AND refuses on method-change"
    primary_focus: "Minimal extensions to 9 layers + 12 edges + 5 alphas; OR zero-extension justification; feedback loops surfaced concretely"

  - cell: systems × integrator
    cell_id: 11
    wave: 3
    class: M
    ap_cost: 40000
    ap_budget: 60000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Parts 4, 8)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
      - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md (full)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
    cell_acceptance_predicate: "Returns ≥2 layerA + ≥2 layerB variant outlines AND holarchy-mereology spec tying both AND federated-holon boundary as UC-9 proof option AND ≥4 distinct feedback loops named with Ashby requisite variety check AND dissents[] non-empty if peer cells contradicted"
    primary_focus: "Левенчук ШСМ Методология + Системная инженерия apex; swarm-holon ↔ project-holons ↔ expert-holons ↔ client-holon (UC-9 federated-holon boundary)"

  - cell: systems × scalability
    cell_id: 12
    wave: 4
    class: M
    ap_cost: 35000
    ap_budget: 55000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 6 BOSC-A-T-X, Part 8 holon, E-11 Janus)
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Part G)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-scalability-both-layers-horizon.md
    cell_acceptance_predicate: "Projects BOTH layers through all 5 gates with BOSC-A-T-X trigger per gate AND MHT Fission/Role-Lift/Fusion events named AND requisite-variety check AND federation per-client scaling per gate AND Janus degraded-mode spec for S-A excess + INT excess"
    primary_focus: "BOSC-A-T-X per gate; MHT events; requisite variety; Mittelstand AI Alliance federation scaling per gate"

  - cell: philosophy × critic
    cell_id: 13
    wave: 1
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - prompts/km-architecture-research-2026-04-24.md
      - decisions/JETIX-PHILOSOPHY.md (§§6, 10, 14)
      - decisions/JETIX-ARCHITECTURE-BRIEF.md (§4 F-G-R)
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Parts 4, 5, 9)
      - .claude/agents/philosophy-expert.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks for epistemic hygiene (falsifiability + multiple-alternatives + Anti-scope-explicit + supersession-chain) AND ≥2 alternatives AND Anti-scope; flags every 'works at scale' assertion as candidate-falsification target"
    primary_focus: "Popperian falsifiability on every 'scales' assertion; Anti-scope explicit; F-G-R discipline check; epistemic hygiene of client-isolated knowledge"

  - cell: philosophy × optimizer
    cell_id: 14
    wave: 2
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
      - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (E-5 F-G-R, E-9 DRR)
      - decisions/JETIX-ARCHITECTURE-BRIEF.md (§4)
      - .claude/agents/philosophy-expert.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md
    cell_acceptance_predicate: "Returns sharpened F-G-R tagging discipline AND 4-part DRR entry format AND supersession-chain invariants AND each delta WLNK/MONO/IDEM/COMM/LOC declared AND refuses on method-change"
    primary_focus: "F-G-R sharpening; DRR per-variant template; supersession-chain invariants"

  - cell: philosophy × integrator
    cell_id: 15
    wave: 3
    class: M
    ap_cost: 32000
    ap_budget: 50000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
      - decisions/JETIX-PHILOSOPHY.md (§§6, 10, 14)
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md
    cell_acceptance_predicate: "Returns epistemic-backbone overlay for both layers AND claim-validity gates AND contradiction-handling protocol AND universality test per JETIX-PHILOSOPHY §10 for each variant AND dissents[] preserved"
    primary_focus: "Epistemic backbone; universality test; contradiction-handling; meta-decision arbitration"

  - cell: philosophy × scalability
    cell_id: 16
    wave: 4
    class: M
    ap_cost: 25000
    ap_budget: 40000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-scalability-epistemic-horizon.md
    cell_acceptance_predicate: "Projects epistemic invariants through 5 gates AND names $1T-equivalent of peer-review AND research-programme hardcore per Lakatos AND epistemic integrity of client-isolated knowledge AND Janus risk per gate"
    primary_focus: "$1T peer-review equivalent; Lakatos hardcore; epistemic integrity of federated multi-client deployment"

  - cell: investor × critic
    cell_id: 17
    wave: 1
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - prompts/km-architecture-research-2026-04-24.md
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (§5 hosting paths)
      - decisions/ROY-INFORMATION-DIET.md (§1.6)
      - decisions/JETIX-ARCHITECTURE-BRIEF.md (§4)
      - .claude/agents/investor-expert.md
      - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Part G)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks on capital allocation AND margin-of-safety analysis on infrastructure migrations AND unit-econ check per page/per query AND per-client deployment cost for Path A/B/C AND Anti-scope"
    primary_focus: "Capital allocation; margin-of-safety; per-client deployment cost (Path A/B/C); unit-econ per page/query"

  - cell: investor × optimizer
    cell_id: 18
    wave: 2
    class: M
    ap_cost: 22000
    ap_budget: 35000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
      - .claude/agents/investor-expert.md
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md
    cell_acceptance_predicate: "Returns Kelly-like bet-sizing per gate-upgrade decision AND barbell construction across variants AND local-LLM inference cost-curve per client AND each delta WLNK/MONO/IDEM/COMM/LOC AND refuses on method-change"
    primary_focus: "Kelly bet-sizing per gate (BM25 G2 vs Neo4j G2 vs stay-filesystem G2); barbell across variants; local-LLM hardware cost-curve"

  - cell: investor × integrator
    cell_id: 19
    wave: 3
    class: M
    ap_cost: 32000
    ap_budget: 50000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (§3-§4 EISA)
      - decisions/ROY-INFORMATION-DIET.md (§1.6)
      - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md (full)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-integrator-moat-synthesis.md
    cell_acceptance_predicate: "Returns moat analysis across variants AND Private Library ROI AND knowledge compounding as intangible asset valuation AND Mittelstand AI Alliance EISA-moment valuation AND dissents[] preserved"
    primary_focus: "Moat synthesis; Private Library ROI; knowledge-as-intangible asset; EISA-moment network-effect valuation"

  - cell: investor × scalability
    cell_id: 20
    wave: 4
    class: M
    ap_cost: 28000
    ap_budget: 45000
    inputs:
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-integrator-moat-synthesis.md
      - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
      - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
      - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md (skim)
    expected_artefact: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-scalability-investment-horizon.md
    cell_acceptance_predicate: "Projects investment-fund mechanics through 5 gates AND named Private Library asset value crossover AND Token economy Option B (D23) tie-in at G3-G4 AND Mittelstand AI Alliance methodology-license vs per-client revenue stack per gate"
    primary_focus: "Investment-fund mechanics per gate; Private Library $10M/$100M asset value crossover; Mittelstand AI Alliance revenue model per gate"

## §3 Risk Register

risk_register:
  - risk_id: R1
    risk: "Scalability cells diverge on G4-G5 upgrade paths between experts"
    likelihood: high
    impact: medium
    mitigation: "Preserve as dissents per Cycle-1 precedent; brigadier handles in Phase 5 §12"

  - risk_id: R2
    risk: "Integrator cells produce label-only variants without concrete mechanics"
    likelihood: medium
    impact: high
    mitigation: "cell_acceptance_predicate explicitly demands skill+path+frontmatter+edge specificity; reject on insufficient concreteness; re-dispatch with stricter brief"

  - risk_id: R3
    risk: "UC-9 + UC-10 architectural-proof reduces to policy-claim ('Jetix admins careful')"
    likelihood: medium
    impact: critical
    mitigation: "Engineering-integrator + systems-integrator both required to produce named proof mechanism (filesystem-namespaced / cryptographic-scoping / federated-holon); reject on policy-only; iterate to drop variant if can't prove"

  - risk_id: R4
    risk: "Cells inadvertently propose touching legacy wiki/ v2 or 14 legacy agents"
    likelihood: low
    impact: high
    mitigation: "Each cell brief explicitly cites Anti-scope §9; brigadier validates at integration; reject any draft proposing legacy mods"

  - risk_id: R5
    risk: "Variant word-count floor (4500-5500w each) not met → shallow variants"
    likelihood: medium
    impact: high
    mitigation: "Brigadier Phase-5 self-audit per §13.2 V8 wc check; iterate on under-floor variants before gate emission"

## §4 Integration Strategy (post-W3 → variants)

After Wave 3, brigadier reads all 5 integrator drafts + 5 critic + 5
optimizer drafts. Inter-expert coherence sweep per §6.2:

- Engineering's Layer-A candidate vs Systems' Layer-A candidate → if
  diverge categorically (e.g., filesystem-pure vs ontological-layered),
  BOTH become candidate variants, axis identified.
- Mgmt's Layer-B candidate vs Systems' Layer-B candidate → same logic.
- Philosophy × integrator → epistemic backbone overlay validates UC-9
  isolation proof + UC-10 offline-first proof; flags policy-claims.
- Investor × integrator → moat-synthesis informs which variant best
  preserves knowledge-as-leverage at horizon.

Brigadier composes 6 variants on categorically different axes (per §2.2
+ §2.3 axis-of-differentiation rules):

**Layer-A axes (planned):**
- A1: Filesystem-resident, retrieval-lean, write-heavy (Karpathy++)
- A2: Pre-compiled-heavy, GraphRAG community-summaries
- A3: Federated typed-graph with HippoRAG PPR (or zero-hierarchy ZK
      surfing — to be decided post-W3 from cell signal)

**Layer-B axes (planned):**
- B1: Thin-scaffold high-autonomy (Layer-6 namespaces)
- B2: Rich-scaffold per-project mini-swarm (Cagan-problem-over-solution)
- B3: Adaptive-scaffold federated-per-project (Mittelstand AI Alliance
      prototype)

Final axis-selection happens after W3 returns. If cell signal points to
different categorical axes, brigadier follows the signal, NOT this plan.

## §5 Dispatch budget summary

- Total ap_cost: 25K + 22K + 35K + 28K + 22K + 22K + 35K + 28K + 22K +
  22K + 40K + 35K + 22K + 22K + 32K + 25K + 22K + 22K + 32K + 28K = 549K
- Total ap_budget: ~880K (1.6× ap_cost = standard buffer)
- Per-wave parallel dispatch: 4 brigadier-messages of 5 Task() calls each
- Brigadier integration + variant-drafting: ~150K turns
- Final consolidation + gate file: ~50K turns
- **Total estimated brigadier session burn: ~750K-1M turns** (Max-sub,
  no billing)

## §6 Side-effects on dispatch

- Per cell dispatch: append line to `swarm/logs/cyc-km-architecture-2026-04-24/events.md`
- Per cell return: append line to same events.md
- Per wave boundary: commit + push (per §8.3 Stage-Gated commit
  discipline)
- Per integration milestone: commit + push
- At gate emit: commit + push + HALT

— brigadier, 2026-04-24 01:50 CET
