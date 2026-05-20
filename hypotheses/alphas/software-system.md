---
alpha: software-system
date: 2026-05-20
F: F2
G: hypotheses-alpha-machinery
R: low
source: "OMG Essence 2.0:2024 + Левенчук Методология 2025 Гл. 4"
adaptation_note: "Adapted for Jetix substrate — covers any artefact, not only software"
---

# Alpha: Software-System (adapted for Jetix)

## Purpose
Software / artifact / Jetix substrate piece being created по hypothesis.

**Adaptation:** Original OMG Essence «software-system» here generalized к **artefact**:
- agents (.claude/agents/)
- wikis (wiki/concepts/)
- pipelines (tools/)
- decks / one-pagers
- decisions / Foundation Parts
- prompts / methodology documents

## State graph
```
architecture_selected → demonstrable → usable → ready → operational → retired
```

## State definitions

| State | Meaning |
|---|---|
| **architecture_selected** | High-level structure / approach chosen |
| **demonstrable** | Smallest skeleton works; can be shown |
| **usable** | Working для at least one user/scenario |
| **ready** | Production-quality; ready для broad use |
| **operational** | Live; actively used |
| **retired** | Decommissioned; superseded |

## Jetix application

- **Engineering hypothesis** — artefact = tool/agent being created
- **Method hypothesis** — artefact = methodology document / template
- **Outreach hypothesis** — artefact = pitch / one-pager / sequence
- **FPF-extension hypothesis** — artefact = FPF spec amendment / new pattern

## Example transition

```
2026-05-20 — software-system → architecture_selected: 7-layer architecture chosen
2026-05-20 — software-system → demonstrable: Phase 1 substrate complete
2026-05-20 — software-system → usable: Phase 8 5 samples + skills functional
2026-XX-XX — software-system → ready: production migration of pool candidates
2026-XX-XX — software-system → operational: daily workflow integrated
```

## Cross-refs

- Schema: `_schema/alphas.yaml`
- State-graph: `state-graphs/software-system-state-graph.md`
- Overview: `_alphas-overview.md`
