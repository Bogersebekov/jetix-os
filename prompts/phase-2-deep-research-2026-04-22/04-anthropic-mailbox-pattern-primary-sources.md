---
id: phase-2-04-anthropic-mailbox-primary-sources
title: Anthropic Mailbox Pattern — Primary-Source Verification — Perplexity Deep Research
author: cloud-cowork
date: 2026-04-22
tool: Perplexity Pro Deep Research
priority: P1
gap-coverage: Domain 2 MAJOR #3 (no official Anthropic engineering blog on mailbox pattern)
related-architecture: comms/mailboxes/<agent>.jsonl (Jetix Phase 2+ coordination layer), Decision 17 (filesystem = single source of truth)
status: ready-to-run
---

# Anthropic Mailbox Pattern — Primary-Source Verification Prompt

## Как использовать

1. Открой Perplexity Pro в **Deep Research** режиме
2. Скопируй блок ниже от `===BEGIN PROMPT TO PASTE===` до `===END PROMPT TO PASTE===`
3. Paste + submit. Wait 15-20 минут.
4. Сохрани output в `raw/research/phase-2-deep-research-2026-04-22/RESULT-04-mailbox.md`
5. Скажи Cloud Cowork — Phase 3 synthesis начнётся.

## Context для понимания (не копируй в Perplexity)

Jetix current architecture определяет `comms/mailboxes/<agent>.jsonl` как основной inter-agent communication layer. Этот паттерн описан как "Anthropic mailbox pattern" в нескольких secondary-source references (Erik Schluntz personal blog, Mike Krieger tweet thread, WaveSpeed leaked materials Apr 2026). Но **не существует официального Anthropic engineering blog post** который явно документирует этот паттерн. Phase 1 inventory зафиксировала это как Domain 2 MAJOR gap.

До Phase 2 implementation нужна ground truth:
- (a) Существует ли official Anthropic writeup? (URL, дата, authors)
- (b) Является ли "mailbox pattern" корректной интерпретацией Claude Code / sub-agent internals?
- (c) Каковы production-scale failure modes JSONL mailbox'ов?
- (d) Верифицируема ли WaveSpeed Apr 2026 "leak" — реальный source code или fabricated?
- (e) Alternatives к JSONL (Temporal, Inngest, Kafka, in-memory queue, SQLite queue) — tradeoffs для solo-founder budget

Связанные уже-имеющиеся материалы (не повторять):
- Perplexity Apr 22 Domain 2 §mailbox — mentions pattern, no official source
- R-7 Boris Cherny Claude Code principles — но нет mailbox-specific disclosure
- R-8 Skills / CLAUDE.md — nope
- R-2 Swarm Intelligence §mailbox — short section

---

## ===BEGIN PROMPT TO PASTE===

I need a deep primary-source verification research on the **"Anthropic mailbox pattern" for multi-agent / sub-agent coordination in Claude Code and related systems**. This is for an architectural decision on whether to adopt, modify, or replace a JSONL-file mailbox pattern in a production multi-agent system. Cite every claim. Prefer primary sources (Anthropic official) over secondary interpretations. Admit uncertainty. Flag rumors vs. verified.

## Background and the specific thing I need to verify

Multiple 2025-2026 secondary sources refer to an "Anthropic mailbox pattern" for inter-agent communication in Claude Code — described as JSONL-file queues, `.jsonl` per agent, message-passing with schema validation, append-only semantics. My current understanding is derived from:

- Erik Schluntz (Anthropic) personal blog posts and conference talks
- Mike Krieger (Anthropic CPO) tweet threads
- Boris Cherny (Claude Code architect) talks and blog posts
- Claimed "leaked Claude Code source code" via WaveSpeed (Apr 2026) — unverified provenance
- Secondary analyses on Reddit r/ClaudeAI, Hacker News, personal Substacks

**I do not know if an official Anthropic engineering blog post explicitly documents this pattern.** I need to find out.

## Research scope — 7 concrete sub-domains

### Sub-domain A — Official Anthropic publications on multi-agent communication

Exhaustive search of:

- anthropic.com/engineering/ (engineering blog)
- anthropic.com/research/ (research section)
- anthropic.com/news/ (announcements)
- docs.anthropic.com/en/docs/claude-code/ (Claude Code docs)
- docs.anthropic.com/en/docs/agents-and-tools/ (agent docs)
- Anthropic's GitHub (github.com/anthropics/*) — any open-source references to mailbox / inter-agent queues
- Anthropic's tech talks on YouTube (Anthropic channel, AI Engineer Summit, Code with Claude event, AI Eng World's Fair)
- Anthropic papers on arXiv (specifically "How we built our multi-agent research system" Jun 2025 and any successors)
- Anthropic Developer Hub, Anthropic Discord announcements, Anthropic Newsletter

**Specific question**: Does any official Anthropic resource explicitly use the term "mailbox", "inbox", "message queue", "inter-agent queue", or describe a JSONL-based inter-agent coordination mechanism? For each hit: URL + date + exact quote.

### Sub-domain B — Anthropic engineers' personal channels (primary-source)

- Erik Schluntz (Anthropic) — blog, tweets, talks where he discusses Claude Code internals
- Mike Krieger (Anthropic CPO) — relevant discussions of agent coordination
- Boris Cherny (Claude Code creator) — all talks 2024-2026 (AI Engineer Summit, conferences); does he describe mailbox pattern?
- Catherine Olsson (Anthropic) — interpretability work relevant to inter-agent signals
- Kyle Turner / Tom Brown / Dario Amodei — if any discuss agent architecture in interviews
- Anthropic engineering employees' Substacks / Medium / personal blogs with relevant posts
- Retrieve exact quotes + dates; distinguish "official" (on Anthropic domain) vs "personal" (employee blog)

### Sub-domain C — The WaveSpeed April 2026 leak: fact-checking

Claim: WaveSpeed (or similarly-named source) published what purported to be leaked Claude Code source code / internal design documents in April 2026, which described the mailbox pattern.

Required verification:

- Is WaveSpeed a real entity? Provide a URL if yes.
- Is the leak real or rumored? What's the provenance chain?
- Has Anthropic confirmed, denied, or declined to comment?
- Is the leak still publicly accessible? (URL if yes)
- Do security researchers / independent reviewers (Willison, others) believe the leak is authentic?
- What specifically did the leak describe about inter-agent messaging?

If the leak is not credible, say so. If it's credible, extract the concrete mailbox-pattern details described with proper attribution.

### Sub-domain D — Claude Code internal mechanisms: what's publicly known

Beyond the mailbox-pattern claim, what is publicly known about how Claude Code's sub-agents actually communicate?

- Sub-agent invocation syntax and parameters (from Claude Code docs)
- How results return from sub-agents to the parent — streaming? file? in-memory?
- Whether parallel sub-agents share any common data channel
- The role of CLAUDE.md, hooks, and filesystem in inter-agent state
- Session-resume / conversation-state persistence (ndjson log, etc.)
- Any GitHub issues at github.com/anthropics/claude-code that reveal internal implementation
- Reverse-engineering by practitioners (Reddit r/ClaudeAI, Matt Wolfe, Boris Cherny talks)

**Specific question**: Given what's public, can one infer whether Claude Code internally uses a JSONL-file mailbox, an in-memory queue, a Unix-domain-socket IPC, or something else?

### Sub-domain E — Mailbox / message-queue patterns in other production multi-agent systems

Compare and contrast:

- **LangGraph**: how do agents communicate? Shared state object, explicit message passing, checkpointer (SQLite, Postgres, Redis) — what's in production?
- **CrewAI**: inter-agent communication model
- **OpenAI Agents SDK**: handoff mechanism — does it use a message queue underneath?
- **Microsoft Agent Framework 1.0**: messaging primitives (inherited from AutoGen 0.4)
- **AutoGen 0.4 (event-driven)**: event bus architecture
- **MetaGPT**: "Role" inbox/outbox pattern — how is it implemented?
- **Magentic-One** (Microsoft Research): coordination mechanism
- **Chain-of-Agents** (Google 2025): communication mechanism
- **Factory AI Droids**: any disclosure on inter-droid messaging?

For each: what's public, what's inferred, what's the analog to a "mailbox"?

### Sub-domain F — Mailbox-pattern alternatives for solo-founder production budget

For a system running 5-15 specialist agents with <€2000/mo total infrastructure spend:

- **JSONL files + filesystem** (the "Jetix pattern"): pros, cons, scaling properties, failure modes, tooling
- **SQLite queues**: pros, cons; examples (WAL mode, `queue.SimpleQueue` from Python)
- **Redis / Upstash Redis**: pros, cons, cost, when it becomes necessary
- **Temporal.io**: durability layer — but is it a mailbox? Examples in production
- **Inngest**: TypeScript-first workflow durability — mailbox analog?
- **Trigger.dev**: similar analysis
- **Hatchet**: DAG-based, how does messaging work
- **Cloudflare Queues**: cheap, works at edge, production examples
- **AWS SQS / Amazon EventBridge**: standard, but overkill?
- **Kafka / Redpanda**: when does a solo founder need a real log?
- **Named pipes / Unix domain sockets**: local IPC, what are the real patterns?
- **ndjson files** (vs JSONL): any meaningful difference in this context

For each: when should a solo founder choose it? When would it be wrong?

### Sub-domain G — Production-scale failure modes of JSONL-file mailboxes specifically

The concerning properties of JSONL-file mailboxes:

- Concurrent write (multiple agents appending at once) — what goes wrong?
- File-size growth unbounded (rotation policy)
- Readers missing messages (tail -F semantics, file truncation)
- Schema drift (JSONL has no schema enforcement)
- Message loss on crash (no fsync without explicit call)
- Ordering guarantees (append-only gives total-order on single writer, but multi-writer?)
- Filesystem limits (inode exhaustion, path-length, POSIX-compatibility across OSes)
- Git interaction (mailboxes committed vs. ignored — implications)
- Observability (reading .jsonl files ad-hoc vs. structured observability)
- Retention / archival / purge
- Partition tolerance (what if mailbox is on a network mount and the mount fails)
- Performance at 10K / 100K / 1M messages

What do production practitioners report? (Search Reddit, HN, engineering blogs, GitHub issues, Stack Overflow). Specifically seek post-mortems where "we used JSONL mailbox → switched to X because Y".

### Sub-domain H — Official Anthropic Claude Code engineering blog series (if it exists)

Beginning of 2026, did Anthropic start a Claude Code engineering blog series? If yes:

- Full post list with dates + URLs
- Authors (sometimes pseudonymous like `@claude-code-team`)
- Topics covered specifically about architecture / sub-agents / MCP / Skills / hooks

If no dedicated series exists, what's the closest (AI Engineer newsletter cross-posts? Medium Anthropic Publication?).

## Specifically required deliverables

### D1. Answer the core question

**Does an official Anthropic engineering blog post or paper explicitly document a JSONL/mailbox-based inter-agent coordination pattern as of April 22, 2026?**

One of three answers with confidence level:

- YES — cite URL + date + verbatim passage
- NO — state it clearly; list the closest proxies (employee blog posts, conference talks)
- UNCLEAR / AMBIGUOUS — explain why

### D2. Anthropic mailbox-pattern knowledge reconstruction

Reconstruct the best-available-evidence description of what Anthropic actually does (or is alleged to do). Fields:

- Channel type (file / in-memory / Redis / socket / other)
- Message format (JSON / JSONL / protobuf / YAML)
- Schema (typed / untyped / validation layer)
- Persistence (ephemeral / journaled / durable)
- Ordering (total / partial / unordered)
- Concurrency model (single-writer / multi-writer / CRDT / lease-based)
- Failure recovery (replay / checkpoint / at-least-once / at-most-once / exactly-once)

Rate each field with confidence (high/medium/low/unknown). Separate "official Anthropic" fields from "inferred/rumored" fields.

### D3. WaveSpeed leak verdict

Structured verdict:

- Real entity? (Y/N/unclear — URL)
- Real leak (authentic document dump)? (Y/N/unclear — evidence)
- Anthropic response? (confirmed / denied / silence — source)
- Credibility assessment from 3 independent security researchers (with citations)
- Final verdict: "trust / treat as signal / treat as noise / ignore"

### D4. Reference architecture: Jetix-style JSONL mailbox design

Given D1-D3 findings, produce a reference design for a solo-founder JSONL-file mailbox:

- File layout (one file per agent? per channel? per topic?)
- Schema recommendation (JSON Schema draft-07? JSON Schema 2020-12?)
- Concurrency-safety recipe (flock? tempfile+rename? Redis lock for coordination?)
- Rotation policy (size-based? time-based? message-count-based?)
- Observability hooks (tail -F, structured log shipper, per-line timestamp)
- Failure recovery (checkpoint pointer, resume on crash)
- Upgrade path (when to move to Redis / Temporal)

Cite each recommendation with primary-source evidence or the absence thereof.

### D5. Alternatives comparison matrix

Rows: mailbox implementations (JSONL / SQLite / Redis / Temporal / Inngest / Kafka / AWS SQS)
Columns: setup cost / monthly cost / durability / ordering / concurrency safety / observability / learning curve / ecosystem

At each cell: qualitative rating (Poor / OK / Good / Excellent) with 1-sentence citation.

### D6. Honest assessment

Close with:

1. **Is "Anthropic mailbox pattern" actually Anthropic's real pattern, or a community-invented term?** Evidence either way.
2. **Is the Jetix `comms/mailboxes/<agent>.jsonl` architecture safe for Phase 2+ production?** What would you change?
3. **If you had to defend the current Jetix pattern to a skeptical reviewer**, what are the strongest 3 arguments?
4. **If you had to attack the current Jetix pattern**, what are the strongest 3 attacks?
5. **What's the migration path** from JSONL-file to SQLite/Temporal/Redis if scale demands it — is the pattern portable?

## Output requirements

- Each sub-domain A-H: executive summary + top references + 5-10 findings + gaps
- Deliverables D1-D6: complete
- Final one-page summary: 10 bullets the reader must remember
- Length target: 6,000-12,000 words
- Citations: every claim; URL + date; primary Anthropic domain sources marked [OFFICIAL]; employee blogs marked [EMPLOYEE-PERSONAL]; third-party marked [THIRD-PARTY]; rumor/leak marked [UNVERIFIED]
- Confidence: rate each non-trivial claim high/medium/low

## Constraints

- **Primary sources first**: anthropic.com > employee blog > conference talk transcript > Reddit/HN aggregate > Twitter
- If a claim has no primary source, say so explicitly
- 2025-2026 preferred; flag 2023-2024 as potentially outdated
- No "I believe" — every belief traces to a source or is labeled as inference
- If WaveSpeed leak is taken offline or inaccessible at the time of research, treat as [UNVERIFIED] and note the inaccessibility

## ===END PROMPT TO PASTE===

---

## Alternative: split into 2 focused prompts (optional)

1. **Prompt A — Primary-source Anthropic search + WaveSpeed verification** (sub-domains A-D + D1-D3) — ~10 min
2. **Prompt B — Alternatives + reference design + failure modes** (sub-domains E-G + D4-D6) — ~15 min

## After Perplexity returns

1. Save raw output to `raw/research/phase-2-deep-research-2026-04-22/RESULT-04-mailbox.md`
2. Flag Cloud Cowork — Phase 3 synthesis will:
   - Cross-reference D1-D2 with Jetix current `comms/mailboxes/*.jsonl` implementation
   - Update `design/SYSTEM-DESIGN-TECH.md` with evidence-based mailbox specification
   - Adjust `design/AGENT-PROTOCOLS.md` schema if reference design suggests improvements
   - Decide whether to migrate to SQLite/Temporal in Phase 2+ or stay with JSONL

---

*END PROMPT 04 — Anthropic Mailbox Pattern Verification*
