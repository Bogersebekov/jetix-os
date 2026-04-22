---
title: "Sub-agent D extraction — baseline from master synthesis + ROY"
date: 2026-04-23
sources: [MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md, ROY-ALIGNMENT-2026-04-22.md, ROY-BUILD-LOGIC-2026-04-23.md]
pipeline: ingested
---

# Sub-agent D — Baseline Extraction (FPF Enhancement Scan, Step 2.2.2)

Purpose: establish verbatim baseline (what exists today) so the main agent can
scan for FPF-style enhancements. No enhancement proposals here — extraction only.

Abbreviations used: **MS** = MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md;
**ALIGN** = ROY-ALIGNMENT-2026-04-22.md; **BUILD** = ROY-BUILD-LOGIC-2026-04-23.md.

---

## Part 1 — Brigadier 11-section skeleton (MS §5.1.1)

File: `agents/brigadier/system.md`. Target length 1,500–2,000 lines (MS §5.1
header, ALIGN §5 envelope). Brigadier sits OUTSIDE the 5×4 matrix (MS §4.4; §5.1).

1. **§1 Identity + mission (50–80 lines)** — Jetix-swarm orchestrator, 5 experts
   × 4 role-modes = 20 cells, no domain expertise, serves Ruslan, external-facing
   actions require HITL.
2. **§2 Task intake protocol (200–250 lines)** — Read incoming tasks, Phase
   A/B/C classification (ALIGN §9), Stage-Gated vs Full-Auto (§4.8), Grove-TRM
   task-class (EXT-D §2), acceptance-predicate requirement (AP-25), refusal +
   routing-back template.
3. **§3 Decomposition protocol (250–300 lines)** — CE wall-clock 40/10/40/10
   (Every guide; NOT turn budget), matrix-cell selection rules (§4.7.2),
   complexity-to-fan-out (simple ≤10 = single; comparison 2–4; open-ended
   10+ capped 20; >20 = sub-cycle), nested §5.1.3 task-shape → cell-selection
   matrix (design / review / optimize / scale-project) with default /
   optional / forbidden cells.
4. **§4 Invocation protocol (200–300 lines)** — `Task()` template (§5.3);
   file-reference-only rule (wiki, never inline); log to
   `comms/mailboxes/brigadier.jsonl`; parallel invocation rules with integrator
   consolidation (AP-23).
5. **§5 Reception + integration protocol (250–300 lines)** — Read each cell's
   full artefact; conflict resolution via `<domain> × integrator`;
   dissent-preservation (AP-6 — dissents surfaced, not averaged); output schema
   `wiki/drafts/<task-id>-integrated.md`.
6. **§6 Gate-check protocol (150–200 lines)** — Trigger list (ALIGN §8);
   AWAITING-APPROVAL template (§5.3.3); commit-push-pause; four-response handling
   (Approve / Redirect / Drill-down / Abort); resume procedure.
7. **§7 Compound protocol (150–200 lines)** — Error→Rule extraction;
   strategies.md write (ACE append-only, §5.5); skill promotion (§5.10);
   provenance requirement.
8. **§8 Termination-stack enforcement (150 lines)** — maxTurns per role (§5.4);
   Max-turn budget; verifier requirement; HITL trigger list.
9. **§9 Cycle reporting (80–120 lines)** — `logs/<YYYY-MM-DD>-cycle-<N>.md`
   schema; Notion mirror one-way, opt-in, optional Phase A.
10. **§10 Shared protocols (100–150 lines; same across all agents)** — Write
    to wiki (§5.5 provenance); structured output (§5.3); HITL request; reference
    other cell's output; tool-permission self-check.
11. **§11 Anti-pattern awareness (100–150 lines)** — AP-1..AP-26 (Part 3)
    trigger signals; on detection (pause / escalate / integrate).

**Plus §5.1.2 "Canonical quotes loaded":** ~15–20 verbatim quotes (Boris Cherny,
Grove, Cagan, Yan, MAST synthesis, Netflix) embedded in brigadier prompt.

---

## Part 2 — Domain-expert 9-section skeleton (MS §5.2.1)

File: `agents/<expert>/system.md` (one per expert, ×5). Target length 1,500–3,000
lines (ALIGN §5). MS §5.2 explicitly flags length as a **gate-2 risk** — the
1,500–3,000 directive is unattested in Tier-1 and cuts against shorter-is-better
evidence; compression to 800–1,500 lines is a prime Phase-B calibration target
(MS §5.2 header caveat).

### Canonical 9-section structure (verbatim titles; inputs/outputs noted)

1. **§1 Identity + canonical domain (80–120 lines)** — Declare expert as
   `<domain>`-expert; canonical source list verbatim from ALIGN §2; what expert
   OWNS (first-sources, primary frameworks, decision heuristics); what expert
   does NOT own (redirect cross-domain to other experts via brigadier).
   *Inputs:* ALIGN §2 per-expert table. *Outputs:* mission + scope-boundary.

2. **§2 Primary domain knowledge (800–1,200 lines)** — Framework 1..N (deep);
   decision heuristics; canonical quotes (verbatim, sourced); known failure
   modes; cross-reference table to other experts.
   *Inputs:* Phase-A strategies distillation from Tier 1+2+3 (MS §5.2.3).
   *Outputs:* domain-knowledge body + cross-ref map.

3. **§3 Mode: critic (300–500 lines, `mode=="critic"`)** — Activation check
   (first instruction reads `mode`; if not "critic", skip to §7); adversarial
   rubric (Hamel-calibrated binary criteria); failure-pattern library
   (domain-specific from §2 + MAST + AP-1..26); 3–5 few-shot critic outputs;
   escalation conditions (when defers to HITL).
   *Output schema:* `{context, critique, specific-failures-found,
   recommended-changes, acceptance-test}`.

4. **§4 Mode: optimizer (300–500 lines, `mode=="optimizer"`)** — Activation
   check; optimization rubric (measurable delta: turns, tokens, complexity,
   LoC); simplification heuristics (Ousterhout deep-modules / Boris
   do-simple-thing / Poppendieck waste-elimination); 3–5 few-shot outputs;
   refusal conditions (e.g., "cannot optimize design lacking acceptance
   criteria — defer to critic").
   *Output schema:* `{baseline, proposed, delta, justification, risks}`.

5. **§5 Mode: integrator (300–500 lines, `mode=="integrator"`)** — Activation
   check; integration rubric (all inputs accounted for; dissents surfaced;
   synthesis verifiable); synthesis heuristics (Cagan vision-strategy-tactics;
   Senge 11 laws; Anthropic Orchestrator-Workers); 3–5 few-shot outputs;
   dissent-preservation protocol (AP-6).
   *Output schema:* `{inputs, synthesis, dissents-flagged,
   residual-open-questions, recommended-next-step}`.

6. **§6 Mode: scalability-architect (300–500 lines, `mode=="scalability"`)** —
   Activation check; scalability rubric (≤30% refactor per 10× gate per Brief
   §5.1; antifragility check; degraded-mode spec); long-horizon heuristics
   (West scaling laws; Beer VSM recursion; Taleb via-negativa); 3–5 few-shot
   outputs; horizon-projection template (€50K → €200K → €1M → $100M → $1T).
   *Output schema:* `{horizon, projection, gate-risk-table, degraded-mode-spec,
   antifragility-check}`.

7. **§7 Shared protocols (150–200 lines, always active)** — Write to wiki
   (§5.5); return structured output (§5.3); request HITL escalation; reference
   other cell's output; tool-permission self-check (§5.7).
   *Inputs:* §5.5 wiki protocol, §5.3 schemas, §5.7 tool matrix.

8. **§8 Anti-pattern awareness (100–150 lines)** — Domain-specific anti-patterns
   from §2; cross-cutting AP-1..AP-26 briefs; what to emit on detection.
   *Inputs:* Part 3 catalog.

9. **§9 strategies.md reading protocol (30–50 lines)** — On every invocation,
   read `agents/<expert>/strategies.md` first; prioritise rules with highest
   ✓/✗ ratio; ignore retired (tombstoned) rules.
   *Inputs:* per-expert strategies.md (ACE-style ledger).

### §5.2.2 Mode activation mechanic (the gate)

First body instruction: if `mode` not set → default "integrator"; read only
§1–§2 + matching mode + §7–§9; skip other modes. MS flags this as "a
prompt-level soft constraint, not an enforceable gate" (AP-5). Phase-A adopts
**Option A**: UserPromptSubmit hook (§5.6.4) refuses expert launch if prompt
lacks `[mode: …]` prefix (brigadier always generates prefix; malformed prompt
rejected at tool layer). Option B (separate mode files per expert) rejected
(canonical-source duplication). Drift monitoring: §7 rejects mixed-mode
outputs; Hamel golden set per mode (Part 6 §6.3); Compound step writes
mode-confusion rules to strategies.md.

---

## Part 3 — Per-expert canonical-source allocation (MS §5.2.3)

§5.2.3 exists and is titled "Per-expert canonical-source allocation". It
reproduces ALIGN §2 with EXT-D §5 mapping. Source-corpus sizes are not enumerated
per expert in §5.2.3 itself; the ALIGN §2 table (Part 4 below) is verbatim. MS
§4.6 "Private Library integration (Phase B fuel)" explicitly states Tier-4 books
are Phase B reading — experts do NOT read them in Phase A (MS §4.6; ALIGN §9).

Table format (MS §5.2.3 verbatim, abbreviated):

| Expert | Phase-A first-sources | Phase-B Tier-4 reading | Scope (ALIGN §2) |
|---|---|---|---|
| **engineering-expert** | CE research (R-1..R-11 + SYNTHESIS + Every guide); Perplexity AI-native (Cursor, Factory, Replit, Aider); Karpathy LLM Wiki source card | Ousterhout, Brooks, Fowler, Martin, Hunt/Thomas, Raymond (TAoUP), Kernighan/Pike, Boris Cherny, Anthropic eng blog, Aider blog, Shape Up (shared) | CE + clean code + unix + AI-native + architecture |
| **mgmt-expert** | Phase-2 RESULT-05/06/07 (PM + Product + Mgmt philosophy) | Cagan (Inspired/Empowered/Transformed), Torres, Grove (HOM + OTPS), Drucker, Laloux, Horowitz, Netflix Culture, 37signals, Watkins 90 Days, Ries, Christensen JTBD | PM + Project Mgmt + management philosophy |
| **systems-expert** | Perplexity AI-native systems; FPF + Levenchuk corpus | Meadows, Senge, Ashby, Beer (Brain + Heart), Wiener, Kelly, Kauffman, Mitchell, Beinhocker, Holland, Dawkins, Dennett, Maynard Smith/Szathmáry | systems + cybernetics + complexity + biology |
| **philosophy-expert** | RESULT-07 mgmt-philosophy subset; FPF epistemology | Popper (LoSD + C&R), Kuhn, Lakatos, Feyerabend, Naval, Aurelius/Epictetus, Munger (shared), Koen, Vincenti, Petroski, Altshuller TRIZ | philosophy of science + mental models + stoic + epistemology + engineering foundations |
| **investor-expert** | RESULT-07 Holdco doctrine; Perplexity unit-econ; Brief financial constraints | Buffett letters 1977–present, Graham, Marks, Fisher, Munger (shared), Taleb (Antifragile + SitG), Poundstone | investing + value creation + capital allocation + long-term compounding |

**Corpus-size note.** ALIGN §12 references "Jetix Private Library 393 books"
(domain-filtered) as global pool; per-expert sizes NOT enumerated in §5.2.3
or ALIGN §2. MS §4.6.2 specifies "pool-first-query-second protocol" but no
book-count quotas.

---

## Part 4 — 5 domain-experts roster (ALIGN §2, verbatim)

ALIGN §2 "Domain expertise — 5 merged experts". Title: "5 domain experts (base)
+ brigadier = 6 agents total" (ALIGN §1). "Не 9, не 10 как separate agents.
5 мёрджед мега-экспертов обладают функциональным overlap с 9-expert handoff
варианта, но без dilution" (ALIGN §1).

| Agent | Primary domain (verbatim) |
|---|---|
| **engineering-expert** | Compounding Engineering + clean code + unix + AI-native + architecture |
| **mgmt-expert** | Product Management + Project Management + management philosophy |
| **systems-expert** | Systems thinking + cybernetics + complexity + biology/evolution |
| **philosophy-expert** | Philosophy of science + mental models + stoic + epistemology + engineering foundations |
| **investor-expert** | Investing + value creation + capital allocation + long-term compounding |

**Brigadier** is explicitly "отдельная роль вне matrix. Coordinator / task
delegator / synthesis manager. Orchestrates matrix invocations. Reads собственный
`brigadier.md` system prompt" (ALIGN §2).

---

## Part 5 — 5 × 4 matrix pattern (ALIGN §3 + MS §4.4 cross-reference)

### 4 columns (macro role-modes / activation lenses)

ALIGN §3 table (verbatim functions):

| Role-mode | Функция |
|---|---|
| **Critic** | Ищет дыры / challenges assumptions / flags weakness / adversarial lens |
| **Optimizer** | Улучшает cost / complexity / elegance / removes unnecessary |
| **Integrator** | Синтезирует куски в coherent whole / finds unifying patterns |
| **Scalability-architect** | Phase 3 / $1T defense / anti-fragility / edge cases / long-term projections |

"Каждый domain expert может быть **invoked в одном из 4 role-modes**. Не либо
domain либо role — **обе оси одновременно**" (ALIGN §3).

### Matrix operational protocol

- **Prompt implementation** (ALIGN §3): each expert prompt = Primary section
  (~800-1200 lines: domain expertise + canonical sources + frameworks +
  heuristics) + Mode-switching section (~300-500 lines × 4 modes).
- **Invocation signature** (ALIGN §3): `Task(agent: "systems-expert", mode:
  "critic"|"optimizer"|"integrator"|"scalability", context: {...})`. Agent
  reads base prompt + activates relevant mode.
- **Same deep domain knowledge per mode → no dilution.** Role-mode = framing
  lens, not separate knowledge base.
- **Parallel / composite patterns allowed:** 4 experts × 1 mode (parallel
  adversarial review); 1 expert × 4 modes (deep single-domain analysis); mixed
  (systems-critic + engineering-optimizer) for complementary lenses.
- **MS §4.12 load-bearing:** "5 × 4 = 20 cells, brigadier outside matrix,
  single-writer to wiki; same deep knowledge per mode; cells do NOT call cells
  — all routing via brigadier, all state via wiki artefacts; full traces not
  summaries (AP-1); all 4 termination layers always active; Stage-Gated default
  Phase A."
- **MS §4.5.4 cell-to-cell:** cells do NOT call cells; outputs flow cell →
  wiki artefact → brigadier reads → brigadier invokes next cell / integrator.
- **MS §4.4 cell map:** explicit 20-row table (engineering×critic through
  investor×scalability-architect) with one-line function + example invocation
  per cell.
- **Matrix rationale (MS §4.3):** rejects separate-agents-per-cell (20 agents)
  due to dilution; matrix = 5-expert depth × 20-cell breadth via
  activation-lens multiplexing.
- **Brigadier selects (domain × mode) per task-shape** via §5.1.3 table
  (design / review / optimize / scale-project).

---

## Part 6 — File location + communication (BUILD §1–§2)

### Location of agent system prompts (BUILD §1.1)

**`.claude/agents/` top-level only** (CC auto-discovery doesn't descend
subdirs; Task tool has no custom-path param). New files: `brigadier.md,
engineering-expert.md, mgmt-expert.md, systems-expert.md, philosophy-expert.md,
investor-expert.md`. 14 legacy files (manager, personal-assistant,
system-admin, sales-lead, sales-researcher, sales-outreach, inbox-processor,
crazy-agent, knowledge-synth, strategist, life-coach, meta-agent,
staging-writer, sweep-worker) remain untouched. No namespace collisions
(BUILD §1.1).

### Swarm runtime data — `swarm/` top-level (BUILD §1.2)

```
swarm/
├── README.md
├── wiki/
│   ├── tasks/<task-id>/{context, artefacts, decisions, open-questions.md}
│   ├── global/                  # accumulated compound learnings
│   ├── concepts/                # Karpathy LLM Wiki pattern
│   ├── graph/edges.jsonl        # typed relationships (GraphRAG)
│   └── _templates/
├── strategies/                  # per-expert ACE append-only memory
│   ├── brigadier.md + engineering-expert.md + mgmt-expert.md
│   └── systems-expert.md + philosophy-expert.md + investor-expert.md
├── scratchpads/<agent>.md       # ephemeral, .gitignored
├── gates/<topic>-<date>.md      # AWAITING-APPROVAL gates
├── mailboxes/<agent>.jsonl      # fallback queue (minimal Phase A)
└── logs/<cycle-id>.md           # cycle logs
```

**Alpha / strategies state files** live at `swarm/strategies/<expert>.md`
(BUILD §1.2). Compound-step outputs append here.

**Task-scoped wiki:** all task-specific state lives in
`swarm/wiki/tasks/<task-id>/...` (BUILD §4.1, conceptually approved, detailed
spec deferred to Шаг 2.2.3).

### Untouched systems (BUILD §1.3 + §5)

Explicitly NOT touched: `.claude/agents/*.md` (14 legacy), `wiki/` top-level
(existing Karpathy v2 wiki), `knowledge-base/` (migration in progress),
`decisions/ design/ raw/ prompts/ tools/`, `CLAUDE.md` + `.claude/rules/`, all
existing `.claude/skills/`, voice-notes pipeline, content pipeline, Notion
integration, MCP servers.

### Communication — 3-layer mechanics (BUILD §2)

**Layer 1 — Task tool (PRIMARY, direct) (BUILD §2.1).** Brigadier is the ONLY
caller; experts invokable only via Task. Canonical invocation spawns fresh CC
instance in isolated context; sub-agent reads `.claude/agents/<expert>.md`;
parses `Mode: <mode>` prefix → activates mode section; reads input artefact
paths; produces output artefact in wiki; returns summary (delta + verdict),
NOT full artefact. Prompt template includes: `Mode`, `Task context`, `Input
artefact`, `Canonical lens`, `Output file`, `Success predicate`, `Max turns`.

**Layer 2 — Stigmergic wiki (SHARED STATE, indirect) (BUILD §2.2).** Experts
don't talk directly; coordination via `swarm/wiki/`. Single-writer Phase A:
**only brigadier commits**; experts produce artefacts, brigadier picks up from
Task return + commits. Phase B+: CRDT/MVCC may be introduced if contention
observed (ALIGN §10). Provenance mandatory: YAML frontmatter with `source,
captured_by, captured_date, task_id, commit_sha`.

**Layer 3 — Mailbox JSONL (FALLBACK, async) (BUILD §2.3).** Per-agent JSONL
queue at `swarm/mailboxes/<agent>.jsonl`. Phase A minimised: async
notifications (post-return critical-issue flagging), HITL escalation,
cross-cycle messaging. Schema inherits from
`shared/schemas/message.schema.json`. De-emphasised (wiki handles 95%).

### Launch pattern (BUILD §3) — single-session, brigadier as entry

Single tmux session on server. Launch: `ssh → cd ~/jetix-os → git pull →
unset ANTHROPIC_API_KEY / GROQ_API_KEY → tmux new -ds roy-<task-id> →
claude --dangerously-skip-permissions`. First message pastes task + task-id +
operating mode; brigadier runs protocol (intake → decompose → invoke →
integrate → gate → compound → report). Monitoring without SSH via GitHub
commit feed. **Multi-tmux parallel rejected** (no native coordination,
Stage-Gated impossible). **Daemon mode rejected** (overkill Phase A).

### Constraints on file structure

- `.claude/agents/` flat top-level only (BUILD §1.1).
- Single-writer to `swarm/wiki/` Phase A (BUILD §2.2).
- Rollback: `rm -rf swarm/ && rm .claude/agents/{brigadier,*-expert}.md`
  (BUILD §1.4, §5).

---

## Part 7 — Gaps / weak spots in current design (flags, no proposals)

Honest read of where the 9-section skeleton feels under-specified and where MS
defers to future work. All flags cited; main agent decides whether they warrant
FPF enhancement.

1. **Prompt-length envelope unattested** (MS §5.2 header). 1,500–3,000-line
   directive explicitly "unattested in Tier-1", "cuts against evidence in §1.6"
   (shorter wins). §5.2 flags compression to 800–1,500 lines as Phase-B
   calibration target. Unresolved at Phase A.
2. **§3–§6 rubrics are structural placeholders.** §5.2.1 specifies rubric
   types but not concrete per-domain content — delegated to
   `agents/<expert>/rubrics/<mode>.md` (referenced in §5.3.1 as
   `mode_rubric_ref`). Per-domain rubric content unspecified in MS §5.
3. **Few-shot exemplars placeholder.** Every mode section says "Few-shot
   examples: 3-5 <mode> outputs" (MS §5.2.1 §3–§6). No exemplars provided;
   generation pathway not described.
4. **§8 Anti-pattern awareness is summary only** (MS §5.2.1 §8). No per-domain
   AP-mapping table; Part 3 catalog listed globally only.
5. **§9 strategies.md protocol is 30–50 lines** (MS §5.2.1 §9). Entry format,
   ✓/✗ ratio computation, tombstoning mechanism, ACE-append-only write format
   referenced (§5.5) but not fully specified inside expert skeleton.
6. **Mode activation gate is "soft"** (MS §5.2.2, AP-5). UserPromptSubmit hook
   solution exists in §5.6.4 but exact match-rule and failure messaging not
   spelled out in §5.2.
7. **Cross-reference table placeholder** (MS §5.2.1 §2). No canonical format /
   example given.
8. **Canonical quotes quantity is "author estimate"** for brigadier only
   (MS §5.1.2, ~15–20 quotes). No equivalent quota or canon for each expert's
   §2 — quote counts per expert unspecified.
9. **§5.2.3 provides sources but NOT per-expert corpus sizes.** Book counts,
   page counts, token budgets absent. ALIGN §12 references global 393-book
   Private Library; per-expert quotas unspecified.
10. **Task-shape matrix (§5.1.3) is explicit "stub"** — "minimum-viable
    deterministic guidance — prompt writers iterate on it during smoke tests
    (Part 6)". Only 4 task-shapes; hybrid / multi-shape tasks only covered
    by "combine cell sets, cap at 20".
11. **Wiki v3 task-scoped assembly deferred** (BUILD §4.4 explicit): how
    `context/` populated (manual vs HippoRAG PPR), promotion-to-global,
    retention policy, multi-task fusion, unification of Karpathy + GraphRAG +
    Zettelkasten + HippoRAG — all "TBD in Шаг 2.2.3".
12. **Mode-confusion compound writeback** (MS §5.2.2) stated at high level only;
    no concrete detection heuristic or write format.
13. **§7 Shared protocols duplicated across all 5 experts** (MS §5.2.1 §7
    "same across all agents"). Maintenance burden of syncing 5 copies not
    addressed; no "include" mechanism described.
14. **"Private-Library pool-first-query-second" (MS §4.6.2)** — Phase B
    domain-to-library mapping named but operational retrieval mechanics and
    Phase B distillation write path (`wiki/foundations/<domain>/`) only
    sketched.
15. **Length gate-2 risk threatens the section structure itself** (MS §5.2
    header). If smoke tests fail, §2 may collapse to Skill-based progressive
    disclosure — 9-section skeleton itself not stable.

---

## Part 8 — Explicit out-of-scope / deferred items (respect these)

Verbatim or citation-backed. Enhancements must not cross these boundaries.

1. **Domain-internal vocabulary of the 5 experts** (MS §1.14 clause 1):
   Ousterhout deep-modules, Ashby requisite variety, Cagan 4-risks, Popper
   falsifiability, Buffett circle-of-competence belong inside each expert's
   prompt; "loading them here would collapse the tier discipline Phase A
   enforces."
2. **Business-layer vocabulary** (MS §1.14 clause 2): ICP criteria,
   archetypes, token-model, matchmaker taxonomy — in Locks but not ontology.
3. **UI / dashboard / notifications** (MS §1.14 clause 3) — "Reserved for Phase B+."
4. **Tier-4 books in Phase A** (ALIGN §9; MS §4.6) — "Tier 4 books НЕ трогает
   в Phase A (explicit — recursive self-improvement fuel)."
5. **Phase-1 community chat (Lock 16)** — Phase B overlay (MS §4.10).
6. **Token Option B (Lock 23)** — Phase 2+ (MS §4.10).
7. **OSS research (Lock 24)** — Phase 2+ (MS §4.10).
8. **Equity / token / ownership schemas** (MS §4.11) — "No equity/token
   decisions in Phase A."
9. **Option B symmetric co-ownership; Option C/D token participation** — Phase
   2+ per Lock 23 (MS §4.11).
10. **Telegram / Notion notifications** — Phase B (MS §5.5; DIET §1.8).
11. **Roy-replication kit contents (Lock 21 full kit)** — Phase 2+ (MS §5.8.3).
12. **Render adapters for content pipeline (Lock 12)** — Phase B (MS Appendix A).
13. **CRDT / MVCC wiki writes** — Phase A single-writer only (MS §5.5.2; BUILD §2.2).
14. **Deferred skills (MS §5.10.4):** roy-replication-kit-generator, partial
    voice-memo ingestion, Telegram notifications — all Phase B+.
15. **Wiki v3 task-scoped assembly detailed spec** — "deferred to Шаг 2.2.3"
    (BUILD §4.4).
16. **Enterprise-Fast ops (Lock 20)**, **ICP archetype schema (Locks 7, 22)**,
    **Pain primary framing (Lock 9)**, **detailed content pipeline (Lock 12)**
    — all Phase B overlay (MS §4.10).

---

## Part 9 — 24 Locks (MS §4.10 + Appendix A; titles verbatim)

MS §4.10 title: "24 Locks compliance matrix (for Part 4)". Status legend:
✅ = addressed Phase A; ⚠️ = supported-but-overlay; N/A = Phase 2+.
Compliance summary: 15 ✅, 6 ⚠️, 3 N/A; no direct tension. Canonical Lock
charter lives outside MS at `raw/research/architecture-variants-2026-04-22/
TENSIONS-*.md` (ALIGN §12).

1. **Gentleman/Predator** ✅ — tiered outputs per observer; closed-core.
2. **Solo-now-team-ready** ✅ — matrix scales to multi-pilot without refactor.
3. **Closed/Open** ✅ — partner/member/public tiers explicit.
4. **Name = Jetix** ✅ — ingest hook rewrites `Jackson|Джек` → `Jetix`.
5. **Consulting-first** ✅ — brigadier prioritises quick-money P1.
6. **No advisors** ✅ — roster excludes advisor slot.
7. **Union archetypes (11)** ⚠️ — archetype metadata Phase B overlay.
8. **Layered identity** ✅ — configurable observer/phase; outputs tag frame.
9. **Pain primary** ⚠️ — pain/opportunity at overlay, not base.
10. **EN+US first** ✅ — all prompts English.
11. **Consulting+Producer+Fund** ✅ — investor-expert = fund lens.
12. **Smart+site+social-TOF** ⚠️ — detailed pipeline Phase B overlay.
13. **Open surface / Closed core** ✅ — tier enforcement in wiki.
14. **Revenue-instrumental research** ✅ — research budget revenue-gated.
15. **Revenue-gated spend** ✅ — turn-denominated budget; gates applied.
16. **Phase 1 simple chat** N/A — community agent Phase B overlay only.
17. **Filesystem = SoT** ✅ — wiki = truth; Notion one-way.
18. **Productization** ✅ — Skills = productized units.
19. **$1T Holding-Scale** ✅ — scalability-architect mode first-class.
20. **USB-C + Enterprise-Fast** ⚠️ — protocol layer explicit; enterprise-fast
    Phase B overlay.
21. **Matchmaker + Roy-Replication** ⚠️ — base replicable by construction;
    kit Phase B overlay.
22. **ICP 5-criteria + direction** ⚠️ — overlay responsibility.
23. **Token Option B** N/A — Phase 2+.
24. **OSS research** N/A — Phase 2+.

---

## Extraction notes

- MS = 3,985 lines; Part 5 spans 2714–3579. ALIGN = 285 lines. BUILD = 427 lines.
- Phase A = Tier 1+2+3; Phase B = Tier 4; Phase C = real work. Do not mix.
- Single-writer rule: brigadier ONLY commits to `swarm/wiki/` in Phase A.
- MS §5.2 self-disagrees on prompt length — watch §2–§6 expansion risk.
