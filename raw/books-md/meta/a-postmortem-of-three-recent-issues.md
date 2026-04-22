---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: a-postmortem-of-three-recent-issues
subcategory: meta
tags:
- meta
title: A Postmortem Of Three Recent Issues
word_count: 2411
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
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/0321b0ecbbf53535e93be1310ae1935157bcebdd-1000x1000.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="1000" height="1000" />

</div>

# A postmortem of three recent issues

</div>

<div class="HeroEngineering-module-scss-module__j1ivRa__metadata">

Published Sep 17, 2025

This is a technical report on three bugs that intermittently degraded
responses from Claude. Below we explain what happened, why it took time
to fix, and what we're changing.

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

Between August and early September, three infrastructure bugs
intermittently degraded Claude's response quality. We've now resolved
these issues and want to explain what happened.

In early August, a number of users began reporting degraded responses
from Claude. These initial reports were difficult to distinguish from
normal variation in user feedback. By late August, the increasing
frequency and persistence of these reports prompted us to open an
investigation that led us to uncover three separate infrastructure bugs.

To state it plainly: We never reduce model quality due to demand, time
of day, or server load. The problems our users reported were due to
infrastructure bugs alone.

We recognize users expect consistent quality from Claude, and we
maintain an extremely high bar for ensuring infrastructure changes don't
affect model outputs. In these recent incidents, we didn't meet that
bar. The following postmortem explains what went wrong, why detection
and resolution took longer than we would have wanted, and what we're
changing to prevent similar future incidents.

We don't typically share this level of technical detail about our
infrastructure, but the scope and complexity of these issues justified a
more comprehensive explanation.

## How we serve Claude at scale

We serve Claude to millions of users via our first-party API, Amazon
Bedrock, and Google Cloud's Vertex AI. We deploy Claude across multiple
hardware platforms, namely AWS Trainium, NVIDIA GPUs, and Google TPUs.
This approach provides the capacity and geographic distribution
necessary to serve users worldwide.

Each hardware platform has different characteristics and requires
specific optimizations. Despite these variations, we have strict
equivalence standards for model implementations. Our aim is that users
should get the same quality responses regardless of which platform
serves their request. This complexity means that any infrastructure
change requires careful validation across all platforms and
configurations.

## Timeline of events

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd707dfc2effceba608d04007bc776132a3e57838-3840x1800.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd707dfc2effceba608d04007bc776132a3e57838-3840x1800.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="3840" height="1800"
alt="Illustrative timeline of events on the Claude API. Yellow: issue detected, Red: degradation worsened, Green: fix deployed." />
<figcaption aria-hidden="true">Illustrative timeline of events on the
<strong>Claude API</strong>. Yellow: issue detected, Red: degradation
worsened, Green: fix deployed.</figcaption>
</figure>

</div>

The overlapping nature of these bugs made diagnosis particularly
challenging. The first bug was introduced on August 5, affecting
approximately 0.8% of requests made to Sonnet 4. Two more bugs arose
from deployments on August 25 and 26.

Although initial impacts were limited, a load balancing change on August
29 started to increase affected traffic. This caused many more users to
experience issues while others continued to see normal performance,
creating confusing and contradictory reports.

## Three overlapping issues

Below we describe the three bugs that caused the degradation, when they
occurred, and how we resolved them:

### 1. Context window routing error

On August 5, some Sonnet 4 requests were misrouted to servers configured
for the upcoming [1M
token](https://docs.claude.com/en/docs/build-with-claude/context-windows#1m-token-context-window)
[context
window](https://docs.claude.com/en/docs/build-with-claude/context-windows).
This bug initially affected 0.8% of requests. On August 29, a routine
load balancing change unintentionally increased the number of
short-context requests routed to the 1M context servers. At the worst
impacted hour on August 31, 16% of Sonnet 4 requests were affected.

Approximately 30% of Claude Code users who made requests during this
period had at least one message routed to the wrong server type,
resulting in degraded responses. On Amazon Bedrock, misrouted traffic
peaked at 0.18% of all Sonnet 4 requests from August 12. Incorrect
routing affected less than 0.0004% of requests on Google Cloud's Vertex
AI between August 27 and September 16.

However, some users were affected more severely, as our routing is
"sticky". This meant that once a request was served by the incorrect
server, subsequent follow-ups were likely to be served by the same
incorrect server.

**Resolution:** We fixed the routing logic to ensure short- and
long-context requests were directed to the correct server pools. We
deployed the fix on September 4. Rollout to our first-party platform and
Google Cloud's Vertex AI was completed by September 16, and to AWS
Bedrock by September 18.

### 2. Output corruption

On August 25, we deployed a misconfiguration to the Claude API TPU
servers that caused an error during token generation. An issue caused by
a runtime performance optimization occasionally assigned a high
probability to tokens that should rarely be produced given the context,
for example producing Thai or Chinese characters in response to English
prompts, or producing obvious syntax errors in code. A small subset of
users that asked a question in English might have seen "สวัสดี" in the
middle of the response, for example.

This corruption affected requests made to Opus 4.1 and Opus 4 on August
25-28, and requests to Sonnet 4 August 25–September 2. Third-party
platforms were not affected by this issue.

**Resolution:** We identified the issue and rolled back the change on
September 2. We've added detection tests for unexpected character
outputs to our deployment process.

### 3. Approximate top-k XLA:TPU miscompilation

On August 25, we deployed code to improve how Claude selects tokens
during text generation. This change inadvertently triggered a latent bug
in the XLA:TPU<sup>\[1\]</sup> compiler, which has been confirmed to
affect requests to Claude Haiku 3.5.

We also believe this could have impacted a subset of Sonnet 4 and Opus 3
on the Claude API. Third-party platforms were not affected by this
issue.

**Resolution:** We first observed the bug affecting Haiku 3.5 and rolled
it back on September 4. We later noticed user reports of problems with
Opus 3 that were compatible with this bug, and rolled it back on
September 12. After extensive investigation we were unable to reproduce
this bug on Sonnet 4 but decided to also roll it back out of an
abundance of caution.

Simultaneously, we have (a) been working with the XLA:TPU team on a fix
for the compiler bug and (b) rolled out a fix to use exact top-k with
enhanced precision. For details, see the deep dive below.

## A closer look at the XLA compiler bug

To illustrate the complexity of these issues, here's how the XLA
compiler bug manifested and why it proved particularly challenging to
diagnose.

When Claude generates text, it calculates probabilities for each
possible next word, then randomly chooses a sample from this probability
distribution. We use "top-p sampling" to avoid nonsensical outputs—only
considering words whose cumulative probability reaches a threshold
(typically 0.99 or 0.999). On TPUs, our models run across multiple
chips, with probability calculations happening in different locations.
To sort these probabilities, we need to coordinate data between chips,
which is complex.<sup>\[2\]</sup>

In December 2024, we discovered our TPU implementation would
occasionally drop the most probable token when
[temperature](https://docs.claude.com/en/docs/about-claude/glossary#temperature)
was zero. We deployed a workaround to fix this case.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fefee0d3d25f6b03cbfc57e70e0e364dcd8b82fe0-2000x500.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fefee0d3d25f6b03cbfc57e70e0e364dcd8b82fe0-2000x500.png&amp;w=2048&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fefee0d3d25f6b03cbfc57e70e0e364dcd8b82fe0-2000x500.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="2000" height="500"
alt="Code snippet of a December 2024 patch to work around the unexpected dropped token bug when temperature = 0." />
<figcaption aria-hidden="true">Code snippet of a December 2024 patch to
work around the unexpected dropped token bug when temperature =
0.</figcaption>
</figure>

</div>

The root cause involved mixed precision arithmetic. Our models compute
next-token probabilities in
[bf16](https://github.com/tensorflow/tensorflow/blob/f41959ccb2d9d4c722fe8fc3351401d53bcf4900/tensorflow/core/framework/bfloat16.h)
(16-bit floating point). However, the vector processor is
[fp32-native](https://dl.acm.org/doi/pdf/10.1145/3360307), so the TPU
compiler (XLA) can optimize runtime by converting some operations to
fp32 (32-bit). This optimization pass is guarded by the
`xla_allow_excess_precision` flag which defaults to true.

This caused a mismatch: operations that should have agreed on the
highest probability token were running at different precision levels.
The precision mismatch meant they didn't agree on which token had the
highest probability. This caused the highest probability token to
sometimes disappear from consideration entirely.

On August 26, we deployed a rewrite of our sampling code to fix the
precision issues and improve how we handled probabilities at the limit
that reach the top-p threshold. But in fixing these problems, we exposed
a trickier one.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6d10e58c0bd5fd7cb03dc0adc716cb1e4f039343-2000x2560.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6d10e58c0bd5fd7cb03dc0adc716cb1e4f039343-2000x2560.png&amp;w=2048&amp;q=75amp;qhttps://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6d10e58c0bd5fd7cb03dc0adc716cb1e4f039343-2000x2560.png&amp;w=3840&amp;q=75;w=3840&amp;q=75 2x"
width="2000" height="2560"
alt="Code snippet showing minimized reproducer merged as part of the August 11 change that root-caused the “bug” being worked around in December 2024; in reality, it’s expected behavior of the xla_allow_excess_precision flag." />
<figcaption>Code snippet showing a minimized reproducer merged as part
of the August 11 change that root-caused the "bug" being worked around
in December 2024. In reality, it’s expected behavior of the
<code>xla_allow_excess_precision</code> flag.</figcaption>
</figure>

</div>

Our fix removed the December workaround because we believed we'd solved
the root cause. This led to a deeper bug in the [approximate
top-k](https://docs.jax.dev/en/latest/_autosummary/jax.lax.approx_max_k.html)
operation—a performance optimization that quickly finds the highest
probability tokens.<sup>\[3\]</sup> This approximation sometimes
returned completely wrong results, but only for certain batch sizes and
model configurations. The December workaround had been inadvertently
masking this problem.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7e42db934d0e84ea40fc56b416ddb09b2097a5ff-2400x1404.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7e42db934d0e84ea40fc56b416ddb09b2097a5ff-2400x1404.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="2400" height="1404"
alt="Slack message showing reproducer of the underlying approximate top-k bug shared with the XLA:TPU engineers who developed the algorithm. The code returns correct results when run on CPUs." />
<figcaption>Reproducer of the underlying approximate top-k bug shared
with the XLA:TPU engineers who <a
href="https://arxiv.org/pdf/2206.14286">developed the algorithm</a>. The
code returns correct results when run on CPUs.</figcaption>
</figure>

</div>

The bug's behavior was frustratingly inconsistent. It changed depending
on unrelated factors such as what operations ran before or after it, and
whether debugging tools were enabled. The same prompt might work
perfectly on one request and fail on the next.

While investigating, we also discovered that the exact top-k operation
no longer had the prohibitive performance penalty it once did. We
switched from approximate to exact top-k and standardized some
additional operations on fp32 precision.<sup>\[4\]</sup> Model quality
is non-negotiable, so we accepted the minor efficiency impact.

## Why detection was difficult

Our validation process ordinarily relies on benchmarks alongside safety
evaluations and performance metrics. Engineering teams perform spot
checks and deploy to small "canary" groups first.

These issues exposed critical gaps that we should have identified
earlier. The evaluations we ran simply didn't capture the degradation
users were reporting, in part because Claude often recovers well from
isolated mistakes. Our own privacy practices also created challenges in
investigating reports. Our internal privacy and security controls limit
how and when engineers can access user interactions with Claude, in
particular when those interactions are not reported to us as feedback.
This protects user privacy but prevents engineers from examining the
problematic interactions needed to identify or reproduce bugs.

Each bug produced different symptoms on different platforms at different
rates. This created a confusing mix of reports that didn't point to any
single cause. It looked like random, inconsistent degradation.

More fundamentally, we relied too heavily on noisy evaluations. Although
we were aware of an increase in reports online, we lacked a clear way to
connect these to each of our recent changes. When negative reports
spiked on August 29, we didn't immediately make the connection to an
otherwise standard load balancing change.

## What we're changing

As we continue to improve our infrastructure, we're also improving the
way we evaluate and prevent bugs like those discussed above across all
platforms where we serve Claude. Here's what we're changing:

- **More sensitive evaluations:** To help discover the root cause of any
  given issue, we’ve developed evaluations that can more reliably
  differentiate between working and broken implementations. We’ll keep
  improving these evaluations to keep a closer eye on model quality.
- **Quality evaluations in more places:** Although we run regular
  evaluations on our systems, we will run them continuously on true
  production systems to catch issues such as the context window load
  balancing error.
- **Faster debugging tooling:** We'll develop infrastructure and tooling
  to better debug community-sourced feedback without sacrificing user
  privacy. Additionally, some bespoke tools developed here will be used
  to reduce the remediation time in future similar incidents, if those
  should occur.

Evals and monitoring are important. But these incidents have shown that
we also need continuous signal from users when responses from Claude
aren't up to the usual standard. Reports of specific changes observed,
examples of unexpected behavior encountered, and patterns across
different use cases all helped us isolate the issues.

It remains particularly helpful for users to continue to send us their
feedback directly. You can use the `/bug` command in Claude Code or you
can use the "thumbs down" button in the Claude apps to do so. Developers
and researchers often create new and interesting ways to evaluate model
quality that complement our internal testing. If you'd like to share
yours, reach out to <feedback@anthropic.com>.

We remain grateful to our community for these contributions.

#### Acknowledgments

Written by Sam McAllister, with thanks to Stuart Ritchie, Jonathan Gray,
Kashyap Murali, Brennan Saeta, Oliver Rausch, Alex Palcuie, and many
others.

<sup>\[1\]</sup> XLA:TPU is the optimizing compiler that translates
[XLA](https://openxla.org/xla/architecture) High Level Optimizing
language—often written using [JAX](https://docs.jax.dev/en/latest)—to
TPU machine instructions.

<sup>\[2\]</sup> Our models are too large for single chips and are
partitioned across tens of chips or more, making our sorting operation a
distributed sort. TPUs (just like GPUs and Trainium) also have different
performance characteristics than CPUs, requiring different
implementation techniques using vectorized operations instead of serial
algorithms.

<sup>\[3\]</sup> We had been using this approximate operation because it
yielded substantial performance improvements. The approximation works by
accepting potential inaccuracies in the lowest probability tokens, which
shouldn't affect quality—except when the bug caused it to drop the
highest probability token instead.

<sup>\[4\]</sup> Note that the now-correct top-k implementation may
result in slight differences in the inclusion of tokens near the top-p
threshold, and in rare cases users may benefit from re-tuning their
choice of top-p.

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