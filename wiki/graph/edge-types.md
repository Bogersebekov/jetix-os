---
title: Edge Types — wiki/graph/edges.jsonl
type: reference
date: 2026-04-26
status: active
---

# Edge Types

Authoritative enum of `type` field values in `wiki/graph/edges.jsonl`.

Each edge is a JSONL line:
```json
{"from": "<path>", "to": "<path>", "type": "<edge-type>", "created": "YYYY-MM-DD", "confidence": "high|medium|low", "context": "(optional)"}
```

Paths are relative to repo root and include the `.md` extension.

## Wiki edges (9 types — pre-existing)

| Type | Direction | Meaning |
|------|-----------|---------|
| `derived_from` | source → derivative | Idea/concept derived from a source |
| `extends` | child → parent | Concept extends/builds on another |
| `supports` | evidence → claim | Evidence supports a claim |
| `contradicts` | A → B | A contradicts B |
| `mentions` | A → B | A name-drops B |
| `cites` | A → B | A formally cites B |
| `replaces` | new → old | New replaces deprecated old |
| `parent_of` | parent → child | Hierarchical containment |
| `same_as` | A → B | A and B refer to the same entity |

## CRM edges (8 types — added 2026-04-26)

Used between `crm/people/<slug>.md` and `crm/orgs/<slug>.md` files. Asymmetric
edges have explicit direction; symmetric (peer-to-peer) edges are conventionally
written from alphabetically-earlier slug to later, but tooling treats them as
undirected.

| Type | Symmetric? | From → To | Meaning |
|------|------------|-----------|---------|
| `co-founder-with` | yes (peer) | person → person | They co-founded a venture together |
| `shares-mentor-with` | yes (peer) | person → person | Both have the same mentor (network adjacency) |
| `founder-of` | no | person → org | Person founded the org |
| `employee-at` | no | person → org | Person works at the org (current OR past — qualify in `context`) |
| `introduced-by` | no | person → person | "to" introduced "from" to Jetix (warm intro provenance) |
| `partner-with` | yes (peer) | person/org → person/org | Active partnership relationship |
| `client-of` | no | person/org → person/org | "from" is a client of "to" (Jetix lens: "to" is the service provider) |
| `advisor-of` | no | person → person/org | "from" is advising "to" |

**Confidence levels** (same as wiki edges):
- `high` — verified directly (Ruslan met both, has signed paper, etc.)
- `medium` — inferred from public profiles / single-source mention
- `low` — speculative, needs verification

**Context field** is optional but recommended for CRM edges to record the
provenance ("met at AI Berlin meetup 2024-09", "mentioned by anton during
discovery call 2026-04-26", etc.).

## Examples

### Wiki edges
```json
{"from": "ideas/X.md", "to": "concepts/Y.md", "type": "derived_from", "created": "2026-04-16", "confidence": "high"}
```

### CRM edges
```json
{"from": "crm/people/anton.md", "to": "crm/people/vladislav.md", "type": "co-founder-with", "created": "2026-04-26", "confidence": "high", "context": "co-founded test-ai.com 2020-2022"}
{"from": "crm/people/anton.md", "to": "crm/orgs/test-ai.md", "type": "founder-of", "created": "2026-04-26", "confidence": "high"}
{"from": "crm/people/anna.md", "to": "crm/people/anton.md", "type": "introduced-by", "created": "2026-04-22", "confidence": "high", "context": "warm intro by anton via LinkedIn"}
{"from": "crm/orgs/customer-co.md", "to": "crm/orgs/jetix.md", "type": "client-of", "created": "2026-04-26", "confidence": "high"}
```

## How to add edges

Manually:
```bash
echo '{"from": "...", "to": "...", "type": "...", "created": "2026-04-26", "confidence": "high"}' >> wiki/graph/edges.jsonl
```

Programmatically (during CRM ops): future enhancement; currently edges added
manually after `/crm-update` or `/ingest` flows.

**Validation** (Phase 2 candidate): `wiki/graph/build_graph.py` should reject
edges with `from`/`to` paths that don't exist + reject types not listed above.
Currently the file is append-only with no automated linting.
