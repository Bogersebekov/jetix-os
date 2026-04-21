---
type: meta-task-prompt
created: 2026-04-21
target: claude-code-on-server (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: 8 deep Perplexity research prompts в prompts/perplexity-ce-research-2026-04-22/
estimated-time: 1-2 hours
status: ready-to-execute
purpose: Создать 8 deep, structured prompts для Perplexity Pro Search execution by Ruslan (Step 1.2 из CE Research plan)
---

# Meta-Task Prompt: Write 8 Perplexity Research Prompts

## Context

Ты — main Claude Code session на сервере. **Твоя единственная задача** — написать
8 deep Perplexity research prompts для Compounding Engineering / Swarm Intelligence /
Boris Cherny / Every Cora / Skills+CLAUDE.md research project.

**Background:**
- Jetix OS (AI-native consulting + multi-business portfolio) только что completed
  D6 JETIX-FPF v2 (constitutional ontology, FPF-based, verified 93/100)
- Перед написанием D1-D8 Ruslan хочет глубоко изучить **Compounding Engineering**
  и **Swarm Intelligence** approaches, чтобы возможно revise methodology
- 3 архитектурных архетипа на столе:
  - **A. Иерархия** (Jetix HQ сейчас — CEO/Стратег→Менеджер→Sales/Dev/Ops)
  - **B. Рой** (Boris Cherny / Claude Code — взаимозаменяемые агенты + shared CLAUDE.md)
  - **C. Compound** (Every / Cora — Plan→Work→Review×12→Compound cycle)
- Главный вопрос: где живёт интеллект (в агентах / в документах / в процессе)?

**Твой output не будет прогоняться сам через Perplexity — Ruslan вручную возьмёт
каждый prompt и запустит в Perplexity Comet/Pro Search.** Поэтому prompts должны
быть production-ready: copy-paste и run.

---

## Inputs (load перед началом)

1. **`design/JETIX-FPF.md`** v2 (constitutional doc — для понимания Jetix context)
2. **`decisions/2026-04-19-architecture-v2-approval.md`** (ADR — для понимания
   approved decisions)
3. **`prompts/d6-jetix-fpf-2026-04-20/`** package (для understanding качества
   prompts которые мы пишем)
4. **`CLAUDE.md`** (project context)

**Не загружай:** все raw research, full ADR Chunk 8 detail, тонны history. Достаточно
high-level context.

---

## Output structure

### Folder

Создать: `prompts/perplexity-ce-research-2026-04-22/`

### 8 files (точные имена)

```
prompts/perplexity-ce-research-2026-04-22/
  README.md                                   ← overview + execution instructions для Ruslan
  wave-1-compounding-engineering-core.md
  wave-2-swarm-intelligence.md
  wave-3-self-improving-systems.md
  wave-4-failure-modes-critique.md
  wave-5-production-case-studies.md
  wave-6-every-cora-compound.md
  wave-7-boris-cherny-claude-code.md
  wave-8-skills-claudemd-knowledge.md
```

---

## Per-prompt structure (universal template)

КАЖДЫЙ wave-N-*.md файл должен иметь **эту structure** (адаптировать contents под wave):

```markdown
---
type: perplexity-research-prompt
wave: N
topic: <wave topic>
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-N-<topic-slug>.md
---

# Perplexity Prompt — Wave N: <Topic>

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet или Pro web)
2. Включите **Pro Search mode** (deep research)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions для probing depth (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-N-<topic>.md`

## Recommended follow-up questions (после initial answer)

1. <specific deepening question 1>
2. <specific deepening question 2>
3. <specific deepening question 3>

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on
<wave topic> for a Berlin-based AI consultancy (Jetix) building a multi-agent
operational system. The output will be used to make a critical architecture
decision: should we adopt <wave-relevant pattern>?

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older.

# Research Questions (answer ALL)

1. <question 1 — concrete>
2. <question 2 — concrete>
... (10-15 questions specific к этой wave)

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)
[Single-paragraph synthesis + top 5 key findings]

## Section 1 — <Section title>
[Detailed answer questions 1-N from this section]

## Section 2 — <Section title>
... (4-7 sections per wave)

## Specific Production Examples
[5+ named entities — companies/products/people — with URLs]

## Critical Assessment
- Pros (specific, evidence-backed)
- Cons + failure modes (specific, evidence-backed)
- When to use vs avoid

## Comparison к Anthropic ecosystem
[Если relevant — как это relates к Claude / Claude Code / Claude Agent SDK]

## Sources List
[Numbered list of ALL URLs cited inline, with author + date when available]

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Devin uses LangGraph for orchestration" NOT "Devin uses some framework"
- **Critical lens:** include pros AND cons, NOT marketing claims as truth
- **Recency:** prefer 2024-2026 sources (acceptable: 2023 if foundational)
- **Authoritative sources:** academic papers, founder blog posts, podcast transcripts,
  github repos, official documentation > random blog spam
- **Verbatim quotes:** when source makes claim, quote it directly (don't paraphrase)
- **Length:** comprehensive — likely 10-30 pages markdown when copied to file

# What to AVOID

- Marketing fluff ("revolutionary", "game-changing" without evidence)
- Generic "AI agents are powerful" prose
- Single-source dependencies (one blog post citation = insufficient)
- Aged sources (pre-2023 unless foundational paper)
- Speculation without source attribution
```

---

## Per-wave content specifications

Ниже — **detailed scope per wave**. Используй это как input для писания promptов.
Адаптируй research questions под specific topic.

### Wave 1 — Compounding Engineering core

**Output filename:** `wave-1-compounding-engineering-core.md`
**Perplexity output target:** `R-1-compounding-engineering-core.md`

**Topic essence:** Что такое "compounding engineering" как термин и practice. Откуда
вырос, кто практикует, ключевые patterns.

**Research questions to embed (10-15):**
1. Что такое "compounding engineering" — official + community definitions?
2. Откуда вырос термин (Anthropic? Cognition Labs? Kent Beck? Other origin)?
3. Кто canonical practitioners + ссылки на их writings/talks?
4. Какие core patterns: memory accumulation, pattern reuse, agent specialization,
   meta-learning, recursive self-improvement?
5. Какое tooling enables CE: Claude Agent SDK, Cursor, Devin, Sweep.dev,
   Continue, Aider — кто что implements?
6. Конкретные production case studies (3-5 with named results)?
7. Как CE отличается от просто "good multi-agent design" — substantive distinction
   или marketing?
8. Какие failure modes / когда НЕ работает?
9. Cost dynamics — сколько token spend vs single-agent baseline?
10. Adoption curve — production практика или research-only?
11. Solo founder applicability vs team-only?
12. Comparison к other compounding metaphors (Buffett financial / Naval leverage)?
13. What metrics measure "compounding effect"?
14. Failure post-mortems (transparency examples)?
15. Future direction (where this practice heading 2026-2027)?

**Suggested follow-ups для Ruslan:**
- "Show me a specific code example or workflow snippet of compounding engineering"
- "What's the smallest-scale operational example I can study?"
- "Critique from skeptics — who has argued CE is overhyped?"

---

### Wave 2 — Swarm intelligence agents

**Output filename:** `wave-2-swarm-intelligence.md`
**Perplexity output target:** `R-2-swarm-intelligence.md`

**Topic essence:** Multi-agent collectives, swarm patterns, hive-mind coordination
для code/research. Почему swarm > sequential в каких-то cases.

**Research questions (10-15):**
1. Definitions: swarm intelligence vs multi-agent system vs hive-mind?
2. Stigmergy + indirect coordination через shared environment — examples?
3. Production frameworks: AutoGen (Microsoft), CrewAI, LangGraph, Anthropic MCP,
   Claude Agent SDK swarm patterns — comparison?
4. OpenAI Swarm framework — что it teaches?
5. Где swarm побеждает sequential? Где проигрывает?
6. Cost dynamics — multi-agent ~15× tokens per literature; is leverage worth?
7. Coordination overhead patterns — когда becomes prohibitive?
8. Real production examples с metrics (5+)?
9. Devin's swarm vs hierarchy approach?
10. Anthropic's research papers on multi-agent systems (2024-2026)?
11. Replaceable agents principle — implementation patterns?
12. Compound errors problem — каждый agent вносит noise → result hallucinated?
13. Token economics практически — solo developer perspective?
14. Hybrid hierarchy+swarm patterns (best of both)?
15. Future predictions для swarm AI agents?

**Suggested follow-ups:**
- "What's the production-tested team size for swarm coordination?"
- "Show me the simplest possible swarm implementation I can replicate"

---

### Wave 3 — Self-improving / recursive systems

**Output filename:** `wave-3-self-improving-systems.md`
**Perplexity output target:** `R-3-self-improving-systems.md`

**Topic essence:** Meta-agents которые улучшают других agents. Recursive self-
improvement. System prompt learning. Constitutional AI. Iterative refinement.

**Research questions (10-15):**
1. Что значит "self-improving agent system" в production context (НЕ AGI hype)?
2. System prompt learning — как агент accumulates patterns в свои prompts?
3. Constitutional AI mechanism — Anthropic implementation details?
4. RLHF / DPO / iterative refinement — production examples?
5. Meta-agents которые audit/improve other agents — production cases?
6. "Skill" creation patterns — automated vs human-curated?
7. Karpathy's writings on agent improvement (Software 2.0/3.0 essays)?
8. Failure modes — recursive degradation / drift / over-fitting?
9. Real production wins (5+ named with metrics)?
10. How to measure "self-improvement" — what metrics?
11. Time horizons — daily / weekly / monthly improvement cycles?
12. Human-in-loop vs fully autonomous improvement?
13. Anthropic vs OpenAI vs Cognition approaches differences?
14. Solo founder applicability (small scale)?
15. Левенчук critique applies? ("agents don't strategize")

**Suggested follow-ups:**
- "What's the canonical production example of recursive agent improvement?"
- "What goes wrong when agents try to improve themselves?"

---

### Wave 4 — Failure modes + critique

**Output filename:** `wave-4-failure-modes-critique.md`
**Perplexity output target:** `R-4-failure-modes-critique.md`

**Topic essence:** Где CE/swarm/self-improving НЕ работает. Critical voices.
Production failures. Unsolved problems.

**Research questions (10-15):**
1. Documented production failures of multi-agent / swarm systems (named cases)?
2. Prompt injection between agents — known vulnerabilities + exploits?
3. Compound errors — quantitative measurements (errors compound at rate X)?
4. Coordination overhead — when does cost exceed benefit (specific thresholds)?
5. Sycophancy in agent reviewers — agents agreeing with each other rather
   than catching errors?
6. Critics: who argues against CE / swarm / self-improvement (named voices)?
7. Yann LeCun / Gary Marcus / similar AI critics на multi-agent claims?
8. Левенчук critique — "agents не стратегируют" — full reasoning?
9. Cost overruns — where teams adopted CE and regretted (post-mortems)?
10. Debugging multi-agent systems — known difficulty (specific cases)?
11. Reproducibility crisis — same prompt → different agent behavior?
12. Latency multiplication — UX impact?
13. Single-agent baselines beating multi-agent — published results?
14. Tooling immaturity issues (debugging / observability / testing)?
15. Anthropic's own published warnings / limitations docs?

**Suggested follow-ups:**
- "What's the most damaging publicly-documented multi-agent system failure?"
- "Where would you NEVER use multi-agent today?"

---

### Wave 5 — Production case studies general

**Output filename:** `wave-5-production-case-studies.md`
**Perplexity output target:** `R-5-production-case-studies.md`

**Topic essence:** Deep dive на конкретные production multi-agent / CE products.
Architecture, results, challenges.

**Research questions (10-15):**
1. **Devin (Cognition Labs)** — architecture details, results, controversies
   (Pokemon benchmark)?
2. **Cursor** — multi-agent features, sub-agents, production usage stats?
3. **Sweep.dev** — how their swarm of agents works, metrics?
4. **Aider** — solo-but-iterative model, lessons?
5. **Wispr Flow** — voice-to-action multi-agent design?
6. **GitHub Copilot Workspace** — multi-agent architecture?
7. **Replit Agent** — design + adoption?
8. **Anthropic's own production agents** (Claude Code, Claude Computer Use)?
9. **Lovable / v0 / Bolt** — design tool agents?
10. **Continue** — open source agent architecture?
11. Comparison matrix: who uses swarm / hierarchy / compound / hybrid?
12. Pricing/cost models — what works commercially?
13. User feedback patterns — what users love/hate?
14. Engineering team sizes за каждым из этих products?
15. Open source vs proprietary — what works in each?

**Suggested follow-ups:**
- "What's the single most successful production multi-agent system today by revenue?"
- "Which of these would you copy directly for a Berlin AI consultancy?"

---

### Wave 6 — Every / Cora Compound deep dive

**Output filename:** `wave-6-every-cora-compound.md`
**Perplexity output target:** `R-6-every-cora-compound.md`

**Topic essence:** Specifically Every.to publication + Cora email assistant +
Compound architecture (Plan→Work→Review×12→Compound). Dan Shipper writings.

**Research questions (10-15):**
1. **Every.to** — history, founding, current writers (Dan Shipper, Nathan Baschez,
   others)?
2. Every.to thesis on AI tools and agents — core claims?
3. **Cora email assistant** — full product description, target user, pricing?
4. **Cora technical architecture** — what tech stack, how agents work internally?
5. **Compound concept** — Plan agent → Work agents → Review×12 → Compound cycle —
   detailed mechanics?
6. "Знание учится на ошибках" / "Knowledge learns from errors" — how exactly errors
   become rules become subagents become skills?
7. Dan Shipper specific essays on compound / agents (2024-2026) — links + summaries?
8. Every podcasts / interviews where Compound discussed?
9. AI Daily, AI Labs newsletter — Every's other AI properties?
10. How does Compound differ from Devin's planning approach?
11. Tooling stack — Anthropic? OpenAI? Custom orchestration?
12. Critical reception — who challenges Compound's claims?
13. Adoption — how many users, growth rate, retention?
14. Open source any of it?
15. Future direction — where Every is taking Compound?

**Suggested follow-ups:**
- "Show me a concrete error → rule → subagent → skill cycle example from Cora"
- "What's the smallest compound architecture I can replicate?"
- "Where does Compound break down or fail?"

---

### Wave 7 — Boris Cherny + Claude Code design philosophy

**Output filename:** `wave-7-boris-cherny-claude-code.md`
**Perplexity output target:** `R-7-boris-cherny-claude-code.md`

**Topic essence:** Boris Cherny (Claude Code creator at Anthropic) — все его
writings, talks, design decisions. Why Claude Code uses swarm pattern.

**Research questions (10-15):**
1. Boris Cherny biography + role at Anthropic — background?
2. All Boris's public writings (blog posts, Twitter @bcherny, essays) — comprehensive list?
3. Boris's podcast appearances (Latent Space, AI Daily, Lex Fridman, etc) —
   list + key quotes?
4. Boris's talks at conferences (AI Engineer Summit, etc) — links?
5. Claude Code architecture decisions — why swarm > hierarchy?
6. **Replaceable agents principle** — Boris's reasoning?
7. **CLAUDE.md as shared context** — design rationale Boris explained?
8. **Sub-agent system in Claude Code** — mechanics, when use, best practices?
9. **Hooks system** (settings.json hooks, lifecycle hooks) — full design?
10. **Skills feature** in Claude Code (newer 2025-2026) — how it works, Boris's
    intent?
11. **MCP (Model Context Protocol)** — Boris's role + design rationale?
12. Boris's broader views on agent design philosophy?
13. Anthropic research papers с Boris involvement?
14. Public criticism Boris has faced + his responses?
15. Future direction Boris hints at для Claude Code?

**Suggested follow-ups:**
- "What's Boris's most important essay or talk about agent design?"
- "What does Boris say about NOT using swarm patterns?"
- "Boris's specific advice for solo developers using Claude Code?"

---

### Wave 8 — Skills + CLAUDE.md + knowledge storage

**Output filename:** `wave-8-skills-claudemd-knowledge.md`
**Perplexity output target:** `R-8-skills-claudemd-knowledge.md`

**Topic essence:** Native Claude Code knowledge mechanisms — Skills, CLAUDE.md,
plugins, MCP, slash commands, memory. Best practices. Comparison к custom solutions.

**Research questions (10-15):**
1. **Skills system** в Claude Code — full documentation, format, location
   (~/.claude/skills/, project skills/)?
2. Skills discovery — how Claude knows which skills available?
3. Skills inheritance / scope (user vs project vs plugin)?
4. **anthropic-skills** package — what's в нём, examples?
5. **CLAUDE.md best practices** — user-level (~/.claude/CLAUDE.md) vs project-level
   (./CLAUDE.md)?
6. CLAUDE.md hierarchy + override rules?
7. CLAUDE.md size limits, chunking strategies, performance impacts?
8. **Memory systems** в Claude Code — auto-memory feature, session vs persistent?
9. Per-agent memory layering patterns?
10. **Plugins ecosystem** в Claude Code — marketplace, examples, installable packages?
11. **MCP servers integration** — how stores knowledge across sessions?
12. **Slash commands** + their relation to skills?
13. Best community-curated examples (Awesome Claude Code lists)?
14. Common mistakes with CLAUDE.md / Skills (anti-patterns)?
15. Comparison: native Claude Code knowledge mechanisms vs custom solutions
    (wiki + per-agent strategies.md) — when each makes sense?

**Suggested follow-ups:**
- "Show me the canonical example of an excellent CLAUDE.md"
- "What's the relationship between Skills and Sub-agents in Claude Code?"
- "Where do most teams reinvent something Claude Code already provides?"

---

## README.md content (для Ruslan)

Также напиши `prompts/perplexity-ce-research-2026-04-22/README.md` со следующим:

```markdown
# Perplexity CE Research Prompts — 8 Waves

**Created:** 2026-04-21
**Purpose:** Step 1.3 из CE Research execution plan
**For:** Ruslan to manually run в Perplexity Comet/Pro Search

## Execution

For each wave (1-8):

1. Open Perplexity (Comet desktop or Pro web)
2. Enable **Pro Search** mode (deep research, NOT Quick Search)
3. Open `wave-N-<topic>.md` файл
4. Copy everything below the `═══` divider
5. Paste into Perplexity, run
6. Wait 5-15 min для completion
7. Optional: ask 2-3 follow-up questions (suggested in each prompt file)
8. Save output as markdown в `raw/research/compounding-engineering-2026-04-22/R-N-<topic>.md`
9. Spot-check quality:
   - All questions answered?
   - 5+ sources cited?
   - Recent (2024-2026)?
   - Specific, не vague?

## Order

Recommend execution order: 1, 2, 3, 4, 5 (general theory first), then 6, 7, 8
(specific case studies). Or batch parallel — your call.

## Total time

~3-5h Ruslan active time across all 8 waves. Можно разбить на 2 sessions (utro/dnem).

## After all 8 done

Commit + push folder `raw/research/compounding-engineering-2026-04-22/` →
Cloud Cowork inspects quality (Step 1.4) → proceed Step 2 (synthesis).

## File list

- wave-1-compounding-engineering-core.md
- wave-2-swarm-intelligence.md
- wave-3-self-improving-systems.md
- wave-4-failure-modes-critique.md
- wave-5-production-case-studies.md
- wave-6-every-cora-compound.md
- wave-7-boris-cherny-claude-code.md
- wave-8-skills-claudemd-knowledge.md
```

---

## Process

### Step 1 — Read inputs (~15-20 min)

Load D6 v2 (selectively), ADR (selectively), CLAUDE.md, existing prompts package
для understanding quality bar.

### Step 2 — Write 8 prompt files + README (~60-90 min)

Extended thinking max. Per wave:
- Адаптируй universal template structure
- Embed 10-15 specific research questions (use specifications above)
- Embed 3 follow-up suggestions
- Quality requirements consistent across all 8

**Key principle:** prompts должны быть production-ready copy-paste для Perplexity.
Ruslan не должен думать "что here meant" — всё specified.

### Step 3 — Self-review (~10-15 min)

Verify:
- 8 wave files + 1 README created в правильной folder
- Каждый file follows universal template structure
- Research questions specific (НЕ generic)
- Follow-up suggestions concrete
- Quality requirements identical across all 8

### Step 4 — Commit + push

```bash
git add prompts/perplexity-ce-research-2026-04-22/
git commit -m "[prompts] CE Research 8 Perplexity prompts package — Step 1.2 complete

Step 1.2 deliverable из 🌊 Step 1: Research 8 Waves Execution Plan.
Готовы 8 deep prompts + README для Ruslan ручного execution через
Perplexity Pro Search.

Wave coverage:
1. Compounding Engineering core
2. Swarm intelligence agents
3. Self-improving / recursive systems
4. Failure modes + critique
5. Production case studies general
6. Every / Cora Compound deep dive (NEW priority)
7. Boris Cherny + Claude Code design philosophy (NEW priority)
8. Skills + CLAUDE.md + knowledge storage (NEW priority)

Each prompt: production-ready copy-paste, 10-15 specific questions,
3 follow-up suggestions, quality requirements (multi-source, recent,
specific, critical lens, citations inline + URL list).

Next: Ruslan executes manually через Perplexity, saves outputs в
raw/research/compounding-engineering-2026-04-22/. ETA 3-5h Ruslan active.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

git push origin claude/jolly-margulis-915d34
```

### Step 5 — Report back

Compact summary:
- 9 files created (8 wave + README)
- Total prompt content size (lines)
- Commit SHA
- Verification: все 8 follow consistent structure
- Ready для Ruslan Step 1.3 execution

---

## Critical constraints

1. **Production-ready prompts** — Ruslan should copy-paste без mental overhead
2. **Consistent structure** — всех 8 follows universal template
3. **Specific questions** — 10-15 concrete per wave, NOT generic
4. **Quality bar identical** — все 8 enforce same multi-source / recent / specific
5. **Universal template сначала designed** — потом 8 instances из неё
6. **README essential** — Ruslan opens folder и сразу понимает что делать

---

## Success criteria

- [ ] `prompts/perplexity-ce-research-2026-04-22/` folder created
- [ ] 8 wave files created (correct names)
- [ ] README.md created
- [ ] Each wave file follows universal template
- [ ] Research questions adapted per wave (10-15 specific)
- [ ] Follow-up suggestions present (3 per wave)
- [ ] Quality requirements consistent
- [ ] Commit + push successful
- [ ] Report generated

**END OF META-TASK PROMPT**
