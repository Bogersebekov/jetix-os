---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (428 words)
quality_grade: C
slug: documentationchapter
subcategory: unix
tags:
- unix
title: Documentationchapter
word_count: 428
---

<div class="navheader">

| Chapter 18. Documentation |  |  |
|:---|:--:|---:|
| <a href="ch17s07.html" accesskey="p">Prev</a>  | Part IV. Community |  <a href="ch18s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="documentationchapter"></span>Chapter 18. Documentation

</div>

<div>

### *Explaining Your Code to a Web-Centric World*

</div>

</div>

<div class="toc">

**Table of Contents**

[Documentation Concepts](ch18s01.html)

[The Unix Style](ch18s02.html)

[The Large-Document Bias](ch18s02.html#id3001392)

[Cultural Style](ch18s02.html#id3001522)

[The Zoo of Unix Documentation Formats](ch18s03.html)

[troff and the Documenter's Workbench Tools](ch18s03.html#id3001604)

[TeX](ch18s03.html#id3001898)

[Texinfo](ch18s03.html#id3002206)

[POD](ch18s03.html#id3002268)

[HTML](ch18s03.html#id3002291)

[DocBook](ch18s03.html#id3002310)

[The Present Chaos and a Possible Way Out](ch18s04.html)

[DocBook](ch18s05.html)

[Document Type Definitions](ch18s05.html#id3006015)

[Other DTDs](ch18s05.html#id3006182)

[The DocBook Toolchain](ch18s05.html#db_toolchain)

[Migration Tools](ch18s05.html#id3006742)

[Editing Tools](ch18s05.html#id3007022)

[Related Standards and Practices](ch18s05.html#id3007143)

[SGML](ch18s05.html#id3007192)

[XML-DocBook References](ch18s05.html#id3007297)

[Best Practices for Writing Unix Documentation](ch18s06.html)

</div>

<div class="epigraph" xmlns="">

I've never met a human being who would want to read 17,000 pages of
documentation, and if there was, I'd kill him to get him out of the gene
pool.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Joseph Costello</span> </span>*

</div>

Unix's first application, in 1971, was as a platform for document
preparation — Bell Labs used it to prepare patent documents for filing.
Computer-driven phototypesetting was still a novel idea then, and for
years after it debuted in 1973 Joe Ossana's troff(1) formatter defined
the state of the art.

Ever since, sophisticated document formatters, typesetting software, and
page-layout programs of various sorts have been an important theme in
the Unix tradition. While troff(1) has proven surprisingly durable, Unix
has also hosted a lot of groundbreaking work in this application area.
Today, Unix developers and Unix tools are at the cutting edge of
far-reaching changes in documentation practice triggered by the advent
of the World Wide Web.

At the user-presentation level, Unix-community practice has been moving
rapidly toward ‘everything is HTML, all references are URLs’ since the
mid-1990s. Increasingly, modern Unix help browsers are simply Web
browsers that know how to parse certain specialized kinds of URLs (for
example, ‘man:ls(1)’ interprets the ls(1) man page into HTML). This
relieves the problems created by having lots of different formats for
documentation masters, but does not entirely solve them. Documentation
composers still have to grapple with issues about which master format
best meets their particular needs.

In this chapter, we'll survey the rather unfortunate surfeit of
different documentation formats and tools left behind by decades of
experimentation, and we'll develop guidelines for good practice and good
style.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch17s07.html" accesskey="p">Prev</a>  | <a href="community.html" accesskey="u">Up</a> |  <a href="ch18s01.html" accesskey="n">Next</a> |
| Portability, Open Standards, and Open Source  | <a href="index.html" accesskey="h">Home</a> |  Documentation Concepts |

</div>