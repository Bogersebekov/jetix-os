---
type: daily-log
date: {{date:YYYY-MM-DD}}
weekday: {{date:dddd}}
energy: null
projects_touched: []
plan: []
work-blocks: []
reflection: ""
drafts: []
owner: ruslan
created: {{date:YYYY-MM-DD}}
---

<!--
Template: T-08 tpl-daily.md
Example usage: daily-log/{{date:YYYY-MM-DD}}.md

Frontmatter schema:
- plan: список pledge'ев из /plan-day
- work-blocks: что реально делалось (заполняется по ходу дня)
- reflection: короткий итог дня (заполняется в /close-day)
- drafts: [path] — ссылки на daily-log/drafts/{{date}}-*.md созданные в этот день

Append within the day (I-05). Закрывается в /close-day — после этого файл read-only.
-->

# {{date:YYYY-MM-DD}} — {{date:dddd}}

## Фокус дня
> Главная цель:

## План
### Приоритет
- [ ]

### Если останется время
- [ ]

## Контекст на утро
### Статусы активных проектов
<!-- next_action из overview.md каждого active проекта -->

### Pending из вчера
<!-- Незакрытые задачи из вчерашнего лога -->

### Ресурсы
<!-- Доступное время, остаток бюджета, energy level -->

---

## Что сделано (append в течение дня)

## Drafts созданные сегодня
<!-- daily-log/drafts/{{date:YYYY-MM-DD}}-*.md -->
- [ ] draft-slug — topic

## Инсайты дня

## На завтра

## Итог дня (/close-day)
- Главный результат:
- Что не сделано и почему:
- Энергия: /10
- Drafts распределены: (да/нет, список куда)
