# 🤝 🤝 Stakeholders / CRM lite

> Универсальный CRM: клиенты, партнёры, инвесторы, вендоры.

*Источник спеки:* reports/.../05-layer-3-universal-business-foundation-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Kind` | select — опции: person, org |
| `Type` | select — опции: customer, partner, investor, advisor, vendor, other |
| `Status` | select — опции: lead, active, paused, past |
| `Last touch` | date |
| `Next action` | rich_text |
