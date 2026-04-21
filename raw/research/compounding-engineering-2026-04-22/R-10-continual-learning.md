# Continual Learning for LLM-based Agent Systems (2024–2026)
## Due-Diligence Report for Jetix — Berlin AI Consultancy

*Prepared: April 2026 · 11 Claude-based agents · 6 departments · Single operator*

---

## Executive Summary

Continual learning for LLM-based agents underwent a decisive reframing between 2023 and 2026. The academic definition — gradient-based weight updates that resist catastrophic forgetting — gave way to a practical one: the accumulation and retrieval of external state (memories, skills, knowledge graphs) that persists across context window boundaries. Modern production agents almost never update their weights in deployment. Instead they adapt through evolving external stores, and the 2024–2026 literature is overwhelmingly about the architecture, tooling, and failure modes of those stores.

Three architectural families now dominate production deployments. **File-based semantic memory** — markdown files injected into system prompts at session start — remains the most widely used pattern because it is transparent, version-controllable, and requires zero additional infrastructure. Anthropic's own engineers (Boris Cherny, creator of Claude Code) report working this way: "multiple parallel sessions, shared team memory in git, plan mode for everything non-trivial" [34]. **Managed vector + graph memory** — represented by Mem0 (48K GitHub stars, $24M Series A) and Zep/Graphiti — adds semantic retrieval over growing stores, at the cost of additional infrastructure or managed-service dependency. **Native Anthropic memory** — the memory tool (beta, September 2025) and Claude Projects — offers the tightest platform integration for Claude-based systems but currently lacks built-in semantic retrieval.

The benchmark evidence, though contested, favours Zep/Graphiti on temporal reasoning tasks (LongMemEval: 63.8% vs. Mem0's 49.0%, independent testing) and Mem0 on high-throughput personalisation (LoCoMo: 26% relative improvement over OpenAI's memory, 91% latency reduction). Letta's sleep-time compute architecture (April 2025) demonstrates a Pareto improvement — 5× compute reduction for equivalent accuracy — by running memory consolidation asynchronously during agent idle periods [19]. Anthropic's memory tool shows 39% agentic task improvement and 84% token reduction in internal evaluations, though no independent benchmarks exist [10].

Key failure modes that the practitioner literature consistently flags are memory poisoning (≥80% attack success rate at <0.1% corpus contamination [38]), context rot (measurable quality degradation starting well below context window limits, all 18 frontier models affected [42]), false memory consolidation via LLM-based summarisation [44], and temporal inconsistency when facts change but memory stores are not updated.

For Jetix, the current file-based architecture (wiki/ markdown + per-agent strategies.md + scratchpad.md + mailboxes.jsonl + voice-notes pipeline) is correctly classified as **System Prompt Learning + Voyager-style skill library** — the dominant practitioner pattern as of 2025–2026. It is not a technical debt problem but a deliberate transparency trade-off, strongly endorsed by both Anthropic's own engineering team and Andrej Karpathy's April 2026 "LLM Wiki" framework [4]. The ceiling of the current approach is the context window, not the pattern.

The concrete gaps relative to state-of-the-art are: no vector retrieval across the wiki, no temporal knowledge graph, no automatic memory consolidation, no cross-agent query API, and no evaluation harness for measuring whether memory improves task performance. Addressing these in phases — starting with Anthropic Claude Projects memory (zero cost, zero infrastructure) and sqlite-vec (zero-server semantic indexing), then optionally adding Letta sleep-time agents for consolidation — covers the most important gaps at minimal operational overhead for a single operator.

### Top 5 Key Findings

- **No production system beats the file-based baseline on transparency and maintainability** at Jetix's scale (11 agents, 1 operator). The gap between file-based and managed-SaaS approaches is narrowing as tooling matures, but the operational overhead of managed systems is not yet justified at this scale.
- **Zep leads on temporal reasoning; Mem0 leads on personalisation throughput.** These are different use cases. Temporal validity tracking (Zep's bitemporal model) matters for agents that track evolving facts; extraction throughput and cost efficiency (Mem0) matter for high-volume conversational memory.
- **Letta's sleep-time compute is the most architecturally compelling 2025 innovation.** Separating memory consolidation from active inference eliminates the latency cost of in-session memory management and directly addresses the "context rot" failure mode by keeping active context clean.
- **GDPR is an acute risk for any EU consultancy adopting managed memory.** Replika's €5M GDPR fine (May 2025), ChatGPT's EU/UK exclusion for its Reference Chat History feature, and the EDPB's 2025 Coordinated Enforcement Framework on the right to erasure all create specific obligations for Berlin-based deployments storing personal data in memory systems [17][18][49].
- **Benchmark scores are unreliable for procurement decisions.** The LoCoMo benchmark — most cited in vendor comparisons — has only 50 dialogues and no knowledge-update task. Independent testing regularly contradicts vendor-reported figures. The Zep vs. Mem0 benchmark dispute remains unresolved as of April 2026 [43].

---

## Section 1 — Definitions & Conceptual Landscape

### 1.1 Academic Anchors

**Lifelong learning**, as introduced in the neural-network literature, is the ability of a system to "continually acquire, fine-tune, and transfer knowledge and skills throughout its lifespan," mediated by mechanisms contributing to "the development and specialization of sensorimotor skills as well as to long-term memory consolidation and retrieval" [1]. Parisi et al. treat lifelong learning and continual learning as near-synonyms, both defined by the need for autonomous agents "interacting in the real world and processing continuous streams of information." The central obstacle is **catastrophic forgetting (catastrophic interference)**: the continual acquisition of "incrementally available information from non-stationary data distributions generally leads to catastrophic forgetting or interference," a fundamental failure mode of gradient-descent trained neural networks when task distributions shift [1].

**Continual learning** is the narrower, task-centric operationalisation. De Lange et al. define it as "shifting the paradigm towards networks that can continually accumulate knowledge over different tasks without the need to retrain from scratch," focusing on sequential task arrival with "clear boundaries" [2]. Their 2021/2022 survey introduces the **stability–plasticity trade-off** as the organising framework: a continual learner must simultaneously maintain stability (resist forgetting prior tasks) and plasticity (accommodate new information). Mitigation strategies group into regularisation (penalising weight drift), parameter isolation (task-specific sub-networks), and replay (rehearsal or generative replay of prior task data) [2].

**Online learning** is technically distinct from both: sequential sample-by-sample parameter updating with no task-boundary assumption. In the LLM context it typically means gradient updates on a stream of tokens without discrete task labels — a stricter engineering requirement than externalising new facts into a store.

### 1.2 The LLM-Agent Reframing (2023–2026)

When applied to LLM-based agents, all three classical terms undergo a conceptual shift. The primary reason: **modern LLMs rarely update their weights in production.** Instead, adaptation occurs through external state — context windows, vector databases, knowledge graphs, and tool-generated outputs. Zheng et al. (2025) treat "lifelong learning, also known as continual or incremental learning" as "a crucial component for advancing AGI by enabling systems to continuously adapt in dynamic environments," explicitly distinguishing LLM agents from prior ML models because "LLM agents are designed to interact with dynamic environments and perform intricate tasks… requiring advanced lifelong learning capabilities to manage multimodal inputs, execute sequential decision-making processes, and maintain coherent performance across diverse and evolving tasks" [3].

Letta/MemGPT coined the phrase **continual learning in token space** to describe their foundational paradigm: "updates to learned context, not weights, should be the primary mechanism for LLM agents to learn from experience" [4]. Letta formalises the agent as the pair (θ, C) where θ is the frozen model and C is the evolving learned context, and the optimisation objective is to minimise cumulative loss across sequentially arriving tasks by updating C rather than θ. This is a significant conceptual departure from the classical academic definition — no gradient descent on model parameters occurs — yet it is the operative definition in virtually all production deployments.

Anthropic avoids the term "continual learning" entirely. Their 2025 blog on context engineering defines **context engineering** as "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference," framing it as the evolution beyond prompt engineering [6]. Separately, their memory tool is described as enabling "agents to build up knowledge bases over time" through a file-based system [10].

Mem0 positions itself as providing "a scalable memory-centric architecture that addresses [context-window limitations] by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations," approximating "human cognitive processes of selective storage and consolidation" [7].

### 1.3 Terminological Overloading

The field has a significant **terminological overloading problem**. Four distinct phenomena frequently share the label "learning" in the LLM-agent literature:

1. **Weight-parametric continual learning** — gradient-based adaptation (the classical academic definition).
2. **Non-parametric memory accumulation** — storing new information in external databases without weight changes (Mem0, MemGPT, Generative Agents).
3. **In-context adaptation** — exploiting the context window for new tasks without persistent state (few-shot prompting, ReAct).
4. **Reflective self-improvement** — generating verbal summaries of past mistakes stored and reused across sessions (Reflexion, Generative Agents reflections).

Only (1) satisfies the classical definition. However, (2) and (4) dominate the production literature, and many key papers — including Letta's own blog — explicitly claim they are doing "continual learning" while using only token-space updates [4]. Practitioners must clarify which definition is operative when evaluating a memory architecture.

### 1.4 Distinction from Adjacent Concepts

**Fine-tuning** (including LoRA and QLoRA) updates the parameters θ of a pre-trained model via gradient descent. Parameter-efficient fine-tuning via LoRA adds low-rank adapter matrices to existing weight layers, enabling adaptation with a fraction of trainable parameters [8]. Fine-tuning is the only method in this taxonomy that modifies model weights.

**Knowledge distillation** transfers the "knowledge" of a large teacher model into a smaller student by training on the teacher's output distribution (soft labels). Distillation can consolidate memories accumulated in a RAG or episodic store back into model weights — a process sometimes called *sleep consolidation* by analogy with biological memory [9].

**Retrieval-Augmented Generation (RAG)** augments the context window at inference time with passages retrieved from an external corpus via dense vector similarity. Model parameters are not changed; knowledge is injected as context tokens [10]. RAG is fundamentally stateless with respect to the retrieval corpus unless the corpus is explicitly updated.

**In-Context Learning (ICL)** exploits the LLM's ability to adapt outputs based solely on examples placed in the context window. No persistence occurs across inference calls; ICL is purely ephemeral.

**Episodic memory** stores individual interaction events — timestamped observations, conversation turns, agent actions — in an external database, retrievable by similarity or recency. The canonical implementation is the memory stream in Generative Agents (Park et al., 2023), which "stores a complete record of the agent's experiences using natural language" and retrieves memories via a composite score combining recency, importance, and relevance [11].

**Semantic memory / knowledge graphs** organise extracted facts into structured relational representations. GraphRAG (Edge et al., 2024) builds entity knowledge graphs from corpora and uses community detection to enable global sensemaking [12]. HippoRAG (Gutierrez et al., 2024) models the hippocampal indexing theory, using a knowledge graph where "PPR enables HippoRAG to explore KG paths and identify relevant subgraphs, essentially performing multi-hop reasoning in a single retrieval step" [13].

**Procedural memory / skill libraries** store reusable executable behaviours. Voyager (Wang et al., 2023) implements an "ever-growing skill library of executable code for storing and retrieving complex behaviors," where the "skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting" [14].

**Weight-update taxonomy:**

| Method | Changes Model Weights? | Persistence Mechanism |
|---|---|---|
| Fine-tuning (full) | **Yes** | Parameters θ |
| LoRA / QLoRA | **Yes** (adapter matrices only) | Adapter parameters |
| Knowledge distillation | **Yes** (student model) | Student parameters |
| RAG (vector retrieval) | No | External vector store |
| In-context learning | No | Context window only (ephemeral) |
| Episodic memory (MemGPT/Generative Agents) | No | External DB + context injection |
| Semantic memory / KG (GraphRAG, HippoRAG) | No | Knowledge graph |
| Procedural memory / skill library (Voyager) | No | Code/text library in external store |
| Temporal KG (Zep/Graphiti) | No | Bi-temporal knowledge graph |
| MEMORYLLM / Memory³ | **Yes** (memory pool in latent space) | Dedicated memory parameters |

---

## Section 2 — Research Frontier 2024–2026

The ten papers below were selected for architectural novelty, empirical impact, and direct relevance to production memory design. They are presented in rough chronological order.

### 2.1 Reflexion — Language Agents with Verbal Reinforcement Learning (2023)

**Paper:** Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," *arXiv:2303.11366*, NeurIPS 2023 [17].

Reflexion introduces a framework in which an LLM agent improves by generating *verbal* feedback on its own failed attempts rather than by gradient-based weight updates. Three LLM roles compose the architecture: an *Actor* that generates actions, an *Evaluator* that scores outcomes, and a *Self-Reflection* model that produces textual summaries of what went wrong. "This self-reflective feedback acts as a 'semantic' gradient signal by providing the agent with a concrete direction to improve upon" [17]. Reflections are stored in a bounded episodic memory buffer (typically capped at 3 prior reflections) appended to the context for subsequent attempts.

**Results:** HumanEval Python coding: **91.0% pass@1**, surpassing GPT-4's 80.1%. AlfWorld (134 environments): **130/134 tasks** completed, 22% absolute improvement over ReAct. HotPotQA: GPT-4 + Reflexion achieves **0.80** vs. 0.68 baseline.

**Limitation:** The sliding-window episodic buffer has hard capacity limits; the authors note that long-term storage would be needed for multi-session continuity. Reflexion also fails to improve on WebShop tasks requiring creative exploration beyond self-reflection [17].

### 2.2 Generative Agents — Interactive Simulacra of Human Behavior (2023)

**Paper:** Park et al., "Generative Agents: Interactive Simulacra of Human Behavior," *arXiv:2304.03442*, UIST 2023 [11].

Generative Agents introduces the canonical three-layer memory architecture: a **memory stream** (chronological log of all observations in natural language), **reflection** (periodic synthesis of higher-level insights), and **planning** (forward-looking action sequencing). The retrieval function scores memories as `score = α·recency + β·importance + γ·relevance`, using exponential decay (factor 0.995/hour), LLM-scored importance (1–10), and cosine embedding similarity as the three components with equal weights [11].

**Results:** Ablation studies demonstrate that all three architectural components contribute critically to believable agent behaviour. Agents autonomously propagated party invitations across 25 characters over two simulated days — emergent social coordination arising from individual memory retrieval without explicit multi-agent communication protocols.

**Limitation:** Significant LLM API cost because every observation is processed and scored. Importance scoring relies on LLM self-evaluation, which may be inconsistent. No formal evaluation of long-term consistency beyond 24 simulated hours [11].

### 2.3 Voyager — Open-Ended Embodied Lifelong Learning (2023)

**Paper:** Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models," *arXiv:2305.16291*, 2023 [14].

Voyager is the first demonstrated lifelong-learning agent using LLMs as a policy backbone. Its three components address continual learning directly: (1) an **automatic curriculum** proposing tasks of increasing complexity based on current capability, (2) an **ever-growing skill library** storing GPT-4-generated JavaScript programs each validated via self-verification before storage, and (3) an **iterative prompting mechanism** incorporating environment feedback for in-context program repair. Voyager "interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning" [14] — making it a purely non-parametric continual learner.

**Results:** **3.3× more unique items** obtained, **2.3× longer distances** travelled, and key tech-tree milestones unlocked **up to 15.3× faster** than prior state-of-the-art. The skill library transfers to a new Minecraft world, enabling task completion where previous agents fail.

**Limitation:** Depends on GPT-4's code generation quality; open-source variants degrade significantly. Evaluation is limited to a single environment (Minecraft) [14].

### 2.4 MemGPT — Towards LLMs as Operating Systems (2023)

**Paper:** Packer et al., "MemGPT: Towards LLMs as Operating Systems," *arXiv:2310.08560*, 2023 (became Letta in 2024) [5].

MemGPT proposes **virtual context management**, a direct analogy to OS virtual memory paging: "a technique drawing inspiration from hierarchical memory systems in traditional operating systems which provide the illusion of an extended virtual memory via paging between physical memory and disk" [5]. The memory hierarchy comprises: (a) **main context** (active LLM prompt, split into system instructions, a fixed-size working context block, and a FIFO queue); (b) **recall storage** (searchable message database); and (c) **archival storage** (read/write database for arbitrary-length text). The agent manages its own context via function calls (`recall_memory_search`, `archival_memory_insert`, `archival_memory_search`) and chains multiple calls using `request_heartbeat=true`.

**Results:** On the Deep Memory Retrieval (DMR) benchmark (50 questions requiring cross-session recall), MemGPT+GPT-4 achieves **92.5% accuracy** vs. 32.1% for baseline GPT-4. MemGPT+GPT-4 Turbo reaches **93.4%** [5].

**Limitation:** "MemGPT has significantly degraded performance using GPT-3.5, due to its limited function calling capabilities." The system also tends to stop paging through retrieval results before exhausting the database, capping effective recall depth [5].

### 2.5 Self-RAG — Learning to Retrieve, Generate and Critique (2023)

**Paper:** Asai et al., "Self-RAG: Learning to Retrieve, Generate and Critique through Self-Reflection," *arXiv:2310.11511*, ICLR 2024 [18].

Self-RAG trains a single LLM to decide *when to retrieve* and *evaluate quality of retrieved passages* using special reflection tokens (Retrieve, ISREL, ISSUP, ISUSE). Retrieval is adaptive rather than fixed-K; segment-level beam search ranks candidate outputs by a composite critique score. This differs from standard RAG in that retrieval is agent-initiated and self-critique is built into the generation process.

**Results:** Self-RAG 7B achieves **54.9% accuracy on PopQA** (vs. 20.0% for Llama2-7B without retrieval), **72.4% on PubHealth**, and **81.2% FactScore on biography generation**, outperforming ChatGPT on multiple tasks despite being a far smaller model [18].

**Limitation:** Critic training relies on expensive GPT-4 annotations. Performance depends on the retrieval model quality [18].

### 2.6 GraphRAG — From Local to Global (2024)

**Paper:** Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization," *arXiv:2404.16130*, Microsoft Research, 2024 [12].

GraphRAG addresses a fundamental gap in standard vector RAG: inability to answer *global* sensemaking questions about an entire corpus. The pipeline builds an entity knowledge graph using LLM-based entity/relationship extraction, applies Leiden community detection hierarchically to produce a tree of community summaries, and uses map-reduce over community summaries for global queries. "GraphRAG contrasts with vector RAG in its ability to answer queries that require global sensemaking over the entire data corpus" [12].

**Results:** LLM-as-a-judge evaluation on ~1M-token corpora shows GraphRAG beats standard semantic search by **72–83% win rate on comprehensiveness** and **62–82% on diversity**, all significant at p < 0.001.

**Limitation:** Graph construction is expensive (requires LLM calls per document chunk) and static — updates require re-running community detection. Evaluation relies on LLM-as-a-judge without gold-standard answers [12].

### 2.7 HippoRAG and HippoRAG 2 — Neurobiological Memory Indexing (2024–2025)

**Papers:** Gutierrez et al., "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models," *arXiv:2405.14831*, NeurIPS 2024 [13]; Gutierrez et al., "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models," *arXiv:2502.14802*, ICML 2025 [16].

HippoRAG draws on the hippocampal indexing theory to design retrieval architecture mimicking human associative memory. An LLM performs OpenIE on passages to extract knowledge-graph triples; retrieval uses **Personalized PageRank (PPR)** from query-entity seed nodes, propagating activation through multi-hop graph paths in a single retrieval step. HippoRAG 2 adds passage nodes to the knowledge graph for deeper passage-level activation alongside phrase-level PPR.

**Results (HippoRAG):** On multi-hop QA, HippoRAG achieves R@2 of **41.0 on MuSiQue**, **71.5 on 2WikiMultiHopQA**, and **60.5 on HotpotQA**, outperforming ColBERTv2 alone by 3.1–11.3 points. "Single-step HippoRAG is on par or outperforms IRCoT while being 10–30 times cheaper and 6–13 times faster during online retrieval" [13].

**HippoRAG 2:** "7% improvement in associative memory tasks over the state-of-the-art embedding model" [16]. Average F1 of **59.8** vs. 57.0 for NV-Embed-v2, with +13.5 F1 on MuSiQue and +19.0% on HotpotQA Recall@5.

**Limitation:** NER errors account for 48% of retrieval failures. Memory requirements for HippoRAG 2 are substantially higher (9.9 GB GPU vs. 1.7 GB for embedding baselines) [13][16].

### 2.8 Mem0 — Production-Ready Agents with Scalable Long-Term Memory (2025)

**Paper:** Chhikara et al., "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory," *arXiv:2504.19413*, April 2025 [7].

Mem0 addresses the deployment gap between research memory systems and production AI agents. On every message pair: (1) an LLM extracts salient facts as atomic memory units; (2) the top-10 semantically similar existing memories are retrieved and the LLM decides ADD, UPDATE, DELETE, or NOOP; (3) embedding-based nearest-neighbour search occurs at query time. An enhanced variant, Mem0g, replaces the flat vector store with a Neo4j knowledge graph.

**Results:** On LOCOMO benchmark (10 conversations, ~26K tokens each), Mem0 achieves **67.13% LLM-as-a-Judge** overall, a **26% relative improvement over OpenAI's memory system** (52.90%). Compared to full-context (72.90% J), Mem0 reduces p95 latency by **91%** (1.44s vs. 17.12s) and **saves >90% of token cost** [7].

**Limitation:** Full-context still outperforms Mem0 on overall J (72.90% vs. 66.88%), indicating information loss in extraction. Independent LongMemEval benchmarks give Mem0 a lower score (49.0%) than the paper's favourable framing [3][7].

### 2.9 Sleep-Time Compute — Beyond Inference Scaling at Test-Time (2025)

**Paper:** Lin et al. (Letta / UC Berkeley), "Sleep-time Compute: Beyond Inference Scaling at Test-time," *arXiv:2504.13171*, April 2025 [19].

Sleep-time compute introduces a paradigm in which agents perform inference during **idle periods between user interactions** to pre-compute context enrichment. The agent decomposes its prompt into static context c and dynamic query q, and during sleep applies test-time scaling (chain-of-thought, summary, hypothesis generation) to produce enriched context c′ stored in a "rethink memory block." At query time, the agent reads c′ instead of reasoning from scratch. "Sleep-time compute: where inference is done between interactions with the model while it would otherwise be idle" [19].

**Results:** A **Pareto improvement** — "reducing the test-time compute needed to achieve the same accuracy by ~5×." On Stateful AIME, accuracy improves by **18%**; on GSM-Symbolic P2, by **13%**. When 10 queries share one context, average cost per query is reduced by **2.5×** [19].

**Limitation:** Effectiveness correlates strongly with query predictability. At high test-time compute budgets, standard test-time scaling can outperform sleep-time [19].

### 2.10 Anthropic Context Engineering and Memory Tool (2025)

**Source:** Anthropic Engineering Blog, "Effective Context Engineering for AI Agents," September 29, 2025 [6].

Anthropic's 2025 blog synthesises production experience into a **context engineering** framework — "the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information" [6]. Three concrete strategies are described: (1) **Compaction** — summarising conversations approaching context limits and reinitiating with the summary; (2) **Structured note-taking (agentic memory)** — "the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times"; (3) **Multi-agent architectures** — sub-agents perform focused tasks with clean context windows, returning "a condensed, distilled summary of its work (often 1,000–2,000 tokens)" to the orchestrator. Alongside the blog, Anthropic released a memory tool in public beta on the Claude Developer Platform.

**Key metric (internal evaluation):** 39% performance improvement on agentic search tasks and 84% token reduction in a 100-turn web search evaluation [10].

**Limitation:** "The art of compaction lies in the selection of what to keep versus what to discard, as overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later" [6].

---

## Section 3 — Methods Comparison

### 3.1 Trade-Off Table

| Method | Compute Cost | Latency | Forgetting Resistance | Knowledge Recall | Explainability | Weight Update? | Best Use Case |
|---|---|---|---|---|---|---|---|
| **LoRA / QLoRA fine-tuning** | High (GPU cluster) | Low at inference | High (baked in weights) | High for trained domain; degrades OOD | Low (opaque) | **Yes** | Stable domain adaptation; compliance-critical knowledge embedding |
| **RAG (vector/semantic)** | Low–Medium (embedding + ANNS) | Low–Medium (~50–300ms) | Medium (corpus update required) | High for factual recall if well-indexed | Medium (passages citable) | **No** | Dynamic knowledge bases; citation-required applications |
| **Episodic memory (MemGPT/Generative Agents)** | Medium (LLM function calls) | Medium (~150–500ms search) | High (events stored, not overwritten) | Medium–High (depends on retrieval) | High (natural-language auditable) | **No** | Multi-session personalised agents; long-running task continuity |
| **Semantic KG (GraphRAG, HippoRAG, Zep)** | High (graph construction + maintenance) | Medium–High (traversal + reranking) | High (explicit relations; temporal invalidation in Zep) | Very High for multi-hop relational queries | Very High (entity–relation inspectable) | **No** | Enterprise knowledge; multi-hop reasoning; temporal fact tracking |
| **Procedural memory / skill library (Voyager)** | Medium (code generation + validation) | Low (skills are code, fast to execute) | Very High (verified programs, no interference) | Very High for covered task types | High (code is human-readable) | **No** | Tool-using agents with repeated task patterns; coding agents |
| **Knowledge distillation** | Very High (training data + teacher) | Very Low (no retrieval) | High for distilled knowledge; opaque to post-distillation updates | High within distilled scope | Low | **Yes** (student) | Model compression; offline consolidation of mature retrieval corpora |
| **Sleep-time compute (Letta)** | Medium (idle-period compute) | Very Low at query time (pre-computed) | High (proactive consolidation prevents rot) | High (pre-processed context) | Medium (rethink block readable) | **No** | Long-lived agents with predictable context; recurring clients/tasks |

### 3.2 When Each Method Wins

**LoRA / QLoRA fine-tuning** is the right choice when an organisation has a stable, well-defined domain corpus, latency requirements are strict, and model outputs must reflect deep domain expertise in generated text style as well as content. Its fundamental weakness is that it cannot update knowledge after deployment without a new training run, making it unsuitable for facts that change frequently.

**RAG with vector retrieval** is the production workhorse for most enterprise applications. The corpus can be updated without retraining, and retrieved passages provide citation trails. Its failure mode is reliance on embedding similarity: topically adjacent but non-answering passages can crowd out correct evidence ("lost in the middle"). Self-RAG partially addresses this via retrieval critiquing [18]; HippoRAG 2 addresses multi-hop failures via graph traversal [16].

**Episodic memory** wins when the agent needs to personalise over time — remembering user preferences, tracking task progress across sessions, or adapting tone based on prior interaction patterns. The key design challenge is the promotion rule: which observations are worth storing as memories vs. letting them expire in the FIFO queue. The Generative Agents importance score provides one principled answer [11]; Mem0's LLM-based extraction filter provides a production-ready alternative [7].

**Semantic memory / knowledge graphs** win for structured enterprise knowledge where relationships matter: product catalogues, organisational hierarchies, compliance rule networks, or any domain requiring multi-hop inference. Zep/Graphiti adds temporal fact tracking — the key missing feature in all static KG approaches [24]. The main deterrent is upfront indexing cost and graph maintenance overhead.

**Procedural memory / skill libraries** shine for agents that must repeatedly execute the same categories of complex actions. Voyager's verified-code library virtually eliminates catastrophic forgetting because skills are immutable once validated [14]. The pattern extends naturally to tool-using agents: a code-writing agent that saves and retrieves verified helper functions is implementing Voyager-style procedural memory.

### 3.3 Memory Hierarchies in Production LLM Agents

All major production agent architectures converge on a three-tier memory hierarchy analogous to CPU/RAM/disk in operating systems.

**Short-term (in-context) memory** is the live context window — the set of tokens the LLM attends to during a single inference call. It is fast (zero retrieval latency), fully attended, and *brutally finite*: even a 200K-token Claude window fills within a few hundred turns of a rich multi-tool conversation. Anthropic explicitly warns that "even as models get better, context will remain a bottleneck" and that "LLMs are constrained by a finite attention budget" [6].

**Medium-term (session / working) memory** refers to state maintained within a single extended session but not necessarily persisted to long-term storage. In Letta's architecture, "all state, including memories, user messages, reasoning, tool calls, are all persisted in a database, so they are never lost, even once evicted from the context window" [27] — the session/working memory distinction collapses because everything is journaled.

**Long-term (persistent) memory** lives in an external store — a vector database (Pinecone, Weaviate, pgvector), a relational database, a knowledge graph (Neo4j/Zep), or a document store. It is durable across sessions, can grow without bound, and requires an explicit retrieval trigger.

**Promotion rules — how observations move from ephemeral context into durable long-term storage — are the central design decision:**

- *MemGPT / Letta:* Promotion is agent-controlled via function calls (`archival_memory_insert`). The FIFO queue auto-summarises evicted messages into a recursive summary [5]. Letta's `core_memory_append` and `core_memory_replace` control the in-context working scratchpad.
- *Generative Agents:* Every observation is automatically appended to the memory stream. Periodic reflection synthesises higher-level insights when accumulated importance exceeds a threshold [11].
- *Mem0:* LLM-selective extraction — for each message pair, the extraction function identifies salient facts, the update function handles conflicts, and only extracted memories are stored [7].
- *Anthropic context engineering:* Promotion triggered by compaction events or explicit agent note-taking. The Claude memory tool uses a file-based system as the long-term store [6].

**Named system memory architecture comparison:**

| System | In-Context Block | Session/Working Memory | Long-Term Store | Retrieval Trigger | Promotion Rule |
|---|---|---|---|---|---|
| **MemGPT / Letta** | System prompt + working context + FIFO queue | FIFO with recursive summary at index 0 | Recall DB + archival DB | Agent-initiated function call | Agent decides via `archival_memory_insert` |
| **Generative Agents** | Planning context (reflection summary + retrieved memories) | N/A (single-session) | Memory stream (append-only flat log) | Per-action retrieval (every decision) | Auto-append all observations; synthetic reflections on threshold |
| **Mem0** | Conversation summary S + top-k extracted memories | Rolling summary S | Vector DB + optional graph | Query-time embedding NN search | LLM extraction filter (ADD/UPDATE/DELETE/NOOP) |
| **Zep / Graphiti** | Retrieved KG context | N/A | Temporal KG (episode + semantic + community subgraphs) | Text-query multi-step search | All ingested episodes → entity extraction → bi-temporal KG update |
| **Anthropic (Claude Code)** | System prompt + recent turns + retrieved notes | Tool result history | File-based memory tool / NOTES.md | Context nearing limit (compaction) or explicit agent write | Agent writes notes; compaction summarises on overflow |

---

## Section 4 — Tooling Deep Dive

### 4.1 Mem0

**mem0.ai · github.com/mem0ai/mem0 · ~48K GitHub stars · $24M Series A (YC, October 2025)**

Mem0 implements a **hybrid two-pipeline architecture**: a vector store for semantic search (episodic/semantic facts), an optional knowledge graph for relational memory (Mem0g), and key-value metadata indexing [1]. The core processing loop on every message pair: (1) **Extraction phase** — an LLM identifies salient facts from the latest conversation turn and a rolling summary; (2) **Update phase** — each candidate fact is compared against existing memories via vector similarity (top-k cosine) and a second LLM call decides ADD, UPDATE, DELETE, or NOOP [7].

Mem0 (base) stores memories as dense natural language strings in a pluggable vector database (Qdrant, ChromaDB, Pinecone, FAISS supported). Mem0g represents memories as a directed labelled graph G=(V, E, L) where nodes are typed entities with embeddings. The graph backend defaults to Neo4j; Kuzu (embedded, serverless) was added in September 2025 as a lower-overhead alternative [2]. Memory is scoped across three namespaces: user-level, session-level, and agent-level. Importantly, there is no native temporal validity window — facts are timestamped at creation but cannot model "this fact was true between T1 and T2" [3].

**Benchmarks:**

- LoCoMo (Mem0 paper, April 2025): **26% relative improvement over OpenAI's built-in memory**, 91% lower p95 latency vs. full-context, >90% token cost reduction. Mem0 p95 latency: **1.44s**; full-context: 17.12s [7].
- Mem0's newer token-efficient algorithm (April 2026 research page): LoCoMo **91.6**, LongMemEval **93.4**, mean tokens per retrieval **<7,000** [5].
- Independent LongMemEval (vectorize.io): Mem0 **49.0%**, Zep **63.8%** — a 15-point gap attributable to Mem0's lack of temporal fact modelling [3].

**Cost:** Free tier (10K memories); Starter $19/mo; Pro $249/mo (adds graph memory, SOC 2/HIPAA); Enterprise custom. Graph features are gated to the $249/mo Pro tier — a 13× jump from Starter [9].

**Claude ecosystem fit:** External integration via API/SDK. Works cleanly with Claude API. MCP server enables use in Claude Desktop and Cursor. No native Claude Agent SDK support; integration requires implementing memory retrieval and injection in the system prompt. For Jetix's 11-agent deployment, Mem0 is viable as a shared memory layer with per-agent scoped namespacing, but graph memory requires Pro tier.

**Limitations:** No temporal validity windows; graph features paywalled; multi-agent memory requires custom scoping; LLM dependency at write time adds per-operation cost. Benchmark self-promotion concern: the Mem0 paper uses Mem0's own LLM judge and eval model [3][7].

### 4.2 Letta (formerly MemGPT)

**letta.com · github.com/letta-ai/letta · OSS under Apache 2.0**

Letta is built on the MemGPT paper's OS-inspired virtual context management [5]. The central insight — described by Charles Packer — is that agents should manage memory the way operating systems manage physical memory: with hierarchical tiers, paging, and self-directed movement of information between storage levels.

> "In Claude Code — and every other coding CLI — every time you want to work on a task, you spin up a new 'agent'... The agent is brand new — it doesn't know anything about you. In contrast, Letta Code is fully stateful. The idea is that you work with a small handful of agents that get better and better over time." — Charles Packer, CEO Letta [86]

**Three-tier memory hierarchy:**

1. **Core memory (in-context)**: Fixed-size blocks always resident in the LLM context window, divided into `human` block (facts about the user) and `persona` block (agent identity/instructions). Modified via `core_memory_append`, `core_memory_replace` tool calls.
2. **Archival memory (external, out-of-context)**: Long-term RAG-style storage in a vector database (LanceDB default). Accessed via `archival_memory_insert` and `archival_memory_search`.
3. **Recall memory (external, out-of-context)**: The complete uncompressed conversation history. Searchable via `conversation_search` and semantic search. Never lost; FIFO summarisation moves oldest turns to recall rather than discarding them [5].

In 2025, Letta introduced the **sleep-time agent** architecture: a background sleep-time agent runs asynchronously between conversations, reads the primary agent's conversation history and archival memory, and rewrites the primary agent's core memory blocks to produce cleaner, denser learned context [19][22].

> "Your brain is always enhancing itself, absorbing more information like a sponge. With language models, it's almost the opposite. If you run these models in a loop for an extended period, the context becomes tainted; they become disoriented, and you simply want to restart." — Charles Packer, Wired, 2025 [24]

**Benchmarks:** DMR: 93.4% (GPT-4-turbo), narrowly below Zep's 94.8% [81]. On LoCoMo, MemGPT lags Mem0 by more than 25 points in J score [7]. LongMemEval was not successfully evaluated for MemGPT due to message-ingestion limitations [81].

**Cost:** Pro $20/mo (20 stateful agents); Max Lite $100/mo; Max $200/mo; API Plan $20/mo base + $0.10/active agent/mo + $0.00015/sec tool execution.

**Claude ecosystem fit:** Strong. Letta explicitly supports Claude models (`anthropic:claude-*` in agent configuration). Sleep-time agents can use a lighter model (Haiku 4.5) for conversation and a heavier model (Opus 4) for memory consolidation. Native multi-agent memory sharing is valuable for Jetix's multi-agent setup.

**Limitations:** Context window overhead from core memory blocks; original MemGPT single-agent bundling addressed by sleep-time architecture; lock-in to Letta runtime schema.

### 4.3 Zep + Graphiti

**getzep.com · github.com/getzep/graphiti · ~24K GitHub stars (Graphiti, Apache 2.0)**

Zep's memory layer is powered by **Graphiti**, a temporally-aware knowledge graph engine [81][82]. The fundamental architectural difference from Mem0: **time is a first-class data dimension**.

The knowledge graph G = (N, E, φ) is organised into **three hierarchical subgraphs:** episode subgraph (raw conversational episodes, non-lossy), semantic entity subgraph (extracted entities with relationships and community summaries), and community subgraph (higher-order clusters reducing retrieval noise). **Bitemporal modelling** is the key differentiator: every edge carries an *event time T* (when the fact occurred) and *ingestion time T'* (when it was added), plus a validity window (`valid_from`, `valid_to`, `invalid_at`). When a fact is superseded (e.g., user changes job), Zep updates the validity window rather than deleting — enabling queries like "What was true on March 15?" [81].

Retrieval combines three strategies: semantic embedding search, BM25 keyword search, and graph traversal — a genuine hybrid, not vector-primary with graph as an add-on. Graphiti MCP Server v1.0 shipped November 2025 [83].

**Benchmarks:**

- DMR: **94.8%** (GPT-4-turbo), **98.2%** (GPT-4o-mini) vs. MemGPT's 93.4% [81].
- LongMemEval: **+18.5% accuracy improvement** over full-context baseline (GPT-4o), **–90% latency**. Zep median latency: **2.58s**; full-context baseline: 28.9s. Independent absolute score: **63.8%** [3][82].
- *Caveat:* Zep's graph construction involves asynchronous background processing; immediate retrieval attempts after ingestion may fail — re-running after a delay yields better results [7].

**Cost:** Free (1K credits); Flex $25/mo (full feature access); Enterprise custom. All features available at every tier — no capability paywalling. SOC 2 Type 2 and HIPAA compliant [83].

**Claude ecosystem fit:** Good via the Graphiti MCP Server, which provides direct integration with Claude Desktop and any MCP client. Not a native Claude tool. For Jetix, Zep's temporal modelling is the strongest fit for use cases where facts change (client status, project state, team composition).

**Limitations:** Zep Community Edition was deprecated April 2025, removing full self-hosting; only the Graphiti engine (open-source) remains self-hostable, requiring three systems to provision (Graphiti + graph DB + optional embedding service). Async ingestion delays can affect real-time freshness [83][32].

### 4.4 Cognee

**cognee.ai · github.com/topoteretes/cognee · ~14.1K GitHub stars · $7.5M seed (February 2026)**

Cognee is an **ontology-driven knowledge graph engine** with a modular **ECL (Extract, Cognify, Load) pipeline** [13][14]. **Extract:** Ingest raw content from 38+ source types (PDFs, APIs, databases, audio, images), chunked and normalised. **Cognify:** LLM-powered transformation — generate embeddings, identify entities, map relationships, build knowledge graph structure. Optionally adds temporal cognification (timestamps, event-before/after/during relations). A `memify` layer rates and weights edges based on feedback, so the graph sharpens over time. **Load:** Write both vector embeddings (LanceDB default) and graph structures (Kuzu default) to their respective backends.

The result is a **poly-store architecture**: knowledge graph (Kuzu or Neo4j) + vector store (LanceDB, Qdrant, Weaviate, etc.) + relational/columnar store (DuckDB for SQL analytics). Cognee describes itself as a "self-improving memory graph" — the `memify` feedback loop adjusts edge weights based on response ratings [14].

**Temporal cognification** (open-source core, November 2025): When enabled, the ECL pipeline extracts explicit temporal cues and materialises event-centric graph nodes with before/after/during edges [13].

**Benchmarks:** No Cognee-specific LoCoMo or LongMemEval published numbers. This is a meaningful due-diligence gap for a system at its commercial stage [15].

**Cost:** Open-source (Apache 2.0) with self-hosted deployment as the primary path. Enterprise pricing on request.

**Claude ecosystem fit:** External integration only. Claude integration via LLM provider abstraction. CLAUDE.md present in repository. No native Claude Agent SDK or Anthropic-specific tooling. For Jetix, Cognee is most compelling for building a knowledge base from diverse document sources (client documents, research papers, codebase semantics) — the use case most analogous to Jetix's existing wiki entity structure.

**Limitations:** No published benchmarks; smaller community than Mem0 or Zep; ECL pipeline complexity; early commercial stage ($7.5M seed in February 2026 means enterprise SLAs and compliance certifications are not yet equivalent to Mem0 or Zep) [15][17].

### 4.5 Anthropic Memory Tool

**docs.anthropic.com/en/docs/agents-and-tools/memory-tool**

Anthropic's memory tool represents a **distinctly different philosophy** from all other tools in this survey: rather than a managed memory service, it is a **client-side, file-based primitive** [10][6].

**Timeline:**
- **September 29, 2025:** Memory tool launched in public beta on Claude Developer Platform alongside Sonnet 4.5 release. Beta header: `context-management-2025-06-27` [6].
- **October 2025:** Memory enabled for Max/Pro Claude.ai consumer plan users.
- **March 2, 2026:** Memory extended to free-tier Claude.ai users; import tool launched to migrate memories from ChatGPT/Gemini [71].

**How it works (developer API):** The memory tool operates via a `/memory` file directory that persists between sessions. Agents call six memory commands as tool calls: `view`, `create`, `str_replace`, `insert`, `delete`, `rename`. Developers implement client-side handlers by subclassing `BetaAbstractMemoryTool` (Python) or `betaMemoryTool` (TypeScript). Developers control the storage backend — files can be stored locally, in a database, in cloud storage, or encrypted. There is no centralised Anthropic storage service for API-tier memory [10].

The consumer Claude.ai memory implementation is a *separate system* from the developer API memory tool. It automatically extracts and stores facts from conversations as Claude-managed summaries, viewable and editable by users in Settings → Memory.

**Internal evaluations (vendor claims):**
- 39% performance improvement on agentic search tasks when combining memory tool with context editing [10].
- 84% token reduction in a 100-turn web search evaluation [10].
- ~2,500 tokens of overhead from automatically injected system prompt per session [10].

**Memory type coverage:**

| Memory Type | Support |
|---|---|
| Episodic (file-based) | ✓ |
| Semantic (user-defined structure) | ✓ (free-form file content) |
| Procedural (instruction files) | ✓ |
| Temporal | ✗ (no native temporal modelling) |

**Claude ecosystem fit:** Most native option for Claude-based agents. The only memory mechanism with first-class platform support. Combined with CLAUDE.md for procedural memory and the file-based `/memory` system for episodic and semantic storage, this covers most baseline use cases. The primary gap is lack of built-in semantic retrieval.

**Limitations:** No vector search built in; agent-directed rather than automatic; no managed persistence (developers must operate their own backend); consumer vs. API split is a common source of confusion; beta status means API surface may change [10].

### 4.6 Sleep-Time Compute (Letta Pattern)

Sleep-time compute is an architectural **pattern**, not a standalone product [19]. It is enabled within Letta via the sleep-time agent configuration. The formal definition: given context c (without the query q), during sleep time S(c) → c′. At test time T(q, c′) → a. The re-represented context c′ is richer and more query-ready than raw context c.

The sleep-time process uses function calling. The model is given tools `rethink_memory` (iterative context rewriting, up to 10 calls) and `finish_rethinking`. During sleep, the model: anticipates likely queries, draws inferences, resolves contradictions in stored memories, abstracts patterns from specific experiences, and pre-computes associations [19][22].

> "This 'sleep-time compute' might involve identifying contradictions in stored memories, abstracting patterns from specific experiences, or pre-computing associations that will speed up future reasoning and retrieval." — Letta blog, December 2025 [22]

Bilt (loyalty platform) deployed millions of Letta agents with sleep-time memory: "We can modify a single memory block and alter the behavior of hundreds of thousands of agents. This is beneficial in any situation where you need precise control over the context of the agents" [24].

**Relevance for Jetix:** Sleep-time compute directly addresses the manual consolidation step in the voice-notes pipeline. A coding agent studying a codebase overnight, or a client relationship agent consolidating interaction history between sessions, would benefit substantially. Implementable today in Letta Cloud or in any custom agent framework.

### 4.7 Shorter Tools

**LangMem (LangChain, Apache 2.0):** LangChain's opinionated memory layer for LangGraph-based agents (stable SDK April 2026) [113]. Distinguishes semantic (facts), episodic (structured past interactions), and procedural (instructions stored as prompt updates) memory types. Background `ReflectionExecutor` processes conversation history asynchronously via `create_memory_store_manager`. First-class Claude integration: `create_memory_manager("anthropic:claude-3-5-sonnet-latest")` works out of the box. Benchmarks: ~8% below Mem0 on LoCoMo (Mem0 paper); LangMem p95 latency 60 seconds, not production-viable at this threshold [7]. LangGraph-native; teams not using LangGraph see less value.

**LlamaIndex Memory (Apache 2.0, updated May 2025):** Updated Memory component with short-term memory (SQL/SQLite, token-limited FIFO) plus pluggable long-term memory blocks: `StaticMemoryBlock`, `FactExtractionMemoryBlock`, `VectorMemoryBlock` (token overflow writes to a vector store). When short-term hits the token limit, it flushes to configured long-term blocks [114]. No published benchmarks; no graph memory; best suited for teams already in the LlamaIndex ecosystem.

**Redis for Agent Memory (SSPL v1 / proprietary):** Dual-purpose — short-term memory via Redis Lists and long-term memory via Redis JSON + Redis Query Engine (vector search). Redis 8 added built-in vector database capabilities. Benchmark claim: vector search latency from 2 seconds down to **10 milliseconds** [115]. Redis is infrastructure, not an opinionated memory API; teams must implement memory extraction, deduplication, and retrieval logic. Not a drop-in alternative to Mem0/Zep.

**Weaviate (BSD 3-Clause / Weaviate Cloud):** Vector database with hybrid search (semantic + BM25 + graph extensions) positioning as agent memory infrastructure [116]. 2025 additions: Embedding Service, HIPAA compliance. Large-dataset P95 latency 300–700ms. Serves as the vector store backend for LlamaIndex's VectorMemoryBlock, for Mem0's pluggable vector DB, and for custom RAG-based memory — infrastructure tier, not a full memory stack.

**MemoryOS (BAI Lab, EMNLP 2025 Oral, arXiv:2506.06326):** OS-inspired three-tier hierarchy with four modules (Storage, Updating, Retrieval, Generation). Benchmarks on LoCoMo (GPT-4o-mini): **+49.11% F1** and **+46.18% BLEU-1** improvement over baselines [28]. MemoryOS-MCP released June 2025 for integration with any MCP client. Academic project; no production managed service.

**A-MEM (Xu et al., NeurIPS 2025, arXiv:2502.12110):** Applies Zettelkasten method to LLM agent memory — each new memory generates a "note" with contextual description, keywords, tags, and dynamically evolving links to related memories. Token usage: ~1,200 tokens per memory operation (85–93% reduction vs. LoCoMo/MemGPT baselines). Outperforms MemGPT and MemoryBank on both LoCoMo and DialSim benchmarks [29]; lags Mem0 by ~25 points on LLM-Judge score [7]. Academic system; no production managed service.

### 4.8 Tooling Comparison Table

| Tool | Memory Types | Architecture | Open-source | Managed Tier | LoCoMo Score | LongMemEval Score | Claude Native | Self-host Option | Latency (retrieval) | Key Limitation |
|---|---|---|---|---|---|---|---|---|---|---|
| **Mem0** | Episodic, Semantic | Hybrid (Vector + optional Graph) | Apache 2.0 | Yes ($0–$249/mo) | 91.6 (own eval, 2026) | 49.0% (independent) | External (MCP, SDK) | Yes (full stack) | p50 0.15s / p95 1.44s | Graph paywalled at $249/mo; no temporal windows |
| **Mem0g** | Episodic, Semantic, Relational | Graph (Neo4j / Kuzu) | Apache 2.0 | Yes (Pro $249/mo) | ~2% above base | Not published | External | Yes | p50 0.48s / p95 2.59s | Part of Mem0 Pro; additional latency |
| **Letta** | Episodic, Semantic, Procedural | OS-tiered (Core/Archival/Recall) | Apache 2.0 | Yes ($20–$200/mo) | Below Mem0 (~25pts) | Not benchmarked | External (direct API) | Yes | Not published | Complexity; context overhead; runtime lock-in |
| **Zep / Graphiti** | Episodic, Semantic, Temporal | Temporal Knowledge Graph | Graphiti Apache 2.0; Zep CE deprecated | Yes ($0–$25/mo+) | Not published | 63.8% (independent) | Via MCP server | Graphiti only (3 systems) | ~300ms p95 (cloud) | CE deprecated; async ingestion delays |
| **Cognee** | Episodic, Semantic, Temporal (partial) | Poly-store (Graph + Vector + Relational) | Apache 2.0 | Early stage | Not published | Not published | External | Yes (local-first) | Not published | No benchmarks; early commercial |
| **Anthropic Memory Tool** | Episodic, Semantic, Procedural | File-based (client-side) | N/A (API beta) | Included in API | Not benchmarked | Not benchmarked | **Native (first-class)** | Developer-managed | Token call latency | No built-in semantic search; beta status |
| **LangMem** | Semantic, Episodic, Procedural | Pluggable (LangGraph BaseStore) | Apache 2.0 | Via LangGraph Platform | ~8% below Mem0 | Not published | Via LangChain SDK | Yes | Depends on store (p95 60s reported) | LangGraph-native; no graph memory |
| **LlamaIndex Memory** | Semantic, Episodic, Static | Vector blocks + SQL short-term | Apache 2.0 | Via LlamaCloud | Not published | Not published | Via LlamaIndex | Yes | Depends on store | No deduplication; no graph; framework-locked |
| **Redis** | Episodic, Semantic | Vector + Key-Value | SSPL | Redis Cloud | N/A | N/A | Via SDK | Yes | **10ms** (vector search) | Infrastructure only; no extraction logic |
| **Weaviate** | Semantic | Hybrid Vector (semantic + BM25) | BSD 3-Clause | Weaviate Cloud | N/A | N/A | Via SDK | Yes | 300–700ms (large) | Infrastructure only; not a complete memory system |
| **MemoryOS** | Episodic, Semantic | 3-tier OS hierarchy | Research (GitHub) | None | +49.11% F1 vs. baselines | Not published | Via MCP | Self-hosted only | Not published | Academic; no production SLAs |
| **A-MEM** | Episodic, Semantic | Linked notes (Zettelkasten) | GitHub (research) | None | Below Mem0 by ~25pts | Not published | External | Self-hosted only | ~1,200 tokens/op | Academic; no production managed service |
| **Sleep-time Compute** | Procedural, Semantic (meta-pattern) | Async pre-computation (Letta) | Apache 2.0 (Letta) | Via Letta | N/A (pattern) | N/A | Via Claude + Letta | Yes | N/A | Pattern, not standalone tool; requires Letta |

---

## Section 5 — Production Examples & Failure Modes

### 5.1 Named Production Deployments

**ChatGPT Memory (OpenAI, launched February 13, 2024)**

OpenAI announced memory for ChatGPT on February 13, 2024, with full rollout to Free, Plus, Team, and Enterprise tiers by September 2024 [66]. A significant expansion on April 10, 2025 enabled reference to *all* past conversations (not just explicitly saved facts) for Plus/Pro subscribers, with EU/UK/EEA exclusions due to GDPR [67]. Two mechanisms operate in parallel: (1) **Saved Memories ("Notepad" layer)** — structured text notes appended to the user-specific store and prepended to the system prompt at session start, with a budget of "a few thousand tokens"; (2) **Reference Chat History (RAG layer)** — implicit semantic search over full conversation history, organised into sections including "Model Set Context," "Notable Past Conversation Topic Highlights," and "Recent Conversation Content," capped at approximately 40 entries [68]. Memory is not available via API; consumer app only. EU/UK exclusion for Reference Chat History persists as of 2025 pending GDPR data-portability compliance [67].

**LongMemEval finding:** ChatGPT "tended to overwrite crucial information as the chat continues," indicating a recency-biased write policy [52].

**Claude Memory / Projects / CLAUDE.md / Memory Tool API (Anthropic, multiple releases 2024–2026)**

Anthropic launched Claude Projects in May 2024 with a persistent document store and per-project instructions. Consumer memory rolled out to Team and Enterprise (September 2025), Pro and Max (November 2025), and free-tier users (March 2, 2026). The consumer implementation uses a file-based architecture: memories are stored in Markdown files organised hierarchically, loaded into Claude's context window at session start — not a vector database RAG system [70]. The developer API memory tool (beta, August 2025) provides a file-system metaphor with six commands and entirely client-side storage [10].

**Disclosed metrics:** 39% performance improvement on agentic search tasks; 84% token reduction in a 100-turn web search evaluation; ~2,500 token system prompt overhead per session [10].

**Sierra (sierra.ai) — Agent Data Platform, November 5, 2025**

Sierra (Bret Taylor, Clay Bavor) reached a $10 billion valuation by November 2025 [72]. The Agent Data Platform (ADP) as part of Agent OS 2.0 unifies unstructured customer conversation history with structured CRM records, billing systems, and transaction logs, enabling agents to "greet customers by name, remember prior conversations and preferences, surface relevant insights, and take initiative on their behalf" [73].

**Disclosed metrics:**
- Rocket Mortgage: Sierra-powered agent processes a mortgage refinance in ~30 minutes vs. several hours across multiple days.
- Ramp: Sierra agents handle **90% of support inquiries** without human intervention [72].

**Decagon User Memory (launched March 2026)**

Decagon's two-tiered architecture: (1) conversational memory (unstructured history persisting across sessions) and (2) structured metadata (feature requests, sentiment, stated preferences). The platform provides full API accessibility, opt-in storage, expiration controls, redaction policies, and audit logs [113][114].

**Disclosed metrics:**
- Bilt: Reduced support headcount from hundreds to 65 using Decagon agents.
- ClassPass: Handles 2.5 million customer conversations, reducing cost per reservation by 95% [115].

**Devin (Cognition AI, cross-session memory disclosed March 2026)**

Devin implements session-persistent memory through a notes-based system. "Devin carries state between runs. It reads and writes its own notes across sessions, which means each run builds on the context of the one before it rather than starting from scratch" [116]. Enabling incremental compilation (weekly release-notes Devin knows where it left off) and state accumulation (feature-request monitoring Devin tracks already-processed Slack messages). The underlying mechanism appears to be flat file/note storage analogous to CLAUDE.md rather than a vector database [116].

**Replika (Luka, Inc.) — €5M GDPR Fine, May 2025**

Italy's Garante DPA fined Replika €5 million in May 2025 for GDPR violations: lack of valid legal basis for data processing (Article 6), deficient transparency disclosures (Articles 12–14), inadequate safeguards for sensitive behavioural/emotional data, and failure of age verification protecting minors [17][18]. The Garante opened a further investigation into training-data practices. The most significant regulatory enforcement action against an AI companion app's memory/data practices in Europe to date.

**Perplexity Memory (launched November 26, 2025)**

Perplexity launched memory as part of the Comet Assistant initiative [79]. Two layers: structured preferences auto-extracted from conversations (not manually addable, only deletable), and past questions/answers referenced when relevant to new queries. Memory is not available in the EEA at launch. Notably, memory is **context-portable** — travels with the user across all model choices (GPT-4o, Claude, Sonar) [79].

**Production systems summary table:**

| System | Memory Type | Architecture | Key Metric | GDPR Status | EU Deployment |
|---|---|---|---|---|---|
| ChatGPT Memory | Notepad + RAG history | Structured notes + chat-history semantic retrieval | >100M users (estimated) | EU/UK Reference History blocked | Limited |
| Claude Memory Tool | File-based | Client-side file I/O | 39% agentic improvement, 84% token reduction | ZDR eligible | Full |
| Sierra ADP | Unified structured + unstructured | Enterprise CRM + conversation history | 90% automation (Ramp) | Unverified DSAR compliance | Probably limited |
| Decagon User Memory | Episodic + structured metadata | Two-tier with audit logs | 95% cost reduction (ClassPass) | Full controls | Available |
| Devin | Notes-based | Flat file / CLAUDE.md analog | Incremental session continuity | Not disclosed | Available |
| Replika | Fact extraction | Limited context window approach | ~6M MAU (pre-acquisition) | **€5M GDPR fine** | Restricted |
| Perplexity Memory | Auto-extracted facts + search history | Two-layer (facts + RAG history) | Cross-model portability | Not EEA at launch | Limited |

### 5.2 Failure Modes with Mitigations

**Catastrophic Forgetting (Classical)**

Catastrophic forgetting in the classical sense applies only to systems that update model weights during deployment. For production LLM memory systems using external retrieval-augmented approaches (frozen weights), the analogous problem is **memory overwrite under write-conflict policies**: LongMemEval testing documented that ChatGPT "tended to overwrite crucial information as the chat continues," indicating a recency-weighted consolidation heuristic that discards older facts [52]. For systems that *do* update weights, April 2025 empirical work on continual fine-tuning found sharp performance degradation on prior tasks, with Phi-3.5-mini exhibiting the least forgetting among <10B parameter models evaluated [122].

*Mitigation:* Conflict-resolution LLM call on write (ADD/UPDATE/DELETE/NOOP rather than simple overwrite); temporal validity windows; explicit supersession events in the knowledge graph.

**Memory Poisoning**

AgentPoison (Chen et al., arXiv:2407.12784, July 2024) is the foundational paper. Key findings: **≥80% attack success rate** across three real-world agents; benign performance impact **≤1%** degradation; poison rate **<0.1%** of the knowledge base [38]. A single poisoned instance with a single-token trigger achieves ≥60% attack success rate. Does not require model retraining — attacks the retrieval mechanism. PoisonedRAG (Zou et al., USENIX Security 2025) extends this to knowledge database corruption [39]. Notably, a May 2025 benchmark covering 13 attack methods found **Claude demonstrates markedly stronger resistance to poisoning attacks** than other models, suggesting alignment training provides partial but incomplete defence [40].

*Mitigation:* Input sanitisation; read-only retrieval paths (no write-back from retrieved content); memory write audit logs; differential trust levels for different memory sources; adversarial trigger detection.

**Retrieval Drift**

As a memory store grows, the signal-to-noise ratio of vector similarity search degrades — semantically similar but factually unrelated content accumulates, compressing effective retrieval precision. MemoryAgentBench (Hu et al., July 2025) found that simple BM25 retrieval often outperforms complex embedding-based approaches as the knowledge base grows, because embedding similarity becomes less discriminative at scale [41]. In the Mem0 vs. Zep benchmark dispute, Zep's counter-analysis revealed Mem0's published Zep scores were deflated due to sequential search implementation compounding retrieval latency, suggesting retrieval architecture significantly determines quality at scale [43].

*Mitigation:* Re-ranking pipelines (cross-encoder re-ranking over initial ANN results); deduplication on write; temporal decay weights; graph-based retrieval (HippoRAG's Personalized PageRank) to maintain associative relevance at scale.

**False Memory Consolidation**

False memory consolidation occurs when a summarisation or consolidation pass introduces fabricated, distorted, or generalised content into the long-term memory store. The SSGM framework paper (arXiv:2603.11768, March 2026) formally models this as "semantic drift" where "knowledge stored by an agent gradually deviates from ground truth" through iterative lossy summarisation [44]. Palo Alto Networks Unit 42 (October 2025) demonstrated false memory consolidation via indirect prompt injection in AWS Bedrock Agents: content from a web page could manipulate session summarisation, causing malicious instructions to persist across sessions for up to 365 days [45].

*Mitigation:* Confidence scoring on extracted facts before write; verification passes re-checking extracted facts against source transcript; human-in-loop review queues for high-sensitivity memory writes; checksums of source content to detect post-write divergence.

**Context Rot**

"Context rot" refers to measurable degradation in LLM output quality as input context grows, even well below the model's maximum context limit. Chroma's 2025 study tested 18 frontier models (including GPT-4.1, Claude Opus 4, Gemini 2.5) and found context rot at every input length increment [42]. Three compounding mechanisms: (1) lost-in-the-middle effect — 30%+ accuracy drops for middle-positioned content; (2) attention dilution — quadratic attention means 100K tokens = 10 billion pairwise relationships; (3) distractor interference — semantically similar but irrelevant content causes degradation beyond length effects alone. For coding agents specifically, context rot is identified as the *primary* failure mode [42]. The precursor work is Liu et al., "Lost in the Middle" (TACL 2024, arXiv:2307.03172) [47].

*Mitigation:* Context compression/pruning (DyCP achieved 81% context reduction with +8.1 GPT-4-Score improvement on LoCoMo [48]); sub-agent delegation with fresh-context workers; sliding window summarisation; memory externalisation before context fill; Anthropic's multi-agent research system outperformed a single long-context agent by 90.2% on research tasks by using short-context subagents [42].

**Temporal Inconsistency (Stale Memory Overwriting Fresh Knowledge)**

Temporal inconsistency occurs when a memory store contains outdated facts that contradict recent user-provided information, and the retrieval system returns stale entries over current ones because they have higher retrieval scores from historical reinforcement. LongMemEval introduced *Knowledge Update* as a specific evaluation axis, and on LoCoMo, temporal question-answering was the hardest category: GPT-3.5/4-Turbo scored 20–30 F1 vs. human performance of 92.6 [48].

*Mitigation:* Temporal weighting in retrieval (recency bonus); explicit timestamps with query-time temporal filtering (+6.8–11.3% recall gain in LongMemEval temporal tasks [52]); knowledge-update conflict resolution with explicit supersession events; TTL (time-to-live) on perishable facts.

**Privacy / GDPR Failure Modes**

The EDPB launched its 2025 Coordinated Enforcement Framework (CEF) on March 5, 2025, with the right to erasure (GDPR Article 17) as its priority [49]. For high-risk AI systems, EU AI Act Articles 12 and 72 require audit trail retention for up to 10 years, while GDPR Article 17 requires erasure on request — irreconcilable demands unless memory is architecturally tiered into session context (ephemeral), extracted facts (GDPR-deletable), decision audit records (pseudonymised), and model influence records [50].

*Mitigation:* Privacy-by-design memory tiers; ZDR arrangements for sensitive memory pipelines (Claude Memory Tool supports this); explicit consent flows before memory writes; automated TTL expiry for personal facts; DPIA for memory-enabled AI systems.

---

## Section 6 — Evaluation & Benchmarks

### 6.1 LongMemEval (Wu et al., ICLR 2025)

**Paper:** arXiv:2410.10813. Authors: Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu (UCLA, Tencent AI Lab Seattle, UC San Diego) [52][52].

**What it tests:** 500 manually curated questions testing five long-term memory abilities: Information Extraction, Multi-Session Reasoning, Knowledge Updates, Temporal Reasoning, and Abstention (correctly refusing to answer when information was never mentioned). Two settings: LongMemEval-S (~115K tokens, 30–40 sessions) and LongMemEval-M (~1.5M tokens, 500 sessions).

**Scores:**
- Commercial systems on a simplified subset: GPT-4o drops from 91.8% accuracy with full offline reading to **57.7% in online memory settings** — a 34-point gap [52].
- Zep (Graphiti): **63.8%** overall (GPT-4o) on LongMemEval-S, with +17.3pp on temporal reasoning and +13.6pp on multi-session QA [43].
- TiMem: **76.88%** (GPT-4o-mini), state-of-the-art as of January 2026, +9.49pp on knowledge update [53].
- EverMemOS: **83.0%** overall, +15.5pp on knowledge update [53].
- Supermemory: **85.4%** overall (self-reported) [53].
- Mem0: **49.0%** (independent, vectorize.io) [3].

**Critical verdict:** LongMemEval is the best-designed current benchmark for end-to-end chat-assistant memory because it tests human-AI dialogues (not human-human), explicitly targets knowledge update and abstention, and is freely scalable in session length. However, it is a *static offline evaluation* — questions are pre-curated against synthetic histories. It does not capture continual real-time memory accumulation dynamics, write-conflict resolution under concurrent users, or adversarial injection scenarios. Its abstention category tests "unknown information" cases but not adversarially crafted false-premise questions at scale.

### 6.2 LoCoMo (Maharana et al., ACL 2024)

**Paper:** arXiv:2402.17753. Authors: Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, Yuwei Fang (Snap Research, UNC Chapel Hill) [54][55].

**What it tests:** Three tasks over very long-term conversations: QA (single-hop, multi-hop, temporal, adversarial), Event Summarisation, and Multimodal Dialogue Generation. 50 dialogues, each averaging 300–600 turns, 9K–26K input tokens, spanning 19–35 sessions over 6–12 months of imagined time.

**Human vs. model gap:** Human QA overall F1 ≈ 88 vs. best LLM baselines ≈ 37–42 (GPT-3.5/4-Turbo). Temporal questions: models 20–30 F1 vs. human 92.6. Adversarial QA: can drop to ≈2 F1 [55].

**Leading system scores:**
- Mem0: **66.9%** LLM-as-Judge accuracy; full-context baseline: 72.9% with 9.87s median latency [56].
- OpenAI Memory: **52.9%** LLM-as-Judge [56].
- LangMem: 58.1%, but p95 latency 60 seconds — not production-viable [56].
- Zep (Graphiti, self-reported): **75.14%** (disputed by Mem0 at 65.99%) — benchmark methodology dispute ongoing [43].

**Critical verdict:** LoCoMo is widely cited but has severe limitations. (1) Dataset size: 50 dialogues is extremely small; minor implementation choices can shift reported scores by 10+ percentage points [43]. (2) Synthetic construction: dialogues are LLM-generated and human-edited, with vocabulary and topic distributions that may not reflect real conversations. (3) Multimodal dependency: image-grounded tasks require multimodal models, limiting comparability. (4) No knowledge-update task: LoCoMo tests recall of stable history but not supersession of contradicted facts. (5) Benchmark contamination risk: the small dataset size makes leaderboard gaming feasible. The Mem0/Zep/Supermemory benchmark dispute is unresolved and illustrates the fragility of single-benchmark evaluation. Zep's team publicly states a preference for LongMemEval over LoCoMo for these reasons [43].

### 6.3 MemoryBank / MemoryBench

**MemoryBank (Zhong et al., 2024):** Multi-day chat history from 15 users with 194 human-written probing questions. Incorporates an Ebbinghaus Forgetting Curve mechanism — memories decay exponentially but are reinforced on access [57]. Small scale (194 questions) limits statistical power; serves as a personalisation-focused benchmark for single-user dialogue continuity.

**MemoryBench (Ai et al., arXiv:2510.17281, October 2025):** Broader benchmark covering 11 public datasets (20,000 cases) spanning reading comprehension, writing, coding, legal judgment, and summarisation [58]. Key innovation: a **User Feedback Simulation Framework** to test *procedural memory* — the ability to improve performance from accumulated user feedback. **Critical finding:** Memory system generalisation is fragile — specialised architectures (A-Mem, Mem0, MemoryOS) are robustly superior only on reading comprehension/long-context retrieval; on other domains, well-tuned naïve RAG is competitive or superior [58]. This significantly undercuts vendor claims of general-purpose memory superiority.

### 6.4 MemoryAgentBench (Hu et al., arXiv:2507.05257, July 2025)

Tests four competencies: Accurate Retrieval (AR), Test-Time Learning (TTL), Long-Range Understanding (LRU), and Conflict Resolution (CR-SH, CR-MH) [41].

| Agent Class | AR (%) | TTL (%) | LRU (%) | CR-SH (%) |
|---|---|---|---|---|
| Long-Context | 43.5 | 82.0 | 28.9 | 45.0 |
| Simple RAG (BM25) | 61.0 | 75.4 | 20.9 | 56.0 |
| Embedding RAG | 65.0 | 69.4 | 20.7 | 55.0 |
| Agentic (MemGPT) | 30.6 | 67.6 | 2.5 | 28.0 |

BM25 outperforms embedding RAG on conflict resolution; MemGPT performs worst overall, highlighting that paging-based architectures struggle with structured memory tasks [41].

**Critical verdict:** MemoryAgentBench reveals that simple retrieval often outperforms complex architectures on specific tasks — a sobering finding for expensive memory systems. MemGPT's 30.6% AR is particularly striking given its architectural focus on memory management.

### 6.5 Other Relevant Benchmarks

**MINT (arXiv:2309.10691):** Tests multi-turn interaction with tools and language feedback. Key finding: better single-turn performance does **not** guarantee better multi-turn performance; RLHF and instruction fine-tuning generally *hurt* multi-turn capabilities in tested models [59]. Relevant for the session-layer memory management underlying long-horizon agentic tasks.

**InfiniteBench (Zhang et al., arXiv:2402.13718, February 2024):** First benchmark with average data length >100K tokens. Results show existing LLMs "still require significant advancements to process 100K+ contexts effectively" [62]. Tests raw long-context processing, not cross-session memory with write/retrieve cycles.

**DialSim (Kim et al., 2024):** TV show character roles with multi-party dialogues averaging 350K tokens. Unique: **time-constrained evaluation** with 1s/3s/5s response deadlines, testing whether memory retrieval is feasible for real-time conversation [63].

### 6.6 What Current Benchmarks Actually Measure

The fundamental question for Jetix due-diligence: do any current benchmarks capture **genuine continual learning** (the system becomes demonstrably better at a task through accumulated experience) versus **one-shot retrieval** (the system simply stores and retrieves pre-supplied facts)?

LongMemEval, LoCoMo, MemoryAgentBench, DialSim, and InfiniteBench all primarily measure the latter — the system's ability to recall information injected at the start of the evaluation. A perfectly accurate human transcription service would score near-ceiling on these benchmarks without any learning. **MemoryBench (2025) is the exception**, introducing procedural memory evaluation. But current results show memory systems provide inconsistent procedural improvement: benefits are domain-specific and often non-generalisable [58].

True continual learning evaluation would require: multi-phase evaluation measuring performance delta attributable to memory accumulation; negative transfer tests (does memory on Task A degrade Task B?); zero-shot generalisation from one user's feedback to another's; and temporal stability testing over 6–12 months of store growth.

**Verdict:** Procurement decisions based solely on LoCoMo scores are evaluating an incomplete and potentially misleading metric. LongMemEval provides the best-designed evaluation of retrieval quality with the most realistic task distribution. MemoryBench is the only benchmark approximating true continual learning assessment.

---

## Section 7 — Solo-Founder Applicability & Jetix Fit

### 7.1 Tiered Stacks for a Single Operator

Running 11 agents without a platform team is a resource-allocation problem masquerading as an architecture problem. The real constraints are: zero dedicated ops time, all debugging must be transparent and readable without tooling, migration cost is paid entirely by the founder, and vendor failure cannot be catastrophic.

**Tier 0 — File-Based (Current Jetix Baseline)**

Plain-text markdown files injected as context at session start. Anthropic's Claude Code documentation defines four scopes of CLAUDE.md files: managed-policy, project-level, user-level, and local, loaded by walking the directory tree upward. Claude Code's Auto Memory feature (available since v2.1.59) extends this: the model writes its own notes to `~/.claude/projects/<project>/memory/`, with MEMORY.md acting as an index loaded at every session start [1].

Andrej Karpathy formalised this philosophy in April 2026 with his "LLM Wiki" pattern: "Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files… The knowledge is compiled once and then kept current, not re-derived on every query." He describes the CLAUDE.md as "the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot" [4].

Simon Willison's reverse-engineering of Claude's native memory confirmed it uses two tools — `conversation_search` and `recent_chats` — and emphasised transparency: "The good news here is transparency — Claude's memory feature is implemented as visible tool calls, which means you can see exactly when and how it is accessing previous context" [107].

**Verdict for 1 operator:** Optimal for the current 11-agent setup. Zero infra cost, full debuggability, version-controllable with git, no external dependency. The ceiling is the context window, not the pattern.

**Tier 1 — Local Vector DB**

Options: `sqlite-vec` (C, zero dependencies, Mozilla-sponsored, Apache 2.0) [96]; `chromadb` local (Python-native, in-process, Apache 2.0); `qdrant-embedded` (Rust, production-grade HNSW, Apache 2.0); `pgvector` (PostgreSQL extension, MIT) [97].

All four are free to self-host. What it adds over Tier 0: semantic retrieval across all 11 agents' wiki entities without loading everything into context. A query like "find all client entities related to AI governance compliance" becomes a 5ms vector search rather than a full context dump. The practical gain is scale: when the wiki grows beyond ~200 entities, semantic search becomes necessary.

**Verdict for 1 operator:** `sqlite-vec` is the natural first step — it inherits SQLite's battle-tested reliability, has zero server infrastructure, and can coexist with the existing wiki directory as an index layer.

**Tier 2 — Managed SaaS**

- **Mem0 Cloud:** Hobby (free, 10K add requests/month); Starter ($19/mo, 50K adds); Pro ($249/mo, graph memory, SOC 2/HIPAA); Enterprise (custom) [99].
- **Letta Cloud:** Pro ($20/mo, 20 stateful agents); Max Lite ($100/mo, 50 agents); API Plan ($20/mo base + $0.10/active agent/mo) [102].
- **Zep Cloud:** Credit-based; Flex $25/mo (full feature access, SOC 2/HIPAA) [83].

**Verdict for 1 operator:** At Jetix's scale, the Mem0 Starter tier at $19/mo is the cheapest way to add vector retrieval without running Docker. Risk: 50K adds/month across 11 agents = ~150 adds/agent/day, barely under the limit at heavy usage. The Pro tier at $249/mo is disproportionate for a solo operation unless graph features are genuinely required.

**Tier 3 — Native Anthropic Memory Tool + Claude Projects**

As of March 2026, Claude's memory feature is available on all plans. Claude Projects provide isolated memory namespaces: "if you use projects, Claude creates a separate memory for each project" [107]. This is directly relevant to Jetix: each of the 6 departments could be a Claude Project, with per-project memory summaries maintained automatically. Zero cost, zero infrastructure.

**Limitations:** Memory is personal, not shared (no team-level shared context); compressed summary, not structured records; memories live on Anthropic's servers and do not travel to other tools [106].

**Tier 4 — Knowledge Graph Tools**

Cognee (Apache 2.0, self-hosted): ECL pipeline ingests 38+ source types, extracts entities and relationships via LLMs, maintains a queryable knowledge graph. Integrates with Claude Agent SDK via MCP, LangGraph, Neo4j, and Amazon Neptune [17]. The Obsidian-Cognee integration (100% local, LM Studio + Qwen 3 on Apple Silicon) is a documented use case for personal knowledge management [18].

Microsoft GraphRAG (MIT): Extracts rich knowledge graph from text documents using LLMs, applies hierarchical community detection. LazyGraphRAG (June 2025) reduces indexing cost to ~0.1% of full GraphRAG [104].

**Verdict for 1 operator:** Tier 4 is the highest-capability, highest-maintenance option. For Jetix's `edges.jsonl` structure (which already encodes relationships), Cognee's ECL pipeline is the most natural upgrade path — it formalises what `edges.jsonl` does manually. Defer until `edges.jsonl` becomes impossible to maintain manually (typically at 500+ edges with multiple entity type updates per week).

**Decision framework:**

| Tier | Monthly Cost | Maintenance Burden | Capability Ceiling | Time to First Value |
|------|-------------|-------------------|-------------------|-------------------|
| 0 — File-based | $0 | Lowest (git) | Context window | Immediate |
| 1 — Local vector | $0 (local) | Low–Medium | Semantic scale | 1–2 days |
| 2 — Managed SaaS | $0–$249 | Low (managed) | Vector + graph | Hours |
| 3 — Native Anthropic | $0 (included) | Zero | Profile + history | Immediate |
| 4 — KG tools | $0 (OSS) | High | Full ontology | Days–weeks |

### 7.2 Jetix Baseline Classification

The Jetix memory architecture — `wiki/` markdown with 9 entity types, frontmatter-indexed, `edges.jsonl` graph, per-agent `strategies.md` + `scratchpad.md`, `mailboxes.jsonl` inter-agent messaging, and voice-notes ingest→extract→filter→review pipeline — maps most precisely to three academic patterns:

**1. System Prompt Learning (Karpathy, 2025–2026):** Karpathy's "third paradigm" for LLM learning involves building explicit problem-solving strategies in the system prompt from accumulated experience. Jetix's `strategies.md` files are direct instantiations: human-curated, per-agent strategy libraries that encode successful patterns [21].

**2. Voyager-style skill library:** Voyager's ever-growing skill library of executable code stored and retrieved for lifelong learning provides the conceptual model [14]. Jetix's `wiki/` entities + `strategies.md` are a markdown analogue: composable knowledge artefacts indexed by frontmatter, retrieved by the operator rather than by automated semantic search.

**3. External semantic + procedural memory with human-in-loop consolidation:** The voice-notes pipeline (ingest→extract→filter→review) is precisely the MemGPT/Letta human-in-loop consolidation pattern, applied manually. The `mailboxes.jsonl` inter-agent messaging system adds episodic communication memory not common in academic implementations.

**In Baddeley's cognitive memory taxonomy:** the wiki provides semantic memory (facts, entities, relationships); `strategies.md` provides procedural memory (how to act); `scratchpad.md` provides working memory; `mailboxes.jsonl` provides episodic memory (event sequences); `edges.jsonl` provides associative memory (entity relationships).

### 7.3 Gap Analysis

| Gap | What's Missing | SOTA Analogue |
|-----|---------------|-------------|
| No vector retrieval | All wiki access is context-load or manual lookup | sqlite-vec / chromadb semantic search |
| No temporal KG | `edges.jsonl` is static; edges are not timestamped or weighted | Graphiti (Zep), Cognee memify layer |
| No automatic consolidation | Voice-notes pipeline requires human filter+review step | Letta sleep-time agents, Mem0 auto-extraction |
| No episodic event store | `mailboxes.jsonl` stores messages but is not a queryable event store | Letta recall memory, LangGraph checkpointing |
| No cross-agent query API | Agents cannot query each other's strategies/wiki programmatically | Letta multi-agent messaging, CrewAI shared memory |
| No eval harness | No mechanism to measure if memory improves task performance | LangSmith evals, custom benchmark harness |

### 7.4 What Each Candidate Tool Would Add and Displace

**Mem0 (Apache 2.0 / Cloud):**
- *Adds:* Vector + graph hybrid memory with automatic LLM-driven extraction from agent interactions. Every agent conversation can automatically surface memories relevant to the current task.
- *Displaces:* Nothing structurally — Mem0 acts as an indexing layer over existing interactions. Does not replace `wiki/` or `strategies.md`; augments them with retrieval.
- *Integration point:* Use Mem0 as the retrieval engine for `wiki/` entities while keeping markdown files as the source of truth.
- *Risk:* LLM-driven extraction can mis-classify or over-generalise facts. Reported ~85% accuracy on LongMemEval vs. 100% for verbatim storage approaches [125].

**Letta (Apache 2.0 / Cloud):**
- *Adds:* Self-editing memory agent — a sleep-time agent runs asynchronously to reorganise core memory blocks, consolidate insights, and clean context. This directly replaces the manual step in Jetix's voice-notes pipeline.
- *Displaces:* The human-in-loop consolidation step for `scratchpad.md` and `strategies.md`. Letta's sleep-time agent can automatically promote scratchpad observations to permanent strategy entries.
- *Integration point:* Replace the voice-notes filter+review pipeline with a Letta sleep-time agent configured to process daily summaries and propose wiki updates for human approval.

**Anthropic Memory Tool (Native, Beta):**
- *Adds:* Zero-config memory that persists user preferences and facts across Claude sessions. Per-project memory for Claude.ai.
- *Displaces:* The MEMORY.md component of the Claude Code auto-memory system partially overlaps with `scratchpad.md`. Native memory is simplest for the 6 Claude.ai Projects representing Jetix departments.
- *Limitation:* Memory is a compressed summary, not structured records. Cannot be queried programmatically. No export to other tools [106].

**Cognee (Apache 2.0, self-hosted):**
- *Adds:* Formal ontology + knowledge graph over `edges.jsonl`. Cognee's ECL pipeline can ingest all 9 entity types from `wiki/`, extract their relationships via LLMs, and build a queryable graph where edges are weighted and timestamped [17].
- *Displaces:* `edges.jsonl` as a hand-maintained flat file. Cognee's `memify` layer (feedback-driven edge weight updates) adds continuous self-improvement that static JSONL cannot provide.
- *Integration pattern:* Keep `wiki/` as Cognee's `raw/` source; let Cognee maintain the derived graph. Run ECL pipeline on wiki changes via a git hook.

---

## Section 8 — Integration Patterns & Future

### 8.1 Production Integration Patterns

**Pattern 1: RAG + Memory Hybrid**

The 2026 practitioner consensus is that "vanilla RAG fails for agentic use cases" and production agents use both: RAG for broad knowledge retrieval, memory for personalised session continuity [119]. Harrison Chase (LangChain co-founder and CEO) states: "I would argue that memory is a type of context. A significant part of an AI engineer's role involves ensuring the model receives the appropriate context" [24].

In LangGraph, this is implemented as a `checkpointer` (SQLite/PostgreSQL for conversation history) plus `BaseStore` (cross-session semantic memory). The standard production pattern: `PostgresSaver` for checkpointing, `PostgresStore` for long-term memory, combined with a vector index for RAG [120]. Mem0 + static RAG — Mem0 handles user-level and agent-level memory (facts, preferences, past decisions); a separate vector store handles document-level RAG (product docs, wikis, reference material). These complement rather than replace each other: memory is *mutable* (facts about users change) while RAG sources are *append-only* (documents don't rewrite themselves).

**Pattern 2: Memory + KG + Skills (Triple-Layered)**

Three canonical implementations:
- *Generative Agents:* memory stream + reflection + planning = emergent social behaviour [11].
- *Voyager:* skill library (procedural memory) + automatic curriculum (planning) + iterative prompting (reflection). Skills are "temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting" [14].
- *Letta / MemGPT 2.0:* `core_memory` (in-context facts, ~2K tokens) + `archival_memory` (external database) + `recall_memory` (conversation history). Sleep-time agents rewrite `core_memory` asynchronously while primary agents handle user interactions [22].

**Pattern 3: Context Engineering as the Unifying Pattern**

Anthropic's engineering blog defines context engineering as "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference" [6]. Three techniques for long-horizon tasks: (1) **Compaction** — summarise and reinitialise; (2) **Structured note-taking** — NOTES.md / scratchpad; (3) **Sub-agent architectures** — specialised agents with clean context windows that return 1,000–2,000 token summaries to the orchestrator.

Jetix's architecture already implements all three: voice-notes pipeline (compaction), `scratchpad.md` (structured note-taking), and 11 specialised agents (sub-agent architecture). The gap is *automated execution* of the compaction and note-taking steps.

**Pattern 4: Anthropic Agent Skills Standard**

The Anthropic Agent Skills standard (open standard, Apache-licensed, December 2025) uses SKILL.md files with YAML frontmatter and progressive disclosure [30]. At session start, only skill metadata (name, description) is loaded into the system prompt; the full skill file is loaded only when triggered. This directly maps to Jetix's `strategies.md` pattern — strategies are skills. Formalising Jetix's existing files as SKILL.md provides progressive disclosure and cross-platform portability with zero architectural change.

### 8.2 Best-in-Class Reference Architecture 2026

**The Letta + Git-Backed Memory Architecture (Context Repositories)**

Letta's February 2026 "Context Repositories" release represents the clearest evidence-backed reference architecture for production stateful agents. Memory is projected into a git repository as plain files, manipulated by the agent via standard computer use tools (bash, file I/O). Sleep-time agents run during idle periods to reorganise, consolidate, and improve the memory repository. Skills are composable SKILL.md files. Subagents handle specialised tasks with clean context windows. The model is agnostic; primary and sleep-time agents can use different providers [26].

Three pieces of published empirical evidence support this as best-in-class:

1. **Benchmark performance.** Sleep-time compute paper (April 2025) demonstrated Pareto improvements on math benchmarks: sleep-time agents shift computation from high-latency user interactions to idle periods "without sacrificing performance quality" [19].
2. **Production deployment at scale.** Bilt deployed millions of Letta agents with sleep-time memory: "We can modify a single memory block and alter the behavior of hundreds of thousands of agents" [24].
3. **Portability and lock-in resistance.** Git-backed memory means memory lives in plain files, readable by any tool, version-controlled, and portable across model providers.

This architecture is a formalisation of what Jetix already builds manually. The wiki is already a git-tracked collection of markdown files. `edges.jsonl` is already a graph. `strategies.md` files are already skills. Adding Letta's sleep-time agent would provide: automatic memory consolidation, semantic retrieval over the git-backed store, and multi-model orchestration — while preserving full transparency and portability.

Boris Cherny (creator of Claude Code) shared his personal workflow in January 2026, described as "surprisingly vanilla" — no exotic customisation, just "multiple parallel sessions, shared team memory in git, plan mode for everything non-trivial, and verification infrastructure that closes the feedback loop" [34]. The platform team at Anthropic itself uses file-based memory (git) as the primary persistence layer.

### 8.3 Future Directions 2026–2027

**Test-time training (TTT) / memory-weight interpolation:** Research at ICLR 2026 introduces In-Place TTT: "Can we turn part of an LLM's weights into long-term memory that continuously absorbs new knowledge?" [111]. TTT-E2E (NVIDIA, January 2026) shows compressing context into weights at inference time scales better than full-attention transformers at 128K+ context length [112]. This points toward a future where memory is not just retrieval but weight-level adaptation — blurring the boundary between memory and fine-tuning.

**Agents outliving model versions:** Charles Packer frames the next phase as "agents with lifespans exceeding underlying models via persistent, learning memory systems" [26]. The practical implication: in 2026–2027, agents should port their learned memory to newer models as those are released. On selective forgetting: "If a user states, 'that project we were working on, erase it from your memory,' then the agent should be capable of retroactively modifying every single memory" [24]. This is the first published statement about *selective forgetting* as a first-class memory operation — architecturally non-trivial for systems using database embeddings rather than editable files.

**Multi-agent shared memory:** Taranjeet Singh (Mem0 co-founder and CEO) frames the company's product as a "memory passport" — a portable memory layer that travels with users across tools, devices, and agents. "One of the primary reasons that agents are not reliable is they have this amnesia problem wherein they forget what was the feedback given in the last run… The memory is automatically enabling agents to improve over time" [109]. In 2026–2027, Singh sees multi-agent shared memory (where one agent's learned context propagates to peer agents) as the primary scaling direction.

**Agentic self-improvement:** The Anthropic Agent Skills standard explicitly anticipates "agents creating, editing, and evaluating skills autonomously" [30]. Combined with Letta's sleep-time agents, the trajectory is clear: agents that not only use skill libraries but maintain and improve them from experience — online continual learning at the level of behavioural policies rather than weights.

**Longer effective context:** Alex Albert (Anthropic) noted that with Claude Opus 4, "30 minutes to an hour of coherent performance, while Opus 4 works continuously for hours" for agentic tasks [35]. The 1M-token context window (available at standard pricing since March 2026) partially defers the memory problem but does not eliminate it — n² attention costs still apply, and context rot remains real at large context sizes [42].

Simon Willison's 2026 predictions: "in 2026 the quality of LLM-generated code will become impossible to deny" [110], suggesting the primary unsolved problem shifts from capability to continuity — i.e., memory. His December 2025 year-in-review: "reasoning models with access to tools can plan out multi-step tasks, execute on them and continue to reason about the results such that they can update their plans to better achieve the desired goal" — framing memory as the persistence layer that converts reactive capability into sustained long-horizon competence [37].

**LazyGraphRAG and cost-aware graph construction:** The GraphRAG team (Darren Edge, Jonathan Larson, Ha Trinh, Microsoft Research) released LazyGraphRAG in June 2025, reducing indexing cost to ~0.1% of full GraphRAG by deferring LLM summarisation to query time [104]. This makes GraphRAG practical for smaller-scale deployments like Jetix that previously could not afford upfront indexing cost.

---

## Specific Production Examples

Named systems with URLs and descriptors:

- **Mem0** (mem0.ai) — Most widely deployed standalone memory layer; hybrid vector + graph extraction; 48K GitHub stars; $24M Series A; 26% improvement over OpenAI memory on LoCoMo; 91% latency reduction vs. full-context [7].
- **Letta (formerly MemGPT)** (letta.com) — OS-inspired tiered memory with sleep-time compute; three-tier hierarchy (core/archival/recall); Apache 2.0; 93.4% DMR accuracy; native multi-agent memory sharing [5][19].
- **Zep / Graphiti** (getzep.com / github.com/getzep/graphiti) — Temporal knowledge graph with bitemporal modelling; 63.8% LongMemEval (independent); Community Edition deprecated April 2025; Graphiti MCP Server v1.0 November 2025 [81][32].
- **Cognee** (cognee.ai) — Ontology-driven ECL pipeline with poly-store architecture; $7.5M seed February 2026; integrates with 38+ source types and 17+ LLM providers; self-hostable Apache 2.0 [15].
- **Anthropic Memory Tool** (platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — File-based memory primitive, client-side; six memory commands; first-class Claude SDK integration; beta September 29, 2025; 39% agentic improvement (vendor claim); ZDR eligible [10].
- **ChatGPT Memory** (openai.com/index/memory-and-new-controls-for-chatgpt) — Consumer memory launched February 13, 2024; full rollout September 2024; Notepad + RAG history layers; EU/UK exclusion for Reference Chat History layer pending GDPR compliance; not available via API [66].
- **Pi (Inflection AI)** — Emotionally-focused conversational AI with persistent memory; ~1M DAU, 6M MAU at peak; post-acqui-hire by Microsoft (March 2024), resource-constrained and no technical updates since Q3 2024 [136][135].
- **Character.AI** (character.ai) — Pinned Memories (5 messages per chat, March 2024); Memory Box (2025); per-character and per-chat isolation; no cross-character memory consolidation [138].
- **Sierra / Agent OS 2.0** (sierra.ai) — $10B valuation (November 2025); Agent Data Platform unifying unstructured conversation history with structured CRM data; 90% inquiry automation at Ramp; Rocket Mortgage refinance in ~30 minutes [72][73].
- **Decagon User Memory** (decagon.ai) — Two-tier (conversational memory + structured metadata); launched March 2026; full API access, expiration controls, audit logs; 95% cost reduction at ClassPass; 2.5M customer conversations [113][114].
- **Devin (Cognition AI)** (cognition.ai) — Notes-based cross-session memory (disclosed March 2026); reads/writes its own notes across runs; hierarchical Manage Devins architecture for context isolation [116].
- **Perplexity Memory** (perplexity.ai/hub/blog/introducing-ai-assistants-with-memory) — Launched November 26, 2025; auto-extracted facts + search history; cross-model portable; not available in EEA at launch [79].

---

## Critical Assessment

### Pros of Each Major Approach (Cited)

**File-based semantic memory (wiki/ + CLAUDE.md pattern):**
- Maximum transparency: every memory is a readable file, debuggable without tooling [95].
- Zero infrastructure cost and vendor dependency; version-controllable with git [1].
- Directly endorsed by Anthropic's own engineers (Boris Cherny) and Andrej Karpathy [4][34].
- Full portability: files are readable by any LLM or operator [26].
- Procedural and semantic memory coexist naturally in the same structure.

**Managed vector memory (Mem0):**
- Production-ready with 48K GitHub stars and $24M institutional backing [99][102].
- 26% improvement over OpenAI memory on LoCoMo; 91% latency reduction vs. full-context [7].
- Automatic extraction and conflict resolution at write time eliminates manual curation.
- Apache 2.0 open-source ensures self-hosting option; MCP server enables Claude Desktop integration.

**Temporal knowledge graph (Zep/Graphiti):**
- Bitemporal modelling is the only production-ready architecture for tracking fact evolution [81].
- 63.8% LongMemEval (independent) vs. 49.0% for Mem0 — 15-point advantage on temporal tasks [3].
- All features available at $25/mo Flex tier; no capability paywalling unlike Mem0.
- Full non-lossy episode preservation alongside derived entity and community subgraphs.

**Sleep-time compute (Letta):**
- Pareto improvement — 5× compute reduction for equivalent accuracy [19].
- Proactively addresses context rot by consolidating memory during idle periods rather than waiting for overflow.
- Native multi-agent memory sharing via shared memory blocks [22].
- Published evidence from production deployment (Bilt, millions of agents) [24].

**Anthropic Memory Tool:**
- Native Claude platform integration — only memory mechanism with first-class SDK support [10].
- Zero Data Retention (ZDR) eligible — critical for GDPR compliance as a Berlin-based EU consultancy [10].
- Fully client-side storage: developer controls the backend, enabling any storage architecture.
- Consumer memory (claude.ai) is well-designed with clear user controls [71].

### Cons + Failure Modes (Cited)

**File-based semantic memory:**
- Context-window saturation past ~20–30K tokens; agents forget cross-file connections.
- No semantic retrieval — all wiki access is context-load or manual lookup.
- Manual consolidation is the sole consistency mechanism; human-in-loop is a bottleneck.

**Mem0:**
- Graph features paywalled at $249/mo — 13× jump from Starter tier [99].
- No temporal validity windows; cannot answer "what was true on date X?" [3].
- LLM dependency at write time adds per-operation cost and latency (~2 LLM calls per write).
- Benchmark self-promotion: Mem0 paper uses Mem0's own LLM judge; independent scores are significantly lower [3][7].
- Independent LongMemEval score (49.0%) vs. self-reported (93.4%) raises reproducibility concerns.

**Zep:**
- Zep Community Edition deprecated April 2025; no full self-hosting option for the managed platform [32].
- Three-system provisioning (Graphiti + graph DB + optional embedding service) for self-hosted deployment.
- Async graph construction means immediate retrieval after ingestion may fail [7].
- Less ecosystem than Mem0 (~24K vs. ~48K GitHub stars) [81].

**Letta:**
- Context window overhead from core memory blocks on every call.
- Lock-in to Letta runtime schema; migration requires data export and transformation.
- No published independent LongMemEval scores; performs worse than Mem0 on LoCoMo [7].
- Complexity disproportionate for basic personalisation use cases.

**Anthropic Memory Tool:**
- No vector search built in — semantic retrieval requires building on top [10].
- Agent-directed, not automatic — unreliable with less capable models or inadequate prompting.
- Consumer claude.ai memory and developer API memory tool are separate systems (common source of confusion).
- Beta status (`context-management-2025-06-27`) means API surface may change [10].

### When to Use vs. Avoid — Decision Rules for Jetix (11-Agent Claude Code System)

**Use file-based (Tier 0):**
- Current scale (11 agents, single operator, <200 wiki entities). Always as the source of truth.
- When transparency and debuggability are paramount — operator must be able to diagnose failures without tooling.
- When git is already the version control system (zero additional infrastructure).
- *Avoid* when: wiki entities exceed ~200 and semantic search across them becomes daily friction; when voice-notes consolidation backlog exceeds 1–2 hours per day.

**Use Anthropic Memory Tool (Tier 3):**
- Immediately, for all 6 Claude Projects (zero cost, zero infrastructure).
- When GDPR compliance requires ZDR-eligible storage for any memory containing personal data.
- When the team's model lock-in to Claude is acceptable — this only works with Claude.
- *Avoid* as the sole memory layer for agents that need semantic search or temporal reasoning — supplement with Tier 1 or Tier 2 retrieval.

**Use sqlite-vec / local vector DB (Tier 1):**
- When wiki depth exceeds ~200 entities and context-window saturation is a daily occurrence.
- When no managed service dependency is acceptable (self-sovereign operation).
- When budget is constrained ($0 operational cost).
- *Avoid* if concurrent write operations from multiple agents are required (sqlite-vec is single-writer; use pgvector with PostgreSQL for multi-writer scenarios).

**Use Mem0 Standard ($19/mo, Tier 2):**
- When semantic memory retrieval across agents is needed and managed reliability is preferred over self-hosting.
- For conversational, unstructured memory (client preferences, user history).
- *Avoid* if: temporal fact evolution matters (no temporal validity windows); if graph reasoning is required (Pro tier $249/mo, not cost-effective for solo operation); if GDPR requires data localisation in Germany (Mem0 Cloud infrastructure is US-based — verify with Mem0 enterprise for EU hosting).

**Use Zep Flex ($25/mo, Tier 2):**
- When agents track evolving facts (client status, project state, team composition over weeks/months).
- When temporal reasoning tasks are important (63.8% LongMemEval vs. Mem0's 49.0%) [3].
- *Avoid* if: immediate read-after-write is required (async ingestion delays); if full self-hosting without managed cloud is required (CE deprecated).

**Use Letta sleep-time agents:**
- When the voice-notes consolidation pipeline is a bottleneck (daily friction exceeds 30 minutes).
- When the agent portfolio includes long-lived stateful agents accumulating >1,000 memories.
- For agents with predictable, recurring contexts (project-specific coding agents, recurring client relationship agents).
- *Avoid* for stateless or one-shot agents where the sleep-time overhead is not amortised.

**Use Cognee / GraphRAG (Tier 4):**
- When `edges.jsonl` exceeds ~500 edges and manual maintenance becomes a bottleneck.
- When diverse document sources (client PDFs, research papers, codebase) need to be ingested into a unified knowledge graph.
- When ontological consistency and temporal edge weighting are required.
- *Avoid* until the simpler tiers are stress-tested — the operational overhead is not justified at current Jetix scale.

---

## Comparison to Anthropic Ecosystem

### Mem0

Integration with Claude API is external — Mem0 functions as a third-party memory layer that Claude can call via API. No native Claude Agent SDK or Anthropic Agent Skills integration exists. The OpenMemory MCP Server allows use via any MCP-compatible Claude client. For Jetix, this means Mem0 must be wired into the agent's prompt construction and tool-calling loop manually. The integration is well-documented and tested (48K GitHub stars means many production examples exist), but it is not a first-class Claude feature. Mem0 is model-agnostic by design.

### Letta

Letta explicitly supports Claude models via `anthropic:claude-*` configuration. The Letta REST Agents API and Apache 2.0 open-source code make it straightforward to build Claude-powered agents with Letta as the memory/state backend. Sleep-time agents can use different Claude model tiers: Haiku 4.5 for latency-sensitive primary agent conversation, Opus 4 for memory consolidation during sleep [86]. For Jetix's multi-agent setup, Letta's native multi-agent memory sharing is the most relevant differentiator over Mem0. Not a native Claude platform feature; requires self-hosting or Letta Cloud.

### Zep

Integration with Claude via the Graphiti MCP Server (November 2025) provides direct connectivity with Claude Desktop and any MCP client [83]. Claude API integration requires standard Zep SDK patterns (not native). Zep is explicitly model-agnostic. The Graphiti OSS repository (Apache 2.0) can be run independently and connected to Claude agents via tool calls. Not a Claude-native feature.

### Cognee

External integration only. Cognee works with Claude via its LLM provider abstraction. CLAUDE.md is present in the Cognee repository. No native Claude Agent SDK or Anthropic-specific tooling. Integration with Claude requires standard Anthropic API patterns [17].

### Anthropic Memory Tool

This is the only memory system with native first-class integration into the Claude platform. The tool appears in the official Claude SDK (`BetaAbstractMemoryTool` in Python, `betaMemoryTool` in TypeScript) as a first-party tool rather than a third-party integration. It is eligible for Zero Data Retention arrangements, which no external memory service can offer for data flowing through the Anthropic API. It integrates natively with CLAUDE.md and the Agent Skills standard.

**Critical scope distinction:** The developer API memory tool (beta, `context-management-2025-06-27`) and the consumer Claude.ai memory feature are separate systems with different architectures and different APIs. The developer tool requires explicit implementation of client-side storage handlers; the consumer feature is automatic. Confusing the two leads to incorrect architectural expectations.

### Sleep-Time Compute

Sleep-time compute is a Letta-developed pattern that works with any Claude model through the Letta platform. It is not directly supported by the Claude API or Claude Agent SDK as a first-class feature. The pattern can be implemented independently of Letta using any orchestration framework that supports asynchronous agent execution, but Letta's open-source implementation is the most complete reference.

### Anthropic's Own Memory Tool Scope and Native vs. External Trade-Off

Anthropic's memory tool is deliberately minimal — a file-based primitive that gives agents file I/O operations and lets developers build on top. It solves the problem of "where does the state live" but not "how is state semantically organised" or "how does temporal fact evolution work." The design philosophy aligns with Anthropic's broader approach of providing composable primitives rather than opinionated frameworks.

The native vs. external trade-off for Jetix: native (Anthropic memory tool) provides ZDR compliance, zero additional vendor, and deepest Claude integration; external (Mem0, Zep) provides semantic retrieval, temporal modelling, and multi-agent coordination that the native tool lacks. The optimal architecture is layered: native tool for write-side capture and GDPR compliance, supplemented by external retrieval (sqlite-vec or Mem0 Standard) for semantic search across the growing memory corpus.

---

## Recommendation for Jetix

### 1. Baseline Classification

Jetix's current architecture — `wiki/` markdown with 9 entity types, frontmatter-indexed, `edges.jsonl` graph, per-agent `strategies.md` + `scratchpad.md`, `mailboxes.jsonl` inter-agent messaging, and voice-notes ingest→extract→filter→review pipeline — is correctly classified as **System Prompt Learning + Voyager-style skill library + human-in-loop consolidation**. This is the dominant production pattern as described by both Andrej Karpathy ("LLM Wiki" pattern, April 2026) and Anthropic's own engineering team (Boris Cherny's "shared team memory in git" workflow, January 2026) [4][34]. It is not a technical debt problem requiring urgent remediation. It is a defensible, transparent, portable architecture that any operator can inspect, version, and debug without tooling.

The patterns Jetix already implements: compaction (voice-notes pipeline), structured note-taking (scratchpad.md), sub-agent architecture (11 specialised agents), skill library (strategies.md), associative memory (edges.jsonl). What is missing is automated execution of the compaction and consolidation steps, and semantic retrieval at scale.

### 2. Concrete Gaps

The five concrete gaps that distinguish the current Jetix baseline from state-of-the-art, ranked by operational impact:

1. **No vector retrieval** — all wiki access requires loading files into context, which does not scale past ~200 entities. Semantic search across agents' collective knowledge requires either loading large amounts of context (expensive, context-rot prone) or manual operator lookup (time-intensive). *Impact: Medium now, High at 200+ wiki entities.*

2. **No automatic consolidation** — the voice-notes ingest→extract→filter→review pipeline requires human filter+review of every entry before it enters the wiki. This is the highest-friction maintenance step in the current architecture. *Impact: High (daily operational burden).*

3. **No temporal knowledge graph** — `edges.jsonl` is a static, unweighted flat file. It cannot answer "what was the relationship between Entity A and Entity B in December?" or "which edges have been superseded by newer information?" For a consultancy where client relationships, project statuses, and team compositions evolve over weeks, this is a real gap. *Impact: Medium currently, will grow.*

4. **No cross-agent query API** — agents cannot programmatically query each other's `strategies.md`, wiki entities, or conversation history. Cross-agent knowledge sharing requires the operator to manually surface relevant context. *Impact: Medium (workaround exists via operator mediation, but does not scale).*

5. **No evaluation harness** — there is no mechanism to measure whether memory additions improve task performance, whether memory content is drifting from ground truth, or whether specific agents are accumulating stale facts. Without evaluation, memory quality can degrade silently. *Impact: Low now, High as system scales.*

### 3. Phased Recommendation

**Phase 1 — Immediate (this week, zero infrastructure cost, zero disruption)**

*Action:* Enable Claude Projects memory for all 6 departments. Map Jetix's 6-department structure to 6 Claude Projects. Per-project memory isolation, available on all Claude plans since March 2026, provides free cross-session context accumulation without any new infrastructure. No change to existing wiki/ or strategies.md files.

*Action:* Formalise `strategies.md` files as SKILL.md files using the Anthropic Agent Skills standard (Apache 2.0, cross-platform, December 2025) [30]. This is a drop-in upgrade: add YAML frontmatter to each `strategies.md` specifying `name`, `description`, `trigger_phrases`, and `full_skill_path`. This adds progressive disclosure (only metadata loaded at session start; full strategy loaded when triggered), cross-platform portability (works with Claude Code, Claude.ai, and the Claude Agent SDK), and future-proofs the procedural memory layer without changing content.

*Action:* Add a simple evaluation canary to the wiki: a file `wiki/eval-canaries.md` containing 10–15 deliberately unusual, specific facts (e.g., "The fictional client Zephyr GmbH uses a custom data pipeline named 'Redwing'"). Run these as probe queries every two weeks against each agent's memory. If an agent fails to recall a canary it should know, it signals memory degradation. This is the minimum viable evaluation harness — zero infrastructure, immediate.

*Expected outcomes:* Cross-session preference learning for all 6 departments (via Claude Projects); progressive skill disclosure reducing per-session token overhead; a baseline for memory quality tracking. Cost: $0 additional.

**Phase 2 — Targeted Tool Adoption (1–4 weeks)**

*Action:* Add `sqlite-vec` as a semantic index over wiki entities when wiki entity count exceeds ~200 or when semantic search across entities becomes daily friction [96]. The integration pattern: maintain `wiki/` markdown files as the authoritative source of truth; run a lightweight embedding script on wiki changes (via git hook or cron) to update the sqlite-vec index; add a `wiki-search` tool to relevant agents that performs semantic lookup against the index. This is the highest-ROI addition for a single operator: free, zero-server, coexists with the existing file structure, and directly addresses the "no vector retrieval" gap.

*Action:* Replace the manual voice-notes filter+review step with a **Letta sleep-time agent trial** on one high-volume agent (e.g., the client relationship agent or the primary orchestration agent). Self-host Letta (free, Apache 2.0, Docker). Configure a sleep-time agent to: (1) process daily voice-note summaries extracted from the ingest pipeline; (2) propose wiki updates in a `proposed-wiki-updates.md` file for human approval before committing; (3) surface consolidation candidates (duplicate entities, outdated edges) for operator review. Human approval before committing to wiki preserves the existing quality gate while automating the extraction step. If the trial reduces consolidation time from hours to <15 minutes of approval, promote to all agents.

*Action:* For agents that track evolving facts (client status, project states, engagement histories), trial **Zep Flex ($25/mo)** for temporal memory. The Graphiti MCP server enables Claude Desktop integration without additional code. Limit the trial to 2–3 agents with the most dynamic fact profiles. Run for 30 days and measure recall accuracy on known temporal queries (e.g., "What was Client X's project status in February?"). If accuracy meaningfully exceeds the file-based baseline, expand.

*Expected outcomes:* Semantic wiki search (sqlite-vec); reduced manual consolidation burden (Letta sleep-time); temporal fact tracking for evolving entities (Zep Flex). Estimated cost: $25/mo Zep + $0 Letta self-hosted + $0 sqlite-vec = **$25/mo**.

**Phase 3 — Long-term Architecture (3–6 months, if Phase 2 validates)**

*Action:* If `edges.jsonl` maintenance exceeds practical limits (>500 edges, multiple entity type updates per week), migrate to **Cognee's ECL pipeline** as the knowledge graph layer. The migration pattern: keep `wiki/` as Cognee's `raw/` source; let Cognee maintain the derived graph (entity extraction, relationship mapping, edge weighting via `memify`); run the ECL pipeline on wiki changes via git hook. Cognee's Apache 2.0 license and local-first design preserve self-sovereign operation [17].

*Action:* Implement a formal **evaluation harness** (LangSmith or a custom benchmark script) that runs weekly against a fixed set of 50+ memory probe questions across all 11 agents. This measures memory recall stability over time and surfaces any retrieval drift or false memory consolidation before it affects production. The probe set should cover: (1) stable facts (entity attributes); (2) temporal supersession (facts that changed); (3) multi-hop reasoning (facts requiring cross-entity inference); (4) abstention (questions whose answers are not in the wiki).

*Expected outcomes:* Fully maintained knowledge graph without manual JSONL editing; measurable memory quality metrics enabling proactive quality management. Estimated additional cost: $0 (Cognee self-hosted) + LangSmith tracing costs (free tier available).

### 4. Tool Choice with Rationale

**Primary recommendation: Anthropic Memory Tool (native) + sqlite-vec (Phase 2) + Letta sleep-time agent (Phase 2, trial)**

Rationale:

- **Anthropic Memory Tool** is the correct default for all Claude-based agents because it is the only ZDR-eligible memory mechanism for a Berlin-based EU consultancy. GDPR data-subject access and erasure rights apply to any personal data retained in memory systems. Using a client-side storage handler (e.g., local PostgreSQL or encrypted file store) keeps all data within Jetix's infrastructure, eliminates the third-party DPA agreements required by Mem0 Cloud or Zep Cloud, and is eligible for ZDR arrangements with Anthropic. Cost: $0 additional.

- **sqlite-vec** is the correct semantic retrieval layer at Jetix's scale because it requires zero server infrastructure, coexists with the existing file-based system as an index layer rather than a replacement, and is free. It does not displace any existing component — it adds capability on top. This is the single highest-ROI upgrade when wiki depth reaches the context-saturation threshold.

- **Letta sleep-time agents** (trial, self-hosted) directly address the most acute operational burden: the manual filter+review step in the voice-notes pipeline. The trial approach (one agent, human approval gates maintained) limits risk while providing genuine operational data on whether the automation saves meaningful time. If the trial is successful, the pattern extends to all 11 agents. If unsuccessful, Letta self-hosted is free to abandon with no data migration cost.

**Do not adopt at this stage:** Mem0 Cloud Standard ($19/mo) — provides less value than the Anthropic Memory Tool + sqlite-vec combination at lower cost; no temporal modelling; independent benchmark scores (49.0% LongMemEval) do not justify the managed dependency. Zep Cloud Flex ($25/mo) — defer until a specific agent demonstrably needs temporal fact tracking and the Letta trial has validated automation appetite. Cognee — defer until `edges.jsonl` maintenance is a practical bottleneck.

### 5. Risk Flags

**Lock-in risk:** The Anthropic Memory Tool is Claude-specific — memories stored using it do not port to other LLM providers. Given Jetix's deliberate Claude-native architecture, this is an acceptable trade-off, but should be noted explicitly. If the organisation ever evaluates a non-Anthropic model, the memory layer would require rebuilding. Mitigation: keep the file-based wiki as the primary source of truth regardless of which memory tool is layered on top; the wiki files are model-agnostic.

**GDPR risk (acute for Berlin-based EU consultancy):** Any memory system that retains personal data about clients, their employees, or their customers is subject to GDPR. Specific obligations triggered:
- *Article 6 (lawful basis):* Memory writes containing personal data require a lawful basis (likely legitimate interest or contract performance for B2B contexts).
- *Article 17 (right to erasure):* Any personal data stored in the memory layer must be erasable on request. File-based systems are erasable; vector embeddings may require re-embedding to fully purge a fact; knowledge graphs require explicit edge deletion (Zep's validity windows support this; Mem0's audit trail supports targeted deletion).
- *Article 20 (data portability):* If memory stores personal data, data subjects may request export in a structured format. File-based memory is trivially portable; managed cloud systems require API export.
- *Replika precedent:* The €5M GDPR fine (May 2025) establishes that inadequate safeguards for emotional/behavioural data and lack of age verification triggers enforcement. For a B2B consultancy, the risk profile is lower but the obligations are the same [17][18].

*Mitigation:* Use ZDR-eligible configurations (Anthropic Memory Tool with client-side storage); implement tiered memory (session context is ephemeral and not retained; extracted facts are GDPR-deletable on request; audit logs are pseudonymised); conduct a DPIA before deploying any memory system that stores personal client data; document the lawful basis for each memory category.

**Retrieval drift risk:** As the wiki and vector index grow, semantic search quality may degrade (retrieval drift, discussed in Section 5.2). Mitigation: the evaluation canary harness (Phase 1) provides early detection. Monthly re-embedding of the sqlite-vec index (if the embedding model changes) prevents dimension mismatch issues.

**Memory poisoning risk:** For a consultancy ingesting external data (client documents, voice notes from meetings), any content from external sources that enters the memory pipeline could poison downstream retrieval. The most relevant vector is indirect prompt injection via document content (as demonstrated in the AWS Bedrock case [45]). Mitigation: apply content sanitisation before the voice-notes extraction step; maintain differential trust levels (operator-written wiki entries are trusted; client-provided documents are sandboxed until reviewed); never allow extracted memories from external documents to directly overwrite existing entries without a conflict-resolution step.

**Vendor failure risk:** Zep Community Edition was deprecated April 2025 with no self-hosting option for the full platform — the most recent example of an agent memory vendor reducing open-source viability [32]. Mitigation: prefer Apache 2.0 open-source tools (Mem0, Letta, Cognee, sqlite-vec) over managed-only services; keep the file-based wiki as the primary source of truth regardless of which retrieval layer is adopted; ensure all memory data can be exported and re-ingested if a vendor discontinues service.

---

## Sources

[1] Parisi, G.I., Kemker, R., Part, J.L., Kanan, C., & Wermter, S. "Continual Lifelong Learning with Neural Networks: A Review." *Neural Networks* (Elsevier, 2019-05-01). https://arxiv.org/abs/1802.07569

[2] De Lange, M., Aljundi, R., Masana, M., Parisot, S., Jia, X., Leonardis, A., Slabaugh, G., & Tuytelaars, T. "A Continual Learning Survey." *IEEE Transactions on Pattern Analysis and Machine Intelligence* (2021/2022). https://arxiv.org/abs/1909.08383

[3] Vectorize. "Mem0 vs Zep (Graphiti): AI Agent Memory Compared (2026)." March 2026. https://vectorize.io/articles/mem0-vs-zep-graphiti-agent-memory-comparison/

[4] Antigravity.codes. "Karpathy's LLM Wiki: The Complete Guide to His Idea File." April 2026 (based on Karpathy's viral post). https://antigravity.codes/blog/karpathy-llm-wiki

[5] Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S.G., Stoica, I., & Gonzalez, J.E. "MemGPT: Towards LLMs as Operating Systems." *arXiv:2310.08560* (2023). https://arxiv.org/abs/2310.08560

[6] Anthropic Engineering. "Effective Context Engineering for AI Agents." *Anthropic Blog* (2025-09-29). https://www.anthropic.com/engineering/effective-context-engineering

[7] Chhikara, P., Khant, D., Aryan, S., Singh, T., & Yadav, D. "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory." *arXiv:2504.19413* (2025). https://arxiv.org/abs/2504.19413

[8] Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. "LoRA: Low-Rank Adaptation of Large Language Models." *ICLR 2022* (arXiv:2106.09685). https://arxiv.org/abs/2106.09685

[9] Hinton, G., Vinyals, O., & Dean, J. "Distilling the Knowledge in a Neural Network." *arXiv:1503.02531* (2015). https://arxiv.org/abs/1503.02531

[10] Anthropic. "Memory tool — Claude API Docs." *platform.claude.com* (2025-09-29, beta). https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool

[11] Park, J.S., O'Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., & Bernstein, M.S. "Generative Agents: Interactive Simulacra of Human Behavior." *arXiv:2304.03442* / UIST 2023. https://arxiv.org/abs/2304.03442

[12] Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson, J. "From Local to Global: A Graph RAG Approach to Query-Focused Summarization." *arXiv:2404.16130* (Microsoft Research, 2024). https://arxiv.org/abs/2404.16130

[13] Gutierrez, B.J., Shu, Y., Gu, Y., Yasunaga, M., & Su, Y. "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models." *arXiv:2405.14831* / NeurIPS 2024. https://arxiv.org/abs/2405.14831

[14] Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., & Anandkumar, A. "Voyager: An Open-Ended Embodied Agent with Large Language Models." *arXiv:2305.16291* (2023). https://arxiv.org/abs/2305.16291

[15] Cognee. "Cognee Raises $7.5M Seed to Build Memory for AI Agents." February 2026. https://www.cognee.ai/blog/cognee-news/cognee-raises-seven-million-five-hundred-thousand

[16] Gutierrez, B.J., Shu, Y., Qi, W., Zhou, S., & Su, Y. "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models." *arXiv:2502.14802* / ICML 2025. https://arxiv.org/abs/2502.14802

[17] Morri Rossetti. "Replika: €5 Million fine for the U.S.-based company." June 2025. https://morrirossetti.it/en/insight/publications/

[18] Buchanan Ingersoll & Rooney PC. "Emotional AI Company Fined for Privacy Violations." May 2025. https://bipc.com

[19] Lin, K., Snell, C., Wang, Y., Packer, C., Wooders, S., Stoica, I., & Gonzalez, J.E. "Sleep-time Compute: Beyond Inference Scaling at Test-time." *arXiv:2504.13171* (Letta AI / UC Berkeley, April 2025). https://arxiv.org/abs/2504.13171

[20] Anthropic. "Anthropic Brings Claude's Memory Feature to All Paid Users." CNET report (2025-10-23). https://www.cnet.com/tech/services-and-software/anthropic-brings-claudes-memory-feature-to-all-paid-users/

[21] HuggingFace / codelion. "System Prompt Learning: Teaching LLMs to Learn Problem-Solving Strategies from Experience." HuggingFace Papers (2025). https://huggingface.co/papers

[22] Letta. "Continual Learning in Token Space." *Letta Blog* (2025-12-11). https://www.letta.com/blog/continual-learning

[23] Letta Docs. "Sleep-time agents." https://docs.letta.com/guides/agents/architectures/sleeptime/

[24] Will Knight / Wired. "Do Large Language Models Dream of AI Agents?" (Letta/sleep-time compute profile). 2025. https://www.wired.com/story/sleeptime-compute-chatbots-ai-agents/

[25] Zheng, J., Shi, C., Cai, X., Li, Q., Zhang, D., Yu, C., Dong, M., & Ma, Q. "Lifelong Learning of Large Language Model Based Agents: A Roadmap." *arXiv:2501.07278* (2025). https://arxiv.org/abs/2501.07278

[26] Letta. "What We Are Leaving Behind / Context Repositories." *Letta Blog* (2026-03-16). https://www.letta.com/blog/our-next-phase

[27] Letta Documentation. "Introduction to Stateful Agents." *Letta Docs* (2024–2025). https://docs.letta.com/guides/core-concepts/agents

[28] Letta Engineering. "Sleep-time Compute." *Letta Blog* (2025-04-21). https://www.letta.com/blog/sleep-time-compute

[29] Xu, W., Liang, Z., Mei, K., Gao, H., Tan, J., & Zhang, Y. "A-MEM: Agentic Memory for LLM Agents." *arXiv:2502.12110* / NeurIPS 2025. https://arxiv.org/abs/2502.12110

[30] Anthropic Engineering. "Equipping agents for the real world with Agent Skills." *Anthropic Blog* (December 2025). https://www.anthropic.com/engineering/equipping-agents-with-skills

[31] Mem0. "State of AI Agent Memory 2026." April 2026. https://mem0.ai/blog/state-of-ai-agent-memory-2026

[32] Zep. "Announcing a New Direction for Zep's Open Source Strategy." April 2025. https://blog.getzep.com/announcing-a-new-direction-for-zeps-open-source-strategy/

[33] Dwarves Foundation Memo. "Mem0 & Mem0-Graph breakdown." August 2025. https://memo.d.foundation/breakdown/mem0

[34] AI Agent Economy / Substack. "Anthropic Just Leaked How Their Best Engineers Use Claude Code." January 2026 (Boris Cherny workflow). https://aiagenteconomy.substack.com

[35] LinkedIn. "Claude 4 Models: Opus vs Sonnet." (Alex Albert quote on long-horizon performance). 2025. https://www.linkedin.com/pulse/claude-4-guide-new-ai-models-when-how-use-them/

[36] Lewis, P., Perez, E., Piktus, A., et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020* (arXiv:2005.11401). https://arxiv.org/abs/2005.11401

[37] Simon Willison. "2025: The year in LLMs." *simonwillison.net* (2025-12-31). https://simonwillison.net/2025/Dec/31/the-year-in-llms/

[38] Chen, Zhaorun et al. "AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases." *arXiv:2407.12784* (July 2024). https://arxiv.org/abs/2407.12784

[39] Zou et al. "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models." *USENIX Security 2025*. https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf

[40] arXiv:2505.18543. "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation." May 2025. https://arxiv.org/html/2505.18543

[41] Hu et al. "MemoryAgentBench: Evaluating Memory Agents." *arXiv:2507.05257* (July 2025). https://huggingface.co/datasets/ai-hyz/MemoryAgentBench

[42] Morph LLM / Chroma research. "Context Rot: Why LLMs Degrade as Context Grows." 2025. https://morphllm.com/context-rot

[43] Zep blog. "Is Mem0 Really SOTA in Agent Memory?" *blog.getzep.com* (2025). https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/

[44] arXiv:2603.11768. "Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the SSGM Framework." March 2026. https://arxiv.org/abs/2603.11768

[45] Palo Alto Networks Unit 42. "When AI Remembers Too Much — Persistent Behaviors in Agents." October 2025. https://unit42.paloaltonetworks.com/indirect-prompt-injection-attacks-on-llm-agents/

[46] Memgraph. "Context Rot Is Real: Why Your AI Gets Worse Over Time." March 2026. https://memgraph.com/blog/ai-context-rot

[47] Liu, Nelson F. et al. "Lost in the Middle: How Language Models Use Long Contexts." *Transactions of the ACL* 2024 (arXiv:2307.03172, July 2023). https://arxiv.org/abs/2307.03172

[48] Emergent Mind. "LoCoMo: Conversational Memory Benchmark." (Compiled from Maharana et al. 2024 and extensions). https://emergentmind.com/topics/locomo

[49] EDPB. "CEF 2025: Launch of coordinated enforcement on the right to erasure." *edpb.europa.eu* (March 5, 2025). https://edpb.europa.eu

[50] Chanl AI. "GDPR says delete. EU AI Act says keep. Now what?" April 2026. https://channel.tel/blog/gdpr-delete-eu-ai-act-keep-memory-compliance

[51] EDPB Opinion 28/2024 on data controller status of AI developers. *edpb.europa.eu* (2024). https://edpb.europa.eu

[52] Wu, Di et al. "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory." *arXiv:2410.10813* / ICLR 2025. https://arxiv.org/abs/2410.10813

[53] Emergent Mind. "LongMemEval Benchmark." (Updated February 2026, TiMem/EverMemOS/Supermemory scores). https://emergentmind.com/topics/longmemeval-benchmark

[54] Maharana, Adyasha et al. "Evaluating Very Long-Term Conversational Memory of LLM Agents." *arXiv:2402.17753* / ACL 2024. https://arxiv.org/abs/2402.17753

[55] Snap Research. LoCoMo project page. https://snap-research.github.io/locomo/

[56] Mem0. "AI Memory Research: 26% Accuracy Boost for LLMs." *mem0.ai/research* (April 2026). https://mem0.ai/research-3

[57] Zhong, W., Guo, L., Gao, Q., Ye, H., & Wang, Y. "MemoryBank: Enhancing Large Language Models with Long-Term Memory." *AAAI 2024* (arXiv:2305.10250). https://arxiv.org/abs/2305.10250

[58] Ai et al. "MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems." *arXiv:2510.17281* (October 2025). https://arxiv.org/abs/2510.17281

[59] Wang, Xingyao et al. "MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback." *arXiv:2309.10691* (September 2023). https://arxiv.org/abs/2309.10691

[60] Guo, Bernal et al. "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models." *NeurIPS 2024*. https://arxiv.org/abs/2405.14831

[61] HippoRAG 2. "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models." *ICML 2025*. https://icml.cc/virtual/2025/poster/45585

[62] Zhang et al. "InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens." *arXiv:2402.13718* (February 2024). https://arxiv.org/abs/2402.13718

[63] DialSim project. Multi-party TV show dialogues averaging 350K tokens, time-constrained evaluation. https://dialsim.github.io

[64] Shinn, N., Cassano, F., Labash, B., Gopinath, A., Narasimhan, K., & Yao, S. "Reflexion: Language Agents with Verbal Reinforcement Learning." *arXiv:2303.11366* / NeurIPS 2023. https://arxiv.org/abs/2303.11366

[65] Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. "Self-RAG: Learning to Retrieve, Generate and Critique through Self-Reflection." *arXiv:2310.11511* / ICLR 2024. https://arxiv.org/abs/2310.11511

[66] OpenAI. "Memory and new controls for ChatGPT." *openai.com* (February 13, 2024, updated June 2025). https://openai.com/index/memory-and-new-controls-for-chatgpt/

[67] Ars Technica. "ChatGPT can now remember and reference all your previous chats." April 2025. https://arstechnica.com/ai/2025/04/chatgpt-can-now-reference-all-your-previous-chats/

[68] Embrace the Red. "How ChatGPT Remembers You: A Deep Dive into Its Memory and Preferences." May 2025. https://embracethered.com/blog/posts/2025/chatgpt-memory-deep-dive/

[69] Reworked.co. "Claude AI Gains Persistent Memory in Latest Anthropic Update." September 2025. https://reworked.co/digital-workplace/claude-ai-gains-persistent-memory/

[70] Skywork AI. "Claude Memory: A Deep Dive into Anthropic's Persistent Context Solution." September 2025. https://skywork.ai/blog/claude-memory/

[71] MacRumors. "Anthropic Adds Free Memory Feature and Import Tool." March 2026. https://www.macrumors.com/2026/03/02/anthropic-adds-free-memory-feature-and-import-tool/

[72] Forbes. "Inside OpenAI Chairman's $10 Billion AI Customer Service Startup." November 2025. https://forbes.com/sites/richardnieva/2025/11/05/sierra-ai-bret-taylor/

[73] Sierra. "Sierra Agent OS 2.0: from answers to memory and action." November 5, 2025. https://sierra.ai/blog/agent-os-2-0

[74] Decagon. "User memory: Persistent context that makes every interaction feel personal." March 2026. https://decagon.ai/blog/user-memory

[75] Decagon. "Introducing Proactive Agents: User Memory and Outbound Voice." March 2026. https://decagon.ai/blog/spring26-product-launch

[76] Assembled. "What is Decagon AI? Benefits, Use Cases, & Alternatives." November 2025. https://assembled.com/page/decagon-ai

[77] Cognition AI. "Devin can now Schedule Devins." March 2026. https://cognition.ai/blog/devin-can-now-schedule-devins

[78] Cognition AI. "Devin can now Manage Devins." March 2026. https://cognition.ai/blog/devin-can-now-manage-devins

[79] Perplexity. "Introducing AI assistants with memory." November 26, 2025. https://perplexity.ai/hub/blog/introducing-ai-assistants-with-memory

[80] Google Support. "Get personalization with memory of your past Gemini chats." https://support.google.com/gemini/answer/16598469

[81] Ryan, Jack and Chalef, Daniel (Zep AI). "Zep: A Temporal Knowledge Graph Architecture for Agent Memory." *arXiv:2501.13956* (January 2025). https://arxiv.org/abs/2501.13956

[82] Zep. "Zep Is The New State of the Art In Agent Memory." January 2025. https://blog.getzep.com/state-of-the-art-agent-memory/

[83] Atlan. "Zep vs Mem0: Benchmarks, Pricing, and When to Use Each." April 2026. https://atlan.com/know/zep-vs-mem0/

[84] Cognee. "Temporal Cognification: Time-Aware AI Memory for LLMs." November 2025. https://www.cognee.ai/blog/cognee-news/update-temporal-cognification

[85] LanceDB. "How Cognee Builds AI Memory Layers with LanceDB." September 2025. https://www.lancedb.com/blog/case-study-cognee/

[86] Packer, Charles. "Letta Code bets on memory as the missing layer in coding agents." Tessl, December 2025. https://tessl.io/blog/letta-code

[87] Monigatti, Leonie. "Virtual context management with MemGPT and Letta." October 2025. https://www.leoniemonigatti.com/blog/memgpt-letta/

[88] Mem0 Research Page. "Benchmarking Mem0's token-efficient memory algorithm." April 2026. https://mem0.ai/research

[89] Kynoch, B., Latapie, H., & Van Der Sluis, D. "RecallM: An Adaptable Memory Mechanism with Temporal Understanding for Large Language Models." *arXiv:2307.02738* (2023). https://arxiv.org/abs/2307.02738

[90] Wang, Y. et al. "MEMORYLLM: Towards Self-Updatable Large Language Models." *arXiv:2402.13795* (2024). https://arxiv.org/abs/2402.13795

[91] Fountas, Z. et al. "Human-like Episodic Memory for Infinite Context LLMs." *arXiv:2407.09450* (2024). https://arxiv.org/abs/2407.09450

[92] Wang, W. et al. "Augmenting Language Models with Long-Term Memory." *arXiv:2306.07174* / NeurIPS 2023. https://arxiv.org/abs/2306.07174

[93] Zhang, Z. et al. "A Survey on the Memory Mechanism of Large Language Model based Agents." *arXiv:2404.13501* (2024). https://arxiv.org/abs/2404.13501

[94] Anthropic. "Claude Code Memory documentation." *docs.anthropic.com* (2026-04-13). https://docs.anthropic.com/en/docs/claude-code/memory

[95] Reddit/r/ClaudeCode. "Treating CLAUDE.md as an Operating System." https://www.reddit.com/r/ClaudeCode/

[96] Alex Garcia / Mozilla. "asg017/sqlite-vec: A vector search SQLite extension that runs anywhere." https://github.com/asg017/sqlite-vec

[97] PostgreSQL.org. "pgvector 0.7.0 Released." April 2024. https://www.postgresql.org/about/news/pgvector-070-released-2852/

[98] Qdrant. "Pricing for Cloud and Vector Database Solutions." https://qdrant.tech/pricing/

[99] Mem0. "AI Memory Pricing — LLM Memory Plans Starting Free." April 2026. https://mem0.ai/pricing

[100] Techmeme. "Mem0 raises $24M including a $20M Series A." October 2025. https://www.techmeme.com/251028/p32

[101] Mem0. "Platform vs Open Source." https://docs.mem0.ai/platform/platform-vs-oss

[102] Letta. "Pricing." https://www.letta.com/pricing

[103] Microsoft Research. "GraphRAG: New tool for complex data discovery now on GitHub." https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery/

[104] Articsledge. "What is GraphRAG? Complete Guide to Graph-Based RAG in 2026." (Including LazyGraphRAG). https://www.articsledge.com/post/graphrag-review/

[105] Obsidian Forum. "Automated Knowledge Graphs with Cognee." https://forum.obsidian.md/t/automated-knowledge-graphs-with-cognee/

[106] XTrace.ai. "Is Claude's Memory Worth the Price?" April 2026. https://xtrace.ai/blog/claude-memory-2026-limits-and-fixes

[107] Simon Willison. "Simon Willison on llm-memory." https://simonwillison.net/tags/llm-memory/

[108] IBTimes India. "YC-Backed Startup Mem0 Launches Long-Term AI Memory." https://www.ibtimes.co.in/yc-backed-startup-mem0-launches-long-term-ai-memory

[109] YouTube. "Why AI Agents Need Memory with Taranjeet Singh (Mem0)." June 2025. https://www.youtube.com/watch?v=ljb7zd2nzfk

[110] Simon Willison. "LLM predictions for 2026, shared with Oxide and Friends." January 2026. https://simonwillison.net/2026/Jan/8/llm-predictions-2026/

[111] arXiv:2604.06169. "In-Place Test-Time Training." April 2026. https://arxiv.org/abs/2604.06169

[112] NVIDIA Technical Blog. "Reimagining LLM Memory: Using Context as Training Data Unlocks Models that Learn at Test Time." January 2026. https://developer.nvidia.com/blog/reimagining-llm-memory-using-context-as-training-data/

[113] LangChain. "LangMem SDK for agent long-term memory." April 2026. https://www.langchain.com/blog/langmem-sdk-launch

[114] LlamaIndex. "Improved Long & Short-Term Memory for LlamaIndex Agents." May 2025. https://www.llamaindex.ai/blog/improved-memory-agents

[115] Redis. "It's official: We're the #1 AI agent data storage tool." August 2025. https://redis.io/blog/best-ai-agent-data-storage-2025/

[116] Weaviate. "Weaviate in 2025: Reliable Foundations for Agentic Systems." January 2026. https://weaviate.io/blog/weaviate-in-2025

[117] Zhang et al. (BAI Lab). "Memory OS of AI Agent." *arXiv:2506.06326* / EMNLP 2025 Oral. https://arxiv.org/pdf/2506.06326

[118] Atlan. "Best AI Agent Memory Frameworks 2026." April 2026. https://atlan.com/know/best-ai-agent-memory-frameworks-2026/

[119] Atlan. "AI Memory System vs RAG: Key Differences and Use Cases 2026." 2026. https://atlan.com/know/ai-memory-system-vs-rag/

[120] Atlan. "How to Add Long-Term Memory to LangChain Agents." 2026. https://atlan.com/know/long-term-memory-langchain-agents/

[121] Till Freitag. "LangGraph vs. CrewAI vs. AutoGen: Which Multi-Agent Framework in 2026?" https://till-freitag.com/blog/langraph-vs-crewai-vs-autogen/

[122] arXiv:2504.01241. "Catastrophic Forgetting in LLMs: A Comparative Analysis Across Architectures." April 2025. https://arxiv.org/abs/2504.01241

[123] Santopaolo. "Your LLM Has Amnesia: A Production Guide to Memory That Actually Works." February 2026. https://genmind.ch/your-llm-has-amnesia/

[124] Mem0. "Self-Hosting Mem0: A Complete Docker Deployment Guide." February 2026. https://mem0.ai/blog/self-host-mem0-docker

[125] MemPalace.tech. "MemPalace vs Mem0 (2026): $0 vs $249/mo." April 2026. https://www.mempalace.tech/compare/mempalace-vs-mem0

[126] Let's Data Science. "Claude Agent SDK: Build a Production AI Agent." https://letsdatascience.com/blog/claude-agent-sdk-tutorial/

[127] YouTube. "Codex in Cursor: 3 Levels of AGENTS.md Memory Explained." October 2025. https://www.youtube.com/watch?v=A1wct93Haz4

[128] Anthropic API Release Notes Overview. https://platform.claude.com/docs/en/release-notes/overview

[129] DeepMind. "Titans: Learning to Memorize at Test Time." *arXiv:2501.00663* (December 2025). https://arxiv.org/abs/2501.00663

[130] arXiv:2505.18543. "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation." May 2025. https://arxiv.org/html/2505.18543

[131] Cognition AI. "How Cognition Uses Devin to Build Devin." February 2026. https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin

[132] Microsoft Research. "Jonathan Larson at Microsoft Research — News and Awards." (BenchmarkQED project). https://www.microsoft.com/en-us/research/people/jolarso/

[133] Monigatti, Leonie. "Exploring Anthropic's Memory Tool." November 2025. https://www.leoniemonigatti.com/blog/claude-memory-tool/

[134] Letta. "Agent Memory: How to Build Agents that Learn and Remember." July 2025. https://www.letta.com/blog/agent-memory

[135] Section AI. "Pi had a million users. So why did Inflection just implode?" https://sectionai.com/blog/what-happened-to-inflection/

[136] Brian Solis. "AInsights: Microsoft's Pseudo-Acquisition of Inflection AI." April 2024. https://briansolis.com

[137] Skywork AI. "Mem0 for OpenClaw: The Definitive 2026 Guide." https://skywork.ai/skypage/en/mem0-openclaw-fixing-ai-agent-amnesia/
[138] Character.AI Support. "New Feature: Pinned Memories." March 2024. https://support.character.ai/hc/en-us/articles/24327914463003
