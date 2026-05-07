---
title: Diagrams 2026-05-07 — Visual schemas для видео Цэрэну
date: 2026-05-07
type: visual-overview-mermaid
purpose: 4 диаграммы для frame презентации Цэрэну (Phase 2 partnership)
audience: Цэрэн, Левенчук (ШСМ), потенциальные партнёры
render_engine: Mermaid (GitHub native render + Notion native render)
parent_canonical:
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
style_guide: ../../operations/mermaid-style-guide-2026-05-07.md
preview_setup: ../../operations/mermaid-preview-setup-2026-05-07.md
authoring_skills:
  - .claude/skills/mermaid-create/SKILL.md
  - .claude/skills/mermaid-iterate/SKILL.md
  - .claude/skills/mermaid-export/SKILL.md
  - .claude/skills/mermaid-validate/SKILL.md
status: active
---

# 📊 Diagrams 2026-05-07 — для видео Цэрэну

> **Stack:** Mermaid (text-to-diagram, free, GitHub + Notion native render).
> **Workflow:** CC пишет mermaid в `.md` → push → Ruslan открывает file в GitHub
> или Notion subpage → видит рендер автоматически → feedback в chat → CC edit → push → refresh.

---

## 4 диаграммы

| # | File | Что покрывает | Source |
|---|------|---------------|--------|
| 1 | [01-workshop-7-elements.md](01-workshop-7-elements.md) | 🏭 7 базовых элементов мастерской (фундамент / охрана / склад / станки / мастер / автоматизация / телефон) | 1A §1.3 + Workshop concept §3 |
| 2 | [02-trm-6-resources.md](02-trm-6-resources.md) | 💼 TRM — 6 ресурсов клиента под управлением (финансы / время / аудитория / знания / compute / команда) | TRM model §3 |
| 3 | [03-l0-l5-ladder.md](03-l0-l5-ladder.md) | 🪜 L0-L5 Land-and-Expand ladder (от €3K diagnostic → asset management) | TRM §5 + 1B §3 |
| 4 | [04-collaboration-triangle.md](04-collaboration-triangle.md) | ⚭ Synergy: Ruslan + Цэрэн + ШСМ (Левенчук) → Mittelstand | 1B §10 Roadmap |

---

## 🔄 Workflow

### Где открывать (3 варианта)

1. **GitHub UI** (рекомендую — самое быстрое):
   - Open file URL → GitHub renders mermaid в браузере автоматически
   - Refresh страницы → видишь updates
   - Без login, без подписки, instant
   - Пример URL: `https://github.com/Bogersebekov/jetix-os/blob/main/swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md`

2. **Notion subpage** `📊 Diagrams` под Daily Log 7.05:
   - Mermaid embedded как code block с language=mermaid
   - Notion renders native
   - Можешь добавлять комментарии прямо в Notion

3. **Mermaid Live Editor** (для quick experiments):
   - [mermaid.live](https://mermaid.live/)
   - Paste mermaid block → instant preview + theme switcher + export PNG/SVG
   - Без login

### Workflow цикл

1. **Ruslan открывает GitHub URL** конкретной diagram
2. **Видит current render**
3. **Feedback в chat:** «нода X должна быть больше / связь Y цвет другой / добавь Z»
4. **CC edit `.md`** → commit → push на main
5. **Ruslan refresh страницу** → видит updated diagram
6. Repeat пока pixel-perfect → final SVG export для видео

---

## 🟢 Что НЕ нужно устанавливать

- ❌ D2 / TALA / D2 Studio — отказались, Mermaid лучше для git workflow
- ❌ Antigravity D2 extension
- ❌ Подписки

## 🟡 Что опционально (если захочешь offline edit)

- **Mermaid VSCode extension** — preview pane локально (для CC edit это не нужно — ты смотришь в GitHub)
- **Mermaid Chart desktop** — paid, не нужен

---

## 📁 Структура

```
swarm/wiki/synthesis/diagrams-2026-05-07/
├── INDEX.md                       (этот файл — navigation)
├── 01-workshop-7-elements.md      (готов / WIP / TBD)
├── 02-trm-6-resources.md          (TBD)
├── 03-l0-l5-ladder.md             (TBD)
└── 04-collaboration-triangle.md   (TBD)
```

Старые D2 sources (`workshop-7-elements.d2` + `v1-component-architecture.d2`) **остаются** в `swarm/wiki/synthesis/foundation-visuals-2026-04-30/` — append-only, как archive.

---

## 🛠 Canonical tooling (2026-05-07)

- **Style guide** — [`mermaid-style-guide-2026-05-07.md`](../../operations/mermaid-style-guide-2026-05-07.md) — palette, naming, init directive, validation checklist
- **Preview setup** — [`mermaid-preview-setup-2026-05-07.md`](../../operations/mermaid-preview-setup-2026-05-07.md) — Antigravity / GitHub / Notion / mermaid.live / mmdc
- **Skills:**
  - `/mermaid-create <topic>` — scaffold new diagram
  - `/mermaid-iterate <file> <change>` — apply text-instruction edit
  - `/mermaid-export <file>` — render SVG/PNG
  - `/mermaid-validate <file-or-glob>` — syntax + style compliance check
- **Research base** — [`reports/mermaid-research-notes-2026-05-07.md`](../../../../reports/mermaid-research-notes-2026-05-07.md) — Mermaid 2026 syntax + render env feature matrix
