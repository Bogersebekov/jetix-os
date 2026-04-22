---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: building-c-compiler
subcategory: meta
tags:
- meta
title: Building C Compiler
word_count: 2657
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
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/7e2e39544a35760367049072406377a54f2b58c0-2554x2554.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="2554" height="2554" />

</div>

# Building a C compiler with a team of parallel Claudes

</div>

<div class="HeroEngineering-module-scss-module__j1ivRa__metadata">

Published Feb 05, 2026

We tasked Opus 4.6 using agent teams to build a C Compiler, and then
(mostly) walked away. Here's what it taught us about the future of
autonomous software development.

</div>

</div>

</div>

<div class="page-wrapper">

<div class="ArticleDetail-module-scss-module__YVTUHa__grid">

<div class="ArticleDetail-module-scss-module__YVTUHa__sidebar-container">

<span class="caption bold"></span><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjgiIGhlaWdodD0iNSIgdmlld2JveD0iMCAwIDggNSI+PHBhdGggZD0iTTcuMzAxNiAwLjIzMTgwOEM3LjQ0OTMyIDAuMDY3ODE2MiA3LjcwMzA2IDAuMDU0NjM5OCA3Ljg2NzI0IDAuMjAyMTJDOC4wMzEzNyAwLjM0OTg4OCA4LjA0NDYxIDAuNjAzNTY4IDcuODk2OTIgMC43Njc3NjZMNC4yOTY4NCA0Ljc2NzkxTDQuMjM0MzQgNC44MjQxN0M0LjE2NjYyIDQuODczMjggNC4wODQyNSA0Ljg5OTk1IDMuOTk5MTggNC44OTk5NUMzLjg4NTg4IDQuODk5ODkgMy43NzczMyA0Ljg1MjEzIDMuNzAxNTIgNC43Njc5MUwwLjEwMTQ0IDAuNzY3NzY2TDAuMDUzNzgyNSAwLjcwMjEzOUMtMC4wNDAyMDYgMC41NDE3NTMgLTAuMDEyNDI1NCAwLjMzMTM1NiAwLjEzMTEyOCAwLjIwMjEyQzAuMjc0Nzc1IDAuMDcyODg0NCAwLjQ4Njk3MiAwLjA2NzQ1OTMgMC42MzY2MDggMC4xNzc5TDAuNjk2NzY1IDAuMjMxODA4TDMuOTk5MTggMy45MDE0OEw3LjMwMTYgMC4yMzE4MDhaIiBmaWxsPSIjMTQxNDEzIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" />

<div>

</div>

</div>

<div class="Body-module-scss-module__z40yvW__body ArticleDetail-module-scss-module__YVTUHa__body-container"
theme="ivory">

*Written by Nicholas Carlini, a researcher on our Safeguards team.  
  
*

I've been experimenting with a new approach to supervising language
models that we’re calling "agent teams."

With agent teams, multiple Claude instances work in parallel on a shared
codebase without active human intervention. This approach dramatically
expands the scope of what's achievable with LLM agents.

To stress test it, I tasked 16 agents with writing a Rust-based C
compiler, from scratch, capable of compiling the Linux kernel. Over
nearly 2,000 Claude Code sessions and \$20,000 in API costs, the agent
team produced a 100,000-line compiler that can build Linux 6.9 on x86,
ARM, and RISC-V.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="Video-module-scss-module__qJNyFq__post-wrapper">

<figure class="Video-module-scss-module__qJNyFq__post-video-container">

</figure>

</div>

</div>

[The compiler is an interesting
artifact](https://github.com/anthropics/claudes-c-compiler) on its own,
but I focus here on what I learned about designing harnesses for
long-running autonomous agent teams: how to write tests that keep agents
on track without human oversight, how to structure work so multiple
agents can make progress in parallel, and where this approach hits its
ceiling.

## Enabling long-running Claudes

Existing agent scaffolds like Claude Code require an operator to be
online and available to work jointly. If you ask for a solution to a
long and complex problem, the model may solve part of it, but eventually
it will stop and wait for continued input—a question, a status update,
or a request for clarification.

To elicit sustained, autonomous progress, I built a harness that sticks
Claude in a simple loop (if you’ve seen Ralph-loop, this should look
familiar). When it finishes one task, it immediately picks up the next.
*(Run this in a container, not your actual machine).*

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
#!/bin/bash

while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    LOGFILE="agent_logs/agent_${COMMIT}.log"

    claude --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-X-Y &> "$LOGFILE"
done
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

  
In the agent prompt, I tell Claude what problem to solve and ask it to
approach the problem by breaking it into small pieces, tracking what
it’s working on, figuring out what to work on next, and to effectively
keep going until it’s perfect. (On this last point, Claude has no
choice. The loop runs forever—although in one instance, I did see Claude
`pkill -9 bash` on accident, thus killing itself and ending the loop.
Whoops!).

##  Running Claude in parallel

Running multiple instances in parallel can address two weaknesses of a
single-agent harness:

- One Claude Code session can only do one thing at a time. Especially as
  the scope of a project expands, debugging multiple issues in parallel
  is far more efficient.
- Running multiple Claude agents allows for specialization. While a few
  agents are tasked to solve the actual problem at hand, other
  specialized agents can be invoked to (for example) maintain
  documentation, keep an eye on code quality, or solve specialized
  sub-tasks.

My implementation of parallel Claude is bare-bones. A new bare git repo
is created, and for each agent, a Docker container is spun up with the
repo mounted to `/upstream`. Each agent clones a local copy to
`/workspace`, and when it's done, pushes from its own local container to
upstream.

To prevent two agents from trying to solve the same problem at the same
time, the harness uses a simple synchronization algorithm:

1.  Claude takes a "lock" on a task by writing a text file to
    current_tasks/ (e.g., one agent might lock
    current_tasks/parse_if_statement.txt, while another locks
    current_tasks/codegen_function_definition.txt). If two agents try to
    claim the same task, git's synchronization forces the second agent
    to pick a different one.
2.  Claude works on the task, then pulls from upstream, merges changes
    from other agents, pushes its changes, and removes the lock. Merge
    conflicts are frequent, but Claude is smart enough to figure that
    out.
3.  The infinite agent-generation-loop spawns a new Claude Code session
    in a fresh container, and the cycle repeats.

This is a very early research prototype. I haven’t yet implemented any
other method for communication between agents, nor do I enforce any
process for managing high-level goals. I don’t use an orchestration
agent.

Instead, I leave it up to each Claude agent to decide how to act. In
most cases, Claude picks up the “next most obvious” problem. When stuck
on a bug, Claude will often maintain a running doc of failed approaches
and remaining tasks. In the [git
repository](https://github.com/anthropics/claudes-c-compiler) of the
project, you can read through the history and watch it take out locks on
various tasks.

## Lessons from programming with Claude agent teams

The scaffolding runs Claude in a loop, but that loop is only useful if
Claude can tell how to make progress. Most of my effort went into
designing the environment around Claude—the tests, the environment, the
feedback—so that it could orient itself without me. These are the
approaches I’ve found most helpful when orchestrating multiple Claude
instances.

### Write extremely high-quality tests

Claude will work autonomously to solve whatever problem I give it. So
it’s important that the task verifier is nearly perfect, otherwise
Claude will solve the wrong problem. Improving the testing harness
required finding high-quality compiler test suites, writing verifiers
and build scripts for open-source software packages, and watching for
mistakes Claude was making, then designing new tests as I identified
those failure modes.

For example, near the end of the project, Claude started to frequently
break existing functionality each time it implemented a new feature. To
address this, I built a continuous integration pipeline and implemented
stricter enforcement that allowed Claude to better test its work so that
new commits can’t break existing code.

### Put yourself in Claude’s shoes

I had to constantly remind myself that I was writing this test harness
for Claude and not for myself, which meant rethinking many of my
assumptions about how tests should communicate results.

For example, each agent is dropped into a fresh container with no
context and will spend significant time orienting itself, especially on
large projects. Before we even reach the tests, to help Claude help
itself, I included instructions to maintain extensive READMEs and
progress files that should be updated frequently with the current
status.

I also kept in mind the fact that language models have inherent
limitations, which, in this case, needed to be designed around. These
include:

- **Context window pollution:** The test harness should not print
  thousands of useless bytes. At most, it should print a few lines of
  output and log all important information to a file so Claude can find
  it when needed. Logfiles should be easy to process automatically: if
  there are errors, Claude should write ERROR and put the reason on the
  same line so grep will find it. It helps to pre-compute aggregate
  summary statistics so Claude doesn't have to recompute them.
- **Time blindness:** Claude can't tell time and, left alone, will
  happily spend hours running tests instead of making progress. The
  harness prints incremental progress infrequently (to avoid polluting
  context) and includes a default `--fast `option that runs a 1% or 10%
  random sample. This subsample is deterministic per-agent but random
  across VMs, so Claude still covers all files but each agent can
  perfectly identify regressions.

### Make parallelism easy

When there are many distinct failing tests, parallelization is trivial:
each agent picks a different failing test to work on. After the test
suite reached a 99% pass rate, each agent worked on getting a different
small open-source project (e.g., SQlite, Redis, libjpeg, MQuickJS, Lua)
to compile.

But when agents started to compile the Linux kernel, they got stuck.
Unlike a test suite with hundreds of independent tests, compiling the
Linux kernel is one giant task. Every agent would hit the same bug, fix
that bug, and then overwrite each other's changes. Having 16 agents
running didn't help because each was stuck solving the same task.

The fix was to use <a href="https://gcc.gnu.org/" target="_blank"
rel="noopener noreferrer">GCC</a> as an online known-good compiler
oracle to compare against. I wrote a new test harness that randomly
compiled most of the kernel using GCC, and only the remaining files with
Claude's C Compiler. If the kernel worked, then the problem wasn’t in
Claude’s subset of the files. If it broke, then it could further refine
by re-compiling some of these files with GCC. This let each agent work
in parallel, fixing different bugs in different files, until Claude's
compiler could eventually compile all files. (After this worked, it was
still necessary to apply delta debugging techniques to find pairs of
files that failed together but worked independently.)

### Multiple agent roles

Parallelism also enables specialization. LLM-written code frequently
re-implements existing functionality, so I tasked one agent with
coalescing any duplicate code it found. I put another in charge of
improving the performance of the compiler itself, and a third I made
responsible for outputting efficient compiled code. I asked another
agent to critique the design of the project from the perspective of a
Rust developer, and make structural changes to the project to improve
the overall code quality, and another to work on documentation.

## Stress testing the limits of agent teams

This project was designed as a capability benchmark. I am interested in
stress-testing the limits of what LLMs can just *barely* achieve today
in order to help us prepare for what models will reliably achieve in the
future.

I’ve been using the C Compiler project as a benchmark across the entire
Claude 4 model series. As I did with prior projects, I started by
drafting what I wanted: a from-scratch optimizing compiler with no
dependencies, GCC-compatible, able to compile the Linux kernel, and
designed to support multiple backends. While I specified some aspects of
the design (e.g., that it should have an SSA IR to enable multiple
optimization passes) I did not go into any detail on how to do so.

Previous Opus 4 models were barely capable of producing a functional
compiler. Opus 4.5 was the first to cross a threshold that allowed it to
produce a functional compiler which could pass large test suites, but it
was still incapable of compiling any real large projects. My goal with
Opus 4.6 was to again test the limits.

### Evaluation

Over nearly 2,000 Claude Code sessions across two weeks, Opus 4.6
consumed 2 billion input tokens and generated 140 million output tokens,
a total cost just under \$20,000. Compared to even the most expensive
Claude Max plans, this was an extremely expensive project. But that
total is a fraction of what it would cost me to produce this myself—let
alone an entire team.

This was a clean-room implementation (Claude did not have internet
access at any point during its development); it depends only on the Rust
standard library. The 100,000-line compiler can build a bootable Linux
6.9 on x86, ARM, and RISC-V. It can also compile QEMU, FFmpeg, SQlite,
postgres, redis, and has a 99% pass rate on most compiler test suites
including the [GCC torture test
suite](https://gcc.gnu.org/onlinedocs/gccint/Torture-Tests.html). It
also passes the developer's ultimate litmus test: it can compile and run
Doom.

The compiler, however, is not without limitations. These include:

- It lacks the 16-bit x86 compiler that is necessary to boot Linux out
  of real mode. For this, it calls out to GCC (the x86_32 and x86_64
  compilers are its own).
- It does not have its own assembler and linker; these are the very last
  bits that Claude started automating and are still somewhat buggy. The
  demo video was produced with a GCC assembler and linker.
- The compiler successfully builds many projects, but not all. It's not
  yet a drop-in replacement for a real compiler.
- The generated code is not very efficient. Even with all optimizations
  enabled, it outputs less efficient code than GCC with all
  optimizations *disabled.*
- The Rust code quality is reasonable, but is nowhere near the quality
  of what an expert Rust programmer might produce.

The resulting compiler has nearly reached the limits of Opus’s
abilities. I tried (hard!) to fix several of the above limitations but
wasn’t fully successful. New features and bugfixes frequently broke
existing functionality.

As one particularly challenging example, Opus was unable to implement a
16-bit x86 code generator needed to boot into 16-bit real mode. While
the compiler can output correct 16-bit x86 via the 66/67 opcode
prefixes, the resulting compiled output is over 60kb, far exceeding the
32k code limit enforced by Linux. Instead, Claude simply cheats here and
calls out to GCC for this phase (This is only the case for x86. For ARM
or RISC-V, Claude’s compiler can compile completely by itself.)

The [source code for the compiler is
available](https://github.com/anthropics/claudes-c-compiler). Download
it, read through the code, and try it on your favorite C projects. I’ve
consistently found the best way to understand what language models can
do is to push them to their limits, and then study where they start to
break down. Over the coming days, I’ll continue having Claude push new
changes if you want to follow along with Claude’s continued attempts at
addressing these limitations.

## Looking forward

Each generation of language models opens up new ways of working with
them. Early models were useful for tab-completion in IDEs. Before long,
models could complete a function body from its docstring. The launch of
Claude Code brought agents into the mainstream and enabled developers to
pair-program with Claude. But each of these products operates under the
assumption that a user defines a task, an LLM runs for a few seconds or
minutes and returns an answer, and then the user provides a follow-up.

Agent teams show the possibility of implementing entire, complex
projects autonomously. This allows us, as users of these tools, to
become more ambitious with our goals.

We are still early, and fully autonomous development comes with real
risks. When a human sits with Claude during development, they can ensure
consistent quality and catch errors in real time. For autonomous
systems, it is easy to see tests pass and assume the job is done, when
this is rarely the case. I used to work in penetration testing,
exploiting vulnerabilities in products produced by large companies, and
the thought of programmers deploying software they’ve never personally
verified is a real concern.

So, while this experiment excites me, it also leaves me feeling uneasy.
Building this compiler has been some of the most fun I’ve had recently,
but I did not expect this to be anywhere near possible so early in 2026.
The rapid progress in both language models and the scaffolds we use to
interact with them opens the door to writing an enormous amount of new
code. I expect the positive applications to outweigh the negative, but
we’re entering a new world which will require new strategies to navigate
safely.

### Acknowledgements

Special thanks to Josef Bacik, Edwin Chen, Bernardo Meurer Costa, Jake
Eaton, Dan Kelley, Felix Klock, Jannet Park, Steve Weis, and many other
people across Anthropic for their assistance and contributions.

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