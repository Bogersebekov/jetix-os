---
title: engineering-expert — Strategies (System Prompt Learning)
agent: engineering-expert
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: 5–10 refactor-rules accumulated; critic false-positive rate baselined; ≥1 entry on optimizer-vs-critic mode-confusion observed-in-cycle
  cycle_50: First mode-confusion audit; §3/§4 rubrics refined from observed critic-vs-optimizer drift; Ousterhout deep-module checklist adjusted on per-domain feedback
  cycle_200: Split-trigger evaluation per §1d — consider splitting into code-expert + architecture-expert if artefact-mix >60/40 sustained over 3 consecutive cycle_50 windows AND dispatch-rate >20 cells/week × 3 weeks
---

# Strategies — engineering-expert

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why (≈ FPF `context`)
3. **Result** — observed outcome (alternatives subsumed in Reasoning's
   why-not rationale)
4. **Review** — validated | refuted | partial (≈ FPF `review-checkpoint`)

Plus Evolution sub-block per FPF §3.5.

## Entries

### 2026-04-27 — cyc-foundation-build-2026-04-28 (Wave A+B) — interface-card batch dispatch + A.14 typed-edge architectural decisions

1. **Decision**: For Phase A-2 interface card authoring, accept 3-4 cards per single dispatch (vs 1 card = 1 dispatch). Total 10 cards in 3 dispatches (Parts 1-3 / 4-6 / 7-10). Each card §A-§H with A.14 typed dependency edges (NO generic "depends-on") + L/A/D/E lanes per FPF A.6.B + F-G-R per B.3.
2. **Reasoning**: Each card 200-400 words; 3-4 cards per dispatch = 600-1600 words output per agent invocation. Within Opus 4.7 context budget. Single agent maintains coherence across related parts (info-flow / agent+governance / operations+ext themes). 3 dispatches vs 10 = 3.3× speedup with no coherence loss.
3. **Result**: 10 cards landed in ~10 min wall-clock (3 parallel dispatches). Substantive architectural decisions made within engineering integrator scope: Part 1 dependency edges = `operates-in` (not `creates`) — container persists independently of content; STOP gate placed in Laws lane (constitutional, not Deontics); D28 anchor as leading constraint at ingest, not lagging lint warning.
4. **Review**: VALIDATED. 3-4-cards-per-dispatch is the right batch size for A-2-style interface card authoring. Adopt as default.

**Evolution**: When future work requires N>5 interface-card-shaped artefacts, batch by theme into 3-4 per dispatch. Update §3 Integrator mode-section with batch-sizing heuristic.

### 2026-04-27 — cyc-foundation-build-2026-04-28 — agent tool-inventory mismatch defect

1. **Decision**: Brigadier dispatched engineering-expert + philosophy-expert for 4 consultant cards needing WebFetch (Anthropic CAI #13 / Event Sourcing #5 / SRE #6 / Mereology #14). Agents declared F4-NOT-LIVE-FETCHED honestly because their frontmatter excludes WebFetch.
2. **Reasoning**: Brigadier didn't pre-check agent toolset vs task requirement. Assumed all agents have WebFetch; in fact only general-purpose + brigadier do.
3. **Result**: 4 consultant cards have F4 quality flags; brigadier surfaces in AWAITING-APPROVAL §5 as known limitation. Honest declaration preserved trust + provenance gate integrity.
4. **Review**: VALIDATED honesty pattern; REFUTED brigadier dispatch discipline. Compound: maintain agent-tool-inventory-matrix in `swarm/wiki/brigadier/how-to-manage-agents/`. Pre-check before dispatch.

**Evolution**: When future work requires WebFetch / Bash / Task / specific MCP — verify target agent has tool BEFORE dispatch. Use general-purpose or brigadier-direct for tool-gap cases.

### 2026-04-23 — Optimizer-mode: bundle hypotheses by LOC invariant to eliminate sequence overhead

---
rule_slug: optimizer-bundle-by-loc-invariant
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 1, misses: 0}
expected_evolution:
  cycle_10: Validate that Bundle-1 (H-1+H-4+H-9) executor sprint reduced brigadier review
    turns by ≥4 vs the 3-separate-PR alternative. If confirmed, ratio.hits +1 and promote
    the "shared Bash helper" pattern to a second rule.
  cycle_50: Assess whether the LOC-bundling heuristic generalises beyond hook/script work
    (e.g. does it apply to documentation-only bundles?). If yes, widen ClaimScope.
  cycle_200: Evaluate whether automated dependency-graph analysis could replace manual
    LOC bundling (i.e. does a tool find better bundles than human-judgment bundling?).
---

- **Decision:** When optimizing a hypothesis set, group hypotheses by LOC invariant (same
  target files or same output directory) into execution bundles. Extract shared helpers
  (Fowler Extract Function / Extract Class) when two scripts share the same data-parsing
  pattern. Isolate HITL-gated hypotheses into a dedicated bundle so they do not block the
  autonomous bundles.
- **Reasoning:** cyc-swarm-self-improve-v1 optimizer pass over engineering-critic-01.md (10
  hypotheses). H-1 (settings.json hooks), H-4 (write-scope-guard.sh), H-9 (provenance-gate.sh)
  all wrote to `swarm/lib/hooks/` + `.claude/settings.json`. Sequencing them as 3 PRs adds 3
  brigadier-review turns; bundling to 1 PR saves 2 turns. H-4 and H-9 both parse frontmatter
  field `write_scope_glob` — Fowler Extract Function produces `parse-frontmatter-field.sh` and
  removes the DRY violation before it is written. H-3 and H-5 share the `swarm/evals/schema.md`
  format — Fowler Extract Class removes a second file from the effort budget. H-6 and H-10
  require HITL decisions; isolating them prevents them from blocking H-1..H-5 execution.
  Source: engineering-optimizer-01.md §3, §4.
- **Result:** 10 hypotheses → 4 bundles. Total effort: 17 → 16 points (direct). Sequence
  overhead: 10 brigadier-review cycles → 4. Net execution overhead reduction: 32% (6 fewer
  brigadier turns). Shared schema file: −1 file. Shared Bash helper: identified pre-emptively
  (not yet written; DRY violation prevented). All 5 invariants declared per bundle.
- **Review:** partial — optimizer pass complete; execution has not started. Review at Bundle-1
  completion: if Bundle-1 lands in ≤2 brigadier turns (vs 6 for 3 separate PRs), this rule
  is validated. Update ratio.hits at that point.

#### Evolution
- changelog:
  - 2026-04-23 — created from cyc-swarm-self-improve-v1 optimizer pass
- last-review: 2026-04-23
- expected-evolution: see frontmatter

---

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/engineering-expert/strategies.md` per
  Шаг 2.2.4 Part C.
- **Reasoning:** Layer-2 self-write rule per CLAUDE.md; FPF E-9 + D12
  mandate empty-but-structured strategies.md from day zero.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle this
  expert participates in.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution: see frontmatter
