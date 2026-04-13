---
type: dashboard
tags:
  - home
created: 2026-04-13
---

# 🏠 Jetix OS — Dashboard

---

## 🎯 Быстрый доступ

| | |
|---|---|
| 📋 [[CLAUDE.md\|Master Context]] | 📐 [[_meta/conventions.md\|Конвенции]] |
| 📊 [[_meta/pipeline-spec.md\|Wiki Pipeline]] | 🧪 [[templates/tpl-daily.md\|Шаблон дня]] |
| 💰 [[projects/quick-money/overview.md\|Quick Money — Overview]] | 👤 [[crm/icp.md\|ICP профиль]] |

---

## 📂 Проекты

> [!tip] Активные проекты — `projects/`

| Приоритет | Проект | Статус |
|-----------|--------|--------|
| 🔴 P1 | [[projects/quick-money/overview.md\|💰 Quick Money]] | Active |
| 🟠 P2 | [[projects/research/CONTEXT.md\|🔬 Research]] | Active |
| 🟠 P2 | [[projects/brand/CONTEXT.md\|🏷️ Brand Jetix]] | Active |
| 🟠 P2 | [[projects/ai-tools/CONTEXT.md\|🛠️ AI Tools]] | Active |
| 🟡 P3 | [[projects/community/CONTEXT.md\|👥 Community]] | Planned |
| 🟡 P3 | [[projects/life-os/CONTEXT.md\|🧬 Life OS]] | Active |
| 🟡 P3 | [[projects/engineering-thinking/CONTEXT.md\|⚙️ Engineering Thinking]] | Active |
| ⚪ P4 | [[projects/bets/CONTEXT.md\|🎲 Bets]] | Paused |

### Quick Money — навигация

- [[projects/quick-money/plan.md|📋 План]]
- [[projects/quick-money/log.md|📝 Лог]]
- [[projects/quick-money/decisions.md|⚖️ Решения]]
- [[projects/quick-money/questions.md|❓ Вопросы]]
- [[projects/quick-money/resources.md|📚 Ресурсы]]

---

## 🧠 База знаний

> [!abstract] Knowledge Base — `knowledge-base/`

### AI Consulting
- [[knowledge-base/ai-consulting/_moc.md|📌 MOC — AI Consulting]]
- [[knowledge-base/ai-consulting/icp-analysis.md|ICP Analysis]]
- [[knowledge-base/ai-consulting/ai-readiness-assessment.md|AI Readiness Assessment]]
- [[knowledge-base/ai-consulting/leadgen-stack.md|Leadgen Stack]]
- [[knowledge-base/ai-consulting/market-analytics-smb.md|Market Analytics SMB]]
- [[knowledge-base/ai-consulting/operational-plan.md|Operational Plan]]
- [[knowledge-base/ai-consulting/hypotheses-quick-money.md|Hypotheses Quick Money]]
- [[knowledge-base/ai-consulting/claude-gemini-power.md|Claude & Gemini Power]]
- [[knowledge-base/ai-consulting/workspace-architecture.md|Workspace Architecture]]

### Другие кластеры
- `knowledge-base/market/` — *пусто*
- `knowledge-base/sales/` — *пусто*
- `knowledge-base/_health/` — *пусто*

---

## 💡 Идеи

[[ideas/bank.md|🏦 Банк идей]]

---

## 👥 CRM

[[crm/icp.md|🎯 Ideal Customer Profile]]

---

## 📅 Сегодня

> [!note] Ежедневные заметки — `daily-log/`

*Используй `/plan-day` для создания плана дня.*



---

## 🕐 Последние изменения

```dataview
TABLE file.mtime AS "Изменён", file.folder AS "Папка"
FROM ""
WHERE file.name != "HOME"
SORT file.mtime DESC
LIMIT 10
```

---

## 📊 Статистика KB

```dataview
TABLE length(rows) AS "Статей"
FROM "knowledge-base"
WHERE file.name != "_moc"
GROUP BY file.folder AS "Кластер"
```

---

*Jetix OS v1.0 · Obsidian + Claude Code*
