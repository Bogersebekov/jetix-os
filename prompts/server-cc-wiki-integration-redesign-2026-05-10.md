---
title: Server CC Brigadier — Wiki Integration Redesign (2-phase, Plan Mode + Ultrathink)
type: brigadier-prompt
created: 2026-05-10
author: cloud-cowork (Ruslan ack)
target_executor: server-cc on branch claude/voice-pipeline-2026-05-10 (or successor)
authority: Ruslan ack via cloud cowork chat 2026-05-10 (after Phase 2 voice pipeline review)
phase_1_mode: Plan Mode + Ultrathink
phase_2_mode: Execute approved plan
push_policy: draft commits на свою ветку, await Ruslan merge ack
F: F4
G: wiki-integration-redesign
R: refuted_if_wiki_writes_silent_or_match_heuristic_collapses_in_2nd_run
constitutional_anchor:
  - Tier 2 Rule 1 (no AI strategizing — matching + proposing only)
  - Tier 2 Rule 2 (no architectural changes без gate — wiki writes pending Ruslan ack каждый candidate)
  - Tier 2 Rule 6 (provenance per candidate)
  - Append-only (existing wiki/ untouched)
  - Default-Deny (3-gate: plan ack → execute redesign → ack candidates → write wiki/)
estimated_effort: Phase 1 = 30-45 min Plan Mode / Phase 2 = 1.5-3 hours autonomous
---

# Wiki Integration Redesign — 2-Phase Brigadier

> **Контекст.** Voice pipeline Phase 2 (2026-05-10) Stage 5 — wiki candidates extraction — **FAILED quality criteria**: match_rate=0% (0 из 1285 items found match-to-existing wiki entries). Все 1285 = propose-new. Это значит heuristic broken — items не сравниваются адекватно с existing wiki.
>
> **Goal.** Redesign Stage 5 + сделать **reusable wiki integration workflow** так что:
> 1. Future voice pipeline runs автоматически находят real match-to-existing для items уже зафиксированных
> 2. Ruslan может одобрить candidates batch-style (не по одному) — минимум manual burden, но preserve constitutional Default-Deny
> 3. Auto-merge для high-confidence matches с manual review для low-confidence
> 4. Bulk-merge mode для approved candidates → real writes в wiki/
> 5. Post-merge — voice items linked к wiki entries (cross-reference)
>
> **Branch.** Continue на `claude/voice-pipeline-2026-05-10` (or successor).

---

## §1 PHASE 1 — Plan Mode + Ultrathink

### §1.1 Inputs to study

A.1 **Current Stage 5 implementation** (что failed):
   - `tools/voice-pipeline-orchestrator.py` — orchestrator
   - Stage 5 logic — как match-to-existing была реализована
   - `reports/voice-pipeline-2026-05-10/04-wiki-candidates.md` (1285 candidates, 0 match) — что сейчас выдаёт
   - `reports/voice-pipeline-2026-05-10/07-discipline-log.md` Stage 5 verdict (PARTIAL)

A.2 **Current wiki/ state** (что сравниваемое):
   - `wiki/index.md` — catalog (count entries)
   - `wiki/concepts/` — concepts entries
   - `wiki/entities/` — entities entries
   - `wiki/sources/` — sources entries
   - `wiki/topics/` — topics entries
   - `wiki/ideas/` — ideas entries
   - `wiki/experiments/` — experiments entries
   - `wiki/claims/` — claims entries
   - `wiki/summaries/` — summaries entries
   - `wiki/foundations/` — foundations entries
   - `wiki/comparisons/` — bonus
   - `wiki/niches/` — 6 срезов
   - `wiki/graph/edges.jsonl` — typed edges (9 types)
   - `wiki/_templates/` — schemas
   - `wiki/log.md` — chronology

A.3 **Existing wiki tools** (что есть):
   - `/ingest <path-or-url>` skill — source → wiki/ страницы + index + log + edges
   - `/ask <question>` skill — поиск + синтез с citations + опциональная запись в comparisons/
   - `/lint` skill — health check (orphans, contradictions, stale claims)
   - `/consolidate` skill — merge дубликатов
   - `/build-graph` skill — пересборка communities

A.4 **Constitutional context:**
   - `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — 11 hard rules
   - `swarm/wiki/foundations/principles/architecture.md` — Pillar C principles
   - `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` — KB architecture
   - `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` — F-G-R discipline

A.5 **Voice items дerelivered:**
   - `reports/voice-pipeline-2026-05-10/04-wiki-candidates.md` — 1285 candidates (real test set)
   - `reports/voice-pipeline-2026-05-10/02-structured-clean.md` — 196 lines, deduplicated
   - `reports/voice-pipeline-2026-05-10/03-current-lens-actionables.md` — 20 top items

### §1.2 Plan Mode deliverable — `reports/wiki-integration-redesign-2026-05-10/PLAN.md`

Server CC produces **comprehensive redesign plan** answering:

**P.1 Diagnosis — почему Stage 5 failed (0% match)?**
- Heuristic был token-overlap / cosine fuzzy / regex-keyword? Какой именно?
- Существующие wiki entries — count, types, structure. Действительно ли есть entries чтобы match?
- Если wiki almost empty — все candidates legitimately propose-new. Это not failure, это reality.
- Если wiki has entries — почему не нашли? Word boundaries? Russian stemming? Thresholds?

**P.2 New approach для match-to-existing:**

Suggest 3-5 alternative approaches с trade-offs:

| Approach | Pros | Cons |
|---|---|---|
| Embedding cosine (e.g. via Claude embeddings) | Semantic match, robust к paraphrase | Cost: API calls per candidate |
| Keyword + TF-IDF | Fast, no API | Misses synonyms |
| LLM-pass (Claude Sonnet rates each candidate vs top-K wiki entries) | Highest quality | Slow, expensive |
| Hybrid: keyword filter → LLM rank top-K | Balance | Multi-stage complexity |
| Ingest each candidate via `/ingest` skill (existing) → `/ask` for similar | Reuses existing tooling | May not scale |

Recommend chosen approach + rationale.

**P.3 New approach для propose-new:**
- Template auto-fill via `wiki/_templates/<type>.md`
- Entity type inference (concept / entity / source / etc.) via Claude Sonnet
- Slug generation rules
- Frontmatter completeness (provenance + sources + tags)

**P.4 Bulk ack workflow для Ruslan:**

Ruslan не хочет ack по одному candidate из 1000+. Suggest 3-tier:
- **Tier A: High-confidence match** (score ≥0.85) — auto-merge after Ruslan single bulk-ack «approve all Tier A»
- **Tier B: Medium-confidence match** (score 0.60-0.85) — Ruslan reviews list, batch-ack subset
- **Tier C: Low-confidence / propose-new** (score <0.60 or new entry) — manual review, can defer to backlog

For each tier: explicit doc structure + workflow + commands.

**P.5 Auto-merge mechanics:**
- After Tier A bulk-ack → automatic write в wiki/<type>/ + update wiki/index.md + append wiki/log.md + update wiki/graph/edges.jsonl
- Each merged candidate gets frontmatter `voice_provenance:` field linking to source memo:line
- Append-only — wiki entry создаётся, существующие entries не редактируются blindly (separate flow для updates)

**P.6 Reusable orchestrator integration:**
- Stage 5 в `tools/voice-pipeline-orchestrator.py` updated с new heuristic
- Each future voice pipeline run automatically runs new Stage 5
- Lens config может override match thresholds per run

**P.7 Quality criteria for Phase 2 self-evaluation:**
- New Stage 5 на 1285 existing candidates from voice-pipeline-2026-05-10 — match rate ≥30% (target)
- Auto-merge after bulk ack — verify zero items lost
- All merged candidates have voice_provenance field
- wiki/log.md updated correctly
- wiki/index.md updated correctly
- No silent updates к existing wiki entries

**P.8 Constitutional cross-check:**
- Tier 2 R1: pipeline = matching + proposing, не deciding wiki content
- Tier 2 R2: wiki/ writes pending Ruslan ack каждого batch
- Tier 2 R6: provenance per candidate (memo:line + transcript path)
- Append-only: existing wiki entries untouched (this redesign creates only new entries)
- Default-Deny: 3-gate (plan ack → execute redesign → bulk-ack candidates → write)

**P.9 Open questions for Ruslan:**
- §6.1 Match threshold tier boundaries (default 0.85 / 0.60)?
- §6.2 Auto-merge на Tier A — yes by default или сначала dry-run?
- §6.3 Re-process current 1285 candidates с new heuristic — yes/no?
- §6.4 Bulk-ack format — single command «approve all Tier A»?
- §6.5 Update workflow для existing wiki entries (entry already exists, voice item adds new info) — supplement or skip?
- §6.6 Wiki schema enforcement — strict (reject candidate если frontmatter incomplete) or lenient?
- §6.7 Future runs lens-driven match priority — высокий matching внутри lens scope (Tseren / Phase 1)?

### §1.3 Phase 1 deliverable & wait

After PLAN.md created and pushed на свою ветку:
- `git commit -m "[wiki-integration] Phase 1 plan — redesign Stage 5 + bulk-ack workflow awaiting Ruslan ack"`
- `git push origin HEAD`
- Signal Ruslan через cloud cowork bridge — ready for review
- **WAIT for Ruslan ack** — не начинай Phase 2 без explicit «ack — execute redesign»

---

## §2 PHASE 2 — Execute approved plan (after Ruslan ack)

### §2.1 Implementation

For each P.X в approved PLAN.md:
- Implement chosen match approach
- Implement propose-new template auto-fill
- Implement bulk ack workflow (CLI или CC command)
- Update orchestrator Stage 5
- Implement auto-merge mechanics

### §2.2 Test on existing 1285 candidates

Run new Stage 5 на existing `04-wiki-candidates.md` candidates:
- Re-process all 1285 items
- Output:
  - `04-wiki-candidates-v2.md` (new categorized list, 3-tier)
  - `match-rate-comparison.md` (old 0% vs new X%)

### §2.3 Bulk ack integration

CLI / CC command:
- `/wiki-bulk-ack --tier A` — approves all Tier A → triggers auto-merge
- `/wiki-bulk-ack --tier B --select <list>` — Ruslan selects subset
- `/wiki-bulk-ack --reject <list>` — defer to backlog
- `/wiki-bulk-status` — current review queue state

### §2.4 Self-evaluation

Run criteria from P.7. Write `discipline-log.md` с pass/fail per criterion.

### §2.5 Final push

```bash
git add tools/voice-pipeline-orchestrator.py reports/wiki-integration-redesign-2026-05-10/ tools/wiki-integration/ .claude/skills/wiki-bulk-ack/
git commit -m "[wiki-integration] Phase 2 execute — new Stage 5 heuristic + bulk-ack workflow + reusable orchestrator (Ruslan ack pending merge + bulk wiki ack)"
git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** **НЕ write в wiki/** автоматически — only после Ruslan bulk-ack.

---

## §3 What NOT to do

- ❌ НЕ удалять existing wiki/ entries
- ❌ НЕ редактировать existing wiki/ entries (только add new entries)
- ❌ НЕ auto-merge candidates без Ruslan bulk-ack
- ❌ НЕ перезаписывать `tools/transcribe.py` / `extract.py` / `filter.py` (existing scripts)
- ❌ НЕ менять lens config (Stage 6 unaffected)
- ❌ НЕ push to main, НЕ tag

---

## §4 Constitutional cross-check

| Rule | Application | Compliance |
|---|---|---|
| Tier 2 R1 | Heuristic = matching + proposing. Ruslan = sole decider что становится wiki entry. | ✅ |
| Tier 2 R2 | 3-gate: plan ack → redesign execute ack → bulk wiki ack. wiki/ writes only after explicit ack. | ✅ |
| Tier 2 R6 | Provenance per candidate (memo:line + transcript path). | ✅ |
| Append-only | New wiki entries создаются. Existing entries untouched в этом цикле. | ✅ |
| Default-Deny | wiki/ untouched до bulk-ack. Each tier separately ack'd. | ✅ |

---

## §5 Time / size budget

- Phase 1 plan: 30-45 min
- Wait for Ruslan ack: variable
- Phase 2 implementation + test: 1.5-3 hours autonomous
- (Future) Bulk wiki ack + auto-merge: 30-60 min Ruslan time на 1285 candidates batch-style

---

## §6 Final signal к Ruslan

After Phase 1 push:
- Branch + commit SHA
- PLAN.md path
- Open questions count
- Phase 2 estimated duration
- Diagnosis verdict (почему Stage 5 failed)

After Phase 2 push:
- Branch + commit SHA
- New Stage 5 quality (match rate %)
- Files inventory
- Bulk ack workflow ready (commands list)
- Ready для:
  - Merge to main (orchestrator + skills update)
  - Bulk wiki ack (Ruslan reviews + acks tiers → wiki/ writes)

Ruslan acks → push to main + optional tag `wiki-integration-v2-2026-05-10`.

---

**Brigadier signature.** Acting_as `wiki-integration-redesign-orchestration-role`. Ultrathink + Plan Mode required для Phase 1. Ruslan = sole decider — что в wiki, что в backlog.
