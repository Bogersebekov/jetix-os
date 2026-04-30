---
name: d2-diagrams
description: Best practices для написания D2 диаграмм в Jetix. Использовать когда создаёшь / правишь .d2 файлы (особенно в swarm/wiki/synthesis/foundation-visuals-*/). Содержит canonical color scheme, theme conventions, file structure, и pattern'ы для Foundation v1.0 визуалов.
---

# D2 Diagrams Skill — Jetix Conventions

## Когда применять

Используй этот skill **каждый раз** когда:
- Пишешь или редактируешь `.d2` файл в `swarm/wiki/synthesis/foundation-visuals-*/`
- Создаёшь новые визуалы для Foundation v1.0 / Vision / strategy документов
- Правишь существующие диаграммы по запросу Ruslan'а

## Toolchain

- **D2 CLI** установлен на сервере + Windows. Версия v0.7.1+.
- **D2 Studio** (web) — для drag-and-drop visual edit. Sync через GitHub plugin.
- **VSCode/Antigravity D2 extension** — syntax highlighting.
- **SVG Preview extension** в editor — inline SVG view.

## Canonical Color Scheme (Jetix Foundation)

Все Foundation visuals используют **одну** color schema по 6 кластерам. **Никогда не меняй эти цвета** без явного approval Ruslan'а — они wired into V1 master diagram и должны быть consistent across V1-V7+.

| Кластер | Метафора (дом) | Fill | Stroke | Контраст для текста |
|---|---|---|---|---|
| Substrate | Подвал — git | `#e1f5ff` | `#0277bd` | dark text |
| Governance | Несущие стены | `#fff3e0` | `#f57c00` | dark text |
| Knowledge | Кладовая | `#f1f8e9` | `#558b2f` | dark text |
| Work | Рабочие комнаты | `#fff8e1` | `#f9a825` | dark text |
| Interaction | Гостиная и дверь | `#fce4ec` | `#c2185b` | dark text |
| Strategy | Стол стратегии | `#f3e5f5` | `#7b1fa2` | dark text |

**Source of truth:** `swarm/wiki/synthesis/foundation-visuals-2026-04-30/v1-component-architecture.d2`

## Edge Conventions

| Тип flow | Стиль stroke | Когда использовать |
|---|---|---|
| Content flow | solid 2px, цвет цели | передача данных между Parts (STOP-gate, methodology promotion, CRM edges, draft promotion) |
| Approval flow | dashed (stroke-dash: 3), `#f57c00` | любой Part → Part 6b Human Gate |
| Constitutional mirror | dashed (stroke-dash: 5), `#7b1fa2` | Pillar C → Part 6b (11 hard rules) |
| Health alert | solid 2px, `#c2185b` | Part 8 → Part 6a/6b |
| Substrate operates-in | solid 2px, `#0277bd` | Part 1 → others |

## Theme Conventions

| Use case | D2 theme | CLI flag |
|---|---|---|
| Финальный для презентации (Tseren видео) | Flagship Terrastruct | `--theme=200` |
| Default professional | Default | `--theme=0` |
| Hand-drawn для casual / brainstorm | Sketch | `--sketch` |
| Dark mode | Dark | `--theme=300` |

**Layout engine для Jetix:**
- `--layout=elk` — DEFAULT для Foundation visuals (handle complex multi-cluster well)
- `--layout=dagre` — fallback если ELK не справляется
- `--layout=tala` — premium aesthetic, требует TALA license

## File Naming Convention

```
swarm/wiki/synthesis/foundation-visuals-YYYY-MM-DD/
├── README.md                              # обзор + render commands
├── v1-component-architecture.d2           # 11 Parts overview
├── v2-data-flow-layers.d2                 # вертикальный layered
├── v3-task-sequence.d2                    # uml_sequence
├── v4-trust-boundaries.d2                 # zones
├── v5-agent-topology.d2                   # ROY + legacy
├── v6-phase-roadmap.d2                    # timeline
└── v7-constitutional-layer.d2             # 11 rules → enforcement
```

После рендера — рядом с .d2 файлом появляются `.svg` (vector, для Miro), `.png` (bitmap), `.pdf` (для печати).

## File Structure Pattern (canonical)

Каждый .d2 файл должен начинаться с этого header pattern:

```d2
# V<N> — <название визуала>
# <одна строка описания>
# Source: <откуда взято содержимое>
#
# Render:
#   d2 --theme=200 --layout=elk <name>.d2 <name>.svg
#   d2 --sketch <name>.d2 <name>-sketch.svg

title: |md
  # <главный заголовок>
  ## <подзаголовок>
| {near: top-center}

direction: <down|right>
```

Дальше — clusters / nodes / connections.

В конце — **legend** (для standalone readability):

```d2
legend: "Легенда" {
  style: {
    fill: "#f5f5f5"
    stroke: "#9e9e9e"
    border-radius: 8
    font-size: 14
  }

  solid: "─── content flow"
  dashed: "- - - approval flow → gate"
}
```

## Common D2 Patterns для Jetix

### Cluster (subgraph) с canonical стилем

```d2
substrate: "🏗 Подвал — Substrate" {
  style: {
    fill: "#e1f5ff"
    stroke: "#0277bd"
    stroke-width: 3
    border-radius: 12
    font-size: 18
  }

  P1: "Part 1\ngit substrate\ncommit interface" {
    style: {fill: "#ffffff"; stroke: "#0277bd"; border-radius: 8}
  }
}
```

### Content flow

```d2
knowledge.P2 -> knowledge.P3: "STOP-gate\nпосле ack" {
  style: {stroke: "#558b2f"; stroke-width: 2}
}
```

### Approval flow (dashed → gate)

```d2
knowledge.P2 -> governance.P6b: {style: {stroke-dash: 3; stroke: "#f57c00"}}
```

### Multi-line label

```d2
P5: "Part 5\nCompound Learning\nDRR ledger"
```

### Sequence diagram (для V3 task flow)

```d2
direction: right
shape: sequence_diagram

ruslan: "Ruslan"
voicepipe: "Voice Pipeline"
gate: "Part 6b\nHuman Gate"
wiki: "Part 3\nWiki"

ruslan -> voicepipe: "voice memo"
voicepipe -> gate: "STOP-gate request"
gate -> ruslan: "AWAITING-APPROVAL"
ruslan -> gate: "ack"
gate -> wiki: "promote draft"
```

## Anti-patterns (НЕ делать)

- ❌ **Менять canonical colors** без approval Ruslan'а
- ❌ **Mixing themes** в одном проекте (если V1 в theme=200 — все остальные тоже)
- ❌ **Слишком много nodes** (>15 в одном subgraph) — расщепляй на под-кластеры
- ❌ **Длинные labels** (>3 строк) — выноси в подзаголовок subgraph
- ❌ **Стрелки без labels** для критичных flows — теряется значение
- ❌ **Использовать TALA** без явного флага (TALA premium = $$, не free)

## Workflow с D2 Studio

Когда Ruslan работает в D2 Studio:
1. Studio имеет **GitHub plugin** подключенный к `claude/practical-swirles-24ab2a` (или текущей Cloud Cowork ветке)
2. Любые мои изменения в .d2 → push → Ruslan видит в Studio
3. Любые его изменения визуально → push back в repo → я вижу через `git fetch`

**При cycle:**
- Я делаю commit с message `[viz] V<N> — <description>`
- Ruslan делает commit с message `[viz] V<N> studio edit — <what changed>`
- Cycle short — каждые 5-10 минут sync

## Render Commands Cheatsheet

```bash
# В папке foundation-visuals-YYYY-MM-DD/

# Single file, default settings
d2 v1-component-architecture.d2 v1.svg

# С Jetix conventions
d2 --theme=200 --layout=elk v1-component-architecture.d2 v1-flagship.svg

# Sketch для casual presentation
d2 --sketch v1-component-architecture.d2 v1-sketch.svg

# Watch mode (live preview в браузере, hot reload)
d2 -w v1-component-architecture.d2 v1.svg

# Render все 7 разом (bash)
for f in v*.d2; do
  d2 --theme=200 --layout=elk "$f" "${f%.d2}.svg"
done

# Render PNG (для embed в Notion)
d2 --theme=200 v1-component-architecture.d2 v1.png

# Animation (multiple boards в одной .d2)
d2 --animate-interval 1000 v1-component-architecture.d2 v1.svg
```

## Sources

- D2 docs: https://d2lang.com/tour/intro/
- D2 themes: https://d2lang.com/tour/themes/
- D2 Studio: https://terrastruct.com/d2-studio/
- D2 GitHub: https://github.com/terrastruct/d2
- Master Foundation overview: `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` §4
- Visual plan: `swarm/wiki/synthesis/foundation-visuals-2026-04-30/README.md`
