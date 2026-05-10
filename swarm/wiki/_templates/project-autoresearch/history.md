---
title: "History — {{PROJECT_TITLE}}"
type: history
project: "{{SLUG}}"
project_type: autoresearch
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
tier: tier-internal
produced_by: "/project-bootstrap --type=autoresearch"
binding_scope: "project-{{SLUG}}"
---

# History — {{PROJECT_TITLE}}

Append-only events log (newest-on-top per CLAUDE.md convention).

Each event line:

    YYYY-MM-DD  HH:MM  <event-type>  <one-line summary>  [refs]

Event types: `bootstrap`, `experiment-batch`, `keep-variant`, `revert-variant`,
`halt-log-alert`, `cost-cap-hit`, `consecutive-failure-abort`,
`drr-candidate-emit`, `draft-promotion-gate-emit`, `methodology-promoted`,
`cycle-close`.

## Events

- {{TODAY}}  bootstrap — project scaffolded via /project-bootstrap --type=autoresearch
