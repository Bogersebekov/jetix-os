---
name: crm-stuck
description: List CRM contacts in active pipeline statuses with no touch >14 days. For weekly review.
type: skill
---

# /crm-stuck

Statuses checked: warm, contacted, discovery_call, proposal, negotiation. Threshold: 14 days (config in `crm/_schema/statuses.yaml#stuck`).

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm stuck
```
