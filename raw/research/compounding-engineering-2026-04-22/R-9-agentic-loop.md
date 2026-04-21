# Agentic Loop — Technical Due Diligence for Jetix

*Berlin AI Consultancy | 11 Claude-based Agents | 6 Departments*
*Prepared as a deep reference document for architecture decisions*
*Sources compiled from Anthropic, OpenAI, Google, arXiv, and production post-mortems, 2022–2026*

---

## Executive Summary

### What Is the Agentic Loop?

The agentic loop is the fundamental execution primitive of any autonomous AI system. At its most general, it is a while-loop in which a language model receives an observation from its environment, reasons about what to do next, emits a structured action (typically a tool call), observes the result, and repeats — until a stopping condition fires or the model judges the task complete. Anthropic's canonical formulation is direct: agents are *"typically just LLMs using tools based on environmental feedback in a loop"* [1]. The loop is not a complex design pattern but a logical consequence of the fact that many tasks require more information than fits in a single prompt.

The formal grounding comes from the ReAct paper (Yao et al., ICLR 2023), which augments an agent's action space to \( \hat{A} = A \cup L \), where \( L \) is the space of natural language "thoughts." Thoughts update context without affecting the external environment; tool calls affect the environment and return observations. The interleaved Thought→Action→Observation trajectory is now the de facto standard for production agentic systems including Claude Code, Cursor, Devin, and OpenHands [4].

### Which Variants Matter?

Nine published variants build on this core:

1. **ReAct** (2022) — the foundational interleaved thought/action/observation loop. The default for most production systems.
2. **Reflexion** (2023) — adds verbal self-reflection between trial episodes; best for tasks with clear pass/fail signals (unit tests, game scores).
3. **Plan-and-Execute** (2023) — separates planning from execution, using a cheaper executor model; best for predictable multi-step pipelines.
4. **Tree-of-Thoughts** (2023) — branching search over candidate reasoning paths; powerful for combinatorial problems but exponentially expensive.
5. **CodeAct** (2024) — replaces JSON tool calls with executable Python; enables multi-tool composition and self-debugging via tracebacks.
6. **Voyager** (2023) — builds a persistent skill library; the pattern most relevant to long-running consultancy workflows.
7. **Self-Refine** (2023) — iterative generate→critique→rewrite with no external oracle; effective for writing/dialogue, ineffective for math.
8. **Self-Consistency** (2022) — majority-vote over multiple independent reasoning paths; for discrete-answer reasoning tasks only.
9. **AutoGPT-style** (2023) — unbounded autonomous loop with memory and planning; historically important, practically unreliable.

For Jetix's Claude-based system, **ReAct is the de facto default** (it is what Claude Code implements natively). **Plan-and-Execute** is directly applicable for research and operations workflows. **Reflexion** applies wherever there is a verifiable oracle (e.g., code tests, data validation). **Self-Refine** is relevant for marketing and content generation agents.

### What Does Claude Code Use?

Claude Code implements a minimalist ReAct loop: chain-of-thought reasoning, native JSON tool calls, and context compaction at 95% capacity. It explicitly avoids framework abstractions. Boris Cherny, Claude Code's creator, describes it as *"the thinnest possible wrapper over the model. We literally could not build anything more minimal"* [26]. Planning is behavioral (user-prompted), not architectural — there is no separate planner module. Sub-agents are supported but do not inherit parent context, making them best suited for well-scoped isolated tasks rather than collaborative deliberation.

### Should Jetix Adopt a Specific Variant?

The evidence supports a **hybrid approach by department type, grounded in the simplest adequate variant**:

- **Engineering/Technical** agents: ReAct (default) + CodeAct action space, with Reflexion loops where unit tests are available
- **Research** agents: Orchestrator-worker multi-agent (Anthropic's own published pattern) with Plan-and-Execute decomposition
- **Marketing/Content** agents: Self-Refine loops with explicit quality criteria
- **Sales** agents: ReAct with retrieval tools + Reflexion on CRM outcome signals
- **Operations** agents: Plan-and-Execute pipelines with human-in-the-loop interrupts at irreversible actions
- **Design** agents: Self-Refine for iteration, ReAct for research gathering

The critical constraint: **multi-agent systems use ~15× more tokens than single-agent chat interactions** [3]. For a solo-founder operating 11 agents, token cost is the primary architectural constraint. The recommendation is to default every agent to single-agent ReAct and introduce multi-agent coordination only where the task demonstrably requires parallelism that single-agent cannot provide.

---

### Top 5 Key Findings

- **The 15× token cost of multi-agent is a hard architectural constraint.** Anthropic's own published data: agents use ~4× more tokens than chat; multi-agent systems use ~15× more than chat [3]. For Jetix's 11-agent system running on Claude (Sonnet or Opus pricing), this means multi-agent coordination must be reserved for tasks where the value clearly exceeds the token cost. For most consultancy tasks, single-agent ReAct with well-scoped tools is the correct default.

- **Claude Code's "thinnest wrapper" philosophy is a design prescription, not a limitation.** The agentic search replacing RAG, CLAUDE.md as the simplest persistent memory, and behavioral plan mode represent deliberate choices that outperformed more complex alternatives in Anthropic's own testing [26]. Jetix should resist the temptation to add framework complexity (LangGraph, AutoGen) that Claude Code already renders unnecessary.

- **Termination conditions are the most under-specified part of most agent deployments.** The "Ralph Wiggum problem" (premature completion), doom loops, and goal drift all stem from inadequate stopping conditions. Every Jetix agent must have: a `maxTurns` hard cap, a cost budget, and an externally-verifiable completion signal where possible [84].

- **Benchmark scores are unreliable without contamination controls.** Devin's 13.86% SWE-bench score was on a 25% sample without independent verification [61]; SWE-bench Verified scores are contaminated at the frontier (80.9% on Verified vs. 45.9% on Pro) [109]. OpenHands achieves 72% on Verified but only 19–25% on live, post-cutoff benchmarks. Jetix should evaluate its agents on its own closed-domain tasks, not public benchmarks.

- **The Cognition contradiction is instructive.** Walden Yan's June 2025 "Don't Build Multi-Agents" argued that *"running multiple agents in collaboration only results in fragile systems"* [62]. In March 2026, Cognition launched Devin-manages-Devins [63]. The reconciliation: multi-agent works when agents share full traces (Principle 1) and have isolated focus. The failure mode is multi-agent systems that pass only summaries between agents, not full context. Claude Code's sub-agents share this limitation by design.

---

## Section 1 — Canonical Definitions & Core Concepts

### Q1: What Is an Agent vs. a Workflow?

The most authoritative published taxonomy comes from Anthropic's December 2024 blog post "Building Effective Agents" [1]:

> **"Workflows** are systems where LLMs and tools are orchestrated through **predefined code paths**. **Agents**, on the other hand, are systems where LLMs **dynamically direct their own processes and tool usage**, maintaining control over how they accomplish tasks."

The defining criterion is **who controls the flow graph**: in a workflow, deterministic code decides which tools to call and in what order; in an agent, the LLM decides. Harrison Chase (LangChain CEO) at the 2025 AI Engineer Summit expressed this concisely: *"The more agentic an application is, the more an LLM decides the **control flow** of the application"* [11].

This distinction maps onto a concrete architectural test: if you could draw a fixed flowchart of the system before any LLM is invoked, it is a workflow. If the LLM's outputs determine which nodes are visited next, it is agentic.

Anthropic groups both under **"agentic systems"** as an umbrella but draws a hard architectural line between them [1]. A RAG pipeline (retrieve → augment → generate in a fixed sequence) is a workflow. Claude Code resolving a GitHub issue over many file edits and test runs is agentic.

#### The Formal Mathematical Grounding (ReAct Paper)

The ReAct paper (Yao et al., 2022 / ICLR 2023) provides the formal foundation:

> "Consider a general setup of an agent interacting with an environment for task solving. At time step t, an agent receives an **observation** \(o_t \in O\) from the environment and takes an **action** \(a_t \in A\) following some policy \(\pi(a_t | c_t)\), where \(c_t = (o_1, a_1, \cdots, o_{t-1}, a_{t-1}, o_t)\) is the **context** to the agent." [4]

The ReAct augmentation extends the action space:

> "The idea of ReAct is simple: we augment the agent's action space to \(\hat{A} = A \cup L\), where \(L\) is the space of language. An action \(\hat{a}_t \in L\) in the language space, which we will refer to as a **thought or reasoning trace**, does not affect the external environment, thus leading to no observation feedback. Instead, a thought \(\hat{a}_t\) aims to compose useful information by reasoning over the current context \(c_t\), and update the context \(c_{t+1} = (c_t, \hat{a}_t)\) to support future reasoning or acting." [4]

This formalism captures everything essential: the context is a growing list \(c_t\) that accumulates all prior observations and actions; thoughts are actions in language space that update context without side effects; tool calls are actions that affect the external environment and produce new observations; the policy \(\pi\) (the LLM) determines which action to take at each step.

#### Competing Definitions from the Ecosystem

The Latent Space "Agent Engineering" post from the 2025 AI Engineer Summit [11] compiled multiple practitioner definitions:

> **Lilian Weng (formerly OpenAI, now co-founder Thinking Machines):**
> **Agent = LLM + memory + planning skills + tool use**

> **OpenAI Agents SDK (TRIM definition):**
> *"An agent is an AI application consisting of: a **model** equipped with **instructions** that guide its behavior, access to **tools** that extend its capabilities, encapsulated in a **runtime** with a dynamic lifecycle."*

> **Harrison Chase (LangChain CEO):**
> *"The more agentic an application is, the more an LLM decides the **control flow** of the application."*

> **Dan Jeffries:**
> *"An AI system that's capable of carrying out and completing **long running**, open ended tasks in the real world."*

The TRIM definition (Model, Instructions, Tools, Runtime) notably omits explicit memory and planning, which swyx notes is a gap versus Weng's formulation [11]. For Jetix's purposes, Weng's formulation is more operationally complete.

LangGraph's official definition adds a useful specificity:

> "An agent is a system that uses an LLM to **decide the control flow of an application**. There are many ways that an LLM can control application: An LLM can route between two potential paths; An LLM can decide which of many tools to call; An LLM can decide whether the generated answer is sufficient or more work is needed." [8]

### Q2: What Is the Canonical "Agentic Loop" Structure?

Anthropic's multi-agent research system paper (June 2025) provides the tightest shorthand: *"A multi-agent system consists of **multiple agents (LLMs autonomously using tools in a loop) working together**"* [3]. The unit definition is: **one agent = one LLM + one tool loop**.

The LangGraph documentation provides the implementation-level definition:

> "In a tool-calling agent, an LLM is called **repeatedly in a while-loop**. At each step the agent decides which tools to call, and what the inputs to those tools should be. Those tools are then executed, and the outputs are fed back into the LLM as **observations**. The while-loop terminates when the agent decides it has enough information to solve the user request and it is not worth calling any more tools." [8]

The OpenAI Agents SDK's developer portal formalizes the loop as five explicit states [6]:

> "One SDK run is one application-level turn. The runner keeps looping until it reaches a real stopping point:
> 1. Call the current agent's model with the prepared input.
> 2. Inspect the model output.
> 3. If the model produced tool calls, execute them and continue.
> 4. If the model handed off to another specialist, switch agents and continue.
> 5. If the model produced a final answer with no more tool work, return a result.
>
> That loop is the core concept behind the SDK. Tools, handoffs, approvals, and streaming all build on top of it rather than replacing it." [6]

#### Chain vs. Loop vs. Workflow — Comparative Table

| Concept | Control Flow Owner | Feedback / State | Iteration | Canonical Example |
|---|---|---|---|---|
| **Chain (no feedback)** | Deterministic code | None (open-loop) | Fixed, single-pass | RAG: retrieve → augment → generate. Anthropic's "prompt chaining" workflow [1] |
| **Workflow (deterministic)** | Deterministic code; LLM called at fixed nodes | Limited (results fed to next fixed step) | Predefined | Anthropic "evaluator-optimizer" with fixed N rounds [1] |
| **Agentic loop** | LLM determines next action | Full: each tool result becomes the next observation; context accumulates as \(c_t\) | Unbounded (until stop condition) | ReAct [4], Claude Code [26], OpenAI Agents SDK [6] |

Anthropic contrasts RAG with agentic loops explicitly [3]:

> "Traditional approaches using Retrieval Augmented Generation (RAG) use **static retrieval** — they fetch some set of chunks that are most similar to an input query... In contrast, our architecture uses a **multi-step search** that dynamically finds relevant information, adapts to new findings, and analyzes results to formulate high-quality answers."

#### The Four Phases: Observe → Think → Act → Reflect

The four-phase characterization maps onto concrete implementation artifacts:

**OBSERVE**: The `tool_result` content block (Claude) / `function_call_output` (OpenAI) / `functionResponse` (Gemini) from the previous turn. Lives in the harness — the harness executes the tool and constructs the observation [2][5][10].

**THINK**: Claude's `thinking` content blocks (extended thinking); OpenAI's opaque reasoning tokens; Gemini's `thought_signature`. Lives in the LLM — the harness does not control this unless extended thinking is explicitly enabled. Formalized in ReAct as thought \(\hat{a}_t \in L\) [4].

**ACT**: A `tool_use` block (Claude), `function_call` item (OpenAI), or `functionCall` part (Gemini). The model emits `stop_reason: "tool_use"` (Claude), signaling to the harness to dispatch the call [2][5][10].

**REFLECT**: In Claude's multi-agent system, subagents *"use interleaved thinking after tool results to evaluate quality, identify gaps, and refine their next query"* [3]. In standard loops, reflection is implicit in the model's generation decision. LangGraph supports explicit `reflection` nodes.

---

## Section 2 — Tool-Use Cycle Mechanics

### Q3: How Does the Tool-Use Cycle Work at the Implementation Level?

The tool-use cycle is identical across the three major providers at the structural level, with differences only in the message format.

#### Claude (Anthropic)

The Claude API tool loop [2]:

1. Claude returns `stop_reason: "tool_use"` + one or more `tool_use` content blocks (each with `id`, `name`, `input`)
2. The harness executes the tool, constructs a `tool_result` content block (keyed by `tool_use_id`)
3. The harness appends this as a new `user` turn containing the `tool_result`
4. The loop continues until Claude returns `stop_reason: "end_turn"` with no tool calls

```
Assistant turn:
  content: [
    {type: "tool_use", id: "toolu_xyz", name: "search", input: {"query": "..."}}
  ]
  stop_reason: "tool_use"

Next user turn:
  content: [
    {type: "tool_result", tool_use_id: "toolu_xyz", content: "...result..."}
  ]
```
*Source: [Anthropic Tool Use docs][2]*

**Token overhead**: The `tools` parameter definition, `tool_use` blocks in responses, `tool_result` blocks in requests, and an automatically injected tool-use system prompt (~346 tokens for Claude Opus 4 / Sonnet 4.5 with `auto` tool choice) [2].

**Parallel tool calls**: Claude may issue multiple `tool_use` blocks in a single response. The key spec constraint: *"All tool results must be in a single user message"* — sending separate messages reduces parallelism in future turns [84]. Can be disabled with `disable_parallel_tool_use=true` [84].

#### OpenAI (Responses API)

OpenAI's 5-step description [5]:

> "1. Make a request to the model with tools it could call
> 2. Receive a tool call from the model
> 3. Execute code on the application side with input from the tool call
> 4. Make a second request to the model with the tool output
> 5. Receive a final response from the model (or more tool calls)"

The "or more tool calls" qualifier in step 5 makes this a loop, not a single-turn flow. Loop termination = text output with no more tool calls [5].

OpenAI's Agents SDK adds `max_turns` as a safety parameter, raising `MaxTurnsExceeded` when exceeded [6].

#### Gemini (Google)

Google's 4-step function calling [10]:

> "1. **Define function declaration**
> 2. **Call API with function declarations**: The model responds with a **structured JSON object** containing the function name, arguments, and a unique `id`
> 3. **Execute function code (your responsibility)**
> 4. **Create user friendly response with function result and call the model again**"

Gemini uniquely supports "thought signatures" — mechanisms for preserving reasoning context across multi-turn conversations without exposing it in visible turn history [10].

#### What Lives in the Prompt vs. the Harness

| Component | Location | Description |
|---|---|---|
| **System prompt** | LLM context | Role/persona, task instructions, tool usage guidance, stopping criteria, safety rules |
| **Tool definitions** | LLM context (injected as tokens) | JSON Schema schemas for each available tool |
| **Conversation history** | LLM context | Growing `messages` list — the context \(c_t\) |
| **Scratchpad / thinking** | LLM context (often opaque) | Claude `thinking` blocks; Gemini `thought_signature`; OpenAI reasoning tokens |
| **Tool dispatcher** | Harness | Routes `tool_use` blocks to actual implementations |
| **Loop controller** | Harness | The `while` that checks stop conditions: `end_turn` + no tool calls; `max_turns` |
| **State manager** | Harness | Maintains and appends `tool_result` blocks to context |
| **Memory backend** | External | Long-horizon summarization store; LangGraph checkpointer; CLAUDE.md |

#### System Prompt Structure (Anthropic Pattern)

```
<system>
  [Role / persona definition]
  [Task instructions + goals]
  [Tool usage guidance — "when to call X, when not to call X"]
  [Output format instructions]
  [Stopping criteria]
  [Safety / escalation rules]
</system>
```

Anthropic guidance: *"Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters?"* — treating tool docstrings like docstrings for a junior developer [1].

#### Tool Schema (JSON Schema)

All three providers use JSON Schema. Minimal canonical example [5]:

```json
{
  "type": "function",
  "name": "get_weather",
  "description": "Retrieves current weather for the given location.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City and country e.g. Bogotá, Colombia"
      }
    },
    "required": ["location"],
    "additionalProperties": false
  },
  "strict": true
}
```

Anthropic uses an equivalent structure under the `tools` parameter with `input_schema` instead of `parameters` [2].

---

## Section 3 — Loop Variants Comparison

### Q4: What Are the Main Loop Variants and How Do They Compare?

Nine variants have significant research grounding and/or production adoption. The comparison table below covers the canonical dimensions.

#### Loop Variants Comparison Table

| Variant | Core Mechanic | Termination Condition | Token Cost Profile | Best For | Worst For | Production Adoption | Key Failure Mode |
|---------|--------------|----------------------|-------------------|----------|-----------|---------------------|-----------------|
| **ReAct** [4] | Interleaved Thought/Action/Observation in a single LLM stream; external tool results injected as observations; augmented action space \(\hat{A} = A \cup L\) | `Finish[answer]` action emitted, or max steps reached | **Medium** — 1 LLM call per step; grows linearly with task depth | Grounded QA, web navigation, fact lookup requiring dynamic search | Long-horizon tasks needing global planning; tasks with uninformative search spaces | LangChain `create_react_agent` (default agent), LlamaIndex ReActAgent, Amazon Bedrock Agents, Meta Engineering Agent [41] | Repetitive loop when search returns nothing useful (47% of failures) |
| **Reflexion** [14] | Trial → Evaluate → Verbal Self-Reflection → retry; reflection stored in episodic memory buffer for next trial; three-model setup (Actor M_a, Evaluator M_e, Self-Reflection M_sr) | Evaluator scores pass, or max trials (3–5) reached | **High** — full trajectory per trial × N trials; 3 model calls per trial cycle | Coding with unit test feedback, sequential decision-making, any task with clear success/fail oracle | Tasks requiring exploration/diversity; high-variance open-ended tasks | LangGraph Reflexion implementation [73], coding agent internals | Local minima trapping; cost blowup on N trials |
| **Plan-and-Execute** [15][16] | Large model plans upfront; smaller executor runs sub-tasks sequentially; replanning if needed; explicit two-phase separation | Planner decides FINISH after executor completes all steps | **Medium-Low** — planner called O(1) times; executor is cheaper per step | Long multi-step tasks with predictable sub-task structure; batch research workflows | Exploratory tasks with surprises; tasks requiring mid-plan adaptation | LangChain PlanAndExecute, BabyAGI [17], Microsoft AutoGen | Rigid plan fails on unexpected results; semantic errors persist |
| **Tree-of-Thoughts** [18] | Branching search (BFS/DFS) over multiple candidate "thought" continuations; LLM-as-evaluator prunes branches; generates \(k\) candidates per step then evaluates | BFS: depth T reached; DFS: node passes threshold or T exceeded | **Very High** — O(b^d) nodes in worst case; $0.74/case for Game of 24 vs $0.13 for IO prompt | Tasks requiring exploration, backtracking, or strategic lookahead (puzzles, planning) | Real-time applications; tasks GPT-4 solves in 1–2 steps; cost-constrained deployments | LangGraph LATS, OpenAI o1/o3 (analogous internal search) | Exponential cost; imperfect evaluator prunes valid paths |
| **CodeAct** [21] | Agent emits executable Python code; interpreter runs it; stdout/traceback fed as observation; enables multi-tool composition and control flow in a single action | Task complete signal or max turns | **Medium** — similar to ReAct but fewer turns per task (self-debugging in-loop); typically 20.7% fewer turns than JSON baseline | Complex multi-step tool composition, data analysis, software tasks | Environments without code interpreter; atomic single-API-call workflows; security-sensitive contexts | OpenHands/OpenDevin [34], SWE-bench top agents | Open-source models fail badly (13.4% vs 74.4%); sandbox escape risk |
| **Voyager** [22] | Automatic curriculum → code skill generation → iterative self-verification → skill library accumulation; skills stored as named JavaScript functions with docstrings for retrieval | Task verified by GPT-4 self-check, or max retries reached | **Very High** — multiple GPT-4 calls per task: curriculum + skill gen + verification; GPT-4 required | Open-ended lifelong learning in code-API-accessible environments; multi-episode knowledge accumulation | Non-code-API domains; single-session tasks; real-time applications | Minecraft research, skill-library pattern in software agents | Minecraft-specific; GPT-4 required; no visual perception |
| **Self-Refine** [23] | Generate → Feedback (same model) → Refine loop; single model, no external oracle; same LLM acts as generator, critic, and refiner; stop condition in feedback text | Task-specific quality signal in feedback, or max 4 iterations | **Low-Medium** — 2 extra LLM calls per iteration; typically 3–4 iterations | Open-ended generation (writing, dialogue, code style); tasks with articulable quality criteria | Math/formal reasoning; tasks model can't self-evaluate | Writing assistants, LangGraph reflection chains | Cannot detect own arithmetic errors (94% of math feedback says "looks good") |
| **Self-Consistency** [24] | Sample N independent reasoning chains with temperature > 0; majority-vote the most frequent final answer; no iteration | Fixed N samples (no iteration) | **High** — N × single inference cost (N=10–40 typically) | Closed-answer reasoning (math, QA, multiple-choice); tasks with discrete answer space | Open-ended generation; latency-sensitive; cost-sensitive | Google Brain LLMs, production RAG pipelines, coding pass@k | N×T token cost; fails on open-ended tasks; majority can be wrong |
| **AutoGPT-style** [25] | Memory + Planning + Reflection + Tools in a continuous loop; agent self-tasks indefinitely toward a high-level goal; vector store for long-term memory | Max iterations limit (user-set), cost limit, or user interrupt | **Very High** — unbounded loop; context accumulates; multiple LLM calls per iteration | Exploratory autonomous tasks with unclear endpoints; multi-day research | Well-scoped tasks with clear success criteria; production reliability | AutoGPT Platform (183k+ stars) [25], BabyAGI [17], AgentGPT | Goal drift, infinite loops, hallucinated tool calls, cost explosion |

#### Verbatim Traces

**ReAct HotpotQA Trace (from arXiv:2210.03629, Appendix C.1)** [4]:

```
Question: What is the elevation range for the area that the eastern sector of
the Colorado orogeny extends into?

Thought 1: I need to search Colorado orogeny, find the area that the eastern
sector of the Colorado orogeny extends into, then find the elevation range of
the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building
(an orogeny) in Colorado and surrounding areas.

Thought 2: It does not mention the eastern sector. So I need to look up
eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The eastern sector extends into the High Plains
and is called the Central Plains orogeny.

Thought 3: The eastern sector of Colorado orogeny extends into the High Plains.
So I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]
Observation 3: High Plains refers to one of two distinct land regions

Thought 4: I need to instead search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains. From east
to west, the High Plains rise in elevation from around 1,800 to 7,000 ft
(550 to 2,130 m).[3]

Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so
the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]
```

**Reflexion AlfWorld Example (from arXiv:2303.11366)** [14]:

```
Reflection: In this environment, my plan was to find a mug then find and use
a desklamp. However, the task says to examine the mug with the desklamp.
I should have looked for the desklamp first, then looked for the mug.
I noticed that the desklamp was found on desk 1. In the next trial, I will go
to desk 1, find the lamp, then look for the mug and examine it with the desklamp.
```

**Reflexion HotpotQA Example (from arXiv:2303.11366)** [14]:

```
Reflection: I searched the wrong title for the show, "'Allo 'Allo!", which
resulted in no results. I should have searched the show's main character,
Gordon Kaye, to find the role he was best known for in the show.
```

#### Token Cost Tier Summary

| Tier | Variants | Rough Multiple of Single ReAct Step |
|------|----------|-------------------------------------|
| Low-Medium | Self-Refine (4 iters), ReAct (short tasks) | 1–5× |
| Medium | ReAct (deep tasks), Plan-and-Execute, CodeAct | 5–20× |
| High | Self-Consistency (N=40), Reflexion (5 trials) | 20–50× |
| Very High | ToT (b=5, d=3), Voyager (full curriculum), AutoGPT (unbounded) | 50×–∞ |

---

## Section 4 — Production Implementations

### Q5: How Do Major Production Systems Implement the Agentic Loop?

The eight major production systems reviewed here span the spectrum from maximally simple (Aider: single-request-per-turn) to fully autonomous cloud agents (Devin, OpenHands).

#### Production Systems Side-by-Side Table

| System | Loop Architecture | Planning Model | Tool Model | Sub-Agents? | Termination | Published Performance |
|--------|-------------------|----------------|------------|-------------|-------------|----------------------|
| **Claude Code** [26][27] | Multi-turn interactive + headless; chain-of-thought only; auto-compaction at 95% context; MCP client+server | Informal: user-prompted Plan Mode (Shift+Tab×2); no architectural planner; "Keep it simple. Tell it to think." | Anthropic native JSON tool calls; Bash, Read/Write/Edit, Glob/Grep, Task, Browser | Yes — YAML-defined, model-selectable (`haiku`/`sonnet`/`opus`/`inherit`), fresh context per subagent, `maxTurns` limit; not parallel by default | Text response with no tool call; `maxTurns`; user Ctrl+C; auto-compact | ~80–90% of Claude Code itself written by Claude Code [26] (internal, not public) |
| **Devin** [61][62][63] | Multi-turn cloud VM; explicit plan→execute phases; 45-min runtime limit; indexing + vectorized codebase search | **Explicit interactive planning gate** — user-editable plan with 30s approval timeout; separate from execution | Shell + VS-Code-style editor + Chrome browser in sandboxed Devbox VM; Brain (cloud) + Devbox (VM) architecture | Yes (Devin-manages-Devins, March 2026) — each child gets own VM; full traces passed to children | Task completion/PR submission; 45-min limit; ACU budget | **13.86%** SWE-bench Full (March 2024, 25% sample, unverified) [61] |
| **Cursor** [36][37] | Multi-turn ReAct orchestrator; 25-tool-call-per-turn limit; parallel tool calls supported; RL-trained Composer model; planning/applying split | Plan Mode (explicit editable Markdown plan); planning model (frontier) ≠ apply model (specialized fine-tuned) | ~10 tools: read/edit file, semantic search, grep, terminal; custom speculative-edits apply model; XML tokens in RL training context | Yes — up to 8 parallel agents via Git worktree isolation | 25 tool call limit; model returns text w/ no tool call; user interrupt | Not published on SWE-bench; internal CursorBench |
| **Cline** [38][39] | Multi-turn IDE extension (VS Code/JetBrains); per-step workspace checkpoints; browser via Computer Use | **Explicit Plan/Act mode** — separate model configs for each mode; `/deep-planning` command; read-only in Plan | XML tool calls (pre-v3.35) → native JSON tool calls (v3.35+); 15% token reduction from migration; `attempt_completion` signals done | No native sub-agents | `attempt_completion` tool call; user abort; context window limit | Not published |
| **Continue** [40][41] | Multi-turn IDE extension + CLI (`cn`); three modes: Chat (no tools) / Plan (read-only) / Agent (full tools) | Chat → Plan (read-only) → Agent mode progression | Native JSON tool calling + MCP; ~10 built-in tools; policy-based auto-approval (`Automatic` skips per-step confirmation) | No native (sequential multi-instance via CLI) | Model response with no tool call; user interrupt | Not published |
| **Aider** [42][43] | **Single-request-per-turn** (not fully agentic); one LLM call per user message; auto-commit to git; no autonomous tool iteration | Informal: `/ask` mode for planning, `/code` for execution; Architect/Editor = two sequential LLM calls per turn | **No JSON tool calls** — text-based edit formats (diff, udiff, whole, editor-diff); repo map via tree-sitter; Paul Gauthier: *"LLMs write worse code if you ask them to return the code wrapped in JSON via a tool function call"* [44] | No — Architect/Editor uses two sequential LLM calls, not sub-agents | User types next message; single response per turn | SOTA SWE-bench Lite (mid-2024); **88.0%** on aider code editing benchmark (gpt-5, diff format, 2025) [43] |
| **OpenHands** [34][35] | Multi-turn event-driven; CodeAct: executable Python/Bash as primary action modality; stateless single-step model; `step()` is atomic | No explicit plan phase; LM reasons inline; Condenser for context | **Code as actions** (Python/Bash execution); Docker sandbox + Jupyter kernel + VNC browser; typed ActionEvent/ObservationEvent architecture | Yes — hierarchical multi-agent delegation with filtered tool access and risk levels (low/medium/high) | Finish action; context overflow + condensation; max iterations (100 default); user interrupt | **72%** SWE-bench Verified (Claude 4.5 + Extended Thinking, 2025) [34] |
| **SWE-agent** [32][33] | **ReAct loop** (thought→command→observation); custom Agent-Computer Interface; pure single-agent; $4/instance budget cap | No explicit plan phase — planning occurs as thought steps within ReAct | Custom ACI commands (not JSON tools): `open`, `goto`, `edit`, `search_dir`, `submit`; linter as mandatory gatekeeper (blocks invalid edits before proceeding) | No | `submit` command; 3+ malformed responses; $4 cost budget | **12.47%** SWE-bench Full (GPT-4 Turbo, 2024) [32]; >74% SWE-bench Verified (mini-SWE-agent, 100 lines, 2025) |

### Q6: What Does Claude Code Specifically Use?

Claude Code's architecture is defined by its explicit rejection of complexity. Boris Cherny [26][27]:

> *"This is the thinnest possible wrapper over the model. We literally could not build anything more minimal. This is the most minimal thing."*
> — Boris Cherny, Latent Space Podcast, May 2025

> *"Claude Code is not a product as much as it's a Unix utility."*
> — Boris Cherny, Latent Space Podcast, May 2025

> *"There's kind of three layers at which we can build something. The most natural way is to just build it into the model and have the model do the behavior. The next layer is probably scaffolding on top, so it's like Claude Code itself. And then the layer after that is using Claude Code as a tool in a broader workflow, to compose stuff in."*
> — Boris Cherny, Latent Space Podcast, May 2025

**Key architectural decisions in Claude Code:**

- **No RAG** — replaced entirely by agentic search (glob, grep, file reads). Boris Cherny: *"Agentic search just sidesteps all of that [indexing complexity]. One is it outperformed everything. By a lot."* [26]
- **No framework** — no LangGraph, no AutoGen, no LlamaIndex. Standard Anthropic API tool calls only.
- **CLAUDE.md as memory**: *"ClaudeMD, it's another example of this idea of, you know, do the simple thing first. We had all these crazy ideas about like memory architectures... But in the end, the thing we did is ship the simplest thing, which is, you know, it's a file that has some stuff. And it's auto-read into context."* [26]
- **Chain-of-thought only**: *"It's all chain of thought, actually, in Claude Code. So we don't use the think tool. Anytime that Claude Code does thinking, it's all chain of thought."* [26]
- **Context compaction at 95%**: *"We tried a bunch of different options for compacting... And then in the end, we actually just did the simplest thing, which is ask Claude to summarize the previous messages and just return that and that's it."* [26]
- **Plan mode as behavioral convention**: *"Most of Boris's sessions start in Plan mode (Shift+Tab twice). If his goal is to write a Pull Request, he uses Plan mode to go back and forth with Claude until he likes the plan. Then he switches to auto-accept edits mode and Claude can usually one-shot it."* [27]

**Sub-agent architecture** (from official docs, April 2026 — **public**) [28]:

> *"Subagents receive only the subagent's system prompt (plus basic environment details like working directory), not the full Claude Code system prompt. Subagents don't inherit skills from the parent conversation."*

Sub-agents are configured via YAML frontmatter with fields including `tools`, `model`, `maxTurns`, `permissionMode`, `isolation`, `memory`, and `background`. The key practical constraint: **sub-agents start fresh with only their defined system prompt** — they do not inherit the parent conversation's context, tool call history, or accumulated findings.

**Critical note from Cognition on Claude Code's sub-agent model** [62]:

> *"Claude Code is an example of an agent that spawns subtasks. However, it never does work in parallel with the subtask agent... The subtask agent lacks context from the main agent that would otherwise be needed to do anything beyond answering a well-defined question."*
> — Walden Yan, Cognition, "Don't Build Multi-Agents," June 2025

### Q7: What Are the Critical Differences Between Production Systems?

**Three architectural dimensions differentiate the systems:**

1. **Planning architecture**: Devin and Cursor implement explicit planning gates (separate plan phase with human approval window); Claude Code and SWE-agent treat planning as behavioral (embedded in ReAct thought steps).

2. **Tool invocation model**: OpenHands uses code execution as the primary action space (CodeAct); SWE-agent uses a custom purpose-built ACI; Claude Code, Cline, and Continue use native API tool calls; Aider uses text-based edit formats to avoid JSON tool calls entirely.

3. **Context management**: Claude Code uses agentic search (replacing RAG) + CLAUDE.md; Cursor uses codebase indexing with embeddings; Aider uses tree-sitter-based repo maps; OpenHands uses a stateless event-driven architecture with a Condenser.

**On SWE-bench scores and benchmark saturation** [109]:

The SWE-EVO paper (2025) documents a stark reality:
> *"Experiments reveal a striking capability gap: GPT-5.4 with OpenHands achieves only 25% on SWE-EVO versus 72.80% on SWE-Bench Verified, showing that current agents struggle with sustained, multi-file reasoning."*

SWE-bench-Live scores (novel, post-cutoff issues) show both OpenHands and SWE-agent solving only ~18–20% of tasks — a significant gap below curated benchmark scores. **Jetix should not use SWE-bench scores as a guide for selecting agents for its own workflows.**

---

## Section 5 — Termination, Patterns, Anti-Patterns

### Q8: How Should Loops Terminate?

Production systems use **layered stopping mechanisms** because no single condition reliably handles every failure mode [84]. Eight canonical mechanisms:

#### 1. Max Iterations (Hard Cap)

- **LangGraph**: `recursion_limit` (default 25 super-steps); raises `GraphRecursionError` [78]
- **OpenAI Agents SDK**: `max_turns` on all runner methods; raises `MaxTurnsExceeded` [6]
- **SWE-agent**: `turn_limit` + `per_instance_cost_limit` ($3.00 default) [33]
- **Claude Code sub-agents**: `maxTurns` field in YAML frontmatter [28]

**Known failure**: Hard caps truncate mid-action. A cap set too low causes spurious failures; too high allows cost accumulation.

#### 2. Token Budget

Anthropic's Task Budgets API (public beta, `task-budgets-2026-03-13` header): configured via `output_config.task_budget = {"type": "tokens", "total": N, "remaining": M}`. The API injects a countdown marker server-side; Claude sees remaining tokens and self-regulates [85].

> *"Task budgets let you tell Claude how many tokens it has for a full agentic loop, including thinking, tool calls, tool results, and output. The model sees a running countdown and uses it to prioritize work and finish gracefully as the budget is consumed."* [85]

**Critical finding (2026 research)**: When Claude approaches token budget exhaustion, it has an internal "desperate" activation pattern that fires, causing silent quality degradation 20–44% of the time with no linguistic warning [86]. The practical implication: *"If you need to constrain output length, tell Claude ('keep this under 400 words') rather than setting max_tokens=400. Framing gets absorbed into planning. Caps cause truncation and silent failure."* [86]

#### 3. Convergence Detection

LangGraph's native termination: nodes with no incoming messages vote to halt; graph execution terminates when all nodes are inactive [78]. Tool call deduplication via system prompt injection: *"It is forbidden to re-run a tool for the same request once you have its output"* prevents the n8n-documented case of identical tool calls 10+ times [84].

#### 4. LLM Self-Declared Completion

Claude: `stop_reason: "end_turn"` with no `tool_use` blocks [2]. OpenAI Agents SDK: LLM produces `final_output` with no pending tool calls [6].

**Critical failure mode — the "Ralph Wiggum" problem** [84]:

> *"The agent tends to eliminate obvious unused functions, tidy up a few imports, and update some call sites, then declares the job finished. However, upon reviewing the changes, you may find outdated helpers without any callers, CI configurations still referencing old test names, or branches that continue to import deleted modules."* [84]

The root cause: agents pattern-match to what *looks* like a reasonable stopping point — 80% complete looks like 100% from the inside. The fix: specifying completion as an external, machine-readable predicate, not an internal judgment [84].

#### 5. External Judge / Verifier

Reflexion's evaluator model (M_e) [14]; MetaGPT's executable feedback mechanism (+5.4% MBPP improvement via code execution pass/fail) [93]; Agent-as-a-Judge framework (arXiv:2410.10934) which *"dramatically outperforms LLM-as-a-Judge and is as reliable as our human evaluation baseline"* [98].

#### 6. Timeout

Wall-clock timer. AWS Lambda: 15-minute hard process-kill. AgencyBench (2026) reports execution averaging 0.3–1.4 hours per complex task [101]. GPT-5.2 required 3.4M tokens and 0.6 hours per task on complex benchmarks [101].

#### 7. Budget-Aware Stop (Cost Ceiling)

SWE-agent's `per_instance_cost_limit` ($3.00 default) is the canonical implementation. The "Token Snowball" effect (SWE-Effi, 2025): failed SWE-agent runs use 8.8M tokens vs. 1.8M for successful runs on the same task — a 4.9× cost premium for failure [87].

#### 8. Human-in-the-Loop Confirmation

LangGraph's `interrupt()` function pauses graph execution at any node, saves state to checkpointer, waits indefinitely for `Command(resume=...)` [82].

Simon Willison (2025 Year in LLMs): *"The default setting for most coding agents is to ask the user for confirmation for almost every action they take."* [88]

Harrison Chase (LangChain): *"Harness and context engineering are as important as model quality."* [83]

**Anthropic's `pause_after_compaction`**: Setting `pause_after_compaction: true` causes the API to return `stop_reason: "compaction"` after summarization, allowing the orchestrator to inspect and modify context before continuing [85].

#### Stop Conditions by Provider

| Provider | Normal Termination | Safety Termination |
|---|---|---|
| **Anthropic** | `stop_reason == "end_turn"` with no `tool_use` blocks | `max_tokens` exceeded; explicit stop sequences |
| **OpenAI Agents SDK** | LLM produces `final_output` (text + no tool calls) | `max_turns` exceeded → `MaxTurnsExceeded` |
| **LangGraph** | Agent returns no tool calls; no node has new work | `recursion_limit` → `GraphRecursionError` |
| **Gemini** | Model returns text without `functionCall` parts | Context window exceeded; application-level iteration limit |

### Q9: What Are the Common Patterns?

**Parallel Tool Calls**: Claude may issue multiple `tool_use` blocks in a single response. Anthropic's production finding from their multi-agent research system: *"For speed, we introduced two kinds of parallelization: (1) the lead agent spins up 3–5 subagents in parallel rather than serially; (2) the subagents use 3+ tools in parallel. These changes cut research time by up to 90% for complex queries."* [3]

**Sub-Agent Spawning**: Claude Code's Task tool creates a fresh sub-context for isolated work. From Anthropic's multi-agent system: *"Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."* [3]

**Memory Writeback**: LangGraph Checkpointer saves full graph state after every super-step, enabling fault-tolerant resumption. CrewAI checkpoints state to JSON after each task. Anthropic's system: *"The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated."* [3]

**Deferred Tool Discovery (MCP)**: Dynamic tool loading reduces context from ~77K tokens (static) to ~8.7K tokens (intent-based loading) — an 88.7% reduction [90].

**Context Compaction Mid-Loop**: Claude Code auto-compacts at ~95% context capacity. SWE-bench measurement: compression scheduled every 10–15 tool calls achieved 22.7% token savings while matching baseline accuracy. However, aggressive ongoing summarization increased average turns from 4.0 to 14.0, with only 14% net token saving — compaction can increase iterations if used indiscriminately [89].

### Q10: What Are the Major Anti-Patterns?

#### 1. Tool-Call Storms

Named case — Anthropic's early multi-agent system [3]:

> *"Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates."*

Named case — n8n repetitive tool call: an agent calling the same vector search tool with identical parameters **10 times** in a row [84]. Fix: injecting a "Single Execution Rule" into the system prompt.

Quantified: enterprise teams report cost overruns averaging 340% above initial estimates from infinite retry loops with no backoff logic [84].

#### 2. Hallucinated Tool Arguments

Five categories of tool hallucination: non-existent function invocation, semantically inappropriate tool selection, invalid parameters, missing required arguments, and tool bypass (agent simulates the tool's behavior internally) [84].

The paradox of better reasoning: *"Improving an agent's reasoning capabilities can actually increase tool hallucination rates. Stronger reasoning lets the model construct more elaborate plans, which creates more opportunities for it to need tools that don't exist."* Reasoning-focused models like o3 and o4-mini have pushed hallucination rates to 33% and 48% on certain benchmarks [84].

#### 3. Context Exhaustion

The triangular series trap: naive loops accumulate context as a triangular number series. A 20-step loop with 1,000 tokens/step produces **210,000 cumulative input tokens** rather than the 20,000 a per-step estimate suggests — a 10.5× overrun [89]. SWE-bench data: 30,400 of 48,400 total tokens came from tool results alone, and 39.9–59.7% of those tokens were removable with no performance loss [89].

Symptom: *"After 30–50 messages, agents forget earlier conversation and contradict themselves. I watched an agent recommend a solution in message 12, then flag that exact solution as a risk in message 40."* [84]

#### 4. Doom Loops / Infinite Self-Reflection

Reflexion paper (arXiv:2303.11366): *"after only four trials, we terminate the runs as the agent does not show signs of improvement"* [14] — without a trial cap, an agent that always finds marginal improvement will stall.

2026 Goal Drift paper (arXiv:2603.03258): *"Both Qwen3-235B and Claude-Sonnet-4.5 (standard) consistently fail to recognize the new goal, either not aware of the fact that system prompt has changed, or making an intentional choice to abandon the system goal given the prior context."* Only GPT-5.1 maintained consistent resilience in 32-step experiments [103].

Quantified trigger: *"Goal drift shows up most in tasks above 300 lines."* [84]

#### 5. Premature Completion

The "Ralph Wiggum" pattern: agents declare completion before the work is actually done. Named after the plugin created to fix this in Claude Code's marketplace [84]. Root cause architectural, not prompt-based: *"No prompt can enable the agent to validate its own fuzzy work. This issue is rooted in the architecture of the system rather than the language used."* [84]

#### 6. Rabbit Holes

Named case — Devin (Answer.AI post-mortem, January 2025) [84]:

> *"When asked to deploy multiple applications to a single Railway deployment (something that Railway doesn't support), instead of identifying this limitation, Devin spent over a day attempting various approaches and hallucinating features that didn't exist. The most frustrating aspect wasn't the failures themselves — all tools have limitations — but rather how much time we spent trying to salvage these attempts."*

---

## Section 6 — Economics & Research Frontier

### Q11: What Are the Cost Dynamics of Agentic Loops?

#### The Anthropic 15× Token Claim — Verbatim

From "How we built our multi-agent research system" (Anthropic Engineering Blog, June 13, 2025) [3]:

> *"There is a downside: in practice, these architectures burn through tokens fast. In our data, agents typically use about **4× more tokens** than chat interactions, and **multi-agent systems use about 15× more tokens than chats**. For economic viability, multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance."*

Additional quantitative findings from the same post [3]:
- Multi-agent Claude Opus 4 (lead) + Claude Sonnet 4 (subagents) outperformed single-agent Claude Opus 4 by **90.2%** on Anthropic's internal research eval
- Token usage alone explains **80%** of performance variance on BrowseComp
- Parallel execution **cut research time by up to 90%** for complex queries
- Tool description improvement led to **40% decrease in task completion time**
- Upgrading from Claude Sonnet 3.7 to Claude Sonnet 4 was a *larger performance gain than doubling the token budget*

#### Cost Dynamics Table

| Model / Configuration | SWE-bench Verified | GAIA Score | GAIA Cost (165 Qs) | Notes |
|---|---|---|---|---|
| Claude Opus 4.7 | 82.0% | — | — | [vals.ai leaderboard] [88] |
| Claude 4 Sonnet | 77.2% | — | — | [88] |
| GPT-5 | 74.9% | — | — | As of Oct 2025 |
| Gemini 2.5 Pro | 71.8% | — | — | As of Oct 2025 |
| Claude Sonnet 4.5 | — | 74.55% | $178.20 | HAL GAIA, Sep 2025 [87] |
| Claude Opus 4.1 High | — | 68.48% | $562.24 | HAL GAIA, Aug 2025 [87] |
| Claude Opus 4 High | — | 64.85% | $665.89 | HAL GAIA, May 2025 [87] |
| Claude 3.7 Sonnet High | — | 64.24% | $122.49 | HAL GAIA, Feb 2025 [87] |
| GPT-5 Medium | — | 59.39% | $104.75 | HAL GAIA, Aug 2025 [87] |
| o4-mini Low | — | 58.18% | $73.26 | Pareto-optimal [87] |
| DeepSeek R1 | — | 30.30% | $73.19 | HAL GAIA, Jan 2025 [87] |

*Note: Claude Opus 4 High at $665.89 is 9× more expensive than o4-mini at $73.26 for comparable or lower GAIA performance. Claude Sonnet 4.5 at $178.20 achieves 74.55% — the best cost-adjusted outcome for Jetix's consultancy tasks. [87]*

#### How Cost Scales with Loop Depth

**Linear accumulation (ideal)**: Each iteration adds a fixed new context block. Total cost = O(N).

**Quadratic accumulation (naive full-history)**: Total input tokens follow a triangular series: `N×S + u×N(N+1)/2 + r×N(N-1)/2`, where S = system prompt size, u = new tokens per iteration, r = output tokens per iteration. At N=20 iterations with u=1,000 tokens/step: **210,000 cumulative input tokens vs. 20,000 naively expected** — a 10.5× overrun [89].

**Concrete example** (sequential 10-step agent on Claude Sonnet pricing $3.00/$15.00 per 1M tokens) [89]:
- Naive full-context: 472,500 input tokens → **$1.49**
- Constrained (2-step window): 260,000 input tokens → **$0.86** (42% saving)
- Single-pass: 9,000 tokens → **$0.03**

**Reliability tax**: A sequential chain with 95% per-step reliability achieves only **60% end-to-end reliability** over 10 steps (0.95^10 = 0.598). Retries multiply token costs ~40% beyond the deterministic case [89].

**Multi-agent chain cost (AutoGen pattern)** [93]: In a 3-agent chain, total cost ≈ 3× single-agent cost per round, scaling as O(k × N) for k agents and N rounds. AutoGen's experiments show 8% (GPT-4) to 35% (GPT-3.5-turbo) F1 improvement for multi-agent coding vs. single-agent — the value-per-cost tradeoff benchmark.

### Q12: What Does the Research Frontier Show?

Key 2024–2026 papers with direct relevance to Jetix:

**SWE-Effi (arXiv:2509.09853, 2025)** [87]: Introduces EuTB (Effectiveness under Token Budget) and EuCB (Effectiveness under Cost Budget) metrics. Key finding: failed attempts average **4× more tokens** than successful ones. SWE-agent + GPT-4o-mini achieves 10% resolution at 8.1M tokens per attempt vs. SWE-agent + Qwen3-32B at 28% resolution with 440k tokens — an **18× token cost differential for worse performance**.

**Efficient Agents (arXiv:2508.02694, 2025)** [102]: First systematic study of efficiency-effectiveness tradeoff. "Efficient Agents" retains **96.7% of OWL's GAIA performance while reducing costs from $0.398 to $0.228 per task** — a 28.4% improvement in cost-of-pass.

**Agent Workflow Memory / AWM (arXiv:2409.07429, ICML 2025)** [99]: +51.1% relative success rate on WebArena vs. top autonomous method; +24.6% on Mind2Web by inducing reusable task workflows from past agent trajectories. Direct relevance to Jetix: workflows induced from successful consultancy task trajectories can be stored and retrieved to reduce per-task iteration count.

**τ-bench (arXiv:2406.12045, 2024)** [100]: Introduces `pass^k` metric measuring agent reliability over multiple trials. Key finding: *"Even state-of-the-art function calling agents (like gpt-4o) succeed on <50% of tasks, and are quite inconsistent (pass^8 <25% in retail)"*. Production deployment requires far higher per-trial success rates than single-run evaluation shows.

**Inherited Goal Drift (arXiv:2603.03258, 2026)** [103]: Claude-Sonnet-4.5 (standard) *"consistently fails to recognize goal switches"* in 32-step experiments. Only thinking variants and GPT-5.1 show resilience. Implication: Jetix's long-horizon agents should use extended thinking mode for complex workflows.

**Magentic-One (arXiv:2411.04468, 2024)** [96]: Dual-loop orchestrator-worker achieves competitive GAIA/WebArena performance. Key innovation: **stall detection** — the Orchestrator counts "stuck" iterations and resets strategy when stall counter exceeds threshold, preventing doom loops architecturally.

---

## Section 7 — Multi-Agent Loops & Best Practices

### Q13: How Do Multi-Agent Systems Differ from Single-Agent Loops?

The key structural differences [112]:

| Dimension | Single-agent | Multi-agent |
|-----------|-------------|-------------|
| Context window | One, shared with all history | Separate per agent; information must be deliberately passed |
| Parallelism | Sequential by default | Agents can work concurrently |
| Specialization | One generalist | Role-specific prompts/tools per agent |
| Coordination cost | None | Message-passing overhead; routing decisions; conflict resolution |
| Token cost | Baseline | Typically 4–15× higher (Anthropic: ~15× vs. chat) |
| Error propagation | Isolated to one trajectory | Errors in one agent can cascade across the ensemble |
| Termination | Orchestrator or single condition | Requires consensus or authoritative orchestrator |

### Q14: What Are the Major Multi-Agent Coordination Frameworks?

#### Multi-Agent Frameworks Comparison Table

| Framework | Coordination Pattern | Communication Channel | Conflict Resolution | Memory Model | Termination |
|-----------|---------------------|----------------------|--------------------|-------------|-------------|
| **AutoGen v0.2** [93] | GroupChat round-robin / LLM-selected speaker | Shared conversation transcript (blackboard) | Manager LLM selects next speaker; conversational negotiation | Shared message history | Keyword / max-turns / human proxy |
| **AutoGen v0.4** [104] | Actor model; asynchronous message-passing | Per-actor typed message queues | Actor responds to contradictions conversationally; no merge | Per-actor private state + explicit message passing | Event-driven; runtime termination signal |
| **CrewAI** [105] | Sequential pipeline or hierarchical orchestrator-worker | Task output passed as context to next agent | Manager agent validates and may request revision | Short/long-term/entity memory + crew-level knowledge; JSON checkpoints | Last task completion |
| **MetaGPT** [94] | SOP-driven assembly line; role specialization | Shared message pool (global blackboard) | Structured typed artifacts prevent semantic conflict | Global message pool; role-scoped SOP prompts | QA stage produces passing tests |
| **Magentic-One** [96] | Orchestrator-led with 4 specialist agents | Natural-language instructions to specialists; full transcript visible to Orchestrator | Two-ledger stall detection + reflection/replan cycle | Task ledger (plan) + progress ledger (working memory) | Orchestrator determines completion or max-attempt limit |
| **Anthropic Research System** [3] | Lead agent + parallel subagents | Task specs downward; summarized results upward; filesystem for artifacts | Lead agent arbitrates; subagents don't coordinate with each other | Separate context windows per agent; external memory for long-horizon | Lead agent synthesizes all subagent results; currently synchronous |
| **OpenAI Swarm / Agents SDK** [106][107] | Handoff-based peer routing | Conversation history passed through handoff chain | Last agent in handoff chain has final authority; input filters prune history | Conversation history (filterable via `input_filter`) | No active agent issues further handoffs or function calls |
| **LangGraph** [79] | Graph-based: network, supervisor, hierarchical, custom | Shared state channel (message list) or private scratchpad | Supervisor LLM routes; deterministic edges override | Shared scratchpad OR private scratchpad + final result | `END` node reached in graph |

#### AutoGen — The Actor Model Redesign (v0.4)

Gagan Bansal (Microsoft Research) on the v0.4 redesign [104]:

> *"In early 2024, we used these learnings to experiment with alternate architectures, and we ended up adopting an actor model for multi-agent orchestration. The actor model is a well-known programming model for concurrent programming and high-use systems. Here, actors are the computational building blocks that can exchange messages and also perform work."*

#### MetaGPT — The SOP Architecture

MetaGPT's central abstraction — the shared message pool and assembly line — from arXiv:2308.00352 [94]:

> *"MetaGPT encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows, thus allowing agents with human-like domain expertise to verify intermediate results and reduce errors. MetaGPT utilizes an **assembly line paradigm** to assign diverse roles to various agents, efficiently breaking down complex tasks into subtasks involving many agents working together."*

The shared message pool: *"Every agent monitors the environment (i.e., the message pool in MetaGPT) to spot important observations (e.g., messages from other agents). Every agent not only publishes their structured messages in the pool but also accesses messages from other entities transparently."* [94]

#### Magentic-One — The Dual-Loop Architecture

The Orchestrator's two-loop design from arXiv:2411.04468 [96]:

> *"The Orchestrator performs several functions to guide progress towards accomplishing a high-level goal: it formulates a plan, maintains structured working memory of progress, directs tasks to other agents, restarts and resets upon stalling, and determines task completion."*

> *"The workflow contains two loops: the outer loop maintains the task ledger, which contains the overall plan, while the inner loop maintains the progress ledger, which directs and evaluates the individual steps that contain instructions to the specialized agents."*

The stall detection mechanism [96]:

> *"The Orchestrator also maintains a counter for how long the team has been stuck or stalled. If a loop is detected, or there is a lack of forward progress, the counter is incremented. As long as this counter remains below a threshold (≤ 2 in our experiments), the Orchestrator initiates the next team action... However, if the counter exceeds the threshold, the Orchestrator breaks from the inner loop, and proceeds with another iteration of the outer loop. This includes initiating a reflection and self-refinement step, where it identifies what may have gone wrong, what new information it learned along the way, and what it might do differently on the next iteration of the outer loop."*

#### Cognition's "Don't Build Multi-Agents" Position

Walden Yan (co-founder/CPO, Cognition) published this post on June 12, 2025 — the most cited production critique of multi-agent architectures [62]:

> *"Libraries such as OpenAI/swarm and Microsoft/autogen actively push concepts which I believe to be the wrong way of building agents. Namely, using multi-agent architectures."*

> *"Most real-world tasks have many layers of nuance that all have the potential to be miscommunicated."*

**Principle 1:** *"Share context, and share full agent traces, not just individual messages."*

**Principle 2:** *"Actions carry implicit decisions, and conflicting decisions carry bad results."*

> *"While I'm optimistic about the long-term possibilities of agents collaborating with one another, it is evident that in 2025, running multiple agents in collaboration only results in fragile systems. The decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough between the agents."*

> *"The simplest way to follow the principles is to just use a single-threaded linear agent."*

> *"At the moment, I don't see anyone putting a dedicated effort to solving this difficult cross-agent context-passing problem. I personally think it will come for free as we make our single-threaded agents even better at communicating with humans."*

**The self-contradiction**: In March 2026, Cognition launched "Devin can now Manage Devins" [63]:

> *"Starting today, Devin can break down large tasks and delegate them to a team of managed Devins that work in parallel. Each managed Devin is a full Devin, running in its own isolated virtual machine with its own terminal, browser, and development environment."*

The reconciliation: the new system passes **full context/trajectories** to child sessions (consistent with Principle 1) and gives children isolated focus. This is arguably consistent with Walden's principles but challenges his 2025 conclusion about fragility.

### Q15: What Are Anthropic's Best Practices for Claude-Based Multi-Agent Systems?

Anthropic's "Building Effective Agents" (Dec 2024) [1] defines six patterns and three core principles:

**Three Core Principles:**

> *"When implementing agents, we try to follow three core principles: 1. Maintain **simplicity** in your agent's design. 2. Prioritize **transparency** by explicitly showing the agent's planning steps. 3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**."*

**Overarching Philosophy:**

> *"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."*

> *"We recommend finding the simplest solution possible, and only increasing complexity when needed... you should consider adding complexity only when it demonstrably improves outcomes."*

**The Five Workflow Patterns + One Agent Pattern** [1]:

1. **Prompt Chaining**: *"Decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one... ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks."*

2. **Routing**: *"Classifies an input and directs it to a specialized followup task... works well for complex tasks where there are distinct categories that are better handled separately."*

3. **Parallelization** (Sectioning + Voting): *"LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically... effective when the divided subtasks can be parallelized for speed."*

4. **Orchestrator-workers**: *"A central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results... well-suited for complex tasks where you can't predict the subtasks needed."*

5. **Evaluator-optimizer**: *"One LLM call generates a response while another provides evaluation and feedback in a loop... particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value."*

6. **Agents**: *"Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path."*

**Eight Principles from the June 2025 Multi-Agent Research System Post** [3]:

- **Think like your agents**: Build simulations to watch agents work step-by-step before deploying
- **Teach the orchestrator how to delegate**: Each subagent needs an objective, output format, tool guidance, and clear task boundaries
- **Scale effort to query complexity**: Simple fact-finding: 1 agent, 3-10 tool calls; open-ended research: 10+ subagents
- **Tool design is critical**: *"Agent-tool interfaces are as critical as human-computer interfaces"*
- **Let agents improve themselves**: Claude 4 models can diagnose prompt failures and suggest improvements; tool-testing agent rewrote tool descriptions resulting in **40% decrease in task completion time**
- **Start wide, then narrow**: Expert human research pattern: explore landscape before drilling into specifics
- **Guide the thinking process**: Extended thinking as a controllable scratchpad for the lead agent
- **Parallel tool calling transforms speed**: 3–5 parallel subagents + 3+ parallel tools per subagent → up to **90% reduction in research time**

---

## Specific Production Examples

- **Claude Code** (https://docs.anthropic.com/en/docs/claude-code/overview) — Anthropic's terminal-based agentic coding assistant; the canonical "thinnest wrapper" ReAct loop with CLAUDE.md memory and agentic search; ~80–90% of its own code written by itself [26][28]

- **Devin** (https://cognition.ai) — Cloud-hosted VM-based software engineering agent with explicit planning gate; first agent to publicly claim ~14% SWE-bench; controversial benchmark methodology; published "Don't Build Multi-Agents" then launched multi-Devin orchestration [61][62][63]

- **OpenHands** (https://github.com/All-Hands-AI/OpenHands) — Open-source CodeAct agent; 72% SWE-bench Verified with Claude 4.5 Extended Thinking; stateless event-driven architecture with Docker sandbox and Jupyter kernel; broadest benchmark coverage of any reviewed system [34]

- **SWE-agent** (https://swe-agent.com) — Princeton research agent; defines the Agent-Computer Interface (ACI) concept; demonstrates that architecture design matters more than complexity (mini-SWE-agent: 100 lines of Python, >74% SWE-bench Verified) [32][33]

- **Cursor** (https://cursor.com) — IDE built on top of VS Code; RL-trained Composer model; dedicated apply model for 13× faster file editing via speculative decoding; 8 parallel agents via Git worktree isolation; explicit Plan Mode [36][37]

- **Magentic-One** (https://aka.ms/magentic-one) — Microsoft Research; dual-loop orchestrator with four specialized agents; implements stall detection and outer-loop re-planning as a doom-loop prevention mechanism; statistically competitive with SOTA on GAIA without task-specific tuning [96]

- **Anthropic Multi-agent Research System** (https://www.anthropic.com/engineering/built-multi-agent-research-system) — Anthropic's internal research assistant; orchestrator-worker with 3–5 parallel subagents; 90.2% improvement over single-agent Opus 4; the source of the published 15× token cost figure; uses extended thinking as a controllable scratchpad [3]

- **AutoGen** (https://github.com/microsoft/autogen) — Microsoft Research's multi-agent conversation framework; v0.4 adopted actor model for asynchronous coordination; GroupChat pattern with LLM-selected speakers; 8–35% F1 improvement on coding tasks vs. single-agent [93][104]

---

## Critical Assessment

### ReAct

**Pros (evidence-backed)**:
- Significantly reduces hallucination vs. CoT-only: 0% hallucination rate on HotpotQA vs. 56% for CoT [4]
- Strong on interactive, grounded decision-making: ALFWorld +34pp vs. RL baselines [4]
- Works with only 1–2 in-context examples; highly sample-efficient
- Human-interpretable trajectories; the standard for debugging and auditing
- Production-validated at scale: LangChain default, Amazon Bedrock, Meta Engineering Agent [4][41]

**Cons + failure modes (evidence-backed)**:
- **Verbosity**: *"ReAct Agents require an LLM call for each tool invocation... the LLM only plans for 1 sub-problem at a time, which may lead to sub-optimal trajectories."* — Harrison Chase, LangChain blog [16]
- **Repetitive loop**: When search returns non-informative results, the model issues near-identical queries (47% of failures in HotpotQA paper [4])
- No long-horizon memory: context window fills; no mechanism to compress or externalize between steps

**When to use**: General-purpose tool-using agents with moderate task depth (<15 steps), grounded QA, fact lookup, any task where interpretability matters. The default for Jetix agents.

**When to avoid**: Tasks requiring global planning or lookahead across many steps; tasks where the search space is known to be uninformative.

---

### Reflexion

**Pros (evidence-backed)**:
- 91% Pass@1 on HumanEval, surpassing GPT-4's 80.1% baseline [14]
- 130/134 AlfWorld tasks completed vs. ~108 for plain ReAct (+22%) [14]
- No weight updates — improves at test time via prompting only

**Cons + failure modes (evidence-backed)**:
- *"Reflexion is an optimization technique... it may still succumb to non-optimal local minima solutions... after only four trials, we terminate the runs as the agent does not show signs of improvement."* — Shinn et al. [14]
- *"Reflexion struggles to overcome local minima choices that require extremely creative behavior to escape... Reflexion is unable to solve tasks that require a significant amount of diversity and exploration."* [14]
- Token cost blowup: each trial runs a full trajectory + reflection; K trials multiplies cost by K
- MBPP false positive rate 16.3% vs HumanEval 1.4% — reflection can reinforce wrong fixes [14]
- *"Reflexion is effective in sequential decision-making... [but] Reflexion requires multiple LLM calls and trajectories, making it significantly more expensive than single-pass methods."* [74]

**When to use**: Coding tasks with unit tests, any task with a clear pass/fail oracle (data validation, form filling with schema checks), game-playing with a score function.

**When to avoid**: Creative tasks requiring diverse exploration; tasks where the success signal is ambiguous; cost-constrained workflows.

---

### Plan-and-Execute

**Pros (evidence-backed)**:
- Lower cost per tool step: executor can be a smaller model; planner called O(1) vs. O(N) for ReAct
- LLMCompiler variant achieves **3.6× speed boost** vs. sequential ReAct [16]
- Better task completion for multi-step tasks with predictable structure

**Cons + failure modes (evidence-backed)**:
- *"Plan-and-Execute is restricted by serial tool calling and uses an LLM for each task since it doesn't support variable assignment."* — LangChain blog [16]
- *"PS prompting addresses calculation errors and missing-reasoning-step errors, but semantic misunderstanding errors still remain."* — Wang et al. [15]
- Rigid plans fail on surprises; re-planning requires another expensive planner call

**When to use**: Research pipelines, report generation, multi-step data workflows with predictable structure, batch processing tasks.

**When to avoid**: Exploratory tasks where sub-task results are highly unpredictable; real-time tasks requiring immediate adaptation.

---

### Tree-of-Thoughts

**Pros (evidence-backed)**:
- 74% success on Game of 24 vs. 4% for CoT — an 18.5× improvement using GPT-4 [18]
- Enables backtracking — recovers from dead ends that linear methods cannot
- Significantly outperforms all sampling-based baselines on tasks requiring exploration

**Cons + failure modes (evidence-backed)**:
- *"Computational cost: naïve ToT search scales exponentially in depth d... Effectiveness on small models is limited; at low parameter counts ToT may offer less or even negative return."* [75]
- *"Only explores three relatively simple tasks that challenge GPT-4... Requires more resources (e.g. GPT-4 API cost) than sampling methods."* — Yao et al. [18]
- *"The expected number of mainline nodes at depth d scales like (ak)^d — exponential in depth."* — Lateral ToT paper [76]

**When to use**: Tasks with combinatorial structure requiring backtracking; strategic planning with lookahead; puzzles.

**When to avoid**: Production deployments with latency SLAs; cost-sensitive workflows; tasks where GPT-4/Claude Opus is not available.

---

### CodeAct

**Pros (evidence-backed)**:
- *"CodeAct outperforms widely used alternatives (up to 20% higher success rate)"* — Wang et al. [21]
- *"the best model gpt-4-1106-preview achieves a 20.7% absolute improvement compared to the next best action format (text)"* [21]
- Enables multi-tool composition in a single action (impossible with JSON one-tool-at-a-time)
- Self-debugging via traceback observation reduces error recovery turns

**Cons + failure modes (evidence-backed)**:
- *"there is still a significant gap in terms of absolute CodeAct performance between open- and closed-source LLMs as the best open-source model achieving 13.4% while the best closed-source model gpt-4-1106-preview [achieves] 74.4%."* — Wang et al. [21]
- *"CodeActAgent may suffer from hallucination... e.g., imagine the content of a variable without actually printing it out"* [21]
- *"CodeAct directly grants access for the agent to freely execute code in a sandbox environment... such an agent may potentially break free of the sandbox restriction"* [21]

**When to use**: Data analysis, software engineering tasks, multi-tool composition in a code-API environment.

**When to avoid**: Security-sensitive environments without sandboxing; atomic single-API-call workflows.

---

### AutoGPT-Style

**Pros (evidence-backed)**:
- Demonstrated that GPT-4 can autonomously complete multi-step tasks without step-by-step guidance (historical)
- Long-term memory via vector store enables context beyond a single prompt window

**Cons + failure modes (evidence-backed)**:
- *"It looks amazing on first glance, but then completely fails because it creates elaborate plans that are completely unnecessary."* — Taivo Pungas [77]
- *"AutoGPT is known for significant limitations, including a tendency to get stuck in loops, hallucinate information, and incur high operational costs due to its reliance on paid APIs."* — Wikipedia [25]
- Goal drift, infinite loops, hallucinated tool calls: the three failure modes that defined 2023 agent deployments
- *"The real work is the other 7 steps: workflows, routing, memory, tools, retries, logging, evaluation. You're not 'prompting a model.' You're engineering a system."* [25]

**When to use**: Exploratory research prototypes where cost is not a constraint and endpoints are undefined.

**When to avoid**: Any production deployment requiring reliability, cost accountability, or predictable behavior.

---

## Comparison to Anthropic Ecosystem

### How Each Loop Variant Maps to Claude Code / Claude API / Claude Agent SDK

| Variant | Claude Code Support | Claude API Support | Claude Agent SDK | External Scaffolding Needed |
|---------|--------------------|--------------------|-----------------|----------------------------|
| **ReAct** | ✅ Native (default loop) | ✅ Native (tool_use/tool_result cycle) | ✅ Native | None — this is the baseline |
| **Reflexion** | ⚠️ Manual (trial-restart pattern, explicit reflection prompt) | ⚠️ Manual | ⚠️ Manual | LangGraph Reflexion node, or custom trial loop |
| **Plan-and-Execute** | ⚠️ Partial (Plan Mode + separate execution session) | ⚠️ Manual (two-call pattern: planner prompt then executor prompt) | ⚠️ Manual | None strictly required; LangChain PlanAndExecute for convenience |
| **Tree-of-Thoughts** | ❌ Not native | ❌ Not native | ❌ Not native | LangGraph LATS required; expensive |
| **CodeAct** | ✅ Native (Bash tool is code execution) | ✅ Native (Bash/code_execution tools) | ✅ Native | None — Claude's Bash tool implements CodeAct semantics |
| **Voyager / Skill Library** | ⚠️ Partial (CLAUDE.md as static skill store) | ⚠️ Manual | ⚠️ Manual | Custom skill library with embedding retrieval |
| **Self-Refine** | ⚠️ Manual (Evaluator-optimizer workflow pattern from Anthropic) | ⚠️ Manual (two-agent evaluator-optimizer pattern) | ⚠️ Manual | None — two-prompt pattern with feedback loop |
| **Self-Consistency** | ❌ Not native | ⚠️ Manual (N parallel requests + majority vote) | ⚠️ Manual | Custom orchestration for N parallel calls |
| **AutoGPT-style** | ⚠️ Available but not recommended (Claude Code's max_turns as guardrail) | ⚠️ Manual | ⚠️ Manual | Requires explicit stopping logic |

**Key Anthropic-native features Jetix should leverage**:

1. **Sub-agents via Task tool** (Claude Code): Isolated context, configurable `maxTurns`, model selection per task. Best for: parallel research tasks, code review in isolation, well-scoped subtasks [28].

2. **Extended thinking as scratchpad**: Anthropic's multi-agent research system uses this as a *"controllable scratchpad"* for the lead agent to plan its approach [3]. Enable for complex planning-heavy agents.

3. **Context compaction API** (`compact_20260112`): Default trigger at 150,000 input tokens; supports `pause_after_compaction` for orchestrator inspection [85].

4. **Task Budgets API** (`task-budgets-2026-03-13`): Token-based soft limit with model-visible countdown; enables graceful wrap-up [85].

5. **Hooks** (Claude Code): `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStart/Stop` — inject custom logic without modifying agent prompts [113].

6. **MCP** (Model Context Protocol): Claude Code is both an MCP client and server; dynamic tool discovery reduces context overhead by 88.7% vs. static loading [90].

**What requires external scaffolding**:

- **Reflexion**: Requires a multi-trial harness that restarts the agent with accumulated reflections. Not native to Claude Code's single-session architecture. If you need Reflexion, implement it at the harness level or use LangGraph's Reflexion node [73].
- **ToT**: Requires a branching search controller. Not available natively anywhere in the Anthropic ecosystem. Use LangGraph LATS if needed, but expect exponential costs [18].
- **Self-Consistency**: Requires N parallel API calls + majority vote aggregation. Not native. Easy to implement externally but expensive.
- **AutoGen-style multi-agent**: Claude API supports multi-agent via the `Task` tool (sub-agent spawning), but AutoGen's conversational GroupChat pattern requires external orchestration.

---

## Recommendations for Jetix (11-agent Claude System, 6 Departments)

*Assumption: 6 departments = Engineering, Research, Marketing, Sales, Operations, Design. Flag if the actual departments differ.*

### Which Variants to Adopt Per Department

| Department | Primary Variant | Secondary Variant | Rationale |
|------------|----------------|-------------------|-----------|
| **Engineering** | ReAct + CodeAct action space | Reflexion (when tests exist) | Claude Code's Bash tool implements CodeAct natively; Reflexion applies where unit tests or CI provide a pass/fail oracle |
| **Research** | Orchestrator-worker (Anthropic Research System pattern) | Plan-and-Execute for structured queries | Open-ended research matches the Anthropic multi-agent paper's exact use case; 90.2% improvement over single-agent for complex research [3] |
| **Marketing / Content** | Self-Refine (3–4 iterations) | ReAct for data gathering | Open-ended generation benefits from iterative critique; quality criteria (brand voice, readability) can be articulated in prompts [23] |
| **Sales** | ReAct with CRM tools | Reflexion on deal-outcome signals | Grounded tool use (CRM search, email retrieval, prospect research) matches ReAct's strengths; Reflexion if CRM has measurable win/loss signals |
| **Operations** | Plan-and-Execute | Human-in-the-loop interrupts at irreversible actions | Operations tasks (workflows, scheduling, external API calls) have predictable multi-step structure; irreversible actions require approval gates |
| **Design** | Self-Refine + ReAct | ReAct for research, Self-Refine for iteration | Design brief research is ReAct; iterative asset critique is Self-Refine; combine in an evaluator-optimizer workflow [1] |

### Concrete Defaults

#### Per-Agent `maxTurns` Recommendations

| Agent Type | Recommended `maxTurns` | Rationale |
|------------|------------------------|-----------|
| Simple lookup / Q&A | 5–8 | Single-topic queries should resolve in a few tool calls |
| Code editing (single file) | 15–20 | Sufficient for most PR-level tasks without runaway cost |
| Code debugging | 20–30 | Debugging may require multiple test-run cycles |
| Research (broad query) | 30–50 | Complex research involves many search iterations |
| Research (deep query, multi-agent) | 15–25 per subagent; orchestrator: 10 | Subagents are scoped; orchestrator manages overall termination |
| Data pipeline / ETL | 20–30 | Structured but may need iteration on schema discovery |
| Content generation + refine | 8–12 | 3–4 Self-Refine cycles; each cycle = ~2 turns |
| Sales research | 10–20 | CRM lookups, prospect research, email drafting |
| Operations workflow | 15–25 with human gates | Human-in-the-loop interrupts add overhead |

#### Token Budget per Iteration

Use Anthropic's Task Budgets API [85] for long-running agents. Suggested defaults:

- **Engineering agent**: 50,000–100,000 tokens (code reads + writes are verbose)
- **Research agent**: 80,000–150,000 tokens (search results are large)
- **Marketing agent**: 20,000–40,000 tokens (content generation is shorter)
- **Sales agent**: 15,000–30,000 tokens (mostly lookup + email drafting)
- **Operations agent**: 20,000–40,000 tokens (structured workflows)
- **Design agent**: 20,000–40,000 tokens (brief + iteration cycles)

Set `total` at 2–3× the expected per-task cost to allow for retries, and set `remaining` to match. Monitor token usage per task for the first 2–3 weeks to calibrate.

#### CLAUDE.md Structure Recommendation

Based on Claude Code documentation [108][113] and Boris Cherny's guidance [26]:

```markdown
# [Agent Name] — Jetix [Department]

## Role
[2–3 sentences defining the agent's specific responsibility]

## Scope
- IN SCOPE: [explicit list of what this agent should handle]
- OUT OF SCOPE: [explicit list of what to delegate or decline]

## Tools Available
- [Tool 1]: [when to use it; specific guidance]
- [Tool 2]: [when to use it; specific guidance]

## Output Format
[Required structure for this agent's outputs]

## Completion Criteria
[Machine-verifiable criteria — not fuzzy statements like "when done"]
[Examples: "When all tests pass", "When the brief has been approved", "When 3 sources have been found"]

## Escalation Rules
- [Condition 1]: Pause and ask user
- [Condition 2]: Halt and report error
- [Condition 3]: Delegate to [other agent name]

## Standards
- Use 2-space indentation (if engineering)
- Cite every factual claim with source URL (if research)
- [Department-specific standards]
```

Target under 200 lines. Use concrete, verifiable instructions. If two rules could contradict, Claude may pick arbitrarily [108].

#### When to Use Sub-agents via Task Tool vs. Keep in Main Agent

**Use sub-agents when:**
- The task requires context isolation (e.g., exploratory research that should not pollute the main conversation)
- You need a different model for a specific step (e.g., Haiku for cheap summarization, Opus for complex reasoning)
- The subtask has a well-defined input/output contract and does not need the full parent context
- You want parallel execution (multiple subagents for independent research threads)
- You need tool restrictions (e.g., a read-only subagent for security)

**Keep in main agent when:**
- The subtask requires full conversation context to function correctly (Walden Yan's Principle 1: share full context [62])
- The task is a short sequence of tool calls that fits in the current turn
- You need to avoid the coordination overhead and context fragmentation of sub-agents
- The task involves sequential decisions where each step informs the next

**Critical constraint from Claude Code docs** [28]:
> *"Subagents receive only the subagent's system prompt (plus basic environment details like working directory), not the full Claude Code system prompt. Subagents don't inherit skills from the parent conversation."*

If a subagent needs context from the parent conversation, **explicitly pass it in the subagent's task description** — it will not be inherited automatically.

### Coordination Model Between the 11 Agents

**Recommended: Hierarchical Orchestrator-Worker with Department Isolation**

Given a solo founder with 11 agents and a 15× multi-agent token cost multiplier:

```
[User / Founder]
       |
[Master Orchestrator Agent]     ← routes tasks to departments; monitors budget
       |
  ┌────┴──────────────────────────────┐
  │Engineering │Research│Marketing│Sales│Operations│Design│
  │   Agent    │ Agent  │  Agent  │Agent│  Agent   │Agent │
  └────────────────────────────────────┘
       |
  [Sub-agents spawned per task, as needed, within department]
```

**Why orchestrator-worker over flat peer routing:**
- The Anthropic Research System demonstrated 90.2% improvement with this pattern [3]
- Magentic-One achieved competitive GAIA/WebArena results with an Orchestrator directing 4 specialist agents [96]
- Flat peer routing (AutoGen GroupChat, OpenAI Swarm handoffs) introduces unpredictable costs and context fragmentation

**Why NOT full-parallel multi-agent for all tasks:**
- 15× token cost vs. chat — only justified where task parallelism delivers clear value [3]
- Walden Yan's Principle 1 [62]: most tasks have context-dependencies that serial execution handles better
- A solo founder cannot review 11 parallel agent trajectories simultaneously; sequential is debuggable

**Practical coordination rules for Jetix:**

1. **Separate sessions by department** — do not share context across Engineering and Marketing agents. Each agent has its own CLAUDE.md, its own MEMORY.md, and its own context.

2. **The master orchestrator routes, not executes** — it classifies incoming tasks and delegates; it does not do the domain work itself.

3. **Use sub-agents within departments for parallelism** — a Research agent can spawn 3–5 parallel subagents for a complex research query (matching the Anthropic pattern [3]); an Engineering agent can spawn parallel review subagents.

4. **Pass full context on sub-agent delegation** — not just a summary. If a subagent needs the parent's findings, include them in the task description. This is Walden's Principle 1 [62] applied to Claude Code's architecture.

5. **Monitor cost per department weekly** — use hooks (`PostToolUse`, `Stop`) to log token consumption per agent and compare against task value [113].

### Termination Conditions to Set

For every Jetix agent, configure **all four layers**:

1. **`maxTurns`** (hard cap, per agent type above): Set in YAML frontmatter for sub-agents; use hooks to enforce for main agents.

2. **Task Budget** (token-denominated soft limit): Use Anthropic's `task-budgets-2026-03-13` header for long-running agents. Set total = 2× expected token use [85].

3. **Completion predicate** (machine-verifiable): Every agent system prompt must include a completion section with verifiable criteria. *"When all tests pass"* is good; *"When you've done a good job"* is not [84].

4. **Escalation trigger** (human-in-the-loop): Define which actions require user approval before execution:
   - Any irreversible external action (sending email, posting content, committing to main branch)
   - Any action exceeding a defined cost threshold ($X per run)
   - Any action that modifies production data

**Recommended completion predicates by department:**
- Engineering: *"When all failing tests now pass and no previously passing tests fail"*
- Research: *"When 5+ primary sources have been found, cited with URLs, and the summary has been reviewed"*
- Marketing: *"When the draft has been through 3 Self-Refine iterations and the final quality score ≥ 7/10 per rubric"*
- Sales: *"When the prospect profile has been populated with all required fields from CRM"*
- Operations: *"When the workflow has been validated against the checklist and human approval has been received for each irreversible step"*
- Design: *"When the brief meets all client requirements and has been reviewed in Plan Mode before execution"*

### What to Avoid Given the 15× Token Cost of Multi-Agent

1. **Do not deploy all 11 agents in parallel for every task.** Reserve multi-agent for tasks where parallelism genuinely reduces elapsed time or where task complexity requires specialization. A single ReAct agent will handle most consultancy tasks at 1/15th the cost.

2. **Do not use AutoGPT-style unbounded loops.** Every agent must have a `maxTurns` ceiling and a cost budget. No exceptions [84][85].

3. **Do not use Tree-of-Thoughts in production workflows.** O(b^d) cost scaling is incompatible with production economics. Use it only for offline combinatorial planning if needed [18].

4. **Do not pass summaries between agents — pass full traces.** Walden Yan's Principle 1 [62] is correct: context loss during agent handoffs causes duplicated work, gaps, and fragile outputs. The coordination overhead of passing full traces is worth it.

5. **Do not add LangGraph or other orchestration frameworks on top of Claude Code.** Claude Code already implements the loop. Adding a framework adds latency, complexity, and debugging surface area without improving the core loop behavior. Use LangGraph only if you need features Claude Code cannot provide natively (e.g., complex graph routing, ToT search).

6. **Do not use Self-Consistency sampling for routine tasks.** N=40 parallel samples is 40× the cost of a single inference [24]. Reserve for high-stakes, discrete-answer decisions only.

7. **Do not rely on model self-declaration for fuzzy completion signals.** "Done" from a model is unreliable for open-ended tasks [84]. Implement external completion predicates, tests, or human review gates.

8. **Avoid long (>200 line) CLAUDE.md files.** Longer files consume more context and reduce adherence — *"If two rules contradict each other, Claude may pick one arbitrarily"* [108]. Keep instructions concrete and concise.

---

## Sources List

[1] Erik S. and Barry Zhang (Anthropic), "Building Effective Agents" (Anthropic Research, 2024-12-19). https://www.anthropic.com/research/building-effective-agents

[2] Anthropic, "Claude Tool Use Documentation" (Anthropic Docs, continuously updated, fetched mid-2025). https://docs.anthropic.com/en/docs/build-with-claude/tool-use

[3] Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford (Anthropic Engineering), "How We Built Our Multi-Agent Research System" (Anthropic Engineering Blog, 2025-06-13). https://www.anthropic.com/engineering/built-multi-agent-research-system

[4] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao, "ReAct: Synergizing Reasoning and Acting in Language Models" (ICLR 2023, arXiv, 2022-10-06). https://arxiv.org/abs/2210.03629

[5] OpenAI, "Function Calling Documentation (Responses API)" (OpenAI Docs, continuously updated, fetched 2025-08-07). https://platform.openai.com/docs/guides/function-calling

[6] OpenAI, "Agents SDK 'Running Agents' (Python SDK)" (OpenAI Docs, 2025). https://openai.github.io/openai-agents-python/running_agents/

[7] OpenAI, "Running Agents (Developer Portal)" (OpenAI Docs, 2025). https://developers.openai.com/api/docs/guides/agents/running-agents

[8] LangChain AI / Harrison Chase, "LangGraph Agent Architectures Documentation" (LangGraph Docs, continuously updated). https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/

[9] LangChain, "Agents Documentation" (LangChain Docs, continuously updated). https://docs.langchain.com/oss/python/langchain/agents

[10] Google AI for Developers, "Gemini Function Calling Documentation" (Google AI Docs, continuously updated, fetched mid-2025). https://ai.google.dev/gemini-api/docs/function-calling

[11] swyx (Shawn Wang), "Agent Engineering" (Latent Space, 2025-03-24). https://www.latent.space/p/agent

[12] AnthropicAI, "Twitter/X announcement of multi-agent research system post" (2025-06-13). https://x.com/AnthropicAI/status/1933630785879507286

[13] Shunyu Yao et al., "ReAct PDF (full benchmarks and trace)" (arXiv, 2022-10-06). https://arxiv.org/pdf/2210.03629

[14] Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao, "Reflexion: Language Agents with Verbal Reinforcement Learning" (arXiv, 2023-03-20). https://arxiv.org/abs/2303.11366

[15] Xuezhi Wang et al., "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning in Large Language Models" (ACL 2023, arXiv, 2023-05-06). https://arxiv.org/abs/2305.04091

[16] Harrison Chase (LangChain), "Planning Agents" (LangChain Blog, 2023). https://blog.langchain.dev/planning-agents/

[17] Yohei Nakajima, "BabyAGI" (GitHub, 2023-04). https://github.com/yoheinakajima/babyagi

[18] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan, "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" (arXiv, 2023-05-17). https://arxiv.org/abs/2305.10601

[19] Princeton NLP, "Tree-of-Thought Code Repository" (GitHub, 2023). https://github.com/princeton-nlp/tree-of-thought-llm

[20] Emergent Mind, "Tree of Thoughts topic summary" (Emergent Mind, 2023). https://www.emergentmind.com/topics/program-of-thoughts-pot

[21] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, Heng Ji, "Executable Code Actions Elicit Better LLM Agents" (arXiv, 2024-02-01). https://arxiv.org/abs/2402.01030

[22] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar, "Voyager: An Open-Ended Embodied Agent with Large Language Models" (arXiv, 2023-05-25). https://arxiv.org/abs/2305.16291

[23] Aman Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback" (arXiv, 2023-03-30). https://arxiv.org/abs/2303.17651

[24] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou, "Self-Consistency Improves Chain of Thought Reasoning in Language Models" (ICLR 2023, arXiv, 2022-03-21). https://arxiv.org/abs/2203.11171

[25] Toran Bruce Richards / Significant Gravitas Ltd, "AutoGPT" (GitHub, released 2023-03-30). https://github.com/Significant-Gravitas/AutoGPT

[26] Boris Cherny, Catherine Wu, "Claude Code: Anthropic's Agent in Your Terminal" (Latent Space Podcast, 2025-05-07). https://www.latent.space/p/claude-code

[27] "How the Creator of Claude Code Actually Uses Claude Code" (Push To Prod Newsletter, 2026-02). https://getpushtoprod.substack.com/p/how-the-creator-of-claude-code-actually

[28] Anthropic, "Claude Code Sub-Agents Documentation" (Anthropic Docs, 2026-04). https://docs.anthropic.com/en/docs/claude-code/sub-agents

[29] Anthropic, "Claude Code Overview" (Anthropic Docs, 2026-04). https://docs.anthropic.com/en/docs/claude-code/overview

[30] Walden Yan (Cognition), "Don't Build Multi-Agents" (Cognition.ai Blog, 2025-06-12). https://cognition.ai/blog/dont-build-multi-agents

[31] Wikipedia, "AutoGPT" (Wikipedia). https://en.wikipedia.org/wiki/AutoGPT

[32] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press, "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering" (NeurIPS 2024, arXiv, 2024-05-06). https://arxiv.org/abs/2405.15793

[33] SWE-agent, "ACI Documentation" (swe-agent.com). https://swe-agent.com/0.7/background/aci/

[34] Xingyao Wang et al., "OpenHands: An Open Platform for AI Software Developers as Generalist Agents" (arXiv, 2024-07-23). https://arxiv.org/abs/2407.16741

[35] OpenHands, "Agent SDK Documentation" (docs.openhands.dev). https://docs.openhands.dev/sdk/arch/agent

[36] Cursor Team, "Composer: Building a Fast Frontier Model with RL" (cursor.com/blog, 2025-10). https://cursor.com/blog/composer

[37] Aman Sanger, "Editing Files at 1000 Tokens per Second" (cursor.com/blog, 2024-05). https://cursor.com/blog/instant-apply

[38] Cline GitHub README (cline/cline). https://github.com/cline/cline

[39] Cline, "Plan & Act Mode Documentation" (cline.bot). https://docs.cline.bot/features/plan-and-act

[40] Continue, "How Agent Mode Works" (docs.continue.dev). https://docs.continue.dev/ide-extensions/agent/how-it-works

[41] Continue, "Using Plan Mode with Continue" (docs.continue.dev). https://docs.continue.dev/guides/plan-mode-guide

[42] Paul Gauthier, "Separating code reasoning and editing" (aider.chat Blog, 2024-09-26). https://aider.chat/2024/09/26/architect.html

[43] Paul Gauthier, "Aider LLM Leaderboards" (aider.chat, updated 2025-11). https://aider.chat/docs/leaderboards/

[44] Paul Gauthier, "Aider Edit Formats Documentation" (aider.chat). https://aider.chat/docs/more/edit-formats.html

[45] Paul Gauthier, "Paul Gauthier quote on large context windows" (via Simon Willison's Weblog, 2025-01-26). https://simonwillison.net/2025/Jan/26/paul-gauthier/

[46] Cognition Team, "SWE-bench Technical Report: Devin 13.86%" (Cognition.ai Blog, 2024-03-15). https://cognition.ai/blog/swe-bench-technical-report

[47] Cognition, "Devin can now Manage Devins" (Cognition.ai Blog, 2026-03-19). https://cognition.ai/blog/devin-can-now-manage-devins

[48] Devin, "Interactive Planning Documentation" (docs.devin.ai). https://docs.devin.ai/work-with-devin/interactive-planning

[49] Lex Fridman Podcast #447, "Cursor Team: Future of Programming with AI" (Transcript, 2024-10-06). https://lexfridman.com/cursor-team-transcript/

[50] Taivo Pungas, "Why AutoGPT Fails" (taivo.ai, 2023). https://www.taivo.ai/__why-autogpt-fails-and-how-to-fix-it/

[51] LangChain, "Reflection Agents Blog" (LangChain Blog, 2024). https://www.langchain.com/blog/reflection-agents

[52] Prompt Engineering Guide, "Reflexion Overview" (promptingguide.ai). https://www.promptingguide.ai/techniques/reflexion

[53] "Lateral Tree-of-Thoughts exponential cost analysis" (arXiv:2510.01500). https://arxiv.org/html/2510.01500v1

[54] Emergent Mind, "Self-Consistency Decoding Strategy" (emergentmind.com). https://www.emergentmind.com/topics/self-consistency-decoding-strategy

[55] Guanzhi Wang et al., "Voyager project site" (voyager.minedojo.org). https://voyager.minedojo.org/

[56] Hacker News discussion on Voyager (HN #36085936). https://news.ycombinator.com/item?id=36085936

[57] "Agentic Program Repair from Test Failures at Scale (Meta Engineering Agent)" (arXiv:2507.18755). https://arxiv.org/html/2507.18755v1

[58] ZenML / ByteByteGo, "Building Cursor Composer" (zenml.io). https://www.zenml.io/llmops-database/building-cursor-composer-a-fast-intelligent-agent-based-coding-model-with-reinforcement-learning

[59] OpenHands Blog, "Learning to Verify AI-Generated Code" (openhands.dev, 2026-03-05). https://openhands.dev/blog/20260305-learning-to-verify-ai-generated-code

[60] "SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution" (arXiv:2512.18470, 2025-12). https://arxiv.org/html/2512.18470v5

[61] Cognition Team, "SWE-bench Technical Report" (March 2024). https://cognition.ai/blog/swe-bench-technical-report

[62] Walden Yan (Cognition), "Don't Build Multi-Agents" (cognition.ai, 2025-06-12). https://cognition.ai/blog/dont-build-multi-agents

[63] Cognition, "Devin can now Manage Devins" (cognition.ai, 2026-03-19). https://cognition.ai/blog/devin-can-now-manage-devins

[64] Cline v3.35 Release Notes (Reddit r/CLine). https://www.reddit.com/r/CLine/comments/1ol0c5u/cline_v335_native_tool_calling_redesigned/

[65] Continue Blog, "Building Cloud Agents with Continue CLI" (blog.continue.dev, 2025-08). https://blog.continue.dev/building-async-agents-with-continue-cli/

[66] "Demystifying LLM-Based Software Engineering Agents (Agentless)" (UIUC, FSE 2025). https://lingming.cs.illinois.edu/publications/fse2025.pdf

[67] "OpenHands vs SWE-agent technical comparison" (localaimaster.com, 2026-02). https://localaimaster.com/blog/openhands-vs-swe-agent

[68] "The OpenHands Software Agent SDK" (arXiv:2511.03690, 2025-11). https://arxiv.org/pdf/2511.03690

[69] Jason Liu, "Why Cognition does not use multi-agent systems" (jxnl.co, 2025-09-11). https://jxnl.co/writing/2025/09/11/why-cognition-does-not-use-multi-agent-systems/

[70] Paul Gauthier, "Aider Repository Map" (aider.chat). https://aider.chat/docs/repomap.html

[71] ZenML, "LlamaIndex vs LangChain comparison" (zenml.io). https://www.zenml.io/blog/llamaindex-vs-langchain

[72] LangGraph, "LangGraph Concepts Low Level" (LangGraph Docs). https://langchain-ai.github.io/langgraph/concepts/low_level/

[73] LangChain, "LangGraph Reflexion node" (langchain.com/blog). https://www.langchain.com/blog/reflection-agents

[74] Prompt Engineering Guide, "Reflexion" (promptingguide.ai). https://www.promptingguide.ai/techniques/reflexion

[75] Emergent Mind, "Tree of Thoughts" (emergentmind.com). https://www.emergentmind.com/topics/program-of-thoughts-pot

[76] "Lateral Tree-of-Thoughts" (arXiv:2510.01500). https://arxiv.org/html/2510.01500v1

[77] Taivo Pungas, "Why AutoGPT Fails" (taivo.ai, 2023). https://www.taivo.ai/__why-autogpt-fails-and-how-to-fix-it/

[78] LangGraph, "LangGraph Low Level Concepts" (LangGraph Docs). https://langchain-ai.github.io/langgraph/concepts/low_level/

[79] LangGraph, "Multi-Agent Systems Concepts" (LangGraph Docs). https://langchain-ai.github.io/langgraph/concepts/multi_agent/

[80] LangGraph, "Persistence Documentation" (LangGraph Docs). https://docs.langchain.com/oss/python/langgraph/persistence

[81] LangGraph, "Interrupts Documentation" (LangGraph Docs). https://docs.langchain.com/oss/python/langgraph/interrupts

[82] LangChain, "Making it easier to build human-in-the-loop agents with interrupt" (LangChain Blog). https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt

[83] Harrison Chase (LangChain), "Sequoia Capital Podcast: Context Engineering" (Sequoia Capital Podcast, 2026-01). https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/

[84] Various practitioners, "Anti-patterns and failure modes compilation" — Sources include: Benjamin Hopwood LinkedIn ("The Ralph Wiggum Problem"), https://www.linkedin.com/pulse/ralph-wiggum-problem-why-agents-quit-early-how-fix-benjamin-hopwood-qb3gc; Reddit r/ClaudeCode, https://www.reddit.com/r/ClaudeCode/comments/1rwd8fa/; Saurav Bhatia LinkedIn ("7 Failure Modes"), https://www.linkedin.com/posts/sauravbhats_7-failure-modes-of-ai-agents-framework-from-activity-7429704521141944320-WMGY; Tianpan.co ("Phantom Tool Calls"), https://tianpan.co/blog/2026-04-14-phantom-tool-calls-when-ai-agents-invoke-tools-that-dont-exist; n8n Community, https://community.n8n.io/t/ai-agent-keeps-calling-same-tool-with-same-parameters/196961

[85] Anthropic, "Claude API Docs: Task Budgets" (platform.claude.com, public beta 2026). https://platform.claude.com/docs/en/build-with-claude/task-budgets

[86] Wondering About AI, "Does Claude get desperate when running out of tokens?" (wonderingaboutai.substack.com, 2026-04). https://wonderingaboutai.substack.com/p/does-claude-get-desperate-when-its

[87] HAL GAIA Leaderboard (Princeton, live). https://hal.cs.princeton.edu/gaia

[88] vals.ai, "SWE-bench Leaderboard" (vals.ai). https://www.vals.ai/benchmarks/swebench

[89] Augment Code, "AI Agent Loop Token Costs" (augmentcode.com, 2026-04). https://www.augmentcode.com/guides/ai-agent-loop-token-cost-context-constraints

[90] EclipseSource, "MCP and Context Overload" (eclipsesource.com, 2026-01-22). https://eclipsesource.com/blogs/2026/01/22/mcp-context-overload/

[91] Anthropic, "Claude API Docs: Compaction" (platform.claude.com, beta compact_20260112). https://platform.claude.com/docs/en/build-with-claude/compaction

[92] Anthropic, "Claude API Docs: Parallel Tool Use" (platform.claude.com). https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use

[93] Qingyun Wu, Gagan Bansal, Jieyu Zhang et al. (Microsoft Research), "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" (arXiv:2308.08155, 2023-08-23). https://arxiv.org/abs/2308.08155

[94] Sirui Hong, Mingchen Zheng et al., "MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework" (arXiv:2308.00352, 2023-08-01). https://arxiv.org/abs/2308.00352

[95] Shuyan Zhou, Frank F. Xu, Hao Zhu et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents" (arXiv:2307.13854, 2023-07-25). https://arxiv.org/abs/2307.13854

[96] Adam Fourney, Gagan Bansal, Hussein Mozannar et al. (Microsoft Research), "Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks" (arXiv:2411.04468, 2024-11-07). https://arxiv.org/abs/2411.04468

[97] Zora Zheng Wang et al., "Agent Workflow Memory" (arXiv:2409.07429, ICML 2025, 2024-09-11). https://arxiv.org/abs/2409.07429

[98] Mingchen Zhuge, Changsheng Zhao, Dylan Ashley et al., "Agent-as-a-Judge: Evaluate Agents with Agents" (arXiv:2410.10934, 2024-10-14). https://arxiv.org/abs/2410.10934

[99] Zora Zheng Wang et al., "Agent Workflow Memory" (arXiv:2409.07429, 2024-09-11). https://arxiv.org/abs/2409.07429

[100] Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan, "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains" (arXiv:2406.12045, 2024-06-17). https://arxiv.org/abs/2406.12045

[101] "AgencyBench: A Benchmark for Evaluating Agency in AI Systems" (arXiv:2601.11044, 2026). https://arxiv.org/html/2601.11044v2

[102] "Efficient Agents: Building Effective Agents While Reducing Cost" (arXiv:2508.02694, 2025-07). https://arxiv.org/html/2508.02694v1

[103] "Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Behavior" (arXiv:2603.03258, 2026-03). https://arxiv.org/html/2603.03258v1

[104] Gagan Bansal (Microsoft Research), "AutoGen v0.4: Reimagining the foundation of agentic AI" (Microsoft Research Blog, 2025-02-25). https://www.microsoft.com/en-us/research/articles/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness/

[105] João Moura, "CrewAI Official Documentation — Crews" (crewai.com). https://docs.crewai.com/concepts/crews

[106] OpenAI, "OpenAI Swarm" (GitHub, educational framework). https://github.com/openai/swarm

[107] OpenAI, "Agents SDK — Handoffs documentation" (openai.github.io). https://openai.github.io/openai-agents-python/handoffs/

[108] Anthropic, "Claude Code Memory (CLAUDE.md)" (Anthropic Docs). https://docs.anthropic.com/en/docs/claude-code/memory

[109] SWE-bench contamination analysis — Sources include: arXiv:2506.12286, https://arxiv.org/html/2506.12286v1; CodeAnt AI SWE-bench analysis, https://www.codeant.ai/blogs/swe-bench-scores

[110] Xiao Liu, Hao Yu, Hanchen Zhang et al., "AgentBench: Evaluating LLMs as Agents" (ICLR 2024, arXiv:2308.03688, 2023-08-07). https://arxiv.org/abs/2308.03688

[111] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, Thomas Scialom, "GAIA: A Benchmark for General AI Assistants" (arXiv:2311.12983, 2023-11-21). https://arxiv.org/abs/2311.12983

[112] Stream E Research, "How Multi-agent Loops Differ from Single-agent Loops" — compiled from sources cited above including Anthropic Engineering Blog [3] and Magentic-One [96].

[113] Anthropic, "Claude Code Hooks Reference" (Anthropic Docs). https://docs.anthropic.com/en/docs/claude-code/hooks

[114] Simon Willison, "2025 Year in LLMs" (simonwillison.net, 2025-12-31). https://simonwillison.net/2025/Dec/31/the-year-in-llms/

[115] Simon Willison, "Anthropic multi-agent research system summary" (simonwillison.net, 2025-06-14). https://simonwillison.net/2025/Jun/14/multi-agent-research-system/

[116] Answer.AI, "Thoughts on a Month with Devin" (answer.ai, 2025-01-08). https://www.answer.ai/posts/2025-01-08-devin.html

[117] Steve Kinney, "Claude Code Compaction" (stevekinney.com). https://stevekinney.com/courses/ai-development/claude-code-compaction

[118] "SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness" (arXiv:2509.09853, 2025-09). https://arxiv.org/html/2509.09853v1

[119] Oracle Developer Blog, "What Is the AI Agent Loop?" (blogs.oracle.com, 2026-03). https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems

[120] OpenAI, "Introducing SWE-bench Verified" (openai.com, 2024-08-13). https://openai.com/index/introducing-swe-bench-verified/

[121] Boris Cherny quote via Simon Willison's Weblog (simonwillison.net, 2026-02-14). https://simonwillison.net/2026/Feb/14/boris/

[122] Lunar.dev, "Why Dynamic Tool Discovery Solves the Context Management Problem" (lunar.dev). https://www.lunar.dev/post/why-dynamic-tool-discovery-solves-the-context-management-problem

[123] SWE-agent, "Competitive Runs Documentation" (swe-agent.com). https://swe-agent.com/latest/usage/competitive_runs/

[124] DEV Community, "A Postmortem on Autonomous LLM-as-Judge" (dev.to). https://dev.to/gpgkd906/a-postmortem-on-autonomous-llm-as-judge-how-my-eval-agent-got-two-verdicts-wrong-before-i-found-a-a3j

[125] "INoT Multi-agent Debate" (arXiv:2507.08664). https://arxiv.org/html/2507.08664v1

[126] OpenAI Agents SDK, "Runner Reference — max_turns" (openai.github.io). https://openai.github.io/openai-agents-python/ref/run/

[127] Model Context Protocol, "Architecture Overview" (modelcontextprotocol.io). https://modelcontextprotocol.io/docs/learn/architecture

---

*Document compiled from 127 sources across 5 research streams. All verbatim quotes are attributed with source number and date. Items that stream source files flagged as internal-not-public are so noted (primarily: Claude Code internal benchmark scores, Claude Code internal architecture details beyond what is publicly documented, and Devin's post-2024 SWE-bench scores).*
