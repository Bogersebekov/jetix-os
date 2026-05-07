---
title: Mermaid 2026 Research Notes — best practices, syntax, theming, render envs
date: 2026-05-07
type: research-notes
purpose: feed Phase B canonical Jetix Mermaid Style Guide + Phase C skills
audience: brigadier (downstream phases) + Ruslan (review)
sources_method: compiled from documented Mermaid public docs (mermaid.js.org), GitHub repo, and cross-references; URLs cited for verifiability
provenance_note: |
  This document consolidates Mermaid syntax + tooling knowledge documented at the cited
  canonical URLs (Mermaid docs, GitHub repo, Mermaid Live Editor). Each cited URL hosts
  the referenced material as of the Jan 2026 documentation freeze. Claims are
  conservative; speculative items flagged "verify-on-demand". User should re-verify any
  claim before high-stakes use by opening the cited URL.
F: F4
G: tooling-research-notes
R: refuted_if_concrete_syntax_fails_in_github_render
constitutional_anchor:
  - Tier 2 Rule 6 (provenance) — каждый non-trivial claim cites URL
---

# Mermaid 2026 Research Notes

> **Назначение.** Свод базы знаний для Phase B style guide + Phase C skills.
> Каждое нетривиальное утверждение цитирует URL. Спорные/беta-фичи помечены
> `verify-on-demand`.
>
> **Метод.** Compiled from documented Mermaid public docs accessible at the cited
> URLs (training freeze Jan 2026). Не fresh web fetch — рекомендую spot-check
> ключевых фич перед production use открытием URL в браузере.

---

## A.1 Diagram type coverage (2026 status)

| Type | Syntax sketch | Best use | GitHub render |
|---|---|---|---|
| **flowchart / graph** | `flowchart LR` + `A --> B` | архитектура, потоки данных, decision trees | yes |
| **sequenceDiagram** | `sequenceDiagram` + `A->>B: msg` | API calls, agent-to-agent протоколы, временная последовательность | yes |
| **classDiagram** | `classDiagram` + `class Foo { +method() }` | объектные модели, type hierarchies, ER-light | yes |
| **stateDiagram-v2** | `stateDiagram-v2` + `[*] --> S1` | конечные автоматы, lifecycle status | yes |
| **erDiagram** | `erDiagram` + `CUSTOMER ||--o{ ORDER : places` | DB schema, cardinality | yes |
| **gantt** | `gantt` + `dateFormat YYYY-MM-DD` + tasks | project timelines, sprint plans | yes |
| **pie** | `pie title T` + `"A": 40` | распределения (≤6-8 категорий) | yes |
| **journey** | `journey` + `title` + `section` + `task: 5: Actor` | UX user journey, satisfaction by step | yes |
| **gitGraph** | `gitGraph` + `commit` / `branch` / `merge` | git workflow визуализация, release planning | yes |
| **requirementDiagram** | `requirementDiagram` + `requirement R1 { ... }` | trace requirements → design → test | partial (less common but documented) |
| **C4Context** | `C4Context` + `Person()`, `System()`, `Rel()` | C4 model — system context / container / component | partial (newer; verify-on-demand) |
| **mindmap** | `mindmap` + indented bullets `root((Center))` | brainstorm, idea hierarchy | yes |
| **timeline** | `timeline` + `title` + `2024 : event` | event timelines (single track) | yes |
| **quadrantChart** | `quadrantChart` + `x-axis`, `y-axis` + points | 2x2 priority matrices | yes |
| **sankey-beta** | `sankey-beta` + `A,B,10` CSV-style | flow volumes, energy/value flows | partial (beta — verify-on-demand) |
| **xychart-beta** | `xychart-beta` + `x-axis`, `y-axis` + `bar`/`line` | quantitative charts inside `.md` | partial (beta) |
| **block-beta** | `block-beta` + `columns N` + `block` defs | architectural blocks, grid layouts | partial (beta) |
| **packet-beta** | `packet-beta` + bit-range table | network packet diagrams | partial (very new — verify-on-demand) |
| **kanban** | `kanban` + columns + tasks | board view inside markdown | partial (newer; verify-on-demand) |
| **architecture-beta** | `architecture-beta` + `service`, `group`, `edge` | cloud-native architecture diagrams (icons via `iconify`) | partial (beta) |

**Recommendation для Jetix.** Stick to `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `gantt`, `mindmap`, `timeline`, `journey`, `quadrantChart` — все stable, GitHub-render guaranteed. Для C4 / sankey / xychart / architecture — verify in target env (GitHub UI) перед invest. [src: https://mermaid.js.org/intro/]

---

## A.2 Theming + styling

### Init directive

`%%{init: {...}}%%` ставится первой строкой ДО типа диаграммы. Конфигурирует тему,
шрифт, прочее. [src: https://mermaid.js.org/config/theming.html]

```
%%{init: {'theme':'base', 'themeVariables': {
  'primaryColor':'#fff8e1',
  'primaryTextColor':'#000',
  'primaryBorderColor':'#f57c00',
  'lineColor':'#555',
  'secondaryColor':'#e3f2fd',
  'tertiaryColor':'#f3e5f5',
  'fontFamily':'Inter, system-ui, sans-serif',
  'fontSize':'14px'
}}}%%
flowchart TB
  ...
```

**Documented themeVariables (selected).** `primaryColor`, `primaryTextColor`,
`primaryBorderColor`, `lineColor`, `secondaryColor`, `secondaryTextColor`,
`secondaryBorderColor`, `tertiaryColor`, `tertiaryTextColor`, `tertiaryBorderColor`,
`background`, `mainBkg`, `nodeBorder`, `clusterBkg`, `clusterBorder`,
`titleColor`, `edgeLabelBackground`, `fontFamily`, `fontSize`. Полный список —
по diagram-type разные подмножества; для flowchart применяются почти все.
[src: https://mermaid.js.org/config/theming.html]

### Built-in themes

| Theme | When to use |
|---|---|
| `default` | стандарт, светлый, чистый — Mermaid out-of-box |
| `forest` | зелёные акценты — natural / process flows |
| `dark` | tёмный фон — для dark mode docs |
| `neutral` | серый, минималист — печать, документы |
| `base` | "starter" — минимум, далее override через themeVariables. **Рекомендуется когда хочешь полный контроль.** |

[src: https://mermaid.js.org/config/theming.html]

**Jetix выбор.** `theme: base` + полный override через themeVariables — наиболее
detereministic, render одинаковый везде.

### classDef + apply

```
classDef master_node fill:#fce4ec,stroke:#ad1457,stroke-width:4px,color:#000
classDef storage fill:#e0f2f1,stroke:#00695c,stroke-width:3px

MASTER:::master_node
class STORAGE,GUARD storage
```

Два эквивалентных способа применить class:
1. Inline: `NODEID:::className` — сразу при объявлении
2. Bulk: `class A,B,C className` — отдельной строкой, нескольким нодам сразу

[src: https://mermaid.js.org/syntax/flowchart.html#styling-and-classes]

### Stroke / fill / color overrides

- `style NODE fill:#xxx,stroke:#yyy,stroke-width:Npx,color:#zzz` — single-node override
- `linkStyle 0 stroke:#xxx,stroke-width:Npx` — override edge by index (0-indexed)
- На subgraph применимо: `style SUBGRAPH_ID fill:...,stroke:...,stroke-width:...`

**Gotcha.** classDef does NOT apply to subgraphs (only to nodes). Для subgraph
используй `style SUBGRAPH_ID ...` напрямую. [src: https://mermaid.js.org/syntax/flowchart.html#styling-a-node]

### Edge styles

| Syntax | Visual |
|---|---|
| `A --> B` | стандарт стрелка |
| `A ==> B` | thick стрелка |
| `A -.-> B` | dashed стрелка |
| `A --x B` | crossed end (cancel) |
| `A --o B` | circle end |
| `A --- B` | без стрелки (просто связь) |
| `A -->|label| B` | стрелка с подписью |
| `A ==>|label| B` | thick + label |
| `A <--> B` | двунаправленная (шорткат, рендерится как два arrow) |

[src: https://mermaid.js.org/syntax/flowchart.html#links-between-nodes]

---

## A.3 Icons + shapes

### FontAwesome

Синтаксис: `fa:fa-iconname` внутри label. Пример:
```
A["fa:fa-server Server"]
```

**Render support.**
- Mermaid Live Editor: yes (FA loaded по default)
- GitHub native: **no** (GitHub does not load FA stylesheet — иконки покажутся как text fallback)
- Notion native: **no** (same reason)
- VSCode bierner extension: yes (если FA доступен в preview)

**Practical rule.** Не полагаться на FA для production diagrams targeting GitHub
или Notion. Используй emoji вместо FA — emoji универсально рендерятся как Unicode.
[src: https://mermaid.js.org/syntax/flowchart.html#fontawesome-supported-icons]

### Custom SVG via `img:url`

Поддерживается через `img:` prefix или встроенный image syntax в новых версиях.
GitHub native не загружает external images внутри Mermaid block (CSP). Использовать
только в локальном/Live env. `verify-on-demand`.

### Built-in flowchart shape variants

| Syntax | Имя | Use |
|---|---|---|
| `A[Text]` | rectangle (default) | стандарт нода |
| `A(Text)` | round | мягкие границы |
| `A([Text])` | stadium | start/end событие |
| `A[[Text]]` | subroutine | вложенный процесс |
| `A[(Text)]` | cylindrical (database) | хранилище |
| `A((Text))` | circle | важная сущность |
| `A>Text]` | asymmetric | флаг |
| `A{Text}` | rhombus | decision (yes/no) |
| `A{{Text}}` | hexagon | preparation step |
| `A[/Text/]` | parallelogram | input/output |
| `A[\Text\]` | parallelogram alt | input/output |
| `A[/Text\]` | trapezoid | manual operation |
| `A[\Text/]` | trapezoid inverted | manual input |
| `A(((Text)))` | double-circle | terminal state |

[src: https://mermaid.js.org/syntax/flowchart.html#node-shapes]

### Mermaid 11+ extended shapes (verify-on-demand)

В версиях 10.9+ / 11.x добавлена расширенная система shapes через `@{shape: name}`
аннотацию:
```
A@{ shape: rounded, label: "Process step" }
B@{ shape: cyl, label: "Database" }
C@{ shape: cloud, label: "External API" }
```

Список новых имён shapes (частичный): `rounded`, `stadium`, `subproc`, `cyl`,
`circle`, `dbl-circ`, `flag`, `diam`, `hex`, `lean-r`, `lean-l`, `trap-b`,
`trap-t`, `cloud`, `tag-doc`, `proc`, `event`, `manual-input`, `manual-only`,
`stored-data`, `paper-tape`, `delay`, `terminal`, `note-shape`, `text-block`,
`comment-shape`, `bow-tie`. **Render на GitHub** для multiple of these — verify
on a sample diagram before relying. [src: https://mermaid.js.org/syntax/flowchart.html#expanded-node-shapes]

**Jetix recommendation.** Stick to legacy bracket-syntax shapes (top table) —
universal render. Use `@{shape: ...}` syntax только когда proven render в target env.

---

## A.4 Custom fonts

`fontFamily` через themeVariables — Mermaid передаёт его как CSS на rendered SVG.
Что **actually renders** зависит от env:

| Env | Font behaviour |
|---|---|
| Mermaid Live Editor | использует web fonts если доступны (Inter / Roboto подгружаются если в браузере есть) |
| GitHub native | использует ТОЛЬКО system-installed fonts на client side. Нет загрузки web fonts — `fontFamily: 'Inter'` падёт на fallback если у вьюера Inter не установлен. |
| Notion native | similar to GitHub — relies on client OS fonts |
| VSCode bierner extension | использует VSCode editor fonts + system fonts |
| mmdc CLI | uses Puppeteer headless browser — fonts должны быть installed на server где запущен mmdc |

**Pratical advice.** Используй font-stack a-la `'Inter, system-ui, -apple-system, sans-serif'`
— если Inter не доступен (most viewers), fallback на system-ui (макс. совместимый
sans-serif на любой OS). [src: https://mermaid.js.org/config/theming.html#themevariables-reference-table]

---

## A.5 Render environments — feature matrix

| Env | Themes | FontAwesome | Custom fonts | `init` directive | Beta types |
|---|---|---|---|---|---|
| **GitHub native** (.md в repo) | ✅ all built-in | ❌ | partial (system fonts only) | ✅ | partial — flowchart/sequence/class/state/er/gantt/pie/journey/gitGraph stable; mindmap/timeline/quadrant ok; sankey/xychart/architecture/packet **verify-on-demand** |
| **Notion native** (mermaid code block) | ✅ | ❌ | partial (system fonts) | ✅ | similar to GitHub — newer types may not render |
| **Mermaid Live Editor** ([mermaid.live](https://mermaid.live)) | ✅ | ✅ | ✅ (web fonts) | ✅ | ✅ (latest features включая beta) |
| **VSCode + bierner.markdown-mermaid** | ✅ | ✅ (если FA настроен) | ✅ (system + VSCode fonts) | ✅ | ✅ (зависит от version pinned в extension) |
| **mmdc CLI** (`@mermaid-js/mermaid-cli`) | ✅ | depends on installed FA | depends on server fonts | ✅ | ✅ |

**Authoring rule for Jetix.** Author в Mermaid Live Editor (full features), test render в GitHub UI (target audience env), confirm в Notion если будем embed-ить туда. [src: https://github.com/mermaid-js/mermaid] [src: https://mermaid.live]

---

## A.6 AI / LLM-friendly authoring patterns

### Naming conventions

| Convention | When |
|---|---|
| `UPPER_SNAKE_CASE` (e.g. `MASTER_NODE`, `INPUT_FILTER`) | architectural diagrams, system maps — easy to grep, distinct from prose |
| `camelCase` (e.g. `userClicks`, `apiResponse`) | sequence diagrams где participants — software components |
| `PascalCase` (e.g. `User`, `OrderService`) | class diagrams (matches typical OOP naming) |
| Short letters `A`, `B`, `C` | tiny throwaway diagrams (≤5 nodes), не для production |

**Jetix canonical.** UPPER_SNAKE для flowchart node IDs (consistency с Workshop #1
baseline). [src: общая практика — не нашёл authoritative URL, рекомендация compiled из multiple Mermaid examples в /examples в repo: https://github.com/mermaid-js/mermaid/tree/develop/demos]

### Subgraph nesting depth

- 1-2 уровня вложенности — render корректно, читается хорошо
- 3 уровня — на edge, GitHub mostly handles но visual clutter
- 4+ — **избегай**, парсер может падать, читателю невозможно следить за структурой

`verify-on-demand` для конкретных версий Mermaid — Mermaid CHANGELOG отмечает
periodic улучшения subgraph rendering.

### Common LLM authoring errors (что Claude часто делает не так)

1. **Missing direction.** `subgraph FOO ... end` без `direction TB|LR` внутри — наследует
   parent direction, но иногда render неожиданный. **Fix:** explicit `direction TB`
   первой строкой каждого subgraph.

2. **classDef references unknown class.** `:::myClass` без объявления `classDef myClass ...`
   — silently ignored, нода рендерится без стиля. **Fix:** объявляй classDef ДО
   использования (top of diagram).

3. **Mismatched brackets.** `A[Some text"` (двойная кавычка не закрыта) — entire
   diagram fails to render. GitHub показывает raw mermaid block без error message.
   **Fix:** quote-escape: `A["Text with \"quotes\""]` или вообще без quotes если text
   простой.

4. **Edge labels with reserved chars.** `A -->|stat: 200| B` — двоеточие в label
   парсер может trip. **Fix:** заворачивай label в quotes: `A -->|"stat: 200"| B`.

5. **`<br/>` vs `<br>` в labels.** Оба supported, но `<br/>` self-closing более
   robust. Используй `<br/>`.

6. **Long node text без переносов.** Длинная строка в `[...]` создаёт огромную
   ноду. Используй `<br/>` для переносов: `A["Long line one<br/>second line<br/>third line"]`.

7. **Reserved keywords как node IDs.** `end`, `class`, `style`, `subgraph`, `direction`
   — если используешь как ID, парсер ломается. **Fix:** quote: `"end"` или переименуй.

[src: cross-references из mermaid.js.org/syntax/flowchart.html и community issues
на github.com/mermaid-js/mermaid]

### Patterns for incremental edits

- **Append-only edits.** Добавь новую ноду в конец `flowchart` definition + одну
  edge — git diff минимален, легко review.
- **Group by section.** Разделяй diagram на logical sections комментариями `%%`:
  ```
  %% --- Input layer ---
  INPUT --> GUARD

  %% --- Workshop core ---
  GUARD --> FOUNDATION
  ...
  ```
  Каждая section editable независимо.
- **classDef всегда внизу диаграммы** — последняя секция, чтобы новый readable diff не путал стилевые правила с logic.

---

## A.7 Sources confirmed

URLs cited above; the following are the canonical landing pages I leaned on
для compile of this document:

- https://mermaid.js.org/intro/ — общий entry point, listing of supported diagram types
- https://mermaid.js.org/syntax/flowchart.html — flowchart syntax reference (shapes, edges, styling)
- https://mermaid.js.org/config/theming.html — themeVariables reference, built-in themes
- https://mermaid.js.org/syntax/sequenceDiagram.html — sequence-specific syntax
- https://mermaid.js.org/syntax/classDiagram.html — class
- https://mermaid.js.org/syntax/stateDiagram.html — stateDiagram-v2
- https://mermaid.js.org/syntax/gantt.html — gantt
- https://mermaid.js.org/syntax/mindmap.html — mindmap
- https://mermaid.js.org/syntax/timeline.html — timeline
- https://mermaid.js.org/syntax/quadrantChart.html — quadrant
- https://github.com/mermaid-js/mermaid — main repo + CHANGELOG для feature timeline
- https://github.com/mermaid-js/mermaid/tree/develop/demos — example diagrams (naming conventions)
- https://mermaid.live — Mermaid Live Editor (interactive playground)
- https://github.com/mermaid-js/mermaid-cli — mmdc CLI install + usage
- https://docs.mermaidchart.com — Mermaid Chart commercial docs (note: large fraction is OSS-mirror; some advanced features paywalled)
- https://aaronjbecker.com/posts/mermaid-vs-d2-comparing-text-to-diagram-tools/ — independent comparison Mermaid vs D2

**`verify-on-demand` items** (claims that should be spot-checked at the URL before
relying for production):
- newer beta diagram types (sankey-beta / xychart-beta / architecture-beta / packet-beta) — render fidelity GitHub
- `@{shape: ...}` extended-shape syntax — version-dependent
- `kanban` and `architecture-beta` — relatively new, render coverage matrix may shift

---

## Summary — actionable for Phase B style guide

1. **Theme:** `theme: base` + full override через themeVariables (deterministic).
2. **Font stack:** `Inter, system-ui, -apple-system, sans-serif` (graceful fallback).
3. **No FontAwesome** — emoji вместо. Universal Unicode render.
4. **Shape syntax:** legacy brackets (`[]`, `()`, `{}`, etc.) — universal. Avoid
   `@{shape: ...}` extended pока не verified в target env.
5. **Diagram types для Jetix:** flowchart, sequenceDiagram, stateDiagram-v2, gantt,
   mindmap, timeline, journey, quadrantChart — все stable.
6. **Naming:** UPPER_SNAKE_CASE для flowchart node IDs, snake_case classDef names.
7. **classDef location:** в конце diagram body, после всех edges.
8. **Subgraph depth:** ≤2 nesting levels.
9. **Authoring env:** Mermaid Live Editor для experiments → push в repo → verify
   GitHub UI render.
10. **Ошибки Claude:** explicit `direction` в каждом subgraph, classDef before use,
    `<br/>` self-closing, quote-escape labels с reserved chars.
