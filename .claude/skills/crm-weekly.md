---
name: crm-weekly
description: Weekly CRM report — extends /crm-dash with new contacts detail, status changes, action items.
type: skill
---

# /crm-weekly [--save]

Combined weekly report. Without `--save` — print to terminal. With `--save` — write to `crm/views/weekly-YYYY-MM-DD.md`.

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm weekly "$@"
```

Examples:
- `/crm-weekly` (preview)
- `/crm-weekly --save` (persist for archive)
