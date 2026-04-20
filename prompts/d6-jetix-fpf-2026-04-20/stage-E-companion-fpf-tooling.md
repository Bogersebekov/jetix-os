---
type: task-prompt
stage: E (optional companion)
target: claude-code main session (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: wiki/foundations/fpf-tooling.md (10-20 pages)
estimated-time: 2-3 hours
status: ready-to-execute (OPTIONAL — only if Stage D verdict = VERIFIED READY)
---

# Stage E — Companion: wiki/foundations/fpf-tooling.md

## Context

D6 JETIX-FPF v2 verified READY (Stage D passed). Теперь пишем **companion
document** per OQ-07 decision (soft split) + Rec-13 E.5.1 DevOps Lexical
Firewall.

**Jetix FPF Core** (D6) — abstract principles, patterns, philosophy — 30-50 pages.
**FPF Tooling Companion** (этот deliverable) — tooling-specific patterns,
operational workflows, Claude Code specifics — 10-20 pages.

**E.5.3 Unidirectional Dependency:** Tooling references Core (not reverse).
Core stays clean abstract; Tooling concretizes.

---

## Inputs

1. **`design/JETIX-FPF.md`** v2 (Core) — reference document, don't modify
2. **`raw/external/ailev-FPF/FPF-Spec.md`** — FPF-Spec Part E (Constitution) esp. E.5.1, E.5.3
3. **`decisions/2026-04-19-architecture-v2-approval.md`** — ADR context (Chunk 8 Rec-13)
4. **`decisions/gap-analysis-review-decisions-2026-04-20.md`** — OQ-07 decision
5. **`decisions/2026-04-20-jetix-architecture-final-DRAFT.md`** — D9 v0.6 operational details

---

## Deliverable

### File path
`wiki/foundations/fpf-tooling.md`

### Size target
10-20 pages structured tooling companion.

### Frontmatter

```yaml
---
id: JETIX-FPF-TOOLING
title: JETIX-FPF Tooling Companion
subtitle: Operational implementation patterns для JETIX-FPF Core
date: 2026-04-20
version: v1.0
status: draft
companion-of: design/JETIX-FPF.md (Core)
dependency: unidirectional — Tooling references Core, not reverse (E.5.3)
scope: internal-only (per OT5 + OQ-09 A)
lang: [ru, en]
---
```

### Structure — 8 sections

#### Section 1 — Introduction + E.5.1 Lexical Firewall
~1 page
- Rationale для Core/Tooling split
- E.5.1 DevOps Lexical Firewall explained
- E.5.3 Unidirectional Dependency enforcement

#### Section 2 — Claude Code specifics
~2-3 pages
- `--dangerously-skip-permissions` usage
- Task tool для subagent spawning
- Read/Write/Edit/Grep patterns recommended
- Context window management strategies (25K exocortex reservation)
- Extended thinking usage

#### Section 3 — Pre-commit hooks (5 hooks)
~2 pages
- Hook 1: Asymmetric reference check (Jetix → Life-OS blocked)
- Hook 2: Rechnungsnummer sequential monotonicity
- Hook 3: Role-manifest required-fields lint
- Hook 4: Past-participle state check
- Hook 5: Auto-translation hook (OT2)

Per hook: implementation language, trigger pattern, failure message.

#### Section 4 — Pre-commit hook templates
~2-3 pages
- Template для each hook — bash / Python specifics
- CI integration (where minimal GitHub Actions apply)
- Local development workflow

#### Section 5 — Agent workflows
~2-3 pages
- Daily workflows per agent type (manager / sales-research / sales-outreach / knowledge-synth / meta-agent)
- Example invocation patterns
- Mailbox / scratchpad / system.md loading

#### Section 6 — Tool-specific patterns
~2 pages
- SOPS + age secrets management
- restic → Backblaze B2 backup
- Healthchecks.io cron monitoring
- Stripe payment integration patterns
- Toggl Deep Hours tracking

#### Section 7 — Ritual protocols (operational)
~2 pages
- Daily 30-min ritual — exact steps
- Weekly Friday 60-min — Shape Up protocol
- Monthly 2h — P&L + OKR + founder note specific
- Quarterly 1 day — letter + role-manifest delta + strategy
- FPF-Steward quarterly audit — protocol

#### Section 8 — Troubleshooting + FAQ
~1-2 pages
- Common issues + resolutions
- When ритуал не fired — fallback
- When agent drifts — FPF-Steward action

---

## Quality requirements

- **References JETIX-FPF Core** explicitly (don't duplicate abstract concepts)
- **Concrete > abstract** в companion (opposite focus of Core)
- **Code examples** где applicable (bash snippets, YAML templates)
- **Russian primary** + English FPF/tool citations
- **Operational focus** — "how to" not "why"

---

## Process

### Step 1 — Read inputs (~30-45 min)

D6 v2 for reference context. ADR Chunk 8 for tooling decisions. D9 v0.6 for
operational specifics.

Extended thinking.

### Step 2 — Write companion (~90-120 min)

Follow structure 8 sections. Concrete examples везде где applicable.

### Step 3 — Consistency check (~15-30 min)

- No duplication с Core (companion references, не replicates)
- All references к Core correct
- Operational claims match ADR + D9 v0.6

### Step 4 — Commit + push

```
git add wiki/foundations/fpf-tooling.md
git commit -m "[design] JETIX-FPF Tooling Companion v1 — Stage E complete

Soft split per OQ-07 + Rec-13 E.5.1 DevOps Lexical Firewall:
- Core: design/JETIX-FPF.md (abstract principles, ~30-50 pages)
- Tooling: wiki/foundations/fpf-tooling.md (operational, ~10-20 pages)

Unidirectional dependency preserved (E.5.3 — Tooling references Core).

Content:
- 8 sections (Intro / Claude Code / Pre-commit hooks / Hook templates /
  Agent workflows / Tool-specifics / Rituals / Troubleshooting)
- Operational focus complement к Core abstract philosophy
- Concrete examples + code snippets

Together: D6 Core + Tooling Companion = complete JETIX-FPF methodology.

Unblocks D1-D5 + D7-D8 writing (remaining Stage 4 documents).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

git push origin claude/jolly-margulis-915d34
```

### Step 5 — Report

- File path + line count
- 8 sections written
- Key patterns covered
- Commit SHA

---

## Critical constraints

1. **Unidirectional dependency** (E.5.3) — Tooling references Core, not reverse
2. **No Core duplication** — reference, not replicate
3. **Operational focus** — how, not why (why lives в Core)
4. **Russian primary** + English citations
5. **Code examples** где applicable

---

## Success criteria

- [ ] D6 Core read fully for reference
- [ ] 8 sections written
- [ ] All пять pre-commit hooks documented
- [ ] Agent workflows concrete
- [ ] Ritual protocols operational
- [ ] Commit + push successful

**END OF STAGE E TASK PROMPT**
