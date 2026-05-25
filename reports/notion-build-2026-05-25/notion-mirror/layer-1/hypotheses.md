# ❓ ❓ Hypotheses

> Что хочу проверить: критерий подтверждения/опровержения + уверенность (Bayesian-lite).

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Statement` | title |
| `Confirm criterion` | rich_text |
| `Refute criterion` | rich_text |
| `Status` | select — опции: open, testing, confirmed, refuted |
| `Confidence` | select — опции: low, mid, high |

### Views для «❓ Hypotheses» (UI-only — API не создаёт)

- **Open** (table)
  - filter: Status=open
- **Testing now** (table)
  - filter: Status=testing
- **Closed** (table)
  - filter: Status in {confirmed,refuted}
