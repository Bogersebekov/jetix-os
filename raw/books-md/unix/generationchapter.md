---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (613 words)
quality_grade: C
slug: generationchapter
subcategory: unix
tags:
- unix
title: Generationchapter
word_count: 613
---

<div class="navheader">

| Chapter 9. Generation |  |  |
|:---|:--:|---:|
| <a href="ch08s03.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch09s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="generationchapter"></span>Chapter 9. Generation

</div>

<div>

### *Pushing the Specification Level Upwards*

</div>

</div>

<div class="toc">

**Table of Contents**

[Data-Driven Programming](ch09s01.html)

[Case Study: ascii](ch09s01.html#id2939746)

[Case Study: Statistical Spam Filtering](ch09s01.html#bayes_spam)

[Case Study: Metaclass Hacking in
fetchmailconf](ch09s01.html#fetchmailconf)

[Ad-hoc Code Generation](ch09s02.html)

[Case Study: Generating Code for the ascii
Displays](ch09s02.html#id2938615)

[Case Study: Generating HTML Code for a Tabular
List](ch09s02.html#htmlgen)

</div>

<div class="epigraph" xmlns="">

The programmer at wit's end ... can often do best by disentangling
himself from his code, rearing back, and contemplating his data.
Representation is the essence of programming.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Fred Brooks</span> *The Mythical Man-Month,
Anniversary Edition (1975-1995), p. 103* <span id="id2939500"
class="indexterm"></span> </span>*

</div>

In [Chapter 1](philosophychapter.html "Chapter 1. Philosophy") we
observed that human beings are better at visualizing data than they are
at reasoning about control flow. We recapitulate: To see this, compare
the expressiveness and explanatory power of a diagram of a fifty-node
pointer tree with a flowchart of a fifty-line program. Or (better) of an
array initializer expressing a conversion table with an equivalent
switch statement. The difference in transparency<span id="id2939533"
class="indexterm"></span> and clarity is
dramatic.<sup>\[<a href="generationchapter.html#ftn.id2939543" id="id2939543">97</a>\]</sup>

Data is more tractable than program logic. That's true whether the data
is an ordinary table, a declarative markup language, a templating
system, or a set of macros that will expand to program logic. It's good
practice to move as much of the complexity in your design as possible
away from procedural code and into data, and good practice to pick data
representations that are convenient for humans to maintain and
manipulate. Translating those representations into forms that are
convenient for machines to process is another job for machines, not for
humans.

<div class="blockquote">

|  |  |  |
|----|----|----|
|   | Another important advantage of higher-level, more declarative notations is that they lend themselves better to compile-time checking. Procedural notations inherently have complex runtime behavior which is difficult to analyze at compile time. Declarative notations give the implementation much more leverage for finding mistakes, by permitting much more thorough understanding of the intended behavior. |   |
| --<span class="attribution"> <span class="author">Henry Spencer</span> <span id="id2939580" class="indexterm"></span> </span> |  |   |

</div>

These insights ground in theory a set of practices that have always been
an important part of the Unix programmer's toolkit — very high-level
languages, data-driven programming, code generators, and domain-specific
minilanguages. What unifies these is that they are all ways of lifting
the generation of code up some levels, so that specifications can be
smaller. We've previously noted that defect densities tend to be nearly
constant across programming languages; all these practices mean that
whatever malign forces generate our bugs will get fewer lines to wreak
their havoc on.

In [Chapter 8](minilanguageschapter.html "Chapter 8. Minilanguages") we
discussed the uses of domain-specific minilanguages. In
[Chapter 14](languageschapter.html "Chapter 14. Languages") we'll make
the argument for very-high-level languages<span id="id2939637"
class="indexterm"></span>. In this chapter we'll look at some design
studies in data-driven programming and a few examples of ad-hoc code
generation; we'll look at some code-generation tools in
[Chapter 15](toolschapter.html "Chapter 15. Tools"). As with
minilanguages, these methods can enable you to drastically cut the line
count of your programs, and correspondingly lower debugging time and
maintenance costs.

<div class="footnotes">

  

------------------------------------------------------------------------

<div class="footnote">

<sup>\[<a href="generationchapter.html#id2939543" id="ftn.id2939543">97</a>\]</sup>
For further development of this point see
\[[Bentley](apb.html#Bentley "[Bentley]")\].

</div>

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch08s03.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch09s01.html" accesskey="n">Next</a> |
| Designing Minilanguages  | <a href="index.html" accesskey="h">Home</a> |  Data-Driven Programming |

</div>