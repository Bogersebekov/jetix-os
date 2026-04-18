---
type: strategy-project
project-slug: "{{project-slug}}"
point-a: ""
point-b: ""
horizon: ""
metric-50k-contribution: ""
resources-allocated:
  hours: 0
  money: 0
  people: []
owner: ruslan
status: active
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

<!--
Template: T-05 tpl-strategy-project.md
Example usage: strategy/projects/quick-money/strategy.md

Frontmatter schema:
- project-slug: совпадает с projects/{slug}/
- point-a: короткая строка текущего состояния
- point-b: целевое состояние + дедлайн
- horizon: "2 weeks" | "Q2-2026" | "6 weeks" — период охвата
- metric-50k-contribution: явная связь с $50K goal
- resources-allocated: budget hours/money + люди (имена или роли)

L3 Strategic (I-11): только Ruslan write.
Дополняет projects/{slug}/overview.md, не заменяет — overview фокус на
тактическом (next_action, timebox), strategy на глобальной картине.
-->

# Strategy — {{project-slug}}

## Why this project exists (в 3 строки)
<!-- Зачем проект существует в контексте Jetix и $50K -->

## Point A
> {{point-a}}

## Point B ({{horizon}})
> {{point-b}}

## Главная гипотеза
<!-- Если верна — проект работает; если нет — pivot/kill -->

## Стратегические ходы (3-5)
<!-- Список больших шагов, не тактических задач:
1. ...
2. ...
-->

## Resources allocated
- **Часы:** {{resources-allocated.hours}}h
- **Деньги:** {{resources-allocated.money}}
- **Люди:** {{resources-allocated.people}}

## Metric → $50K contribution
> {{metric-50k-contribution}}

## Kill / pivot signals
<!-- Конкретные условия — если X не случилось к Y, то Z -->

## Links
<!-- Cross-refs: projects/{slug}/overview.md, related hypotheses, decisions, claims -->
