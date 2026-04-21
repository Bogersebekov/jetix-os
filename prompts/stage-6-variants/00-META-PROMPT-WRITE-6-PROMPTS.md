---
id: stage-6-meta-prompt-write-6-prompts
title: Stage 6 META — Write 6 Deep Architect-Variant Prompts
date: 2026-04-21
type: meta-prompt
status: ready
priority: P1
depends_on: D1 + D2 + D3 + D4 all APPROVED
outputs:
  - prompts/stage-6-variants/00-README.md
  - prompts/stage-6-variants/01-conservative.md
  - prompts/stage-6-variants/02-aggressive-maximalist.md
  - prompts/stage-6-variants/03-aggressive-deep-tech.md
  - prompts/stage-6-variants/04-hybrid.md
  - prompts/stage-6-variants/05-emergent.md
  - prompts/stage-6-variants/06-wildcard.md
  - LAUNCHERS-STAGE-6.md (6 copy-paste launcher blocks для Ruslan)
---

# Stage 6 META — Write 6 Deep Architect-Variant Prompts

## Твоя миссия

Написать **6 глубоких promts** для Stage 6 architecture-variant generation. Каждый prompt = полная спецификация для одного из 6 Claude Code architect-agents которые будут генерировать **свой вариант** архитектуры Jetix, отвечая на 15 architect questions из D4 §10.

Плюс написать **master index** (`00-README.md`) объясняющий parallelization + shared inputs + output format.

Плюс написать **LAUNCHERS-STAGE-6.md** — 6 copy-paste ready launcher blocks для Ruslan для 6 отдельных CC sessions.

**Всё должно быть academic-grade (как Stage 4 D4).** Ruslan directive: *"самый глубокий вариант… на максималку"*.

---

## Обязательные inputs (что ты сам должен прочитать перед писанием)

1. **`decisions/JETIX-VISION.md`** (D1 APPROVED)
2. **`decisions/JETIX-PHILOSOPHY.md`** (D2 APPROVED)
3. **`decisions/JETIX-PLAN.md`** (D3 APPROVED)
4. **`decisions/JETIX-ARCHITECTURE-BRIEF.md`** (D4 APPROVED) — **SUPER КРИТИЧНО. 15 questions здесь.**
5. **`decisions/STAGE-3-APPROVAL.md` + `decisions/STAGE-4-APPROVAL.md`**
6. **`raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md`** (8 locks)
7. **`raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md`** (10 locks)
8. **`raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md`** (6 locks)
9. **`raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md`**
10. **`design/JETIX-FPF.md`** (D6)
11. **`decisions/2026-04-19-architecture-v2-approval.md`** (ADR Chunks 1-8)
12. **`CLAUDE.md`**

---

## 6 Variants — character specifications

Каждый variant имеет **distinct lens** — разный способ смотреть на same brief.

### Variant 1: Conservative

**Character:**
- Minimum deviation от current state (CLAUDE.md + D6 FPF + OME reference)
- Incremental evolution over revolution
- Proven patterns preferred
- Risk-averse architectural choices
- Uses existing 11-12 agent roster as anchor

**Philosophical lens:** "evolve what works, don't rewrite what isn't broken"

**Expected character of output:**
- Familiar structure
- Low complexity additions
- Clear migration path from current
- Fewer architectural experiments

**Score tendency (per D4 §8 axes):** high on locks-compliance / operational-simplicity; low on innovation / scale-trajectory.

---

### Variant 2: Aggressive Maximalist

**Character:**
- Maximum agent count + skills + tools upfront
- Full-throttle complexity
- All 15 questions answered с maximum capability
- Heavy investment в infrastructure Phase 1 (trust future ROI)
- Multi-provider everything from Day 1
- Every Phase 2+ capability stubbed/scaffolded Phase 1

**Philosophical lens:** "build for Phase 3 from Day 1 — pay technical debt upfront, not later"

**Expected character of output:**
- Complex agent roster (possibly 15-20 agents)
- Rich protocol layer
- Heavy tooling / observability
- Aggressive early productization

**Score tendency:** high on scale-trajectory / innovation; low on operational-simplicity / cost Phase 1.

---

### Variant 3: Aggressive Deep-Tech

**Character:**
- Heavy FPF integration — ontology-first architecture
- Advanced protocols (USB-C protocol layer prioritized Phase 1 scaffold)
- Multi-level mereology (FPF A.14)
- Formal contracts with type systems
- Research-grade rigor
- Leverages Левенчук систем-thinking deeply
- Every agent has formal FPF contract

**Philosophical lens:** "correctness through formalism — FPF is the substrate, Jetix is the instance"

**Expected character of output:**
- Deep type systems / contract formalisms
- Ontology-first structure
- Research-grade protocols
- Academic-level precision в specs

**Score tendency:** high on Foundation-depth / universality / innovation; low on operational-simplicity / Phase 1 readiness (depth slows shipping).

---

### Variant 4: Hybrid

**Character:**
- Explicitly synthesizes best-of-breed от других variants
- Pragmatic trade-offs
- Phase-progression-driven (Phase 1 simple, Phase 2+ richer, Phase 3+ maximalist)
- Decisions staged to revenue gates (aligns с D15)
- Borrows OME structure where resonant, adds Jetix-specifics

**Philosophical lens:** "right depth at right phase — simplicity Phase 1, richness Phase 2+"

**Expected character of output:**
- Phase-keyed complexity evolution
- Explicit staging of architectural decisions
- Balanced trade-offs
- Clear "what activates when"

**Score tendency:** balanced across all axes; may lack distinctive strength any single axis.

---

### Variant 5: Emergent

**Character:**
- Sparse skeleton Phase 1
- Infrastructure for self-organization
- Organizational structure не designed top-down, а emerges from agent interactions
- Minimal governance, strong protocols
- Trust system evolution over planning
- Lightweight — "build the trellis, let the plant grow"

**Philosophical lens:** "design the space of possibilities, not the outcome itself"

**Expected character of output:**
- Thin governance layer
- Rich protocols but few prescribed structures
- Self-describing agents / self-organizing task routing
- Minimal hardcoded hierarchy

**Score tendency:** high on operational-simplicity / cost / Foundation (if protocols done well); risk on scale-trajectory (emergence может не масштабироваться predictably).

---

### Variant 6: Wildcard

**Character:**
- Radical reframe — challenge assumptions в D4 brief
- Question "hub-and-spoke" / "11-agent roster" / "consulting-first Phase 1" orthodoxies
- Propose unconventional patterns: e.g., no distinct agents (just skills + workflows), or swarm-of-specialists (no manager), or pure-protocol (no agents at all, just contracts + LLM calls)
- Still respects 24 locks, but approaches them sideways
- **If variant disagrees with brief directive — MUST flag explicitly в "Variant Contrarian Claims" section**

**Philosophical lens:** "orthodox answers produce orthodox results — challenge the question"

**Expected character of output:**
- Surprising architectural choices
- Explicit contrarian flags
- Novel patterns not seen в other variants
- May not фit into D4 scoring axes cleanly

**Score tendency:** high on innovation; unpredictable on other axes; highest variance.

---

## Каждый prompt file structure (~400-500 lines each)

Каждый из 6 prompt files должен содержать:

### Section 1: Variant Identity (20-30 lines)
- YAML frontmatter (id, title, variant-number, character tags)
- Variant character description (pull из specification выше)
- Philosophical lens
- Expected output character

### Section 2: Mission (30-50 lines)
- Что architect делает: читает brief + proposes variant
- Boundary: он НЕ implementation plan writer, он architectural-choice maker
- Output: `decisions/variants/JETIX-ARCH-V{N}-{NAME}.md`
- Size target: 40-60 pages equivalent / 8000-12000 words
- Multi-pass approach (3 passes: skeleton / flesh / coherence-critic)

### Section 3: Binding Inputs (40-50 lines)
- Full list of mandatory reading
- 24 locks binding precedence
- D4 §10 — 15 questions МUST answer каждый

### Section 4: Variant Output Document Structure (100-150 lines)

Каждый variant output должен содержать (**same structure для всех 6 для comparability**):

1. **Executive Summary** (1 page) — variant character + key differences от других potential approaches + selection case (почему Ruslan выбрать именно этот)
2. **Variant Character Statement** (1 page) — philosophical lens + core bets + trade-off stance
3. **Answer to Q1: Repository layout** (3-5 pages) — detailed design с diagrams (ASCII art in markdown)
4. **Answer to Q2: Agent roster** (3-5 pages) — 11/12/N agents, rationale, contracts per agent
5. **Answer to Q3: Integration points** (2-3 pages) — Stripe/Wise/Claude/fallback specification
6. **Answer to Q4: Scaling mechanism** (3-5 pages) — $0 → $1T path architectural choices
7. **Answer to Q5: Data architecture** (3-4 pages) — wiki + atoms + F-G-R tagging
8. **Answer to Q6: Privacy/security membrane** (2-3 pages) — tier design
9. **Answer to Q7: API architecture** (2-3 pages) — multi-provider + failover
10. **Answer to Q8: Token economy Option B** (2-3 pages) — Phase 2 internal / Phase 3 limited public
11. **Answer to Q9: Matchmaker algorithm** (3-4 pages) — task↔specialist matching logic
12. **Answer to Q10: Roy-replication packaging** (2-3 pages) — methodology-as-system export
13. **Answer to Q11: Content pipeline** (2-3 pages) — 3-tier orchestration
14. **Answer to Q12: Dashboard implementation** (2-3 pages) — v1/v2/v3 phase-keyed
15. **Answer to Q13: Escalation routing** (2-3 pages) — 6 non-delegatable + 4-class FPF
16. **Answer to Q14: Onboarding architecture** (2-3 pages) — 2nd pilot ≤7 days
17. **Answer to Q15: USB-C protocol layer** (3-5 pages) — protocol taxonomy + verification
18. **Foundation Layer Specification** (5-7 pages) — variant's specific Foundation design per D4 §4
19. **Hard Constraints Compliance Matrix** (1-2 pages) — все 24 locks × how variant respects each
20. **Anti-Patterns Avoidance Statement** (1-2 pages) — каждый из 16 anti-patterns × confirm avoidance
21. **Self-Scoring on D4 §8 Quality Axes** (1-2 pages) — variant scores себя по 10 axes (honest)
22. **Variant Contrarian Claims** (0.5-2 pages) — места где variant challenges brief directive (only for Variant 6 substantive; others brief comment)
23. **Risk Profile** (1-2 pages) — top 5 failure modes + mitigation
24. **Selection Case for Ruslan** (1 page) — "why pick me" pitch

### Section 5: Multi-Pass Approach (30-50 lines)
- Pass 1 skeleton (90-120 min)
- Pass 2 flesh (180-240 min)
- Pass 3 coherence-critic (60-90 min) — self-critique section
- Use subagents for parallelism (specify how)

### Section 6: Commit + Push (20 lines)
- Standard git flow
- Branch `claude/jolly-margulis-915d34`
- Commit message template

### Section 7: Notion Update (10 lines)
- Append to https://www.notion.so/3492496333bf812e8b62cbc61338ce06

### Section 8: Deliverable stdout summary (30 lines)
- Format consistent across variants

### Section 9: Anti-Patterns (for the WRITER) (20-30 lines)
- Don't skip coherence-critic pass
- Don't invent locks
- Don't skip D4 question
- Preserve voice where quotes used
- Don't copy other variants (this is YOUR variant)

### Section 10: ETA (10 lines)
- 5-7 hours total with subagents
- Parallel subagents per question group during Pass 2

---

## Master index `00-README.md` content

Должен включать:

1. **Stage 6 context** — что это, для чего
2. **6 variants overview** table (variant / character / philosophical lens)
3. **Shared inputs** (same для всех 6)
4. **How parallelization works** (6 CC sessions, different tmux windows)
5. **Output directory structure** — `decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md` и т.д.
6. **Evaluation approach Stage 7** (Ruslan reads 6 variants, uses D4 §8 axes + §9 selection criteria, может делать hybrid)
7. **Why 6 variants не 1** — diversity argument
8. **Notion page reference**

---

## LAUNCHERS-STAGE-6.md — 6 copy-paste launcher blocks

**Format each launcher:**

```
### CC session #N — Variant {NAME}

cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/0{N}-{name}.md` полностью и исполни. Variant {NAME} — {character}.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections (для comparability с другими 5 variants)
- Multi-pass (skeleton → flesh → coherence-critic)
- Use subagents параллельно
- Size target: 40-60 pages / 8000-12000 words

Deliverable: decisions/variants/JETIX-ARCH-V{N}-{NAME}.md

После:
git add decisions/variants/JETIX-ARCH-V{N}-{NAME}.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant {N} {NAME} — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

ETA 5-7 hours с subagents.
```

Заполни для всех 6 variants (Conservative / Maximalist / Deep-Tech / Hybrid / Emergent / Wildcard).

Также в `LAUNCHERS-STAGE-6.md` добавь:

**Before running 6 launchers — prep step (one CC):**
```
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull origin claude/jolly-margulis-915d34
git merge origin/claude/recursing-kirch-26223c --no-edit
git push origin claude/jolly-margulis-915d34
ls prompts/stage-6-variants/
```

**Claude launch command:**
```
ssh ruslan@100.99.156.28
tmux new -s stage6-v1  (или v2/v3/v4/v5/v6 в разных окнах)
claude --dangerously-skip-permissions
```

---

## Quality bar для ЭТОГО meta-task

Academic-grade, как Stage 4. То есть:
- Prompts substantive (не bullet-lists)
- Каждый variant prompt имеет clear lens / character
- Output structures identical для comparability
- All 15 questions explicitly framed в каждом prompt
- 24 locks referenced properly
- Voice preservation rules included
- Anti-patterns для writer specified

**Size per prompt:** ~400-600 lines markdown (substantial, but focused).

---

## Execution plan для ТВОЕЙ работы

**Pass 1 — Structure planning (20-30 min):**
- Read D1/D2/D3/D4 (already approved — skim for architect-relevant content)
- Draft skeleton каждого из 6 prompts (same structure, different character)

**Pass 2 — Detailed writing (120-180 min):**
- Use subagents for parallelism:
  - Subagent A: Draft Variant 1 Conservative full prompt
  - Subagent B: Draft Variant 2 Maximalist full prompt
  - Subagent C: Draft Variant 3 Deep-Tech full prompt
  - Subagent D: Draft Variant 4 Hybrid full prompt
  - Subagent E: Draft Variant 5 Emergent full prompt
  - Subagent F: Draft Variant 6 Wildcard full prompt
- Host thread: draft 00-README + LAUNCHERS-STAGE-6

**Pass 3 — Consistency polish (30-45 min):**
- Verify все 6 имеют identical output structure
- Check character differentiation (each has distinct lens)
- Cross-check 15 questions in each prompt
- Polish README + LAUNCHERS

**Total ETA:** 3-4.5 hours с subagents.

---

## Commit + push

```bash
git add prompts/stage-6-variants/
git add LAUNCHERS-STAGE-6.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[prompts] Stage 6 — 6 architect variant prompts + master index + launchers"
git push origin claude/jolly-margulis-915d34
```

---

## Notion update

https://www.notion.so/3492496333bf812e8b62cbc61338ce06

Append:
```
- 2026-04-21 late night (update 6) — Stage 6 prompts written (6 variants + master index + launchers). Ready for Ruslan to execute 6 parallel CC sessions.
```

---

## Deliverable (stdout summary)

```
# Stage 6 Prompts Complete

## Artifacts created
- prompts/stage-6-variants/00-README.md (master index)
- prompts/stage-6-variants/01-conservative.md (X lines)
- prompts/stage-6-variants/02-aggressive-maximalist.md
- prompts/stage-6-variants/03-aggressive-deep-tech.md
- prompts/stage-6-variants/04-hybrid.md
- prompts/stage-6-variants/05-emergent.md
- prompts/stage-6-variants/06-wildcard.md
- LAUNCHERS-STAGE-6.md (6 copy-paste blocks + prep step + claude launch command)

## Metrics
- Total lines: N
- Variants covered: 6/6
- 15 questions framed в каждом prompt
- 24 locks referenced: yes
- Output structure consistent: 24 sections per variant

## Ready for
- Ruslan reads LAUNCHERS-STAGE-6.md
- Runs prep step (one CC)
- Launches 6 parallel CC sessions (different tmux)
- Each variant writes its architecture (5-7 hours parallel)
- Stage 7: Ruslan reads 6 variants + selects

## Commit hash: abc1234
## Notion updated: yes
```

---

## Anti-patterns для твоей meta-work

1. ❌ **НЕ пиши один generic prompt 6 раз** — каждый variant имеет distinct character
2. ❌ **НЕ забудь Wildcard contrarian clause** — variant 6 может challenge brief
3. ❌ **НЕ skip 15 questions framing** — каждый prompt должен их перечислить
4. ❌ **НЕ разная output structure в разных variants** — consistency для Stage 7 comparison критична
5. ❌ **НЕ забудь LAUNCHERS-STAGE-6.md** — это самое важное для Ruslan (copy-paste ready)
6. ❌ **НЕ вставляй narrative философию в каждый prompt** — это instruction to architect, не Vision retelling

---

## After твоя meta-task complete

Ruslan:
1. Читает `LAUNCHERS-STAGE-6.md`
2. Выполняет prep step
3. Открывает 6 terminals (tmux windows)
4. В каждом copy-pastes launcher block для variant 1-6
5. Ждёт ~6 часов пока все 6 variants пишутся параллельно
6. Читает 6 variants (Stage 7) + выбирает final

**Это critical path к Jetix architecture v3.** Делай academic-grade.
