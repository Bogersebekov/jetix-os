---
type: design-document
status: archived
owner: ruslan
created: 2026-04-18
---

<!--
Архив numbered-версий папок проектов (01-research…08-bets), которые
содержали только `CONTEXT.md` и были удалены из canonical структуры в
рамках Шага 4 плана v1-beta (B-4.1 default resolution).
-->

# `projects/_archive/` — legacy numbered project folders

**Что здесь.** Восемь папок `NN-<slug>/` с единственным файлом `CONTEXT.md` —
это исторические scaffolds (создавались 2026-04-13), предшествующие
canonical named-версии (`projects/quick-money/`, `projects/research/`, …).

**Зачем архивировали, а не удалили.** `CONTEXT.md` каждой папки содержит
уникальное описание (~1KB каждый) — это ценный контекст для первоначального
замысла проекта. При написании overview.md для named-версий (Шаг 6 или
позже) можно подтянуть ключевые формулировки отсюда.

**Mapping numbered → named canonical:**

| Archived | Canonical |
|----------|-----------|
| `01-research/` | `projects/research/` |
| `02-business/` | `projects/quick-money/` |
| `03-community/` | `projects/community/` |
| `04-ai-tools/` | `projects/ai-tools/` |
| `05-life-os/` | `projects/life-os/` |
| `06-engineering/` | `projects/engineering-thinking/` |
| `07-brand/` | `projects/brand/` |
| `08-bets/` | `projects/bets/` |

**Когда удалять полностью.** После того как содержимое `CONTEXT.md` каждой
архивной папки будет интегрировано в соответствующий `projects/<name>/overview.md`
(шаблон T-01) — эту папку можно удалить. Решение по удалению — за Ruslan'ом
в рамках Шага 6 или позже.

**Status:** `archived` — не трогаем, не редактируем, не ссылаемся из active
документации.
