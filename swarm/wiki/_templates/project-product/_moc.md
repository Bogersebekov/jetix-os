---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: "{{PROJECT_TYPE}}"
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Cagan: describe the problem in terms customers understand.
  Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition that kills this product project.
  Example: "if 5 validation cycles yield < 3 positive outcomes, kill."
  /lint hard-fails if blank.}}
kpi_targets:
  validation_cycles: 5
  releases_per_quarter: 1
stage_gates:
  SG-p-1:
    predicate: "count(validation/*.md) >= 3"
    description: "At least 3 validation run records exist under validation/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-p-2:
    predicate: "count(releases/*.md) >= 1"
    description: "At least 1 release note file exists under releases/ (directory pre-created at bootstrap)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-p-3:
    predicate: "count(metrics.md:metric_count:) >= 1"
    description: "Metrics tracking has begun — at least one metric_count: entry in metrics.md."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
    state: pending
    fired_at: null
    spawned_paths: []
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Offline
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.product"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Map of Content

## Problem

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Solution hypothesis

See `solution-hypothesis.md`.

## Validation status

See `validation.md`. Runs: 0.

## Roadmap

See `roadmap.md`.

## Related themes

- [[{{AUTO_THEME}}]]
