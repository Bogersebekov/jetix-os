---
name: crm-show
description: Pretty-print full CRM record (frontmatter summary + 14 body sections).
type: skill
---

# /crm-show <slug>

Show person/org record by slug. Outputs frontmatter summary header + full markdown body.

```bash
cd ~/jetix-os
python3 -m crm._scripts.crm show "$@"
```

Example: `/crm-show ivan-ivanov`
