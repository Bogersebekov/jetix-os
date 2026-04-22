---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (978 words)
quality_grade: C
slug: modularitychapter
subcategory: unix
tags:
- unix
title: Modularitychapter
word_count: 978
---

<div class="navheader">

| Chapter 4. Modularity |  |  |
|:---|:--:|---:|
| <a href="design.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch04s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="modularitychapter"></span>Chapter 4. Modularity

</div>

<div>

### *Keeping It Clean, Keeping It Simple*

</div>

</div>

<div class="toc">

**Table of Contents**

[Encapsulation and Optimal Module Size](ch04s01.html)

[Compactness and Orthogonality](ch04s02.html)

[Compactness](ch04s02.html#compactness)

[Orthogonality](ch04s02.html#orthogonality)

[The SPOT Rule](ch04s02.html#spot_rule)

[Compactness and the Strong Single Center](ch04s02.html#id2895445)

[The Value of Detachment](ch04s02.html#id2899405)

[Software Is a Many-Layered Thing](ch04s03.html)

[Top-Down versus Bottom-Up](ch04s03.html#id2899552)

[Glue Layers](ch04s03.html#id2899777)

[Case Study: C Considered as Thin Glue](ch04s03.html#c_thin_glue)

[Libraries](ch04s04.html)

[Case Study: GIMP Plugins](ch04s04.html#gimp_plugins)

[Unix and Object-Oriented Languages](unix_and_oo.html)

[Coding for Modularity](ch04s06.html)

</div>

<div class="epigraph" xmlns="">

There are two ways of constructing a software design. One is to make it
so simple that there are obviously no deficiencies; the other is to make
it so complicated that there are no obvious deficiencies. The first
method is far more difficult.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">C. A. R. Hoare</span> *The Emperor's Old Clothes,
CACM February 1981* <span id="id2895948" class="indexterm"></span>
</span>*

</div>

There is a natural hierarchy of code-partitioning methods that has
evolved as programmers have had to manage ever-increasing levels of
complexity. In the beginning, everything was one big lump of machine
code. The earliest procedural languages brought in the notion of
partition by subroutine. Then we invented service libraries to share
common utility functions among multiple programs. Next, we invented
separated address spaces and communicating processes. Today we routinely
distribute program systems across multiple hosts separated by thousands
of miles of network cable.

The early developers of Unix were among the pioneers in software
modularity. Before them, the Rule of Modularity was computer-science
theory but not engineering practice. In *Design Rules*
\[[Baldwin-Clark](apb.html#Baldwin-Clark "[Baldwin-Clark]")\], a
path-breaking study of the economics of modularity in engineering
design, the authors use the development of the computer industry as a
case study and argue that the Unix community was in fact the first to
systematically apply modular decomposition to production software, as
opposed to hardware. Modularity of hardware has of course been one of
the foundations of engineering since the adoption of standard screw
threads in the late 1800s.

The Rule of Modularity bears amplification here: The only way to write
complex software that won't fall on its face is to build it out of
simple modules connected by well-defined interfaces, so that most
problems are local and you can have some hope of fixing or optimizing a
part without breaking the whole.

The tradition of being careful about modularity and of paying close
attention to issues like orthogonality<span id="id2896019"
class="indexterm"></span> and compactness are still much deeper in the
bone among Unix programmers than elsewhere.

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Early Unix programmers became good at modularity because they had to be. An OS is one of the most complicated pieces of code around. If it is not well structured, it will fall apart. There were a couple of early failures at building Unix that were scrapped. One can blame the early (structureless) C for this, but basically it was because the OS was too complicated to write. We needed both refinements in tools (like C structures) and good practice in using them (like Rob Pike's rules for programming) before we could tame that complexity. |   |
| --<span class="attribution"> <span class="author">Ken Thompson</span> <span id="id2896043" class="indexterm"></span> </span> |  |   |

</div>

Early Unix hackers struggled with this in many ways. In the languages of
1970 function calls were expensive, either because call semantics were
complicated (PL/1. Algol) or because the compiler was optimizing for
other things like fast inner loops at the expense of call time. Thus,
code tended to be written in big lumps. Ken and several of the other
early Unix developers knew modularity was a good idea, but they
remembered PL/1 and were reluctant to write small functions lest
performance go to hell.

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Dennis Ritchie encouraged modularity by telling all and sundry that function calls were really, really cheap in C. Everybody started writing small functions and modularizing. Years later we found out that function calls were still expensive on the PDP-11, and VAX code was often spending 50% of its time in the CALLS instruction. Dennis had lied to us! But it was too late; we were all hooked... |   |
| --<span class="attribution"> <span class="author">Steve Johnson</span> <span id="id2896096" class="indexterm"></span> </span> |  |   |

</div>

All programmers today, Unix natives or not, are taught to modularize at
the subroutine level within programs. Some learn the art of doing this
at the module or abstract-data-type level and call that ‘good design’.
The design-patterns<span id="id2896126" class="indexterm"></span>
movement is making a noble effort to push up a level from there and
discover successful design abstractions that can be applied to organize
the large-scale structure of programs.

Getting better at all these kinds of problem partitioning is a worthy
goal, and many excellent treatments of them are available elsewhere. We
shall not attempt to cover all the issues relating to modularity within
programs in too much detail: first, because that is a subject for an
entire volume (or several volumes) in itself; and second, because this
is a book about the art of <span class="emphasis">*Unix*</span>
programming.

What we will do here is examine more specifically what the Unix
tradition teaches us about how to follow the Rule of Modularity. In this
chapter, our examples will live within process units. Later, in
[Chapter 7](multiprogramchapter.html "Chapter 7. Multiprogramming"),
we'll examine the circumstances under which partitioning programs into
multiple cooperating processes is a good idea, and discuss more specific
techniques for doing that partitioning.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="design.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch04s01.html" accesskey="n">Next</a> |
| Part II. Design  | <a href="index.html" accesskey="h">Home</a> |  Encapsulation and Optimal Module Size |

</div>