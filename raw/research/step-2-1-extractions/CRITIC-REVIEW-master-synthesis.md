---
title: Adversarial critic review — master synthesis
date: 2026-04-22
role: adversarial-critic (Phase-3 review, pre-finalization)
reviewed_file: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
reviewed_word_count: ~24600
---

# Adversarial review — findings

## Executive summary

32 findings flagged: 0 SHOWSTOPPER / 6 HIGH / 15 MEDIUM / 11 LOW.

**Single most important issue.** Parts 4 and 5 use two incompatible
interpretations of CE's 40/10/40/10 time allocation. §4.7.2 and §4.9 treat it
as wall-clock allocation; §5.4.1's maxTurns table carves a per-role turn budget
that cannot reconcile with it (Plan=10 turns in 40% of cycle vs Work = 4
expert invocations @ 25-30 turns each = 100-180 turns in 10%). A prompt writer
must guess which interpretation governs.

**Gate-2 recommendation: revise-first.** Citation discipline is strong, no
SHOWSTOPPER hallucinations. But the blueprint ships with (a) two conflicting
compliance-matrix totals, (b) the turn-vs-wall-clock conflation, (c) an
unattested "closed-verification regimes" qualifier on Qian et al., (d) a
verifier signature that changes between Parts 4 and 5, and (e) an ambiguous
`Task(mode=…)` schema whose §4.5.1 presentation overstates Claude Code's
native surface. Fix before 6 system prompts are generated.

---

## Surface 1 — Citation verification

| # | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| 1.1 | MED | §1.6 / §2.3.1 "16 — DAG topology sweet spot … only in closed-verification regimes" | Qualifier NOT in EXT-A §1 term 6, §4, or EXT-B. Blueprint added a hedge the source does not make. | Drop "but only in closed-verification regimes" or cite in-corpus source. |
| 1.2 | MED | §2.1.19 + §5.1.2 "Verification architecture matters more than agent count." — attributed to Anthropic | EXT-B §2 shows the string as a synthesis summary, not an Anthropic quote. §5.1.2 loads it as an Anthropic "canonical quote." | Change §5.1.2 attribution to "[synthesis of R-4 §2.1 / MAST Cemri et al.]". |
| 1.3 | LOW | §3.4 + §1.11 "$47K (Dev.to Mar 2026, EXT-C §4)" | EXT-C confirms; EXT-B §6 flags it is NOT named in R-7..R-11. Blueprint attributes to EXT-C, which is legitimate. | Optional: add parenthetical "[unattested in R-7..R-11; Perplexity-output only]". |
| 1.4 | LOW | Walden Yan quote (§1.8, §2.2.3, §3.1) | Character-match with EXT-B §2. OK. | None. |
| 1.5 | LOW | Shipper codify quote (§1.5) | Matches EXT-A §1 term 5; elision marked with "…". OK. | None. |
| 1.6 | LOW | MAST 41.77%/36.94%/21.30%; +90.2%; 17.2×/4.4×/0.022×/96.4%; Kim et al. β=−0.408, −3.5%; 45% ceiling | All verified against EXT-A §4 and EXT-B. OK. | None. |
| 1.7 | LOW | Constitutional Classifiers 86% → 4.4% (339 × 3,700h) | Verified EXT-A §4 + EXT-B §2. OK. | None. |
| 1.8 | LOW | Cora >1wk→1-3d / $25-35→<$5 / 10K→2.5K→1K+ DAU | Verified EXT-A §2, EXT-B §1, EXT-C §1. OK. | None. |
| 1.9 | LOW | Bloom Spearman 0.86 / 0.75 | Verified EXT-B §2. OK. | None. |

**Judgement.** No load-bearing hallucinations. Two minor issues (1.1, 1.2)
worth fixing; the rest is disciplined.

---

## Surface 2 — Internal contradictions

| # | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| 2.1 | HIGH | §4.10 summary vs Appendix A | §4.10 prose: "13 ✅ / 7 ⚠️ / 4 N/A". The §4.10 *table* actually counts 15/6/3 (same as Appendix A). §4.10 prose summary is inconsistent with its own table AND Appendix A. | Change §4.10 prose to "15 / 6 / 3". |
| 2.2 | HIGH | §4.9.4 vs §5.4.3 verifier interface | §4.9.4: `fn verifier(artefact_path, rubric_path)`. §5.4.3: `fn verifier(artefact_path, rubric_path, task_context)`. Worked example drops `task_context`. | Unify to §5.4.3's three-arg. |
| 2.3 | HIGH | §4.7.2 + §4.9 CE 40/10/40/10 vs §5.4.1 maxTurns | §4.7.2: "40% Plan / 10% Work." §5.4.1: Plan = 10 turns; Work = 4+ expert invocations @ 20-30 turns each = 100-180 turns. Work is ~10× Plan in turns but 0.25× in wall-clock framing — the blueprint treats Every's *wall-clock / human-effort* split as if it applied to programmatic budget. | In §4.7.2 label as "wall-clock effort allocation (after Every §Main Loop), not turn allocation. Turn budgets per §5.4.1." |
| 2.4 | MED | §4.10 Lock 20 vs Appendix A Lock 20 | §4.10: "Part 5 §5.7 + Part 4 §4.5.1". Appendix A: "Part 5 §5.3 + §5.7". Reference drift. | Change §4.10 to match Appendix A (Task schema is §5.3.1). |
| 2.5 | MED | §4.9.4 maxTurns bullets vs §5.4.1 table | §4.9.4 lists "Work (simple): 15" and "Work (research): 25". §5.4.1 has no Work-simple/Work-research rows (only mode-level: optimizer=20, integrator=25, critic=25, scalability=30). | Add Work rows to §5.4.1, or re-label §4.9.4 bullets in §5.4.1's mode vocabulary. |
| 2.6 | MED | §4.5.1 Task pseudocode vs §5.3.1 | §4.5.1: `task_id` + `mode_rubric` + no `parent_cycle`. §5.3.1: `parent_cycle` + `mode_rubric_ref` + no top-level `task_id`. | Unify — pick §5.3.1 as canonical; replace §4.5.1 pseudocode with a reference. |
| 2.7 | MED | §5.4.1 table mixes modes and phases | Rows: "Brigadier — Plan / Reception+Integration / Compound" (phases) + "Expert — critic / optimizer / integrator / scalability / research" (modes). Unclear whether "Expert compound" exists. §5.1 §7 compound protocol implies brigadier-owned only. | Add caption: "Compound is brigadier-owned; experts have no compound budget." |
| 2.8 | MED | §4.8 Full-Auto decision tree vs §6.4.4 trust-region | §4.8 rule 6: "smoke test / validated pattern → Full-Auto." §6.4.4: cell eligible for Full-Auto only after ≥3 Stage-Gated runs + golden-set ≥90% + trust-grant. §4.8 tree does not mention trust-grant. | Cross-reference: "For matrix-cell Full-Auto activation, see §6.4.4 trust-region predicate." |
| 2.9 | MED | §4.5.4 "cells don't call cells" vs §5.7.1 expert Bash-write | §4.5.4 rule is Task-tool-level. §5.7.1 grants engineering-expert scoped `Bash (write)` for tests — could `claude -p` a new instance bypassing Task. | Add `claude -p`, `claude --` to §5.7.2 destructive-op deny-list. |
| 2.10 | LOW | §4.7.2 "10+ cell invocations" for open-ended research | Suspiciously close to AP-12 ("50-subagents-for-simple-query") threshold with no hard ceiling. | Cap at "10-20 cells max; beyond = decompose into sub-cycles." |
| 2.11 | LOW | §4.11.5 "Option E — ligament network" | Not in DIET §1.7 original 3-5 design options. | Label as "[Jetix synthesis option, not in DIET §1.7]". |

---

## Surface 3 — Missing anti-patterns

| # | Sev | Missing AP | Evidence | Fix |
|---|---|---|---|---|
| 3.1 | HIGH | KB / embedding rot | EXT-C §2 row 7 "meanings drift, facts go stale"; §4 row 20. | Add AP-27: detection = eval scores decay on fixed golden set; prevention = scheduled re-embedding + golden refresh. |
| 3.2 | HIGH | Operator cognitive overload / "brain fry" | EXT-C §4 row 14: BCG/UC Riverside Axios Apr 2026; Garry Tan 19hr; Karpathy "AI psychosis"; Rousse prescribed sleep aids. Human operator failure. | Add AP-28: session >4h without break; HITL pause >48h; hard daily session cap. |
| 3.3 | HIGH | LLM-specific zero-click (EchoLeak) | CVE-2025-32711 CVSS 9.3 in EXT-A §3 (row noted), NOT referenced in blueprint. Zero-click indirect-prompt-injection. | Add AP-29: any unrelated Assistant query triggering retrieval of malicious email/doc; prevention = input sanitization + no auto-fetch untrusted content into context. |
| 3.4 | MED | Vibe-revenue / category-before-PMF | EXT-C §4 rows 18-19 (Isenberg; Postma divested; Marc Lou DataFast). Business-layer precedent exists in Brief §7 AP-2. | Add AP-30: high AI-curiosity conversion + 3-6mo churn; prevention = persistent-pain validation before ship. |
| 3.5 | MED | Framework version churn (detection gap) | AP-20 covers "Framework-first" but under-treats the version-churn aspect — pinning mentioned, no detection signal. | AP-20 add detection: "minor-version bump breaks production". |
| 3.6 | MED | Decision debt (Horowitz) | EXT-D §1 Horowitz. Relevant: Stage-Gated default + long Ruslan gate-turnaround = compounding decision debt. §6.7.2 flags >48h gate turnaround but not as named AP. | Add AP-31 "Decision debt"; link to §6.7.2. |
| 3.7 | LOW | AgentPoison adversarial memory attack | EXT-B §3: ≥80% attack success at <0.1% contamination. Blueprint AP-18 covers summarization-induced distortion, not adversarial poisoning. | AP-18 subsection on adversarial vs accidental. |

---

## Surface 4 — Evidence thinness

| # | Sev | Claim | Gap | Fix |
|---|---|---|---|---|
| 4.1 | HIGH | §4.2.4 "four verbs are orthogonal in a way narrower sets are not" | Asserted, not argued. "Scalability" is arguably a time-extended Integrator (same synthesis, projected to future). Four-mode claim could degenerate to three-mode + time-horizon parameter. | Add (a) test case where Integrator and Scalability produce different outputs on same input, or (b) acknowledge orthogonality is a design decision not a proven property. |
| 4.2 | HIGH | §4.9.4 maxTurns 15/25/25/12/10/30 presented as "emerging from matrix" | Values were picked for Phase A per §5.4.1 "operational starting points." §4.9 reads as if matrix derived them, not vice versa. | Add note: "Values here are Phase-A seeds per §5.4.1; worked example demonstrates the matrix *could* produce such a synthesis, not that numbers derive from it." |
| 4.3 | HIGH | "1,500-3,000 line system prompt" (ALIGN §5, §5.1-5.2) | No Tier-1 evidence 1,500-3,000 beats 500-1,000. §1.6 attention-budget primitives all point *shorter*: Anthropic CLAUDE.md <200, HumanLayer <60, CE plugin crushed by 1,400-char description overflow. Directive contradicts blueprint's own §1.6. | Flag as "[unattested prompt-length directive from ALIGN §5; contradicts §1.6 attention-budget primitives; calibrate down in Phase B if compliance degrades]". |
| 4.4 | MED | §4.6.2 "Private Library distillation > runtime book-RAG" | Supported by analogy ("Karpathy surprisingly vanilla") and AP-18 hand-wave. No direct A/B on distillation-vs-RAG for book-scale. | Re-label as "engineering choice grounded in §2.1.14 memory-tool data" instead of pseudo-evidential "rationale". |
| 4.5 | MED | §4.1.2 Rule-of-4 argument against 9 experts | Permits 5 with "heterogeneous experts mitigate coordination tax." But Kim et al. is specifically about heterogeneous too; EXT-B §6 contradiction 3 says *explicitly* "Jetix's heterogeneous agents violate homogeneous assumption → coordination tax." Heterogeneity is a *cost*, not a mitigation. | Re-frame: 5 is accepted because we pay the heterogeneity cost, not because heterogeneity excuses 5. |
| 4.6 | MED | §5.1.1 brigadier section line-counts (§2 = 200-250, §3 = 250-300, …) | No basis for 200-250 vs 150-200. Precise budgets with no grounding. | Acknowledge: "[sections sum to ~1,500-2,000 target; individual budgets are author estimates; calibrate in smoke test]". |
| 4.7 | LOW | §5.1.2 "≤20 canonical quotes loaded" | Author-invented number. | Flag as "author estimate." |

---

## Surface 5 — 24 Locks compliance

| # | Sev | Lock | Issue | Fix |
|---|---|---|---|---|
| 5.1 | HIGH | Lock 7 (archetypes 11 vs 10) | Blueprint writes "(11)" silently. EXT-E §H.2 contradiction 2: PRE §D7 locks *10*; Brief §2 re-normalizes to 11. Blueprint adopts 11 without acknowledging the tension. | Add to §4.10 / Appendix A rationale: "[Brief §2 normative: 10 base + bloggers Stage 3 = 11; PRE §D7 originally 10]." |
| 5.2 | MED | Lock 13 tier enforcement | §4.10 marks ✅ "Tier enforcement in wiki." §5.5.4: "Cells check tier on every `wiki_read` via MCP server." §5.6.1 PreToolUse tier-check is *only* for outbound tools (email/notion/webhook). Read-side tier enforcement is *specified* but not implemented — MCP server method is not defined. | Add §5.7.4 "Wiki MCP server tier-check logic": `wiki_read` returns `core`-tier only if invoker's role has `core` access; else redacted/denied. |
| 5.3 | MED | Lock 19 ($1T holding-scale) | §4.10 marks ✅ "scalability-architect role-mode first-class." But this is a *lens*, not *scaffolding*. Lock implication: "Schemas 10³-10⁶ entity Day 1." Blueprint does not test wiki schema at 10⁶, nor specify sharding. | Add §5.5.6 "Schema scale-out anchors" referencing EXT-E §A row 19 and Brief §5.1 even if Phase-B-implemented. |
| 5.4 | MED | Lock 15 (revenue-gated spend) | §4.10 marks ✅ "Turn-denominated budget; gates applied." Actual gate thresholds ($20-30K → €50K → €200K → €1M per EXT-E §A row 15) are NOT encoded anywhere. §5.4.2 "3 cycles/day soft cap" is unrelated. | Add `gate_state` field in brigadier context or `config/gates.json` listing four thresholds; reference from §5.4.2. |
| 5.5 | LOW | Lock 21 kit contents / kill criteria | §5.8.3 lists 7 kit items; Brief §10 Q10 requires "kit contents, lifecycle, inter-roy protocol, kill criteria." §5.8.3 defers lifecycle/inter-roy/kill criteria to Phase 2+. Kill criteria is the critical missing piece. | Add stub: "Kill criteria for cloned roys: default revoke on tier-escape or Lock-violation audit." |

---

## Surface 6 — Part 5 actionability

I simulated "I am a prompt writer given only the cited section. Can I write it?"

| # | Sev | Section | Actionability problem | Fix |
|---|---|---|---|---|
| 6.1 | HIGH | §5.1 §3 Decomposition protocol (250-300 lines) | Given only §5.1.1 I know three fan-out rules and four task-shape labels ("design / review / optimize / scale-project"). I do NOT know: which cells to pick for "design" vs "optimize", how to weight domains against task-shapes, decision heuristics when shapes overlap, or what to do when the task is ambiguous between shapes. Prompt writer must invent the mapping. | Add §5.1.3 "Task-shape → cell selection matrix" stub: per shape, default cells, optional, forbidden. Even a stub table gives deterministic guidance. |
| 6.2 | HIGH | §5.2.2 Mode activation mechanic | "If `mode` not set → treat as `integrator` … Read only §1-§2 + §<matching>." Enforcement is prompt-level, exactly the AP-5 anti-pattern ("never rely on prompt-level prohibitions"). §5.2.2 diagnostics (Hamel golden set + Compound) are detection, not prevention. | Option A: §5.6 UserPromptSubmit hook refuses expert launch without `mode`, wraps rigid header. Option B: acknowledge as prompt-level soft constraint. Either way, flag explicitly. |
| 6.3 | HIGH | §5.3.1 Task invocation schema with `mode` field | Claude Code's actual Task tool accepts `subagent_type`, `description`, `prompt` — no `mode` field. §5.3.1 acknowledges "`mode` written into agent's system prompt on invocation by brigadier concatenating a mode-selector prefix" — this is a *convention* implemented via string-prefixing, not an API. §4.5.1 pseudocode reads as if it's an API. | In §4.5.1, add "This is a convention implemented via prompt prefixing (§5.3.1), not a Claude Code native primitive. Schema validation is brigadier-owned." |
| 6.4 | MED | §5.4.3 Verifier interface | Given only §5.4.3 I could write Python/Bash scaffolding. But: rubric_path format (markdown? YAML? binary criteria list?) under-specified; "structural not semantic" tells me *what* to check but not *how* to match section boundaries robustly. | Add 1-page example `verifier-critic.py` in §5.4.3 with regex/YAML parse, pass-rule logic, reasons format. |
| 6.5 | MED | §5.2.1 few-shot examples (3-5 per mode per expert = 16-20+ per expert) | Zero examples provided, even as stubs. Prompt writer cannot synthesize without concrete task runs. | Either (a) defer all few-shots to smoke-test ("populate after §6.1 + first 3 Stage-Gated runs") or (b) stub one per mode × expert = 20 stubs. |
| 6.6 | LOW | §5.5.3 inline citation format `[src:path#section]` | No worked example with spaces in path, section-range syntax, escaping rules. | One worked example in §5.5.3. |
| 6.7 | LOW | §5.10.1 brigadier skills (plan-cycle / invoke-cell / etc.) | Six skills named, no stubs. | Accept — low-risk to create iteratively on smoke-test eve. |

---

## Surface 7 — Phase-A scope discipline

| # | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| 7.1 | LOW | §4.4 cell map uses Tier-4 labels ("Ashby requisite-variety", "Cagan 4-risks", "Laloux CLOU", "Popper falsifiability", "Koen heuristic ranking", "Taleb antifragile", etc.) | Labels / pointers, not distillations from direct book reading. Provenance traced via Tier-3 (RESULT-05/06/07, EXT-D). Phase-A-compliant. | None. |
| 7.2 | LOW | §4.6.1 domain-to-library mapping | Correctly tags all listed books "Phase B reading." ✅ | None. |
| 7.3 | LOW | §5.2.3 expert canonical-source allocation | Explicit split "Phase A distillation from Tier 1+2+3 / Phase B Tier 4 books." ✅ | None. |
| 7.4 | LOW | §4.2.1 critic rubric evidence basis | R-11 §4 (Tier-1), RESULT-07 (Tier-3), EXT-D — all correctly sourced via extractions. | None. |
| 7.5 | MED | §2.1.20 "(Ravikant, Graham)" cited directly | Neither is in EXT-A/B/C/D/E as directly-read. Both are Tier-4 (Naval in §4.6.1 Phase-B). Framing comes via RESULT-07 §I. | Change to "(Ravikant via RESULT-07; Graham via RESULT-07)" to mark pointer-vs-source. |

---

## What the blueprint does well

1. **Citation discipline is top-tier.** Every claim traces to extraction
   shortcodes. Jetix-specific terms are labelled `[unattested in Tier-1]`;
   self-reported data is `[self-reported]`. §1.0 voluntary self-flagging
   ("every Jetix-specific term is explicitly labelled as a synthesis") is
   unusually disciplined.
2. **Yan / Anthropic tension (§1.8 + §2.2.3) is handled cleanly.** The
   resolution — "parallel review of a single artefact = safe; parallel code
   generation with summary hand-offs = Flappy Bird trap" — is the correct
   synthesis of EXT-B §6 contradiction 1.
3. **Part 3 anti-pattern catalog (26 items) with concrete prevention
   primitives.** AP-14 reward hacking requires read-only test runner — that's
   implementable, not a vague "don't cheat" (which §3.14 itself flags as
   ineffective per R-3 §6.1.3).
4. **§4.3.2 synergy argument with Ruslan's verbatim quote** turns the matrix
   from "arbitrary Jetix invention" to "Ruslan's own words, with mechanically-
   precise operational translation." Defends the matrix against the easy "why
   not 20 separate agents" attack.

---

## Overall judgement

**Good enough to generate 6 system prompts?** Yes, with revisions. Brigadier
and engineering-expert prompts can be generated from §5.1 + §5.2 + §5.3 +
extractions as-is. The other four experts (mgmt, systems, philosophy,
investor) have §5.2.3 allocations Phase-A-sufficient for Primary + Shared
sections (~900-1,400 lines); the Mode sub-sections (~1,200-2,000 lines) need
few-shot examples acknowledged in 6.5 as "stubs + populate-at-smoke-test" or
prompts ship under-specified.

**Single highest-value revision.** Fix 2.3 — the 40/10/40/10 wall-clock vs
maxTurns turn-budget conflation. Load-bearing because every cycle the
brigadier runs exposes it; a prompt writer will hard-code one interpretation
and operational behavior diverges from intent after the first real task.

**Second.** Fix 4.3 — 1,500-3,000 line system-prompt directive contradicts the
blueprint's own attention-budget primitive (§1.6). Justify the length with an
in-Phase-A citation, or explicitly label as ALIGN §5 directive to calibrate.

**Third.** Add missing anti-patterns 3.1 (KB rot), 3.2 (operator cognitive
overload), 3.3 (EchoLeak zero-click). Named production failure modes missing
from Part 3.

Not-revisions (deferrable to Phase-B iteration without re-gating Phase-A):
few-shot stubs (6.5), Lock 15 gate-threshold encoding (5.4), verifier signature
unification (2.2).
