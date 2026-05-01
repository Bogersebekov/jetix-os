---
type: backlog-not-found-flag
date: 2026-05-01
batch: audio_540-586 (period 26-30.04)
status: flag-only (Hard rule 8 brief: НЕ создавать новый файл)
---

# Backlog Update — FLAG: file не найден

> **Hard rule 8 brief:** «если backlog file не найден — flag explicitly, не создавай новый (Ruslan скажет где)».

---

## Brief candidates искал — все NOT FOUND

| Brief candidate pattern | Search result | Status |
|------------------------|---------------|--------|
| `swarm/wiki/topics/backlog-*.md` | `swarm/wiki/topics/` directory не существует | NOT FOUND |
| `swarm/wiki/topics/open-questions-*.md` | same — directory не существует | NOT FOUND |
| `swarm/wiki/topics/pending-tasks-*.md` | same — directory не существует | NOT FOUND |
| `decisions/operational/stoppers-*.md` | `decisions/operational/` directory не существует | NOT FOUND |
| Notion Daily Log open questions sections | Not searched (out-of-band) | UNKNOWN — Ruslan ack required |

**Search command record (audit trail):**

```bash
find . -type f \( -name "backlog*.md" -o -name "open-questions*.md" -o -name "pending-tasks*.md" \
    -o -name "stoppers*.md" -o -name "open_questions*.md" \) -print
```

**Files found (NOT brief-pattern matches):**

| File | Why это не tracked-backlog | Status |
|------|---------------------------|--------|
| `hypotheses/backlog.md` | Hypothesis-tracking, статус "Пусто на 2026-04-18". Не задачи/вопросы. | scope mismatch |
| `swarm/wiki/operations/quick-money/open-questions.md` | Project-scoped (per project-bootstrap KM MVP), не cross-project backlog | scope mismatch |
| `swarm/wiki/operations/levenchuk-deep-dive/open-questions.md` | Project-scoped | scope mismatch |
| `swarm/wiki/_templates/project-{bets,research,consulting,product}/open-questions.md` | Templates only, не active records | template only |
| `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/open-questions.md` | Task-scoped (specific cycle), не general backlog | scope mismatch |
| `swarm/wiki/tasks/T-km-architecture-research-2026-04-24/open-questions.md` | Task-scoped | scope mismatch |
| `swarm/wiki/drafts/T-*-philosophy-critic-*-open-questions.md` | Domain-expert critique drafts (per Roy-alignment), не canonical backlog | scope mismatch |

**Conclusion:** **No file matches brief patterns** (`swarm/wiki/topics/backlog-*` / `swarm/wiki/topics/open-questions-*` / `swarm/wiki/topics/pending-tasks-*` / `decisions/operational/stoppers-*`).

**`swarm/wiki/topics/` does not exist.** `decisions/operational/` does not exist.

---

## Items to be merged ONCE backlog file location confirmed

> Hard rule 7 brief: НЕ creating new backlog file. Storing items here для будущей миграции after Ruslan указует.

### From Phase B-1 voice-extract §4.5

| Item | Type | Source | Priority |
|------|------|--------|----------|
| Tseren outreach 30.04 — followup status | task | audio_582@30-04-2026_18-12-09.txt:L6 | P1 |
| Foundation closure → Phase 2 product launch | task | audio_562@27-04-2026_08-49-24.txt:L6 + CLAUDE.md Foundation v1.0 LOCKED | P1 |
| Withdraw V-Work / ilon-mask / dima-draft CRM auto-drafts | task | pipeline log Шаг 2b | P2 |
| Mishu Takhovinin / Oscar Hartman identity verify | open-question | audio_558@26-04-2026_12-30-58.txt:L6 | P2 |
| Antoine CRM record decision | open-question | reports/review_2026-04-26-DEEP.md:L1055 | P2 |
| Token-economy Phase 3 design study | open-question | raw/voice-memos-text/holding-vision-2026-04-21.md:L62 | P3 |
| AI-Psy-Led design Strategic Insight promote | task | reports/review_2026-04-26-DEEP.md D-DRAFT-30 §5 | P2 |
| Korp-Startup positioning D29 vs Strategic Insight | open-question | reports/review_2026-04-26-DEEP.md D-DRAFT-29 §5 | P1 |
| Public-company-from-Day-1 D-DRAFT review | open-question | audio_556@26-04-2026_11-26-32.txt:L6 + audio_559@26-04-2026_13-34-23.txt:L6 | P3 |
| Lazy-vs-strong paradox brand frame | task | audio_546@26-04-2026_07-09-48.txt:L6 | P3 |
| WeWork sub-lease case study research (TRM platform analogue) | task | audio_575@28-04-2026_21-56-57.txt:L6 | P3 |
| Workshop view = cognitive offload mechanism documented | task | audio_565@27-04-2026_14-41-06.txt:L6 | P2 |

### From Phase B-2 structured report (Q1-Q12 + T1-T12)

> See `reports/review_2026-05-01-STRUCTURED.md` "Вопросы" + "Задачи" sections — все source-tagged. 12 questions + 12 tasks. Не дублирую здесь — single-source.

### Carry-forward open from 04-26 (still unanswered)

> See `reports/review_2026-04-26-DEEP.md` §12 Q1-Q10 + §3 Group A items — still pending Ruslan ack.

---

## Closure / resolved items (если в новых заметках есть closure)

| Item | Original source | Closure source | Status |
|------|-----------------|----------------|--------|
| Workshop concept articulation (was open since «Jetix как мастерская» riffs) | review_2026-04-26-DEEP.md derived | audio_582-586 30.04 + LOCKED canonical | RESOLVED — Workshop v2 LOCKED 30.04 |
| Founder isolation stopper (was P1 stopper 04-26) | review_2026-04-26-DEEP.md §2 Theme 1 | audio_582 30.04 (Tseren outreach planned) | PARTIALLY-RESOLVED — concrete first move planned |
| V-Work clarification (open Q3 in 04-26 §12) | review_2026-04-26-DEEP.md §12 Q3 | audio_575 28.04 confirms WeWork business model | RESOLVED — WeWork = WeWork; sub-lease arbitrage confirmed |

---

## Action для Ruslan

1. **Указать local backlog file path** (или confirm Notion) — куда mapping items above.
2. После ack — Cloud Cowork делает one-shot merge всех items + closure marks (separate sprint, не этот).
3. Или Ruslan может create canonical backlog file и tell location (suggest: `swarm/wiki/themes/_backlog.md` или `decisions/operational/_backlog.md`).

---

**END Backlog Flag.**

> **Note:** `wiki/log.md` entry NOT appended per Hard rule 7 (брифа: НЕ promote / NOT modify wiki without ack). Append будет done после Ruslan указует backlog file location.
