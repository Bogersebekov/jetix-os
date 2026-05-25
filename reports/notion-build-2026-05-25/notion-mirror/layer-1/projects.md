# 🚀 🚀 Projects

> Личные проекты: тип, статус, чекпоинт, детект застрявших (>14d).

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Type` | select — опции: consulting, research, product, bets, personal |
| `Status` | select — опции: idea, active, paused, done, archived |
| `Checkpoint` | select — опции: start, in-progress, done |
| `Priority` | select — опции: P1, P2, P3, P4 |
| `Last touched` | date |
| `Notes` | rich_text |

### Views для «🚀 Projects» (UI-only — API не создаёт)

- **Active** (table)
  - filter: Status = active
  - sort: Priority
- **Board** (board)
  - group: Checkpoint
- **Stuck** (table)
  - filter: Status=active AND Last touched > 14d ago
