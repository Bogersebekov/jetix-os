---
title: "Phase-2 WBS — KM Materialization MVP (matrix 5×4 decomposition)"
type: task-decomposition
id: T-km-materialization-mvp-2026-04-24-decomposition
cycle_id: cyc-km-materialization-mvp-2026-04-24
task_class: M
shape: combined-design-plus-scale-project      # cross-cutting materialization; design + scale-project lenses
chat_or_decompose: decompose                   # all 4 §3.0 predicates fire
decomposed_at: 2026-04-24
decomposed_by: brigadier
layer: root
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: decomposed
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§§2 + 7 + 13"}
  - {path: "prompts/swarm-launch-brigadier-km-materialization-2026-04-24.md", range: "§2 decomposition table"}
  - {path: ".claude/agents/brigadier.md", range: "§3.1 + §3.2 + §3.3 + §3.3.1 + §4.6"}
  - {path: "swarm/wiki/tasks/T-km-materialization-mvp-2026-04-24/intake.md"}
related:
  - "swarm/wiki/tasks/T-km-materialization-mvp-2026-04-24/intake.md"
  - "agents/brigadier/strategies.md"
binding_scope: task-T-km-materialization-mvp-2026-04-24
granularity: jetix-internal
---

# Phase-2 WBS — 16-cell decomposition across 3 waves + verification + gate

## §1 Decompose-or-Chat gate result (§3.0 predicates)

All 4 E-17 predicates fire:

- **P1 complexity > simple:** 30+ new files across 7 file trees; mini-swarm spawn logic; DSL evaluator; 10-UC integration.
- **P2 adversarial review required:** `philosophy × critic` mandated on SG predicate DSL (Hamel-binary discipline gate) per deep §2.C.6.
- **P3 horizon projection required:** stage-gates project through €50K–$1T trajectory per HD-01; quick-money kpi_targets reference the €50K Q2 2026 gate.
- **P4 multi-domain synthesis required:** company-as-code (Part D) synthesizes engineering + mgmt + systems + philosophy + investor lenses over every new artefact.

→ **Decompose.** Matrix invoked per §3.1 (open-ended synthesis → 10+ cells, hard cap 20).

## §2 Cell count + matrix activation

**Total cells: 14** (within 20-cap). **Modes used:** integrator (9), critic (3), optimizer (1), scalability (1). Matrix invariant 5×4=20 preserved at the definition level; this cycle activates 14 of the 20 possible (integrator-heavy by task shape).

**Weak-Supplementation floor:** 5 experts × ≥2 cells? Not strictly required across ALL experts (per brigadier §3.1). Activated: engineering (4), mgmt (3), systems (2), philosophy (2), investor (1), integrator-composite across Part D (implicit). Minimum-≥2-per-cycle floor trivially satisfied (14 > 2).

## §3 Cell table (OPP-04 compliant — every `cell_acceptance_predicate` non-trivial)

### Wave 1 — Parts A + B + C in parallel (4 cells)

```yaml
- cell: engineering × integrator                                # Part A owner
  class: M
  wave: 1
  ap_cost: 60000
  ap_budget: 90000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.A
    - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md#§§4-6
    - .claude/config/wiki-roots.yaml
    - .claude/skills/ingest.md
    - .claude/skills/ask.md
    - .claude/skills/consolidate.md
    - .claude/skills/build-graph.md
    - .claude/skills/lint.md
    - swarm/lib/shared-protocols.md#§§1-9
    - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md#D1-D8
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md
  cell_acceptance_predicate: "Draft covers A.1 wiki-roots clients: stanza (schema v2) + A.2 tools/bootstrap-demo-clients.sh (≤60 LoC, shebang + set -euo pipefail) + A.3 ≥50 typed edges plan + A.4 /ingest 6-source-type extension (youtube, pdf, md, web, voice, stdin) + A.5 /ask OFFLINE_MODE=1 Step-2.5 structured-excerpt path + A.7 /consolidate --weekly + A.8 /build-graph Louvain communities.jsonl + A.9 /lint 5 new signals (L-DANGLING-EDGE, L-ORPHAN-CONCEPT, L-MISSING-FRONTMATTER, L-DUPLICATE-SLUG, L-CROSS-CLIENT-GLOBAL). Each skill extension includes complete bash snippet or MD body block promotable by brigadier. Draft body grep match for 'schema_version: 2' AND 'OFFLINE_MODE' AND 'Louvain' AND 'L-DANGLING-EDGE' AND 'yt-dlp' must all return non-zero."

- cell: mgmt × integrator                                       # Part B owner
  class: M
  wave: 1
  ap_cost: 50000
  ap_budget: 80000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.B
    - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md#§§4-6
    - decisions/JETIX-VISION.md#§§7.1-7.2
    - decisions/JETIX-PLAN.md#§§3.1-3.9
    - .claude/agents/brigadier.md                          # parent of project-brigadier template
    - swarm/lib/shared-protocols.md
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partB-b2-mini-swarm-bundle.md
  cell_acceptance_predicate: "Draft provides full text of .claude/config/project-types.yaml (schema v1; 4 types consulting/research/product/bets with default_experts + default_stage_gates + default_kpi_targets + required_frontmatter_fields + promotion_rules) + full /project-bootstrap skill body + full .claude/agents/project-brigadier.md template (with {{SLUG}} placeholders) + 4 scaffold template directories' _moc.md contents (project-consulting, project-research, project-product, project-bets) + /project-review + /project-archive skill bodies + /lint L-PROJECT-MISSING-REQUIRED-FRONTMATTER extension. Every required_frontmatter_fields enum must include problem_statement, kill_criteria, kpi_targets, project_type, priority, state, pmbok_phase, granularity. Grep body for 'problem_statement' AND 'kill_criteria' AND 'kpi_targets' AND 'project-types.yaml' AND 'project-brigadier' AND 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' returns non-zero for all 6."

- cell: systems × integrator                                    # Part C owner
  class: M
  wave: 1
  ap_cost: 35000
  ap_budget: 60000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.C
    - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md#§§4.2-4.9
    - swarm/lib/shared-protocols.md
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-systems-integrator-partC-stage-gates-merged.md
  cell_acceptance_predicate: "Draft provides full /lint --check-stage-gates algorithm (including SG-status annotation schema in _moc.md) + full tools/stage-gate-eval.py DSL evaluator (≤120 LoC, deterministic, offline, supporting count(glob), count(glob:marker), metric>=N, AND/OR compound) + auto-spawn protocol per project-types.yaml.promotion_rules + /project-de-morph skill body (including ≥50-LoC user-content HITL guard) + /project-promote skill body (bets→consulting|research|product; SG-4 gate) + philosophy-expert critic wiring for new SG predicate validation (non-binary/ambiguous reject path). Grep body for 'stage_gate_number' AND 'de-morph' AND 'promotion_rules' AND 'spawned_paths' AND 'Hamel-binary' returns non-zero for all 5."

- cell: philosophy × critic                                     # Part C SG-predicate-rigor gate
  class: M
  wave: 1
  ap_cost: 20000
  ap_budget: 40000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.C.6
    - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md
    - .claude/agents/philosophy-expert.md
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-philosophy-critic-sg-predicate-rigor.md
  cell_acceptance_predicate: "Draft returns ≥5 binary Conformance Checks verifying each of project-types.yaml default_stage_gates predicates is Hamel-binary (falsifiable, no subjective adjectives, no 'when it feels important'-style) + anti-regex list of 10+ banned phrases (e.g., 'when ready', 'if meaningful', 'appropriate quality', 'good enough', 'mature enough') that /lint --check-stage-gates --validate-predicate MUST reject + explicit (F, ClaimScope, R) triple per check + ≥2 Alternatives + Anti-scope. If ANY default_stage_gate fails Hamel-binary test, cell returns escalations[]{trigger: rephrase-required, target: 'project-types.yaml.types.<type>.default_stage_gates.<SG>'}."
```

### Wave 2 — Part D cross-cutting (serial after Wave 1 integration, 1 cell + implicit per-expert pass-through)

```yaml
- cell: engineering × integrator                                # Part D owner (/company-status + /knowledge-diff)
  class: M
  wave: 2
  ap_cost: 25000
  ap_budget: 40000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.D
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md    # Wave-1 self-reference
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partB-b2-mini-swarm-bundle.md         # Wave-1 peer reference
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-systems-integrator-partC-stage-gates-merged.md        # Wave-1 peer reference
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partD-company-as-code.md
  cell_acceptance_predicate: "Draft provides full /company-status skill body (output ≤80 lines; derives every field from local git + filesystem reads; zero network; zero external deps) + full /knowledge-diff skill body (git log --since --until parameters; Added/Modified/Deleted classification; aggregate-by-niche output) + CLAUDE.md delta-block text for post-materialization 'KM MVP (2026-04-<XX>) — what changed' + 'KM MVP quick ops' sections. Additionally: before/after snapshot table identifying every skill (ingest/ask/consolidate/build-graph/lint/project-bootstrap/project-review/project-archive/project-de-morph/project-promote/company-status/knowledge-diff) and its company-as-code compliance (config-driven / git-provenance-clean / no-hardcoded-jetix-paths). Grep for 'company-status' AND 'knowledge-diff' AND 'git log --since' AND 'no hardcoded' returns non-zero."
```

### Wave 3 — Part E real-work bootstrap (serial after Wave 2; 3 cells + 1 dissent-preservation integrator)

```yaml
- cell: mgmt × integrator                                       # Part E owner (quick-money + levenchuk bootstrap)
  class: M
  wave: 3
  ap_cost: 40000
  ap_budget: 65000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.E
    - decisions/JETIX-VISION.md#§§7.1-7.2
    - decisions/JETIX-PLAN.md#§§3.1-3.9
    - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partB-b2-mini-swarm-bundle.md
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partE-quick-money-levenchuk-bootstrap.md
  cell_acceptance_predicate: "Draft provides full body text of swarm/wiki/operations/quick-money/{_moc.md, icp.md, pipeline.md, history.md, decisions.md, open-questions.md, offline-inference-spec.md} with real content (problem_statement as one-paragraph Cagan frame citing JETIX-PLAN §3.1; kill_criteria Hamel-binary with absolute date 2026-07-24; kpi_targets leads_per_quarter:20 contracts_per_quarter:2 mrr_eur_target_q2_2026:15000 cumulative_revenue_q2_2026_eur:50000 per JETIX-PLAN D3; icp.md populated verbatim from JETIX-VISION §§7.1-7.2 5 criteria + selected archetypes) + full body text of swarm/wiki/operations/levenchuk-deep-dive/{_moc.md, history.md, open-questions.md} adaptive 3-file baseline with bets-style stage_gates declared + .claude/agents/{quick-money-brigadier.md, levenchuk-deep-dive-brigadier.md} instantiated from project-brigadier template with correct default_experts (consulting→mgmt+sales-researcher; research→systems+philosophy). Grep for 'Mittelstand' AND 'Startupper' AND '2026-07-24' AND '€50' AND 'Левенчук' returns non-zero for all 5."

- cell: investor × critic                                       # Part E ICP + KPI realism gate
  class: M
  wave: 3
  ap_cost: 18000
  ap_budget: 35000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§2.E.1-E.2
    - decisions/JETIX-VISION.md#§7
    - decisions/JETIX-PLAN.md
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partE-quick-money-levenchuk-bootstrap.md
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-investor-critic-icp-kpi-realism.md
  cell_acceptance_predicate: "Draft returns ≥5 binary Conformance Checks on quick-money _moc.md + icp.md: (1) kpi_targets arithmetic consistent with €50K Q2 2026 gate (leads×contract_rate×avg_deal_size crosses target); (2) Path B vs Path C hosting path call explicit + gross-margin arithmetic (€3K onboarding + €15K/yr = 70.7% GM yr1 per Strategic Insight §5 + Dissent D-3); (3) 11 archetypes filtered to Phase-1 buyers justified by upward-direction criterion; (4) kill_criteria date 2026-07-24 not aspirational — triangulated with weekly outreach volume and conversion funnel; (5) levenchuk-deep-dive kpi leaves P3 (research) flexibility without 'optional empty'. ≥2 Alternatives + Anti-scope. (F, ClaimScope, R) per check. Dissent preservation: if draft-E disagrees with §5 Strategic Insight on Path B/C, preserve both with F-G-R."

- cell: engineering × optimizer                                 # Part E end-to-end demo (measurable baseline)
  class: M
  wave: 3
  ap_cost: 15000
  ap_budget: 30000
  inputs:
    - prompts/km-materialization-mvp-execution-2026-04-24.md#§§2.E.4 + §3 UC-INGEST-1 + UC-ASK-1
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-optimizer-e2e-demo-deltas.md
  cell_acceptance_predicate: "Draft provides before/after snapshot table for E.4 end-to-end demo (before: /ingest URL → N concepts K edges; after: /ask synthesized answer with ≥3 [src:...] citations + 1 comparison file + 1 history.md insight entry) with WLNK/MONO/IDEM/COMM/LOC invariants declared (apply/preserve) + 1-paragraph `method-change=false` attestation + fixture path for hermetic re-run under swarm/tests/fixtures/km-mvp/. No new ingest source types proposed (that is Part A territory; optimizer mode forbids method-change per §4.6). Grep for 'WLNK' AND 'MONO' AND 'IDEM' AND 'COMM' AND 'LOC' AND 'method-change=false' returns non-zero for all 6."
```

### Wave 4 — Verification sweep (1 cell; pre-gate consolidation)

```yaml
- cell: systems × scalability                                   # 5-horizon projection on the whole MVP
  class: M
  wave: 4
  ap_cost: 30000
  ap_budget: 50000
  inputs:
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partB-b2-mini-swarm-bundle.md
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-systems-integrator-partC-stage-gates-merged.md
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partD-company-as-code.md
    - swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partE-quick-money-levenchuk-bootstrap.md
    - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§11 trajectory
  expected_artefact: swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-systems-scalability-5-gate-projection.md
  cell_acceptance_predicate: "Draft projects the MVP substrate through 5 horizon gates (€50K Q2 2026 / €200K / €1M / $100M / $1T per HD-01). For each gate: BOSC-A-T-X trigger predicates + MHT events named + Janus degraded-mode spec for (a) brigadier overload under mini-swarm proliferation (Self-Assertive excess) and (b) brigadier deference to mini-swarms (Integrative excess) + explicit migration trigger from A1↔B1 Phase-A to A2↔B2 Phase-B (per trajectory §11). Binary recovery predicate per gate. Grep for '€50K' AND '€200K' AND '€1M' AND '$100M' AND '$1T' AND 'Janus' AND 'migration trigger' returns non-zero for all 7."
```

### Wave 5 — Per-expert learning + gate packet (brigadier-direct, NOT Task() dispatched)

This wave is executed by brigadier inline (no new cells) to honor §3.1–3.3
of the launch prompt: gate-learning + per-expert learnings + emergent
insights captured IN-FLIGHT, then Part F AWAITING-APPROVAL packet written.

- Brigadier writes gate-learning entries to `agents/brigadier/strategies.md`
  per Part completion (A, B, C, D, E, F).
- Each expert's `writing-support` extraction (from their own Wave drafts)
  is composed by brigadier into `swarm/wiki/meta/agent-improvements/<expert>-2026-04-<XX>.md`.
- Emergent insights surfaced during gate promotion are written to
  `swarm/wiki/insights/<slug>-2026-04-24.md` as full concept pages.

## §4 Dispatch sequencing (timeline)

```
t=0           : Write intake.md + decomposition.md (this file); commit; push.
t+1 (Wave 1)  : Dispatch 4 cells in parallel (eng×integrator-A, mgmt×integrator-B, sys×integrator-C, phil×critic-SG).
                Single message, 4× Task() calls per brigadier §4.3.
                Expected elapsed: drafts land in expert sandboxes; brigadier reads, runs §5.5.5 gate.
t+2           : Promote Wave-1 drafts → canonical wiki + .claude/* paths.
                Commit per Part (3 separate commits: Part A, Part B, Part C).
                Write gate-learning entries for Parts A/B/C in strategies.md.
                Write expert learnings for engineering/mgmt/systems/philosophy.
t+3 (Wave 2)  : Dispatch 1 cell (eng×integrator-D).
                Integrate + promote. Part D commit. Gate-learning. Engineering expert second learning entry.
t+4 (Wave 3)  : Dispatch 3 cells in parallel (mgmt×integrator-E, investor×critic, eng×optimizer).
                Integrate with dissent preservation (investor critique may disagree with mgmt bootstrap).
                Promote. Part E commit. Gate-learning. mgmt + investor + engineering learnings.
t+5 (Wave 4)  : Dispatch 1 cell (sys×scalability — 5-gate projection).
                Promote. Gate-learning. systems second learning entry.
t+6 (Part F)  : Run verification suite. Write swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>.md.
                Commit + push. HALT.
t+∞ (Part G)  : Resume ONLY after Ruslan ack. Write decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md
                (≥3000w) + 4 × 4-part DRR + 5 × agent-improvements finalization + cycle-archive.
                Compound complete.
```

## §5 Pre-dispatch checklist per cell (OPP-02 fallback discipline)

Before each `Task()` invocation brigadier verifies:
1. `ap_cost` + `ap_budget` are non-zero integers (present in §3 table).
2. `expected_artefact` glob matches `swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-*`
   (write-scope-guard OPP-02).
3. `cell_acceptance_predicate` length 20–∞ chars, no "artefact exists" /
   "returns output" / "file is non-empty" anti-regex matches (OPP-04 check #13).
4. Mode prefix present on first non-blank line of prompt (§4.2 mandate).
5. Inputs list is paths only, NOT inlined content (AP-1 prevention).

## §6 Cell-acceptance-predicate audit

All 10 cells carry non-trivial predicates per OPP-04. Sample grep on
this file:

```bash
grep -c 'cell_acceptance_predicate:' swarm/wiki/tasks/T-km-materialization-mvp-2026-04-24/decomposition.md
# expected: 10

grep -E 'artefact exists|file is non-empty|returns output' swarm/wiki/tasks/T-km-materialization-mvp-2026-04-24/decomposition.md
# expected: zero matches (anti-regex clean)
```

## §7 Risk register (from intake §6 + cycle-specific)

| Risk | Mitigation in WBS |
|---|---|
| Drafts too large → §5.5.5 gate latency | Each cell's expected_artefact scoped to one Part; not a monolithic draft |
| Peer-input-needed cascade Wave 1 → Wave 3 | Wave ordering respects dependencies (Part B needs no Part A runtime — only spec; Part E needs Parts A+B promoted) |
| Dissent between mgmt-E and investor-critic | Brigadier integrates with dissent preservation per §5.5; dissents carry (F, ClaimScope, R) triples |
| HD-02 N=3 confusion | Counter `m_class_dispatched_this_cycle` explicitly managed; overflow path per §3.3.1 |
| OPP-02 mode-prefix hook missing | Fallback Alt-B log-only; cycle-2 landed; brigadier runs `.claude/hooks/mode-prefix.sh` inline if present |

## §8 Side-effects performed at decomposition

1. This file written.
2. `swarm/logs/cyc-km-materialization-mvp-2026-04-24/events.md` opened with frontmatter + header (next step).
3. `swarm/wiki/log.md` receives `task-decomposed` entry at commit time.
4. `swarm/mailboxes/brigadier.jsonl` (operational log; append-only; created at dispatch).

α-1 transitions `intaked → decomposed` on commit of this file.
