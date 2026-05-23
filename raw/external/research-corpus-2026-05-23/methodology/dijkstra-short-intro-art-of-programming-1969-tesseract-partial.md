---
title: dijkstra-short-intro-art-of-programming-1969
source_pdf: dijkstra-short-intro-art-of-programming-1969.pdf
source_folder: methodology
extraction_method: tesseract-ocr-psm6-oem1-100dpi
extraction_date: 2026-05-24
pages_total: 101
pages_ocr: 25
ocr_coverage: partial
ocr_remaining: 76
chars: 46905
approx_tokens: 11726
ocr_runtime_sec: 21.7
pipeline_phase: 3-ocr-extracted
constitutional_posture: R1-surface
note: PARTIAL OCR — first 25 pages only. 76 pages flagged for paid OCR re-processing.
phase4_cleaned: true
phase4_chars_before: 46907
phase4_chars_after: 46896
phase4_saved_pct: 0.0
---

## Page 1

TECHNISCHE HOGESCHOOL EINDHOVEN
Afdeling Algemene Wetenschappen
Onderafdeling der Wiskunde
A short Introduction
to the
ART of PROGRAMMING
Prof. Dr. Edsger W. Dijkstra
August 1971

## Page 2

- Bikei aed
vt EWD 316:
A SHORT INTRODUCTION
TO THE ART
i OF PROGRAMMING
Dictaatnr, 2,268 Prijs f 4,--

## Page 3

TT
EWD316
Ewn316: A Short Introduction to the Art of Programming
by :
prof.dr.Edsger W.Dijkstra
|
|
August 1971

I

|

## Page 4

EWwD316 ~ 0

Contents.

© Contents

1 Preface

5 Some fundamental notions

20 Programming lenguages and their implementation

33 Variables and relations between their values

44 Programs corresponding to recurrence relations

53 A first exanple of step-wise program composition
64 The shortest spanning subtree of 2 graph
Ti The towers of Hanoi
| 76 The problem of the eight queens
: 89 A rearranging routine
|

{

## Page 5

EWO316 - 1
Preface.

The market is alreedy so heavily overloaded with introductory texts on
computers and computer programming that one must have rather specific reasons
to justify the investment of one's time and energy in the writing of yet
another "Short Introduction to the Art of Prograwming". The sole fact that
one Likes to write is, in itself, an insufficient justification. Before
undertaking such @ task I should therefore ask myself "Why am I going to do
i?" and also "What do I expect to be the distinguishing features of this
Little monagraph?".

There is 8 simple, practical reason. At my University I give, mainly

| for future Mathematical Engineers, en introduction to the art of programming
and my students would welcome some supporting material. Besides that, without
some form of lecture notes, my colleagues have very little idea of what I an
really trying to teach! The contents of this course show signs of settling

down -I have now given it three times~ and therefore this seems the

eppropriate moment to produce a document that can serve as lecture notes.

These are purely local circumstances and as far as they are concerned, 7
2 normal set of lecture notes in Dutch, say- would do. The fact that I have
Rot chosen this form means that I am aiming at a lerger audience. Such an
act is always somewhat presumptuous and the usual author's trick to save the
image of his modesty is to say that from various sides he has been urged to
produce his manuscript ~a trick that I could apply in this case without
lying. But I don't think that I shall resort to that trick because I really
believe that a larger audience than just my students can benefit from it, or

, even enjoy it.

| The fact is that over the last years I have addressed myself to the

| question of whether it was conceivable to increase our programming ability

by on onder of magnitude and what techniques (mental, orgenizetional or

H mechanical) should then be applied in the process of pragram composition.

j Personally, I felt these investigations very rewarding: I gained a much
deeper understanding of the nature of the difficulty of the programming
task, I became much more conscious about my "programming style", which im
proved considerably, and found myself, when progranming, in much better
control of what I was doing than I had ever been before. Needless to say, _

Ser trot off what T was doing then I had ever been before. Needless to say,

## Page 6

ewD316 - 2
|

my teaching was heavily influenced by these experiences. Hl

The purpose of this little monograph is to assist the programming
reader in cleaning up his own thinking, to transmit to him some mental disciplines by sticking to which he cen avoid making his job unnecessarily difficult.
It is born out of dissatisfaction with the usual kind of programming course,
which now strikes me as like the type of driving lessons in which one is taught
how to handle a car instead of how to use a car to reach ane's intended des~
tiation. This monograph is intended es a complement to such courses: I shall
try to present programming ~to quote Niklaus Wirth "as a discipline on its own |
merits, as a methodology of constructive reasoning applicable to any problem
capable of algorithmic solution", '

I expect: the distinguishing feature of this little monograph to be its
incompleteness, incompleteness in many, many respects.

Tt will not be self-contained in the sense thet I assume my readers
somewhat familiar with a decent higher level programming language. (This
assumption is a direct consequence of the local circumstance that my students |
have had a modest prior exposure to the cleaner aspects of ALGOL 60.) |

For those readers who identify the programmer's competence with a |
thorough knowledge of the idiosyncrasies of one or more of the beroque tools |
book will also be very incomplete, because I won't describe any programming i
ronguage “rot even the one I use to ary degree of detail, I shat use some |
sort of pragranning language, 28 "a communication language say, not for the |
communication of algorithms, but for the communication of ways of thinking, !
as a vehicle for programming style.

In yet another respect, this little monograph will be very incomplete.
As said above, I shall try to present programing "as a discipline on its own
merits, as @ methodology of constructive reasoning, applicable to any problem
capable of algorithmic solution", At present, such a methodology does not yet
exist in the full sense of the word, only elements of it have become apparent,
others are just lurking behind our mental horizon. This, of course, is not very
satisfactory, but it is a true reflection of the current, still rather poor
state of the art. It is a consolation that no piece of scholarship ever reaches

## Page 7

EWD316 - 3
the state of perfection and I tell myself that the conviction that there is
more to come is no justification for witholding what we have got.
It will also be incomplete as a result of the choice of the examples

and the choice of the considerations. By necessity, the examples will be "smell"
programs, while the need for @ discipline becomes really vital in the case

of "large" programs. Dealing with small examples in en ad-hoc fashion gives

the student not the slightest clue as to how to keep the construction of a

large progran under his intellectual control. Illustrating how we can avoid
unmastered complexity, I hope to deal with smell examples in such a fashion,

that methodological extrapolation to lerger tasks is feasible. The selection ~

of consideretions is also kept to a strict minimum: we restrict’ ourselves to
progrenming for purely sequential machines and when we consider a trade-off
question, we shell usually present this in the form of @ trade-off between
computation time versus store requirements, In this respect the document may

strike the reader as very strongly dated, perhaps even out-dated by the tine

it appears in print. If so, I hope that I can justify my defense, which is

thet such a reader has failed to read between the lines: it is not so much

the particular trade-off question chosen that matters, as the fact thet the

problem has been approached in such a fashion that we have made @ conceptual
framework in which such specific trade-off questions can be postponed until -
the appropriate moment. The only thing I can do at this stage is to urge my

readers to read between the lines as much as possible. (If one tries to

transmit ideas or methods, one can talk-about them but that alone is insuf- .
ficient: one must shaw examples illustrating them. When lecturing, it is my

sed experience that after having dealt with @ specific example, I find the

attention of half my audience completely usurped by this example: they have
forgotten that the example was only brought to their attention to illustrate
something more general. This is a sad experience and no amount of prior warning .
that this misunderstanding is bound to happen if they are not careful, has

ever enabled me to avoid it!) To put it in another way: it is my purpose to

transmit the importance of good taste and style in programming, the specific
elenents of style presented serve only to illustrate what benefits can be .
derived from "style" in general. In this respect I feel akin to the teacher

of composition at a conservatory: he does not teach his pupils how to compose

a particular symphony, he must help his pupils to find their own style and

must explain to them what is implied by this. (It has been this analogy that

made me talk about "The Art of Pragramming”.)

## Page 8

EWD316 - 4

There is a further class of potential readers that will find this subject
matter very incompletely dealt with, viz. those who identify the programmer's
task with writing programs in, say, FORTRAN or PL/1. One of my implicit morals
will be that such programming languages, each in their own way, are vehicles
inadequate to guide our thoughts. If FORTRAN has been called an infantile
disorder, PL/1 must be classified as a fatal disease.

Although I would love to do it, it is impossible to give a true
acknowledgement, listing all persons whose relevant influence on my thinking
I gratefully renenber or should remember. With my epolagies to all persons
unmentioned I would like to make a few exceptions and list in alphabetical
order: my mother mrs.B.C.Dijkstra ~ Kluyver, R.W.Floyd, C.A.R.Hoare, P.Naur,
B.Randell, D.T.Ross, N.Wirth and M.Woodger. None of the persans listed,
however, should in any way be held responsible for the views expressed (with
the possible exception of my mother who is in some sense responsible for ny
existence).

I am deeply indebted to my sister-in-law, mrs.E.L.Dijkstre - Tucker
for her willingness to correct my use of English in yet another manuscript
and to W.H.J.Feijen for the great care with which he has screened the text
for typing errors.

## Page 9

EWD316 ~ 5

Some fundamental notions.

In this section @ nunber of notions will be introduced, because they
are fundamental to the whole activity of programming. They are so fundanental
that they will not be dissected into more primitive concepts. As a result,
this section will be @ very informal one, analogy, metaphor and naturel
language (poetry, if I were able!) being the only aveilable vehicles to
convey their contents end connotations.

It is not unusual ~although 2 mistake~ to consider the programez's
task to be the production of programs. (One finds terms such as "software
manufacturing", proposals to measure programmer productivity by the number
of lines of code produced per month etc., although I have never seen the
suggestion to measure composer productivity by the number of notes, monthly
scribbled on his score!) This mistake may be at the heart of the managenent
failure which is so apparent in many large software efforts. It is a mistake,
because the true subject matter of the programmer's activity is not the
program he composes, but the class of possible computations that may be
evoked by it, the "production" of which he delegates to the machine. It seens
more fruitful to describe the programmer's activity as "designing a class of
computations", rather than es "making a progran". In this connection it should
be borne in mind that the more relevant assertions about programs ~e.g. about
their correctness or their resource demands- indeed pertain to the computations,
rather than to the last thing that leaves the programmer's hands, viz. the
program text, It is for this reason that, when introducing fundamental notions,
I will start at the side of the computations, with the "happenings in time",

The first notion is that of an action, An action is @ happening, taking
place in a finite period of time and establishing @ well-defined, intended
Det effect. In this description, we have included the requirement that the
action's net effect should be "intended", thereby stressing the purposefulness.
If we are interested in the action at all, it will be by virtue of our interest
in its net effect.

The requirement that the action should take place in a finite period
of time is most essential: it implies that we cen talk about the moment TO,
when the action begins, and the later moment T1, when the ection ends. We

## Page 10

EWD316 - 6
assume that the net effect of the action can be described by comparing "the
state at moment TO" with "the state at moment Ti",

An example of an action would be @ housewife peeling the potatoes for
the evening dinner. The net effect is that the potatoes for the evening dinner
are at moment TO still unpeeled, say in the potato basket in the celier, while
at moment T1 they will be peeled and, say, in the pan they are to be cooked

When we dissect such a happening as a tine sequence of (sub)actions,
the cumulative effect of which then equals the net effect of the total
happening, then we sey that we regard the happening as @ Sequential process,
or process for short.

Whenever such a dissection is permissible, we can regard the sone
happening either as 2n action, or as a sequential process. When our interest
is confined to the net effect, to the states "before and after", then we
regard it as an ection. If, however, we are interested in one or more intermediate states as well, then we regard it es a process. In the letter case
the moment 10 coincides with the beginning of the first subaction and the
end of each subaction coincides with the beginning of the next one, with the
exception of the last subaction, whose end coincides with T1, the end of the
whole happening.

I must stress, that whether some happening is regarded as on action or
as @ process is not so much an inherent property of the happening as an
expression of our mood, of the way in which we prefer to look at it. (Why we
should want to look at it in different ways will be left for later discussion.)
Similerly, if we have chosen to regard the happening as e process, the way
in which it has been dissected is also not so such an inherent property of
the happening as a result of which of its distinguishable intermediate states
(for some reason or another) we wish to take into consideration.

The happening of the potato~peeling housewife could, for instance, be
described by the time-succession of the following subactions of the housewife:

## Page 11

. EWD316 - 7
"fetches the basket from the celler;
fetches the pan from the cupboard;
peels the potatoes;
returns the basket to the cellar"

Here the total happening has been described es a time-succession of
four subactions. In order to stress that we have given the description of a
happening, we have phrased it in the form of an eye-witness account. Note,
that if the eye-witness did not bother to describe that the basket was
fetched from the cellar before the pan was fetched from the cupboard, the
first two Lines would have been condensed into a single subsection "fetches
the basket from the cellar and the pan from the cupboard”.

We postulate that in each happening we cen recognize a pattern of
behaviour, or pattern for short; the happening occurs when this pattern is
followed. The net effect of the happening is fully determined by the patter
and (possibly) by the initial state (i.e. the state at moment TO). Different
happenings may follow the sane pattern; if these happenings establish different
net effects, the net effect must have been dependent on the initial state as
well, and the corresponding initial states must have been different.

How we can recognize the same pattern in different happenings felle

| outside the scope of this text. If we mest a friend, we can recognize his
face, no matter what facial expression he shows: it may be an expression we -
have never seen on his face before! Similarly with different happenings: we

states and net effects.

We return for a moment to the housewife. On a certain day she has peeled

the potatoes for the evening dinner and we have an eye-witness account of this

happening. The next day, again, she peels the potatoes for the evening dinner
and the second happening gives rise to an eye-witness account equal to the
previous one. Can we say, without further ado: "Obviously, the two accounts
are equal to eachother for on both accasions she has done exactly the sane
thing."?

How correct or incorrect this last statement is depends on what we mean
by "doing the same thing", We must be careful not to make the mistake of the

## Page 12

_

EWD316 - 8
journalist whe, covering 2 marriage ceremony, seported that the four bridesmaids
wore the same dress. what he meant to say wes that the four dresses were mede
from material of the same design and -apart from possible differences in size~
according to the seme pattern.

The two actions of the housewife ere as different from eachother es the
dresses are: they have, as happenings, at least a different identity: one
took place yesterday, one today. As each potato cen only be peeled once, the
potatoes involved in the twa happenings have different identities as well;
the first time the basket mey have been fuller than the second time; the
number of potatoes peeled may differ, etc.

Yet the two happenings are so similer that the some eye-witness account
is accepted as adequate for both occasions and that we are willing to apply
the same name to both actions (e.g. "peeling the potatoes for the evening
dinner"),

An algorithm is the description of e pattern of behaviour, expressed
in terms of a well-understood, finite repertoire of named (so-called “primitive")
actions of which it is assumed a priori that they can be done (i.e. can be
caused to happen).

In writing dows an algorithm, we start by considering the happening to
take place as a process, dissected into a sequence of subactions to be dove
in succession. If such a subaction occurs in the well-understood, finite
repertoire of named actions, the algorithm refers to it by its name. If such
a subaction does nat occur in the finite repertoire, the algorithm eventually
refers to it by means of a subalgorithm in which the subaction, in its turn,
is regarded as a process, etc. until at the end all has been reduced to
actions from the well-understood, finite repertoire.

The notion of an algorithm, of an executable precept for the establishing of a certain net effect, is very well known from daily life: knitting
patterns, directions for use, recipes and musical scores are all algorithns.
And if one asks the way to the railway station in an unfamiliar town, one
asks essentially for an algorithm, for the description of a pattern of
behaviour which, when followed, will lead to the desired goal.

## Page 13

EWD316 - 9

In bur definition of an algorithm we have stressed that the primitive
actions should be executable, that they could be done. "Ga to the other side
of the square." is perfectly acceptable, "Go to hell.", however, is not ar
algorithm but @ curse, because it cannot be done.

Besides that we have stressed that the repertoire should be well-arder—
stood: between the one who composed the algorithm and the one who intends to
follow it there shauld be no misunderstanding abaut this repertoire. (In this
respect knitting patterns are, as a rule, excellent, recipes are of moderate
quality while the instructions one gets when asking the way are usually :
incredibly bad!) How essential this lack of misunderstanding is may ermaps
best be demonstrated by @ recipe for jugged hare as it occurs in an old Dutch
cookery-book; translated into English the recipe runs as follows: "One taketh
a hare and prepareth jugged hare from it." The recice is not exactly wrong,
but it is hardly helpful!

Let us now contrast the eye-witness account of the potato peeling
session: "fetches the basket from the cellar;

fetches the pan from the cupboard;

peels the potatoes;

returns the basket to the cellar”
with the corresponding algorithm ~the set of instructions, say, the housewife
might give to anew maic=:

‘fetch the basket from the cellar;

fetch the pan from the cupboerd;

peel the potatoes;

return the basket to the cellar”

Comparing the two, we may well ask what we have gained, for it seems
2 roundsbaut way of doing things: describing @ pattern of behavicur which,
when followed, will evoke the happening, while in the eye-witness account we
had an excellent way of describing the happening itself.

What have we gained? Well, nothing as long as we restrict ourselves to
algorithms thet cen be given -as in our example- by a concatenation of names
af actions, to be done in the given order. Under that restriction an eye~
witness account of the ections "as they take place” is equally good. But the

## Page 14

= - — - —_ - =
EWD316 - 10
behaviour of the housewife (or the maid) could be a little bit more complicated:
let us suppose that after the pan has been fetched, she puts on an apron if
necessary, i.e. when she wears a light-coloured skitt and that on one day she
uses the apron while on the other day she doesn't.
On a rather ebstract level ~i.e. without explicit mentioning of the apron
‘and the condition under which it is used, @ uniform eye-witness account would
still do (in some fashion) for both sessions, e.g.:
"fetches the basket from the cellar;
fetches the pan from the cupboard;
takes preparation with regard to clothing;
peels the potatoes;
returns the basket to the cellar"
with the implicit understanding that "takes preparation with regard to
clothing" covers the empty action when her skirt is not light-coloured and
covers putting on an apron when her skirt is light-coloured.
If, however, we want to go into more detail and want to mention the
apron explicitly, then "takes preparation with regard to clothing" has to be
repleced in the eye-witness account of the one day's session by
"sees that her skirt is light-coloured and therefore puts on an apron” —
and in the other day's session by
“sees that her skirt is not light-coloured and therefore omits putting
on an apron”.
The trouble is, that the eye-witness account cannot contain the single
sentence:
"puts on an apron if her skirt is light-coloured”
for. then the audience justly asks “dees she do it or not?". In other words:
in that degree af detail we cannot cover the two happenings by the same eye~
witness account, for in that degree of detail the two happenings differ!
&
. It is here that the potential power of the algorithm becomes apparent, %
for we can recognize the sane pattern af behaviaur in the two happenings and iy
by describing that pattern of behaviour we give something that is apPlicable .
a wet
- . — - ee : dee -

## Page 15

€WD316 - 11
under bath circumstances, light~ as well as dark-coloured skirt. This is
possible thanks to the fact thet what actually happens when a'certain pattern
of behaviour is followed may be co-datermined by the state of affairs which
is current when the action begins.

We see two things: the inspectiqn of whether the skirt is light-coloured
or not and, depending on the outcome of this inspection, the action "put on
2n apron" is to take place or not, In order to express this conditional
execution we need in our algorithm another connective besides the semicolon.
In our example of the algorithm (I refer $c the instructians to the new maid)
‘the semicolon had a double function: in the text it separates one action mare
fron the next action nene, but besides that it implied for the happening 3
certain amount of what is technically called "sequencing control", i.e. it
was meant to imply that the end moment of the preceding action should co-incide
with the beginning of the following action. We now need another connective,
Indicating whether or not the inspegtion should be followed by the next action
in the text, Ne write for instance the following algorithm:

"fetch the basket from the cellars

fetch the pan from the cupboard;

Af skirt is light-coloured do put on an apron;
peel the potatces;

return the basket to the cellar".

(For historical reasons the sorcalled conditionel connective "if...co”
ie split into two symbols "if" and "do", enclosing the inspection.)

The conditional connective connects two actions, the first of which must
be 2 so-called "inspection". This inspection describes a stote of affairs,
which may be true or false ("false" is the tachnical term for "not true").

The happening which is to take place corresponding to the conditional
‘compound "if inspection go action"
nay take one of two mutually exclusive forms: either the inspectign gives the
result true and it is followed by the action, or the inspection delivers the
result false and thereby the whele compound action has been completed. The
algorithn derives its superiority over the eye-witness account from the fact
that ‘it may contain connectives (such as the conditional connective) that
imply a more elebarate sequencing control than the semicolon.

## Page 16

iQ —_— a - — - —
EWD316 - 12

We need a further connective before we can see the full superiority.of
the: algorithm over the eye-witness account, viz. a repetitive connective. »

Suppose that we want to express that “peeling the potatoes" is in itself
2 process that deals with one poteto at a time and that, correspondingly, our ~
primitive action is named "peel a next potato". If the number of potatoes to
be peeled is a fixed constant, say always 25, then we can replace "peel the
potatoes" by 25 times "peel a next poteto", separated from eachother by in
toto 24 semicolons. But we now assume that the number of potatoes ta be peeled
may differ from one day to the next; yet we want to recognize in each peeling
session the same pattern of behaviour. We suppose the housewife capable of
looking into the pan and judging whether the amount of peeled potatoes is
sufficient or not.

If we know @ priori that in the worst case (i.e. many guests and very
small potetoes) she will never have to peel mare than 500 potatoes, we can
give a general algorithm describing the actual peeling by repeating in the
text of our algorithm 500 times (separated by in toto 499 semicolons) the
conditional compound:

“if number of peeled potatoes is insufficient do peel anext potato” .

Several objections can be made to this solution. There is the practical
objection that it would reduce the construction of algorithms to doing lines.
Furthermore we had to make the fundamental assumption that we knew in advance
a maximum number. Often it is very hard to give such an upper bound 2 priori
end if it can be given, such an upper bound is usually many times larger’ than
the average value. And if in actual fect 25 potatces have to be peeled, the
26th inspection "number of peeled potatoes insufficient” -i.e. the first one
to deliver the result "false"~ gives fresh information, the following 474
inspections (which are prescribed by the algorithm as suggested) give no new
information. Once the housewife has established that the number of peelewt i
potatoes is no longer insufficient, she should not be forced to look into
the pan another 474 times in order to convince herself!

In order to meet these objections, we introduce @ repetitive connective
which, again for historical reasons, is written in two parts "while...do". \
Using this connective we can write the algorithm:

## Page 17

EwD316 - 13
"fetch the basket from the cellar;
fetch the pan from the cupboard;
Af skirt is light-coloured do put on en apron;
while number of peeled patatoes is insufficient do
peel a next potato;
return the basket to the cellar” .
The process corresponding to
‘while inspection do action"
. consists of one or more executions of the conditional compound
"if inspection Jo action" ,
viz. up to and including the first time that the inspections gives the result
"false".
We can also describe the semantice of the repetitive connective in
terms of the conditional one recursively:
“while inspection do action"
is semantically equivalent to
“if inspection do
begin action; while inspection go action end" .
Here the symbols "begin" and "end" are used as apening and clesing bracket
respectively; they ere 2 syntactical device to indicate that the conditional
connective connects the inspection (from the first line) to the whole of the
second line: the value delivered by the first inspection decides whether what
is described on the second line (from begin until end) will be done in its
entirety or will be skipped in its entirety.
Note. In the above I have approached the idea of an algorithm sterting ny
considerations from the class of happenings in which we wanted to discern
the same pattern of behaviour. In addition to the semicolon as cannective in
‘the text of the algorithm this led to other connectives such as the conditional
connective "if...do" and the repetitive connective "while...do". It is not
unusual to approach the relation between algorithm and computations from the
side of the algorithn; such an approach leads in a very early stage to
syntactical considerations, as a result of which the connectives are introduced

## Page 18

EWD316 - 14
in @ somewhat different terminology. Instead of
"if inspection do action"
cople write
peop "if condition do statement” .

The part of the text denoted by "if condition do” is then described
as "conditional clause", which is regarded as a prefix attached to the
"statement", the whole construction comprising clause and statement together
is then called "a conditional statenent". Similarly, in

"while condition do statenent” ,
“while condition do” is called "a repetitive clause" and the statement is
called "the repeatable statement", This terminology is so widely used that
win spite of its syntactical origin~ I shall not refrain from using it
whenever I see fit to do so.

As a final exercise I shall describe the patter of behaviour of 2
housewife who ~for some obscure reason- is so conditioned that she can only
peel en even nunber of potatoes for the evening dinner:

“fetch the basket from the celler;

fetch the pan from the cupboard;

Ef skirt is light-coloured do put on an apron;

while nunber af peeled potatces is insufficient do

begin peel a next potato; peel @ next potato end;

return the basket to the cellar" .
This example is included to show that the sane set of primitive actions allows
different patterns of behaviour.

The notion of an algorithm is a very powerful one, for a single
algorithn "extracts" whet @ lerge number of different happenings may have in
conman. And it does not do so by ignoring details, on the contrary, # single
algorithn cavers @ whole class of happenings to the very degree of detail in
which the corresponding eye-witness accounts would differ from eachother. The
possibly large number of different corresponding happenings is generated by ,
the different ways of sequencing as might be controlled by the conditional,
the repetitive (and similar, see later) connectives.

## Page 19

EWD316 = 15

On the one hand we have the algorithm, a finite text, a timeless, static

concepts on the other hand we have the corresponding happenings that mey be
evoked by it, dynamic concepts, happenings evolving in time. The intimate
relation between the two to which we xefer by the term “sequencing” lies
at the heart of the algorithmic notion, (It is to this intimate relation
that I refer whenever I stress that the programmer's true activity is "The
design of classes of computations.) The nation of an slgorithn is sdmittediy
2 very powerful ane; before going on, however, I shall allow myself 2 1ittle
detour in order ta indicate what “price” we have paid for its introduction.

We have stated thet we restrict ourselves to happenings taking plece

in a Finite period of tine. whenever an algorithm is followed, @ happening
is taking place, eventually as a time-succession of primitive actions. It

is only realistic to postulate thet each primitive action will take a finite
period of tine, unequal to zero: no action will take place "infinitely fast".
This implies that we confine our sttention to happenings that ere taking
place as a time~succesion of a finite number of primitive actions.

And now we are beginning to see the price: it is very easy to write
down a text that Looks Like an algorithm but that is not an algorithm in aur
| sense of the word, because the effort to follow it turns out to be 8 never~

ending task, e.g.

“while skirt is light-coloured do peel a next potato” .

When we assume that the peeling of a next potato does not influence the colour
of the skirt, we have just two ceses: either the skirt is not light-cololred
end the only action taking place is the inspection establishing this fact,
or the skirt is light-coloured and will remain so and what the pattern could

| be interpreted to describe is the peeling of an infinite number of next
potatoes, This is usually called "an improper algorithn".

The question of whether @ text that looks Like an algorithn is indeed

4 proper algorithm or not, is far from trivial. As a water af fact Alen M,

Turing has proved that there cannot exist an algorithm cepeble of inspecting

any text and establishing whether it is @ proper algorithm or not. The

assumption of the existence of such an algorithm leads to a contradiction which

will be sketched below. Suppose that we have such an algorithm, an inspection
"proper(L)"

## Page 20

EwD316 ~ 16
which delivers the result true when the text named L is @ proper algorithm
and the result false when it is improper. Consider now the following text,
paned Lt

L: “while proper(L) do whistle once"
(in which "whistle once" is assumed to be an available primitive). If we
start to follow this algorithm, how many times will a whistle sound? The
assumption that "proper(L)" delivers the result true will cause the algorithm
to be improper and vice versa! The conclusion is that no algorithm for the
inspection "proper" can exist. (Marvin Minsky conciudes in "Computation,
Finite and Infinite Machines", Prentice Hall, 1967 @ formal treatment of this
proof with the sentence: "We have only the deepest sympathy for those readers
who have not encountered this type of simple yet mind-boggling argument
before.".)

The moral of this story is that it is an intrinsic part of the duty of
everyone who professes to compose algarithms to supply a proof that his text
indeed represents a proper algorithm,

Our next fundamental notion is a machine (or a "computer"). A machine
is a mechaniom capable of causing actions to take place following a pattern
of behaviour such as can be described by algorithms expressed in terms of @
repertoire of primitive actions belonging to this machine.

Above we have given two algorithms for peeling potatoes, one for a
natural number of potatoes and one only for even numbers of potatoes. Both
algorithms have been expressed in the same repertoire of primitive actions.
They were introduced in the realm of "observing happenings"; the one could
describe the pattern of behaviour of my left-hand neighbour, the other the
one of my right-hand neighbour. Suppose that my ow wife
1} is also cepable of performing those primitive actions
2) will accept from me algorithms expressed in these primitives and will

follow such an algorithm obediently.

Then I can make her peel either as my left-hand neighbour or as my right-hand
neighbour, depending on the algorithm I have supplied to her. Then she is an :
exanple of @ machine.

## Page 21

ewD316 = 17

A mechanism that can only do one thing (such as one of the most widelyspread automata, the toilet flusher) is not called a machine. Essential for
us is the associated repertoire of actions, the ability to accept patterns
of behaviour and to behave accordingly.

Mechines are mechenicel algorithm followers. The fact thet in the lest
decennia increasingly powerful machines have becore available to mankind is
directly responsible for the increased importance of and interest in algorithms
and their composition.

Note. It is a trivial matter to compase an algorithm for the fastest machine
in the world, @ proper algorithm in the theoretical sense of the word but
somewhat impractical, as it would take the machine @ million years to carry
the corresponding process to completion. The claim that "the machine is
capable of causing the process to take place” is then somewhat subject to
doubt: in actual fact it cannot. In what follows we shalln't be bothered by
the distinction between "theoretically possible" and “practically feasible".
Not because we are imprectical, on the contrary! The point is thet in the
meantime computers are so powerful that the class of practically feasible
computations is by now sufficiently large —to put it mildly!~ to make
machines very useful and intriguing pieces of equipment, fully worthy of
our attention.

We call an algorithm intended to control the behaviour of a machine,

‘2 program. In other words, we reserve the nane program for those algorithms
that are intended for mechanical execution. In the general notion of an
algorithm we have only required that the repertoire should be “well-understood”,
without bothering how this understanding is established: if a composer
indicates "Andante" (= "going") for a composition in three-four time, he may

do 80, because, remarkably enough, we may expect this indication to be somehow
meaningful even for a player with two legs. In the case of a machine, the
situation is drastically different, for a machine is a finite piece of equipment
which, by its very construction, has associated with it a finite, very well
defined repertoire and whenever it is fed with @ program it shall behave
exactly as prescribed.

The fact that machines are completely obedient slaves has caused
complaints from many beginning programmers. Their obedience, they felt, makes

## Page 22

EwD316 - 18
progranming cruelly difficult, for a trivial misteke in the progran is sure
to lead to entirely unintended behaviour. The progremmer's inability to appeal
to "the common sense of the machine" has been experienced as one of its major
shortcomings. The more experienced progrenmer learns to appreciate its servile,
strict obedience: thanks to it we can instruct it to do something "uncommon"!
And this is something you cannot do with @ servant who "rounds off his
instructions to the nearest probable interpretation.

In the preceding paragraphs I have introduced progranming as an
important activity because now we have machines that can be controlled by
programs and for which we have to compose prograns when we want to use then,
i.e, when we want to convert them into the tool solving our problem. But this
is not the whole story. A computer is a many-sided thing. For its manufacturer
it is primarily @ product that he con (hopefully) produce and sell with
profit. For many institutional buyers the computer is probably primarily 2
status symbol. For many users it is either a source of endless worries or,
as the case may be, a highly useful tool. In University surroundings, the
view af the computer as a tool to be used tends to be the predominant one.

And there is no denying it: in their capacity of tools the computers are
changing the face of the earth (and of the moon as well!), Yet I am convinced
that we underestimate the computer's significance if we confine our appreciation
of it to the aspects mentioned. They may couse shocks to the basis of our
society, but I believe that in the longer run these will turn aut to be but
ripples on the surface of our culture, I expect a much more profound influence
fron the advent of the modern computer, viz. in its capacity of a gigantic
intellectual challenge, unprecedented in the history of mankind.

The computer as a piece of equipment presents us with an entirely new
combination of simplicity and power, which makes the programming task 3
unique challenge. When the electronic engineers have done their job properly,
they present to the progranmer @ mathenatically trivial piece of equipment.
Its instruction code (its "repertoire") can be described perfectly well on
2 modest number of pages, everything is finite ad discrete, there is just
no place for conceptually difficult mathematical notions, such as continuity,
infinity, Limits, irretional numbers ond whatnots. The mathematical basis of
programming is just very, very simple, so simple that programming should be
easy! it should be easy to conceive programs, it should be easy to convince
oneself that a prdigram is correct and that the machine working under its

oo _ _ a '

## Page 23

EWD316 = 19
control will indeed produce the desired result. From its besic simplicity
one derives the intuitive feeling that it should be o trivial matter to keep
the happening evoked by one's program firmly within one's intellectual grip.

But its besic simplicity is only one side of the coin: the other side
presents the extreme power (both as regards capacity and speed) of currently
available computers. As @ result of its extreme power, bath the amount of
information playing @ role in the computations as well as the number of
operations performed in the course of a computation, escape our unaided
imagination by several orders of magnitude. Due te the limited size of our
skull we are absolutely unable to visualize to any appreciable degree of
detail whet we are going to set in motion, and programming thereby cones an
activity facing us with conceptual problems that have risen far, far above
the originel level of trivielity.

Tt is the possibility of considering realistically effective solutions
of any degree of sophistication, combined with our complete intellectual
grip on what we ere considering, which will deeply influence our ways of
thinking end our appreciation of our own thought processes. It has no precedent,
for whenever in the past we were faced with something powerful (a storm or an
army) we never had effective control over it. (This, for a long time, used
to be the definition of "powerful", viz. that we were "powerless" in the

| face of it!)

## Page 24

EWD316 ~ 20
Progranming Languages and their Implementation.

The activity of composing programs is called "programming". In the
preceding section we have introduced programs as algorithms intended to
control the behaviour of machines and by virtue of the actual existence of
such machines, programming is a very practical activity. It is one of the
youngest branches of applied mathematics (in the broad sense of the word,

i.e. not confined to mathematical physics or numerical analysis), it is as
important as the applications in question, it is practical in the sense that
it is the programmer's intention that @ machine will actually displey the
behaviour as prescribed by the algorithn. For that reason @ conscious
programmer should respect the limitations of the (finite) machines. Alternative
prograns causing @ machine to establish the sane net result and therefore in
thet respect equivalent, may differ greatly in what is usually celled
"efficiency", ive. in the demands they make upon the machine's resources.
For many years, efficiency has been used as the sole yard-stick along which
to compare the relative quelity of elternative programs for the same task.
In the meantime, programming has turned aut to be so difficult, that other
quality aspects have gained relative importence, such as the ease with which
we can understand a progren, can convince ourselves of its correctness or
con modify it, etc. Yet, efficiency concerns cannot be ignored end in order
to give the reader some feeling for the nature of the limitations he should
respect, we shall give in this section an overall view of computing machines
and the way in which they execute programs.

In this little monograph we shall confine our attention to sequential
algorithms, i.e. algorithms describing what actions should happen in succession,
one after the other. Such algorithms have @ property for which they have been
blamed (and not entirely without justification), viz. that they are often
“overspecific" as regards the order in which things have to happen. If two
actions, say "A" and "B" have both to be done, @ purely sequential algorithm
will prescribe

either "A; BM or "By Ay,
viz. action A followed in tine by action B or the other way round. It will
‘not express that the order is immaterial and, what is possibly more importent,
it will not express that the two actions are so "non-interfering" with eachother
that they may take place concurrently, or ~ta use the jargon~ may be done in

## Page 25

EWDS16 - 2
parallel.
For various reasons I have decided to restrict my attention to purely
sequential programs. The most obvious reason is to be found in the structure
of the machines that are currently available or can be expected to becone
available in the next years. One or two decades ago, machines used to be
purely sequential. In the meantime we have got equipment allowing for a
Limited amount of parallelism (dual processor machines, independent communication
channels etc.), but such pieces of equipment are at best an aggregate of a
smell number of individual sequential components. In such machines the
| potential parellelien of activities is exploited by stendard control progrens
(so-called "operating systems"), while the individual user still works in a
strictly sequential environment. And it is to the individual user that this
Little monograph addresses itself.
With the advent of what is called “large scale integration” (being 2
term from the computer field, its acronym "LSI" is better known!) it seems
‘to become technically feasible to build machines nore like "clouds of arithmetic
units" with information processing activities going on simultaneously all
over the place, for shorter periods of time even independently of eachother.
Programming for such machines will pose completely different trade-off
problems; one will he willing to invest in potentially usefUl computing activity
before its actual usefulness has been established, all for the seke of speeding
up the whole computation. But although I know that such machines may be coming,
I shall not touch these problems for the following reasons. First, as fer as
general purpose applications are concerned, I have my doubts about the
effectiveness with which such forns of parallelism can ever be exploited.
Second and that is the most important consideration~ parallel programming
| is an order of magnitude more difficult than sequential programming. (This
statement will be doubted but I have enough experience in multiprogranming
to feel myself entitled to say so. The point is that with parallelism e
great variety of happenings mey take place under control of the same progran(s).
On account of undefined speed ratios a set of parallel prograns is written
for a partly non-deterministic machine and speciel care is required to ensure
that, on a higher level of abstraction, its totel behaviour can again be
regarded as uniquely determined by the program(s).) Third, I am not over~
impressed by the complaints that sequential programs specify @ more stringent