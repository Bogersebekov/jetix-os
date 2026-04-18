---
type: task
status: backlog
project-slug: ""
estimate: ""
next_action: ""
owner: ruslan
priority: p2
created: {{date:YYYY-MM-DD}}
tags: []
---

<!--
Template: T-06 tpl-task.md
Example usage:
  tasks/master.md entry,
  projects/{slug}/tasks.md entry.

Lifecycle (state machine §F.9 DATA-FLOWS):
  backlog → today → in-progress → done | blocked
  blocked → in-progress (when unblocked) или backlog.

Fields:
- status: backlog / today / in-progress / done / blocked
- project-slug: owning project или пусто (general task)
- estimate: "30m" | "2h" | "1d" — свободный формат
- next_action: конкретный first step
- priority: p0 (blocker) | p1 | p2 | p3
-->

# Task — {{task-slug}}

## Что сделать
<!-- Одна-две строки, actionable -->

## Next action
> {{next_action}}

## Definition of done
<!-- Что именно значит "сделано" -->

## Blockers / dependencies
<!-- Если blocked — на что, кто разблокирует -->

## Links
<!-- Cross-refs: project-slug, related hypothesis / decision / claim -->
