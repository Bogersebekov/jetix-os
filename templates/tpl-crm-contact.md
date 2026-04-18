---
type: contact
category: clients
name: "Имя Фамилия"
company: ""
role: ""
stage: lead
sensitive: false
tags: []
language: ru
channel: ""
last-touch: {{date:YYYY-MM-DD}}
next_action: ""
notes-ref: ""
source: ""
owner: ruslan
created: {{date:YYYY-MM-DD}}
---

<!--
Template: T-11 tpl-crm-contact.md
Example usage:
  crm/clients.md entry   (category: clients)
  crm/partners.md entry  (category: partners)
  crm/personal.md entry  (category: personal)

Frontmatter schema (ADR-016 — three CRM bases):
- category: clients / partners / personal
- stage: lead / qualified / engaged / active / paused / closed-won / closed-lost
- last-touch: YYYY-MM-DD последнего контакта
- next_action: конкретный next step для Ruslan'а
- notes-ref: путь к подробным заметкам если они отдельным файлом
- sensitive: true опционально (B-3.2) — пометка для privacy-фильтров;
  crm/personal.md entries обычно sensitive: true.
  Sensitive=true НЕ убирает файл из git автоматически — решение о .gitignore
  принимается на уровне folder policy, не поштучно.
-->

# {{name}}

## Контекст
<!-- Как познакомились, чем занимается, что интересно -->

## Заметки по контактам
### {{date:YYYY-MM-DD}} — Первый контакт
- Канал:
- Тема:
- Ключевое:
- Follow-up:

## Pain points
<!-- Боли, задачи, потребности — для ICP-калибровки (если client/partner) -->

## Потенциал для Jetix (только clients/partners)
<!-- Что можно предложить, какой формат, какой следующий шаг -->

## Links
<!-- Cross-refs: related contacts, projects, meetings в wiki/sources/ -->
