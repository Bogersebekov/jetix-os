---
sub_agent: A
title: Mechanics + Goals + Build-Logic Extraction for Wiki v3 Стадия C
date: 2026-04-23
sources_read:
  - decisions/WIKI-V3-MECHANICS-2026-04-23.md
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md
  - design/ROY-BUILD-LOGIC-2026-04-23.md
word_count_target: ≤2500
purpose: Feed Phase 2 architecture-spec drafting (Deliverables 1–12)
---

# Sub-agent A — Extraction for Wiki v3 Стадия C

Extraction-only. No re-debate. Citations mandatory. "Spec MUST" = acceptance criterion.

## Section 1 — Q1..Q9 acceptance criteria

### Q1 — Retrieval (primary)
- **Recommended:** 4-tier filesystem+graph stack — direct path lookup → index+niche+grep → typed-edge BFS on `edges.jsonl` (≤2 hops, top-k=10) → long-context fallback. PPR/HyDE/embeddings deferred. (MECHANICS Part 1 row Q1; Part 2 §Q1 L50–125.)
- **Applicability:** valid until `edges.jsonl` >~2,000 edges OR `/ask` FPAR <80% over rolling 20-query window. (Part 2 §Q1 L113–116.)
- **New variants:** (a) `alpha_direct_lookup` promoted to dedicated Tier 1; (b) `alpha_aware: true` filter on Tiers 2–3 when task carries `alpha_type`; (c) "≤1 hop до источника" invariant — `/lint` flags violators. (Part 2 §Q1 L118–125.)
- **Spec MUST:** define the 4-tier stack in that order; NOT mandate embeddings/PPR Phase A; add `/lint`-enforced "≤1 hop to source" rule; expose `alpha_aware` filter on tiers 2–3.

### Q2 — Write serialization
- **Recommended:** single-writer brigadier across all 9 layers Phase A; experts produce drafts in `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md`, return via Task; brigadier commits through §5.5.5 provenance gate; PostToolUse `/lint` validator. (Part 1 row Q2; Part 2 §Q2 L128–177.)
- **Applicability:** Phase A; revisit at close OR when brigadier commit queue >~5 pending artefacts/cycle. (L174–176.)
- **New variant:** strategies content currently has 3 candidate locations — `agents/<expert>/strategies.md`, `swarm/strategies/<expert>.md`, `swarm/wiki/meta/agent-improvements/<agent>-*.md`. Mechanics resolves: keep (a) + (c), DROP (b). (L178–187; T5.)
- **Spec MUST:** forbid expert direct writes outside `wiki/drafts/`; require Task round-trip; embed §5.5.5 compound provenance gate (≥1 source + commit hash OR verbatim source + line range); install PostToolUse `/lint`; drop `swarm/strategies/`; route Level-1 CE → `agents/<expert>/strategies.md`, Level-2 CE → `swarm/wiki/meta/agent-improvements/`.

### Q3 — Cross-reference format
- **Recommended:** triple-channel — YAML frontmatter (`sources[]`, `related[]`, `captured_by`, `captured_date`, `task_id?`, `commit_sha?`) + inline `[[type/slug]]` wikilinks under typed section headers + append-only `swarm/wiki/graph/edges.jsonl` + inline `[src:path#section]` atomic citations. **12-edge enum** (9 intra + `part_of` + 3 cross-layer: `alpha-ref`, `layer-ref`, `cross-tree-ref`). (Part 1 row Q3; Part 2 §Q3 L190–267.)
- **Applicability:** Phase A–B; revisit consolidation at >5K edges. (L259–261.)
- **New variants:** (a) Diátaxis-for-data mapping — Tutorial/Procedural→`roles/`; Reference/Facts→`concepts/`/alpha YAMLs; Explanation→`topics/`/`ideas/`; Episodic/Log→`history.jsonl`/`experiments/`; (b) `part_of` formalised as 10th intra-layer edge (233 ad-hoc edges, 40% of v2 graph). (L226–229, L263–267.)
- **Spec MUST:** enumerate exactly 12 edge types (definition + cardinality + inverse + example) in `swarm/wiki/_templates/edge-types.md`; require all 4 channels on every page; treat `edges.jsonl` as derivative (rebuilt by `/build-graph` from body+frontmatter); adopt Diátaxis mapping for layer template choice.

### Q4 — Task-scoped context population
- **Recommended:** hybrid auto-pull + brigadier override — declare `task.niche`/`task.alpha_type`/5–10 keywords → Tier A (niche symlinks + `decisions/` filtered niche+90d + 24-Locks subset) → Tier B (typed-edge BFS top-k=10, ≤2 hops) → Tier C (book-derived summary excerpts) → brigadier `pinned.md`/`excluded: true` override → 20K-token cap with priority-based digest fallback. (Part 1 row Q4; Part 2 §Q4 L270–325.)
- **Applicability:** Phase A; revisit when (a) PPR lands Phase B, (b) >70% tasks trigger brigadier override. (L318–319.)
- **New variants:** (a) `context/manifest.yaml` with `priority: 1..N` for compaction-by-priority; (b) `alpha_aware` filter applies to typed-BFS seeds. (L321–324.)
- **Spec MUST:** define `swarm/wiki/tasks/<task-id>/` with `open-questions.md`, `context/`, `context/manifest.yaml`, `context/pinned.md`; cap context at 20K tokens; specify the 4-tier pull pipeline; allow `pinned.md` and `excluded: true` overrides.

### Q5 — Rot / staleness
- **Recommended:** 5-signal `/lint` orchestration — (1) structural (orphans, broken links, missing frontmatter, index drift); (2) α-2/α-3 lifecycle states (`superseded`, `retired`, `tombstoned`); (3) confidence×age (low conf + >60d → flag; foundation + >365d → re-review); (4) contradiction-edge integrity (semantic detection deferred Phase B); (5) time-based (foundations only Phase A; global trigger >10K pages). (Part 1 row Q5; Part 2 §Q5 L328–397.)
- **Applicability:** Phase A; revisit signal #4 semantic when Phase-B brigadier-LLM audits land; revisit #5 at 10K entries. (L390–392.)
- **New variant:** **FPAR (First-Pass Acceptance Rate)** as indirect staleness signal on `/ask`, target >80%, weekly emit to `swarm/wiki/meta/health.md`. (L394–396.)
- **Spec MUST:** define `/lint` as 5-signal orchestrator (PostToolUse + scheduled); require `last_reviewed` on `foundations/`; require bidirectional `contradicts` edges; create `swarm/wiki/meta/health.md` with FPAR + cycle metrics + cross-theme-ref count + tombstone rate.

### Q6 — Skill-learning pipeline
- **Recommended:** formal α-3 pipeline at `swarm/wiki/skills/{candidates,learning,active,usage}/`; DRR frontmatter (context/decision/alternatives/checkpoint); states `proposed → drafting → active → validated → tombstoned`; activation = golden-set ≥80% pass + brigadier provenance gate; validation = ≥10 uses + ✓/✗ ≥3:1; tombstone = ≥10 uses + <1:1 OR Ruslan retire. `.claude/skills/<slug>.md` symlinks to `swarm/wiki/skills/active/<slug>.md`. (Part 1 row Q6; Part 2 §Q6 L400–493.)
- **Applicability:** Phase A; revisit at >20 active skills (Langfuse decision) or when ≥10-use gate blocks too many. (L485–487.)
- **New variant:** **System Prompt Learning pump** — Level-1 sink in `agents/<expert>/strategies.md`; brigadier Level-2 sweep promotes patterns appearing in ≥2 strategies.md files into `skills/candidates/`; per-skill FPAR in `usage/<slug>.md`. (L489–492.)
- **Spec MUST:** create the 4 `skills/` subdirs; define DRR YAML schema verbatim; assign owners per transition (propose=any/Ruslan; draft+golden-set=brigadier or matrix-expert; eval=brigadier; activate=brigadier under §5.5.5; weekly audit=meta-agent; retire=meta-agent or Ruslan); install symlink and remove (file retained, `status: tombstoned`) on tombstone.

### Q7 — Git branches
- **Recommended:** `roy/<project-slug>/{main,iter-vN,fork-<variant>,exp-<hypothesis>}`; `<project-slug>` kebab-case ≤30 chars matching `swarm/wiki/operations/<project-slug>/` 1:1; only brigadier creates `roy/` branches; depth ≤2; CI skips `roy/*`. (Part 1 row Q7; Part 2 §Q7 L496–541.)
- **Applicability:** all long-horizon swarm work (W-6), Phase A+B; revisit only on multi-branch git bottleneck. (L537–539.)
- **New variants:** none (naming-only). (L541.)
- **Spec MUST:** adopt the schema; require `<project-slug>` 1:1 with `swarm/wiki/operations/<project-slug>/`; forbid expert branch creation; cap nesting depth at 2.

### Q8 — Layer 9 activation
- **Recommended:** cumulative-AND, human-gated — Phase A scaffolds only `swarm/wiki/insights/{README.md,candidates/,promoted/}` with no agent. Phase B activation requires ALL three: (1) ≥50 closed α-4 cycles; (2) ≥2 theme-wikis with ≥50 concepts each AND ≥3 inter-theme refs; (3) explicit Ruslan approval. (Part 1 row Q8; Part 2 §Q8 L544–598.)
- **Applicability:** trigger evaluated only at Phase B window; Phase A never activates. (L594–596.)
- **New variants:** none. (L598.)
- **Spec MUST:** scaffold `insights/{README.md,candidates/,promoted/}`; encode 3-AND + Ruslan trigger in README; NOT instantiate any insights-writer agent; preserve future flow (`candidates/` writes by crazy-agent, `promoted/` by brigadier under §5.5.5).

### Q9 — `wiki/` v2 vs `swarm/wiki/` v3
- **Recommended:** coexist + parameterize. v2 untouched; v3 new; `$WIKI_ROOT` indirection across 6 skills (~85 line edits to `ingest.md`/`ask.md`/`lint.md`/`consolidate.md`/`build-graph.md`/`sweep-notion-bank.md`); 9 v2 templates **copied** (not symlinked) into `swarm/wiki/_templates/`; cross-tree edges in `swarm/wiki/graph/cross-tree.jsonl` via `cross-tree-ref` (v3→v2 only); migration deferred Phase B. (Part 1 row Q9; Part 2 §Q9 L601–666.)
- **Applicability:** Phase A; migration deferred until v3 ≥50 entries + ≥1 closed cycle + observed value delta. (L658–660.)
- **New variants:** (a) `$WIKI_ROOT` parameterize-as-unifier (≈ same cost as full-migrate, keeps both trees); (b) `part_of` schema-drift fix — formalise in 12-edge enum, back-port docs. (L662–666.)
- **Spec MUST:** keep `wiki/` v2 untouched; place v3 under `swarm/wiki/`; add `.claude/config/wiki-roots.yaml` with `wiki_root_v2: wiki` + `wiki_root_v3: swarm/wiki`; diff each of the 6 skills to consume `$WIKI_ROOT`; isolate cross-tree edges; `/lint`-flag any v2→v3 reverse edge.

---

## Section 2 — W-1..W-12 locked constraints

- **W-1 Multi-layer 9-layer.** Realise Wiki v3 as multiple specialised layers under `swarm/wiki/` with defined boundaries + cross-refs — not flat KB. (GOALS §3 W-1 L397–400; §2 L302–389.)
- **W-2 Brigadier own Wiki.** Treat `swarm/wiki/brigadier/` as mandatory, offloading orchestration state from context window. (GOALS §3 W-2 L402–404; §1.2; §2 Layer 2.)
- **W-3 Books → Wiki distillation.** Seed theme-wikis via brigadier book-distillation Phase A; experts deepen Phase B. (GOALS §3 W-3 L406–409; §1.3; §1.5.)
- **W-4 Agent-improvement dedicated layer.** Place meta-improvement in `swarm/wiki/meta/agent-improvements/`, separate from task content. (GOALS §3 W-4 L411–413; §1.6; §2 Layer 4.)
- **W-5 Two-level CE.** Support Level-1 per-agent + Level-2 system-level CE; brigadier Level-2 outputs land in Layer 4. (GOALS §3 W-5 L415–419; §1.10.)
- **W-6 Git branches.** Native git branches as version control for long-horizon projects (per-iteration + fork + checkout-rollback). (GOALS §3 W-6 L421–424; §1.9.)
- **W-7 Two parallel task layers.** Keep Layer α (task-knowledge) and Layer β (operational) **separate**. (GOALS §3 W-7 L426–430; §1.8.)
- **W-8 Workflow standard.** Enforce FPF + versioning + deep Wiki + 2-level CE as baseline — no shortcut. (GOALS §3 W-8 L432–434; §1.12.)
- **W-9 Skills first-class layer.** Make skills first-class Layer 8 with formal candidate→eval→golden-set→activation pipeline. (GOALS §3 W-9 L436–438; §1.11; §2 Layer 8.)
- **W-10 Crazy-agent deferred.** Scaffold Layer 9 placeholder without instantiating Phase A. (GOALS §3 W-10 L440–442; §1.7; §2 Layer 9.)
- **W-11 Wiki = cognitive infrastructure.** Treat Wiki as central cognitive infrastructure (memory + coordination + improvement), not storage. (GOALS §3 W-11 L444–447; meta-principle L21–31.)
- **W-12 1000% depth.** Honour "1000% deeply worked" bar — every page, cross-ref, provenance tag deep, not adequate. (GOALS §3 W-12 L449–453; meta-principle L21–24.)

---

## Section 3 — R1..R8 accepted defaults (TRUE preconditions)

All Yes per Ruslan 2026-04-23 (MECHANICS Part 5 L803–818; frontmatter L7).

- **R1.** `roy/<project-slug>/{tag}` is the accepted Phase-A branch convention; spec uses without re-justification.
- **R2.** 4-tier filesystem + typed-BFS is Phase-A retrieval default; PPR/HyDE/embeddings deferred.
- **R3.** v2 untouched, v3 added, `$WIKI_ROOT` indirection mandatory; full migrate off-table Phase A.
- **R4.** Q6 owners fixed (propose=anyone; draft=brigadier/expert; eval=brigadier; audit=meta-agent; retire=meta-agent or Ruslan).
- **R5.** 3-signal AND + Ruslan manual trigger for Layer 9; spec encodes in `swarm/wiki/insights/README.md`.
- **R6.** Drop `swarm/strategies/`; keep `agents/<expert>/strategies.md` (Level-1) + `swarm/wiki/meta/agent-improvements/` (Level-2).
- **R7.** 12-type edge enum locked (no wait-and-tune); enumerate all 12 with cardinality+inverse+example.
- **R8.** T1–T5 are specification clarifications, not scope changes; spec resolves within its own deliverables (no escalation).

---

## Section 4 — T1..T5 tension resolutions

(MECHANICS Part 3 L669–710.)

- **T1 — `edges.jsonl` location asymmetry.** Three files: v2 `wiki/graph/edges.jsonl`, v3 `swarm/wiki/graph/edges.jsonl`, cross-tree `swarm/wiki/graph/cross-tree.jsonl`. Resolution: `/build-graph --tree {v2|v3|both}`; cross-tree is **derivative**, rebuilt from page scans, never hand-edited. (L693–695.)
- **T2 — Q4 niche-cap vs Q8 cross-theme density.** Niche-filtered tasks may never produce cross-theme refs, blocking Layer 9 trigger. Log cross-theme refs weekly into `swarm/wiki/meta/health.md`; re-evaluate Q8 signal #2 after 20 cycles if count is 0. (L696–698.)
- **T3 — Q6 activation-vs-validation rubric.** Activation = golden-set ≥80% binary; validation = usage-driven (≥10 uses + ≥3:1). Стадия C MUST write explicit rubric distinguishing the two gates. (L699–701.)
- **T4 — Edge-type empty counts.** 4 of 9 v2 types have 0 entries; v3 inherits. Accept upfront enum; `/lint` reports per-type counts so emptiness is visible, not blocking. (L702–704.)
- **T5 — strategies.md trio collapse.** Q2 §5 resolves: keep `agents/<expert>/strategies.md` + `swarm/wiki/meta/agent-improvements/`; drop `swarm/strategies/`. Spec MUST document and note the dropped path. (L705–708.)

---

## Section 5 — Build-logic phasing (Phase A vs Phase B)

(BUILD §1.2, §1.3, §2.1–§2.3, §3, §4.2, §4.4.)

### Phase A — what this Стадия C spec MUST cover
- **`swarm/` scaffold.** Realise 9-layer `swarm/wiki/` inside the scaffold (`swarm/scratchpads/`, `swarm/gates/`, `swarm/mailboxes/`, `swarm/logs/`); explicitly drop `swarm/strategies/` per T5/R6. (BUILD §1.2 L56–95.)
- **Untouchables.** MUST NOT touch v2 `wiki/`, `knowledge-base/`, `decisions/`, `design/`, `raw/`, `prompts/`, `tools/`, `CLAUDE.md`, `.claude/rules/`, existing `.claude/skills/` content. (BUILD §1.3 L97–104; §5 L374–386.)
- **Communication.** Layer 1 = Task tool (brigadier sole caller); Layer 2 = stigmergic via `swarm/wiki/` (single-writer brigadier, provenance YAML mandatory); Layer 3 = mailbox JSONL minimal. (BUILD §2.1 L115–153; §2.2 L154–192; §2.3 L194–211.)
- **Provenance frontmatter.** Require `source`, `captured_by`, `captured_date`, `task_id`, `commit_sha` on every wiki entry. (BUILD §2.2 L178–186.)
- **Single tmux session.** Brigadier-as-entry, experts via Task; affects branch discipline, gate flow, atomic per-task git audit trail. (BUILD §3 L215–314.)
- **Task-scoped layering.** Four explicit context sources for `tasks/<task-id>/context/`: Private Library books, `decisions/` current, 24-Locks subset, previous global learnings. (BUILD §4.2 L326–349.)
- **§4.4 deferred items.** §4.4 defers manual-vs-auto context, promotion criteria, retention, multi-task fusion, taxonomic integration — now resolve all five via Q4 pipeline + brief retention policy + global-promotion rule + taxonomic integration note (Karpathy + GraphRAG typed edges + Zettelkasten atomic notes unified by Q3 triple-channel + 12-edge enum). (BUILD §4.4 L359–371.)

### Phase B — doors MUST stay open (NOT implemented now)
- **393-book ingestion.** Preserve hooks: theme-wiki layout (W-3) accepts incremental deepening; `cross-tree-ref` accommodates new book pages; provenance already supports `source: raw/books-md/...`. (GOALS §1.5; W-3.)
- **PPR / HyDE / embeddings.** Keep `edges.jsonl` clean so PPR-on-top is mechanically possible. (Q1.)
- **Layer 9 / crazy-agent.** Placeholder only; do not preclude Phase B promotion flow. (Q8.)
- **CRDT / per-layer owners.** Layout neutral so per-layer owners can be added without restructuring. (Q2.)
- **Langfuse skills registry.** Keep `skills/active/<slug>.md` authoritative so a registry can later index, not replace. (Q6.)
- **Full v2→v3 migration.** Use `$WIKI_ROOT` so migration is a config flip, not a rewrite. (Q9.)

---

## Section 6 — Cross-references and watch-outs

Non-obvious mechanical couplings between locked items.

1. **12-edge enum locks `/build-graph` + `/lint` + cross-tree separation.** The enum drives the `/build-graph` section-header parser, `/lint` per-type counts (T4), and `cross-tree.jsonl` separation (T1). Changing one edge name moves three deliverables. (Q3 L215–238.)

2. **Q1 Tier 3 + Q4 Tier B share one mechanism** (typed-edge BFS on `edges.jsonl`). Spec MUST factor into one subroutine consumed by `/ask` and the brigadier task-context populator — otherwise read/write semantic drift is guaranteed. (Part 3 #1, L675.)

3. **Q6 α-3 state machine doubles as Q5 staleness signal.** `tombstoned`/`superseded`/`retired` feed three of the five `/lint` signals — treat skills + content lifecycle as the **same** state machine. (Part 3 #4, L682.)

4. **R4 owners require meta-agent in Phase-A scaffolding.** Meta-agent owns weekly skill audit + tombstone authority. The matrix is 5 domain experts + brigadier; meta-agent isn't a domain expert but owns the audit role. (§Q6 L449–463; R4.)

5. **Q9 `$WIKI_ROOT` mechanically requires Q6 symlink parameterization.** `.claude/skills/<slug>.md → swarm/wiki/skills/active/<slug>.md` references an absolute v3 path; if `$WIKI_ROOT_V3` is parameterised, symlink target must be too. Spec MUST deliver `$SKILLS_ROOT`. (§Q6 L482; §Q9 L612–613.)

6. **W-7 (α/β) couples to Q7 branches.** Layer α = `tasks/<task-id>/`; Layer β = `operations/<project-slug>/`; Q7 branch slug MUST 1:1 with Layer β slug — enforce via `/lint` check. (§Q7 L517; W-7; Part 4 L724.)

7. **Q4 manifest `priority` couples to W-12 depth.** 20K-token cap + priority-based digest fallback means low-priority pages get summarised; "1000% depth" (W-12) requires summarised pages to preserve provenance + ≤1-hop reachability — otherwise digest violates the Q1 invariant. Spec MUST require digest pages retain `sources[]` paths. (§Q1 L124; §Q4 L296–315; W-12.)

8. **R6 makes BUILD §1.2 layout diagram stale.** §1.2 lists `swarm/strategies/` top-level; T5 + R6 drop it. Spec MUST emit a corrected `swarm/` tree and note the deliberate amendment. (BUILD §1.2 L76–82; T5; R6.)

9. **POTENTIAL CONFLICT — Q4 Tier C "book excerpts" vs hard constraint NOT to read books.** Tier C requires distilled summary pages in `wiki/sources/` to **exist**; W-3 says brigadier seeds them by reading curated books. Spec MUST clarify whether Phase A includes the seeding sweep or Tier C starts empty. (§Q4 L289–292; W-3 L406–409.) Escalate.

10. **POTENTIAL CONFLICT — single-writer brigadier (Q2) vs meta-agent weekly audit (Q6).** Q2: brigadier is sole writer across 9 layers Phase A. Q6: meta-agent runs weekly skill audit + tombstones via `usage/<slug>.md`. Either meta-agent gets a single-writer carve-out OR emits a draft brigadier commits. Spec MUST pick one. (§Q2 L130–162; §Q6 L449–463.) Escalate.

---

**End of extraction.**
