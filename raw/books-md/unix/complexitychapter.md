---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (354 words)
quality_grade: C
slug: complexitychapter
subcategory: unix
tags:
- unix
title: Complexitychapter
word_count: 354
---

<div class="navheader">

| Chapter 13. Complexity |  |  |
|:---|:--:|---:|
| <a href="ch12s04.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch13s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="complexitychapter"></span>Chapter 13. Complexity

</div>

<div>

### *As Simple As Possible, but No Simpler*

</div>

</div>

<div class="toc">

**Table of Contents**

[Speaking of Complexity](ch13s01.html)

[The Three Sources of Complexity](ch13s01.html#id2964646)

[Tradeoffs between Interface and Implementation
Complexity](ch13s01.html#id2964843)

[Essential, Optional, and Accidental Complexity](ch13s01.html#id2961759)

[Mapping Complexity](ch13s01.html#id2961870)

[When Simplicity Is Not Enough](ch13s01.html#id2963237)

[A Tale of Five Editors](ch13s02.html)

[ed](ch13s02.html#id2963445)

[vi](ch13s02.html#vi_complexity)

[Sam](ch13s02.html#id2963798)

[Emacs](ch13s02.html#emacs_editing)

[Wily](ch13s02.html#id2967110)

[The Right Size for an Editor](ch13s03.html)

[Identifying the Complexity Problems](ch13s03.html#id2967267)

[Compromise Doesn't Work](ch13s03.html#id2967642)

[Is Emacs an Argument against the Unix
Tradition?](ch13s03.html#id2967765)

[The Right Size of Software](ch13s04.html)

</div>

<div class="epigraph" xmlns="">

Everything should be made as simple as possible, but no simpler.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Albert Einstein</span> <span id="id2964548"
class="indexterm"></span> </span>*

</div>

At the end of
[Chapter 1](philosophychapter.html "Chapter 1. Philosophy"), we
summarized the Unix philosophy as “Keep It Simple, Stupid!” Throughout
the Design section, one of the continuing themes has been the importance
of keeping designs and implementations as simple as possible. But what
<span class="emphasis">*is*</span> “as simple as possible”? How do you
tell?

We've held off on addressing this question until now because
understanding simplicity is complicated. It needs some of the ideas we
developed earlier in the Design section, especially in
[Chapter 4](modularitychapter.html "Chapter 4. Modularity") and
[Chapter 11](interfacechapter.html "Chapter 11. Interfaces"), as
background.

The large questions in this chapter are central preoccupations of the
Unix tradition, some of them motivating holy wars that have simmered for
decades. This chapter starts from established Unix practice and
vocabulary, then goes a bit further beyond it than we do in the rest of
the book. We don't try to develop simple answers to these questions,
because there aren't any — but we can hope that you will walk away with
better conceptual tools for developing your own answers.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch12s04.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch13s01.html" accesskey="n">Next</a> |
| Throughput vs. Latency  | <a href="index.html" accesskey="h">Home</a> |  Speaking of Complexity |

</div>