# Swarm Intelligence in AI Agent Systems — Technical Due Diligence for Jetix

*Prepared for: Ruslan / Jetix (Berlin), April 2026*
*Decision at stake: replace the current 12-agent CEO→Manager→Leads→Workers hierarchy with a swarm pattern (interchangeable agents + shared context, Claude Code-style).*

---

## Executive Summary

The term "swarm" is the most abused word in multi-agent AI. In its canonical meaning — from [Bonabeau, Dorigo & Theraulaz's *Swarm Intelligence: From Natural to Artificial Systems*](https://jmvidal.cse.sc.edu/lib/bonabeau99a.html) — a swarm requires three properties simultaneously: **decentralized control, homogeneous agents, and emergent (not pre-programmed) global behavior**. Measured against that definition, virtually no production LLM framework marketed as a "swarm" qualifies. OpenAI Swarm is flat routing. CrewAI is explicitly hierarchical. LangGraph is a general graph engine. ruvnet/claude-flow calls itself a "hive-mind" while implementing queen-led hierarchical coordination — the [architectural opposite of decentralization](https://github.com/ruvnet/claude-flow). What Boris Cherny practices in Claude Code is closer to the theoretical ideal than anything sold as "swarm," and even his pattern is better described as **stigmergic coordination among fungible compute units** than as a classical swarm.

The second finding is that the empirical evidence on multi-agent performance is much more critical than the marketing suggests. A December 2025 study of 260 configurations ([Kim et al., arXiv:2512.08296](https://arxiv.org/abs/2512.08296)) found that the aggregate mean improvement of multi-agent systems over single agents is **−3.5%** — i.e., the average multi-agent deployment *underperforms* a single agent. Wins are real but narrow: breadth-first research (+90.2%, [Anthropic's internal eval](https://www.anthropic.com/engineering/built-multi-agent-research-system)), decomposable financial reasoning (+80.8%), mathematical debate (+14.8 percentage points, [Du et al.](https://arxiv.org/abs/2305.14325)). Losses are equally real: sequential planning (−39 to −70%), tool-heavy workflows (2–6× efficiency penalty), SWE-bench coding (single-agent 73.2% vs. multi-agent 62.2%, [Emergent Mind](https://www.emergentmind.com/topics/swe-bench-leaderboards)). Independent multi-agent systems amplify errors **17.2×** relative to single-agent baselines; centralized verification reduces this to 4.4× ([Kim et al.](https://arxiv.org/abs/2512.08296)).

The third finding is that Anthropic's own production-measured number — *"multi-agent systems use about 15× more tokens than chats"* ([Hadfield et al., June 2025](https://www.anthropic.com/engineering/built-multi-agent-research-system)) — is both a constraint and a mechanism: *"token usage by itself explains 80% of the variance"* in performance, meaning multi-agent architectures pay for their token bill by giving you more parallel cognition, but only if the task is parallelizable. Cognition (the company behind Devin) publicly argues the opposite position in [Walden Yan's "Don't Build Multi-Agents"](https://cognition.ai/blog/dont-build-multi-agents): for long-horizon coding tasks, they keep a single-thread agent with a fine-tuned compression model, and explicitly warn that parallel subagents produce "fragile systems" because "decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough."

### Top 5 findings for the Jetix decision

1. **A 12-agent fixed hierarchy is almost certainly the wrong architecture for a solo founder.** It combines the coordination tax of multi-agent systems with the rigidity of role specialization, and the coupling between roles matches the failure profile [Cemri et al. (arXiv:2503.13657)](https://arxiv.org/abs/2503.13657) identify in their [MAST taxonomy of 14 failure modes](https://arxiv.org/abs/2503.13657).

2. **A pure swarm is also wrong.** Flat peer-to-peer coordination requires infrastructure (verification, shared memory, quorum logic) that does not yet exist in open form. Every credible production system — Anthropic Research, Devin, Cursor, Sierra, Factory AI, Harvey — is a hybrid: hierarchical control at the top, homogeneous parallelism at the leaves, shared environment in the middle.

3. **Claude Code's actual pattern, correctly described, is stigmergic.** Agents are fungible compute units reading and writing a shared environment (CLAUDE.md + filesystem + git state). They do not talk to each other. They coordinate through cumulative modification of the environment — exactly Grassé's 1959 definition of stigmergy.

4. **At €50K ARR, the practical multi-agent budget is $100–$300/month.** The subscription-vs-API arbitrage is extreme (up to 25–50×). For Jetix, the right default is **Claude Code Max 5× ($100/mo) with API overflow for batch jobs**, not a 12-agent pipeline at API rates.

5. **The Rule of 4 is the sweet spot.** Kim et al. find effective multi-agent team sizes peak at 3–4 agents under current token economics. Anthropic Research deploys 3–10 subagents. Twelve specialized agents is well past the diminishing-returns knee of the logistic scaling curve described in [Qian et al. (arXiv:2406.07155)](https://arxiv.org/abs/2406.07155).

---

## Section 1 — Definitions & Distinctions

### 1.1 The five terms, precisely

**Swarm Intelligence.** The canonical definition is from [Bonabeau, Dorigo & Theraulaz's 1999 Oxford volume *Swarm Intelligence: From Natural to Artificial Systems*](https://jmvidal.cse.sc.edu/lib/bonabeau99a.html). Its operative form appears in the [Scholarpedia article co-authored by Dorigo](http://www.scholarpedia.org/article/Swarm_intelligence):

> "Swarm intelligence is the discipline that deals with natural and artificial systems composed of many individuals that coordinate using decentralized control and self-organization. In particular, the discipline focuses on the collective behaviors that result from the local interactions of the individuals with each other and with their environment."

The same source enumerates the necessary and sufficient properties: many individuals, relative **homogeneity**, simple local rules, self-organization (**emergence**, not pre-programming), and **no centralized controller**. [Wikipedia's summary](https://en.wikipedia.org/wiki/Swarm_intelligence) adds the key phrase *"intelligent global behavior, **unknown to the individual agents**"* — the global property is not derivable from any single agent's knowledge.

**Multi-Agent System (MAS).** The canonical textbook is [Michael Wooldridge's *An Introduction to MultiAgent Systems*, 2nd ed. (2009)](https://archive.org/details/introductiontomu0000wool). From [Wooldridge's lecture slides](http://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/imas/distrib/2up/lect02-2up.pdf):

> "An agent is a computer system capable of autonomous action in some environment, in order to achieve its delegated goals… Social ability in agents is the ability to interact with other agents (and possibly humans) via cooperation, coordination, and negotiation."

[Shoham & Leyton-Brown's *Multiagent Systems* (MIT Press 2013)](https://mitpress.ublish.com/book/multiagent-systems-0) adds that MAS agents are entities "able to cooperate, compete, communicate, act flexibly, and exercise control over their behavior." Crucially, MAS **permits** hierarchy, heterogeneity, centralized orchestration, and explicit messaging — none of which a swarm allows. Every swarm is a MAS; the reverse is false.

**Hive-mind coordination.** This is not a technical term in classical AI. Its current usage in LLM agent discourse is driven almost entirely by [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow), which defines its hive-mind system as *"queen-led hierarchical coordination where strategic queen agents direct specialized workers through collective decision-making and shared memory."* Architecturally, this is **the opposite** of a classical swarm: centralized, hierarchical, heterogeneous (Queens: Strategic/Tactical/Adaptive; Workers: 8 specializations). The substrate is SQLite with WAL mode as shared memory. The term "hive-mind" in AI therefore denotes a **hierarchical orchestration system with persistent shared state**, not the distributed cognition of an actual beehive.

**Agent society.** Two lineages. Minsky's *Society of Mind* (Simon & Schuster, 1986) used the metaphor loosely. Jennings and colleagues in the 1990s formalized normative MAS governed by obligations and contracts. The defining recent usage is [Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (arXiv:2304.03442, UIST 2023)](https://3dvar.com/Park2023Generative.pdf), the Stanford "Smallville" simulation:

> "A society full of generative agents is marked by emergent social dynamics where new relationships are formed, information diffuses, and coordination arises across agents."

The Park paper is important because it demonstrates **environment-mediated coordination** — agents coordinate not through direct messaging but through observation of shared world state. This is structurally analogous to stigmergy.

**Actor Model.** [Carl Hewitt, Peter Bishop & Richard Steiger, "A Universal Modular ACTOR Formalism for Artificial Intelligence" (IJCAI 1973)](https://www.ijcai.org/Proceedings/73/Papers/027B.pdf):

> "Intuitively, an **ACTOR** is an active agent which plays a role on cue according to a script… Our formalism shows how all of the modes of behavior can be defined in terms of one kind of behavior: **sending messages to actors**."

[Hewitt's 2010 restatement](https://arxiv.org/pdf/1008.1459) clarifies: the Actor Model is a mathematical theory of concurrent computation where actors communicate "only through direct asynchronous message passing" — no shared mutable state. Erlang and Akka are direct implementations.

The Actor Model is a **concurrency substrate**, not a coordination paradigm. A MAS can be built on top of actors; a swarm could be; but the Actor Model itself says nothing about emergence, hierarchy, or stigmergy.

### 1.2 Conceptual definitions matrix

| Term | Decentralized? | Emergent behavior? | Homogeneous agents? | Explicit hierarchy? | Shared mutable state? | Canonical source |
|---|---|---|---|---|---|---|
| **Swarm Intelligence** | ✅ Required | ✅ Required | ✅ Required | ❌ Forbidden | ✅ Via environment | [Bonabeau et al. 1999](https://jmvidal.cse.sc.edu/lib/bonabeau99a.html) |
| **Multi-Agent System** | Optional | Optional | Optional | Optional | Optional | [Wooldridge 2009](https://archive.org/details/introductiontomu0000wool) |
| **Hive-Mind (AI usage)** | ❌ Queen-led | Partial | ❌ Specialized | ✅ Yes | ✅ SQLite/memory | [claude-flow](https://github.com/ruvnet/claude-flow) |
| **Agent Society** | Optional | ✅ Social dynamics | Optional | Optional | Via environment | [Park et al. 2023](https://3dvar.com/Park2023Generative.pdf) |
| **Actor Model** | ✅ No shared state | N/A | Optional | Optional | ❌ Prohibited | [Hewitt et al. 1973](https://www.ijcai.org/Proceedings/73/Papers/027B.pdf) |

**Core terminological hazard.** In 2024–2026 LLM discourse, "swarm" has become a marketing term for any multi-agent framework. Measured against the classical definition, [OpenAI's `openai/swarm`](https://github.com/openai/swarm) is an orchestrated MAS with heterogeneous roles and explicit handoffs; [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) is a hierarchical system branded as swarm intelligence; CrewAI explicitly models a corporate org chart. **None** of the production LLM frameworks reviewed satisfy the triple constraint of decentralization + homogeneity + emergence.

### 1.3 Stigmergy and indirect coordination

Stigmergy was coined by French entomologist Pierre-Paul Grassé in 1959 (*Insectes Sociaux* 6(1): 41–80) to resolve the "coordination paradox": how do insects of minimal individual intelligence, without apparent direct communication, collaboratively build complex nests? His answer: they communicate indirectly by modifying a shared medium (the nest itself).

[Theraulaz & Bonabeau's "A Brief History of Stigmergy" (*Artificial Life* 5(2), 1999)](https://pubmed.ncbi.nlm.nih.gov/10633572/) carries the concept into artificial-life research:

> "Stigmergy is a class of mechanisms that mediate animal-animal interactions. Its introduction in 1959 by Pierre-Paul Grassé made it possible to explain what had been until then considered paradoxical observations: In an insect society individuals work as if they were alone while their collective activities appear to be coordinated."

They distinguish **quantitative stigmergy** (intensity of a signal modulates behavior — the ant pheromone model) from **qualitative stigmergy** (the pattern of environmental state triggers a specific action type). Four operative properties: no direct communication; coordination emerges from cumulative environmental modification; self-organization without central control; the environment is simultaneously the communication medium and the work product.

**The ant-trail / pheromone canonical illustration.** Foraging ants deposit pheromone on paths to food. Each subsequent ant probabilistically follows the stronger-scented trail, adding pheromone. Shorter paths traverse faster and accumulate pheromone faster; longer paths evaporate before reinforcement. The colony converges on the shortest path **without any ant knowing the global route**. This is [Dorigo's Ant Colony Optimization (ACO) algorithm](https://jmvidal.cse.sc.edu/lib/bonabeau99a.html). The computational properties are: positive feedback (good solutions attract resources), negative feedback (evaporation), stochasticity (prevents premature convergence), emergence (the colony property, not any agent's).

### 1.4 Stigmergy mapped to AI agents — three concrete production examples

| Biological mechanism | AI/software equivalent |
|---|---|
| Pheromone trail | Message history in shared buffer |
| Nest material configuration | CLAUDE.md, project state files |
| Pheromone evaporation | LRU cache expiry, memory TTL |
| Trail reinforcement | Upvoting / memory importance scoring |
| Ant choosing path | Agent selecting task from blackboard |

**Example 1 — Claude Code / CLAUDE.md as stigmergic shared context.** [Anthropic's Claude Code memory documentation](https://docs.anthropic.com/en/docs/claude-code/memory) describes CLAUDE.md as *"markdown files that give Claude persistent instructions… Claude reads them at the start of every session."* Boris Cherny, creator of Claude Code, describes the team's practice in a [January 2026 Twitter thread](https://x.com/bcherny/status/2007179832300581177): *"Our team shares a single CLAUDE.md in the Claude Code repo. We commit it to git and contribute to it several times a week. Whenever Claude behaves incorrectly, we add a note to CLAUDE.md so it learns not to repeat the mistake."* His explicit rule ([Jitendra Zaa's synthesis of Cherny's tips](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)): *"After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."*

This is **quantitative stigmergy** in the strict sense: each agent invocation reads the CLAUDE.md, acts, and potentially writes back; no agent communicates directly with any prior agent; coordination — the accumulation of project knowledge, avoidance of repeated errors — emerges from cumulative environmental modification. CLAUDE.md follows a six-tier discovery hierarchy (managed policy → project root → `.claude/rules/*.md` → `~/.claude/CLAUDE.md` → `./CLAUDE.local.md` → auto-memory), with Claude Code walking up the directory tree to discover files ([Claude Code Advanced Patterns doc](https://resources.anthropic.com/hubfs/Claude%20Code%20Advanced%20Patterns_%20Subagents,%20MCP,%20and%20Scaling%20to%20Real%20Codebases.pdf)).

**Example 2 — CrewAI's shared memory system.** [CrewAI's unified memory](https://docs.crewai.com/en/concepts/memory) provides a `Memory` class shared across all agents in a crew: *"All agents in the crew share the crew's memory unless an agent has its own. After each task, the crew automatically extracts discrete facts from the task output and stores them. Before each task, the agent recalls relevant context from memory and injects it into the task prompt."* The TTL-based decay structure (short-term cache vs. long-term store) is the framework's closest analog to pheromone evaporation. CrewAI's memory is, design-wise, the most stigmergy-faithful of any current LLM framework — but task routing is still explicit (researcher→analyst→writer), so the emergent self-organization property is absent.

**Example 3 — ruvnet/claude-flow's SQLite pheromone store.** [claude-flow](https://github.com/ruvnet/claude-flow) implements *"Collective Memory: Shared knowledge, LRU cache, SQLite persistence with WAL"* with typed TTLs: `knowledge` (permanent), `context` (1h), `task` (30min), `result` (permanent), `error` (24h). The TTL schema explicitly mirrors pheromone evaporation. Agents share a "memory namespace"; a gossip protocol for dissemination is listed as *"Epidemic protocol dissemination | High partition tolerance | ~200ms | Eventually consistent."* This is the strongest mechanical analog to ant-pheromone stigmergy in production LLM systems — undermined by the queen-led control layer that replaces the decentralization requirement with hierarchical command.

The historical AI precedent is the **blackboard architecture** from [Barbara Hayes-Roth's "A Blackboard Architecture for Control" (*Artificial Intelligence* 26(3), 1985)](https://www.christopherdebeer.com/isnt-this-just-react.html), and Hearsay-II speech recognition. As [Christopher de Beer (2026) observes](https://www.christopherdebeer.com/isnt-this-just-react.html), the blackboard pattern *"had the right shape: shared state, independent observers, opportunistic activation. It failed for a specific reason: the knowledge sources were hand-coded pattern matchers. They could not tolerate ambiguity… Every implementation eventually reintroduced a scheduler — a centralized controller that selected which knowledge source to run next."* LLMs **resolve** this failure mode: they can interpret open-world state in natural language, selecting their own activations. This is why the blackboard pattern is quietly returning as the substrate for LLM multi-agent coordination.

### 1.5 The "replaceable agents" principle — evidence and caveat

Boris Cherny is widely credited with the claim that Claude Code agents are interchangeable. **One caveat documented up front**: extensive source searching — [Latent Space podcast (May 2025)](https://www.latent.space/p/claude-code), [Lenny's Newsletter (Feb 2026)](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens), [Every.to (Oct 2025)](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it), and his [Twitter threads](https://x.com/bcherny/status/2007179832300581177) — does not yield a verbatim Cherny quote using the words "interchangeable," "fungible," or "replaceable." The concept is inferred from a consistent set of verified practices:

From [Latent Space](https://www.latent.space/p/claude-code):

> "Something I'll do sometimes is if I have a planning question or a research type question, I'll ask Claude to investigate a few paths in parallel. And you can do this today if you just ask it. Say, I want to refactor X to do Y. Can you research three separate ideas for how to do it? Do it in parallel. Use three agents to do it." — Boris Cherny

From [Cherny's January 2026 Twitter thread](https://x.com/bcherny/status/2007179832300581177):

> "My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much. There is no one correct way to use Claude Code: we intentionally build it in a way that you can use it, customize it, and hack it however you like. **Each person on the Claude Code team uses it very differently.**"

From [Jitendra Zaa's synthesis of Cherny's tips](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/): *"Boris runs 5 instances of Claude Code simultaneously in his terminal using 5 separate git checkouts of the same repo… Each tab runs in its own git checkout, so Claude can make changes in parallel without conflicts."* And: *"Pour your energy into the plan so Claude can 1-shot the implementation."*

From [Every.to](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it) on subagent use: *"Cherny uses subagents—separate instances of Claude working in parallel—to catch issues before code gets merged, and he's discovered that making them challenge each other produces cleaner results… One checks style guidelines, another combs through the project's history, another flags obvious bugs… he uses five more subagents specifically tasked with poking holes in the original findings. 'In the end, the result is awesome,' he says, 'it finds all the real issues without the false [ones].'"*

These quotes support a **functional** interchangeability doctrine — any invocation can execute any well-specified task — even if the specific words "interchangeable agent" are not used.

### 1.6 What must be shared for interchangeability to work

For an agent invocation to be effectively fungible, the coordination state must be **external to the agent's context window**:

| State component | Mechanism | Source |
|---|---|---|
| Project conventions, coding standards | `CLAUDE.md` (git-tracked) | [Anthropic docs](https://docs.anthropic.com/en/docs/claude-code/memory) |
| Tool permissions, MCP configuration | `.claude/settings.json` (git-tracked) | [Cherny tips](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/) |
| Slash commands / workflows | `.claude/commands/` (git-tracked) | [Cherny tips](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/) |
| Subagent definitions | `.claude/agents/*.md` | [Advanced Patterns doc](https://resources.anthropic.com/hubfs/Claude%20Code%20Advanced%20Patterns_%20Subagents,%20MCP,%20and%20Scaling%20to%20Real%20Codebases.pdf) |
| Working directory / file state | Git worktree or shared checkout | [Cherny tips](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/) |
| Git history and branch state | Git repository | [Anthropic multi-agent blog](https://www.anthropic.com/engineering/built-multi-agent-research-system) |
| Implementation plan | Plan mode output written to file | [Every.to](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it) |
| Accumulated corrections | Auto-memory / CLAUDE.md entries | [Cherny tips](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/) |

[Anthropic's multi-agent research system engineering blog](https://www.anthropic.com/engineering/built-multi-agent-research-system) flags the fragility when context is **not** shared: *"some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today."* This matters directly for Jetix: if your 12 agents each hold role-specific context in their own prompts, you have the worst of both worlds — coordination overhead without shared-environment benefits.

### 1.7 Fungible-agent pattern vs role-specialized pattern

| Dimension | Fungible agent pattern (Claude Code) | Role-specialized pattern (CrewAI) |
|---|---|---|
| Agent identity | Ephemeral; any invocation can execute any task | Persistent; each agent has a fixed role |
| Context carrier | External (CLAUDE.md + filesystem) | Internal (system prompt per agent) |
| Coordination | Stigmergic (shared file/memory state) | Direct delegation (orchestrator assigns) |
| Failure mode | Any agent can be restarted without state loss | Role gaps require workflow redesign |
| Emergent behavior | Possible | Limited (fixed role scripts) |
| Best for | Exploration, parallel trials, code migration | Defined pipelines with stable decomposition |

[Anthropic's own Research architecture](https://www.anthropic.com/engineering/built-multi-agent-research-system) is a **hybrid**: a lead agent (heterogeneous, planner) coordinates a *single* type of subagent launched in parallel with different task descriptions. The subagents are homogeneous-and-fungible; the lead is specialized. This is the empirically dominant production pattern (see Section 4).

---

## Section 2 — Framework Comparison Matrix

### 2.1 Full comparison matrix

| Framework | Coordination Primitive | Shared State | Replaceability | Production Readiness | License | GitHub Stars ~Apr 2026 | Actively Maintained? |
|---|---|---|---|---|---|---|---|
| **Microsoft AutoGen v0.4** | Async message passing (Core); team patterns — `RoundRobinGroupChat`, `SelectorGroupChat`, `Swarm` + handoff messages (AgentChat) | Broadcast context; shared message list | Moderate — `SelectorGroupChat` picks next dynamically | High; v0.7.5 (Sep 2025); successor "Microsoft Agent Framework" | MIT (code), CC-BY-4.0 (docs) | ~57.2k | In maintenance mode post-AG2 fork |
| **CrewAI** | Role-based task delegation via `Process.sequential` or `Process.hierarchical` | Implicit task-output chaining; SQLite + RAG memory | Low-moderate; fixed roles | Medium-High; v1.9.3 (Jan 2026) | MIT | ~44.6k | Yes |
| **LangGraph** | `StateGraph` with typed nodes, edges, `Command`, `Send`, `interrupt` | `TypedDict`/Pydantic state with annotated reducers; `Checkpointer` | Very high; nodes are functions | Very High; v1.1.8 (Apr 2026); LangSmith | MIT | ~29.8k | Yes (very active) |
| **Anthropic MCP** | **Not a coordination framework** — JSON-RPC 2.0 protocol for tool/resource sharing | Protocol-level only | N/A | High as a protocol; widespread | MIT (spec) | N/A (spec) | Yes |
| **OpenAI Swarm** | `handoffs` (agent returns another `Agent`); `context_variables` dict | Stateless per call; context dict | High; soft roles | **Not for production**; deprecated | MIT | ~20.6k (archived) | No — Agents SDK is successor |
| **OpenAI Agents SDK** | Handoffs; `Runner` loop; Guardrails; Sessions | Sessions; `context_variables`; Responses API state | Very high | Very High; v0.4.2 (Oct 2025); [Temporal GA Mar 2026](https://temporal.io/blog/announcing-openai-agents-sdk-integration) | MIT | ~16.9k | Yes |
| **Claude Agent SDK** | `query()` + agent loop; `AgentDefinition` subagents via `Agent` tool; Hooks | Context isolation per subagent; parent sees only final summary | Moderate; LLM-mediated dispatch | High; v0.1.19 (Jan 2026) | MIT | ~4k | Yes |
| **MetaGPT** | Pub/sub via `Environment`; `_watch([Action])` + `publish_message()`; SOPs | `Environment` message bus; role-local `Memory` | Low; strongly typed roles | Medium (declining); v0.8.1 (Apr 2024), last commit Jun 2025 | MIT | ~57.4k | Slowing |
| **AutoGPT (legacy)** | Single-agent goal-decomposition loop (classic); visual node workflow editor (Platform) | Monolithic (classic); typed node outputs (Platform) | N/A (classic); fixed types (Platform) | Classic: deprecated; Platform: beta v0.6.34 (Oct 2025) | MIT (classic); Polyform Shield (platform) | ~179k | Platform yes; classic deprecated |

### 2.2 Per-framework notes relevant to the Jetix decision

**AutoGen v0.4.** [Microsoft AutoGen](https://github.com/microsoft/autogen) v0.4 introduced a two-layer architecture: a Core API for async message passing, and an AgentChat layer with team patterns. The v0.4 redesign explicitly moved away from the v0.2 `GroupChatManager` god-object toward modular teams. `SelectorGroupChat` is a centralized selector with LLM-based routing; `RoundRobinGroupChat` is rigid; the `Swarm` team uses handoff messages between named peers. The Microsoft GitHub notes the project is [*"now in maintenance mode"*](https://github.com/microsoft/autogen) with a successor called "Microsoft Agent Framework" positioned for enterprise LTS — relevant for Jetix because it signals AutoGen is not the long-term direction for Microsoft's own production work.

**CrewAI.** [CrewAI](https://docs.crewai.com/introduction) is unambiguously hierarchical. It models a corporate org chart: roles, manager, tasks, delegation. In sequential mode, output of each task becomes context for the next — a simple pipeline. In hierarchical mode, a manager LLM allocates tasks at runtime based on agent capabilities. [Flows](https://docs.crewai.com/introduction) sit above Crews for explicit state management and branching. For Jetix's 12-agent design, CrewAI's hierarchical process most closely matches what is currently built — and it is precisely what the Kim et al. (2025) study identifies as a failure profile: rigid role assignment with coordination overhead.

**LangGraph.** [LangGraph](https://langchain-ai.github.io/langgraph/) is the only framework reviewed that is *"neither a swarm nor a strict hierarchy"* — it is a general-purpose graph orchestration primitive. A developer explicitly encodes the topology: a star graph with a supervisor is hierarchical; a fully connected graph is flat. The typed `TypedDict` state with annotated reducers (`Annotated[list, add_messages]`) plus `Checkpointer` persistence is the production-strongest feature set. [v1.1.8 released April 17, 2026](https://github.com/langchain-ai/langgraph). It leads in monthly searches among multi-agent frameworks. LangGraph's value proposition is **maximum structural control at the cost of requiring you to design the graph**.

**Anthropic MCP.** [The Model Context Protocol](https://modelcontextprotocol.io/introduction) is a **JSON-RPC 2.0 protocol for tool/resource/prompt sharing**, not a coordination framework. The [architecture spec](https://modelcontextprotocol.io/docs/concepts/architecture) is explicit: *"MCP focuses solely on the protocol for context exchange — it does not dictate how AI applications use LLMs or manage the provided context."* Every other framework sits on top of MCP. AutoGen v0.4 ships `McpWorkbench`; the Claude Agent SDK supports `mcpServers`; OpenAI Agents SDK has built-in MCP tool calling; LangGraph supports MCP tools via LangChain integration. MCP is the USB-C port of agent tool integration — a horizontal layer, not a competitor to the coordination frameworks. Conflating MCP with multi-agent frameworks is one of the most common errors in current discourse.

**OpenAI Swarm.** [Released October 2024](https://github.com/openai/swarm), Swarm is the smallest, clearest statement of the handoff pattern. The README: *"Swarm focuses on making agent coordination and execution lightweight, highly controllable, and easily testable. It accomplishes this through two primitive abstractions: Agents and handoffs."* An agent hands off by returning another `Agent` from a tool function. [Researcher Shyamal Anadkat was explicit on release](https://venturebeat.com/ai/openai-unveils-experimental-swarm-framework-igniting-debate-on-ai-driven-automation): *"Swarm is not an official OpenAI product. Think of it more like a cookbook. It's experimental code for building simple agents. It's not meant for production and won't be maintained by us."* The GitHub repo now carries a banner: *"Swarm is now replaced by the OpenAI Agents SDK."*

**OpenAI Agents SDK.** [Launched March 11, 2025](https://www.infoq.com/news/2025/03/openai-responses-api-agents-sdk/) as the production-ready evolution of Swarm, with four core primitives: **Agents**, **Handoffs**, **Guardrails**, and **Sessions**. Retains Swarm's handoff semantics plus a real runtime (tracing, guardrails, session memory, MCP tool calling). The [Temporal integration became GA in March 2026](https://temporal.io/blog/announcing-openai-agents-sdk-integration) for durable execution. OpenAI [updated it in April 2026](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/) with enterprise sandbox and safety harness capabilities. Supports both flat (handoff) and hierarchical (manager) orchestration.

**Claude Agent SDK.** The [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) (formerly Claude Code SDK, renamed late 2025) exposes Claude's own agent loop as a library. The key primitive is **subagents** defined via `AgentDefinition`, each running in its own fresh context window — intermediate work stays isolated, only the final summary returns to the parent. The `Agent` tool must appear in `allowedTools` for subagent invocation to occur. **Hooks** provide deterministic pre/post processing (`PreToolUse`, etc.). The SDK wraps the Claude Code CLI as a subprocess, which adds deployment complexity. For Jetix this is the most directly relevant framework — it implements the Claude Code stigmergic pattern as a programmable library.

**MetaGPT.** [MetaGPT](https://github.com/geekan/MetaGPT) encodes *"Code = SOP(Team)"* — a software-company simulation using pub/sub via an `Environment` message bus. Roles `_watch([ActionClass])` and `publish_message()`. Strongly typed roles (ProductManager, Architect, Engineer, QA) with fixed Action associations. Python 3.9–3.11 only. [Last release v0.8.1 was April 2024](https://github.com/geekan/MetaGPT); last commit June 2025. Its historical 57k stars reflect the early-2023 viral moment, not current velocity. For Jetix, MetaGPT's pattern (strict pipeline, non-interchangeable roles) is structurally similar to the current 12-agent hierarchy — and Kim et al. show this is one of the weakest architectures under realistic token budgets.

**AutoGPT.** The [original 2023 AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) was a single-agent goal-decomposition loop — deprecated. The current project is **AutoGPT Platform**, a visual node-based workflow editor under the Polyform Shield license (source-available, commercial use restricted). The 179k stars are historical viral impact, not current technical leadership.

### 2.3 OpenAI Swarm — design choices and legacy

OpenAI released Swarm to GitHub on [October 11, 2024](https://github.com/openai/swarm), without a formal announcement. Shyamal Anadkat preemptively set expectations on X: educational, not for production. The README articulates a clear design philosophy:

> "Swarm focuses on making agent coordination and execution lightweight, highly controllable, and easily testable… It accomplishes this through two primitive abstractions: Agents and handoffs. These primitives are powerful enough to express rich dynamics between tools and networks of agents."

> "Approaches similar to Swarm are best suited for situations dealing with a large number of independent capabilities and instructions that are difficult to encode into a single prompt."

The four explicit design choices: **ergonomic** (agents are plain Python classes), **lightweight** (thin wrapper over Chat Completions), **stateless** (`client.run()` does not persist state; caller manages history), **educational** (not production).

**Current status (April 2026).** Swarm is functionally deprecated. The repo banner directs users to the OpenAI Agents SDK. The [Mem0 review summarizes](https://mem0.ai/blog/openai-agents-sdk-review): *"Agents SDK was launched in March 2025 as a production-ready evolution of OpenAI's experimental Swarm project."* The repo is not formally "archived" on GitHub but maintenance has ceased.

**What Swarm contributed that carries forward.** Four patterns now standard across the ecosystem:

1. **Routines as patterns** — multi-agent behavior decomposed into composable routines rather than monolithic prompts.
2. **Handoff semantics** — transfer of control as a typed return value. Agents SDK `handoffs=[...]`, AutoGen `HandoffMessage`, and the Claude Agent SDK's `Agent` tool are direct descendants.
3. **Lightweight agent definitions** — an agent is instructions + tools, not a class hierarchy.
4. **Testability as first-class** — statelessness forces unit-testable design.

---

## Section 3 — Empirical Performance: Swarm vs Sequential

### 3.1 The core finding: architecture-task alignment dominates

The strongest meta-finding from 2023–2025 research is that **multi-agent architecture is neither universally superior nor universally inferior**. Its value is determined by task structure. The landmark December 2025 study [Kim et al., "Towards a Science of Scaling Agent Systems" (arXiv:2512.08296)](https://arxiv.org/abs/2512.08296) tested 260 configurations across five architectures (Single, Independent, Centralized, Decentralized, Hybrid), three LLM families, and six benchmarks. The headline result: multi-agent relative performance ranged from **+80.8%** on decomposable financial reasoning to **−70.0%** on sequential planning. The aggregate mean improvement was **−3.5%** (95% CI: [−18.6%, +25.7%], σ = 45.2%) — meaning the average multi-agent deployment **underperformed** a single agent.

This is the most important empirical data point in this report. If your default prior is that "more agents = better," the population data says you are more likely to be wrong than right.

### 3.2 Where multi-agent wins

| Task Type | Best Architecture | Evidence |
|---|---|---|
| Breadth-first research (web, multi-source) | Hierarchical orchestrator + parallel subagents | [Anthropic 2025](https://www.anthropic.com/engineering/built-multi-agent-research-system): +90.2% vs single-agent |
| Multi-turn factual QA / biography | Multi-agent debate (3–5 agents) | [Du et al. 2023](https://arxiv.org/abs/2305.14325): +7–15 pp on bio, math, MMLU |
| Hard mathematical reasoning | Debate / ensemble | Du et al.: +14.8 pp arithmetic; [Li et al.](https://arxiv.org/abs/2402.05120): up to +20% on MATH |
| Structured software development | Sequential pipeline with SOPs | [MetaGPT](https://arxiv.org/abs/2308.00352): 85.9% HumanEval Pass@1 |
| Small end-to-end software projects | Role-specialized multi-agent company | [ChatDev](https://arxiv.org/abs/2307.07924): $0.30/project, 86.66% flawless |
| ML engineering competitions | Ensemble agent systems | [MLE-Bench](https://openai.com/index/mle-bench/): Neo 34.2% vs AIDE 8.6% |
| High-volume parallel clinical tasks | Centralized MAS | [PubMed 2025](https://pubmed.ncbi.nlm.nih.gov/40894146/): 65.3% vs 16.6% at 80-task load |
| Decomposable financial analysis | Centralized MAS | Kim et al.: +80.8% vs single |

[Anthropic's Research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) is the strongest production data point: *"A multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval."* The mechanism is parallelizing breadth-first search across separate context windows.

The [Du et al. multi-agent debate paper](https://arxiv.org/abs/2305.14325) shows three agents in two rounds beating single agents substantially:

| Benchmark | Single Agent | Multi-Agent Debate | Gain |
|---|---|---|---|
| Arithmetic | 67.0% | **81.8%** | +14.8 pp |
| GSM8K | 77.0% | **85.0%** | +8.0 pp |
| Biography factuality | 66.0% | **73.8%** | +7.8 pp |
| MMLU | 63.9% | **71.1%** | +7.2 pp |
| Chess Move Validity | 29.3% | **45.2%** | +15.9 pp |

Debate reduced hallucinations on all factuality tasks.

### 3.3 Where multi-agent loses

| Task Type | Best Architecture | Evidence |
|---|---|---|
| Sequential planning | Single agent | [Kim et al.](https://arxiv.org/abs/2512.08296): MAS degrades 39–70% |
| Tool-heavy workflows (>10 tools) | Single agent | Kim et al.: 2–6× efficiency penalty |
| GitHub issue resolution (SWE-bench) | Single agent (emergent) | [Emergent Mind](https://www.emergentmind.com/topics/swe-bench-leaderboards): single 73.2% vs multi 62.2% |
| Tasks where single agent already >45% | Single agent | Kim et al.: negative returns past the capability ceiling |

[Anthropic concurs](https://www.anthropic.com/engineering/built-multi-agent-research-system): *"most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time."*

The **Rule of 4** is critical for Jetix. [Kim et al. find](https://arxiv.org/abs/2512.08296) that the "45% capability ceiling" is the most robust predictor in their study (β = −0.408, p < 0.001): when a single agent achieves ~45% accuracy on a task, **adding more agents typically yields negative returns**. The coordination overhead exceeds the marginal value of additional reasoning. On tool-heavy workflows (~16 tools), every multi-agent configuration underperformed single agents (β = −0.330, p < 0.001).

[The MAST study (Cemri et al., arXiv:2503.13657)](https://arxiv.org/abs/2503.13657) analyzed 1,600+ traces across 7 MAS frameworks and found: *"despite enthusiasm for Multi-Agent LLM Systems, their performance gains on popular benchmarks are often minimal."* ChatDev's success rate on ProgramDev was only **33.33%** (67% failure).

### 3.4 Cost dynamics — the verbatim "15×" source

The authoritative first-party source is [Anthropic's "How we built our multi-agent research system" (June 13, 2025)](https://www.anthropic.com/engineering/built-multi-agent-research-system):

> "In our data, agents typically use about **4× more tokens than chat interactions**, and **multi-agent systems use about 15× more tokens than chats**."

This is Anthropic's own production measurement from deploying the Claude Research feature. The same post adds:

> "Token usage by itself explains **80% of the variance**, with the number of tool calls and the model choice as the two other explanatory factors."

The multiplier is relative to a chat baseline, not a single-agent API call. Decomposing: ~1× chat, ~4× single agent, ~15× multi-agent research. In Anthropic's architecture, the lead agent spawns 3–10 subagents, each running 3–15 tool calls.

Corroborating evidence:

- [MacNet scaling (Qian et al.)](https://arxiv.org/abs/2406.07155): *"Token length increased by 7.51 times when scaling from 2⁰ (1 agent) to 2⁴ (16 agents)"* — consistent with a 15× ceiling for larger swarms.
- [Kim et al.](https://arxiv.org/abs/2512.08296) measured token efficiency: single agents 67 tasks/1,000 tokens; centralized multi-agent 21 tasks/1,000 tokens (3.2× penalty); hybrid teams 14 tasks/1,000 tokens (4.8× penalty).
- [GAIA leaderboard](https://hal.cs.princeton.edu/gaia): HF Open Deep Research with Claude Opus 4 costs **$1,686 for 165 questions** ($10.22/question) vs. the HAL Generalist Agent at $178 — a 9.4× orchestration overhead.

### 3.5 Coordination overhead — the sweet-spot curve

[Qian et al. "Scaling Large Language Model-based Multi-Agent Collaboration" (arXiv:2406.07155, ICLR 2025)](https://arxiv.org/abs/2406.07155) is the most rigorous agent-scaling study. They tested 1 to 64+ agents in DAG topologies and identified a **logistic scaling law**:

\[
f(|\mathcal{V}|) = \frac{\gamma}{1 + e^{-\beta (\log |\mathcal{V}| - \alpha)}} + \delta
\]

Three phases: slow growth (1–8 agents), rapid improvement (~16 agents), saturation (32+, plateau at ~100). The study endorses **2⁴ = 16 nodes** as "a reasonable choice" balancing performance and cost.

[Kim et al.](https://arxiv.org/abs/2512.08296) push this further with the **Rule of 4** — under current token economics, effective team sizes peak at **3–4 agents**:

> "The effective limit of multi-agent systems arises from the fact that agents presently communicate in a dense, resource-heavy manner."

Empirical team sizes from deployed systems:

| System | Team Composition | Size | Domain |
|---|---|---|---|
| [MetaGPT](https://arxiv.org/abs/2308.00352) | PM, Architect, Engineer, QA | 5 | Software development |
| [ChatDev](https://arxiv.org/abs/2307.07924) | CEO, CTO, Programmer, Reviewer, Tester | 5 | Small software projects |
| Anthropic Research | Lead Opus + Sonnet subagents | 3–10 | Breadth-first research |
| [Agent Forest (Li et al.)](https://arxiv.org/abs/2402.05120) | Sampling ensemble | Up to 40 | GSM8K/MATH/HumanEval |
| MacNet | DAG topology | 16 (sweet spot) | Coding, QA |

**Implication for Jetix.** A 12-agent fixed hierarchy sits past the Rule of 4 knee, below the MacNet sweet spot of 16, and above the ChatDev/MetaGPT norm. Worse, it is heterogeneous (CEO→Manager→Leads→Workers), which compounds coordination cost.

### 3.6 Compound errors — the 17.2× amplification factor

Error compounding in multi-agent pipelines follows basic probability: for uniform per-step accuracy p and N steps, P(success) = p^N.

| Per-step accuracy (p) | N = 5 steps | N = 10 steps |
|---|---|---|
| 95% | 77% | 59% |
| 90% | 59% | 35% |
| 85% | 44% | 20% |
| 80% | 33% | 11% |

But empirical rates are worse because errors are **not independent** — [Sinha et al. (arXiv:2509.09677)](https://arxiv.org/abs/2509.09677) show LLMs self-condition on their own hallucinations in the context window.

**The 17.2× amplification factor (Kim et al. 2025).** Independent multi-agent systems (no centralized verification) amplify errors **17.2×** relative to the single-agent baseline. Centralized architectures with validation checkpoints contain this to **4.4×**. Concretely: if a single agent has a 5% error rate, an independent multi-agent system can exhibit an error rate approaching **86%** (5% × 17.2).

**The MAST failure taxonomy.** [Cemri et al.](https://arxiv.org/abs/2503.13657) annotated 1,600+ traces and identified 14 failure modes:

- **Specification Issues (41.77%)**: Step repetition 17.14% (most common single mode), disobey task spec 10.98%, unaware of termination 9.82%.
- **Inter-Agent Misalignment (36.94%)**: Reasoning-action mismatch 13.98%, fail to ask for clarification 11.65%, task derailment 7.15%.
- **Task Verification (21.30%)**: Premature termination 7.82%, no/incomplete verification 6.82%, incorrect verification 6.66%.

**Wand.ai production measurement.** A 1% per-token error rate compounds to **87% cumulative failure by token 200** ([Zartis analysis](https://www.zartis.com/the-compounding-errors-problem-why-multi-agent-systems-fail-and-the-architecture-that-fixes-it/)).

**Direct single-vs-multi comparisons where multi-agent loses.** Three:

- SWE-bench Verified: emergent single-agent 73.2% (Group G6); emergent multi-agent 62.2% (Group G7) — **11 pp deficit** ([Emergent Mind](https://www.emergentmind.com/topics/swe-bench-leaderboards)).
- PlanCraft (Minecraft-style planning): every multi-agent configuration performed worse by **39–70%** ([Kim et al.](https://arxiv.org/abs/2512.08296)).
- The [Cognition "Flappy Bird" case](https://cognition.ai/blog/dont-build-multi-agents) — quoted in full in Section 4 — describes subagent 1 building Super Mario Bros while subagent 2 builds a non-game-asset bird.

**Context contamination from Anthropic production.** [Anthropic's engineering post](https://www.anthropic.com/engineering/built-multi-agent-research-system) documents agents *"spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates."* Early agents showed path-dependency: *"one subagent explored the 2021 automotive chip crisis while 2 others duplicated work investigating current 2025 supply chains."*

**Mitigations that work:**

| Configuration | Error amplification vs single agent |
|---|---|
| Single agent (baseline) | 1.0× |
| Independent MAS (no verification) | **17.2×** |
| Centralized MAS (validation checkpoints) | **4.4×** |
| Consensus voting (n=5, p=0.05 error) | **0.022×** (0.11% error) |
| Six Sigma Agent (13-agent DAG consensus) | 3.4 defects / million opportunities |
| Inspector pattern (closed loop) | 96.4% error recovery |

The takeaway is operationally precise: **verification architecture matters more than agent count**. A 3-agent system with a dedicated verifier beats a 12-agent system without one.

---

## Section 4 — Production Deployments

### 4.1 Named production systems with quantitative results

| Company / Product | Architecture | Deployment | Key Results | Source |
|---|---|---|---|---|
| **Anthropic Claude Research** | Orchestrator-worker: 1 Opus 4 lead + parallel Sonnet 4 subagents | Customer-facing | +90.2% vs single-agent; 15× token cost; up to 90% time reduction on complex queries | [Anthropic Engineering](https://www.anthropic.com/engineering/built-multi-agent-research-system) |
| **Cognition Devin** | Single-thread primary + limited verification sub-agents + IDE sandbox | Customer-facing | 13.86% SWE-bench (7× prior SOTA); Devin 2.0 completes 83% more junior tasks per ACU | [SWE-bench Technical Report](https://cognition.ai/blog/swe-bench-technical-report); [Devin 2.0](https://cognition.ai/blog/devin-2) |
| **Cursor 2.0 Composer + Agent Mode** | Up to 8 parallel agents with Git worktree isolation; Architect → Planner → Implementers | Customer-facing | Composer 4× faster; 15-hr sequential workloads collapse to ~3 hrs | [Cursor 2.0 Guide](https://www.digitalapplied.com/blog/cursor-2-0-agent-first-architecture-guide) |
| **Replit Agent** | Manager → Editor agents → Verifier (hierarchical, human-in-loop) | Customer-facing | Hundreds of thousands of production runs since Sept 2024; ~90% tool-call success | [LangChain case study](https://www.langchain.com/breakoutagents/replit) |
| **Factory AI Droids** | Coordinator + role-scoped specialist droids (Code/Review/Docs/Test/Knowledge) | Customer-facing | Parallel droid sessions in isolated sandboxes; Knowledge Droid as shared memory layer | [NEA blog](https://www.nea.com/blog/factory-the-platform-for-agent-native-development) |
| **Sierra (Taylor/Bavor)** | Supervisor-LLM over primary conversational agent; "Agent OS" | Customer-facing | 70%+ resolution rate in production at SiriusXM, Weight Watchers, OluKai | [Sequoia Training Data podcast](https://sequoiacap.com/podcast/training-data-clay-bavor/) |
| **Decagon** | Single conversation agent with tool access | Customer-facing | $1.5B valuation; ~80% avg deflection; Duolingo >80%; Bilt 70% of 60K monthly tickets | [SaaStr](https://www.saastr.com/ai-wont-so-much-replace-sales-reps-as-deflect-them-what-supports-70-deflection-rates-tell-us-about-sales-future/) |
| **Parloa** | Multi-agent CX for auth/lookup/escalation under one conversation state | Customer-facing | 71.4% call containment; enterprise voice + digital at millions conv/month | [Parloa blog](https://www.parloa.com/blog/ai-agent-lifecycle-customer-service/) |
| **Harvey AI** | Multi-agent workflow platform; Agent Builder | Customer-facing (legal) | 400K+ agentic queries/day; 25,000+ workflows built; 20M+ terms extracted | [Harvey Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder) |
| **GitHub Copilot Agent Mode** | Single-agent IDE loop; separate async Coding Agent via GitHub Actions | Customer-facing | 20M+ Copilot users; Coding Agent opens draft PRs autonomously | [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/) |
| **CrewAI customers** | Hierarchical manager + role-defined crew | Framework + platform | 2B agentic executions in 12 months; Big Four firm 10%→70%+ accuracy; BPO QA 74 hrs→3 hrs | [CrewAI LinkedIn](https://www.linkedin.com/posts/joaomdmoura_2025-was-a-defining-year-for-crewai-we-activity-7414398929120878592-bdzW) |
| **Sourcegraph Amp** | Single agentic loop + Sonnet 4 sub-agents for large token tasks | Customer-facing | Multi-model; sub-agents have "MASSIVE impact" on tokens at enterprise scale | [ZenML case study](https://www.zenml.io/llmops-database/building-production-ai-coding-assistants-and-agents-at-scale) |
| **OpenHands / OpenDevin** | ReAct single agent + pluggable LLM backends | Open-source | 64.4k GitHub stars; ICLR 2025; Claude Sonnet 4.5 recommended | [GitHub](https://github.com/All-Hands-AI/OpenHands) |

The internal-vs-customer-facing split matters. **Customer-facing**: Claude Research, Devin, Cursor, Replit Agent, GitHub Copilot, Factory Droids, Sierra, Decagon, Parloa, Harvey, Relevance AI, Sourcegraph Amp. **Internal tooling / platform**: CrewAI (open-source framework used in 2B executions/year by enterprise), OpenHands (open-source). Every customer-facing system has a verification loop.

### 4.2 Devin's internal architecture — the strongest anti-swarm argument

Cognition AI (founded by Scott Wu, Russell Kaplan, Kieran Klassen, Steve Hsu) launched Devin publicly March 2024. The company is valued $4B+ and uses Devin internally to build Devin ("recursive eating its own cooking").

**Original benchmarks.** [The SWE-bench Technical Report](https://cognition.ai/blog/swe-bench-technical-report): 13.86% end-to-end resolution on SWE-bench (570/2294 sample) vs. previous SOTA 1.96% — a 7× improvement. 72% of passing tests took over 10 minutes. In test-driven development mode: 23% success on 100 sampled tests. Devin is given 45 minutes and navigates the full repo autonomously with no file hints.

**Devin 2.0 (April 2025).** [Devin 2.0 announcement](https://cognition.ai/blog/devin-2) introduced parallel Devin instances (each in its own cloud IDE), Interactive Planning (proactive codebase research producing editable preliminary plans), Devin Search / Devin Wiki (agentic exploration with auto-indexed architecture diagrams). Pricing dropped from $500/month to **$20/month Core** with per-ACU at $2.00–$2.25. **83% more junior tasks completed per ACU** vs. Devin 1.x.

**Devin 2.2 (Feb 2026).** Adds computer use for testing, self-verification, auto-fix of own PRs, 3× faster session startup.

**The "Don't Build Multi-Agents" doctrine.** The most architecturally important Cognition document is [Walden Yan's "Don't Build Multi-Agents" (June 12, 2025)](https://cognition.ai/blog/dont-build-multi-agents). Its two principles:

> **Principle 1:** "Share context, and share full agent traces, not just individual messages."
>
> **Principle 2:** "Actions carry implicit decisions, and conflicting decisions carry bad results."

The Flappy Bird failure case:

> "Suppose your **Task** is 'build a Flappy Bird clone'. This gets divided into **Subtask 1** 'build a moving game background with green pipes and hit boxes' and **Subtask 2** 'build a bird that you can move up and down'. It turns out subagent 1 actually mistook your subtask and started building a background that looks like Super Mario Bros. Subagent 2 built you a bird, but it doesn't look like a game asset and it moves nothing like the one in Flappy Bird. Now the final agent is left with the undesirable task of combining these two miscommunications."

Yan's core critique of parallel multi-agent:

> "In 2025, running multiple agents in collaboration only results in fragile systems. The decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough between the agents. At the moment, I don't see anyone putting a dedicated effort to solving this difficult cross-agent context-passing problem."

Cognition's answer:

> "The simplest way to follow the principles is to just use a single-threaded linear agent: Here, the context is continuous. However, you might run into issues for very large tasks with so many subparts that context windows start to overflow."
>
> "In this world, we introduce a new LLM model whose key purpose is to compress a history of actions & conversation into key details, events, and decisions. This is hard to get right. It takes investment into figuring out what ends up being the key information and creating a system that is good at this. Depending on the domain, you might even consider fine-tuning a smaller model **(this is in fact something we've done at Cognition)**."

Even Claude Code's subagents earn measured approval from Yan — with a caveat:

> "Claude Code is an example of an agent that spawns subtasks. However, it **never does work in parallel** with the subtask agent, and the subtask agent is usually only tasked with answering a question, **not writing any code**. Why? The subtask agent lacks context from the main agent that would otherwise be needed to do anything beyond answering a well-defined question."

**Devin's actual graph, in plain language:** single-thread primary agent with linear context, fine-tuned compression model for long contexts, limited read-only sub-queries, and parallel independent Devin instances on separate tasks (not collaborating subagents on a single task). This is the anti-swarm position argued from 13.86% → SOTA on the hardest coding benchmark.

### 4.3 Anthropic's 2024–2026 multi-agent research — four canonical posts

**1. [Erik Schluntz & Barry Zhang, "Building effective agents" (Dec 19, 2024)](https://www.anthropic.com/engineering/building-effective-agents).** The foundational taxonomy post. Defines workflows vs agents:

> "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."

Enumerates five canonical workflow patterns: **Prompt chaining, Routing, Parallelization (sectioning + voting), Orchestrator-workers, Evaluator-optimizer**. On orchestrator-workers: *"A central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results… the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."* Core principle: *"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."* The three design principles: simplicity, transparency, and **agent-computer interface (ACI)** — the insight that tool documentation matters as much as the system prompt (*"We actually spent more time optimizing our tools than the overall prompt"* in SWE-bench work).

**2. [Jeremy Hadfield et al., "How we built our multi-agent research system" (June 13, 2025)](https://www.anthropic.com/engineering/built-multi-agent-research-system).** The production orchestrator-worker case study. Key findings:

- Architecture: lead agent (Opus 4) decomposes queries, spawns Sonnet 4 subagents in parallel; each subagent has its own context window.
- **+90.2% over single-agent Opus 4** on internal research eval.
- **80% of BrowseComp performance variance explained by token usage**; tool calls and model choice explain the rest.
- **15× multi-agent token cost** vs chat; **4× for single-agent**.
- Parallelization *"cut research time by up to 90%"* for complex queries.
- **Self-improving tools**: a tool-testing agent that rewrote MCP tool descriptions *"resulted in a 40% decrease in task completion time for future agents."*
- Artifact pattern: *"Rather than requiring subagents to communicate everything through the lead agent, implement artifact systems where specialized agents can create outputs that persist independently… This prevents information loss during multi-stage processing and reduces token overhead from copying large outputs through conversation history."*
- Current limitation: *"Currently, our lead agents execute subagents synchronously… This simplifies coordination, but creates bottlenecks."*
- Production pattern — rainbow deployments: *"We use rainbow deployments to avoid disrupting running agents, by gradually shifting traffic from old to new versions while keeping both running simultaneously."*

**3. [Prithvi Rajasekaran et al., "Effective context engineering for AI agents" (Sept 29, 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).** Context engineering as the successor discipline to prompt engineering:

> "The set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference."

**Context rot:** *"As the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases."* (Attributed to n² attention relationships.) Guiding principle: *"Find the **smallest possible set of high-signal tokens** that maximize the likelihood of some desired outcome."* Three techniques for long-horizon tasks: **compaction** (summarize and reinitiate — Claude Code preserves *"architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs"*), **structured note-taking** (persistent memory outside the context window — the NOTES.md pattern), and **sub-agent architectures** where each subagent *"returns only a condensed, distilled summary of its work (often 1,000–2,000 tokens)."*

Claude Code's hybrid retrieval: CLAUDE.md loaded upfront, glob/grep for just-in-time file retrieval — *"effectively bypassing the issues of stale indexing."*

**4. [Anthropic, "Claude Code: Best Practices for Agentic Coding" (April 3, 2026)](https://www.anthropic.com/engineering/claude-code-best-practices).** Key findings:

- *"Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills."*
- **Subagents as first-class primitive** — `.claude/agents/` files with their own model/tools/prompt.
- **Verification loop**: *"Claude performs dramatically better when it can verify its own work"* (tests, screenshots, linter).
- **Explore → Plan → Implement** workflow; separate Plan Mode (read-only) from Normal Mode.
- **Fan-out automation**: `claude -p "Migrate $file"` in a shell loop — 2,000 Python files can be migrated in parallel invocations.
- Key antipattern: *"The kitchen sink session"* — mixed tasks pollute context; `/clear` frequently.

---

## Section 5 — Design Patterns

### 5.1 The replaceable-agent implementation patterns that work

Synthesizing Cherny's practices with Anthropic's production findings, four patterns make agent interchangeability practical:

**1. Shared filesystem + idempotent operations.** Each agent invocation operates on the same git repository (or a worktree). File writes by one are visible to subsequent agents. Operations — writing a file, running a test suite, pushing a commit — are idempotent and safe to retry. Cherny: *"I use git worktrees. Create isolated working directories from the same repo: `claude --worktree`. Each Claude instance operates on a different worktree, avoiding file conflict."* ([Advanced Patterns](https://resources.anthropic.com/hubfs/Claude%20Code%20Advanced%20Patterns_%20Subagents,%20MCP,%20and%20Scaling%20to%20Real%20Codebases.pdf))

**2. Declarative task specs in CLAUDE.md and plan files.** Agents receive instructions via CLAUDE.md (permanent conventions) and plan-mode output (task-specific specification). The agent executing the plan need not be the same agent that wrote it. This is the declarative equivalent of a work order: any sufficiently capable agent can execute it.

**3. Structured output contracts.** Custom subagents in `.claude/agents/` define tool access and output format in YAML frontmatter. This creates an interface contract: an orchestrating agent knows exactly what to expect regardless of which invocation runs the subagent. Examples: `code-reviewer.md`, `researcher.md`, `writer.md`.

**4. Stop hooks for continuous operation.** From Every.to: *"You can set up a stop hook that runs your test suite… if any tests fail, it tells Claude to fix the problem and finish testing instead of stopping. 'You can just make the model keep going until the thing is done.'"* An idempotent loop: agent identity within the loop doesn't matter; only the external test result does.

**The artifact pattern (Anthropic).** From the multi-agent research post: *"Subagents call tools to store their work in external systems, then pass lightweight references back to the coordinator. Rather than requiring subagents to communicate everything through the lead agent, implement artifact systems where specialized agents can create outputs that persist independently."* This is direct stigmergy — environmental modification as the coordination channel.

### 5.2 Hybrid hierarchy + swarm patterns — five named implementations

Every production system that scales is a **hybrid**. The consistent pattern: strict hierarchical control at the top, homogeneous parallelism at the leaves, shared environment in the middle.

**Pattern 1 — Anthropic Research: Hierarchical Orchestrator + Parallel Subagent Swarm.**
- *Hierarchical:* one Opus 4 lead agent receives the query, plans, decides how many subagents (1–10+), writes task descriptions.
- *Swarm-like:* Sonnet 4 subagents run in parallel with independent context windows, each exploring a different research direction. Homogeneous (same model, same toolset), differentiated only by task description. They do not communicate with each other.
- *State flow:* user query → lead planning → parallel subagent spawn → subagents write artifacts to filesystem (not through lead) → lightweight references returned → lead synthesizes.
- *Pattern label:* Top-down hierarchical → bottom-up parallel homogeneous swarm; asymmetric (heterogeneous orchestrator, homogeneous workers).

**Pattern 2 — Factory AI Droids: Coordinator + Role-Scoped Specialist Swarm.**
- *Hierarchical:* a coordinator receives a Linear/Jira ticket, decomposes it, routes subtasks to specialist droids. Never executes itself.
- *Swarm-like:* when three services need parallel changes, *"the coordinator dispatches three code droid sessions in isolated sandboxes rather than serializing through one agent"* ([NEA](https://www.nea.com/blog/factory-the-platform-for-agent-native-development)).
- *Shared-environment:* the Knowledge Droid provides an index that all droids read from — preventing context divergence and directly addressing Cognition's Principle 1 (share full traces).
- *Pattern label:* Hierarchical coordinator → role-specialized parallel workers; shared knowledge store prevents conflicting decisions.

**Pattern 3 — Sierra: Supervisor-over-Agent Layered Architecture ("Agent OS").**
- *Hierarchical:* an "Agent OS" wraps the primary conversational agent in supervisory layers (goals, guardrails, task scaffolding). A separate LLM supervisor reviews output.
- *Swarm-like:* for complex journeys, *"specialized agents handle subtasks like authentication, order lookup, and escalation under a single conversation state."*
- *Supervisory insight (Clay Bavor, Sierra):* *"One of the more interesting learnings from the past year and a half of working on this stuff is that the solution to many problems with AI is more AI… one of the remarkable properties of large language models is that they're better at detecting errors in their own output than in not making those errors in the first place."* ([Sequoia Training Data podcast](https://sequoiacap.com/podcast/training-data-clay-bavor/))
- *Result:* 70%+ resolution rates at SiriusXM, Weight Watchers, OluKai. This is the evaluator-optimizer pattern at production scale.

**Pattern 4 — LangGraph Supervisor: Canonical Framework Implementation.**
- *Hierarchical:* central supervisor holds handoff tools (`transfer_to_research_agent`, `transfer_to_math_agent`). Receives input, selects next worker, passes full message history, waits for return. Workers can only return to supervisor ([LangGraph Supervisor Tutorial](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/)).
- *Swarm-like:* supervisor manages N workers; teams nest — top-level supervisor delegates to sub-supervisors. Two-tier hierarchies demonstrated in the tutorial.
- *State flow:* `START → supervisor → [transfer_to_X] → worker → [transfer_back] → supervisor → … → END`. Workers see parent state via `InjectedState`. `Command` objects drive routing.
- *Pattern label:* Hierarchical supervisor as dynamic router; workers as ReAct sub-graphs; composable into multi-tier hierarchies.

**Pattern 5 — MetaGPT: Strict Software-Company Hierarchy with SOP-Encoded Assembly Line.**
- *Hierarchical:* five role-specialized agents in strict sequential order: Product Manager → Architect → Project Manager → Engineer → QA Engineer. Each has fixed profile, goal, output format ([IBM Think](https://www.ibm.com/think/topics/metagpt)).
- *Swarm-like:* the Engineer layer may use multiple parallel engineer agents; QA loops iteratively.
- *Shared-environment:* pub/sub `Environment` as blackboard; all agents read prior outputs.
- *SOP insight:* *"All handovers between agents must comply with certain established standards that reduce the risk of hallucination caused by idle chatter between LLMs."* This directly addresses Cognition's Principle 2.

### 5.3 Comparative summary of hybrid patterns

| System | Top Level | Middle Level | Bottom Level | Context Sharing | Production Scale |
|---|---|---|---|---|---|
| Anthropic Research | Lead Opus 4 — plans | — | Sonnet 4 subagents — parallel | Filesystem artifacts + lightweight refs | Shipped in Claude Research |
| Factory AI | Coordinator agent | Knowledge Droid (memory) | Role droids (Code/Review/Test/Docs) | Knowledge Droid index; typed handoffs | Enterprise SaaS |
| Sierra | Supervisor LLM + goals/guardrails | Primary conversational agent | Auth/lookup/escalation sub-agents | Single conversation state | Fortune 500 brands |
| LangGraph Supervisor | Top supervisor → sub-supervisors | Team supervisors (optional) | Worker agents | Full message history via `InjectedState` | Framework; widely adopted |
| MetaGPT | Product Manager | Architect → PM → Engineer | QA loop | Shared memory pool (blackboard) | Research / small tasks |

---

## Section 6 — Solo-Founder Economics

### 6.1 Claude API pricing — April 2026

[Anthropic's current pricing](https://www.anthropic.com/pricing):

| Model | Input ($/MTok) | Output ($/MTok) | Cache Write | Cache Read |
|---|---|---|---|---|
| **Opus 4.7** | $5.00 | $25.00 | $6.25 | $0.50 |
| **Sonnet 4.6** | $3.00 | $15.00 | $3.75 | $0.30 |
| **Haiku 4.5** | $1.00 | $5.00 | $1.25 | $0.10 |

Generational price compression from Opus 4 ($15 input) to Opus 4.7 ($5 input) is a 3× drop in 18 months — a meaningful tailwind for cost-sensitive pipelines. One notable caveat: [Simon Willison observed in April 2026](https://simonwillison.net/) that Opus 4.7's new tokenizer maps the same input to **1.0–1.35× more tokens** than Opus 4.6, effectively increasing real-world cost 10–40% despite the identical nominal price.

Additional platform fees relevant to agentic use: Managed Agents at $0.08 per session-hour plus token rates; web search $10 per 1,000 searches; code execution 50 free container-hours/day per org, $0.05/hr beyond.

### 6.2 Claude Code subscription plans

[Confirmed April 2026 via multiple sources](https://www.ssdnodes.com/blog/claude-code-pricing-in-2026-every-plan-explained-pro-max-api-teams/):

| Plan | Monthly Price | Claude Code Access | Session Limit | Opus Access |
|---|---|---|---|---|
| Free | $0 | ✗ | — | ✗ |
| **Pro** | $20/mo | ✓ (limited) | ~44K tokens / 5-hr | ✓ |
| **Max 5×** | $100/mo | ✓ | ~88K tokens / 5-hr | ✓ |
| **Max 20×** | $200/mo | ✓ | ~220K tokens / 5-hr | ✓ |
| Team Premium | $100/seat/mo | ✓ | 5× Pro | ✓ |
| API direct | Pay-per-token | ✓ | Unlimited | ✓ |

Usage resets on rolling 5-hour windows. Anthropic enforces separate weekly caps on total usage and on Opus 4 specifically since August 2025. From April 2026, third-party harnesses previously run under subscriptions now bill through a separate pay-as-you-go "extra usage" system — shifting per-task costs for agentic workflows to **$0.50–$2.00** per task for many hobbyist setups ([Reddit r/AI_Agents](https://www.reddit.com/r/AI_Agents/comments/1scdq0o/anthropic_effectively_ends_the_unlimited_claude/)).

### 6.3 Real solo-dev monthly bills — the subscription/API arbitrage

The most data-rich account is [Kyle Redelinghuys, who tracked eight months of Claude Code usage](https://www.ksred.com/claude-code-pricing-guide-which-plan-actually-saves-you-money/):

> "I've been using Claude Code daily for eight months now, across something like 10 billion tokens of usage. I recently dug through my local session logs to estimate what all of that would have cost on API pricing, and the number came to over $15,000. I've been paying roughly $100/month on the Max plan, so around $800 total. That's a 93% saving, and it's not even close to being a marginal decision."

His peak: **July 2025, 2.4B tokens, API-equivalent $5,623 — actual subscription cost ~$100.**

| Month | Tokens | API Equivalent | Max Subscription |
|---|---|---|---|
| June 2025 | 421M | $897 | ~$100 |
| July 2025 | 2.4B | $5,623 | ~$100 |
| Aug 2025 | 320M | $771 | ~$100 |
| Oct–Dec 2025 | ~5B est | ~$4,600 | ~$300 |
| Jan–Feb 2026 | ~1.5B est | ~$3,000 | ~$200 |
| **Total** | **~10B** | **~$15,000+** | **~$800** |

A Reddit data pull of 31 Claude Code users [posted April 2026](https://www.reddit.com/r/ClaudeAI/comments/1sg85eu/i_tracked_what_31_claude_code_subscriptions/) found average API-equivalent costs **25–50× the subscription fee**, with the top user at $18K/month API-equivalent on a $200 subscription.

[Anthropic's own Claude Code docs](https://code.claude.com/docs/en/costs) state: *"Across enterprise deployments, the average cost is around $13 per developer per active day and $150–250 per developer per month, with costs remaining below $30 per active day for 90% of users."*

### 6.4 Realistic monthly budget for Jetix

Assumptions: Sonnet 4.6 at $3/$15; 70/30 input-output ratio; no prompt caching unless stated.

| Usage Pattern | Monthly Cost | Notes |
|---|---|---|
| **Light Claude Code (Pro $20)** | **$20/mo** | ~44K tokens / 5-hr window; fine for few sessions/day |
| **Heavy Claude Code (Max $200)** | **$200/mo** | ~220K tokens / 5-hr window; effectively unlimited for one solo dev |
| **API direct, single-agent, ~10M tokens/mo** | **~$45–54/mo** | ~7M input ($21) + ~3M output ($45) on Sonnet 4.6 |
| **API direct, multi-agent, ~150M tokens/mo (15×)** | **~$675–810/mo** | Sonnet 4.6: 105M input ($315) + 45M output ($675) |
| **API direct, multi-agent Opus 4.7, ~150M tokens/mo** | **~$1,575–2,250/mo** | $5/$25 balloons cost 3× vs Sonnet |
| **Hybrid: Max $100 + API overflow** | **~$150–300/mo** | Common pattern for active solo founders |

**Break-even analysis for Ruslan (€50K ARR ≈ €4,167/mo).** At $200/mo (Max 20×), token costs are **4.8% of target revenue** — comfortably within a 5–10% SaaS COGS ceiling. The high-risk scenario is API-direct at 150M tokens on Opus 4.7 (~$2,000/mo, **48% of target revenue**), which only pencils if the agent workflow outputs equivalent-or-greater value. Heuristic: if a multi-agent workflow replaces 10 hours of Ruslan's time at €50/hr (€500), the workflow should cost under €250/mo — achievable with Sonnet 4.6 at 50M tokens/mo.

**Cost levers.** (1) Route 80% of agent volume through Haiku 4.5 ($1/$5) for filtering, classification, scaffolding; reserve Sonnet for generation and Opus for planning. (2) Use prompt caching — subscription interface gives free cache reads; API gives 10% of input cost. [One Reddit analysis](https://www.reddit.com/r/ClaudeAI/comments/1qpcj8q/claude_subscriptions_are_up_to_36x_cheaper_than/) found subscriptions up to 36× cheaper than API for agentic loops precisely because of free cache reads. (3) Batch API gives 50% discount for async workloads.

---

## Section 7 — Future Direction

### 7.1 The protocol stack: MCP won the tool layer; A2A is niche

Two protocols emerged in 2025. [Google announced A2A (Agent2Agent) on April 9, 2025](https://fast.io/resources/a2a-vs-mcp-protocol-comparison/) with 50+ launch partners. By June 2025 it moved to Linux Foundation governance with 100+ companies. Anthropic donated MCP to the Agentic AI Foundation in December 2025 with 10,000+ active public MCP servers and cross-platform adoption (ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code).

The protocols address different layers:

> "MCP standardizes how an agent or model connects to tools, data, and external systems. A2A standardizes how one agent communicates and coordinates with another agent." — [DEV Community analysis, April 2026](https://dev.to/chunxiaoxx/a2a-vs-mcp-in-2025-different-layers-not-rivals-25ij)

By September 2025, [A2A's development had slowed significantly](https://blog.fka.dev/blog/2025-09-11-what-happened-to-googles-a2a/) as the ecosystem consolidated around MCP. Google Cloud itself added MCP compatibility — a tacit admission that MCP won.

**Implication for swarm vs hierarchy.** The MCP/A2A stack assumes hierarchical dispatch (orchestrator calls MCP tools, dispatches A2A tasks to subagents). True flat swarms with emergent coordination remain a research-phase concept; production systems in 2026 are almost exclusively orchestrator-worker hybrids.

### 7.2 Eleven attributed predictions for 2026–2027

**1. Millions of simultaneous agent instances by ~2027** — Dario Amodei, Anthropic CEO, October 2024, [*Machines of Loving Grace*](https://darioamodei.com/machines-of-loving-grace): *"The resources used to train the model can be repurposed to run millions of instances of it (this matches projected cluster sizes by ~2027)… Each of these million copies can act independently on unrelated tasks, or if needed can all work together in the same way humans would collaborate, perhaps with different subpopulations fine-tuned to be especially good at particular tasks. We could summarize this as a 'country of geniuses in a datacenter.'"* Implications: fungible copies for independent tasks; specialized subpopulations for collaborative ones. Current 15× cost makes continuous million-agent operation prohibitive except for mission-critical work.

**2. Software engineering agents doing a junior engineer's day of work by end 2025 / early 2026** — Sholto Douglas (Anthropic), May 22, 2025, [Dwarkesh Podcast](https://www.dwarkesh.com/p/sholto-trenton-2): *"By the end of this year to this time next year, we will have software engineering agents that can do close to a day's worth of work for a junior engineer."* And: *"Over the remainder of the year, basically we're going to see progressively more and more experiments of the form: how can I dispatch work to a software engineering agent in such a way that it's async?"* Implication: 2025–2026 is the exploration phase of async hierarchical dispatch; reliability ("nines") keeps flat swarms impractical.

**3. The bottleneck shifts from generation to verification** — Trenton Bricken (Anthropic), May 22, 2025, [Dwarkesh Podcast](https://www.dwarkesh.com/p/sholto-trenton-2): *"We're going to move away from 'can an agent do XYZ', and more towards 'can I efficiently deploy 100 agents and then give them the feedback they need'… it's so easy to generate with these agents that the bottleneck is actually, can I as the human verify the answer? If 20 of my 100 agents all found this one thing, then it has a higher chance of being true."* Operational implication: **quorum-based swarm pattern** (run 100, take the plurality) becomes standard for high-stakes agentic tasks in 2026–2027.

**4. "Phase transition" in agent coherence around Dec 2025** — Andrej Karpathy, February 2026, [LinkedIn summary](https://www.linkedin.com/pulse/andrej-karpathy-february-2026-neal-whittle-btqic): *"LLM agent capabilities (Claude & Codex especially) have crossed some kind of threshold of coherence around December 2025 and caused a phase shift in software engineering… The intelligence part suddenly feels quite a bit ahead of all the rest of it — integrations (tools, knowledge), the necessity for new organizational workflows, processes, diffusion more generally. 2026 is going to be a high energy year as the industry metabolizes the new capability."* Karpathy frames 2026 as integration year, not capability-leap year. Swarm systems are waiting for the surrounding infrastructure.

**5. Agent swarms replace academic research communities for AI optimization** — Andrej Karpathy, March 2026, [*Fortune*, "The Karpathy Loop"](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/): *"You spin up a swarm of agents, you have them collaborate to tune smaller models, you promote the most promising ideas to increasingly larger scales, and humans (optionally) contribute on the edges."* And: *"The next step for autoresearch is that it has to be asynchronously massively collaborative for agents. The goal is not to emulate a single PhD student, it's to emulate a research community of them. All LLM frontier labs will do this. It's the final boss battle."* His autoresearch case (700 experiments, 2 days, 11% training speedup) is the first credible production swarm pattern: agents coordinate through a shared objective rather than a central brain — **"emergent specialization through selection."**

**6. Agents join the workforce in 2025; novel insights in 2026; physical robots in 2027** — Sam Altman, January 2025, [*The Gentle Singularity*](https://blog.samaltman.com/the-gentle-singularity): *"2025 has seen the arrival of agents that can do real cognitive work; writing computer code will never be the same."* For 2026: *"Likely see the arrival of systems that can figure out novel insights."* For 2027: *"May see the arrival of robots that can do tasks in the real world."* A straight hierarchical escalation; Altman does not publicly endorse flat swarms.

**7. Agentic AI at Peak of Inflated Expectations; frameworks heading to Trough** — Gartner, 2025 Hype Cycle for Generative AI, [LinkedIn summary](https://www.linkedin.com/posts/alexandra-podsekina_this-is-gartners-2025-hype-cycle-for-generative-activity-7446301833582735362-5zXB): *"Agentic AI and Multimodal Generative AI sit at the very top [Peak of Inflated Expectations]. Prompt Engineering, GenAI Application Orchestration Frameworks, and Agent Development Frameworks are sliding toward disillusionment — a normal maturation signal, not a death knell."* Implication: practical productivity arrives on the Slope of Enlightenment circa 2027–2028; swarm architectures being designed today find production-ready tooling in 2027.

**8. Most white-collar tasks automated within 12–18 months (by mid-2027)** — Mustafa Suleyman (Microsoft AI CEO), February 2026, [*Business Insider*](https://www.businessinsider.com/microsoft-ai-ceo-mustafa-suleyman-white-collar-tasks-automation-prediction-2026-2): *"I think that we're going to have a human-level performance on most, if not all, professional tasks. White-collar work, where you're sitting down at a computer… will be fully automated by an AI within the next 12 to 18 months."* Separately names *"a marketplace of specialized agents — one for fitness coaching, another for financial planning, all interoperable via standardized protocols"* — the **fungible-agent-marketplace** vision. Most commercially plausible path for a solo developer.

**9. Agentic workflows, not bigger models, drive the next wave** — Andrew Ng, September 2025 newsletter, [Reddit summary](https://www.reddit.com/r/PromptEngineering/comments/1noh0aa/andrew_ng_the_ai_arms_race_is_over_agentic_ai/): *"The future won't revolve around larger language models. Instead, it will focus on agentic workflows — reflection, planning, tool usage, and collaboration among multiple agents. Smaller, more affordable models, when integrated into well-structured agent workflows, can already surpass the performance of larger systems like GPT-4 in certain practical scenarios."* Ng's four patterns (Reflection, Tool Use, Planning, Multi-Agent Collaboration) describe specialized roles with hierarchy, not flat swarms.

**10. Agents don't achieve AGI-level reliability by end 2025; swarm misuse before productivity** — Gary Marcus, December 2025, [*Marcus on AI*](https://garymarcus.substack.com/p/six-or-seven-predictions-for-ai-2026): *"Despite all the hype, agents didn't turn out to be reliable."* And on swarms specifically, January 2026, [*AI bot swarms threaten to undermine democracy*](https://garymarcus.substack.com/p/ai-bot-swarms-threaten-to-undermine): *"The unique danger of a swarm is that it acts less like a megaphone and more like a coordinated social organism."* Marcus grounds the debate: production-grade reliability has not arrived, so autonomous flat swarms remain premature outside research.

**11. Token usage alone explains 80% of multi-agent performance variance; model quality is a multiplier** — Anthropic engineering (Jeremy Hadfield et al.), June 2025, [*How we built our multi-agent research system*](https://www.anthropic.com/engineering/built-multi-agent-research-system): *"Multi-agent systems work mainly because they help spend enough tokens to solve the problem… upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7."* The most important empirical finding of 2025 for swarm architecture: **swarm performance is a compute-budget problem, not a coordination problem.** As model capability improves and prices fall, the same task quality becomes achievable with fewer tokens, making swarm economics increasingly viable for solo developers.

### 7.3 Swarm scaling — where is the bottleneck?

- **1–5 agents:** coordination overhead is trivial; task decomposition quality is the bottleneck.
- **5–20 agents:** context-window management becomes dominant. Anthropic's architecture avoids *"the game of telephone"* by routing subagent outputs to an external filesystem rather than through the coordinator.
- **20–100 agents:** human verification is the bottleneck (Trenton Bricken).
- **100+ agents:** orchestration infrastructure (scheduling, retry logic, state management) becomes the primary cost driver, 25–30% of total compute per [Latenode analysis](https://community.latenode.com/t/when-multiple-ai-agents-handle-different-parts-of-a-workflow-where-does-the-cost-actually-explode/57933).

[Nathan Labenz notes on *The Cognitive Revolution*](https://www.youtube.com/watch?v=XOuTWc46CtA) a "Moore's Law for AI agents": max task length AI can handle has been **doubling every 7 months for 6 years**, potentially accelerating to a 4-month doubling with RL. If this holds, by mid-2027 agents could autonomously handle tasks currently requiring days — at which point swarm-of-swarms architectures become the natural next step.

**For Jetix specifically:** at €50K ARR with 15× multi-agent costs, the practical ceiling today is a **3–7 agent workflow** at Sonnet 4.6 prices ($100–300/month). By 2027, at projected 50–70% lower token prices (based on the 3× drop from Opus 4 to Opus 4.7 over 18 months), the same budget will support 10–20 agent pipelines — pushing solo-founder economics into territory that currently requires a small engineering team.

---

## Critical Assessment

### Pros — when swarm is the right choice (evidence-backed)

- **Breadth-first research with independent subtasks.** +90.2% Anthropic; the most robust positive evidence in the literature.
- **High-volume parallel task batches.** PubMed clinical study: 65.3% vs 16.6% single-agent at 80-task load.
- **Decomposable analytical work (financial, market research).** Kim et al. +80.8%.
- **Mathematical / factual reasoning through debate.** Du et al. +7–15 pp across benchmarks.
- **When per-subtask context fits in a single window and work is embarrassingly parallel.** Claude Code's `claude -p "Migrate $file"` shell fan-out for 2,000 Python files.
- **When ample shared environment can carry coordination state.** CLAUDE.md + filesystem + git are rich enough to make fungible-agent patterns work without direct agent-to-agent messaging.

### Cons + failure modes — when swarm hurts

- **Compound errors (17.2× amplification).** Independent MAS without verification is catastrophically worse than single-agent on accuracy.
- **Coordination overhead past 4 agents.** Kim et al.'s Rule of 4; Jetix's 12-agent design is well past this knee.
- **Sequential / tightly-coupled tasks degrade 39–70%.** PlanCraft evidence; most coding tasks fit this profile.
- **Tool-heavy workflows lose 2–6× efficiency.** Each agent's context fragments; agents exhaust capacity on coordination.
- **The Flappy Bird failure mode.** Parallel subagents build incompatible components because implicit decisions conflict.
- **Cost: 15× tokens only justifies itself if task value is high and parallelism is real.**
- **Debugging is hard.** State is distributed across agents and environments; traces are fragmentary; most frameworks have immature observability.
- **"Swarm misuse precedes swarm productivity"** — Marcus's warning. At scale, swarms amplify the worst as well as the best.

### When to use vs avoid — explicit decision rules

**Use multi-agent (hierarchical + swarm-at-leaves) if ALL:**
1. The task is decomposable into independent subtasks whose outputs compose mechanically, not semantically.
2. Each subtask fits comfortably in a single agent's context window.
3. The task value clears a 15× token overhead (rule of thumb: saves ≥ 2 hours of skilled human time).
4. You have a verification step at the merge point (evaluator-optimizer).
5. Team size sits at 3–7 agents — the Rule of 4 sweet spot.

**Avoid multi-agent if ANY:**
1. The task is sequential and each step depends on the previous (planning, debugging a single codebase).
2. The single-agent baseline is already above ~45% (capability ceiling).
3. The workflow uses more than ~10 tools (efficiency penalty of 2–6×).
4. You can't afford ~$200/mo on subscription or ~$700–2,000/mo at API rates.
5. You don't have a verifier or shared environment layer. Unverified parallel agents ≈ amplified hallucinations.
6. The decomposition requires subagents to infer each other's implicit decisions (the Flappy Bird trap).

---

## Comparison to the Anthropic Ecosystem

| Component | Role in swarm-vs-hierarchy spectrum | Anthropic's position |
|---|---|---|
| **Claude (API)** | Foundation model; single-agent unless wrapped | "Use the smallest tool for the job" |
| **Claude Code** | Stigmergic fungible-agent pattern with shared CLAUDE.md + filesystem + git state | Recommended default; *"No one correct way"* (Cherny) |
| **Claude Agent SDK** | Hierarchical parent-child (subagents via `Agent` tool) with context isolation | Production path for programmable agents |
| **MCP** | Horizontal tool/resource layer; orthogonal to coordination | *"Focuses solely on the protocol for context exchange"* — protocol, not framework |

[Anthropic's official taxonomy (Schluntz & Zhang, Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents) distinguishes **workflows** (predefined code paths) from **agents** (dynamic self-direction). Their canonical patterns in order of increasing autonomy: prompt chaining, routing, parallelization (sectioning + voting), orchestrator-workers, evaluator-optimizer.

**Anthropic's official guidance is summary-level hierarchical, leaf-level swarm:**
- For most work: *"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."* (Start with single agent.)
- For breadth-first research that justifies 15× cost: orchestrator-worker with parallel homogeneous subagents (their own production pattern).
- For long-horizon coding: compaction + structured note-taking + focused sub-agents (the context-engineering post).
- For Claude Code specifically: shared environment (CLAUDE.md + filesystem + git) + fungible parallel invocations + verification loops (tests, subagent review).

Anthropic does **not** officially recommend flat emergent swarms. The practical guidance, consistently across all four engineering posts, is: **hierarchical planning, parallel homogeneous execution at the leaves, strong shared-environment layer, mandatory verification.** This matches every production system reviewed in Section 4.

---

## Specific Production Examples

Twelve named entities/products/papers, 1–2 line descriptor each, all cited above:

1. [**Anthropic Claude Research**](https://www.anthropic.com/engineering/built-multi-agent-research-system) — Opus-4-lead + parallel Sonnet-4 subagents. +90.2% vs single-agent; 15× tokens; 90% time reduction on complex queries.

2. [**Cognition Devin**](https://cognition.ai/blog/dont-build-multi-agents) — Single-thread primary + fine-tuned compression model. Walden Yan's "Don't Build Multi-Agents" is the strongest anti-swarm engineering argument in print.

3. [**Cursor 2.0**](https://www.digitalapplied.com/blog/cursor-2-0-agent-first-architecture-guide) — Up to 8 parallel agents with git worktree isolation; proprietary Composer model 4× faster. Collapses 15-hour workloads to 3 hours.

4. [**Replit Agent**](https://www.langchain.com/breakoutagents/replit) — Manager → Editor → Verifier hierarchy with human-in-loop. Hundreds of thousands of production runs; ~90% tool-call success.

5. [**Sierra**](https://sequoiacap.com/podcast/training-data-clay-bavor/) — Bret Taylor and Clay Bavor's "Agent OS" with supervisor-over-agent layered architecture. 70%+ resolution at SiriusXM, Weight Watchers, OluKai.

6. [**Harvey AI**](https://www.harvey.ai/blog/introducing-agent-builder) — Legal workflow platform. 400K+ agentic queries/day; 25,000+ custom workflows; 20M+ terms extracted.

7. [**Kim et al. 2025, "Towards a Science of Scaling Agent Systems"** (arXiv:2512.08296)](https://arxiv.org/abs/2512.08296) — 260-configuration study; Rule of 4; 17.2× error amplification; −3.5% aggregate mean vs single agent.

8. [**Anthropic Hadfield et al., "How we built our multi-agent research system"** (June 2025)](https://www.anthropic.com/engineering/built-multi-agent-research-system) — Source of the 15× token claim and the 80%-variance-explained-by-tokens finding.

9. [**Cemri et al. 2025, "Why Do Multi-Agent LLM Systems Fail?"** (arXiv:2503.13657)](https://arxiv.org/abs/2503.13657) — MAST taxonomy of 14 failure modes; 1,600+ annotated traces across 7 frameworks.

10. [**Qian et al. 2024, "Scaling Large Language Model-based Multi-Agent Collaboration"** (arXiv:2406.07155)](https://arxiv.org/abs/2406.07155) — Logistic scaling law; 16-agent sweet spot for DAG topologies.

11. [**Schluntz & Zhang, "Building effective agents"** (Anthropic, Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents) — Foundational workflow/agent taxonomy; five canonical patterns.

12. [**Boris Cherny interviews** (Latent Space, Lenny's, Every.to, Twitter)](https://www.latent.space/p/claude-code) — The fungible-agent-via-shared-environment pattern, expressed as practice rather than manifesto.

---

## The Jetix Recommendation

Given Ruslan's parameters — solo founder, Berlin, €50K ARR goal, Claude Code stack, currently running a 12-agent CEO→Manager→Leads→Workers hierarchy — the evidence-backed recommendation is:

**Move from a 12-agent rigid hierarchy to a hybrid pattern: 1 planner (Opus/Sonnet) + 3–5 fungible parallel executor invocations + explicit verification step, coordinated through CLAUDE.md + filesystem + structured artifacts rather than direct agent-to-agent messaging.**

The 12-agent design combines the worst of both architectural worlds: role specialization (high coordination cost, compound errors), fixed topology (no emergent adaptation), past the Rule of 4 knee, without the mandatory shared-environment layer that makes Claude Code's pattern work. A pure swarm is also wrong — no production system operates as a flat emergent swarm and the supporting infrastructure isn't mature. The right architecture is the one every serious production system converged on: **hierarchical orchestrator, homogeneous parallel leaves, rich shared environment, explicit verifier.** Spend the €200/month on Max 20× until usage justifies the API.

---

*Report prepared April 2026. All citations inline as markdown links. Length: ~11,000 words.*
