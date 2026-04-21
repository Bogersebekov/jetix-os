---
type: meta-task-prompt
created: 2026-04-21 (evening)
target: claude-code-on-server (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: 3 deep Perplexity research prompts (Wave 9, 10, 11) в prompts/perplexity-ce-research-2026-04-22/
estimated-time: 30-60 min
status: ready-to-execute
purpose: Step 1.5 (extension) из CE Research execution plan — добавить 3 новые waves к existing 8
---

# Meta-Task Prompt: Write 3 NEW Perplexity Research Prompts (Waves 9-11)

## Context

Ты — main Claude Code session на сервере. **Step 1 (Waves 1-8) уже completed:**
- 8 prompts written в `prompts/perplexity-ce-research-2026-04-22/wave-1...wave-8.md`
- 8 R-N research outputs collected by Ruslan через Perplexity Pro Search
- Lying в `raw/research/compounding-engineering-2026-04-22/R-1...R-8.md`

**Now Ruslan расширил scope:** добавляет 3 новые waves к research:
- **Wave 9 — Agentic Loop** (как работает внутри, основные понятия, mechanics, patterns)
- **Wave 10 — Continual Learning** (последние наработки 2024-2026, что работает лучше всего)
- **Wave 11 — Evals** (frameworks, benchmarks, как использовать в Jetix)

**Твоя задача:** написать 3 production-ready Perplexity prompts для этих waves
+ update README.md в той же папке.

**Format должен быть identical к existing wave-1...wave-8 prompts** — Ruslan
будет copy-paste каждый prompt в Perplexity Pro Search exactly как с предыдущими 8.

---

## Inputs (load перед началом)

### Required reading (для quality bar)

1. **`prompts/perplexity-ce-research-2026-04-22/wave-1-compounding-engineering-core.md`** — example existing prompt structure
2. **`prompts/perplexity-ce-research-2026-04-22/wave-7-boris-cherny-claude-code.md`** — second example (different topic для variation)
3. **`prompts/perplexity-ce-research-2026-04-22/README.md`** — existing README (will be updated to mention 3 new waves)
4. **`prompts/meta-write-perplexity-prompts-2026-04-21.md`** — original meta-prompt (universal template definition)

### Optional context (selectively, для grounding если нужно)

5. **`design/JETIX-FPF.md`** v2 — для understanding Jetix specifics
6. **`CLAUDE.md`** — для current 11-agent context

---

## Output structure

### Folder (existing)

`prompts/perplexity-ce-research-2026-04-22/`

### 3 NEW files + 1 update

```
prompts/perplexity-ce-research-2026-04-22/
  README.md                                   ← UPDATE: add waves 9-11 to file list
  wave-9-agentic-loop.md                      ← NEW
  wave-10-continual-learning.md               ← NEW
  wave-11-evals.md                            ← NEW
```

---

## Universal template (use existing structure)

**\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439 EXACTLY \u0442\u0443 \u0436\u0435 structure** \u043a\u0430\u043a wave-1...wave-8 (read existing
files for reference). Recap structure:

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

[Same as existing — 6 steps + save instructions]

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
decision: <wave-specific decision question>.

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older.

# Research Questions (answer ALL)

1. <question 1 — concrete>
... (10-15 questions per wave)

# Required Output Format

[Same sections as existing — Executive Summary / Sections 1-N / Production
Examples / Critical Assessment / Comparison к Anthropic ecosystem / Sources List]

# Quality Requirements

[Same as existing — citations inline + URL list, 5+ sources, specificity,
critical lens, recency 2024-2026, authoritative sources, verbatim quotes,
length 10-30 pages, what to AVOID]
```

---

## Per-wave content specifications

### Wave 9 — Agentic Loop deep dive

**Output filename:** `wave-9-agentic-loop.md`
**Perplexity output target:** `R-9-agentic-loop.md`

**Topic essence:** What is "agentic loop", canonical mechanics, internal concepts,
loop variants, production implementations, Jetix applicability.

**Decision question** для context: "Should Jetix's 11-agent architecture adopt
specific agentic loop patterns (ReAct / CodeAct / Plan-and-Execute / etc) и какие
именно?"

**Research questions to embed (12-15):**
1. What is "agentic loop" — canonical definitions from Anthropic, OpenAI, LangGraph,
   ReAct paper (Yao et al. 2022), and recent 2024-2026 sources?
2. Core internal concepts: observe → think → act → reflect cycle. How implemented?
3. Tool-use cycle within agentic loop — invocation, error handling, retry patterns.
4. Loop variants comparison: ReAct vs Reflexion vs Plan-and-Execute vs Tree-of-Thoughts
   vs CodeAct vs Voyager — when to use which?
5. How does **Claude Code's agentic loop** work internally? (sub-agents, Task tool,
   main session orchestration, message-passing)
6. Devin's agentic loop architecture (Cognition Labs)?
7. Cursor / Cline / Continue / Aider loop designs — comparison?
8. Termination conditions: max iterations, convergence detection, completion
   recognition. How avoid infinite loops?
9. Common patterns: parallel tool calls, sub-agent spawning, memory writeback
   between iterations, observation→action timing.
10. Anti-patterns: tool-call storms, hallucinated tool args, context exhaustion,
    infinite reflection.
11. Cost dynamics: tokens per iteration, total iterations to task completion
    (Claude/GPT/Gemini comparisons if data available).
12. Latest research papers (2024-2026) on agentic loop optimization (e.g.,
    Reflexion, Voyager, AutoGen, Skill Library).
13. Multi-agent loops: how does loop differ когда multiple agents coordinate vs
    single agent?
14. Anthropic-specific best practices для Claude Code agentic loop design?
15. What metrics measure quality of agentic loop (task completion rate, iterations
    to convergence, tool-call efficiency, cost per task)?

**Suggested follow-ups для Ruslan:**
1. "Show me a step-by-step trace of one ReAct iteration with actual tool calls"
2. "What's the simplest possible agentic loop I can implement в Claude Code?"
3. "Where do most production agentic loops break down — specific failure cases?"

---

### Wave 10 — Continual Learning state-of-the-art

**Output filename:** `wave-10-continual-learning.md`
**Perplexity output target:** `R-10-continual-learning.md`

**Topic essence:** Continual learning (a.k.a. lifelong learning) for LLM/agent
systems. State-of-the-art 2024-2026. Best methods. Practical tooling. Jetix
applicability.

**Decision question** для context: "Should Jetix adopt specific continual learning
mechanism (Mem0 / Letta / Anthropic memory tool / custom RAG) для its 11 agents,
заменяя или augmenting current wiki + per-agent strategies.md approach?"

**Research questions to embed (12-15):**
1. What is "continual learning" / "lifelong learning" / "online learning" в
   context LLM-based agents? Canonical definitions.
2. Distinction от related concepts: fine-tuning vs RAG vs in-context learning
   vs continual learning vs prompt-engineering. Specific differences с examples.
3. Latest 2024-2026 research: top 10 papers/breakthroughs in continual learning
   for LLM agents. What works empirically vs hype.
4. Methods comparison: LoRA fine-tuning, QLoRA, RAG-based memory, episodic memory,
   semantic memory (knowledge graphs), knowledge distillation. Trade-offs.
5. Memory hierarchies в production LLM agents: short-term (context window) vs
   medium-term (session memory) vs long-term (vector DB / knowledge graph). Best
   practices for boundary management.
6. **Practical tooling 2026** (deep dive each):
   - **Mem0** (formerly Embedchain) — architecture, capabilities, limitations
   - **Letta** (formerly MemGPT) — design philosophy, production usage
   - **Zep** — temporal knowledge graphs, results
   - **Cognee** — knowledge graph + memory hybrid
   - **Anthropic memory tool** (recent) — design, scope, limitations
   - **Sleep-time compute** (Anthropic concept) — what it is, how applies
7. Production examples с metrics: ChatGPT memory feature, Claude memory tool, Pi
   (Inflection), agent-specific implementations.
8. Failure modes: catastrophic forgetting, memory poisoning, retrieval drift,
   false memory consolidation. Mitigations.
9. Evaluation: how do you measure agent learning over time? Benchmarks?
10. Solo founder context: realistic implementation для team of 11 agents без
    massive infrastructure?
11. Comparison к existing Jetix infrastructure (wiki/ + per-agent strategies.md +
    voice-notes pipeline) — это какой level continual learning? Gaps?
12. Open-source vs proprietary: which tools are usable now, costs, scalability.
13. Integration patterns: continual learning + RAG hybrid? + memory hierarchies?
14. What's the canonical "best in class" production continual learning system
    in 2026?
15. Future direction: where this practice heading 2026-2027?

**Suggested follow-ups:**
1. "Compare Mem0 vs Letta vs Anthropic memory tool head-to-head with specific
   feature matrix"
2. "Show me the simplest continual learning implementation для solo founder Phase 1"
3. "Where does continual learning go wrong in production — specific case studies?"

---

### Wave 11 — Evals: agent quality measurement frameworks

**Output filename:** `wave-11-evals.md`
**Perplexity output target:** `R-11-evals.md`

**Topic essence:** Evals — what they are, eval types, latest 2024-2026 frameworks,
benchmarks, LLM-as-judge best practices, production patterns. Jetix-specific
application.

**Decision question** для context: "What minimum viable eval setup should Jetix
implement Phase 1 чтобы measure quality of 11 agents + D-document writing +
compound learning over time?"

**Research questions to embed (12-15):**
1. What are "evals" в LLM/agent context? Distinction от traditional unit tests
   и QA testing.
2. Eval types: deterministic (pass/fail), LLM-as-judge, human-in-loop, A/B
   testing, multi-turn evaluation, agent trajectory evaluation. When use which.
3. **Latest 2024-2026 frameworks** (deep dive each):
   - **Anthropic Evals** (open source) — capabilities, design
   - **OpenAI Evals** (open source) — comparison
   - **LangSmith** / **LangFuse** evaluation — production patterns
   - **Promptfoo** — strengths
   - **DeepEval** — testing framework
   - **Inspect AI** (UK AI Safety Institute) — research-grade
   - **Braintrust** — commercial offering
   - **Humanloop** — workflow integration
   - **Helicone** — observability + evals
   - **Phoenix** (Arize) — open source observability
   - **Galileo** — agent evaluation
   - **Anthropic Console Evals** — built-in
4. Benchmarks for agent quality: SWE-bench (verified), MMLU, HumanEval,
   AgentBench, ToolLLM, GAIA, OSWorld, WebArena, MLE-bench. Strengths/weaknesses.
5. **LLM-as-judge specifically:**
   - Best practices for prompt design
   - Known biases (position bias, length bias, self-enhancement bias)
   - Calibration techniques
   - Multi-judge ensembles vs single judge
   - When LLM-as-judge fails (vs human judgment)
6. Agent trajectory evaluation: how to evaluate multi-step reasoning, tool-use
   correctness, sub-agent coordination quality.
7. Production patterns: how teams build eval pipelines (offline + CI/CD +
   production monitoring). Real architectures.
8. Real production case studies (5+ named with metrics):
   - Anthropic — how they eval Claude
   - Cognition — how Devin is evaluated
   - Cursor / Replit / Sweep — eval approaches
   - OpenAI — eval for GPT models
9. Failure modes: eval gaming, Goodhart's law, dataset contamination, eval-train
   leakage, sycophancy in LLM-judges.
10. Cost dynamics: how much eval tokens vs production tokens (typical ratios)?
11. Solo founder applicable: minimum viable eval setup для Jetix Phase 1
    (no team, 11 agents, limited budget).
12. Specific Jetix application:
    - Как evaluate каждый из 11 agents (sales-lead / knowledge-synth / strategist /
      meta-agent / etc) — что measure для каждого?
    - Как evaluate D-document writing quality (instead of manual Stage B reviewers)?
    - Как evaluate compound learning over time (improvement metrics)?
    - Как evaluate FPF compliance в agent outputs?
13. Integration с Claude Agent SDK / Claude Code — native eval features?
14. Eval-driven development pattern — applies к agent system development?
15. Open questions / unsolved problems in agent evals 2026?

**Suggested follow-ups:**
1. "Build me a minimal eval setup for a solo founder с 11 Claude agents — concrete
   tools + workflow"
2. "How do I avoid eval gaming when LLM-judges evaluate my LLM-agents?"
3. "Show me Anthropic's published eval methodology для their own products"

---

## README.md update

Update existing `prompts/perplexity-ce-research-2026-04-22/README.md` — add waves
9-11 to file list section.

**Add к existing file list (после wave-8 line):**

```markdown
- wave-9-agentic-loop.md (NEW 2026-04-21 evening)
- wave-10-continual-learning.md (NEW 2026-04-21 evening)
- wave-11-evals.md (NEW 2026-04-21 evening)
```

**Update total time estimate** if README mentions it (e.g., "~3-5h Ruslan active
time" → "~5-7h для всех 11 waves").

**Add note** в README:

```markdown
## NEW: Waves 9-11 added 2026-04-21 evening

Waves 1-8 already executed by Ruslan (R-1...R-8 в raw/research/). Waves 9-11
are NEW additions — Ruslan executes via Perplexity then commits R-9, R-10, R-11
к raw/research/compounding-engineering-2026-04-22/.

Step 2 synthesis ждёт ВСЕ 11 reports.
```

---

## Process

### Step 1 — Read inputs (~10-15 min)

1. Read `wave-1-compounding-engineering-core.md` fully (для quality bar reference)
2. Read `wave-7-boris-cherny-claude-code.md` fully (variation reference)
3. Read existing `README.md`
4. Skim `meta-write-perplexity-prompts-2026-04-21.md` (universal template recap)

### Step 2 — Write 3 new prompt files (~30-45 min)

Extended thinking max. Per wave:
- Use EXACT structure from wave-1...wave-8 (frontmatter / Instructions / Follow-ups /
  ═══ divider / THE PROMPT / Role+Context / Research Questions / Output Format /
  Quality Requirements)
- Embed 12-15 research questions specific к этой wave (use specifications above)
- Embed 3 specific follow-up suggestions
- Quality requirements identical к existing 8

### Step 3 — Update README (~5 min)

Add 3 new file entries + brief note.

### Step 4 — Self-review (~5-10 min)

Verify:
- 3 new files created (correct names: wave-9, wave-10, wave-11)
- README updated
- Each new file follows EXACT template structure
- Research questions specific (NOT generic)
- Follow-up suggestions concrete

### Step 5 — Commit + push

```bash
git add prompts/perplexity-ce-research-2026-04-22/wave-9-agentic-loop.md \
        prompts/perplexity-ce-research-2026-04-22/wave-10-continual-learning.md \
        prompts/perplexity-ce-research-2026-04-22/wave-11-evals.md \
        prompts/perplexity-ce-research-2026-04-22/README.md

git commit -m "[prompts] CE Research Waves 9-11 — agentic loop + continual learning + evals

Step 1.5 (extension) deliverable. 3 NEW Perplexity prompts добавлены к existing
8 waves package per Ruslan request 2026-04-21 evening.

NEW prompts:
- wave-9-agentic-loop.md — internal mechanics, ReAct/Reflexion/CodeAct variants,
  Claude Code loop, production examples
- wave-10-continual-learning.md — Mem0/Letta/Zep/Cognee/Anthropic memory tool,
  memory hierarchies, latest 2024-2026 research, Jetix applicability
- wave-11-evals.md — Anthropic Evals/LangSmith/Inspect AI/Braintrust frameworks,
  SWE-bench/AgentBench benchmarks, LLM-as-judge best practices, Jetix application

Each prompt: production-ready copy-paste, 12-15 specific questions, 3 follow-up
suggestions, identical quality requirements к existing 8 waves.

README updated с 3 new file entries + execution note.

Step 2 synthesis (commit 65f9774) НА HOLD до Ruslan executes Waves 9-11 →
synthesis prompt updated к 11 waves → launch.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

git push origin claude/jolly-margulis-915d34
```

### Step 6 — Report

Compact summary:
- 3 new files created (correct paths)
- README updated
- Each follows universal template structure
- Total prompt content size (lines per file)
- Commit SHA
- Ready для Ruslan execution Step 1.6

---

## Critical constraints

1. **EXACT same structure** as existing wave-1...wave-8 prompts — Ruslan should
   copy-paste those 3 без mental overhead, identical UX.
2. **12-15 specific questions per wave** — NOT generic platitudes
3. **3 concrete follow-up suggestions** per wave
4. **Quality bar identical** — multi-source / recent 2024-2026 / specific /
   critical lens / authoritative sources
5. **README must be updated** — Ruslan should see all 11 wave files в single list
6. **DO NOT modify existing wave-1...wave-8 files** — read-only reference

---

## Success criteria

- [ ] 3 new files created (wave-9, wave-10, wave-11)
- [ ] README.md updated с 3 new entries + note
- [ ] Each new file follows universal template (EXACT structure of wave-1...wave-8)
- [ ] 12-15 questions per wave (specific, not generic)
- [ ] 3 follow-up suggestions per wave
- [ ] Quality requirements identical
- [ ] No modifications к existing wave-1...wave-8
- [ ] Commit + push successful
- [ ] Report generated

**END OF META-TASK PROMPT — WAVES 9-11**
