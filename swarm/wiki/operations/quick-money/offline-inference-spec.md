---
title: "Offline Inference Spec — Quick Money AI Consulting P1"
type: offline-inference-spec
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: uc-10-alignment
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "§B.3.1 offline-inference-spec.md template + UC-10"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path B/C"}
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Offline Inference Spec — Quick Money AI Consulting P1

Per UC-10 Phase-A offline-first architecture
[src:partB-b2-mini-swarm-bundle.md §B.3.1 offline-inference-spec.md].
Validated by engineering-expert before first client deployment.

## Model choice

**Default:** ollama + Mistral 7B Q4_K_M (Apache 2.0 license; cleanest for
Mittelstand commercial deployment per KM-ARCHITECTURE-VARIANTS §12 Dissent 2).

**Alternative:** ollama + Llama 3.1-8B Q4_K_M (pending DACH golden-set evaluation).

**Rationale for Mistral default:** Mittelstand clients require verifiable license
for commercial deployment. Apache 2.0 is unambiguous; Llama commercial terms have
thresholds and exceptions that require legal review. For Phase-1 speed, Mistral wins.

## Hardware requirements

| Requirement | Spec |
|---|---|
| VRAM floor | 8 GB (Mistral 7B Q4_K_M) |
| RAM (system) | 16 GB minimum |
| Storage | ~4 GB model file + ~500 MB per-project KB index |
| OS | Linux (Ubuntu 22.04+ recommended); ollama daemon running |
| GPU | Optional (CUDA/Metal acceleration if available; CPU-only ≈ 3–5× slower) |

## Hosting path

- **Path B (default for Phase-1):** client-hosted; Jetix ships methodology
  + agent configs + ollama setup scripts. Client hosts on own infrastructure
  (on-prem mini-PC or dedicated VPS in EU). Jetix provides remote consulting
  and support only. Data never leaves client. Maximum data sovereignty.
  [src:STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5 Path B]

- **Path C (enterprise clients):** client owns KB on their infrastructure;
  Jetix hosts agent-swarm with mTLS tunnel. Requires GDPR audit trail per
  client. Activates at €200K validation gate per JETIX-PLAN §4.

**Selected path for quick-money Phase-1:** Path B (client-hosted).

## 5-question acceptance test

Per UC-10 spec. All 5 must return TRUE before client handover.

```
Q1: Does `/ask "Summarize our Q1 sales report"` return an answer with >= 3
    [src:...] citations from the client's own wiki within 5 seconds p95 on
    client hardware?
    PASS criterion: TRUE

Q2: Does the local model operate with OFFLINE_MODE=1 (no cloud LLM calls)
    and still return a structured response?
    PASS criterion: TRUE

Q3: Does `ollama list` show mistral:7b-q4_k_m as the active model?
    PASS criterion: TRUE

Q4: Does `/ingest <client-document>` complete without errors and produce
    >= 1 wiki page under the client's operations/<slug>/ tree?
    PASS criterion: TRUE

Q5: Does the entire ingest+ask round-trip complete in < 120 seconds on
    client mini-PC hardware (Intel N100 or equivalent; no GPU)?
    PASS criterion: TRUE
```

**Golden-set:** 20 queries representative of the first Mittelstand client's
knowledge domain. Pass criterion: >= 80% of queries return >= 3 [src:...]
citations in <= 5 seconds p95 latency on client hardware.

## Phase-A fallback

If local LLM not yet provisioned: use `OFFLINE_MODE=1` structured-excerpt
path in `/ask` skill (retrieval-only; zero cloud LLM calls per UC-10
Phase-A proof). All wiki ingest and retrieval are filesystem-only.

## Fixture path for hermetic testing

`swarm/tests/fixtures/km-mvp/` — seeded corpus for CI validation.
