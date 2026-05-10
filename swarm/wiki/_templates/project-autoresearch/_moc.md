---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: autoresearch
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — What domain are we running a Karpathy-style propose→eval→keep
  loop on? Which lens / artefact mutates? What does "better" look like?
  Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition that kills this autoresearch loop.
  Example: "if 0 KEEP variants after 50 experiments OR consecutive failures
  hit 10, kill this domain pilot."
  /lint hard-fails if blank.}}
kpi_targets:
  primary_metric_improvement_pct: null  # set per domain after baseline measurement
  hamel_binary_acceptance_rate: null
stage_gates:
  SG-0:
    predicate: "context.md:cycle_count >= 1"
    description: "Initial baseline measurement complete — first orchestrator run finished."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-1:
    predicate: "count(reports/autoresearch-*/drr-candidates/*.md) >= 5"
    description: "At least 5 DRR-candidate entries emitted (KEEP variants exist)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-2:
    predicate: "count(reports/autoresearch-*/drr-candidates/*.md:validated_in_cycles: 3) >= 1"
    description: "At least 1 DRR candidate has cleared Q4 threshold (≥3 validated cycles) — eligible for draft_promotion gate."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 3"
    description: "Domain pilot has run 5+ cycles with sustained activity — eligible for cross-domain expansion proposal."
    state: pending
    fired_at: null
    spawned_paths: []
adaptive: true
granularity: "{{GRANULARITY}}"
inference_stack: cc-headless-max-sub
default_inference_tier: T-Hybrid
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: low
confidence_method: bootstrap-autoresearch
tier: tier-internal
produced_by: "/project-bootstrap --type=autoresearch"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.autoresearch"}
  - {path: "reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md", range: "full"}
related:
  - "{{WIKI_ROOT}}/operations/voice-pipeline-canonical-2026-05-10.md"
binding_scope: "project-{{SLUG}}"
constitutional_anchors:
  - Tier 2 Rule 1 (no AI strategizing)
  - Tier 2 Rule 2 (no autonomous architectural change)
  - Tier 2 Rule 11 (Default-Deny on uncategorized actions)
---

# {{PROJECT_TITLE}}

> AutoResearch project — Karpathy-style propose→evaluate→keep-or-revert loop.
>
> **Authoritative spec:** `reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md`
> **Brigadier:** `autoresearch-brigadier` (RUSLAN-LAYER auto-loop scope)
> **Inference:** `tools/lib/cc_helper.py` (Max-sub headless; no API key)

## Problem statement

See frontmatter `problem_statement`.

## Kill criteria

See frontmatter `kill_criteria`.

## Stage gates

See frontmatter `stage_gates`. Predicates are Hamel-binary + file-anchored.

## Hypothesis configs

- _list each `config/autoresearch-hypothesis-*.yaml` for this domain_

## Program / research agenda

- `program/<domain>.md` (Ruslan-authored per Q8)

## DRR ledger

- Per-experiment DRR candidates land under
  `reports/autoresearch-karpathy-integration-*/drr-candidates/`. Validated
  candidates (≥3 cycles per Q4) emit AWAITING-APPROVAL `gate_class: draft_promotion`
  to `swarm/approvals/log.jsonl`. Methodology promotion to `wiki/methodology/`
  requires Ruslan ack.

## Open questions

See `open-questions.md`.
