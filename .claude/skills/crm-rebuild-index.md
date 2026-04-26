---
name: crm-rebuild-index
description: Regenerate crm/index.md from all crm/people/*.md + crm/orgs/*.md (idempotent).
type: skill
---

# /crm-rebuild-index

Re-generates `crm/index.md` from scratch. Idempotent (no-op if no diff). Run after manual file edits.

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm rebuild-index
```
