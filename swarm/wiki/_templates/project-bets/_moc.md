---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: bets
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Describe the bet: what thesis are we testing? What outcome would
  validate this bet? Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition that kills this bet.
  Example: "if SG-2 not fired after 8 cycles, kill."
  /lint hard-fails if blank.}}
kpi_targets: {}
  # Bets start with no fixed KPI targets.
  # kpi_targets populated after SG-2 fires (bet validated).
stage_gates:
  SG-0:
    predicate: "context.md:cycle_count >= 3"
    description: "Bet has survived at least 3 cycles — triggers HITL bet-review gate (kill | continue | promote)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-1:
    predicate: "count(leads/*.md) >= 3"
    description: "Bet has generated 3+ leads — auto-spawn leads/ + pipeline.md."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-2:
    predicate: "count(contracts/*.md) >= 1 OR count(hypotheses.md:status: validated) >= 1"
    description: "Bet validated via contract file OR hypothesis marked 'status: validated'."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Bet has sufficient momentum at evaluation timestamp for full B2 promotion."
    state: pending
    fired_at: null
    spawned_paths: []
adaptive: true
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Hybrid
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: low
confidence_method: bootstrap-adaptive
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.bets"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Bet

## Thesis

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Current stage

SG-0: pending (bet started {{TODAY}}).

## Adaptive scaffold note

This bet starts with minimal scaffold (5 files). Additional files auto-spawn
when stage-gates fire:
- SG-1 fires → leads/ + pipeline.md spawned
- SG-4 fires → eligible for /project-promote to consulting/research/product

## Related themes

- [[{{AUTO_THEME}}]]
