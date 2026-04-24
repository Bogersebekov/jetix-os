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
  {{FILL_IN — Cagan: describe the research problem being investigated.
  Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition under which this research project is killed.
  Example: "if no refuted or supported hypotheses after 6 cycles, kill."
  /lint hard-fails if blank.}}
kpi_targets:
  hypotheses_per_cycle: 3
  papers_per_quarter: 1
stage_gates:
  SG-rd-1:
    predicate: "count(hypotheses.md:status: supported) >= 2"
    description: "At least 2 lines in hypotheses.md contain marker 'status: supported'."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-rd-2:
    predicate: "count(hypotheses.md:status: refuted) >= 1"
    description: "At least 1 line in hypotheses.md contains 'status: refuted' — Popperian refutation event."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-rd-3:
    predicate: "count(drafts/*.md) >= 1"
    description: "At least 1 draft artefact exists under drafts/."
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
default_inference_tier: T-Hybrid
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.research"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Map of Content

## Problem

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Current focus

{{FILL_IN — 2-3 sentences on current research direction.}}

## Hypotheses

See `hypotheses.md`. Current: 0 supported / 0 refuted / 0 pending.

## Drafts

See `drafts/` directory.

## Sources

See `sources.md`.

## Related themes

- [[{{AUTO_THEME}}]]
