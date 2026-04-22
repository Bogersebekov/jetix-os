---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_grade: A
slug: minilanguageschapter
subcategory: unix
tags:
- unix
title: Minilanguageschapter
word_count: 1105
---

<div class="navheader">

| Chapter 8. Minilanguages |  |  |
|:---|:--:|---:|
| <a href="ch07s04.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch08s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="minilanguageschapter"></span>Chapter 8. Minilanguages

</div>

<div>

### *Finding a Notation That Sings*

</div>

</div>

<div class="toc">

**Table of Contents**

[Understanding the Taxonomy of Languages](ch08s01.html)

[Applying Minilanguages](ch08s02.html)

[Case Study: sng](ch08s02.html#id2924747)

[Case Study: Regular Expressions](ch08s02.html#regexps)

[Case Study: Glade](ch08s02.html#id2933450)

[Case Study: m4](ch08s02.html#id2933775)

[Case Study: XSLT](ch08s02.html#id2934034)

[Case Study: The Documenter's Workbench Tools](ch08s02.html#id2934197)

[Case Study: fetchmail Run-Control Syntax](ch08s02.html#fetchmailrc)

[Case Study: awk](ch08s02.html#awk)

[Case Study: PostScript](ch08s02.html#id2935613)

[Case Study: bc and dc](ch08s02.html#id2935779)

[Case Study: Emacs Lisp](ch08s02.html#emacs_lisp_study)

[Case Study: JavaScript](ch08s02.html#javascript)

[Designing Minilanguages](ch08s03.html)

[Choosing the Right Complexity Level](ch08s03.html#id2936413)

[Extending and Embedding Languages](ch08s03.html#id2936650)

[Writing a Custom Grammar](ch08s03.html#id2936912)

[Macros — Beware!](ch08s03.html#macroexpansion)

[Language or Application Protocol?](ch08s03.html#id2937424)

</div>

<div class="epigraph" xmlns="">

A good notation has a subtlety and suggestiveness which at times makes
it almost seem like a live teacher.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Bertrand Russell</span> *The World of Mathematics
(1956)* <span id="id2930925" class="indexterm"></span> </span>*

</div>

One of the most consistent results from large-scale studies of error
patterns in software is that programmer error rates in defects per
hundreds of lines are largely independent of the language in which the
programmers are
coding.<sup>\[<a href="minilanguageschapter.html#ftn.id2930951" id="id2930951">78</a>\]</sup>
Higher-level languages, which allow you to get more done in fewer lines,
mean fewer bugs as well.

Unix has a long tradition of hosting little languages specialized for a
particular application domain, languages that can enable you to
drastically reduce the line count of your programs. Domain-specific
language examples include the numerous Unix typesetting languages
(*troff*, *eqn*, *tbl*, *pic*, *grap*), shell utilities (*awk*, *sed*,
*dc*, *bc*), and software development tools (*make*, *yacc*, *lex*).
There is a fuzzy boundary between domain-specific languages and the more
flexible sort of application run-control file (*sendmail*, BIND, X);
another with data-file formats; and another with scripting
languages<span id="id2931070" class="indexterm"></span> (which we'll
survey in [Chapter 14](languageschapter.html "Chapter 14. Languages")).

Historically, domain-specific languages of this kind have been called
‘little languages’ or ‘minilanguages’ in the Unix world, because early
examples were small and low in complexity relative to general-purpose
languages (all three terms for the category are in common use). But if
the application domain is complex (in that it has lots of different
primitive operations or involves manipulation of intricate data
structures), an application language for it may have to be rather more
complex than some general-purpose languages. We'll keep the traditional
term ‘minilanguage’ to emphasize that the wise course is usually to keep
these designs as small and simple as possible.

The domain-specific little language is an extremely powerful design
idea. It allows you to define your own higher-level language to specify
the appropriate methods, rules, and algorithms for the task at hand,
reducing global complexity relative to a design that uses hardwired
lower-level code for the same ends. You can get to a minilanguage design
in at least three ways, two of them good and one of them dangerous.

One right way to get there is to realize up front that you can use a
minilanguage design to push a given specification of a programming
problem up a level, into a notation that is more compact and expressive
than you could support in a general-purpose language. As with code
generation and data-driven programming, a minilanguage lets you take
practical advantage of the fact that the defect rate in your software
will be largely independent of the level of the language you are using;
more expressive languages mean shorter programs and fewer bugs.

The second right way to get to a minilanguage design is to notice that
one of your specification file formats is looking more and more like a
minilanguage — that is, it is developing complex structures and implying
actions in the application you are controlling. Is it trying to describe
control flow as well as data layouts? If so, it may be time to promote
that control flow from being implicit to being explicit in your
specification language.

The wrong way to get to a minilanguage design is to extend your way to
it, one patch and crufty added feature at a time. On this path, your
specification file keeps sprouting more implied control flow and more
tangled special-purpose structures until it has become an ad-hoc
language without your noticing it. Some legendary nightmares have been
spawned this way; the example every Unix guru will think of (and shudder
over) is the `sendmail.cf` configuration file associated with the
*sendmail* mail transport.

Sadly, most people do their first minilanguage the wrong way, and only
realize later what a mess it is. Then the question is: how to clean it
up? Sometimes the answer implies rethinking the entire application
design. Another notorious example of language-by-feature creep was the
editor *TECO*, which grew first macros and then loops and conditionals
as programmers wanted to use it to package increasingly complex editing
routines. The resulting ugliness was eventually fixed by a redesign of
the entire editor to be based on an intentional language; this is how
Emacs Lisp<span id="id2931189" class="indexterm"></span> (which we'll
survey below) evolved.

All sufficiently complicated specification files aspire to the condition
of minilanguages. Therefore, it will often be the case that your only
defense against designing a bad minilanguage is knowing how to design a
good one. This need not be a huge step or involve knowing a lot of
formal language theory; with modern tools, learning a few relatively
simple techniques and bearing good examples in mind as you design should
be sufficient.

In this chapter we'll examine all the kinds of minilanguages normally
supported under Unix, and try to identify the kinds of situation in
which each of them represents an effective design solution. This chapter
is not meant to be an exhaustive catalog of Unix languages, but rather
to bring out the design principles involved in structuring an
application around a minilanguage. We'll have much more to say about
languages for general-purpose programming in
[Chapter 14](languageschapter.html "Chapter 14. Languages").

We'll need to start by doing a little taxonomy, so we'll know what we're
talking about later on.

<div class="footnotes">

  

------------------------------------------------------------------------

<div class="footnote">

<sup>\[<a href="minilanguageschapter.html#id2930951" id="ftn.id2930951">78</a>\]</sup>
Les Hatton reports by email on the analysis in his book in preparation,
*Software Failure*: “Provided you use executable line counts for the
density measure, the injected defect densities vary less between
languages than they do between engineers by about a factor of 10”.

</div>

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch07s04.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch08s01.html" accesskey="n">Next</a> |
| Process Partitioning at the Design Level  | <a href="index.html" accesskey="h">Home</a> |  Understanding the Taxonomy of Languages |

</div>