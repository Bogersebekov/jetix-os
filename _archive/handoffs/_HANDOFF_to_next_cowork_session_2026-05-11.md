# 🤝 HANDOFF — Cloud Cowork Session Context Transfer (2026-05-11 → next session)

> **Цель этого файла.** Mega context-transfer prompt для нового CC chat session. Прочитав это, новая сессия знает где мы остановились, что в работе, какие конвенции соблюдать, как продолжать.
>
> **Как использовать:** в новом chat session paste весь этот файл как первый prompt. CC прочитает + продолжит работу.

---

## §0 Кто я и что строю (для new session)

Я **Руслан**, founder **Jetix OS** — multi-agent система для управления AI consulting business + личной жизнью. Live в Берлине.

**Цель Phase 1:** $100K к концу лета 2026 ($August-September timeframe).
**Long-term:** $1T market cap trajectory (engineering-faith bet, не pyramid).

**Foundation:** 11 Parts + Pillar C, LOCKED 28.04.2026 (`foundation-architecture-locked-2026-04-28`).

---

## §1 ГДЕ МЫ СЕЙЧАС (11.05.2026 evening)

### §1.1 Сегодня (11.05) progress

**Сделано:**
- ✅ Voice pipeline Phase 2 → 8 deliverables (47 memos)
- ✅ Action Plan synthesized (4-tier ladder, 25 variants forward) — `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md`
- ✅ Video Proposal Options doc для Цэрэн + Левенчук + ШСМ — `decisions/VIDEO-PROPOSAL-OPTIONS-TSEREN-LEVENCHUK-2026-05-10.md`
- ✅ **Wiki Integration v2** — Stage 5 fix from 0% → 50.1% match rate (BM25 + Russian morphology + 3-tier classification). Merged to main, tag `wiki-integration-v2-2026-05-10`.
- ✅ **AutoResearch Phase 2 MVP** — Karpathy pattern applied. D.2 voice lens pilot: 81 experiments, 8 KEEPs, baseline 0.129 → 0.240 (+86%). Merged to main, tag `autoresearch-v1-2026-05-11`.
- ✅ Deep analysis report — `reports/deep-analysis-wiki-autoresearch-2026-05-11.md` (1095 lines, 4 mermaid, 25 variants forward)
- ✅ Wiki edges deep explanation — `reports/wiki-edges-deep-explanation-2026-05-11.md` (6 mermaid, concrete 39 examples)

### §1.2 6 Strategic Insights дня (Hexagon) — все 10-11.05

1. **Foundation Model** (10.05) — WHAT Jetix is — `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md`
2. **Partnership Model** (10.05) — HOW grow — Manifest pattern, online-first, RES.1-3 (Mittelstand DACH abandoned, R&D 90% reinvest, partnership terms deferred Phase 2) — `decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md`
3. **R&D Flywheel** (§13 within Partnership) — HOW compound — 90% reinvest target
4. **Network State (Balaji)** (10.05) — WHERE Workshop fits — `decisions/STRATEGIC-INSIGHT-BALAJI-NETWORK-STATE-2026-05-10.md`
5. **Tyson Pattern** (10.05) — HOW founder masters — depth-mentorship-dedication — `decisions/STRATEGIC-INSIGHT-TYSON-MENTORSHIP-PATTERN-2026-05-10.md`
6. **Gamified Platform** ⭐ (11.05) — WHY users engage — Torn/MMO + Castronova confirmed + Machinations.io (new core tool) + Yanis Varoufakis + Joost van Dreunen + Game Economy 10 candidates — `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md`

---

## §2 ТРИ LOCKED CANONICAL ДОКУМЕНТА (read first для context)

| # | Документ | Path | Tag |
|---|---|---|---|
| 1 | Базовая Система Управления (Документ 1A) | `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` | `base-management-system-locked-2026-05-05` |
| 2 | Jetix Corporation (Документ 1B) | `decisions/JETIX-CORPORATION-2026-05-05.md` | `jetix-corporation-locked-2026-05-06` |
| 3 | Foundation v1.0 (11 Parts + Pillar C) | `swarm/wiki/foundations/` | `foundation-architecture-locked-2026-04-28` |

Plus:
- Workshop concept LOCKED — `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- TRM model — `decisions/JETIX-TRM-MODEL-2026-04-30.md` (status fixed retroactively)
- Vision FUNDAMENTAL — `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- Foundation overviews — `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` + `foundation-master-overview-human-workshop-2026-05-06.md`

---

## §3 НОВАЯ ИНФРАСТРУКТУРА (built today, операционная)

### §3.1 Wiki Architecture v2 (Karpathy LLM Wiki + OmegaWiki)

**Main KB:** `wiki/` (НЕ `knowledge-base/` — тот в миграции).

**9 entity types:** concepts/ entities/ sources/ topics/ ideas/ experiments/ claims/ summaries/ foundations/
**Plus:** comparisons/, niches/ (6 срезов), graph/edges.jsonl (577 edges currently), _templates/.

**Skills:**
- `/ingest <path-or-url>` — source → wiki/ pages + index + log + edges
- `/ask <question>` — поиск + синтез
- `/lint` — health check
- `/consolidate` — merge дубликатов
- `/build-graph` — communities

### §3.2 Voice Pipeline Canonical (reusable, lens-driven)

- `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` — operational canon
- `tools/voice-pipeline-orchestrator.py` — orchestrator
- `tools/wiki_integration/` — Stage 5 v2 (BM25 + Russian morphology + 3-tier)
- `config/voice-pipeline-lens-template.yaml` + per-run lens configs

### §3.3 AutoResearch (Karpathy pattern applied)

- `reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md` — Phase 1 plan (16 domains, 4-phase rollout)
- `tools/jetix-autoresearch/` — orchestrator + mutation_generator + evaluator + constitutional_gate + cost_tracker
- `agents/autoresearch-brigadier/` — new role
- `config/autoresearch-hypothesis-2026-05-11-d2-voice-lens.yaml` — first pilot config
- D.2 voice lens pilot DONE: 81 exp / 8 KEEPs / 0.129 → 0.240

### §3.4 Mermaid Stack (canonical) — Variant A cool blues palette

- `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` — palette / strokes / naming
- `.claude/skills/mermaid-create/` + iterate / export / validate
- Diagrams в `swarm/wiki/synthesis/diagrams-2026-05-07/`
- Workshop v4 system boundary diagram = canonical (for video Цэрэну)

---

## §4 ЧТО В РАБОТЕ ПРЯМО СЕЙЧАС (план на overnight + tomorrow)

Per Daily Log 2026-05-11 — `https://www.notion.so/35c2496333bf81a88569e669f1303b87`:

### Шаг 1 (CURRENT) — ACK Wiki Tier A (5-10 min)
- `/wiki-bulk-ack --tier A --dry-run` → preview
- `/wiki-bulk-ack --tier A` → execute +39 edges

### Шаг 2 (TONIGHT) — Overnight Wiki Full Rebuild (9h)
- Drop `STAGE5_SKIP_LLM=1` + full LLM rerun
- All 1262 voice candidates через LLM precision rerank
- Re-categorize Tier A/B/C cleaner
- Output: `04-wiki-candidates-v3.md` + `match-rate-comparison-v3.md`

### Шаг 3 (TOMORROW MORNING) — Review Wiki Stats
- Hub nodes / themes / contradictions
- 20-30 min

### Шаг 4 (TOMORROW MID-DAY) — Gamification Deep Wiki Training
- Brigadier specifically on gamification topic
- Collect: Top 10 games + Game economy experts + Game theory + Psychology + 6 Realm entities + Concrete patterns
- Edges to existing canonical (Workshop / TRM / 1B)
- 1.5-2.5h server CC autonomous

### Шаг 5 ⭐ (TOMORROW EVENING) — Видео Цэрэну
- Recording proposal на основе Document 1B + Workshop v4 + Gamified Platform insight + mentions Левенчука/МИМ
- Send TG @TserenTserenov

---

## §5 КОНВЕНЦИИ + Style preferences (важно для CC)

### §5.1 Constitutional discipline (Tier 2 Rules)
- **R1:** AI = scribe / structurer / analyst. НЕ author strategy. Ruslan = sole strategist.
- **R2:** No architectural changes без gate (AWAITING-APPROVAL packet via Part 6b).
- **R6:** Provenance per item (memo:line + commit SHA + file path).
- **R11:** Default-Deny on uncategorized actions.
- **Append-only** для all artifacts.

### §5.2 Language + tone
- **Русский primary.** English ok для technical / code / commit messages.
- **Прямой, без воды.** Никаких corporate buzzwords.
- **НЕ multi-choice опросы** ("выбери из 5") — делать research/задачу до конца.
- **НЕ daунгрейдить** на "solo-founder scope" — всегда $1T trajectory baseline preserved.
- **Beta-первый.** Не perfectionize. $50K → $100K первичная цель.

### §5.3 Workflow (Cloud Cowork ↔ Server CC)
- Cloud Cowork (этот chat) = lightweight bridge + short briefs.
- Server CC = deep prompts + autonomous Plan Mode + execution.
- Pattern: я даю short brief → server CC pишет deep prompt → следующая CC session выполняет.
- НЕ pushить много кода в Cloud Cowork — delegate execution к server CC.

### §5.4 Git discipline
- НЕ force-push без explicit ask
- НЕ skip hooks (`--no-verify`)
- НЕ touch `~/.ssh/` / `private/` / `.env`
- НЕ commit secrets
- Commit messages: `[area] description` (`[strategic-insight]`, `[voice-pipeline]`, `[autoresearch]`, etc.)

### §5.5 NO API keys
- Все LLM calls через `tools/lib/cc_helper.py` → `claude -p` headless (Max sub).
- НЕ touch `ANTHROPIC_API_KEY` env var.
- Cost cap €10/день для external services только.

---

## §6 КЛЮЧЕВЫЕ ЛЮДИ + ВНЕШНИЕ КОНТАКТЫ

### §6.1 Active outreach targets (Phase 1)
- **Цэрэн Цэрэнов** — TG `@TserenTserenov` — Managing Partner МИМ (Мастерская Инженеров-Менеджеров, новая 2026 structure spin-off ШСМ). 11-летний партнёр Левенчука. Video sent 04.05 (response unknown). Critical path A1.1 Action Plan.
- **Анатолий Левенчук** — научный руководитель ШСМ; equal-partner Цэрэна; methodology specialist. Critical path A1.2 Action Plan.
- **Strategic Council 7-8 candidates** — Оскар / Федорев / Олег / другие TBD per Action Plan A2.1.

### §6.2 Game Economy Experts (future Phase 2+ outreach)
- **Yanis Varoufakis** (ex-Valve economist, ex-Greek Finance Minister) — TOP candidate
- **Edward Castronova** (Indiana University, «Synthetic Worlds» author) — CONFIRMED по Ruslan ack 11.05 — primary academic mentor target
- **Joost van Dreunen** (NYU Stern professor) — likely the "профессор YouTube" Ruslan имел in mind
- + 7 more candidates (Eyjólfur Guðmundsson, Lehdonvirta, James, Shokrizade, Williams, Trudeau, Sarbaum)

### §6.3 Mentors (personal)
- **Антон** — ментор, системное мышление, психология
- **Владислав** — экономист, value-based pricing
- **Родион** — YouTuber, AI-темы

---

## §7 PROJECTS (8 active)

| ID | Project | Priority | Status |
|---|---|---|---|
| quick-money | Быстрые деньги (AI services for biz) | P1 | Active |
| research | Research | P2 | Active |
| brand | Бренд Jetix | P2 | Active |
| community | Community | P3 | Planned |
| ai-tools | AI-инструменты | P2 | Active |
| life-os | Life OS | P3 | Active |
| engineering-thinking | Инженерное мышление | P3 | Active |
| bets | Ставки на будущее | P4 | Paused |

---

## §8 ⚠️ TENSIONS / UNRESOLVED (для будущего strategic session)

Per `STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md` §10.1:

- **RES.1 Mittelstand DACH ICP → ABANDONED.** Online-first verticals = Phase 1 focus. Document 1B §7 needs rewrite at next revisit.
- **RES.2 R&D 90% reinvest target.** Founder living costs bare minimum.
- **RES.3 Equity-leaning partnership terms** deferred to Phase 1→2 transition.

Plus 5 open tensions surfaced в Action Plan §1.5:
1. Уволиться сейчас vs больничные (cash runway)
2. Strategic Council 7-8 vs Document 1B §10 «3-5 человек к концу первого месяца»
3. Workshop scale ambiguity (Life OS vs Strategic Council vs customer product)
4. Outreach posture (голодный vs гивер vs open)
5. Сосредоточиться только на Jetix vs AI-услуги quick

---

## §9 КАК ПРОДОЛЖАТЬ В НОВОЙ СЕССИИ

### §9.1 First actions

1. Read this handoff fully
2. Read Document 1A + Document 1B + Workshop concept (§2 above) — TL;DR each (5-10 min)
3. Glance at canonical/INDEX.md если нужен fuller orientation
4. Glance at `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` Tier 1-4 ladder
5. Check status: `git log origin/main --oneline -20` to see most recent commits

### §9.2 Current focus

Per Daily Log 11.05 plan §4 above — overnight wiki rebuild → gamification deep wiki training → видео Цэрэну. Если sessионю late evening 11.05 / morning 12.05 — check what brigade outputs accumulated overnight.

### §9.3 What NOT to do

- НЕ promote strategy autonomously (Ruslan = sole strategist)
- НЕ trogает Foundation paths без AWAITING-APPROVAL packet
- НЕ pushить prematurely к main без acks
- НЕ override constitutional discipline
- НЕ создавать новые insights без Ruslan input
- НЕ commit без Ruslan ack

### §9.4 Tone

- Direct, without filler
- Russian primary
- No multi-choice
- Don't downgrade to solo-founder framing
- Beta-first, action-oriented

---

## §10 КЛЮЧЕВЫЕ ПУТИ (cheat sheet)

| Что | Path |
|---|---|
| Canonical INDEX | `canonical/INDEX.md` |
| Daily Logs Notion DB | `30a24963-33bf-8005-817a-000beb10bcd4` |
| Documents 1A / 1B | `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` / `decisions/JETIX-CORPORATION-2026-05-05.md` |
| Workshop concept | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` |
| Foundation v1.0 | `swarm/wiki/foundations/part-1..11/` + `principles/` |
| Action Plan | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` |
| Strategic Insights (6) | `decisions/STRATEGIC-INSIGHT-*.md` |
| Voice pipeline canon | `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` |
| Mermaid style guide | `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` |
| Wiki entries | `wiki/concepts/` / `wiki/ideas/` / `wiki/sources/` / etc. (552 entries) |
| Edges graph | `wiki/graph/edges.jsonl` (577 edges) |
| Tools | `tools/voice-pipeline-orchestrator.py` / `tools/jetix-autoresearch/` / `tools/wiki_integration/` |
| Skills | `.claude/skills/` (mermaid-create / wiki-bulk-ack / etc.) |
| Memory (cloud-cowork) | `~/.claude/projects/C--Users-49152-Desktop-jetix-os/memory/` |

---

## §11 НАЧНИ ТАК (если ты — новая CC session)

1. Прочитай этот файл fully
2. Read §2 canonical docs TL;DR
3. Дай мне (Ruslan) **короткий summary под 200 слов**: что ты понял, какой текущий state, что планируешь делать, есть ли вопросы.
4. Жди от меня next instruction.

---

**Создано:** 2026-05-11 evening (Hexagon strategic posture complete; Tier A ready to ack; overnight rebuild + gamification + video planned for tomorrow).

**Constitutional anchor:** AI = scribe/analyst, Ruslan = sole strategist. Tier 2 R1/R2/R6/R11 + append-only + Default-Deny.
