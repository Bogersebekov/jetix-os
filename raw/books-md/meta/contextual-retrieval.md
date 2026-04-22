---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: contextual-retrieval
subcategory: meta
tags:
- meta
title: Contextual Retrieval
word_count: 2630
---

<div id="main-content" role="main">

<div class="section page-wrapper HeroEngineering-module-scss-module__j1ivRa__hero"
aria-label="Engineering Article Hero">

<a href="../engineering.html"
class="body-2 bold HeroEngineering-module-scss-module__j1ivRa__hubLink">Engineering
at Anthropic</a>

<div class="HeroEngineering-module-scss-module__j1ivRa__content">

<div class="HeroEngineering-module-scss-module__j1ivRa__header">

<div class="HeroEngineering-module-scss-module__j1ivRa__heroImage">

<img
src="https://www-cdn.anthropic.com/images/4zrzovbb/website/7e2e39544a35760367049072406377a54f2b58c0-2554x2554.svg"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
width="2554" height="2554" />

</div>

# Introducing Contextual Retrieval

</div>

<div class="HeroEngineering-module-scss-module__j1ivRa__metadata">

Published Sep 19, 2024

For an AI model to be useful in specific contexts, it often needs access
to background knowledge.

</div>

</div>

</div>

<div class="page-wrapper">

<div>

<div class="Body-module-scss-module__z40yvW__body" theme="ivory">

For an AI model to be useful in specific contexts, it often needs access
to background knowledge. For example, customer support chatbots need
knowledge about the specific business they're being used for, and legal
analyst bots need to know about a vast array of past cases.

Developers typically enhance an AI model's knowledge using
Retrieval-Augmented Generation (RAG). RAG is a method that retrieves
relevant information from a knowledge base and appends it to the user's
prompt, significantly enhancing the model's response. The problem is
that traditional RAG solutions remove context when encoding information,
which often results in the system failing to retrieve the relevant
information from the knowledge base.

In this post, we outline a method that dramatically improves the
retrieval step in RAG. The method is called “Contextual Retrieval” and
uses two sub-techniques: Contextual Embeddings and Contextual BM25. This
method can reduce the number of failed retrievals by 49% and, when
combined with reranking, by 67%. These represent significant
improvements in retrieval accuracy, which directly translates to better
performance in downstream tasks.

You can easily deploy your own Contextual Retrieval solution with Claude
with <a
href="https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide"
target="_blank" rel="noopener noreferrer">our cookbook</a>.

### A note on simply using a longer prompt

Sometimes the simplest solution is the best. If your knowledge base is
smaller than 200,000 tokens (about 500 pages of material), you can just
include the entire knowledge base in the prompt that you give the model,
with no need for RAG or similar methods.

A few weeks ago, we released [prompt
caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
for Claude, which makes this approach significantly faster and more
cost-effective. Developers can now cache frequently used prompts between
API calls, reducing latency by \> 2x and costs by up to 90% (you can see
how it works by reading our
<a href="https://platform.claude.com/cookbook/misc-prompt-caching"
target="_blank" rel="noopener noreferrer">prompt caching cookbook</a>).

However, as your knowledge base grows, you'll need a more scalable
solution. That’s where Contextual Retrieval comes in.

## A primer on RAG: scaling to larger knowledge bases

For larger knowledge bases that don't fit within the context window, RAG
is the typical solution. RAG works by preprocessing a knowledge base
using the following steps:

1.  Break down the knowledge base (the “corpus” of documents) into
    smaller chunks of text, usually no more than a few hundred tokens;
2.  Use an embedding model to convert these chunks into vector
    embeddings that encode meaning;
3.  Store these embeddings in a vector database that allows for
    searching by semantic similarity.

At runtime, when a user inputs a query to the model, the vector database
is used to find the most relevant chunks based on semantic similarity to
the query. Then, the most relevant chunks are added to the prompt sent
to the generative model.

While embedding models excel at capturing semantic relationships, they
can miss crucial exact matches. Fortunately, there’s an older technique
that can assist in these situations. BM25 (Best Matching 25) is a
ranking function that uses lexical matching to find precise word or
phrase matches. It's particularly effective for queries that include
unique identifiers or technical terms.

BM25 works by building upon the TF-IDF (Term Frequency-Inverse Document
Frequency) concept. TF-IDF measures how important a word is to a
document in a collection. BM25 refines this by considering document
length and applying a saturation function to term frequency, which helps
prevent common words from dominating the results.

Here’s how BM25 can succeed where semantic embeddings fail: Suppose a
user queries "Error code TS-999" in a technical support database. An
embedding model might find content about error codes in general, but
could miss the exact "TS-999" match. BM25 looks for this specific text
string to identify the relevant documentation.

RAG solutions can more accurately retrieve the most applicable chunks by
combining the embeddings and BM25 techniques using the following steps:

1.  Break down the knowledge base (the "corpus" of documents) into
    smaller chunks of text, usually no more than a few hundred tokens;
2.  Create TF-IDF encodings and semantic embeddings for these chunks;
3.  Use BM25 to find top chunks based on exact matches;
4.  Use embeddings to find top chunks based on semantic similarity;
5.  Combine and deduplicate results from (3) and (4) using rank fusion
    techniques;
6.  Add the top-K chunks to the prompt to generate the response.

By leveraging both BM25 and embedding models, traditional RAG systems
can provide more comprehensive and accurate results, balancing precise
term matching with broader semantic understanding.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F45603646e979c62349ce27744a940abf30200d57-3840x2160.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F45603646e979c62349ce27744a940abf30200d57-3840x2160.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="3840" height="2160" />
<figcaption>A Standard Retrieval-Augmented Generation (RAG) system that
uses both embeddings and Best Match 25 (BM25) to retrieve information.
TF-IDF (term frequency-inverse document frequency) measures word
importance and forms the basis for BM25.</figcaption>
</figure>

</div>

This approach allows you to cost-effectively scale to enormous knowledge
bases, far beyond what could fit in a single prompt. But these
traditional RAG systems have a significant limitation: they often
destroy context.

### The context conundrum in traditional RAG

In traditional RAG, documents are typically split into smaller chunks
for efficient retrieval. While this approach works well for many
applications, it can lead to problems when individual chunks lack
sufficient context.

For example, imagine you had a collection of financial information (say,
U.S. SEC filings) embedded in your knowledge base, and you received the
following question: *"What was the revenue growth for ACME Corp in Q2
2023?"*

A relevant chunk might contain the text: *"The company's revenue grew by
3% over the previous quarter."* However, this chunk on its own doesn't
specify which company it's referring to or the relevant time period,
making it difficult to retrieve the right information or use the
information effectively.

## Introducing Contextual Retrieval

Contextual Retrieval solves this problem by prepending chunk-specific
explanatory context to each chunk before embedding (“Contextual
Embeddings”) and creating the BM25 index (“Contextual BM25”).

Let’s return to our SEC filings collection example. Here's an example of
how a chunk might be transformed:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
original_chunk = "The company's revenue grew by 3% over the previous quarter."

contextualized_chunk = "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

It is worth noting that other approaches to using context to improve
retrieval have been proposed in the past. Other proposals include:
[adding generic document summaries to
chunks](https://aclanthology.org/W02-0405.pdf) (we experimented and saw
very limited gains), [hypothetical document
embedding](https://arxiv.org/abs/2212.10496), and [summary-based
indexing](https://www.llamaindex.ai/blog/a-new-document-summary-index-for-llm-powered-qa-systems-9a32ece2f9ec)
(we evaluated and saw low performance). These methods differ from what
is proposed in this post.

### Implementing Contextual Retrieval

Of course, it would be far too much work to manually annotate the
thousands or even millions of chunks in a knowledge base. To implement
Contextual Retrieval, we turn to Claude. We’ve written a prompt that
instructs the model to provide concise, chunk-specific context that
explains the chunk using the context of the overall document. We used
the following Claude 3 Haiku prompt to generate context for each chunk:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<div class="CodeBlock-module-scss-module__PbWBnq__codeBlock">

```
<document> 
{{WHOLE_DOCUMENT}} 
</document> 
Here is the chunk we want to situate within the whole document 
<chunk> 
{{CHUNK_CONTENT}} 
</chunk> 
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else. 
```

<div class="CodeBlock-module-scss-module__PbWBnq__controls">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjExIiBoZWlnaHQ9IjE1IiB2aWV3Ym94PSIwIDAgMTEgMTUiPjxwYXRoIGQ9Ik01LjQgMEM2LjM5ODc1IDAgNy4yNjgxOSAwLjU0MzgxNCA3LjczNTI1IDEuMzVIOS40NUMxMC4xOTU2IDEuMzUgMTAuOCAxLjk1NDQyIDEwLjggMi43VjEzLjVDMTAuOCAxNC4yNDU2IDEwLjE5NTYgMTQuODUgOS40NSAxNC44NUgxLjM1QzAuNjA0NDE1IDE0Ljg1IDIuMTc0MzZlLTA4IDE0LjI0NTYgMCAxMy41VjIuN0MxLjczOTVlLTA3IDEuOTU0NDIgMC42MDQ0MTUgMS4zNSAxLjM1IDEuMzVIMy4wNjQ3NUMzLjUzMTgxIDAuNTQzODE0IDQuNDAxMjUgMCA1LjQgMFpNMS4zNSAyLjI1QzEuMTAxNDcgMi4yNSAwLjkgMi40NTE0NyAwLjkgMi43VjEzLjVDMC45IDEzLjc0ODUgMS4xMDE0NyAxMy45NSAxLjM1IDEzLjk1SDkuNDVDOS42OTg1MyAxMy45NSA5LjkgMTMuNzQ4NSA5LjkgMTMuNVYyLjdDOS45IDIuNDUxNDcgOS42OTg1MyAyLjI1IDkuNDUgMi4yNUg4LjA2MjIxQzguMDg2NzcgMi4zOTYzNyA4LjEgMi41NDY2NSA4LjEgMi43VjMuNkM4LjEgMy44NDg1MyA3Ljg5ODUzIDQuMDUgNy42NSA0LjA1SDMuMTVDMi45MDE0NyA0LjA1IDIuNyAzLjg0ODUzIDIuNyAzLjZWMi43QzIuNyAyLjU0NjY1IDIuNzEzMjMgMi4zOTYzNyAyLjczNzc5IDIuMjVIMS4zNVpNNy42ODYwMyAxMC42MjMzQzcuNzgzNzYgMTAuMzk1IDguMDQ4MjggMTAuMjg4NiA4LjI3NjY2IDEwLjM4NkM4LjUwNDk5IDEwLjQ4MzggOC42MTE0MyAxMC43NDgzIDguNTEzOTYgMTAuOTc2N0M4LjI0ODU2IDExLjU5NjcgNy43MzAxNCAxMi4xNSA3LjAxOTgyIDEyLjE1QzYuNTgxOTIgMTIuMTQ5OSA2LjIxNzIyIDExLjkzOTcgNS45Mzk2NSAxMS42MzMyQzUuNjYyMTUgMTEuOTM5NSA1LjI5ODAxIDEyLjE0OTkgNC44NjAzNSAxMi4xNUM0LjQyMjI5IDEyLjE1IDQuMDU2OTIgMTEuOTM5OCAzLjc3OTMgMTEuNjMzMkMzLjUwMTc1IDExLjkzOTUgMy4xMzc3MyAxMi4xNSAyLjcgMTIuMTVDMi40NTE0NyAxMi4xNSAyLjI1IDExLjk0ODUgMi4yNSAxMS43QzIuMjUgMTEuNDUxNSAyLjQ1MTQ3IDExLjI1IDIuNyAxMS4yNUMyLjg5MTIgMTEuMjUgMy4xNjcyNiAxMS4wODc5IDMuMzY2MjEgMTAuNjIzM0wzLjM5Njk3IDEwLjU2MzZDMy40NzgwNiAxMC40MzIxIDMuNjIyNjEgMTAuMzUgMy43ODAxOCAxMC4zNUMzLjk2MDIgMTAuMzUwMSA0LjEyMzMgMTAuNDU3OCA0LjE5NDE0IDEwLjYyMzNDNC4zOTMwOSAxMS4wODc4IDQuNjY5MTcgMTEuMjUgNC44NjAzNSAxMS4yNUM1LjA1MTU2IDExLjI0OTggNS4zMjc3MyAxMS4wODc3IDUuNTI2NTYgMTAuNjIzM0w1LjU1NzMyIDEwLjU2MzZDNS42MzgzNyAxMC40MzIzIDUuNzgyMjkgMTAuMzUwMSA1LjkzOTY1IDEwLjM1QzYuMTE5NzQgMTAuMzUgNi4yODI3NSAxMC40NTc4IDYuMzUzNjEgMTAuNjIzM0M2LjU1MjUxIDExLjA4NzggNi44Mjg2MiAxMS4yNDk5IDcuMDE5ODIgMTEuMjVDNy4yMTEwMiAxMS4yNSA3LjQ4NzA4IDExLjA4NzkgNy42ODYwMyAxMC42MjMzWk03LjY4NjAzIDcuMDIzMzRDNy43ODM3NiA2Ljc5NTAxIDguMDQ4MjggNi42ODg1NyA4LjI3NjY2IDYuNzg2MDRDOC41MDQ5OSA2Ljg4Mzc2IDguNjExNDMgNy4xNDgyOCA4LjUxMzk2IDcuMzc2NjZDOC4yNDg1NiA3Ljk5Njc1IDcuNzMwMTQgOC41NSA3LjAxOTgyIDguNTVDNi41ODE5MiA4LjU0OTk0IDYuMjE3MjIgOC4zMzk3IDUuOTM5NjUgOC4wMzMyQzUuNjYyMTUgOC4zMzk0NyA1LjI5ODAxIDguNTQ5ODkgNC44NjAzNSA4LjU1QzQuNDIyMjkgOC41NSA0LjA1NjkyIDguMzM5ODMgMy43NzkzIDguMDMzMkMzLjUwMTc1IDguMzM5NDUgMy4xMzc3MyA4LjU1IDIuNyA4LjU1QzIuNDUxNDcgOC41NSAyLjI1IDguMzQ4NTMgMi4yNSA4LjFDMi4yNSA3Ljg1MTQ3IDIuNDUxNDcgNy42NSAyLjcgNy42NUMyLjg5MTIgNy42NSAzLjE2NzI2IDcuNDg3OTEgMy4zNjYyMSA3LjAyMzM0TDMuMzk2OTcgNi45NjM1N0MzLjQ3ODA2IDYuODMyMTMgMy42MjI2MSA2Ljc1IDMuNzgwMTggNi43NUMzLjk2MDIgNi43NTAwNyA0LjEyMzMgNi44NTc4MyA0LjE5NDE0IDcuMDIzMzRDNC4zOTMwOSA3LjQ4NzgyIDQuNjY5MTcgNy42NSA0Ljg2MDM1IDcuNjVDNS4wNTE1NiA3LjY0OTggNS4zMjc3MyA3LjQ4NzcyIDUuNTI2NTYgNy4wMjMzNEw1LjU1NzMyIDYuOTYzNTdDNS42MzgzNyA2LjgzMjMyIDUuNzgyMjkgNi43NTAxMiA1LjkzOTY1IDYuNzVDNi4xMTk3NCA2Ljc1IDYuMjgyNzUgNi44NTc3OCA2LjM1MzYxIDcuMDIzMzRDNi41NTI1MSA3LjQ4NzgyIDYuODI4NjIgNy42NDk5IDcuMDE5ODIgNy42NUM3LjIxMTAyIDcuNjUgNy40ODcwOCA3LjQ4Nzg2IDcuNjg2MDMgNy4wMjMzNFpNNS40IDAuOUM0LjQwNTg5IDAuOSAzLjYgMS43MDU4OSAzLjYgMi43VjMuMTVINy4yVjIuN0M3LjIgMS43MDU4OSA2LjM5NDExIDAuOSA1LjQgMC45WiIgZmlsbD0iY3VycmVudENvbG9yIiAvPjwvc3ZnPg=="
class="Icon-module-scss-module__lqbdHG__icon" /><span class="body-3">Copy</span>

</div>

</div>

</div>

The resulting contextual text, usually 50-100 tokens, is prepended to
the chunk before embedding it and before creating the BM25 index.

Here’s what the preprocessing flow looks like in practice:

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2496e7c6fedd7ffaa043895c23a4089638b0c21b-3840x2160.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2496e7c6fedd7ffaa043895c23a4089638b0c21b-3840x2160.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="3840" height="2160" />
<figcaption><em>Contextual Retrieval is a preprocessing technique that
improves retrieval accuracy.</em><br />
</figcaption>
</figure>

</div>

If you’re interested in using Contextual Retrieval, you can get started
with <a
href="https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide"
target="_blank" rel="noopener noreferrer">our cookbook</a>.

### Using Prompt Caching to reduce the costs of Contextual Retrieval

Contextual Retrieval is uniquely possible at low cost with Claude,
thanks to the special prompt caching feature we mentioned above. With
prompt caching, you don’t need to pass in the reference document for
every chunk. You simply load the document into the cache once and then
reference the previously cached content. Assuming 800 token chunks, 8k
token documents, 50 token context instructions, and 100 tokens of
context per chunk, **the one-time cost to generate contextualized chunks
is \$1.02 per million document tokens**.

#### Methodology

We experimented across various knowledge domains (codebases, fiction,
ArXiv papers, Science Papers), embedding models, retrieval strategies,
and evaluation metrics. We’ve included a few examples of the questions
and answers we used for each domain in [Appendix
II](https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf).

The graphs below show the average performance across all knowledge
domains with the top-performing embedding configuration (Gemini Text
004) and retrieving the top-20-chunks. We use 1 minus recall@20 as our
evaluation metric, which measures the percentage of relevant documents
that fail to be retrieved within the top 20 chunks. You can see the full
results in the appendix - contextualizing improves performance in every
embedding-source combination we evaluated.

#### Performance improvements

Our experiments showed that:

- **Contextual Embeddings reduced the top-20-chunk retrieval failure
  rate by 35%** (5.7% → 3.7%).
- **Combining Contextual Embeddings and Contextual BM25 reduced the
  top-20-chunk retrieval failure rate by 49%** (5.7% → 2.9%).

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7f8d739e491fe6b3ba0e6a9c74e4083d760b88c9-3840x2160.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7f8d739e491fe6b3ba0e6a9c74e4083d760b88c9-3840x2160.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="3840" height="2160" />
<figcaption><em>Combining Contextual Embedding and Contextual BM25
reduce the top-20-chunk retrieval failure rate by 49%.</em></figcaption>
</figure>

</div>

#### Implementation considerations

When implementing Contextual Retrieval, there are a few considerations
to keep in mind:

1.  **Chunk boundaries:** Consider how you split your documents into
    chunks. The choice of chunk size, chunk boundary, and chunk overlap
    can affect retrieval performance<sup>1</sup>.
2.  **Embedding model:** Whereas Contextual Retrieval improves
    performance across all embedding models we tested, some models may
    benefit more than others. We found
    [Gemini](https://ai.google.dev/gemini-api/docs/embeddings) and
    [Voyage](https://www.voyageai.com/) embeddings to be particularly
    effective.
3.  **Custom contextualizer prompts:** While the generic prompt we
    provided works well, you may be able to achieve even better results
    with prompts tailored to your specific domain or use case (for
    example, including a glossary of key terms that might only be
    defined in other documents in the knowledge base).
4.  **Number of chunks:** Adding more chunks into the context window
    increases the chances that you include the relevant information.
    However, more information can be distracting for models so there's a
    limit to this. We tried delivering 5, 10, and 20 chunks, and found
    using 20 to be the most performant of these options (see appendix
    for comparisons) but it’s worth experimenting on your use case.

**Always run evals:** Response generation may be improved by passing it
the contextualized chunk and distinguishing between what is context and
what is the chunk.

## Further boosting performance with Reranking

In a final step, we can combine Contextual Retrieval with another
technique to give even more performance improvements. In traditional
RAG, the AI system searches its knowledge base to find the potentially
relevant information chunks. With large knowledge bases, this initial
retrieval often returns a lot of chunks—sometimes hundreds—of varying
relevance and importance.

Reranking is a commonly used filtering technique to ensure that only the
most relevant chunks are passed to the model. Reranking provides better
responses and reduces cost and latency because the model is processing
less information. The key steps are:

1.  Perform initial retrieval to get the top potentially relevant chunks
    (we used the top 150);
2.  Pass the top-N chunks, along with the user's query, through the
    reranking model;
3.  Using a reranking model, give each chunk a score based on its
    relevance and importance to the prompt, then select the top-K chunks
    (we used the top 20);
4.  Pass the top-K chunks into the model as context to generate the
    final result.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8f82c6175a64442ceff4334b54fac2ab3436a1d1-3840x2160.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8f82c6175a64442ceff4334b54fac2ab3436a1d1-3840x2160.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="3840" height="2160" />
<figcaption><em>Combine Contextual Retrieva and Reranking to maximize
retrieval accuracy.</em></figcaption>
</figure>

</div>

### Performance improvements

There are several reranking models on the market. We ran our tests with
the [Cohere reranker](https://cohere.com/rerank). Voyage [also offers a
reranker](https://docs.voyageai.com/docs/reranker), though we did not
have time to test it. Our experiments showed that, across various
domains, adding a reranking step further optimizes retrieval.

Specifically, we found that Reranked Contextual Embedding and Contextual
BM25 reduced the top-20-chunk retrieval failure rate by 67% (5.7% →
1.9%).

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F93a70cfbb7cca35bb8d86ea0a23bdeeb699e8e58-3840x2160.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F93a70cfbb7cca35bb8d86ea0a23bdeeb699e8e58-3840x2160.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="3840" height="2160" />
<figcaption><em>Reranked Contextual Embedding and Contextual BM25
reduces the top-20-chunk retrieval failure rate by
67%.</em></figcaption>
</figure>

</div>

#### Cost and latency considerations

One important consideration with reranking is the impact on latency and
cost, especially when reranking a large number of chunks. Because
reranking adds an extra step at runtime, it inevitably adds a small
amount of latency, even though the reranker scores all the chunks in
parallel. There is an inherent trade-off between reranking more chunks
for better performance vs. reranking fewer for lower latency and cost.
We recommend experimenting with different settings on your specific use
case to find the right balance.

## Conclusion

We ran a large number of tests, comparing different combinations of all
the techniques described above (embedding model, use of BM25, use of
contextual retrieval, use of a reranker, and total \# of top-K results
retrieved), all across a variety of different dataset types. Here’s a
summary of what we found:

1.  Embeddings+BM25 is better than embeddings on their own;
2.  Voyage and Gemini have the best embeddings of the ones we tested;
3.  Passing the top-20 chunks to the model is more effective than just
    the top-10 or top-5;
4.  Adding context to chunks improves retrieval accuracy a lot;
5.  Reranking is better than no reranking;
6.  **All these benefits stack**: to maximize performance improvements,
    we can combine contextual embeddings (from Voyage or Gemini) with
    contextual BM25, plus a reranking step, and adding the 20 chunks to
    the prompt.

We encourage all developers working with knowledge bases to use <a
href="https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide"
target="_blank" rel="noopener noreferrer">our cookbook</a> to experiment
with these approaches to unlock new levels of performance.

## Appendix I

Below is a breakdown of results across datasets, embedding providers,
use of BM25 in addition to embeddings, use of contextual retrieval, and
use of reranking for Retrievals @ 20.

See [Appendix
II](https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf)
for the breakdowns for Retrievals @ 10 and @ 5 as well as example
questions and answers for each dataset.

<div class="Body-module-scss-module__z40yvW__media-column Body-module-scss-module__z40yvW__inline">

<figure
class="ImageWithCaption-module-scss-module__Duq99q__e-imageWithCaption">
<img
src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F646a894ec4e6120cade9951a362f685cd2ec89b2-2458x2983.png&amp;w=3840&amp;q=75"
style="color:transparent" loading="lazy" decoding="async" data-nimg="1"
srcset="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F646a894ec4e6120cade9951a362f685cd2ec89b2-2458x2983.png&amp;w=3840&amp;q=75amp;q=75 1x"
width="2458" height="2983" />
<figcaption><em>1 minus recall @ 20 results across data sets and
embedding providers.</em></figcaption>
</figure>

</div>

## Acknowledgements

Research and writing by Daniel Ford. Thanks to Orowa Sikder, Gautam
Mittal, and Kenneth Lien for critical feedback, Samuel Flamini for
implementing the cookbooks, Lauren Polansky for project coordination and
Alex Albert, Susan Payne, Stuart Ritchie, and Brad Abrams for shaping
this blog post.

</div>

</div>

<div class="NewsletterSubscribe-module-scss-module__MOPAja__wrapper">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__content">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__text-content">

## Get the developer newsletter

<div class="NewsletterSubscribe-module-scss-module__MOPAja__body">

Product updates, how-tos, community spotlights, and more. Delivered
monthly to your inbox.

</div>

</div>

<div class="NewsletterSubscribe-module-scss-module__MOPAja__form-container">

<div class="NewsletterSubscribe-module-scss-module__MOPAja__input-wrapper">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iSWNvbi1tb2R1bGUtc2Nzcy1tb2R1bGVfX2xxYmRIR19faWNvbiIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB2aWV3Ym94PSIwIDAgMjEgMjEiPjxwYXRoIGQ9Ik00LjE0NTg1IDkuODc0OTJMMTQuNDU4NCA5Ljg3NDkyTDkuNjA0MTkgNS4wNDE1OEwxMC41IDQuMTQ1NzVMMTYuODU0MiAxMC40OTk5TDEwLjUgMTYuODU0MUw5LjYwNDE5IDE1Ljk1ODNMMTQuNDU4NCAxMS4xMjQ5TDQuMTQ1ODUgMTEuMTI0OUw0LjE0NTg1IDkuODc0OTJaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+"
class="Icon-module-scss-module__lqbdHG__icon" />

</div>

Please provide your email address if you'd like to receive our monthly
developer newsletter. You can unsubscribe at any time.

</div>

</div>

</div>

</div>

</div>