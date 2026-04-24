---
title: "Pipeline — {{PROJECT_TITLE}}"
type: pipeline
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/leads/"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Pipeline — {{PROJECT_TITLE}}

Lead pipeline state machine. Updated by project-brigadier each cycle.

## Stages

| Stage | Definition | Count |
|-------|-----------|-------|
| lead | Initial contact or identified prospect | 0 |
| prospect | Engaged; discovery call scheduled or completed | 0 |
| qualified | Meets ICP; problem confirmed; budget indicated | 0 |
| proposal | Proposal sent; awaiting response | 0 |
| closed | Contract signed | 0 |
| lost | Declined or unresponsive after 3 follow-ups | 0 |

## KPI tracking

| KPI | Target | Current |
|-----|--------|---------|
| leads_per_quarter | 20 | 0 |
| contracts_per_quarter | 2 | 0 |
| contract_signed_count (lifetime) | — | 0 |
| client_revenue_recurring_eur_per_month | 5000 | 0 |

## Notes

{{FILL_IN — Any pipeline-specific notes or constraints.}}
