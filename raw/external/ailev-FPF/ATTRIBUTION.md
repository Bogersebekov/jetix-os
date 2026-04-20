---
type: external-source-attribution
vendored: 2026-04-20
source: https://github.com/ailev/FPF
commit-source: main branch HEAD at 2026-04-20
author: Anatoly Levenchuk (with AI-agents assistance)
version: March 2026 (per FPF-Spec.md header)
usage-scope: internal Jetix reference only (Phase 1+)
---

# ailev/FPF — External Source Attribution

## Source

**Repository:** https://github.com/ailev/FPF
**Author:** Анатолий Левенчук (Anatoly Levenchuk)
**GitHub handle:** @ailev
**Title:** First Principles Framework (FPF) — Core Conceptual Specification
**Version:** March 2026 (per FPF-Spec.md header)
**Status (author's own):** "Normative kernel, 'eternal alpha'"

## Files vendored (2026-04-20)

- `FPF-Spec.md` — 62,202 lines, 5.7 MB — core specification (Parts A-K)
- `Readme.md` — 384 lines — entry routes + quick-start

## License status

**NO explicit license file in repository** (as of 2026-04-20 inspection).

By default (GitHub standard), absence of license = "all rights reserved" —
code can be viewed but reuse permissions are not automatically granted.

**However, the repository explicitly requests citation format:**

> "Levenchuk, Anatoly. First Principles Framework (FPF).
> GitHub repository: https://github.com/ailev/FPF"

This citation request, combined с repository being public, suggests author's
implicit permission for **reference + internal adaptation** (common pattern
for academic/research frameworks).

## Permitted use (conservative interpretation)

- ✅ **Internal reference** — reading, quoting с citation
- ✅ **Adaptation** для internal Jetix documentation — create derivative
  works для internal use (Phase 1+ internal-only aligns с our OT5 decision
  to keep Jetix FPF internal anyway)
- ✅ **Citation in derivative works** — following author's requested format
- ✅ **Inspiration + pattern inspiration** — drawing concepts, adapting
  them to Jetix-specific context
- ❌ **Public redistribution** of modified copy — requires explicit permission
- ❌ **Commercial use of unmodified content** — uncertain; ask author if scope grows

## Citation in Jetix documents

Every Jetix document that draws substantially from FPF MUST cite:

```markdown
This work draws from First Principles Framework (FPF) by Anatoly Levenchuk
(https://github.com/ailev/FPF) — March 2026 version. Adapted для Jetix OS
internal use с acknowledgment of author's conceptual foundation.
```

## Relationship к Jetix FPF

Jetix internal FPF document (D6 JETIX-FPF.md) is a **Jetix-specific adaptation**
of the broader Levenchuk FPF methodology. Key differences:

- **Scope:** Jetix focuses on AI-native DACH business operations;
  ailev/FPF covers general engineering/research/AI teams
- **Phase 1 subset:** Jetix selects pattern subset applicable к solo founder
  + 11 AI agents; ailev/FPF is comprehensive
- **Context adaptation:** Jetix examples are Mittelstand consulting,
  Portfolio of Directions, etc.; ailev/FPF is domain-agnostic

## If author objects

If Anatoly Levenchuk objects к this vendored copy:
1. Remove from `raw/external/ailev-FPF/`
2. Retain derivative Jetix FPF document (clean-room rewrite if needed)
3. Replace с external link reference only
4. Document the incident в `decisions/incidents/`

## Monitoring

- **Quarterly check** для upstream updates (new commits, new patterns)
- **Update vendored copy** when significant changes merged upstream
- **Re-validate citation** format annually

## Review trigger

- If Jetix ever goes public с FPF-derivative content — revisit license question
  formally с legal counsel
- If Левенчук publishes formal license — update this attribution
