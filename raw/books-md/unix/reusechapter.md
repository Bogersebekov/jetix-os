---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (603 words)
quality_grade: C
slug: reusechapter
subcategory: unix
tags:
- unix
title: Reusechapter
word_count: 603
---

<div class="navheader">

| Chapter 16. Reuse |  |  |
|:---|:--:|---:|
| <a href="ch15s08.html" accesskey="p">Prev</a>  | Part III. Implementation |  <a href="ch16s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="reusechapter"></span>Chapter 16. Reuse

</div>

<div>

### *On Not Reinventing the Wheel*

</div>

</div>

<div class="toc">

**Table of Contents**

[The Tale of J. Random Newbie](ch16s01.html)

[Transparency as the Key to Reuse](ch16s02.html)

[From Reuse to Open Source](ch16s03.html)

[The Best Things in Life Are Open](ch16s04.html)

[Where to Look?](ch16s05.html)

[Issues in Using Open-Source Software](ch16s06.html)

[Licensing Issues](ch16s07.html)

[What Qualifies as Open Source](ch16s07.html#id2991059)

[Standard Open-Source Licenses](ch16s07.html#id2993547)

[When You Need a Lawyer](ch16s07.html#id2993874)

</div>

<div class="epigraph" xmlns="">

When the superior man refrains from acting, his force is felt for a
thousand miles.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml"> *Tao
Te Ching (as popularly mistranslated)* </span>*

</div>

Reluctance to do unnecessary work is a great virtue in programmers. If
the Chinese sage Lao-Tze were alive today and still teaching the way of
the Tao, he would probably be mistranslated as: When the superior
programmer refrains from coding, his force is felt for a thousand miles.
In fact, recent translators have suggested that the Chinese term
<span class="foreignphrase">*wu-wei*</span> that has traditionally been
rendered as “inaction” or “refraining from action” should probably be
read as “least action” or “most efficient action” or “action in
accordance with natural law”, which is an even better description of
good engineering practice!

Remember the Rule of Economy. Re-inventing fire and the wheel for every
new project is terribly wasteful. Thinking time is precious and very
valuable relative to all the other inputs that go into software
development; accordingly, it should be spent solving new problems rather
than rehashing old ones for which known solutions already exist. This
attitude gives the best return both in the “soft” terms of developing
human capital and in the “hard” terms of economic return on development
investment.

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Reinventing the wheel is bad not only because it wastes time, but because reinvented wheels are often square. There is an almost irresistible temptation to economize on reinvention time by taking a shortcut to a crude and poorly-thought-out version, which in the long run often turns out to be false economy. |   |
| --<span class="attribution"> <span class="author">Henry Spencer</span> <span id="id2992698" class="indexterm"></span> </span> |  |   |

</div>

The most effective way to avoid reinventing the wheel is to borrow
someone else's design and implementation of it. In other words, to reuse
code.

Unix supports reuse at every level from individual library modules up to
entire programs, which Unix helps you script and recombine. Systematic
reuse is one of the most important distinguishing behaviors of Unix
programmers, and the experience of using Unix should teach you a habit
of trying to prototype solutions by combining existing components with a
minimum of new invention, rather than rushing to write standalone code
that will only be used once.

The virtuousness of code reuse is one of the great
apple-pie-and-motherhood verities of software development. But many
developers entering the Unix community from a basis of experience in
other operating systems have never learned (or have unlearned) the habit
of systematic reuse. Waste and duplicative work is rife, even though it
seems to be against the interests both of those who pay for code and
those who produce it. Understanding why such dysfunctional behavior
persists is the first step toward changing it.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch15s08.html" accesskey="p">Prev</a>  | <a href="implementation.html" accesskey="u">Up</a> |  <a href="ch16s01.html" accesskey="n">Next</a> |
| Combining Tools with Emacs  | <a href="index.html" accesskey="h">Home</a> |  The Tale of J. Random Newbie |

</div>