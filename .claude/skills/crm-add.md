---
name: crm-add
description: Create new person/org entry in CRM (crm/people/<slug>.md). Auto-prefills §7-§8 from strategy hooks.
type: skill
---

# /crm-add

Add new person to CRM. Generates slug from name, applies template, prefills §7-§8 from strategy-hooks.yaml, validates frontmatter, rebuilds index.

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm add "$@"
```

Examples:
- `/crm-add "Иван Иванов" --role=advisor --country=DE --channel=indiehackers --context="ответил на IH post"`
- `/crm-add "Acme Corp" --org --role=client_lead --country=DE`

Required prompts (if not given as flags): role, country, source channel, context.
