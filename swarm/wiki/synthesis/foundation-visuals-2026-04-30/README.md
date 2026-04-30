---
title: Foundation v1.0 Visuals — D2 source files
date: 2026-04-30
type: visual-overview-source
audience: ruslan
related_docs:
  - swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md
  - swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md
---

# Foundation v1.0 Visuals — D2 source files

7 диаграмм, каждая — свой ракурс на Foundation Architecture v1.0 (LOCKED 2026-04-28).

## Визуалы

| # | Файл | Что | Тип D2 |
|---|------|-----|--------|
| V1 | `v1-component-architecture.d2` | 11 Parts + Pillar C в 6 цветных кластерах | flowchart |
| V2 | `v2-data-flow-layers.d2` | вертикальный разрез 8 слоёв данных | flowchart |
| V3 | `v3-task-sequence.d2` | end-to-end поток задачи (mentor-call → Direction Card) | uml_sequence |
| V4 | `v4-trust-boundaries.d2` | HITL / Approved-AI / Autonomous / External зоны | flowchart |
| V5 | `v5-agent-topology.d2` | ROY 6 + Legacy 14 + slots в Parts | flowchart |
| V6 | `v6-phase-roadmap.d2` | Phase A → B → C+ trajectory | flowchart |
| V7 | `v7-constitutional-layer.d2` | 11 hard rules → derivation → Default-Deny | flowchart |

## Цветовая схема (consistent across all visuals)

| Кластер | Цвет (fill / stroke) |
|---|---|
| Substrate | `#e1f5ff` / `#0277bd` (blue) |
| Governance | `#fff3e0` / `#f57c00` (orange) |
| Knowledge | `#f1f8e9` / `#558b2f` (green) |
| Work | `#fff8e1` / `#f9a825` (yellow) |
| Interaction | `#fce4ec` / `#c2185b` (pink) |
| Strategy | `#f3e5f5` / `#7b1fa2` (purple) |

## Workflow рендера

### Локально (Windows / VSCode / Antigravity)

1. Открой `.d2` файл в Antigravity / VSCode с D2 extension от Terrastruct
2. Ctrl+Shift+P → `D2: Open Preview to the Side` → preview справа
3. Save → preview обновляется автоматически

### CLI (любая ОС)

```bash
# Render SVG (vector, recommended для Miro)
d2 v1-component-architecture.d2 v1-component-architecture.svg

# С темой и layout engine
d2 --theme=200 --layout=elk v1-component-architecture.d2 v1.svg

# Sketch mode (hand-drawn aesthetic)
d2 --sketch v1-component-architecture.d2 v1-sketch.svg

# Watch mode (live preview в браузере)
d2 -w v1-component-architecture.d2 v1.svg
```

### Drag-and-drop в Miro

После рендера SVG → перетащи файл прямо на Miro Board → масштабируется без потери качества.

## Источники для контента

Все визуалы — derivation из:
- Master overview (`foundation-master-overview-human-2026-04-29.md`)
- Wave D INTEGRATION-REPORT (52 inter-Part edges, 6 M-D gates)
- 11 part architecture.md
- Pillar C principles/architecture.md
