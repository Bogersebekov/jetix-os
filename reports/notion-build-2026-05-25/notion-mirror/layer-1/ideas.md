# 💡 💡 Ideas

> Банк идей / inbox для сырых мыслей. Дозрело → промоут в проект/гипотезу.

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Maturity` | select — опции: C-raw, B-shaping, A-ready |
| `Domain` | multi_select — опции: business, tech, life, research |
| `Promote to` | select — опции: —, project, hypothesis |
| `Note` | rich_text |

### Views для «💡 Ideas» (UI-only — API не создаёт)

- **Inbox** (table)
  - filter: Maturity=C-raw
- **Ready to promote** (table)
  - filter: Maturity=A-ready
- **By domain** (board)
  - group: Domain
