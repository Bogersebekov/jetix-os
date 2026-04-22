---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_grade: A
slug: c_evolution
subcategory: unix
tags:
- unix
title: C_Evolution
word_count: 1561
---

<div class="navheader">

| Evolution of C |  |  |
|:---|:--:|---:|
| <a href="portabilitychapter.html" accesskey="p">Prev</a>  | Chapter 17. Portability |  <a href="ch17s02.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="sect1" lang="en">

<div class="titlepage">

<div>

## <span id="c_evolution"></span>Evolution of C

</div>

</div>

<span id="id2998161" class="indexterm"></span>

The central fact of the Unix programming experience has always been the
stability of the C language and the handful of service interfaces that
always travel with it (notably, the standard I/O library and friends).
The fact that a language originated in 1973 has required as little
change as this one has in thirty years of heavy use is truly remarkable,
and without parallels anywhere else in computer science or engineering.

In [Chapter 4](modularitychapter.html "Chapter 4. Modularity"), we
argued that C has been successful because it acts as a layer of thin
glue over computer hardware approximating the “standard architecture” of
\[[BlaauwBrooks](apb.html#BlaauwBrooks "[BlaauwBrooks]")\]. There is, of
course, more to the story than that. To understand the rest of the
story, we'll need to take a brief look at the history of C.

<div class="sect2" lang="en">

<div class="titlepage">

<div>

### <span id="id2998213"></span>Early History of C

</div>

</div>

C began life in 1971 as a systems-programming language for the
PDP-11<span id="id2998222" class="indexterm"></span> port of Unix, based
on Ken Thompson's<span id="id2998234" class="indexterm"></span> earlier
B interpreter which had in turn been modeled on BCPL, the Basic Common
Programming Language designed at Cambridge University in
1966-67.<sup>\[<a href="c_evolution.html#ftn.id2998245" id="id2998245">142</a>\]</sup>

Dennis Ritchie's<span id="id2998269" class="indexterm"></span> original
C compiler (often called the “DMR” compiler after his initials) served
the rapidly growing community around Unix versions 5, 6, and 7. Version
6 C spawned Whitesmiths C, a reimplementation that became the first
commercial C compiler and the nucleus of IDRIS, the first Unix
workalike. But most modern C implementations are patterned on Steven C.
Johnson's “portable C compiler” (PCC) which debuted in Version 7 and
replaced the DMR compiler entirely in both System V<span id="id2998294"
class="indexterm"></span> and the BSD 4.x<span id="id2998302"
class="indexterm"></span> releases.

In 1976, Version 6 C introduced the `typedef`, `union`, and
`unsigned int` declarations. The approved syntax for variable
initializations and some compound operators also changed.

The original description of C was Brian Kernighan and Dennis M.
Ritchie's<span id="id2994041" class="indexterm"></span> original *The C
Programming Language* aka “the White Book”
\[[Kernighan-Ritchie](apb.html#Kernighan-Ritchie "[Kernighan-Ritchie]")\].
It was published in 1978, the same year the Whitemiths C compiler became
available.

The White Book described enhanced Version 6 C, with one significant
exception involving the handling of public storage. Ritchie's original
intention had been to model C's rules on FORTRAN COMMON declarations, on
the theory that any machine that could handle FORTRAN would be ready for
C. In the common-block model, a public variable may be declared multiple
times; identical declarations are merged by the linker. But two early C
ports (to Honeywell and IBM 360 mainframes) happened to be to machines
with very limited common storage or a primitive linker or both. Thus,
the Version 6 C compiler was moved to the stricter definition-reference
model (requiring at most one definition of any given public variable and
the **extern** keyword tagging references to it) described in
\[[Kernighan-Ritchie](apb.html#Kernighan-Ritchie "[Kernighan-Ritchie]")\].

This decision was reversed in the C compiler that shipped with Version 7
after it developed that a great deal of existing source depended on the
looser rules. Pressure for backward-compatibility would foil yet another
attempt to switch (in 1983's System V Release 1<span id="id2994104"
class="indexterm"></span>) before the ANSI Draft Standard finally
settled on definition-reference rules in 1988. Common-block public
storage is still admitted as an acceptable variation by the standard.

V7 C introduced `enum` and treated `struct` and `union` values as
first-class objects that could be assigned, passed as arguments, and
returned from functions (rather than being passed around by address).

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Another major change in V7 was that Unix data structure declarations were now documented on header files, and included. Previous Unixes had actually printed the data structures (e.g., for directories) in the manual, from which people would copy it into their code. Needless to say, this was a major portability problem. |   |
| --<span class="attribution"> <span class="author">Steve Johnson</span> <span id="id2994167" class="indexterm"></span> </span> |  |   |

</div>

The System III<span id="id2994191" class="indexterm"></span> C version
of the PCC compiler (which also shipped with BSD
4.1c<span id="id2994201" class="indexterm"></span>) changed the handling
of struct declarations so that members with the same names in different
structs would not clash. It also introduced `void` and `unsigned char`
declarations. The scope of `extern` declarations local to a function was
restricted to the function, and no longer included all code following
it.

The ANSI C Draft Proposed Standard added `const` (for read-only storage)
and `volatile` (for locations such as memory-mapped I/O registers that
might be modified asynchronously from the thread of program control).
The `unsigned` type modifier was generalized to apply to any type, and a
symmetrical `signed` was added. Initialization syntax for `auto` array
and structure initializers and `union` types was added. Most
importantly, function prototypes were added.

The most important changes in early C were the switch to
definition-reference and the introduction of function prototypes in the
Draft Proposed ANSI C Standard. The language has been essentially stable
since copies of the X3J11 committee's working papers on the Draft
Proposed Standard signaled the committee's intentions to compiler
implementers in 1985-1986.

A more detailed history of early C, written by its designer, can be
found at \[[Ritchie93](apb.html#Ritchie93 "[Ritchie93]")\].

</div>

<div class="sect2" lang="en">

<div class="titlepage">

<div>

### <span id="id2994334"></span>C Standards

</div>

</div>

C standards development has been a conservative process with great care
taken to preserve the spirit of the original C language, and an emphasis
on ratifying experiments in existing compilers rather than inventing new
features. The C9X
charter<sup>\[<a href="c_evolution.html#ftn.id2994347" id="id2994347">143</a>\]</sup>
document is an excellent expression of this mission.

Work on the first official C standard began in 1983 under the auspices
of the X3J11 ANSI committee. The major functional additions to the
language were settled by the end of 1986, at which point it became
common for programmers to distinguish between “K&R C” and “ANSI C”.

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Many people don't realize how <span class="emphasis">*unusual*</span> the C standardization effort, especially the original ANSI C work, was in its insistence on standardizing only tested features. Most language standard committees spend much of their time inventing new features, often with little consideration of how they might be implemented. Indeed, the few ANSI C features that <span class="emphasis">*were*</span> invented from scratch — e.g., the notorious “trigraphs”—were the most disliked and least successful features of C89. |   |
| --<span class="attribution"> <span class="author">Henry Spencer</span> <span id="id2994392" class="indexterm"></span> </span> |  |   |

</div>

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Void pointers were invented as part of the standards effort, and have been a winner. But Henry's point is still well taken. |   |
| --<span class="attribution"> <span class="author">Steve Johnson</span> <span id="id2994442" class="indexterm"></span> </span> |  |   |

</div>

While the core of ANSI C was settled early, arguments over the contents
of the standard libraries dragged on for years. The formal standard was
not issued until the end of 1989, well after most compilers had
implemented the 1985 recommendations. The standard was originally known
as ANSI X3.159, but was redesignated ISO/IEC 9899:1990 when the
International Standards Organization (ISO) took over sponsorship in
1990. The language variant it describes is generally known as C89 or
C90.

The first book on C and Unix portability practice, *Portable C and Unix
Systems Programming* \[[Lapin](apb.html#Lapin "[Lapin]")\], was
published in 1987 (I wrote it under a corporate pseudonym forced on me
by my employers at the time). The Second Edition of
\[[Kernighan-Ritchie](apb.html#Kernighan-Ritchie "[Kernighan-Ritchie]")\]
came out in 1988.

A very minor revision of C89, known as Amendment 1, AM1, or C93, was
floated in 1993. It added more support for wide characters and Unicode.
This became ISO/IEC 9899-1:1994.

Revision of the C89 standard began in 1993. In 1999, ISO/IEC 9899
(generally known as C99) was adopted by ISO. It incorporated Amendment
1, and added a great many minor features. Perhaps the most significant
one for most programmers is the C++-like ability to declare variables at
any point in a block, rather than just at the beginning. Macros with a
variable number of arguments were also added.

The C9X working group has a
<a href="http://anubis.dkuug.dk/JTC1/SC22/WG14/www/projects"
target="_top">Web page</a>, but no third standards effort is planned as
of mid-2003. They are developing an addendum on C for embedded systems.

Standardization of C has been greatly aided by the fact that working and
largely compatible implementations were running on a wide variety of
systems before standards work was begun. This made it harder to argue
about what features should be in the standard.

</div>

<div class="footnotes">

  

------------------------------------------------------------------------

<div class="footnote">

<sup>\[<a href="c_evolution.html#id2998245" id="ftn.id2998245">142</a>\]</sup>
The ‘C’ in C therefore stands for Common — or, perhaps, for
‘Christopher’. BCPL originally stood for “Bootstrap CPL”—a much
simplified version of CPL, the very interesting but overly ambitious and
never implemented Common Programming Language of Oxford and Cambridge,
also known affectionately as “Christopher's Programming Language” after
its prime advocate, computer-science pioneer Christopher Strachey.

</div>

<div class="footnote">

<sup>\[<a href="c_evolution.html#id2994347" id="ftn.id2994347">143</a>\]</sup>
<a href="http://anubis.dkuug.dk/JTC1/SC22/WG14/www/charter"
target="_top">Available on the Web</a>.

</div>

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="portabilitychapter.html" accesskey="p">Prev</a>  | <a href="portabilitychapter.html" accesskey="u">Up</a> |  <a href="ch17s02.html" accesskey="n">Next</a> |
| Chapter 17. Portability  | <a href="index.html" accesskey="h">Home</a> |  Unix Standards |

</div>