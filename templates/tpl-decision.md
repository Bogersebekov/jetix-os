---
type: decision
status: recorded
created: {{date:YYYY-MM-DD}}
context: ""
alternatives: []
decision: ""
evidence: ""
replay-check: ""
relevant-agents: []
owner: ruslan
tags: []
---

<!--
Template: T-02 tpl-decision.md
Example usage:
  decisions/life-decisions-log.md entry,
  decisions/2026-04-decisions.md entry,
  projects/{slug}/decisions.md entry.

Frontmatter schema (инвариант I-12, §11.5 TECH):
- context: короткая строка — ситуация, в которой принималось решение
- alternatives: список рассмотренных альтернатив (может быть пустым — тогда evidence должен пояснить почему)
- decision: собственно текст решения, 1-3 предложения
- evidence: ссылки на источники / "no-evidence: intuition" если нет
- replay-check: как проверить через 3 месяца что решение было правильным
- relevant-agents: [list] — для /propagate-decision (I-29)

Lifecycle: recorded → reviewed → superseded (через новый decision с link на старый).
Append-only (I-05). Не редактировать после записи — создавать новое решение-коррекцию.
-->

# Decision — {{decision-slug}}

## Контекст
<!-- Что происходило, почему нужно решение -->

## Альтернативы рассмотренные
<!-- 2-3 варианта, каждый с коротким pros/cons -->

## Решение
<!-- Что выбрано и короткое обоснование -->

## Evidence
<!-- Ссылки на wiki/claims/, raw/, conversations; либо "no-evidence: intuition" -->

## Replay-check
<!-- Конкретный критерий/метрика через 3 месяца: "если X произошло — решение было верным" -->

## Relevant agents (для /propagate-decision)
<!-- Список agent-id, чьи strategies.md должны получить запись об этом решении -->
