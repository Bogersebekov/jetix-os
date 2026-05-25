# 🔁 🔁 Habits

> Трекер привычек: список + отметка дня через Daily Log. Приватно.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Cadence` | select — опции: daily, weekly, Nx-week |
| `Target` | rich_text |
| `Area` | multi_select — опции: health, mind, work, relationships |
| `Active` | checkbox |
| `Notes` | rich_text |

### Views для «🔁 Habits» (UI-only — API не создаёт)

- **Active** (table)
  - filter: Active=✓
- **By area** (board)
  - group: Area
- **Paused** (table)
  - filter: Active=☐
