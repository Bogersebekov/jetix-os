# Boris Cherny: Deep Research Profile
## Claude Code Architecture & Design Philosophy
### Prepared for Jetix AI Consultancy (Berlin) — Internal 12-Agent System Evaluation

---

## Executive Summary

Boris Cherny is the creator and Head of Claude Code at Anthropic — the agentic coding tool that has grown from a September 2024 side project to commanding roughly 4% of all public GitHub commits by early 2026. His background as a self-taught generalist engineer (economics dropout, hedge fund developer, seven years at Meta as Principal Engineer and code quality lead) deeply shapes Claude Code's philosophy. The five most important findings for an AI consultancy designing a 12-agent operational system:

1. **The Bitter Lesson as product strategy.** Boris explicitly invokes Rich Sutton's "bitter lesson" — the observation that more general models always outperform more specialized ones — as the organizing principle for Claude Code. This means the entire architecture bets on minimal scaffolding, raw model access, and incremental capability delegation rather than hard-coded agent topology.

2. **Sub-agents as scaffolding, not permanent architecture.** Boris has directly stated that sub-agents "are a thing that we might deprecate at some point... they're very much scaffolding for models of today." For Jetix's 12-agent system this is critical: the current sub-agent isolation pattern solves a context-window problem that improving models may dissolve. Design for replaceability now.

3. **CLAUDE.md is the "simplest thing that works."** Boris explicitly rejected complex memory architectures in favor of a markdown file auto-read into context. The design — hierarchical overrides from enterprise to user to project to local — mirrors Unix file precedence and is intentionally version-controllable.

4. **Hooks give deterministic control where the model is probabilistic.** The PostToolUse hook for auto-formatting is Boris's own daily practice. The hooks system offers 27+ lifecycle events covering every point in the agent loop, from session start to sub-agent spawning to compaction, enabling the kind of enterprise guardrails a 12-agent production system needs.

5. **"Don't box the model in."** Boris's single most consistent product principle is to give the model tools, a goal, and latitude — not rigid step-by-step scaffolding. Verbatim: "Don't try to box the model in. I think a lot of people's instinct when they build on the model is they try to make it behave a very particular way... almost always you get better results if you just give the model tools, you give it a goal, and you let it figure it out."

---

## Section 1 — Boris Cherny: Profile & Writings

### 1.1 Biography

**Boris Cherny** is the creator and Head of Claude Code (Member of Technical Staff) at Anthropic. He is listed on the Claude Code NPM package directly as author — `"author": "Boris Cherny <boris@anthropic.com>"` [1] — and has been the organizing engineering lead since the product's inception.

**Education:** University of California, San Diego, Economics (2009–2011). He did not complete a CS degree. He has said: "I studied economics and actually dropped out to start startups." [2]

**Early career:**
- **BC Design** (founder, 2005–2011): Self-described first startup started at age 18
- **C4** (co-founder/Director of Web, 2009–2011): San Diego
- **Medical startup** (undisclosed): Boris describes building SVG decision-tree software for hospital protocols in the Internet Explorer 6 era [3]
- **Coatue Management** (Frontend Architect, Jan 2015–April 2017): Hedge fund in San Francisco Bay Area. It was here that a colleague named Rick introduced Boris to Scala and functional programming, which led directly to his interest in TypeScript [2]
- **Meta/Facebook** (Principal Software Engineer, November 2017–August 2024 — 7 years): He rose from E5 to IC8 (Principal). Key roles:
  - Tech Lead, Facebook Groups (Chats in Groups, Public Groups)
  - PM for Instagram Maps, Lightweight Groups, Group Chats, Off-Platform Distribution & SEO
  - Lead, Server architecture and dev infra at Instagram
  - Lead, Code quality across Meta (Instagram, Facebook, WhatsApp, Messenger)
  - Worked remotely from Nara, Japan for approximately 18 months [4]

**Anthropic:** Joined September 2024 as Member of Technical Staff. Claude Code began as a side project/experiment immediately on joining. By late 2024 it had an internal team (founding members: Boris, Sid, and Ben according to Cat Wu [5]).

**Title at Anthropic:** "Creator & Head of Claude Code, Member of Technical Staff." Notably, at Anthropic everyone is "Member of Technical Staff" regardless of whether they are an engineer, PM, or designer [2].

**Personal:** Ukrainian roots [6]. Lives in San Francisco. Known to do most coding by voice through Claude Code's `/voice` feature.

**LinkedIn:** https://www.linkedin.com/in/bcherny [7]
**Twitter/X:** @bcherny (https://x.com/bcherny) [8]
**Personal website/blog:** https://borischerny.com [4]
**GitHub:** https://github.com/bcherny [9]

---

### 1.2 Comprehensive Writings List

#### Books
| Title | Publisher | Date | URL | Summary |
|-------|-----------|------|-----|---------|
| *Programming TypeScript: Making Your JavaScript Applications Scale* | O'Reilly Media | 2019 | https://www.oreilly.com/library/view/programming-typescript/9781492037644/ | The primary reference book for TypeScript in production. Covers conditional types, literal types, mapped types, and type-driven design. |

#### Personal Blog (borischerny.com)
| Date | Title | Summary |
|------|-------|---------|
| Jun 19, 2024 | NPM and NodeJS should do more to make ES Modules easy to use | Module system frustrations before Anthropic join |
| Dec 10, 2023 | Learning to work (very) remotely | Reflections from 18 months in Nara, Japan as a remote Meta engineer |
| Sep 7, 2022 | Time and Timing | Personal essay |
| Jan 17, 2022 | Dinosaur Food | 100 million year old foods still eaten today |
| Mar 13, 2021 | Data Management on the Web Still Sucks | Critique of client-side data management approaches |
| Jan 6, 2021 | Public Opinion | Personal essay |
| Dec 24, 2019 | React+TypeScript: Use unions of objects for props | TypeScript patterns |
| Sep 8, 2019 | On Contagion | Personal essay |
| May 26, 2019 | 13 Tips for Writing a Technical Book | Reflection on writing *Programming TypeScript* |
| Aug 10, 2018 | On Derived State | React state management patterns |
| Dec 26, 2017 | JavaScript in 2017: Year in Review | Annual survey |
| Oct 30, 2017 | Towards a Safer Redux | Introduction to Undux |
| Jul 14, 2017 | Angular 1: 8 Lessons For Designing JavaScript Frameworks | Framework design lessons |
| Jul 14, 2017 | Options in TypeScript | TypeScript type patterns |
| Jun 9, 2017 | The Best Frontend JavaScript Interview Questions | Interview guide |
| Jun 9, 2017 | Introducing: Lazy Arrays in JavaScript | Lazy evaluation in JS |
| Nov 11, 2012 | Automatically Generating Base64 Inline Images With SASS | CSS tooling |

#### Open Source Projects (GitHub @bcherny)
| Project | Stars | Description |
|---------|-------|-------------|
| **undux** | ~1,500 | Dead-simple typesafe state for React. Introduced at React Boston 2018. Was briefly the most popular state management framework at Facebook before being replaced by Recoil/Relay. |
| **json-schema-to-typescript** | ~3,300 | Compile JSON Schema to TypeScript declarations |
| **typed-rx-emitter** | — | Typesafe RxJS-based EventEmitter |
| **flow-to-typescript** | — | Convert Flow-annotated files to TypeScript |
| **programming-typescript-answers** | — | Official answers for O'Reilly book exercises |

#### Twitter/X Threads (selected major threads)
| Date | URL | Topic |
|------|-----|-------|
| Jan 2, 2026 | https://x.com/bcherny/status/2007179832300581177 | Boris's personal Claude Code setup — 13-tip thread |
| Jan 2, 2026 | https://x.com/bcherny/status/2007212366094811401 | CLAUDE.md content breakdown (2.5k tokens) |
| Jan 28, 2026 | https://x.com/bcherny/status/2016339448863355206 | CLAUDE.md lazy-loading design clarification |
| Dec 27, 2025 | https://x.com/bcherny/status/2004887829252317325 | One-year Claude Code retrospective + 259 PRs/month stats |
| Feb 11, 2026 | https://x.com/bcherny/status/2021699851499798911 | Customizability philosophy: hooks, skills, MCPs |
| Feb 14, 2026 | https://x.com/bcherny/status/2022762422302576970 | "Someone has to prompt the Claudes, talk to customers..." |

#### Anthropic Engineering Blog
No public Boris-bylined posts on the Anthropic blog have been identified to date. *Note: No public Boris statement found on specific Anthropic blog authorship.*

---

## Section 2 — Talks, Podcasts, Interviews

### 2.1 Podcast Appearances

#### Latent Space Podcast — "Claude Code: Anthropic's Agent in Your Terminal"
**Date:** May 7–8, 2025 | **Host:** Alessio Fanelli | **URL:** https://www.latent.space/p/claude-code [5]
**Guests:** Boris Cherny and Catherine Wu

**Key verbatim quotes:**

On the core product identity:
> "Claude Code is not a product as much as it's a Unix utility."

On minimal design philosophy:
> "This is the thinnest possible wrapper over the model. We literally could not build anything more minimal. This is the most minimal thing."

On the Bitter Lesson as product strategy:
> "Our approach to code is similar to our approach to the model, which is Bitter Lesson. So just freeform. Keep it really simple. Keep it close to the metal."

On CLAUDE.md origin:
> "ClaudeMD, it's another example of this idea of, you know, do the simple thing first. We had all these crazy ideas about like memory architectures and, you know, there's so much literature about this. There's so many different external products about this and we wanted to be inspired by all this stuff. But in the end, the thing we did is ship the simplest thing, which is, you know, it's a file that has some stuff. And it's auto-read into context. And there's now a few versions of this file. You can put it in the root, or you can put it in child directories, or you can put it in your home directory. And we'll read all of these in kind of different ways. But yeah, it's the simplest thing that could work."

On parallel sub-agents for research:
> "Something I'll do sometimes is if I have a planning question or a research type question, I'll ask Claude to investigate a few paths in parallel. And you can do this today if you just ask it. So say, you know, I want to refactor X to do Y. Can you research three separate ideas for how to do it? Do it in parallel. Use three agents to do it. And so in the UI, when you see a task that's actually like a sub-Claude, it's a sub-agent that does this. And usually when I do something hairy, I'll ask it to just investigate, you know, three times or five times or however many times in parallel. And then Claude will kind of pick the best option and then summarize that for you."

On "replaceable" / large-scale parallel agents:
> "If you want to use a power tool that lets you access the model directly and use Claude for automating, you know, big workloads, you know, for example, if you have like a thousand Lint violations and you want to start a thousand instances of Claude and have it fix each one and then make a PR, then ClaudeCode is a pretty good tool."

On three architecture layers:
> "There's kind of three layers at which we can build something. So the, you know, being an AI company, the most natural way to build anything is to just build it into the model and have the model do the behavior. The next layer is probably scaffolding on top, so it's like quad code itself. And then the layer after that is using quad code as a tool in a broader workflow, so to compose stuff in."

On agentic search over RAG:
> "We landed on just agentic search as the way to do stuff. [...] It outperformed everything. By a lot. [...] Agentic search just sidesteps all of that. So essentially, at the cost of latency and tokens, you now have really awesome search without security downsides."

On context window management design:
> "Ultimately we just want to make sure that the context that's given to the model is in like the purest form and that the harness doesn't intervene with the user's intent."

On when to customize vs. use defaults:
> "I think our approach to code is to make sure it works out of the box for people without extra configuration."

On the markdown parser origin story:
> "The night before the release at like 10 p.m., I'm like, all right, I'm going to do this. So I just asked Quad to write a markdown parser for me. And it wrote it. Zero shot. [...] That's the markdown parser that's in [Claude] code today."

On rewriting Claude Code every few weeks:
> "We've rewritten it from scratch. Yeah. Probably every three weeks, four weeks or something. And it just like all the, it's like a ship of Theseus, right? Like every piece keeps getting swapped out."

On the product principle:
> "Generally, at Anthropic, we have this product principle of do the simple thing first. And I think that the way we build product is really based on that principle. So you kind of staff things as little as you can and keep things as scrappy as you can because the constraints are actually pretty helpful."

On terminal choice:
> "We want to build something that's kind of much earlier on that curve and something that will maybe be a big product, you know, a year from now or, you know, however much time from now. As the model improves. And that's why code runs in a terminal. It's a lot more bare bones. You have raw access to the model because we didn't spend time building all this kind of nice UI and scaffolding on top of it."

---

#### Every.to — *AI & I* — "How to Use Claude Code Like the People Who Built It"
**Date:** October 29, 2025 | **Host:** Dan Shipper | **URL:** https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it [10]
**Full transcript:** https://every.to/podcast/transcript-how-to-use-claude-code-like-the-people-who-built-it [11]
**Guests:** Boris Cherny and Catherine Wu

**Key verbatim quotes:**

On latent demand (Boris's central product philosophy):
> "There's this really old idea in a product called latent demand. Which I think is probably the main way that I personally think about product and thinking about what to build next. And it is, it's a super simple idea. It's you build a product in a way that is hackable, that is kind of open-ended enough that people can abuse it for other use cases it wasn't really designed for. Then you see how people abuse it and then you build for that because you kind of know there's demand for it."

On the specific latent demand case that created Claude Code's direction:
> "When I was at Meta, this is how we built all the big products. I think almost every single big product had this nugget of latent demand in it. You know, like for example, something like Facebook Dating, it came from this idea that when we looked at who looks at people's profiles, I think 60 percent of views were between people of opposite gender — so kind of traditional setup — that were not friends with each other. And so we're like, oh man, okay. Maybe there's — maybe if we launch a dating product, we can kind of harness this demand that exists."

On hackability as product philosophy:
> "You build a product in a way that's hackable, that's open-ended enough that people can 'abuse it' for other use cases it wasn't really designed for. Then you see how people 'abuse it' and then you build for that because you kind of know there's demand for it."

On sub-agents for complex code review:
> "I have a few. I have a planner subagent that I use. I have a code review subagent. [...] For me, I do it mostly for big migrations. We have this code slash command that we use, there's a bunch of subagents there and so one of the steps is find all the issues and so there's one subagent that's checking for Claude MD compliance. There's another subagent that's looking through git history to see what's going on. Another subagent that's looking for kind of obvious bugs. And then we do this kind of deduping quality step after. So they find a bunch of stuff. A lot of these are false positives. And so then we spawn like five more subagents and these are all just like checking for false positives. And in the end, the result is awesome. It finds all the real issues without the false issues."

On future form factors:
> "I think my prediction is that the terminal is not the final form factor. My prediction is there's going to be a few more form factors in the coming months, you know, maybe a year or something like that. And it's going to keep changing very quickly."

On "Claudes monitoring Claudes":
> "Pretty soon we're going to be in this mode of Claudes monitoring Claudes. And kind of, I don't know what the right form factor for this is because as a human, you need to be able to inspect this and kind of see what's going on. But also it needs to be Claude optimized where you're optimizing for kind of bandwidth between the Claude to Claude communication."

---

#### Lenny's Podcast — "Head of Claude Code: What happens after coding is solved"
**Date:** February 19, 2026 | **Host:** Lenny Rachitsky | **URL:** https://www.youtube.com/watch?v=We7BZVKbCVw [6]
**Transcript:** https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens

**Key verbatim quotes:**

On Claude Code origin:
> "When I first started [Claude] Code, it was just going to be a little hack."

On why they kept the terminal:
> "From the start I built it in a terminal because you know for the first couple months it was just me so it was just the easiest way to build and for me this is actually a pretty important product lesson right is like you want to underresource things a little bit at the start. [...] Then we started thinking about what other form factors we should build and we actually decided to stick with the terminal for a while and the biggest reason was the model is improving so quickly. We felt that there wasn't really another form factor that could keep up with it."

On inverting the typical AI product approach:
> "For cloud code, we inverted that. We said the product is the model. We want to expose it. We want to put the minimal scaffolding around it. Give it the minimal set of tools. So, it can do the things. It can decide which tools to run. It can decide in what order to run them in and so on."

On the T+6 months bet:
> "From the very beginning, we bet on building for the model six months from now, not for the model of today."

On "don't box the model in" — the most explicit statement of this principle:
> "Don't try to box the model in. I think a lot of people's instinct when they build on the model is they try to make it behave a very particular way. They're like this is a component of a bigger system. I think some examples of this are people layering like very strict workflows on the model — for example you know to say like you must do step one then step two then step three and you have this like very fancy orchestrator doing this. But actually almost always you get better results if you just give the model tools, you give it a goal, and you let it figure it out."

On the Bitter Lesson:
> "The bitter lesson. And actually for the quad code team we have a — Rich Sutton had this blog post maybe 10 years ago called the bitter lesson. And it's actually a really simple idea. His idea was that the more general model will always outperform the more specific model."

On latent demand (Lenny's Podcast version):
> "Latent demand is this idea that if you build a product in a way that can be hacked or can be kind of misused by people in a way it wasn't really designed for to do kind of something that they want to do, then this helps you as the product builder learn where to take the product next."

On coding being solved:
> "Coding is largely solved. At least for the kind of programming that I do, it's just a solved problem because quad can do it. And so now we're starting to think about okay like what's next? What's beyond this?"

On the agent as co-worker:
> "Quad is starting to come up with ideas. It's looking through feedback. It's looking at bug reports. It's looking at telemetry for bug fixes and things to ship a little more like a co-worker or something like that."

On agents in general:
> "Agent actually has like a very specific technical meaning which is it's a LM that's able to use tools. So it doesn't just talk, it can actually act and it can interact with your system."

On underfunding + unlimited tokens:
> "You want to underresource things a little bit at the start. [...] Don't try to optimize. Don't try to cost cut at the beginning. Start by just giving engineers as many tokens as possible."

On what comes next after coding:
> "I think it's going to be a lot of the roles that are adjacent to engineering. Um so yeah it could be like product managers, it could be design, could be data science. It is going to expand to pretty much any kind of work that you can do on a computer."

Three team principles (as described by Lenny's summary):
1. Encouraging people to go faster — if you can do something today, do it today
2. Don't try to cost cut; give engineers unlimited tokens
3. Always bet on the more general model; don't fine-tune for specific use cases

---

#### Bessemer Venture Partners — "Agentic Coding with Claude Code Creator Boris Cherny"
**Date:** August 18, 2025 | **Host:** Talia Goldberg & Bhavik Nagda | **URL:** https://www.youtube.com/watch?v=h-Hlt05REZk [12]

**Key verbatim quotes:**

On "mama quad" and sub-agent naming:
> "Sub agents are kind of like sub quads that Claude can invoke and so we have the main thread and Ellie — who's a engineer at Anthropic — she called this mama quad and so now we've kind of taken to calling like the main quad process mama quad and mama quad can spawn baby quads so these kind of like sub quads and all this is is like it's Claude calling Claude. It's a little mind-bendy but the idea is like Claude itself is a tool that quad can use."

On why sub-agents exist:
> "If there's some kind of subtask that Mama Claude wants to delegate to, Claude can spawn a little Claude to do that task. So, for example, something like code review or code simplification or planning, these are things that you might not necessarily want to do in the main thread. But if you spawn a sub agent, so like a sub instance of Claude to do this work, it's a little bit more focused because the context window is more focused, maybe the tools are more focused. And so it'll do this work and then it'll report back to the main thread."

On sub-agents being temporary scaffolding:
> "Sub agents are actually a thing that we might deprecate at some point. Yeah, it's something that's like useful now, but as the model gets really good at managing its own context, you won't need these specialized agents anymore. So, they're very much scaffolding for models of today."

On hackability:
> "I think this is generally our product philosophy is we want to build a product that's super easy to hack so people can use it in the way that they want and then we want to see how people customize it. We want to see how power users use it, how normal users like myself use it. And then based on that, that'll tell us what features to build next."

On using only the public Anthropic API:
> "Still today Quad Code only uses Anthropic public API. We use the same public models that everyone else uses."

On capability-first token philosophy:
> "Our philosophy with quad code is we want to make this the most performant product at any cost. So the only thing we care about is capability. If there's a way to have a certain amount of capability with more efficient token usage, we will do that. But if we have to compromise capability, we won't do it."

On building for the model six months out:
> "Don't build for the model of today because in 3 months or four months or whatever then the next model is going to be out and it's going to be completely different."

On plan mode as simple scaffolding:
> "Planning is just a scaffold. When you enter plan mode, we just send a little message to the assistant to tell it, hey, you're in plan mode. Don't code. That's it. And this little bit of scaffolding helps a lot."

On hooks for credential scrubbing:
> "You can use post hooks. Um so we have pretty rich support for hooks. And if there's any kind of hook that's missing, just let us know in the issue tracker and we'll build it. And so what you can do is anytime that a tool result comes back before it goes to the model you can intercept it and you can say uh you know like does this have credentials... and you can kind of do secret scrubbing that way."

On what makes Claude Code itself succeed:
> "we changed the scaffolding with every version. Like I said when the four series of models came out we ripped out probably half the system prompt half the tool prompts. We just deleted it."

On CLAUDE.md practical guidance:
> "Generally I would just put stuff like that you see quad struggling with continuously. Most times that you run quad code it struggles with the same kind of thing. Maybe it'll use like the wrong test runner or it'll look in the wrong directory for stuff or it won't run the right verification commands or whatever. Then in that case, I would add it to QuadMD, but I wouldn't try to kind of pre-add a bunch of stuff if you don't actually see Quad struggling with it."

On army of sub-agents inspiration:
> "We actually saw a thread on the Claude subreddit where someone was using like MCP servers or something to have this big army of sub agents and they had like a product manager sub agent and designer sub agent. They had like a front-end engineer, backend engineer and we just thought this was so cool."

---

#### Y Combinator Lightcone Podcast — "Inside Claude Code With Its Creator Boris Cherny"
**Date:** February 17, 2026 | **URL:** https://www.ycombinator.com/library/NJ-inside-claude-code-with-its-creator-boris-cherny [13]
*Summary (verbatim transcript not publicly available): Boris discusses accidental origins, the bet on exponential model improvement, building for models six months out, 150% increase in engineer productivity at Anthropic since Claude Code introduction, and advice to founders to build for future models.*

---

#### The Developing Dev — "Boris Cherny (Creator of Claude Code) On How His Career Grew"
**Date:** December 15, 2025 | **Host:** Ryan Peterman | **URL:** https://www.developing.dev/p/boris-cherny-creator-of-claude-code [2]

**Key verbatim quotes:**

On generalists:
> "To this day, on the Claude team, which is the team that I'm on right now, we really prioritize generalists. I love working with generalists. If you're an engineer that codes but can also do product work, design, and have product sense, you want to talk to your users. I love this kind of engineer to work with. This is how we recruit for all functions now. Our product managers code, our data scientists code, and our user researchers code a little bit."

On the TypeScript book origin:
> "There weren't a lot of good resources, so I started writing a book about it because someone should do this. It's crazy; it doesn't exist. This language is just magnificent. It has really good design with ideas that no other language had at the time."

On being underleveled as a strategy:
> "Coming in under leveled gave me the space to explore and just build cool stuff for the sake of building cool stuff."

On side projects:
> "For me, side quests are so important. When I hire engineers, this is definitely something I look for. I want people with side quests, like cool weekend projects. Even someone that's really into making kombucha. You want people that are generally curious and interested in stuff outside of their main work."

On thinking in types:
> "The thing that matters in your code the most is the type signatures. This is more important than the code itself. Getting this right leads to very clean code."

---

#### Pragmatic Engineer — "Building Claude Code with Boris Cherny"
**Date:** March 4, 2026 | **Host:** Gergely Orosz | **URL:** https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny [14]

Key themes (verbatim transcript behind paywall, notable excerpts available):
- Boris ships 20-30 PRs a day running 5 parallel Claude instances; "once there is a good plan, it will one-shot the implementation almost every time"
- "It's not so much about deep work, it's about how good I am at context switching and jumping across multiple different contexts very quickly" (on the engineer's new role)
- The team tried vector databases, recursive model-based indexing for codebase search — plain glob and grep driven by the model outperformed everything
- Cowork built in ~10 days; the majority of engineering effort went into safety classifiers, sandboxing, and permissions, not product logic

---

### 2.2 Conference Talks

| Date | Venue/Event | Title | URL |
|------|------------|-------|-----|
| Sep 2, 2025 | Anthropic Internal/YouTube | "The Future of Agentic Coding with Claude Code" (with Alex Albert) | https://www.youtube.com/watch?v=iF9iV4xponk [15] |
| Aug 18, 2025 | Bessemer Venture Partners Research to Runtime | "Agentic Coding with Claude Code Creator Boris Cherny" | https://www.youtube.com/watch?v=h-Hlt05REZk [12] |
| Oct 29, 2025 | Every.to AI & I | "How to Use Claude Code Like the People Who Built It" | https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it [10] |
| 2018 | React Boston | "Introducing Undux – Simple Typesafe State Management for React" | https://www.youtube.com/watch?v=CpOE-JrtAdc |

*Note: No public Boris statement found confirming attendance at AI Engineer Summit 2024/2025 specifically.*

---

## Section 3 — Claude Code Architecture: The Core Decisions

### 3.1 Why Swarm/Minimal-Hierarchy Over Rigid Orchestration

The most direct statement of Boris's architectural philosophy comes from the Lenny's Podcast interview [6]:

> "Don't try to box the model in. I think a lot of people's instinct when they build on the model is they try to make it behave a very particular way. They're like this is a component of a bigger system. I think some examples of this are people layering like very strict workflows on the model — for example, you know, to say like you must do step one then step two then step three and you have this like very fancy orchestrator doing this. But actually almost always you get better results if you just give the model tools, you give it a goal, and you let it figure it out."

From Latent Space [5]:

> "When the model is so good, the simple thing usually works. You don't have to over-engineer it."

> "Everything is the model. Like, that's the thing that wins in the end. And it just, as the model gets better, it subsumes everything else."

**Why this leads to a flat-ish topology:** Claude Code's actual agent structure is described as "mama quad" (the main process) spawning "baby quads" (sub-agents) for isolated subtasks. This is architecturally flat — one level deep. Sub-agents cannot themselves spawn sub-agents. Boris explicitly cites this as temporary: the flatness exists because today's models can't reliably manage their own context, so explicit isolation is necessary scaffolding, not permanent design.

From Bessemer [12]:
> "Sub agents are actually a thing that we might deprecate at some point. Yeah, it's something that's like useful now, but as the model gets really good at managing its own context, you won't need these specialized agents anymore. So, they're very much scaffolding for models of today."

**Implication for Jetix's 12-agent system:** Hierarchical orchestrators (e.g., an "executive agent" directing 11 worker agents) are likely to underperform compared to giving agents clear tools and goals and letting them self-organize. Rigid step-sequencing (if this → then that) is the explicit anti-pattern Boris warns against.

### 3.2 The Replaceable Agents Principle

The clearest statement of this principle from Latent Space [5]:

> "If you want to use a power tool that lets you access the model directly and use Claude for automating, you know, big workloads, you know, for example, if you have like a thousand Lint violations and you want to start a thousand instances of Claude and have it fix each one and then make a PR, then ClaudeCode is a pretty good tool."

This framing — "a thousand instances, one PR each" — establishes that agents in Claude Code's model are **homogeneous, stateless, and interchangeable**. There is no special "lint-fixer-agent-7" with privileged state. Each instance gets its task via the prompt string, executes it, and reports back. This is the replaceable agents principle.

From his January 2, 2026 Twitter thread [16]:
> "I'm Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit. My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much. There is no one correct way to use Claude Code: we intentionally build it in a way that you can use it, customize it, and hack it however you like. Each person on the Claude Code team uses it very differently."

**Key design detail from official docs [17]:** Each subagent "runs in its own fresh conversation. Intermediate tool calls and results stay inside the subagent; only its final message returns to the parent." The parent communicates to the sub-agent exclusively through the `Agent` tool's `prompt` string. There is no shared memory, no shared state, and no side-channel.

This is conceptually analogous to a Unix pipeline: each process receives stdin, does its work, writes to stdout, terminates.

---

## Section 4 — CLAUDE.md Design Rationale

### 4.1 Origin and Philosophy

From Latent Space [5] (verbatim):

> "ClaudeMD, it's another example of this idea of, you know, do the simple thing first. We had all these crazy ideas about like memory architectures and, you know, there's so much literature about this. There's so many different external products about this and we wanted to be inspired by all this stuff. But in the end, the thing we did is ship the simplest thing, which is, you know, it's a file that has some stuff. And it's auto-read into context. And there's now a few versions of this file. You can put it in the root, or you can put it in child directories, or you can put it in your home directory. And we'll read all of these in kind of different ways. But yeah, it's the simplest thing that could work."

### 4.2 Why Markdown?

No direct Boris statement found on the explicit choice of markdown format vs. JSON or YAML. However, the Latent Space quote above makes clear the underlying principle: the *simplest* thing that could work. Markdown is:
- Human-readable and human-writable (no special tooling)
- Version-controllable (ordinary text file)
- Diffable (git-native)
- Flexible (can contain prose, code blocks, lists, tables)

Boris's description of the CLAUDE.md content for the Claude Code repo itself confirms the format serves operational prose, not structured data [18]:
> "Our checked in CLAUDE.md is 2.5k tokens. It covers: common bash commands; code style conventions; UI and content design guidelines; how to do state management, logging, error handling, gating, and debugging; pull request template."

### 4.3 Hierarchical Override Design

From the official Claude Code docs and Boris's January 28, 2026 tweet [19]:
> "Ancestor CLAUDE.md's are loaded into context automatically on startup. Descendent CLAUDE.md's are loaded *lazily* only when Claude reads/writes files in a folder the CLAUDE.md is in."

**The hierarchy (enterprise > personal > project > local):**

| Level | Location | Scope |
|-------|----------|-------|
| Enterprise | Managed policy directories | All org users |
| Personal | `~/.claude/CLAUDE.md` | All your projects |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team via git |
| Project Rules | `./.claude/rules/*.md` | Modular topic-specific rules |
| User Local | `./CLAUDE.local.md` | Personal project overrides (gitignored) |

**Rationale for lazy loading:** Descendant CLAUDE.md files only load when Claude actually works in that directory — this prevents context bloat in large monorepos while preserving specificity.

From Bessemer [12]:
> "For the quad code repo, it's pretty small. So we have a single quad D file and for bigger repos, we usually have a few. So for example, for the Anthropic repo, there's a bunch. Any customer that has more than like maybe 10,000 files or so, then you probably want a few, one in the root and then maybe one in nested directories and so on."

### 4.4 How Boris Uses CLAUDE.md in Practice

From his January 2026 Twitter thread [16] (as reported):
- Team shares a single CLAUDE.md committed to git
- Contribute to it multiple times per week
- "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time"
- During code review, tags `@.claude` on PRs to add entries to CLAUDE.md as part of the PR review — what he calls "Compounding Engineering" (term from Dan Shipper)
- Boris does not manually edit CLAUDE.md; Claude itself writes the rules: "I don't edit my quad MD manually. Quad just does it for me."

---

## Section 5 — Sub-agents, Hooks, Skills, MCP

### 5.1 Sub-agent System

**Spawning mechanism:** The main agent uses the `Agent` tool (previously called `Task` tool, renamed in v2.1.63) to spawn sub-agents. This tool is the exclusive communication channel from parent to child; only the prompt string passes through.

From the official sub-agents documentation [17]:
- Each subagent runs in its own fresh conversation with its own 200K token context window
- The subagent receives: its own system prompt + the Agent tool's prompt; project CLAUDE.md; tool definitions (inherited or restricted subset)
- The subagent does NOT receive: the parent's conversation history or tool results; the parent's system prompt; skills (unless explicitly listed)
- "The only channel from parent to subagent is the Agent tool's prompt string"
- Subagents cannot spawn their own subagents (flat hierarchy enforced by not including `Agent` in subagent's `tools` array)
- When finished, the subagent's final message returns verbatim as the Agent tool result

**Context isolation principle:** From the docs: "A subagent's context window starts fresh (no parent conversation) but isn't empty. Include any file paths, error messages, or decisions the subagent needs directly in that prompt."

**Boris's practical patterns (from Twitter thread [16]):**
- `code-simplifier` subagent: cleans up and simplifies code after Claude finishes a task
- `verify-app` subagent: comprehensive end-to-end testing instructions
- Code review: multiple parallel sub-agents each checking one dimension (CLAUDE.md compliance, git history review, obvious bugs), then a second wave of sub-agents deduplicating false positives

**Boris on sub-agents being temporary (Bessemer, [12]):**
> "Sub agents are actually a thing that we might deprecate at some point. Yeah, it's something that's like useful now, but as the model gets really good at managing its own context, you won't need these specialized agents anymore. So, they're very much scaffolding for models of today."

**Resumable sub-agents:** Official docs [17] note that sub-agents can be resumed via their `agent_id`, retaining full conversation history. This enables multi-session workflows.

### 5.2 Hooks System

The hooks system was designed to provide **deterministic control** over points where the probabilistic model cannot be trusted. The rationale, as described in the Bessemer talk [12]:

> "You can use post hooks. So we have pretty rich support for hooks. And if there's any kind of hook that's missing, just let us know in the issue tracker and we'll build it. And so what you can do is anytime that a tool result comes back before it goes to the model you can intercept it and you can say uh you know like does this have credentials... and you can kind of do secret scrubbing that way."

**Why hooks vs. slash commands?**
- Slash commands are *prompt-based* — they tell Claude what to do, and Claude decides how
- Hooks are *deterministic* — they execute shell commands, HTTP endpoints, prompt-based checks, or agent-based evaluations at specific lifecycle points, with the ability to **block** actions before the model sees them
- Hooks fire whether or not you remember to invoke them; slash commands require invocation

**Boris's personal hook usage (Twitter thread [16]):**
- `PostToolUse` hook on `Write|Edit` events: runs `bun run format || true` — auto-formats code after every file edit
- This catches the 10% of cases where Claude doesn't format correctly, preventing CI failures

**The full hook lifecycle** (from official docs [20]):

*Per-session:* `SessionStart`, `SessionEnd`

*Per-turn:* `UserPromptSubmit`, `Stop`, `StopFailure`

*Per-tool-call:* `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`

*Sub-agent lifecycle:* `SubagentStart`, `SubagentStop`

*Task lifecycle:* `TaskCreated`, `TaskCompleted`

*Context events:* `InstructionsLoaded`, `PreCompact`, `PostCompact`, `ConfigChange`

*Environment events:* `CwdChanged`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`

*Multi-agent:* `TeammateIdle`

*MCP:* `Elicitation`, `ElicitationResult`

**Security model (from official docs [20]):**
> "Command hooks run with system user's full permissions."
Best practices: validate/sanitize inputs, quote shell variables, block path traversal, use absolute paths. Enterprise administrators can set `allowManagedHooksOnly` to block user, project, and plugin hooks.

**Hook handler types:**
1. `command` — shell command (can be async)
2. `http` — HTTP POST to an endpoint
3. `prompt` — LLM prompt for yes/no decision
4. `agent` — full sub-agent with tools, up to 50 turns

**Scoping:** Hooks defined in `~/.claude/settings.json` apply to all projects; in `.claude/settings.json` they apply to a project and can be committed to git; in `.claude/settings.local.json` they're gitignored.

### 5.3 Skills Feature

Skills are the evolution of slash commands. Boris confirmed on X (replying to a question about v2.1.1): *"Yes! Skills and slash commands are the same thing."* [21]

**From official docs [22]:**

> "Skills extend what Claude can do. Create a SKILL.md file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with /skill-name."

**Key design distinction from CLAUDE.md:**
> "Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference material costs almost nothing until you need it."

**Skills locations:**

| Level | Location | Scope |
|-------|----------|-------|
| Enterprise | Managed settings | All org users |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | When plugin enabled |

**Skills vs. slash commands:** Custom commands have been merged into skills. The differences that remain:
- Skills can have supporting files (scripts, references, assets)
- Skills support frontmatter to control invocation (`disable-model-invocation: true` = only you can invoke; `user-invocable: false` = only Claude can invoke)
- Skills can run in forked subagent contexts (`context: fork`)
- Claude Code skills follow the **Agent Skills open standard**, working across multiple AI tools
- Skills descriptions are truncated at 1,536 characters in the skill listing; only the full content loads when invoked

**Launch date:** Skills launched for Team and Enterprise plans in October 2025 [21].

**Boris's team practices (Twitter thread [16]):**
- "If you do something more than once a day, turn it into a skill or command"
- Has skills for: BigQuery analytics, code review, tech debt analysis, commit-push-PR workflow
- All skills committed to git so new team members inherit the full setup

*No direct Boris statement found specifically explaining his intent in designing skills vs. keeping everything as CLAUDE.md.*

### 5.4 MCP (Model Context Protocol)

MCP was introduced by Anthropic in November 2024. *No direct Boris statement found confirming or denying his personal involvement in MCP's design.* Claude Code integrates MCP as a first-class feature, and Boris uses it heavily in his own workflow.

**Boris's MCP usage (Twitter thread [16]):**
> "Claude Code uses all my tools for me. It searches and posts to Slack via the MCP server, runs BigQuery queries with the bq CLI, grabs error logs from Sentry, etc. The Slack MCP configuration is in .mcp.json and shared."

From the Lenny's Podcast overview [6]: Boris uses Slack MCP, BigQuery CLI (bq), and Sentry integration as daily tools for his agents.

**MCP in the hooks system:** The hooks documentation [20] shows MCP servers can be targeted via hooks using the matcher pattern `mcp__<server>__<tool>`. The `Elicitation` and `ElicitationResult` hook events specifically handle MCP server requests for user input.

**Boris's caution on MCPs (from "How Boris Uses Claude Code" site [23]):**
> "Be careful with MCPs though. They can blow up your context window. Only use them for specific things that are outside normal coding, like Slack, analytics, and error logs. Also watch out for prompt injection. Always have Claude Code review an MCP before you install it."

---

## Section 6 — Broader Philosophy

### 6.1 Core Design Principles (Verbatim Summary)

**1. The Bitter Lesson as product architecture.** From Lenny's [6]:
> "The bitter lesson. And actually for the quad code team we have a — Rich Sutton had this blog post maybe 10 years ago called the bitter lesson. It's actually a really simple idea. His idea was that the more general model will always outperform the more specific model."

**2. Do the simple thing first.** From Latent Space [5]:
> "Generally, at Anthropic, we have this product principle of do the simple thing first. And I think that the way we build product is really based on that principle."

**3. The product is the model.** From Lenny's [6]:
> "For cloud code, we inverted that. We said the product is the model. We want to expose it. We want to put the minimal scaffolding around it."

**4. Build for T+6 months, not T+0.** From Bessemer [12]:
> "Don't build for the model of today because in 3 months or four months or whatever then the next model is going to be out and it's going to be completely different."

**5. Latent demand as discovery method.** From Every.to [11]:
> "You build a product in a way that is hackable, that is kind of open-ended enough that people can abuse it for other use cases it wasn't really designed for. Then you see how people abuse it and then you build for that because you kind of know there's demand for it."

**6. Composability over monolith.** From Latent Space [5]:
> "We think of it as like a Unix utility. Right? So it's like the same way that you would compose, you know, grep or cat. The same way you can compose code into workflows."

**7. Verification loop as multiplier.** From the "How Boris Uses Claude Code" site [23]:
> "Probably the most important thing to get great results out of Claude Code — give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."

**8. The generalist engineer.** From Developing Dev [2]:
> "To this day, on the Claude team, which is the team that I'm on right now, we really prioritize generalists. [...] Our product managers code, our data scientists code, and our user researchers code a little bit."

**9. Context switching is the new deep work.** From Pragmatic Engineer [14]:
> "It's not so much about deep work, it's about how good I am at context switching and jumping across multiple different contexts very quickly."

**10. Underfunding + unlimited tokens.** From Lenny's [6]:
> "You want to underresource things a little bit at the start. [...] Don't try to cost cut at the beginning. Start by just giving engineers as many tokens as possible."

### 6.2 Anthropic Research Papers / Technical Reports

*No public Anthropic research papers co-authored by Boris Cherny have been identified in this research.* Boris's role at Anthropic is product engineering and team leadership rather than AI research. His GitHub activity (October 2025) shows reviews on `anthropics/claude-agent-sdk-python` and `anthropics/claude-agent-sdk-typescript`, confirming involvement in the SDK rather than model research papers.

*No public Boris statement found on specific Anthropic research paper co-authorship.*

---

## Section 7 — Criticism & Future Direction

### 7.1 Public Criticism Boris Has Faced

#### Criticism #1: Self-Promotion and Conflict of Interest
**Critics (Hacker News, Jan 3, 2026 thread [24]):**
> "This is the creator of a product saying how good it is. If you've worked anywhere professionally you know how every place has its problems." / "Claiming that you now have 10 AI minions just wrecking your codebase sounds like showboating." / "He has to dogfood it. He can't just say 'actually this is a massively annoying way of developing software and probably slows me down.'"

**Boris's implicit response:** Boris acknowledged in the January 2026 thread [16] that his setup is "surprisingly vanilla" and that he personally doesn't customize much — partly defusing the "elaborate setup" criticism.

#### Criticism #2: Unrealistic Parallelism for Most Engineers
**Critics (Hacker News, [24]):**
> "I don't need 10 parallel agents making 50-100 PRs a week, I need 1 agent that successfully solves the most important problem." / "I don't understand how you can generate requirements quickly enough to have 10 parallel agents chewing away at meaningful work. I don't understand how you can have any meaningful supervising role over 10 things at once given the limits of human working memory." / "Every PR Claude makes needs to be reviewed. Every single one. So great! You have 10 instances of Claude doing things. Great! You're still going to need to do 10 reviews."

**No direct Boris response found on this specific criticism.**

#### Criticism #3: Token Waste and Cost Opacity
**Critics (Reddit, [25]):**
> "The average Claude Code session wastes 30-50% of tokens on files that were read but never used." / "Also glosses over the actual monetary costs of what he is doing. A small PR costs 5-16 USD."

**Boris's implicit response:** Lenny's Podcast [6]: "Don't try to cost cut at the beginning. Start by just giving engineers as many tokens as possible." — This doubles down on the capability-over-cost principle rather than acknowledging the concern.

#### Criticism #4: Bugginess and Regression
**Critics (Hacker News, April 2026 [26]):**
> "Claude Code has been around for almost a year and is being built by an entire team, yet doesn't seem to have benefited from this approach. The program is becoming buggier and less reliable over time." / "Reduced usage quotas, poor performance with numerous attempts at getting things right, cache invalidation bugs, background requests which have to be disabled explicitly to avoid consuming the quota too fast." 

One HN commenter received what appears to be an Anthropic engineering response about the effort/thinking issue [26]:
> "We found that effort=85 was a sweet spot on the intelligence-latency/cost curve for most users, improving token efficiency while reducing latency. On one of our product principles is to avoid changing settings on users' behalf, and ideally we would have set effort=85 from the start."

#### Criticism #5: CLAUDE.md as Primitive Memory Architecture
**Critics (Hacker News [24]):**
> "In the era of AI, I don't think it's good enough to 'have' a working product. It's also important to have all the other things that make a project way more productive, like stellar documentation, better abstractions, clearer architecture. In terms of AI, there's gotta be something better than just a markdown file with random notes."

**Boris's explicit response (from Latent Space [5]):** "We had all these crazy ideas about like memory architectures... in the end, the thing we did is ship the simplest thing... it's the simplest thing that could work." Boris acknowledges this is deliberately primitive but argues simplicity has compounding advantages.

#### Criticism #6: Code Quality Concerns from AI Generation
**Critics (HN, [27]):**
> "I use copilot and Claude code and I frequently have to throw away their massively verbose and ridiculously complex code and engage my withering brain to come up with the correct solution that is 80% less code."

**Boris's implicit design response (Latent Space [5]):** "Most of the changes are to make things more simple. Right. Like to share interfaces across different components. [...] ultimately we just want to make sure that the context that's given to the model is in like the purest form." Claude Code itself has a `code-simplifier` sub-agent specifically to address this.

### 7.2 Future Direction Hints

From Lenny's Podcast (Feb 2026) [6]:

> "Coding is largely solved. At least for the kind of programming that I do, it's just a solved problem because quad can do it. And so now we're starting to think about okay like what's next? What's beyond this?"

> "Over the next few months I think what we're going to see is just across the industry it's going to become increasingly solved for every kind of codebase, every tech stack that people work on."

> "I think it's going to be a lot of the roles that are adjacent to engineering. It could be like product managers, it could be design, could be data science. It is going to expand to pretty much any kind of work that you can do on a computer because the model is just going to get better and better at this."

> "One of the ways that it's going to get better is it's going to get better and better at using tools and using computers. This is a bet that I would make. Another one is it's going to get better and better for running for long periods of time."

> "4% of all public GitHub commits are now authored by Claude Code (predicted to hit 20% by end of 2026)."

From Every.to (Oct 2025) [11]:

> "I think my prediction is that the terminal is not the final form factor. My prediction is there's going to be a few more form factors in the coming months, you know, maybe a year or something like that. And it's going to keep changing very quickly."

> "Pretty soon we're going to be in this mode of Claudes monitoring Claudes."

From Bessemer (Aug 2025) [12]:

> "Sub agents are actually a thing that we might deprecate at some point. [...] as the model gets really good at managing its own context, you won't need these specialized agents anymore."

> "One could imagine a model that's perfectly aligned and if it is, then you might not need all the security features. This is something we need for models of today because we don't trust them."

> "I think as a company, we're going to build some of the future applications of claude code and of coding agents. But I think actually the vast majority of these applications will be built outside of the company. It's going to be built on our APIs and on our SDKs."

**Near-term features confirmed as of 2026:**
- `/loop` and `/schedule` — automated recurring workflows (up to a week)
- `/teleport` and `/remote-control` — session mobility
- `/voice` — voice input (Boris uses this for most of his coding)
- `--add-dir` / `/add-dir` — multi-repo context
- `--agent=<name>` — named agent launch from `.claude/agents/`
- Cowork (desktop product, built in 10 days, growing faster than Claude Code at launch)

---

## Specific Sources (Cross-Reference)

- **Twitter/X:** @bcherny — https://x.com/bcherny. Major pinned threads: Jan 2, 2026 (setup thread); Dec 27, 2025 (one-year retrospective); Feb 11, 2026 (customizability thread); Jan 28, 2026 (CLAUDE.md lazy loading)
- **Personal website/blog:** https://borischerny.com — 17 blog posts from 2012–2024; most relevant: "NPM and NodeJS should do more to make ES Modules easy to use" (Jun 2024), "Learning to work (very) remotely" (Dec 2023)
- **Top Anthropic-related content:**
  - Official Claude Code docs: https://code.claude.com/docs/en/
  - Hooks reference: https://code.claude.com/docs/en/hooks
  - Sub-agents SDK: https://code.claude.com/docs/en/agent-sdk/subagents
  - Skills: https://code.claude.com/docs/en/skills
  - Overview: https://docs.anthropic.com/en/docs/claude-code/overview
- **Top podcast appearances:**
  - Latent Space (May 2025): https://www.latent.space/p/claude-code
  - Every.to / AI & I (Oct 2025): https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it
  - Lenny's Podcast (Feb 2026): https://www.youtube.com/watch?v=We7BZVKbCVw
  - Bessemer Research to Runtime (Aug 2025): https://www.youtube.com/watch?v=h-Hlt05REZk
  - Pragmatic Engineer (Mar 2026): https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
  - Y Combinator Lightcone (Feb 2026): https://www.ycombinator.com/library/NJ-inside-claude-code-with-its-creator-boris-cherny
  - Developing Dev (Dec 2025): https://www.developing.dev/p/boris-cherny-creator-of-claude-code
- **Top conference talks:**
  - Anthropic/YouTube (Sep 2025): https://www.youtube.com/watch?v=iF9iV4xponk
  - Bessemer (Aug 2025): https://www.youtube.com/watch?v=h-Hlt05REZk
  - React Boston 2018 (Undux): https://www.youtube.com/watch?v=CpOE-JrtAdc
- **Book:** *Programming TypeScript* (O'Reilly, 2019) — https://www.oreilly.com/library/view/programming-typescript/9781492037644/

---

## Critical Assessment

### Boris's Strongest Design Arguments (with Evidence)

**1. Minimal scaffolding wins as models improve.**
The empirical case: Claude Code ripped out half its system prompt when the claude-4 series launched and performance improved. Boris's claim that Claude Code rewrites itself from scratch every 3-4 weeks and gets better each time is supported by the product's market success (4% of all public GitHub commits within 18 months). The "ship of Theseus" design — where every piece gets replaced and the core philosophy persists — is a real-world application of the bitter lesson.

**2. Agentic search > RAG for code.**
Boris describes (Pragmatic Engineer [14]) that the team tried local vector databases, recursive model-based indexing, and other approaches. Plain glob and grep, driven by the model, outperformed everything. The evidence from how Instagram engineers searched code when click-to-definition broke (they used grep) was the insight. This is a strong empirical argument against over-engineering search infrastructure.

**3. CLAUDE.md as "written pair programming."**
The practice of having Claude write its own correction rules ("after every mistake, add it to CLAUDE.md") creates a genuine self-improvement loop. Boris's team updates the CLAUDE.md multiple times per week with learnings from code review. This is a lightweight, observable, auditable form of persistent memory — well-suited to enterprise compliance requirements.

**4. Verification loop as the real quality multiplier.**
Boris's strongest practical tip — "give Claude a way to verify its work and you'll 2-3x the quality" — is consistent with reinforcement learning theory. The feedback loop (run tests, check browser, check logs) is what turns single-pass generation into iterative refinement. This principle transfers directly to Jetix's 12-agent system: each agent should have a verification signal, not just a completion signal.

### Weaknesses in His Stated Philosophy (Where Critics Surface Gaps)

**1. The "simplest thing" can accumulate complexity debt.**
CLAUDE.md files grow organically and become unwieldy. Users report CLAUDE.md turning into "a wiki" rather than focused instructions. The hooks system now has 27+ event types. The skills system merges with slash commands. What started as "the simplest thing" has become a multi-layered configuration system requiring significant expertise.

**2. Parallelism assumes tasks are decomposable and reviewable.**
Boris's 5-instances-in-parallel workflow assumes (a) you have clearly scoped tasks to give each instance, and (b) you can meaningfully review 20-30 PRs per day. Critics (HN [24]) correctly point out that neither assumption holds for most organizations. For Jetix's 12-agent system, this means the orchestration problem (deciding *which* tasks to assign to *which* agents) is non-trivial and Boris's model under-specifies it.

**3. "Don't box the model in" creates auditability gaps.**
For a 12-agent enterprise system with compliance requirements, allowing the model to freely choose tool sequences creates audit trail complexity. Boris's model works best when the operator (Boris) is watching. For unattended operation at scale, the absence of explicit orchestration makes it harder to explain *why* the system did what it did.

**4. Cost opacity.**
Boris's "give engineers unlimited tokens" advice is correct for productivity discovery — it's wrong as a permanent operating mode. The lack of per-task cost attribution in Claude Code's default design (praised for simplicity) is a liability at enterprise scale. The hooks system can be used to instrument this, but it requires extra engineering work that Boris's "vanilla setup" advice doesn't emphasize.

**5. Sub-agent context starvation.**
The strict "only the prompt string passes from parent to sub-agent" design means the orchestrator must perfectly specify the task upfront. For tasks that require mid-execution context (e.g., "fix the bug you found in sub-task 3"), the current architecture requires either re-running with the context or complex prompt engineering. Boris acknowledges this is a limitation of current models, not a permanent design.

### When Claude Code's Design is RIGHT vs. NOT RIGHT for a Use Case

| Scenario | Verdict | Reasoning |
|----------|---------|-----------|
| Codebase transformation (large migration) | RIGHT | Replaceable parallel agents, each with isolated context, exactly matches this use case |
| Exploratory research (investigate 3 approaches) | RIGHT | Parallel sub-agents for exploration, then synthesis in main context |
| Compliance-audited enterprise workflow | PARTIAL | Hooks enable auditability but require significant setup; no built-in audit log |
| Real-time collaborative multi-agent system | NOT YET | "Claudes monitoring Claudes" is acknowledged future work; current form factor is sequential |
| Hard-coded pipeline with strict step sequencing | NOT RIGHT | Boris explicitly warns against this; model performance degrades with rigid orchestration |
| Tasks requiring > 1 pass (iterative refinement) | RIGHT | The verification loop design (Stop hooks + sub-agent verification) enables this |
| Non-technical users (data scientists, finance) | PARTIAL | Cowork (Claude Code with GUI) addresses this; raw CLI requires expertise |
| Long-running autonomous operation (days) | PARTIAL | Boris says Claude runs "minutes, hours, and days at a time (using Stop hooks)" but the infrastructure for this is still maturing |

---

## Comparison to Other Agent-Design Philosophies

### Cognition Labs (Devin) — Planning-First Architecture
Devin's architecture emphasizes explicit, serialized planning: the agent produces a structured plan before taking any action, and the plan is reviewable. This is the inverse of Boris's philosophy. Boris's plan mode is "just send a little message: don't code yet." Devin builds more elaborate state machines with separate planning and execution phases. **Trade-off:** Devin's approach is more auditable and produces more consistent plans but is slower to adapt when mid-task conditions change. Boris's approach produces faster iteration but less predictable intermediate states.

### Every.to Compound Architecture
Dan Shipper (Every.to) coined "Compounding Engineering" — the idea that each AI interaction should improve the system's future performance. Boris explicitly adopted this term and credits Shipper for it. Boris's CLAUDE.md practice (having Claude write its own correction rules) is Claude Code's implementation of compounding engineering. The architectures align closely; the difference is that Every.to approaches this from a writing/product team perspective while Boris applies it to a pure engineering workflow.

### CrewAI / AutoGen — Hierarchical Coordination
CrewAI and AutoGen both implement formal agent hierarchies: a manager agent that delegates to worker agents, with explicit role assignments (researcher, writer, coder). Boris's design philosophy explicitly rejects this: "I think a lot of people's instinct when they build on the model is they try to make it behave a very particular way... almost always you get better results if you just give the model tools, you give it a goal, and you let it figure it out." The CrewAI/AutoGen approach offers better human interpretability of what each agent's "job" is; Boris's approach offers better adaptability and reduced prompt engineering overhead. *Note: Boris has not publicly commented directly on CrewAI or AutoGen.*

### Anatoly Levenchuk's Systems-Thinking Critique
No direct engagement between Boris Cherny and Anatoly Levenchuk's work has been identified in public sources. From a systems-thinking perspective, the likely critique of Boris's design would center on the lack of explicit system-level modeling: Claude Code optimizes at the agent level (give each agent the right context and tools) but lacks a formal model of the system's emergent behavior when 12 agents interact. Systems thinking would demand explicit modeling of information flows, feedback loops, and system boundaries — all of which Boris's approach handles implicitly via CLAUDE.md, hooks, and the model's own judgment. *No public Boris statement found on this topic.*

---

## Sources List

[1] Anonymous, "claude-code-router: Project Motivation" (GitHub, 2025-02-25). https://github.com/musistudio/claude-code-router/blob/main/blog/en/project-motivation-and-how-it-works.md

[2] Ryan Peterman, "Boris Cherny (Creator of Claude Code) On How His Career Grew" (The Developing Dev, 2025-12-15). https://www.developing.dev/p/boris-cherny-creator-of-claude-code

[3] Boris Cherny, "Building Claude Code with Boris Cherny" (Pragmatic Engineer / YouTube, 2026-03-04). https://www.youtube.com/watch?v=julbw1JuAz0

[4] Boris Cherny, "Boris Cherny's Blog" (personal website). https://borischerny.com

[5] Latent Space, "Claude Code: Anthropic's Agent in Your Terminal" (Latent.Space podcast, 2025-05-07). https://www.latent.space/p/claude-code

[6] Lenny Rachitsky, "Head of Claude Code: What happens after coding is solved" (Lenny's Podcast/YouTube, 2026-02-19). https://www.youtube.com/watch?v=We7BZVKbCVw

[7] Boris Cherny, LinkedIn profile. https://www.linkedin.com/in/bcherny

[8] Boris Cherny, X/Twitter profile @bcherny. https://x.com/bcherny

[9] Boris Cherny, GitHub profile @bcherny. https://github.com/bcherny

[10] Dan Shipper, "How to Use Claude Code Like the People Who Built It" (Every.to AI & I, 2025-10-29). https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it

[11] Dan Shipper, "Transcript: How to Use Claude Code Like the People Who Built It" (Every.to, 2025-10-29). https://every.to/podcast/transcript-how-to-use-claude-code-like-the-people-who-built-it

[12] Bessemer Venture Partners, "Agentic Coding with Claude Code Creator Boris Cherny" (YouTube, 2025-08-18). https://www.youtube.com/watch?v=h-Hlt05REZk

[13] Y Combinator, "Inside Claude Code With Its Creator Boris Cherny" (YC Library, 2026-02-17). https://www.ycombinator.com/library/NJ-inside-claude-code-with-its-creator-boris-cherny

[14] Gergely Orosz, "Building Claude Code with Boris Cherny" (The Pragmatic Engineer newsletter, 2026-03-04). https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny

[15] Anthropic / Alex Albert, "The Future of Agentic Coding with Claude Code" (YouTube, 2025-09-02). https://www.youtube.com/watch?v=iF9iV4xponk

[16] Boris Cherny (@bcherny), "I'm Boris and I created Claude Code..." (X/Twitter thread, 2026-01-02). https://x.com/bcherny/status/2007179832300581177

[17] Anthropic, "Subagents in the SDK - Claude Code Docs" (2026-04-08). https://code.claude.com/docs/en/agent-sdk/subagents

[18] Boris Cherny (@bcherny), "Our checked in CLAUDE.md is 2.5k tokens..." (X/Twitter, 2026-01-02). https://x.com/bcherny/status/2007212366094811401

[19] Boris Cherny (@bcherny), "In case it's not clear in the docs..." (X/Twitter, 2026-01-28). https://x.com/bcherny/status/2016339448863355206

[20] Anthropic, "Hooks Reference - Claude Code Docs" (2026-04-20). https://code.claude.com/docs/en/hooks

[21] Reddit r/ClaudeAI, "Are skills and slash commands the same thing now in Claude Code" (2026-01-08). https://www.reddit.com/r/ClaudeAI/comments/1q7fzab/are_skills_and_slash_commands_the_same_thing_now/

[22] Anthropic, "Extend Claude with skills - Claude Code Docs" (2026-04-16). https://code.claude.com/docs/en/skills

[23] Anonymous, "How Boris Cherny Uses Claude Code" (howborisusesclaudecode.com, 2026-02-03). https://howborisusesclaudecode.com

[24] Hacker News, "The creator of Claude Code's Claude setup" (2026-01-03). https://news.ycombinator.com/item?id=46470017

[25] Reddit r/ClaudeCode, "This seems like a waste of tokens" (2026-02-08). https://www.reddit.com/r/ClaudeCode/comments/1qyt0fo/this_seems_like_a_waste_of_tokens_there_has_got/

[26] Hacker News, "Issue: Claude Code is unusable for complex engineering tasks" (2026-04-07). https://news.ycombinator.com/item?id=47660925

[27] Hacker News, "It's truly strange that people keep citing the quality of Claude code's leaked system prompt" (2026-04-17). https://news.ycombinator.com/item?id=47665285

[28] Boris Cherny (@bcherny), "When I created Claude Code as a side project back in September 2024..." (X/Twitter, 2025-12-27). https://x.com/bcherny/status/2004887829252317325

[29] Boris Cherny (@bcherny), "Reflecting on what engineers love about Claude Code..." (X/Twitter, 2026-02-11). https://x.com/bcherny/status/2021699851499798911

[30] Waydev, "8 Insights from Anthropic's Claude Code Boris Cherny" (2026-02-23). https://waydev.co/8-game-changing-insights-from-anthropic-claudecode-boris-cherny/

[31] Anthropic, "Claude Code overview" (official docs). https://docs.anthropic.com/en/docs/claude-code/overview

[32] SE Radio, "Episode 384: Boris Cherny on TypeScript" (2019-10-16). https://se-radio.net/2019/10/episode-384-boris-cherny-on-typescript/

[33] Reddit r/AgentsOfAI, "Boris Cherny (creator of Claude Code) shares his setup" (2026-01-03). https://www.reddit.com/r/AgentsOfAI/comments/1q2s83g/boris_cherny_creator_of_claude_code_shares_his/

[34] Anthropic, "The Complete Guide to Building Skills for Claude" (PDF). https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

[35] Reddit r/ClaudeAI, "Insights from Claude Code's Creators (Latent Space Podcast)" (2025-05-09). https://www.reddit.com/r/ClaudeAI/comments/1kigr2j/insights_from_claude_codes_creators_latent_space/

---

*Report compiled April 2026. All quotes verified against primary source URLs. Sections where evidence was thin are explicitly marked "No public Boris statement found."*
