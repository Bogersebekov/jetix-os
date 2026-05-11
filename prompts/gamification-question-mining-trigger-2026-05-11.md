# Gamification Question Mining — Шаг D Trigger Prompt

> **Создано:** 2026-05-11 evening.
> **Назначение:** триггерит Шаг D Question Mining — 4 categories × 44 параметров × 220+ deep questions с 3-7 variants per question.
> **Wall-clock target:** 2h / hard cap 3h.
> **Parent template:** `reports/gamification-question-mining-template-2026-05-11.md` (SHA `5502584`)
> **Parent plan:** `reports/gamification-deep-wiki-mining-plan-2026-05-11.md`
> **Parent analysis:** `reports/gamification-mining-analysis-2026-05-11.md`

---

## Команды запуска

```bash
# В новом tmux window:
claude --dangerously-skip-permissions

# Затем paste весь текст ниже под линией ===PROMPT===
```

---

===PROMPT===

поехали Шаг D — Gamification Question Mining.

Прочитай ПОЛНОСТЬЮ перед началом:
- `reports/gamification-question-mining-template-2026-05-11.md` (468 строк, 4 categories × 44 parameters × 220+ questions)
- `reports/gamification-mining-analysis-2026-05-11.md` (Шаг C results context)
- `reports/gamification-mining-run-2026-05-11.md` (technical run report)
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` (Strategic anchor)

## Strategic decisions ack (Ruslan 2026-05-11 evening)

- **Decision 6 Priority order:** Категория **4 (Core ядро) → 3 (Workflow) → 2 (Clan) → 1 (Платформа)**. Process в этом order — important questions get budget first, если halt mid-run важные done.
- **Decision 7 Total questions:** 220+ comprehensive (default A) — деeply на 1000%.
- **Decision 8 Parameter granularity:** 44 parameters (12+12+10+10, default A).
- **Decision 9 Output format:** 3-7 variants per question (default A).
- **Decision 10 Wiki refs per variant:** ≥2 wiki refs mandatory (default A) — Tier 2 R6 provenance.

## Wiki state на entry (post Шаг C)

```
Total entries: 722 (was 552 + 170 new)
- concepts: 108 (incl. 6 Realm stubs E1-E6)
- entities: 39 (14 games + 15 people + 1 tool + others)
- sources: 292
- ideas: 262
- claims: 14 (incl. 9 anti-patterns)
- summaries: 6 (4 domain summaries + 2 synthesis)
Total edges canonical: 609 (UNCHANGED — Tier A v3 + gamification staged NOT yet bulk-ack'd)
Staged edges pending: 133 in wiki/graph/edges-gamification-pending-2026-05-11.jsonl
```

## Execution Sequence

### Step 0 — PRE-DISPATCH (10 min)

1. Read all 4 source documents (template + analysis + run report + Strategic Insight)
2. Build canonical questions list — 220+ from template §§1-4 (extract every Q.X.Y.Z)
3. Build wiki index map — slug → file path for all 722 entries (для fast cite lookups)
4. Initialize scratchpad: `agents/gamification-question-mining-scratchpad/scratchpad.md`
5. Write priority queue: Category 4 questions first (50), then 3 (50), then 2 (60), then 1 (60)

### Step 1 — CATEGORY 4: Core ядро / архитектура (~40 min, 10 params × 5 questions = 50 Q)

Process per parameter (4.1 → 4.2 → ... → 4.10):
- 4.1 6 entities refinement (5 Q)
- 4.2 Layer architecture Linux pattern (5 Q)
- 4.3 Data model (5 Q)
- 4.4 Engineering principles (5 Q)
- 4.5 Extensibility / community contribution (5 Q)
- 4.6 Versioning / migration (5 Q)
- 4.7 Open source policy (5 Q)
- 4.8 Scale targets (5 Q)
- 4.9 Foundation grounding (existing canonical) (5 Q)
- 4.10 Anti-pattern enforcement (5 Q)

Per question: generate 3-7 variants, cite ≥2 wiki entries each, surface pros/cons/F-G-R.

**Checkpoint #1** end-of-category: variants/Q ratio audit + Tier distribution + halt check.

### Step 2 — CATEGORY 3: Workflow gamification (~40 min, 10 params × 5 questions = 50 Q)

Process per parameter (3.1 → 3.10):
- 3.1 Quest = real business task mapping
- 3.2 Difficulty curves / progression
- 3.3 Reward structures
- 3.4 Skill trees / Class specialization
- 3.5 Time tracking integration (Toggl + game)
- 3.6 Learning gamification (Tyson mentorship)
- 3.7 TRM 6 resources as game stats
- 3.8 Status / public visibility
- 3.9 Critique / feedback loops
- 3.10 AI agent integration

**Checkpoint #2** end-of-category.

### Step 3 — CATEGORY 2: Клан / Community (~45 min, 12 params × 5 questions = 60 Q)

Process per parameter (2.1 → 2.12):
- 2.1 Clan size dynamics
- 2.2 Recruitment механика
- 2.3 Exit механика
- 2.4 Internal hierarchy / Roles
- 2.5 Communication tools
- 2.6 Activity rhythm
- 2.7 Conflicts resolution
- 2.8 Reputation / Accountability
- 2.9 Cross-Clan interaction
- 2.10 Identity / Branding
- 2.11 Economic mechanism
- 2.12 Retention > 6 months

**Checkpoint #3** end-of-category.

### Step 4 — CATEGORY 1: Платформа в целом (~45 min, 12 params × 5 questions = 60 Q)

Process per parameter (1.1 → 1.12):
- 1.1 First impression / Hook
- 1.2 Onboarding flow
- 1.3 Identity / Persona system
- 1.4 Visual / Aesthetic language
- 1.5 Mobile vs desktop
- 1.6 Notifications / Attention strategy
- 1.7 Privacy / Data ownership
- 1.8 Performance / latency / scale
- 1.9 Internationalization / Language
- 1.10 Anti-extraction principle
- 1.11 Mechanic vs Theme separation
- 1.12 Skill ceiling / accessibility

**Checkpoint #4** end-of-category.

### Step 5 — CROSS-CATEGORY SYNTHESIS (~15 min)

После всех 4 categories done:
- Cross-cutting patterns identified
- Variants conflicts (если variant 4.X.Y contradicts variant 2.X.Y → surface)
- Top 10 «most diverged» questions (where 3-7 variants spread widely — signal для Ruslan)
- Top 10 «most converged» questions (variants point one direction — confident recommendations)

### Step 6 — RUN REPORT (~10 min)

Write `reports/gamification-question-mining-run-2026-05-11.md`:
- TL;DR (20 строк): total Q processed, variants generated, time per category, halt events
- Per-category audit summaries (4 checkpoints)
- Top 10 diverged / converged questions
- Surprising findings (3-5 sentences, non-obvious surfaced)
- Quality targets achievement (mirror Шаг C 9-target format)
- Awaits Ruslan strategize phase (ФАЗА 4)

### Step 7 — HAND-BACK (~5 min)

- Commit + push
- Surface to Ruslan: «Шаг D Question Mining done — N questions / V variants / T per-category time. Run report at <path>. Awaits ack для ФАЗА 4 (Ruslan-words spec).»

## Per-question Output Format

For each of 220+ questions, write to `reports/gamification-question-mining-run-2026-05-11.md`:

```markdown
### Q<X.Y.Z>: <question text>

**Category:** <1|2|3|4>
**Parameter:** <X.Y>
**Variants generated:** <3-7>

#### Variant 1: <short title>
- **Hypothesis:** <1-2 sentences>
- **Evidence from wiki:**
  - [<entry-slug-1>](wiki/concepts/<slug>.md) — relevance: <why>
  - [<entry-slug-2>](wiki/entities/<slug>.md) — relevance: <why>
- **Precedent games:** [<game-1>, <game-2>]
- **Pros:** [pro-1, pro-2, pro-3]
- **Cons:** [con-1, con-2]
- **F-G-R:** F2 / hypothesis-applied-now / R-medium
- **Anti-pattern risk:** <none|some|high — explanation>

#### Variant 2: ...
... (3-7 variants per Q)

**Recommended next:** Ruslan strategize — choose / refine / synthesize variants.
```

## Audit Hooks (mirror Addendum §3)

Per variant frontmatter (embedded in generated markdown):
- `confidence: low | medium | high`
- `primary_wiki_cite: <slug>` (the strongest reference)
- `hallucination_risk: low | medium | high`
- `cross_validated: true | false`

Per-category checkpoint summary:
```yaml
category: 4 | 3 | 2 | 1
parameters_processed: N
questions_processed: N
variants_generated_total: N
variants_per_question_distribution: {3: x, 4: y, 5: z, 6: w, 7: v}
confidence_distribution: {low: x, medium: y, high: z}
hallucination_risk_distribution: {low: x, medium: y, high: z}
cross_validated_rate: N%
wiki_refs_avg_per_variant: N
halt_triggered: true | false
recommended_next_action: continue | pause | abort
```

## Real-time halt conditions

| Condition | Threshold | Action |
|---|---|---|
| Wall-clock | > 3h | auto-pause + checkpoint |
| Question with only 1 variant | > 20% of questions per category | PAUSE — depth insufficient |
| Hallucination_risk: high | > 10% variants per category | PAUSE — quality drop |
| Wiki refs missing | variant without ≥2 refs | REJECT variant (regenerate or skip) |
| ANY contradicts edge proposed к 6 Hexagon | per event | halt-log-alert (Tier 2 R7) |
| ANY write attempt outside reports/ | per event | halt-log-alert + Default-Deny (Tier 2 R2) |

## Hard constraints

- **Constitutional posture:** F2 blast-radius, append-only к `reports/`, ZERO writes к `swarm/wiki/foundations/` / `principles/` / `.claude/config/` / `shared/schemas/` / `CLAUDE.md` / `decisions/` / `wiki/` (Шаг D НЕ создаёт новые wiki entries, только использует existing 722).
- **AI = scribe (Tier 2 R1):** variants/hypotheses only; NO strategic prose; Ruslan strategizes ФАЗА 4.
- **Tier 2 R6 provenance:** every variant cites ≥2 wiki entries (mandatory).
- **Tier 2 R7:** 0 contradicts к 6 Hexagon insights.
- **Idempotent:** rerun safe (skip if run report exists unless --force).
- **Background mode:** не блокируй chat. Параллельные processes: PDF→MD done, Anton report done, Шаг C done.

## Quality target — 1000% deep

- 220+ questions processed (target — full template)
- Average variants per question: ≥4 (target band 4-6)
- ≥80% variants with `confidence: medium` или `high`
- ≤5% variants with `hallucination_risk: high`
- ≥70% variants `cross_validated: true`
- Wiki refs avg per variant: ≥2 (mandatory floor)
- 0 contradicts edges к Hexagon insights
- 0 writes outside `reports/`

## Wall-clock budget

- **Target:** 2h total (~30s per question × 220 Q)
- **Soft cap:** 2h 30min — switch к cite-only mode для remaining
- **Hard cap:** 3h — auto-pause + partial report
- **Expected actual:** ~1-1.5h based on Шаг C 4× speed precedent (29min vs 2h target)

## Commit + push на success

```
[gamification] Шаг D Question Mining done — <N> questions / <V> variants / category 4-3-2-1 priority order / report at reports/gamification-question-mining-run-2026-05-11.md
```

На halt:
```
[gamification] Шаг D HALT — <condition>, checkpoint at <path>, partial report preserved
```

## Final report формат

When done — surface to Ruslan:
- SHA финального commit
- GitHub URL `reports/gamification-question-mining-run-2026-05-11.md`
- Per-category stats (Q count / variants / time / quality)
- Top 10 diverged questions (need Ruslan strategize)
- Top 10 converged questions (clear recommendations)
- 3-5 surprising findings (non-obvious patterns surfaced)
- Total wall-clock + comparison к budget
- Recommended next: «ФАЗА 4 — Ruslan-words spec» per overall plan

After report — Ruslan reviews, ФАЗА 4 (Ruslan strategize → write FINAL spec).

Constitutional preserved. AI = scribe. Ruslan = sole strategist.

GO. Жгу до конца или 3h hard cap. Priority order: 4 → 3 → 2 → 1.

===END PROMPT===
