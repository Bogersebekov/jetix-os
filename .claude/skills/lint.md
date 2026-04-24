---
name: lint
description: "Health check `${WIKI_ROOT}/` (default v3): 11 проверок per Q5 5-signal orchestration + структурные (orphans, stale, broken links, missing frontmatter, contradictions, missing cross-refs, index drift, α-2/α-3 lifecycle, triple-channel cross-refs, Q8 Layer-9 lock, symlink integrity)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3→v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /lint

## Описание

Проверка целостности `${WIKI_ROOT}/`. Находит проблемы, не чинит автоматически — только отчёт.

## Триггер

`/lint` — без аргументов. Или `/lint <niche>` — для одного niche.

## Проверки

### 1. Orphan pages

Страницы, на которые никто не ссылается (нет входящих `[[links]]` и нет в `${WIKI_ROOT}/graph/edges.jsonl`).

**Grep:** найти упоминания `[[slug]]` или `[slug](path)` в других файлах.

**Исключения:** `index.md`, `log.md`, `overview.md`, `_templates/*`, `niches/*/README.md`,
страницы с `tags: [#status/standalone]`.

### 2. Stale claims

`${WIKI_ROOT}/claims/*.md` где `confidence: low` И `updated:` старше 60 дней от сегодня. **Дополнительно: `${WIKI_ROOT}/foundations/*.md` где `last_reviewed:` старше 365 дней (Q5 §3 + D2 §2.3 foundations re-review).**

### 3. Broken wikilinks

`[[path]]` или `[text](relative-path)` указывающие на несуществующий файл.

### 4. Missing frontmatter

Markdown в `${WIKI_ROOT}/**/*.md` без обязательных полей per D2 §2.2 cross-layer:
`id, title, type, layer, niche, created, last_modified, pipeline, state, confidence, tier, produced_by, sources, related, topics, captured_by, captured_date`.

Исключения: `index.md`, `log.md`, `.gitignore`, `_templates/*` (у них свой frontmatter).

### 5. Contradictions

Для каждой пары (A, B), соединённой edge `contradicts` — проверить, что:
- Обе страницы существуют.
- В обеих упомянута противоположная в секции `## Связи`.

### 6. Missing cross-refs

Страница A упомянута в 3+ других страницах, но её нет в `related:` frontmatter тех страниц.

### 7. Index drift

- Файл есть в `${WIKI_ROOT}/`, но его нет в `index.md` (в соответствующей секции).
- Наоборот: в index.md есть строка, но файла нет.

### 8. α-2/α-3 lifecycle state validity (per Q5 signal #2)

Для страниц под `${WIKI_ROOT}/skills/` ИЛИ с `type: skill`:
flag pages with `state ∉ {candidate, learning, active, tombstoned}`
(α-3 4-state lock per D2 §2.4 Layer 8).

Для остальных страниц: flag pages with
`state ∉ {drafted, reviewed, revised, accepted, referenced, superseded, retired, tombstoned}`
(α-2 8-state set per D5 §5.3).

### 9. Triple-channel cross-ref consistency (per D2 §2.2 lint #5)

Каждый inline wikilink матчинг `\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]`
(non-matching forms like `[[A]]` or `[[file.md]]` warned as legacy/unparseable,
not errored) MUST появляться в `related[]` AND produce one record in
`${WIKI_ROOT}/graph/edges.jsonl`.

### 10. Q8 Layer-9 lock (per D1 §1.6)

Flag the existence of any file under `${WIKI_ROOT}/insights/{candidates,promoted}/*.md`
(any leaf `.md` write outside `README.md`) when D1 §1.6 boilerplate is in
effect. Per Q8 `phase_a_lock: true`.

<!-- TODO(cycle-3+): check #12 reserved for future slug; OPP-04 (cycle-2-impl 2026-04-24) claimed slot #13 per artefact §3.3. Backfill #12 from prior /lint design notes or skip numbering when backfill unclear. -->

### 11. Symlink integrity (per D9 §9.7)

For each `.md` file in `.claude/skills/`:
- if file is a symlink:
  - EMIT "broken symlink" if target doesn't exist
  - EMIT "symlink target outside active/" if not `../../swarm/wiki/skills/active/`
  - EMIT "symlink basename mismatch" if target basename != file basename

### 13. `cell_acceptance_predicate` present in all WBS cells (per OPP-04 §3.3, cycle-2-impl)

Two slugs emitted:

- **`cell-ap-missing`** — field absent in ≥1 cell row in any file matching
  `swarm/wiki/proposals/*-decomposition.md`. Measured as
  `count(^ *cell_acceptance_predicate:) < count(^ *- cell:)` in the same file.
- **`cell-ap-trivial`** — field present but (a) fails length regex `^.{20,200}$`
  OR (b) matches the case-insensitive anti-regex
  `^(artefact exists|file is non-empty|file exists|expected_artefact returned|non-empty file|returns output|2[x×]( improvement)?( vs baseline)?$)`.
  Artefact-existence phrasings are AP-MGMT-1 violations per brigadier §4.1.

**Bash implementation (target ~25 lines; callable against a single decomposition
file OR a glob):**

```bash
#!/usr/bin/env bash
# /lint check #13 — cell_acceptance_predicate present + non-trivial
# Usage: bash check-13.sh <decomposition-file>  (or: <glob>)
# Exits 0 on pass; 1 on any FAIL with slug emitted to stderr.
set -euo pipefail
file="$1"
cells=$(grep -c "^ *- cell:" "$file" || true)
preds=$(grep -c "^ *cell_acceptance_predicate:" "$file" || true)
if (( preds < cells )); then
  echo "FAIL cell-ap-missing: $file ($preds of $cells cells carry field)" >&2
  exit 1
fi
# extract every predicate value and validate
grep -E "^ *cell_acceptance_predicate:" "$file" |
  sed -E 's/^ *cell_acceptance_predicate: *//; s/^"(.*)"$/\1/; s/^ *# .*$//' |
  while IFS= read -r val; do
    [[ -z "$val" ]] && continue
    len=${#val}
    if (( len < 20 || len > 200 )); then
      echo "FAIL cell-ap-trivial: $file — predicate length $len (want 20..200): $val" >&2
      exit 1
    fi
    if echo "$val" | grep -qEi '^(artefact exists|file is non-empty|file exists|expected_artefact returned|non-empty file|returns output|2[x×])'; then
      echo "FAIL cell-ap-trivial: $file — predicate matches anti-regex: $val" >&2
      exit 1
    fi
  done
echo "OK"
exit 0
```

**Pass condition (Hamel-binary):** for every `swarm/wiki/proposals/*-decomposition.md`
file, `count(cell_acceptance_predicate:) == count(- cell:)` AND every predicate
value matches `^.{20,200}$` AND no predicate matches the anti-regex. Else
`/lint` emits the failing slugs and exits 1.

**Helper runner:** `swarm/evals/run-check-13.sh` takes a single decomposition
file as argument and exits 0/1 per the spec (created by Part C of cycle-2-impl).

## Выход

`${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md`:

```yaml
---
type: lint-report
date: YYYY-MM-DD
checks: 7
---
```

```markdown
# Lint Report — YYYY-MM-DD

## Summary
- Orphans: N
- Stale claims: N
- Broken links: N
- Missing frontmatter: N
- Contradictions issues: N
- Missing cross-refs: N
- Index drift: N (missing in index: X, dangling entries: Y)

## Details

### 1. Orphans
- [[...]] — последний апдейт YYYY-MM-DD
  Hint: добавить в related у ... или удалить

### 2. Stale claims
...

### 3. Broken links
- ${WIKI_ROOT}/concepts/foo.md → [[bar]] (нет такого файла)

...
```

## Правила

- Не удалять / не править другие файлы.
- Только отчёт. Действия — вручную через `/consolidate` или правки.
- Приоритеты: broken links и missing frontmatter — высокий; orphans / stale — средний.
- Добавить запись в `${WIKI_ROOT}/log.md`:
  `## [YYYY-MM-DD] lint | report | issues: N`
