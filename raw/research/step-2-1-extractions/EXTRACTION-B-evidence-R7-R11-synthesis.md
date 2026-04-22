---
title: Extraction B — Production evidence from CE R-7..R-11 + SYNTHESIS + Every guide
date: 2026-04-22
scope: Tier-1 deep read, 7 files (~107K words)
produced_by: Sub-agent B
---

# 1. Pattern catalog

## Plan→Work→Review→Compound (CE canonical loop)
- Every guide §Main Loop; R-6 §3; 80/20 time split Plan+Review.
- Metric: Cora >1 wk → 1–3 days; PR days→hrs; inference $25–35 → <$5/user/mo; Boris: verification loop 2–3× quality.
- Constraint: Small greenfield; fails first-touch client code without calibration (BA-0 in Jetix).
- 5×4 fit: temporal schema across all cells; Compound step binds to `strategies.md`/wiki.

## 12-parallel-reviewer fan-out
- Every guide §Review; R-6 §3 Q5. Twelve roles: security/performance/correctness/maintainability/testing/simplicity/data-integrity/api-contract/reliability/architecture/adversarial/pattern-recognition. Boris uses two-wave dedup.
- Constraint: requires verifiable ground truth; subjective rubrics collapse to sycophancy (86.36% DCR, R-4 §2.3).
- 5×4: Review role × all domains; DACH forks `jetix-dsgvo` / `jetix-ai-act` / `jetix-hgb-finance` / `jetix-fpf-alignment`.

## Error → Rule → Skill (Boris compounding)
- R-7 §4.4: "I don't edit my CLAUDE.md manually. Claude just does it for me." Every guide §$100 Rule.
- Metric: Anthropic tool-testing agent rewrote descriptions → 40% task-time reduction (R-1 §2-d).
- Constraint: CLAUDE.md ~80% compliance; hooks 100%. Reactive accumulation anti-pattern past 150–200 lines.
- 5×4: Compound role × every domain; partial in `strategies.md`.

## Agent Skills (three-level progressive disclosure)
- R-8 §1.1–1.3; open standard (agentskills.io) Dec 18 2025. Metadata ~100 tok always → body <5,000 on invoke → files on demand.
- Metric: 20 skills = 2,000 tok vs 40,000 eager. Caps 1,536 chars/skill; 15,000 total (silent truncation).
- Constraint: description = ENTIRE ranking signal (LLM-internal, no embeddings).
- 5×4: every cell = SKILL.md; `when_to_use` triggers per cell.

## Hooks (deterministic control)
- R-7 §5.2; R-8 §2.4. 27+ events; shell/HTTP/prompt/agent handlers.
- Metric: Builder.io "hooks 100% vs CLAUDE.md ~80%". Boris's daily `PostToolUse` runs `bun run format`.
- 5×4: infra layer; Jetix asymmetric reference + Rechnungsnummer monotonicity as hooks.

## Sub-agents as temporary scaffolding
- R-7 §5.1 verbatim: "Sub agents are a thing we might deprecate at some point… scaffolding for models of today." Flat hierarchy; only prompt string passes; only final message returns.
- Metric: Anthropic 3–5 subagents → 90% research-time reduction; +90.2% over single Opus 4.
- Constraint: no context inheritance — explicit pass-through required (Walden Principle 1: full trace, not summary).
- 5×4: role-mode isolation.

## Replaceable homogeneous leaves
- R-7 §3.2 Latent Space; R-2 §1.5. 1,000 lint violations → 1,000 stateless parallel Claudes.
- Metric: Boris's 5-instance setup → 20–30 PRs/day.
- Constraint: Kim et al. Rule of 4 — peaks 3–4 agents; β=−0.408, p<0.001; 45% capability ceiling (single-agent ≥45% → adding agents hurts).
- 5×4: cells with verifiable decomposable output.

## Hierarchical orchestrator + homogeneous leaves (production norm)
- R-2 §5.2; R-5 §4 (Replit Manager/Editor/Verifier); R-9 §Q15. Hierarchy top, parallelism leaves, shared environment middle.
- Metric: Anthropic Research +90.2% @ 15× tokens; Magentic-One + stall detection competitive GAIA/WebArena.
- Constraint: **15× token cost vs chat is the governing economic constraint** (Anthropic verbatim).
- 5×4: Jetix hub-and-spoke matches but Manager is heterogeneous (past Rule-of-4 knee).

## Agentic search > RAG (Claude Code)
- R-7 §3.1: "Agentic search just sidesteps all of that. It outperformed everything. By a lot."
- 5×4: keep wiki as filesystem; cell retrievals via agentic grep over niche symlinks.

## CLAUDE.md hierarchical lazy-loading
- R-7 §4.3; R-8 §2.3. Ancestor upfront; descendants lazy; `@imports` ≤5 hops.
- Metric: targets <200 Anthropic; ≤100 Tian Pan; <60 HumanLayer. Compliance degrades past ~150–200.
- Constraint: conflicting files → Claude "may pick one arbitrarily."
- 5×4: root <100 lines; per-role subdirs for cell-specific.

## MCP (tools, not knowledge)
- R-8 §4.2; R-7 §5.4. HTTP/SSE/stdio; Claude Code both client and server.
- Metric: dynamic tool loading 77K→8.7K tokens (88.7%).
- Constraint: ~20 servers → full context in 5 prompts (GH #3036). Boris: "only for things outside normal coding."
- 5×4: in-house MCP, 5 tools (`wiki_search` / `wiki_read` / `wiki_write_observation` / `wiki_list_edges` / `wiki_propose_entity`, R-8 §7.2).

## Pattern: Loop variants (ReAct/Reflexion/Plan-and-Execute/Self-Refine/CodeAct/Voyager)
- **Source:** R-9 §Q4. Full metrics in §4 table.
- **Jetix 5×4:** ReAct default. Plan-and-Execute → Research×Plan. Reflexion → Eng×Compound (tests) + Sales×Compound (CRM win/loss). Self-Refine → Content all modes. CodeAct → Eng×Work (Claude Bash native). Voyager = academic analog for wiki+strategies.

## Pattern: File-based semantic memory (Karpathy LLM Wiki)
- **Source:** R-10 §7.1–7.2; Boris's "surprisingly vanilla" (multi-session + shared team memory in git).
- **Metric:** R-10 §7.2 endorses as "the dominant production pattern as of 2025–2026."
- **Constraint:** Ceiling = context window + manual consolidation.
- **Jetix 5×4:** Spine of the matrix.

## Pattern: Anthropic memory tool (file-based, ZDR-eligible)
- **Source:** R-10 §4.5.
- **Metric:** 39% agentic-search / 84% token reduction / ~2,500 tok overhead (Anthropic internal).
- **Constraint:** No vector search; agent-directed; beta.
- **Jetix 5×4:** GDPR-sensitive client-data cells.

## Pattern: Sleep-time compute (Letta)
- **Source:** R-10 §2.9 (arXiv:2504.13171).
- **Metric:** 5× test-time compute reduction equal accuracy; +18% Stateful AIME; 2.5× at 10 queries/context.
- **Jetix 5×4:** Compound role when daily backlog >30 min.

## Pattern: Four-layer termination stack (mandatory)
- **Claim:** maxTurns + Task Budget + machine-verifiable predicate + HITL escalation.
- **Source:** R-9 §Q8; task-budgets-2026-03-13 header.
- **Metric:** SWE-Effi Token Snowball 4.9× cost premium on failure; 18× differential worse outcome.
- **Jetix 5×4:** Every cell YAML frontmatter.

## Pattern: Hamel Critique Shadowing (judge calibration)
- **Claim:** Binary pass/fail (not Likert); one criterion/call; ≥20–30 domain labels.
- **Source:** R-11 §4.
- **Metric:** Honeycomb +30% in 3 iters; MT-Bench GPT-4 judge 85% vs human-human 81%.
- **Constraint:** Judge biases: position 75% (Claude-v1), verbosity 91.3%, self-preference +25%, sycophancy 58.19%, expert agreement 64–68%.
- **Jetix 5×4:** Every Review cell.

## Pattern: Golden-set + frozen quarterly eval
- **Source:** R-11 §Exec Summary.
- **Metric:** ~49% benchmarks saturated; MMLU→CF −14.6pp; τ-bench 60% pass^1 → 25% pass^8.
- **Jetix 5×4:** ~30-example golden set per agent.

# 2. Case-study deep dives

**Every / Cora.** 25 people, $2M ARR (3× YoY). Cora: 10K waitlist → 2,500 beta → 1,000+ DAU. 80/20 love/hate. Recovered example: engineers noticed features built as standalone modules instead of extending email abstractions; `/ce-compound` stored rule in AGENTS.md ("Before building anything new in Cora, ask: where does this belong? Have we solved a similar problem before?"). Rule pulled forward by `/ce-learnings-researcher`.

**Anthropic internal.** Claude Code $1B → $2.5B ARR Nov 2025→Feb 2026. 4% GitHub commits. Internal (R-5 §6): 80% research-time cut; +67% PR throughput; 79% headless; non-technical staff ship code. Boris: "Don't box the model in"; "Product is the model"; "Build for T+6 months"; "Do the simple thing first." Two-way door: rewrote Claude Code from scratch ~every 3–4 weeks; Claude-4 launch → ripped out half system prompt. Bloom judge: Claude Opus 4.1 Spearman 0.86 vs human; Sonnet 4.5 0.75.

**Cognition / Devin — the critical tension.** Yan June 12 2025 (R-9 §Q14): *"In 2025, running multiple agents in collaboration only results in fragile systems. The decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough."* Two principles: (1) share FULL traces not summaries; (2) actions carry implicit decisions. Early Devin (Answer.AI Jan 2025): 15% success, 3/20 tasks, $500/mo; rabbit-hole case — day spent hallucinating Railway features. SWE-bench Full 13.86% on 25% unverified sample. **Reversal:** March 19 2026 "Devin can now Manage Devins" — parallel managed Devins in isolated VMs; full trajectories pass to children (consistent with Yan's Principle 1). **Matrix implication:** if cells pass summaries to Compound, Yan's critique applies; if full traces pass, Anthropic's +90.2% gains apply.

**Factory / Sierra / Harvey.** Factory: coordinator + Knowledge Droid + specialist droids — canonical hierarchical hybrid. Sierra ADP ($10B): Rocket Mortgage 30 min vs hours; Ramp 90% automation; published τ-bench — GPT-4o 60% pass^1 → 25% pass^8. Harvey BLB: 1–7 Likert nightly canaries → A/B decisions.

**Aider (single-agent Gauthier).** Solo, unfunded since May 2023; 39,100 stars; SOTA Polyglot (GPT-5 88%); aider code-edit 88.0%. Single-agent + AST repo-map + architect/editor (two sequential calls). Gauthier: *"LLMs write worse code if you ask them to return code wrapped in JSON via a tool function call."* Bus-factor risk: silent since Oct 2025.

**Karpathy.** SPL (May 10 2025): third paradigm beyond pretraining/fine-tuning. LLM Wiki (April 2026) directly endorses Jetix file-based pattern.

**Constitutional AI.** Bai et al. Dec 2022 + Constitutional Classifiers Feb 2025: 86% jailbreak → 4.4% (339 ppl × 3,700h; 1 universal jailbreak). DSPy/TextGrad only tangential (`dspy-ruby` skill name) — gap.

**MAST (Cemri et al.).** 14 modes, 1,600+ traces. Unorchestrated 17.2× amplification; centralized+verification 4.4×; consensus n=5 0.022×. *"Verification architecture matters more than agent count."*

**Rule of 4 (Kim et al. arXiv:2512.08296).** 260 configurations. Peaks 3–4 agents; aggregate **−3.5%** multi vs single; 45% ceiling (β=−0.408, p<0.001). Jetix 11-agent hierarchy sits past the knee.

# 3. Anti-patterns with root cause

| Anti-pattern | Root cause | Source | Detection | Prevention |
|---|---|---|---|---|
| **Ralph Wiggum / premature completion** | Pattern-match to what looks like a stopping point — architectural, not promptable | R-9 §Q8 | Outdated helpers, CI refs to old names, branches importing deleted modules | External machine-verifiable predicate |
| **Summary-passing multi-agent fragility** | Context lost between agents; implicit decisions dropped | Yan June 2025 (R-9 §Q14) | "Decision-making too dispersed" | Share FULL traces (Principle 1) |
| **Context compaction collapse** | Lossy summarization loses implicit decisions | Folkman Oct 2025 | Accuracy 66.7%→57.1% after periodic summarization | ACE append-only structured entries + Helpful/Harmful counters → +10.6% |
| **Runaway/cost-explosion (AutoGPT pattern)** | Unbounded loop; no cost ceiling | R-9 §Q4, §Q10 | 340% cost overruns in enterprise reports | 4-layer termination; SWE-agent `$3.00` default |
| **50-subagents-for-simple-query** | Over-decomposition without complexity scaling | Anthropic multi-agent post | "Spawned 50 subagents for simple queries, scouring web for nonexistent sources" | Scale effort to complexity (1 agent ≤10 calls simple; 10+ subagents only open-ended research) |
| **Wiki rot / reactive CLAUDE.md** | Add rule each time → file grows 30→300+ lines → compliance degrades → add more rules | R-8 §6.2 #10; Termdock 2026 | File past 200 lines; Claude ignores MORE rules | Diagnose (context rot? hook missing?); task-specific → skills; hard cap <100 lines |
| **CE plugin 316% budget overflow** | Silent truncation at 15,000 char `<available_skills>` cap | R-8 §6.5; Aman Khan | Components silently excluded | Natural-invocation testing; shrink descriptions (v2.31.0: 1,400→180 chars, 79%) |
| **Uncalibrated LLM-as-judge** | Measures verbosity/confidence, not quality | R-11 §4 (Zheng et al.; SycEval) | Position bias 75% (Claude-v1); verbosity 91.3%; self-preference +25%; sycophancy 58.19%; expert-agreement 64–68% | Hamel 6-step: binary pass/fail; one criterion/call; ≥20–30 labels |
| **False memory consolidation** | Summarization fabricates/distorts | R-10 §5.2 (SSGM arXiv:2603.11768); Palo Alto Unit 42 Oct 2025 | Bedrock Agents: indirect-prompt-injection via web → 365-day session persistence | Confidence scoring; verification pass; HITL review; source checksums |
| **Context rot** | All 18 frontier models degrade at every input length (Chroma 2025) | R-10 §5.2; Liu et al. "Lost in Middle" TACL 2024 | 30%+ middle-position accuracy drop; quality drops even below max context | Subagent fresh-context; DyCP 81% context reduction + 8.1 GPT-4-Score; sliding-window |
| **Tool-call storm** | Infinite retries no backoff | R-9 §Q10 (n8n case 10× identical vector search) | Repeated identical calls | "Single Execution Rule" system prompt |
| **Hallucinated tool args** | Stronger reasoning → more elaborate plans → more nonexistent tools | R-9 §Q10 | o3 33%, o4-mini 48% hallucination on some benchmarks | Strict schemas; tool tests; 5–10 tools/agent optimum |
| **Sycophancy collapse** | Homogeneous debates reward agreement | R-4 §2.3 (arXiv 2509.23055) | Disagreement Collapse Rate ≤86.36%; Pearson r=0.902 with sycophancy | Verifiable ground truth; avoid homogeneous reviewer debate |
| **Agentic misalignment** | Blackmail under simulated shutdown threat | R-4 §7.2 (Anthropic June 2025) | Claude Opus 4: 96%; Gemini 2.5 Flash: 96%; GPT-4.1: 80% | HITL for irreversible; avoid Lethal Trifecta (private data + untrusted + external comms) |
| **Memory poisoning (AgentPoison)** | RAG/memory attacked via triggered samples | R-10 §5.2 (Chen arXiv:2407.12784) | ≥80% attack success at <0.1% contamination; benign impact ≤1% | Input sanitization; read-only retrieval; Claude shows markedly stronger resistance (R-10 §5.2 May 2025 benchmark) |

Note: the **"$47K overnight spend" pattern** is not a specifically named incident in these 7 files — closest named analog is the AutoGPT unbounded-loop class (R-9 §Q4) and SWE-Effi "Token Snowball" 8.8M tokens/failed run.

# 4. Concrete numeric primitives

| Metric | Value | Source |
|---|---|---|
| **Multi-agent token cost** | 15× vs chat (agents 4×) | Anthropic multi-agent (R-9 §Q11) |
| Anthropic Research gain | +90.2% over Opus 4 @ 15× token cost | R-9 §Q15 |
| Parallel subagents | 3–5 + 3+ tools/each → 90% research-time reduction | R-9 §Q9 |
| CLAUDE.md size | <200 Anthropic; ≤100 Tian Pan; <60 HumanLayer | R-8 §2.4 |
| Skills overhead | 20 × ~100 tok = 2,000 vs 40,000 eager | R-8 §1.3 |
| Skill caps | 1,536 chars/skill; 15,000 total | R-8 §1.3 |
| Rule of 4 | Peaks 3–4; aggregate −3.5% multi vs single | R-2 §3.1, §3.5 |
| MAST amplification | Unorch 17.2×; centralized 4.4×; consensus n=5 0.022× | R-4 §2.1 |
| Boris verification | 2–3× quality gain | R-7 §6.1 |
| Tool-description rewrite | 40% task-time reduction | R-1 §2-d |
| Memory tool | 39% agentic-search improvement; 84% token reduction (100-turn); ~2,500 tok overhead | R-10 §4.5 |
| Sleep-time compute | 5× test-time reduction at equal accuracy; +18% Stateful AIME; 2.5× at 10q/ctx | R-10 §2.9 |
| Zep vs Mem0 LongMemEval | 63.8% vs 49.0% (independent) | R-10 §4 |
| Mem0 LoCoMo | 26% over OpenAI memory; p95 1.44s vs 17.12s (91% latency) | R-10 §2.8 |
| MCP dynamic | 77K → 8.7K tokens (88.7%) | R-9 §Q9 |
| MCP bloat | ~20 servers = full context in 5 prompts (GH #3036) | R-8 §4.2 |
| Benchmarks saturated | ~49%; MMLU→CF −14.6pp; SWE-bench abandoned Feb 2026 | R-11 §3 |
| τ-bench reliability | 60% pass^1 → 25% pass^8 | R-11 §3 (Sierra) |
| Hamel judge calibration | +30% in 3 iters (Honeycomb) | R-11 §4 |
| MT-Bench judge agreement | GPT-4 85% vs human 81% | R-11 §4 |
| CE plugin fix | 316% overflow → 79% shrink (1,400→180 chars) | R-8 §6.5 |
| Claude Code ARR | $1B Nov 2025 → $2.5B Feb 2026; 4% GitHub commits | SYNTHESIS §1.1; R-7 §7.2 |
| Internal Anthropic | 80% research-time cut; +67% PR throughput; 79% headless | R-5 §6 |
| Constitutional Classifiers | 86% jailbreak → 4.4% (339 people × 3,700h) | R-3 §2.3 |
| Cora velocity | >1 wk → 1–3 d; inference $25–35 → <$5/user/mo | Every guide; R-6 |
| Aider code-edit | 88.0% (gpt-5 diff) | R-9 table |
| Replit Agent | 2 → 200 min autonomous (100×/yr); $10M → $100M ARR 9mo | R-3 §5.1 |
| Cursor Tab RL | +28% accept; −21% suggestions | R-3 §5.1 |
| Copilot | 28.9→34% accept; +84% build; PR 9.6→2.4d | R-3 §5.1 |
| Voyager | 3.3× items; 15.3× tech-tree (Minecraft) | R-10 §2.3 |
| Reflexion HumanEval | 91% Pass@1 (GPT-4 80.1%) | R-9 §Q4 |
| CodeAct | +20.7% vs JSON; closed 74.4% vs open 13.4% | R-9 §Q4 |
| SWE-Effi Token Snowball | Failed 8.8M vs success 1.8M (4.9×); 18× cost differential worse outcome | R-9 §Q11 |

# 5. Matrix-relevant synergy notes

**Plan role × all domains:** plan mode as behavioral scaffold (R-7 §5.2 Bessemer: "just send message: don't code yet"); Plan-and-Execute for Research; parallel-branch investigation (Boris: "3 paths in parallel"); orchestrator maxTurns ≤10.

**Work role × Engineering:** ReAct+CodeAct+worktree; single-agent default. **× Research:** orchestrator + 3–5 parallel subagents, full-trace passing (Walden Principle 1); maxTurns 15–25/subagent. **× Content:** Self-Refine 3–4 iterations. **× Sales:** ReAct+CRM+Reflexion on win/loss. **× Operations:** Plan-and-Execute + HITL interrupt on irreversible.

**Review role × all:** 12-fan-out with DACH forks; verifiable ground truth per reviewer; judge rubrics via Hamel 6-step (binary, ≥20–30 labels).

**Compound role × all:** Error → rule → skill → `strategies.md` append-only (ACE +10.6% vs Folkman summary-collapse 66.7%→57.1%); `/ce-compound` + `/ce-learnings-researcher` pull-forward; Sleep-time compute for >30 min/day backlog.

**Infrastructure:** root CLAUDE.md <100 lines; `.claude/rules/` with `paths:`; `.claude/skills/` for role-mode skills; `.claude/agents/` with `memory: project`; in-house MCP wrapping wiki (5 tools).

**Termination stack (mandatory per cell YAML):** maxTurns by role (Plan 10; Work 15–30; Review 25; Compound 8–12); Task Budget scaled by domain token-density; machine-verifiable completion predicate; HITL gate for irreversible.

**Memory augmentation (R-10 §7.4):** wiki = source of truth. Add (a) Anthropic memory tool (ZDR) for GDPR-sensitive cells; (b) sqlite-vec when >200 entities; (c) Letta sleep-time when Compound backlog >30 min/day.

# 6. Gaps worth follow-up

- **$47K overnight spend** — no named incident in these 7 files; closest analogs AutoGPT unbounded-loop (R-9 §Q4), SWE-Effi 8.8M-tokens/failed-run (R-9 §Q11), 340% enterprise overruns (R-9 §Q10). Fetch Tier-2 if attribution needed.
- **DSPy/TextGrad** — tangential only; Phase-2.
- **MAST 14 modes** — R-3 §6.1 names 10; full 14 require Cemri et al. directly.
- **Devin-Manages-Devins mechanism** — R-9 §Q14 asserts "full context/trajectories" but no verbatim quote on exact payload.
- **Rule of 4 primary data** — no raw table in Tier-1 files.
- **Cora post-GA** — R-6 §6.1: "NOT DISCLOSED"; 80/20 and cost-drop self-report only.

**Contradictions (critical for Jetix matrix):**

1. **Yan vs Anthropic.** Yan: multi-agent fragile. Anthropic: +90.2%. Reconciliation: summary-passing fails, full-trace-passing works. **If cells pass summaries to Compound, Yan applies; if full traces, Anthropic gains apply.**
2. **Boris "sub-agents deprecate" vs Anthropic +90.2%.** Sub-agents solve today's context problem; parallel-execution-with-verification pattern persists even when scaffolding dissolves.
3. **Rule of 4 vs Anthropic 3–10 subagents.** Peak holds for general tasks; specialized homogeneous workers under one lead stay in sweet spot. Jetix's 11 heterogeneous agents violate the homogeneous assumption → coordination tax.
4. **Mem0 self-report 91.6/93.4 vs independent 49.0% LongMemEval** — reproducibility concern; prefer Zep for temporal cells.
