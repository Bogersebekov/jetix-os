---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: unix-expert
priority: P1
quality_grade: A
slug: index
subcategory: unix
tags:
- unix
title: Index
word_count: 2446
---

<div class="navheader">

| The Art of Unix Programming |  |  |
|:---|:--:|---:|
|   |   |  <a href="preface.html" accesskey="n">Next</a> |

------------------------------------------------------------------------

</div>

<div class="book" lang="en">

<div class="titlepage">

<div>

# <span id="id2805785"></span>The Art of Unix Programming

</div>

<div>

<div class="author">

### Eric Steven Raymond

<div class="affiliation">

<span class="orgname">
<a href="http://www.catb.org/~esr/" target="_top">Thyrsus
Enterprises</a>  
</span>

<div class="address">

  
    `<`[`esr@thyrsus.com`](mailto:esr@thyrsus.com)`>`  
    

</div>

</div>

</div>

</div>

<div>

Copyright © 2003 Eric S. Raymond

</div>

<div>

<div class="legalnotice">

This book and its on-line version are distributed under the terms of the
Creative Commons Attribution-NoDerivs 1.0 license, with the additional
proviso that the right to publish it on paper for sale or other
for-profit use is reserved to Pearson Education, Inc. A reference copy
of this license may be found at
<a href="http://creativecommons.org/licenses/by-nd/1.0/legalcode"
target="_top">http://creativecommons.org/licenses/by-nd/1.0/legalcode</a>.

</div>

</div>

<div>

<div class="legalnotice">

AIX, AS/400, DB/2, OS/2, System/360, MVS, VM/CMS, and IBM PC are
trademarks of IBM. Alpha, DEC, VAX, HP-UX, PDP, TOPS-10, TOPS-20, VMS,
and VT-100 are trademarks of Compaq. Amiga and AmigaOS are trademarks of
Amiga, Inc. Apple, Macintosh, MacOS, Newton, OpenDoc, and OpenStep are
trademarks of Apple Computers, Inc. ClearCase is a trademark of Rational
Software, Inc. Ethernet is a trademark of 3COM, Inc. Excel, MS-DOS,
Microsoft Windows and PowerPoint are trademarks of Microsoft, Inc. Java.
J2EE, JavaScript, NeWS, and Solaris are trademarks of Sun Microsystems.
SPARC is a trademark of SPARC international. Informix is a trademark of
Informix software. Itanium is a trademark of Intel. Linux is a trademark
of Linus Torvalds. Netscape is a trademark of AOL. PDF and PostScript
are trademarks of Adobe, Inc. UNIX is a trademark of The Open Group.

The photograph of Ken and Dennis in
[Chapter 2](historychapter.html "Chapter 2. History") appears courtesy
of Bell Labs/Lucent Technologies.

The epigraph on the Portability chapter is from the Bell System
Technical Journal, v57 \#6 part 2 (July-Aug. 1978) pp. 2021-2048 and is
reproduced with the permission of Bell Labs/Lucent Technologies.

</div>

</div>

<div>

<div class="revhistory">

| **Revision History** |  |  |
|:---|:---|:---|
| Revision 1.0 | 19 September 2003 | esr |
| This is the content that went to Addison-Wesley's printers. |  |  |
| Revision 0.4 | 5 February 2003 | esr |
| Release for public review. |  |  |
| Revision 0.3 | 22 January 2003 | esr |
| First eighteen-chapter draft. Manuscript walkthrough at Chapter 12. Limited release for early reviewers. |  |  |
| Revision 0.2 | 2 January 2003 | esr |
| First manuscript walkthrough at Chapter 7. Released to Dmitry Kirsanov at AW production. |  |  |
| Revision 0.1 | 16 November 2002 | esr |
| First DocBook draft, fifteen chapters. Languages rewritten to incorporate lots of feedback. Transparency, Modularity, Multiprogramming, Configuration, Interfaces, Documentation, and Open Source chapters released. Shipped to Mark Taub at AW. |  |  |
| Revision 0.0 | 1999 | esr |
| Public HTML draft, first four chapters only. |  |  |

</div>

</div>

------------------------------------------------------------------------

</div>

<div class="dedication" lang="en">

<div class="titlepage">

<div>

## <span id="id2807216"></span>Dedication

</div>

</div>

To Ken Thompson and Dennis Ritchie, because you inspired me.

</div>

<div class="toc">

**Table of Contents**

[Preface](preface.html)

[Who Should Read This Book](pr01s01.html)

[How to Use This Book](pr01s02.html)

[Related References](pr01s03.html)

[Conventions Used in This Book](pr01s04.html)

[Our Case Studies](pr01s05.html)

[Author's Acknowledgements](pr01s06.html)

I. [Context](context.html)

1\. [Philosophy](philosophychapter.html)

[Culture? What Culture?](ch01s01.html)

[The Durability of Unix](ch01s02.html)

[The Case against Learning Unix Culture](ch01s03.html)

[What Unix Gets Wrong](ch01s04.html)

[What Unix Gets Right](ch01s05.html)

[Open-Source Software](ch01s05.html#id2808846)

[Cross-Platform Portability and Open Standards](ch01s05.html#id2872776)

[The Internet and the World Wide Web](ch01s05.html#id2872827)

[The Open-Source Community](ch01s05.html#id2872945)

[Flexibility All the Way Down](ch01s05.html#id2873031)

[Unix Is Fun to Hack](ch01s05.html#id2873078)

[The Lessons of Unix Can Be Applied Elsewhere](ch01s05.html#id2873180)

[Basics of the Unix Philosophy](ch01s06.html)

[Rule of Modularity: Write simple parts connected by clean
interfaces.](ch01s06.html#id2877537)

[Rule of Clarity: Clarity is better than
cleverness.](ch01s06.html#id2877610)

[Rule of Composition: Design programs to be connected with other
programs.](ch01s06.html#id2877684)

[Rule of Separation: Separate policy from mechanism; separate interfaces
from engines.](ch01s06.html#id2877777)

[Rule of Simplicity: Design for simplicity; add complexity only where
you must.](ch01s06.html#id2877917)

[Rule of Parsimony: Write a big program only when it is clear by
demonstration that nothing else will do.](ch01s06.html#id2878022)

[Rule of Transparency: Design for visibility to make inspection and
debugging easier.](ch01s06.html#id2878054)

[Rule of Robustness: Robustness is the child of transparency and
simplicity.](ch01s06.html#id2878145)

[Rule of Representation: Fold knowledge into data, so program logic can
be stupid and robust.](ch01s06.html#id2878263)

[Rule of Least Surprise: In interface design, always do the least
surprising thing.](ch01s06.html#id2878339)

[Rule of Silence: When a program has nothing surprising to say, it
should say nothing.](ch01s06.html#id2878450)

[Rule of Repair: Repair what you can — but when you must fail, fail
noisily and as soon as possible.](ch01s06.html#id2878538)

[Rule of Economy: Programmer time is expensive; conserve it in
preference to machine time.](ch01s06.html#id2878666)

[Rule of Generation: Avoid hand-hacking; write programs to write
programs when you can.](ch01s06.html#id2878742)

[Rule of Optimization: Prototype before polishing. Get it working before
you optimize it.](ch01s06.html#rule_of_optimization)

[Rule of Diversity: Distrust all claims for one true
way.](ch01s06.html#id2879078)

[Rule of Extensibility: Design for the future, because it will be here
sooner than you think.](ch01s06.html#id2879112)

[The Unix Philosophy in One Lesson](ch01s07.html)

[Applying the Unix Philosophy](ch01s08.html)

[Attitude Matters Too](ch01s09.html)

2\. [History](historychapter.html)

[Origins and History of Unix, 1969-1995](ch02s01.html)

[Genesis: 1969–1971](ch02s01.html#genesis)

[Exodus: 1971–1980](ch02s01.html#id2879627)

[TCP/IP and the Unix Wars: 1980-1990](ch02s01.html#id2880014)

[Blows against the Empire: 1991-1995](ch02s01.html#id2886020)

[Origins and History of the Hackers, 1961-1995](hackers.html)

[At Play in the Groves of Academe: 1961-1980](hackers.html#id2886621)

[Internet Fusion and the Free Software Movement:
1981-1991](hackers.html#id2886828)

[Linux and the Pragmatist Reaction:
1991-1998](hackers.html#linux_reaction)

[The Open-Source Movement: 1998 and Onward](ch02s03.html)

[The Lessons of Unix History](ch02s04.html)

3\. [Contrasts](contrastchapter.html)

[The Elements of Operating-System Style](ch03s01.html)

[What Is the Operating System's Unifying Idea?](ch03s01.html#id2892028)

[Multitasking Capability](ch03s01.html#id2892085)

[Cooperating Processes](ch03s01.html#id2892171)

[Internal Boundaries](ch03s01.html#id2888136)

[File Attributes and Record Structures](ch03s01.html#id2888217)

[Binary File Formats](ch03s01.html#id2888298)

[Preferred User Interface Style](ch03s01.html#id2888363)

[Intended Audience](ch03s01.html#id2888484)

[Entry Barriers to Development](ch03s01.html#id2888581)

[Operating-System Comparisons](ch03s02.html)

[VMS](ch03s02.html#vms)

[MacOS](ch03s02.html#mac_os_contrast)

[OS/2](ch03s02.html#os_2)

[Windows NT](ch03s02.html#nt_contrast)

[BeOS](ch03s02.html#beos)

[MVS](ch03s02.html#mvs)

[VM/CMS](ch03s02.html#id2893777)

[Linux](ch03s02.html#linux)

[What Goes Around, Comes Around](ch03s03.html)

II\. [Design](design.html)

4\. [Modularity](modularitychapter.html)

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

5\. [Textuality](textualitychapter.html)

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

6\. [Transparency](transparencychapter.html)

[Studying Cases](ch06s01.html)

[Case Study: audacity](ch06s01.html#audacity)

[Case Study: fetchmail's -v option](ch06s01.html#fetchmail_v)

[Case Study: GCC](ch06s01.html#id2909841)

[Case Study: kmail](ch06s01.html#id2909954)

[Case Study: SNG](ch06s01.html#id2910193)

[Case Study: The Terminfo Database](ch06s01.html#id2910334)

[Case Study: Freeciv Data Files](ch06s01.html#id2914115)

[Designing for Transparency and Discoverability](ch06s02.html)

[The Zen of Transparency](ch06s02.html#zen_of_transparency)

[Coding for Transparency and Discoverability](ch06s02.html#id2914509)

[Transparency and Avoiding Overprotectiveness](ch06s02.html#id2914680)

[Transparency and Editable Representations](ch06s02.html#id2914758)

[Transparency, Fault Diagnosis, and Fault
Recovery](ch06s02.html#id2915107)

[Designing for Maintainability](ch06s03.html)

7\. [Multiprogramming](multiprogramchapter.html)

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

8\. [Minilanguages](minilanguageschapter.html)

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

9\. [Generation](generationchapter.html)

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

10\. [Configuration](configurationchapter.html)

[What Should Be Configurable?](ch10s01.html)

[Where Configurations Live](ch10s02.html)

[Run-Control Files](ch10s03.html)

[Case Study: The .netrc File](ch10s03.html#id2942210)

[Portability to Other Operating Systems](ch10s03.html#id2942358)

[Environment Variables](ch10s04.html)

[System Environment Variables](ch10s04.html#id2942463)

[User Environment Variables](ch10s04.html#id2942749)

[When to Use Environment Variables](ch10s04.html#id2942882)

[Portability to Other Operating Systems](ch10s04.html#id2947980)

[Command-Line Options](ch10s05.html)

[The -a to -z of Command-Line Options](ch10s05.html#id2948149)

[Portability to Other Operating Systems](ch10s05.html#id2950162)

[How to Choose among the Methods](ch10s06.html)

[Case Study: fetchmail](ch10s06.html#fetchmail_environment)

[Case Study: The XFree86 Server](ch10s06.html#id2950578)

[On Breaking These Rules](ch10s07.html)

11\. [Interfaces](interfacechapter.html)

[Applying the Rule of Least Surprise](ch11s01.html)

[History of Interface Design on Unix](ch11s02.html)

[Evaluating Interface Designs](ch11s03.html)

[Tradeoffs between CLI and Visual Interfaces](ch11s04.html)

[Case Study: Two Ways to Write a Calculator
Program](ch11s04.html#id2951734)

[Transparency, Expressiveness, and Configurability](ch11s05.html)

[Unix Interface Design Patterns](ch11s06.html)

[The Filter Pattern](ch11s06.html#id2957637)

[The Cantrip Pattern](ch11s06.html#id2957916)

[The Source Pattern](ch11s06.html#id2958032)

[The Sink Pattern](ch11s06.html#id2958116)

[The Compiler Pattern](ch11s06.html#id2958199)

[The ed pattern](ch11s06.html#id2958336)

[The Roguelike Pattern](ch11s06.html#id2958491)

[The ‘Separated Engine and Interface’ Pattern](ch11s06.html#id2958899)

[The CLI Server Pattern](ch11s06.html#id2959821)

[Language-Based Interface Patterns](ch11s06.html#id2959928)

[Applying Unix Interface-Design Patterns](ch11s07.html)

[The Polyvalent-Program Pattern](ch11s07.html#id2960228)

[The Web Browser as a Universal Front End](ch11s08.html)

[Silence Is Golden](ch11s09.html)

12\. [Optimization](optimizationchapter.html)

[Don't Just Do Something, Stand There!](ch12s01.html)

[Measure before Optimizing](ch12s02.html)

[Nonlocality Considered Harmful](ch12s03.html)

[Throughput vs. Latency](ch12s04.html)

[Batching Operations](ch12s04.html#id2961306)

[Overlapping Operations](ch12s04.html#id2961372)

[Caching Operation Results](ch12s04.html#binary_caches)

13\. [Complexity](complexitychapter.html)

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

III\. [Implementation](implementation.html)

14\. [Languages](languageschapter.html)

[Unix's Cornucopia of Languages](ch14s01.html)

[Why Not C?](why_not_c.html)

[Interpreted Languages and Mixed Strategies](ch14s03.html)

[Language Evaluations](ch14s04.html)

[C](ch14s04.html#c_language)

[C++](ch14s04.html#cc_language)

[Shell](ch14s04.html#sh)

[Perl](ch14s04.html#perl)

[Tcl](ch14s04.html#tcl)

[Python](ch14s04.html#python_language)

[Java](ch14s04.html#java)

[Emacs Lisp](ch14s04.html#emacs_lisp_language)

[Trends for the Future](ch14s05.html)

[Choosing an X Toolkit](ch14s06.html)

15\. [Tools](toolschapter.html)

[A Developer-Friendly Operating System](ch15s01.html)

[Choosing an Editor](ch15s02.html)

[Useful Things to Know about vi](ch15s02.html#vi_literacy)

[Useful Things to Know about Emacs](ch15s02.html#id2979540)

[The Antireligious Choice: Using Both](ch15s02.html#id2979678)

[Special-Purpose Code Generators](ch15s03.html)

[yacc and lex](ch15s03.html#id2979797)

[Case Study: Glade](ch15s03.html#id2986324)

[make: Automating Your Recipes](ch15s04.html)

[Basic Theory of make](ch15s04.html#id2986550)

[make in Non-C/C++ Development](ch15s04.html#id2986902)

[Utility Productions](ch15s04.html#id2987148)

[Generating Makefiles](ch15s04.html#id2987644)

[Version-Control Systems](ch15s05.html)

[Why Version Control?](ch15s05.html#id2988357)

[Version Control by Hand](ch15s05.html#id2988464)

[Automated Version Control](ch15s05.html#id2988503)

[Unix Tools for Version Control](ch15s05.html#id2988625)

[Runtime Debugging](ch15s06.html)

[Profiling](ch15s07.html)

[Combining Tools with Emacs](ch15s08.html)

[Emacs and make](ch15s08.html#id2989559)

[Emacs and Runtime Debugging](ch15s08.html#id2989677)

[Emacs and Version Control](ch15s08.html#id2989781)

[Emacs and Profiling](ch15s08.html#id2989869)

[Like an IDE, Only Better](ch15s08.html#id2989926)

16\. [Reuse](reusechapter.html)

[The Tale of J. Random Newbie](ch16s01.html)

[Transparency as the Key to Reuse](ch16s02.html)

[From Reuse to Open Source](ch16s03.html)

[The Best Things in Life Are Open](ch16s04.html)

[Where to Look?](ch16s05.html)

[Issues in Using Open-Source Software](ch16s06.html)

[Licensing Issues](ch16s07.html)

[What Qualifies as Open Source](ch16s07.html#id2991059)

[Standard Open-Source Licenses](ch16s07.html#id2993547)

[When You Need a Lawyer](ch16s07.html#id2993874)

IV\. [Community](community.html)

17\. [Portability](portabilitychapter.html)

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

18\. [Documentation](documentationchapter.html)

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

19\. [Open Source](opensourcechapter.html)

[Unix and Open Source](ch19s01.html)

[Best Practices for Working with Open-Source Developers](ch19s02.html)

[Good Patching Practice](ch19s02.html#patching)

[Good Project- and Archive-Naming Practice](ch19s02.html#naming)

[Good Development Practice](ch19s02.html#develpractice)

[Good Distribution-Making Practice](ch19s02.html#distpractice)

[Good Communication Practice](ch19s02.html#communication)

[The Logic of Licenses: How to Pick One](ch19s03.html)

[Why You Should Use a Standard License](ch19s04.html)

[Varieties of Open-Source Licensing](ch19s05.html)

[MIT or X Consortium License](ch19s05.html#id3014860)

[BSD Classic License](ch19s05.html#id3014890)

[Artistic License](ch19s05.html#id3014963)

[General Public License](ch19s05.html#id3015011)

[Mozilla Public License](ch19s05.html#id3015063)

20\. [Futures](futurechapter.html)

[Essence and Accident in Unix Tradition](ch20s01.html)

[Plan 9: The Way the Future Was](plan9.html)

[Problems in the Design of Unix](ch20s03.html)

[A Unix File Is Just a Big Bag of Bytes](ch20s03.html#id3015538)

[Unix Support for GUIs Is Weak](ch20s03.html#id3015724)

[File Deletion Is Forever](ch20s03.html#id3015838)

[Unix Assumes a Static File System](ch20s03.html#id3015895)

[The Design of Job Control Was Badly Botched](ch20s03.html#id3015943)

[The Unix API Doesn't Use Exceptions](ch20s03.html#id3016077)

[ioctl2 and fcntl2 Are an Embarrassment](ch20s03.html#id3016155)

[The Unix Security Model May Be Too Primitive](ch20s03.html#id3019078)

[Unix Has Too Many Different Kinds of Names](ch20s03.html#id3019113)

[File Systems Might Be Considered Harmful](ch20s03.html#id3019140)

[Towards a Global Internet Address Space](ch20s03.html#id3019193)

[Problems in the Environment of Unix](ch20s04.html)

[Problems in the Culture of Unix](ch20s05.html)

[Reasons to Believe](ch20s06.html)

A. [Glossary of Abbreviations](apa.html)

B. [References](apb.html)

C. [Contributors](apc.html)

D. [Rootless Root](unix_koans.html)

[Editor's Introduction](introduction.html)

[Master Foo and the Ten Thousand Lines](ten-thousand.html)

[Master Foo and the Script Kiddie](script-kiddie.html)

[Master Foo Discourses on the Two Paths](two_paths.html)

[Master Foo and the Methodologist](methodology-consultant.html)

[Master Foo Discourses on the Graphical User
Interface](gui-programmer.html)

[Master Foo and the Unix Zealot](zealot.html)

[Master Foo Discourses on the Unix-Nature](unix-nature.html)

[Master Foo and the End User](end-user.html)

</div>

<div class="list-of-figures">

**List of Figures**

2.1. [The PDP-7.](ch02s01.html#pdp7)

3.1. [Schematic history of timesharing.](ch03s02.html#os-history)

4.1. [Qualitative plot of defect count and density vs. module
size.](ch04s01.html#hatton)

4.2. [Caller/callee relationships in GIMP with a plugin
loaded.](ch04s04.html#libgimp)

6.1. [Screen shot of audacity.](ch06s01.html#id2909476)

6.2. [Screen shot of kmail.](ch06s01.html#id2910036)

6.3. [Main window of a Freeciv game.](ch06s01.html#id2914147)

8.1. [Taxonomy of languages.](ch08s01.html#taxonomy)

11.1. [The xcalc GUI.](ch11s04.html#xcalc)

11.2. [Screen shot of the original Rogue game.](ch11s06.html#rogue)

11.3. [The Xcdroast GUI.](ch11s06.html#id2959548)

11.4. [Caller/callee relationships in a polyvalent
program.](ch11s07.html#id2960323)

13.1. [Sources and kinds of
complexity.](ch13s01.html#complexity-sources)

18.1. [Processing structural documents.](ch18s05.html#docfig1)

18.2. [Present-day XML-DocBook toolchain.](ch18s05.html#docfig2)

18.3. [Future XML-DocBook toolchain with FOP.](ch18s05.html#docfig3)

</div>

<div class="list-of-tables">

**List of Tables**

8.1. [Regular-expression examples.](ch08s02.html#regexp_table)

8.2. [Introduction to regular-expression
operations.](ch08s02.html#regexp_intro)

14.1. [Language choices.](ch14s05.html#lang_usage)

14.2. [Summary of X Toolkits.](ch14s06.html#x_toolkits)

</div>

<div class="list-of-examples">

**List of Examples**

5.1. [Password file example.](ch05s01.html#passwd)

5.2. [A .newsrc example.](ch05s01.html#newsrc)

5.3. [A fortune file example.](ch05s02.html#fortune)

5.4. [Basic data for three planets in a record-jar
format.](ch05s02.html#planets)

5.5. [An XML example.](ch05s02.html#xml_example)

5.6. [A .INI file example.](ch05s02.html#ini_example)

5.7. [An SMTP session example.](ch05s03.html#smtp_example)

5.8. [A POP3 example session.](ch05s03.html#pop_example)

5.9. [An IMAP session example.](ch05s03.html#imap_example)

6.1. [An example fetchmail -v
transcript.](ch06s01.html#fetchmail_session)

6.2. [An SNG Example.](ch06s01.html#SNG_Example)

7.1. [The pic2graph pipeline.](ch07s02.html#pic2graph)

8.1. [Glade Hello, World.](ch08s02.html#glade_example)

8.2. [A sample m4 macro.](ch08s02.html#m4_macro)

8.3. [A sample XSLT program.](ch08s02.html#xslt_example)

8.4. [Taxonomy of languages — the pic source.](ch08s02.html#pic_source)

8.5. [Synthetic example of a fetchmailrc.](ch08s02.html#hogwarts)

8.6. [RSA implementation using dc.](ch08s02.html#rsa)

9.1. [Example of fetchmailrc syntax.](ch09s01.html#fetchmail_example)

9.2. [Python structure dump of a fetchmail
configuration.](ch09s01.html#conf_dump)

9.3. [copy_instance metaclass code.](ch09s01.html#solution_code)

9.4. [Calling context for copy_instance.](ch09s01.html#solution_caller)

9.5. [ascii usage screen.](ch09s02.html#ascii-splash)

9.6. [Desired output format for the star table.](ch09s02.html#star_list)

9.7. [Master form of the star table.](ch09s02.html#colon_table)

10.1. [A .netrc example.](ch10s03.html#netrc)

10.2. [X configuration example.](ch10s06.html#X_config)

18.1. [groff1 markup example.](ch18s03.html#troffexample1)

18.2. [man markup example.](ch18s03.html#man_example)

19.1. [tar archive maker production.](ch19s02.html#tar_trick)

</div>

</div>

<div class="navfooter">

------------------------------------------------------------------------

|     |     |                                                |
|:----|:---:|-----------------------------------------------:|
|     |     |  <a href="preface.html" accesskey="n">Next</a> |
|     |     |                                        Preface |

</div>