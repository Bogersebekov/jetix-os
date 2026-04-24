---
title: "Pipeline — Quick Money AI Consulting P1"
type: pipeline
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
mrr_eur_contracted: 0
sources: []
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
  - "${WIKI_ROOT}/operations/quick-money/leads/"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Pipeline — Quick Money AI Consulting P1

Lead pipeline state machine. Updated by quick-money-brigadier each cycle.
`mrr_eur_contracted` frontmatter key is the SG-5 data source:
`pipeline.md:mrr_eur_contracted >= 1000`.

## Stage definitions

| Stage | Definition | Count |
|-------|-----------|-------|
| prospect | Identified from ICP filter; not yet engaged | 0 |
| qualified | Engaged + ICP 5-criteria passed + problem confirmed | 0 |
| proposal | Proposal sent (€150/час или productized package); awaiting decision | 0 |
| signed | Contract signed; project active | 0 |
| closed-won | Delivered + invoiced + paid | 0 |
| closed-lost | Declined or unresponsive after 3 follow-ups | 0 |

## KPI tracking

| KPI | Target | Current |
|-----|--------|---------|
| leads_per_quarter | 20 | 0 |
| contracts_per_quarter | 2 | 0 |
| mrr_eur_contracted | 1000 (SG-5 threshold) | 0 |
| mrr_eur_target_q2_2026 | 15 000 | 0 |
| cumulative_revenue_q2_2026_eur | 50 000 | 0 |

## Stage-gate SG-5 tracking

SG-5 predicate: `pipeline.md:mrr_eur_contracted >= 1000`
Current value: 0 (pending).
Update `mrr_eur_contracted:` frontmatter key when first retainer contract is signed.

## Notes

Phase-1 primary offer: €150/час consulting (D3 / JETIX-PLAN §3.1).
Productized packages in development (D18 productization path).
Продюсерский центр retainers (D11) count toward mrr_eur_contracted once signed.
