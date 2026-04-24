---
title: "Fixture manifest — E2E demo — KM MVP"
type: fixture-manifest
fixture_for: "UC-INGEST-1 + UC-ASK-1 + E.4 end-to-end demo"
created: 2026-04-24
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E.4 + §3 UC-INGEST-1 + UC-ASK-1"}
---

# Fixture — E2E demo (UC-INGEST-1 + UC-ASK-1 + Part E.4)

## Purpose

Hermetic offline substitute for the live Mittelstand AI reference article ingested
in Part E.4 of the KM Materialization MVP sprint. Enables deterministic re-run without
network access.

## Files

| File | Purpose |
|---|---|
| `meadows-leverage-points-transcript.md` | Substitute for live Bitkom/external URL; local-markdown source type |
| `expected-concepts.txt` | 5 expected concept slugs; IDEM + COMM assertion target |
| `expected-ask-question.txt` | Canonical /ask query; deterministic for re-run |
| `expected-comparison-slug.txt` | Expected comparisons/ filename fragment |

## Re-run instructions (offline)

1. `cp swarm/tests/fixtures/km-mvp/e2e-demo/meadows-leverage-points-transcript.md raw/transcripts/`
2. `/ingest raw/transcripts/meadows-leverage-points-transcript.md`
3. Assert: `delta_concepts in [5,8]` AND `delta_edges in [8,20]` (per UC-INGEST-1 probe).
4. Assert: every slug in `expected-concepts.txt` exists under `swarm/wiki/concepts/`.
5. `/ask "$(cat swarm/tests/fixtures/km-mvp/e2e-demo/expected-ask-question.txt)"`
6. Assert: answer contains ≥3 `[src:...]` citations.
7. Assert: `swarm/wiki/comparisons/` contains a file matching `*leverage-points-quick-money-icp.md`.
8. Append insight to `swarm/wiki/operations/quick-money/history.md` per E.4 step 4 template.

## IDEM re-run assertion

Run step 2 again (same fixture file, same path):
- Assert: `delta_concepts == 0` (IDEM guard fires; no new concept pages created).
- Assert: `delta_edges == 0` (IDEM guard fires; no duplicate edges appended).

## COMM order-independence assertion (optional; requires second fixture)

If a second fixture `swarm/tests/fixtures/km-mvp/e2e-demo/second-article-fixture.md` exists:
- Run: `/ingest meadows-...` then `/ingest second-article-...`; capture concept slug set A.
- Reset wiki state (git checkout swarm/wiki/concepts/ swarm/wiki/graph/edges.jsonl).
- Run: `/ingest second-article-...` then `/ingest meadows-...`; capture concept slug set B.
- Assert: `sort(A) == sort(B)` (COMM holds).
