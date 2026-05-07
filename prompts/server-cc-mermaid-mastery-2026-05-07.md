---
title: Server CC Brigadier Prompt — Mermaid Mastery (research + skills + style guide + setup)
type: brigadier-prompt
created: 2026-05-07
author: cloud-cowork (Ruslan ack)
target_executor: server-cc on branch claude/jolly-margulis-915d34 (or successor)
authority: Ruslan ack via cloud cowork chat 2026-05-07 (after Workshop #1 рендер verified в GitHub)
push_policy: draft commit на server CC ветку, await Ruslan ack для merge
F: F4
G: tooling-mastery-deliverable
R: refuted_if_skills_unusable_or_style_guide_inconsistent
constitutional_anchor:
  - Tier 2 Rule 1 (AI does not strategize) — собирает best practices + creates tooling, не decide whether использовать
  - Tier 2 Rule 6 (provenance) — каждое claim cited к URL / source
  - Append-only — не удаляет existing diagrams or D2 sources в foundation-visuals-2026-04-30/
sla_tier: L2
estimated_effort: 1.5-2.5 hours brigadier autonomous
---

# Server CC Brigadier Prompt — Mermaid Mastery

> **Контекст.** Ruslan переключается с D2 (Studio trial expired, paid wall) на
> Mermaid (FREE, GitHub native render, Notion native). Workshop #1 уже работает
> ([commit f5fdc65](https://github.com/Bogersebekov/jetix-os/commit/f5fdc65) — `swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md`).
> Сейчас нужно: research → canonical style guide → skills → preview setup →
> apply consistent style ко всем будущим diagrams.
>
> **Workflow target:** CC пишет `.md` с mermaid block → push → Ruslan видит в GitHub UI / Antigravity preview / Notion subpage.

---

## §1 Phases

### Phase A — Deep web research Mermaid 2026 (30-45 min)

A.1 **Syntax coverage** — все типы diagrams:
   - flowchart / graph (LR / TB / BT / RL)
   - sequence / class / state / ER / gantt / pie / journey / gitgraph
   - requirement / C4 / mindmap / timeline / quadrant / sankey
   - xychart / block / packet / kanban / architecture (новые в 2026)

   Для каждого типа — quick syntax примеры + best use case.

A.2 **Theming + styling — что доступно:**
   - `%%{init: {...}}%%` directive — themeVariables / fontSize / fontFamily
   - Built-in themes: default / forest / dark / neutral / base
   - classDef syntax + apply via `:::className` или `class A,B,C name`
   - Stroke / fill / color overrides
   - Edge styles (`-->`, `==>`, `-.->`, `-->|label|`)

A.3 **Icons + shapes:**
   - FontAwesome support (`fa:fa-server`, `fa:fa-database`)
   - Custom SVG icons (img:url syntax)
   - Все built-in shape variants (round, stadium, subroutine, cylindrical, circle, asymmetric, rhombus, hexagon, parallelogram, trapezoid, double-circle, cloud в новых версиях)
   - Mermaid 11+ extended shapes (если доступно)

A.4 **Custom fonts** — можно ли? Через themeVariables `fontFamily` — да.
   - Inter / Roboto / system-ui / Open Sans — что Mermaid actually renders
   - Limitations при GitHub render vs local render

A.5 **Render environments** — где как:
   - GitHub native (`.md` files) — что поддерживается / не поддерживается (некоторые advanced features могут не работать)
   - Notion native (mermaid code block) — limits
   - Mermaid Live Editor (mermaid.live) — full features
   - Antigravity / VSCode extension (Markdown Preview Mermaid Support — Bierner) — local render
   - Mermaid CLI (`mmdc`) — server-side render для PNG/SVG export

A.6 **AI / LLM-friendly patterns** — best practices для CC writing diagrams:
   - Naming conventions для node IDs
   - Subgraph nesting depth limits
   - Avoiding common errors (missing direction, broken classDef)

A.7 **Resources to scrape:**
   - https://mermaid.js.org/intro/ (official)
   - https://mermaid.js.org/syntax/flowchart.html (each diagram type)
   - https://mermaid.js.org/config/theming.html
   - https://mermaid.live (играй чтобы понять)
   - https://github.com/mermaid-js/mermaid (latest features)
   - https://docs.mermaidchart.com (commercial extras)
   - https://aaronjbecker.com/posts/mermaid-vs-d2-comparing-text-to-diagram-tools/ (comparison)
   - StackOverflow / Reddit r/diagrams threads на «mermaid styling tips»
   - YouTube tutorials by Knut Sveidqvist (creator), Mermaid Chart team

### Phase B — Canonical Jetix Mermaid Style Guide (20 min)

Создать `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` с:

B.1 **Color palette** — extend существующую (Workshop #1 sets baseline):
   ```
   Substrate: #e8eaf6 fill / #283593 stroke
   Governance/Guard: #ffebee fill / #c62828 stroke
   Knowledge/Storage: #e0f2f1 fill / #00695c stroke
   Work/Master: #fce4ec fill / #ad1457 stroke
   Tools: #fff3e0 fill / #e65100 stroke
   Automation: #f3e5f5 fill / #6a1b9a stroke
   Network/Phone: #e1f5fe fill / #01579b stroke
   Cloud/Input/Output: #e3f2fd fill / #1565c0 stroke
   ```
   Plus: расширить на TRM (6 ресурсов разных цветов) + L0-L5 ladder (gradient blue) + Collaboration (3 цвета per partner).

B.2 **Typography:**
   - fontFamily: `Inter, system-ui, sans-serif` (renders on most platforms)
   - fontSize: `14px` body / `18px` titles
   - Bold для emphasis (master node, key labels)

B.3 **Stroke widths:**
   - 4px — primary container (subgraph fill border)
   - 3px — major nodes
   - 2px — secondary nodes / edges

B.4 **Init directive boilerplate** — copy-paste header для каждой diagram:
   ```
   %%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#fff8e1', 'primaryTextColor':'#000', 'primaryBorderColor':'#f57c00', 'lineColor':'#555', 'fontFamily':'Inter, system-ui, sans-serif', 'fontSize':'14px'}}}%%
   ```

B.5 **Naming conventions:**
   - Node IDs: UPPERCASE_SNAKE (e.g. `MASTER`, `INPUT_FILTER`)
   - classDef names: snake_case (e.g. `master_node`, `cloud_io`)
   - Subgraph IDs: UPPERCASE single word (e.g. `WORKSHOP`, `LADDER`)

B.6 **File structure standard** — boilerplate header + body для каждой `.md`:
   - Frontmatter (title, date, type, source citations, audience)
   - H1 title with emoji
   - Tagline / one-liner blockquote
   - Mermaid block
   - Table описание элементов
   - Source links footer

### Phase C — Claude Code Skills (30-45 min)

Создать в `.claude/skills/` 3-4 skill folders:

C.1 **`mermaid-create`** — `/mermaid-create <topic>` создаёт new diagram в `swarm/wiki/synthesis/diagrams-YYYY-MM-DD/` с standard boilerplate (frontmatter + style header + empty mermaid block + section template)
   - Args: topic name, output folder (optional), source-doc citation
   - Read mermaid-style-guide-2026-05-07.md для consistency
   - Write file + log в wiki/log.md

C.2 **`mermaid-iterate`** — `/mermaid-iterate <file> <change>` modifies existing diagram per text instruction
   - Read existing file
   - Apply change preserving style
   - Validate mermaid syntax (basic — balanced brackets / classDef / subgraph)

C.3 **`mermaid-export`** — `/mermaid-export <file>` — render `.md` mermaid block в SVG / PNG через mmdc CLI (если установлен) или через kroki.io API fallback
   - Output: `<filename>.svg` + `<filename>.png` рядом с `.md`
   - Note: requires mermaid-cli installed OR kroki API access

C.4 **`mermaid-validate`** (optional) — quick syntax check существующих diagrams без external tooling
   - Simple regex / parser based
   - Report broken classDef / unbalanced brackets / missing direction

### Phase D — Antigravity / VSCode preview setup doc (15 min)

Создать `swarm/wiki/operations/mermaid-preview-setup-2026-05-07.md`:

D.1 **VSCode / Antigravity extensions to install:**
   - **Markdown Preview Mermaid Support** by Matt Bierner (`bierner.markdown-mermaid`) — free, рендерит mermaid в `.md` preview pane
   - **Mermaid Markdown Syntax Highlighting** by bpruitt-goddard (`bpruitt-goddard.mermaid-markdown-syntax-highlighting`) — free, syntax highlight внутри mermaid blocks
   - Optional: **Markdown All in One** by Yu Zhang — extra markdown features

D.2 **Workflow в Antigravity:**
   - Open `.md` file
   - `Ctrl+Shift+V` или `Ctrl+K V` — open Markdown preview to side
   - Edit `.md` → preview updates automatically
   - Mermaid renders inline в preview pane

D.3 **Workflow в browser (GitHub):**
   - Open file URL → render automatic
   - Refresh для updates

D.4 **Workflow в Notion:**
   - `/code` block → language: mermaid → paste mermaid source
   - Native render
   - Copy mermaid из repo, paste в Notion

D.5 **mermaid CLI install (для export):**
   - `npm install -g @mermaid-js/mermaid-cli`
   - Use: `mmdc -i diagram.md -o diagram.svg`

### Phase E — Apply style guide retroactively to Workshop #1 (10 min)

Update `swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md`:
- Verify init directive matches style guide canonical
- Verify classDef names match canonical
- Update station label "D2" → "Mermaid" (это уже сделано в commit перед этим promptом — verify only)
- Update INDEX.md если style guide adds new fields

### Phase F — Push draft + signal Ruslan (5 min)

```bash
git add .claude/skills/mermaid-* swarm/wiki/operations/mermaid-* swarm/wiki/synthesis/diagrams-2026-05-07/
git commit -m "[mermaid-mastery] research + style guide + skills + preview setup (Ruslan ack pending merge)"
git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** Wait for Ruslan ack.

---

## §2 Output spec — что должно быть готово

| File | Type | Required |
|---|---|---|
| `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` | canonical style guide | ✅ |
| `swarm/wiki/operations/mermaid-preview-setup-2026-05-07.md` | setup doc | ✅ |
| `swarm/wiki/synthesis/diagrams-2026-05-07/INDEX.md` | navigation (update only) | ⚠️ if style guide changes |
| `.claude/skills/mermaid-create/SKILL.md` | skill | ✅ |
| `.claude/skills/mermaid-iterate/SKILL.md` | skill | ✅ |
| `.claude/skills/mermaid-export/SKILL.md` | skill | ✅ |
| `.claude/skills/mermaid-validate/SKILL.md` | skill | ⚠️ optional |
| `reports/mermaid-research-notes-2026-05-07.md` | research notes (Phase A output) | ✅ |

---

## §3 Discipline (constitutional check)

| Rule | Application | Compliance |
|---|---|---|
| Tier 2 Rule 1 | Research собирает best practices, style guide = consensus от documented sources, skills = tooling. Не decides «нам нужны диаграммы» (это Ruslan-decided). | ✅ |
| Tier 2 Rule 2 | Затрагивает `.claude/skills/` и `swarm/wiki/operations/` — moderate blast radius. Default-Deny → push draft, await Ruslan ack для merge. | ✅ |
| Tier 2 Rule 6 | Все claims в research notes + style guide cited URL. | ✅ |
| Append-only | Старые D2 sources в `foundation-visuals-2026-04-30/` НЕ trogаем (preserved). New stuff в `diagrams-2026-05-07/` + `mermaid-*` files. | ✅ |
| Tier 2 Rule 11 (blast radius) | F4 tooling deliverable. Skills могут быть activated только когда invoked. Style guide = reference doc, не enforcement. | ✅ |

---

## §4 What NOT to do

- ❌ НЕ удалять existing D2 sources (`foundation-visuals-2026-04-30/`) — append-only
- ❌ НЕ переписывать Workshop #1 diagram radically — только verify style alignment
- ❌ НЕ создавать диаграммы #2/3/4 (TRM, L0-L5, Collaboration) — это Ruslan + cloud cowork next, не brigadier scope
- ❌ НЕ устанавливать npm packages / mermaid-cli автоматически — flag в setup doc что нужно
- ❌ НЕ push to main, НЕ tag

---

## §5 Time budget

- Phase A research: 30-45 min
- Phase B style guide: 20 min
- Phase C skills (3 obligatory + 1 optional): 30-45 min
- Phase D preview setup doc: 15 min
- Phase E Workshop #1 verify: 10 min
- Phase F push draft: 5 min

**Total: 1.5-2.5 hours autonomous.**

If значительно превышает 2.5 часа — pause + signal Ruslan.

---

## §6 After-push deliverable signal к Ruslan

Через cloud cowork bridge:
- Branch + commit SHA
- Files created (counts)
- Skills count (3 / 4)
- Research notes word count + sources cited count
- Style guide section count
- Any conflicts / unclears
- Discipline check verified
- Ready для merge ack → push to main + tag `mermaid-mastery-2026-05-07`

Ruslan тогда:
1. Reviews delivery
2. Тестирует skills (`/mermaid-create test-topic` → проверяет что boilerplate ОК)
3. ack → merge to main + tag
4. Continue работу с диаграммами #2/3/4 уже в new style + skills

---

**Brigadier signature.** Acting_as tooling-mastery-orchestration-role.
Ruslan = sole authority по style decisions (final aesthetic call).
Append-only discipline preserved. Default-Deny gate: Ruslan merge ack required.
