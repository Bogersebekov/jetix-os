---
title: "Decisions — {{PROJECT_TITLE}}"
type: decision-log
project: "{{SLUG}}"
project_type: bets
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: high
confidence_method: 4-part-drr
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Decisions — {{PROJECT_TITLE}}

4-part DRR entries per FPF E-9. Labels: Decision / Reasoning / Result / Review.
Appended by project-brigadier. Newest entries on top.

---

### {{TODAY}} — Project bootstrap

- **Decision:** Bootstrap bet project {{SLUG}} at {{PRIORITY}} in adaptive mode.
- **Reasoning:** {{FILL_IN — why this bet was started; what thesis is being tested.}}
- **Result:** Minimal scaffold created (5 files). SG-0 predicate: context.md:cycle_count >= 3.
- **Review:** At SG-0 firing (3 cycles), Ruslan acks: kill | continue | promote.
