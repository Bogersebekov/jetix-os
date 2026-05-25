# 🤝 🤝 Contacts

> Облегчённый личный CRM: кто, когда общались, что предлагаю/прошу.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Type` | select — опции: family, friend, colleague, mentor, client |
| `Status` | select — опции: active, warm, cold, paused |
| `Last touch` | date |
| `What I offer` | rich_text |
| `What I ask` | rich_text |

### Views для «🤝 Contacts» (UI-only — API не создаёт)

- **Active** (table)
  - filter: Status=active
- **Reconnect** (table)
  - filter: Last touch > 30d ago
- **By type** (board)
  - group: Type
