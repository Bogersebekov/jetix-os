# 🛡️ 🛡️ R12 Audit Log

> 4 детектора жадности/принуждения. Срабатывание → HALT + лог + Steward.

*Источник спеки:* reports/.../04-layer-2-team-collaboration-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Event` | title |
| `Trigger` | select — опции: extraction_beyond_share, wage_ratio_violation, non_consensual_distribution, fork_prevention_attempt |
| `Severity` | select — опции: F2, F4, F8 |
| `Detected` | date |
| `Action taken` | rich_text |
| `Status` | select — опции: open, resolved |
| `Project` | rich_text |
| `Member` | rich_text |
