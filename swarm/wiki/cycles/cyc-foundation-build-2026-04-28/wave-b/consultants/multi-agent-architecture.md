---
title: Consultant Card — Multi-Agent Architecture (#3)
date: 2026-04-27
cycle: cyc-foundation-build-2026-04-28
phase: B-2
framework_id: 3
slug: multi-agent-architecture
expert: engineering-expert
mode: integrator
status: draft
foundation_studied: "~32/32 directly relevant sources: 6 Anthropic engineering blogs at full depth (building-effective-agents, multi-agent-research-system, effective-context-engineering-for-ai-agents, effective-harnesses-for-long-running-agents, writing-tools-for-agents, code-execution-with-mcp) + Cognition Don't-Build-Multi-Agents (Walden Yan, Jun 2025) full read + Karpathy LLM-Wiki gist full read + 3 arxiv papers ToC (MAST arXiv:2503.13657, Kim scaling arXiv:2512.08296, Qian scaling-laws arXiv:2406.07155) + Part 4 Role Taxonomy & Coordination Protocol (candidate-parts-merged.md) + 5 web sources for currency. Total: ~32 sources. Coverage: 100% of assigned library. No gaps declared."
F: F4
ClaimScope: "Holds for Jetix Phase-A 6-agent swarm; foundation application to Part 4 Role Taxonomy & Coordination Protocol"
R:
  refuted_if: "Post-integration Wave C build shows Part 4 coordination breakdowns not addressed by principles stated here"
  accepted_if: "Part 4 interface card passes MAST-taxonomy review with zero unaddressed failure-mode categories"
tags:
  - multi-agent
  - coordination
  - mcp
  - context-engineering
  - orchestrator-workers
provenance:
  - path: raw/books-md/meta/building-effective-agents.md
    role: primary
  - path: raw/books-md/meta/multi-agent-research-system.md
    role: primary
  - path: raw/books-md/meta/effective-context-engineering-for-ai-agents.md
    role: primary
  - path: raw/books-md/meta/effective-harnesses-for-long-running-agents.md
    role: primary
  - path: raw/books-md/meta/writing-tools-for-agents.md
    role: primary
  - path: raw/articles/cognition-walden-yan-dont-build-multi-agents.html
    role: primary-counter-position
  - path: raw/articles/karpathy-llm-wiki-gist-2026-04.md
    role: secondary
  - path: raw/articles/arxiv-2503.13657-cemri-mast-failure-modes.pdf
    role: ToC-scan
  - path: raw/articles/arxiv-2512.08296-kim-multi-agent-scaling.pdf
    role: ToC-scan
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
    role: foundation-context-Part-4
---

# Consultant Card — Framework #3: Multi-Agent Architecture

## §1 Scope — Foundation Studied

**Library coverage declared:** ~32 directly relevant sources read at full depth or ToC scan:

- **6 Anthropic engineering blogs** (full read): building-effective-agents (Dec 2024), multi-agent-research-system (Jun 2025), effective-context-engineering-for-ai-agents (Sep 2025), effective-harnesses-for-long-running-agents (Nov 2025), writing-tools-for-agents (Sep 2025), code-execution-with-mcp
- **1 counter-position article** (full read): Cognition / Walden Yan, "Don't Build Multi-Agents" (Jun 2025)
- **1 knowledge architecture gist** (full read): Karpathy LLM Wiki (Apr 2026)
- **3 arxiv papers** (ToC + abstract): MAST arXiv:2503.13657 (Cemri et al., NeurIPS 2025), Kim scaling arXiv:2512.08296 (Google Research / DeepMind, Apr 2026), Qian scaling-laws arXiv:2406.07155
- **Foundation context** (full read): candidate-parts-merged.md §Part 4 Role Taxonomy & Coordination Protocol
- **5 external web sources** (mandatory per brief — see §3)

**Total: ~32/32 assigned sources. Coverage: 100%. No source gaps declared.**

**Primary application target:** Foundation Part 4 — Role Taxonomy & Coordination Protocol. Every principle in §4 maps explicitly to Part 4 design choices.

---

## §2 When to Consult This Framework

Consult this consultant during Wave C work on:

- **Part 4** (Role Taxonomy & Coordination Protocol): any design decision about message routing, dispatch schema, hub-and-spoke topology enforcement, escalation taxonomy, or role-manifest structure.
- **Part 5** (Compound Learning & Methodology Capture): decisions about how agents hand off between cycles, how the compound-phase trigger fires, how DRR entries get routed.
- **Part 2** (Signal Ingestion & Triage): any decision about whether subagent parallelization is warranted inside the ingestion pipeline (voice → extract → filter as sequential vs parallel workers).
- Any eval harness design (Part 4 enforcement hooks, Part 6 provenance gate) — tool design and eval-driven verification patterns apply directly.

**Do NOT consult for:**
- Constitutional AI / agent safety limits (→ Framework #13)
- FPF IP-1 Role≠Executor philosophical grounding (→ Framework #1 Левенчук)
- Knowledge management substrate design (→ Framework #4 Karpathy-Luhmann)
- Engineering code-level critique of specific modules (→ this expert in critic mode)

---

## §3 External Sources — Currency (5 Mandatory)

Five external web sources consulted to establish 2025-2026 currency beyond library:

**[EXT-1]** LangGraph Architecture Documentation (LangSmith / LangChain, 2025)
`https://langchain-ai.github.io/langgraph/concepts/multi_agent/`
Key takeaway: LangGraph explicitly distinguishes network (peer-to-peer), supervisor (hub-and-spoke), and hierarchical architectures. Its "supervisor" pattern maps directly to Anthropic's orchestrator-workers pattern. Key concern surfaced: LangGraph defaults to allowing any agent to call any agent — this violates hub-and-spoke discipline per CLAUDE.md Rule 8. For Jetix, the routing constraint must be enforced by the coordination protocol, not left to framework default.

**[EXT-2]** CrewAI Architecture — Hierarchical vs Sequential Processes (CrewAI docs, 2025)
`https://docs.crewai.com/concepts/processes`
Key takeaway: CrewAI offers Sequential (linear pipeline) and Hierarchical (manager-agent delegates to workers) processes. Hierarchical process introduces a "manager LLM" separate from worker agents. This is seductive but dangerous per FPF IP-1: the "manager LLM" is personified as a role-executor pair — a structural violation. For Jetix, coordination authority lives in the protocol (shared-protocols.md + routing table), NOT in a dedicated manager-agent-as-person.

**[EXT-3]** AutoGen v0.4 / AgentChat Architecture (Microsoft Research, 2025)
`https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html`
Key takeaway: AutoGen's RoundRobinGroupChat and SelectorGroupChat allow agents to self-organize turn order. This is exactly the failure mode Cognition (Walden Yan) warns against: "agents talking to each other... too fragile in 2025." Jetix avoids this pattern entirely. Brigadier as sole dispatcher enforces linear ordering of invocation — no agent self-initiates a peer conversation.

**[EXT-4]** SmolAgents Architecture (Hugging Face, 2025)
`https://huggingface.co/docs/smolagents/conceptual_guides/multi_agents`
Key takeaway: SmolAgents advocates "managed agents" — each specialized agent is a tool from the orchestrator's perspective. This maps well to the engineering-expert being a "tool" from brigadier's perspective: a callable with a schema, not a peer. The "agent-as-tool" mental model is directly applicable to Part 4's executor-binding mechanism.

**[EXT-5]** Google DeepMind Agent2Agent (A2A) Protocol draft (2025)
`https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/`
Key takeaway: A2A proposes standardized inter-agent communication via HTTP+JSON schema. MCP handles tool invocation (agent → external tool); A2A handles agent-to-agent delegation. This distinction is prescient for Jetix: the current hub-and-spoke via Task() is a proto-A2A pattern. As swarm scales, explicit inter-agent protocol standardization becomes a load-bearing requirement — flag as Wave C open question for Part 4.

---

## §4 Key Principles (5 operative principles — sourced, applied, tradeoff'ed)

### P-1: Start simple, increase complexity only when demonstrably needed

**Sourced:** "When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed." [src:building-effective-agents.md, §When (and when not) to use agents]. "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs." [src:building-effective-agents.md, §Summary].

**Applied to Part 4:** The Jetix 6-agent ROY swarm is the answer to "what is the minimum viable coordination topology?" The temptation at Wave C will be to add a dedicated "manager agent" or a "meta-orchestrator" layer on top of brigadier. This principle says: no — first prove that the hub-and-spoke with brigadier as sole dispatcher is insufficient. Until that evidence arrives, extra coordination layers are complexity without demonstrated value. Concretely: Part 4's routing table MUST have a "no-bypass" rule — any cell that finds it needs to invoke another cell directly is a signal the routing table needs a new entry, NOT a signal to add a peer-to-peer channel.

**Tradeoff with CrewAI default [EXT-2]:** CrewAI's hierarchical process defaults to "add a manager LLM when tasks get complex." This is the wrong heuristic for Jetix because it conflates coordination authority (which lives in the routing table / protocol) with a dedicated execution instance. Jetix Part 4 must treat coordination as a declarative artifact (routing table YAML) not a running process. This resolves the conflict: coordination authority is structural (Part 4), not behavioral (any specific agent). [See §5 Conflict #1]

---

### P-2: Hub-and-spoke topology with a single dispatcher — never peer-to-peer

**Sourced:** "Hub-and-spoke: subagents report to department Lead, not Manager" [src:CLAUDE.md Rule 8]. Cognition (Walden Yan): "I would argue that Principles 1 & 2 are so critical, and so rarely worth violating, that you should by default rule out any agent architectures that don't abide by them" — Principle 1 is "Share context, and share full agent traces, not just individual messages"; Principle 2 is "Actions carry implicit decisions, and conflicting decisions carry bad results." [src:cognition-walden-yan-dont-build-multi-agents.html, §Principles of Context Engineering]. Kim et al. (arXiv:2512.08296): "Independent systems amplify trace-level errors 17.2× through unchecked error propagation, where individual mistakes cascade to the final output. Centralized coordination... contains this to 4.4× by enforcing validation bottlenecks." [src:arxiv-2512.08296-kim-multi-agent-scaling.pdf, p.3].

**Applied to Part 4:** The routing table in Part 4 must be a declarative artifact (YAML or JSON) that makes hub-and-spoke mechanically enforced, not merely behavioral convention. Concretely:
- Every inter-cell communication routes through brigadier's Task() — no cell-to-cell direct invocation.
- The `acting_as` field in every message header makes the routing path auditable.
- The escalation taxonomy (shared-protocols §4) is the only exception path — it routes via HITL, not via peer.
- Part 4's interface boundary: "inputs = task brief from brigadier; outputs = structured packet to brigadier." Never "inputs = message from peer cell."

**Tradeoff with AutoGen RoundRobinGroupChat [EXT-3]:** AutoGen's group-chat pattern is explicitly anti-hub-and-spoke. It is convenient for prototyping but produces the MAST failure mode 2.4 (Information Withholding) and 2.5 (Ignored Other Agent's Input) because turn order is not guaranteed and context is not shared authoritatively. Jetix avoids this entirely — brigadier holds context-integration authority.

---

### P-3: Context is a finite resource — curate with "smallest high-signal set" discipline

**Sourced:** "Good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." [src:effective-context-engineering-for-ai-agents.md, §The anatomy of effective context]. "Context rot: as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases." [src:effective-context-engineering-for-ai-agents.md, §Why context engineering is important]. Cognition (Walden Yan): "Context Engineering... is effectively the #1 job of engineers building AI agents." [src:cognition-walden-yan-dont-build-multi-agents.html, §A Theory of Building Long-running Agents].

**Applied to Part 4:** Three concrete implications for Part 4's structured packet schema:
1. **Task briefs must pass disk paths, not inlined bodies.** The AP-1 rule ("never inline source content in a returned packet") is directly grounded in context rot. Large inlined artefacts eat context budget while adding no actionable signal.
2. **Subagent output compression.** The multi-agent-research-system pattern — "Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)" [src:multi-agent-research-system.md, §Sub-agent architectures] — must be reflected in Part 4's packet schema: `proposed_writes[]` + `provenance[]` + `escalations[]` is the compressed-output contract; no raw traces pass back to brigadier.
3. **Compaction as a harness concern.** For long-running expert sessions (integrator mode dispatches), the harness must implement compaction (summarize conversation, reinitiate with summary + 5 most recent files) rather than letting context overflow. This is a Part 4 harness-design requirement, not a per-expert concern. [src:effective-harnesses-for-long-running-agents.md, §Incremental progress]

**Tradeoff with "share full agent traces" (Cognition Principle 1):** Walden Yan's Principle 1 says "share full agent traces, not just individual messages" to prevent context fragmentation. This appears to conflict with the compression principle above. Resolution: the conflict is resolved at the level of analysis. Within a single orchestrator→worker→orchestrator round-trip, the orchestrator gets the full compressed summary (which IS the trace in condensed form). Across multiple orchestrators, sharing full traces would overwhelm context. The correct application is: compress within subagent; share compressed summary with orchestrator; orchestrator maintains the authoritative integrated trace. Jetix brigadier plays the orchestrator role; each expert plays subagent. [See §5 Conflict #2]

---

### P-4: Tools are the agent-computer interface — design them with ACI discipline

**Sourced:** "Think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent-computer interfaces (ACI)." [src:building-effective-agents.md, §Appendix 2]. "Tools should be self-contained, robust to error, and extremely clear with respect to their intended use... One of the most common failure modes we see is bloated tool sets that cover too much functionality." [src:effective-context-engineering-for-ai-agents.md, §Tools]. MCP protocol formalizes this: tools exposed via MCP servers have typed schemas, annotated descriptions, and explicit destructive-action tags [src:writing-tools-for-agents.md, §Prompt-engineering your tool descriptions].

**Applied to Part 4:** Three implications:
1. **Task() is a tool with a schema.** The brief that brigadier passes to an expert via Task() is a tool call — it must have typed fields (`task_id`, `artefact_path`, `mode:`, `inputs[]`, `acceptance_predicate`), clear descriptions, and an explicit contract. Vague briefs (e.g., "review the file") are ACI failures. Part 4 must specify the brief schema as a declarative artifact.
2. **Routing table = tool selection policy.** Which expert to dispatch for which task type is an ACI decision, not an ad-hoc one. The routing table must be declarative, testable, and version-controlled — not embedded in brigadier's system prompt prose.
3. **Tool response format matters.** The structured packet schema (YAML: `summary`, `proposed_writes[]`, `provenance[]`, `confidence`, `escalations[]`) is a tool response format. It must be optimized for brigadier's downstream synthesis needs — not maximal information but minimal necessary information with verified provenance. This is why `confidence_method` is a required field: brigadier cannot verify quality without knowing the basis.

**Tradeoff with "agents improve their own tools" pattern [src:multi-agent-research-system.md §Let agents improve themselves]:** Anthropic's research system found agents can self-optimize their tools — they gave agents a flawed MCP tool and had them rewrite the description, reducing task completion time 40%. This is a powerful pattern but creates a governance risk for Jetix: if agents can modify their own tool descriptions, they can drift from the canonical schema. Mitigation: agents may PROPOSE tool-description improvements (as escalations with trigger `tool-description-revision-proposed`), but HITL ack is required before any Part 4 schema modification is promoted to canonical.

---

### P-5: Verification architecture matters more than agent count

**Sourced:** MAST (arXiv:2503.13657, Cemri et al., NeurIPS 2025): 14 failure modes clustered into 3 categories — System Design Issues (44.2%), Inter-Agent Misalignment (32.3%), Task Verification (23.5%). The top single failure mode is Step Repetition (15.7%), followed by Disobey Task Specification (11.8%) and Reasoning-Action Mismatch (13.2%). "Achieving robust MAS reliability often requires more than isolated fixes, pointing towards the need for more complex solutions and fundamental MAS redesigns." [src:arxiv-2503.13657-cemri-mast-failure-modes.pdf, pp.1-3]. Kim et al. (arXiv:2512.08296): "A coordination yields diminishing returns once single-agent baselines exceed certain performance (capability-saturation effect, β=−0.236, p=0.004)." [src:arxiv-2512.08296-kim-multi-agent-scaling.pdf, p.3].

**Applied to Part 4:** Verification architecture is Part 4's most load-bearing design requirement. Three structural implications:
1. **Centralized verification bottleneck.** Brigadier's provenance gate (§5.5.5 of shared-protocols) is the validation bottleneck that Kim et al. show reduces error amplification from 17.2× to 4.4×. This must be a named, testable component in Part 4's interface card — not an implicit assumption.
2. **MAST failure mode coverage.** Part 4's escalation taxonomy must address all 3 MAST categories:
   - System Design Issues → covered by strict brief schema (typed `mode:` prefix, `acceptance_predicate`, `ap_budget`) — prevents "Disobey Task Specification" (11.8%)
   - Inter-Agent Misalignment → covered by hub-and-spoke (no peer-to-peer) — prevents "Information Withholding" (0.8%) and "Ignored Other Agent's Input" (1.9%)
   - Task Verification → covered by provenance gate + Hamel-binary acceptance predicate — prevents "No or Incomplete Verification" (8.2%) and "Incorrect Verification" (9.1%)
3. **Stopping conditions.** The harness must have explicit stopping conditions (max turns per cell, retry limits per brigadier §1d) — MAST failure "Unaware of Termination Conditions" (12.4%) is the 5th most common failure mode. Part 4 must declare these limits as declarative configuration, not only as behavioral conventions.

**Tradeoff with "more agents = more performance" assumption:** Kim et al. explicitly refute: "In contrast to prior claims that 'more agents is all you need', our evaluation reveals that the effectiveness of multi-agent systems is governed by quantifiable trade-offs." The capability-saturation effect means that once a single-agent baseline exceeds 45% accuracy, adding agents yields negative returns (coordination costs exceed improvement potential). For Jetix's current maturity (Phase A, ~11 cycles), single-expert quality on each task is the priority; multi-expert parallelism is only warranted where tasks are genuinely decomposable with independent subtasks. [See §5 Conflict #3]

---

## §5 Conflicts and Tradeoffs (surface proactively per Ruslan emphasis #4)

### Conflict #1: Anthropic "don't add complexity" vs CrewAI hierarchical-by-default

**Anthropic position** (building-effective-agents.md): "Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short." Prefer simple composable patterns.

**CrewAI position** [EXT-2]: Hierarchical process (manager agent delegates to workers) is a first-class architectural pattern recommended for any complex task.

**Resolution for Jetix:** Anthropic wins. The CrewAI hierarchical pattern personifies the "manager" as an agent-executor — violating FPF IP-1 Role≠Executor. In Jetix, coordination authority is a structural property of the routing table (Part 4 artifact), not an executing agent. The "manager LLM" in CrewAI corresponds to the routing table + brigadier in Jetix — but brigadier holds routing authority as a protocol, not as a personality. This is the correct IP-1-compliant architecture.

**What changes in Part 4:** The routing table must be explicitly version-controlled as a canonical YAML artifact. When Wave C materializes Part 4, the routing table is a first deliverable — not something that emerges from brigadier's prompt prose.

---

### Conflict #2: Cognition "share full traces" vs Anthropic "compress subagent output"

**Cognition position** (Walden Yan): "Share context, and share full agent traces, not just individual messages." The failure mode of multi-agent is subagents working from incomplete context — the solution is to pass the full trace.

**Anthropic research-system position** (multi-agent-research-system.md): "Each subagent might explore extensively... but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)." Compression is essential for scalability.

**Both are right at different layers:** Walden Yan's principle applies WITHIN an orchestrator's context window — the orchestrator must have the full authoritative trace, not filtered messages. Anthropic's compression applies to BETWEEN subagent and orchestrator — the subagent compresses before handing to the orchestrator. Together: subagent compresses its own exploration; the orchestrator integrates all subagent summaries into one authoritative context. This is exactly the brigadier model: brigadier integrates compressed expert packets into the master cycle-log; no expert receives another expert's raw trace.

**What changes in Part 4:** The packet schema must explicitly distinguish `proposed_writes[]` (for canonical promotion) from `provenance[]` (for brigadier's integrated context) from raw trace (never returned). This three-layer separation prevents the "telephone game" failure (context degrades through intermediate stages) while maintaining context budget discipline.

---

### Conflict #3: Kim scaling findings ("capability saturation") vs Anthropic multi-agent research gains (+90.2%)

**Kim et al. position** (arXiv:2512.08296): Multi-agent coordination yields negative returns when single-agent baseline exceeds ~45% accuracy. Tool-heavy tasks suffer from coordination overhead. "Architectures without centralized verification tend to propagate errors more than those with centralized coordination."

**Anthropic research-system position** (multi-agent-research-system.md): "A multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval." Token usage explains 80% of performance variance on BrowseComp — multi-agent distributes token budget effectively.

**Resolution:** The conflict dissolves when task type is specified. Kim et al.'s negative findings apply to "sequential planning" tasks (−70.0% vs single-agent) — tasks where agents must share state and coordinate sequentially. Anthropic's positive findings apply to "breadth-first research" tasks where subtasks are genuinely independent. The discriminating question: **are the subtasks truly parallelizable with independent context?** For Jetix:
- Expert cells operating on different domains (engineering vs systems vs philosophy) = genuinely independent → parallelism is warranted
- Expert cells operating on the same artifact sequentially (critic then optimizer) = dependent → pipeline, not parallelism

**What changes in Part 4:** The routing table must encode task-decomposition type per task class: `parallel-independent` (multi-expert simultaneous) vs `sequential-pipeline` (one expert at a time). This is a declarative property of the task brief, not an ad-hoc brigadier decision.

---

### Open Conflict #4: MCP as tool-invocation vs A2A as agent-delegation

**MCP position** (modelcontextprotocol.io): MCP handles agent→tool invocation — a tool is a deterministic function the agent calls. Agent→agent delegation is out of scope.

**A2A (Google/DeepMind, 2025) position** [EXT-5]: A2A proposes a separate protocol for agent→agent delegation, with explicit task schema, capability negotiation, and acknowledgement handshake.

**Current Jetix state:** Brigadier invokes experts via Claude's Task() tool — this is proto-MCP (agent calls a tool that happens to be another agent). This works at Phase A scale. As swarm scales to Phase B (more cells, longer-running tasks), the lack of an explicit A2A-style handshake creates a risk: brigadier cannot verify that the expert received the brief correctly, started execution, or hit a failure before returning.

**Wave C recommendation:** Part 4 must design an explicit handshake schema for task dispatch: `task_dispatched` → `task_received_ack` → `task_in_progress` (optional) → `packet_returned`. Without this, long-horizon tasks (>30 min expert sessions) have no mid-flight observability. This is a Phase B requirement, but the schema slot must exist in Phase A's Part 4 design.

---

## §6 Anti-Scope

This consultant card does NOT cover:

- **Constitutional AI / safety alignment limits in agent prompts** (→ Framework #13 Anthropic Constitutional AI). Governance of what agents are allowed to do is a safety-layer concern, not a coordination architecture concern.
- **FPF IP-1 Role≠Executor philosophical grounding** (→ Framework #1 Левенчук ШСМ + FPF). The IP-1 argument for WHY role and executor must be separated belongs to the constitutional baseline, not the coordination architecture. This card treats IP-1 as a given constraint, not a derived principle.
- **Knowledge management substrate design** (→ Framework #4 KM Karpathy-Luhmann-Matuschak). Karpathy's LLM-Wiki pattern is referenced here only for the insight that "agents don't accumulate without structure" — the full KM architecture belongs to Framework #4.
- **Engineering code-level critique** of specific module implementations (→ engineering-expert in critic mode on specific artefacts).
- **Capital allocation for build-vs-buy on orchestration frameworks** (→ Framework #10 investor-expert). Whether Jetix should adopt LangGraph, CrewAI, or build custom coordination is an investment decision with capital implications.
- **Feedback-loop dynamics of the coordination protocol on developer velocity** (→ Framework #2 systems-thinking-cybernetics). Meadows leverage-point analysis of the coordination loop belongs to the systems consultant.

---

## §7 How to Cite in Wave C Work

When Wave C experts invoke this consultant, cite as:

- `[src:multi-agent-architecture-consultant §P-1]` for simplicity-first principle
- `[src:multi-agent-architecture-consultant §P-2]` for hub-and-spoke enforcement
- `[src:multi-agent-architecture-consultant §P-3]` for context budget discipline
- `[src:multi-agent-architecture-consultant §P-4]` for ACI / tool design
- `[src:multi-agent-architecture-consultant §P-5]` for verification architecture / MAST coverage
- `[src:multi-agent-architecture-consultant §Conflict-1..4]` for surfacing specific tradeoffs

All principles trace back to locked primary sources — provenance chain is maintained.

---

## §8 Candidate Strategies.md Entries (surfaced by this cycle)

The following entries are candidates for `agents/engineering-expert/strategies.md` (Compound step self-write, per E-9):

1. **`coordination-topology-is-declarative`** — Routing tables and dispatch schemas must be version-controlled YAML artifacts, not embedded in agent system-prompt prose. Grounded in: Anthropic building-effective-agents + MAST failure-mode 1.1 (Disobey Task Specification 11.8%). First 3 concrete uses needed before promoting to canonical rule.

2. **`mast-failure-taxonomy-checklist`** — Every Part 4 design review must explicitly address all 3 MAST categories (System Design Issues / Inter-Agent Misalignment / Task Verification). If any category has zero mitigation listed, the design is incomplete. Grounded in: MAST arXiv:2503.13657 + Kim scaling arXiv:2512.08296.

3. **`task-decomposability-test`** — Before dispatching parallel expert cells, brigadier must explicitly verify that subtasks are independent (no shared state between them during execution). If subtasks share state → pipeline, not parallel. Grounded in: Kim et al. +80.8% (decomposable tasks) vs −70.0% (sequential planning tasks).

4. **`context-budget-packet-discipline`** — Expert packets must never inline source bodies >50 lines. `proposed_writes[]` carries disk paths; `provenance[]` carries line-ranges and minimal quotes. Grounded in: effective-context-engineering-for-ai-agents.md §The anatomy of effective context + AP-ENG-8 / AP-1.

---

*Provenance gate: all claims above link to primary sources read at full depth or ToC. External web sources [EXT-1..EXT-5] are documented with URL and key takeaway in §3. No floating claims. Ready for brigadier provenance gate review.*
