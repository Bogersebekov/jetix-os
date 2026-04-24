---
title: "Decisions — {{PROJECT_TITLE}}"
type: decision-log
project: "{{SLUG}}"
project_type: product
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

- **Decision:** Bootstrap product project {{SLUG}} at {{PRIORITY}}.
- **Reasoning:** {{FILL_IN — why this product project was started.}}
- **Result:** Scaffold created; mini-swarm spawned (if P1/P2); state: active.
- **Review:** At SG-p-1 firing or after first validation cycle, verify problem_statement
  and kill_criteria are still accurate.
