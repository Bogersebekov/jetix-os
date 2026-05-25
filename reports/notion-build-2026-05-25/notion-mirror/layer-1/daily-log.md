# 📅 📅 Daily Log

> День = одна запись: цель дня, что реально сделал, энергия, тип дня, связи.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Date` | title |
| `Цель дня` | rich_text |
| `Реально сделано за день` | rich_text |
| `Energy` | number (number) |
| `Deep work minutes` | number (number) |
| `Day type` | select — опции: production, development, recovery, orientation |

### Views для «📅 Daily Log» (UI-only — API не создаёт)

- **Today** (table)
  - filter: Date = today
- **This week** (table)
  - filter: Date within last 7 days
- **По типу дня** (board)
  - group: Day type
