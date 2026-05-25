---
title: Phase 4 — Outdated / устаревшее (drop из активного фокуса)
date: 2026-05-25
type: phase-report
phase: 4
parent_prompt: prompts/jetix-full-map-and-docs-skeleton-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: jetix-full-map-and-docs-skeleton-phase-4
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + append-only
language: russian primary
---

# 🗑️ Phase 4 — Что устарело (drop из активного фокуса)

> **Что это.** Список документов/планов, которые superseded или deprecated. **Drop ≠
> delete.** Append-only: ничего не удаляем — только убираем из *активного фокуса*. Каждый
> пункт: что устарело / чем заменено / куда смотреть вместо.
>
> **R2 STRICT:** этот список — *surface*, не действие. Реальная архивация (`git mv`) — R1
> решение Руслана, не этого run'а.

---

## §0 TL;DR

- **4 категории устаревшего:** (1) superseded версии (V1→V2), (2) deprecated roster (12 агентов), (3) superseded планы (старые монетизации), (4) scaffold-незавершённое (Wave 1.4 pending).
- **Главное:** legacy 12-агентный roster (заменён ROY swarm), Method V1 (заменён V2), старые tokenomics-варианты (заменены V10 Hybrid), `distribute.py` (заархивирован осознанно).
- **Не путать с substrate:** 80+ книг, research-deep'ы, D-LOCK — **не устарели**, они depth-refs. Устарело только то, что *заменено новее версией*.

---

## §1 Superseded версии (заменены новее версией)

| Что | Статус | Чем заменено | Смотреть вместо |
|---|---|---|---|
| `METHOD-DEEP-DESCRIPTION-2026-05-21.md` (V1) | reference-only | Method V2 human-language | `METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` 🔒 |
| `DMITRIY-CALL-PLAN-2026-05-22.md` | superseded | переписан под actual prompt 25.05 | `CALL-PLAN-DMITRIY-KAISER-2026-05-25.md` |
| Старые tokenomics-варианты (V1-V9 в TOKENOMICS-VARIANTS) | reference | V10 Hybrid выбран | `ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md` §V10 🔒 |
| `JETIX-NAVIGATION-GUIDE-2026-05-22-DRAFT.md` | ⚠️ DRAFT | нужен polish (не устарел, но не готов как final) | сам файл после polish |

**Правило:** V1-документы держим как reference (объясняют «почему пришли к V2»), но
наружу/в работу берём только последнюю версию. Не отправлять V1 партнёру.

---

## §2 Deprecated roster (заменён архитектурно)

| Что | Статус | Чем заменено |
|---|---|---|
| **Legacy 12-агентный roster** (manager / personal-assistant / system-admin / sales-lead / sales-researcher / sales-outreach / inbox-processor / crazy-agent / knowledge-synth / strategist / life-coach / meta-agent + 2 utility) | 🗑️ DEPRECATED-2026-05-17 | **ROY swarm** (17 агентов: brigadier + 5 ROY + 3 mini-swarm + 8 book-driven) |
| Файлы старого roster | архивированы `git mv` → `.claude/agents/_archived/` | per Ruslan ack `prompts/phase-0-plus-ruslan-acks-2026-05-17.md` §0.6 |

**Важно:** в CLAUDE.md таблица legacy roster ПРЕДНАМЕРЕННО сохранена (append-only, как
исторический substrate) — но помечена DEPRECATED. Активный roster = только ROY swarm.

---

## §3 Superseded планы / гипотезы

| Что | Статус | Чем заменено |
|---|---|---|
| Старые монетизационные варианты (monetization v0 / Wave2 sub-deliverables) | superseded | Economic V10 Hybrid 🔒 |
| `distribute.py` (авто-распределение voice → KB) | 🗑️ заархивирован `distribute.py.bak` | осознанно — чтобы Claude-выводы не попадали в KB без человеческого ревью (DRAFT-only) |
| `knowledge-base/` (старый pipeline raw→ingested→compiled→linted→ready) | в миграции | Wiki Architecture v2 (`wiki/`), см. `MIGRATION.md` |
| Старые гипотезо-деревья (pre-saturation hypothesis trees) | superseded | O-163 substrate saturation closed → organize, не add |
| Pre-Foundation docs (~63 файла) | archived | `archive/INDEX.md` (append-only история via `git mv`) |

---

## §4 Scaffold-незавершённое (не устарело, но «висит»)

Это **не deprecated**, а *неоконченное* — Wave 1.4 migration не доведена:

| Что | Статус | Что нужно |
|---|---|---|
| 29 D-LOCK entries | scaffold-pending-review | Wave 1.4 ack: для каждого 6 действий (PROMOTE-AS-IS / REFACTOR / SPLIT / ARCHIVE / SUPERSEDE / ESCALATE) |
| 7 стратегических инсайтов | scaffold-pending-review | реальное содержание в source `TENSIONS-*.md`, нужно promote до F4 |
| Phase 13 Build Artefacts Specs main | server CC бросил | рестарт или Cloud Cowork собирает |

**Quick win:** батч-promotion 29 D-LOCK закрыл бы крупный «висящий» хвост (см. Phase 3 §4).

---

## §5 Что НЕ устарело (anti-confusion)

Чтобы не дропнуть лишнего, явно: **следующее — depth-substrate, не устаревшее:**

- ✅ 80+ книг в markdown — depth-refs для research, append-only
- ✅ 5 research-deep'ов — substrate для R12 / методологии / образования
- ✅ JETIX-ETHEREUM-ARCHITECTURE 12-doc bundle — Phase 2+ материал (не Build, но не устарел)
- ✅ POINT-A / POINT-B — где мы / куда идём (актуально)
- ✅ JETIX-AS-X conceptual hubs (6 docs от 18.05) — insight library (D-08 active)
- ✅ wiki concepts / ideas / sources — живая lookup-сеть

**Анти-паттерн:** дропнуть substrate потому что «старый по дате». Дата ≠ устаревание.
Устарело = *заменено новее версией того же объекта*.

---

## §6 Рекомендация по фокусу (R1 surface)

Варианты для Руслана:
- **Вариант A (минимальный):** ничего не архивировать сейчас; держать DEPRECATED-маркеры, фокус только на active.
- **Вариант B (чистка):** `git mv` superseded версий (Method V1 / старые call-plan / monetization v0) в `archive/`.
- **Вариант C (закрыть хвосты):** батч-promote 29 D-LOCK + 7 insights (Wave 1.4) до F4, чтобы scaffold перестал «висеть».

*Выбор — Руслан. Этот run ничего не архивирует (R2 STRICT, append-only).*

---

*Phase 4 closure. 4 категории устаревшего (superseded версии / deprecated roster /
superseded планы / scaffold-pending) + явный список «что НЕ устарело». Drop ≠ delete.
R1 surface — архивация = решение Руслана. NO modifications.*
