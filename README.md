# jetix-os

Multi-agent personal + business operating system. Owner: Ruslan (Berlin).

## Architecture overview

```
.claude/        — Claude Code config: agents, skills, settings, rules
agents/         — 12+ agent definitions (system.md / strategies.md / scratchpad.md / niche/)
comms/          — JSONL mailboxes for inter-agent messaging
config/         — system-wide config files
crm/            — multi-purpose contact network (people + orgs); see crm/README.md
decisions/      — decision records (architectural, strategic)
directions/     — active vs paused strategic directions
inbox/          — incoming notes / voice / chats / articles for triage
knowledge-base/ — legacy KB (in migration to wiki/, see MIGRATION.md)
logs/           — execution logs
projects/       — per-project working dirs
raw/            — voice memos + transcripts (raw inputs)
reports/        — voice-pipeline review reports
shared/         — shared state, schemas, knowledge
swarm/          — Phase-A swarm (brigadier, mini-swarms, awaiting-approval)
tools/          — Python pipeline scripts (transcribe, extract, filter, review, distribute)
wiki/           — main KB v2 (Karpathy LLM Wiki + OmegaWiki); see CLAUDE.md "Wiki Architecture"
_meta/          — conventions, pipeline-spec
```

See `CLAUDE.md` for full system spec and `MIGRATION.md` for legacy → wiki/ migration plan.
