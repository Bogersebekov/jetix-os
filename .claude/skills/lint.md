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

### 14. L-DANGLING-EDGE — dangling edge detection

For each record in `${WIKI_ROOT}/graph/edges.jsonl` (skip comment lines):
- Parse `from` and `to` fields.
- Resolve both as paths relative to `${WIKI_ROOT}` (strip leading `../` segments for cross-tree refs first).
- For intra-tree edges: check `os.path.exists(${WIKI_ROOT}/<from>)` AND `os.path.exists(${WIKI_ROOT}/<to>)`.
- For cross-tree refs (`type: cross-tree-ref`): check only that the `from` file exists (destination is in v2 tree; checked separately).

**Flag:** `L-DANGLING-EDGE` — edge at line N: from <from> OR to <to> does not exist.

**Severity:** HIGH (dangling edges corrupt Tier-C BFS retrieval).

### 15. L-ORPHAN-CONCEPT — orphan concept detection

For each `.md` file under `${WIKI_ROOT}/concepts/`:
- Check whether it has ≥1 inbound OR outbound edge in `${WIKI_ROOT}/graph/edges.jsonl`
  (i.e., any record where `from` or `to` matches this file's path relative to `${WIKI_ROOT}`).

**Flag:** `L-ORPHAN-CONCEPT` — `concepts/<slug>.md` has zero edges (inbound+outbound).

**Severity:** MEDIUM (orphan concepts are unreachable via Tier-C BFS; may indicate stale pages or missed edges after ingest).

**Exclusions:** `concepts/_index.md` if present.

### 16. L-MISSING-FRONTMATTER — mandatory field enforcement

For each `.md` file under `${WIKI_ROOT}/` (excluding `index.md`, `log.md`, `_templates/*`, `graph/*`, `_archive/*`, `niches/*/README.md`):
- Parse YAML frontmatter (content between first `---` delimiters).
- Verify ALL mandatory fields present (non-null, non-empty):
  `title`, `type`, `created`, `pipeline`, `state`, `confidence`, `confidence_method`, `tier`, `produced_by`, `sources`.

**Flag:** `L-MISSING-FRONTMATTER` — `<path>`: missing fields: [field1, field2, ...].

**Severity:** HIGH (missing frontmatter breaks Tier-B grep filtering + provenance gate §2).

**Note:** `sources: []` (empty list) is acceptable only for bootstrap/seed pages (`pipeline: raw`). For `pipeline ∈ {compiled, linted, ready, accepted}`, `sources` must be non-empty.

### 17. L-DUPLICATE-SLUG — cross-subtree duplicate basename detection

Walk all `.md` files under `${WIKI_ROOT}/`. Group by `basename` (filename without directory).
For each basename appearing ≥2 times in different subdirectories:
- If files are symlinks pointing to the same target → acceptable (intentional per-niche symlink). Skip.
- Otherwise → flag.

**Flag:** `L-DUPLICATE-SLUG` — basename `<slug>.md` appears at: <path1>, <path2>.

**Severity:** MEDIUM (may indicate accidental duplication; may cause Tier-B grep to return two pages for one slug).

**Exclusions:** `index.md`, `log.md`, `README.md`, `health.md` (expected in multiple dirs).

### 18. L-CROSS-CLIENT-GLOBAL — cross-client global contamination (hard error)

**Activates only when `WIKI_ROOT_CLIENT_ID` env-var is set** (i.e., skill is running in client-scoped mode).

For each `.md` file under `${WIKI_ROOT}/global/`:
- Parse frontmatter `granularity:` field.
- If `granularity` matches `client:*` pattern → HARD ERROR.

**Flag:** `L-CROSS-CLIENT-GLOBAL` — `global/<path>`: artefact has granularity `<value>` which is client-scoped; global/ must only contain `granularity: jetix-internal` OR `granularity: global`.

**Severity:** HARD ERROR — triggers non-zero exit immediately; does not wait for full scan completion. Per A1 §5 UC-9 Layer-2: client-scoped content in global/ is a data-leak vector.

---

### --check-stage-gates (daily cron mode)

**Invocation:** `/lint --check-stage-gates [--project=<slug>] [--dry-run]`

When `--check-stage-gates` is passed, lint enters stage-gate evaluation mode.

**Algorithm:**

1. RESOLVE project scope:
   a. If --project=<slug> given: scope = single project at `${WIKI_ROOT}/operations/<slug>/_moc.md`
   b. Else: walk all `${WIKI_ROOT}/operations/*/` `_moc.md` files (recursive; skip `_archived/`).

2. For each `_moc.md` in scope:
   a. Parse YAML frontmatter via `python3 -c "import yaml, ..."`
   b. Extract `stage_gates:` block. If absent or empty: skip project.
   c. Check `project_type in {bets}` OR `adaptive: true` in frontmatter. If neither: skip.

3. For each SG entry where `state == "pending"`:
   a. Extract `predicate:` string.
   b. Call `tools/stage-gate-eval.py evaluate --project-root=${WIKI_ROOT}/operations/<slug>/ --predicate="<predicate-string>"`
   c. Receive: `{result: true|false, evidence: <string>}`
   d. If `result == false`: record as "predicate not yet met"; continue.
   e. If `result == true` AND `--dry-run`: log "DRY-RUN: SG-<N> would fire for <slug>; evidence: <evidence>"; continue without writing.
   f. If `result == true` AND NOT `--dry-run`:
      i.   Call auto-spawn logic (C.3 auto-spawn protocol).
      ii.  On successful spawn: set `state = "fired"`, `fired_at = <ISO8601 now>`, `spawned_paths = [...]`; write back `_moc.md`.
      iii. Append fire record to `${WIKI_ROOT}/meta/stage-gate-fires-<YYYY-MM-DD>.md`.
      iv.  On failed spawn (overwrite guard): escalate `peer-input-needed`; do NOT mark SG as fired.

4. After all projects processed: append summary row to `${WIKI_ROOT}/log.md`; surface in next weekly digest.

**Exit codes:** 0 = success (even if SGs fired); 1 = evaluator error; 2 = spawn blocked.

### --validate-predicate sub-flag (Hamel-binary guard)

**Invocation:** `/lint --check-stage-gates --validate-predicate <path-or-glob>`

Runs the philosophy-critic anti-regex list against every predicate string in `_moc.md:stage_gates.*.predicate` fields. Rejects non-Hamel-binary predicates BEFORE dispatch to evaluator.

Banned-phrase list sourced from `.claude/config/sg-banned-phrases.yaml` (single source of truth).

**Exit codes:** 0 = zero findings; 1 = ≥1 `L-SG-NON-BINARY` or `L-SG-NON-CANONICAL` finding.

Wired into `/project-bootstrap` and `/project-promote`: both skills invoke this sub-flag before declaring project state active.

---

## Signal: L-PROJECT-MISSING-REQUIRED-FRONTMATTER

**Scope:** every `_moc.md` under `${WIKI_ROOT}/operations/` AND
every `_moc.md` under `clients/*/swarm/wiki/operations/` (per-client projects).

**Trigger source:** `.claude/config/project-types.yaml` `required_frontmatter_fields` list.
The list is the canonical authority; changes to project-types.yaml auto-apply here.

**Algorithm:**

```python
# Pseudocode — implemented in lint.md's embedded logic
import yaml, glob, sys

WIKI_ROOT = resolve_wiki_root()  # per D7 §7.4

# Collect all _moc.md files under operations/ (Jetix-internal + per-client)
moc_paths = glob.glob(f"{WIKI_ROOT}/operations/**/_moc.md", recursive=True)
client_moc_paths = glob.glob("clients/*/swarm/wiki/operations/**/_moc.md", recursive=True)
all_mocs = moc_paths + client_moc_paths

# Load required_frontmatter_fields from config
config = yaml.safe_load(open(".claude/config/project-types.yaml"))
required_fields = config["required_frontmatter_fields"]

errors = []
warnings = []

for moc_path in all_mocs:
    fm = yaml.safe_load(open(moc_path).read().split("---")[1])
    priority = fm.get("priority", "")

    for field in required_fields:
        value = fm.get(field)

        if field == "problem_statement":
            if not value or str(value).strip() in ("", "null", "None"):
                errors.append(f"HARD-FAIL L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                              f"{moc_path} missing non-empty 'problem_statement'")

        elif field == "kill_criteria":
            if not value or str(value).strip() in ("", "null", "None"):
                errors.append(f"HARD-FAIL L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                              f"{moc_path} missing non-empty 'kill_criteria'")

        elif field == "kpi_targets":
            if priority in ("P1", "P2"):
                if not value or value == {}:
                    errors.append(f"HARD-FAIL L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                                  f"{moc_path} is {priority} but missing 'kpi_targets'")
            # P3/P4: kpi_targets optional; skip

        elif field == "pmbok_phase":
            if not value:
                warnings.append(f"WARN L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                                 f"{moc_path} missing 'pmbok_phase' (soft warning)")

        else:
            if not value:
                warnings.append(f"WARN L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                                 f"{moc_path} missing '{field}'")

if errors:
    print("\n".join(errors))
    sys.exit(1)

if warnings:
    print("\n".join(warnings))
```

**Hard-fail conditions (non-zero exit):**
- `problem_statement` missing or empty in any `_moc.md`
- `kill_criteria` missing or empty in any `_moc.md`
- `kpi_targets` missing or empty (`{}`) for any P1 or P2 project

**Soft-warn conditions (non-zero exit NOT triggered):**
- `pmbok_phase` missing in any `_moc.md`
- Any other required_frontmatter_fields entry missing

**`--project=<slug>` scoped mode:**
When `/lint --project=<slug>` is invoked (from project-brigadier's §2 Step 9),
scope is limited to `${WIKI_ROOT}/operations/<slug>/_moc.md` only.
Same hard-fail / warn rules apply within this narrower scope.

---

## Обновлённый report target

Lint report писать в `${WIKI_ROOT}/meta/lint-report-<YYYY-MM-DD>.md`
(изменена с `${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md` per A.9 spec — путь теперь под `meta/` для health.md интеграции).

Non-zero exit: если ANY hard-error check (broken links, L-MISSING-FRONTMATTER HIGH,
L-CROSS-CLIENT-GLOBAL, L-DANGLING-EDGE count > 0) fired.

Обновить Summary-секцию report:
```
## Summary
- L-DANGLING-EDGE: N
- L-ORPHAN-CONCEPT: N
- L-MISSING-FRONTMATTER: N
- L-DUPLICATE-SLUG: N
- L-CROSS-CLIENT-GLOBAL: N (HARD ERROR if >0 in client-scoped mode)
- L-PROJECT-MISSING-REQUIRED-FRONTMATTER: N
```

Обновить log.md entry:
```
## [YYYY-MM-DD] lint | report | issues: N | hard-errors: M
```

## Правила

- Не удалять / не править другие файлы.
- Только отчёт. Действия — вручную через `/consolidate` или правки.
- Приоритеты: broken links и missing frontmatter — высокий; orphans / stale — средний.
- Добавить запись в `${WIKI_ROOT}/log.md`:
  `## [YYYY-MM-DD] lint | report | issues: N`
