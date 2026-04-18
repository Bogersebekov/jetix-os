---
type: strategy-life
level: yearly
period: "meta-readme"
north-star: "$50K revenue до 30.06.2026"
focus-blocks: []
budget-resources: {}
metric-50k-contribution: "Структурирует стратегические документы, но сам по себе не двигает выручку"
owner: ruslan
status: active
created: 2026-04-18
updated: 2026-04-18
---

<!--
Индекс раздела `strategy/life/`. Реальные стратегические документы пишутся
по шаблону templates/tpl-strategy-life.md (T-04).
-->

# `strategy/life/` — Life-level стратегия

**Структура (fractal strategy, I-31 MAY):**

```
strategy/life/
├── README.md                    # этот файл
├── 2026-yearly.md               # level: yearly, period: "2026"
├── 2026-04-monthly.md           # level: monthly, period: "2026-04"
├── 2026-Wnn-weekly.md           # level: weekly, period: "2026-Wnn"
│   └── ...                      # каждая неделя — отдельный файл
└── archive/                     # (v1-final) закрытые периоды ротируются сюда
```

**Три уровня:**

| Уровень | Period format | Cadence | Кто пишет |
|---------|---------------|---------|-----------|
| **Yearly** | `"2026"` | раз в год (+ quarterly review) | только Ruslan (L3 strategic, I-11) |
| **Monthly** | `"2026-04"` | 1-го числа месяца | Ruslan + monthly ritual |
| **Weekly** | `"2026-W17"` | воскресенье/понедельник | Ruslan + weekly ritual |

**Fractal связь (опциональная в v1-beta):** yearly/monthly/weekly могут ссылаться
друг на друга через Obsidian transclude `![[2026-yearly#^north-star]]` — меняешь
yearly → каскадно видно везде.

**Обязательное поле `metric-50k-contribution`:** каждый period-файл должен
явно отвечать «как этот период двигает к $50K до 30.06.2026». Если пусто —
strategy drift, weekly review это ловит.

**Project-level стратегия:** `strategy/projects/{project-slug}/strategy.md` —
шаблон `templates/tpl-strategy-project.md` (T-05).

**Первые файлы v1-beta создаются в Шаге 6** (см. `design/IMPLEMENTATION-PLAN-2026-04-18.md` §6).
