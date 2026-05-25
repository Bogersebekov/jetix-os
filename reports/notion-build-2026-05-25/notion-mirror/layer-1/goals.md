# 🎯 🎯 Goals

> Конкретные цели с метриками и сроками. Смысл целей — в Strategic-документе рядом.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Horizon` | select — опции: year, quarter, month |
| `Metric` | rich_text |
| `Target` | rich_text |
| `Due` | date |
| `Status` | select — опции: not-started, in-progress, done |
| `Why` | rich_text |

### Views для «🎯 Goals» (UI-only — API не создаёт)

- **By horizon** (board)
  - group: Horizon
- **Active** (table)
  - filter: Status=in-progress
