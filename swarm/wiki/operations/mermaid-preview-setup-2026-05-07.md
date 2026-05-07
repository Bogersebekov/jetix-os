---
title: Mermaid Preview Setup — Antigravity / VSCode / GitHub / Notion
date: 2026-05-07
type: operational-setup
purpose: пошаговый setup для preview Mermaid диаграмм в каждом env где Ruslan работает
audience: Ruslan
parent_research: reports/mermaid-research-notes-2026-05-07.md
parent_style_guide: swarm/wiki/operations/mermaid-style-guide-2026-05-07.md
F: F4
G: tooling-setup-doc
R: refuted_if_setup_steps_dont_produce_working_preview
---

# Mermaid Preview Setup

> **Назначение.** Как установить preview для Mermaid в каждом env где Ruslan работает.
> Цель — иметь minimum 2 рабочих env'а: GitHub (для финальной верификации) + Antigravity/VSCode (для local edit с live preview).

---

## §1 Antigravity / VSCode extensions

Antigravity = fork VSCode → большинство VSCode extensions работают.

### §1.1 Required (для basic preview)

**Markdown Preview Mermaid Support** — by Matt Bierner

- ID: `bierner.markdown-mermaid`
- Free, OSS
- Что делает: рендерит Mermaid блоки в Markdown preview pane (стандартный VSCode preview)
- Install: Open Extensions panel (`Cmd+Shift+X` macOS / `Ctrl+Shift+X` Linux) → search "Markdown Preview Mermaid Support" → Install
- Альтернативный install через terminal:
  ```bash
  code --install-extension bierner.markdown-mermaid
  ```
  (для Antigravity подмени `code` на `antigravity` если CLI binary доступен — verify-on-demand для конкретного Antigravity build)

### §1.2 Recommended (для удобства)

**Mermaid Markdown Syntax Highlighting** — by bpruitt-goddard

- ID: `bpruitt-goddard.mermaid-markdown-syntax-highlighting`
- Free, OSS
- Что делает: syntax highlighting внутри Mermaid code block (без него — plain text монохром)
- Install:
  ```bash
  code --install-extension bpruitt-goddard.mermaid-markdown-syntax-highlighting
  ```

### §1.3 Optional (extra markdown features)

**Markdown All in One** — by Yu Zhang

- ID: `yzhang.markdown-all-in-one`
- Free, OSS
- Bonus features: TOC generation, list editing helpers, math, table formatting
- Install:
  ```bash
  code --install-extension yzhang.markdown-all-in-one
  ```

### §1.4 Verify install

После install, открой любой `.md` файл с mermaid block (e.g. `swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md`). Открой preview side-by-side:
- macOS: `Cmd+K V`
- Linux/Windows: `Ctrl+K V`

Должна быть видна rendered диаграмма в preview pane. Если показывается raw mermaid block — extension не активен или не установлен.

---

## §2 Workflow в Antigravity / VSCode

1. Открой `.md` файл с mermaid block
2. Открой preview side-by-side (`Ctrl+K V`)
3. Edit `.md` слева → preview справа auto-updates через ~1 sec
4. Удобно: Mermaid Live Editor встроен (если хочешь полный preview с theme switcher) — установи `tomoki1207.pdf` или используй внешний browser tab на mermaid.live для experiments

**Совет.** Для итеративной работы:
- Edit в Antigravity (быстро, c live preview)
- Final verify в GitHub UI (это что увидят Цэрэн / partners)
- Кросс-чек в Mermaid Live Editor если хочешь поиграть с темами

---

## §3 Workflow в browser (GitHub)

GitHub native рендерит mermaid автоматически в `.md` файлах.

### §3.1 Открыть

URL pattern:
```
https://github.com/<owner>/<repo>/blob/<branch>/<path-to-md>
```

Пример:
```
https://github.com/Bogersebekov/jetix-os/blob/main/swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md
```

Render видно сразу, без login (для public repo) или после login (для private).

### §3.2 Update flow

1. CC pushes update на ветку (server-CC pushes на `claude/jolly-margulis-915d34`; merge на `main` происходит после Ruslan ack)
2. Ruslan refresh страницу — видит новый render
3. Optional: открой URL с `?_=<random>` параметром в конце чтобы bypass GitHub raw caching

### §3.3 Caveats

- **GitHub native render limitations** — некоторые beta diagram types (sankey, xychart, architecture) могут НЕ рендериться. Style guide §8 рекомендует stick to stable types.
- **No FontAwesome.** GitHub не загружает FA stylesheet — используй emoji (см. style guide §7.2 #1).
- **No external images.** GitHub CSP блокирует `img:url` syntax.
- **Caching.** GitHub агрессивно кеширует `.md` rendered output. Если update не виден — hard refresh (`Cmd+Shift+R` macOS, `Ctrl+Shift+R` Linux/Win).

---

## §4 Workflow в Notion

Notion native рендерит mermaid через code block с language `mermaid`.

### §4.1 Setup

В любой Notion page:
1. Type `/code` (или `/`)
2. Выбери "Code"
3. В language dropdown — выбери "Mermaid"
4. Paste mermaid source (то что между ` ```mermaid ` и ` ``` ` в `.md` файле — БЕЗ обрамляющих fences)

### §4.2 Update flow

Notion НЕ ссылается автоматически на GitHub repo. Если хочешь sync:
1. CC pushes на main → файл в repo
2. Ruslan копирует mermaid source из GitHub файла
3. Paste в Notion code block (replace existing content)

**Альтернатива:** Notion supports `/embed` GitHub Gist URLs — можно создать Gist с mermaid и embed в Notion. Меньше vendor-locked но добавляет шаг.

### §4.3 Caveats

- Notion render ≈ GitHub render (similar limitations) — no FA, no external images, system fonts only
- Some beta diagram types may not render — verify

---

## §5 Workflow в Mermaid Live Editor

[mermaid.live](https://mermaid.live) — official Mermaid playground.

### §5.1 Use cases

- **Quick experiments** с syntax / theming перед commit в repo
- **Theme switcher** — посмотреть как diagram look в forest / dark / neutral
- **Export** — Actions → Export → SVG / PNG (без mmdc CLI)
- **Share** — Live Editor генерирует URL с base64-encoded diagram source. Удобно для быстро показать кому-то без commit в repo.

### §5.2 Limitations

- **Latest features.** Live Editor использует latest Mermaid release — некоторые beta features могут работать там и не работать в GitHub. **Always verify в GitHub UI** перед finalizing.

---

## §6 Mermaid CLI (for export)

`@mermaid-js/mermaid-cli` — CLI tool который рендерит Mermaid в SVG / PNG / PDF локально.

### §6.1 Install

⚠️ **Не устанавливай автоматически.** Требует npm + Node.js.

```bash
# Verify Node.js installed
node --version  # должен быть v16+

# Install mermaid-cli globally
npm install -g @mermaid-js/mermaid-cli

# Verify install
mmdc --version
```

Если `npm` не установлен:
- macOS: `brew install node` (если есть Homebrew)
- Linux: package manager (`apt install nodejs npm` Ubuntu / `dnf install nodejs npm` Fedora)
- Или [nvm](https://github.com/nvm-sh/nvm) для version management

### §6.2 Use

Базовый export:
```bash
mmdc -i diagram.md -o diagram.svg
mmdc -i diagram.md -o diagram.png -s 2 -w 1920
```

Подробнее: см. `/mermaid-export` skill — он wraps mmdc в Jetix conventions.

### §6.3 Caveats

- mmdc использует Puppeteer (headless Chromium) — install ~200 MB
- Fonts на server side — нужен Inter / system-ui installed (или fallback)
- Network не нужен после install (renders локально)

---

## §7 Recommended setup matrix (Ruslan-specific)

| Use case | Env | Why |
|---|---|---|
| **Live edit + preview pane** | Antigravity + bierner.markdown-mermaid | Fast feedback loop |
| **Final verification render** | GitHub UI на main или branch | Это что увидят partners |
| **Quick experiments** | mermaid.live (browser tab) | No commit needed |
| **Notion embed для отдельных subpages** | Notion mermaid code block | Native Notion experience |
| **Export для презентаций / видео** | mmdc CLI (или /mermaid-export skill) | High-res SVG/PNG output |
| **Shared external view (без login)** | mermaid.live URL | Base64-encoded link |

---

## §8 Quick troubleshooting

### Q: GitHub не рендерит, показывает raw mermaid

- Hard refresh (Cmd+Shift+R / Ctrl+Shift+R)
- Проверь syntax: `/mermaid-validate <file>`
- Проверь init directive — должен быть на первой строке mermaid block
- Проверь что нет broken brackets

### Q: Antigravity preview показывает raw mermaid

- Extension `bierner.markdown-mermaid` not installed → install per §1.1
- Reload window: `Cmd+Shift+P` → "Developer: Reload Window"

### Q: Notion не рендерит

- Code block language должен быть точно `mermaid` (lowercase)
- Beta diagram types (sankey, xychart) — Notion может не support; используй stable types

### Q: mmdc render выглядит иначе чем GitHub

- mmdc использует latest Mermaid; GitHub pinned на старую version. Style guide §4 init directive deterministic — должно совпадать. Если не совпадает — surface разницу + verify через mermaid.live.

### Q: Шрифт другой чем ожидал

- Inter не установлен на client → fallback на system-ui. Style guide §2 учитывает это (graceful fallback). Установи Inter для consistency: [Inter Fonts](https://fonts.google.com/specimen/Inter).

---

## §9 Cross-references

- Research base: [`reports/mermaid-research-notes-2026-05-07.md`](../../../reports/mermaid-research-notes-2026-05-07.md)
- Style guide: [`mermaid-style-guide-2026-05-07.md`](mermaid-style-guide-2026-05-07.md)
- Skills:
  - [`/mermaid-create`](../../../.claude/skills/mermaid-create/SKILL.md)
  - [`/mermaid-iterate`](../../../.claude/skills/mermaid-iterate/SKILL.md)
  - [`/mermaid-export`](../../../.claude/skills/mermaid-export/SKILL.md)
  - [`/mermaid-validate`](../../../.claude/skills/mermaid-validate/SKILL.md)
- Workshop #1 example: [`01-workshop-7-elements.md`](../synthesis/diagrams-2026-05-07/01-workshop-7-elements.md)
- INDEX: [`INDEX.md`](../synthesis/diagrams-2026-05-07/INDEX.md)
