# ✅ ✅ Tasks

> Атомарные действия. На старте можно жить чек-листами внутри Projects.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Status` | select — опции: todo, doing, done |
| `Priority` | select — опции: now, next, later |
| `Due` | date |

### Views для «✅ Tasks» (UI-only — API не создаёт)

- **Today** (table)
  - filter: Priority=now OR Due ≤ today
- **By project** (board)
  - group: Project
- **Done** (table)
  - filter: Status=done
