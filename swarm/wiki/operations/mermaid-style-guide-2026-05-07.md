---
title: Mermaid Style Guide — Jetix Canonical
date: 2026-05-07
type: style-guide
purpose: единый стиль для всех Mermaid diagrams в Jetix repo + Notion
audience: Ruslan (author), CC (writer), partners (viewer)
authority: Ruslan ack pending merge (cyc-mermaid-mastery-2026-05-07)
parent_research: reports/mermaid-research-notes-2026-05-07.md
applies_to:
  - swarm/wiki/synthesis/diagrams-*/**.md
  - decisions/**/*-diagram*.md
  - any new mermaid block в Jetix repo или Notion subpages
versioning:
  current: v1.0
  changelog:
    - 2026-05-07 v1.0 — initial canonical (extends Workshop #1 baseline)
F: F4
G: tooling-style-guide
R: refuted_if_diagrams_render_inconsistent_across_github_and_notion
constitutional_anchor:
  - Tier 2 Rule 1 (no AI strategizing) — guide consolidates Ruslan-decided defaults + research-backed best practices
  - Tier 2 Rule 6 (provenance) — each rule cites parent_research section
---

# Mermaid Style Guide — Jetix Canonical v1.0

> **Назначение.** Единый язык для всех будущих Mermaid диаграмм. Одинаковый
> рендер в GitHub UI + Notion + Mermaid Live Editor. Узнаваемый Jetix look.
>
> **Источник истины.** Этот документ. При расхождении prevails canonical guide;
> старые diagrams приводятся к стилю incrementally.
>
> **Source.** Workshop #1 baseline ([`01-workshop-7-elements.md`](../synthesis/diagrams-2026-05-07/01-workshop-7-elements.md))
> + research notes ([`mermaid-research-notes-2026-05-07.md`](../../../reports/mermaid-research-notes-2026-05-07.md)).

---

## §1 Color palette

### §1.1 Core 8 (Workshop #1 baseline — preserved)

| Class | Fill | Stroke | Use case |
|---|---|---|---|
| `substrate` / `foundation` | `#e8eaf6` | `#283593` | substrate / git / naming / основа |
| `guard` / `governance` | `#ffebee` | `#c62828` | filters / gates / охрана / Default-Deny |
| `storage` / `knowledge` | `#e0f2f1` | `#00695c` | KB / склад / archives |
| `master` / `work` | `#fce4ec` | `#ad1457` | владелец / actor / centerpiece |
| `tools` | `#fff3e0` | `#e65100` | adaptable станки / utilities |
| `auto` / `automation` | `#f3e5f5` | `#6a1b9a` | cron / sync / pipelines |
| `phone` / `network` | `#e1f5fe` | `#01579b` | внешние связи / partners / collaborators |
| `cloud` / `io` | `#e3f2fd` | `#1565c0` | INPUT / OUTPUT / external |

[src: research §A.2 + Workshop #1 §1]

### §1.2 TRM extension (6 ресурсов клиента)

Для TRM-стиля диаграмм (resource management):

| Class | Fill | Stroke | Resource |
|---|---|---|---|
| `trm_finance` | `#fff8e1` | `#f57c00` | финансы |
| `trm_time` | `#e8f5e9` | `#2e7d32` | время |
| `trm_audience` | `#fce4ec` | `#ad1457` | аудитория |
| `trm_knowledge` | `#e0f2f1` | `#00695c` | знания |
| `trm_compute` | `#e3f2fd` | `#1565c0` | compute |
| `trm_team` | `#f3e5f5` | `#6a1b9a` | команда |

### §1.3 L0-L5 ladder gradient (Land-and-Expand)

Голубой gradient для уровней (от L0 к L5):

| Level | Fill | Stroke |
|---|---|---|
| `ladder_l0` | `#e3f2fd` | `#1565c0` |
| `ladder_l1` | `#bbdefb` | `#1565c0` |
| `ladder_l2` | `#90caf9` | `#0d47a1` |
| `ladder_l3` | `#64b5f6` | `#0d47a1` |
| `ladder_l4` | `#42a5f5` | `#0d47a1` |
| `ladder_l5` | `#1e88e5` | `#0d47a1` |

### §1.4 Collaboration triple (3 partner colors)

Для diagrams с несколькими agentes/partners:

| Class | Fill | Stroke | Persona |
|---|---|---|---|
| `partner_a` | `#fce4ec` | `#ad1457` | Ruslan / primary |
| `partner_b` | `#e3f2fd` | `#1565c0` | Цэрэн / secondary |
| `partner_c` | `#e8f5e9` | `#2e7d32` | ШСМ / Левенчук / tertiary |

### §1.5 Container / subgraph fill

- Subgraph (контейнер мастерской и т.п.): `#fff8e1` fill, `#f57c00` stroke, **stroke-width:4px**

---

## §2 Typography

| Element | Setting |
|---|---|
| `fontFamily` | `Inter, system-ui, -apple-system, sans-serif` (graceful fallback per research §A.4) |
| `fontSize` | `14px` body |
| Title в `<b>...</b>` | implicit bold (HTML inside label) |
| Subtitle / hint в `<small>...</small>` | smaller secondary text |

**Why this stack.** Inter renders nicely в Mermaid Live Editor + локальном VSCode.
GitHub / Notion fall back на system-ui автоматически — universal compat.
[src: research §A.4]

---

## §3 Stroke widths

| Width | Use |
|---|---|
| `4px` | Subgraph container (e.g. WORKSHOP контур); MASTER node (centerpiece) |
| `3px` | Major nodes (foundation, guard, storage, tools, auto, phone) |
| `2px` | Secondary / cloud / IO nodes; default edges |

[src: Workshop #1 baseline]

**Edge thickness via syntax** (rather than width):
- `-->` standard (default ~2px)
- `==>` thick (visual ~3px) — для primary flows
- `-.->` dashed — для secondary / async

---

## §4 Init directive — copy-paste boilerplate

**Standard (use unless specific reason to deviate):**

```
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fff8e1', 'primaryTextColor':'#000', 'primaryBorderColor':'#f57c00', 'lineColor':'#555', 'fontFamily':'Inter, system-ui, sans-serif', 'fontSize':'14px'}}}%%
```

**Why `theme: base` + override.** Deterministic — render одинаковый на всех envs.
Built-in themes (`forest` / `dark`) добавляют unwanted variation. [src: research §A.2]

**One-liner (no whitespace) рекомендуется** — Mermaid парсер чувствителен к
переносам внутри `init` block в некоторых старых рендерерах GitHub. Inline
form universally safe.

---

## §5 Naming conventions

### §5.1 Node IDs

`UPPER_SNAKE_CASE`. Examples: `MASTER`, `INPUT_FILTER`, `KNOWLEDGE_BASE`,
`OUTPUT_DELIVERABLE`, `RUSLAN`, `CLAUDE_CODE`.

**Rule.** Без пробелов, без kebab-case, без camelCase. Распознаётся в grep,
в diff читаемо, distinct from prose. [src: research §A.6]

### §5.2 classDef names

`snake_case`. Examples: `master_node`, `cloud_io`, `trm_finance`, `partner_a`.

**Rule.** Совпадает с frontmatter / config conventions Jetix.

### §5.3 Subgraph IDs

`UPPER_CASE` single word или `UPPER_SNAKE`. Examples: `WORKSHOP`, `LADDER`,
`INPUT_LAYER`, `OUTPUT_LAYER`.

### §5.4 Reserved keywords — никогда как ID

`end`, `class`, `style`, `subgraph`, `direction`, `click`, `link`, `classDef`,
`linkStyle` — Mermaid keywords. Если хочешь использовать как имя ноды,
переименуй (e.g. `END_STATE` вместо `end`). [src: research §A.6 #7]

---

## §6 File structure standard

Каждая Mermaid `.md` диаграмма следует этому шаблону:

````markdown
---
title: <Diagram title>
date: YYYY-MM-DD
type: visual
diagram_engine: mermaid
source: <citation путь к исходному canonical document>
audience: <who looks at this>
purpose: <one-line purpose>
F: F4
G: visual-deliverable
R: refuted_if_<binary condition>
---

# <emoji> <Title>

> <One-line tagline blockquote>

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fff8e1', 'primaryTextColor':'#000', 'primaryBorderColor':'#f57c00', 'lineColor':'#555', 'fontFamily':'Inter, system-ui, sans-serif', 'fontSize':'14px'}}}%%
flowchart TB
    %% --- Input layer ---
    INPUT(["..."]):::cloud

    %% --- Core ---
    subgraph CORE ["..."]
        direction TB
        ...
    end

    %% --- Output layer ---
    OUTPUT(["..."]):::cloud

    %% --- Edges ---
    INPUT ==> CORE
    CORE ==> OUTPUT

    %% --- classDef block (always last) ---
    classDef cloud fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    classDef ...

    style CORE fill:#fff8e1,stroke:#f57c00,stroke-width:4px
```

---

## 📖 <Section: explanation table>

| # | Element | Function |
|---|---------|----------|
| 1 | **<element>** | <one-line description> |
| ... | ... | ... |

---

## 🔗 Source

- [<canonical source #1>](<relative path>) — <description>
- [<canonical source #2>](<relative path>) — <description>
````

---

## §7 Authoring rules (do / don't)

### §7.1 DO

1. **`direction` explicit в каждом subgraph** — `direction TB` (top-bottom) или `LR` (left-right) первой строкой subgraph body. Иначе наследует unpredictable.
2. **classDef declarations в конце diagram body** — после всех edges. Один логический блок.
3. **Comments `%%` для секционирования** — особенно для diagrams >20 нод. Делает diff-friendly.
4. **`<br/>` self-closing для line breaks в node labels** — robust во всех envs.
5. **Quote-escape labels с reserved chars** — двоеточия, скобки: `A -->|"stat: ok"| B`.
6. **Emoji вместо FontAwesome** — universal Unicode render. [src: research §A.3]
7. **Keep ≤30 nodes per diagram.** Если больше — split into 2 diagrams + INDEX page.
8. **One thought per diagram.** Не мешай 7-elements + TRM + L0-L5 в одну картинку.

### §7.2 DON'T

1. **Не используй `fa:fa-*`** — GitHub / Notion не загружают FontAwesome stylesheet. Покажется raw text.
2. **Не используй `img:url`** — GitHub CSP блокирует external images внутри Mermaid block.
3. **Не вкладывай subgraph >2 уровней** — render fragile, читать невозможно.
4. **Не используй themes `forest`/`dark`** для production — deterministic look = `base` + themeVariables override.
5. **Не используй reserved keywords как node IDs** — `end`, `class`, `style`, etc.
6. **Не пиши длинные строки в одну node** — переноси через `<br/>`.
7. **Не используй `@{shape: ...}` extended syntax** пока render не verified в GitHub UI на образце. Stick to legacy brackets `[]`/`()`/`{}` — universally supported. [src: research §A.3]
8. **Не используй цвета вне palette §1** — каждый новый цвет = либо extension (PR в style guide), либо inconsistency.

---

## §8 Diagram type recommendations

| Use case | Type |
|---|---|
| Архитектура / системные карты / data flow | `flowchart TB` или `flowchart LR` |
| Agent-to-agent / API protocol | `sequenceDiagram` |
| Lifecycle / FSM / status pipeline | `stateDiagram-v2` |
| Project timelines / sprint plans | `gantt` |
| Brainstorm / concept tree | `mindmap` |
| Event timelines (single track) | `timeline` |
| User journey / satisfaction by step | `journey` |
| 2x2 priority matrices | `quadrantChart` |
| Distribution (≤6-8 categories) | `pie` |

**Avoid (Phase B status — verify-on-demand перед production):**
- `sankey-beta`, `xychart-beta`, `architecture-beta`, `packet-beta`, `kanban`, `requirementDiagram`, `C4Context` — render fidelity на GitHub UI inconsistent через 2026; verify на sample перед invest.

[src: research §A.1]

---

## §9 Validation checklist (pre-commit)

Перед commit диаграммы пройди:

- [ ] Frontmatter заполнен (title, date, type, source, audience, purpose, F-G-R)
- [ ] Init directive — canonical из §4
- [ ] Все node IDs `UPPER_SNAKE_CASE`
- [ ] Все classDef имена `snake_case`
- [ ] Все subgraphs имеют explicit `direction TB|LR`
- [ ] classDef declarations в конце diagram body
- [ ] Subgraph nesting ≤2 уровней
- [ ] Цвета только из palette §1
- [ ] Stroke widths только из {2px, 3px, 4px}
- [ ] Нет `fa:fa-*`, `img:url`, `@{shape: ...}` (unless verified в target env)
- [ ] Нет reserved keywords как node IDs
- [ ] Source links footer с relative paths к canonical docs
- [ ] Diagram render verified в GitHub UI + Notion subpage (manual check)

---

## §10 Cross-references

- Research base: [`reports/mermaid-research-notes-2026-05-07.md`](../../../reports/mermaid-research-notes-2026-05-07.md)
- Workshop #1 example: [`swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md`](../synthesis/diagrams-2026-05-07/01-workshop-7-elements.md)
- INDEX: [`swarm/wiki/synthesis/diagrams-2026-05-07/INDEX.md`](../synthesis/diagrams-2026-05-07/INDEX.md)
- Setup doc: [`swarm/wiki/operations/mermaid-preview-setup-2026-05-07.md`](mermaid-preview-setup-2026-05-07.md)
- Skills: [`.claude/skills/mermaid-create/SKILL.md`](../../../.claude/skills/mermaid-create/SKILL.md), [`mermaid-iterate`](../../../.claude/skills/mermaid-iterate/SKILL.md), [`mermaid-export`](../../../.claude/skills/mermaid-export/SKILL.md), [`mermaid-validate`](../../../.claude/skills/mermaid-validate/SKILL.md)

---

## §11 Evolution

- **v1.0 (2026-05-07)** — initial canonical. Workshop #1 + research notes baseline.
- **Future v1.1+** — add diagrams when new use cases surface (TRM diagram #2, L0-L5 diagram #3, Collaboration #4 — каждый extends palette §1.2/§1.3/§1.4 already prepared).
- **Versioning rule.** Breaking changes (palette renaming, naming convention shift) — bump major. Additive changes (new class, new section) — bump minor. Document в frontmatter `versioning.changelog`.
