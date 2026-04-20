---
wave: B
target: shsm-5-primitives-deep-dive
quality: ontological precision; full mereology + state-machine semantics
expected-length: 5000-7000 words
output-file: raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md
---

# Research R-B — ШСМ 5 примитивов: deep ontological dive

## Цель

Максимально глубокое research пяти примитивов Системного мышления
Левенчука: роль / альфа / граф создания / стратегирование / мышление
письмом. Каждый примитив — full ontological treatment с definitions,
distinctions от near-concepts, examples, anti-patterns, applications.

=== PROMPT START ===

You are conducting an **ontologically rigorous deep-dive** into the
**5 primitives of Системное мышление (Systems Thinking)** as taught by
**Анатолий Левенчук** in his ШСМ (Школа системного менеджмента) framework.

These 5 primitives are the foundational ontological commitments that
distinguish Levenchuk's framework from other systems thinking approaches.
I need rigorous understanding to apply them correctly in a software-as-
business context (Jetix OS — AI-native business operating system).

## Background context

Jetix OS uses Levenchuk's 5 primitives as the foundational philosophical
framework (we call it "FPF — Foundational Philosophy Framework", a Jetix-
specific full adaptation of Levenchuk's ontology).

**Critical concern:** Levenchuk himself warns that **violation by misuse**
(decorating software practices with ШСМ names while keeping software
semantics) is more damaging than **violation by omission** (not using
ШСМ names at all).

Therefore I need ontological precision — what each primitive **is** AND
what it is **NOT**.

## The 5 primitives (research each comprehensively)

### Primitive 1 — РОЛЬ (Role)

1.1. **Definition** — give the precise Levenchuk definition. Cite source
(book chapter, course module).

1.2. **Distinction from neighboring concepts:**
- Role ≠ Position (job title)
- Role ≠ Person (executor)
- Role ≠ Software class
- Role ≠ Holacracy "role" (compare and contrast)
- Role ≠ Sociocracy 3.0 role pattern
- Role ≠ RACI assignment
For each, explicit description of what is shared and what differs.

1.3. **Roles vs Executors** — Levenchuk's strict separation:
- Roles are abstract function contracts
- Executors are concrete entities (humans, teams, AI agents) that fill roles
- One executor can fill multiple roles
- One role can be filled by multiple executors (in parallel or in sequence)
- "Multi-roled executor" critique (founder syndrome)
- Dynamic role assignment forbidden (and why)

1.4. **Role-as-method** — Levenchuk's method-level treatment:
- Roles have methods (ways of accomplishing their function)
- Methods evolve; roles are more stable
- How role-as-method differs from job description

1.5. **Role discovery vs role design** — Levenchuk's stance:
- Are roles "discovered" in problem space (essentialist) or
  "designed" by architect (constructivist)?
- What's his epistemological position?

1.6. **Onto-correctness checks** — how to verify a defined role is
ontologically correct under ШСМ:
- Naming conventions
- Required components
- Common errors / anti-patterns

### Primitive 2 — АЛЬФА (Alpha)

2.1. **Definition** — Levenchuk's precise definition + relation to Essence
Kernel (SEMAT) origin.

2.2. **Critical distinction**: Alpha vs Work Product vs Entity
- Alpha — has lifecycle states, "things to care about"
- Work Product — produced/consumed artifact, no lifecycle states
- Entity — object without state machine
- Examples of each
- Common confusion patterns (e.g., calling Invoice an alpha vs work product)

2.3. **State machines on alphas** — Levenchuk requirements:
- Past-participle naming convention (why)
- States as completed checklists (semantics)
- State transitions vs status updates
- Multiple state-machines per alpha (allowed?)

2.4. **Past-participle convention** — full justification:
- Why "qualified" not "qualifying"
- Why "activated" not "active"
- Why "in-negotiation" not "negotiating"
- Why "started" not "in-progress"
- Why "delivered" not "delivery"
- Semantic precision argument
- Machine-readability for AI agents

2.5. **Standard alphas в ШСМ Essence-derived practice:**
- Customer (Заказчик)
- Project / Endeavour
- Stakeholders
- Solution
- Way of Working
- ... (full Essence Kernel set + Levenchuk extensions)

2.6. **Alpha discovery** — how to identify what should be an alpha:
- Heuristics
- Common false-positives (things that look like alphas but aren't)
- Common false-negatives (alphas missed)

### Primitive 3 — ГРАФ СОЗДАНИЯ (Creation Graph)

3.1. **Definition** — Levenchuk's precise definition.

3.2. **Critical distinction:** Creation graph ≠ workflow ≠ dependency tree
≠ org chart ≠ value stream map.

3.3. **Mereological structure** — how creation graph is **mereological**:
- Systems-as-parts hierarchy (target system / creation system / supersystem)
- Recursive property (creation systems are themselves systems)
- Part-of vs creates relations
- Why bipartite "supplier-consumer chart" is NOT a creation graph

3.4. **3-level mereological structure** (full Levenchuk treatment):
- Level 1: Target systems (what is created)
- Level 2: Creation systems (what creates)
- Level 3: Supersystems (the wholes that contain/use creations)
- Examples
- Edge types (part-of, creates, operates-in, methodologically-uses,
  constrained-by)

3.5. **Creation graph discovery method** — how Levenchuk teaches deriving
creation graph for a specific endeavour:
- Starting points
- Decomposition rules
- Verification heuristics

### Primitive 4 — СТРАТЕГИРОВАНИЕ (Strategizing)

4.1. **Definition** — Levenchuk's definition. Critical: what makes
strategizing **strategizing** vs planning vs scheduling?

4.2. **Strategizing as event vs ceremony:**
- Why Levenchuk insists strategizing is trigger-driven, not scheduled
- What constitutes a "trigger" for strategizing
- Critique of "monthly strategic planning meetings"
- Past-participle naming for strategy artifacts

4.3. **Strategizing as invent (vs adapt vs 1:1):**
- Levenchuk's three operational modes: invent / adapt / 1:1
- Why strategizing is in "invent" category
- Implications for AI agents — "agents do not strategize" principle
- AI as strategizing-support (analysis, options enumeration) vs
  strategizing-itself

4.4. **Strategizing in solo founder context:**
- Levenchuk's view on solo strategizing
- "Founder mode" as operational reality
- Multi-role founder critique

4.5. **Strategy artifacts** — what gets written down:
- Strategy as decision record
- Trigger-slug naming convention (e.g., `strategizing/<trigger-slug>-YYYY-MM-DD.md`)
- Required components

### Primitive 5 — МЫШЛЕНИЕ ПИСЬМОМ (Writing-as-Thinking)

5.1. **Definition** — Levenchuk's full conceptualization.

5.2. **Critical distinction:** Writing-as-thinking ≠ documentation generation
≠ Confluence pages ≠ note-taking ≠ stenography.

5.3. **Why writing IS thinking** (epistemological argument):
- Externalization of cognitive load
- Thinking vs cognition distinction
- Writing as exocortex for working memory expansion
- Quality criteria for writing-as-thinking artifacts

5.4. **Practitioner techniques** — how Levenchuk teaches writing-as-thinking:
- Daily writing practice
- Meta-cognitive prompts
- Exocortex maintenance (linked notes, atomic concepts)
- Tools recommended (Obsidian / Roam / Notion / etc.)

5.5. **Writing-as-thinking + AI agents:**
- AI as writing-thinking partner
- Limitations (AI lacks "cognitive externalization need")
- How AI agents can support but not replace human writing-as-thinking

### Section 6 — Inter-relations between primitives

How do the 5 primitives connect?
- Roles **operate on** alphas (managing state transitions)
- Roles **occupy positions** in creation graphs
- Strategizing **decides** which alphas to track + which roles to activate
- Writing-as-thinking **externalizes** strategizing process
- Creation graphs **constrain** which roles can affect which alphas

Provide a systems diagram (text-based) showing inter-relations.

### Section 7 — "What ШСМ is NOT" — full protection list

Levenchuk's "защита от software-language colonization" — full list of
common errors when applying ШСМ in software/business contexts:

7.1. ШСМ роль ≠ software class или GitHub team — full justification
7.2. ШСМ alpha ≠ database table или Kanban column — full justification
7.3. ШСМ creation graph ≠ workflow diagram или dependency tree — full
7.4. ШСМ strategizing ≠ planning meeting или OKR session — full
7.5. ШСМ thinking-by-writing ≠ documentation generation или Confluence pages — full

For each, give:
- Surface similarity (why confusion arises)
- Critical difference (what makes ШСМ version distinct)
- Example of correct ШСМ usage vs incorrect "decorated software" usage
- Damage caused by confusion

### Section 8 — Operational application checklist

For each primitive, provide:
- "Quick start" minimum requirements to apply correctly
- Common mistakes to avoid (top 3)
- Verification heuristics ("am I doing this correctly?")
- Source materials for deeper learning

## Output structure

Format as structured Markdown:
1. **Executive summary** (300-500 words) covering all 5 primitives at high level
2. **Sections 1-5** — one per primitive, each ~800-1500 words
3. **Section 6** — inter-relations diagram + explanation
4. **Section 7** — "What ШСМ is NOT" full list
5. **Section 8** — operational checklists
6. **Bibliography** — every source cited
7. **Glossary** — Russian + English equivalents

## Quality requirements

- **Primary sources cited везде** (chapter-level references к книгам Левенчука)
- **Russian terms primary**, English secondary
- **Examples concrete и practical** (not abstract)
- **Anti-patterns explicit** (what NOT to do)
- **Internal consistency** — definitions across primitives align

## Length target

5000-7000 words. This is a foundational reference that should leave no
ambiguity about each primitive.

=== PROMPT END ===
