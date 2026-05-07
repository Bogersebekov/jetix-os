---
name: mermaid-validate
description: "Проверяет Mermaid диаграмму на синтаксические ошибки и compliance с Jetix style guide. Используй когда: проверь диаграмму, mermaid-validate, lint mermaid, syntax check, прежде чем pushнуть."
disable-model-invocation: true
allowed-tools: Read Glob Grep Bash(grep *) Bash(awk *) Bash(wc *) Bash(test *)
---

# /mermaid-validate — Валидация Mermaid диаграммы

## Назначение

Standalone syntax check + style-guide compliance check для `.md` файлов с Mermaid блоками. Не требует mmdc / external tooling. Чисто regex / parser.

## Аргументы

- `<file-or-glob>` (обязательно) — path к `.md` файлу или glob (e.g. `swarm/wiki/synthesis/diagrams-2026-05-07/*.md`)
- `--strict` (опционально) — fail на warnings (по default warnings — non-blocking)

## Шаг 1: Resolve file list

Если `<file-or-glob>` содержит wildcard — Glob tool. Иначе — single file Read.

Для каждого файла иди по checks ниже. Aggregate report в конце.

## Шаг 2: Извлечь mermaid block(s)

Если `.md` не содержит ` ```mermaid ` — skip с note "no mermaid block".

Извлечь content между ` ```mermaid ` и ` ``` ` (могут быть множественные блоки — обработай каждый).

## Шаг 3: Syntax checks (per block)

### C1. Init directive present

Первая non-empty строка mermaid block должна быть `%%{init: ...}%%` (canonical per style guide §4).

- ❌ если отсутствует: **WARNING** — diagram render будет с default theme, inconsistent с canonical

### C2. Diagram type declaration

Вторая non-empty строка должна быть одним из: `flowchart TB|LR|BT|RL`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `gantt`, `pie`, `journey`, `gitGraph`, `mindmap`, `timeline`, `quadrantChart`, ...

- ❌ если отсутствует: **ERROR** — diagram не рендерится

### C3. Bracket balance

Подсчитать pairs:
- `[` and `]` — должны совпадать count
- `(` and `)` — должны совпадать
- `{` and `}` — должны совпадать
- ` ``` ` (triple backtick) opens должны иметь closes

Используй `grep -o` + `wc -l` или awk character counting.

- ❌ mismatch — **ERROR** — diagram не рендерится

### C4. Subgraph / end balance

Count `subgraph` keyword vs `end` keyword. Должны быть равны (хотя `end` может также появляться в state diagrams для `[*] --> end` — distinguish: в flowchart context, `end` после subgraph closes a subgraph; otherwise it's a node ID, что само по себе bug).

```bash
SUBGRAPHS=$(grep -cE '^\s*subgraph\b' <mermaid block>)
ENDS=$(grep -cE '^\s*end\s*$' <mermaid block>)
```

- ❌ mismatch — **ERROR**

### C5. classDef references resolved

Для каждого `:::className` apply — должен быть `classDef className ...` declaration в том же block.

```
applies = grep -oE ':::[a-zA-Z_][a-zA-Z0-9_]*' | sort -u
classes_defined = grep -oE '^\s*classDef\s+[a-zA-Z_][a-zA-Z0-9_]*' | awk '{print $2}' | sort -u
unresolved = applies - classes_defined
```

Аналогично для `class A,B,C name` syntax.

- ❌ если есть unresolved: **WARNING** — node renders без styling

### C6. Reserved keywords as node IDs

Список keywords: `end`, `class`, `style`, `subgraph`, `direction`, `click`, `link`, `classDef`, `linkStyle`, `flowchart`, `graph`.

Если node defined как reserved keyword (`end[Text]`, `class --> X`) — error.

- ❌ **ERROR**

### C7. Subgraph nesting depth

Track running depth of `subgraph ... end` pairs. Max depth >2 — warning.

- ⚠️ **WARNING** if depth >2 (per style guide §7.2 #3)

## Шаг 4: Style-guide compliance checks

### S1. Init directive matches canonical

Compare init directive против §4 canonical. Допустимы variations в whitespace внутри JSON, но keys + values должны matchать.

Canonical reference:
```
'theme':'base'
'primaryColor':'#fff8e1'
'primaryTextColor':'#000'
'primaryBorderColor':'#f57c00'
'lineColor':'#555'
'fontFamily':'Inter, system-ui, sans-serif'
'fontSize':'14px'
```

- ⚠️ deviation in `theme` или цветов — **WARNING** (might be intentional, surface for review)

### S2. Color palette compliance

Список разрешённых цветов из §1 (fills + strokes — extract в reference list):

Allowed fills: `#e8eaf6`, `#ffebee`, `#e0f2f1`, `#fce4ec`, `#fff3e0`, `#f3e5f5`, `#e1f5fe`, `#e3f2fd`, `#fff8e1`, `#e8f5e9`, `#bbdefb`, `#90caf9`, `#64b5f6`, `#42a5f5`, `#1e88e5`.

Allowed strokes: `#283593`, `#c62828`, `#00695c`, `#ad1457`, `#e65100`, `#6a1b9a`, `#01579b`, `#1565c0`, `#f57c00`, `#2e7d32`, `#0d47a1`, `#555`.

Найти hex colors в classDef / style declarations. Если color вне list — warning.

- ⚠️ **WARNING** — color outside palette (might need style guide extension)

### S3. Naming conventions

- Node IDs: проверить что они в основном UPPER_SNAKE_CASE. Допустимы tiny throwaway diagrams (≤5 nodes) с `A`, `B`, `C`, но big diagrams (>10 nodes) с camelCase / lowercase — warning.
- classDef names: snake_case. Если PascalCase / camelCase — warning.
- Subgraph IDs: UPPER_CASE single word.

### S4. classDef location

classDef declarations должны быть после ВСЕХ edges, в логическом блоке внизу diagram. Если classDef разбросан по всему body — warning.

### S5. FontAwesome / external image usage

`fa:fa-` или `img:` в node labels — warning ("won't render on GitHub or Notion per style guide §7.2").

### S6. `@{shape: ...}` extended syntax

`@{shape:` substring — warning (verify-on-demand per style guide §7.2 #7).

## Шаг 5: Frontmatter checks

- [ ] Frontmatter present (`---` at top)
- [ ] Required fields: `title`, `date`, `type`, `source`, `audience`, `purpose`
- [ ] `date` matches `YYYY-MM-DD` format
- [ ] `F`, `G`, `R` triple present (style guide §6 file structure standard)

- ⚠️ если missing fields — **WARNING**

## Шаг 6: Aggregate report

Output format:

```
=== Mermaid validate report ===
Files scanned: <N>
Mermaid blocks total: <M>

❌ ERRORS (<count>):
  <file>:<block#> - <error description>
  ...

⚠️ WARNINGS (<count>):
  <file>:<block#> - <warning description>
  ...

✅ <file>: clean
✅ <file>: clean
...

Result: <PASS | FAIL (errors found) | PASS WITH WARNINGS>
```

## Шаг 7: Exit code

- 0 — clean OR warnings only (без `--strict`)
- 1 — errors found, OR warnings + `--strict`

## Правила

1. Это standalone tool — не требует mmdc / npm / external network.
2. Не fix-в-place — read-only check. Surface findings, user fixes manually OR runs `/mermaid-iterate`.
3. False positives возможны (color check, naming) — surface как WARNING, не ERROR.
4. ERRORS блокируют render; WARNINGS — style-guide deviation (might be intentional).

## Cross-references

- Style guide: `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` — canonical reference
- Iterate skill: `/mermaid-iterate` — для fix found issues
- Create skill: `/mermaid-create` — для new diagrams (style-compliant by construction)
