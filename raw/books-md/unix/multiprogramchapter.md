---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (836 words)
quality_grade: C
slug: multiprogramchapter
subcategory: unix
tags:
- unix
title: Multiprogramchapter
word_count: 836
---

<div class="navheader">

| Chapter 7. Multiprogramming |  |  |
|:---|:--:|---:|
| <a href="ch06s03.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch07s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="multiprogramchapter"></span>Chapter 7. Multiprogramming

</div>

<div>

### *Separating Processes to Separate Function*

</div>

</div>

<div class="toc">

**Table of Contents**

[Separating Complexity Control from Performance Tuning](ch07s01.html)

[Taxonomy of Unix IPC Methods](ch07s02.html)

[Handing off Tasks to Specialist Programs](ch07s02.html#id2915475)

[Pipes, Redirection, and Filters](ch07s02.html#plumbing)

[Wrappers](ch07s02.html#id2921506)

[Security Wrappers and Bernstein Chaining](ch07s02.html#id2921634)

[Slave Processes](ch07s02.html#id2922002)

[Peer-to-Peer Inter-Process Communication](ch07s02.html#id2922148)

[Problems and Methods to Avoid](ch07s03.html)

[Obsolescent Unix IPC Methods](ch07s03.html#id2923376)

[Remote Procedure Calls](ch07s03.html#id2923675)

[Threads — Threat or Menace?](ch07s03.html#id2923889)

[Process Partitioning at the Design Level](ch07s04.html)

</div>

<div class="epigraph" xmlns="">

If we believe in data structures, we must believe in independent (hence
simultaneous) processing. For why else would we collect items within a
structure? Why do we tolerate languages that give us the one without the
other?

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Alan Perlis</span> *Epigrams in Programming, in ACM
SIGPLAN (Vol 17 \#9, 1982)* <span id="id2918338"
class="indexterm"></span> </span>*

</div>

The most characteristic program-modularization technique of Unix is
splitting large programs into multiple cooperating processes. This has
usually been called ‘multiprocessing’ in the Unix world, but in this
book we revive the older term ‘multiprogramming’ to avoid confusion with
multiprocessor hardware implementations.

Multiprogramming is a particularly murky area of design, one in which
there are few guidelines to good practice. Many programmers with
excellent judgment about how to break up code into subroutines
nevertheless wind up writing whole applications as monster
single-process monoliths that founder on their own internal complexity.

The Unix style of design applies the do-one-thing-well approach at the
level of cooperating programs as well as cooperating routines within a
program, emphasizing small programs connected by well-defined
interprocess communication or by shared files. Accordingly, the Unix
operating system encourages us to break our programs into simpler
subprocesses, and to concentrate on the interfaces between these
subprocesses. It does this in at least three fundamental ways:

<div class="itemizedlist">

- by making process-spawning cheap;

- by providing methods (shellouts, I/O redirection, pipes,
  message-passing, and sockets) that make it relatively easy for
  processes to communicate;

- by encouraging the use of simple, transparent, textual data
  formats<span id="id2918409" class="indexterm"></span> that can be
  passed through pipes and sockets.

</div>

Inexpensive process-spawning and easy process control are critical
enablers for the Unix style of programming. On an operating system such
as VAX VMS<span id="id2918428" class="indexterm"></span>, where starting
processes is expensive and slow and requires special privileges, one
must build monster monoliths because one has no choice. Fortunately the
trend in the Unix family has been toward lower fork(2) overhead rather
than higher. Linux<span id="id2918448" class="indexterm"></span>, in
particular, is famously efficient this way, with a process-spawn faster
than thread-spawning on many other operating
systems.<sup>\[<a href="multiprogramchapter.html#ftn.id2918458" id="id2918458">65</a>\]</sup>

Historically, many Unix programmers have been encouraged to think in
terms of multiple cooperating processes by experience with shell
programming. Shell makes it relatively easy to set up groups of multiple
processes connected by pipes<span id="id2918482"
class="indexterm"></span>, running either in background or foreground or
a mix of the two.

In the remainder of this chapter, we'll look at the implications of
cheap process-spawning and discuss how and when to apply pipes, sockets,
and other interprocess communication (IPC) methods to partition your
design into cooperating processes. (In the next chapter, we'll apply the
same separation-of-functions philosophy to interface design.)

While the benefit of breaking programs up into cooperating processes is
a reduction in global complexity, the cost is that we have to pay more
attention to the design of the protocols which are used to pass
information and commands between processes. (In software systems of all
kinds, bugs collect at interfaces.)

In [Chapter 5](textualitychapter.html "Chapter 5. Textuality") we looked
at the lower level of this design problem — how to lay out application
protocols that are transparent, flexible and extensible. But there is a
second, higher level to the problem which we blithely ignored. That is
the problem of designing state machines for each side of the
communication.

It is not hard to apply good style to the syntax of application
protocols, given models like SMTP or BEEP or XML-RPC. The real challenge
is not protocol syntax but protocol
<span class="emphasis">*logic*</span>—designing a protocol that is both
sufficiently expressive and deadlock-free. Almost as importantly, the
protocol has to be <span class="emphasis">*seen*</span> to be expressive
and deadlock-free; human beings attempting to model the behavior of the
communicating programs in their heads and verify its correctness must be
able to do so.

In our discussion, therefore, we will focus on the kinds of protocol
logic one naturally uses with each kind of interprocess communication.

<div class="footnotes">

  

------------------------------------------------------------------------

<div class="footnote">

<sup>\[<a href="multiprogramchapter.html#id2918458" id="ftn.id2918458">65</a>\]</sup>
See, for example, the results quoted in *Improving Context Switching
Performance of Idle Tasks under Linux*
\[[Appleton](apb.html#Appleton "[Appleton]")\].

</div>

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch06s03.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch07s01.html" accesskey="n">Next</a> |
| Designing for Maintainability  | <a href="index.html" accesskey="h">Home</a> |  Separating Complexity Control from Performance Tuning |

</div>