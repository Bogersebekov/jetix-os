---
title: AI Tools & Lifehacks — Mega-page (archive ref)
date: 2026-05-25
type: phase-report-ai-tools-archive-ref
phase: 5
parent_prompt: prompts/notion-templates-3-layers-architecture-v2-2026-05-25.md
related_main: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-3-layers-architecture-v2-2026-05-25
R: low
constitutional_posture: R1 surface only + R6 + R11 + append-only
language: russian primary
audience: companion to any of 3 Notion layers
---

# 📎 AI Tools & Lifehacks — Mega-page (archive ref)

> **Archive ref → главный документ живёт в `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md`; см. там полный список 20 инструментов (16 основных в 4 кластерах + 4 bonus) с разбивкой «Что делает / Как использовать / Когда / Где живёт в Jetix».**

Этот файл — короткий указатель (Phase 5 архивный ref) в рамках Notion 3-Layers Architecture v2. Полный контент НЕ дублируется здесь намеренно — companion-страница на ≥3000 слов живёт в `decisions/strategic/`. Здесь — только оглавление, чтобы найти нужный кластер/инструмент и перейти в главный документ.

## Оглавление главного документа

- **§1 Назначение страницы** — зачем этот companion (один абзац).
- **§2 20 инструментов в 4 кластерах:**
  - 🟦 **Кластер A — Capture & Process:** Telegram processor (#1), Voice pipeline (#2), Mistral OCR (#3), Web clipper (#4).
  - 🟩 **Кластер B — Visualize & Communicate:** Mermaid quick setup (#5), Miro/Mural (#6), Excalidraw (#7), Notion charts (#8).
  - 🟨 **Кластер C — Synthesize & Decide:** Claude/GPT synthesis (#9), OFFLINE_MODE /ask (#10), Hypothesis tracker (#11), Wiki ingest (#12).
  - 🟥 **Кластер D — Coordinate & Track:** ROY swarm (#13), CRM voice integration (#14), Toggl pipeline (#15), ActivityWatch (#16).
  - ➕ **Bonus:** Mistral OCR для книг (#17), Schema validation/lint (#18), Mermaid validation (#19), AI-augmented review / plan-day (#20).
- **§3 Discovery** — как находить новые инструменты (Twitter / Hacker News / Reddit / community + правило фильтра через hypothesis tracker).
- **§4 Стыковка с 3 слоями** — таблица «какой инструмент полезнее на каком слое» (Layer 1 Personal Core / Layer 2 Team Collaboration / Layer 3 Universal Business).

## Заметки

- Большинство инструментов **уже работает** в реальной системе Jetix: 54 skill-команды Claude Code (45 single-file + 9 директорийных), Python-пайплайны в `tools/` (transcribe.py, extract.py, run_pipeline.sh, mistral_ocr.py, toggl_sync.py, aggregate_activity.py), рой из 17 ROY-агентов. Внешние/планируемые помечены явно.
- Constitutional posture: R1 surface-only + R6 + R11 (reference-doc, не авто-запуск) + append-only. Никаких Notion API-вызовов, никаких API-ключей.
