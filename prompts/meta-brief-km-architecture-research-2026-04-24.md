---
title: Meta-Brief — Knowledge Management + Project Management Architecture Research (swarm deep prompt) [v2 — post-BIOS-research revision]
date: 2026-04-24
revision: v2 (added UC-9 client-isolation + UC-10 offline-first inference as MANDATORY acceptance criteria, triggered by Strategic Insight 2026-04-24 AI-BIOS moment)
type: meta-brief
author: Cloud Cowork (short brief; deep prompt to be written by Claude Code on server)
target_executor_this_pass: Claude Code on server (writes the deep execution prompt for the swarm)
target_executor_next_pass: Phase A ROY swarm (brigadier + 5 domain experts, matrix 5×4) — researches and produces 3 fully-viable variants per layer
output_this_pass: prompts/km-architecture-research-2026-04-XX.md (deep execution prompt, 1500-2500 lines, 1000% depth)
output_next_pass: decisions/KM-ARCHITECTURE-VARIANTS-2026-04-XX.md (3 × wiki variants + 3 × project-mgmt variants + integration spec)
estimated_duration_this_pass: 1-2h (prompt-writing only)
estimated_duration_next_pass: 4-8h swarm work (one M-class structural task per HD-02 Option A budget)
precedes: ruslan-review → selection of preferred variant → materialization task
relates_to:
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md (§1 C-1 topic-wiki / C-2 project-wiki / C-3 memory-map)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (v2 addition — local-first client-private KB positioning)
  - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md (v2 addition — trigger research)
  - memory/project_jetix_private_library_knowledge_leverage.md (moat philosophy)
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (existing wiki v3 infrastructure)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (5 alphas + expert allocation)
locked_decisions_referenced: [D13 closed-core/open-surface, D17 filesystem-SoT, D19 $1T trajectory, D20 USB-C, D21 matchmaker+roy, D24 open-source research, W-5 Two-level CE, HD-02 M-class N=2]
new_non_negotiables_v2:
  - "UC-9 client-isolation as mandatory acceptance criterion (architectural proof required)"
  - "UC-10 offline-first inference as mandatory acceptance criterion (local distilled LLM path required)"
  - "Every variant must support local-first client-private KB OR be dropped"
m_class_budget_impact: 1 structural M-task (this research); leaves 1 M-slot for companion measurement task in same cycle if needed
---

# META-BRIEF — Knowledge Management + Project Management Architecture Research

## §0 Your task in THIS session

Write a **deep, long, research-grounded execution prompt** (1500-2500 lines) that the Phase A ROY swarm (brigadier + 5 domain experts, matrix 5×4) will execute in a **next dedicated swarm cycle**. The swarm's output will be a decision document proposing **3 fully-viable variants** for each of two tightly-integrated layers:

- **Layer A — Wiki / Knowledge Management architecture** (how knowledge accumulates, self-reinforces, gets retrieved)
- **Layer B — Project Management architecture** (how 8 active Jetix projects are tracked, spawned, reviewed, cross-leveraged)

**You are NOT designing the architecture yourself in this session.** You are writing the prompt which the swarm will use. Stop after the deep prompt is committed + pushed.

**Output path:** `prompts/km-architecture-research-2026-04-<XX>.md`

## §1 Why this split

Per Ruslan's durable rule 2026-04-23 (`feedback_cc_writes_own_deep_prompts.md`): Cloud Cowork specifies short briefs; Claude Code on server (1M context, sub-agents, full repo access) writes the deep prompts. Then a fresh swarm cycle executes. This meta-brief is the short brief.

## §2 Ruslan's vision — non-negotiable kernel to propagate

> **Knowledge-as-leverage is Jetix's primary competitive moat.** (memory: `project_jetix_private_library_knowledge_leverage.md`)
> The architecture you design must make Jetix **accumulate advantage month-over-month** through compounding knowledge. AI on garbage = garbage; Jetix on curated + self-reinforcing KB = 10× leverage. Every decision in variant design is scored against: *does this compound, or does this decay?*

**Five core demands Ruslan voiced (2026-04-24):**

1. **Ingestion pipeline that learns.** Feed wiki a YouTube video / article / paper → it transcribes, extracts, categorizes, links. Not one-off summary: persistent structured knowledge.
2. **Query-driven retrieval patterns (at least 3 canonical queries must work day-1):**
   - *"Что нового было за неделю?"* — weekly-digest query across any niche
   - *"Как мы можем решить конкретно этот X используя wiki?"* — application/solve query
   - *"Что мы знаем про Y?"* — topic-summary query
3. **Agent skill accumulation.** Every time an agent (or brigadier) **solves something well**, the skill / pattern / insight writes itself back to wiki. Long-term memory that enables "the system gets smarter monthly, not just per-cycle".
4. **Optimized memory substrate.** Not naive markdown pile; not bloated enterprise DB. **Right-sized** — fast retrieval, persistent provenance, decay-resistant, survives 10× scale (pre-€1M architecture must accommodate €1T — D19 locked).
5. **Self-reinforcing generation.** Wiki is input AND output: insights emerge from cross-links, answer-chains, compound queries. Agents discover patterns they didn't explicitly write.

**SIXTH demand added 2026-04-24 post-BIOS-clone-wars research (see `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`):**

6. **Local-first, client-private architecture mandatory.** The KM architecture is not just Jetix-internal — it IS the template we will deploy per client. Each client's KB lives on their infrastructure. Their data never enters Jetix central pool. Their AI archivist runs on their server (locally-distilled LLM). Jetix methodology is pushed to them as versioned updates, their data is not pulled back. This is non-negotiable positioning: business clients reject AI because of data-leak fear; Jetix's answer is architectural, not policy-based. Every variant MUST demonstrably support client-isolation (UC-9) and offline-first inference (UC-10) or be dropped.

**Ruslan's explicit quality bar:** *«должны сделать работу тоже ёбнутую мощную на всю тысячу процентов глубокую»*. No "good enough". 3 variants must each be independently viable at 100%. Ruslan picks one (or hybrid) and ships to reality. The deep prompt must set this bar explicitly in §1 Mission framing.

## §3 Scope — Two layers, one coherent task

### Layer A — Wiki / Knowledge Management Architecture

The swarm must design (and the deep prompt must demand) 3 full variants of HOW knowledge is:

- **Structured** — entity types, edge types, layer hierarchy, granularity rules
- **Ingested** — video/article/book → structured notes → wiki entries (pipelines, automation triggers, dedup)
- **Retrieved** — query types, retrieval latency, retrieval precision, how agents use wiki in-session
- **Accumulated** — agent skills, insights, emergent patterns write back to wiki (compound loop)
- **Self-reinforced** — cross-links, contradiction detection, claim-updating when new evidence arrives
- **Refreshed** — curated-book reading cadence, expert knowledge refresh cycle
- **Scaled** — what breaks at €1M / $100M / $1T, upgrade paths

**Existing substrate to ENHANCE (not ignore):** `swarm/wiki/` v3 (9 layers already bootstrapped, 12 edge types, 9 entity templates, 5 alphas — see `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`). Legacy `wiki/` v2 stays untouched (D17). 393 books + curated blogs already in `raw/books-md/` = Tier-4 corpus ready for ingestion.

**Variants should differ meaningfully** — not three flavors of same design. Examples of real axis-dimensions:
- retrieval-heavy (GraphRAG-inspired, query-time assembly) vs pre-compiled-heavy (summaries, topic MoCs prebuilt)
- strict hierarchy (Левенчук ШСМ ontological) vs emergent-link (Zettelkasten / Roam-style)
- agent-owned (each expert masters own sub-wiki) vs shared-spine (one canonical wiki, agents read with niche filters)

### Layer B — Project Management Architecture

The swarm must design 3 full variants of HOW projects are managed:

- **Project onboarding** — new Jetix project → scaffold wiki + agent allocation + decision records
- **State tracking** — ICP / leads / contracts / decisions / open questions / next actions
- **Agent-per-project model** — single project brigadier? mini-swarm inside? shared experts across projects?
- **Cross-project leverage** — insight from project A informs project B (knowledge transfer)
- **Cadence** — weekly / monthly review rhythm, what gets reviewed, who reports
- **Ruslan's strategic overview** — at any moment, how does Ruslan see "all 8 projects health" without drowning
- **Lifecycle** — project pause, project kill, project pivot, project spawn
- **Linkage to Layer A** — how project-wiki reads from topic-wikis, writes back its own learnings

**Existing context:** 8 active projects per CLAUDE.md (quick-money P1 / research P2 / brand P2 / community P3 / ai-tools P2 / life-os P3 / engineering-thinking P3 / bets P4 paused).

**Variants should span operating modes** — examples of real axes:
- high-autonomy (project-brigadier runs daily, Ruslan only sees Monday digest) vs high-touch (Ruslan sees every decision gate)
- thin-scaffold (minimal structure, agent improvises) vs rich-scaffold (PMBOK-style WBS per project)
- monolithic (one wiki, projects are namespaces) vs federated (per-project independent wikis, explicit cross-refs)

### Integration requirement (non-optional)

Variants must show HOW Layer A and Layer B fit together. A wiki architecture is incomplete if it doesn't specify how project-managers-agents query topic-wikis. A project-mgmt architecture is incomplete if it can't declare what it writes back to the knowledge layer.

**One coherent output document** (not two separate docs). Each of the 6 variants must have clearly-paired Layer A + Layer B choices.

## §4 Use cases the deep prompt MUST demand each variant demonstrably support

The deep prompt must include a use-case acceptance matrix. Each variant is scored against these concrete scenarios:

1. **UC-1 Video ingest:** Ruslan shares a 45-min YouTube lecture on systems thinking → pipeline extracts → ≥5 wiki concept pages + ≥8 edges created + appears in systems-expert's training corpus + triggers "new knowledge" alert in next weekly digest
2. **UC-2 Weekly digest query:** Monday morning — *"Что нового в wiki за прошлую неделю?"* returns grouped-by-niche summary with top 5 concepts + new cross-links + emergent themes
3. **UC-3 Solve-with-wiki:** Ruslan asks *"Как применить systems-thinking к нашему outreach-процессу в DACH?"* → agent retrieves relevant concepts + synthesizes + returns with citations + writes insight back to wiki
4. **UC-4 Skill accumulation:** Brigadier successfully runs a novel task decomposition → pattern extracted + stored in `agents/brigadier/strategies.md` + queryable in next cycle as "have we done this before?"
5. **UC-5 Project onboarding:** New Jetix project direction spawned → project-wiki scaffold + mini-swarm allocation + initial ICP/thesis drafts + linked to relevant topic-wikis in <30 min
6. **UC-6 Cross-project insight:** Pattern learned in `quick-money` project (e.g. specific objection-handling) propagates to `research` project's methodology via explicit cross-project edge
7. **UC-7 Contradiction detection:** Two claims disagree (e.g. one concept says "X is essential", another derived later says "X is obsolete") → surfaced at `/lint` + Ruslan prompted to resolve
8. **UC-8 Scale test:** Variant explicitly projects behaviour at 10K wiki pages / 50 projects / 100 agents — breakage points + upgrade path per MHT horizon (€50K / €200K / €1M / $100M / $1T)
9. **UC-9 Client isolation (MANDATORY — added 2026-04-24 post-BIOS-research):** Variant must demonstrate how TWO simultaneous Jetix clients (Client-A and Client-B) running the SAME Jetix methodology + tooling on separate infrastructure CANNOT see each other's data, wiki entries, project files, agent memory, or derived insights. Architecture proof required: (a) cross-client data-leak impossible by construction (not by policy), (b) each client's KB is mountable/portable/deletable independently, (c) Jetix methodology updates can be pushed from Jetix central repo to client without pulling client's private data back. **If variant cannot architecturally prove client-isolation → drop variant, replace.** This is the foundation of Jetix's local-first / client-private KB positioning (`decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`).
10. **UC-10 Offline-first inference (MANDATORY — added 2026-04-24 post-BIOS-research):** Variant must demonstrate how a Jetix client's AI "archivist" — powered by a locally-runnable distilled model (Llama / DeepSeek / Mistral family) — answers a substantive query about the client's own data while network-disconnected from OpenAI/Anthropic/cloud APIs. Architecture proof required: (a) inference path doesn't require external API call for client-private-data queries, (b) KB retrieval protocol works against local filesystem/vectorstore, (c) response quality bar on local distilled model is measurable (not marketing claim) — variant must specify what use-case complexity tier works fully offline vs when cloud LLM augmentation becomes needed, (d) security layer controls WHAT enters the client KB (signed provenance, audit trail for every ingest). **If variant cannot architecturally support offline-first inference path → drop variant, replace.** This is the moat: OpenAI/Anthropic CANNOT replicate "your data never leaves your server" via any API upgrade.

**If a variant cannot demonstrably support all 10 use cases → variant is incomplete; swarm must iterate until it can, OR remove the variant and produce a 3rd that does.**

UC-9 + UC-10 are NOT optional extensions. They are **the architectural differentiation of Jetix vs 35K generic AI-wrapper consulting companies.** Every variant that cannot pass them is deleting Jetix's strategic position. Drop + replace > "partial support".

## §5 What the execution prompt (you write this session) must make the swarm deliver

### Per variant (×6 variants total = 3 Layer-A × 3 Layer-B with integration pairs)

- **Name + 1-line pitch + axis-of-differentiation** from other 2 variants in its layer
- **Architecture diagram** (ASCII or Mermaid in markdown)
- **Mechanics** — every mechanism spelled out (ingest pipeline, retrieval protocol, write-back protocol, refresh cadence)
- **Use-case walkthrough** — UC-1..UC-10 traced through this variant concretely (ALL 10, including client-isolation proof + offline-first inference proof)
- **Integration spec** — how paired Layer-A + Layer-B halves interact
- **Pros / cons / tradeoffs** — honest, not marketing
- **Effort estimate** — hours to bootstrap + days to reach UC-1..UC-4 live + weeks to UC-5..UC-8 stable
- **Horizon projection (MHT per gate)** — at €50K / €200K / €1M / $100M / $1T what strains, what upgrades, what breaks
- **Anti-fragility assessment** — does it get BETTER with scale (true-antifragile, like OPP-04) or just survive
- **Migration path from current state** — `swarm/wiki/` v3 already built, legacy `wiki/` v2 coexists; variant must show migration strategy
- **Open questions** — what must Ruslan decide before this variant ships

### Swarm-level deliverables (across all 6 variants)

- **Comparison matrix** — 6 variants × 8 use cases × quality-score binary (pass/partial/fail)
- **Recommendation** — brigadier's pick (may be hybrid) with dissents preserved (philosophy × integrator + systems × scalability must both sign)
- **Explicit 3 dissents preserved** minimum (per Cycle-1 epistemic hygiene pattern — no averaging)
- **Matrix 5×4 invocation trace** — all 5 experts × 4 modes fired at least once each (20 minimum cells); scalability-mode fires horizon projection on all 6 variants
- **F-G-R tagging** per claim (Formality / Scope / Reliability per JETIX-ARCHITECTURE-BRIEF D4)
- **Citations** — every major claim cites Tier-1 source (Private Library book / existing Jetix artefact / research paper); no single-author assertion without source

### Output file

Single combined document: `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-<XX>.md`

- 15-25K words
- Structured: §1 Context / §2 Method / §3-5 Layer-A variants / §6-8 Layer-B variants / §9 Integration pairs / §10 Use-case matrix / §11 Recommendation / §12 Dissents / §13 Ruslan decision packet

## §6 Critical framing to propagate into the deep prompt

Include verbatim (or equivalent-strength) in §1 Mission of the written execution prompt:

> **This research cycle is Pillar 2 + Pillar 3 of the Next Strategic Horizon (VISION-NEXT doc §2).** The variants you produce will determine how Jetix's primary competitive moat (knowledge-as-leverage) physically materializes. Shallow design = decaying moat. Deep design = compound returns for years.
>
> You are producing 3 variants PER LAYER that each work to 100% independently. Ruslan's explicit quality bar: 1000% depth. Not three flavors of the same design — three genuinely different positions in the design space so Ruslan has a real choice.
>
> Every variant must demonstrably support 8 concrete use cases (UC-1..UC-8 below). If a variant can't pass UC-1..UC-8 → drop it, produce a new one. Do not ship a "close enough" variant. Matrix 5×4 must actually fire (all 5 experts × 4 modes = 20 minimum cells). Scalability-mode must actually project horizons. Philosophy × integrator verdict + systems × scalability verdict must both appear.

## §7 Research corpus the swarm MUST use

**Mandatory reads (Tier-1):**
- `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` (existing wiki v3 design)
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` (5 alphas + expert allocation)
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (Pillars 2 + 3 kernel)
- **`decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` (MANDATORY — local-first / client-private architecture positioning — defines UC-9 + UC-10 acceptance rationale)**
- **`raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` (MANDATORY — historical parallel, 621 lines, FULL READ required — understand WHY local-first is the moat)**
- `decisions/JETIX-PHILOSOPHY.md` D2 §§6, 10, 14 (foundation-first, universality criterion, quality invariant)
- `decisions/JETIX-ARCHITECTURE-BRIEF.md` D4 (F-G-R / boundary discipline / multi-view publication)
- `raw/research/knowledge-architecture-deep-research-2026-04-19.md` (Karpathy LLM Wiki / GraphRAG / HippoRAG / MemGPT / Zettelkasten / BASB — 828 lines of prior research, FULL READ required)
- `memory/project_jetix_private_library_knowledge_leverage.md` (moat philosophy)

**Tier-4 curated reads (per expert allocation):**
- systems-expert: Левенчук ШСМ / Beer (cybernetics) / Meadows / Senge — for Layer A ontology axis
- mgmt-expert: Grove / Drucker / Cagan / PMBOK / Allen GTD / BASB — for Layer B project mgmt axis
- engineering-expert: Fowler (Extract) / Clean Code / AI-native / Karpathy LLM OS — for ingest + retrieval pipelines
- philosophy-expert: Popper / Kuhn / Munger / epistemology — for claim-validity + contradiction handling
- investor-expert: Graham / Kelly / Taleb antifragile — for MHT horizon projection + scalability verdicts

**External-domain tools to reference (not re-derive):** Zettelkasten method, Roam/Logseq graph-notes, Obsidian (backlinks), Notion (database-first), Karpathy LLM Wiki, GraphRAG (Microsoft), HippoRAG, MemGPT, BASB (Tiago Forte), Левенчук FPF, ATLAS.ti (coding), org-mode, TiddlyWiki.

## §8 Locked decisions (non-negotiable)

- **D17 Filesystem = SoT.** Wiki lives in git. Notion is mirror/view only.
- **D19 $1T trajectory.** Every variant must project through all 5 gates (€50K / €200K / €1M / $100M / $1T).
- **D24 Open-source research.** Research-direction content is eligible for future open-sourcing; methodology-direction stays closed.
- **W-5 Two-level CE.** Compound feedback loop mandatory.
- **HD-01 5-gate propagation** (cycle-2 landed).
- **HD-02 N=2 M-class per cycle.** This research = 1 M-class structural task. Leaves 1 slot for companion measurement task (e.g. M3 solo-vs-matrix, which can run same cycle).
- **24 Locks unchanged, FPF E-1..E-18 unchanged, W-1..W-12 unchanged, shared-protocols 9 sections unchanged.**
- **Legacy coexistence:** `wiki/` v2 + 14 legacy agents untouched.
- **Max-subscription discipline:** `unset ANTHROPIC_API_KEY` before launch. No paid API.

## §9 Operating mode

**Stage-Gated.** Between swarm Phase 5 (variants drafted) and Phase 6 (brigadier consolidation) — write `swarm/gates/AWAITING-APPROVAL-km-architecture-variants-<date>.md` with variant summaries. Ruslan reviews 6 variants + recommendation + preserved dissents → picks / modifies / hybrid / rejects. Only after ack → brigadier writes final consolidation + Compound step fires.

Full-Auto NOT authorized.

## §10 Anti-scope (deep prompt must enforce)

- **NO implementation** in this swarm cycle — this is research + variant design ONLY. Materialization is a separate task after Ruslan picks.
- **NO touching legacy** `wiki/` v2 or 14 legacy agents.
- **NO re-opening 24 Locks** / FPF E-items / W-decisions / shared-protocols.
- **NO collapsing to 1 variant** for expediency — 3 × 3 is the minimum; less = failure.
- **NO variant without UC-1..UC-8 demonstrable support** — drop + replace instead of "partial support" excuses.
- **NO skipping matrix 5×4 invocation** — all 20 cells minimum fire + logged.
- **NO averaging dissents** — preserve verbatim per Cycle-1 precedent.
- **NO M3 execution** in this cycle (separate task; can run parallel in same M-budget).
- **NO OPP-03/05/06 work** (Cycle-3+ queue).

## §11 What the written execution prompt should look like

- **Length:** 1500-2500 lines (this is a big research task — spec must be complete).
- **Structure:** §1 Mission + critical framing / §2 Scope (Layer A + Layer B + integration) / §3 Use-case matrix UC-1..UC-8 / §4 Per-variant deliverable template / §5 Research corpus (mandatory + curated) / §6 Matrix 5×4 invocation plan / §7 Locked decisions / §8 Operating mode + gates / §9 Anti-scope / §10 Output format / §11 Definition of done / §12 Escalation / §13 Verification checks
- **Style:** imperative, numbered, specific. Every reference to a file uses a `path/to/file.md:§N` pointer. Bash verification snippets where relevant.
- **Depth markers:** include explicit per-section word-count floors where quality matters (e.g. "Each variant architecture description: ≥1500 words") — prevent shallow shortcuts.
- **Executor-facing directive:** same 1000% depth framing as cycle-2 execution prompt (§1.3 anti-pattern catalog).

## §12 Definition of done for THIS session (Cloud Cowork brief)

1. `prompts/km-architecture-research-2026-04-<XX>.md` written, 1500-2500 lines
2. Committed to `claude/jolly-margulis-915d34` + pushed to origin
3. Brief summary reply: file path + line count + ready-to-launch command snippet + estimated swarm duration

## §13 Escalation

If while writing the execution prompt you hit:
- Contradictions between existing wiki v3 spec and Ruslan's vision voiced 2026-04-24
- Ambiguity on whether Layer A + Layer B fit one document or two
- Uncertainty on UC-1..UC-8 granularity (too vague / too prescriptive)

→ Stop, write `prompts/AMBIGUITY-km-architecture-<date>.md` with contradiction, notify via commit. Do not guess.

---

*End of meta-brief. Execute.*
