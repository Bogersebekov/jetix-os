---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_grade: A
slug: plan9
subcategory: unix
tags:
- unix
title: Plan9
word_count: 1100
---

<div class="navheader">

| Plan 9: The Way the Future Was |  |  |
|:---|:--:|---:|
| <a href="ch20s01.html" accesskey="p">Prev</a>  | Chapter 20. Futures |  <a href="ch20s03.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="sect1" lang="en">

<div class="titlepage">

<div>

## <span id="plan9"></span>Plan 9: The Way the Future Was

</div>

</div>

<span id="id3015182" class="indexterm"></span>

We know what Unix's future used to look like. It was designed by the
research group at Bell Labs that built Unix and called ‘Plan 9 from Bell
Labs’.<sup>\[<a href="plan9.html#ftn.id3015199" id="id3015199">154</a>\]</sup>
Plan 9 was an attempt to do Unix over again, better.

The central design challenge the designers attempted to meet in Plan 9
was integrating graphics and ubiquitous networking into a comfortable
Unix-like framework. They kept the Unix choice to mediate access to as
many system services as possible through a single big file-hierarchy
name space. In fact, they improved on it; many facilities that under
Unix are accessed through various ad-hoc interfaces like BSD sockets,
fcntl(2), and ioctl(2) are in Plan 9 accessed through ordinary read and
write operations on special files analogous to device files. For
portability and ease of access, almost all device interfaces are textual
rather than binary. Most system services (including, for example, the
window system) are *file servers* containing special files or directory
trees representing the served resources. By representing all resources
as files, Plan 9 turns the problem of accessing resources on different
servers into the problem of accessing files on different servers.

Plan 9 combined this more-Unix-than-Unix file model with a new concept:
private name spaces. Every user (in fact, every process) can have its
own view of the system's services by creating its own tree of
file-server mounts. Some of the file server mounts will have been
manually set up by the user, and others automatically set up at login
time. So (as the *Plan 9 from Bell Labs* survey paper points out)
“`/dev/cons` always refers to your terminal device and `/bin/date` to
the correct version of the date command to run, but which files those
names represent depends on circumstances such as the architecture of the
machine executing **date**”.

The single most important feature of Plan 9 is that all mounted file
servers export the same file-system-like interface, regardless of the
implementation behind them. Some might correspond to local file systems,
some to remote file systems accessed over a network, some to instances
of system servers running in user space (like the window system or an
alternate network stack), and some to kernel interfaces. To users and
client programs, all these cases look alike.

One of the examples from the Plan 9 survey paper is the way FTP access
to remote sites is implemented. There is no ftp(1) command under Plan 9.
Instead there is an *ftpfs* fileserver, and each FTP connection looks
like a file system mount. *ftpfs* automatically translates open, read,
and write commands on files and directories under the mount point into
FTP protocol transactions. Thus, all ordinary file-handling tools such
as ls(1), mv(1) and cp(1) simply work, both underneath the FTP mount
point and across the boundaries with the rest of the user's view of the
namespace. The only difference the user (or his scripts and programs)
will notice is retrieval speed.

Plan 9 has much else to recommend it, including the reinvention of some
of the more problematic areas of the Unix system-call interface, the
elimination of superuser, and many other interesting rethinkings. Its
pedigree is impeccable, its design elegant, and it exposes some
significant errors in the design of Unix. Unlike most efforts at a
second system, it produced an architecture that was in many ways simpler
and more elegant than its predecessor. Why didn't it take over the
world?

One could argue for a lot of specific reasons — lack of any serious
effort to market it, scanty documentation, much confusion and stumbling
over fees and licensing. For those unfamiliar with Plan 9, it seemed to
function mainly as a device for generating interesting papers on
operating-systems research. But Unix itself had previously surmounted
all these sorts of obstacles to attract a dedicated following that
spread it worldwide. Why didn't Plan 9?

The long view of history may tell a different story, but in 2003 it
looks like Plan 9 failed simply because it fell short of being a
compelling enough improvement on Unix to displace its ancestor. Compared
to Plan 9, Unix creaks and clanks and has obvious rust spots, but it
gets the job done well enough to hold its position. There is a lesson
here for ambitious system architects: the most dangerous enemy of a
better solution is an existing codebase that is just good enough.

Some Plan 9 ideas have been absorbed into modern Unixes, particularly
the more innovative open-source versions. FreeBSD has a `/proc` file
system modeled exactly on that of Plan 9 that can be used to query or
control running processes. FreeBSD's rfork(2) and Linux's clone(2)
system calls are modeled on Plan 9's rfork(2). Linux's `/proc` file
system, in addition to presenting process information, holds a variety
of synthesized Plan 9-like device files used to query and control kernel
internals using predominantly textual interfaces. Experimental 2003
versions of Linux are implementing per-process mount points, a long step
toward Plan 9's private namespaces. The various open-source Unixes are
all moving toward systemwide support for UTF-8, an encoding actually
invented for Plan
9.<sup>\[<a href="plan9.html#ftn.id3015486" id="id3015486">155</a>\]</sup>

It may well be that over time, much more of Plan 9 will work its way
into Unix as various portions of Unix's architecture slide into
senescence. This is one possible line of development for Unix's future.

<div class="footnotes">

  

------------------------------------------------------------------------

<div class="footnote">

<sup>\[<a href="plan9.html#id3015199" id="ftn.id3015199">154</a>\]</sup>
The name is a tribute to the 1958 movie that has passed into legend as
“the worst ever made”, *Plan 9 from Outer Space*. (The legend is,
unfortunately, incorrect, as the few who have seen an even worse
stinkeroo from 1966 called *Manos: The Hands of Fate* can attest.)
Documentation, including a survey paper describing the architecture,
along with complete source code and a distribution that installs on PCs,
can be readily found with a Web search for the phrase ‘Plan 9 from Bell
Labs’.

</div>

<div class="footnote">

<sup>\[<a href="plan9.html#id3015486" id="ftn.id3015486">155</a>\]</sup>
The tale of how UTF-8 was born involves
<a href="http://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt"
target="_top">Ken Thompson, Rob Pike, a new Jersey diner, and a frenzied
overnight hack</a>.

</div>

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|  |  |  |
|:---|:--:|---:|
| <a href="ch20s01.html" accesskey="p">Prev</a>  | <a href="futurechapter.html" accesskey="u">Up</a> |  <a href="ch20s03.html" accesskey="n">Next</a> |
| Essence and Accident in Unix Tradition  | <a href="index.html" accesskey="h">Home</a> |  Problems in the Design of Unix |

</div>