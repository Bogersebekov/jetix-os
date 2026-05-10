---
title: "Context — {{PROJECT_TITLE}}"
type: context-snapshot
project: "{{SLUG}}"
project_type: autoresearch
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap-autoresearch
tier: tier-internal
produced_by: "/project-bootstrap --type=autoresearch"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
cycle_count: 0
active_tasks_current: 0
experiments_run_total: 0
keep_variants_total: 0
constitutional_violations_total: 0
daily_cost_eur_today: 0.0
---

# Context — {{PROJECT_TITLE}}

Updated by autoresearch-brigadier each cycle. Snapshot of current autoresearch
state.

## Cycle count

0 (SG-0 fires at 1; SG-4 fires at 5 with active_tasks_current >= 3)

## Experiments to date

0 total, 0 KEEP, 0 REVERT.

## Cost ledger (today)

€0.00 spent against daily cap (see hypothesis-config `budget.daily_cap_eur`).
