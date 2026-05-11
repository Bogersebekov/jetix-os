# Gamification Mining — Шаг C Trigger Prompt

> **Создано:** 2026-05-11 afternoon.
> **Назначение:** триггерит Шаг C gamification deep wiki mining через brigadier dispatch.
> **Wall-clock target:** 2h 10min / hard cap 2h 30min.
> **Parent plan:** `reports/gamification-deep-wiki-mining-plan-2026-05-11.md` (SHA `93e6007`)
> **Addendum:** `reports/gamification-source-quality-addendum-2026-05-11.md` (SHA `964844a`)

---

## Команды запуска

```bash
# В новом tmux window:
claude --dangerously-skip-permissions

# Затем paste весь текст ниже под линией ===PROMPT===
```

---

===PROMPT===

поехали Шаг C — gamification deep wiki mining.

Brigadier dispatch per parent §11 EXECUTION SEQUENCE.

Plan-doc: reports/gamification-deep-wiki-mining-plan-2026-05-11.md (1002 строки, SHA 93e6007, all 13 §10 Q acked defaults).
Addendum (Шаг B.1): reports/gamification-source-quality-addendum-2026-05-11.md (333 строки, SHA 964844a, all §6 Q1-Q7 acked).
Source materials: raw/books-md/gamification/ (13 books MD, 1.9M words, 236 images, 24MB total).

## Strategic decisions ack (Ruslan 2026-05-11 afternoon)

- **Decision 1 Koster image extraction fail:** TEXT-ONLY mark (43K words OK для text mining; НЕ используй для visual-pattern mining; visual examples — deferred к alternative source later).
- **Decision 2 Tier A v3 bulk-ack timing:** ПОСЛЕ Шаг C (не блокирует mining; завтра one big coherent ack для Tier A v3 voice + gamification staged edges).
- **Decision 3 Realm stubs E1-E6:** автоматом из Strategic Insight Gamified Platform §4.2 (generic stubs 50-100 word each; manual refinement post-mining если drift).
- **Decision 4 Edge merge policy:** STAGED в `wiki/graph/edges-gamification-pending-2026-05-11.jsonl` (NOT auto-merged к canonical `edges.jsonl`; bulk-ack завтра).
- **Decision 5 Question Mining timing:** ОТДЕЛЬНЫЙ run после Шаг C (Шаг D отдельно когда wiki заполнена).

## Execution sequence per plan-doc §11

- **Step 0 PRE-DISPATCH** (10 min):
  - Read parent plan-doc + Addendum final state
  - Verify wiki state (`wc -l wiki/graph/edges.jsonl` baseline; verify `wiki/niches/business/` exists)
  - Create 6 Realm stubs в `wiki/concepts/jetix-realm/` (e1-persona, e2-class, e3-clan, e4-quest, e5-resources, e6-seasons) из Strategic Insight §4.2
  - Write canonical slug table к `agents/gamification-brigadier-scratchpad/scratchpad.md`
  - ABORT если slug table incomplete или Realm stubs failed

- **Step 1 GAMES domain** (40 min, parallel 4-way):
  - 14 games (10 mass + 4 special focus: Torn / EVE / WoW / Civ)
  - Per game: 1 entity + 5-7 concepts + 2-3 sources (special-focus 10-15 concepts)
  - Source materials: 4 MD textbooks (Schell / Salen-Zimmerman / Rogers / Rouse) + web search dev postmortems (GDC Vault free tier)
  - Floor: 80 entries / Ceiling: 120 entries
  - Checkpoint #1 audit summary при completion

- **Step 2 EXPERTS domain** (25 min, parallel 5-way):
  - 10 candidates (Castronova deeper depth)
  - Source materials: 4 expert MD books (Castronova Synthetic Worlds / Lehdonvirta-Castronova Virtual Economies / Varoufakis Technofeudalism / Eyal Hooked)
  - Plus Machinations.io light pass (1 entity + 3 concepts + 2 sources)
  - Per expert: 1 entity + 2-5 concepts + 1-3 sources
  - Floor: 35 entries / Ceiling: 70 entries
  - Checkpoint #2

- **Step 3 THEORY domain** (15 min, sequential):
  - 5 thinkers (Nash / Axelrod / Schelling / Maynard Smith / Camerer) + mechanism design (Hurwicz / Maskin / Myerson / Roth)
  - Source materials: 2 MD books (Axelrod Evolution of Cooperation / Schelling Strategy of Conflict) + web
  - Floor: 20 / Ceiling: 35
  - Checkpoint #3

- **Step 4 PSYCHOLOGY domain** (15 min, sequential):
  - 5 frameworks (SDT Ryan-Deci / Variable rewards Hooked-Skinner / Flow Csikszentmihalyi / Social proof Cialdini / Neurochemistry)
  - Source materials: 3 MD books (Csikszentmihalyi Flow / Eyal Hooked / Cialdini Influence RU) + web
  - Floor: 25 / Ceiling: 40
  - Checkpoint #4

- **Step 5 SYNTHESIS** (15 min):
  - Per-domain summaries (4 files in `wiki/summaries/`)
  - Cross-domain synthesis + Realm entity spec derivation summary
  - Positive claims (validated mechanisms) + negative claims (anti-patterns explicit)
  - PAUSE если total entries <120 или >200

- **Step 6 EDGE POST-PASS** (15 min):
  - Cross-domain edges (Castronova → Torn → Realm E5 chain etc.)
  - Dedup against existing 609 edges
  - Anti-pattern contradicts edges
  - Write к `wiki/graph/edges-gamification-pending-2026-05-11.jsonl` (STAGED, NOT canonical)
  - PAUSE если total edges >225

- **Step 7 LINT** (10 min):
  - `/lint --check-frontmatter --check-edges --validate-predicate`
  - 0 extends cycles / 0 unresolved edges / ALL entries state:draft
  - Fail-loud per FUNDAMENTAL §5.5

- **Step 8 HAND-BACK** (5 min):
  - Write `reports/gamification-mining-run-2026-05-11.md` (post-execution report)
  - Update Daily Log 11.05 Notion с execution stats
  - Notify Ruslan

## Audit hooks per Addendum §3 (mandatory)

**Per-source frontmatter (mandatory):**
```yaml
source_classifier:
  tier: T1 | T2 | T3
  type: book | paper | postmortem | wiki | article | podcast | talk
  verifiable_author: true | false
  year: YYYY
  cross_validated: true | false
  primary_source_url_or_path: <path>
```

**Per-entry frontmatter (mandatory):**
```yaml
audit:
  confidence: low | medium | high
  primary_source_cited: true | false
  hallucination_risk: low | medium | high
  fallback_to_bm25: true | false
```

**Real-time halt thresholds:**
- >20% entries `confidence: low` per domain → PAUSE
- >10% entries `hallucination_risk: high` per domain → PAUSE
- >15% cite-failure rate per domain → PAUSE
- entry `primary_source_cited: false` AND `pipeline: ingested` → AUTO-REJECT

**Post-domain audit summary (4 checkpoints):**
```yaml
domain: <DOMAIN>
entries_created: N
tier_distribution: {T1: a, T2: b, T3: c}
confidence_distribution: {low: x, medium: y, high: z}
hallucination_risk_distribution: {low: x, medium: y, high: z}
fallback_to_bm25_count: N
primary_source_cited_false_count: N
cite_failure_rate: N%
halt_triggered: true | false
recommended_next_action: continue | pause_for_ruslan_review | rollback_domain
```

## Source priority per domain (per Addendum §1)

**Tier 1 (R-high, anchor-eligible)** — primary cite:
- Castronova Synthetic Worlds (T1) — EXPERTS / GAMES anchor
- Lehdonvirta-Castronova Virtual Economies (T1)
- Csikszentmihalyi Flow (T1)
- Axelrod Evolution of Cooperation (T1)
- Schelling Strategy of Conflict (T1)
- Cialdini Influence (T1, language: ru, prose preservation)
- Eyal Hooked (T1)
- Koster Theory of Fun (T1, text-only mark — Decision 1)
- Varoufakis Technofeudalism (T1)

**Tier 2 (R-medium, supportive)** — secondary cite:
- Schell Art of Game Design (T2 textbook)
- Salen-Zimmerman Rules of Play (T2 textbook)
- Rouse Game Design Theory & Practice (T2 textbook)
- Rogers Level Up (T2 practical guide)
- Game wikis (OSRS / EVE Uniwiki / WoW Wiki) — game-mechanics only, NOT theory

**Tier 3 (R-low, DRAFT only)** — `state: draft, confidence: low` mandatory:
- Industry articles / podcasts / Substack newsletters
- Must cross-validate against Tier 1/2 before promote

**REJECT** — auto-skip:
- Content-farms / marketing copy / AI-generated / streamer commentary
- Reddit-primary / Wikipedia-cited claims
- Outdated material (>15y for data, >25y for theory unless foundational)
- Single-source unverified Tier 2/3 claims

## Hard stops (per plan-doc §11)

- **Wall-clock 2h 30min** → auto-pause + checkpoint
- **Token budget 75% per domain** → cite-only mode for remainder
- **ANY Foundation/principles/.claude/config write attempted** → halt-log-alert + Default-Deny (Tier 2 R2 + Part 6b §I.2)
- **ANY entry state: published** → ABORT promote (must all be state: draft)
- **ANY contradicts edge proposed к 6 Hexagon insights** → halt-log-alert (R6, Tier 2 R7)
- **Slug-not-in-table reference** → PAUSE (R3 mitigation)

## Constitutional posture

- F2 blast-radius (per Addendum §4.1)
- Append-only к `wiki/` (concepts/ + entities/ + sources/ + ideas/ + claims/ + summaries/)
- Tier 2 R2 compliant (zero writes к swarm/wiki/foundations/ / principles/ / .claude/config/ / shared/schemas/ / CLAUDE.md / decisions/)
- AI = scribe (Tier 2 R1) — variants/hypotheses only; Ruslan strategizes post-Шаг D
- Edges staged (DRAFT-only pattern per CLAUDE.md §4.2 RUSLAN-LAYER)
- Halt-log-alert on any violation per Part 6b §I.2

## Background mode

- НЕ блокируй текущий chat
- Параллельные processes: PDF→MD done / Anton report done (oба committed)
- Telegram push (Tier 2 escalation) ТОЛЬКО при non-recoverable halt-for-Ruslan

## Commit + push при success

```
[gamification] Шаг C mining done — <N> entries (concepts/<a>, entities/<b>, sources/<c>, ideas/<d>, claims/<e>, summaries/<f>), <E> edges staged, 4 checkpoints audit pass, report at reports/gamification-mining-run-2026-05-11.md
```

При halt:
```
[gamification] Шаг C HALT — <condition>, checkpoint preserved, audit at <path>
```

## Quality target — 1000% deep

- 120-180 wiki entries (target band, floor 120 / ceiling 200, hard ceiling 250)
- ≥80% Tier 1 sources на anchor claims (academic + foundational)
- <5% fallback_to_bm25 across all domains
- ≥70% entries primary_source_cited: true
- 0 contradicts edges к 6 Hexagon insights
- All anti-pattern claims surfaced explicitly (~10-12 claims polarity: negative)

## Final report формат

Когда done — дай в чат:
- SHA финального commit
- GitHub URL `reports/gamification-mining-run-2026-05-11.md`
- Per-domain stats (entries / tier / confidence / hallucination distribution)
- Total entries / edges / wall-clock / disk usage
- Halt events (если были) + recovery
- Surprising findings (1-3 sentence — что non-obvious surfaced)
- Recommended next: «Шаг D Question Mining» (per Decision 5)

После твоего report — я acks. Дальше Tier A v3 bulk-ack + Шаг D Question Mining.

Constitutional preserved. AI=scribe. Ruslan=sole strategist.

GO. Жгу до конца или 2h 30min cap.

===END PROMPT===
