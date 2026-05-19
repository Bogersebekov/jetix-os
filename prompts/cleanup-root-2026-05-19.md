---
type: maintenance-prompt
date: 2026-05-19 afternoon
session: cleanup-root-2026-05-19
target_brigadier: ROY swarm (lightweight; eng × scalability primary)
estimated_duration: 5-10 min
estimated_cost: <€0.50
constitutional_posture: R6 (history preserved via git mv) + append-only (no content modification)
purpose: Move 42 _*.md/.json files из repo root в organised subdirs to declutter
language: russian + english
---

# PROMPT — Cleanup Repo Root (move 42 _* files to subdirs)

ultrathink (light)

Ты brigadier. Quick maintenance task: move 42 `_*` files из repo root в organised subdirs. Preserve git history через `git mv`. Update cross-references where needed.

═══════════════════════════════════════════════════════════
§0 MISSION
═══════════════════════════════════════════════════════════

Move files preserving history. Update relative path references. Single commit per category. Final push.

═══════════════════════════════════════════════════════════
§1 TARGET DIRECTORY STRUCTURE
═══════════════════════════════════════════════════════════

Create (if not exists):
- `daily-logs/` — Daily Logs + Plan-of-Day
- `prompts/explanations/` — _EXPLAIN files
- `_archive/handoffs/` — _HANDOFF files
- `_archive/launchers/` — _LAUNCH files (after use)
- `_archive/meta/` — _MASTER-PICTURE + _META-* files
- `_archive/toggl/` — _toggl-entries-*.json
- `_archive/analytics/` — _DEEP-WORK-ANALYTICS-*
- `_archive/inventories/` — _FPF-REAL-EXAMPLES-INVENTORY-*
- `_archive/calls/` — _DMITRY-CALL-PREP-* / _VIDEO-RECORDING-*

═══════════════════════════════════════════════════════════
§2 FILE MAPPING
═══════════════════════════════════════════════════════════

### Daily logs / planning → `daily-logs/`:
- `_DAILY-LOG-*.md` (3 files: 17.05 / 18.05 / 19.05)
- `_PLAN-OF-DAY-*.md` (if any)

### Explanations → `prompts/explanations/`:
- `_EXPLAIN-*.md` (~22 files)

### Handoffs → `_archive/handoffs/`:
- `_HANDOFF_*.md` (~4 files)

### Launchers → `_archive/launchers/`:
- `_LAUNCH-*.md` (~2 files)

### Meta / Master Picture → `_archive/meta/`:
- `_MASTER-PICTURE-*.md`
- `_META-*.md`

### Toggl → `_archive/toggl/`:
- `_toggl-entries-*.json` (2 files)

### Analytics → `_archive/analytics/`:
- `_DEEP-WORK-ANALYTICS-*.md`

### Inventories → `_archive/inventories/`:
- `_FPF-REAL-EXAMPLES-INVENTORY-*.md`

### Calls / people → `_archive/calls/`:
- `_DMITRY-CALL-PREP-*.md`
- `_VIDEO-RECORDING-*.md`

### KEEP в root (DO NOT MOVE):
- `CLAUDE.md`
- `README.md`
- `HOME.md`
- `MIGRATION.md`
- `CANONICAL-WALKTHROUGH-*.md`
- `JETIX-WORKING-FILE-*.md`
- `JETIX-DOCUMENT-MAP-*.md`

═══════════════════════════════════════════════════════════
§3 PHASE 1 — Create directories + git mv
═══════════════════════════════════════════════════════════

```bash
cd ~/jetix-os
mkdir -p daily-logs prompts/explanations _archive/handoffs _archive/launchers _archive/meta _archive/toggl _archive/analytics _archive/inventories _archive/calls

# Daily logs
git mv _DAILY-LOG-*.md daily-logs/ 2>/dev/null

# Explanations  
for f in _EXPLAIN-*.md; do git mv "$f" prompts/explanations/ 2>/dev/null; done

# Handoffs
for f in _HANDOFF_*.md; do git mv "$f" _archive/handoffs/ 2>/dev/null; done

# Launchers
for f in _LAUNCH-*.md; do git mv "$f" _archive/launchers/ 2>/dev/null; done

# Meta + Master Picture
for f in _MASTER-PICTURE-*.md _META-*.md; do git mv "$f" _archive/meta/ 2>/dev/null; done

# Toggl
for f in _toggl-entries-*.json; do git mv "$f" _archive/toggl/ 2>/dev/null; done

# Analytics
for f in _DEEP-WORK-ANALYTICS-*.md; do git mv "$f" _archive/analytics/ 2>/dev/null; done

# Inventories
for f in _FPF-REAL-EXAMPLES-INVENTORY-*.md; do git mv "$f" _archive/inventories/ 2>/dev/null; done

# Calls / people
for f in _DMITRY-CALL-PREP-*.md _VIDEO-RECORDING-*.md; do git mv "$f" _archive/calls/ 2>/dev/null; done
```

COMMIT 1: `[cleanup] move 42 _* files из root в organised subdirs (daily-logs/explanations/archive/...) — git mv preserves history`

═══════════════════════════════════════════════════════════
§4 PHASE 2 — Update cross-references
═══════════════════════════════════════════════════════════

Search for relative-path references к moved files в active canonical docs:

```bash
# Find references
cd ~/jetix-os
grep -rn "_DAILY-LOG-\|_EXPLAIN-\|_HANDOFF_\|_LAUNCH-\|_MASTER-PICTURE-\|_META-" \
    --include='*.md' \
    --exclude-dir=_archive \
    --exclude-dir=prompts/explanations \
    --exclude-dir=daily-logs \
    --exclude-dir=.git \
    | head -50
```

For each found reference:
- Update path к new location
- Examples:
  - `_DAILY-LOG-2026-05-19.md` → `daily-logs/_DAILY-LOG-2026-05-19.md`
  - `_EXPLAIN-foo.md` → `prompts/explanations/_EXPLAIN-foo.md`
  - `_MASTER-PICTURE-NEXT-STEPS-2026-05-18.md` → `_archive/meta/_MASTER-PICTURE-NEXT-STEPS-2026-05-18.md`

Common file types к check:
- `vision/*.md`
- `decisions/*.md`
- `reports/*.md`
- `research/*/*-SUMMARY-FOR-RUSLAN.md`
- `wiki/concepts/*.md` / `wiki/ideas/*.md`

Update via `sed` per category OR Edit tool per file.

COMMIT 2: `[cleanup] update cross-references to moved files (relative paths corrected)`

═══════════════════════════════════════════════════════════
§5 PHASE 3 — Verify + summary + push
═══════════════════════════════════════════════════════════

Verify:
```bash
ls _*.md _*.json 2>/dev/null | wc -l
# Expected: 0 or just config files
```

Create `_archive/CLEANUP-2026-05-19-README.md`:
- §1 Summary (how many files moved per category)
- §2 New directory structure overview
- §3 Cross-references updated count
- §4 Files KEPT в root (canonical docs)

COMMIT 3: `[cleanup] final summary + push origin main`

`git push origin main`

Final echo: `DONE — N files moved / M cross-refs updated / root декleaned`

═══════════════════════════════════════════════════════════
§6 HALT CONDITIONS
═══════════════════════════════════════════════════════════

- Any file unintentionally lost → halt + escalate
- `git mv` failure → halt + diagnose
- Cross-reference update breaks canonical → halt + revert specific change

═══════════════════════════════════════════════════════════
§7 DON'T
═══════════════════════════════════════════════════════════

❌ Modify content of any moved file
❌ Move CLAUDE.md / README.md / HOME.md / MIGRATION.md / CANONICAL-WALKTHROUGH-* / JETIX-WORKING-* / JETIX-DOCUMENT-MAP-*
❌ Use `mv` instead of `git mv` (history loss)
❌ Skip Phase 2 cross-reference update (broken links)

═══════════════════════════════════════════════════════════
§8 START
═══════════════════════════════════════════════════════════

ultrathink (light). Read §0. Execute Phases 1-3. Per-phase commit. Final push.

---

*Lightweight cleanup prompt 2026-05-19 afternoon. ~5-10 min. <€0.50.*
