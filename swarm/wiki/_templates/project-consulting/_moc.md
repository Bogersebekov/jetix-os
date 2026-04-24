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
  {{FILL_IN — Cagan: describe the problem being solved in terms the customer understands.
  One paragraph. Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: specific measurable condition that ends this project.
  Example: "if no signed contract after 12 weeks of structured outreach, kill."
  Must be a single binary observable condition. /lint hard-fails if blank.}}
kpi_targets:
  leads_per_quarter: 20
  contracts_per_quarter: 2
  mrr_eur: 5000
stage_gates:
  # All predicates Hamel-binary + DSL-canonical (file-anchored).
  # Post philosophy-critic-1 revision: only count(<glob>), count(<glob>:<marker>),
  # and <file.md>:<key> OP <n> forms are legal.
  SG-1:
    predicate: "count(leads/*.md) >= 3"
    description: "At least 3 active lead pages exist under leads/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-2:
    predicate: "count(contracts/*.md) >= 1"
    description: "At least 1 signed contract file exists under contracts/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-3:
    predicate: "count(leads/*.md:status: qualified) >= 3"
    description: "At least 3 leads contain the marker 'status: qualified' (grep-anchored)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-5:
    predicate: "pipeline.md:mrr_eur_contracted >= 1000"
    description: "Contracted MRR (pipeline.md frontmatter mrr_eur_contracted) >= EUR 1000/month."
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
  - {path: ".claude/config/project-types.yaml", range: "types.consulting"}
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

{{FILL_IN — 2-3 sentences describing what this project is actively working on right now.}}

## KPIs

| KPI | Target | Current |
|-----|--------|---------|
| Leads per quarter | 20 | 0 |
| Contracts per quarter | 2 | 0 |
| MRR (EUR) | 5000 | 0 |

## Stage gates declared

See frontmatter stage_gates block above. Evaluated daily by `/lint --check-stage-gates`.

## Active leads

See `leads/` directory. Current count: 0.

## Pipeline status

See `pipeline.md`.

## Related themes

- [[{{AUTO_THEME}}]]

## Open questions

See `open-questions.md`.
