---
title: .claude/skills/ — Symlink Convention (v3)
type: readme
updated: 2026-04-23
---

# `.claude/skills/` — Symlink Convention

This directory hosts Claude Code skill entrypoints. In the v3 swarm wiki
architecture, active skills' canonical content lives under
`swarm/wiki/skills/active/<slug>.md` per Layer 8 (D1). The files here
are **symlinks** (for v3-born skills) pointing back to that canonical
location.

The 5 in-scope D8-parameterised skills (`/ingest`, `/ask`, `/lint`,
`/consolidate`, `/build-graph`) and the 3 documented exclusions
(`/compile`, `/search-kb`, `/sweep-notion-bank`) plus the legacy plan-day
/ close-day / focus skills remain regular files in this directory —
they are not promoted via the candidate→learning→active pipeline. Only
**new** v3-born skills go through the D9 promotion + symlink path.

## Canonical symlink rule

```
.claude/skills/<slug>.md  →  ../../swarm/wiki/skills/active/<slug>.md
```

**Relative path** (not absolute):

1. Roy-replication discipline (master synthesis §5.8.3): no hard-coded
   `/home/ruslan/*` paths.
2. Repo portability: relative target resolves correctly regardless of
   absolute repo root.

`<slug>` matches the `skill_slug` field per D2 §2.4 Layer 8 — one
canonical naming.

## Filename normalisation

The `skill_slug` MUST satisfy:

- Regex `^[a-z0-9-]{1,60}$` — body half of D2 §2.2 `id` regex
  (`^[a-z]+-[a-z0-9-]{1,60}$` where `[a-z]+-` is the type-prefix
  `skill-`).
- Unique across `.claude/skills/` (no collision with v2 names).
- Match the basename of `swarm/wiki/skills/active/<slug>.md` exactly.

Slug derivation:

- Single-word: lowercase as-is (`focus` → `focus`).
- Multi-word: hyphen-separated lowercase (`Build Graph` → `build-graph`).
- No spaces, underscores, uppercase, or extension inside the slug.

## Symlink creation hook (α-3 `learning → validated` transition)

Triggered by D11 activation predicate (golden-set ≥3 + ≥10 uses + ✓/✗
≥3:1). Brigadier executes:

```bash
# Pre-flight
test -f swarm/wiki/skills/active/<slug>.md  || exit "no canonical"
test ! -e .claude/skills/<slug>.md          || exit "name collision; see Conflict handling"

# Create symlink (atomic)
ln -s ../../swarm/wiki/skills/active/<slug>.md .claude/skills/<slug>.md

# Verify
readlink .claude/skills/<slug>.md
test -f .claude/skills/<slug>.md  || exit "broken symlink"
```

Part of α-3 `active → validated` mover (D5 §5.4). Committed in the same
commit as the file move `learning/<slug>/manifest.md` → `active/<slug>.md`.

## Symlink removal hook (α-3 `validated → tombstoned` transition)

```bash
test -L .claude/skills/<slug>.md          || exit "not a symlink (or absent)"
rm .claude/skills/<slug>.md
mv swarm/wiki/skills/active/<slug>.md \
   swarm/wiki/_archive/skills/<slug>.md
```

Skill content file is **not deleted** — only archived. Symlink IS
deleted (Claude Code registers skills via `.claude/skills/`).

Per critic-gate1 S2 of the wiki-v3 spec — α-3 has only 4 states
(proposed/active/validated/tombstoned). No separate `retired` removal
path; graceful supersession routes through tombstone with `supersedes:`
edge from the successor (D3 §3.2.7).

## Conflict handling — v2 skill collides with v3 promotion

When a v3 skill candidate's slug collides with a v2 file:

1. **Detect.** `test -e .claude/skills/<slug>.md` → collision.
2. **Preserve v2.** `mv .claude/skills/<slug>.md .claude/skills/<slug>_v2.md`.
   `_v2` suffix marks deprecated v2 skill retained for audit. `/lint`
   flags `_v2`-suffixed files as deprecated (informational only).
3. **Create v3 symlink.** Per §Symlink creation hook above.
4. **Record migration in frontmatter** of `swarm/wiki/skills/active/<slug>.md`:

   ```yaml
   migrated_from: .claude/skills/<slug>_v2.md
   migration_date: <YYYY-MM-DD>
   migration_note: <one-line summary of v2→v3 differences>
   ```

The 5 in-scope D8 skills (`/ingest`, `/ask`, `/lint`, `/consolidate`,
`/build-graph`) are NOT promoted via candidate→learning→active pipeline
— they are v2 skills parameterised in place per D8 (remain regular
files, not symlinks). Only **new** v3-born skills go through D9
promotion.

## `/lint` broken-symlink detection

`/lint` (per D8 check #11) walks `.claude/skills/`:

```
For each .md in .claude/skills/:
  if is_symlink:
    target := readlink
    if not file_exists(target):
      EMIT "broken symlink: .claude/skills/<slug>.md → <target>"
    if not target.startswith("../../swarm/wiki/skills/active/"):
      EMIT "symlink target outside active/"
    if not target.endswith("/<basename>"):
      EMIT "symlink basename mismatch"
```

Catches: (a) canonical removed without symlink removal; (b) symlink to
`learning/` or `_archive/`; (c) canonical renamed without symlink update.

## Worked example — `query-pricing-models`

1. **proposed** (α-3). Compound-step writes
   `swarm/wiki/skills/candidates/query-pricing-models/manifest.md`.
   No symlink yet.
2. **active** (α-3 learning). Brigadier moves manifest to
   `swarm/wiki/skills/learning/query-pricing-models/manifest.md`,
   creates `golden-set.jsonl`. Usage logged to
   `swarm/wiki/skills/usage/query-pricing-models.jsonl`. No symlink yet.
3. **validated** (α-3). D11 predicate satisfied. Brigadier:
   - `mv swarm/wiki/skills/learning/query-pricing-models/manifest.md \
        swarm/wiki/skills/active/query-pricing-models.md`
   - Pre-flight (no v2 collision).
   - `ln -s ../../swarm/wiki/skills/active/query-pricing-models.md \
        .claude/skills/query-pricing-models.md`
   - Update `swarm/wiki/log.md`. Single commit.
4. **tombstoned** (α-3). Ratio drops <1:1. Brigadier:
   - `rm .claude/skills/query-pricing-models.md`
   - `mv swarm/wiki/skills/active/query-pricing-models.md \
        swarm/wiki/_archive/skills/query-pricing-models.md`
   - Records `tombstoned_by:` in archived frontmatter.
   - Updates `swarm/wiki/log.md`.

## Phase A initial state

**No symlinks exist yet** in `.claude/skills/` as of Шаг 2.2.4 close.
The first symlink is created lazily on the first α-3
`learning → validated` promotion. The README above is the contract;
symlinks are an artefact of operating the swarm, not of bootstrap.
