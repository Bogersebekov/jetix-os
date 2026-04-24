---
name: consolidate
description: "Найти дубликаты в `${WIKI_ROOT}/` и предложить merge. Поддерживает --weekly (ISO-week digest), --dry-run, --quiet."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.7"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§5 UC-2"}
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3->v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /consolidate

## Описание

Объединение дубликатов в `${WIKI_ROOT}/`. Не мержит автоматически — всегда confirm от пользователя.
Флаг `--weekly` генерирует ISO-week digest вместо dedup scan.

## Триггер

- `/consolidate` — пройтись по всей wiki (dedup scan).
- `/consolidate <type>` — только один type.
- `/consolidate <niche>` — только в одном niche.
- `/consolidate --weekly` — сгенерировать weekly digest.
- `/consolidate --weekly --dry-run` — вывести digest в stdout, не писать файл.
- `/consolidate --weekly --quiet` — писать файл без progress logs.

## Алгоритм A — Dedup scan (default, без --weekly)

### 1. Собрать кандидатов

Попарная проверка внутри одного type:
1. Одинаковые/похожие `title` (normalized: lowercase, без пробелов/дефисов).
2. Одинаковые/похожие slug.
3. 70%+ пересечения по словам в теле.
4. Одинаковая entity_kind / topic.

### 2. Для каждой пары — diff

```
CANDIDATE MERGE:
  A: ${WIKI_ROOT}/concepts/value-based-pricing.md (4 sources, 120 lines)
  B: ${WIKI_ROOT}/concepts/value-pricing.md (2 sources, 80 lines)
  Reason: 85% overlap, похожий title
  A unique: [...], B unique: [...], Common: [...]
  Предлагаемый merge: A остаётся, B мержится в A. Ссылки на B: N файлов.
  [y] merge, [n] skip, [s] skip all similar
```

### 3. После confirm (`y`)

1. Объединить frontmatter (title — длиннее; sources/related/tags — union; confidence — минимум; updated — сегодня).
2. Объединить тело (уникальные секции из обоих; общие — из A).
3. Обновить внешние ссылки (grep `[[B]]` → заменить на A в edges.jsonl + cross-tree.jsonl + index.md).
4. Архивировать B в `${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md` с HTML-комментом:
   `<!-- merged into A on YYYY-MM-DD per /consolidate; α-2 state transition pending brigadier review -->`.
   (brigadier затем: `state: superseded` + `superseded_by: [[A]]` per D5.)
5. Логировать в `${WIKI_ROOT}/log.md` (сверху):
   ```
   ## [YYYY-MM-DD] consolidate | merge | A <- B
   A: ${WIKI_ROOT}/concepts/...  B (archived): _archive/YYYY-MM-DD-B.md
   Updated refs in: N files
   ```

### 4. Skip / Skip all

- `n` — пропустить пару, продолжить.
- `s` — пропустить все похожие данного type в текущей сессии.

## Алгоритм B — Weekly digest (`--weekly`)

### B.1 Определить ISO-неделю

```python
import datetime
today = datetime.date.today()
iso_year, iso_week, _ = today.isocalendar()
week_label = f"{iso_year}-W{iso_week:02d}"  # e.g. "2026-W17"
```

### B.2 Walk log.md for last 7 days

Прочитать `${WIKI_ROOT}/log.md`. Извлечь все записи с датами в диапазоне `[today-7d, today]`.
Из каждой записи извлечь: niche, created page slugs, edge counts.

### B.3 Группировка по niche + top-5

Для каждого из 6 niches (personal/business/sales/life/tech/meta):
- Собрать все страницы, созданные/обновлённые за 7 дней.
- Вычислить edge-degree каждой (из edges.jsonl, `from == page OR to == page`).
- Взять top-5 по degree.

### B.4 Emergent theme clusters

Из edges.jsonl взять только записи с `ts >= today-7d` (7-дневный подграф).
Найти связные компоненты (BFS/DFS по смежности from/to) в этом подграфе.
Clusters ≥3 nodes = "emergent theme". Имя кластера = slug с максимальным degree.

### B.5 Render digest

```markdown
---
title: "Weekly digest <week_label>"
type: digest
week: <week_label>
created: <today>
niche: meta
pipeline: ready
state: accepted
confidence: medium
confidence_method: automated-log-walk
tier: tier-internal
produced_by: consolidate-weekly
sources:
  - {path: "${WIKI_ROOT}/log.md", range: "last 7 days"}
  - {path: "${WIKI_ROOT}/graph/edges.jsonl", range: "ts >= <today-7d>"}
---

# Weekly digest <week_label>

## New pages this week (by niche)

### personal (N pages)
- [Page title](concepts/slug.md) — edge-degree: D

### business (N pages)
...

## Top edges this week

| From | To | Type | Count |
|------|----|------|-------|
| [src:...] | [src:...] | supports | 3 |

## Emergent themes (clusters >=3 nodes)

### Theme: <cluster-name>
Pages: [A], [B], [C], ...
Dominant edge types: supports(3), derived_from(2)

## Citations resolved

N new sources[] entries pointing to existing wiki pages this week.

---
_Generated by /consolidate --weekly at <datetime>. Zero LLM calls._
```

**Empty-week handling:** if no new pages — render "no new pages this week" in all sections
and still write the file (cron-idempotent).

### B.6 Write or dry-run

- `--dry-run`: вывести digest в stdout; не писать файл; не обновлять log.
- Default: записать в `${WIKI_ROOT}/digests/<week_label>.md`.
- `--quiet`: писать файл без промежуточных progress logs.

### B.7 Append log row

```
## [YYYY-MM-DD] consolidate | weekly | <week_label>
weekly digest <week_label> generated; N pages summarised.
```

## Правила

- Никогда не мержить без `y` (dedup mode).
- Никогда не удалять без архива.
- Не трогать `_templates/`, `index.md`, `log.md`, `niches/*/README.md`.
- Если у страницы 10+ входящих ссылок — двойной confirm (dedup mode).
- `--weekly` никогда не мержит / не удаляет страницы; только читает и пишет digest.

## Cron-ready wiring

Файл документации расписания (НЕ устанавливается автоматически):
`tools/cron/consolidate-weekly.cron`

```cron
# /consolidate --weekly — Sunday 21:00 CET (UTC+1 CET = UTC+2 CEST in summer)
# Run from repo root. Requires: WIKI_ROOT env-var set or default swarm/wiki/.
# NOT auto-installed; operator activates via: crontab tools/cron/consolidate-weekly.cron
0 19 * * 0 cd /path/to/jetix-os && /consolidate --weekly --quiet
```

## Отчёт после сессии

```
Dedup mode: рассмотрено N пар, смерджено M, скипнуто K.
Weekly mode: digest <week_label> written to ${WIKI_ROOT}/digests/<week_label>.md.
```
