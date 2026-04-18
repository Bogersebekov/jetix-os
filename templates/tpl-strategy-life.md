---
type: strategy-life
level: weekly
period: "{{period}}"
north-star: "$50K revenue до 30.06.2026"
focus-blocks: []
budget-resources:
  hours: 0
  money: 0
  attention: ""
metric-50k-contribution: ""
owner: ruslan
status: active
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

<!--
Template: T-04 tpl-strategy-life.md
Example usage:
  strategy/life/2026-yearly.md       (level: yearly, period: "2026")
  strategy/life/2026-04-monthly.md   (level: monthly, period: "2026-04")
  strategy/life/2026-W17-weekly.md   (level: weekly, period: "2026-W17")

Frontmatter schema:
- level: yearly / monthly / weekly
- period: "2026" | "2026-04" | "2026-W17" — ISO-формат
- north-star: главная цель, обычно $50K до 30.06.2026
- focus-blocks: список фокус-блоков с часами
- budget-resources: hours / money / attention
- metric-50k-contribution: как этот период двигает к $50K (обязательно в v1-beta)

L3 Strategic (I-11): редактирует только Ruslan.
Fractal strategy (I-31 MAY): yearly/monthly/weekly связаны через Obsidian transclude ![[path#^block]].
-->

# Strategy — {{level}} {{period}}

## North star
> {{north-star}}

## Point A (начало периода)
<!-- Где я на старте: ресурсы, состояние проектов, открытые вопросы -->

## Point B (конец периода)
<!-- Measurable результаты — 2-3 штуки -->

## Focus-blocks
<!-- Распределение времени между главными направлениями:
1. [project-slug] — N часов — что конкретно
2. [project-slug] — N часов
3. [meta/health/reflection] — N часов
-->

## Daily breakdown (для weekly уровня)
<!-- пн/вт/ср/чт/пт/сб/вс — короткие focus + блокеры -->

## Hypotheses активные
<!-- Cross-link на hypotheses/active.md — что тестируем в этот период -->

## Decisions ожидаются
<!-- Решения которые должны быть приняты к концу периода -->

## Kill-criteria / pivot-points
<!-- Что пересматриваем на ritual следующего уровня если не сдвинулось -->

## Metric → $50K contribution
> {{metric-50k-contribution}}

## Links
<!-- Obsidian transclude на yearly/monthly parents, related projects, weekly children -->
