---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (698 words)
quality_grade: C
slug: portabilitychapter
subcategory: unix
tags:
- unix
title: Portabilitychapter
word_count: 698
---

<div class="navheader">

| Chapter 17. Portability |  |  |
|:---|:--:|---:|
| <a href="community.html" accesskey="p">Prev</a>  | Part IV. Community |  <a href="c_evolution.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="portabilitychapter"></span>Chapter 17. Portability

</div>

<div>

### *Software Portability and Keeping Up Standards*

</div>

</div>

<div class="toc">

**Table of Contents**

[Evolution of C](c_evolution.html)

[Early History of C](c_evolution.html#id2998213)

[C Standards](c_evolution.html#id2994334)

[Unix Standards](ch17s02.html)

[Standards and the Unix Wars](ch17s02.html#id2994594)

[The Ghost at the Victory Banquet](ch17s02.html#id2999310)

[Unix Standards in the Open-Source World](ch17s02.html#id2999366)

[IETF and the RFC Standards Process](ietf_process.html)

[Specifications as DNA, Code as RNA](ch17s04.html)

[Programming for Portability](ch17s05.html)

[Portability and Choice of Language](ch17s05.html#id3000303)

[Avoiding System Dependencies](ch17s05.html#id3000882)

[Tools for Portability](ch17s05.html#id3000984)

[Internationalization](ch17s06.html)

[Portability, Open Standards, and Open Source](ch17s07.html)

</div>

<div class="epigraph" xmlns="">

The realization that the operating systems of the target machines were
as great an obstacle to portability as their hardware architecture led
us to a seemingly radical suggestion: to evade that part of the problem
altogether by moving the operating system itself.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="ERROR">\<authorgroup\><span class="author">Steve
Johnson</span><span class="author">Dennis
Ritchie</span>\</authorgroup\></span> *Portability of C Programs and the
UNIX System (1978)* <span id="id2998019" class="indexterm"></span>
<span id="id2998026" class="indexterm"></span> </span>*

</div>

Unix was the first production operating system to be ported between
differing processor families (Version 6 Unix, 1976-77). Today, Unix is
routinely ported to every new machine powerful enough to sport a
memory-management unit. Unix applications are routinely moved between
Unixes running on wildly differing hardware; in fact, it is unheard of
for a port to fail.

Portability has always been one of Unix's principal advantages. Unix
programmers tend to write on the assumption that hardware is evanescent
and only the Unix API is stable, making as few assumptions as possible
about machine specifics such as word length, endianness or memory
architecture. In fact, code that is hardware-dependent in any way that
goes beyond the abstract machine model of C<span id="id2998066"
class="indexterm"></span> is considered bad form in Unix circles, and
only really tolerated in very special cases like operating system
kernels.

Unix programmers have learned that it is easy to be wrong when
anticipating that a software project will have a short
lifetime.<sup>\[<a href="portabilitychapter.html#ftn.id2998082" id="id2998082">141</a>\]</sup>
Thus, they tend to avoid making software dependent on specific and
perishable technologies, and to lean heavily on open standards. These
habits of writing for portability are so ingrained in the Unix tradition
that they are applied even to small single-use projects that are thought
of as throwaway code. They have had secondary effects all through the
design of the Unix development toolkit, and on programming languages
like Perl and Python and Tcl that were developed under Unix.

The direct benefit of portability is that it is normal for Unix software
to outlive its original hardware platform, so tools and applications
don't have to be reinvented every few years. Today, applications
originally written for Version 7 Unix (1979) are routinely used not
merely on Unixes genetically descended from V7, but on variants like
Linux<span id="id2998121" class="indexterm"></span> in which the
operating system API was written from a Unix specification and shares no
code with the Bell Labs source tree.

The indirect benefits are less obvious but may be more important. The
discipline of portability tends to exert a simplifying influence on
architectures, interfaces, and implementations. This both increases the
odds of project success and reduces life-cycle maintenance costs.

In this chapter, we'll survey the scope and history of Unix standards.
We'll discuss which ones are still relevant today and describe the areas
of greater and lesser variance in the Unix API. We'll examine the tools
and practices that Unix developers use to keep code portable, and
develop some guides to good practice.

<div class="footnotes">

  

------------------------------------------------------------------------

<div class="footnote">

<sup>\[<a href="portabilitychapter.html#id2998082" id="ftn.id2998082">141</a>\]</sup>
PDP-7 Unix and Linux were both examples of unexpected persistence. Unix
originated as a research toy hacked together by some researchers between
projects, half to play with file-system ideas and half to host a game.
The second was summed up by its creator as “My terminal emulator grew
legs” \[[Torvalds](apb.html#Torvalds "[Torvalds]")\].

</div>

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="community.html" accesskey="p">Prev</a>  | <a href="community.html" accesskey="u">Up</a> |  <a href="c_evolution.html" accesskey="n">Next</a> |
| Part IV. Community  | <a href="index.html" accesskey="h">Home</a> |  Evolution of C |

</div>