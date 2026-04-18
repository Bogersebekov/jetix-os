---
type: adr
number: 0
title: "ADR layer placeholder"
status: proposed
date: 2026-04-18
context: "ADR split launches в v1-final"
decision: "В v1-beta ADR'ы живут inline в design/SYSTEM-DESIGN-TECH.md §12"
consequences: "В v1-final разделяем 18 существующих ADR + новые в отдельные файлы"
owner: ruslan
created: 2026-04-18
related-adrs: []
---

<!--
Placeholder-файл. Папка `docs/adr/` активируется в v1-final (см. ADR-018, §12 TECH).
-->

# `docs/adr/` — Architecture Decision Records

**В v1-beta:** пусто. Все 18 ADR (ADR-001 … ADR-018) живут inline в
`design/SYSTEM-DESIGN-TECH.md` §12 в формате Michael Nygard lightweight.

**В v1-final:** split — каждое ADR выносится в отдельный файл
`docs/adr/0001-docs-as-code.md`, `docs/adr/0002-single-central-claude.md`, …
в хронологическом порядке. Шаблон для новых записей: `templates/tpl-adr.md` (T-12).

**Когда создавать новые ADR:**
- Значимое архитектурное решение, которое нужно зафиксировать в истории.
- Изменение существующего инварианта или deprecation предыдущего ADR.
- Формат — Michael Nygard: Title · Date · Status · Context · Decision · Consequences. Max 1 страница.

**Наследование статуса:** proposed → accepted → [superseded | deprecated].
Superseded ADR остаются в папке с явной ссылкой на заменившее (append-only, §11.2).
