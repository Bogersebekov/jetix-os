# Jetix CRM-as-Code: A Markdown + Git Architecture for AI-Native Sales Operations

**Research for Wave 2 Knowledge Architecture · Target reader: Ruslan / Jetix founding architect · Scope: Parts A–J**

## Executive Summary

Jetix needs a CRM that behaves like source code: diff-able, scriptable, agent-readable, GDPR-auditable, and portable. The research below synthesises prior art from Obsidian/Logseq CRM communities, open-source CRMs (EspoCRM, Krayin, Monica), git-based databases (Dolt, Irmin), event sourcing literature (Fowler, Young, Kleppmann, Microsoft patterns), and — critically — the German legal stack (§ 14 UStG, GoBD 2025, Art. 17 GDPR) that a Berlin-based Mittelstand consultancy cannot avoid.

The recommended architecture is a **three-layer system**: (1) durable entity notes as YAML-fronted markdown under `clients/`, (2) an **append-only event log** (`alpha-log/YYYY-MM.jsonl`) for state transitions and activities, and (3) **derived projections** regenerated on commit (pipeline snapshot, weekly report, revenue ledger) via a small DuckDB/jq toolchain. Communications and binary artefacts live **outside git** with cryptographic references inside it. Encryption is selective via SOPS+age. Migration to HubSpot is a 48-hour CSV export by design. Part J delivers a copy-paste-ready folder layout, six YAML schemas, four filled example files, a 12-query cookbook, and explicit scale triggers.

---

## Part A — Markdown-based CRM: SOTA 2024-2026

### A.1 Obsidian + Dataview: the dominant PKM-CRM pattern

The de facto approach in the Obsidian community is **one note per entity, linked via `[[wikilinks]]`, queried via Dataview**. Community tutorials converge on a "People / Companies / Meetings / Projects" quadruplet, with YAML frontmatter holding structured fields and Dataview materialising views ([Obsidian r/ObsidianMD showcase](https://www.reddit.com/r/ObsidianMD/comments/1bcad3a/im_a_simple_man_and_new_to_obsidian_pls_someone/), [How to use Obsidian as CRM with Dataview and Metadata Menu](https://www.youtube.com/watch?v=KOw_LtMgMlQ)).

A typical Dataview query over frontmatter looks like this ([Obsidian Forum](https://forum.obsidian.md/t/dataview-how-to-query-for-frontmatter-keys/70992)):

```dataview
TABLE file.link AS Name, last-contact AS "Last Contact", stage
FROM #deal AND -"Templates"
WHERE stage = "negotiating" AND value > 10000
SORT last-contact DESC
```

Strengths: zero infrastructure, instant local-first editing, visible audit trail, AI-agent-friendly plain text. Weaknesses relevant to Jetix: Dataview is **Obsidian-specific** (not portable to CI or to agents running outside the vault), handles lists-of-links awkwardly, and degrades on vaults above ~10,000 notes ([Reddit — Dataview WHERE with frontmatter links](https://www.reddit.com/r/ObsidianMD/comments/1frgybd/can_a_dataview_query_where_clause_use_a/)). The takeaway for Jetix: **use Dataview as a viewing layer, not a storage contract** — the canonical schema must be queryable without Obsidian.

### A.2 Logseq: block-based, Datalog queries

Logseq treats **blocks** as first-class entities with properties (`status:: negotiating`, `value:: 25000`). Queries use Datalog (a Prolog-like logic language) against the block graph ([Logseq Discourse — CRM queries](https://discuss.logseq.com/t/advanced-queries-for-use-with-crm/14379), [Logseq block properties](https://discuss.logseq.com/t/are-you-using-and-if-so-how-are-you-using-block-properties/20046)). For a single-person CRM this is powerful, but for Jetix two problems disqualify it as canonical storage:

1. Datalog locks data into Logseq's semantics; exporting to CSV for HubSpot is lossy.
2. Logseq's outliner model fights the "one file per entity" model that git diff-ability requires.

Use Logseq as an **optional read-only client** pointed at the same markdown folder, not as the authoring tool.

### A.3 Notion as CRM: the anti-pattern

Many bootstrapped teams start with Notion because its hybrid database/markdown UI is ergonomic. At scale three failures recur: (1) Notion's API rate-limits at 3 requests/second, breaking agentic workloads; (2) export fidelity is poor (nested DBs, rollups, and relations degrade on Markdown export); (3) Notion's page IDs are opaque UUIDs that make git-style referencing impossible. For Jetix's "company-as-code" principle, Notion is **explicitly incompatible** as source of truth. It may serve as a stakeholder-facing read-only mirror during the solo→team transition (see Part H).

### A.4 Monica: open-source personal CRM

[Monica](https://docs.monicahq.com) is a PHP/Laravel application backed by MySQL. It pioneered the "relationships as first-class objects" model — life events, reminders, gift tracking — and demonstrates the **Person-Activity-Relationship triad** as a minimal viable CRM data model. Jetix should borrow two ideas: (a) every contact note has an "activities" timeline attached, not scattered; (b) reminders are first-class, not bolted onto tasks. Monica's storage (relational MySQL) is not directly applicable — it is cited as schema inspiration, not tech stack ([Monica on Ubuntu guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-personal-crm-with-monica-on-ubuntu-20-04)).

### A.5 EspoCRM and Krayin: the relational reference

[EspoCRM](https://github.com/espocrm/espocrm) (PHP, PostgreSQL/MySQL, AGPLv3) is the most rigorous open-source B2B CRM. Its entity model — Account, Contact, Lead, Opportunity, Case, Campaign — is metadata-driven via JSON Schema, which makes it a useful **canonical reference** when designing YAML schemas. [Krayin](https://github.com/krayin/laravel-crm) (Laravel+Vue) targets SME sales pipelines with a simpler Lead → Person → Organization → Quote structure. Both ship with **built-in GDPR "Data Privacy" modules** ([EspoCRM on SourceForge](https://sourceforge.net/projects/espocrm/)) — evidence that EU-serious CRMs treat consent/erasure as core, not optional.

For Jetix the lesson is schema shape, not deployment. Copy EspoCRM's field names where possible to preserve migration compatibility (see Part H).

### A.6 Markdown frontmatter as a storage contract

YAML frontmatter between `---` fences is the **de facto metadata standard** for markdown files across Jekyll, Hugo, Obsidian, and Logseq ([PBS 168 intro to YAML](https://pbs.bartificer.net/pbs168)). Two properties make it ideal for CRM:

1. **Tool ubiquity**: `yq`, `jq` (via `yaml-to-json`), Python `PyYAML`, Ruby Front Matter parser, Go `gopkg.in/yaml.v3`, Node `gray-matter` all parse it.
2. **Git-diffability**: YAML is line-oriented, so `git diff` produces meaningful patches when a deal stage changes.

The implementation detail that matters: `yq --front-matter="process"` can mass-edit frontmatter across thousands of files in-place ([Haseeb Majid — yq for mass frontmatter edits](https://haseebmajid.dev/posts/2022-11-17-til-you-can-use-yq-to-mass-edit-markdown-files/), [Richard's Blog — YQ, Frontmatter and Jekyll](https://www.main-vision.com/richard/blog/yq-frontmatter-and-jekyll/)). This replaces a large category of "bulk update" operations that would otherwise require a real database.

### A.7 Git as database: Dolt, Irmin, and the lessons that apply

Two projects formalise "git for data":

- **[Dolt](https://docs.dolthub.com/introduction/getting-started/git-for-data)** implements the git CLI on top of SQL tables — cell-wise diffs, branches, merges, `dolt log`. Its architectural insight is that **version-control primitives (commit, branch, merge, diff) are applicable to any structured data, not just source code** ([DoltHub — Database Versioning](https://www.dolthub.com/blog/2022-08-04-database-versioning/)).
- **[Irmin](https://irmin.org)** (Tarides, OCaml) is a distributed store with a pluggable Git backend that uses the on-disk git format directly, so every commit is inspectable with stock `git` tools ([mirage/irmin GitHub](https://github.com/mirage/irmin)). Irmin's contribution is **user-defined merge functions for structured data** — two branches updating the same deal stage can be resolved semantically (latest wins, or reject if conflict) rather than as textual merge conflict.

Jetix does not need to run Dolt or Irmin. The lessons to import:

1. **Primary key per entity** (slug or UUID) to survive renames.
2. **Semantic merge rules** documented per entity type (what wins when two branches bump `stage`?).
3. **Time-travel queries** are almost free when storage is git-based — `git show HEAD~30:clients/deals/acme.md` shows the deal 30 commits ago.

### A.8 Jupyter-as-CRM (noted, not recommended for Jetix)

Analyst-heavy teams (trading desks, quant researchers) sometimes treat notebook cells as mutable dashboards over a Pandas/DuckDB layer. This is a reporting layer, not a storage layer. For Jetix it's relevant only insofar as the `analyst` agent may emit Jupyter notebooks as quarterly reports (Part G).

### A.9 Summary comparison

| Approach | Storage | Query | Jetix fit |
|---|---|---|---|
| Obsidian + Dataview | markdown + YAML | Dataview (DQL) | **Reading layer, optional** |
| Logseq | markdown + properties | Datalog | Read-only mirror, optional |
| Notion | proprietary | Notion API | ❌ Anti-pattern |
| Monica | MySQL (PHP app) | SQL | Schema inspiration only |
| EspoCRM / Krayin | Postgres/MySQL | REST + SQL | Schema + migration target |
| Dolt | SQL tables in git format | MySQL dialect | Conceptual inspiration |
| Irmin | Custom/git backend | OCaml API | Merge-semantics inspiration |
| **Jetix proposal** | **markdown+YAML + `alpha-log/*.jsonl` + DuckDB projection** | **jq / DuckDB / Dataview** | **Canonical** |

---

## Part B — Data Model for Markdown-based CRM

### B.1 Entity inventory

Eight entity types are required to serve the full DACH B2B sales cycle. They align with R3's ten approved alphas, collapsing "Deal/Contract" and "Invoice" into separate files where lifecycle differs:

| Entity | Alpha (R3) | File location | Key |
|---|---|---|---|
| Company | (Client, org-side) | `clients/companies/<slug>.md` | slug |
| Contact | (Client, person-side) | `clients/contacts/<slug>.md` | slug |
| Lead | Client (pre-qualified) | `clients/leads/<slug>.md` | slug |
| Deal | Client (in pipeline) + Deal/Contract | `clients/deals/YYYY-MM-DD-<slug>.md` | date-slug |
| Contract / SOW | Deal/Contract (signed) | `clients/contracts/signed/<id>.md` | contract_id |
| Invoice | Invoice | `clients/invoices/YYYY/<number>.md` | Rechnungsnummer |
| Activity | Client.activity | `clients/activities/YYYY-MM-DD-<slug>.md` | date-slug |
| Task (follow-up) | (cross-cutting) | `ops/tasks/<slug>.md` | slug |

EspoCRM separates "Lead" from "Contact" — a Lead becomes a Contact + Account + Opportunity on qualification. Jetix should replicate this to preserve migration compatibility: a `clients/leads/*.md` file is **promoted** (via a git-tracked script) into `companies/` + `contacts/` + `deals/` on qualification, not mutated in place.

### B.2 Relationship representation

Markdown has no referential integrity. Three patterns are available, and Jetix should use all three with clear rules:

1. **YAML reference by slug** (primary):
   ```yaml
   company: acme-gmbh        # → clients/companies/acme-gmbh.md
   primary_contact: hans-mueller
   contacts: [hans-mueller, sabine-weber]
   ```
2. **Wikilink `[[slug]]`** in prose body (secondary) — lets Obsidian, Logseq, and static site generators render graph views without reading YAML.
3. **Event-log foreign key** (in `alpha-log/*.jsonl`) — every event carries `entity_type`, `entity_id`, and optional `related_entity_ids`.

Rule: **YAML is the contract**; wikilinks are for humans; events are for history. If wikilinks and YAML disagree, YAML wins. A pre-commit hook can flag divergence.

Cardinalities:

| Relationship | Cardinality | Where stored |
|---|---|---|
| Company ↔ Contacts | 1:N | `contacts[]` array on Company; `company: <slug>` on Contact |
| Contact ↔ Deals | N:M (one primary) | `primary_contact` + `contacts[]` on Deal |
| Deal ↔ Activities | 1:N | `deal: <slug>` on Activity |
| Deal ↔ Contract | 1:1 | `contract: <slug>` on Deal; `deal: <slug>` on Contract |
| Contract ↔ Invoices | 1:N | `contract: <slug>` on Invoice |
| Company ↔ Company (parent/subsidiary) | N:1 | `parent_company: <slug>` optional |

### B.3 YAML frontmatter schemas

Schemas below are **authoritative for v1**. Each field is annotated with required (`*`) or optional. Full copy-paste schemas with enumerated states are in Part J.

**Company** (excerpt):

```yaml
---
id: acme-gmbh                    # * slug, immutable
type: company                    # * discriminator
legal_name: "Acme Maschinenbau GmbH"   # *
trade_name: "Acme"               # display name
legal_form: GmbH                 # GmbH | AG | GmbH & Co. KG | UG | GbR | other
hrb: "HRB 12345 Berlin"          # Handelsregister eintrag (optional)
ust_id: "DE123456789"            # Umsatzsteuer-ID (EU cross-border)
steuernummer: "12/345/67890"     # Tax number
industry: "machine building"
industry_wz: "28.49"             # WZ 2008 code (Destatis)
employees: 180
revenue_eur: 42000000
location: { city: "Stuttgart", postcode: "70173", country: "DE" }
website: https://acme.de
linkedin: https://www.linkedin.com/company/acme
status: active                   # active | prospect | churned | archived
icp_score: 8                     # 1..10
tags: [mittelstand, manufacturing, dach-core]
sources: [linkedin-outreach]
owner: sales-lead
created: 2026-04-19
updated: 2026-04-19
gdpr_lawful_basis: legitimate_interest   # Art. 6(1)(f)
---
```

**Contact** (excerpt):

```yaml
---
id: hans-mueller
type: contact
company: acme-gmbh               # * slug FK
full_name: "Hans Müller"         # *
salutation: Herr                 # Herr | Frau | (diverse) — German pronoun-correctness
role: "Geschäftsführer"          # Geschäftsführer | CFO | IT-Leiter | Prokurist | Einkäufer | other
decision_power: sponsor          # sponsor | decision-maker | influencer | blocker | champion | user
email: hans.mueller@acme.de
phone: "+49 711 1234567"
linkedin: https://www.linkedin.com/in/hansmueller
language: de                     # de | en
consent: { marketing: false, processing: legitimate_interest, date: 2026-04-19 }
notes_path: ./notes.md           # optional long-form, in same directory
status: active
created: 2026-04-19
---
```

**Deal** (excerpt):

```yaml
---
id: 2026-04-20-acme-audit
type: deal
company: acme-gmbh               # *
primary_contact: hans-mueller    # *
contacts: [hans-mueller, sabine-weber]
sku: ai-readiness-audit          # * links clients/skus/<id>.md
stage: proposal                  # lead | qualified | proposal | negotiation | won | lost | churned
probability: 0.4                 # 0..1, mirrors stage default but overridable
value_eur: 7500
currency: EUR
expected_close: 2026-06-15
competitor: null                 # slug of competitor or null
source: linkedin-outreach
owner: sales-lead
discount_pct: 0                  # 0..10 per R1 decision-rights
lost_reason: null                # on stage=lost
won_at: null                     # on stage=won
contract: null                   # slug when signed
---
```

Similar schemas for Lead, Contract, Invoice, Activity are in Part J.

### B.4 Validation via JSON Schema

Every entity type has a JSON Schema under `schemas/<entity>.schema.json`. Validation runs in a pre-commit hook:

```bash
# .git/hooks/pre-commit (excerpt)
for f in $(git diff --cached --name-only --diff-filter=ACM | grep '^clients/'); do
  yq --front-matter=extract "$f" | ajv validate -s "schemas/$(yq '.type' "$f").schema.json" -d -
done
```

Rejecting malformed commits is the cheapest possible data-quality mechanism. EspoCRM internally follows the same JSON Schema approach for all metadata ([EspoCRM README](https://github.com/espocrm/espocrm)).

### B.5 File naming conventions

Two rules, applied consistently:

1. **Slug-based** for long-lived entities (Company, Contact, Lead): `<slug>.md` where slug is lowercase kebab-case of the legal/display name, max 40 chars. Never renamed after creation — rename is a hard break.
2. **Date-prefix** for event-like entities (Deal, Activity, Invoice): `YYYY-MM-DD-<slug>.md`. Ordering is calendrical, making `ls` useful as a first-pass pipeline.

Invoices are an exception: `clients/invoices/2026/R-2026-0017.md` — the filename **is** the legally-required sequential Rechnungsnummer (Part E).

### B.6 Static vs dynamic data

A Company's `legal_name`, `hrb`, `ust_id` change rarely. A Deal's `stage` changes every few days. Storing both in the same file is fine, but co-locating **event-velocity data with slow-changing reference data creates noisy diffs** (git history becomes 90% stage changes, burying the 10% real business changes).

The solution is separation of concerns:

| Data class | Location | Rationale |
|---|---|---|
| Reference/profile (rare change) | Entity file frontmatter | Diffs are meaningful |
| State (every few days) | Entity file frontmatter **+** event log | Current state visible; history in log |
| Activity log (daily, append-only) | `alpha-log/YYYY-MM.jsonl` | Append-only, no merge conflicts |
| Communications (high volume) | **Outside git** (maildir, S3), referenced by hash | Git performance; GDPR erasure |

This maps onto the classic **event sourcing + snapshot** pattern (Part C).

---

## Part C — State transitions and event sourcing

### C.1 The core design choice

R3 proposed git-commit tags like `[alpha:client:acme][state:proposal→active]`. This is lightweight but has three limitations:

1. Commit messages are unstructured — parsing them reliably is brittle.
2. A single commit may touch multiple entities; one message cannot describe them all.
3. Commits mix human-readable narrative with machine-parseable state changes.

Event sourcing, as formalised by Greg Young and Martin Fowler and canonised by Microsoft's Azure Architecture Center, stores **state changes as immutable events, from which current state is a projection** ([Microsoft Learn — Event Sourcing Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing), [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html), [Confluent Developer — CQRS in event sourcing](https://developer.co/courses/event-sourcing/cqrs/)).

### C.2 Recommended hybrid: snapshot + event log

Jetix should adopt a **lightweight hybrid**:

- **Snapshot**: the current state of every entity lives in its markdown file (`stage: proposal`, `probability: 0.4`). This is what humans and agents read.
- **Event log**: every state transition and every activity is appended to `alpha-log/YYYY-MM.jsonl` as a structured event.

This is the "snapshot with event log" pattern Kleppmann describes in *Designing Data-Intensive Applications* (Chapter 11): keep both, regenerate the snapshot from events when schemas evolve.

Benefits:

- Humans edit markdown directly; a post-commit hook emits the corresponding event.
- Agents read snapshots for speed, events for context.
- Audit trail is cryptographically secured by git (events are immutable once committed).
- Re-projection is possible: wipe all snapshots, replay events, regenerate.
- Compensating events (C.5) remain first-class.

Microsoft's guidance cautions against full event sourcing for systems where auditability does not justify complexity ([Microsoft Learn — Event Sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)). Jetix's hybrid sits in the sweet spot: full audit trail with minimal ceremony.

### C.3 Event schema

One file per month (`alpha-log/2026-04.jsonl`), JSON-lines, append-only. One event per line:

```json
{"ts":"2026-04-20T09:14:00+02:00","actor":"ruslan","agent":null,"type":"deal.stage-changed","entity":"deals/2026-04-20-acme-audit","from":"lead","to":"qualified","context":{"reason":"discovery-call-positive"}}
{"ts":"2026-04-20T09:15:00+02:00","actor":"ruslan","agent":null,"type":"activity.logged","entity":"activities/2026-04-20-acme-discovery-call","related":["deals/2026-04-20-acme-audit","contacts/hans-mueller"],"channel":"video-call","duration_min":42}
{"ts":"2026-04-21T16:02:11+02:00","actor":"sales-outreach","agent":"sales-outreach","type":"email.sent","entity":"activities/2026-04-21-acme-followup","related":["deals/2026-04-20-acme-audit","contacts/hans-mueller"],"subject_hash":"sha256:ab12…","body_ref":"comms/sha256-ab12.eml.age"}
```

Field contract:

| Field | Type | Required | Notes |
|---|---|---|---|
| `ts` | ISO 8601 with offset | ✔ | Europe/Berlin offset, never naive |
| `actor` | string (user id) | ✔ | Human user or agent id |
| `agent` | string or null | ✔ | Non-null if action was agent-initiated |
| `type` | event type enum | ✔ | See C.4 |
| `entity` | path relative to clients/ | ✔ | Primary entity |
| `related` | array of paths | ✖ | Other entities touched |
| `from` / `to` | strings | — | Required for `.stage-changed` |
| `context` | object | ✖ | Free-form; never contains PII |

### C.4 Canonical event types

Borrowed from EspoCRM, Fowler's CQRS vocabulary, and Greg Young's event-sourcing primers:

```
lead.created · lead.qualified · lead.disqualified · lead.promoted
deal.created · deal.stage-changed · deal.value-changed · deal.won · deal.lost · deal.reopened
contact.added · contact.role-changed · contact.moved-company · contact.consent-updated · contact.erased
company.created · company.updated · company.merged · company.archived
contract.drafted · contract.signed · contract.amended · contract.completed · contract.cancelled
invoice.issued · invoice.sent · invoice.paid · invoice.partially-paid · invoice.disputed · invoice.corrected
activity.logged · email.sent · email.received · call.logged · meeting.held · note.added
task.created · task.completed · task.cancelled
```

This vocabulary is stable across schema evolution — new event types are added, old ones are never removed or redefined.

### C.5 Projections

A projection is a derived file regenerated from the event log. Jetix needs three projections on day one:

1. `sales/pipeline.md` — all active deals, grouped by stage, sorted by probability × value. Regenerated on every commit that touches `clients/deals/` or `alpha-log/`.
2. `sales/reports/YYYY-Www-weekly.md` — generated Sunday night (cron), summarises the week's events.
3. `finance/ledger.md` — running revenue from `invoice.paid` events.

All projections are committed to git. This is intentional redundancy: it makes `git diff` on a projection a human-readable weekly change report.

Re-projection (rebuilding all projections from scratch) is a single command:

```bash
python scripts/project.py --from 2026-01-01 --to HEAD
```

This is what lets schema evolution be painless: change the event handler, re-run.

### C.6 Reversibility and compensating events

Never delete events. If an event was wrong, append a **compensating event** that negates it ([Fowler on CQRS](https://martinfowler.com/bliki/CQRS.html) — same pattern):

```json
{"ts":"2026-04-22T10:00:00+02:00","type":"deal.stage-changed","entity":"deals/…","from":"won","to":"negotiation","context":{"reason":"won-reversal-wrong-entry","compensates_event_at":"2026-04-21T17:30:00+02:00"}}
```

Git history remains honest; the error and the correction are both visible. This is **operationally important for German bookkeeping** — the Grundsatz der Unveränderbarkeit in GoBD explicitly prohibits silently editing records ([AODocs — GoBD explained](https://www.aodocs.com/blog/gobd-explained-requirements-for-audit-ready-digital-bookkeeping-in-germany-and-beyond/)).

### C.7 When NOT to use event sourcing

For Jetix's first 5–20 deals, strict event sourcing is overkill. The recommendation: **start events.jsonl from day one but only for state-change events and activity events**. Do not event-source field edits on Companies or Contacts — those belong to the markdown file and rely on git commits as the audit trail. This keeps the log lean (10–50 events/week) while delivering the auditability GoBD and GDPR require.

---

## Part D — Communications tracking

DACH B2B sales cycles run 6–12 weeks across Konsenskultur stakeholders (Geschäftsführer, CFO, IT-Leiter), accumulating 30–100 touchpoints per deal. Storing them correctly is non-trivial.

### D.1 Email: plaintext archival with out-of-git storage

**Never store emails as git blobs.** Binary attachments inflate the repo; full MIME messages bloat diffs; and — critically — GDPR right-to-erasure becomes operationally intractable (Part I).

The recommended pattern:

1. Fetch emails via IMAP (Gmail/Microsoft365/Fastmail) into a **maildir** outside git at `~/jetix-comms/maildir/`.
2. Each message is content-addressed: `sha256-<hash>.eml`.
3. In git, only the **reference** lives: the matching `clients/activities/YYYY-MM-DD-*.md` file records sender, recipient, subject hash, body hash, and optional summary.
4. If the user's DPIA deems emails "routine business correspondence under Art. 6(1)(f) legitimate interest", bodies may be stored encrypted at rest (age keys).

Activity example:

```yaml
---
id: 2026-04-21-acme-proposal-follow-up
type: activity
channel: email.sent
deal: 2026-04-20-acme-audit
contact: hans-mueller
from: ruslan@jetix.ai
to: [hans.mueller@acme.de]
subject: "Follow-up zum AI Readiness Audit Proposal"
body_hash: sha256:ab12cd34…
body_ref: ~/jetix-comms/maildir/sha256-ab12cd34.eml.age  # encrypted blob
summary: "Reminded Hans about next steps, proposed week of April 28."
sent_at: 2026-04-21T16:02:11+02:00
---
```

### D.2 Meeting notes: structured template + optional transcript

Every meeting produces a `clients/activities/YYYY-MM-DD-<slug>.md` file with structured sections: **Attendees, Agenda, Decisions, Action Items, Risks, Next Steps**. This is the T-xx convention from Jetix's existing knowledge architecture (R4). The transcript (from the existing voice-memo pipeline — Otter.ai, Fireflies, or local Whisper) is stored as a sibling file `YYYY-MM-DD-<slug>.transcript.md`, referenced by `transcript_path` in frontmatter.

Search across meeting notes uses `ripgrep` or DuckDB's `fts_main` extension; the transcript files are indexed.

### D.3 Call logs: just markdown

Short notes after each call (2–10 sentences) in the same `activities/` folder with `channel: call`. Agents can generate a draft summary immediately after the call if the call was recorded; humans confirm or edit.

### D.4 LinkedIn messages: export + import

LinkedIn provides a periodic data export (Settings → Data Privacy → Get a copy of your data) containing messages as CSV. A simple script ingests it into `activities/` with `channel: linkedin-message`. Because LinkedIn does not offer a reliable live API for DMs, **export-on-demand** is the only lawful ingestion path. Jetix should run it weekly.

### D.5 Thread continuity

The cross-channel thread for a contact is reconstructed by query, not by storage:

```sql
-- Via DuckDB over frontmatter (see Part F)
SELECT ts, channel, summary
FROM read_markdown('clients/activities/*.md')
WHERE contact = 'hans-mueller'
ORDER BY ts;
```

Storage stays per-event; continuity is a view, not a table. This mirrors the CQRS read-side pattern ([Confluent — CQRS](https://developer.co/courses/event-sourcing/cqrs/)).

---

## Part E — Contract / SOW / Invoice management

This part is where German legal specifics stop being aesthetic and start being binding.

### E.1 Contracts and SOWs

Jetix's four SKUs (AI Readiness Audit, Quick Win Automation, Custom Agent Build, Operations Retainer) should have **parametric markdown templates** under `clients/contracts/templates/`. Templates render to PDF via `pandoc + eisvogel` LaTeX template, producing the signable artifact.

Flow:

```
templates/ai-readiness-audit-sow.md.tmpl
    → scripts/render-sow.py (fills variables from deal YAML)
    → clients/contracts/drafts/<deal_slug>.md + .pdf
    → legal review (human)
    → DocuSign envelope
    → clients/contracts/signed/<contract_id>.md + .pdf (signed PDF is append-only)
```

Key decisions:

1. **Draft** files live in `drafts/` and are git-tracked — iteration is diff-visible.
2. **Signed** files live in `signed/` and are **never modified** (amendments are new files with `amends: <id>` reference).
3. Signed PDFs are stored in git **only if under 2 MB**; larger PDFs go to an encrypted S3 bucket, referenced by hash in the markdown counterpart. GoBD requires the original signed document to be retained unchanged for 10 years ([RTC Suite — GoBD 2025 e-invoice archiving rules](https://rtcsuite.com/germany-clarifies-e-invoice-archiving-rules-gobd-2025-amendment-how-businesses-must-now-store-einvoices/)).

### E.2 SOW scope definition and change orders

SOW templates include an explicit **Leistungsbeschreibung** section enumerating deliverables, a **Change-Request** subsection defining the process for scope additions, and an **Abnahme-Kriterien** section (acceptance criteria). Scope creep protection is procedural: any work outside the Leistungsbeschreibung requires a signed Change Order (itself a contract file).

### E.3 Invoicing — German Rechnung requirements

Per § 14 Abs. 4 UStG, every Jetix invoice over €250 gross must contain ([IHK Frankfurt — Rechnungen: Pflichtangaben](https://www.frankfurt-main.ihk.de/recht/uebersicht-alle-rechtsthemen/steuerrecht/umsatzsteuer-national/rechnungen-pflichtangaben-in-der-rechnung-5195692), [Lexware — § 14 UStG](https://www.lexware.de/wissen/unternehmerlexikon/paragraph-14-ustg/), [sevDesk — § 14 UStG](https://sevdesk.de/lexikon/paragraph-14-ustg/)):

1. Vollständiger Name und Anschrift des leistenden Unternehmers und des Leistungsempfängers
2. Steuernummer **oder** Umsatzsteuer-ID (USt-IdNr.) des Ausstellers
3. Ausstellungsdatum
4. Fortlaufende, einmalig vergebene Rechnungsnummer (one or more numerical series, strictly sequential)
5. Menge und handelsübliche Bezeichnung der Leistung / Lieferung
6. Zeitpunkt (Monat ausreichend) der Lieferung oder Leistung
7. Nach Steuersätzen und Steuerbefreiungen aufgeschlüsseltes Entgelt
8. Im Voraus vereinbarte Minderungen des Entgelts
9. Anzuwendender Steuersatz + Steuerbetrag **oder** Hinweis auf Steuerbefreiung
10. Ggf. Hinweis auf Aufbewahrungspflicht des Empfängers (§ 14b Abs. 1 Satz 5)
11. Bei Gutschriftverfahren: Angabe "Gutschrift"

Kleinbetragsrechnungen up to €250 gross have a reduced set (name/address of issuer only, date, description, gross sum, tax rate or exemption note — [IHK Frankfurt](https://www.frankfurt-main.ihk.de/recht/uebersicht-alle-rechtsthemen/steuerrecht/umsatzsteuer-national/rechnungen-pflichtangaben-in-der-rechnung-5195692)). This simplification **does not apply** to intra-EU deliveries (§ 6a UStG), Versandhandel (§ 3c UStG), or reverse-charge cases (§ 13b UStG) — relevant for Jetix if any client is an Austrian or Swiss entity.

Invoice YAML (Part J has the full schema):

```yaml
---
id: R-2026-0017                      # * fortlaufende Rechnungsnummer, immutable
type: invoice
contract: acme-audit-2026-04
company: acme-gmbh
issued: 2026-05-02                   # * Ausstellungsdatum
performance_date: 2026-04            # * Leistungszeitpunkt (month sufficient)
due: 2026-05-16                      # Zahlungsziel 14 days
line_items:
  - description: "AI Readiness Audit – Acme GmbH"
    qty: 1
    unit_price_net: 7500.00
    vat_rate: 0.19
    vat_amount: 1425.00
    line_total_gross: 8925.00
subtotal_net: 7500.00
vat_total: 1425.00
total_gross: 8925.00
currency: EUR
payment_method: sepa
bank: { iban: "DE89 3704 0044 0532 0130 00", bic: "COBADEFFXXX", bank_name: "Commerzbank" }
issuer:
  name: "Jetix UG (haftungsbeschränkt)"
  address: "…, Berlin"
  steuernummer: "…"
  ust_id: "DE…"
status: sent                         # draft | issued | sent | paid | partially-paid | disputed | corrected
sent_at: 2026-05-02T11:00:00+02:00
paid_at: null
stripe_invoice_id: in_1Abc…          # if Stripe rails
---
```

### E.4 Sequential numbering

Rechnungsnummern must be **strictly sequential without gaps** — a gap is a tax-law red flag. Recommended format: `R-YYYY-NNNN` reset annually, with the counter stored in a single file `finance/next-invoice-number.txt`. A pre-commit hook verifies monotonicity.

### E.5 Stripe Billing + accounting integration

The existing Jetix plan (R2) uses Stripe Billing. Stripe generates its own invoice numbers, but German law allows **parallel numbering systems** per § 14 UStG as long as each is internally sequential and uniquely identifies the invoice. Recommendation:

- Stripe handles B2C / self-serve subscriptions (L3 SaaS).
- L4 consulting invoices are issued manually from markdown templates (rendered to PDF) to preserve full control over Pflichtangaben, then paid via SEPA or Stripe Invoice link.
- Every Jetix invoice — regardless of rail — appears as one file under `clients/invoices/YYYY/`.

For accounting, **export monthly** to DATEV CSV format (the Steuerberater's preferred import) via a script:

```bash
python scripts/datev-export.py --month 2026-04 > finance/datev/2026-04.csv
```

### E.6 Payment reconciliation

Bank statement (CAMT.053 XML from most German banks) is ingested weekly. A matching script pairs SEPA payments with open invoices by reference string (`R-2026-0017` in the payment purpose) and emits `invoice.paid` events. Partial payments generate `invoice.partially-paid` events with residual amount.

### E.7 GoBD 2025 compliance

The July 2025 amendment to GoBD formalises that e-invoices must be archived in their **original structured format** (XML for ZUGFeRD/XRechnung) for 10 years, machine-readable, with guaranteed integrity and authenticity ([RTC Suite — GoBD 2025 amendment](https://rtcsuite.com/germany-clarifies-e-invoice-archiving-rules-gobd-2025-amendment-how-businesses-must-now-store-einvoices/), [AODocs — GoBD explained](https://www.aodocs.com/blog/gobd-explained-requirements-for-audit-ready-digital-bookkeeping-in-germany-and-beyond/)). For Jetix, this means:

1. Every issued invoice is rendered as **ZUGFeRD 2.x** (embedded XML in a PDF/A-3) in addition to the markdown source.
2. The PDF and the XML both live in git (or encrypted S3 for larger sizes).
3. The immutability requirement is satisfied by git's append-only history + branch protection on `main`.
4. A quarterly cron verifies that all `status: paid` invoices from prior quarters still have their XML files on disk and unchanged.

---

## Part F — Query and reporting patterns

### F.1 Three-tier query strategy

Queries fall into three performance classes:

| Class | Example | Tool | Expected latency |
|---|---|---|---|
| Ad-hoc grep | "find all deals mentioning 'DSGVO'" | ripgrep | <100 ms up to 10k files |
| Structured frontmatter | "all active deals > €10K" | jq / yq / DuckDB | <1 s up to 10k files |
| Cross-entity joins + aggregations | "revenue by stage by month" | DuckDB | <5 s |

### F.2 Grep tier

Works fine up to ~10k files. Examples:

```bash
# All currently-active deals
rg -l '^stage: (qualified|proposal|negotiation)$' clients/deals/

# Deals mentioning a competitor
rg -l 'competitor: aleph-alpha' clients/deals/

# Anything changed in last 14 days
find clients/ -name '*.md' -mtime -14
```

### F.3 yq / jq tier (portable, no dependencies)

`yq` extracts frontmatter as YAML/JSON and is composable in shell pipelines ([yq frontmatter docs](https://haseebmajid.dev/posts/2022-11-17-til-you-can-use-yq-to-mass-edit-markdown-files/)):

```bash
# All active deals over €10K
for f in clients/deals/*.md; do
  yq --front-matter=extract -o=json "$f" | \
    jq -r 'select(.stage|IN("qualified","proposal","negotiation")) |
           select(.value_eur > 10000) |
           "\(.id)\t\(.value_eur)\t\(.stage)"'
done
```

This is the reference query language: present on every developer machine, trivial to script, portable.

### F.4 DuckDB tier (recommended for reports)

DuckDB 2024+ ships a community **markdown extension** that parses markdown files with frontmatter into relational rows ([DuckDB — Markdown Community Extension](https://duckdb.org/community_extensions/extensions/markdown.html), [DuckDB — YAML extension](https://duckdb.org/community_extensions/extensions/yaml.html)). This turns the `clients/` folder into a queryable database without ETL:

```sql
INSTALL markdown FROM community;
LOAD markdown;

-- All active deals > €10K
SELECT frontmatter->>'id'       AS id,
       frontmatter->>'stage'    AS stage,
       (frontmatter->>'value_eur')::DOUBLE AS value_eur,
       frontmatter->>'expected_close' AS close
FROM read_markdown('clients/deals/*.md')
WHERE stage IN ('qualified','proposal','negotiation')
  AND value_eur > 10000
ORDER BY value_eur DESC;
```

DuckDB handles ~100k files without trouble on a laptop, so this tier covers Jetix up to the migration threshold (Part H).

### F.5 Dataview tier (Obsidian-only view)

For the founder working inside Obsidian, Dataview gives live-updating tables without external commands. Keep Dataview queries in **dashboard files** (`sales/dashboard.md`) that are git-tracked so the queries themselves are versioned:

```dataview
TABLE value_eur AS €, stage, expected_close
FROM "clients/deals"
WHERE stage != "won" AND stage != "lost"
SORT value_eur DESC
```

### F.6 Automated reports via GitHub Actions

Three scheduled jobs cover routine reporting:

| Report | Cadence | Trigger | Output |
|---|---|---|---|
| Pipeline snapshot | on push to `clients/deals/` or `alpha-log/` | pre-merge action | `sales/pipeline.md` |
| Weekly report | Sunday 22:00 CET | cron action | `sales/reports/YYYY-Www.md` + agent email |
| Monthly revenue | 1st of month 08:00 CET | cron action | `finance/reports/YYYY-MM.md` + DATEV export |

The scripts are Python + PyYAML + DuckDB, <200 LOC each. No external service required. Output is committed back to the repo; `git log sales/reports/` is itself a history of business performance.

### F.7 Dashboards

Three options, in order of recommended adoption:

1. **Markdown dashboard files** regenerated into `sales/pipeline.md` — zero infra, works in any viewer.
2. **Obsidian Dataview dashboard** — for the founder's daily glance.
3. **Lightweight web UI** (Streamlit or Evidence.dev over DuckDB) — unlock when the team expands and non-technical members need to view pipeline.

Avoid building a custom web UI before the team phase — it is premature optimisation.

---

## Part G — AI-agent integration

R1 approved three sales roles: `sales-lead` (senior), `sales-research` (junior), `sales-outreach` (junior). A fourth role, `analyst`, consumes CRM data for reporting. Each agent has a **read-set** and a **write-set** over the CRM folder; context loading must be minimal.

### G.1 Read/write matrix

| Agent | Reads | Writes |
|---|---|---|
| `sales-research` | web sources, `wiki/**`, `clients/skus/**` | `clients/companies/<new>.md`, `clients/leads/<new>.md` |
| `sales-lead` | `sales/pipeline.md`, `clients/deals/**`, `clients/contacts/**`, `clients/skus/**`, `roles/sales-lead.md` (manifest) | `clients/deals/**` (stage, value, notes), `clients/activities/**`, `clients/contracts/drafts/**`, `alpha-log/*.jsonl` |
| `sales-outreach` | specific `clients/contacts/<target>.md`, `clients/companies/<target>.md`, `sales/playbooks/**` | `clients/activities/<new>.md`, `alpha-log/*.jsonl` |
| `analyst` | `clients/**`, `alpha-log/**`, `finance/**` | `sales/reports/**`, `finance/reports/**` — NEVER touches `clients/*` |

Enforcement: git pre-commit hook rejects commits where author (git `user.name` = agent id) writes outside the allowed paths.

### G.2 Decision-rights (from R1)

`sales-lead` may:

- Qualify / disqualify leads (emits `lead.qualified` or `lead.disqualified`).
- Advance deal stages up to `negotiation`.
- Grant discounts up to 10% (`discount_pct ≤ 10`).
- Draft (not sign) contracts.

`sales-lead` MUST escalate to human (Ruslan) when:

- Deal value > €40K.
- Discount > 10%.
- Competitor named is in escalation list (e.g., Big-Four consulting).
- Contract amendment affects liability or IP clauses.

Escalation is mechanical: the agent creates a `ops/decisions/YYYY-MM-DD-<slug>.md` file with `approval_required_from: ruslan` and `status: pending`, and does not proceed.

### G.3 Context loading: what each agent reads when a task arrives

Agent context windows are precious. Rule: **load the minimum that lets the agent answer correctly**.

**sales-lead receives task "advance deal Acme to negotiation":**

```
Load:
  - roles/sales-lead.md                               # role manifest, decision-rights (~2KB)
  - clients/deals/2026-04-20-acme-audit.md            # target deal (~3KB)
  - clients/companies/acme-gmbh.md                    # company context (~3KB)
  - clients/contacts/hans-mueller.md                  # primary contact (~2KB)
  - clients/activities/2026-*-acme-*.md               # last 10 activities (~10KB)
  - clients/skus/ai-readiness-audit.md                # SKU template (~2KB)
  - sales/pipeline.md (excerpt: deals where company=acme-gmbh)  # ~1KB
TOTAL: ~23KB — fits any context window.

DO NOT LOAD:
  - Other clients' deals (context explosion, privacy risk).
  - Full alpha-log.
  - Wiki ingestion beyond SKU.
```

**sales-research receives task "research TargetCorp GmbH as lead":**

```
Load:
  - roles/sales-research.md                           # ~1KB
  - wiki/icp/mittelstand-manufacturing.md             # ICP definition (~3KB)
  - clients/companies/*.md frontmatter only (to dedupe) # ~5KB
  - web (Handelsregister, LinkedIn, Destatis)
TOTAL: ~9KB before web.
```

**sales-outreach receives task "send LinkedIn DM to Hans Müller":**

```
Load:
  - roles/sales-outreach.md                           # ~1KB
  - clients/contacts/hans-mueller.md                  # ~2KB
  - clients/companies/acme-gmbh.md                    # ~3KB
  - sales/playbooks/linkedin-first-touch.md           # ~3KB
  - last 2 activities for this contact                # ~2KB
TOTAL: ~11KB.
```

### G.4 Agent write protocol

Every agent write follows the same six steps:

1. Read target file (if exists).
2. Compute new content, validate against JSON Schema.
3. Write to working tree.
4. Append event to `alpha-log/YYYY-MM.jsonl`.
5. Commit with message `[agent:<id>][<event-type>] <entity>: <short summary>`.
6. Push to a feature branch `agent/<id>/<task-id>`; human merges after review in team phase (direct to main in solo phase).

The commit message convention makes `git log --grep '\[agent:sales-lead\]'` instantly useful.

### G.5 Analyst agent

Analyst runs on a cron (weekly, monthly, quarterly). It uses DuckDB over `clients/**/*.md` and `alpha-log/*.jsonl` to produce:

- Win/loss analysis (past quarter's `deal.won` vs `deal.lost` events, grouped by source, SKU, lost_reason).
- CAC estimation (total outreach costs / won deals).
- Pipeline aging (deals stuck >14 days in same stage).

Output is always a committed markdown file; the analyst never mutates `clients/`.

---

## Part H — Scale: solo → 100 → 1000 clients

### H.1 Phase table

| Phase | Active deals | Team size | CRM state | Query tier | Migration pressure |
|---|---|---|---|---|---|
| Solo | 0–20 | 1 human + agents | Pure git+md | grep + jq | none |
| Small team | 20–100 | 2–5 humans + agents | Git+md canonical; Notion or Obsidian Publish as read-only mirror | DuckDB default | low |
| Scale | 100–500 | 5–20 humans | HubSpot canonical; git retains strategic docs, SOPs, templates, agent code | HubSpot + git | active migration |
| Mega-corp | 500+ | 20+ | Salesforce + dbt-modelled warehouse; git retains decisions only | Warehouse SQL | complete |

### H.2 Merge conflict risk in small-team phase

Once two humans edit the same `deals/<id>.md` simultaneously, merge conflicts appear. Mitigation:

1. **Ownership field** (`owner: <user>`) — convention that only the owner edits frontmatter fields.
2. **Event log bypass** — stage-change events go to `alpha-log/` which is append-only (no merges possible on `.jsonl` when both sides only append).
3. **Field-level locking via directory structure** — if conflicts become painful, split `deals/<id>/` into `deals/<id>/profile.md` (slow-change) and `deals/<id>/state.md` (fast-change). This is the last resort before migrating.

### H.3 Migration to HubSpot: what carries over

HubSpot's import format is CSV per object, with unique keys (Email for contacts, Company name or Domain for companies, Record ID for deals) used to build associations ([HubSpot — Sample import files](https://knowledge.hubspot.com/import-and-export/sample-import-files)). A migration script should:

1. Emit `companies.csv` from `clients/companies/*.md` frontmatter.
2. Emit `contacts.csv` from `clients/contacts/*.md`, with `Company name` referencing the company slug.
3. Emit `deals.csv` from `clients/deals/*.md`, with `Deal name` = deal id and association columns for companies and contacts.
4. Emit `activities.csv` for each activity type (calls, emails, meetings, notes) with reference to deal/contact ids.
5. Emit `engagements.csv` of historical events from `alpha-log/` for auditing — HubSpot accepts them as notes.

Field names in Jetix YAML were deliberately chosen to match HubSpot/EspoCRM defaults where possible (e.g., `primary_contact`, `expected_close`, `value_eur`). Salesforce migration follows the same pattern: Data Loader with `RelationshipName.IndexedFieldName` syntax to preserve N:M associations ([Salesforce Help — Prepare a CSV File for Import](https://help.salesforce.com/s/articleView?id=000381876), [Salesforce Developers — Data Loader Field Mappings](https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/defining_field_mappings.htm)).

### H.4 What stays in git after migration

Even after HubSpot/Salesforce migration, git remains canonical for:

- Contract templates (legally sensitive, version-controlled).
- SOW drafts awaiting signature.
- Sales playbooks, ICP analysis, strategic notes.
- Agent role manifests and role-based access definitions.
- Postmortems and loss-reason analyses.
- Decision records (R-series from R2's RFD methodology).

HubSpot becomes the **operational CRM** (pipeline, activities, communications); git remains the **strategic CRM** (playbooks, decisions, learnings). This is the same split Vercel, Gitlab, and Linear operate internally.

### H.5 Triggers for migration

Quantitative triggers:

| Metric | Threshold | Action |
|---|---|---|
| Active deals | 50 | Add DuckDB-backed dashboard, evaluate Notion as read-only mirror |
| Active deals | 100 | Start HubSpot evaluation; begin bi-directional sync prototype |
| Team members editing CRM | 3 | Must have proper RBAC; HubSpot likely mandatory |
| Monthly conflicts in `deals/` | >2 | Accelerate migration |
| Query latency on DuckDB | >5s | Migration overdue |
| Legal request for detailed audit | any | Exercise git log audit trail; confirm migration preserves it |

Qualitative triggers: any non-technical team member cannot work with markdown; any auditor refuses to accept git history as evidence.

### H.6 Multi-product isolation (L3/L4/L5)

Jetix runs three commercial surfaces: L3 Jetix Club (community subscriptions, Stripe), L4 Delivery (consulting, this CRM), L5 Alliance (AI-agent ecosystem). Each has a distinct customer type. Keep them physically separated:

```
clients/         # L4 Delivery only
members/         # L5 Alliance members (different schema)
subscribers/     # L3 Club subscribers (lightweight: email + plan + status, minimal PII)
```

Never merge these folders — different lawful bases under GDPR, different consent capture, different retention. A single query across them is a Dataview/DuckDB `UNION` when needed for executive reporting.

---

## Part I — GDPR and compliance

GDPR is not optional for Jetix — Berlin-based controller, EU data subjects, Mittelstand clients who will ask about DPIAs during procurement.

### I.1 Lawful basis per entity

| Entity | Lawful basis (Art. 6 GDPR) | Notes |
|---|---|---|
| Lead contacted first time | Art. 6(1)(f) legitimate interest | B2B business contact data; balancing test documented |
| Contact after opt-in to newsletter | Art. 6(1)(a) consent | Must be revocable |
| Contact in active commercial negotiation | Art. 6(1)(b) pre-contract | Contract performance |
| Contact with signed contract | Art. 6(1)(b) contract performance + Art. 6(1)(c) legal obligation (tax) | |
| Invoice | Art. 6(1)(c) legal obligation | § 147 AO — 10-year retention |
| Communication archive (email, call) | Art. 6(1)(f) legitimate interest | Balancing test + minimisation |

Every Company / Contact file carries `gdpr_lawful_basis: <value>` in frontmatter, auditable by script.

### I.2 Right to erasure (Art. 17) vs git

Git history is append-only; once committed, data is durable through clones. Art. 17 requires erasure "without undue delay", within one month of a valid request ([Pro Backup — GDPR and Backups 2026](https://www.probackup.io/blog/gdpr-and-backups-how-to-handle-deletion-requests), [Jetico — Right to Erasure guide](https://jetico.com/blog/how-right-erasure-applied-under-gdpr-complete-guide-organizational-compliance/), [hoop.dev — GDPR Compliance in Git](https://hoop.dev/blog/gdpr-compliance-in-git-preventing-data-leaks-and-protecting-privacy/)).

Three valid approaches, in increasing order of cost:

1. **Pseudonymise in place**: replace `full_name`, `email`, `phone` with `"[erased per GDPR request YYYY-MM-DD]"`. Commit the change. The historical data remains in old commits, but Art. 17 is interpreted by most DPAs (French CNIL, Danish Datatilsynet) as satisfied when live data is gone and the data in "backups" (here, git history) is "put beyond use" and will expire on retention schedule ([Pro Backup 2026 analysis](https://www.probackup.io/blog/gdpr-and-backups-how-to-handle-deletion-requests)). Document the retention ceiling (e.g., 10 years for legal obligations, then forced history-rewrite).
2. **Rewrite git history** with `git filter-repo` or BFG Repo-Cleaner to scrub specific files from all commits, then force-push ([hoop.dev — GDPR in Git](https://hoop.dev/blog/gdpr-compliance-in-git-preventing-data-leaks-and-protecting-privacy/)). Heavy operation, must be coordinated with all clones, disrupts CI.
3. **Segregated PII**: keep personally identifying fields in a separate, **never-committed** file (`.gdpr/contacts.yaml`, gitignored, encrypted, backed up separately). The git-tracked file holds only a pseudonymous id. Erasure is then a plain file delete. This is the recommended pattern for any field that might later require erasure (email, phone, message bodies).

Jetix's policy should combine (1) and (3): pseudonymise in-place for quick compliance; for high-risk fields (private mobile numbers, personal email when the person is only a gatekeeper), use the segregated pattern from day one.

### I.3 Exceptions to Art. 17

Art. 17(3) allows retention for legal obligations, defence of legal claims, or public interest. For Jetix:

- **Invoices** (§ 147 AO — 10-year tax retention) override erasure requests. Name on an invoice cannot be erased for 10 years after issuance.
- **Signed contracts** retained under limitation periods.
- **Communication records** related to active claims — retain until resolution.

Document each exception in `compliance/retention-matrix.md`, git-tracked, reviewed annually.

### I.4 Encryption at rest: SOPS + age

R2 recommended SOPS + age. Implementation ([OneUptime — SOPS with Age for K8s](https://oneuptime.com/blog/post/2026-02-09-sops-age-encryption-kubernetes-secrets/view), [Datenkollektiv — SOPS with Age and Git](https://devops.datenkollektiv.de/using-sops-with-age-and-git-like-a-pro.html), [DEV — SOPS and AGE](https://dev.to/waqasahmed/securely-encrypting-secrets-using-open-source-tools-sops-and-age-3g46)):

```yaml
# .sops.yaml at repo root
creation_rules:
  # Full-file encrypt for communications archive metadata
  - path_regex: clients/activities/.*\.eml\.ya?ml$
    age: age1publickey…
  # Selective field encryption for contact PII
  - path_regex: clients/contacts/.*\.md$
    encrypted_regex: ^(email|phone|private_phone|personal_email|address|dob)$
    age: age1publickey…
  # Secrets repo — bank details, API keys
  - path_regex: secrets/.*\.ya?ml$
    age: age1publickey…
```

Selective field encryption preserves git diff usefulness for non-PII fields (stage, value, probability) while protecting regulated fields. Keys are per-person; multi-key encryption (`--age alice,bob,charlie`) enables team access without shared private keys.

Rotation runbook is pre-written in `ops/runbooks/rotate-age-keys.md` and exercised annually.

### I.5 Access control

Solo phase: git file permissions + local disk encryption are enough.

Team phase: move sensitive sub-trees to separate repositories with GitHub CODEOWNERS and branch protection. Proposed split:

- `jetix/company-core` — playbooks, templates, strategy (team-wide read).
- `jetix/company-ops` — pipeline, deals, activities (sales team only).
- `jetix/company-finance` — invoices, bank details (founder + Steuerberater).
- `jetix/secrets` — encrypted only, key-based access.

When file-level RBAC becomes necessary (regulated data, DORA scope, etc.), migrate to HubSpot / Salesforce (Part H).

### I.6 Audit trail hardening

Git log is free audit trail but must be **tamper-evident**. Three measures:

1. Branch protection on `main`: no force-push, no rewrite.
2. Signed commits (`git commit -S`, GPG or SSH signatures). Agent commits use per-agent signing keys.
3. Quarterly commit-hash anchoring: publish the current `main` hash to a public timestamping service (e.g., Bitcoin OpenTimestamps or an internal HSM) so tampering is detectable.

Commit messages must not themselves contain PII — they become part of the audit trail and cannot be scrubbed easily. Enforce in the pre-commit hook with a regex against email/phone patterns.

---

## Part J — Practical output for Jetix

This is the build blueprint. Everything below is copy-paste ready.

### J.1 Full folder structure

```
jetix/                                          # monorepo root
├── clients/
│   ├── companies/
│   │   └── <slug>.md                           # company profile
│   ├── contacts/
│   │   └── <slug>.md                           # person profile
│   ├── leads/
│   │   └── <slug>.md                           # pre-qualified
│   ├── deals/
│   │   └── YYYY-MM-DD-<slug>.md                # opportunity
│   ├── activities/
│   │   └── YYYY-MM-DD-<slug>.md                # email/call/meeting
│   ├── contracts/
│   │   ├── templates/
│   │   │   ├── ai-readiness-audit.md.tmpl
│   │   │   ├── quick-win-automation.md.tmpl
│   │   │   ├── custom-agent-build.md.tmpl
│   │   │   └── operations-retainer.md.tmpl
│   │   ├── drafts/
│   │   │   └── <deal-slug>.md
│   │   └── signed/
│   │       └── <contract-id>.md  (+ .pdf, + .xml for ZUGFeRD)
│   ├── invoices/
│   │   └── YYYY/
│   │       └── R-YYYY-NNNN.md  (+ .pdf, + .xml)
│   └── skus/
│       ├── ai-readiness-audit.md
│       ├── quick-win-automation.md
│       ├── custom-agent-build.md
│       └── operations-retainer.md
├── sales/
│   ├── pipeline.md                             # regenerated projection
│   ├── dashboard.md                            # Dataview queries (Obsidian)
│   ├── reports/
│   │   └── YYYY-Www-weekly.md
│   └── playbooks/
│       ├── linkedin-first-touch.md
│       ├── discovery-call.md
│       └── proposal-followup.md
├── finance/
│   ├── next-invoice-number.txt                 # counter
│   ├── ledger.md                               # projection from invoice events
│   ├── reports/
│   │   └── YYYY-MM.md
│   └── datev/
│       └── YYYY-MM.csv                         # export for Steuerberater
├── alpha-log/
│   └── YYYY-MM.jsonl                           # append-only event stream
├── schemas/
│   ├── company.schema.json
│   ├── contact.schema.json
│   ├── lead.schema.json
│   ├── deal.schema.json
│   ├── contract.schema.json
│   ├── invoice.schema.json
│   └── activity.schema.json
├── roles/
│   ├── sales-lead.md                           # role manifest (R1)
│   ├── sales-research.md
│   ├── sales-outreach.md
│   └── analyst.md
├── compliance/
│   ├── retention-matrix.md                     # GDPR retention rules
│   ├── dpia/                                   # one DPIA per high-risk activity
│   └── subject-access-requests/
├── ops/
│   ├── tasks/                                  # follow-up items
│   ├── decisions/                              # agent-generated escalations
│   └── runbooks/
├── scripts/
│   ├── validate.py                             # JSON Schema validation
│   ├── render-sow.py
│   ├── project.py                              # re-project events into snapshots
│   ├── pipeline-snapshot.py
│   ├── datev-export.py
│   ├── hubspot-export.py                       # migration trigger
│   └── gdpr-erase.py                           # Art. 17 handler
├── .sops.yaml                                  # encryption rules
└── .github/workflows/                          # CI actions
    ├── validate.yml
    ├── weekly-report.yml
    └── monthly-revenue.yml
```

### J.2 Copy-paste YAML schemas

**Company** (`schemas/company.schema.json` excerpt, here as YAML template):

```yaml
---
id: <slug-kebab>                 # required, immutable, ^[a-z0-9-]{2,40}$
type: company
legal_name: <string>             # required
trade_name: <string>             # optional display
legal_form: GmbH                 # enum: GmbH | AG | GmbH & Co. KG | UG | GbR | eG | other
hrb: <string>                    # e.g. "HRB 12345 Berlin"
ust_id: <DE-VAT-id>              # optional, format: DE[0-9]{9}
steuernummer: <string>           # optional
industry: <string>
industry_wz: <WZ-code>           # Destatis WZ 2008
employees: <int>
revenue_eur: <number>
location:
  street: <string>
  postcode: <string>
  city: <string>
  country: DE                    # ISO 3166-1 alpha-2
website: <url>
linkedin: <url>
status: active                   # enum: prospect | active | churned | archived
icp_score: <int 1..10>
tags: [<string>…]
sources: [<string>…]             # how we found them
owner: <role or person>          # default: sales-lead
gdpr_lawful_basis: legitimate_interest  # enum per Part I.1
parent_company: <slug|null>
created: YYYY-MM-DD              # required
updated: YYYY-MM-DD              # required
---
# Notes
Free-form long-form notes, ICP fit analysis, strategic context.
```

**Contact**:

```yaml
---
id: <slug-kebab>                 # required, immutable
type: contact
company: <company-slug>          # required FK
full_name: <string>              # required
salutation: Herr                 # enum: Herr | Frau | Divers | null
title_prefix: <string>           # e.g. "Dr.", "Prof. Dr.-Ing."
role: <string>                   # Geschäftsführer | CFO | IT-Leiter | Prokurist | Einkäufer | …
decision_power: influencer       # enum: sponsor | decision-maker | influencer | blocker | champion | user
department: <string>
email: <email>                   # consider encrypted_regex
phone: <string>
linkedin: <url>
language: de                     # de | en
consent:
  marketing: false
  processing: legitimate_interest
  captured_at: YYYY-MM-DD
  captured_method: <string>      # inbound-form | verbal-meeting-…
status: active                   # enum: active | archived | erased
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Lead**:

```yaml
---
id: <slug-kebab>
type: lead
company_name: <string>           # company may not yet have a slug
proposed_company_slug: <slug>
primary_contact_name: <string>
primary_contact_email: <email>
primary_contact_role: <string>
icp_match: <bool>
icp_score: <int 1..10>
source: <string>                 # linkedin-outreach | IHK-event | referral | …
first_contact: YYYY-MM-DD
stage: new                       # enum: new | contacted | qualified | disqualified | promoted
qualified_at: <date|null>
promoted_at: <date|null>         # when promoted, becomes Company + Contact + Deal
disqualified_reason: <string|null>
owner: sales-research
gdpr_lawful_basis: legitimate_interest
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Deal**:

```yaml
---
id: YYYY-MM-DD-<slug>            # e.g. 2026-04-20-acme-audit
type: deal
company: <company-slug>          # required
primary_contact: <contact-slug>  # required
contacts: [<contact-slug>…]
sku: <sku-slug>                  # required, from clients/skus/
stage: proposal                  # enum: lead | qualified | proposal | negotiation | won | lost | churned
probability: 0.4                 # 0..1, overrides stage default
value_eur: <number>
currency: EUR
expected_close: YYYY-MM-DD
competitor: <slug|null>
source: <string>
owner: sales-lead
discount_pct: 0                  # 0..10 by sales-lead; >10 requires escalation
lost_reason: <string|null>
won_at: <date|null>
contract: <contract-id|null>
notes_path: ./notes.md           # optional sidecar
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Activity**:

```yaml
---
id: YYYY-MM-DD-<slug>
type: activity
channel: email.sent              # enum: email.sent | email.received | call | meeting | linkedin-message | note
deal: <deal-id|null>
contact: <contact-slug|null>     # at least one of deal/contact required
company: <company-slug|null>
participants: [<contact-slug>…]
duration_min: <int|null>
summary: <string>                # required, human-readable 1-5 sentences
transcript_path: <path|null>     # if meeting with transcript
body_hash: <sha256|null>         # for emails, hash of the MIME message
body_ref: <path|null>            # path to encrypted blob outside git
subject: <string|null>
from_address: <string|null>
to_addresses: [<string>…]
cc_addresses: [<string>…]
occurred_at: YYYY-MM-DDTHH:MM:SS+02:00  # required, Europe/Berlin offset
actor: <user-or-agent-id>
agent: <agent-id|null>
gdpr_lawful_basis: legitimate_interest
---
# Narrative
Optional long-form notes. Always safe to read by agents with proper role.
```

**Contract**:

```yaml
---
id: <contract-id>                # e.g. acme-audit-2026-04
type: contract
deal: <deal-id>
company: <company-slug>
sku: <sku-slug>
contract_type: SOW               # enum: SOW | MSA | NDA | Amendment | Retainer
status: signed                   # enum: draft | sent | signed | active | completed | cancelled
drafted_at: YYYY-MM-DD
signed_at: YYYY-MM-DD
counterparty_signatory: <contact-slug>
our_signatory: ruslan
value_net_eur: 7500
vat_rate: 0.19
effective_from: YYYY-MM-DD
effective_until: YYYY-MM-DD
deliverables: [<string>…]
acceptance_criteria: [<string>…]
payment_terms: "Net 14, SEPA"
governing_law: "Germany"
jurisdiction: "Berlin"
docusign_envelope_id: <string|null>
pdf_path: <path>
xml_path: <path|null>            # ZUGFeRD XML if e-invoice track
amends: <contract-id|null>       # for amendments
retention_ceiling: 10y           # GoBD + limitation period
---
```

**Invoice** (already shown in E.3, full schema):

```yaml
---
id: R-YYYY-NNNN                  # required, sequential Rechnungsnummer, immutable
type: invoice
contract: <contract-id>          # required unless ad-hoc
deal: <deal-id>
company: <company-slug>
issued: YYYY-MM-DD               # Ausstellungsdatum
performance_date: YYYY-MM        # Leistungszeitpunkt (month sufficient)
due: YYYY-MM-DD
kleinbetrag: false               # true if total_gross ≤ 250 EUR
line_items:
  - description: <string>
    qty: <number>
    unit_price_net: <number>
    vat_rate: 0.19               # 0.19 | 0.07 | 0.00
    vat_amount: <number>
    line_total_gross: <number>
subtotal_net: <number>
vat_breakdown:
  - rate: 0.19
    base: <number>
    amount: <number>
discounts: <number|null>         # im Voraus vereinbarte Minderungen
total_gross: <number>
currency: EUR
payment_method: sepa             # sepa | stripe | paypal
bank: { iban, bic, bank_name }
issuer:
  name: "Jetix UG (haftungsbeschränkt)"
  address: "…"
  steuernummer: "…"
  ust_id: "DE…"
  signatory: Ruslan
recipient:
  name: <company-legal-name>
  address: <string>
  ust_id: <string|null>
reverse_charge: false            # § 13b UStG — note "Steuerschuldnerschaft des Leistungsempfängers"
status: sent                     # draft | issued | sent | paid | partially-paid | disputed | corrected
sent_at: <timestamp|null>
paid_at: <timestamp|null>
paid_amount: <number|null>
stripe_invoice_id: <string|null>
retention_ceiling: 10y           # § 147 AO
---
```

### J.3 Four filled example files

**`clients/companies/test-gmbh.md`**:

```markdown
---
id: test-gmbh
type: company
legal_name: "Test Maschinenbau GmbH"
trade_name: "Test"
legal_form: GmbH
hrb: "HRB 54321 München"
ust_id: "DE987654321"
steuernummer: "143/123/45678"
industry: "machine building — precision components"
industry_wz: "28.41"
employees: 220
revenue_eur: 58000000
location:
  street: "Industriestraße 12"
  postcode: "80336"
  city: "München"
  country: DE
website: https://test-gmbh.example
linkedin: https://www.linkedin.com/company/test-gmbh
status: prospect
icp_score: 9
tags: [mittelstand, manufacturing, dach-core, ai-readiness-prime]
sources: [linkedin-outreach]
owner: sales-lead
gdpr_lawful_basis: legitimate_interest
parent_company: null
created: 2026-04-20
updated: 2026-04-20
---

## ICP Analysis

Test GmbH fits Jetix ICP strongly:

- 220 employees, €58M revenue — core Mittelstand band.
- Bavarian precision manufacturer, likely complex ERP (SAP Business One) — automation opportunity.
- LinkedIn signals: CFO posted about "KI-Strategie 2026" in March.
- No visible internal AI capability; no known Big-Four consulting engagement.

## Relationships

Primary contact: [[hans-mueller]] (Geschäftsführer).
Secondary: [[sabine-weber]] (CFO).

## Strategic notes

Entry via AI Readiness Audit. CFO-posted interest is opening — lead with audit, not with automation.
```

**`clients/contacts/hans-mueller.md`**:

```markdown
---
id: hans-mueller
type: contact
company: test-gmbh
full_name: "Hans Müller"
salutation: Herr
title_prefix: "Dr."
role: "Geschäftsführer"
decision_power: decision-maker
department: Geschäftsleitung
email: hans.mueller@test-gmbh.example
phone: "+49 89 1234567"
linkedin: https://www.linkedin.com/in/hansmueller
language: de
consent:
  marketing: false
  processing: legitimate_interest
  captured_at: 2026-04-20
  captured_method: "B2B outreach per § 7 UWG, legitimes Interesse dokumentiert"
status: active
created: 2026-04-20
updated: 2026-04-20
---

## Profile

Dr. Hans Müller, Geschäftsführer seit 2019. Maschinenbau-Ingenieur, promoviert TU München.
Signals: pragmatic, ROI-driven, suspicious of "AI hype" per LinkedIn comments.

## Interaction cadence

Prefers Thursday mornings. Does not read cold emails before 9:30. LinkedIn DMs get ~24h response time if personalised.
```

**`clients/deals/2026-04-20-test-audit.md`**:

```markdown
---
id: 2026-04-20-test-audit
type: deal
company: test-gmbh
primary_contact: hans-mueller
contacts: [hans-mueller, sabine-weber]
sku: ai-readiness-audit
stage: qualified
probability: 0.5
value_eur: 7500
currency: EUR
expected_close: 2026-06-15
competitor: null
source: linkedin-outreach
owner: sales-lead
discount_pct: 0
lost_reason: null
won_at: null
contract: null
created: 2026-04-20
updated: 2026-04-20
---

## Context

Discovery call on 2026-04-20 confirmed fit. Hans is sponsor; Sabine (CFO) controls budget.
Next step: proposal by 2026-04-27, targeting signature first week of May.

## Open questions

- IT landscape: confirmed SAP B1 + custom Excel layer (to validate).
- Decision process: GF + CFO sufficient for €5-8K; IT-Leiter involved for automation follow-up.
```

**`clients/activities/2026-04-20-test-discovery-call.md`**:

```markdown
---
id: 2026-04-20-test-discovery-call
type: activity
channel: meeting
deal: 2026-04-20-test-audit
contact: hans-mueller
company: test-gmbh
participants: [hans-mueller, sabine-weber, ruslan]
duration_min: 42
summary: >
  Discovery call. Hans confirmed interest in AI Readiness Audit. Sabine joined for budget discussion.
  Primary pain: invoice processing latency (14 days → target 3 days). Open to €5-8K audit as entry point.
  Next step: written proposal by 2026-04-27.
transcript_path: ./2026-04-20-test-discovery-call.transcript.md
body_hash: null
body_ref: null
subject: null
occurred_at: 2026-04-20T10:00:00+02:00
actor: ruslan
agent: null
gdpr_lawful_basis: legitimate_interest
---

## Agenda

1. Short company intro (Ruslan).
2. Test GmbH's AI-related pain points (Hans, Sabine).
3. Jetix AI Readiness Audit overview.
4. Q&A, next steps.

## Key decisions

- Proceed to written proposal (2026-04-27 target).
- Sabine sign-off authority for €5-10K.
- IT-Leiter (Peter Wagner) to be looped in on implementation phase, not on audit.

## Action items

- [ ] Ruslan: send proposal PDF via DocuSign by 2026-04-27.
- [ ] Ruslan: send one-pager on Jetix case studies.
- [ ] Hans: confirm IT-Leiter availability for kick-off week of 2026-05-11.

## Risks

- Sabine mentioned "we already tried an automation consultant last year, didn't work" — differentiate on deliverable quality and SOW precision.
```

### J.4 Event-sourcing decision — verdict

**Use the hybrid snapshot + event log pattern from day one, minimal ceremony**:

- State-change events (`*.stage-changed`, `*.qualified`, `*.won`, `*.lost`, `*.paid`) → always event-logged.
- Activity events (`activity.logged`, `email.sent`, `call.logged`, `meeting.held`) → always event-logged.
- Field edits on Company/Contact → git commit sufficient, no event.
- Projection rebuilds on every PR via CI action (takes <1s for first hundred entities).

This captures the 20% of events that drive 80% of the audit and reporting value, without the full ceremony of strict event sourcing.

### J.5 Communications pattern — verdict

- **Emails**: IMAP sync to `~/jetix-comms/maildir/` outside git. Activity files reference hashes.
- **Meeting notes**: inline in `clients/activities/*.md`; transcripts as sidecar files.
- **Call logs**: 2–10 sentences inline in activity file.
- **LinkedIn messages**: weekly export script → `clients/activities/*.md` with `channel: linkedin-message`.
- **Binary attachments**: if under 1 MB and not PII, in git; else in encrypted S3 with hash reference.

### J.6 Contract workflow

```
1. Deal moves to stage: proposal.
2. sales-lead agent runs `scripts/render-sow.py --deal 2026-04-20-test-audit`.
3. Draft markdown + PDF generated in clients/contracts/drafts/2026-04-20-test-audit.md.
4. Human reviews (Ruslan).
5. On acceptance: render ZUGFeRD-compatible PDF, upload to DocuSign.
6. DocuSign webhook triggers a script on signature completion → files moved to clients/contracts/signed/<id>.md (append-only).
7. `contract.signed` event logged. Deal.contract field updated.
```

### J.7 Invoicing pattern

```
1. Contract signed + work delivered → sales-lead or analyst agent triggers `scripts/issue-invoice.py --contract <id>`.
2. Script reads next number from finance/next-invoice-number.txt, increments atomically.
3. Emits markdown invoice + PDF (via pandoc+eisvogel) + ZUGFeRD XML embedded in PDF/A-3.
4. `invoice.issued` event logged.
5. Invoice emailed via Stripe Invoice link or direct SEPA payment link.
6. `invoice.sent` event logged.
7. Bank statement import (CAMT.053) weekly → matches by Rechnungsnummer in purpose field → `invoice.paid` or `invoice.partially-paid` events.
8. Monthly DATEV export for Steuerberater.
```

### J.8 Agent decision tree (sales-lead canonical flow)

```
Task arrives: "advance deal X to next stage"
  ↓
Load role manifest (roles/sales-lead.md)
  ↓
Load target deal (clients/deals/<id>.md)
  ↓
Load company + primary contact + SKU (3 files)
  ↓
Load last 5 activities for this deal
  ↓
Check decision-rights: is target stage within agent authority?
  ├── No (stage = signed, value > €40K, discount > 10%) → create ops/decisions/<id>.md with status:pending, STOP
  └── Yes →
      ↓
      Run stage-specific logic:
        · lead → qualified: ICP match check, BANT criteria
        · qualified → proposal: draft proposal, call render-sow.py
        · proposal → negotiation: verify signed NDA, check competitor field
        · negotiation → won: require contract: non-null, escalate to human
      ↓
      Update deal YAML (stage, probability, updated).
      Append event to alpha-log/YYYY-MM.jsonl.
      Commit: [agent:sales-lead][deal.stage-changed] <deal-id>: qualified → proposal
      Push to feature branch (team) or main (solo).
```

### J.9 Query cookbook — 12 common queries

**1. All active deals > €10K (DuckDB)**

```sql
SELECT frontmatter->>'id'       AS deal,
       frontmatter->>'company'  AS company,
       (frontmatter->>'value_eur')::DOUBLE AS value,
       frontmatter->>'stage'    AS stage,
       frontmatter->>'expected_close' AS close
FROM read_markdown('clients/deals/*.md')
WHERE stage IN ('qualified','proposal','negotiation')
  AND (frontmatter->>'value_eur')::DOUBLE > 10000
ORDER BY value DESC;
```

**2. Deals stuck in negotiation > 14 days (jq)**

```bash
for f in clients/deals/*.md; do
  yq --front-matter=extract -o=json "$f" | jq -r '
    select(.stage == "negotiation") |
    select((now - (.updated | strptime("%Y-%m-%d") | mktime)) > 14*86400) |
    "\(.id)\t\(.updated)\t\(.value_eur)"
  '
done
```

**3. Clients with no activity > 30 days (DuckDB)**

```sql
SELECT c.frontmatter->>'id' AS company,
       MAX(a.frontmatter->>'occurred_at') AS last_touch
FROM read_markdown('clients/companies/*.md') c
LEFT JOIN read_markdown('clients/activities/*.md') a
  ON a.frontmatter->>'company' = c.frontmatter->>'id'
GROUP BY company
HAVING last_touch IS NULL
    OR CAST(last_touch AS TIMESTAMP) < NOW() - INTERVAL 30 DAY;
```

**4. Revenue this quarter (DuckDB, from invoice events)**

```sql
SELECT SUM((frontmatter->>'total_gross')::DOUBLE) AS revenue_eur_gross
FROM read_markdown('clients/invoices/**/*.md')
WHERE frontmatter->>'status' = 'paid'
  AND CAST(frontmatter->>'paid_at' AS DATE)
      BETWEEN DATE_TRUNC('quarter', CURRENT_DATE)
          AND CURRENT_DATE;
```

**5. Pipeline value by stage (DuckDB)**

```sql
SELECT frontmatter->>'stage' AS stage,
       COUNT(*) AS count,
       SUM((frontmatter->>'value_eur')::DOUBLE) AS total_value,
       SUM((frontmatter->>'value_eur')::DOUBLE *
           (frontmatter->>'probability')::DOUBLE) AS weighted_value
FROM read_markdown('clients/deals/*.md')
WHERE stage NOT IN ('won','lost','churned')
GROUP BY stage
ORDER BY weighted_value DESC;
```

**6. Win rate by source (DuckDB, last 12 months)**

```sql
WITH deals_closed AS (
  SELECT frontmatter->>'source' AS source,
         frontmatter->>'stage'  AS stage
  FROM read_markdown('clients/deals/*.md')
  WHERE stage IN ('won','lost')
    AND CAST(frontmatter->>'updated' AS DATE) > NOW() - INTERVAL 12 MONTH
)
SELECT source,
       COUNT(*) FILTER (WHERE stage = 'won') AS won,
       COUNT(*) FILTER (WHERE stage = 'lost') AS lost,
       COUNT(*) FILTER (WHERE stage = 'won')::DOUBLE / COUNT(*) AS win_rate
FROM deals_closed
GROUP BY source
ORDER BY win_rate DESC;
```

**7. All events for one client (jq over alpha-log)**

```bash
cat alpha-log/*.jsonl | jq -r 'select(.entity | startswith("deals/") or startswith("contacts/") or startswith("companies/test-gmbh"))
  | select(.related // [] | any(startswith("companies/test-gmbh")))
  | "\(.ts)\t\(.type)\t\(.entity)"' | sort
```

**8. Stuck pipeline — deals with no activity in 14 days (DuckDB)**

```sql
WITH last_activity AS (
  SELECT frontmatter->>'deal' AS deal,
         MAX(CAST(frontmatter->>'occurred_at' AS TIMESTAMP)) AS last
  FROM read_markdown('clients/activities/*.md')
  WHERE frontmatter->>'deal' IS NOT NULL
  GROUP BY deal
)
SELECT d.frontmatter->>'id' AS deal, l.last
FROM read_markdown('clients/deals/*.md') d
LEFT JOIN last_activity l ON l.deal = d.frontmatter->>'id'
WHERE d.frontmatter->>'stage' NOT IN ('won','lost','churned')
  AND (l.last IS NULL OR l.last < NOW() - INTERVAL 14 DAY)
ORDER BY l.last;
```

**9. Average deal cycle time — qualified → won (DuckDB)**

```sql
WITH events AS (
  SELECT entity,
         type,
         CAST(ts AS TIMESTAMP) AS ts
  FROM read_json('alpha-log/*.jsonl', format='newline_delimited')
)
SELECT AVG(DATE_DIFF('day', q.ts, w.ts)) AS avg_days_qualified_to_won
FROM events q
JOIN events w ON w.entity = q.entity
WHERE q.type = 'deal.stage-changed'
  AND w.type = 'deal.won'
  AND w.ts > q.ts;
```

**10. Open invoices (unpaid > 14 days) (grep + yq)**

```bash
rg -l '^status: sent$' clients/invoices/ | while read f; do
  yq --front-matter=extract -o=json "$f" | \
    jq -r 'select((now - (.sent_at | fromdateiso8601)) > 14*86400) |
           "\(.id)\t€\(.total_gross)\tsince \(.sent_at)"'
done
```

**11. All contacts at a company (Dataview, Obsidian)**

```dataview
TABLE role, decision_power, email
FROM "clients/contacts"
WHERE company = "test-gmbh"
SORT decision_power
```

**12. GDPR — all personal data we hold on one person (jq)**

```bash
# Contact file
cat "clients/contacts/hans-mueller.md"
# Activities mentioning them
rg -l 'hans-mueller' clients/activities/
# Events mentioning them
cat alpha-log/*.jsonl | jq 'select(.related // [] | any(endswith("hans-mueller")) or (.entity | endswith("hans-mueller")))'
# Invoices (usually none at contact level, but for completeness)
rg -l 'hans-mueller' clients/invoices/
```

### J.10 Migration triggers — concrete rules

| Trigger | Threshold | Action |
|---|---|---|
| Active deals | 50 | Introduce DuckDB pipeline dashboard in `sales/pipeline.md`; start evaluating Notion mirror |
| Active deals | 100 | Begin HubSpot evaluation, prototype bi-directional sync |
| Team members with write access | 3 | Must have branch protection + RBAC plan; HubSpot likely in 90 days |
| Team members with write access | 5 | HubSpot migration mandatory within the quarter |
| Merge conflicts / month in `clients/deals/` | >2 | Accelerate migration regardless of client count |
| DuckDB query latency (simple pipeline query) | >5 s | Migration overdue |
| Requested feature: per-field audit with author attribution | any | Reality-check: git log gives 90% of this; if the remaining 10% matters, migrate |
| Client required a formal Verarbeitungsverzeichnis extract | any | Stay on git but generate from schema; if too often, move |

### J.11 Jetix-specific anti-patterns

**Never do any of these.** All have been observed in similar projects:

| Anti-pattern | Why fatal |
|---|---|
| Storing full email MIME messages as git blobs | Repo inflates, diffs useless, Art. 17 erasure requires `git filter-repo` across all clones |
| Notion as canonical source of truth for L4 CRM | Breaks company-as-code, API rate limits, no git diff, no agent parity |
| Event sourcing before 10 deals exist | Over-engineering; maintenance cost > audit value |
| Putting everything in one `clients.md` file | Unsearchable, unresolvable merge conflicts, agents cannot target updates |
| Renaming slug-based entity files after creation | Breaks every backlink and every event reference |
| Committing plaintext API keys, bank IBANs, or personal phone numbers | GDPR breach + security incident; use SOPS+age with `.sops.yaml` |
| Skipping the pre-commit JSON Schema validator | Schema drift becomes untraceable; migration to HubSpot fails |
| Event log without monotonic timestamps | Replaying in wrong order produces wrong current state |
| Editing signed contracts in place | Breaks GoBD Unveränderbarkeit; always create amendments as new files |
| Invoice numbers with gaps or duplicates | Tax audit finding; sequential integrity is § 14 UStG requirement |
| Storing agent credentials in the same repo as encrypted data | If a single credential leaks, so does everything; split secrets repo |
| Relying on Dataview queries as the only reporting path | Breaks when vault is opened outside Obsidian; always have a DuckDB equivalent |

---

## Synthesis

The proposed architecture gives Jetix a CRM that is:

- **Diff-able**: every stage change, every activity, every invoice is a line in a commit.
- **Agent-friendly**: 7 YAML schemas, tight context-loading patterns, mechanical decision-rights enforcement.
- **GDPR-defensible**: lawful basis per entity, selective SOPS+age encryption, pseudonymise-first erasure policy, segregated high-risk PII.
- **GoBD-compliant**: immutable invoice records, sequential Rechnungsnummern, 10-year retention, ZUGFeRD-ready.
- **Portable**: HubSpot and Salesforce migration scripts fit inside a day when the time comes.
- **Measurable**: DuckDB over markdown + jq over alpha-log gives pipeline, revenue, win-rate, cycle-time, and GDPR reports without any external platform.

The 10 alpha entities from R3 map cleanly onto the 8 file types. The hybrid snapshot + event log resolves R3's commit-tagging proposal with something strictly more powerful, at trivial added complexity. Every German-specific requirement — Pflichtangaben per § 14 UStG, 10-year Aufbewahrungspflicht per § 147 AO, GoBD 2025 e-invoice archiving, Art. 17 right to erasure — has an explicit landing spot in either schema, encryption policy, or retention matrix.

The work from here is implementation: instantiate the folder structure, write the seven JSON Schemas, wire the pre-commit hook, build the four projection scripts, record the `retention-matrix.md`, and create the first `test-gmbh.md`. Everything else is volume.
