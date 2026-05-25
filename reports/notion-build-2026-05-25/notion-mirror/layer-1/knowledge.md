# 📚 📚 Knowledge

> Личная вики: источники, выводы, факты + «посмотреть позже».

*Источник спеки:* reports/.../03-layer-1-personal-core-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Name` | title |
| `Kind` | select — опции: source, claim, concept |
| `Status` | select — опции: queued, reading, read |
| `Saved-for-later` | checkbox |
| `Key takeaway` | rich_text |
| `Domain` | multi_select — опции: business, tech, life, research |

### Views для «📚 Knowledge» (UI-only — API не создаёт)

- **Reading queue** (table)
  - filter: Status in {queued,reading}
- **Посмотреть позже** (table)
  - filter: Saved-for-later = ✓
- **By domain** (board)
  - group: Domain
