# CRM — Multi-Purpose Contact Network

> Filesystem-as-truth, grep-friendly, markdown+frontmatter CRM for tracking
> people / orgs across the entire Jetix-life-and-business network.
> NOT just sales — clients, partners, investors, mentors, advisors, friends,
> co-founders, hires, "interesting people", facilitators, vendors. Everyone.

---

## 1. Что это

`crm/` — flat-file knowledge base человеческой сети. Each contact = one
markdown file with structured YAML frontmatter + 14 narrative sections.
Лежит рядом с `wiki/` (общая company-as-code substrate). Notion = view-only
mirror; **filesystem = source of truth**.

**Покрытие:** до 10K records без миграции. До тех пор bash/grep + python
scripts достаточно. Phase-2 (DuckDB index) по необходимости — pre-wired.

**Дизайн принципы:**
- Single source of truth = filesystem. Notion = optional view, not authoritative.
- Append-only history (§11). Edits to status/next-action только через `/crm-update`.
- Идемпотентные patches: rerunning `/crm-rebuild-index` daily safe.
- Grep-first: `grep -rl "discovery_call" crm/people/` works without parsing.
- Voice-pipeline integration: DRAFT-only, never auto-merge into prod records.

## 2. Quickstart

```bash
# Add a person
python3 -m crm._scripts.crm add "Anna Schmidt" --role=advisor,interesting \
    --niche="EU AI VC" --country=DE --channel=referral \
    --context="introduced by Klaus 24.04"

# Show entry
python3 -m crm._scripts.crm show anna-schmidt

# Append touch (updates §11 + last_touch_date)
python3 -m crm._scripts.crm touch anna-schmidt "discovery call 50min, advisor role discussed"

# Update fields
python3 -m crm._scripts.crm update anna-schmidt --set status=discovery_call \
    --set next-action="send proposal" --set next-action-date=2026-05-05

# List filtered
python3 -m crm._scripts.crm list status=discovery_call --sort=last_touch
python3 -m crm._scripts.crm list role=advisor location_country=DE icp.total>=15

# Search full-text
python3 -m crm._scripts.crm search "DACH"

# Dashboard / health
python3 -m crm._scripts.crm dash
python3 -m crm._scripts.crm stuck
python3 -m crm._scripts.crm weekly --save

# After bulk edits
python3 -m crm._scripts.crm rebuild-index
```

Or use Claude Code skills — same effect, terser invocation:

```
/crm-add Anna Schmidt --role=advisor --country=DE
/crm-show anna-schmidt
/crm-touch anna-schmidt "discovery call"
/crm-update anna-schmidt --set status=warm
/crm-list status=warm
/crm-search DACH
/crm-dash
/crm-stuck
/crm-weekly
/crm-rebuild-index
```

## 3. Schema (frontmatter)

Authoritative spec: `crm/_schema/frontmatter.yaml`. JSON-Schema-style.

**Required fields** (validation will reject otherwise):
- `name` — full name (any script)
- `slug` — kebab-case, == filename without `.md`
- `type` — `person` | `org`
- `roles` — list, ≥1 from `_schema/roles.yaml`
- `created`, `updated` — ISO date `YYYY-MM-DD`

**Optional buckets:**
- Identity: `aliases`
- Background: `niche`, `occupation`, `income_bucket`, `location_country` (ISO-2),
  `location_city`, `languages`, `age`
- Contact: `contact.{email,telegram,linkedin,twitter,instagram,youtube,tiktok,
  website,phone,other_links}`
- Audience: `audience.{total_followers,breakdown,audience_type,audience_quality,
  icp_overlap_pct,notes}`
- Tools: `tools.{uses,owns,platforms_active_on}`
- Origin: `origin.{source_channel,introduced_by,first_contact_date,context}`
- ICP fit (D22): `icp.{startupper,azart,stable,adequate,upward,total,scored_at,scored_by}`
- Pipeline: `pipeline.{status,last_touch_date,next_action,next_action_date,owner}`
- Value: `value.{to_jetix,to_jetix_why,to_them,relationship_strength}`
- Meta: `tags`, `created`, `updated`
- Org-only: `org_type`, `founded`, `employees`, `revenue_estimate`, `key_people`

**Auto-fix:** `icp.total = sum(azart+stable+adequate+upward)` recomputed on save.
`updated >= created` enforced.

**Roles** (24, in 6 groups — see `_schema/roles.yaml`):
- sales: `client_lead`, `client_active`, `client_past`, `client_lost`
- capital: `investor_prospect`, `investor_active`
- partnership: `partner_prospect`, `partner_active`, `partner_past`
- advisory: `mentor`, `advisor`, `facilitator`, `consultant`
- team: `cofounder_prospect`, `hire_prospect`, `hire_active`, `hire_past`
- network: `friend`, `interesting`, `vendor`, `competitor`

**Statuses** (13, see `_schema/statuses.yaml`):
- voice ingress: `draft_from_voice` (DRAFT-only, awaiting human ack)
- sales pipeline: `cold` → `warm` → `contacted` → `discovery_call` → `proposal`
  → `negotiation` → `closed_won` / `closed_lost`
- non-sales: `paused`, `active`, `past`

**Stuck definition:** `pipeline.status` ∈ {warm, contacted, discovery_call,
proposal, negotiation} AND `last_touch_date` > 14 days ago.

## 4. Skills cheatsheet

| Skill | What it does |
|-------|--------------|
| `/crm-add NAME [--role=R] [--country=DE] [--channel=...]` | Create new person/org from template; auto-prefill §7 §8 via strategy hooks; append log |
| `/crm-show SLUG` | Print full file with parsed frontmatter summary |
| `/crm-list [filters] [--sort=last_touch\|icp\|name] [--asc] [--no-orgs]` | Filtered table view |
| `/crm-search QUERY` | Full-text grep across name/aliases/body |
| `/crm-touch SLUG NOTE` | Append §11 entry, bump `last_touch_date` |
| `/crm-update SLUG --set field=val [--note=...] [--resync-hooks]` | Update frontmatter fields with alias map (`status` → `pipeline.status`) |
| `/crm-rebuild-index` | Regenerate `crm/index.md` (idempotent) |
| `/crm-dash` | Dashboard: counts by role / status / stuck / recent |
| `/crm-stuck` | List stuck contacts (active status, >14d no touch) |
| `/crm-weekly [--save]` | Weekly review report; `--save` writes to `crm/views/weekly-YYYY-MM-DD.md` |

All skills delegate to `python3 -m crm._scripts.crm <subcommand>`.

## 5. Conventions

- **Filenames:** `crm/people/<slug>.md`, `crm/orgs/<slug>.md`, kebab-case, ASCII.
- **Slugs:** == filename. Pattern `^[a-z0-9]+(-[a-z0-9]+)*$`. No leading underscore.
- **Dates:** ISO `YYYY-MM-DD` everywhere.
- **Append-only history:** §11 entries newest-on-top, never edit old.
- **Frontmatter required** in every contact file.
- **Edges** (cross-contact relationships) stored in `wiki/graph/edges.jsonl`,
  not duplicated in frontmatter (single source).
- **Russian for content / EN for code** (per global CLAUDE.md).

See `_meta/conventions.md` (CRM Conventions section) for full rules.

## 6. Strategy hooks (§7 §8 auto-fill)

`crm/_schema/strategy-hooks.yaml` declares 6 OFFERS + 6 ASKS that we can extend
to network contacts. On `/crm-add` / `/crm-update --resync-hooks`, the script
filters hooks against the contact's frontmatter (roles / tags / icp / location /
audience) and prefills §7 (что мы предлагаем) and §8 (что мы получаем).

**Current OFFERS** (active):
- L6 Community access (Mittelstand AI Alliance founding cohort)
- Sales Methodology Wiki — early access
- USB-C positioning insight
- Jetix Network — early cohort
- AI Pilot engagement (paid, €5-15K, 4-6 weeks)

**Current OFFERS** (draft, opt-in via `--include-draft`):
- L7 Producer Services collab (H4 Podcast / H5 Coaches hypotheses)

**Current ASKS:**
- DACH Mittelstand intros (P1A leads)
- Advisor role (cooperation-not-paid, RU+EN, weekly)
- Case-study source (paying clients permission)
- Methodology v1 feedback (practitioner critique)
- Investor intros (Phase 2, DACH/EU AI VC)
- Audience co-marketing (newsletter swap, podcast guest)

**Refs:** Hooks reference live strategy docs (`directions/_active/`, `decisions/`,
`swarm/wiki/cycles/`). Update `strategy-hooks.yaml` as strategy evolves.

The auto-suggested bullets in §7/§8 carry `[auto-suggested, edit me]` markers —
**always review/edit before outreach**, hooks are starting points, not final copy.

## 7. Voice pipeline integration

`tools/run_pipeline.sh` step 3 (`extract.py`) emits items with `target: crm` for
voice mentions of people. After extract:

1. `crm/_scripts/voice_router.py` reads items → 3 intents:
   - `add` → creates `crm/people/<slug>-DRAFT.md` with `pipeline.status=draft_from_voice`
   - `touch` → if exact slug match: append §11 entry + bump `last_touch_date`
   - `update` → if exact match: update specified fields

2. **DRAFT-only invariant:** voice-routed adds NEVER overwrite existing prod
   records. New entries always get `-DRAFT` suffix. Ambiguous touches (multiple
   fuzzy matches) reported in summary, not auto-applied.

3. Ruslan reviews drafts in `~/review-latest.md` → manually promotes via
   `/crm-update <slug>-DRAFT --set status=warm` + rename file (drop `-DRAFT`)
   OR rejects via `rm crm/people/<slug>-DRAFT.md`.

**Why DRAFT-only:** Claude transcript inference quality varies. Auto-merging
into prod CRM would corrupt high-trust records. Human ack is mandatory.

## 8. Backups

CRM lives in git (`crm/` tracked). Recovery:
```bash
git log --oneline -- crm/people/<slug>.md   # see history
git show HEAD~3:crm/people/<slug>.md        # recover prior version
```

For bulk operations (mass renames / migrations):
```bash
git stash                  # save WIP
# do migration
python3 -m crm._scripts.crm validate   # check schema
python3 -m crm._scripts.crm rebuild-index
git diff crm/                # review
git commit -m "[crm] migration: ..."
git stash pop
```

No external backups beyond git remote (`origin`). Push regularly.

## 9. Privacy

- **PII discipline:** real personal data lives in `crm/`, never copied to
  public-facing wiki/, drafts/, or test fixtures.
- **Test fixtures** (`_tests/fixtures/`) use anonymized samples
  (`sample-person-anton`, `sample-person-vladislav`, `sample-org-acme`).
- **Reference template** (`example-person.md`) uses `example.invalid` domain
  + fictional name + paused status.
- **Voice memos / transcripts** in `raw/` may contain PII — never share raw/
  externally; only sanitized excerpts in published artefacts.
- **Recordings / transcripts** referenced from §14 should be in `crm/recordings/`
  + `crm/transcripts/` (gitignored if needed; or git-tracked if Ruslan accepts
  cost). Currently both dirs tracked but empty.
- `~/.ssh/`, `.env`, `private/` — never touched by CRM scripts.

## 10. Phase 2 roadmap

Triggered by scale OR feature requests, not premature optimization.

- **DuckDB / SQLite index** when 5K+ contacts (estimated when 14d-stuck-list
  recompute >2s). Schema: `frontmatter.yaml` already JSON-Schema-compatible →
  trivial mapping.
- **Notion two-way sync** if collaboration with non-tech advisors needed.
  Direction: filesystem → Notion (push), never Notion → filesystem.
- **Edges UI** (graph viz) — current `wiki/graph/edges.jsonl` already supports;
  needs a viewer (gephi export script or web frontend).
- **AI auto-enrichment** — fetch LinkedIn / Twitter bio for new entries via
  external API (currently disabled per "no direct API keys" feedback).
- **Pipeline reports** — automatic weekly digest emails / Slack ping.
- **Voice DRAFT auto-promote** — only after 3-month accuracy audit (drafts vs.
  Ruslan's manual edits) shows ≥90% precision.
- **Cross-CRM merge** — if Jetix takes on second co-founder with own contact
  base; per-owner namespacing in `crm/<owner>/people/`.

---

**Authoritative design records:** `swarm/wiki/designs/T-crm-build-2026-04-26/`
(when materialized; for now spec lives in `/tmp/crm-deep-prompt.md` + this README).

**Related:**
- `crm/PLAN.md` — embedded copy of the original Notion build plan
- `crm/_meta/` — (none yet; expand as needed)
- `wiki/graph/edge-types.md` — 8 CRM edge types (co-founder-with, founder-of, ...)
- `_meta/conventions.md` — CRM Conventions section
