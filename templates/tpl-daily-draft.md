---
type: draft
topic: "{{topic}}"
parent-day: "{{date:YYYY-MM-DD}}"
promoted-to: null
status: draft
owner: ruslan
created: {{date:YYYY-MM-DD}}
tags: []
---

<!--
Template: T-09 tpl-daily-draft.md
Example usage: daily-log/drafts/{{date:YYYY-MM-DD}}-{{topic-slug}}.md

GitHub-style feature branches:
  projects/ = main (чистое, формальное)
  daily-log/drafts/ = sandbox (черновики, эксперименты, сырые мысли)

Frontmatter schema:
- topic: короткая тема — для /close-day routing
- parent-day: YYYY-MM-DD — ссылка на daily-log entry
- promoted-to: null | <path> — куда выведен в /close-day:
    wiki/ideas/... | wiki/claims/... | wiki/concepts/...
    crm/clients.md | crm/partners.md | crm/personal.md
    tasks/master.md | projects/{slug}/*.md
    decisions/... | "archive-only"

Жизненный цикл: draft → (close-day routing) → promoted OR archived OR kept as draft.
-->

# Draft — {{topic}}

## Что за тема
<!-- 1-2 предложения о чём этот draft -->

## Сырые мысли
<!-- Поток сознания, ссылки, цитаты, незавершённые идеи -->

## Решение в /close-day
<!-- Заполняется на вечернем ритуале:
- [ ] Распределить в wiki/ (концепт / claim / идея / источник)
- [ ] В CRM (контакт)
- [ ] В task (tasks/master.md или projects/{slug}/)
- [ ] В decision (decisions/)
- [ ] В проект (projects/{slug}/)
- [ ] Archive-only (оставить в drafts как sandbox)
-->

## Promoted-to
<!-- Если distilled — указать target path (обновить также frontmatter) -->
