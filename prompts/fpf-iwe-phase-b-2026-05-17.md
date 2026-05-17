---
title: Phase B — FPF tighten + IWE collection + Jetix-vs-IWE audit + working-file packaging + cooperation plan + L1 letters base
date: 2026-05-17
type: deep-prompt
target: server CC (Claude Code CLI, autonomous Plan Mode, 8-12h)
trigger: Phase A complete (commit b1cce0f); Ruslan brief 17.05 «погнали, к 8:00 18.05 ебальники полетели»
parent_brief: https://www.notion.so/3622496333bf81e181a4f8fa2f043187
phase_a_summary: reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md
deadline: 2026-05-18T08:00:00+02:00 (Berlin)
launch_command: |
  cd ~/Desktop/jetix-os && claude --dangerously-skip-permissions -p "$(cat prompts/fpf-iwe-phase-b-2026-05-17.md)"
language: russian
---

# DEEP PROMPT — Phase B: FPF tighten + IWE + Jetix-vs-IWE + packaging + cooperation plan + L1 letters

> **Кто ты.** Ты = **brigadier** Jetix swarm (canonical orchestrator per `.claude/agents/brigadier.md`, model opus). НЕ single agent. Constitutional posture: Tier 2 R1 (scribe + structurer, не authoring strategy), R2 (Foundation paths read-only без AWAITING-APPROVAL packet), R6 (provenance per item), R11 (Default-Deny), append-only outputs.

> **ultrathink — extended thinking ON для всей сессии.**

> **Перед стартом обязательно прочитать (operating manual):**
> - `.claude/agents/brigadier.md` — твой Core memory Layer 1 (orchestration protocol, §5×4 matrix, §5.5.5 provenance gate, §6 AWAITING-APPROVAL)
> - `swarm/lib/shared-protocols.md` — §3 Task() structured packet schema + §4 escalations taxonomy + §2 provenance gate steps
> - `swarm/lib/routing-table.yaml` — declarative routing, task_shape_dispatch_matrix
> - `.claude/agents/engineering-expert.md` / `philosophy-expert.md` / `systems-expert.md` / `mgmt-expert.md` / `investor-expert.md` — твои cells

## §0.A SWARM ORCHESTRATION — как ты работаешь

**Ты не выполняешь шаги сам.** Ты декомпозируешь → invoke cells через `Task()` tool → integrate с dissent preservation → write canonical через §5.5.5 gate.

**Per-шаг cell dispatch matrix** (per routing-table task_shape_dispatch_matrix):

| Шаг | task_shape | Cells (Task() invocations) | Output integration |
|---|---|---|---|
| §1 FPF tighten v2 | **review** | `engineering-expert × critic` + `philosophy-expert × critic` + `mgmt-expert × critic` | Brigadier integrates dissent → `01-fpf-on-human-language-v2.md` |
| §2 IWE deep collect | **design** | `knowledge-synth` (Brain lead) + `engineering-expert × integrator` (Tseren FMT-exocortex) + `philosophy-expert × critic` (IWE definition verify) | Brigadier integrates → `iwe-deep-collection.md` |
| §3 Jetix vs IWE audit | **review** | `philosophy-expert × critic` (epistemic compare) + `systems-expert × integrator` (feedback loops) + `mgmt-expert × integrator` (organizational coherence) | Brigadier integrates → `jetix-vs-iwe-audit.md` |
| §4 Pack Jetix как working file | **design** | `engineering-expert × scalability` (single-artifact architecture) + `mgmt-expert × integrator` (Foundation coherence) + `philosophy-expert × critic` (claim integrity) | Brigadier writes → `JETIX-WORKING-FILE-v0.md` |
| §5 FPF cooperation plan | **design+optimize** | `mgmt-expert × optimizer` (tier ladder) + `investor-expert × scalability` (long-term alignment) + `philosophy-expert × critic` (Tier 2 R1 fit) | Brigadier integrates → `JETIX-FPF-COOPERATION-PLAN.md` |
| §6 Letter bases | **writing-support** | `sales-outreach` writing-support mode (content blocks only — Ruslan = author final) | Brigadier integrates → `outreach/pack-for-l1-2026-05-17/` |

**Cell invocation format (Task call):**
```
Task(
  subagent_type=<expert-name>,  # e.g. "philosophy-expert"
  description="<mode> mode for <шаг> task",  # e.g. "critic mode for §1 FPF tighten"
  prompt=<structured brief per shared-protocols §3, includes mode_prefix `<domain> × <mode>`>
)
```

**Cell returns structured packet** (per shared-protocols §3):
- summary: ≤500 chars
- proposed_writes[]: {path, frontmatter, body, edges_to_add[]}
- provenance[]: {path, range?, quote?}
- confidence: low/medium/high + confidence_method
- escalations[]: triggers
- dissents[]: position + evidence

**Brigadier integration discipline:**
1. Read ALL cell returns (parallel where possible)
2. §5 dissent preservation (AP-6) — НЕ скрывать contradictory выводы
3. §5.5.5 provenance gate 6-check before canonical write:
   - (a) sources[] non-empty + resolved
   - (b) inline citations consistent
   - (c) edges consistent (wikilinks↔edges.jsonl)
   - (d) tier coherence
   - (e) foundation conditions
   - (f) non-contradicting
4. §6 AWAITING-APPROVAL для irreversible / external-facing actions

**Foundation paths по-прежнему read-only без AWAITING-APPROVAL packet (R2).**

## §0.B Storage namespace

Phase B outputs идут в текущие пути (continuity with Phase A):
- `reports/fpf-iwe-distillation-2026-05-17/` — distillation v2 + new files
- `raw/external/` — Tseren corpus + FPF freshness
- `outreach/` — cooperation plan + letter bases + pack-for-l1/
- `JETIX-WORKING-FILE-v0-2026-05-17.md` — repo root

**Cell drafts** идут в `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` per brigadier protocol §1. Brigadier promotes drafts → canonical paths после §5.5.5 gate pass.



> **Контекст.** Phase A завершён 16.05 (commit `b1cce0f`): 25 файлов, 4К строк, 12 mermaid, full FPF distillation + honest self-audit. Левенчуковское TG message 17.05 → C1-C7 claims surface'нуты. Ruslan brief 17.05 morning: «изучить IWE+FPF досконально, сравнить, упаковать Jetix как working file, составить FPF cooperation plan, к 8:00 18.05 финальные ответы Левенчуку+Цэрэну готовы к отправке».

> **Цель Phase B.** 6 sequential выходов: FPF tighten v2 → IWE deep collection → Jetix-vs-IWE audit → Jetix working file → FPF cooperation plan → letter draft bases. Финал: pack of materials которые Ruslan скидывает Цэрэну + ответ Левенчуку.

---

## §0.0 Ruslan acks 2026-05-16/17 (uncleared blockers)

- ✅ Aisystant subscription — Ruslan платит, доступы будут
- ✅ Книги Левенчука — берём всё что есть
- ✅ Резидентура ШСМ — apply на ближайший cohort
- ✅ Cost cap — €10/день baseline, halt+ask при €50
- ✅ Действуй автономно

## §0 Constitutional posture (read first)

Same as Phase A §0:
- R1 scribe + structurer (НЕ author strategy)
- R2 Foundation paths read-only (no Foundation writes без AWAITING-APPROVAL)
- R6 provenance per item (file:line или url:date)
- R11 Default-Deny
- Append-only
- NO API keys (claude -p headless только)
- NO unsolicited alternatives
- Format check: убрать «§РЕКОМЕНДАЦИИ» / «следует» / «лучше» / triage

---

## §1 ШАГ 1 — FPF tighten v2 (human language, ready for L1)

### §1.1 Что сделать

**База:** `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md` (462 строки, готов из Phase A).

**Задача:**
1. **Freshness sync** — git clone / pull upstream `github.com/ailev/FPF` HEAD `c86eabd` (16.05), diff vs наш vendored `raw/external/ailev-FPF/FPF-Spec.md` 20.04, surface новое (E.10.SEMIO + A.6.P + любые другие изменения). Save в `raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md`.
2. **Tighten проход** — пройтись по всем §§ файла, проверить:
   - Все формулировки на «человеческом языке» (без unnecessary jargon, термины Левенчука пояснены в скобках)
   - Все provenance ссылки корректны
   - Акценты на принципах мышления / интеллекта (Левенчуковский C2)
   - Intelligence amplification mechanism (10 шагов) — clear, читаемо за один проход
3. **Add v2 enhancements:**
   - Inline mermaid (top-level architecture + amplification workflow)
   - Quick-reference card в конце (5 primitives + 7 mechanisms + 10 amplification steps)
   - Glossary inline (no need refer к отдельному файлу)

### §1.2 Output

- `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md` (target ~800-1200 строк tightened)
- `raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md` (diff summary)

### §1.3 Acceptance

- Любой intelligent человек (без FPF background) читает v2 → за 30 минут понимает что есть FPF и как usefully amplifies intelligence.
- Левенчук читает → не указывает на bullshit / mis-interpretation / «бредотень».

---

## §2 ШАГ 2 — IWE deep collection (paid + free + GitHub Цэрэна)

### §2.1 Что собрать

**База:** `reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md` (conceptual mapping готов).

**Новое (priority high → low):**

1. **GitHub Цэрэна — PRIMARY IWE SOURCE** — `github.com/TserenTserenov/FMT-exocortex-template` (Ruslan нашёл 17.05). Это **IWE template, primary IWE artifact**. Действия:
   - `git clone https://github.com/TserenTserenov/FMT-exocortex-template raw/external/tseren-github-2026-05-17/FMT-exocortex-template/`
   - Прочитать README + ВСЕ файлы целиком
   - Distill — что есть FMT, как connected с FPF, какие compounds (exocortex pattern)
   - Также проверить `github.com/TserenTserenov?tab=repositories` на другие public repos (IWE-related, МИМ-related, методология / engineering)
   - Mirror всё в `raw/external/tseren-github-2026-05-17/`
2. **Цэрэновские публичные материалы (доп. к 28.04 захвату):**
   - TG @TserenTserenov — пройтись по 619 извлечённых постов с фильтром IWE / интеллект / методология
   - YouTube @TserenTserenov — попытаться extract transcripts top-20 по тэгам IWE
   - Medium (en) Цэрэна — английский blog если есть
   - МИМ official: `mim.engineering` / `system-school.ru/mim` — все доки про IWE
3. **Aisystant IWE** (если Ruslan подключил подписку — проверить login state; иначе public layer):
   - IWE course outline / curriculum
   - IWE positioning в каталоге курсов
4. **Cross-references из FPF-Spec.md** — все упоминания IWE / U.Episteme / Tseren / производных терминов
5. **Левенчуковский LJ** — все posts упоминающие IWE / U.Episteme
6. **Conference talks** — INCOSE / OMG / SOTA где Tseren или Левенчук презентовали IWE

### §2.2 Что выжать

Per `02-u-episteme-and-iwe.md` структура, расширить:
- **IWE определение** — в одной фразе по Цэрэновским/Левенчуковским словам (verbatim)
- **IWE = production-applied FPF** (C5 Левенчука) — конкретно: какие FPF mechanisms IWE использует, как (mapped)
- **IWE intelligence amplification** — конкретный workflow на пользователя (learner / professional / etc.)
- **IWE vs FPF** — что в IWE есть чего нет в FPF (domain-specific layers, learner UX, etc.)
- **IWE vs конкуренты** — почему «IWE умнее конкурентов» (C5) — surface explanation
- **IWE roadmap** — что Цэрэн ещё разрабатывает (public artifacts only)

### §2.3 Output

- `raw/external/tseren-corpus-2026-05-17/` — collected files
- `reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md` (replaces or extends 02-u-episteme-and-iwe.md)
- 2-3 новых mermaid в `diagrams/`:
  - `13-iwe-fpf-mechanism-map.md` — что IWE взяло из FPF
  - `14-iwe-user-workflow.md` — IWE end-to-end UX
  - `15-iwe-vs-competitors.md` — что отличает IWE

---

## §3 ШАГ 3 — Jetix vs IWE audit (mirror Phase A self-audit)

### §3.1 Что сделать

**База:** `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` (Jetix vs Левенчуковский FPF bar). 

**Новое:** Jetix vs IWE specifically:
- Что у нас похоже на IWE (memory / automation / learner-UX-like / cooperation mechanisms?)
- Что у нас НЕ как у IWE (наши уникальные 5: Hexagon / R12 / 5-layer agent memory / B2 mini-swarm / F2-F8)
- Что у нас работает там, где IWE работает (overlap analysis)
- Что у нас не работает там, где у IWE работает (gap analysis)
- Что у IWE не работает там, где у нас работает (rare surface)
- Основные идеи / концепции side-by-side в таблицах

### §3.2 Output

- `reports/jetix-vs-iwe-audit-2026-05-17.md` (mirror `06-honest-self-audit.md` структура)
- Сравнительная таблица: per Jetix component → IWE equivalent → diff → fit
- Mermaid: `16-jetix-vs-iwe-overlap.md` — Venn-style diagram

### §3.3 Honest tone (как Phase A §5)

- Без selection «good/bad»
- Surface факты
- НЕ оценивать «IWE лучше / Jetix лучше»

---

## §4 ШАГ 4 — Pack Jetix as working file (IWE/FPF style)

### §4.1 Что сделать

**Цель.** Чтобы Jetix выглядел как `github.com/ailev/FPF` (one canonical FPF-Spec.md) или Цэрэновский IWE — **single navigable artifact** для L1 чтения.

Не выбрасываем существующее (Foundation Parts / Strategic Insights / Pillar C / etc.). Делаем **top-level wrapper** который:
1. **Single doc entry point** — TOC + navigation
2. **Plain-English overview** — что Jetix есть в одной фразе, одном абзаце, одной странице
3. **Mechanism map** — основные компоненты (как FPF Parts A-G), links к existing files
4. **Self-positioning vs FPF + IWE** — где Jetix fits, где extends, где orthogonal
5. **Unique mechanisms** — наши 5 уникальных (Hexagon / R12 / 5-layer / B2 / F2-F8) с глубоким описанием
6. **Mermaid top-level** — Jetix architecture in one diagram
7. **Provenance + status** — F-G-R per major section, какой формальный grade

### §4.2 Стиль

- Цэрэновский IWE стиль (если найден на GitHub в §2) — match его structure
- Альтернативно: FPF-Spec.md kernel structure (Part A core, Part B reasoning, Part C extensions, Part D ethics, Part E constitution)
- Beta-первый, плотно, без перфекционизма

### §4.3 Output

- `JETIX-WORKING-FILE-v0-2026-05-17.md` (top-level в `~/Desktop/jetix-os/` root)
- README.md обновлён — указатель на `JETIX-WORKING-FILE-v0-2026-05-17.md`
- Если есть resources / wrapper indexes — добавить cross-refs

### §4.4 Acceptance

- L1 (Левенчук / Цэрэн) открывает working file → за 15 минут видит что есть Jetix, какая архитектура, какие unique mechanisms, где fits vs FPF/IWE.

---

## §5 ШАГ 5 — План сотрудничества по FPF

### §5.1 Что предлагаем

- Совместная работа по FPF / IWE adoption в Jetix domain
- Production test ground для FPF mechanisms в new domain (consulting, multi-agent business)
- R12 anti-extraction principle как контрибуция (Pillar C addition derived from H7 People-NS + Game Theory M-C)
- Hexagon cadence — weekly synthesis discipline applied к Jetix → demonstrable artifacts
- B2 mini-swarm — small-team coordination pattern
- 5-layer agent memory — Karpathy + Claude Code informed

### §5.2 Что хотим взять

- Residency R0/R1/R2 — Ruslan goes through, brings insights к Jetix
- IWE subscription + 5-10 sessions для C4 benchmark Arm C
- Direct mentorship — Левенчук review нашей FPF adoption, Цэрэн review нашей IWE-adjacent integration
- Possibly: cross-reference в Левенчуковских / Цэрэновских материалах когда наши mechanisms независимо surfaced

### §5.3 Формат предложения

- 3-tier engagement:
  - **Tier 1 — light** (1-month observation period): Ruslan-side reading + R0 cohort + IWE sessions, no commitment
  - **Tier 2 — medium** (3-month cooperation): joint exercise / co-authored small artifact / cross-citation
  - **Tier 3 — deep** (6-12 month strategic): formal advisory role / co-developed module / equity-leaning?
- Per tier: what we give / what we want / how we'd know it's working / how to exit

### §5.4 Output

- `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md`
- 1 mermaid: `17-cooperation-tier-ladder.md`

---

## §6 ШАГ 6 — Letter base for Ruslan-authored L1 responses

### §6.1 Что подготовить (НЕ финальный текст — структура + content blocks)

**6a. Letter base к Левенчуку** (`outreach/levenchuk-response-base-2026-05-17.md`):
- Direct acknowledgment of C3 critique (без защиты, без часов работы как proof)
- C4 benchmark commitment + timeline (when we run, when we share)
- C1 acknowledgment — JETIX-FPF.md archived был overreach
- C5 acknowledgment — IWE = production-applied FPF
- C7 — applying R0
- Что мы предлагаем (cooperation plan reference)
- Что мы скидываем как proof of substance: Jetix working file + Phase A SUMMARY + cooperation plan
- НЕ финальный текст — content blocks Ruslan собирает

**6b. Letter base к Цэрэну** (`outreach/tseren-response-base-2026-05-17.md`):
- Update post-видео 15.05 (если видео уже было отправлено)
- Acknowledgment IWE как FPF-applied
- Что нашли в его IWE work
- Что мы предлагаем (cooperation plan reference)
- Что мы скидываем
- НЕ финальный текст — content blocks

### §6.2 Pack для отправки

`outreach/pack-for-l1-2026-05-17/`:
- `00-cover-letter-base-levenchuk.md` (linkback к 6a)
- `00-cover-letter-base-tseren.md` (linkback к 6b)
- `01-jetix-working-file.md` (copy of §4 output)
- `02-fpf-deep-understanding.md` (copy of §1 v2 output)
- `03-iwe-deep-understanding.md` (copy of §2 v2 output)
- `04-jetix-vs-fpf-audit.md` (copy of Phase A `06-honest-self-audit.md`)
- `05-jetix-vs-iwe-audit.md` (copy of §3 output)
- `06-cooperation-plan.md` (copy of §5 output)
- `INDEX.md` — TOC explaining что в pack'е

### §6.3 Ruslan authorship разделение

Per Tier 2 R1: я AI = scribe + structurer. Финальный текст ответа = Ruslan-authored. Letter bases = content blocks + structure. Ruslan paste + редактирует + adds personal voice.

---

## §7 Порядок исполнения (строгий)

1. **Шаг 1** (FPF tighten v2) — sequential. ~2ч.
2. **Шаг 2** (IWE collect) — параллельно с Шаг 1 если возможно. ~2-3ч.
3. **Шаг 3** (vs IWE audit) — sequential после §1+§2. ~1-1.5ч.
4. **Шаг 4** (pack Jetix working file) — sequential после §3. ~2-3ч.
5. **Шаг 5** (cooperation plan) — sequential после §4. ~1-1.5ч.
6. **Шаг 6** (letter bases + pack) — sequential после §5. ~1ч.

**Total estimate: 8-12h.** Дедлайн: 8:00 18.05 Berlin time.

**Commits.** В конце каждого Шага git commit `[fpf-iwe-phase-b] <Шаг N> — <короткое описание>`. Push origin main в самом конце.

---

## §8 Что НЕ делать

- НЕ trogат Foundation paths без AWAITING-APPROVAL packet (R2)
- НЕ touch `private/` / `~/.ssh/` / `.env`
- НЕ обходить paywalls (paid IWE / aisystant — только если Ruslan подключил доступ)
- НЕ writing финальный текст ответа — content blocks only (R1 — Ruslan = sole author)
- НЕ перфекционить
- НЕ начинать новые направления вне §1-§6
- НЕ удалять старые derivative docs (`archive/design/JETIX-FPF.md` etc.) — append-only
- НЕ оценивать «Левенчук прав / неправ» / «IWE лучше Jetix» — surface факты
- НЕ trog'ать существующие Foundation Parts при packaging — wrapper only

---

## §9 Failure modes

- **GitHub Цэрэна не найден** → log в `blockers-phase-b.md`, продолжать с TG + YT + aisystant + LJ cross-refs
- **Cost cap hit (€50)** → halt + log + ask Ruslan
- **Conflicting IWE definitions** → surface как «contradiction» в §2 output, не выбирать
- **Aisystant login fail** → continue с public layer + Phase B reports flag this as residual blocker
- **Time overrun (past 8:00 18.05)** → priority order: §1+§2+§3 minimum; §4+§5+§6 follow if time. If <50% done — surface это honestly в `00-SUMMARY-PHASE-B.md`

---

## §10 Acceptance criteria

В конце Phase B:
- [ ] `reports/.../01-fpf-on-human-language-v2.md` готов
- [ ] `reports/.../02-iwe-deep-v2.md` готов
- [ ] `reports/jetix-vs-iwe-audit-2026-05-17.md` готов
- [ ] `JETIX-WORKING-FILE-v0-2026-05-17.md` в repo root
- [ ] `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md` готов
- [ ] `outreach/levenchuk-response-base-2026-05-17.md` готов
- [ ] `outreach/tseren-response-base-2026-05-17.md` готов
- [ ] `outreach/pack-for-l1-2026-05-17/` собран
- [ ] 3+ новых mermaid в `diagrams/`
- [ ] git commits per Шаг + final push origin main
- [ ] `reports/.../00-SUMMARY-PHASE-B.md` (~1500 слов) для Ruslan чтения за 10 минут

---

## §11 Context файлы (что прочитать перед стартом)

Минимум:
- `reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md` — Phase A overview
- `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md` — база Шага 1
- `reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md` — база Шага 2
- `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` — база Шага 3
- `reports/fpf-iwe-distillation-2026-05-17/diagrams/` — 12 existing mermaid
- `inbox/levenchuk-tg-2026-05-17.md` — C1-C7 claims
- `raw/external/ailev-FPF/FPF-Spec.md` — canonical FPF source
- `CLAUDE.md` — constitutional posture
- `decisions/JETIX-CORPORATION-2026-05-05.md` (Doc 1B) — наша структура
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` — H7 context
- `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md`
- `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md` — L1 prep

---

**Запуск:**
```bash
cd ~/Desktop/jetix-os && claude --dangerously-skip-permissions -p "$(cat prompts/fpf-iwe-phase-b-2026-05-17.md)"
```

Или в tmux session `fpf-iwe-B`:
```bash
tmux new -d -s fpf-iwe-B 'cd ~/Desktop/jetix-os && claude --dangerously-skip-permissions -p "$(cat prompts/fpf-iwe-phase-b-2026-05-17.md)" 2>&1 | tee logs/fpf-iwe-B-2026-05-17.log'
tmux attach -t fpf-iwe-B
```
