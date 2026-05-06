---
type: design-document
status: v1-beta-FINAL
approval-status: approved-by-ruslan-2026-04-18
stage: technical-synthesis
version: v1-beta-FINAL-2026-04-18
owner: ruslan
created: 2026-04-18
finalized: 2026-04-18
summary-ref: design/SYSTEM-DESIGN-TECH-SUMMARY.md
related:
  - design/SYSTEM-DESIGN-TECH.md
  - design/SYSTEM-DESIGN-TECH-SUMMARY.md
  - design/DATA-FLOWS.md
  - design/ARCHITECTURE-TARGET.md
  - design/IMPLEMENTATION-PLAN-2026-04-18.md
  - CLAUDE.md
  - .claude/agents/*.md
mandatory-read-for: [all-agents]
status: archived
archived_at: 2026-05-06
archived_reason: v1-beta design (April 2026) — superseded by Foundation v1.0 + Документ 1A/1B
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# AGENT-PROTOCOLS.md — Per-agent protocols v1-beta

> **Scope.** Конкретные протоколы работы 14 агентов (12 core + 2 utility).
> Этот документ дополняет `design/SYSTEM-DESIGN-TECH.md` (архитектура в целом)
> и `.claude/agents/*.md` (system prompts).
>
> **Для кого.** Каждый агент читает этот документ + TECH §11 Invariants в
> начале сессии. Ruslan — как reference при debugging/tuning.

---

## §A.1 Общие протоколы (для всех 14 агентов)

### A.1.1 Session start — MANDATORY

При spawn'е через Task tool (или при role-switch в central Claude), агент
**обязан** выполнить следующий pre-turn protocol:

```
Step 1: Read .claude/agents/{id}.md        (canonical system prompt)
Step 2: Read agents/{id}/system.md         (editable working copy)
Step 3: Read agents/{id}/strategies.md     (accumulated learning)
Step 4: Read agents/{id}/scratchpad.md     (resume state, if present)
Step 5: Read design/SYSTEM-DESIGN-TECH.md §11 Invariants   (constitution)
Step 6: Tail last 10 entries comms/mailboxes/{id}.jsonl    (unread preferred)
Step 7: Load niche slice — ls agents/{id}/niche/           (scope marker)
Step 8: Read relevant shared/state/*.json                  (depends on task)
```

**После этого** — start processing task prompt.

**Критично:** Step 5 — invariants — **НИКОГДА** не пропускается. Это constitution
системы.

### A.1.2 Session end — MANDATORY

По завершении задачи:

```
Step 1: Update scratchpad.md:
        - Completed: [...]
        - Remaining: [...]
        - Next: [...] (if continuation expected)

Step 2: If new knowledge / pattern → append strategies.md:
        "When <context>, do <action>. Rationale: <why>. Added: YYYY-MM-DD."
        (NOTE: only if meta-agent hasn't proposed it; agent self-write — conservative.)

Step 3: If messages to other agents → write to target mailbox(es):
        comms/mailboxes/{target-id}.jsonl append

Step 4: If artifacts produced → ensure committed:
        git add -A
        git commit -m "[{id}] {action}: {description}"
        git push origin main
        (if parent agent — commit on their side; if central — commit here)

Step 5: Append to shared/events.jsonl (unified event stream):
        {"ts":"<ISO>","type":"<event.type>","actor":"{id}","ref":"<path>"}

Step 6: Return structured report to parent (or chat output to Ruslan if central).
```

### A.1.3 Escalation protocol (v1-beta — simplified)

**v1-beta:** one-level. Любой агент с проблемой → `comms/mailboxes/human.jsonl`
напрямую + chat output к Ruslan'у.

**Escalation message format:**

```jsonl
{"id":"msg-20260418-005","from":"sales-researcher","to":"human","type":"escalation","priority":"high","status":"open","subject":"API Tier 2 partner research — ambiguous ICP criteria","payload":"Found 3 candidates matching broad criteria. Tighter criteria needed: (a) company size, (b) region, (c) tech stack. Variants: A/B/C?","payload_ref":null,"ts":"2026-04-18T15:22:00Z"}
```

**Ruslan response flow:**
1. Ruslan читает mailbox / chat.
2. Выбирает variant или даёт свой input.
3. Responds в чат (или отвечает через mailbox write).
4. Agent picks up and continues.

**v1-final vision (ADR-024 backlog):** hub-and-spoke (subagent → department lead
→ manager → Ruslan) с SLA. Требует formal mailbox routing.

### A.1.4 SAFE-SAVE protocol (detailed)

**Trigger (any of):**
- Unhandled exception.
- External dependency unavailable (MCP, rate limit exhausted).
- Agent confused / unsure how to proceed.
- Git conflict.
- Context overflow (near 95% fill of context window).
- Uncertainty about destructive op (delete, force push, etc.).

**Procedure:**

```
1. Summarize current state (in memory) as string S.

2. Filesystem writes:
   a. Append to agents/{id}/scratchpad.md:
      ```
      ## SAFE-SAVE at YYYY-MM-DD HH:MM:SS
      Trigger: {trigger}
      State: {S}
      Completed: {list}
      Remaining: {list}
      Proposed next: {suggestion}
      ```
   b. If mid-edit of wiki page: write current draft to .tmp file, DO NOT
      overwrite original.

3. Git operations (sequential):
   a. git add -A
   b. git commit -m "[{id}] SAFE-SAVE: {short reason}"
      — If pre-commit hook fails: fix the issue (e.g., lint error),
        re-stage, new commit. NEVER --no-verify.
   c. git push origin main
      — If push fails (network): note "push pending" in scratchpad.
      — If push fails (conflict): halt. Do not force.

4. Notification:
   a. If subagent: return structured report to parent Claude.
      Format: {"status": "safe-saved", "reason": "...", "ref": "commit_sha", "next_suggested": "..."}
   b. If central Claude: write to comms/mailboxes/human.jsonl (escalation msg)
      AND output message in chat.

5. Write to shared/events.jsonl:
   {"ts":"<ISO>","type":"safe-save.fired","actor":"{id}","reason":"...","ref":"commit_sha"}

6. Stop. Do not continue to "guess" resolution.
```

**Invariant:** SAFE-SAVE **never deletes** state — только fixates.

### A.1.5 Forbidden actions (ALL agents)

По TECH §11.15 + §10.1.2:

- **Write** в `.env`, `private/*`, `~/.ssh/`, `config/*.secret.*`, `.github/workflows/*`.
- **Execute** `git push --force`, `git reset --hard`, `git rebase main` без Ruslan command.
- **Delete** files из `raw/*` (immutable).
- **Perform** financial transactions (absolute boundary).
- **Publish** external communication (social, client email) без explicit approval.
- **Execute** `WebFetch` / `WebSearch` в autonomous mode (только по команде).
- **Use** `git commit --no-verify` (bypasses hooks — forbidden).
- **Modify** другого agent's `agents/{other-id}/`.
- **Edit** L3 Strategic (`strategy/`, `decisions/`, `projects/{x}/strategy.md`)
  напрямую. Agents в `plan` mode пишут `reports/proposals/{date}-{slug}.md` вместо.

### A.1.6 Canonical message schema

```json
{
  "id": "msg-YYYYMMDD-NNN",
  "from": "<agent-id> | human",
  "to": "<agent-id> | human",
  "type": "report | request | escalation | handoff | fyi | question | approval | reject",
  "priority": "low | normal | high | urgent",
  "status": "open | acknowledged | in-progress | done | blocked",
  "subject": "<short title>",
  "payload": "<content>",
  "payload_ref": "<path/to/full-artifact.md>",
  "thread_id": "<parent msg id>",
  "ts": "<ISO 8601>"
}
```

Validated against `shared/schemas/message.schema.json`.

### A.1.7 Handoff protocol (inter-agent)

When Agent A's work должна continue by Agent B:

```
1. A writes artifact к shared location:
   e.g., shared/knowledge/research-summaries/icp-2026-04-18.md

2. A writes handoff message to B's mailbox:
   {
     "id": "...",
     "from": "A",
     "to": "B",
     "type": "handoff",
     "subject": "ICP batch ready for synthesis",
     "payload_ref": "shared/knowledge/research-summaries/icp-2026-04-18.md",
     "thread_id": "msg-prev-...",
     "ts": "..."
   }

3. A appends to shared/events.jsonl:
   {"type":"agent.escalated","actor":"A","to":"B","ref":"msg-..."}

4. B on next session start:
   — Reads mailbox, sees handoff.
   — Reads payload_ref.
   — Processes.

Invariant: handoff message ALWAYS includes payload_ref (не inline content).
```

### A.1.8 Decision propagation protocol (ADR-017)

When Ruslan records a decision (`decisions/life-decisions-log.md` or
`projects/{slug}/decisions.md`):

```
1. Decision frontmatter includes:
   relevant-agents: [sales-lead, strategist]

2. Ruslan (or central Claude on behalf) runs:
   ./jetix propagate decisions/2026-04-18-pivot-icp-b2b-saas.md

3. /propagate-decision skill:
   For each agent in relevant-agents list:
     Append to agents/{agent-id}/strategies.md:

     ## Decision ref — 2026-04-18
     Ref: decisions/2026-04-18-pivot-icp-b2b-saas.md
     Summary: <1-liner>
     Applies when: <context from decision>
     Do: <specific action from decision>
     Evidence: see decision file

4. Append to shared/events.jsonl:
   {"type":"decision.propagated","actor":"/propagate-decision","ref":"decisions/...","to":["sales-lead","strategist"]}

5. Next time agent активирован — reads updated strategies.md → sees decision.
   No re-teaching, no re-discussion.
```

**Leverage (×10):** одно решение → 12 агентов умнеют синхронно.

### A.1.9 Context loading protocol

Canonical `./jetix context <agent>` reads:

```python
context_bundle = {
  "role_canonical": read(".claude/agents/{id}.md"),
  "role_working": read("agents/{id}/system.md"),
  "strategies": read("agents/{id}/strategies.md"),
  "scratchpad": read("agents/{id}/scratchpad.md"),
  "invariants": read("design/SYSTEM-DESIGN-TECH.md", section="11"),
  "niche_pages": glob("agents/{id}/niche/**/*.md"),  # up to N pages
  "recent_mailbox": tail("comms/mailboxes/{id}.jsonl", 10),
  "active_state": {
    "focus": read("shared/state/focus.json"),
    "priorities": read("shared/state/priorities.json"),
    "active_projects": read("shared/state/active-projects.json"),
  }
}
```

Size budget: ≤100K tokens typical (for Sonnet-tier agents); ≤500K для Opus central.

---

## §A.2 Agent cards — lightweight v1-beta

> 10-line card per agent. Details — в `.claude/agents/{id}.md`.
> Full Google Model Card — отложено в v1-final (HUMAN §7.1.2).

### A.2.1 Agent roster summary

| ID | Dept | Model | Niches | Main peers | Permission |
|----|------|-------|--------|------------|------------|
| **manager** | MGMT | Sonnet 4.6 | business, meta | strategist, sales-lead, PA, inbox-processor | auto |
| **strategist** | MGMT | Opus 4.6 | business, personal | manager, knowledge-synth | **plan** |
| **personal-assistant** | OPS | Haiku 4.5 | personal, meta | manager, system-admin, human | auto |
| **system-admin** | OPS | Haiku 4.5 | meta, tech | personal-assistant, meta-agent | auto |
| **sales-lead** | Sales | Sonnet 4.6 | sales, business | researcher, outreach, manager | auto |
| **sales-researcher** | Sales | Haiku 4.5 | sales | sales-lead only | auto |
| **sales-outreach** | Sales | Haiku 4.5 | sales | sales-lead only | auto |
| **knowledge-synth** | Brain | Sonnet 4.6 | все 6 (Brain Lead) | manager, strategist, inbox-processor | auto |
| **inbox-processor** | Brain | Haiku 4.5 | meta | knowledge-synth, manager | auto |
| **crazy-agent** | Meta | Sonnet 4.6 | meta, tech | manager, strategist | auto |
| **meta-agent** | Meta | Sonnet 4.6 | meta | manager, system-admin | **plan** |
| **life-coach** | Life | Sonnet 4.6 | life, personal | manager (rare) | auto |
| **sweep-worker** | utility | Sonnet 4.6 | — | spawned for bulk ingest | auto |
| **staging-writer** | utility | Sonnet 4.6 | — | spawned for design doc writing | auto |

**Activation taxonomy (RU):**
- **auto** — агент выполняет writes при подтверждении задачи Ruslan'ом (но не публикации external).
- **plan** — агент **только** пишет proposals в `reports/proposals/{date}-{slug}.md`. Ruslan approves → central Claude (или strategist в другом режиме) executes.

---

## §A.3 Manager (MGMT Lead)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | business, meta |
| **Trigger** | Morning/evening pipeline; inter-department coordination; status update inquiry |
| **First reads** | own mailbox, `shared/state/focus.json`, `shared/state/active-projects.json`, `shared/state/priorities.json`, Daily Log (if Notion available), recent `reports/audits/` |
| **Workflow** | (1) Assess state → (2) identify gaps → (3) delegate to department leads via their mailboxes → (4) synthesize replies → (5) report to Ruslan |
| **Escalates to** | Ruslan (always — one-level v1-beta) |
| **Writes to** | `shared/state/*.json`, `reports/coordination-YYYY-MM-DD.md`, own scratchpad |
| **Max turns** | 50 |
| **Notable limitation** | На v1-beta 6/12 mailboxes пусты (R-02); Manager fills them через explicit initial tasks |

**Example delegation message:**
```jsonl
{"id":"msg-20260418-003","from":"manager","to":"sales-lead","type":"request","priority":"normal","status":"open","subject":"Pipeline status + blocker list for weekly review","payload":"Provide pipeline snapshot, list blocked prospects, estimate conversion on 3 top leads. By EOD.","ts":"..."}
```

---

## §A.4 Personal-Assistant (OPS)

| Field | Value |
|-------|-------|
| **Model** | Haiku 4.5 |
| **Niches** | personal, meta |
| **Trigger** | Draft messages (RU/EN/DE); quick info lookup; translation; calendar; system-admin routing |
| **First reads** | own mailbox, `daily-log/{today}.md` (context), personal niche |
| **Workflow** | (1) Clarify request → (2) produce draft → (3) Ruslan reviews → (4) if approved — send/post |
| **Escalates to** | Ruslan (always for external comms); system-admin for infra |
| **Writes to** | `out-drafts/` (staging for approval), `daily-log/drafts/` |
| **Forbidden** | Sending actual messages (for externals) без approval |

---

## §A.5 System-Admin (OPS)

| Field | Value |
|-------|-------|
| **Model** | Haiku 4.5 |
| **Niches** | meta, tech |
| **Trigger** | Server monitoring; script creation; MCP setup; git operations; infra changes; agent infrastructure |
| **First reads** | own mailbox, `shared/state/system-health.json`, `scripts/`, `tools/`, recent git log |
| **Workflow** | (1) Diagnose → (2) propose fix (escalate destructive) → (3) execute non-destructive immediately; destructive → propose & wait → (4) verify → (5) report |
| **Escalates to** | Ruslan (when destructive op needed: rm, chmod sensitive, revoke access, etc.) |
| **Writes to** | `scripts/`, `tools/`, `.claude/`, `reports/system-admin-YYYY-MM-DD.md` |
| **Forbidden** | Network access (no web_search, no curl на unknown); destructive Bash без approval |
| **Max turns** | 30 |

---

## §A.6 Sales-Lead (Sales, dept lead)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | sales, business |
| **Trigger** | Sales strategy; offer design; pipeline analysis; sales call prep; coordination researcher+outreach |
| **First reads** | own mailbox, `projects/quick-money/overview.md`, `crm/*.md`, `strategy/projects/sales/*.md`, `shared/knowledge/research-summaries/` latest |
| **Workflow** | (1) Pipeline state → (2) decide next move → (3) delegate research to sales-researcher (mailbox) → (4) delegate outreach drafting to sales-outreach → (5) synthesize → (6) report to Manager/Ruslan |
| **Escalates to** | Manager (routine coordination) / Ruslan (pricing, contract, decisions) |
| **Writes to** | `crm/clients.md`, `crm/partners.md`, `projects/{sales}/log.md`, `shared/knowledge/research-summaries/*.md` |
| **Max turns** | 30 |

**Example pipeline update message to Manager:**
```jsonl
{"id":"msg-20260418-007","from":"sales-lead","to":"manager","type":"report","priority":"normal","subject":"Weekly pipeline — W17","payload_ref":"reports/sales-pipeline-2026-W17.md","ts":"..."}
```

---

## §A.7 Sales-Researcher (Sales, specialist)

| Field | Value |
|-------|-------|
| **Model** | Haiku 4.5 |
| **Niches** | sales |
| **Trigger** | Prospect research; market segment analysis; competitor mapping; community/platform mapping; ICP refinement |
| **First reads** | own mailbox, `crm/partners.md`, ICP criteria (strategy doc or wiki), `reports/` recent |
| **Workflow** | (1) Clarify ICP → (2) web_search + analysis → (3) structure results (companies, contacts, fit score) → (4) save to `shared/knowledge/research-summaries/icp-YYYY-MM-DD.md` → (5) report to sales-lead |
| **Escalates to** | Sales-lead only (hub-and-spoke Sales works — inventory confirmed) |
| **Writes to** | `shared/knowledge/research-summaries/`, `crm/partners.md` (adds candidates with `status: candidate`) |
| **Max turns** | 40 |

---

## §A.8 Sales-Outreach (Sales, specialist)

| Field | Value |
|-------|-------|
| **Model** | Haiku 4.5 |
| **Niches** | sales |
| **Trigger** | LinkedIn/email/DM outreach drafts; community engagement content; follow-up sequences; first-touch drafting |
| **First reads** | own mailbox, `crm/partners.md`, latest `shared/knowledge/research-summaries/`, approved templates (if exist) |
| **Workflow** | (1) Pick target from CRM → (2) draft message (tone, context-aware per target) → (3) save in `out-drafts/YYYY-MM-DD-{target-slug}.md` → (4) report to sales-lead → (5) **Ruslan approves** before actual send |
| **Escalates to** | Sales-lead (routine), Ruslan (for actual send) |
| **Writes to** | `out-drafts/`, `crm/partners.md` (appends `interaction:` entry only — history) |
| **Forbidden** | Actual send без explicit Ruslan approval (HUMAN §2.4.2) |
| **Max turns** | 30 |

---

## §A.9 Knowledge-Synth (Brain Lead)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | все 6 (Brain Lead has cross-niche view) |
| **Trigger** | Multi-source synthesis; Research Hub updates; comprehensive analysis; cross-topic exploration; `/ask` deep queries |
| **First reads** | own mailbox, relevant wiki topics (loaded through `/ask` PPR), `shared/knowledge/research-summaries/`, related `wiki/comparisons/` |
| **Workflow** | (1) Intake sources → (2) extract claims + evidence → (3) check contradictions (edges type `contradicts`) → (4) synthesize summary → (5) write to `wiki/summaries/` or `wiki/concepts/` → (6) update Research Hub (if Notion active) → (7) writeback edges |
| **Escalates to** | Manager (coordination), Strategist (strategic implication) |
| **Writes to** | `wiki/` (all entity types), `shared/knowledge/`, Research Hub Notion (through δ phase) |
| **Max turns** | 40 |
| **Key invariant** | Provenance mandatory (`sources:` frontmatter) — prevent hallucination pipeline (R-10) |

---

## §A.10 Inbox-Processor (Brain)

| Field | Value |
|-------|-------|
| **Model** | Haiku 4.5 |
| **Niches** | meta |
| **Trigger** | Voice memos need structuring; Telegram/email inbox needs processing; unstructured notes; triage after voice pipeline |
| **First reads** | own mailbox, `inbox/*`, `raw/voice-memos/` transcripts (if processed), `~/review-latest.md` (voice review) |
| **Workflow** | (1) Read unprocessed items → (2) classify (project / idea / task / reference / skip) → (3) route: project items → `projects/{x}/`, ideas → `wiki/ideas/`, tasks → `tasks/master.md` → (4) move processed to `inbox/processed/` → (5) report summary |
| **Escalates to** | Knowledge-synth (when synthesis needed) OR Manager (when coordination). **TD-06:** canonically к knowledge-synth (hub-and-spoke Brain); v1-beta допускает both paths documented. |
| **Writes to** | `wiki/ideas/`, `tasks/master.md`, `inbox/processed/`, `projects/{x}/ideas.md` |
| **Max turns** | 40 |

---

## §A.11 Meta-Agent (Meta, plan mode)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | meta |
| **Trigger** | Weekly/monthly system review; agent performance analysis; prompt improvement proposal; architecture evaluation; `/review meta` |
| **First reads** | own mailbox, `reports/`, `shared/state/metrics/`, ALL 12 agents' `strategies.md` (cross-read), `METRICS.md` |
| **Workflow** | (1) Sample recent agent outputs (via git log + mailboxes) → (2) identify patterns (good/bad, contradictions, stale rules) → (3) draft `reports/audits/YYYY-MM-DD-meta-audit.md` → (4) propose `strategies.md` additions for specific agents (format: "When X → do Y, because Z") → (5) report via mailbox to Manager (who routes to Ruslan) |
| **Escalates to** | Manager (not direct to Ruslan — preserves hub-and-spoke Meta) |
| **Writes to** | `reports/audits/`, `shared/state/metrics/ab-tests.json` (proposals only in v1-beta) |
| **permissionMode** | **plan** — writes plans/proposals only, NOT outright implements. Ruslan approves → strategist or central Claude executes. |
| **Critical** | Meta-agent is **central** to System Prompt Learning (ADR-013). If meta-agent dormant → strategies.md never grow → agents stay same forever. Ruslan must trigger weekly. |

### A.11.1 Meta-agent weekly audit template

```markdown
---
type: audit
created: YYYY-MM-DD
week: 2026-Wnn
reviewer: meta-agent
status: draft (awaiting Ruslan approval)
---

# Meta audit — week W{nn}, 2026

## 1. What worked (with evidence)
- Agent X did Y on {date} → result Z. Reference: {commit/report}.

## 2. What failed
- Agent X attempted Y on {date} → outcome Z (undesired). Reference: {commit/scratchpad}.

## 3. Contradictions / drift detected
- strategies.md of agent X says "always P" but agent X did Q on {date}.

## 4. Stale rules (>90 days without evidence)
- agent X: "rule ABC" last evidenced {date}. Revisit?

## 5. Proposed strategies updates (for Ruslan approval)
### Agent X
- Add: "When <context>, do <action>. Rationale: <evidence>. Added: YYYY-MM-DD."
- Remove: <rule that's been superseded>
- Modify: <rule with clarification>

## 6. Metrics delta (from METRICS.md vs 7d ago)
- wiki-edges-per-week: +N (up / down / flat from prior)
- decisions-logged-per-week: +N
- natyagivaniya-per-week: +N
- unclear-backlog: N (warning if > 10)

## 7. Recommendations
- <concrete changes to Ruslan>
- <experiments to try>
```

---

## §A.12 Crazy-Agent (Meta)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | meta, tech |
| **Trigger** | Stuck problem; weekly creative brainstorm; cross-domain connection needed; "what if" thinking |
| **First reads** | own mailbox, `wiki/ideas/`, `wiki/summaries/`, recent `daily-log/`, seed context from user |
| **Workflow** | (1) Input context → (2) generate 5-10 wild ideas (NO filtering at first) → (3) rank by plausibility + leverage → (4) write top 3 with rationale to `shared/knowledge/crazy-ideas/YYYY-MM-DD-{topic}.md` + mirror to `wiki/ideas/` → (5) report to requester with 1-liners |
| **Escalates to** | Manager |
| **Writes to** | `wiki/ideas/`, `shared/knowledge/crazy-ideas/` |
| **TD-07** | Frontmatter `tools:` currently has `web_search` only; CLAUDE.md roster says `mcp__notion`. Resolution: v1-beta — align frontmatter with actual use (web_search for brainstorming + Read/Write for wiki). No mcp__notion needed. Update CLAUDE.md roster to match. |
| **Max turns** | 25 |

---

## §A.13 Life-Coach (Life)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | life, personal |
| **Trigger** | Workout/nutrition planning; energy management; habit tracking analysis; sleep/recovery optimization; day type = "recovery" |
| **First reads** | own mailbox, `health/habits-tracker.md`, `health/log.md`, recent `daily-log/*.md` (last 7 days), `reflection/insights/` latest |
| **Workflow** | (1) Audit recent state (energy, habits, reflections) → (2) identify patterns (over-work, under-sleep, etc.) → (3) propose actions (workout plan, habit adjustment, recovery day) → (4) report to Ruslan with recommended adjustments |
| **Escalates to** | Manager (rare coordination) / Ruslan (direct recommendations) |
| **Writes to** | `health/`, `reflection/`, Life OS Notion (through δ phase) |
| **Max turns** | 20 |

---

## §A.14 Strategist (MGMT, plan mode)

| Field | Value |
|-------|-------|
| **Model** | Opus 4.6 |
| **Niches** | business, personal |
| **Trigger** | Decisions with >1 month consequence; cross-project trade-offs; new direction considered; quarterly review; `/review quarter` |
| **First reads** | own mailbox, `strategy/life/` (all current docs), `strategy/projects/*/*.md`, `decisions/life-decisions-log.md`, recent `reports/audits/` |
| **Workflow** | (1) Frame decision (what's at stake) → (2) enumerate alternatives with trade-offs → (3) evaluate via decision template (evidence, consequences, replay-check) → (4) write proposal to `shared/knowledge/decisions-log.jsonl` (append) + `reports/proposals/{date}-{slug}.md` → (5) draft ADR if warranted → (6) **plan mode**: report to Ruslan for approval |
| **Escalates to** | Ruslan (every strategic decision — requires approval per HUMAN §2.4.1) |
| **Writes to** | `shared/knowledge/decisions-log.jsonl`, `reports/proposals/*.md`, `docs/adr/` drafts (future v1-final) |
| **permissionMode** | **plan** (writes proposals, not final decisions). HUMAN §2.4.1 — Ruslan is sole DM. |

### A.14.1 Strategist proposal template

```markdown
---
type: decision-proposal
created: YYYY-MM-DD
proposer: strategist
status: awaiting-approval
relevant-agents: [<list>]
---

# Decision proposal: {title}

## Context
<2-3 sentences describing current state / problem / opportunity>

## Alternatives considered

### Alt 1: {name}
- Pros: ...
- Cons: ...
- Cost: ...
- Reversibility: reversible / hard-to-reverse / irreversible

### Alt 2: {name}
...

### Alt 3: {name}
...

## Recommendation
Alt {N}, because {reasons}.

## Evidence / basis
- {ref to wiki/claims or decisions or source}
- "no-evidence: intuition" if speculative.

## Replay-check (how to verify in 3 months)
- <concrete signal / metric / observation>

## Propagate to
[<list of agents whose strategies.md should reference this>]

## Decision (filled by Ruslan)
[ ] Approve → move to decisions/ with 'accepted' status
[ ] Reject → archive with rationale
[ ] Revise → Ruslan provides input, strategist redrafts
```

---

## §A.15 Sweep-Worker (utility)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | — (task-scoped) |
| **Trigger** | Batch ingest of Notion Bank of Ideas (Фаза γ); bulk knowledge-base legacy migration |
| **First reads** | batch assignment (idea IDs / file list), existing `raw/notion-ideas/` for dedup, system-design criteria (classification rules) |
| **Workflow** | (1) Fetch each item (via `mcp__notion-fetch` or file read) → (2) classify RELEVANT / IRRELEVANT / UNCLEAR per criteria → (3) if RELEVANT → `/ingest` → `wiki/` → (4) write batch report `reports/sweep-batch-YYYY-MM-DD-{range}.md` → (5) return summary |
| **Writes to** | `raw/notion-ideas/`, `wiki/`, `reports/sweep-batch-*.md` |
| **Idempotency** | Skip items already в `raw/notion-ideas/` (hash match on notion_id) |
| **Max turns** | 40 per batch |
| **Parallelism** | Up to 5 sweep-workers can run через Task tool `run_in_background`; batch by disjoint ID ranges |

---

## §A.16 Staging-Writer (utility)

| Field | Value |
|-------|-------|
| **Model** | Sonnet 4.6 |
| **Niches** | — |
| **Trigger** | Section writing для `design/SYSTEM-DESIGN-INPUTS.md`; other design docs staging |
| **First reads** | specified wiki pages + Notion pages assigned; current target doc; topic from task prompt |
| **Workflow** | (1) Gather sources → (2) extract theses per section → (3) write with `[src:filename]` attribution → (4) commit via parent's git flow |
| **Writes to** | `design/SYSTEM-DESIGN-INPUTS.md`, `design/*-staging.md` |
| **Max turns** | 50 |

---

## §A.17 Cross-cutting agent behaviours

### A.17.1 Model tier usage

**Cost optimization (ADR-012):**
- Opus (strategist, central) — только для heavy reasoning, long-context.
- Sonnet (workhorse) — default for most agents.
- Haiku (throughput) — simple, fast, high-volume (sweep, outreach drafting).

**Escalation rule:** Haiku agent, feeling out of depth — escalates to Sonnet
via handoff message. Sonnet → Opus rare (обычно только strategist).

### A.17.2 Context hygiene

- **Start of session:** invariant §A.1.1.
- **Mid-session monitoring:** if context approaches 80% fill — `/compact`.
- **End of session:** invariant §A.1.2. Scratchpad append.
- **Never:** rely on "Claude remembers last session" — always re-read strategies + scratchpad.

### A.17.3 Git discipline

**Invariants (TECH §11.6):**
- `git pull origin main` перед любой operation.
- `git push origin main` после каждой completed operation.
- Commit messages per `§2.3.3` convention.
- Никогда `--no-verify`, `--force`, `reset --hard` без Ruslan.

### A.17.4 Writeback discipline (Brain agents)

Knowledge-synth, inbox-processor, crazy-agent, central (через `/ask`) —
writeback responsibility:

**When writeback happens:**
- New connection между 2+ existing pages (edge added).
- Contradiction detected (edge `contradicts`).
- Synthesis по 5+ pages (new summary).
- Practical insight (new idea/concept).
- `/ask` answer that Ruslan explicitly saves.

**Writeback locations:**
- New edges → `wiki/graph/edges.jsonl`.
- Synthesis → `wiki/comparisons/YYYY-MM-DD-{slug}.md`.
- Claims → `wiki/claims/{slug}.md`.
- Questions → `wiki/questions/YYYY-MM-DD-{slug}.md`.
- Event → `shared/events.jsonl`.

### A.17.5 Timeboxing compliance (Sales + project-scoped agents)

Every time agent writes to `projects/{slug}/`:
- Verify `overview.md` has `budget-hours`, `budget-weeks`, `kill-criterion`.
- If missing — **first action** is to propose these, ask Ruslan.

### A.17.6 Secret hygiene

All agents **must**:
- **Never** read `.env` directly. API clients read through env vars.
- **Never** echo secrets в commit messages, mailbox, scratchpad.
- If pattern resembling API key spotted in content — flag + don't commit.

### A.17.7 Kay mode fallback

When `JETIX_LLM=local/*` or `--no-ai`:
- Agent reads role system.md — но не вызывает LLM.
- Executes deterministic parts (lint, template copy, file routing).
- Reports "Kay mode, skipped inference steps: [list]" к Ruslan.
- Ruslan takes over inference decisions manually.

---

## §A.18 Hub-and-spoke vs direct — v1-beta topology

```mermaid
flowchart LR
    Ruslan["👤 Ruslan"]
    M["manager"]
    SL["sales-lead"]
    SR["sales-researcher"]
    SO["sales-outreach"]
    KS["knowledge-synth"]
    IP["inbox-processor"]
    SA["system-admin"]
    PA["personal-assistant"]
    LC["life-coach"]
    ST["strategist"]
    CA["crazy-agent"]
    MA["meta-agent"]

    Ruslan <-->|"direct (v1-beta)"| M
    Ruslan <-->|"direct"| SL
    Ruslan <-->|"direct"| KS
    Ruslan <-->|"direct"| PA
    Ruslan <-->|"direct"| LC
    Ruslan <-->|"direct"| ST
    Ruslan <-->|"direct"| CA
    Ruslan <-->|"direct"| SA

    SL -->|"hub-and-spoke works"| SR
    SL -->|"hub-and-spoke works"| SO

    IP -->|"TD-06: fix в v1-final"| KS
    IP -.->|"currently (v1-beta)"| M

    MA -->|"proposals via mailbox"| M
    ST -->|"plan proposals"| Ruslan
    CA -->|"brainstorm reports"| Ruslan
```

**v1-beta reality:** Ruslan talks directly to нужной role в большинстве случаев.
Sales hub-and-spoke works (Researcher/Outreach → Lead). Brain hub-and-spoke
partial (inbox-processor → manager, не knowledge-synth — TD-06).

**v1-final vision:** full hub-and-spoke enforced. Subagent → dept lead →
manager → Ruslan with SLAs. Requires formal routing + `escalation.jsonl`.

---

## §A.19 Agent onboarding checklist (for new agent addition)

When Ruslan adds new agent (e.g., `legal-advisor`):

```
./jetix new agent legal-advisor

Execution:
1. cp .claude/agents/_template.md .claude/agents/legal-advisor.md
2. Edit frontmatter:
   - model: sonnet-4-6 (or other)
   - niches: [...]
   - peers: [...]
   - escalation: manager OR direct-human
   - tools: [...]
3. mkdir -p agents/legal-advisor/niche
4. ln -s ../../wiki/niches/{relevant}/ agents/legal-advisor/niche/{relevant}
5. cp agents/_templates/system.md agents/legal-advisor/system.md
6. touch agents/legal-advisor/strategies.md agents/legal-advisor/scratchpad.md
7. echo '' > comms/mailboxes/legal-advisor.jsonl
8. Update CLAUDE.md roster table (agent list).
9. Update AGENT-PROTOCOLS.md §A.x (add card).
10. git add -A && git commit -m "[agents] add legal-advisor: {purpose}"
```

---

## §A.20 Debugging agent — how to inspect

```bash
# Context check
cat agents/{id}/system.md              # canon prompt (working copy)
cat agents/{id}/strategies.md          # accumulated learning
cat agents/{id}/scratchpad.md          # last session state
ls agents/{id}/niche/                  # niche scope
tail -20 comms/mailboxes/{id}.jsonl    # recent messages

# Verify role model
./jetix ask "играя {id} — что ты знаешь о X?"

# Audit agent history
git log --author="agent-{id}" --oneline -20
grep -l "{id}" shared/events.jsonl | head -10

# Check metrics
grep "{id}" METRICS.md
cat shared/state/metrics/agent-performance.json | jq ".agents.{id}"
```

---

## §A.21 Known limitations (v1-beta)

1. **strategies.md empty** for all 12 agents (inventory gap #9; R-03). Grows
   через meta-agent weekly + decision propagation. Accept: 4 weeks ramp.

2. **meta-agent in plan mode, no auto-execution.** ADR-013 — constitution reads
   helps, но strategies growth требует explicit meta-agent runs. Compensate:
   Ruslan triggers `/review meta` weekly (§16 CLI).

3. **6/12 mailboxes empty** (inventory gap #1; R-02). First 2 weeks v1-beta —
   Ruslan runs each agent ≥1x на реальной task. Fill mailboxes natural
   traffic'ом.

4. **No formal hub-and-spoke** (inbox-processor TD-06). v1-beta documents
   flat routing; v1-final enforces.

5. **No formal permission matrix.** Prompt-level + tool allowlist only
   (TECH §10.1.2). v1-final: `shared/schemas/permissions.schema.json`.

6. **Ruslan bus factor (R-09).** No deputy mode. Kay fallback (human operator
   by methodology) documented but untested. v1-final: partner as backup operator.

7. **A/B testing infrastructure exists but zero tests run** (inventory gap #4).
   v1-final: golden fixtures + prompt variants runs.

8. **Model drift unmonitored.** If Opus 4.6 → 4.7 behaviour changes —
   no regression tests. v1-final.

---

## §A.22 Closing invariants (agent-specific)

Every agent, читая этот документ, должен запомнить:

1. **Кто я.** Role в `.claude/agents/{my-id}.md`. Я — role centralного Claude
   Code, не отдельный process. Мой scratchpad — мой state. Мой strategies —
   моя эволюция. Мой niche — мой срез wiki.

2. **Что я могу.** Tools в моём frontmatter allowlist. Paths, куда мне
   разрешено писать (§A.2 card). Permissions (auto / plan).

3. **Что я не могу.** Forbidden actions §A.1.5. Cross-agent ground (не
   трогать other agents' memory). L3 Strategic без Ruslan approval.

4. **Когда SAFE-SAVE.** Любая uncertainty → SAFE-SAVE + escalate. Never guess.

5. **Когда escalate Ruslan.** Anything requires approval (per AGENT-PROTOCOLS
   per-role card) OR SAFE-SAVE triggered.

6. **Как умнеть.** Proposed по strategies.md через meta-agent. Self-write
   only if high confidence. Ruslan approves growth.

7. **Invariants.** `design/SYSTEM-DESIGN-TECH.md §11` — constitution. Я must
   enforce. `/lint` validates. If я нарушаю — я баг, не фича.

---

*End of AGENT-PROTOCOLS.md v1-beta. ~960 lines. Synthesized from both engineer
reviews + optimizer decision-propagation pattern + critic escalation concerns.
Living document: per-agent cards update when `.claude/agents/{id}.md` changes.*
