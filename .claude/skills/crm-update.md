---
name: crm-update
description: Update fields in CRM record (status, next-action, ICP scores, etc). Optionally append note to §11 and resync strategy hooks.
type: skill
---

# /crm-update <slug> --set field=value [...]

Update any frontmatter field. Convenience aliases: `status` → `pipeline.status`, `next-action` → `pipeline.next_action`, `next-action-date`, `owner`. If `--note` given — appends §11 entry + bumps last_touch_date. Use `--resync-hooks` to re-prefill §7-§8 from strategy-hooks.yaml.

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm update "$@"
```

Examples:
- `/crm-update ivan-ivanov --set status=proposal --set next-action="отправить v2" --set next-action-date=2026-05-02 --note="acked, просит pricing tweak"`
- `/crm-update ivan-ivanov --set icp.azart=4 --set icp.stable=5 --set icp.adequate=5 --set icp.upward=4`
- `/crm-update ivan-ivanov --resync-hooks`
