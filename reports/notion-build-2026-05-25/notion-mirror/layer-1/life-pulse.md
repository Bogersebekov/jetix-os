# ❤️ ❤️ Life Pulse

> Ежедневный мини-замер: энергия/сон/настроение. Приватно, наверх не уходит.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Date` | title |
| `Energy` | number (number) |
| `Sleep hours` | number (number) |
| `Mood` | select — опции: low, neutral, good |
| `Movement` | checkbox |

### Views для «❤️ Life Pulse» (UI-only — API не создаёт)

- **This week** (table)
  - filter: Date within 7 days
- **Trend** (calendar)
