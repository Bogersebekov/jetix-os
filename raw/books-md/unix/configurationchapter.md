---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (223 words)
quality_grade: C
slug: configurationchapter
subcategory: unix
tags:
- unix
title: Configurationchapter
word_count: 223
---

<div class="navheader">

| Chapter 10. Configuration |  |  |
|:---|:--:|---:|
| <a href="ch09s02.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch10s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="configurationchapter"></span>Chapter 10. Configuration

</div>

<div>

### *Starting on the Right Foot*

</div>

</div>

<div class="toc">

**Table of Contents**

[What Should Be Configurable?](ch10s01.html)

[Where Configurations Live](ch10s02.html)

[Run-Control Files](ch10s03.html)

[Case Study: The .netrc File](ch10s03.html#id2942210)

[Portability to Other Operating Systems](ch10s03.html#id2942358)

[Environment Variables](ch10s04.html)

[System Environment Variables](ch10s04.html#id2942463)

[User Environment Variables](ch10s04.html#id2942749)

[When to Use Environment Variables](ch10s04.html#id2942882)

[Portability to Other Operating Systems](ch10s04.html#id2947980)

[Command-Line Options](ch10s05.html)

[The -a to -z of Command-Line Options](ch10s05.html#id2948149)

[Portability to Other Operating Systems](ch10s05.html#id2950162)

[How to Choose among the Methods](ch10s06.html)

[Case Study: fetchmail](ch10s06.html#fetchmail_environment)

[Case Study: The XFree86 Server](ch10s06.html#id2950578)

[On Breaking These Rules](ch10s07.html)

</div>

<div class="epigraph" xmlns="">

Let us watch well our beginnings, and results will manage themselves.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Alexander Clark</span> </span>*

</div>

Under Unix, programs can communicate with their environment in a rich
variety of ways. It's convenient to divide these into (a)
startup-environment queries and (b) interactive channels. In this
chapter, we'll focus primarily on startup-environment queries. The next
chapter will discuss interactive channels.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch09s02.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch10s01.html" accesskey="n">Next</a> |
| Ad-hoc Code Generation  | <a href="index.html" accesskey="h">Home</a> |  What Should Be Configurable? |

</div>