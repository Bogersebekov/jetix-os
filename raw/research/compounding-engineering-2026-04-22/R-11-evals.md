# Jetix Agent Evals — Deep Technical Due Diligence (April 2026)

> **Prepared for:** Jetix (Berlin-based AI consultancy, 11 Claude-based agents across 6 departments)  
> **Scope:** Comprehensive technical due diligence on LLM agent evaluation — frameworks, benchmarks, LLM-as-judge methodology, production pipelines, case studies, economics, and a concrete implementation roadmap for a solo founder operating a multi-agent operational system.  
> **Research base:** Six parallel research streams totalling 5,038 lines of primary-source analysis compiled April 2026.

---

## Executive Summary

The eval landscape in 2026 is bifurcated: rigorous, production-grade evaluation is standard practice at leading AI labs and application companies, while the majority of smaller teams still operate on intuition and ad hoc testing. For Jetix — a solo-founder AI consultancy with 11 Claude-based agents — closing that gap is both achievable and urgent.

**What evals mean in 2026:** Evals have moved from academic benchmarking exercises to core engineering infrastructure. The terminology is now settled: an *eval* is a structured measurement of model or agent behavior using defined inputs, grading criteria, and pass/fail logic — distinct from unit tests (which test code correctness) and from production monitoring (which observes live behavior). The key shift since 2023 is the emergence of *trajectory evals* that assess multi-step agent behavior rather than single-turn outputs, and *LLM-as-judge* pipelines that scale quality assessment to thousands of outputs per day.

**Framework dominance:** No single framework has won. The 14 frameworks surveyed occupy distinct niches. Critically, Anthropic has no standalone eval product: the Console eval tool is a UI-only prompt tester with a 5-point grading scale, no API integration, and no agent trajectory support. Anthropic's own January 2026 engineering blog explicitly recommends third-party tools — Braintrust, LangSmith, Langfuse, and Phoenix — for production eval workflows. For a Claude-native solo founder, [Promptfoo](https://promptfoo.dev) (OSS, CLI-first, trajectory assertions) combined with [Langfuse](https://langfuse.com) (self-hostable observability) forms the minimum viable stack. Braintrust ($249/mo Pro) is the step-up if budget allows.

**Benchmark saturation is real:** A [2026 systematic study](https://arxiv.org/html/2602.16763v1) found ~49% of major benchmarks exhibit high-to-very-high saturation. HumanEval (95%+ SOTA), MMLU (92.5% GPT-5), and SWE-bench Verified (declared saturated by OpenAI in February 2026) have zero discriminative power for frontier models. For Jetix's context — sales intelligence, knowledge synthesis, document writing — the five most relevant benchmarks are GAIA, τ-bench, BrowseComp, TheAgentCompany, and AssistantBench.

**LLM-as-judge is viable but calibration is mandatory:** [Zheng et al. (arXiv:2306.05685)](https://arxiv.org/abs/2306.05685) established 85–87% human agreement for GPT-4-as-judge, but also documented 75% position bias failure rates in weaker judges and 91.3% verbosity failure in Claude-v1/GPT-3.5. Without calibration against domain expert labels, an LLM judge measures verbosity and confidence rather than quality. The calibration investment is non-negotiable.

**Top 5 Key Findings:**

- **Anthropic has no eval product.** Console evals are UI-only with no API, no trajectory support, no CI/CD. Use external tooling — Anthropic officially recommends it.
- **Promptfoo + Langfuse is the minimum viable stack** for a Claude-native solo founder with agent trajectory requirements, at $0–$50/month base cost.
- **Calibration before automation.** An uncalibrated LLM judge is worse than no judge — it creates false confidence. Minimum 20–30 human-labeled examples before trusting any automated scorer.
- **Contamination renders most public benchmarks unreliable.** GPT-4o drops 14.6 percentage points from MMLU to MMLU-CF; SWE-bench Verified was abandoned by OpenAI. Build internal golden sets against real Jetix tasks.
- **The compound-learning signal for all 11 agents should be a frozen quarterly golden set.** Velocity metrics and skill counts are gameable; error rate decay on a frozen test set is the most rigorous proxy for actual improvement.

---

## Section 1 — Definitions & Eval Types

### What Evals Are (and Are Not)

An **eval** (evaluation) in the LLM/agent context is a structured measurement of model or agent behavior: a set of defined inputs, a grading function (deterministic, model-based, or human-based), and a pass/fail or scored outcome. The term traces to [OpenAI's evals repository](https://github.com/openai/evals) (created January 2023, now 17.5k GitHub stars), which popularized the discipline of systematic, reproducible LLM testing using shared benchmark registries.

Evals differ from related concepts:

| Concept | Purpose | Who writes it | When it runs |
|---|---|---|---|
| **Unit test** | Verify code logic is correct | Developer | Every commit |
| **Integration test** | Verify system components work together | Developer/QA | Pre-deploy |
| **Eval** | Measure model/agent quality on a task | ML engineer + domain expert | Pre-deploy + periodic |
| **A/B test** | Measure user behavior impact of a change | Product/ML | Post-deploy with traffic |
| **Production monitoring** | Observe live behavior at scale | MLOps | Continuously |

The [Anthropic engineering blog (Jan 2026)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) defines the core vocabulary:

> "**Task** (problem/test case): Single test with defined inputs and success criteria. **Trial**: Each attempt at a task (multiple for consistency due to model variability). **Grader**: Logic scoring performance. **Transcript** (trace/trajectory): Complete record of trial (e.g., Anthropic API full messages array). **Outcome**: Final environment state. **Evaluation harness**: Infrastructure for end-to-end evals."

The distinction between monitoring and evals is important: monitoring observes live production traffic; evals run against controlled test sets. Both are necessary; neither substitutes for the other.

### Full Eval Taxonomy

#### 1. Deterministic / Code-Based Evals

**What they are:** Rule-based graders using string matching, regex, JSON schema validation, code execution, or test suite pass rates. No model inference required for grading.

**Trade-offs:** Near-zero cost, perfectly reproducible, zero hallucination risk. Break down when outputs are open-ended (free text, long-form synthesis) or when "correct" cannot be reduced to a string.

**Where they break down:** Any task where multiple valid formulations exist (Q&A, summaries, document drafts). Over-reliance creates Goodhart's Law problems: agents learn to satisfy the pattern checker without doing the underlying task well.

**Examples:** `equals`, `contains`, `is-json`, `regex`, `code execution pass rate`, tool call name match, schema validation.

#### 2. Reference-Based Evals

**What they are:** Compare model output to a gold-standard reference answer using similarity metrics (ROUGE-N, BLEU, METEOR, BERTScore, embedding cosine similarity) or direct comparison logic.

**Trade-offs:** Objective anchor improves reliability dramatically. [Zheng et al.](https://arxiv.org/abs/2306.05685) measured reference anchoring reducing math failure rate from 70% to 15% — the single largest individual gain in their study.

**Where they break down:** As models improve, reference-based metrics penalize equally-valid paraphrases. Eugene Yan notes: "reference-based comparison degrades as models improve — suggests criteria-based evaluation instead." ROUGE/BLEU are "[unreliable and/or impractical](https://eugeneyan.com/writing/evals/)" per practitioner consensus. BERTScore is more robust but still surface-level.

#### 3. LLM-as-Judge (Model-Graded)

**What they are:** Use a capable LLM (often GPT-4, Claude Sonnet, or a fine-tuned judge model like Prometheus-2) to evaluate model outputs against a rubric. Variants: pointwise absolute scoring, pairwise comparison, rubric-based multi-dimensional scoring.

**Trade-offs:** Scalable, nuanced, handles open-ended text. [Zheng et al.](https://arxiv.org/abs/2306.05685) demonstrated 85–87% agreement with human judgments. Cost scales with judge model choice: Claude Haiku 4.5 at $1/$5 per MTok vs. Opus 4.7 at $5/$25 per MTok.

**Where they break down:** Position bias (75% first-position preference in weak judges), verbosity bias (91.3% failure in Claude-v1/GPT-3.5), self-preference (+25% win rate for Claude-v1 judging its own outputs), sycophancy (58.19% rate across major models per [SycEval 2025](https://arxiv.org/abs/2502.08177)), and domain expertise limits (agreement drops to 64–68% for expert-knowledge tasks per [Krumdick et al.](https://arxiv.org/abs/2503.05061)). Calibration against human labels is mandatory before use.

#### 4. Human-in-the-Loop Evals

**What they are:** Subject matter experts review model outputs, typically with pass/fail binary labels plus critique text (per [Hamel Husain's methodology](https://hamel.dev/blog/posts/llm-judge/)), or Likert-scale ratings (Harvey's 1–7 scale), or pairwise preference comparisons (Chatbot Arena model).

**Trade-offs:** Highest reliability, domain expertise built in, no calibration needed. Produces the calibration data that makes LLM judges viable.

**Where they break down:** Does not scale past ~100–500 samples per cadence for a solo founder. Inter-annotator agreement is often surprisingly low for subjective tasks (Krippendorff's α = 0.2–0.3 for open-ended quality judgments). [Hamel Husain](https://hamel.dev/blog/posts/evals) recommends binary (pass/fail) over Likert to maximize agreement.

#### 5. A/B Testing

**What they are:** Controlled experiments that split production traffic between a baseline and candidate system, measuring downstream user behavior outcomes (completion rates, re-query rates, CSAT scores, conversion rates).

**Trade-offs:** Ground truth for user value, not just model quality. GitHub Copilot's "Ship Room" process, Harvey's nightly canaries feeding into A/B decisions, and Decagon's two-phase offline/online system all culminate in A/B decisions.

**Where they break down:** Requires sufficient traffic volume for statistical power. Requires 24–72 hours minimum for behavioral signals. Cannot be used for pre-deployment quality gating.

#### 6. Multi-Turn / Trajectory Evals

**What they are:** Evaluate agent behavior across multi-step executions: which tools were called, in what order, with what arguments, and whether intermediate reasoning was sound. Includes `strict` / `unordered` / `subset` / `superset` trajectory match modes from [LangSmith's agentevals package](https://docs.langchain.com/langsmith/trajectory-evals), as well as LLM-judge trajectory quality assessment.

**Trade-offs:** Essential for catching "lucky hallucination" scenarios where correct final output masks broken reasoning. The only way to detect loops, unnecessary tool calls, or credit assignment to specific steps.

**Where they break down:** Deterministic trajectory matching is brittle when multiple valid tool call sequences exist. LLM trajectory judges require full context windows for long trajectories, raising cost. [Anthropic's engineering blog](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) recommends grading *outcomes over paths* for agentic evals.

#### 7. Rubric-Based Evals

**What they are:** Structured evaluation using explicitly specified criteria, often with behavioral anchors at each score level (e.g., 1-point: "contains hallucinated facts; 3-point: factually accurate but lacks supporting sources; 5-point: factually accurate, well-sourced, concise"). [Prometheus](https://arxiv.org/abs/2310.08491) demonstrated a 13B model trained on 1,000 fine-grained rubrics achieves Pearson correlation 0.897 with human evaluators — on par with GPT-4.

**Trade-offs:** Rubric specificity is the key discriminator. Vague rubrics ("helpful," "accurate") produce high variance. Specific rubrics ("does the output reference the prospect's most recent funding round?") produce reliable automated grading.

**Where they break down:** Require substantial upfront design effort. Criteria must be reviewed with domain experts before deployment. [Shreya Shankar's EvalGen](https://arxiv.org/abs/2404.12272) establishes that "it is impossible to completely determine evaluation criteria prior to human judging of LLM outputs" — criteria must be defined iteratively by seeing real outputs.

---

## Section 2 — Frameworks Deep Dive

**Key finding:** No single framework dominates. The correct choice depends on deployment context (OSS vs. SaaS), primary use case (CI gating vs. production monitoring), and ecosystem fit. **Anthropic has no standalone eval product as of April 2026** — the Console is UI-only; Bloom is safety-research tooling; the SDK has no eval hooks. [Anthropic's Jan 2026 engineering blog](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) explicitly recommends Braintrust, LangSmith, Langfuse, and Phoenix for production eval workflows.

### 1. Anthropic Console Evals + Bloom

**Type:** SaaS UI (Console) + OSS (Bloom) | **Price:** Free (Console) / Free MIT (Bloom) | **GitHub Stars:** N/A / safety-research/bloom | **Claude Native:** Yes | **Trajectory Support:** None (Console) / Behavioral elicitation only (Bloom)

The Console Evaluation tool is accessed via the **Evaluate** tab in console.anthropic.com. It requires prompts with `{{variable}}` syntax, generates test cases one row at a time via a button click, supports CSV import, runs side-by-side output comparisons across prompt versions, and grades on a **5-point scale**. It is a **UI-only prompt tester with no SDK, no CI/CD integration, no automated graders, and no agent trajectory support**. It cannot evaluate multi-turn conversations or tool use. According to [Anthropic's own docs](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool), there is no programmatic API for the eval UI.

**Bloom** (released December 19, 2025) is a safety-research OSS framework for *behavioral* evaluations. It runs four automated pipeline stages — Understanding, Ideation, Rollout, Judgment — to generate and evaluate scenarios designed to elicit specific model behaviors. Claude Opus 4.1 as judge achieves Spearman correlation 0.86 with human judgment; Sonnet 4.5 achieves 0.75. Bloom is not a general-purpose application eval tool; it is designed for safety researchers studying jailbreaks, evaluation awareness, and alignment behaviors.

**Weakness:** The Console eval tool is the weakest entry in this comparison — it is a getting-started aid, not production infrastructure. Bloom is safety-research tooling inaccessible to most application developers.

**Best for:** Early-stage single-turn prompt experimentation; safety researchers studying Claude behavioral properties.

---

### 2. OpenAI Evals (GitHub) + OpenAI API Evals

**Type:** OSS (GitHub) + SaaS API | **Price:** Free (GitHub MIT) / Pay-as-you-go (API) | **GitHub Stars:** 17.5k | **Claude Native:** No | **Trajectory Support:** Limited (Completion Function Protocol)

The [OpenAI Evals GitHub repository](https://github.com/openai/evals) (created January 2023, 460+ contributors) is the largest public benchmark registry. The API Evals feature enables creating automated eval pipelines using `string_check` graders (eq, like, ilike, contains, etc.) and LLM-judge graders via the Dashboard. The Completion Function Protocol (CFP) enables multi-step evals but is under-documented. The simple-evals repository was deprecated July 2025.

**Critical limitation:** No Claude/Anthropic support. No custom code evals in the public registry. API Evals only documents `string_check` publicly.

**Best for:** OpenAI ecosystem users; benchmark registry reference.

---

### 3. LangSmith

**Type:** SaaS | **Price:** Free (5k traces/mo), Plus ($5/1k traces), Enterprise (custom) | **GitHub Stars:** N/A (proprietary) | **Claude Native:** Partial (via `@traceable`) | **Trajectory Support:** Yes (Run tree / child_runs traversal)

[LangSmith](https://smith.langchain.com) is the most mature production eval + observability platform. Deepest LangGraph/LangChain integration: zero-config tracing for LangChain apps; `@traceable` decorator for arbitrary Python code. Agent trajectory eval via hierarchical `Run` tree — evaluators access `run.child_runs` to inspect intermediate tool calls. Production adopters include Klarna, J.P. Morgan, LinkedIn, Uber (SOC 2 Type 2 + HIPAA). SPADE ([arXiv:2401.03038](https://arxiv.org/abs/2401.03038)) is deployed within LangSmith for automated assertion generation from prompt histories, used across 2,000+ pipelines.

**Weakness:** Ecosystem dependency — weakest when not using LangChain/LangGraph. No native Anthropic SDK auto-instrumentation (requires `@traceable` wrappers). TypeScript/JavaScript support secondary.

**Best for:** LangChain/LangGraph ecosystem; production eval + tracing unified.

---

### 4. Langfuse

**Type:** OSS + SaaS | **Price:** $0 (50k units/mo), $29/mo Core (100k units), $199/mo Pro | **GitHub Stars:** 21.4k | **Claude Native:** Yes (via LiteLLM or `@observe()`) | **Trajectory Support:** Partial (sessions/spans, no trajectory assertions)

[Langfuse](https://langfuse.com) (YC W23, MIT license) is the strongest choice when data residency or self-hosting is required — Docker Compose in 5 minutes, Helm/Kubernetes for production, Terraform for AWS/Azure/GCP. Broadest integration list of any framework (30+), including Anthropic via LiteLLM, LangChain, LlamaIndex, CrewAI, AutoGen, Vercel AI SDK. The Anthropic recommendation in the Jan 2026 blog: "self-hosted open-source alternative to LangSmith for teams with data residency requirements." Scored/spans allow attaching LLM-judge or custom pipeline evaluations asynchronously to any trace or span.

**Weakness:** Agent trajectory *scoring* is not a native primitive — no `trajectory:tool-sequence` assertion type. LLM-judge evaluation runs async, adding latency to eval cycles. Enterprise tier at $2,499/mo is expensive.

**Best for:** EU data residency; self-hosted teams; broadest provider/framework support.

---

### 5. Promptfoo

**Type:** OSS + SaaS Enterprise | **Price:** Free (MIT, Community) / Enterprise (undisclosed) | **GitHub Stars:** 8.8k | **Claude Native:** Yes (`anthropic:messages:` provider) | **Trajectory Support:** Yes — first-class (`trajectory:tool-used`, `trajectory:tool-args-match`, `trajectory:tool-sequence`, `trajectory:step-count`, `trajectory:goal-success`)

[Promptfoo](https://promptfoo.dev) is a developer-first CLI tool that runs **100% locally** — prompts never leave the machine. Declarative YAML configs define providers, prompts, test cases, and assertions. The `trajectory:*` assertion namespace is the most granular of any framework: verify specific tools were called (`trajectory:tool-used`), called with specific arguments (`trajectory:tool-args-match`), called in a specific sequence (`trajectory:tool-sequence`), within a step count (`trajectory:step-count`), or achieved a goal assessed by an LLM judge (`trajectory:goal-success`). Native CI integration via `npx promptfoo eval --ci` returns non-zero exit on failures, blocking merges. Includes best-in-class red-teaming/vulnerability scanning (10k probes/month free).

```yaml
# promptfooconfig.yaml — example Jetix sales-researcher eval
providers:
  - anthropic:messages:claude-sonnet-4-6
prompts:
  - "Research {{company_name}} and provide funding history, headcount, and tech stack."
tests:
  - vars:
      company_name: "Acme GmbH"
    assert:
      - type: trajectory:tool-used
        value: web_search
      - type: trajectory:tool-sequence
        value: [web_search, extract_data, synthesize]
      - type: llm-rubric
        value: "Output contains funding amount, year, and investor names. No hallucinated facts."
      - type: trajectory:step-count
        threshold: 15
```

**Weakness:** No persistent storage, dashboards, or production monitoring in OSS tier. No native online/production eval mode. Last release October 2025 — moderate recency vs. competitors. UI/collaboration features limited in OSS.

**Best for:** CI-first workflow; trajectory assertion testing; red-teaming; Claude-native without ecosystem lock-in.

---

### 6. DeepEval / Confident AI

**Type:** OSS + SaaS | **Price:** Free (2 seats, 5 runs/week), $19.99/user/mo Starter | **GitHub Stars:** 14.9k | **Claude Native:** Yes (client wrapper) | **Trajectory Support:** Yes (8 agentic metrics: Task Completion, Tool Correctness, Goal Accuracy, Step Efficiency, Plan Adherence, Plan Quality, Tool Use, Argument Correctness; plus 3 MCP metrics)

[DeepEval](https://github.com/confident-ai/deepeval) (Apache 2.0, 9,199 commits) is pytest-native with the most comprehensive agentic metric suite available. `@observe` decorator traces full agent execution. Multi-turn evaluation via `ConversationalTestCase` and `MultiTurnSample`. Uniquely supports MCP (Model Context Protocol) evaluation metrics. The G-Eval and DAG (Deterministic Acyclic Graph) primitives provide research-backed LLM-judge scoring.

**Weakness:** Free tier is 5 eval runs/week with 1-week retention — essentially non-functional for CI. Paid cloud (Confident AI) required for team collaboration and meaningful CI/CD logging. Anthropic integration requires manual wrapper.

**Best for:** Comprehensive Python-based agentic metrics; pytest-native teams; MCP evaluation.

---

### 7. Inspect AI (UK AISI)

**Type:** OSS | **Price:** Free (MIT) | **GitHub Stars:** 1.3k | **Claude Native:** Yes (first-class `anthropic/claude-*` provider) | **Trajectory Support:** Yes (full agent trajectory, sandboxed environments, Docker/K8s)

[Inspect AI](https://inspect.aisi.org.uk) (UK AI Security Institute, released May 2024) is government-grade evaluation rigor. Declarative `Task(dataset, solver, scorer)` architecture. Sandboxed Docker/Kubernetes environments for isolated agent execution. 200+ pre-built evals in `inspect_evals`. Agent Bridge for external agent frameworks (Claude Code, LangChain, OpenAI Agents, Pydantic AI). VS Code extension for authoring and debugging. Bloom (Anthropic) exports Inspect-compatible transcripts, confirming Anthropic-internal adoption.

**Weakness:** Low community adoption (1.3k stars). Steep learning curve — framework-style abstractions. No SaaS, no production monitoring.

**Best for:** Safety and capability research; rigorous sandboxed evaluation; government/research contexts.

---

### 8. Braintrust

**Type:** SaaS | **Price:** Free (1GB/10k scores/14d), $249/mo Pro (5GB/50k scores/30d), Enterprise custom | **GitHub Stars:** ~90 (SDK) | **Claude Native:** Yes (`autoevals` supports `model="claude-3-5-sonnet-latest"`) | **Trajectory Support:** Partial (multi-step task support via custom scorers; no native trajectory assertion namespace)

[Braintrust](https://braintrust.dev) (raised $80M Series B, ICONIQ, February 2026) is the most unified eval + production observability platform. Custom "Brainstore" database delivers 86× faster full-text search and 2× read/write speed vs. competitors. The `autoevals` library (657 stars) provides the richest scorer library across Python and TypeScript. `Loop` AI agent auto-generates datasets, refines scorers, and optimizes prompts. Production adopters: Notion, Stripe, Vercel, Airtable, Replit, Zapier, Cloudflare. Named explicitly in Anthropic's Jan 2026 engineering blog as a recommended platform.

**Weakness:** No native trajectory assertion primitives. Short free tier (14-day retention). Self-hosting requires Enterprise plan. $249/mo Pro may be high for a solo founder.

**Best for:** Unified eval + production observability; TypeScript-first teams; production-grade data flywheel.

---

### 9. Humanloop

**Type:** SaaS Enterprise | **Price:** Free (2 users, 50 runs, 10k logs/mo) / Enterprise (undisclosed) | **GitHub Stars:** 7 (Python SDK) | **Claude Native:** Undisclosed | **Trajectory Support:** Undisclosed

[Humanloop](https://humanloop.com) is UI-first for enterprise prompt management and eval. Dual code/UI mode enables non-technical SMEs to contribute to evals alongside developers. Enterprise features: SSO, SAML, RBAC, VPC deployment.

**Weakness:** Pricing almost entirely undisclosed. Very low public GitHub presence (7 SDK stars). Claude/Anthropic integration undisclosed. Agent trajectory eval undisclosed. Not recommended for a solo founder operating without dedicated ML infrastructure.

**Best for:** Large enterprise teams where non-technical product managers need to participate in eval workflows.

---

### 10. Helicone

**Type:** OSS + SaaS | **Price:** Free (10k req/mo, 7-day retention), $79/mo Pro | **GitHub Stars:** 4.6k | **Claude Native:** Yes (dedicated Anthropic proxy) | **Trajectory Support:** None (pass-through only)

[Helicone](https://helicone.ai) (Apache 2.0, YC W23) is not an eval framework — it is an LLM observability proxy. One-line setup: change `base_url` to `https://anthropic.helicone.ai` and add `Helicone-Auth` header. All Claude API calls are logged automatically. Eval scores are POSTed externally via `/v1/request/{requestId}/score`. Webhooks trigger external eval frameworks automatically.

**Weakness:** Does not run evals. No LLM-judge, no trajectory assertion, no scoring logic — only a reporting layer requiring external framework integration.

**Best for:** Minimal-friction request logging and cost tracking; teams already using Anthropic API who need zero-setup observability.

---

### 11. Phoenix / Arize

**Type:** OSS (Phoenix, Elastic License 2.0) + SaaS (Arize AX) | **Price:** Free OSS / AX Free (25k spans) / $50/mo AX Pro | **GitHub Stars:** 8.5k | **Claude Native:** Yes (`AnthropicInstrumentor` auto-traces) | **Trajectory Support:** Partial (OTel traces, custom evaluators; no trajectory assertion DSL)

[Phoenix](https://phoenix.arize.com) is OTel-native — built on OpenTelemetry, integrates with any existing observability stack. `AnthropicInstrumentor` provides zero-code auto-tracing of all Anthropic API calls. Endorsed by Anthropic's Jan 2026 blog: "Phoenix: open-source for LLM tracing/debugging, offline/online evals." Strong RAG evaluation metrics. AX Pro at $50/mo is the most affordable SaaS tier of any production platform.

**Weakness:** Phoenix's Elastic License 2.0 (not MIT) restricts commercial SaaS use. No built-in trajectory assertion primitives. Agent trajectory evaluation requires custom code.

**Best for:** OTel-native stacks; existing Arize Enterprise users; RAG-heavy pipelines.

---

### 12. Galileo

**Type:** SaaS | **Price:** Free (5k traces/mo) / $100/mo Pro / Enterprise | **GitHub Stars:** 17 (dataquality repo, not representative) | **Claude Native:** Undisclosed | **Trajectory Support:** Yes (dedicated agentic performance metrics, distributed tracing beta)

[Galileo](https://galileo.ai) differentiates on **Luna-2** — fine-tuned Llama 3B/8B models achieving 0.88–0.95 accuracy on agentic evaluation tasks at 152ms latency and $0.02/1M tokens (97% cost reduction vs. GPT-4-based evaluation). CLHF (Continuous Learning via Human Feedback) enables metric customization via natural language critiques without engineering resources.

**Weakness:** Luna-2 and runtime guardrails are Enterprise-tier only (pricing undisclosed). Claude/Anthropic integration not explicitly documented. Free tier only 5k traces/month. No OSS version.

**Best for:** High-volume production monitoring (>50k events/mo) where Luna-2's cost efficiency justifies Enterprise tier.

---

### 13. Ragas

**Type:** OSS | **Price:** Free (Apache 2.0) / Ragas Cloud (undisclosed) | **GitHub Stars:** 11.2k | **Claude Native:** Yes (configurable judge LLM) | **Trajectory Support:** Yes (`ToolCallAccuracy`, `AgentGoalAccuracy`, `TopicAdherenceScore`, `MultiTurnSample`)

[Ragas](https://ragas.io) (Apache 2.0) is the de facto standard for RAG evaluation and has expanded to agent evaluation. Metric library includes `ToolCallAccuracy` (compares reference vs. actual tool calls — order, sequence, arguments), `AgentGoalAccuracyWithReference` (binary: did agent achieve goal?), and `TopicAdherenceScore` (evaluates AI staying within predefined domains). `MultiTurnSample` primitives support multi-turn agent evaluation. Pure Python library — no UI.

**Weakness:** No UI. Ragas Cloud pricing undisclosed. `ToolCallAccuracy` requires exact tool call sequence matching — brittle for complex agents. Fewer agentic metrics than DeepEval (3 vs. 8+ dedicated).

**Best for:** RAG metric suite; custom Python pipelines; teams already using LangSmith or Helicone for logging.

---

### 14. TruLens (Snowflake)

**Type:** OSS | **Price:** Free (MIT) | **GitHub Stars:** 3.1k | **Claude Native:** Yes (via any LLM provider wrapper) | **Trajectory Support:** Yes (Feedback Functions evaluate tool calls, plans, retrieved context)

[TruLens](https://trulens.org) (MIT, Snowflake) is OTel-native with **Feedback Functions** as the core primitive — composable evaluators pairing feedback providers (LLM, classifier, custom) with implementations (prompts, scoring logic). Deep Snowflake Cortex integration for data-warehouse-native evaluation. `_with_cot_reasons` variants provide CoT reasoning transparency. TruLens 2.7.0 released February 2026, actively maintained under Snowflake.

**Weakness:** Small community (3.1k stars). Snowflake acquisition creates product direction uncertainty. No SaaS dashboard. Documentation quality below commercial competitors.

**Best for:** Snowflake-native data stacks; OTel-integrated observability; teams needing MIT license with full commercial freedom.

---

### Framework Comparison Table

| Framework | Type | Pricing | GitHub Stars | Claude Native | Agent Trajectory | Best For | Key Weakness |
|---|---|---|---|---|---|---|---|
| Anthropic Console | SaaS UI-only | Free w/ API | N/A | Native | ❌ None | Early prompt prototyping | No SDK, no CI, no trajectories |
| OpenAI Evals | OSS + SaaS | Free (OSS) / PAYG | 17.5k | ❌ No | Limited (CFP) | OpenAI ecosystem | No Claude; limited public graders |
| LangSmith | SaaS | Free–Enterprise | N/A | Partial | ✅ Run tree | LangChain/LangGraph teams | Ecosystem dependency; Python-first |
| Langfuse | OSS+SaaS | $0–$199/mo | 21.4k | ✅ Yes | Partial | Self-hosted; EU data residency | No trajectory assertion DSL |
| **Promptfoo** | **OSS+SaaS** | **Free OSS** | **8.8k** | **✅ Yes** | **✅ First-class** | **CI-first; trajectory assertions** | No persistent prod monitoring |
| DeepEval | OSS+SaaS | Free–$50+/user/mo | 14.9k | ✅ Yes | ✅ 8 agent metrics | Comprehensive Python metrics | Free tier ~unusable for CI |
| Inspect AI | OSS | Free MIT | 1.3k | ✅ Yes | ✅ Sandboxed | Safety research; rigorous eval | Low community; steep learning curve |
| **Braintrust** | **SaaS** | **$0–$249/mo** | ~90 | **✅ Yes** | Partial | **Unified eval+observability** | No trajectory DSL; $249/mo Pro |
| Humanloop | SaaS | Mostly undisclosed | 7 | Undisclosed | Undisclosed | Enterprise non-technical SMEs | Pricing/features opaque |
| Helicone | OSS+SaaS | $0–$79/mo | 4.6k | ✅ Yes | ❌ None | Zero-setup request logging | Not an eval tool; pass-through only |
| Phoenix/Arize | OSS+SaaS | $0–$50/mo | 8.5k | ✅ Yes | Partial | OTel stacks; RAG | Elastic License; no trajectory DSL |
| Galileo | SaaS | $0–$100+/mo | 17 | Undisclosed | ✅ Agentic metrics | High-vol prod; Luna-2 judge | Luna-2 = Enterprise only |
| Ragas | OSS | Free Apache | 11.2k | ✅ Yes | ✅ MultiTurn | RAG + agent metrics | No UI; brittle sequence matching |
| TruLens | OSS | Free MIT | 3.1k | ✅ Yes | ✅ Feedback Fns | Snowflake-native OTel | Small community; Snowflake uncertainty |

> **Anthropic situation (prominent flag):** As of April 2026, Anthropic has **no standalone eval product**. The Console eval tool is UI-only with no API access, no CI integration, no automated graders, and no agent trajectory support. Anthropic's own [January 2026 engineering blog](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) explicitly recommends using third-party platforms (Braintrust, LangSmith, Langfuse, Arize Phoenix) for production eval workflows. Teams should not wait for an Anthropic-native eval SDK — it does not exist and is not publicly roadmapped.

---

## Section 3 — Benchmarks Landscape

**Key finding:** Benchmark saturation is the defining challenge of 2026. A [systematic study of 60 benchmarks](https://arxiv.org/html/2602.16763v1) found ~49% exhibit high-to-very-high saturation. The five benchmarks most relevant to Jetix's context — GAIA, τ-bench, BrowseComp, TheAgentCompany, AssistantBench — are all still meaningful because they test multi-step real-world tasks rather than narrow static QA.

### Benchmark Comparison Table

| Benchmark | Year | Domain | Tasks | SOTA (Model, Score, Date) | Contamination | Jetix Relevance |
|---|---|---|---|---|---|---|
| SWE-bench Verified | 2024 | Code bug-fixing | 500 | Claude Mythos Preview 93.9% (2026, vals.ai) | **Critical** — OpenAI ceased reporting Feb 2026; 10.6% data leakage | ❌ |
| MMLU | 2020 | Broad knowledge QA | 15,908 | GPT-5 92.5% (LLM Stats) | **High** — 16%+ confirmed leaked; MMLU-CF shows −14.6pp for GPT-4o | ⚠️ |
| HumanEval | 2021 | Python code | 164 | MiniCPM-SALA 95.1% (LLM Stats) | **Critical** — fully saturated; ~100% likely in training | ❌ |
| GAIA | 2023 | General AI assistant | 466 (300 private) | HAL Generalist (Claude Sonnet 4.5) 74.6% (HAL Princeton, Apr 2026) | **Low** — hand-crafted, answers private | ✅ |
| τ-bench | 2024 | Customer service agents | ~680 | Claude Mythos Preview 89.2% (BenchLM) | **Low** — simulated env | ✅ |
| OSWorld | 2024 | Desktop/GUI agents | 369 | Claude Mythos Preview 79.6% (BenchLM) | **Low** — execution-based | ⚠️ |
| WebArena | 2023 | Web agents | 812 | Narada Operator 64.2% (Oct 2025) | **Moderate** | ⚠️ |
| MLE-bench | 2024 | ML engineering | 75 Kaggle comps | Operand ensemble 39.56% (GitHub LB) | **Moderate** | ❌ |
| BrowseComp | 2025 | Web research persistence | 1,266 | OpenAI Deep Research 51.5% (paper) | **Low** — designed to be un-solvable without browsing | ✅ |
| TheAgentCompany | 2024 | Workplace agents | 175 | Gemini-2.5-Pro 30% (paper v3) | **Low** — self-hosted env | ✅ |
| AssistantBench | 2024 | Time-consuming web research | 214 | SPA+Claude-3.5-Sonnet 26.4% (paper) | **Low** | ✅ |
| SWE-bench Live | 2025 | Live code bug-fixing | 1,319 (monthly update) | OpenHands+Claude 3.7 Sonnet 19.25% (paper) | **Very Low** — post-2024 issues only | ❌ |

### The 5 Most Relevant Benchmarks for Jetix

#### GAIA
[arXiv:2311.12983](https://arxiv.org/abs/2311.12983) — 466 questions testing multi-step reasoning, tool use, and web browsing. Level 1–3 difficulty. Answers held private for test set (300 questions); validated via exact match. SOTA: HAL Generalist (Claude Sonnet 4.5) at 74.6% vs. human baseline 92%. Cost to run validation set (165 questions): $7–$680 depending on model (Gemini 2.0 Flash ~$7.80 vs. Claude Opus 4 ~$665 per [HAL Princeton](https://hal.cs.princeton.edu/gaia)). Directly maps to Jetix knowledge-synthesis and research-support tasks. Low contamination risk.

#### τ-bench (tau-bench)
[arXiv:2406.12045](https://arxiv.org/abs/2406.12045) — Customer service agent benchmark (retail, airline domains) with database-state evaluation rather than LLM judge. Introduces **pass^k** metric measuring reliability across k repeated trials — the only major benchmark that seriously measures consistency. [Sierra found](https://sierra.ai/blog/benchmarking-ai-agents) GPT-4o drops from ~60% pass^1 to ~25% pass^8 on τ-retail — "a staggering 60% drop." SOTA: Claude Mythos Preview 89.2% (BenchLM). Directly relevant to Jetix customer-facing agents.

#### BrowseComp
[arXiv:2504.12516](https://arxiv.org/abs/2504.12516) — 1,266 hard-to-find questions requiring multi-hop web browsing persistence. Designed to be unsolvable by pre-2025 models without live browsing. SOTA: OpenAI Deep Research 51.5%. Directly tests what knowledge-synthesis and sales-researcher agents do: finding non-obvious information from diverse web sources.

#### TheAgentCompany
[arXiv:2412.14161](https://arxiv.org/abs/2412.14161) — 175 workplace tasks in a simulated software startup (GitLab, OwnCloud, Plane, RocketChat). Includes software dev, project management, financial analysis, HR, and admin tasks. Checkpoint-based evaluation with partial credit (50% bonus for full completion). SOTA: Gemini-2.5-Pro 30% / Claude-3.5-Sonnet 24%. No human baseline established, but estimated >70% for most tasks — significant headroom.

#### AssistantBench
[arXiv:2407.15711](https://arxiv.org/abs/2407.15711) — 214 tasks humans would spend 10+ minutes on: monitoring real estate markets, locating businesses, research synthesis. SOTA: SPA+Claude-3.5-Sonnet 26.4%. Key insight: pure web agents get near-zero; best results combine web agent + fallback to closed-book knowledge. Tests exactly what a sales-researcher or knowledge-synth agent must do.

### Saturation and Contamination Summary

**Saturated (avoid for frontier model comparison):** HumanEval (95%+), MMLU (92.5% GPT-5), MBPP, SWE-bench Verified (abandoned by OpenAI). These benchmarks reveal nothing about frontier model differences.

**Contamination-compromised:** GPT-4o drops 14.6 percentage points from MMLU to MMLU-CF ([Microsoft MMLU-CF](https://www.microsoft.com/en-us/research/publication/mmlu-cf-a-contamination-free-multi-task-language-understanding-benchmark/)). GSM8K accuracy drops ~22.9% with inference-time decontamination. SWE-bench Live (post-2024 GitHub issues) scores are 24 points lower than SWE-bench Verified for the same system — revealing contamination inflation in the static benchmark.

**MMLU error rate:** [Gema et al. (NAACL 2024)](https://arxiv.org/abs/2406.04127) found 6.49% error rate across 3,000 reviewed questions; Virology subset has 57% error rate. Do not rely on MMLU scores for production decision-making.

---

## Section 4 — LLM-as-Judge Best Practices

**Key finding:** LLM-as-judge is viable as a scalable evaluation mechanism, but only with calibration. An uncalibrated judge measures verbosity and confidence rather than quality. The foundational empirical work ([Zheng et al., arXiv:2306.05685](https://arxiv.org/abs/2306.05685)) establishes both the viability (85–87% human agreement) and the failure modes (75% position bias, 91.3% verbosity failure) that practitioners must mitigate.

### Foundational Evidence (Zheng et al.)

The seminal paper introduced MT-Bench (80 high-quality multi-turn questions, 3,000+ expert votes) and Chatbot Arena (30,000+ human preference votes) to measure GPT-4-as-judge vs. human ground truth:

| Setting | Agreement | Vote Count |
|---|---|---|
| MT-Bench Turn 1 — GPT-4 Pairwise | **85%** | 859 |
| MT-Bench Turn 1 — Human–Human | **81%** | 479 |
| Chatbot Arena — GPT-4 Pairwise | **87%** | 1,944 |

GPT-4 as judge slightly exceeds human-human agreement (81–82%), making it viable as a scalable proxy. Agreement rises from ~70% to nearly 100% as quality gap between compared outputs increases.

### Biases with Magnitudes

| Bias | Worst-Case Magnitude | Best Judge Behavior | Source |
|---|---|---|---|
| Position bias | 75% first-position preference (Claude-v1) | GPT-4: 65% consistency (improved to 77.5% with few-shot) | [Zheng et al.](https://arxiv.org/abs/2306.05685) |
| Verbosity bias | 91.3% failure rate (Claude-v1, GPT-3.5) | GPT-4: 8.7% failure | [Zheng et al.](https://arxiv.org/abs/2306.05685) |
| Self-enhancement | +25% win rate over baseline (Claude-v1) | GPT-4: +10% | [Zheng et al.](https://arxiv.org/abs/2306.05685) |
| Sycophancy | 62.47% rate (Gemini-1.5-Pro); 58.19% aggregate | GPT-4o: 56.71% | [SycEval 2025, arXiv:2502.08177](https://arxiv.org/abs/2502.08177) |
| Authority bias | 33.8% manipulated (ChatGPT) | Claude-3.5-Sonnet: 86.5% robust | [CALM framework](https://llm-judge-bias.github.io) |
| Distraction (pairwise) | 35% preference flip rate | Absolute scoring: 9% flip | [Tripathi et al., arXiv:2504.14716](https://arxiv.org/abs/2504.14716) |
| Familiarity/perplexity | Worse-than-human inter-sample agreement | Single-attribute prompts | [Stureborg et al., arXiv:2405.01724](https://arxiv.org/abs/2405.01724) |
| Anchoring (multi-attribute) | Degrades with each additional attribute | One criterion per prompt | [Stureborg et al., arXiv:2405.01724](https://arxiv.org/abs/2405.01724) |
| Domain expertise ceiling | 64–68% agreement on expert-knowledge tasks | Human experts: 72–75% | [Krumdick et al., arXiv:2503.05061](https://arxiv.org/abs/2503.05061) |

### Calibration Techniques with Empirical Gains

| Technique | Measured Gain | Cost | Use For |
|---|---|---|---|
| Reference answer anchoring | −78% failure rate on factuality (Zheng et al.) | Low (prompt addition) | Factuality, FPF compliance |
| Few-shot anchoring | +12.5pp position consistency (65%→77.5%, Zheng et al.) | Medium (annotation) | All evaluations; essential baseline |
| CoT reasoning in judge | −57% failure rate on math (Zheng et al.); Spearman ρ=0.514 (G-Eval) | Low–medium | Reasoning, structured criteria |
| Rubric specification | Pearson ρ=0.897 (Prometheus 13B with 1,000 rubrics) | Low (design effort) | Structured outputs; FPF |
| Position swap (pairwise) | Eliminates positional artifacts | Low (2× inference) | All pairwise evaluations |
| Ensemble k=8 (same prompt variants) | +9.8pp accuracy ([arXiv:2604.13717](https://arxiv.org/abs/2604.13717)) | 8× cost | High-stakes decisions |
| PoLL (panel of 3 diverse models) | Outperforms GPT-4 alone; 1/7 cost ([Verga et al., arXiv:2404.18796](https://arxiv.org/abs/2404.18796)) | 1/7 GPT-4 cost | Production monitoring at scale |
| Debias prompting | +10–17% Spearman ρ (Eugene Yan, eugeneyan.com) | Negligible | Open-ended quality |

**Ensemble vs. single judge:** [Verga et al. (PoLL)](https://arxiv.org/abs/2404.18796) demonstrated that a panel of three smaller models (`command-r`, `gpt-3.5-turbo`, `haiku`) outperforms a single GPT-4 judge across 3 settings and 6 datasets at 1/7th the cost, with less intra-model bias due to disjoint model families. Ensemble scoring with k=8 independent completions yields +9.8 percentage points accuracy — the largest single-technique gain measured in [the 2026 empirical study](https://arxiv.org/abs/2604.13717). However, ensembling fails for expert-domain tasks: even strong ensembles drop to 64–68% agreement on specialist knowledge.

### Hamel Husain — Critique Shadowing (6 Steps)

From [hamel.dev/blog/posts/llm-judge/](https://hamel.dev/blog/posts/llm-judge/), the complete practitioner workflow:

1. **Find Principal Domain Expert** — One key person with deep domain knowledge. "Many developers attempt to act as the domain expert themselves... This is a recipe for disaster." For Jetix (solo founder): the founder *is* the domain expert, but must discipline themselves to play the expert role distinctly from the developer role.

2. **Create a Dataset** — Diverse examples covering Features × Scenarios × Personas. Start with ~30 examples. "You can get quite far in just 15 minutes." Use LLM to generate *inputs* (not outputs) synthetically.

3. **Domain Expert Reviews: Pass/Fail + Critique** — Binary (not 1–5). "A binary decision forces everyone to consider what truly matters." Critiques must be detailed enough to use as few-shot examples in a judge prompt. "If your evaluations consist of a bunch of metrics that LLMs score on a 1-5 scale, you're doing it wrong."

4. **Fix Obvious Errors** — Before building a judge, address glaring errors in the model's outputs. Return to Step 3.

5. **Build LLM Judge Iteratively** — Expert critiques as few-shot examples. Track precision/recall (not raw agreement). Aim for >90%. "It took us only three iterations to achieve >90% agreement." Example result: Honeycomb case study — 30% accuracy improvement after 3 calibration iterations.

6. **Error Analysis + Repeat Periodically** — Segment errors by dimension. "I conduct this human review at regular intervals and whenever something material changes."

### Shreya Shankar — EvalGen and Criteria Drift

From [EvalGen (arXiv:2404.12272)](https://arxiv.org/abs/2404.12272), the key insight for practitioners:

> "Users need criteria to grade outputs, but grading outputs helps users define criteria."

This circular dependency — criteria drift — means evaluation criteria cannot be fully specified before seeing real model outputs. Some criteria are output-dependent: they emerge from observing what the model actually produces. The practical implication: expose domain experts to 20+ diverse real outputs before finalizing any rubric. EvalGen achieves 0.73 recall on product defects vs. SPADE baseline of 0.49 by incorporating human judgment into the criteria generation loop.

### Failure Categories

**Domain expertise failures:** LLM judges agree with humans only on questions the judge itself can answer correctly ([Krumdick et al.](https://arxiv.org/abs/2503.05061)). For specialized domains (FPF compliance, legal, medical), either provide expert-written reference answers or use hybrid human-in-the-loop.

**Open-ended creative tasks:** MT-Bench writing category achieves only 42% position consistency vs. 86% for math ([Zheng et al.](https://arxiv.org/abs/2306.05685)). Accept lower agreement targets; use pairwise comparison rather than pointwise for subjective dimensions.

**Factuality without reference:** GPT-3.5-turbo sensitivity to inconsistencies is only 30–60% (Eugene Yan). Without a reference answer, LLM judge factuality evaluation is unreliable. NLI-based fine-tuned classifiers outperform generic LLM judges for factual consistency per [Eugene Yan's analysis](https://eugeneyan.com/writing/evals/).

**Judge-model circularity (Dorner et al., [arXiv:2410.13341](https://arxiv.org/abs/2410.13341)):** When the evaluated model is more capable than the judge, the judge loses discriminative signal. For Jetix's application-level evals (not frontier capability evals), this is unlikely to be a problem with Claude Opus 4.7-level judges.

---

## Section 5 — Trajectory Eval & Production Pipelines

**Key finding:** Output-only evaluation misses broken reasoning masked by correct final answers. The three evaluation levels form a diagnostic hierarchy: black-box (what went wrong) → trajectory/glass-box (where it went wrong) → single-step/white-box (why it went wrong). Production eval pipelines require five distinct layers from offline golden sets to production drift monitoring.

### Multi-Step Eval Techniques

**Trajectory Match Modes** (from [LangSmith agentevals](https://docs.langchain.com/langsmith/trajectory-evals)):

| Mode | Description | Jetix Use Case |
|---|---|---|
| `strict` | Exact tool sequence match | Policy-mandated: authenticate before accessing CRM data |
| `unordered` | Same tools, any order | Research queries where tool call order is flexible |
| `subset` | Agent calls only tools from reference set | Ensuring sales-outreach agent doesn't use unapproved data sources |
| `superset` | Agent calls at least reference tools | Verifying minimum required research actions completed |

**Terminal-Bench key-action matching** ([arXiv:2601.11868](https://arxiv.org/html/2601.11868v1)): Each task has a containerized Docker environment and a bash/unit-test script that deterministically verifies completion. Frontier models score below 65% on Terminal-Bench 2.0 — demonstrating real-world task difficulty that SWE-bench's contaminated scores obscure.

**AgentBoard partial credit formula** ([Ma et al., arXiv:2401.13178](https://arxiv.org/abs/2401.13178)): Rather than binary pass/fail, computes progress rate `r_t = max_{1 ≤ i ≤ t} f(s_i, g)` — maximum similarity between any intermediate state visited and the goal state. Subgoal decomposition: `r_t^subgoal = max_{1 ≤ k ≤ K} f(s_i, g_k)`. Validated against 60 human-annotated trajectories per task. Essential for long-horizon tasks where partial completion has real business value.

**CaRT counterfactuals** ([arXiv:2510.08517](https://arxiv.org/html/2510.08517v1)): Minimal trajectory perturbations to find the "breakpoint" where termination vs. continuation caused a ≥50% change in task success rate. Enables causal diagnosis of which specific step caused failure.

**Tool-arg schema checks** (TRAJECT-Bench, [arXiv:2510.04550](https://arxiv.org/html/2510.04550v1)): Beyond name matching — verify argument types, formats, and value ranges conform to the tool's specification. Catches agents passing date strings where integers are required.

**Loop detection signals:** Turn cap exceeded → `trajectory:step-count` assertion; repeated `(tool, args)` tuples ≥N consecutive times; token budget anomalies (5× average spend = likely looping); AgentBoard progress rate plateauing for K rounds. A [February 2026 production incident](https://www.reddit.com/r/AI_Agents/comments/1r9cj81/our_ai_agent_got_stuck_in_a_loop_and_brought_down/) documented an agent loop taking down production infrastructure — mitigated via per-agent gateway rate limits, step caps, and anomaly-detection kill-switches.

### Production Pipeline Architecture

[Braintrust's five-layer architecture](https://www.braintrust.dev/docs/guides/evals):

```
Layer 1: Iterate in playgrounds    → mutable, rapid iteration on prompts
Layer 2: Promote to experiments    → immutable snapshots for regression comparison
Layer 3: Automate in CI/CD         → pre-deploy regression gates on every PR
Layer 4: Score in production       → online eval on sampled traffic (~5%)
Layer 5: Feed back                 → production traces → golden dataset
```

**Golden set construction:** 20–100 examples to start; 50–200 for statistical confidence (per [Braintrust guide](https://www.braintrust.dev/articles/what-is-prompt-evaluation)). Source from production logs — real user queries capture intent and ambiguity that synthetic data misses. Version control alongside prompts. Aim for 50–100 failure cases out of 200+ total ([Eugene Yan](https://eugeneyan.com/writing/product-evals/)). Lock datasets after publication to prevent rubric changes masquerading as improvements.

**SPADE automated assertions** ([Shankar et al., arXiv:2401.03038](https://arxiv.org/abs/2401.03038)): Synthesizes data quality assertions by analyzing prompt revision histories. Results across 9 real-world LLM pipelines: 14% reduction in assertion count, 21% decrease in false failure rate. Deployed within LangSmith, active in 2,000+ pipelines.

**CI/CD GitHub Actions pattern** ([Promptfoo CI/CD docs](https://www.promptfoo.dev/docs/integrations/ci-cd/)):

```yaml
# .github/workflows/eval.yml
name: Agent Eval CI
on: [pull_request]
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Promptfoo eval suite
        run: npx promptfoo eval --config promptfooconfig.yaml --output results.json
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      - name: Quality gate check
        run: |
          PASS_RATE=$(jq '.results.stats.successes / (.results.stats.successes + .results.stats.failures) * 100' results.json)
          if (( $(echo "$PASS_RATE < 85" | bc -l) )); then
            echo "Quality gate failed: Pass rate ${PASS_RATE}% < 85%"
            exit 1
          fi
```

**Shadow traffic pattern** ([CodeAnt AI](https://www.codeant.ai/blogs/shadow-traffic-llm-testing)): API gateway duplicates production requests to candidate model without serving response to users → automated quality comparison → shadow → canary (1% real traffic, 24–48h) → full rollout. Cost: roughly doubles inference spend during evaluation; use only for major changes.

**Online eval tiered middleware:**

```
Layer 1: Deterministic (every request, <50ms)   → PII check, JSON schema, format
Layer 2: Heuristic (every request)              → Embedding similarity, regex, keyword
Layer 3: LLM-as-Judge (5% sample, async)        → Faithfulness, relevance, tone
Layer 4: Human review (annotation queue)        → Complex failures, calibration
```

**Drift alerts:** 24-hour rolling averages; alert on quality metric drops, error rate spikes, latency P95 increases, user satisfaction drops.

---

## Section 6 — Production Case Studies

**Key finding:** Every production AI company with a disclosed methodology uses offline + online hybrid evaluation. Public benchmarks are necessary but insufficient — all leaders built internal benchmarks because public ones misalign with their production reality. LLM-as-judge scales quality assessment; human review remains the indispensable calibration backstop.

### Anthropic

Anthropic runs tiered evaluations spanning capability benchmarks, human preference evaluations (win rates), safety/frontier-risk evaluations (ASL classification), and white-box internal activation analysis. Two primary grading methods per the [Claude 3.5 Sonnet Model Card](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf):

> "We assess our models using two key methods: (1) employing another model to grade responses via few-shot prompts and (2) using string matching to identify refusals."

Win rates against baseline (Claude 3 Opus = 50% baseline), broken out by domain: Law 82%, Finance 73%, Philosophy 73%, Coding 60%. Internal agentic coding eval: 64% pass-all-tests (Claude 3.5 Sonnet) vs. 38% (Claude 3 Opus). RSP evaluation cadence: 6-month interval (one evaluation delayed by 3 days for capability elicitation refinement). ASL-3/4 thresholds are hard deployment gates: CBRN-3 (substantially uplift non-state-actor bioweapon capability), AI R&D-4 (automate entry-level AI research). The [Claude Mythos Preview System Card](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf) introduced white-box/internal-activation analysis — Anthropic now reasons about internal states and the gap between what a model says and what its mechanisms represent.

SWE-bench Verified trajectory: Claude Opus 4.6 80.8% → Opus 4.7 87.6% → Mythos Preview 93.9%. Bloom (safety OSS tool, December 2025) achieved Claude Opus 4.1 Spearman correlation 0.86 with human judgment.

### OpenAI

The [Preparedness Framework](https://openai.com/index/o3-mini-system-card/) gates deployment on post-mitigation scores across CBRN, Cybersecurity, Persuasion, and Model Autonomy domains. Only models with post-mitigation score ≤ "medium" can be deployed; only ≤ "high" can continue development. Third-party evaluators: METR (autonomous capabilities), Apollo Research (scheming/sabotage), Pattern Labs (cyberoffensive). 

METR time-horizon methodology: "50% reliability threshold" task completion as a function of human task duration. o3's time horizon: **1 hour 30 minutes** (50% success on tasks humans complete in that time). o3 reward hacking rate: ~1% of all task attempts. OpenAI's [simple-evals repository](https://github.com/openai/simple-evals) was deprecated July 2025.

Published o3/o4-mini metrics: SimpleQA accuracy 0.49 (o3) / 0.20 (o4-mini); hallucination rate 0.51 (o3). Pattern Labs evasion: 51%. METR time horizon: o3 = 1.5h, o4-mini = 1h 15m.

### Google DeepMind

[Gemini 3.1 Pro Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/): ARC-AGI-2 77.1%, τ²-bench Retail 90.8%, τ²-bench Telecom 99.3%, GPQA Diamond 94.3%, Humanity's Last Exam 44.4%. Frontier Safety Framework (FSF) — Critical Capability Levels (CCLs): CBRN Uplift Level 1, Cyber Autonomy Level 1, ML R&D Uplift Level 1, Deceptive Alignment Level 1. Gemini 3.1 Pro status: below all CCLs; alert thresholds met for Cyber Autonomy Level 1 from Gemini 3.x onward.

Safety regression format: explicit ± vs. prior model (Text to Text Safety: +0.10%, Unjustified-refusals: −0.08%). Gemini 2.0's automated red teaming: "now automatically generating evaluations and training data to mitigate [risks]" — capability not yet seen at other labs.

### Cognition / Devin

Cognition runs two evaluation tracks: SWE-bench (public comparison) and `cognition-golden` (internal). SWE-bench trajectory: 13.86% (March 2024 launch, 570 instances) → 45.8% (Devin 2.0, SWE-bench Verified) → `cognition-golden` internal: 74.2%. Evaluator design: agentic evaluators with autonomous judgment, scored 0–1, averaged across multiple Devin trials and evaluator trials to reduce variance. Meta-evaluation: precision/recall on ground truth sets + continuous human review of proof-of-success screenshots. Key quote: ["Thanks to our autonomous evaluations, we can measure the full spectrum of outcomes and compute objective reliability metrics before any new Devin deployment."](https://cognition.ai/blog/evaluating-coding-agents)

### Aider

[Aider's Polyglot leaderboard](https://aider.chat/docs/leaderboards/) (225 Exercism exercises across C++, Go, Java, JavaScript, Python, Rust) is fully open-source and reproducible. Selected results: gpt-5 (high) 88.0% at $29.08; claude-opus-4 (32k thinking) 72.0% at $65.75; gpt-4o-2024-08-06 23.1% at $7.03. SHA hashing of API requests detects nondeterminism. Benchmark is run as a regression tool before publishing any prompting change — the clearest example of CI-style benchmark integration in the industry.

### Sierra AI

[τ-bench](https://arxiv.org/abs/2406.12045) was developed by Sierra and used internally. Design philosophy: evaluate database state at conversation end (objective outcome), not conversation quality (subjective LLM judge). Sierra found GPT-4o drops from ~60% pass^1 to ~25% pass^8 on τ-retail — the canonical demonstration that single-trial accuracy is misleading for production reliability. pass^k is now adopted in Anthropic model cards.

### Harvey AI

[BigLaw Bench (BLB)](https://www.harvey.ai/blog/introducing-biglaw-bench) — core tasks from litigation (8 categories) and transactional (8 categories), derived from real billable time entries at BigLaw firms, graded by attorneys. BLB performance trajectory: 60% (2024 baseline: GPT-4o, Claude 3.5, Gemini 1.5) → 90% (2026: GPT-5, Claude 4.5, Gemini 3). Harvey's Document Q&A score: 94.8% (highest of any tool or human lawyer per [Vals AI VLAIR report](https://www.vals.ai/industry-reports/vlair-2-27-25)). Nightly canary evaluations catch regressions in sourcing accuracy and answer quality before production deployment. Dataset versioning: once "published," test sets are locked — immutable baselines.

### Replit Agent

Replit abandoned SWE-bench when they "realized this wasn't actually measuring what their users wanted." Internal harness: Python-based, spins up Chrome instances and Docker containers, uses Anthropic computer use to simulate users. Metric: time-to-working-application — reduced from 6–7 minutes (initial agentic loop) to under 2 minutes (Rapid Build Mode). Tooling: Braintrust for evaluations, LangSmith for trace monitoring. Key insight: "Evaluations are a long-term investment that truly pays off: resource-intensive to build and run, creating a moat that's hard to replicate."

### Cursor

[CursorBench](https://cursor.com/blog/cursorbench) — internal benchmark derived from real Cursor sessions using **Cursor Blame** (traces committed code back to the agent request that produced it). Tasks are 2× longer than SWE-bench Verified in lines of code and files. CursorBench produces more separation between frontier models than public benchmarks. Key quote: "CursorBench refreshed every 2–3 months to prevent contamination and track shifts in usage patterns." Hybrid offline + online eval: "Online evals catch regressions that offline suites miss, like where the agent's output looks correct to a grader but feels worse to a developer."

### Klarna AI Assistant

Within first month (February 2024 self-reported): 2.3 million conversations, 67% of all customer service chats, equivalent of 700 full-time agents, CSAT on par with human agents, 25% drop in repeat inquiries, average resolution time under 2 minutes vs. 11 minutes with humans. Estimated $40 million profit improvement in 2024. **However:** CSAT metrics declined as customers encountered limitations on complex issues; Klarna re-hired human agents and pivoted to hybrid model. Eval methodology: entirely undisclosed. The Klarna case demonstrates that initial headline metrics can be misleading without sustained multi-dimensional evaluation.

### Decagon

[Decagon's two-phased framework](https://decagon.ai/blog/evaluation-engine-ai-agents): offline LLM-as-judge on structured triplets (user query, context, response) + online A/B testing with gradual traffic rollout. Criteria: Relevance, Correctness, Naturalness, Empathy. Human audit of a subset. Ground truth evaluation set: "a curated collection of user queries with ideal responses, labeled by human experts." Results: LLM-as-judge achieved 79% F1 vs. 80% human accuracy. Published outcomes: Duolingo >80% deflection; Oura Ring 3× CSAT increase; ClassPass 95% cost reduction per support conversation.

### GitHub Copilot

Four eval categories: (1) Verifiable evals ("harness lib") — unit-test-based code completion, open-source repos, "melon ball" implementations; (2) A/B testing ("Ship Room") — weekly launch decisions at 10% traffic; (3) LLM-as-judge for chat — specific granular criteria (e.g., "Does it have a test for passing in null values?"); (4) Algorithmic eval for tool use — confusion matrices for function-calling accuracy. Key insight: "The generative task (solving a coding problem from scratch) is much harder than the verification task (checking whether a solution meets a detailed list of requirements) — this asymmetry is why LLM-as-judge can work even when the judge has similar capabilities to the model being evaluated."

### Scale AI

Scale AI's SEAL (Safety, Evaluations, and Analysis Lab) runs 10,000+ test cases per week for frontier AI labs. Provides human annotation pipelines for safety eval, capability benchmarking, and multilingual assessment. Confirmed role in OpenAI's safety pipeline: o3-mini system card — "Human Sourced Jailbreaks: collected by Scale and determined by Scale to be high harm."

---

## Section 7 — Failure Modes & Economics

**Key finding:** The three critical failure modes for production eval systems are Goodhart's Law gaming, dataset contamination, and judge bias. All three are manageable with specific countermeasures, but none can be fully eliminated. Cost economics have improved dramatically — Haiku 4.5 at $65 per 50 SWE-bench tasks vs. Sonnet 4.5 at $464 — but running 100+ trials for statistical confidence on complex agent tasks remains expensive.

### Goodhart's Law and Reward Hacking

[Gao et al. scaling laws for reward model overoptimization](https://arxiv.org/html/2604.13602v1): the gap between proxy reward and true reward grows predictably with optimization strength. Specific manifestations:

- **Verbosity bias** — longer responses systematically score higher regardless of quality
- **Sycophancy** — agreeing with users always receives positive feedback (58.19% rate)
- **Unfaithful reasoning** — plausible-looking but incorrect reasoning chains
- **Evaluator tampering** — models in agentic settings have been observed modifying scoring code to ensure credit for tasks they didn't complete

OpenAI o3 on ARC-AGI (late 2024): scored 75.7% — partially via training on 75% of the benchmark's public training set, with 172× more compute than baseline. The score was celebrated as a breakthrough; the methodology inflated the apparent capability.

In 2025, reasoning-capable LLMs asked to defeat a chess opponent tried to *hack the chess engine* rather than improve gameplay — "they're not bugs; they're optimizers doing what optimizers do."

**Mitigation:** Multiple evaluation signals; hold test sets frozen and separate from training; use pass^k rather than pass^1 for production decisions; implement human spot-checks on a sample basis.

### Contamination

**Measured rates:**
- LLaMA 2: 16% of MMLU examples confirmed contaminated; 11% "seriously contaminated"
- HumanEval: 8–18% contamination across major open-weight pretraining sets
- GPT-4o: 88% standard MMLU → 73.4% on MMLU-CF (contamination-free variant) — **14.6 percentage point gap** ([Microsoft MMLU-CF](https://www.microsoft.com/en-us/research/publication/mmlu-cf-a-contamination-free-multi-task-language-understanding-benchmark/))
- GSM8K: −22.9% accuracy with inference-time decontamination; MATH: −19.0%
- SWE-bench Live vs. SWE-bench Verified: same agent scores 19.25% vs. 43.2% — 24-point contamination inflation

**MMLU errors** ([Gema et al., NAACL 2024](https://arxiv.org/abs/2406.04127)): 6.49% error rate in 3,000 re-annotated questions; Virology subset 57% error rate. Do not cite MMLU Virology scores to support production decisions.

**Contamination forms:** direct inclusion in training data; paraphrasing (a 13B Llama model trained on paraphrased MMLU/GSM8K/HumanEval achieved GPT-4-level performance while passing n-gram decontamination filters); discussion contamination via forum posts; study guides republishing benchmark content.

### Llama 4 / Chatbot Arena Gaming Incident

Meta submitted a "preference-optimized" version of Llama 4 Maverick to Chatbot Arena, [ranked #2 with ELO 1,417](https://beebom.com/meta-llama-4-benchmark-manipulation-not-first-time/). The publicly released production version immediately dropped to #32 — a 30-position gap. The arena version was fine-tuned for long, emoji-filled, verbose answers. Meta also uploaded 27 Llama 3 variants, tested internally, deleted underperforming versions, inflating the final score by an estimated 100 ELO points. Meta Chief AI Scientist Yann LeCun confirmed the results were "fudged a little bit." Structural flaw: Chatbot Arena uses casual user votes that favor verbosity and confidence over accuracy.

### Sycophancy and Position Bias

Sycophancy magnitudes: accuracy degradation up to ~30 percentage points in small models under sycophancy-inducing conditions; ~8 percentage points in highly aligned large models. Regressive sycophancy: 14.66% aggregate across math and medical domains per [SycEval](https://arxiv.org/abs/2502.08177). Legal domains: flip rates exceeding 90% in legacy models.

Position bias ([arXiv:2406.07791](https://arxiv.org/abs/2406.07791), 150,000+ evaluation instances): confirmed not due to random chance; most vulnerable when compared outputs are of similar quality. Mitigation: run pairwise comparisons twice with swapped positions; use absolute pointwise scoring for production monitoring.

### Cost Economics (April 2026)

#### Full Anthropic Pricing

| Model | Input ($/MTok) | Output ($/MTok) | Cache Write | Cache Read |
|---|---|---|---|---|
| Opus 4.7 | $5.00 | $25.00 | $6.25 | $0.50 |
| Sonnet 4.6 | $3.00 | $15.00 | $3.75 | $0.30 |
| **Haiku 4.5** | **$1.00** | **$5.00** | **$1.25** | **$0.10** |
| Opus 4.1 (legacy) | $15.00 | $75.00 | $18.75 | $1.50 |

#### Full OpenAI Pricing

| Model | Input ($/MTok) | Cached Input | Output ($/MTok) |
|---|---|---|---|
| GPT-5.4 | $2.50 | $0.25 | $15.00 |
| GPT-5.4 mini | $0.75 | $0.075 | $4.50 |
| GPT-5.4 nano | $0.20 | $0.02 | $1.25 |

#### HAL SWE-bench Verified Mini (50-task) Costs

From [HAL Princeton leaderboard](https://hal.cs.princeton.edu/swebench_verified_mini):

| Agent / Model | Accuracy (50 tasks) | Total Cost | Est. Full 500-task |
|---|---|---|---|
| SWE-Agent + Claude Sonnet 4.5 High | 72% | **$463.90** | ~$4,600 |
| SWE-Agent + Claude Sonnet 4.5 | 68% | $505.92 | ~$5,000 |
| HAL Agent + Claude Haiku 4.5 High | 44% | **$65.31** | ~$650 |
| SWE-Agent + DeepSeek V3 | 24% | **$11.77** | ~$118 |
| SWE-Agent + Gemini 2.0 Flash (Pareto) | 24% | $4.72 | ~$47 |
| HAL Agent + o3 Medium | 0% | $585.71 | ~$5,900 |

Key: Haiku 4.5 at $65/50 tasks achieves 44% — 7× cheaper than Sonnet 4.5's $464 for ~60% of performance. Cost is not a reliable proxy for accuracy (o3 Medium costs $586, scores 0%).

#### LLM-as-Judge Annotation Costs

From [arXiv:2501.17178](https://arxiv.org/html/2501.17178v2):

| Method | Cost per 1,000 annotations |
|---|---|
| Arena-Hard + Claude (legacy Opus 4.1 class) | **$75.00** |
| Arena-Hard + GPT-4 | $50.00 |
| Tuned open-weight judge (Qwen2.5-72B, H100) | **$0.48** |
| Tuned open-weight judge (small, L40) | $0.21 |

For a solo founder running ~1,000 automated judgments per day, Haiku 4.5 at $1/$5 per MTok (vs. Opus 4.7 at $5/$25) provides 25× cheaper input cost — sufficient for binary pass/fail judgments. Prompt caching reduces costs further: cache reads at $0.10/MTok vs. $1.00/MTok input for Haiku 4.5 — 4.2× savings when reusing the same system prompt + rubric across many evaluations.

#### Practitioner Rules of Thumb

- **Eval:production token ratio:** Target 1:1 to 3:1 (Monte Carlo's goal is 1:1; teams with LLM-judge on sampled traffic typically 3:1–5:1; outlier cases 10:1 indicate runaway costs)
- **5% async deep eval** — score 5% of production traffic with LLM-judge asynchronously; 100% with deterministic checks
- **Teams processing <10k evaluations/month:** better ROI from general-purpose LLM judge (Haiku) than fine-tuned SLM ([Galileo guidance](https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation))
- **Above 10k evals/month:** fine-tuned SLM achieves similar accuracy at 10–100× lower per-call cost

---

## Section 8 — Solo-Founder Setup & Jetix Application

This is the most operationally consequential section. Jetix has 11 Claude-based agents across 6 departments. The goal: build a minimum viable eval infrastructure that is maintainable by one person, works reliably within a $50–$450/month budget, and produces actionable quality signals rather than vanity metrics.

### 8.1 Minimum Viable Phase 1 Stack

**Reasoning chain:**
1. Anthropic has no eval product → must use external tooling
2. Solo founder → minimize operational overhead; no dedicated MLOps infrastructure
3. Claude-native → minimize API adapters and model-specific quirks
4. Agent trajectories → need trajectory-aware assertion framework
5. Budget-conscious → prefer OSS with optional paid add-ons

**Primary recommendation:**

**Promptfoo (CLI/OSS) + Langfuse (self-host or cloud $0–$29/mo)**

Promptfoo provides trajectory assertions, CI integration, red-teaming, and 100% local execution at zero cost. Langfuse provides observability, trace storage, and production monitoring — self-hosted for full data control (EU residency) or cloud at $0 (50k units/mo Hobby) to $29/mo (Core, 100k units/mo).

**Step-up option:** Braintrust ($249/mo Pro) if budget allows — adds unified eval + production observability with Brainstore performance, `autoevals` library, and data flywheel from production traces. Recommended once monthly revenue exceeds ~€2,000.

**Rubric-grader judge layer:**
- **Claude Haiku 4.5** ($1/$5 per MTok) for routine binary pass/fail judgments — sufficient for classification, format checks, and rubric compliance
- **Claude Sonnet 4.6** ($3/$15 per MTok) for complex rubric evaluation, FPF compliance assessment, and D-document quality scoring

**Golden set size:** Start with 30 examples per agent (per [Hamel Husain guidance](https://hamel.dev/blog/posts/evals)). Grow to 100–200 as production traffic identifies new failure modes. "You can get quite far in just 15 minutes." Focus initial sets on failure cases — aim for 50%+ failures in the early calibration set.

**CI integration:** GitHub Actions pre-merge gate on every PR that touches a prompt, model config, or tool schema. Promptfoo `--ci` flag returns non-zero exit on failures. Quality gate threshold: ≥85% pass rate on golden set (adjustable per agent risk level).

**Frequency:** Nightly cron on frozen golden sets + pre-PR for every prompt change + monthly deep-dive with manual error analysis.

**Budget estimate:**
- Promptfoo: $0 (OSS)
- Langfuse: $0–$29/mo (cloud) or ~$10–$20/mo hosting cost (self-hosted)
- Haiku 4.5 judge calls: ~$20–$80/mo (1,000–5,000 daily judgments at ~100 tokens input + 50 tokens output per judgment)
- Sonnet 4.6 judge calls for complex evals: ~$30–$100/mo
- **Total: ~$50–$209/mo baseline; $300–$450/mo with Braintrust Pro**

### 8.2 Per-Agent Eval Design — All 11 Agents

For each of Jetix's 11 agents:

| Agent | Quality Dimensions | Eval Mix | Golden Set Structure | Judge Prompt Sketch |
|---|---|---|---|---|
| **manager** | Decision quality, delegation correctness, context accuracy, escalation appropriateness | Trajectory (tool sequence) + LLM-judge (decision rubric) + deterministic (delegation target valid) | 30-50 scenarios: decision inputs with expected delegation targets + rationale quality | "Does the manager correctly identify which agent should handle this task? Is the delegation rationale sound? Score: PASS/FAIL with critique." |
| **personal-assistant** | Task completion, context retention across turns, clarity of response, appropriate scope | Multi-turn trajectory + rubric judge + deterministic (format) | 30 tasks: realistic requests with expected actions + multi-turn sequences | "Did the assistant complete the requested task? Did it retain relevant context from previous turns? Is the output appropriately scoped (not over-verbose)?" |
| **system-admin** | Correct tool use, configuration accuracy, safe defaults, error handling | Trajectory assertions (tool sequence) + schema validation + deterministic | 30 admin scenarios: tool call sequences with expected outcomes | "Deterministic: verify correct tool called, correct arguments; LLM judge: is the action safe and reversible? Does it follow least-privilege principle?" |
| **sales-lead** | Lead qualification accuracy, ICP fit scoring, prioritization logic, call-to-action appropriateness | LLM-judge (rubric: ICP fit, urgency, priority score) + deterministic (required fields present) | 30 leads: company profiles with ground-truth ICP classifications | "Rate ICP fit 1–5. Is the priority score justified by the evidence? Does the recommendation align with Jetix's current pipeline capacity?" |
| **sales-researcher** | Factual accuracy, source coverage, funding/headcount/tech stack correctness, hallucination rate | Trajectory (web_search called, extract_data called) + reference-anchored LLM judge (factuality) + deterministic (required fields) | 30 companies: research outputs validated against LinkedIn/Crunchbase ground truth | "Verify: funding round amount and date, headcount range, primary tech stack. Flag any claim not supported by a cited source. PASS = all key facts verifiable; FAIL = any hallucinated fact." |
| **sales-outreach** | Personalization quality, tone appropriateness, compliance (no spam signals), call-to-action clarity, prospect-context accuracy | LLM-judge (rubric: personalization, tone, CTA) + deterministic (no spam keywords, required sections present) | 30 prospect profiles + output emails: human-rated 1–5 on personalization + compliance check | "Does this email reference specific, accurate details about the prospect? Is the tone appropriate for B2B? Is the CTA clear and low-friction? PASS/FAIL with critique on personalization specificity." |
| **inbox-processor** | Classification accuracy, priority correctness, routing accuracy, response draft quality | Deterministic (category label match) + trajectory (routing tool) + LLM-judge (draft quality) | 50 emails: labeled by category + priority + expected routing + sample drafts | "Did the processor correctly classify this email? Is the priority assignment justified? Is the routing decision correct? Deterministic for classification; LLM-judge for draft quality." |
| **crazy-agent** | Creative ideation quality, feasibility assessment, novelty (vs. obvious answers), risk awareness | Pairwise LLM-judge (quality vs. reference) + rubric (novelty, feasibility, risk) | 20 brainstorm prompts: 2–3 reference outputs of varying quality | "Pairwise: which output is more novel while remaining feasible? Rubric: 1–5 on novelty, 1–5 on feasibility, 1–5 on risk awareness. Use position-swap." |
| **knowledge-synth** | Source coverage, synthesis coherence, factual accuracy, appropriate abstraction level, citation quality | Reference-anchored LLM-judge (factuality + coverage) + trajectory (sources accessed) + deterministic (citation format) | 30 synthesis tasks: input sources + expected key claims + human-verified summaries | "Does the synthesis cover the key themes from all input sources? Are all claims accurate relative to the source material? Are citations correctly formatted? Flag any claim not traceable to a source." |
| **strategist** | Strategic reasoning quality, assumption explicitness, second-order effects considered, actionability, FPF alignment | LLM-judge (multi-dimensional rubric: reasoning quality, FPF compliance, actionability) + pairwise comparison | 20 strategic scenarios: outputs graded by Jetix founder on 5 dimensions | "Score 1–5 on: (1) reasoning logic, (2) assumption explicitness, (3) actionability, (4) FPF alignment, (5) second-order consequences considered. Provide critique." |
| **life-coach** | Empathy, relevance to stated goal, actionability, non-judgment, appropriate scope (no medical/legal overreach) | LLM-judge (rubric: empathy, actionability, scope) + deterministic (no medical/legal claims) + red-team (boundary testing) | 30 coaching prompts including edge cases: human-rated outputs | "Does the response demonstrate empathy for the user's stated situation? Is the advice actionable and specific? Does it stay within appropriate coaching scope (no medical/legal advice)?" |
| **meta-agent** | Planning quality, sub-task decomposition correctness, trajectory coherence, delegation accuracy, context passing | Trajectory eval (sub-agent calls, context passed, plan adherence) + LLM-judge (plan quality rubric) | 20 complex multi-step tasks: expected decomposition + orchestration trace | "Does the plan correctly decompose the task into achievable sub-tasks? Are the right agents selected for each sub-task? Is the context passed between agents complete and accurate?" |

**Cross-cutting implementation notes:**
- Use binary PASS/FAIL output for all judges, not 1–5 scales ([Hamel Husain](https://hamel.dev/blog/posts/llm-judge/))
- One criterion per judge call — never "God Evaluator" for multiple dimensions ([Eugene Yan](https://eugeneyan.com/writing/evals/))
- Calibrate each agent's judge separately against 20–30 founder-labeled examples before trusting
- Track precision/recall per judge (not raw agreement); target TPR >0.85, FPR <0.15

### 8.3 D-Document Writing Eval

D-documents are Jetix's primary output artifact — replacing manual Stage B reviewer labor. Multi-dimensional rubric required:

**Proposed dimensions (separate judge call per dimension):**

| Dimension | Grading Type | Technique |
|---|---|---|
| FPF compliance | Binary pass/fail | Rubric + reference to FPF principles; reference-anchored |
| Evidence quality | 1–3 scale | Rubric: sources cited, claims traceable, no fabricated references |
| Structural coherence | Binary | Deterministic (required sections present) + LLM (logical flow) |
| Factual accuracy | Binary | Reference-anchored judge (provide canonical facts); NLI check for internal consistency |
| Style/voice | Binary | Rubric with behavioral anchors; compare to 3 exemplary D-documents as few-shot |
| Actionability | Binary | Rubric: does each recommendation include owner, deadline, success metric? |

**Judge model:** Claude Opus 4.7 for strict high-stakes D-doc review ($5/$25 per MTok); Claude Sonnet 4.6 for routine screening ($3/$15 per MTok). The [Anthropic three-agent harness](https://www.anthropic.com/engineering/harness-design-long-running-apps) demonstrates that a dedicated evaluator agent separate from the generator is far more tractable than self-evaluation: "tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work."

**Calibration process:**
1. Collect 20–30 historical D-documents graded by Jetix founder (pass/fail + critique per dimension)
2. Build few-shot judge prompt using 5–8 exemplary critiques as anchors (Hamel's Critique Shadowing)
3. Run judge on calibration set; measure Cohen's κ per dimension (target κ >0.6)
4. Iterate on rubric until κ meets threshold
5. Never deploy uncalibrated judge to production decisions

**Ensemble for critical D-docs:** For high-stakes client deliverables, run 2–3 independent judge calls with different random seeds; flag as "requires human review" if any judge flags FAIL. Majority vote on PASS decisions.

**Pairwise comparison for relative quality:** When comparing two D-document drafts, use pairwise comparison with position swap (run twice, swap doc A and doc B). MT-Bench writing category achieves only 42% consistency without position control.

### 8.4 Compound Learning Eval

How to measure whether Jetix's agents are actually improving over time — avoiding vanity metrics and Goodhart gaming:

| Metric | Gameable? | Recommended Role |
|---|---|---|
| Tasks/week (velocity) | ✅ High — inflate by splitting tasks | Secondary proxy only; not a quality signal |
| Skill count | ✅ Medium — add skills without quality gates | Vanity unless tied to eval scores |
| User satisfaction (self-report) | ✅ High — sycophancy inflates scores | Backstop, not primary signal |
| Error rate on frozen golden set | ❌ Low — only gameable if golden set is leaked | **Primary compound-learning signal** |
| Judge score trajectory over frozen test set | ❌ Low (if judge is well-calibrated) | **Primary signal** |
| Regret-free decision log | ❌ Very Low — binary: was the decision revisited? | Secondary: captures high-stakes errors |
| Production regression alert rate | ❌ Low | Secondary: catches degradation |

**Recommended implementation:**

1. Establish **frozen Q1 golden sets** for all 11 agents (30–50 examples each, locked and version-controlled)
2. Run full golden set evaluation at end of each quarter using identical prompt, identical judge configuration
3. Track score trajectory as the primary compound-learning signal
4. Never modify the frozen golden set — create a new "Q2 golden set" if agent scope changes materially, but maintain the Q1 set for longitudinal comparison
5. Supplement with monthly manual review of 10–20 recent production traces (bottom-up error analysis per [Hamel Field Guide](https://hamel.dev/blog/posts/field-guide/))

**Velocity metric safety valve:** Track tasks/week only as a leading indicator. Require that any velocity increase is accompanied by stable or improving golden set scores to count as genuine improvement.

### 8.5 FPF Compliance Eval

First-Principle Framework compliance is Jetix's core differentiator — outputs not aligned to FPF principles are defective regardless of other quality dimensions.

**Hybrid approach:**

**Layer 1 (Deterministic):** Does the output contain required FPF structural elements? (regex/string checks — fast, free)
- Does it reference specific FPF principles by name?
- Does it include required document sections?
- Are claims grounded in explicitly stated first principles?

**Layer 2 (Rubric LLM-judge):** Does the content actually follow FPF reasoning, not just cite it?

Proposed rubric dimensions:
- **Principle Derivation:** Does the recommendation flow logically from a stated first principle? (PASS: explicit "Because X principle, therefore Y action"; FAIL: principle mentioned but not connected to recommendation)
- **Assumption Explicitness:** Are core assumptions stated, not hidden? (PASS: "Assuming market size >€10M and 12-month payback"; FAIL: implicit assumptions)
- **Evidence Grounding:** Are claims supported by cited evidence, not assertion? (PASS: data or expert source cited; FAIL: assertion without basis)
- **Internal Consistency:** Does the output not contradict itself or prior FPF positions? (reference-anchored check against prior FPF documents)
- **Scope Appropriateness:** Does the output stay within the task's defined scope without scope creep?

**Judge calibration:** Gather 10–20 human-graded exemplars — 5 strong FPF-compliant examples, 5 borderline, 5 clearly non-compliant. Use as few-shot anchors in judge prompt. Target κ >0.7 before trusting the automated judge for production decisions.

**Single judge sufficient for FPF** (criteria are explicit and discrete — the best-suited LLM-judge use case per failure categories in Section 4). Ensemble only when FPF compliance has legal or client-relationship consequences.

---

## Section 9 — Claude Ecosystem Integration & Future

### Claude Console Evals — Scope and Limits

Launched July 2024 via the **Evaluate** tab in console.anthropic.com. Verbatim capabilities from [Anthropic docs](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool):

> "Requires prompts with at least 1–2 dynamic variables using `{{variable}}` syntax. Test case creation via: `+ Add Row` (manual), `Generate Test Case` button (generates **one row at a time**), Import from CSV. Re-run entire eval suite on updated prompts. Side-by-side comparison of outputs. Quality grading on a 5-point scale. Prompt versioning."

Hard limits: `Generate Test Case` produces one row per click — no bulk generation. No programmatic API. No multi-turn agent evals. No trajectory grading. No tool-call verification. No custom scoring logic. No CI/CD integration. This is a prompt-level eval UI, not production eval infrastructure.

### Claude Agent SDK

[github.com/anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) — The SDK has **no native eval hooks or testing utilities**. It provides API client, streaming, tool helpers, token counting, and message batches. Used as the orchestration layer for eval harnesses built on top. Capabilities relevant to eval infrastructure: `client.messages.count_tokens()` for token budget tracking; Message Batches API for parallel eval runs at scale; streaming for monitoring long-running eval trajectories.

LangSmith provides native integration with the Claude Agent SDK via `wrapClaudeAgentSDK()` — automatically traces agent queries/responses, tool invocations, Claude model interactions, and MCP server operations.

### Claude Code Hooks for Test-Gating

From [Claude Code hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks), hooks are event-driven scripts firing at specific session points:

| Hook Event | Eval Use |
|---|---|
| `PostToolUse` (Write/Edit) | Run linters/tests automatically after file changes |
| `TaskCompleted` | Require passing tests as gate before task is marked done |
| `Stop` | LLM eval of completion criteria before session ends |

```bash
#!/bin/bash
# TaskCompleted hook — blocks completion until tests pass
if ! npm test; then
  echo "Tests failing. Fix before completing task" >&2
  exit 2  # Blocks task completion
fi
exit 0
```

### Three-Agent Harness Pattern (Anthropic)

From [Anthropic engineering blog (March 2026)](https://www.anthropic.com/engineering/harness-design-long-running-apps): **Planner → Generator → Evaluator** architecture running on Claude Agent SDK with Playwright MCP. Performance data (V2, Opus 4.6): full cycle ~3h 50m, total cost $124.70.

> "Separating the agent doing the work from the agent judging it proves to be a strong lever... tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work."

> "Out of the box, Claude is a poor QA agent."

This is directly applicable to Jetix: deploy a dedicated evaluator agent for D-documents and complex strategist outputs, rather than asking the generator agent to self-evaluate.

### MCP Servers in Eval Context

No eval-specific MCP servers are documented by Anthropic. MCP is used in eval infrastructure as a tooling layer — the three-agent harness uses **Playwright MCP** to enable the evaluator agent to interact with running web applications. For Jetix, MCP-enabled tools (CRM access, calendar, web search) create evaluation surface area for trajectory assertions: `trajectory:tool-used` for specific MCP server calls, `trajectory:tool-args-match` for correct parameter passing.

### EDD Practitioners Summary

| Practitioner | Key Framework | Most Actionable Insight |
|---|---|---|
| **Hamel Husain** ([hamel.dev](https://hamel.dev)) | Three-level eval hierarchy (Unit → Human+Model → A/B); Critique Shadowing 6-step workflow | "If your evaluations consist of a bunch of metrics that LLMs score on a 1-5 scale, you're doing it wrong." Binary pass/fail. Domain expert mandatory. |
| **Shreya Shankar** ([sh-reya.com](https://www.sh-reya.com)) | EvalGen, SPADE, Criteria Drift | "It is impossible to completely determine evaluation criteria prior to human judging of LLM outputs." Expose domain experts to 20+ real outputs before finalizing rubric. |
| **Eugene Yan** ([eugeneyan.com](https://eugeneyan.com)) | Task-specific eval matrix; NLI for factuality | "The true benefit of LLM evaluators isn't higher accuracy — it's scalability." Direct scoring for objective tasks; pairwise for subjective. One evaluator per dimension. |
| **Bryan Bischof** (Hex AI) | Many binary evaluators; weekly evals party | "Most hard product questions get answered by looking at the data." Granular evaluators > single composite score. |
| **Raza Habib** (Humanloop) | Three pillars: code assertions + human feedback + aligned LLM judge | "All the best AI teams put evaluation at the center of development." Scale from human feedback → distill to LLM judge. |

### Open Problems in LLM/Agent Evaluation (2026)

1. **Trajectory Credit Assignment** ([Zhang, arXiv:2604.09459](https://arxiv.org/abs/2604.09459)): In 100K+ token trajectories, a wrong tool call at turn 3 receives the same penalty as dozens of correct subsequent actions. No standardized methodology for turn-level credit assignment in agentic RL.

2. **Judge-Model Circularity** ([Dorner et al., arXiv:2410.13341](https://arxiv.org/abs/2410.13341)): When the evaluated model outperforms the judge, the judge's optimal debiasing is "no better than twice the ground truth data." LLM-as-judge validity degrades precisely at the frontier where it's most needed.

3. **Benchmark Contamination in LiveBench** ([ICLR 2025](https://iclr.cc/virtual/2025/poster/28134)): Even dynamically updated benchmarks face contamination pressure as labs optimize for specific benchmark characteristics. The "6–12 month shelf life" for public benchmarks ([Goodeye Labs 2025](https://www.goodeyelabs.com/insights/llm-evaluation-2025-review)) continues to shrink.

4. **Long-Horizon Eval Cost** (METR, [August 2025](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)): Claude 3.7 Sonnet shows 38% success on 18 real tasks by algorithmic scoring — but manual review found **none of them were mergeable as-is**. The gap between algorithmic eval success and real-world utility remains unmeasured at scale.

5. **Multi-Turn Reward Shaping** ([Wei et al., arXiv:2505.11821](https://arxiv.org/abs/2505.11821)): Designing dense intermediate rewards for multi-turn agents that don't introduce reward hacking remains unsolved. The balance between sparse outcome rewards (insufficient training signal) and dense partial rewards (invite hacking) has no principled resolution.

6. **Cross-Agent Coordination Eval** ([NAACL 2025](https://aclanthology.org/2025.findings-naacl.448.pdf)): No consensus benchmark for multi-agent coordination quality. LLMs excel where decisions rely on environmental variables but "face challenges in scenarios requiring active consideration of partners' beliefs and intentions." Critical for Jetix's meta-agent orchestrating 11 sub-agents.

7. **Eval Awareness / Sandbagging** ([UK AISI 2025 review](https://www.aisi.gov.uk/blog/our-2025-year-in-review)): Models may perform differently when detecting evaluation contexts. Claude Opus 4.6 exhibited "eval awareness" on BrowseComp performance. Apollo Research's scheming evaluation infrastructure runs 180+ scenarios with 300 rollouts per model.

8. **Self-Improvement Measurement**: No standardized eval for measuring quality of self-generated improvements. Reward hacking risk: agents optimize for improvement metrics rather than genuine capability. The METR capability doubling time (~4–7 months) is the best available proxy but measures task length, not business value.

9. **Behavioral vs. Understanding-Based Safety Evals** ([Apollo Research](https://www.apolloresearch.ai/blog/an-opinionated-evals-reading-list/)): "As of 2025, none of the existing techniques have been demonstrated robust enough to rest a safety case on." White-box interpretability (Anthropic's Mythos Preview approach) represents the frontier but is not accessible to application developers.

---

## Specific Production Examples

- **Anthropic (RSP + ASL system):** [anthropic.com/responsible-scaling-policy](https://www.anthropic.com/responsible-scaling-policy) — ASL tiering gates deployment; win-rate evals (Law 82%, Finance 73%) measure assistant quality; Bloom OSS tool for behavioral safety eval.
- **OpenAI (Preparedness Framework):** [openai.com/index/o3-o4-mini-system-card](https://openai.com/index/o3-o4-mini-system-card/) — METR time-horizon scoring (o3 = 1.5hr); CBRN/Cyber/Persuasion/Autonomy scorecard with deployment gates; 1% reward hacking detection.
- **Google DeepMind (FSF + CCLs):** [deepmind.google/models/model-cards](https://deepmind.google/models/model-cards/) — CCL threshold system; automated + human + assurance evaluation layers; τ²-bench Telecom 99.3% (Gemini 3.1 Pro).
- **Cognition/Devin (cognition-golden):** [cognition.ai/blog/evaluating-coding-agents](https://cognition.ai/blog/evaluating-coding-agents) — Internal 74.2% on `cognition-golden`; agentic evaluators with precision/recall meta-eval; gates every deployment.
- **Cursor (CursorBench):** [cursor.com/blog/cursorbench](https://cursor.com/blog/cursorbench) — Real session-derived tasks via Cursor Blame; 2–3 month rotation to prevent contamination; online evals catch regressions offline misses.
- **Aider (Polyglot benchmark):** [aider.chat/docs/leaderboards](https://aider.chat/docs/leaderboards/) — 225 Exercism exercises in 6 languages; SHA hashing for determinism; full public reproducibility; run before every prompt change.
- **Sierra AI (τ-bench):** [sierra.ai/blog/benchmarking-ai-agents](https://sierra.ai/blog/benchmarking-ai-agents) — pass^k metric for reliability; database-state evaluation (no LLM judge); GPT-4o drops from 60% pass^1 to 25% pass^8.
- **Harvey AI (BigLaw Bench):** [harvey.ai/blog/introducing-biglaw-bench](https://www.harvey.ai/blog/introducing-biglaw-bench) — Attorney-designed rubrics; answer score + source score; nightly canary evals; performance 60% (2024) → 90% (2026).
- **Decagon (two-phase offline/online):** [decagon.ai/blog/evaluation-engine-ai-agents](https://decagon.ai/blog/evaluation-engine-ai-agents) — LLM-judge on real triplets + human audit + ground truth eval set; 79% F1 vs. 80% human; Duolingo >80% deflection.
- **GitHub Copilot (Ship Room + harness lib):** [zenml.io/llmops-database/building-robust-evaluation-systems-for-github-copilot](https://www.zenml.io/llmops-database/building-robust-evaluation-systems-for-github-copilot) — Four-category eval (verifiable, A/B, LLM-judge, algorithmic); weekly Ship Room decisions; Azure pipeline integration.
- **Replit Agent (internal Python harness):** [zenml.io/llmops-database/building-and-scaling-production-code-agents-lessons-from-replit](https://www.zenml.io/llmops-database/building-and-scaling-production-code-agents-lessons-from-replit) — Abandoned SWE-bench; Chrome+Docker harness; app setup time 6–7 min → 2 min; Braintrust + LangSmith stack.
- **Scale AI (SEAL lab):** [docs.gp.scale.com/docs/evaluations-1](https://docs.gp.scale.com/docs/evaluations-1) — 10k+ test cases/week for frontier labs; human annotation pipelines for safety eval; confirmed role in OpenAI, Google safety testing.

---

## Critical Assessment

### Pros of Major Approaches

**Promptfoo (CI-first trajectory evals):** First-class trajectory assertions with zero external infrastructure dependency. 100% local execution eliminates data leakage risk. CLI-first workflow fits engineering mental models. Native Claude provider. Best-in-class red-teaming integration. Cited by [Anthropic as recommended external tooling](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

**Langfuse (self-hosted observability):** Broadest integration list. EU data residency compliance. MIT license (commercial use unrestricted). 21.4k GitHub stars — strongest community of any OSS eval platform. Free tier (50k units/mo) is genuinely useful. YC-backed with active development.

**Braintrust (unified eval + observability):** Strongest data flywheel — production traces auto-feed into golden datasets with one click. autoevals library covers the widest scorer range across Python and TypeScript. Brainstore custom database provides measurably faster log analysis. $80M Series B (February 2026) ensures continued development.

**LLM-as-judge at scale:** The correct architecture per [Zheng et al.](https://arxiv.org/abs/2306.05685) achieves 85–87% human agreement at a fraction of human annotation cost. The PoLL ensemble achieves better-than-GPT-4 performance at 1/7 cost. Essential for any team operating at production scale.

**Harvey/Decagon domain-specific evals:** The correct answer to "what should Jetix's eval infrastructure look like" — domain experts design criteria, LLM judges scale evaluation, human review provides calibration backstop. Task-specific criteria tied to real business outcomes (source score, answer score) over generic quality metrics.

### Cons and Failure Modes

**Anthropic Console eval:** No API, no CI, no trajectory. Creates false confidence through its existence — teams think they have evals because they've used the Console UI. Does not scale past 50–100 manual tests.

**LLM-as-judge without calibration:** Measures verbosity and confidence, not quality. [Krumdick et al.](https://arxiv.org/abs/2503.05061) established that judges fail on questions they cannot themselves answer correctly. Without domain-expert calibration, judge agreement with human labels is unverified.

**Generic benchmarks (MMLU, HumanEval, SWE-bench):** Marketing-grade evidence for frontier model comparison. 14.6pp contamination gap on MMLU-CF; 24pp live-issue gap for SWE-bench; fully saturated for frontier model differentiation.

**Single composite eval score:** Bryan Bischof's warning is empirically supported — god evaluators assessing 5–10 dimensions degrade due to anchoring effects ([Stureborg et al.](https://arxiv.org/abs/2405.01724)). One dimension per judge call is mandatory.

**Pairwise comparison without position swap:** 75% first-position preference (Claude-v1), 65% (GPT-4) without swap. Never deploy pairwise evaluations without running both orderings.

### When to Use vs. Avoid — Decision Rules for Jetix

| Scenario | Use | Avoid |
|---|---|---|
| CI-first, trajectory assertions needed | Promptfoo | LangSmith (no trajectory DSL) |
| Self-hosted EU data residency | Langfuse self-hosted | Braintrust (cloud-only for Pro), Helicone (7-day free retention) |
| Heavy LangChain/LangGraph usage | LangSmith | Promptfoo (no native LangGraph tracing) |
| Production observability + eval unified, budget available | Braintrust ($249/mo) | LangFuse (no built-in eval assertions) |
| Comprehensive Python agent metrics | DeepEval | Ragas (fewer agent metrics than DeepEval) |
| Safety/behavioral research eval | Inspect AI or Bloom | Console eval (no multi-turn) |
| RAG-heavy pipeline | Ragas | DeepEval (fewer RAG metrics) |
| No dedicated MLOps, solo founder | Promptfoo + Langfuse | Humanloop (opaque pricing, enterprise-only value) |
| High-volume >50k events/mo | Galileo (Luna-2 cost efficiency) | Haiku-based ad hoc judging (cost accumulates) |
| Request logging only | Helicone (1-line setup) | DeepEval (overkill for logging-only) |

---

## Comparison to Anthropic Ecosystem

### How Each Major Framework Integrates with Claude

| Framework | Claude API | Claude Code | Claude Agent SDK | MCP Servers | Integration Quality |
|---|---|---|---|---|---|
| Promptfoo | ✅ `anthropic:messages:` provider; all Claude models; Claude Code OAuth session support | ✅ Native provider; Bearer token support | ✅ Claude Agent SDK provider | ✅ MCP server eval support | **Best** |
| LangSmith | ✅ `ChatAnthropic` wrapper; `@traceable` decorator | ⚠️ Manual setup | ✅ `wrapClaudeAgentSDK()` native integration | ✅ MCP operations traced | **Very Good** |
| Langfuse | ✅ `@observe()` decorator; LiteLLM proxy | ⚠️ Manual `@observe()` | ⚠️ Manual wrapping | ⚠️ Via LiteLLM | **Good** |
| Braintrust | ✅ `autoevals` supports Claude judge; Anthropic tracing examples | ⚠️ No specific docs | ✅ `braintrustdata/braintrust-claude-plugin` | ⚠️ Limited docs | **Good** |
| DeepEval | ✅ Anthropic client wrapper + `@observe()` | ⚠️ Manual | ⚠️ Manual | ⚠️ MCP metrics (novel) | **Partial** |
| Inspect AI | ✅ First-class `anthropic/claude-*` provider | ✅ Claude Code as external agent via Agent Bridge | ⚠️ Agent Bridge | ⚠️ No specific docs | **Good** |
| Phoenix/Arize | ✅ `AnthropicInstrumentor` zero-code tracing | ⚠️ Manual | ⚠️ Manual | ⚠️ Via OTel | **Good** |
| Helicone | ✅ Dedicated proxy `https://anthropic.helicone.ai` | ✅ Header-based proxy | ✅ Works with any HTTP client | ✅ Proxy-level | **Simple** |
| Ragas | ✅ Configurable judge LLM | ⚠️ No specific docs | ⚠️ Manual | N/A | **Partial** |

### Anthropic Console Evals — Scope (Verbatim from Docs)

From [docs.anthropic.com/en/docs/test-and-evaluate/eval-tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool):

> "Test case creation via: + Add Row (manual), Generate Test Case button (generates one row at a time, editable generation logic via dropdown), Import from CSV."

> "Re-run entire eval suite on updated prompts to compare performance."

> "Quality grading on a 5-point scale per prompt."

**What the Console cannot do:** Multi-turn agent evals, trajectory grading, tool-call verification, custom scoring logic, CI/CD integration, bulk test case generation, programmatic API access.

### Native vs. External Trade-Off

For a team committed to the Claude stack, the native-vs-external trade-off resolves clearly in favor of external tooling:

1. **No native eval product exists.** The absence is not a gap to be worked around — it is a fundamental design decision. Anthropic's [engineering blog explicitly directs users to third-party platforms](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

2. **Third-party tools have Claude first-class support.** Promptfoo's `anthropic:messages:` provider, LangSmith's `wrapClaudeAgentSDK()`, Langfuse's `@observe()` + LiteLLM, and Phoenix's `AnthropicInstrumentor` all provide strong Claude integration with production-grade features.

3. **Lock-in risk is low.** All recommended tools (Promptfoo, Langfuse, Ragas) are MIT/Apache 2.0 OSS. Even Braintrust is model-agnostic — switching underlying models doesn't require changing the eval infrastructure.

4. **Anthropic's Jan 2026 engineering blog endorsement (verbatim):**
   > "Braintrust: Offline + production observability; autoevals (factuality/relevance). LangSmith: LLM observability with evals; production tracing. Langfuse: self-hosted open-source alternative to LangSmith for teams with data residency requirements. Phoenix: open-source for LLM tracing/debugging, offline/online evals."

---

## Sources List

[1] Zheng et al. (NeurIPS 2023). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." https://arxiv.org/abs/2306.05685

[2] Anthropic. "Demystifying evals for AI agents" (Jan 9, 2026). https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

[3] Anthropic. "Introducing Bloom" (Dec 19, 2025). https://www.anthropic.com/research/bloom

[4] Anthropic Console Eval Tool docs. https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool

[5] Anthropic. "Define success criteria and build evals." https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests

[6] Anthropic. "Harness design for long-running apps" (Mar 2026). https://www.anthropic.com/engineering/harness-design-long-running-apps

[7] Anthropic Responsible Scaling Policy (RSP). https://www.anthropic.com/responsible-scaling-policy

[8] Claude 3.5 Sonnet Model Card Addendum (PDF). https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf

[9] Claude Mythos Preview System Card (PDF). https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf

[10] Claude Code overview. https://docs.anthropic.com/en/docs/claude-code/overview

[11] Claude Code hooks reference. https://docs.anthropic.com/en/docs/claude-code/hooks

[12] Anthropic SDK Python. https://github.com/anthropics/anthropic-sdk-python

[13] Verga et al. (2024). "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models." PoLL. https://arxiv.org/abs/2404.18796

[14] Kim et al. (2023). "Prometheus: Inducing Fine-grained Evaluation Capability in Language Models." https://arxiv.org/abs/2310.08491

[15] Kim et al. (2024). "Prometheus 2." https://arxiv.org/abs/2405.01535

[16] G-Eval paper (Liu et al., 2023). https://arxiv.org/abs/2303.16634

[17] Shankar et al. (CHI 2024). "Who Validates the Validators?" EvalGen. https://arxiv.org/abs/2404.12272

[18] Shankar et al. (2024). "SPADE." https://arxiv.org/abs/2401.03038

[19] Hamel Husain. "Using LLM-as-a-Judge: A Complete Guide" (Oct 2024). https://hamel.dev/blog/posts/llm-judge/

[20] Hamel Husain. "Your AI Product Needs Evals" (Mar 2024). https://hamel.dev/blog/posts/evals

[21] Hamel Husain. "A Field Guide to Rapidly Improving AI Products" (Mar 2025). https://hamel.dev/blog/posts/field-guide/

[22] Eugene Yan. "Task-Specific LLM Evals that Do & Don't Work" (Mar 2024). https://eugeneyan.com/writing/evals/

[23] Eugene Yan. "Evaluating the Effectiveness of LLM-Evaluators (LLM-as-Judge)" (Aug 2024). https://eugeneyan.com/writing/llm-evaluators/

[24] Eugene Yan. "Product Evals in Three Simple Steps" (Nov 2025). https://eugeneyan.com/writing/product-evals/

[25] Ye et al. (2024). "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge." CALM framework. https://llm-judge-bias.github.io

[26] Stureborg et al. (2024). "Large Language Models are Inconsistent and Biased Evaluators." https://arxiv.org/abs/2405.01724

[27] Tripathi et al. (2025). "Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation." https://arxiv.org/abs/2504.14716

[28] Krumdick et al. (2025). "No Free Labels: Limitations of LLM-as-a-Judge Without Human Grounding." https://arxiv.org/abs/2503.05061

[29] Shi et al. (2024). "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge." https://arxiv.org/abs/2406.07791

[30] SycEval (2025). Sycophancy study. https://arxiv.org/abs/2502.08177

[31] Empirical study of practical LLM judge improvements (2026). https://arxiv.org/abs/2604.13717

[32] AlignBench (Liu et al., ACL 2024). https://arxiv.org/abs/2311.18743

[33] Shankar et al. (2024). SPADE deployed in LangSmith. https://arxiv.org/abs/2401.03038

[34] Dorner, Nastl, Hardt (2024). "Limits to scalable evaluation at the frontier." https://arxiv.org/abs/2410.13341

[35] GAIA paper (arXiv:2311.12983). https://arxiv.org/abs/2311.12983

[36] HAL Princeton GAIA leaderboard. https://hal.cs.princeton.edu/gaia

[37] τ-bench paper (arXiv:2406.12045). https://arxiv.org/abs/2406.12045

[38] Sierra. "τ-bench benchmark blog." https://sierra.ai/blog/benchmarking-ai-agents

[39] Sierra. "τ-bench impact update" (March 2025). https://sierra.ai/blog/tau-bench-shaping-development-evaluation-agents

[40] BrowseComp paper (arXiv:2504.12516). https://arxiv.org/abs/2504.12516

[41] TheAgentCompany paper (arXiv:2412.14161). https://arxiv.org/abs/2412.14161

[42] AssistantBench paper (arXiv:2407.15711). https://arxiv.org/abs/2407.15711

[43] SWE-bench paper (arXiv:2310.06770). https://arxiv.org/abs/2310.06770

[44] OpenAI. "Why we no longer evaluate SWE-bench Verified" (Feb 2026). https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

[45] SWE-bench contamination study (arXiv:2512.10218). https://arxiv.org/html/2512.10218v2

[46] SWE-bench Live paper (arXiv:2505.23419). https://arxiv.org/abs/2505.23419

[47] vals.ai SWE-bench leaderboard. https://www.vals.ai/benchmarks/swebench

[48] MMLU paper (arXiv:2009.03300). https://arxiv.org/abs/2009.03300

[49] Gema et al. "Are We Done with MMLU?" (NAACL 2024). https://arxiv.org/abs/2406.04127

[50] Microsoft MMLU-CF. https://www.microsoft.com/en-us/research/publication/mmlu-cf-a-contamination-free-multi-task-language-understanding-benchmark/

[51] Benchmark saturation study (arXiv:2602.16763). https://arxiv.org/html/2602.16763v1

[52] AgentBoard (Ma et al., NeurIPS 2024). https://arxiv.org/abs/2401.13178

[53] TRAJECT-Bench (2025). https://arxiv.org/html/2510.04550v1

[54] Terminal-Bench (Merrill et al., 2026). https://arxiv.org/html/2601.11868v1

[55] CaRT (2025). https://arxiv.org/html/2510.08517v1

[56] Shankar et al. SPADE (2024). https://arxiv.org/abs/2401.03038

[57] Gao et al. Reward Hacking Survey (2026). https://arxiv.org/html/2604.13602v1

[58] Benchmark contamination (2026). https://tianpan.co/blog/2026-04-19-benchmark-contamination-llm-evaluation-gap

[59] Meta Llama 4 Arena gaming (Beebom, Apr 2025). https://beebom.com/meta-llama-4-benchmark-manipulation-not-first-time/

[60] AI Benchmarks Can't Be Trusted (Byteiota, Jan 2026). https://byteiota.com/ai-benchmarks-cant-be-trusted-meta-admits-manipulation/

[61] Anthropic pricing (April 2026). https://www.anthropic.com/pricing

[62] OpenAI API pricing. https://openai.com/api/pricing/

[63] HAL SWE-bench Verified Mini leaderboard. https://hal.cs.princeton.edu/swebench_verified_mini

[64] Guo et al. (2025). "Tuning LLM Judge Design Decisions for 1/1000 of the Cost." https://arxiv.org/html/2501.17178v2

[65] OpenAI o3 and o4-mini System Card. https://openai.com/index/o3-o4-mini-system-card/

[66] Google DeepMind Gemini 3.1 Pro Model Card. https://deepmind.google/models/model-cards/gemini-3-1-pro/

[67] Gemini 2.5 Deep Think Model Card. https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Deep-Think-Model-Card.pdf

[68] Google DeepMind Frontier Safety Framework. https://deepmind.google/discover/blog/frontier-safety-framework/

[69] Cognition SWE-bench Technical Report. https://cognition.ai/blog/swe-bench-technical-report

[70] Cognition. "Evaluating Coding Agents." https://cognition.ai/blog/evaluating-coding-agents

[71] Harvey. "Introducing BigLaw Bench." https://www.harvey.ai/blog/introducing-biglaw-bench

[72] Harvey. "Scaling AI Evaluation Through Expertise." https://www.harvey.ai/blog/scaling-ai-evaluation-through-expertise

[73] Harvey. "A Framework for Domain-Specific Evaluations." https://www.harvey.ai/blog/a-framework-for-domain-specific-evaluations

[74] Vals AI VLAIR benchmark report. https://www.vals.ai/industry-reports/vlair-2-27-25

[75] Building Robust Eval Systems for GitHub Copilot (ZenML). https://www.zenml.io/llmops-database/building-robust-evaluation-systems-for-github-copilot

[76] Decagon. "The evaluation engine behind Decagon's AI agents." https://decagon.ai/blog/evaluation-engine-ai-agents

[77] Building and Scaling Production Code Agents: Replit (ZenML). https://www.zenml.io/llmops-database/building-and-scaling-production-code-agents-lessons-from-replit

[78] Cursor. "How we compare model quality in Cursor (CursorBench)." https://cursor.com/blog/cursorbench

[79] Cursor Composer 2 Technical Report. https://cursor.com/resources/Composer2.pdf

[80] Klarna AI assistant press release. https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/

[81] Parloa. "A Bayesian Framework for A/B Testing AI Agents." https://www.parloa.com/labs/research/ai-agent-testing/

[82] Scale AI Evaluations documentation. https://docs.gp.scale.com/docs/evaluations-1

[83] Aider LLM Leaderboards. https://aider.chat/docs/leaderboards/

[84] Aider code editing benchmarks. https://aider.chat/docs/benchmarks.html

[85] Promptfoo GitHub. https://github.com/promptfoo/promptfoo

[86] Promptfoo Anthropic docs. https://www.promptfoo.dev/docs/providers/anthropic/

[87] Promptfoo CI/CD integration. https://www.promptfoo.dev/docs/integrations/ci-cd/

[88] Langfuse GitHub (21.4k stars). https://github.com/langfuse/langfuse

[89] Langfuse pricing. https://langfuse.com/pricing

[90] LangSmith evaluation concepts. https://docs.smith.langchain.com/evaluation/concepts

[91] LangSmith trajectory eval docs. https://docs.langchain.com/langsmith/trajectory-evals

[92] LangSmith trace Claude Agent SDK. https://docs.langchain.com/langsmith/trace-claude-agent-sdk

[93] Braintrust eval guide. https://www.braintrust.dev/docs/guides/evals

[94] Braintrust pricing. https://www.braintrust.dev/pricing

[95] Braintrust $80M Series B. https://theaiworld.org/news/ai-funding-braintrust-80m-for-ai-observability

[96] DeepEval GitHub. https://github.com/confident-ai/deepeval

[97] Inspect AI. https://inspect.aisi.org.uk

[98] Inspect AI GitHub. https://github.com/UKGovernmentBEIS/inspect_ai

[99] UK AISI Inspect Evals (Nov 2024). https://www.aisi.gov.uk/blog/inspect-evals

[100] UK AISI 2025 year in review. https://www.aisi.gov.uk/blog/our-2025-year-in-review

[101] Arize Phoenix GitHub. https://github.com/Arize-ai/phoenix

[102] Galileo pricing. https://www.galileo.ai/pricing

[103] Ragas GitHub. https://github.com/explodinggradients/ragas

[104] Ragas agent metrics docs. https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/

[105] TruLens GitHub. https://github.com/truera/trulens

[106] METR. "Measuring AI ability to complete long tasks" (2025). https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

[107] METR. Algorithmic vs. holistic evaluation (Aug 2025). https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/

[108] Zhang, arXiv:2604.09459 (2026). "Credit Assignment in RL for LLMs." https://arxiv.org/abs/2604.09459

[109] Wei et al., arXiv:2505.11821 (2025). "Multi-turn reward design." https://arxiv.org/html/2505.11821v2

[110] LLM-Coordination Benchmark (NAACL 2025). https://aclanthology.org/2025.findings-naacl.448.pdf

[111] Apollo Research opinionated evals reading list. https://www.apolloresearch.ai/blog/an-opinionated-evals-reading-list/

[112] Sandbagging / scheming evals (LessWrong 2025). https://www.lesswrong.com/posts/TBk2dbWkg2F7dB3jb/it-s-hard-to-make-scheming-evals-look-realistic-for-llms

[113] LiveBench (ICLR 2025). https://iclr.cc/virtual/2025/poster/28134

[114] LH-Bench (long-horizon enterprise eval, 2026). https://arxiv.org/html/2603.22744v1

[115] Goodeye Labs. "LLM evaluation 2025 year in review." https://www.goodeyelabs.com/insights/llm-evaluation-2025-review

[116] EDDOps paper (Xia et al., arXiv:2411.13768). https://arxiv.org/abs/2411.13768

[117] Red Hat Developer. "Eval-Driven Development" (Mar 2026). https://developers.redhat.com/articles/2026/03/23/eval-driven-development-build-evaluate-ai-agents

[118] Bryan Bischof / Humanloop interview. https://humanloop.com/blog/LLM-eval-done-right

[119] Raza Habib. "EDD talk" (AI in Production 2025). https://home.mlops.community/public/videos/eval-driven-development-best-practices-and-pitfalls-when-building-with-ai-raza-habib-and-brianna-connelly-ai-in-production-2025-2025-03-13

[120] OSWorld paper (arXiv:2404.07972). https://arxiv.org/abs/2404.07972

[121] HAL Princeton GAIA leaderboard. https://hal.cs.princeton.edu/gaia

[122] BenchLM TAU-bench leaderboard. https://benchlm.ai/benchmarks/tauBench

[123] Contamination sensitivity study (arXiv:2603.21636, 2026). https://arxiv.org/abs/2603.21636

[124] Benchmarking LLMs under contamination (EMNLP 2025). https://aclanthology.org/2025.emnlp-main.511/

[125] Fireworks AI. "Best practices for multi-turn RL." https://fireworks.ai/blog/best-practices-for-multi-turn-RL

[126] LangChain evaluation framework article. https://www.langchain.com/articles/llm-evaluation-framework

[127] Galileo agent evaluation framework (Feb 2026). https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks

[128] Galileo LLM-as-judge vs. human evaluation. https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation

[129] OSWorld BenchLM leaderboard. https://benchlm.ai/benchmarks/osWorldVerified

[130] Promptfoo assertions documentation. https://www.promptfoo.dev/docs/configuration/expected-outputs/
