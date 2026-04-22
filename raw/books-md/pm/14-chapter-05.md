---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: pm-expert
priority: P1
quality_grade: A
slug: 14-chapter-05
subcategory: pm
tags:
- pm
title: 14 Chapter 05
word_count: 3674
---

<div id="main" class="wb" role="main">

**Heads up!** This page uses features your browser doesn’t support. Try
a modern browser like
<a href="https://www.mozilla.org/en-US/firefox/new/" target="_blank"
rel="noopener noreferrer">Firefox</a> or
<a href="https://www.google.com/chrome/" target="_blank"
rel="noopener noreferrer">Chrome</a> for the best experience.

<div class="intro">

<div class="intro__content intro__content--sticky">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld2JveD0iMCAwIDExMiA4MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMi4zNyAxMy42M2E3LjcxIDcuNzEgMCAwIDEgLTIuMzctNS42MyA3LjczIDcuNzMgMCAwIDEgMi4zNy01LjYzIDcuNzEgNy43MSAwIDAgMSA1LjYzLTIuMzdoOTZhNy43MyA3LjczIDAgMCAxIDUuNjMgMi4zNyA3LjczIDcuNzMgMCAwIDEgMi4zNyA1LjYzIDcuNzEgNy43MSAwIDAgMSAtMi4zNyA1LjYzIDcuNzMgNy43MyAwIDAgMSAtNS42MyAyLjM3aC05NmE3LjcxIDcuNzEgMCAwIDEgLTUuNjMtMi4zN3ptMTA3LjI2IDIwLjc1YTggOCAwIDAgMSAtNS42MyAxMy42MmgtOTZhNy43MSA3LjcxIDAgMCAxIC01LjYzLTIuMzcgNy44NiA3Ljg2IDAgMCAxIDAtMTEuMjUgNy42OCA3LjY4IDAgMCAxIDUuNjMtMi4zOGg5NmE3LjcgNy43IDAgMCAxIDUuNjMgMi4zOHptMCAzMmE4IDggMCAwIDEgLTUuNjMgMTMuNjJoLTk2YTcuNzEgNy43MSAwIDAgMSAtNS42My0yLjM3IDcuODYgNy44NiAwIDAgMSAwLTExLjI1IDcuNjggNy42OCAwIDAgMSA1LjYzLTIuMzhoOTZhNy43IDcuNyAwIDAgMSA1LjYzIDIuMzh6IiAvPjwvc3ZnPg=="
class="icon" /> Shape Up

Chapter 5:

# [Risks and Rabbit Holes](1.4-chapter-05.html)

- [Different categories of
  risk](1.4-chapter-05.html#different-categories-of-risk)
- [Look for rabbit holes](1.4-chapter-05.html#look-for-rabbit-holes)
- [Case study: Patching a
  hole](1.4-chapter-05.html#case-study-patching-a-hole)
- [Declare out of bounds](1.4-chapter-05.html#declare-out-of-bounds)
- [Cut back](1.4-chapter-05.html#cut-back)
- [Present to technical
  experts](1.4-chapter-05.html#present-to-technical-experts)
- [De-risked and ready to write
  up](1.4-chapter-05.html#de-risked-and-ready-to-write-up)

[Next: Write the Pitch](1.5-chapter-06.html)

</div>

</div>

<div class="content" controller="bookmark anchors tweet"
data-target="sidebar.content"
data-action="click-&gt;sidebar#close mouseup-&gt;tweet#update input-&gt;tweet#update keydown-&gt;tweet#update scroll@window-&gt;tweet#update"
bookmark-id="/shapeup">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiBpY29uLS1saW5rIiB2aWV3Ym94PSIwIDAgODUuNjkgODUuNjkiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTQ5LjcxIDY1LjYxYy43OCAwIDEuMjUuMTQgMS40Mi40MnMwIC42OS0uNTkgMS4yNWwtMTEuNzEgMTEuNzJhMjEuOTQgMjEuOTQgMCAwIDEgLTE2LjA3IDYuNjkgMjEuOTQgMjEuOTQgMCAwIDEgLTE2LjA3LTYuNjkgMjIuNjUgMjIuNjUgMCAwIDEgMC0zMi4xNGwxNi4wNy0xNi4wN2EyMS4zOCAyMS4zOCAwIDAgMSA1LjUyLTQgMjEuNTUgMjEuNTUgMCAwIDEgMTAuNTUtMi42OWguMzNhMjYuNjggMjYuNjggMCAwIDEgOC4zNyAxLjY3di4xN2ExMy40OSAxMy40OSAwIDAgMSAyLjg1IDEuMzQgMjIuMDkgMjIuMDkgMCAwIDEgNC41MiAzLjUxIDUuNjkgNS42OSAwIDEgMSAtOCA4IDExLjMxIDExLjMxIDAgMCAwIC0xNi4wNyAwbC0xNi4xIDE2LjExYTExLjMgMTEuMyAwIDAgMCAwIDE2LjA2IDEwLjkyIDEwLjkyIDAgMCAwIDggMy4zNSAxMC45MiAxMC45MiAwIDAgMCA4LTMuMzVsNi41My02LjUyYy40NS0uNDUgMS42Mi0uMzkgMy41Mi4xNmEyOS43NiAyOS43NiAwIDAgMCA4LjkzIDEuMDF6bTEzLjIyLTY1LjYxYTIxLjk0IDIxLjk0IDAgMCAxIDE2LjA3IDYuNjkgMjEuOTQgMjEuOTQgMCAwIDEgNi42OSAxNi4wNyAyMS45MiAyMS45MiAwIDAgMSAtNi42OSAxNi4wN2wtMTYuMDcgMTYuMDdhMjIuMjMgMjIuMjMgMCAwIDEgLTExLjcyIDYuMTljLS40NC4xMS0xIC4yMi0xLjUuMzNhMTQuNzUgMTQuNzUgMCAwIDEgLTIuNTEuMTcgMTguNzkgMTguNzkgMCAwIDEgLTIuNTEtLjE3Yy0xLS4xMS0xLjc5LS4yMi0yLjM1LS4zMy0xLS4yMi0xLjY3LS4zOS0yLS41YTIyLjY2IDIyLjY2IDAgMCAxIC05LjU0LTUuNjkgNS42OSA1LjY5IDAgMSAxIDgtOCAxMS4zMSAxMS4zMSAwIDAgMCAxNi4wNyAwbDE2LjEzLTE2LjExYTExIDExIDAgMCAwIDMuMzUtOCAxMSAxMSAwIDAgMCAtMy4zNS04IDExLjMgMTEuMyAwIDAgMCAtMTYuMDYgMGwtNi43IDYuNjljLS40NS40NS0xLjYyLjM5LTMuNTEtLjE2YTI5LjgzIDI5LjgzIDAgMCAwIC04Ljg3LTFjLS43OS4xMS0xLjI2IDAtMS40My0uMzNzMC0uNzguNTktMS4zNGwxMS44NC0xMS45NmEyMS45MiAyMS45MiAwIDAgMSAxNi4wNy02LjY5eiIgLz48L3N2Zz4="
class="icon icon--link" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiBpY29uLS10d2l0dGVyIiB2aWV3Ym94PSIwIDAgMTAxLjUzIDgyLjQ5IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im05MSAyMC42MmExOC42OCAxOC42OCAwIDAgMSAuMTkgMi41OCA1OC40NCA1OC40NCAwIDAgMSAtNCAyMC45MiA2Ni4yMiA2Ni4yMiAwIDAgMSAtMTEuMiAxOSA1My4zMyA1My4zMyAwIDAgMSAtMTguODQgMTQgNTkuNiA1OS42IDAgMCAxIC0yNS4yOCA1LjM1IDU4LjM0IDU4LjM0IDAgMCAxIC0zMS44Ny05LjNjMS43Mi4xMyAzLjM3LjIgNSAuMmE0MC43OCA0MC43OCAwIDAgMCAyNi04LjkyIDE5LjA3IDE5LjA3IDAgMCAxIC0xMi00LjA3IDIwLjYgMjAuNiAwIDAgMSAtNy4zLTEwLjM4IDIwLjc1IDIwLjc1IDAgMCAwIDQuMTYuNCAyNi40MSAyNi40MSAwIDAgMCA1Ljk1LS42IDE4LjgyIDE4LjgyIDAgMCAxIC0xMS4yLTcuMjQgMjEuMjEgMjEuMjEgMCAwIDEgLTQuMjYtMTMuMjF2LS4zNWMwIC43OS44OSAxLjQyIDIuNjcgMS44OGEyMi4xNCAyMi4xNCAwIDAgMCA1LjY1LjcgMjUuNDEgMjUuNDEgMCAwIDEgLTcuNTMtNy41OCAxNy40OCAxNy40OCAwIDAgMSAtMy05LjcxIDIxLjE5IDIxLjE5IDAgMCAxIDIuOC0xMC41MiA1OS40NSA1OS40NSAwIDAgMCAxOS4xNCAxNS40NiA1Ny41NCA1Ny41NCAwIDAgMCAyMy45MiA2LjM1IDE5LjM5IDE5LjM5IDAgMCAxIC0uNTktNC43NiAyMCAyMCAwIDAgMSA2LjExLTE0LjY3IDIwLjg0IDIwLjg0IDAgMCAxIDI5Ljk0LjM5IDQ0Ljc0IDQ0Ljc0IDAgMCAwIDEzLjI5LTQuOTUgMjAuNDggMjAuNDggMCAwIDEgLTkuMzIgMTEuNSA0Mi4yNyA0Mi4yNyAwIDAgMCAxMi4xLTMuMzcgNDUuOTMgNDUuOTMgMCAwIDEgLTEwLjUzIDEwLjl6IiAvPjwvc3ZnPg=="
class="icon icon--twitter" />

![Cartoon. A figure stands beside a whiteboard covered in rough
sketches, presenting an idea. An audience of two people sits on chairs
in front of the whiteboard, scratching their chins in consideration. One
responds: 'Yes, but it doesn't work exactly like
that...'](https://basecamp.com/assets/images/books/shapeup/1.4/intro_cartoon.png)

Remember that we’re shaping work for a fixed time window. We may trust
from our experience that the elements we fleshed out in the previous
chapter are buildable within the appetite (six weeks). But we need to
look closer, because all it takes is one hole in the concept to derail
that. Suppose we bet on the project and a team takes it on. If they run
into an unanticipated problem that takes two weeks to solve, they just
burned a third of the budget!

Even worse, sometimes you run into problems that don’t just delay the
project—they have no apparent solution. We once bet on a project to
redesign the way we present projects with clients on Basecamp’s home
screen. We assumed the designer would figure it out; we didn’t do the
work in the shaping phase to validate that a viable approach existed.
Once the project started, it turned out to be a much harder problem than
we expected. None of us were able to find a suitable design solution
within the six weeks we budgeted. We ended up abandoning the project and
rethinking it later.

Of course there will always be unknowns. That’s why we apply the many
practices in Part Three so that teams tackle the right problems in the
right order, leaving room for the unexpected. But that doesn’t mean we
shouldn’t look for the pitfalls we *can* find up front and eliminate
them before betting on the project. Before we consider it safe to bet
on, a shaped project should be as free of holes as possible.

## Different categories of risk

In terms of risk, well-shaped work looks like a thin-tailed probability
distribution. There’s a slight chance it could take an extra week but,
beyond that, the elements of the solution are defined enough and
familiar enough that there’s no reason it should drag on longer than
that.

![Drawing of a thin tailed probability distribution. The Y axis is
probability and the X axis is Time to Ship in Weeks. The X axis extends
from zero weeks to 18 weeks. There is a single spike at 6 weeks shaped
like a normal distribution, extending slightly to the left and right at
the bottom of the curve. The left edge only extends to five weeks and
the right edge to seven
weeks.](https://basecamp.com/assets/images/books/shapeup/1.4/thin_tailed.jpeg)

However, if there are any rabbit holes in the shaping—technical
unknowns, unsolved design problems, or misunderstood
interdependencies—the project could take *multiple times* the original
appetite to complete. The right tail stretches out.

![Drawing of a fat tailed probability distributation. The X and Y axes
are the same as before. This time the spike up at six weeks has a long
slope down which reaches all the way past the 18 week point on the X
axis. The area above 18 weeks where the right tail still stretches is
labled: Possible 3x
delay.](https://basecamp.com/assets/images/books/shapeup/1.4/fat_tailed.jpeg)

We want to remove the unknowns and tricky problems from the project so
that our probability is as thin-tailed as possible. That means a project
with independent, well-understood parts that assemble together in known
ways.

<div class="page-break">

</div>

## Look for rabbit holes

Fleshing out the elements of the solution was a fast-moving, exploratory
process. It was more breadth than depth. In this step, we slow down and
look critically at what we came up with. Did we miss anything? Are we
making technical assumptions that aren’t fair?

One way to analyze the solution is to walk through a use case in slow
motion. Given the solution we sketched, how exactly would a user get
from the starting point to the end? Slowing down and playing it out can
reveal gaps or missing pieces that we need to design.

Then we should also question the viability of each part we think we
solved. We ask ourselves questions like:

- Does this require new technical work we’ve never done before?
- Are we making assumptions about how the parts fit together?
- Are we assuming a design solution exists that we couldn’t come up with
  ourselves?
- Is there a hard decision we should settle in advance so it doesn’t
  trip up the team?

## Case study: Patching a hole

For example, when we defined the To-Do Groups project, we introduced the
idea of dividers in the to-do list:

![The fat marker sketch of the to-do group concept from the previous
chapter, with loose to-dos at the top of the list and grouped to-dos at
the
bottom.](https://basecamp.com/assets/images/books/shapeup/1.3/fat_marker_1.png)

We liked the idea of the dividers, and the logic of loose versus grouped
to-dos made sense to us. But when we looked closer we realized that we
didn’t address how to display completed items. In the pre-existing
design, the latest few completed items displayed below the list. Should
we now render completed items at the bottom of each group instead of the
list? Or should we continue to show completed items at the bottom, and
repeat the same set of dividers within the completed items section?
Should we reconsider how we handle completed items entirely?

This was a hole in the concept. If we didn’t address it, we’d be pushing
a deep design problem down to the team and unreasonably asking them to
find a solution under deadline. It’s not responsible to give the team a
tangled knot of interdependencies and then ask them to untangle it
within a short fixed time window.

We knew from experience that changing the way completed to-dos render
has lots of complicated implications in user experience, navigation, and
performance. To remove uncertainty in the project, we decided to dictate
a solution in the shaped concept. We would leave the completed items
exactly as they worked previously. Instead of grouping or segmenting
them, we would just append the name of the group to each completed item.
It would be a little messy, but we justified the trade-off: it
drastically simplified the problem, and we could still show completed
items from a group on the group’s detail page.

![A sketch showing how to handle completed items. The grouped items in
the to-do list are only outstanding items. All the completed items are
gathered at the bottom of the list. To the right of each completed item
is a graph name in
parenthesis.](https://basecamp.com/assets/images/books/shapeup/1.4/completed_items.png)

This is the kind of trade-off that’s difficult to make when you’re
working inside the cycle under pressure. There are lots of reasons why a
different design or a deeper reconsideration of completed to-dos would
be objectively better. Why not try rendering them inside each group? A
designer could reasonably think, “Maybe if I experiment with the styling
a little more I can make them blend in better.” They could easily waste
a few days of the very few weeks they have going down a dead end.

As shapers, we’re thinking less about the ultimate design and more about
basic quality and risk. With the compromised concept we get to keep all
the elements that made the project worth doing—the groups of incomplete
items—and we get to cut off a big tail of risk.

Next, when we write the pitch for this project, we’ll point out this
specific “patch” as part of the concept. That way nobody down the line
will get tripped up on it.

## Declare out of bounds

Since everyone on the team wants to do their best work, they will of
course look for all the use cases to cover and consider them necessary.
As the team gets more comfortable with `scope hammering` (see [Decide
When to Stop](3.5-chapter-14.html)), this improves. But it’s still a
good idea to call out any cases you specifically *aren’t* supporting to
keep the project well within the appetite.

For example, we worked on an idea for notifying groups of people in
Basecamp. Rather than checking off five programmers one by one, you
could just click “Programmers” and they’d be selected for notification.
As we looked at the product, we saw tons of places where this kind of
behavior might make sense. If we let you choose a group when posting a
message, why not when assigning a to-do, or mentioning people in the
chat room?

We decided for the purpose of the project that the core value was
narrowing down who to notify about a message. We explicitly marked off
the other cases as “out of bounds” for the project and focused on the
win we wanted: a faster flow for posting messages.

## Cut back

There may be parts of the solution we got excited about during the
sketching phase that aren’t really necessary. When we designed the To-Do
Groups feature, we thought it would be great to color-code groups. No
doubt the page would look more interesting with color-coded group
labels, and the feature might be more useful too. But we decided to flag
this as unnecessary and cut it from the core of the project. We could
mention it to the team as a nice-to-have, but everyone should start from
the assumption that the feature is valuable without it.

<div class="page-break">

</div>

## Present to technical experts

Up to this point shaping has been a closed-door activity. Before you’re
ready to write up the idea to share more widely, you might need input on
some parts of the concept you aren’t completely sure about. There may be
a technical assumption that you need to verify with someone who
understands the code better. Or perhaps you want to make sure that usage
data doesn’t contradict an assumption you’re making about current
customer behavior.

This is a good time to grab some technical experts and walk them through
the idea. Communicate that this is just an idea. It’s something you’re
shaping as a potential bet, not something that’s coming down the pipe
yet. The mood is friendly-conspiratorial: “Here’s something I’m thinking
about… but I’m not ready to show anybody yet… what do you think?”

Beware the simple question: “Is this possible?” In software, everything
is possible but nothing is free. We want to find out if it’s possible
within the appetite we’re shaping for. Instead of asking “is it possible
to do X?” ask “is X possible in 6-weeks?” That’s a very different
question.

Talk through the constraints of how this is a good solution given the
appetite, so they’re partners in keeping the project at the size you
intend. And emphasize that you’re looking for risks that could blow up
the project. It’s not just a “what do you think” conversation—we’re
really hunting for time bombs that might blow up the project once it’s
committed to a team.

Try to keep the clay wet. Rather than writing up a document or creating
a slideshow, invite them to a whiteboard and redraw the elements as you
worked them out earlier, building up the concept from the beginning.
Stick completely to the concept you already worked out to get feedback
on the work you’ve already done. Then once you’ve covered the work you
already did, open it up and invite them to suggest revisions. Having
seen this concept, do they have any insights about how to drastically
simplify or approach the problem differently?

Depending on how the conversation goes, you may either have validated
your approach or discovered some problems that send you back for another
round of shaping.

## De-risked and ready to write up

At the end of this stage, we have the elements of the solution, patches
for potential rabbit holes, and fences around areas we’ve declared out
of bounds. We’ve gone from a roughly formed solution with potential risk
in it to a solid idea that we now hope to bet on in the future.

That means we’re ready to make the transition from privately shaping and
getting feedback from an inner-circle to presenting the idea at the
`betting table`. To do that, we write it up in a form that communicates
the boundaries and spells out the solution so that people with less
context will be able to understand and evaluate it. This “pitch” will be
the document that we use to lobby for resources, collect wider feedback
if necessary, or simply capture the idea for when the time is more ripe
in the future.

<a href="1.5-chapter-06.html" class="button">Write the Pitch →</a>

We built <a href="https://basecamp.com" target="_blank">Basecamp</a> to
execute the techniques in this book. It puts all our project
communication, task management, and documentation in one place where
designers and programmers work seamlessly together. See [How to
Implement the Shape Up Method in Basecamp](4.0-appendix-01.html).

*Copyright ©1999-2025 37signals LLC. All rights reserved.*

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld2JveD0iMCAwIDQwLjMgNDAuMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMzkuNDUgMzUuODktMy41NiAzLjU2YTIuMjggMi4yOCAwIDAgMSAtMy41NiAwbC0xMi4yMi0xMi4zOC0xMi4yMiAxMi4zOGEyLjI4IDIuMjggMCAwIDEgLTMuNTYgMGwtMy40LTMuNTZxLTEuODYtMS43IDAtMy41NmwxMi4yMi0xMi4yMi0xMi4yMi0xMi4yMnEtMS44Ni0xLjY5IDAtMy41NmwzLjQtMy40YzEuMjQtMS4yNCAyLjQyLTEuMjQgMy41NiAwbDEyLjIyIDEyLjIyIDEyLjIyLTEyLjIyYzEuMjQtMS4yNCAyLjQyLTEuMjQgMy41NiAwbDMuNTYgMy40YTIuMjkgMi4yOSAwIDAgMSAwIDMuNTZsLTEyLjM4IDEyLjIyIDEyLjM4IDEyLjIyYTIuMjkgMi4yOSAwIDAgMSAwIDMuNTZ6IiAvPjwvc3ZnPg=="
class="icon" />

<div class="book-info">

[*Back to Basecamp.com*](https://basecamp.com/)

# [Shape Up](../shapeup.html)

Stop Running in Circles and Ship Work that Matters

by Ryan Singer

<a href="https://basecamp-goods.com/products/shapeup" class="button">Buy
the print edition</a>

</div>

<div class="toc">

<div class="toc__part">

------------------------------------------------------------------------

## Preface

- ### [Foreword by Jason Fried](0.1-foreword.html)

- ### [Acknowledgements](0.2-acknowledgements.html)

- Chapter 1

  ### [Introduction](0.3-chapter-01.html)

  - [Growing pains](0.3-chapter-01.html#growing-pains)
  - [Six-week cycles](0.3-chapter-01.html#six-week-cycles)
  - [Shaping the work](0.3-chapter-01.html#shaping-the-work)
  - [Making teams
    responsible](0.3-chapter-01.html#making-teams-responsible)
  - [Targeting risk](0.3-chapter-01.html#targeting-risk)
  - [How this book is
    organized](0.3-chapter-01.html#how-this-book-is-organized)

</div>

<div class="toc__part">

## Part 1: Shaping

- Chapter 2

  ### [Principles of Shaping](1.1-chapter-02.html)

  - [Wireframes are too
    concrete](1.1-chapter-02.html#wireframes-are-too-concrete)
  - [Words are too abstract](1.1-chapter-02.html#words-are-too-abstract)
  - [Case study: The Dot Grid
    Calendar](1.1-chapter-02.html#case-study-the-dot-grid-calendar)
  - [Property 1: It’s rough](1.1-chapter-02.html#property-1-its-rough)
  - [Property 2: It’s solved](1.1-chapter-02.html#property-2-its-solved)
  - [Property 3: It’s
    bounded](1.1-chapter-02.html#property-3-its-bounded)
  - [Who shapes](1.1-chapter-02.html#who-shapes)
  - [Two tracks](1.1-chapter-02.html#two-tracks)
  - [Steps to shaping](1.1-chapter-02.html#steps-to-shaping)

- Chapter 3

  ### [Set Boundaries](1.2-chapter-03.html)

  - [Setting the appetite](1.2-chapter-03.html#setting-the-appetite)
  - [Fixed time, variable
    scope](1.2-chapter-03.html#fixed-time-variable-scope)
  - ["Good" is relative](1.2-chapter-03.html#good-is-relative)
  - [Responding to raw
    ideas](1.2-chapter-03.html#responding-to-raw-ideas)
  - [Narrow down the
    problem](1.2-chapter-03.html#narrow-down-the-problem)
  - [Case study: Defining
    "calendar"](1.2-chapter-03.html#case-study-defining-calendar)
  - [Watch out for
    grab-bags](1.2-chapter-03.html#watch-out-for-grab-bags)
  - [Boundaries in place](1.2-chapter-03.html#boundaries-in-place)

- Chapter 4

  ### [Find the Elements](1.3-chapter-04.html)

  - [Move at the right
    speed](1.3-chapter-04.html#move-at-the-right-speed)
  - [Breadboarding](1.3-chapter-04.html#breadboarding)
  - [Fat marker sketches](1.3-chapter-04.html#fat-marker-sketches)
  - [Elements are the
    output](1.3-chapter-04.html#elements-are-the-output)
  - [Room for designers](1.3-chapter-04.html#room-for-designers)
  - [Not deliverable yet](1.3-chapter-04.html#not-deliverable-yet)
  - [No conveyor belt](1.3-chapter-04.html#no-conveyor-belt)

- Chapter 5

  ### [Risks and Rabbit Holes](1.4-chapter-05.html)

  - [Different categories of
    risk](1.4-chapter-05.html#different-categories-of-risk)
  - [Look for rabbit holes](1.4-chapter-05.html#look-for-rabbit-holes)
  - [Case study: Patching a
    hole](1.4-chapter-05.html#case-study-patching-a-hole)
  - [Declare out of bounds](1.4-chapter-05.html#declare-out-of-bounds)
  - [Cut back](1.4-chapter-05.html#cut-back)
  - [Present to technical
    experts](1.4-chapter-05.html#present-to-technical-experts)
  - [De-risked and ready to write
    up](1.4-chapter-05.html#de-risked-and-ready-to-write-up)

- Chapter 6

  ### [Write the Pitch](1.5-chapter-06.html)

  - [Ingredient 1. Problem](1.5-chapter-06.html#ingredient-1-problem)
  - [Ingredient 2. Appetite](1.5-chapter-06.html#ingredient-2-appetite)
  - [Ingredient 3. Solution](1.5-chapter-06.html#ingredient-3-solution)
  - [Help them see it](1.5-chapter-06.html#help-them-see-it)
  - [Embedded sketches](1.5-chapter-06.html#embedded-sketches)
  - [Annotated fat marker
    sketches](1.5-chapter-06.html#annotated-fat-marker-sketches)
  - [Ingredient 4. Rabbit
    Holes](1.5-chapter-06.html#ingredient-4-rabbit-holes)
  - [Ingredient 5. No Gos](1.5-chapter-06.html#ingredient-5-no-gos)
  - [Examples](1.5-chapter-06.html#examples)
  - [Ready to present](1.5-chapter-06.html#ready-to-present)
  - [How we do it in
    Basecamp](1.5-chapter-06.html#how-we-do-it-in-basecamp)

</div>

<div class="toc__part">

## Part 2: Betting

- Chapter 7

  ### [Bets, Not Backlogs](2.1-chapter-07.html)

  - [No backlogs](2.1-chapter-07.html#no-backlogs)
  - [A few potential bets](2.1-chapter-07.html#a-few-potential-bets)
  - [Decentralized lists](2.1-chapter-07.html#decentralized-lists)
  - [Important ideas come
    back](2.1-chapter-07.html#important-ideas-come-back)

- Chapter 8

  ### [The Betting Table](2.2-chapter-08.html)

  - [Six-week cycles](2.2-chapter-08.html#six-week-cycles)
  - [Cool-down](2.2-chapter-08.html#cool-down)
  - [Team and project size](2.2-chapter-08.html#team-and-project-sizes)
  - [The betting table](2.2-chapter-08.html#the-betting-table)
  - [The meaning of a bet](2.2-chapter-08.html#the-meaning-of-a-bet)
  - [Uninterrupted time](2.2-chapter-08.html#uninterrupted-time)
  - [The circuit breaker](2.2-chapter-08.html#the-circuit-breaker)
  - [What about bugs?](2.2-chapter-08.html#what-about-bugs)
  - [Keep the slate clean](2.2-chapter-08.html#keep-the-slate-clean)

- Chapter 9

  ### [Place Your Bets](2.3-chapter-09.html)

  - [Look where you are](2.3-chapter-09.html#look-where-you-are)
  - [Existing products](2.3-chapter-09.html#existing-products)
  - [New products](2.3-chapter-09.html#new-products)
  - [R&D mode](2.3-chapter-09.html#rd-mode)
  - [Production mode](2.3-chapter-09.html#production-mode)
  - [Cleanup mode](2.3-chapter-09.html#cleanup-mode)
  - [Examples](2.3-chapter-09.html#examples)
  - [Questions to ask](2.3-chapter-09.html#questions-to-ask)
  - [Does the problem
    matter?](2.3-chapter-09.html#does-the-problem-matter)
  - [Is the appetite right?](2.3-chapter-09.html#is-the-appetite-right)
  - [Is the solution
    attractive?](2.3-chapter-09.html#is-the-solution-attractive)
  - [Is this the right
    time?](2.3-chapter-09.html#is-this-the-right-time)
  - [Are the right people
    available?](2.3-chapter-09.html#are-the-right-people-available)
  - [Post the kick-off
    message](2.3-chapter-09.html#post-the-kick-off-message)

</div>

<div class="toc__part">

## Part 3: Building

- Chapter 10

  ### [Hand Over Responsibility](3.1-chapter-10.html)

  - [Assign projects, not
    tasks](3.1-chapter-10.html#assign-projects-not-tasks)
  - [Done means deployed](3.1-chapter-10.html#done-means-deployed)
  - [Getting oriented](3.1-chapter-10.html#getting-oriented)
  - [Imagined vs discovered
    tasks](3.1-chapter-10.html#imagined-vs-discovered-tasks)

- Chapter 11

  ### [Get One Piece Done](3.2-chapter-11.html)

  - [Integrate one slice](3.2-chapter-11.html#integrate-one-slice)
  - [Case study: Clients in
    projects](3.2-chapter-11.html#case-study-clients-in-projects)
  - [Programmers don’t need to
    wait](3.2-chapter-11.html#programmers-dont-need-to-wait)
  - [Affordances before pixel-perfect
    screens](3.2-chapter-11.html#affordances-before-pixel-perfect-screens)
  - [Program just enough for the next
    step](3.2-chapter-11.html#program-just-enough-for-the-next-step)
  - [Start in the middle](3.2-chapter-11.html#start-in-the-middle)

- Chapter 12

  ### [Map the Scopes](3.3-chapter-12.html)

  - [Organize by structure, not by
    person](3.3-chapter-12.html#organize-by-structure-not-by-person)
  - [The scope map](3.3-chapter-12.html#the-scope-map)
  - [The language of the
    project](3.3-chapter-12.html#the-language-of-the-project)
  - [Case study: Message
    drafts](3.3-chapter-12.html#case-study-message-drafts)
  - [Discovering scopes](3.3-chapter-12.html#discovering-scopes)
  - [How to know if the scopes are
    right](3.3-chapter-12.html#how-to-know-if-the-scopes-are-right)
  - [Layer cakes](3.3-chapter-12.html#layer-cakes)
  - [Icebergs](3.3-chapter-12.html#icebergs)
  - [Chowder](3.3-chapter-12.html#chowder)
  - [Mark nice-to-haves with
    ~](3.3-chapter-12.html#mark-nice-to-haves-with-)

- Chapter 13

  ### [Show Progress](3.4-chapter-13.html)

  - [The tasks that aren’t
    there](3.4-chapter-13.html#the-tasks-that-arent-there)
  - [Estimates don’t show
    uncertainty](3.4-chapter-13.html#estimates-dont-show-uncertainty)
  - [Work is like a hill](3.4-chapter-13.html#work-is-like-a-hill)
  - [Scopes on the hill](3.4-chapter-13.html#scopes-on-the-hill)
  - [Status without asking](3.4-chapter-13.html#status-without-asking)
  - [Nobody says "I don’t
    know"](3.4-chapter-13.html#nobody-says-i-dont-know)
  - [Prompts to refactor the
    scopes](3.4-chapter-13.html#prompts-to-refactor-the-scopes)
  - [Build your way uphill](3.4-chapter-13.html#build-your-way-uphill)
  - [Solve in the right
    sequence](3.4-chapter-13.html#solve-in-the-right-sequence)

- Chapter 14

  ### [Decide When to Stop](3.5-chapter-14.html)

  - [Compare to baseline](3.5-chapter-14.html#compare-to-baseline)
  - [Limits motivate
    trade-offs](3.5-chapter-14.html#limits-motivate-trade-offs)
  - [Scope grows like grass](3.5-chapter-14.html#scope-grows-like-grass)
  - [Cutting scope isn’t lowering
    quality](3.5-chapter-14.html#cutting-scope-isnt-lowering-quality)
  - [Scope hammering](3.5-chapter-14.html#scope-hammering)
  - [QA is for the edges](3.5-chapter-14.html#qa-is-for-the-edges)
  - [When to extend a
    project](3.5-chapter-14.html#when-to-extend-a-project)

- Chapter 15

  ### [Move On](3.6-chapter-15.html)

  - [Let the storm pass](3.6-chapter-15.html#let-the-storm-pass)
  - [Stay debt-free](3.6-chapter-15.html#stay-debt-free)
  - [Feedback needs to be
    shaped](3.6-chapter-15.html#feedback-needs-to-be-shaped)

- ### [Conclusion](3.7-conclusion.html)

  - [Key concepts](3.7-conclusion.html#key-concepts)
  - [Get in touch](3.7-conclusion.html#get-in-touch)

</div>

<div class="toc__part">

## Appendices

- ### [How to Implement Shape Up in Basecamp](4.0-appendix-01.html)

  - [A Basecamp Team for
    shaping](4.0-appendix-01.html#a-basecamp-team-for-shaping)
  - [Basecamp Projects for cycle
    projects](4.0-appendix-01.html#basecamp-projects-for-the-cycle-projects)
  - [To-Do Lists for
    scopes](4.0-appendix-01.html#to-do-lists-for-scopes)
  - [Track scopes on the Hill
    Chart](4.0-appendix-01.html#track-scopes-on-the-hill-chart)

- ### [Adjust to Your Size](4.1-appendix-02.html)

  - [Basic truths vs. specific
    practices](4.1-appendix-02.html#basic-truths-vs-specific-practices)
  - [Small enough to wing
    it](4.1-appendix-02.html#small-enough-to-wing-it)
  - [Big enough to
    specialize](4.1-appendix-02.html#big-enough-to-specialize)

- ### [How to Begin to Shape Up](4.2-appendix-03.html)

  - [Option A: One six-week
    experiment](4.2-appendix-03.html#option-a-one-six-week-experiment)
  - [Option B: Start with
    shaping](4.2-appendix-03.html#option-b-start-with-shaping)
  - [Option C: Start with
    cycles](4.2-appendix-03.html#option-c-start-with-cycles)
  - [Fix shipping first](4.2-appendix-03.html#fix-shipping-first)
  - [Focus on the end
    result](4.2-appendix-03.html#focus-on-the-end-result)

- ### [Glossary](4.5-appendix-06.html)

- ### [About the Author](4.6-appendix-07.html)

</div>

</div>

Appetite  
The amount of time we want to spend on a project, as opposed to an
estimate.

Baseline  
What customers are doing without the thing we’re currently building.

Bet  
The decision to commit a team to a project for one cycle with no
interruptions and an expectation to finish.

Betting table  
A meeting during cool-down when stakeholders decide which pitches to bet
on in the next cycle.

Big batch  
One project that occupies a team for a whole cycle and ships at the end.

Breadboard  
A UI concept that defines affordances and their connections without
visual styling.

Circuit breaker  
A risk management technique: Cancel projects that don’t ship in one
cycle by default instead of extending them by default.

Cleanup mode  
The last phase of building a new product, where we don’t shape or bet on
any particular projects but instead allocate unstructured time to fix
whatever is needed before launch.

Cool-down  
A two-week break between cycles to do ad-hoc tasks, fix bugs, and hold a
betting table.

Cycle  
A six week period of time where teams work uninterruptedly on shaped
projects.

De-risk  
Improve the odds of shipping within one cycle by shaping and removing
rabbit holes.

Discovered tasks  
Tasks the team discovers they need to do after they start getting
involved in the real work.

Downhill  
The phase of a task, scope or project where all unknowns are solved and
only execution is left.

Fat marker sketch  
A sketch of a UI concept at very low fidelity drawn with a thick line.

Hill chart  
A diagram showing the status of work on a spectrum from unknown to known
to done.

Iceberg  
A scope of work where the back-end work is much more complex than the UI
or vice versa.

Imagined tasks  
Work the teams decide they need to do after just thinking about the
project. See discovered tasks.

Layer cake  
A scope of work you can estimate by looking at the surface area of the
UI.

Level of abstraction  
The amount of detail we leave in or out when describing a problem or
solution.

Must-haves  
Tasks that must be completed for a scope to be considered done.

Nice-to-haves  
Task left for the end of the cycle. If there isn’t time to do them, they
get cut. Marked with a '~' at the beginning.

Pitch  
A document that presents a shaped project idea for consideration at the
betting table.

Production mode  
A phase of building a new product where the core architecture is settled
and we apply the standard Shape Up process.

Rabbit hole  
Part of a project that is too unknown, complex, or open-ended to bet on.

R&D mode  
A phase of building a new product where a senior team spikes the core
features to define the core architecture.

Raw ideas  
Requests or feature ideas that are expressed in words and haven’t been
shaped.

Scopes  
Parts of a project that can be built, integrated, and finished
independently of the rest of the project.

Scope hammering  
Forcefully questioning a design, implementation, or use case to cut
scope and finish inside the fixed time box.

Shape  
Make an abstract project idea more concrete by defining key elements of
the solution before betting on it.

Six weeks  
The length of our cycles. Six weeks is long enough to finish something
meaningful and short enough to feel the deadline from the beginning.

Small batch  
A set of 1-2 week projects that a single team ships by the end of a six
week cycle.

Time horizon  
The longest period of time where we can feel a deadline pushing on us
from the beginning. Six weeks.

Uphill  
The phase of a task, scope or project where there are still unkowns or
unsolved problems. See downhill.

</div>