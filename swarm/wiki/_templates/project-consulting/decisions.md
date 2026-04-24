---
title: "Decisions — {{PROJECT_TITLE}}"
type: decision-log
project: "{{SLUG}}"
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

- **Decision:** Bootstrap project {{SLUG}} as {{PROJECT_TYPE}} at {{PRIORITY}}.
- **Reasoning:** {{FILL_IN — why this project was started.}}
- **Result:** Scaffold created; mini-swarm spawned (if P1/P2); state: active.
- **Review:** At SG-1 firing or after first cycle, verify problem_statement is still
  accurate and kill_criteria is still measurable.
