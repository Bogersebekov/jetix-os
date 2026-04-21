---
type: perplexity-prompts-package-readme
created: 2026-04-21
updated: 2026-04-21 (evening — waves 9-11 added)
purpose: Step 1.2 + 1.5 из CE Research Plan — 11 waves deep research через Perplexity Pro Search
executor: Ruslan (manual execution)
estimated-active-time: 5-7h across all 11 waves
output-target-folder: raw/research/compounding-engineering-2026-04-22/
---

# Perplexity CE Research Prompts — 11 Waves

**Created:** 2026-04-21 (waves 1-8); updated 2026-04-21 evening (waves 9-11 added)
**Purpose:** Step 1.2 + 1.5 из CE Research execution plan
**For:** Ruslan — manually run через Perplexity Comet (desktop) или Pro web

---

## Что здесь

11 deep, production-ready research prompts для Perplexity Pro Search по темам:

1. **Compounding Engineering core** — что это, откуда, кто практикует
2. **Swarm Intelligence agents** — multi-agent collectives, coordination patterns
3. **Self-improving systems** — meta-agents, SPL, Constitutional AI, recursion
4. **Failure modes + critique** — где НЕ работает, compound errors, critics
5. **Production case studies** — Devin, Cursor, Sweep, Aider, Wispr, Replit, Copilot
6. **Every / Cora / Compound** — Dan Shipper, Plan→Work→Review×12 architecture
7. **Boris Cherny + Claude Code** — design philosophy, replaceable agents, CLAUDE.md
8. **Skills + CLAUDE.md + knowledge storage** — native Claude Code mechanisms
9. **Agentic Loop** (NEW) — internal mechanics, ReAct/Reflexion/CodeAct variants, Claude Code loop
10. **Continual Learning** (NEW) — Mem0/Letta/Zep/Cognee/Anthropic memory tool, 2024-2026 state-of-the-art
11. **Evals** (NEW) — frameworks (Anthropic/OpenAI/LangSmith/Inspect AI/Braintrust), benchmarks, LLM-as-judge

Каждый prompt self-contained, copy-paste ready. 10-15 specific research questions,
3 follow-up suggestions, consistent quality requirements (multi-source, 2024-2026,
specificity, critical lens, inline citations + URL list).

---

## Execution (per wave)

Для каждого wave файла (1-11):

1. **Open Perplexity** — Comet desktop или Pro web (https://perplexity.ai)
2. **Enable Pro Search mode** — deep research, **НЕ Quick Search**
3. **Open** `wave-N-<topic>.md` из этой папки
4. **Copy** всё ниже разделителя `═══════════════════════════════` (строка после "THE PROMPT")
5. **Paste** в Perplexity, run
6. **Wait** 5-15 min для completion
7. **Optional:** задать 2-3 follow-up questions (suggested в каждом prompt file — секция
   "Recommended follow-up questions")
8. **Save** markdown output в `raw/research/compounding-engineering-2026-04-22/R-N-<topic>.md`
   (exact filename specified в каждом prompt file's frontmatter `output-target:`)
9. **Spot-check** quality:
   - All questions answered? (не skipped silently)
   - 5+ sources cited? (prefer 10+)
   - Recent (2024-2026)?
   - Specific examples (named entities, URLs)? NOT vague
   - Critical voices included? (pros AND cons)

---

## Execution order

**Recommended:** Linear 1 → 11. Waves 1-5 build general theory; waves 6-8 зум-ин
на specific case studies which assume theory baseline; waves 9-11 deepen на
agentic loop / continual learning / evals (added 2026-04-21 evening).

**Parallel batch (если спешка):** открыть 11 вкладок, запустить 11 одновременно —
sacrifice depth of follow-ups, но save 4-5h wall time. Perplexity Pro не лимитирует
parallel sessions для одного user. Каждый wave self-contained, так что parallel safe.

**Split across sessions:** 4-4-3 по сессиям (каждая ~1.5-2h active time).
Recommended если хочется осмысленно читать results между waves.

---

## Total time

- **Per wave active time:** 5-15 min Perplexity processing + 5-10 min read/follow-up
  + 2-3 min save to file = **~15-30 min Ruslan wall time per wave**
- **Total for 11 waves (serial):** ~3-5h Ruslan active
- **Total for 11 waves (parallel batch):** ~60-90 min Ruslan active
- **Recommended:** split в 3 sessions по 3-4 wave = ~1-1.5h active each

---

## Quality bar (что check в каждом output)

Prompt-level enforcement:
- **Multi-source:** minimum 5 different sources cited, prefer 10+
- **Recency:** 2024-2026 primary, 2023 acceptable if foundational
- **Specificity:** named companies/products/people/URLs, NOT "some framework"
- **Critical lens:** both pros and cons, failure modes, critics voices
- **Inline citations:** [1], [2] etc + full URL list at end with authors/dates
- **Authoritative sources:** academic papers, founder blog posts, podcast
  transcripts, github repos, official docs > random blog spam
- **Verbatim quotes:** when source makes specific claim, quoted directly
- **Length:** comprehensive — likely 10-30 pages markdown per wave

---

## After all 11 waves done

1. `git add raw/research/compounding-engineering-2026-04-22/`
2. `git commit -m "[research] Perplexity CE research 11 waves complete"`
3. `git push origin claude/jolly-margulis-915d34`
4. **Step 1.4 — Cloud Cowork quality inspection:** spawn Claude Code subagent для
   spot-check quality (missing questions? vague answers? missing sources?). Если gaps
   → either re-run specific wave OR note gaps для synthesis stage
5. **Step 2 — Synthesis:** launch main Claude Code для meta-synthesis всех 11 outputs
   → compose обновлённый CE Research Note в wiki/concepts/ + potential ADR addenda

---

## NEW: Waves 9-11 added 2026-04-21 evening

Waves 1-8 already executed by Ruslan (R-1...R-8 в `raw/research/compounding-
engineering-2026-04-22/`). Waves 9-11 are NEW additions per Ruslan request —
Ruslan executes через Perplexity then commits R-9, R-10, R-11 к
`raw/research/compounding-engineering-2026-04-22/`.

**Step 2 synthesis ждёт ВСЕ 11 reports** (не 8) — synthesis prompt должен быть
обновлён до launch, чтобы охватить full 11-wave corpus.

---

## File list

- `README.md` — this file
- `wave-1-compounding-engineering-core.md` — CE core definitions/origins/practitioners
- `wave-2-swarm-intelligence.md` — Swarm vs hierarchy, coordination, frameworks
- `wave-3-self-improving-systems.md` — Meta-agents, SPL, Constitutional AI, recursion
- `wave-4-failure-modes-critique.md` — Where these approaches fail, critics
- `wave-5-production-case-studies.md` — Devin, Cursor, Sweep, Aider, Wispr и т.д.
- `wave-6-every-cora-compound.md` — Every.to, Cora assistant, Compound architecture
- `wave-7-boris-cherny-claude-code.md` — Claude Code design philosophy, Boris writings
- `wave-8-skills-claudemd-knowledge.md` — Native Claude Code knowledge mechanisms
- `wave-9-agentic-loop.md` (NEW 2026-04-21 evening) — internal mechanics, ReAct/Reflexion/CodeAct, Claude Code loop
- `wave-10-continual-learning.md` (NEW 2026-04-21 evening) — Mem0/Letta/Zep/Cognee/Anthropic memory tool, 2024-2026
- `wave-11-evals.md` (NEW 2026-04-21 evening) — Anthropic/OpenAI/LangSmith/Inspect AI/Braintrust frameworks, benchmarks, LLM-as-judge

---

## Context snippet (на случай если Perplexity попросит уточнения)

Если Perplexity mid-research попросит context уточнения — copy-paste:

```
Context: Jetix is a Berlin-based solo-operator AI-native consultancy and multi-business
portfolio. We are deciding the architecture for an internal operational system (currently
12 Claude Code agents across 6 departments). Three architectural archetypes on the table:
(A) Hierarchy — current Jetix HQ (CEO/Strategist → Manager → Sales/Dev/Ops);
(B) Swarm — Boris Cherny / Claude Code pattern (interchangeable agents + shared CLAUDE.md);
(C) Compound — Every / Cora pattern (Plan → Work → Review×12 → Compound cycle).
Central question: where does the intelligence live — in agents, in documents, or in the
process?
```

---

**Next after Step 1.3 execution:** Step 1.4 quality inspection → Step 2 synthesis →
potential revision of D6 JETIX-FPF v2 methodology.
