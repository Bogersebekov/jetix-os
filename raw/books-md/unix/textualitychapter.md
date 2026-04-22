---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_flags:
- too_short (929 words)
quality_grade: C
slug: textualitychapter
subcategory: unix
tags:
- unix
title: Textualitychapter
word_count: 929
---

<div class="navheader">

| Chapter 5. Textuality |  |  |
|:---|:--:|---:|
| <a href="ch04s06.html" accesskey="p">Prev</a>  | Part II. Design |  <a href="ch05s01.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="chapter" lang="en">

<div class="titlepage">

<div>

## <span id="textualitychapter"></span>Chapter 5. Textuality

</div>

<div>

### *Good Protocols Make Good Practice*

</div>

</div>

<div class="toc">

**Table of Contents**

[The Importance of Being Textual](ch05s01.html)

[Case Study: Unix Password File Format](ch05s01.html#id2901332)

[Case Study: .newsrc Format](ch05s01.html#id2901494)

[Case Study: The PNG Graphics File Format](ch05s01.html#png)

[Data File Metaformats](ch05s02.html)

[DSV Style](ch05s02.html#id2901882)

[RFC 822 Format](ch05s02.html#id2902039)

[Cookie-Jar Format](ch05s02.html#id2902164)

[Record-Jar Format](ch05s02.html#id2906931)

[XML](ch05s02.html#id2907018)

[Windows INI Format](ch05s02.html#id2907263)

[Unix Textual File Format Conventions](ch05s02.html#id2907428)

[The Pros and Cons of File Compression](ch05s02.html#id2907903)

[Application Protocol Design](ch05s03.html)

[Case Study: SMTP, the Simple Mail Transfer
Protocol](ch05s03.html#id2908194)

[Case Study: POP3, the Post Office Protocol](ch05s03.html#id2908383)

[Case Study: IMAP, the Internet Message Access
Protocol](ch05s03.html#id2908582)

[Application Protocol Metaformats](ch05s04.html)

[The Classical Internet Application
Metaprotocol](ch05s04.html#id2908835)

[HTTP as a Universal Application Protocol](ch05s04.html#id2908915)

[BEEP: Blocks Extensible Exchange Protocol](ch05s04.html#id2909217)

[XML-RPC, SOAP, and Jabber](ch05s04.html#id2909294)

</div>

<div class="epigraph" xmlns="">

It's a well-known fact that computing devices such as the abacus were
invented thousands of years ago. But it's not well known that the first
use of a common computer protocol occurred in the Old Testament. This,
of course, was when Moses aborted the Egyptians' process with a
control-sea.

--*<span class="attribution" xmlns="http://www.w3.org/1999/xhtml">
<span class="author">Tom Galloway</span> *`rec.arts.comics`, February
1992* <span id="id2906216" class="indexterm"></span> </span>*

</div>

In this chapter, we'll look at what the Unix tradition has to tell us
about two different kinds of design that are closely related: the design
of file formats for retaining application data in permanent storage, and
the design of application protocols for passing data and commands
between cooperating programs, possibly over a network.

What unifies these two kinds of design is that they both involve the
serialization of in-memory data structures. For the internal operation
of computer programs, the most convenient representation of a complex
data structure is one in which all fields have the machine's native data
format (e.g. two's-complement binary for integers) and all pointers are
actual memory addresses (as opposed, say, to being named references).
But these representations are not well suited to storage and
transmission; memory addresses in the data structure lose their meaning
outside memory, and emitting raw native data formats causes
interoperability problems passing data between machines with different
conventions (big- vs. little-endian, say, or 32-bit vs. 64-bit).

For transmission and storage, the traversable, quasi-spatial layout of
data structures like linked lists needs to be flattened or serialized
into a byte-stream representation from which the structure can later be
recovered. The serialization (save) operation is sometimes called
*marshaling* and its inverse (load) operation *unmarshaling*. These
terms are usually applied with respect to objects in an
OO<span id="id2906281" class="indexterm"></span> language like
C++<span id="id2906289" class="indexterm"></span> or
Python<span id="id2906296" class="indexterm"></span> or
Java<span id="id2906304" class="indexterm"></span>, but could be used
with equal justice of operations like loading a graphics file into the
internal storage of a graphics editor and saving it out after
modifications.

A significant percentage of what C<span id="id2906320"
class="indexterm"></span> and C++<span id="id2906328"
class="indexterm"></span> programmers maintain is ad-hoc code for
marshaling and unmarshaling operations — even when the serialized
representation chosen is as simple as a binary structure dump (a common
technique under non-Unix environments). Modern languages like
Python<span id="id2906341" class="indexterm"></span> and
Java<span id="id2906350" class="indexterm"></span> tend to have built-in
unmarshal and marshal functions that can be applied to any object or
byte-stream representing an object, and that reduce this labor
substantially.

But these naïve methods are often unsatisfactory for various reasons,
including both the machine-interoperability problems we mentioned above
and the negative trait of being opaque to other tools. When the
application is a network protocol, economy may demand that an internal
data structure (such as, say, a message with source and destination
addresses) be serialized not into a single blob of data but into a
series of attempted transactions or messages which the receiving machine
may reject (so that, for example, a large message can be rejected if the
destination address is invalid).

Interoperability, transparency<span id="id2906381"
class="indexterm"></span>, extensibility<span id="id2906393"
class="indexterm"></span>, and storage or transaction economy: these are
the important themes in designing file formats and application
protocols. Interoperability and transparency demand that we focus such
designs on clean data representations, rather than putting convenience
of implementation or highest possible performance first. Extensibility
also favors textual protocols, since binary ones are often harder to
extend or subset cleanly. Transaction economy sometimes pushes in the
opposite direction — but we shall see that putting that criterion first
is a form of premature optimization<span id="id2906412"
class="indexterm"></span> that it is often wise to resist.

Finally, we must note a difference between data file formats and the
run-control files that are often used to set the startup options of Unix
programs. The most basic difference is that (with sporadic exceptions
like GNU Emacs's configuration interface) programs don't normally modify
their own run-control files — the information flow is one-way, from file
read at startup time to application settings. Data-file formats, on the
other hand, associate properties with named resources and are both read
and written by their applications. Configuration files are generally
hand-edited and small, whereas data files are program-generated and can
become arbitrarily large.

Historically, Unix has related but different sets of conventions for
these two kinds of representation. The conventions for run control files
are surveyed in
[Chapter 10](configurationchapter.html "Chapter 10. Configuration");
only conventions for data files are examined in this chapter.

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch04s06.html" accesskey="p">Prev</a>  | <a href="design.html" accesskey="u">Up</a> |  <a href="ch05s01.html" accesskey="n">Next</a> |
| Coding for Modularity  | <a href="index.html" accesskey="h">Home</a> |  The Importance of Being Textual |

</div>