---
title: "Offline Inference Spec — {{PROJECT_TITLE}}"
type: offline-inference-spec
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md", range: "UC-10"}
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Offline Inference Spec — {{PROJECT_TITLE}}

Per UC-10 Phase-A offline-first architecture. Completed before first client
deployment. Engineering-expert validates at provisioning.

## Model choice

Default: ollama + Mistral 7B Q4_K_M (Apache 2.0 license; cleanest for Mittelstand
commercial deployment per KM-ARCHITECTURE-VARIANTS §12 Dissent 2).

Alternative: ollama + Llama 3.1-8B Q4_K_M (pending DACH golden-set evaluation).

## Hardware requirements

- VRAM floor: 8 GB (Mistral 7B Q4_K_M)
- Storage: ~4 GB model file + ~500 MB per-project KB index
- OS: Linux (Ubuntu 22.04+ recommended); ollama daemon running

## Hosting path

- **Path B (default):** client-hosted; Jetix ships methodology + prompt updates.
- **Path A:** Jetix EU VPS per-client VM.
- **Path C:** Hybrid mTLS tunnel.

Selected path for this project: {{FILL_IN}}

## Acceptance test

Golden-set: 20 queries representative of this project's knowledge domain.
Pass criterion: >= 80% of queries return a response with >= 3 [src:...] citations
in <= 5 seconds p95 latency on client hardware.

Results after first deployment: {{FILL_IN}}

## Phase-A fallback

If local LLM not yet provisioned: use `OFFLINE_MODE=1` structured-excerpt path
in `/ask` skill (retrieval-only; zero cloud LLM calls per UC-10 Phase-A proof).
