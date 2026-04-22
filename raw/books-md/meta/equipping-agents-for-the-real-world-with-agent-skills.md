---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: equipping-agents-for-the-real-world-with-agent-skills
subcategory: meta
tags:
- meta
title: Equipping Agents For The Real World With Agent Skills
word_count: 1822
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
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/b52f6dbff1c4323ef2371ba0ac50df994835435a-1000x1000.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="1000" height="1000" />

</div>

# Equipping agents for the real world with Agent Skills

</div>

<div class="HeroEngineering-module-scss-module__j1ivRa__metadata">

Published Oct 16, 2025

Claude is powerful, but real work requires procedural knowledge and
organizational context. Introducing Agent Skills, a new way to build
specialized agents using files and folders.

</div>

</div>

</div>

<div class="page-wrapper">

<div>

<div class="Body-module-scss-module__z40yvW__body" theme="ivory">

*Update: We've
published* <a href="https://agentskills.io/" target="_blank"
rel="noopener noreferrer"><em>Agent Skills</em></a> *as an open standard
for cross-platform portability. (December 18, 2025)*

As model capabilities improve, we can now build general-purpose agents
that interact with full-fledged computing environments.
<a href="https://claude.com/product/claude-code" target="_blank"
rel="noopener noreferrer">Claude Code</a>, for example, can accomplish
complex tasks across domains using local code execution and filesystems.
But as these agents become more powerful, we need more composable,
scalable, and portable ways to equip them with domain-specific
expertise.

This led us to create
<a href="https://www.anthropic.com/news/skills" target="_blank"
rel="noopener noreferrer"><strong>Agent Skills</strong></a>: organized
folders of instructions, scripts, and resources that agents can discover
and load dynamically to perform better at specific tasks. Skills extend
Claude’s capabilities by packaging your expertise into composable
resources for Claude, transforming general-purpose agents into
specialized agents that fit your needs.

Building a skill for an agent is like putting together an onboarding
guide for a new hire. Instead of building fragmented, custom-designed
agents for each use case, anyone can now specialize their agents with
composable capabilities by capturing and sharing their procedural
knowledge. In this article, we explain what Skills are, show how they
work, and share best practices for building your own.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fddd7e6e572ad0b6a943cacefe957248455f6d522-1650x929.jpg&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fddd7e6e572ad0b6a943cacefe957248455f6d522-1650x929.jpg&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fddd7e6e572ad0b6a943cacefe957248455f6d522-1650x929.jpg&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1650" height="929"
alt="To activate skills, all you need to do is write a SKILL.md file with custom guidance for your agent." />
<figcaption>A skill is a directory containing a SKILL.md file that
contains organized folders of instructions, scripts, and resources that
give agents additional capabilities.</figcaption>
</figure>

</div>

## The anatomy of a skill

To see Skills in action, let’s walk through a real example: one of the
skills that powers
<a href="https://www.anthropic.com/news/create-files" target="_blank"
rel="noopener noreferrer">Claude’s recently launched document editing
abilities</a>. Claude already knows a lot about understanding PDFs, but
is limited in its ability to manipulate them directly (e.g. to fill out
a form). This <a
href="https://github.com/anthropics/skills/tree/main/document-skills/pdf"
target="_blank" rel="noopener noreferrer">PDF skill</a> lets us give
Claude these new abilities.

At its simplest, a skill is a directory that contains a `SKILL.md file`.
This file must start with YAML frontmatter that contains some required
metadata: `name` and `description`. At startup, the agent pre-loads the
`name` and `description` of every installed skill into its system
prompt.

This metadata is the **first level** of *progressive disclosure*: it
provides just enough information for Claude to know when each skill
should be used without loading all of it into context. The actual body
of this file is the **second level** of detail. If Claude thinks the
skill is relevant to the current task, it will load the skill by reading
its full `SKILL.md` into context.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6f22d8913dbc6228e7f11a41e0b3c124d817b6d2-1650x929.jpg&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6f22d8913dbc6228e7f11a41e0b3c124d817b6d2-1650x929.jpg&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6f22d8913dbc6228e7f11a41e0b3c124d817b6d2-1650x929.jpg&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1650" height="929"
alt="Anatomy of a SKILL.md file including the relevant metadata: name, description, and context related to the specific actions the skill should take." />
<figcaption>A SKILL.md file must begin with YAML Frontmatter that
contains a file name and description, which is loaded into its system
prompt at startup.</figcaption>
</figure>

</div>

As skills grow in complexity, they may contain too much context to fit
into a single `SKILL.md`, or context that’s relevant only in specific
scenarios. In these cases, skills can bundle additional files within the
skill directory and reference them by name from `SKILL.md`. These
additional linked files are the **third level** (and beyond) of detail,
which Claude can choose to navigate and discover only as needed.

In the PDF skill shown below, the `SKILL.md` refers to two additional
files (`reference.md` and `forms.md`) that the skill author chooses to
bundle alongside the core `SKILL.md`. By moving the form-filling
instructions to a separate file (`forms.md`), the skill author is able
to keep the core of the skill lean, trusting that Claude will read
`forms.md` only when filling out a form.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F191bf5dd4b6f8cfe6f1ebafe6243dd1641ed231c-1650x1069.jpg&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F191bf5dd4b6f8cfe6f1ebafe6243dd1641ed231c-1650x1069.jpg&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F191bf5dd4b6f8cfe6f1ebafe6243dd1641ed231c-1650x1069.jpg&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1650" height="1069"
alt="How to bundle additional content into a SKILL.md file." />
<figcaption>You can incorporate more context (via additional files) into
your skill that can then be triggered by Claude based on the system
prompt.</figcaption>
</figure>

</div>

Progressive disclosure is the core design principle that makes Agent
Skills flexible and scalable. Like a well-organized manual that starts
with a table of contents, then specific chapters, and finally a detailed
appendix, skills let Claude load information only as needed:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa3bca2763d7892982a59c28aa4df7993aaae55ae-2292x673.jpg&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa3bca2763d7892982a59c28aa4df7993aaae55ae-2292x673.jpg&amp;w=3840&amp;q=75amp;q=75 1x"
width="2292" height="673"
alt="This image depicts how progressive disclosure of context in Skills." />
</figure>

</div>

Agents with a filesystem and code execution tools don’t need to read the
entirety of a skill into their context window when working on a
particular task. This means that the amount of context that can be
bundled into a skill is effectively unbounded.

### Skills and the context window

The following diagram shows how the context window changes when a skill
is triggered by a user’s message.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F441b9f6cc0d2337913c1f41b05357f16f51f702e-1650x929.jpg&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F441b9f6cc0d2337913c1f41b05357f16f51f702e-1650x929.jpg&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F441b9f6cc0d2337913c1f41b05357f16f51f702e-1650x929.jpg&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1650" height="929"
alt="This image depicts how skills are triggered in your context window." />
<figcaption>Skills are triggered in the context window via your system
prompt.</figcaption>
</figure>

</div>

The sequence of operations shown:

1.  To start, the context window has the core system prompt and the
    metadata for each of the installed skills, along with the user’s
    initial message;
2.  Claude triggers the PDF skill by invoking a Bash tool to read the
    contents of `pdf/SKILL.md`;
3.  Claude chooses to read the `forms.md` file bundled with the skill;
4.  Finally, Claude proceeds with the user’s task now that it has loaded
    relevant instructions from the PDF skill.

### Skills and code execution

Skills can also include code for Claude to execute as tools at its
discretion.

Large language models excel at many tasks, but certain operations are
better suited for traditional code execution. For example, sorting a
list via token generation is far more expensive than simply running a
sorting algorithm. Beyond efficiency concerns, many applications require
the deterministic reliability that only code can provide.

In our example, the PDF skill includes a pre-written Python script that
reads a PDF and extracts all form fields. Claude can run this script
without loading either the script or the PDF into context. And because
code is deterministic, this workflow is consistent and repeatable.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc24b4a2ff77277c430f2c9ef1541101766ae5714-1650x929.jpg&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc24b4a2ff77277c430f2c9ef1541101766ae5714-1650x929.jpg&amp;w=1920&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc24b4a2ff77277c430f2c9ef1541101766ae5714-1650x929.jpg&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="1650" height="929"
alt="This image depicts how code is executed via Skills." />
<figcaption>Skills can also include code for Claude to execute as tools
at its discretion based on the nature of the task.</figcaption>
</figure>

</div>

## Developing and evaluating skills

Here are some helpful guidelines for getting started with authoring and
testing skills:

- **Start with evaluation:** Identify specific gaps in your agents’
  capabilities by running them on representative tasks and observing
  where they struggle or require additional context. Then build skills
  incrementally to address these shortcomings.
- **Structure for scale:** When the `SKILL.md` file becomes unwieldy,
  split its content into separate files and reference them. If certain
  contexts are mutually exclusive or rarely used together, keeping the
  paths separate will reduce the token usage. Finally, code can serve as
  both executable tools and as documentation. It should be clear whether
  Claude should run scripts directly or read them into context as
  reference.
- **Think from Claude’s perspective:** Monitor how Claude uses your
  skill in real scenarios and iterate based on observations: watch for
  unexpected trajectories or overreliance on certain contexts. Pay
  special attention to the `name` and `description` of your skill.
  Claude will use these when deciding whether to trigger the skill in
  response to its current task.
- **Iterate with Claude:** As you work on a task with Claude, ask Claude
  to capture its successful approaches and common mistakes into reusable
  context and code within a skill. If it goes off track when using a
  skill to complete a task, ask it to self-reflect on what went wrong.
  This process will help you discover what context Claude actually
  needs, instead of trying to anticipate it upfront.

### Security considerations when using Skills

Skills provide Claude with new capabilities through instructions and
code. While this makes them powerful, it also means that malicious
skills may introduce vulnerabilities in the environment where they’re
used or direct Claude to exfiltrate data and take unintended actions.

We recommend installing skills only from trusted sources. When
installing a skill from a less-trusted source, thoroughly audit it
before use. Start by reading the contents of the files bundled in the
skill to understand what it does, paying particular attention to code
dependencies and bundled resources like images or scripts. Similarly,
pay attention to instructions or code within the skill that instruct
Claude to connect to potentially untrusted external network sources.

## The future of Skills

Agent Skills are
<a href="https://www.anthropic.com/news/skills" target="_blank"
rel="noopener noreferrer">supported today</a> across <a
href="http://claude.ai/redirect/website.v1.7dfbee6c-de48-457e-ab7e-a34c9478faa9"
target="_blank" rel="noopener noreferrer">Claude.ai</a>, Claude Code,
the Claude Agent SDK, and the Claude Developer Platform.

In the coming weeks, we’ll continue to add features that support the
full lifecycle of creating, editing, discovering, sharing, and using
Skills. We’re especially excited about the opportunity for Skills to
help organizations and individuals share their context and workflows
with Claude. We’ll also explore how Skills can complement
<a href="https://modelcontextprotocol.io/" target="_blank"
rel="noopener noreferrer">Model Context Protocol</a> (MCP) servers by
teaching agents more complex workflows that involve external tools and
software.

Looking further ahead, we hope to enable agents to create, edit, and
evaluate Skills on their own, letting them codify their own patterns of
behavior into reusable capabilities.

Skills are a simple concept with a correspondingly simple format. This
simplicity makes it easier for organizations, developers, and end users
to build customized agents and give them new capabilities.

We’re excited to see what people build with Skills. Get started today by
checking out our Skills <a
href="https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview"
target="_blank" rel="noopener noreferrer">docs</a> and <a
href="https://github.com/anthropics/claude-cookbooks/tree/main/skills"
target="_blank" rel="noopener noreferrer">cookbook</a>.

## Acknowledgements

Written by Barry Zhang, Keith Lazuka, and Mahesh Murag, who all really
like folders. Special thanks to the many others across Anthropic who
championed, supported, and built Skills.

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