---
name: crm-list
description: Filtered table view of CRM records (filter by role, status, country, ICP, audience size).
type: skill
---

# /crm-list [filters]

Filter syntax: `field=value` or `field>=N`. Combine multiple filters (AND).

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm list "$@"
```

Examples:
- `/crm-list roles=advisor`
- `/crm-list pipeline.status=warm,contacted icp.startupper=yes`
- `/crm-list roles=client_lead location_country=DE icp.total>=15`
- `/crm-list audience.total_followers>=5000 --sort=icp`

Sort keys: `last_touch` (default), `icp`, `name`, `created`. Default order: descending. Use `--asc` for ascending.
