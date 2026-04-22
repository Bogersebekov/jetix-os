---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: writing-tools-for-agents
subcategory: meta
tags:
- meta
title: Writing Tools For Agents
word_count: 3730
---

<div id="main-content" role="main">

<div class="section page-wrapper HeroEngineering-module-scss-module__j1ivRa__hero"
aria-label="Engineering Article Hero">

<a href="../engineering.html"
class="body-2 bold HeroEngineering-module-scss-module__j1ivRa__hubLink">Engineering
at Anthropic</a>

<div class="HeroEngineering-module-scss-module__j1ivRa__content">

<div class="HeroEngineering-module-scss-module__j1ivRa__header">

<div class="HeroEngineering-module-scss-module__j1ivRa__heroImage">

<img
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/876165247ba5668bd195854eef4631ad9a184001-1000x1000.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="1000" height="1000"
alt="This is an abstract illustration for the Eng Blog article, Writing effective tools for agents -- with agents." />

</div>

# Writing effective tools for agents — with agents

</div>

<div class="HeroEngineering-module-scss-module__j1ivRa__metadata">

Published Sep 11, 2025

Agents are only as effective as the tools we give them. We share how to
write high-quality tools and evaluations, and how you can boost
performance by using Claude to optimize its tools for itself.

</div>

</div>

</div>

<div class="page-wrapper">

<div>

<div class="Body-module-scss-module__z40yvW__body" theme="ivory">

The [Model Context Protocol
(MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) can
empower LLM agents with potentially hundreds of tools to solve
real-world tasks. But how do we make those tools maximally effective?

In this post, we describe our most effective techniques for improving
performance in a variety of agentic AI systems<sup>1</sup>.

We begin by covering how you can:

- Build and test prototypes of your tools
- Create and run comprehensive evaluations of your tools with agents
- Collaborate with agents like Claude Code to automatically increase the
  performance of your tools

We conclude with key principles for writing high-quality tools we’ve
identified along the way:

- Choosing the right tools to implement (and not to implement)
- Namespacing tools to define clear boundaries in functionality
- Returning meaningful context from tools back to agents
- Optimizing tool responses for token efficiency
- Prompt-engineering tool descriptions and specs

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="1080"
alt="This is an image depicting how an engineer might use Claude Code to evaluate the efficacy of agentic tools." />
<figcaption>Building an evaluation allows you to systematically measure
the performance of your tools. You can use Claude Code to automatically
optimize your tools against this evaluation.</figcaption>
</figure>

</div>

## What is a tool?

In computing, deterministic systems produce the same output every time
given identical inputs, while *non-deterministic* systems—like
agents—can generate varied responses even with the same starting
conditions.

When we traditionally write software, we’re establishing a contract
between deterministic systems. For instance, a function call like
`getWeather(“NYC”)` will always fetch the weather in New York City in
the exact same manner every time it is called.

Tools are a new kind of software which reflects a contract between
deterministic systems and non-deterministic agents. When a user asks
"Should I bring an umbrella today?,” an agent might call the weather
tool, answer from general knowledge, or even ask a clarifying question
about location first. Occasionally, an agent might hallucinate or even
fail to grasp how to use a tool.

This means fundamentally rethinking our approach when writing software
for agents: instead of writing tools and [MCP
servers](https://modelcontextprotocol.io/) the way we’d write functions
and APIs for other developers or systems, we need to design them for
agents.

Our goal is to increase the surface area over which agents can be
effective in solving a wide range of tasks by using tools to pursue a
variety of successful strategies. Fortunately, in our experience, the
tools that are most “ergonomic” for agents also end up being
surprisingly intuitive to grasp as humans.

## How to write tools

In this section, we describe how you can collaborate with agents both to
write and to improve the tools you give them. Start by standing up a
quick prototype of your tools and testing them locally. Next, run a
comprehensive evaluation to measure subsequent changes. Working
alongside agents, you can repeat the process of evaluating and improving
your tools until your agents achieve strong performance on real-world
tasks.

### Building a prototype

It can be difficult to anticipate which tools agents will find ergonomic
and which tools they won’t without getting hands-on yourself. Start by
standing up a quick prototype of your tools. If you’re using [Claude
Code](https://www.anthropic.com/claude-code) to write your tools
(potentially in one-shot), it helps to give Claude documentation for any
software libraries, APIs, or SDKs (including potentially the [MCP
SDK](https://modelcontextprotocol.io/docs/sdk)) your tools will rely on.
LLM-friendly documentation can commonly be found in flat `llms.txt`
files on official documentation sites (here’s our
[API’s](https://docs.anthropic.com/llms.txt)).

Wrapping your tools in a [local MCP
server](https://modelcontextprotocol.io/docs/develop/connect-local-servers)
or [Desktop extension](desktop-extensions.html) (DXT) will allow you to
connect and test your tools in Claude Code or the Claude Desktop app.

To connect your local MCP server to Claude Code, run
`claude mcp add <name> <command> [args...]`.

To connect your local MCP server or DXT to the Claude Desktop app,
navigate to `Settings > Developer` or `Settings > Extensions`,
respectively.

Tools can also be passed directly into [Anthropic
API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
calls for programmatic testing.

Test the tools yourself to identify any rough edges. Collect feedback
from your users to build an intuition around the use-cases and prompts
you expect your tools to enable.

### Running an evaluation

Next, you need to measure how well Claude uses your tools by running an
evaluation. Start by generating lots of evaluation tasks, grounded in
real world uses. We recommend collaborating with an agent to help
analyze your results and determine how to improve your tools. See this
process end-to-end in our <a
href="https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation"
target="_blank" rel="noopener noreferrer">tool evaluation cookbook</a>.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="1080"
alt="This graph measures the test set accuracy of human-written vs. Claude-optimized Slack MCP servers." />
<figcaption>Held-out test set performance of our internal Slack
tools</figcaption>
</figure>

</div>

**Generating evaluation tasks**

With your early prototype, Claude Code can quickly explore your tools
and create dozens of prompt and response pairs. Prompts should be
inspired by real-world uses and be based on realistic data sources and
services (for example, internal knowledge bases and microservices). We
recommend you avoid overly simplistic or superficial “sandbox”
environments that don’t stress-test your tools with sufficient
complexity. Strong evaluation tasks might require multiple tool
calls—potentially dozens.

Here are some examples of strong tasks:

- Schedule a meeting with Jane next week to discuss our latest Acme Corp
  project. Attach the notes from our last project planning meeting and
  reserve a conference room.
- Customer ID 9182 reported that they were charged three times for a
  single purchase attempt. Find all relevant log entries and determine
  if any other customers were affected by the same issue.
- Customer Sarah Chen just submitted a cancellation request. Prepare a
  retention offer. Determine: (1) why they're leaving, (2) what
  retention offer would be most compelling, and (3) any risk factors we
  should be aware of before making an offer.

And here are some weaker tasks:

- Schedule a meeting with jane@acme.corp next week.
- Search the payment logs for `purchase_complete` and
  `customer_id=9182`.
- Find the cancellation request by Customer ID 45892.

Each evaluation prompt should be paired with a verifiable response or
outcome. Your verifier can be as simple as an exact string comparison
between ground truth and sampled responses, or as advanced as enlisting
Claude to judge the response. Avoid overly strict verifiers that reject
correct responses due to spurious differences like formatting,
punctuation, or valid alternative phrasings.

For each prompt-response pair, you can optionally also specify the tools
you expect an agent to call in solving the task, to measure whether or
not agents are successful in grasping each tool’s purpose during
evaluation. However, because there might be multiple valid paths to
solving tasks correctly, try to avoid overspecifying or overfitting to
strategies.

**Running the evaluation**

We recommend running your evaluation programmatically with direct LLM
API calls. Use simple agentic loops (`while`-loops wrapping alternating
LLM API and tool calls): one loop for each evaluation task. Each
evaluation agent should be given a single task prompt and your tools.

In your evaluation agents’ system prompts, we recommend instructing
agents to output not just structured response blocks (for verification),
but also reasoning and feedback blocks. Instructing agents to output
these *before* tool call and response blocks may increase LLMs’
effective intelligence by triggering chain-of-thought (CoT) behaviors.

If you’re running your evaluation with Claude, you can turn on
[interleaved
thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking)
for similar functionality “off-the-shelf”. This will help you probe why
agents do or don’t call certain tools and highlight specific areas of
improvement in tool descriptions and specs.

As well as top-level accuracy, we recommend collecting other metrics
like the total runtime of individual tool calls and tasks, the total
number of tool calls, the total token consumption, and tool errors.
Tracking tool calls can help reveal common workflows that agents pursue
and offer some opportunities for tools to consolidate.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="1080"
alt="This graph measures the test set accuracy of human-written vs. Claude-optimized Asana MCP servers." />
<figcaption>Held-out test set performance of our internal Asana
tools</figcaption>
</figure>

</div>

**Analyzing results**  
Agents are your helpful partners in spotting issues and providing
feedback on everything from contradictory tool descriptions to
inefficient tool implementations and confusing tool schemas. However,
keep in mind that what agents omit in their feedback and responses can
often be more important than what they include. LLMs don’t always [say
what they mean](../research/tracing-thoughts-language-model.html).

Observe where your agents get stumped or confused. Read through your
evaluation agents’ reasoning and feedback (or CoT) to identify rough
edges. Review the raw transcripts (including tool calls and tool
responses) to catch any behavior not explicitly described in the agent’s
CoT. Read between the lines; remember that your evaluation agents don’t
necessarily know the correct answers and strategies.

Analyze your tool calling metrics. Lots of redundant tool calls might
suggest some rightsizing of pagination or token limit parameters is
warranted; lots of tool errors for invalid parameters might suggest
tools could use clearer descriptions or better examples. When we
launched Claude’s [web search
tool](https://www.anthropic.com/news/web-search), we identified that
Claude was needlessly appending `2025` to the tool’s `query` parameter,
biasing search results and degrading performance (we steered Claude in
the right direction by improving the tool description).

### Collaborating with agents

You can even let agents analyze your results and improve your tools for
you. Simply concatenate the transcripts from your evaluation agents and
paste them into Claude Code. Claude is an expert at analyzing
transcripts and refactoring lots of tools all at once—for example, to
ensure tool implementations and descriptions remain self-consistent when
new changes are made.

In fact, most of the advice in this post came from repeatedly optimizing
our internal tool implementations with Claude Code. Our evaluations were
created on top of our internal workspace, mirroring the complexity of
our internal workflows, including real projects, documents, and
messages.

We relied on held-out test sets to ensure we did not overfit to our
“training” evaluations. These test sets revealed that we could extract
additional performance improvements even beyond what we achieved with
"expert" tool implementations—whether those tools were manually written
by our researchers or generated by Claude itself.

In the next section, we’ll share some of what we learned from this
process.

## Principles for writing effective tools

In this section, we distill our learnings into a few guiding principles
for writing effective tools.

### Choosing the right tools for agents

More tools don’t always lead to better outcomes. A common error we’ve
observed is tools that merely wrap existing software functionality or
API endpoints—whether or not the tools are appropriate for agents. This
is because agents have distinct “affordances” to traditional
software—that is, they have different ways of perceiving the potential
actions they can take with those tools

LLM agents have limited "context" (that is, there are limits to how much
information they can process at once), whereas computer memory is cheap
and abundant. Consider the task of searching for a contact in an address
book. Traditional software programs can efficiently store and process a
list of contacts one at a time, checking each one before moving on.

However, if an LLM agent uses a tool that returns ALL contacts and then
has to read through each one token-by-token, it's wasting its limited
context space on irrelevant information (imagine searching for a contact
in your address book by reading each page from top-to-bottom—that is,
via brute-force search). The better and more natural approach (for
agents and humans alike) is to skip to the relevant page first (perhaps
finding it alphabetically).

We recommend building a few thoughtful tools targeting specific
high-impact workflows, which match your evaluation tasks and scaling up
from there. In the address book case, you might choose to implement a
`search_contacts` or `message_contact` tool instead of a `list_contacts`
tool.

Tools can consolidate functionality, handling potentially *multiple*
discrete operations (or API calls) under the hood. For example, tools
can enrich tool responses with related metadata or handle frequently
chained, multi-step tasks in a single tool call.

Here are some examples:

- Instead of implementing a `list_users`, `list_events`, and
  `create_event` tools, consider implementing a `schedule_event` tool
  which finds availability and schedules an event.
- Instead of implementing a `read_logs` tool, consider implementing a
  `search_logs` tool which only returns relevant log lines and some
  surrounding context.
- Instead of implementing `get_customer_by_id`, `list_transactions`, and
  `list_notes` tools, implement a `get_customer_context` tool which
  compiles all of a customer’s recent & relevant information all at
  once.

Make sure each tool you build has a clear, distinct purpose. Tools
should enable agents to subdivide and solve tasks in much the same way
that a human would, given access to the same underlying resources, and
simultaneously reduce the context that would have otherwise been
consumed by intermediate outputs.

Too many tools or overlapping tools can also distract agents from
pursuing efficient strategies. Careful, selective planning of the tools
you build (or don’t build) can really pay off.

### Namespacing your tools

Your AI agents will potentially gain access to dozens of MCP servers and
hundreds of different tools–including those by other developers. When
tools overlap in function or have a vague purpose, agents can get
confused about which ones to use.

Namespacing (grouping related tools under common prefixes) can help
delineate boundaries between lots of tools; MCP clients sometimes do
this by default. For example, namespacing tools by service (e.g.,
`asana_search`, `jira_search`) and by resource (e.g.,
`asana_projects_search`, `asana_users_search`), can help agents select
the right tools at the right time.

We have found selecting between prefix- and suffix-based namespacing to
have non-trivial effects on our tool-use evaluations. Effects vary by
LLM and we encourage you to choose a naming scheme according to your own
evaluations.

Agents might call the wrong tools, call the right tools with the wrong
parameters, call too few tools, or process tool responses incorrectly.
By selectively implementing tools whose names reflect natural
subdivisions of tasks, you simultaneously reduce the number of tools and
tool descriptions loaded into the agent’s context and offload agentic
computation from the agent’s context back into the tool calls
themselves. This reduces an agent’s overall risk of making mistakes.

### Returning meaningful context from your tools

In the same vein, tool implementations should take care to return only
high signal information back to agents. They should prioritize
contextual relevance over flexibility, and eschew low-level technical
identifiers (for example: `uuid`, `256px_image_url`, `mime_type`).
Fields like `name`, `image_url`, and `file_type` are much more likely to
directly inform agents’ downstream actions and responses.

Agents also tend to grapple with natural language names, terms, or
identifiers significantly more successfully than they do with cryptic
identifiers. We’ve found that merely resolving arbitrary alphanumeric
UUIDs to more semantically meaningful and interpretable language (or
even a 0-indexed ID scheme) significantly improves Claude’s precision in
retrieval tasks by reducing hallucinations.

In some instances, agents may require the flexibility to interact with
both natural language and technical identifiers outputs, if only to
trigger downstream tool calls (for example, `search_user(name=’jane’)` →
`send_message(id=12345)`). You can enable both by exposing a simple
`response_format` enum parameter in your tool, allowing your agent to
control whether tools return `“concise”` or `“detailed”` responses
(images below).

You can add more formats for even greater flexibility, similar to
GraphQL where you can choose exactly which pieces of information you
want to receive. Here is an example ResponseFormat enum to control tool
response verbosity:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

Here’s an example of a detailed tool response (206 tokens):

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="1006"
alt="This code snippet depicts an example of a detailed tool response." />
</figure>

</div>

Here’s an example of a concise tool response (72 tokens):

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="725"
alt="This code snippet depicts a concise tool response." />
<figcaption>Slack threads and thread replies are identified by unique
<code>thread_ts</code> which are required to fetch thread replies.
<code>thread_ts</code> and other IDs (<code>channel_id</code>,
<code>user_id</code>) can be retrieved from a <code>“detailed”</code>
tool response to enable further tool calls that require these.
<code>“concise”</code> tool responses return only thread content and
exclude IDs. In this example, we use ~⅓ of the tokens with
<code>“concise”</code> tool responses.</figcaption>
</figure>

</div>

Even your tool response structure—for example XML, JSON, or Markdown—can
have an impact on evaluation performance: there is no one-size-fits-all
solution. This is because LLMs are trained on next-token prediction and
tend to perform better with formats that match their training data. The
optimal response structure will vary widely by task and agent. We
encourage you to select the best response structure based on your own
evaluation.

### Optimizing tool responses for token efficiency

Optimizing the quality of context is important. But so is optimizing the
*quantity* of context returned back to agents in tool responses.

We suggest implementing some combination of pagination, range selection,
filtering, and/or truncation with sensible default parameter values for
any tool responses that could use up lots of context. For Claude Code,
we restrict tool responses to 25,000 tokens by default. We expect the
effective context length of agents to grow over time, but the need for
context-efficient tools to remain.

If you choose to truncate responses, be sure to steer agents with
helpful instructions. You can directly encourage agents to pursue more
token-efficient strategies, like making many small and targeted searches
instead of a single, broad search for a knowledge retrieval task.
Similarly, if a tool call raises an error (for example, during input
validation), you can prompt-engineer your error responses to clearly
communicate specific and actionable improvements, rather than opaque
error codes or tracebacks.

Here’s an example of a truncated tool response:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="1162"
alt="This image depicts an example of a truncated tool response." />
</figure>

</div>

Here’s an example of an unhelpful error response:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="733"
alt="This image depicts an example of an unhelpful tool response. " />
</figure>

</div>

Here’s an example of a helpful error response:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1920" height="850"
alt="This image depicts an example of a helpful error response." />
<figcaption>Tool truncation and error responses can steer agents towards
more token-efficient tool-use behaviors (using filters or pagination) or
give examples of correctly formatted tool inputs.</figcaption>
</figure>

</div>

### Prompt-engineering your tool descriptions

We now come to one of the most effective methods for improving tools:
prompt-engineering your tool descriptions and specs. Because these are
loaded into your agents’ context, they can collectively steer agents
toward effective tool-calling behaviors.

When writing tool descriptions and specs, think of how you would
describe your tool to a new hire on your team. Consider the context that
you might implicitly bring—specialized query formats, definitions of
niche terminology, relationships between underlying resources—and make
it explicit. Avoid ambiguity by clearly describing (and enforcing with
strict data models) expected inputs and outputs. In particular, input
parameters should be unambiguously named: instead of a parameter named
`user`, try a parameter named `user_id`.

With your evaluation you can measure the impact of your prompt
engineering with greater confidence. Even small refinements to tool
descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved
state-of-the-art performance on the [SWE-bench
Verified](../research/swe-bench-sonnet.html) evaluation after we made
precise refinements to tool descriptions, dramatically reducing error
rates and improving task completion.

You can find other best practices for tool definitions in our [Developer
Guide](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions).
If you’re building tools for Claude, we also recommend reading about how
tools are dynamically loaded into Claude’s [system
prompt](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt).
Lastly, if you’re writing tools for an MCP server, [tool
annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
help disclose which tools require open-world access or make destructive
changes.

## Looking ahead

To build effective tools for agents, we need to re-orient our software
development practices from predictable, deterministic patterns to
non-deterministic ones.

Through the iterative, evaluation-driven process we’ve described in this
post, we've identified consistent patterns in what makes tools
successful: Effective tools are intentionally and clearly defined, use
agent context judiciously, can be combined together in diverse
workflows, and enable agents to intuitively solve real-world tasks.

In the future, we expect the specific mechanisms through which agents
interact with the world to evolve—from updates to the MCP protocol to
upgrades to the underlying LLMs themselves. With a systematic,
evaluation-driven approach to improving tools for agents, we can ensure
that as agents become more capable, the tools they use will evolve
alongside them.

## Acknowledgements

Written by Ken Aizawa with valuable contributions from colleagues across
Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh,
Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra,
Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly
Vorwerck), Design (Drew Roper), and Applied AI (Christian Ryan,
Alexander Bricken).

<sup>1</sup>Beyond training the underlying LLMs themselves.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<a href="https://anthropic.skilljar.com/"
class="ToutCallout-module-scss-module__gZk6bG__root" rel="noopener"
target="_blank"></a>

<div class="ToutCallout-module-scss-module__gZk6bG__illustration bg-cactus">

<img
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="1000" height="1000"
alt="Interlocking puzzle piece with complex geometric shape and detailed surface texture" />

</div>

<div class="ToutCallout-module-scss-module__gZk6bG__content">

<div class="ToutCallout-module-scss-module__gZk6bG__textWrapper">

### Looking to learn more?

</div>

<div class="caption ToutCallout-module-scss-module__gZk6bG__cta">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiBUb3V0Q2FsbG91dC1tb2R1bGUtc2Nzcy1tb2R1bGVfX2daazZiR19faWNvbiIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiB2aWV3Ym94PSIwIDAgMTMgMTMiPjxwYXRoIGQ9Ik01Ljg1IDBDNi4wOTg1MyAwIDYuMyAwLjIwMTQ3MiA2LjMgMC40NUM2LjMgMC42OTg1MjggNi4wOTg1MyAwLjkgNS44NSAwLjlIMS4zNUMxLjEwMTQ3IDAuOSAwLjkgMS4xMDE0NyAwLjkgMS4zNVYxMS4yNUMwLjkgMTEuNDk4NSAxLjEwMTQ3IDExLjcgMS4zNSAxMS43SDExLjI1QzExLjQ5ODUgMTEuNyAxMS43IDExLjQ5ODUgMTEuNyAxMS4yNVY2Ljc1QzExLjcgNi41MDE0NyAxMS45MDE1IDYuMyAxMi4xNSA2LjNDMTIuMzk4NSA2LjMgMTIuNiA2LjUwMTQ3IDEyLjYgNi43NVYxMS4yNUMxMi42IDExLjk5NTYgMTEuOTk1NiAxMi42IDExLjI1IDEyLjZIMS4zNUMwLjYwNDQxNiAxMi42IDEuODExOTdlLTA4IDExLjk5NTYgMCAxMS4yNVYxLjM1QzAgMC42MDQ0MTYgMC42MDQ0MTYgMS40NDk1OWUtMDggMS4zNSAwSDUuODVaTTEyLjE1IDBDMTIuMTgzNiAtMi4zOTA2M2UtMDggMTIuMjE3MiAwLjAwMzkyODA5IDEyLjI1MDIgMC4wMTE0MjU4QzEyLjI3MTIgMC4wMTYyMjkyIDEyLjI5MTcgMC4wMjMwMzE3IDEyLjMxMTcgMC4wMzA3NjE3QzEyLjMxODMgMC4wMzMzMDYzIDEyLjMyNDYgMC4wMzY2ODMgMTIuMzMxMSAwLjAzOTU1MDhDMTIuMzQ5MiAwLjA0NzU0NjggMTIuMzY2OCAwLjA1NjQ0NyAxMi4zODM4IDAuMDY2Nzk2OUMxMi4zOTA3IDAuMDcxMDI3MSAxMi4zOTgyIDAuMDc0NDYzMiAxMi40MDQ5IDAuMDc5MTAxNkMxMi40Mjc0IDAuMDk0NTY3OCAxMi40NDg2IDAuMTEyMjQgMTIuNDY4MiAwLjEzMTgzNkwxMi41MjYyIDAuMjAyMTQ4QzEyLjUzNiAwLjIxNzA0NyAxMi41NDIgMC4yMzM4ODkgMTIuNTQ5OSAwLjI0OTYwOUMxMi41NTUgMC4yNTk3MTEgMTIuNTYxNCAwLjI2OTA0NSAxMi41NjU3IDAuMjc5NDkyQzEyLjU4MTEgMC4zMTY5MSAxMi41ODk5IDAuMzU1OTI2IDEyLjU5NDcgMC4zOTU1MDhDMTIuNTk2OSAwLjQxMzU3MyAxMi42IDAuNDMxNjEgMTIuNiAwLjQ1VjQuMDVDMTIuNiA0LjI5ODUzIDEyLjM5ODUgNC41IDEyLjE1IDQuNUMxMS45MDE1IDQuNSAxMS43IDQuMjk4NTMgMTEuNyA0LjA1VjEuNTM2MzNMNy45NjgxNiA1LjI2ODE2QzcuNzkyNDMgNS40NDM5IDcuNTA3NTcgNS40NDM5IDcuMzMxODQgNS4yNjgxNkM3LjE1NjEgNS4wOTI0MyA3LjE1NjEgNC44MDc1NyA3LjMzMTg0IDQuNjMxODRMMTEuMDYzNyAwLjlIOC41NUM4LjMwMTQ3IDAuOSA4LjEgMC42OTg1MjggOC4xIDAuNDVDOC4xIDAuMjAxNDcyIDguMzAxNDcgNC4yNTIyN2UtMDggOC41NSAwSDEyLjE1WiIgZmlsbD0iIzVFNUQ1OSIgLz48L3N2Zz4="
class="Icon-module-scss-module__lqbdHG__icon ToutCallout-module-scss-module__gZk6bG__icon" />Explore
courses

</div>

</div>

</div>

</div>

</div>

<div class="NewsletterSubscribe-module-scss-module__MOPAja__wrapper">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__content">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__text-content">

## Get the developer newsletter

<div class="NewsletterSubscribe-module-scss-module__MOPAja__body">

Product updates, how-tos, community spotlights, and more. Delivered
monthly to your inbox.

</div>

</div>

<div class="NewsletterSubscribe-module-scss-module__MOPAja__form-container">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__input-wrapper">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB2aWV3Ym94PSIwIDAgMjEgMjEiPjxwYXRoIGQ9Ik00LjE0NTg1IDkuODc0OTJMMTQuNDU4NCA5Ljg3NDkyTDkuNjA0MTkgNS4wNDE1OEwxMC41IDQuMTQ1NzVMMTYuODU0MiAxMC40OTk5TDEwLjUgMTYuODU0MUw5LjYwNDE5IDE1Ljk1ODNMMTQuNDU4NCAxMS4xMjQ5TDQuMTQ1ODUgMTEuMTI0OUw0LjE0NTg1IDkuODc0OTJaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+"
class="Icon-module-scss-module__lqbdHG__icon" />

</div>

Please provide your email address if you'd like to receive our monthly
developer newsletter. You can unsubscribe at any time.

</div>

</div>

</div>

</div>

</div>