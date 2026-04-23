---
title: Wiki v3 Overview
type: overview
updated: 2026-04-23
---

# Swarm Wiki v3 — Overview

## Tree

See `swarm/wiki/index.md` for the full tree manifest. The canonical
ASCII layout is mirrored in
`design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D1 §1.2.

Layers (1..9) plus the spine entity-types
(concepts/entities/sources/topics/claims/ideas/experiments/summaries) and
the `foundations/` axiomatic root organise every page. Read
`swarm/wiki/foundations/swarm-alphas.md` for the five state machines
that govern lifecycle of every Task / Artefact / Strategies-Rule /
Cycle / Direction.

## Five principles (W-11 cognitive infrastructure framing)

1. **Single-writer brigadier (Q2).** Experts return drafts via Task; the
   brigadier promotes after the §5.5.5 provenance gate. No cell mutates
   canonical wiki state directly.
2. **Triple-channel cross-refs (Q3).** YAML `related[]` + inline
   `[[type/slug]]` + `graph/edges.jsonl`. `/lint` enforces consistency
   across all three channels.
3. **4-tier retrieval (Q1).** Direct path → index+grep → typed-BFS over
   `graph/edges.jsonl` → bounded long-context fallback. Embeddings
   deferred to Phase B; re-evaluate when FPAR < 0.80.
4. **Provenance gate (D6 §2).** Every wiki write cites at least one
   source artefact; foundations require ruslan-attested or
   brigadier-attested-with-≥3-supports.
5. **9 layers + global spine.** Drop `swarm/strategies/` (T5/R6).
   `agents/<expert>/strategies.md` is the per-agent personal-memory
   layer; cross-agent improvements live in
   `swarm/wiki/meta/agent-improvements/` (brigadier-write).

## Niches (per-agent slice symlinks)

| Niche | Symlinks into |
|---|---|
| personal | (per-agent population in Phase B) |
| business | … |
| sales | … |
| life | … |
| tech | … |
| meta | … |

The 6-niche enum is locked in `CLAUDE.md` line 70. No `global` niche
(Layer 7 holds promoted patterns under `swarm/wiki/global/`).

## Pipeline statuses

`raw → ingested → compiled → linted → ready` (carried from v2; D2
frontmatter `state` field is α-2 lifecycle, distinct from `pipeline`).

## Coexistence with v2

The v2 wiki at `wiki/` is read-write through Phase A. The v2↔v3 bridge
is the `cross-tree-ref` edge type (D3 §3.2.12), v3→v2 only, stored in
`swarm/wiki/graph/cross-tree.jsonl`. No v2 file is mutated as part of
Шаг 2.2.4 wiki-v3 bootstrap.
