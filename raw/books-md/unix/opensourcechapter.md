---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (370 words)
quality_grade: C
slug: opensourcechapter
subcategory: unix
tags:
- unix
title: Opensourcechapter
word_count: 370
---

<div class="navheader">

| Chapter 19. Open Source |  |  |
|:---|:--:|---:|
| <a href="ch18s06.html" accesskey="p">Prev</a>  | Part IV. Community |  <a href="ch19s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="opensourcechapter"></span>Chapter 19. Open Source

</div>

<div>

### *Programming in the New Unix Community*

</div>

</div>

<div class="toc">

**Table of Contents**

[Unix and Open Source](ch19s01.html)

[Best Practices for Working with Open-Source Developers](ch19s02.html)

[Good Patching Practice](ch19s02.html#patching)

[Good Project- and Archive-Naming Practice](ch19s02.html#naming)

[Good Development Practice](ch19s02.html#develpractice)

[Good Distribution-Making Practice](ch19s02.html#distpractice)

[Good Communication Practice](ch19s02.html#communication)

[The Logic of Licenses: How to Pick One](ch19s03.html)

[Why You Should Use a Standard License](ch19s04.html)

[Varieties of Open-Source Licensing](ch19s05.html)

[MIT or X Consortium License](ch19s05.html#id3014860)

[BSD Classic License](ch19s05.html#id3014890)

[Artistic License](ch19s05.html#id3014963)

[General Public License](ch19s05.html#id3015011)

[Mozilla Public License](ch19s05.html#id3015063)

</div>

<div class="epigraph" xmlns="">

Software is like sex — it's better when it's free.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Linus Torvalds</span> <span id="id3009416"
class="indexterm"></span> </span>*

</div>

We concluded [Chapter 2](historychapter.html "Chapter 2. History") by
observing the largest-scale pattern in Unix's history; it flourished
when its practices most closely approximated open source, and stagnated
when they did not. We then asserted in
[Chapter 16](reusechapter.html "Chapter 16. Reuse") that open-source
development tools tend to be of high quality. We'll begin this chapter
by sketching an explanation of how and why open-source development
works. Most of its behaviors are simply intensifications of
long-established Unix-tradition practices.

We'll then descend from realm of abstraction and describe some of the
most important folk customs that Unix has picked up from the open-source
community — in particular, the community-evolved guidelines for what a
good source-code release looks like. Many of these customs could be
profitably adopted by developers on other modern operating systems as
well.

We'll describe these customs on the assumption that you are developing
open source; most are still good ideas even if you are writing
proprietary software. The open-source assumption is also historically
appropriate, because many of these customs found their way back into
proprietary Unix shops via ubiquitous open-source tools like patch(1),
*Emacs*, and GCC<span id="id3009490" class="indexterm"></span>.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch18s06.html" accesskey="p">Prev</a>  | <a href="community.html" accesskey="u">Up</a> |  <a href="ch19s01.html" accesskey="n">Next</a> |
| Best Practices for Writing Unix Documentation  | <a href="index.html" accesskey="h">Home</a> |  Unix and Open Source |

</div>