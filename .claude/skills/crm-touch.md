---
name: crm-touch
description: Quick log of an interaction — append §11 history entry + bump last_touch_date.
type: skill
---

# /crm-touch <slug> "<note>"

Most-frequent CRM use-case. Append entry to §11 (newest top), update `pipeline.last_touch_date = today`. No status change (use /crm-update for that).

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm touch "$@"
```

Example: `/crm-touch ivan-ivanov "ответил в Telegram по proposal — нужен tweak по pricing"`
