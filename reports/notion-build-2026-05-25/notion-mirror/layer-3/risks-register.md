# 🛡️ 🛡️ Risks Register

> Реестр рисков: серьёзность × вероятность + митигация.

*Источник спеки:* reports/.../05-layer-3-universal-business-foundation-revised.md

## Схема полей

| Поле | Тип |
|---|---|
| `Title` | title |
| `Category` | select — опции: financial, operational, legal, market, people |
| `Severity (1-5)` | number (number) |
| `Likelihood (1-5)` | number (number) |
| `Mitigation` | rich_text |
| `Status` | select — опции: open, mitigating, accepted, closed |
