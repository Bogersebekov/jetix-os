---
title: Edge Type Enum
type: edge-template
layer: spine
state: accepted
confidence: high
last_reviewed: 2026-04-23
sources: [{path: "decisions/WIKI-V3-MECHANICS-2026-04-23.md", range: "216-237"}]
---

# Edge Type Enum (v3)

This file is the SINGLE SOURCE OF TRUTH for typed cross-references in
the v3 wiki. `/build-graph`, `/ingest`, `/lint`, and `/ask` Tier-3
typed-BFS retrieval all read from this enum. Adding or modifying an
edge type requires AWAITING-APPROVAL escalation (D6 §4).

## Storage

- **Intra-v3 edges** → append to `swarm/wiki/graph/edges.jsonl`,
  one JSONL record per line.
- **v3 → v2 cross-tree edges** → append to
  `swarm/wiki/graph/cross-tree.jsonl`, same record shape.
- **Record shape**: `{"from": "<path>", "to": "<path>",
  "type": "<edge-type>", "ts": "YYYY-MM-DD",
  "confidence": "low|medium|high", "note": "<optional>"}`.

## Intra-layer types (9 intra-layer — §3.2.1..§3.2.9)

### 1. `extends` (N:1, directed; inverse `extended_by`)
- Definition: Page A refines/expands page B; A is more specific treatment.
- Allowed from/to: spine entity-type (concepts, claims, topics, foundations); Layers 1, 2, 3, 7.
- Lint: no cycles (DAG); flag if `from.layer != to.layer`.
- Example: `{"from":"concepts/llm-wiki","to":"concepts/karpathy-llm-wiki","type":"extends","ts":"2026-04-23","confidence":"high"}`

### 2. `contradicts` (N:M, bidirectional; inverse self)
- Definition: Page A explicitly conflicts with claim/conclusion in B.
- Allowed: claims, foundations, concepts, experiments.
- Lint: both directions present; both pages bear `stance: contested|refuted`.
- Example: `{"from":"claims/embeddings-required","to":"claims/embeddings-deferred","type":"contradicts","ts":"2026-04-23","confidence":"medium"}`

### 3. `supports` (N:M, directed; inverse `supported_by`)
- Definition: Page A provides evidence for claim in B.
- Allowed from: sources, experiments, claims. Allowed to: claims, concepts, foundations.
- Lint: target `support_count` ≥ incoming supports edges.
- Example: `{"from":"sources/2026-04-19-knowledge-arch","to":"claims/4-tier-retrieval","type":"supports","ts":"2026-04-23","confidence":"high"}`

### 4. `inspired_by` (N:M, directed; inverse `inspired`)
- Definition: Creative lineage — idea A inspired by B; looser than extends.
- Allowed from/to: primarily ideas; also experiments, concepts.
- Lint: none blocking; surfaced in /build-graph community detection.
- Example: `{"from":"ideas/swarm-as-memory","to":"ideas/karpathy-llm-wiki","type":"inspired_by","ts":"2026-04-23","confidence":"medium"}`

### 5. `tested_by` (N:M, directed; inverse `tests`)
- Definition: Claim A was empirically tested by experiment B.
- Allowed from: claims, foundations. Allowed to: experiments.
- Lint: experiment must have outcome ∈ {won, lost, aborted} for tests direction; flag open outcome >30d with tested_by ≥1.
- Example: `{"from":"claims/4-tier-retrieval","to":"experiments/2026-05-15-tier3-bfs-benchmark","type":"tested_by","ts":"2026-04-23","confidence":"high"}`

### 6. `invalidates` (N:M, directed; inverse `invalidated_by`)
- Definition: Experiment/evidence B invalidates claim A.
- Allowed from: experiments, sources, claims. Allowed to: claims, foundations.
- Lint: auto-marks `to` page `stance: refuted`; warn if `to` is accepted and not `superseded_by` within 7 days.
- Example: `{"from":"experiments/2026-05-15-tier3-bfs-benchmark","to":"claims/embeddings-required","type":"invalidates","ts":"2026-05-16","confidence":"high"}`

### 7. `supersedes` (N:1, directed new→old; inverse `superseded_by` ALSO stored bidirectionally)
- Definition: New page A replaces older B (often paired with state: superseded on B).
- Allowed from/to: same layer, same type.
- Lint: supersession DAG (no cycles); B bears `state: superseded` and `superseded_by: [[A]]`; A's `supersedes_versions:` includes B.
- Example: `{"from":"foundations/swarm-alphas-v2","to":"foundations/swarm-alphas-v1","type":"supersedes","ts":"2026-04-23","confidence":"high"}`

### 8. `derived_from` (N:M, directed derived→source; inverse `derives`)
- Definition: Source S was used to derive concept/claim/idea P.
- Allowed from: concepts, claims, ideas, summaries, foundations. Allowed to: sources.
- Lint: pages with pipeline ∈ {compiled,linted,ready} AND state ∈ {accepted,referenced} must have ≥1 derived_from OR supports edge OR tier: foundation.
- Example: `{"from":"concepts/4-tier-retrieval","to":"sources/2026-04-19-knowledge-arch","type":"derived_from","ts":"2026-04-23","confidence":"high"}`

### 9. `part_of` (N:1 part→whole, directed; inverse `has_part`) — formalised per Q3
- Definition: Mereological — page A is part of composite B. Dominant v2 edge (233/572 records).
- Allowed from: any spine entity-type. Allowed to: topics (hub→children), foundations (sub → over).
- Lint: target must be topics/<slug>-hub.md OR foundations/ page; re-route otherwise; no cycles (mereology DAG).
- Example: `{"from":"concepts/4-tier-retrieval","to":"topics/retrieval-hub","type":"part_of","ts":"2026-04-23","confidence":"high"}`

## Cross-layer types (3 — §3.2.10..§3.2.12)

### 10. `alpha-ref` (1:1, directed wiki→alpha; inverse `tracked_by` on alpha side)
- Definition: Wiki entity links to alpha tracker (W-1 §D.3).
- Allowed from: entities (spine), agents/<expert>/ (L3), themes/<theme>/ (L1).
- Allowed to: tasks/<task-id>/ (α-1), operations/<project-slug>/ (α-4 composite), swarm/wiki/foundations/swarm-alphas.md.
- Lint: target must exist; flag entities without alpha-ref when entity_type ∈ {company, product, team} AND state ∈ {accepted, referenced}.
- Example: `{"from":"entities/acme-corp","to":"tasks/task-01HF2K3M5N7P9Q","type":"alpha-ref","ts":"2026-04-23","confidence":"high"}`

### 11. `layer-ref` (N:M, directed; inverse `layer-back-ref` derivative)
- Definition: Generic cross-layer link when no specific edge fits. Lower priority than alpha-ref and cross-tree-ref.
- Allowed from/to: any distinct v3 layer pair.
- Lint: "consider more specific edge type" notice when a specific edge matches the from/to pair.
- Example: `{"from":"themes/engineering/concepts/clean-code","to":"global/solved-patterns/test-driven-refactor","type":"layer-ref","ts":"2026-04-23","confidence":"medium"}`

### 12. `cross-tree-ref` (N:M, directed v3→v2 only; no inverse recorded)
- Definition: v3 page citing v2 page (Q9 bridge). v3 → v2 only.
- Allowed from: any v3 page. Allowed to: any v2 page.
- Storage: `swarm/wiki/graph/cross-tree.jsonl` (NOT edges.jsonl).
- Lint: reject `to` under swarm/wiki/ (use layer-ref); reject `from` under v2 wiki/; presence in cross-tree.jsonl mandatory; forbidden in edges.jsonl.
- Example: `{"from":"themes/engineering/concepts/clean-code","to":"wiki/concepts/clean-code","type":"cross-tree-ref","ts":"2026-04-23","confidence":"high","note":"v3 distillation cites v2 baseline"}`

## From-layer × to-layer × allowed types matrix (§3.3)

Rows = `from` layer; columns = `to` layer. Empty cell = rejected by /lint.

Layer abbreviations: **S** = spine entity-type; **L1**=themes;
**L2**=brigadier; **L3**=agents; **L4**=meta/agent-improvements;
**L5**=tasks; **L6**=operations; **L7**=global; **L8**=skills;
**L9**=insights; **v2**=`wiki/`.

| from \ to | S | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | v2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **S**  | extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, derived_from, part_of | layer-ref | layer-ref | layer-ref | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | layer-ref | cross-tree-ref |
| **L1** | layer-ref | extends, contradicts, supports, derived_from, part_of, supersedes | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | cross-tree-ref |
| **L2** | layer-ref | layer-ref | extends, supersedes, part_of | layer-ref | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | — | cross-tree-ref |
| **L3** | layer-ref | layer-ref | layer-ref | extends, derived_from, part_of, supersedes | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | — | cross-tree-ref |
| **L4** | layer-ref | layer-ref | layer-ref | layer-ref | extends, supersedes | — | — | layer-ref (`promoted_to`) | layer-ref | — | cross-tree-ref |
| **L5** | derived_from, supports, part_of | — | — | — | — | extends, supersedes, contradicts | layer-ref | — | — | — | — |
| **L6** | layer-ref | — | — | — | — | layer-ref | extends, supersedes, part_of | layer-ref | — | — | cross-tree-ref |
| **L7** | layer-ref | layer-ref | layer-ref | layer-ref | — | — | — | extends, contradicts, supports, supersedes, part_of, derived_from | layer-ref | — | cross-tree-ref |
| **L8** | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | — | — | layer-ref | extends, supersedes, part_of | — | cross-tree-ref |
| **L9** | layer-ref (Phase B) | layer-ref (Phase B) | — | — | — | — | — | layer-ref (Phase B) | — | extends (Phase B) | cross-tree-ref (Phase B) |
| **v2** | — | — | — | — | — | — | — | — | — | — | (intra-v2; not managed by v3) |

Phase-A specifics: L9 cells marked "(Phase B)" are rejected in Phase A
per `phase_a_lock: true`.

`addresses_gap` dropped per `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`
§3.1 lines 886-893 (the wiki-v3 architecture spec's own internal
critic-gate1 H4 finding, NOT the Шаг 2.2.4 critic-gate1 finding) —
gap-clearing semantics absorbed by `derived_from` + `/lint` orphan-detection
signal.
