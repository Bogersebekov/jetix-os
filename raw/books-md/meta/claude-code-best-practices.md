---
acquired_date: '2026-04-22'
converted_date: '2026-04-22'
converted_via: docling
expert: meta-expert
priority: P2
quality_grade: A
slug: claude-code-best-practices
subcategory: meta
tags:
- meta
title: Claude Code Best Practices
word_count: 13239
---

<div hidden="">

</div>

<div class="relative antialiased text-gray-500 dark:text-gray-400">

<a href="claude-code-best-practices.html#content-area"
class="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:z-50 focus:p-2 focus:text-sm focus:bg-background-light dark:focus:bg-background-dark focus:rounded-md focus:outline-primary dark:focus:outline-primary-light">Skip
to main content</a>

<div class="max-lg:contents lg:flex lg:w-full" docs-theme="mint">

<div class="max-lg:contents lg:flex-1 lg:min-w-0 lg:overflow-x-clip">

<div id="navbar"
class="z-30 fixed lg:sticky top-0 w-full peer is-not-custom peer is-not-center peer is-not-wide peer is-not-frame">

<div id="navbar-transition"
class="absolute w-full h-full backdrop-blur flex-none transition-colors duration-500 border-b border-gray-500/5 dark:border-gray-300/[0.06] data-[is-opaque=true]:bg-background-light data-[is-opaque=true]:supports-backdrop-blur:bg-background-light/95 data-[is-opaque=true]:dark:bg-background-dark/75 data-[is-opaque=false]:supports-backdrop-blur:bg-background-light/60 data-[is-opaque=false]:dark:bg-transparent"
is-opaque="false">

</div>

<div class="max-w-8xl mx-auto relative">

<div>

<div class="relative">

<div class="flex items-center lg:px-12 h-16 min-w-0 mx-4 lg:mx-0">

<div class="h-full relative flex-1 flex items-center gap-x-4 min-w-0 border-b border-gray-500/5 dark:border-gray-300/[0.06]">

<div class="flex-1 flex items-center gap-x-4">

<a href="https://code.claude.com/docs/en/overview" class="select-none"
data-state="closed" data-slot="context-menu-trigger"
style="-webkit-touch-callout:none"><span class="sr-only">Claude Code
Docs home page</span><img
src="https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&amp;auto=format&amp;n=c5r9_6tjPMzFdDDT&amp;q=85&amp;s=78fd01ff4f4340295a4f66e2ea54903c"
class="nav-logo w-auto h-7 relative object-contain shrink-0 block dark:hidden"
alt="light logo" /><img
src="https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&amp;auto=format&amp;n=c5r9_6tjPMzFdDDT&amp;q=85&amp;s=1298a0c3b3a1da603b190d0de0e31712"
class="nav-logo w-auto h-7 relative object-contain shrink-0 hidden dark:block"
alt="dark logo" /></a>

<div class="hidden lg:flex items-center gap-x-2">

<div class="relative size-4 rounded-full shrink-0">

<img src="https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg"
class="w-full h-full rounded-full" alt="US" />

<div class="absolute top-0 left-0 w-full h-full border rounded-full bg-primary-light/10 border-black/10">

</div>

</div>

<span class="truncate max-w-[12.5rem]">English</span><img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0idHJhbnNpdGlvbi10cmFuc2Zvcm0gdGV4dC1ncmF5LTQwMCBvdmVyZmxvdy12aXNpYmxlIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAgZGFyazp0ZXh0LWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTQwMCByb3RhdGUtOTAgZ3JvdXAtYXJpYS1bZXhwYW5kZWQ9dHJ1ZV0vdHJpZ2dlcjpyb3RhdGUtWzI3MGRlZ10gbWwtYXV0byI+PHBhdGggZD0iTTAgMEwzIDNMMCA2IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz48L3N2Zz4="
class="transition-transform text-gray-400 overflow-visible group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 rotate-90 group-aria-[expanded=true]/trigger:rotate-[270deg] ml-auto" />

</div>

</div>

<div class="relative hidden lg:flex items-center flex-1 z-20 gap-2.5">

<div class="flex items-center gap-2">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXNlYXJjaCBtaW4tdy00IGZsZXgtbm9uZSB0ZXh0LWdyYXktNzAwIGdyb3VwLWhvdmVyL3NlYXJjaDp0ZXh0LWdyYXktODAwIGRhcms6dGV4dC1ncmF5LTQwMCBkYXJrOmdyb3VwLWhvdmVyL3NlYXJjaDp0ZXh0LWdyYXktMjAwIj48Y2lyY2xlIGN4PSIxMSIgY3k9IjExIiByPSI4Ij48L2NpcmNsZT48cGF0aCBkPSJtMjEgMjEtNC4zLTQuMyIgLz48L3N2Zz4="
class="lucide lucide-search min-w-4 flex-none text-gray-700 group-hover/search:text-gray-800 dark:text-gray-400 dark:group-hover/search:text-gray-200" />

<div class="truncate min-w-0">

Search...

</div>

</div>

<span class="flex-none text-xs font-semibold">⌘K</span>

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9InNpemUtNCBzaHJpbmstMCB0ZXh0LWdyYXktNzAwIGdyb3VwLWhvdmVyL2FpOnRleHQtZ3JheS04MDAgZGFyazp0ZXh0LWdyYXktNDAwIGRhcms6Z3JvdXAtaG92ZXIvYWk6dGV4dC1ncmF5LTIwMCI+PHBhdGggZD0iTTUuNjU3OTkgMi45OUw0LjM5NDk5IDIuNTY5TDMuOTczOTkgMS4zMDZDMy44MzY5OSAwLjg5OCAzLjE2MTk5IDAuODk4IDMuMDI0OTkgMS4zMDZMMi42MDM5OSAyLjU2OUwxLjM0MDk5IDIuOTlDMS4xMzY5OSAzLjA1OCAwLjk5ODk5MyAzLjI0OSAwLjk5ODk5MyAzLjQ2NEMwLjk5ODk5MyAzLjY3OSAxLjEzNjk5IDMuODcgMS4zNDA5OSAzLjkzOEwyLjYwMzk5IDQuMzU5TDMuMDI0OTkgNS42MjJDMy4wOTI5OSA1LjgyNiAzLjI4NDk5IDUuOTY0IDMuNDk5OTkgNS45NjRDMy43MTQ5OSA1Ljk2NCAzLjkwNTk5IDUuODI2IDMuOTc0OTkgNS42MjJMNC4zOTU5OSA0LjM1OUw1LjY1ODk5IDMuOTM4QzUuODYyOTkgMy44NyA2LjAwMDk5IDMuNjc5IDYuMDAwOTkgMy40NjRDNi4wMDA5OSAzLjI0OSA1Ljg2MTk5IDMuMDU4IDUuNjU3OTkgMi45OVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgc3Ryb2tlPSJub25lIiAvPjxwYXRoIGQ9Ik05LjUgMi43NUwxMS40MTIgNy41ODdMMTYuMjUgOS41TDExLjQxMiAxMS40MTNMOS41IDE2LjI1TDcuNTg3IDExLjQxM0wyLjc1IDkuNUw3LjU4NyA3LjU4N0w5LjUgMi43NVoiIHN0cm9rZT0iY3VycmVudENvbG9yIiB3aWR0aD0iMS41IiBsaW5lY2FwPSJyb3VuZCIgbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg=="
class="size-4 shrink-0 text-gray-700 group-hover/ai:text-gray-800 dark:text-gray-400 dark:group-hover/ai:text-gray-200" /><span class="text-sm text-gray-500 dark:text-white/50 whitespace-nowrap">Ask
AI</span>

</div>

<div class="flex-1 relative hidden lg:flex items-center ml-auto justify-end space-x-4">

- <a href="https://platform.claude.com/"
  class="flex items-center gap-1.5 whitespace-nowrap font-medium text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  target="_blank">Claude Developer Platform</a>
- <a href="https://claude.ai/code"
  class="flex items-center gap-1.5 whitespace-nowrap font-medium text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Claude
  Code on the Web</a>
- <span id="topbar-cta-button"><a href="https://claude.ai/code"
  class="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium"
  target="_blank"><span
  class="absolute inset-0 bg-primary-dark rounded-xl group-hover:opacity-[0.9]"></span></a></span>
  <div class="mr-0.5 space-x-2.5 flex items-center">

  <span class="z-10 text-white">Claude Code on the Web</span><img
  src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMyIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0iaC01IHJvdGF0ZS0wIG92ZXJmbG93LXZpc2libGUgdGV4dC13aGl0ZS85MCI+PHBhdGggZD0iTTAgMEwzIDNMMCA2IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz48L3N2Zz4="
  class="h-5 rotate-0 overflow-visible text-white/90" />

  </div>

<div class="flex items-center">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgY2xhc3M9InNpemUtNCBibG9jayB0ZXh0LWdyYXktNDAwIGRhcms6aGlkZGVuIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAiPjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8yODgwXzczNDApIj48cGF0aCBkPSJNOCAxLjExMTMzVjIuMDAwMjIiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PHBhdGggZD0iTTEyLjg3MTEgMy4xMjg5MUwxMi4yNDI3IDMuNzU3MzUiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PHBhdGggZD0iTTE0Ljg4ODkgOEgxNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMTIuODcxMSAxMi44NzExTDEyLjI0MjcgMTIuMjQyNyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNOCAxNC44ODg5VjE0IiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPjxwYXRoIGQ9Ik0zLjEyODkxIDEyLjg3MTFMMy43NTczNSAxMi4yNDI3IiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPjxwYXRoIGQ9Ik0xLjExMTMzIDhIMi4wMDAyMiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMy4xMjg5MSAzLjEyODkxTDMuNzU3MzUgMy43NTczNSIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNOC4wMDA0MyAxMS43NzgyQzEwLjA4NjggMTEuNzc4MiAxMS43NzgyIDEwLjA4NjggMTEuNzc4MiA4LjAwMDQzQzExLjc3ODIgNS45MTQwMiAxMC4wODY4IDQuMjIyNjYgOC4wMDA0MyA0LjIyMjY2QzUuOTE0MDIgNC4yMjI2NiA0LjIyMjY2IDUuOTE0MDIgNC4yMjI2NiA4LjAwMDQzQzQuMjIyNjYgMTAuMDg2OCA1LjkxNDAyIDExLjc3ODIgOC4wMDA0MyAxMS43NzgyWiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L2c+PGRlZnM+PGNsaXBwYXRoIGlkPSJjbGlwMF8yODgwXzczNDAiPjxyZWN0IHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0id2hpdGUiIC8+PC9jbGlwcGF0aD48L2RlZnM+PC9zdmc+"
class="size-4 block text-gray-400 dark:hidden group-hover:text-gray-600" /><img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLW1vb24gc2l6ZS00IGhpZGRlbiBkYXJrOmJsb2NrIHRleHQtZ3JheS01MDAgZGFyazpncm91cC1ob3Zlcjp0ZXh0LWdyYXktMzAwIj48cGF0aCBkPSJNMTIgM2E2IDYgMCAwIDAgOSA5IDkgOSAwIDEgMS05LTlaIiAvPjwvc3ZnPg=="
class="lucide lucide-moon size-4 hidden dark:block text-gray-500 dark:group-hover:text-gray-300" />

</div>

</div>

<div class="flex lg:hidden items-center gap-3">

<span class="sr-only">Search...</span><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaC00IHctNCBiZy1ncmF5LTUwMCBkYXJrOmJnLWdyYXktNDAwIGhvdmVyOmJnLWdyYXktNjAwIGRhcms6aG92ZXI6YmctZ3JheS0zMDAiIHN0eWxlPSItd2Via2l0LW1hc2staW1hZ2U6dXJsKGh0dHBzOi8vZDNnazJjNXhpbTFqZTIuY2xvdWRmcm9udC5uZXQvdjcuMS4wL3NvbGlkL21hZ25pZnlpbmctZ2xhc3Muc3ZnKTstd2Via2l0LW1hc2stcmVwZWF0Om5vLXJlcGVhdDstd2Via2l0LW1hc2stcG9zaXRpb246Y2VudGVyO21hc2staW1hZ2U6dXJsKGh0dHBzOi8vZDNnazJjNXhpbTFqZTIuY2xvdWRmcm9udC5uZXQvdjcuMS4wL3NvbGlkL21hZ25pZnlpbmctZ2xhc3Muc3ZnKTttYXNrLXJlcGVhdDpuby1yZXBlYXQ7bWFzay1wb3NpdGlvbjpjZW50ZXIiPjwvc3ZnPg=="
class="h-4 w-4 bg-gray-500 dark:bg-gray-400 hover:bg-gray-600 dark:hover:bg-gray-300" />

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9InNpemUtNC41IHRleHQtZ3JheS01MDAgZGFyazp0ZXh0LWdyYXktNDAwIGhvdmVyOnRleHQtZ3JheS02MDAgZGFyazpob3Zlcjp0ZXh0LWdyYXktMzAwIj48cGF0aCBkPSJNNS42NTc5OSAyLjk5TDQuMzk0OTkgMi41NjlMMy45NzM5OSAxLjMwNkMzLjgzNjk5IDAuODk4IDMuMTYxOTkgMC44OTggMy4wMjQ5OSAxLjMwNkwyLjYwMzk5IDIuNTY5TDEuMzQwOTkgMi45OUMxLjEzNjk5IDMuMDU4IDAuOTk4OTkzIDMuMjQ5IDAuOTk4OTkzIDMuNDY0QzAuOTk4OTkzIDMuNjc5IDEuMTM2OTkgMy44NyAxLjM0MDk5IDMuOTM4TDIuNjAzOTkgNC4zNTlMMy4wMjQ5OSA1LjYyMkMzLjA5Mjk5IDUuODI2IDMuMjg0OTkgNS45NjQgMy40OTk5OSA1Ljk2NEMzLjcxNDk5IDUuOTY0IDMuOTA1OTkgNS44MjYgMy45NzQ5OSA1LjYyMkw0LjM5NTk5IDQuMzU5TDUuNjU4OTkgMy45MzhDNS44NjI5OSAzLjg3IDYuMDAwOTkgMy42NzkgNi4wMDA5OSAzLjQ2NEM2LjAwMDk5IDMuMjQ5IDUuODYxOTkgMy4wNTggNS42NTc5OSAyLjk5WiIgZmlsbD0iY3VycmVudENvbG9yIiBzdHJva2U9Im5vbmUiIC8+PHBhdGggZD0iTTkuNSAyLjc1TDExLjQxMiA3LjU4N0wxNi4yNSA5LjVMMTEuNDEyIDExLjQxM0w5LjUgMTYuMjVMNy41ODcgMTEuNDEzTDIuNzUgOS41TDcuNTg3IDcuNTg3TDkuNSAyLjc1WiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHdpZHRoPSIxLjUiIGxpbmVjYXA9InJvdW5kIiBsaW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="size-4.5 text-gray-500 dark:text-gray-400 hover:text-gray-600 dark:hover:text-gray-300" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaC00IHctNCBiZy1ncmF5LTUwMCBkYXJrOmJnLWdyYXktNDAwIGhvdmVyOmJnLWdyYXktNjAwIGRhcms6aG92ZXI6YmctZ3JheS0zMDAiIHN0eWxlPSItd2Via2l0LW1hc2staW1hZ2U6dXJsKGh0dHBzOi8vZDNnazJjNXhpbTFqZTIuY2xvdWRmcm9udC5uZXQvdjcuMS4wL3NvbGlkL2VsbGlwc2lzLXZlcnRpY2FsLnN2Zyk7LXdlYmtpdC1tYXNrLXJlcGVhdDpuby1yZXBlYXQ7LXdlYmtpdC1tYXNrLXBvc2l0aW9uOmNlbnRlcjttYXNrLWltYWdlOnVybChodHRwczovL2QzZ2syYzV4aW0xamUyLmNsb3VkZnJvbnQubmV0L3Y3LjEuMC9zb2xpZC9lbGxpcHNpcy12ZXJ0aWNhbC5zdmcpO21hc2stcmVwZWF0Om5vLXJlcGVhdDttYXNrLXBvc2l0aW9uOmNlbnRlciI+PC9zdmc+"
class="h-4 w-4 bg-gray-500 dark:bg-gray-400 hover:bg-gray-600 dark:hover:bg-gray-300" />

</div>

</div>

</div>

<div class="text-gray-500 hover:text-gray-600 dark:text-gray-400 dark:hover:text-gray-300">

<span class="sr-only">Navigation</span><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaC00IiBmaWxsPSJjdXJyZW50Q29sb3IiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDQ0OCA1MTIiPjxwYXRoIGQ9Ik0wIDk2QzAgNzguMyAxNC4zIDY0IDMyIDY0SDQxNmMxNy43IDAgMzIgMTQuMyAzMiAzMnMtMTQuMyAzMi0zMiAzMkgzMkMxNC4zIDEyOCAwIDExMy43IDAgOTZ6TTAgMjU2YzAtMTcuNyAxNC4zLTMyIDMyLTMySDQxNmMxNy43IDAgMzIgMTQuMyAzMiAzMnMtMTQuMyAzMi0zMiAzMkgzMmMtMTcuNyAwLTMyLTE0LjMtMzItMzJ6TTQ0OCA0MTZjMCAxNy43LTE0LjMgMzItMzIgMzJIMzJjLTE3LjcgMC0zMi0xNC4zLTMyLTMyczE0LjMtMzIgMzItMzJINDE2YzE3LjcgMCAzMiAxNC4zIDMyIDMyeiIgLz48L3N2Zz4="
class="h-4" />

</div>

<div class="ml-4 flex text-sm leading-6 whitespace-nowrap min-w-0 space-x-3 overflow-hidden">

<div class="flex items-center space-x-3 flex-shrink-0">

Use Claude Code<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMyIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0iaC01IHJvdGF0ZS0wIG92ZXJmbG93LXZpc2libGUgZmlsbC1ncmF5LTQwMCI+PHBhdGggZD0iTTAgMEwzIDNMMCA2IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz48L3N2Zz4="
class="h-5 rotate-0 overflow-visible fill-gray-400" />

</div>

<div class="font-semibold text-gray-900 truncate dark:text-gray-200 min-w-0 flex-1">

Best Practices for Claude Code

</div>

</div>

</div>

<div class="hidden lg:flex px-12 h-12">

<div class="nav-tabs h-full flex text-sm gap-x-6">

<a href="https://code.claude.com/docs/en/overview"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium hover:text-gray-800 dark:hover:text-gray-300 text-gray-800 dark:text-gray-200 [text-shadow:-0.2px_0_0_currentColor,0.2px_0_0_currentColor]"
data-active="true">Getting started</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 bg-primary dark:bg-primary-light">

</div>

<a href="https://code.claude.com/docs/en/sub-agents"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Build
with Claude Code</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/third-party-integrations"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Deployment</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/setup"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Administration</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/settings"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Configuration</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/cli-reference"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Reference</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/agent-sdk/overview"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Agent
SDK</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/whats-new"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">What's
New</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

<a href="https://code.claude.com/docs/en/legal-and-compliance"
class="link nav-tabs-item group relative h-full gap-2 flex items-center font-medium text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-300">Resources</a>

<div class="absolute bottom-0 h-[1.5px] w-full left-0 group-hover:bg-gray-200 dark:group-hover:bg-gray-700">

</div>

</div>

</div>

</div>

</div>

<span hidden=""
style="position:fixed;top:1px;left:1px;width:1px;height:0;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0;display:none"></span>

</div>

<div class="scroll-mt-[var(--scroll-mt)] peer-[.is-custom]:max-w-none peer-[.is-center]:max-w-3xl peer-[.is-not-custom]:peer-[.is-not-center]:max-w-8xl peer-[.is-not-custom]:px-4 peer-[.is-not-custom]:mx-auto peer-[.is-not-custom]:lg:px-8 peer-[.is-wide]:[&>div:last-child]:max-w-6xl peer-[.is-custom]:[&>div:first-child]:!hidden peer-[.is-custom]:[&>div:first-child]:sm:!hidden peer-[.is-custom]:[&>div:first-child]:md:!hidden peer-[.is-custom]:[&>div:first-child]:lg:!hidden peer-[.is-custom]:[&>div:first-child]:xl:!hidden peer-[.is-center]:[&>div:first-child]:!hidden peer-[.is-center]:[&>div:first-child]:sm:!hidden peer-[.is-center]:[&>div:first-child]:md:!hidden peer-[.is-center]:[&>div:first-child]:lg:!hidden peer-[.is-center]:[&>div:first-child]:xl:!hidden">

<div id="sidebar"
class="z-20 hidden lg:block fixed bottom-0 right-auto w-[18rem]"
style="top:7rem">

<div id="sidebar-content"
class="absolute inset-0 z-10 stable-scrollbar-gutter overflow-auto pr-8 pb-10">

<div class="relative lg:text-sm lg:leading-6">

<div class="sticky top-0 h-8 pointer-events-none z-10 bg-gradient-to-b from-background-light dark:from-background-dark">

</div>

<div id="navigation-items">

<div>

<div class="sidebar-group-header flex items-center gap-2.5 pl-4 mb-3.5 lg:mb-2.5 font-semibold text-gray-900 dark:text-gray-200">

##### Getting started

</div>

- <span id="/en/overview"><a href="https://code.claude.com/docs/en/overview"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left break-words hyphens-auto rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Overview</span>

  </div>

  </div>
- <span id="/en/quickstart"><a href="https://code.claude.com/docs/en/quickstart"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left break-words hyphens-auto rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Quickstart</span>

  </div>

  </div>
- <span id="/en/changelog"><a href="https://code.claude.com/docs/en/changelog"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left break-words hyphens-auto rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Changelog</span>

  </div>

  </div>

</div>

<div class="mt-6 lg:mt-8">

<div class="sidebar-group-header flex items-center gap-2.5 pl-4 mb-3.5 lg:mb-2.5 font-semibold text-gray-900 dark:text-gray-200">

##### Core concepts

</div>

- <span id="/en/how-claude-code-works"><a href="https://code.claude.com/docs/en/how-claude-code-works"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">How Claude
  Code works</span>

  </div>

  </div>
- <span id="/en/features-overview"><a href="https://code.claude.com/docs/en/features-overview"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Extend
  Claude Code</span>

  </div>

  </div>
- <span id="/en/claude-directory"><a href="https://code.claude.com/docs/en/claude-directory"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Explore the
  .claude directory</span>

  </div>

  </div>
- <span id="/en/context-window"><a href="https://code.claude.com/docs/en/context-window"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Explore the
  context window</span>

  </div>

  </div>

</div>

<div class="mt-6 lg:mt-8">

<div class="sidebar-group-header flex items-center gap-2.5 pl-4 mb-3.5 lg:mb-2.5 font-semibold text-gray-900 dark:text-gray-200">

##### Use Claude Code

</div>

- <span id="/en/memory"><a href="https://code.claude.com/docs/en/memory"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Store
  instructions and memories</span>

  </div>

  </div>
- <span id="/en/permission-modes"><a href="https://code.claude.com/docs/en/permission-modes"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Permission
  modes</span>

  </div>

  </div>
- <span id="/en/common-workflows"><a href="https://code.claude.com/docs/en/common-workflows"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Common
  workflows</span>

  </div>

  </div>
- <span id="/en/best-practices"><a href="claude-code-best-practices.html"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] bg-primary/10 text-primary [text-shadow:-0.2px_0_0_currentColor,0.2px_0_0_currentColor] dark:text-primary-light dark:bg-primary-light/10"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Best
  practices</span>

  </div>

  </div>

</div>

<div class="mt-6 lg:mt-8">

<div class="sidebar-group-header flex items-center gap-2.5 pl-4 mb-3.5 lg:mb-2.5 font-semibold text-gray-900 dark:text-gray-200">

##### Platforms and integrations

</div>

- <span id="/en/platforms"><a href="https://code.claude.com/docs/en/platforms"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left break-words hyphens-auto rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Overview</span>

  </div>

  </div>

- <span id="/en/remote-control"><a href="https://code.claude.com/docs/en/remote-control"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Remote
  Control</span>

  </div>

  </div>

- <div>

  Claude Code on the web

  </div>

  <div class="h-[1lh] flex items-center shrink-0">

  <img
  src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0idHJhbnNpdGlvbi10cmFuc2Zvcm0gdGV4dC1ncmF5LTQwMCBvdmVyZmxvdy12aXNpYmxlIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAgZGFyazp0ZXh0LWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTQwMCB3LTIgaC1bMWxoXSAtbXItMC41Ij48cGF0aCBkPSJNMCAwTDMgM0wwIDYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPjwvc3ZnPg=="
  class="transition-transform text-gray-400 overflow-visible group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 w-2 h-[1lh] -mr-0.5" />

  </div>

- <div>

  Claude Code on desktop

  </div>

  <div class="h-[1lh] flex items-center shrink-0">

  <img
  src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0idHJhbnNpdGlvbi10cmFuc2Zvcm0gdGV4dC1ncmF5LTQwMCBvdmVyZmxvdy12aXNpYmxlIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAgZGFyazp0ZXh0LWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTQwMCB3LTIgaC1bMWxoXSAtbXItMC41Ij48cGF0aCBkPSJNMCAwTDMgM0wwIDYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPjwvc3ZnPg=="
  class="transition-transform text-gray-400 overflow-visible group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 w-2 h-[1lh] -mr-0.5" />

  </div>

- <span id="/en/chrome"><a href="https://code.claude.com/docs/en/chrome"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Chrome
  extension (beta)</span>

  </div>

  </div>

- <span id="/en/computer-use"><a href="https://code.claude.com/docs/en/computer-use"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Computer use
  (preview)</span>

  </div>

  </div>

- <span id="/en/vs-code"><a href="https://code.claude.com/docs/en/vs-code"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Visual
  Studio Code</span>

  </div>

  </div>

- <span id="/en/jetbrains"><a href="https://code.claude.com/docs/en/jetbrains"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">JetBrains
  IDEs</span>

  </div>

  </div>

- <div>

  Code review & CI/CD

  </div>

  <div class="h-[1lh] flex items-center shrink-0">

  <img
  src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0idHJhbnNpdGlvbi10cmFuc2Zvcm0gdGV4dC1ncmF5LTQwMCBvdmVyZmxvdy12aXNpYmxlIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAgZGFyazp0ZXh0LWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTQwMCB3LTIgaC1bMWxoXSAtbXItMC41Ij48cGF0aCBkPSJNMCAwTDMgM0wwIDYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPjwvc3ZnPg=="
  class="transition-transform text-gray-400 overflow-visible group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 w-2 h-[1lh] -mr-0.5" />

  </div>

- <span id="/en/slack"><a href="https://code.claude.com/docs/en/slack"
  class="group flex items-start pr-3 py-1.5 cursor-pointer gap-x-3 text-left rounded-xl w-full outline-offset-[-1px] hover:bg-gray-600/5 dark:hover:bg-gray-200/5 text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem"></a></span>
  <div class="flex-1 flex min-w-0 items-start gap-x-2.5">

  <div class="flex min-w-0 flex-1 flex-wrap items-center gap-1.5 [word-break:break-word]">

  <span class="min-w-0 max-w-full break-words hyphens-auto">Claude Code
  in Slack</span>

  </div>

  </div>

</div>

</div>

</div>

</div>

</div>

<div id="content-container">

<span id="background-color"
class="fixed inset-0 bg-background-light dark:bg-background-dark -z-10 pointer-events-none"></span><span class="block absolute dark:hidden inset-0 overflow-hidden pointer-events-none"></span><span class="hidden absolute dark:block inset-0 overflow-hidden pointer-events-none"></span>

<div class="flex flex-row-reverse gap-12 box-border w-full pt-40 lg:pt-10">

<div id="content-side-layout"
class="hidden xl:flex self-start sticky xl:flex-col max-w-[28rem] z-[21] h-[calc(100vh-9.5rem)] top-[calc(9.5rem-var(--sidenav-move-up,0px))]">

<div id="table-of-contents-layout"
class="z-10 hidden xl:flex box-border max-h-full pl-10 w-[19rem]">

<div id="table-of-contents"
class="text-gray-600 text-sm leading-6 w-[16.5rem] overflow-y-auto space-y-2 pb-4 -mt-10 pt-10">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iaC0zIHctMyI+PHBhdGggZD0iTTIuNDQ0MzQgMTIuNjY2NUgxMy41NTU0IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PHBhdGggZD0iTTIuNDQ0MzQgMy4zMzM1SDEzLjU1NTQiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi40NDQzNCA4SDcuMzMzMjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="h-3 w-3" />On this page

<div>

- <a
  href="claude-code-best-practices.html#give-claude-a-way-to-verify-its-work"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Give
  Claude a way to verify its work</a>
- <a
  href="claude-code-best-practices.html#explore-first-then-plan-then-code"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Explore
  first, then plan, then code</a>
- <a
  href="claude-code-best-practices.html#provide-specific-context-in-your-prompts"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Provide
  specific context in your prompts</a>
- <a href="claude-code-best-practices.html#provide-rich-content"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Provide rich content</a>
- <a href="claude-code-best-practices.html#configure-your-environment"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Configure
  your environment</a>
- <a href="claude-code-best-practices.html#write-an-effective-claude-md"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Write an effective CLAUDE.md</a>
- <a href="claude-code-best-practices.html#configure-permissions"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Configure permissions</a>
- <a href="claude-code-best-practices.html#use-cli-tools"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Use CLI tools</a>
- <a href="claude-code-best-practices.html#connect-mcp-servers"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Connect MCP servers</a>
- <a href="claude-code-best-practices.html#set-up-hooks"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Set up hooks</a>
- <a href="claude-code-best-practices.html#create-skills"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Create skills</a>
- <a href="claude-code-best-practices.html#create-custom-subagents"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Create custom subagents</a>
- <a href="claude-code-best-practices.html#install-plugins"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Install plugins</a>
- <a href="claude-code-best-practices.html#communicate-effectively"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Communicate
  effectively</a>
- <a href="claude-code-best-practices.html#ask-codebase-questions"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Ask codebase questions</a>
- <a href="claude-code-best-practices.html#let-claude-interview-you"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Let Claude interview you</a>
- <a href="claude-code-best-practices.html#manage-your-session"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Manage
  your session</a>
- <a href="claude-code-best-practices.html#course-correct-early-and-often"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Course-correct early and often</a>
- <a href="claude-code-best-practices.html#manage-context-aggressively"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Manage context aggressively</a>
- <a
  href="claude-code-best-practices.html#use-subagents-for-investigation"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Use subagents for investigation</a>
- <a href="claude-code-best-practices.html#rewind-with-checkpoints"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Rewind with checkpoints</a>
- <a href="claude-code-best-practices.html#resume-conversations"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Resume conversations</a>
- <a href="claude-code-best-practices.html#automate-and-scale"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Automate
  and scale</a>
- <a href="claude-code-best-practices.html#run-non-interactive-mode"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Run non-interactive mode</a>
- <a href="claude-code-best-practices.html#run-multiple-claude-sessions"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Run multiple Claude sessions</a>
- <a href="claude-code-best-practices.html#fan-out-across-files"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Fan out across files</a>
- <a
  href="claude-code-best-practices.html#run-autonomously-with-auto-mode"
  class="group flex items-start break-words py-1 whitespace-pre-wrap text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300"
  style="padding-left:1rem">Run autonomously with auto mode</a>
- <a href="claude-code-best-practices.html#avoid-common-failure-patterns"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Avoid
  common failure patterns</a>
- <a href="claude-code-best-practices.html#develop-your-intuition"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Develop
  your intuition</a>
- <a href="claude-code-best-practices.html#related-resources"
  class="break-words py-1 block font-medium hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-300">Related
  resources</a>

</div>

</div>

</div>

</div>

<div id="content-area"
class="relative grow box-border flex-col w-full mx-auto px-1 lg:pl-[23.7rem] lg:-ml-12 xl:w-[calc(100%-28rem)]">

<div id="header" class="relative leading-none">

<div class="mt-0.5 space-y-2.5">

<div class="eyebrow h-5 text-primary dark:text-primary-light text-sm font-semibold">

Use Claude Code

</div>

<div class="flex flex-col sm:flex-row items-start sm:items-center relative gap-2 min-w-0">

# Best Practices for Claude Code

<div id="page-context-menu"
class="items-center shrink-0 min-w-[156px] justify-end ml-auto sm:flex hidden">

<div class="flex items-center gap-2 text-sm text-center font-medium">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9InNpemUtNCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgd2lkdGg9IjEuNSIgbGluZWNhcD0icm91bmQiIGxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHdpZHRoPSIxLjUiIGxpbmVjYXA9InJvdW5kIiBsaW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="size-4" />Copy page

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0idHJhbnNpdGlvbi10cmFuc2Zvcm0gdGV4dC1ncmF5LTQwMCBvdmVyZmxvdy12aXNpYmxlIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAgZGFyazp0ZXh0LWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTQwMCByb3RhdGUtOTAiPjxwYXRoIGQ9Ik0wIDBMMyAzTDAgNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIC8+PC9zdmc+"
class="transition-transform text-gray-400 overflow-visible group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 rotate-90" />

</div>

</div>

</div>

<div class="mt-2 text-lg prose prose-gray dark:prose-invert [&>*]:[overflow-wrap:anywhere]">

Tips and patterns for getting the most out of Claude Code, from
configuring your environment to scaling across parallel sessions.

</div>

<div id="page-context-menu"
class="flex items-center shrink-0 min-w-[156px] mt-3 sm:hidden">

<div class="flex items-center gap-2 text-sm text-center font-medium">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9InNpemUtNCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgd2lkdGg9IjEuNSIgbGluZWNhcD0icm91bmQiIGxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHdpZHRoPSIxLjUiIGxpbmVjYXA9InJvdW5kIiBsaW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="size-4" />Copy page

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAtOSAzIDI0IiBjbGFzcz0idHJhbnNpdGlvbi10cmFuc2Zvcm0gdGV4dC1ncmF5LTQwMCBvdmVyZmxvdy12aXNpYmxlIGdyb3VwLWhvdmVyOnRleHQtZ3JheS02MDAgZGFyazp0ZXh0LWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTQwMCByb3RhdGUtOTAiPjxwYXRoIGQ9Ik0wIDBMMyAzTDAgNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIC8+PC9zdmc+"
class="transition-transform text-gray-400 overflow-visible group-hover:text-gray-600 dark:text-gray-600 dark:group-hover:text-gray-400 rotate-90" />

</div>

</div>

<div id="content"
class="mdx-content @container/columns-container relative mt-8 prose prose-gray dark:prose-invert [contain:inline-size] isolate empty:hidden mb-14"
page-title="Best Practices for Claude Code"
page-href="/en/best-practices">

<span data-as="p">Claude Code is an agentic coding environment. Unlike a
chatbot that answers questions and waits, Claude Code can read your
files, run commands, make changes, and autonomously work through
problems while you watch, redirect, or step away entirely.</span>
<span data-as="p">This changes how you work. Instead of writing code
yourself and asking Claude to review it, you describe what you want and
Claude figures out how to build it. Claude explores, plans, and
implements.</span> <span data-as="p">But this autonomy still comes with
a learning curve. Claude works within certain constraints you need to
understand.</span> <span data-as="p">This guide covers patterns that
have proven effective across Anthropic’s internal teams and for
engineers using Claude Code across various codebases, languages, and
environments. For how the agentic loop works under the hood, see
<a href="https://code.claude.com/docs/en/how-claude-code-works"
class="link">How Claude Code works</a>.</span>

------------------------------------------------------------------------

<span data-as="p">Most best practices are based on one constraint:
Claude’s context window fills up fast, and performance degrades as it
fills.</span> <span data-as="p">Claude’s context window holds your
entire conversation, including every message, every file Claude reads,
and every command output. However, this can fill up fast. A single
debugging session or codebase exploration might generate and consume
tens of thousands of tokens.</span> <span data-as="p">This matters since
LLM performance degrades as context fills. When the context window is
getting full, Claude may start “forgetting” earlier instructions or
making more mistakes. The context window is the most important resource
to manage. To see how a session fills up in practice,
<a href="https://code.claude.com/docs/en/context-window"
class="link">watch an interactive walkthrough</a> of what loads at
startup and what each file read costs. Track context usage continuously
with a
<a href="https://code.claude.com/docs/en/statusline" class="link">custom
status line</a>, and see
<a href="https://code.claude.com/docs/en/costs#reduce-token-usage"
class="link">Reduce token usage</a> for strategies on reducing token
usage.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a
href="claude-code-best-practices.html#give-claude-a-way-to-verify-its-work"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Give Claude a way to verify its work</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Include tests, screenshots, or expected outputs so
Claude can check itself. This is the single highest-leverage thing you
can do.</span>

</div>

</div>

<span data-as="p">Claude performs dramatically better when it can verify
its own work, like run tests, compare screenshots, and validate
outputs.</span> <span data-as="p">Without clear success criteria, it
might produce something that looks right but actually doesn’t work. You
become the only feedback loop, and every mistake requires your
attention.</span>

<div class="[--page-padding:20px] overflow-x-auto flex w-[calc(100%+(var(--page-padding)*2))] my-[1em] py-[1em] -mx-[var(--page-padding)] max-w-none [contain:inline-size]"
table-wrapper="true">

<div class="px-[var(--page-padding)] grow max-w-none table">

| Strategy | Before | After |
|----|----|----|
| **Provide verification criteria** | *”implement a function that validates email addresses"* | *"write a validateEmail function. example test cases: <a href="mailto:user@example.com" class="link" target="_blank"
rel="noreferrer">user@example.com</a> is true, invalid is false, <a href="mailto:user@.com" class="link" target="_blank"
rel="noreferrer">user@.com</a> is false. run the tests after implementing”* |
| **Verify UI changes visually** | *”make the dashboard look better"* | *"\[paste screenshot\] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them”* |
| **Address root causes, not symptoms** | *”the build is failing"* | *"the build fails with this error: \[paste error\]. fix it and verify the build succeeds. address the root cause, don’t suppress the error”* |

</div>

</div>

<span data-as="p">UI changes can be verified using the
<a href="https://code.claude.com/docs/en/chrome" class="link">Claude in
Chrome extension</a>. It opens new tabs in your browser, tests the UI,
and iterates until the code works.</span> <span data-as="p">Your
verification can also be a test suite, a linter, or a Bash command that
checks output. Invest in making your verification rock-solid.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a
href="claude-code-best-practices.html#explore-first-then-plan-then-code"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Explore first, then plan, then code</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Separate research and planning from implementation to
avoid solving the wrong problem.</span>

</div>

</div>

<span data-as="p">Letting Claude jump straight to coding can produce
code that solves the wrong problem. Use <a
href="https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis"
class="link">Plan Mode</a> to separate exploration from
execution.</span> <span data-as="p">The recommended workflow has four
phases:</span>

<div class="steps ml-3.5 mt-10 mb-6" role="list">

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-gray-200/70 dark:bg-white/10"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

1

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Explore

<div class="prose dark:prose-invert" component-part="step-content">

<span data-as="p">Enter Plan Mode. Claude reads files and answers
questions without making changes.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="3" language="text">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0" title="claude (Plan Mode)">claude (Plan
Mode)</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
read /src/auth and understand how we handle sessions and login.
also look at how we manage environment variables for secrets.
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

</div>

</div>

</div>

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-gray-200/70 dark:bg-white/10"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

2

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Plan

<div class="prose dark:prose-invert" component-part="step-content">

<span data-as="p">Ask Claude to create a detailed implementation
plan.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="3" language="text">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0" title="claude (Plan Mode)">claude (Plan
Mode)</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
I want to add Google OAuth. What files need to change?
What's the session flow? Create a plan.
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Press `Ctrl+G` to open the plan in your text editor
for direct editing before Claude proceeds.</span>

</div>

</div>

</div>

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-gray-200/70 dark:bg-white/10"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

3

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Implement

<div class="prose dark:prose-invert" component-part="step-content">

<span data-as="p">Switch back to Normal Mode and let Claude code,
verifying against its plan.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="3" language="text">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0" title="claude (Normal Mode)">claude
(Normal Mode)</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
implement the OAuth flow from your plan. write tests for the
callback handler, run the test suite and fix any failures.
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

</div>

</div>

</div>

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-transparent bg-gradient-to-b from-gray-200 dark:from-white/10 via-80% to-transparent group-has-[[data-component-part="step-content"]:empty]/step:hidden"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

4

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Commit

<div class="prose dark:prose-invert" component-part="step-content">

<span data-as="p">Ask Claude to commit with a descriptive message and
create a PR.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="2" language="text">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0" title="claude (Normal Mode)">claude
(Normal Mode)</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
commit with a descriptive message and open a PR
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

</div>

</div>

</div>

</div>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-zinc-500/20 bg-zinc-50/50 dark:border-zinc-500/30 dark:bg-zinc-500/10"
callout-type="callout">

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-zinc-900 dark:text-zinc-200"
component-part="callout-content">

<span data-as="p">Plan Mode is useful, but also adds
overhead.</span><span data-as="p">For tasks where the scope is clear and
the fix is small (like fixing a typo, adding a log line, or renaming a
variable) ask Claude to do it directly.</span><span data-as="p">Planning
is most useful when you’re uncertain about the approach, when the change
modifies multiple files, or when you’re unfamiliar with the code being
modified. If you could describe the diff in one sentence, skip the
plan.</span>

</div>

</div>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a
href="claude-code-best-practices.html#provide-specific-context-in-your-prompts"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Provide specific context in your
prompts</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">The more precise your instructions, the fewer
corrections you’ll need.</span>

</div>

</div>

<span data-as="p">Claude can infer intent, but it can’t read your mind.
Reference specific files, mention constraints, and point to example
patterns.</span>

<div class="[--page-padding:20px] overflow-x-auto flex w-[calc(100%+(var(--page-padding)*2))] my-[1em] py-[1em] -mx-[var(--page-padding)] max-w-none [contain:inline-size]"
table-wrapper="true">

<div class="px-[var(--page-padding)] grow max-w-none table">

| Strategy | Before | After |
|----|----|----|
| **Scope the task.** Specify which file, what scenario, and testing preferences. | *”add tests for foo.py"* | *"write a test for foo.py covering the edge case where the user is logged out. avoid mocks.”* |
| **Point to sources.** Direct Claude to the source that can answer a question. | *”why does ExecutionFactory have such a weird api?"* | *"look through ExecutionFactory’s git history and summarize how its api came to be”* |
| **Reference existing patterns.** Point Claude to patterns in your codebase. | *”add a calendar widget"* | *"look at how existing widgets are implemented on the home page to understand the patterns. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards to pick a year. build from scratch without libraries other than the ones already used in the codebase.”* |
| **Describe the symptom.** Provide the symptom, the likely location, and what “fixed” looks like. | *”fix the login bug"* | *"users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it”* |

</div>

</div>

<span data-as="p">Vague prompts can be useful when you’re exploring and
can afford to course-correct. A prompt like
`"what would you improve in this file?"` can surface things you wouldn’t
have thought to ask about.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#provide-rich-content"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Provide rich content</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Use `@` to reference files, paste screenshots/images,
or pipe data directly.</span>

</div>

</div>

<span data-as="p">You can provide rich data to Claude in several
ways:</span>

- **Reference files with `@`** instead of describing where code lives.
  Claude reads the file before responding.
- **Paste images directly**. Copy/paste or drag and drop images into the
  prompt.
- **Give URLs** for documentation and API references. Use `/permissions`
  to allowlist frequently-used domains.
- **Pipe in data** by running `cat error.log | claude` to send file
  contents directly.
- **Let Claude fetch what it needs**. Tell Claude to pull context itself
  using Bash commands, MCP tools, or by reading files.

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#configure-your-environment"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Configure your environment</span>

<span data-as="p">A few setup steps make Claude Code significantly more
effective across all your sessions. For a full overview of extension
features and when to use each one, see
<a href="https://code.claude.com/docs/en/features-overview"
class="link">Extend Claude Code</a>.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#write-an-effective-claude-md"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Write an effective CLAUDE.md</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Run `/init` to generate a starter CLAUDE.md file based
on your current project structure, then refine over time.</span>

</div>

</div>

<span data-as="p">CLAUDE.md is a special file that Claude reads at the
start of every conversation. Include Bash commands, code style, and
workflow rules. This gives Claude persistent context it can’t infer from
code alone.</span> <span data-as="p">The `/init` command analyzes your
codebase to detect build systems, test frameworks, and code patterns,
giving you a solid foundation to refine.</span>
<span data-as="p">There’s no required format for CLAUDE.md files, but
keep it short and human-readable. For example:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="7" language="markdown">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0" title="CLAUDE.md">CLAUDE.md</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">CLAUDE.md is loaded every session, so only include
things that apply broadly. For domain knowledge or workflows that are
only relevant sometimes, use
<a href="https://code.claude.com/docs/en/skills" class="link">skills</a>
instead. Claude loads them on demand without bloating every
conversation.</span> <span data-as="p">Keep it concise. For each line,
ask: *“Would removing this cause Claude to make mistakes?”* If not, cut
it. Bloated CLAUDE.md files cause Claude to ignore your actual
instructions!</span>

<div class="[--page-padding:20px] overflow-x-auto flex w-[calc(100%+(var(--page-padding)*2))] my-[1em] py-[1em] -mx-[var(--page-padding)] max-w-none [contain:inline-size]"
table-wrapper="true">

<div class="px-[var(--page-padding)] grow max-w-none table">

| ✅ Include | ❌ Exclude |
|----|----|
| Bash commands Claude can’t guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like “write clean code” |

</div>

</div>

<span data-as="p">If Claude keeps doing something you don’t want despite
having a rule against it, the file is probably too long and the rule is
getting lost. If Claude asks you questions that are answered in
CLAUDE.md, the phrasing might be ambiguous. Treat CLAUDE.md like code:
review it when things go wrong, prune it regularly, and test changes by
observing whether Claude’s behavior actually shifts.</span>
<span data-as="p">You can tune instructions by adding emphasis (e.g.,
“IMPORTANT” or “YOU MUST”) to improve adherence. Check CLAUDE.md into
git so your team can contribute. The file compounds in value over
time.</span> <span data-as="p">CLAUDE.md files can import additional
files using `@path/to/import` syntax:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="5" language="markdown">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0" title="CLAUDE.md">CLAUDE.md</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">You can place CLAUDE.md files in several
locations:</span>

- **Home folder (`~/.claude/CLAUDE.md`)**: applies to all Claude
  sessions
- **Project root (`./CLAUDE.md`)**: check into git to share with your
  team
- **Project root (`./CLAUDE.local.md`)**: personal project-specific
  notes; add this file to your `.gitignore` so it isn’t shared with your
  team
- **Parent directories**: useful for monorepos where both
  `root/CLAUDE.md` and `root/foo/CLAUDE.md` are pulled in automatically
- **Child directories**: Claude pulls in child CLAUDE.md files on demand
  when working with files in those directories

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#configure-permissions"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Configure permissions</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Use <a
href="https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode"
class="link">auto mode</a> to let a classifier handle approvals,
`/permissions` to allowlist specific commands, or `/sandbox` for
OS-level isolation. Each reduces interruptions while keeping you in
control.</span>

</div>

</div>

<span data-as="p">By default, Claude Code requests permission for
actions that might modify your system: file writes, Bash commands, MCP
tools, etc. This is safe but tedious. After the tenth approval you’re
not really reviewing anymore, you’re just clicking through. There are
three ways to reduce these interruptions:</span>

- **Auto mode**: a separate classifier model reviews commands and blocks
  only what looks risky: scope escalation, unknown infrastructure, or
  hostile-content-driven actions. Best when you trust the general
  direction of a task but don’t want to click through every step
- **Permission allowlists**: permit specific tools you know are safe,
  like `npm run lint` or `git commit`
- **Sandboxing**: enable OS-level isolation that restricts filesystem
  and network access, allowing Claude to work more freely within defined
  boundaries

<span data-as="p">Read more about
<a href="https://code.claude.com/docs/en/permission-modes"
class="link">permission modes</a>,
<a href="https://code.claude.com/docs/en/permissions"
class="link">permission rules</a>, and
<a href="https://code.claude.com/docs/en/sandboxing"
class="link">sandboxing</a>.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#use-cli-tools"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Use CLI tools</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Tell Claude Code to use CLI tools like `gh`, `aws`,
`gcloud`, and `sentry-cli` when interacting with external
services.</span>

</div>

</div>

<span data-as="p">CLI tools are the most context-efficient way to
interact with external services. If you use GitHub, install the `gh`
CLI. Claude knows how to use it for creating issues, opening pull
requests, and reading comments. Without `gh`, Claude can still use the
GitHub API, but unauthenticated requests often hit rate limits.</span>
<span data-as="p">Claude is also effective at learning CLI tools it
doesn’t already know. Try prompts like
`Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#connect-mcp-servers"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Connect MCP servers</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Run `claude mcp add` to connect external tools like
Notion, Figma, or your database.</span>

</div>

</div>

<span data-as="p">With
<a href="https://code.claude.com/docs/en/mcp" class="link">MCP
servers</a>, you can ask Claude to implement features from issue
trackers, query databases, analyze monitoring data, integrate designs
from Figma, and automate workflows.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#set-up-hooks"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Set up hooks</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Use hooks for actions that must happen every time with
zero exceptions.</span>

</div>

</div>

<span data-as="p"><a href="https://code.claude.com/docs/en/hooks-guide"
class="link">Hooks</a> run scripts automatically at specific points in
Claude’s workflow. Unlike CLAUDE.md instructions which are advisory,
hooks are deterministic and guarantee the action happens.</span>
<span data-as="p">Claude can write hooks for you. Try prompts like
*“Write a hook that runs eslint after every file edit”* or *“Write a
hook that blocks writes to the migrations folder.”* Edit
`.claude/settings.json` directly to configure hooks by hand, and run
`/hooks` to browse what’s configured.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#create-skills"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Create skills</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Create `SKILL.md` files in `.claude/skills/` to give
Claude domain knowledge and reusable workflows.</span>

</div>

</div>

<span data-as="p"><a href="https://code.claude.com/docs/en/skills" class="link">Skills</a>
extend Claude’s knowledge with information specific to your project,
team, or domain. Claude applies them automatically when relevant, or you
can invoke them directly with `/skill-name`.</span>
<span data-as="p">Create a skill by adding a directory with a `SKILL.md`
to `.claude/skills/`:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="9" language="markdown">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0"
title=".claude/skills/api-conventions/SKILL.md">.claude/skills/api-conventions/SKILL.md</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Skills can also define repeatable workflows you invoke
directly:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="15" language="markdown">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0"
title=".claude/skills/fix-issue/SKILL.md">.claude/skills/fix-issue/SKILL.md</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Run `/fix-issue 1234` to invoke it. Use
`disable-model-invocation: true` for workflows with side effects that
you want to trigger manually.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#create-custom-subagents"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Create custom subagents</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Define specialized assistants in `.claude/agents/`
that Claude can delegate to for isolated tasks.</span>

</div>

</div>

<span data-as="p"><a href="https://code.claude.com/docs/en/sub-agents"
class="link">Subagents</a> run in their own context with their own set
of allowed tools. They’re useful for tasks that read many files or need
specialized focus without cluttering your main conversation.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 bg-gray-50 dark:bg-white/5 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark p-0.5"
numberoflines="13" language="markdown">

<div class="flex text-gray-400 text-xs rounded-t-[14px] leading-6 font-medium pl-4 pr-2.5 py-1"
component-part="code-block-header">

<div class="flex-grow-0 flex items-center gap-1.5 text-gray-700 dark:text-gray-300 min-w-0"
component-part="code-block-header-filename">

<span class="truncate min-w-0"
title=".claude/agents/security-reviewer.md">.claude/agents/security-reviewer.md</span>

</div>

<div class="flex-1 flex items-center justify-end gap-1.5 print:hidden">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-xt bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Tell Claude to use subagents explicitly: *“Use a
subagent to review this code for security issues.”*</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#install-plugins"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Install plugins</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Run `/plugin` to browse the marketplace. Plugins add
skills, tools, and integrations without configuration.</span>

</div>

</div>

<span data-as="p"><a href="https://code.claude.com/docs/en/plugins"
class="link">Plugins</a> bundle skills, hooks, subagents, and MCP
servers into a single installable unit from the community and Anthropic.
If you work with a typed language, install a <a
href="https://code.claude.com/docs/en/discover-plugins#code-intelligence"
class="link">code intelligence plugin</a> to give Claude precise symbol
navigation and automatic error detection after edits.</span>
<span data-as="p">For guidance on choosing between skills, subagents,
hooks, and MCP, see <a
href="https://code.claude.com/docs/en/features-overview#match-features-to-your-goal"
class="link">Extend Claude Code</a>.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#communicate-effectively"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Communicate effectively</span>

<span data-as="p">The way you communicate with Claude Code significantly
impacts the quality of results.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#ask-codebase-questions"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Ask codebase questions</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Ask Claude questions you’d ask a senior
engineer.</span>

</div>

</div>

<span data-as="p">When onboarding to a new codebase, use Claude Code for
learning and exploration. You can ask Claude the same sorts of questions
you would ask another engineer:</span>

- How does logging work?
- How do I make a new API endpoint?
- What does `async move { ... }` do on line 134 of `foo.rs`?
- What edge cases does `CustomerOnboardingFlowImpl` handle?
- Why does this code call `foo()` instead of `bar()` on line 333?

<span data-as="p">Using Claude Code this way is an effective onboarding
workflow, improving ramp-up time and reducing load on other engineers.
No special prompting required: ask questions directly.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#let-claude-interview-you"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Let Claude interview you</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">For larger features, have Claude interview you first.
Start with a minimal prompt and ask Claude to interview you using the
`AskUserQuestion` tool.</span>

</div>

</div>

<span data-as="p">Claude asks about things you might not have considered
yet, including technical implementation, UI/UX, edge cases, and
tradeoffs.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="6" language="text">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Once the spec is complete, start a fresh session to
execute it. The new session has clean context focused entirely on
implementation, and you have a written spec to reference.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#manage-your-session"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Manage your session</span>

<span data-as="p">Conversations are persistent and reversible. Use this
to your advantage!</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#course-correct-early-and-often"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Course-correct early and often</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Correct Claude as soon as you notice it going off
track.</span>

</div>

</div>

<span data-as="p">The best results come from tight feedback loops.
Though Claude occasionally solves problems perfectly on the first
attempt, correcting it quickly generally produces better solutions
faster.</span>

- **`Esc`**: stop Claude mid-action with the `Esc` key. Context is
  preserved, so you can redirect.
- **`Esc + Esc` or `/rewind`**: press `Esc` twice or run `/rewind` to
  open the rewind menu and restore previous conversation and code state,
  or summarize from a selected message.
- **`"Undo that"`**: have Claude revert its changes.
- **`/clear`**: reset context between unrelated tasks. Long sessions
  with irrelevant context can reduce performance.

<span data-as="p">If you’ve corrected Claude more than twice on the same
issue in one session, the context is cluttered with failed approaches.
Run `/clear` and start fresh with a more specific prompt that
incorporates what you learned. A clean session with a better prompt
almost always outperforms a long session with accumulated
corrections.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#manage-context-aggressively"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Manage context aggressively</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Run `/clear` between unrelated tasks to reset
context.</span>

</div>

</div>

<span data-as="p">Claude Code automatically compacts conversation
history when you approach context limits, which preserves important code
and decisions while freeing space.</span> <span data-as="p">During long
sessions, Claude’s context window can fill with irrelevant conversation,
file contents, and commands. This can reduce performance and sometimes
distract Claude.</span>

- Use `/clear` frequently between tasks to reset the context window
  entirely
- When auto compaction triggers, Claude summarizes what matters most,
  including code patterns, file states, and key decisions
- For more control, run `/compact <instructions>`, like
  `/compact Focus on the API changes`
- To compact only part of the conversation, use `Esc + Esc` or
  `/rewind`, select a message checkpoint, and choose **Summarize from
  here**. This condenses messages from that point forward while keeping
  earlier context intact.
- Customize compaction behavior in CLAUDE.md with instructions like
  `"When compacting, always preserve the full list of modified files and any test commands"`
  to ensure critical context survives summarization
- For quick questions that don’t need to stay in context, use <a
  href="https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw"
  class="link"><code>/btw</code></a>. The answer appears in a
  dismissible overlay and never enters conversation history, so you can
  check a detail without growing context.

### 

<div class="absolute" tabindex="-1">

<a
href="claude-code-best-practices.html#use-subagents-for-investigation"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Use subagents for investigation</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Delegate research with
`"use subagents to investigate X"`. They explore in a separate context,
keeping your main conversation clean for implementation.</span>

</div>

</div>

<span data-as="p">Since context is your fundamental constraint,
subagents are one of the most powerful tools available. When Claude
researches a codebase it reads lots of files, all of which consume your
context. Subagents run in separate context windows and report back
summaries:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="3" language="text">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">The subagent explores the codebase, reads relevant
files, and reports back with findings, all without cluttering your main
conversation.</span> <span data-as="p">You can also use subagents for
verification after Claude implements something:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="2" language="text">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
use a subagent to review this code for edge cases
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#rewind-with-checkpoints"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Rewind with checkpoints</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Every action Claude makes creates a checkpoint. You
can restore conversation, code, or both to any previous
checkpoint.</span>

</div>

</div>

<span data-as="p">Claude automatically checkpoints before changes.
Double-tap `Escape` or run `/rewind` to open the rewind menu. You can
restore conversation only, restore code only, restore both, or summarize
from a selected message. See
<a href="https://code.claude.com/docs/en/checkpointing"
class="link">Checkpointing</a> for details.</span>
<span data-as="p">Instead of carefully planning every move, you can tell
Claude to try something risky. If it doesn’t work, rewind and try a
different approach. Checkpoints persist across sessions, so you can
close your terminal and still rewind later.</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-yellow-200 bg-yellow-50 dark:border-yellow-900 dark:bg-yellow-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="warning">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1ub25lIHNpemUtNSB0ZXh0LXllbGxvdy04MDAgZGFyazp0ZXh0LXllbGxvdy0zMDAiIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgYXJpYS1sYWJlbD0iV2FybmluZyI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgOXYybTAgNGguMDFtLTYuOTM4IDRoMTMuODU2YzEuNTQgMCAyLjUwMi0xLjY2NyAxLjczMi0zTDEzLjczMiA0Yy0uNzctMS4zMzMtMi42OTQtMS4zMzMtMy40NjQgMEwzLjM0IDE2Yy0uNzcgMS4zMzMuMTkyIDMgMS43MzIgM3oiIC8+PC9zdmc+"
class="flex-none size-5 text-yellow-800 dark:text-yellow-300" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-yellow-800 dark:text-yellow-300"
component-part="callout-content">

<span data-as="p">Checkpoints only track changes made *by Claude*, not
external processes. This isn’t a replacement for git.</span>

</div>

</div>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#resume-conversations"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Resume conversations</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Run `claude --continue` to pick up where you left off,
or `--resume` to choose from recent sessions.</span>

</div>

</div>

<span data-as="p">Claude Code saves conversations locally. When a task
spans multiple sessions, you don’t have to re-explain the
context:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="2" language="shellscript">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
claude --continue    # Resume the most recent conversation
claude --resume      # Select from recent conversations
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Use `/rename` to give sessions descriptive names like
`"oauth-migration"` or `"debugging-memory-leak"` so you can find them
later. Treat sessions like branches: different workstreams can have
separate, persistent contexts.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#automate-and-scale"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Automate and scale</span>

<span data-as="p">Once you’re effective with one Claude, multiply your
output with parallel sessions, non-interactive mode, and fan-out
patterns.</span> <span data-as="p">Everything so far assumes one human,
one Claude, and one conversation. But Claude Code scales horizontally.
The techniques in this section show how you can get more done.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#run-non-interactive-mode"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Run non-interactive mode</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Use `claude -p "prompt"` in CI, pre-commit hooks, or
scripts. Add `--output-format stream-json` for streaming JSON
output.</span>

</div>

</div>

<span data-as="p">With `claude -p "your prompt"`, you can run Claude
non-interactively, without a session. Non-interactive mode is how you
integrate Claude into CI pipelines, pre-commit hooks, or any automated
workflow. The output formats let you parse results programmatically:
plain text, JSON, or streaming JSON.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="8" language="shellscript">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#run-multiple-claude-sessions"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Run multiple Claude sessions</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Run multiple Claude sessions in parallel to speed up
development, run isolated experiments, or start complex
workflows.</span>

</div>

</div>

<span data-as="p">There are three main ways to run parallel
sessions:</span>

- <a
  href="https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions"
  class="link">Claude Code desktop app</a>: Manage multiple local
  sessions visually. Each session gets its own isolated worktree.
- <a href="https://code.claude.com/docs/en/claude-code-on-the-web"
  class="link">Claude Code on the web</a>: Run on Anthropic’s secure
  cloud infrastructure in isolated VMs.
- <a href="https://code.claude.com/docs/en/agent-teams" class="link">Agent
  teams</a>: Automated coordination of multiple sessions with shared
  tasks, messaging, and a team lead.

<span data-as="p">Beyond parallelizing work, multiple sessions enable
quality-focused workflows. A fresh context improves code review since
Claude won’t be biased toward code it just wrote.</span>
<span data-as="p">For example, use a Writer/Reviewer pattern:</span>

<div class="[--page-padding:20px] overflow-x-auto flex w-[calc(100%+(var(--page-padding)*2))] my-[1em] py-[1em] -mx-[var(--page-padding)] max-w-none [contain:inline-size]"
table-wrapper="true">

<div class="px-[var(--page-padding)] grow max-w-none table">

| Session A (Writer) | Session B (Reviewer) |
|----|----|
| `Implement a rate limiter for our API endpoints` |  |
|  | `Review the rate limiter implementation in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions, and consistency with our existing middleware patterns.` |
| `Here's the review feedback: [Session B output]. Address these issues.` |  |

</div>

</div>

<span data-as="p">You can do something similar with tests: have one
Claude write tests, then another write code to pass them.</span>

### 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#fan-out-across-files"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Fan out across files</span>

<div class="callout my-4 px-5 py-4 overflow-hidden rounded-2xl flex gap-3 border border-green-200 bg-green-50 dark:border-green-900 dark:bg-green-600/20 [&_[data-component-part='callout-icon']]:mt-px"
callout-type="tip">

<div class="mt-0.5 w-4" component-part="callout-icon">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTQiIHZpZXdib3g9IjAgMCAxMSAxNCIgZmlsbD0iY3VycmVudENvbG9yIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJ0ZXh0LWdyZWVuLTgwMCBkYXJrOnRleHQtZ3JlZW4tMzAwIHctMy41IGgtYXV0byIgYXJpYS1sYWJlbD0iVGlwIj48cGF0aCBkPSJNMy4xMjc5NCAxMi40MjMyQzMuMTI3OTQgMTIuNTk1NCAzLjE3NzYgMTIuNzYzNCAzLjI3MjQ0IDEyLjkwN0wzLjc0MTE0IDEzLjYwOTVDMy44ODQ3MSAxMy44MjQ4IDQuMjEwNjcgMTQgNC40Njk2NCAxNEg2LjE1NjA2QzYuNDE0MTUgMTQgNi43NDAxNyAxMy44MjUgNi44ODM3MyAxMy42MDk1TDcuMzUwOCAxMi45MDczQzcuNDMxMTQgMTIuNzg1OSA3LjQ5NzA1IDEyLjU2OSA3LjQ5NzA1IDEyLjQyMzJMNy41MDA1NSAxMS4zNTEzSDMuMTI1MjFMMy4xMjc5NCAxMi40MjMyWk01LjMxMjg4IDBDMi41MjQxNCAwLjAwODc1ODg5IDAuNSAyLjI2ODg5IDAuNSA0Ljc4ODI2QzAuNSA2LjAwMTg4IDAuOTQ5NTY2IDcuMTA4MjkgMS42OTExOSA3Ljk1NDkyQzIuMTQzMjEgOC40NzAxMSAyLjg0OTAxIDkuNTQ3MjcgMy4xMTkxOSAxMC40NTU3QzMuMTIwMDUgMTAuNDYyNSAzLjEyMTc1IDEwLjQ2OTggMy4xMjI2MSAxMC40NzcxSDcuNTAzNDJDNy41MDQyNyAxMC40Njk4IDcuNTA1OTggMTAuNDYzIDcuNTA2ODQgMTAuNDU1N0M3Ljc3Njg4IDkuNTQ3MjcgOC40ODI4MSA4LjQ3MDExIDguOTM0ODQgNy45NTQ5MkM5LjY3NzI4IDcuMTMxODEgMTAuMTI1OCA2LjAyNzAzIDEwLjEyNTggNC43ODgyNkMxMC4xMjU4IDIuMTU0ODYgNy45NzA5IDAuMDAwMTA2NjQ5IDUuMzEyODggMFpNNy45NDkwMiA3LjExMjY3QzcuNTIwNzggNy42MDA3OSA2Ljk5MDgyIDguMzc4NzggNi42MDc3IDkuMTg3OTRINC4wMjA1MUMzLjYzNzM5IDguMzc4NzggMy4xMDc0MyA3LjYwMDc5IDIuNjc5NDcgNy4xMTI5NEMyLjExOTk3IDYuNDc1NTEgMS44MTI2IDUuNjM1OTkgMS44MTI2IDQuNzg4MjZDMS44MTI2IDMuMDk4MjkgMy4xMjc5NCAxLjMxOTQ0IDUuMjg4MjcgMS4zMTI2QzcuMjQzNSAxLjMxMjYgOC44MTMxNSAyLjg4MjI2IDguODEzMTUgNC43ODgyNkM4LjgxMzE1IDUuNjM1OTkgOC41MDY4OCA2LjQ3NTUxIDcuOTQ5MDIgNy4xMTI2N1pNNC44NzUzNCAyLjE4NzY3QzMuNjY5MzkgMi4xODc2NyAyLjY4NzY3IDMuMTY5MzkgMi42ODc2NyA0LjM3NTM0QzIuNjg3NjcgNC42MTcxOSAyLjg4MzM2IDQuODEyODggMy4xMjUyMSA0LjgxMjg4QzMuMzY3MDUgNC44MTI4OCAzLjU2Mjc0IDQuNjE1OTkgMy41NjI3NCA0LjM3NTM0QzMuNTYyNzQgMy42NTE1IDQuMTUxNSAzLjA2Mjc0IDQuODc1MzQgMy4wNjI3NEM1LjExNzE5IDMuMDYyNzQgNS4zMTI4OCAyLjg2NzI3IDUuMzEyODggMi42MjU0OEM1LjMxMjg4IDIuMzgzNjkgNS4xMTU5OSAyLjE4NzY3IDQuODc1MzQgMi4xODc2N1oiIC8+PC9zdmc+"
class="text-green-800 dark:text-green-300 w-3.5 h-auto" />

</div>

<div class="text-sm prose dark:prose-invert min-w-0 w-full [&_kbd]:bg-background-light dark:[&_kbd]:bg-background-dark [&_code]:!text-current [&_kbd]:!text-current [&_a]:!text-current [&_a]:border-current [&_strong]:!text-current text-green-800 dark:text-green-300"
component-part="callout-content">

<span data-as="p">Loop through tasks calling `claude -p` for each. Use
`--allowedTools` to scope permissions for batch operations.</span>

</div>

</div>

<span data-as="p">For large migrations or analyses, you can distribute
work across many parallel Claude invocations:</span>

<div class="steps ml-3.5 mt-10 mb-6" role="list">

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-gray-200/70 dark:bg-white/10"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

1

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Generate a task list

<div class="prose dark:prose-invert" component-part="step-content">

<span data-as="p">Have Claude list all files that need migrating (e.g.,
`list all 2,000 Python files that need migrating`)</span>

</div>

</div>

</div>

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-gray-200/70 dark:bg-white/10"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

2

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Write a script to loop through the list

<div class="prose dark:prose-invert" component-part="step-content">

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="4" language="shellscript">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

</div>

</div>

</div>

<div class="step group/step step-container relative flex items-start pb-5"
role="listitem">

<div class="absolute w-px h-[calc(100%-2.75rem)] top-[2.75rem] bg-transparent bg-gradient-to-b from-gray-200 dark:from-white/10 via-80% to-transparent group-has-[[data-component-part="step-content"]:empty]/step:hidden"
component-part="step-line" contenteditable="false">

</div>

<div class="absolute ml-[-13px] py-2" component-part="step-number"
contenteditable="false">

<div class="relative size-7 shrink-0 rounded-full bg-gray-50 dark:bg-white/10 text-xs text-gray-900 dark:text-gray-50 font-semibold flex items-center justify-center">

<div>

3

</div>

<div class="absolute" component-part="step-number-anchor-link">

<a href="claude-code-best-practices.html#"
class="flex items-center opacity-0 border-0"
aria-label="Navigate to header"></a>

<div class="w-6 h-6 flex items-center justify-center">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

</div>

</div>

<div class="w-full overflow-hidden pl-8 pr-px">

Test on a few files, then run at scale

<div class="prose dark:prose-invert" component-part="step-content">

<span data-as="p">Refine your prompt based on what goes wrong with the
first 2-3 files, then run on the full set. The `--allowedTools` flag
restricts what Claude can do, which matters when you’re running
unattended.</span>

</div>

</div>

</div>

</div>

<span data-as="p">You can also integrate Claude into existing
data/processing pipelines:</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="1" language="shellscript">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
claude -p "<your prompt>" --output-format json | your_command
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">Use `--verbose` for debugging during development, and
turn it off in production.</span>

### 

<div class="absolute" tabindex="-1">

<a
href="claude-code-best-practices.html#run-autonomously-with-auto-mode"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Run autonomously with auto mode</span>

<span data-as="p">For uninterrupted execution with background safety
checks, use <a
href="https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode"
class="link">auto mode</a>. A classifier model reviews commands before
they run, blocking scope escalation, unknown infrastructure, and
hostile-content-driven actions while letting routine work proceed
without prompts.</span>

<div class="code-block mt-5 mb-8 not-prose rounded-2xl relative group min-w-0 print:print-color-exact text-gray-950 dark:text-gray-50 codeblock-light border border-gray-950/10 dark:border-white/10 dark:twoslash-dark bg-transparent dark:bg-transparent"
numberoflines="1" language="shellscript">

<div class="absolute top-3 right-4 flex items-center gap-1.5 print:hidden"
floating-buttons="true">

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJ3LTQgaC00IHRleHQtZ3JheS00MDAgZ3JvdXAtaG92ZXIvY29kZS1zbmlwcGV0LWZlZWRiYWNrLWJ1dHRvbjp0ZXh0LWdyYXktNTAwIGRhcms6dGV4dC13aGl0ZS80MCBkYXJrOmdyb3VwLWhvdmVyL2NvZGUtc25pcHBldC1mZWVkYmFjay1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTEyIDE2aC4wMSIgLz48cGF0aCBkPSJNMTIgOHY0IiAvPjxwYXRoIGQ9Ik0xNS4zMTIgMmEyIDIgMCAwIDEgMS40MTQuNTg2bDQuNjg4IDQuNjg4QTIgMiAwIDAgMSAyMiA4LjY4OHY2LjYyNGEyIDIgMCAwIDEtLjU4NiAxLjQxNGwtNC42ODggNC42ODhhMiAyIDAgMCAxLTEuNDE0LjU4Nkg4LjY4OGEyIDIgMCAwIDEtMS40MTQtLjU4NmwtNC42ODgtNC42ODhBMiAyIDAgMCAxIDIgMTUuMzEyVjguNjg4YTIgMiAwIDAgMSAuNTg2LTEuNDE0bDQuNjg4LTQuNjg4QTIgMiAwIDAgMSA4LjY4OCAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/code-snippet-feedback-button:text-gray-500 dark:text-white/40 dark:group-hover/code-snippet-feedback-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2NvcHktYnV0dG9uOnRleHQtZ3JheS01MDAgZGFyazp0ZXh0LXdoaXRlLzQwIGRhcms6Z3JvdXAtaG92ZXIvY29weS1idXR0b246dGV4dC13aGl0ZS82MCI+PHBhdGggZD0iTTE0LjI1IDUuMjVINy4yNUM2LjE0NTQzIDUuMjUgNS4yNSA2LjE0NTQzIDUuMjUgNy4yNVYxNC4yNUM1LjI1IDE1LjM1NDYgNi4xNDU0MyAxNi4yNSA3LjI1IDE2LjI1SDE0LjI1QzE1LjM1NDYgMTYuMjUgMTYuMjUgMTUuMzU0NiAxNi4yNSAxNC4yNVY3LjI1QzE2LjI1IDYuMTQ1NDMgMTUuMzU0NiA1LjI1IDE0LjI1IDUuMjVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48cGF0aCBkPSJNMi44MDEwMyAxMS45OThMMS43NzIwMyA1LjA3Mzk3QzEuNjEwMDMgMy45ODA5NyAyLjM2NDAzIDIuOTYzOTcgMy40NTYwMyAyLjgwMTk3TDEwLjM4IDEuNzcyOTdDMTEuMzEzIDEuNjMzOTcgMTIuMTkgMi4xNjI5NyAxMi41MjggMy4wMDA5NyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="w-4 h-4 text-gray-400 group-hover/copy-button:text-gray-500 dark:text-white/40 dark:group-hover/copy-button:text-white/60" />

</div>

<div class="z-10 select-none" state="closed">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0idy00IGgtNCB0ZXh0LWdyYXktNDAwIGdyb3VwLWhvdmVyL2Fzay1haS1idXR0b246dGV4dC1ncmF5LTUwMCBkYXJrOnRleHQtd2hpdGUvNDAgZGFyazpncm91cC1ob3Zlci9hc2stYWktYnV0dG9uOnRleHQtd2hpdGUvNjAiPjxwYXRoIGQ9Ik0zLjUxMTY5IDEuNTAwOThMMy45MjA4NyAyLjcyNzU0TDMuOTk5OTcgMi45NjM4N0w1LjQ5OTk3IDMuNDYzODdMNC4yMzgyNSAzLjg4NDc3TDQuMDAwOTUgMy45NjM4N0wzLjkyMTg0IDQuMjAxMTdMMy41MDA5NSA1LjQ2MTkxTDMuNDk5OTcgNS40NjM4N0gzLjQ5ODk5TDIuOTk4OTkgMy45NjM4N0wxLjQ5ODk5IDMuNDYzODdMMi45OTg5OSAyLjk2Mzg3TDMuMDc4MDkgMi43Mjc1NEwzLjQ4NjMgMS41MDA5OEMzLjQ5MDMxIDEuNTAwNDUgMy40OTUyMiAxLjUgMy40OTk5NyAxLjVDMy41MDQxNiAxLjUwMDAyIDMuNTA4MDcgMS41MDA1NCAzLjUxMTY5IDEuNTAwOThaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNOS41IDIuNzVMMTEuNDEyIDcuNTg3TDE2LjI1IDkuNUwxMS40MTIgMTEuNDEzTDkuNSAxNi4yNUw3LjU4NyAxMS40MTNMMi43NSA5LjVMNy41ODcgNy41ODdMOS41IDIuNzVaIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz48L3N2Zz4="
class="w-4 h-4 text-gray-400 group-hover/ask-ai-button:text-gray-500 dark:text-white/40 dark:group-hover/ask-ai-button:text-white/60" />

</div>

</div>

<div class="w-0 min-w-full max-w-full py-3.5 px-4 h-full dark:bg-codeblock relative text-sm leading-6 children:!my-0 children:!shadow-none children:!bg-transparent transition-[height] duration-300 ease-in-out code-block-background [&_*]:ring-0 [&_*]:outline-0 [&_*]:focus:ring-0 [&_*]:focus:outline-0 rounded-2xl bg-white overflow-x-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-black/15 hover:scrollbar-thumb-black/20 active:scrollbar-thumb-black/20 dark:scrollbar-thumb-white/20 dark:hover:scrollbar-thumb-white/25 dark:active:scrollbar-thumb-white/25"
component-part="code-block-root" tabindex="0"
style="font-variant-ligatures:none;height:auto;background-color:#ffffff;--shiki-dark-bg:#0B0C0E">

<div class="font-mono whitespace-pre leading-6">

``` shiki
claude --permission-mode auto -p "fix all lint errors"
```

</div>

</div>

<div class="print:hidden" fade-overlay="true" aria-hidden="true"
style="--fade-color-light:#ffffff;--fade-color-dark:#0B0C0E">

</div>

</div>

<span data-as="p">For non-interactive runs with the `-p` flag, auto mode
aborts if the classifier repeatedly blocks actions, since there is no
user to fall back to. See <a
href="https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back"
class="link">when auto mode falls back</a> for thresholds.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#avoid-common-failure-patterns"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Avoid common failure patterns</span>

<span data-as="p">These are common mistakes. Recognizing them early
saves time:</span>

- **The kitchen sink session.** You start with one task, then ask Claude
  something unrelated, then go back to the first task. Context is full
  of irrelevant information.

  > <span data-as="p">**Fix**: `/clear` between unrelated tasks.</span>

- **Correcting over and over.** Claude does something wrong, you correct
  it, it’s still wrong, you correct again. Context is polluted with
  failed approaches.

  > <span data-as="p">**Fix**: After two failed corrections, `/clear`
  > and write a better initial prompt incorporating what you
  > learned.</span>

- **The over-specified CLAUDE.md.** If your CLAUDE.md is too long,
  Claude ignores half of it because important rules get lost in the
  noise.

  > <span data-as="p">**Fix**: Ruthlessly prune. If Claude already does
  > something correctly without the instruction, delete it or convert it
  > to a hook.</span>

- **The trust-then-verify gap.** Claude produces a plausible-looking
  implementation that doesn’t handle edge cases.

  > <span data-as="p">**Fix**: Always provide verification (tests,
  > scripts, screenshots). If you can’t verify it, don’t ship it.</span>

- **The infinite exploration.** You ask Claude to “investigate”
  something without scoping it. Claude reads hundreds of files, filling
  the context.

  > <span data-as="p">**Fix**: Scope investigations narrowly or use
  > subagents so the exploration doesn’t consume your main
  > context.</span>

------------------------------------------------------------------------

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#develop-your-intuition"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Develop your intuition</span>

<span data-as="p">The patterns in this guide aren’t set in stone.
They’re starting points that work well in general, but might not be
optimal for every situation.</span> <span data-as="p">Sometimes you
*should* let context accumulate because you’re deep in one complex
problem and the history is valuable. Sometimes you should skip planning
and let Claude figure it out because the task is exploratory. Sometimes
a vague prompt is exactly right because you want to see how Claude
interprets the problem before constraining it.</span>
<span data-as="p">Pay attention to what works. When Claude produces
great output, notice what you did: the prompt structure, the context you
provided, the mode you were in. When Claude struggles, ask why. Was the
context too noisy? The prompt too vague? The task too big for one
pass?</span> <span data-as="p">Over time, you’ll develop intuition that
no guide can capture. You’ll know when to be specific and when to be
open-ended, when to plan and when to explore, when to clear context and
when to let it accumulate.</span>

## 

<div class="absolute" tabindex="-1">

<a href="claude-code-best-practices.html#related-resources"
class="-ml-10 flex items-center opacity-0 border-0 group-hover:opacity-100 focus:opacity-100 focus:outline-0 group/link"
aria-label="Navigate to header">​</a>

<div class="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover:brightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20 group-focus/link:border-2 group-focus/link:border-primary dark:group-focus/link:border-primary-light">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9ImdyYXkiIGhlaWdodD0iMTJweCIgdmlld2JveD0iMCAwIDU3NiA1MTIiPjxwYXRoIGQ9Ik0wIDI1NkMwIDE2Ny42IDcxLjYgOTYgMTYwIDk2aDcyYzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDE2MEM5OC4xIDE0NCA0OCAxOTQuMSA0OCAyNTZzNTAuMSAxMTIgMTEyIDExMmg3MmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNjBDNzEuNiA0MTYgMCAzNDQuNCAwIDI1NnptNTc2IDBjMCA4OC40LTcxLjYgMTYwLTE2MCAxNjBIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0aDcyYzYxLjkgMCAxMTItNTAuMSAxMTItMTEycy01MC4xLTExMi0xMTItMTEySDM0NGMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNGg3MmM4OC40IDAgMTYwIDcxLjYgMTYwIDE2MHpNMTg0IDIzMkgzOTJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTg0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0eiIgLz48L3N2Zz4=)

</div>

</div>

<span class="cursor-pointer">Related resources</span>

- <a href="https://code.claude.com/docs/en/how-claude-code-works"
  class="link">How Claude Code works</a>: the agentic loop, tools, and
  context management
- <a href="https://code.claude.com/docs/en/features-overview"
  class="link">Extend Claude Code</a>: skills, hooks, MCP, subagents,
  and plugins
- <a href="https://code.claude.com/docs/en/common-workflows"
  class="link">Common workflows</a>: step-by-step recipes for debugging,
  testing, PRs, and more
- <a href="https://code.claude.com/docs/en/memory"
  class="link">CLAUDE.md</a>: store project conventions and persistent
  context

</div>

<div class="feedback-toolbar pb-16 w-full flex flex-col gap-y-8">

<div class="flex flex-row flex-wrap gap-4 items-center justify-between">

Was this page helpful?

<div class="flex flex-wrap flex-grow gap-3 items-center justify-end">

<div class="flex gap-3 items-center">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiBjbGFzcz0iZmlsbC1jdXJyZW50Ij48cGF0aCBkPSJNMTAuMTE4NyAxLjA4NzQxQzguOTI1IDAuNzQ2Nzg5IDcuNjc4MTMgMS40Mzc0MSA3LjMzNzUgMi42MzExNkw3LjE1OTM4IDMuMjU2MTZDNy4wNDM3NSAzLjY2MjQxIDYuODM0MzggNC4wMzc0MSA2LjU1IDQuMzQ5OTFMNC45NDY4OCA2LjExMjQxQzQuNjY4NzUgNi40MTg2NiA0LjY5MDYyIDYuODkzNjYgNC45OTY4NyA3LjE3MTc5QzUuMzAzMTIgNy40NDk5MSA1Ljc3ODEzIDcuNDI4MDQgNi4wNTYyNSA3LjEyMTc5TDcuNjU5MzggNS4zNTkyOUM4LjEgNC44NzQ5MSA4LjQyMTg4IDQuMjk2NzkgOC42IDMuNjY4NjZMOC43NzgxMiAzLjA0MzY2QzguODkwNjIgMi42NDY3OSA5LjMwNjI1IDIuNDE1NTQgOS43MDYyNSAyLjUyODA0QzEwLjEwNjMgMi42NDA1NCAxMC4zMzQ0IDMuMDU2MTYgMTAuMjIxOSAzLjQ1NjE2TDEwLjA0MzcgNC4wODExNkM5Ljg2NTYyIDQuNzAzMDQgOS41ODQzNyA1LjI5MDU0IDkuMjEyNSA1LjgxNTU0QzkuMDUgNi4wNDM2NiA5LjAzMTI1IDYuMzQzNjYgOS4xNTkzOCA2LjU5MzY2QzkuMjg3NSA2Ljg0MzY2IDkuNTQzNzUgNi45OTk5MSA5LjgyNSA2Ljk5OTkxSDE0QzE0LjI3NSA2Ljk5OTkxIDE0LjUgNy4yMjQ5MSAxNC41IDcuNDk5OTFDMTQuNSA3LjcxMjQxIDE0LjM2NTYgNy44OTY3OSAxNC4xNzUgNy45Njg2NkMxMy45NDM4IDguMDU2MTYgMTMuNzY4OCA4LjI0OTkyIDEzLjcwOTQgOC40OTA1NEMxMy42NSA4LjczMTE3IDEzLjcxMjUgOC45ODQyOSAxMy44NzUgOS4xNjg2NkMxMy45NTMxIDkuMjU2MTYgMTQgOS4zNzE3OSAxNCA5LjQ5OTkxQzE0IDkuNzQzNjYgMTMuODI1IDkuOTQ2NzkgMTMuNTkzOCA5Ljk5MDU0QzEzLjMzNzUgMTAuMDQwNSAxMy4xMjE5IDEwLjIxODcgMTMuMDMxMiAxMC40NjI0QzEyLjk0MDYgMTAuNzA2MiAxMi45ODEzIDEwLjk4NDMgMTMuMTQzOCAxMS4xOTA1QzEzLjIwOTQgMTEuMjc0OSAxMy4yNSAxMS4zODEyIDEzLjI1IDExLjQ5OTlDMTMuMjUgMTEuNzA5MyAxMy4xMTg3IDExLjg5MzcgMTIuOTMxMiAxMS45NjU1QzEyLjU3MTkgMTIuMTA2MiAxMi4zNzgxIDEyLjQ5MzcgMTIuNDgxMiAxMi44NjU1QzEyLjQ5MzcgMTIuOTA2MiAxMi41IDEyLjk1MyAxMi41IDEyLjk5OTlDMTIuNSAxMy4yNzQ5IDEyLjI3NSAxMy40OTk5IDEyIDEzLjQ5OTlIOC45NTMxMkM4LjU1OTM3IDEzLjQ5OTkgOC4xNzE4OCAxMy4zODQzIDcuODQzNzUgMTMuMTY1NUw1LjkxNTYzIDExLjg4MTJDNS41NzE4OCAxMS42NDk5IDUuMTA2MjUgMTEuNzQzNyA0Ljg3NSAxMi4wOTA1QzQuNjQzNzUgMTIuNDM3NCA0LjczNzUgMTIuODk5OSA1LjA4NDM3IDEzLjEzMTJMNy4wMTI1IDE0LjQxNTVDNy41ODc1IDE0Ljc5OTkgOC4yNjI1IDE1LjAwMyA4Ljk1MzEyIDE1LjAwM0gxMkMxMy4wODQ0IDE1LjAwMyAxMy45NjU2IDE0LjE0MDUgMTQgMTMuMDY1NUMxNC40NTYzIDEyLjY5OTkgMTQuNzUgMTIuMTM3NCAxNC43NSAxMS41MDNDMTQuNzUgMTEuMzYyNCAxNC43MzQ0IDExLjIyOCAxNC43MDk0IDExLjA5NjhDMTUuMTkwNiAxMC43MzEyIDE1LjUgMTAuMTUzIDE1LjUgOS41MDMwNEMxNS41IDkuMjk5OTEgMTUuNDY4OCA5LjEwMzA0IDE1LjQxMjUgOC45MTg2NkMxNS43NzUgOC41NTMwNCAxNiA4LjA1MzA0IDE2IDcuNDk5OTFDMTYgNi4zOTY3OSAxNS4xMDYzIDUuNDk5OTEgMTQgNS40OTk5MUgxMS4xMTU2QzExLjI2MjUgNS4xNzQ5MSAxMS4zODc1IDQuODM3NDEgMTEuNDg0NCA0LjQ5MzY2TDExLjY2MjUgMy44Njg2NkMxMi4wMDMxIDIuNjc0OTEgMTEuMzEyNSAxLjQyODA0IDEwLjExODcgMS4wODc0MVpNMSA1Ljk5OTkxQzAuNDQ2ODc1IDUuOTk5OTEgMCA2LjQ0Njc5IDAgNi45OTk5MVYxMy45OTk5QzAgMTQuNTUzIDAuNDQ2ODc1IDE0Ljk5OTkgMSAxNC45OTk5SDNDMy41NTMxMyAxNC45OTk5IDQgMTQuNTUzIDQgMTMuOTk5OVY2Ljk5OTkxQzQgNi40NDY3OSAzLjU1MzEzIDUuOTk5OTEgMyA1Ljk5OTkxSDFaIiAvPjwvc3ZnPg=="
class="fill-current" /><span class="small">Yes</span>

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiBjbGFzcz0iZmlsbC1jdXJyZW50Ij48cGF0aCBkPSJNMTAuMTE4NyAxNC45MTI0QzguOTI1IDE1LjI1MyA3LjY3ODEzIDE0LjU2MjQgNy4zMzc1IDEzLjM2ODdMNy4xNTkzOCAxMi43NDM3QzcuMDQzNzUgMTIuMzM3NCA2LjgzNDM4IDExLjk2MjQgNi41NSAxMS42NDk5TDQuOTQ2ODggOS44ODc0QzQuNjY4NzUgOS41ODExNSA0LjY5MDYyIDkuMTA2MTUgNC45OTY4NyA4LjgyODAzQzUuMzAzMTIgOC41NDk5IDUuNzc4MTMgOC41NzE3OCA2LjA1NjI1IDguODc4MDNMNy42NTkzOCAxMC42NDA1QzguMSAxMS4xMjQ5IDguNDIxODggMTEuNzAzIDguNiAxMi4zMzEyTDguNzc4MTIgMTIuOTU2MkM4Ljg5MDYyIDEzLjM1MyA5LjMwNjI1IDEzLjU4NDMgOS43MDYyNSAxMy40NzE4QzEwLjEwNjMgMTMuMzU5MyAxMC4zMzQ0IDEyLjk0MzcgMTAuMjIxOSAxMi41NDM3TDEwLjA0MzcgMTEuOTE4N0M5Ljg2NTYyIDExLjI5NjggOS41ODQzNyAxMC43MDkzIDkuMjEyNSAxMC4xODQzQzkuMDUgOS45NTYxNSA5LjAzMTI1IDkuNjU2MTUgOS4xNTkzOCA5LjQwNjE1QzkuMjg3NSA5LjE1NjE1IDkuNTQzNzUgOC45OTk5IDkuODI1IDguOTk5OUgxNEMxNC4yNzUgOC45OTk5IDE0LjUgOC43NzQ5IDE0LjUgOC40OTk5QzE0LjUgOC4yODc0IDE0LjM2NTYgOC4xMDMwMyAxNC4xNzUgOC4wMzExNUMxMy45NDM4IDcuOTQzNjUgMTMuNzY4OCA3Ljc0OTkgMTMuNzA5NCA3LjUwOTI4QzEzLjY1IDcuMjY4NjUgMTMuNzEyNSA3LjAxNTUzIDEzLjg3NSA2LjgzMTE1QzEzLjk1MzEgNi43NDM2NSAxNCA2LjYyODAzIDE0IDYuNDk5OUMxNCA2LjI1NjE1IDEzLjgyNSA2LjA1MzAzIDEzLjU5MzggNi4wMDkyOEMxMy4zMzc1IDUuOTU5MjggMTMuMTIxOSA1Ljc4MTE1IDEzLjAzMTIgNS41MzQyOEMxMi45NDA2IDUuMjg3NCAxMi45ODEzIDUuMDEyNCAxMy4xNDM4IDQuODA2MTVDMTMuMjA5NCA0LjcyMTc4IDEzLjI1IDQuNjE1NTMgMTMuMjUgNC40OTY3OEMxMy4yNSA0LjI4NzQgMTMuMTE4NyA0LjEwMzAzIDEyLjkzMTIgNC4wMzExNUMxMi41NzE5IDMuODkwNTMgMTIuMzc4MSAzLjUwMzAzIDEyLjQ4MTIgMy4xMzExNUMxMi40OTM3IDMuMDkwNTMgMTIuNSAzLjA0MzY1IDEyLjUgMi45OTY3OEMxMi41IDIuNzIxNzggMTIuMjc1IDIuNDk2NzggMTIgMi40OTY3OEg4Ljk1MzEyQzguNTU5MzcgMi40OTY3OCA4LjE3MTg4IDIuNjEyNCA3Ljg0Mzc1IDIuODMxMTVMNS45MTU2MyA0LjExNTUzQzUuNTcxODggNC4zNDY3OCA1LjEwNjI1IDQuMjUzMDMgNC44NzUgMy45MDYxNUM0LjY0Mzc1IDMuNTU5MjggNC43Mzc1IDMuMDk2NzggNS4wODQzNyAyLjg2NTUzTDcuMDEyNSAxLjU4MTE1QzcuNTg3NSAxLjE5Njc4IDguMjYyNSAwLjk5MzY1MiA4Ljk1MzEyIDAuOTkzNjUySDEyQzEzLjA4NDQgMC45OTM2NTIgMTMuOTY1NiAxLjg1NjE1IDE0IDIuOTMxMTVDMTQuNDU2MyAzLjI5Njc4IDE0Ljc1IDMuODU5MjggMTQuNzUgNC40OTM2NUMxNC43NSA0LjYzNDI4IDE0LjczNDQgNC43Njg2NSAxNC43MDk0IDQuODk5OUMxNS4xOTA2IDUuMjY1NTMgMTUuNSA1Ljg0MzY1IDE1LjUgNi40OTM2NUMxNS41IDYuNjk2NzggMTUuNDY4OCA2Ljg5MzY1IDE1LjQxMjUgNy4wNzgwM0MxNS43NzUgNy40NDY3OCAxNiA3Ljk0Njc4IDE2IDguNDk5OUMxNiA5LjYwMzAzIDE1LjEwNjMgMTAuNDk5OSAxNCAxMC40OTk5SDExLjExNTZDMTEuMjYyNSAxMC44MjQ5IDExLjM4NzUgMTEuMTYyNCAxMS40ODQ0IDExLjUwNjJMMTEuNjYyNSAxMi4xMzEyQzEyLjAwMzEgMTMuMzI0OSAxMS4zMTI1IDE0LjU3MTggMTAuMTE4NyAxNC45MTI0Wk0xIDExLjk5OTlDMC40NDY4NzUgMTEuOTk5OSAwIDExLjU1MyAwIDEwLjk5OTlWMy45OTk5QzAgMy40NDY3OCAwLjQ0Njg3NSAyLjk5OTkgMSAyLjk5OTlIM0MzLjU1MzEzIDIuOTk5OSA0IDMuNDQ2NzggNCAzLjk5OTlWMTAuOTk5OUM0IDExLjU1MyAzLjU1MzEzIDExLjk5OTkgMyAxMS45OTk5SDFaIiAvPjwvc3ZnPg=="
class="fill-current" /><span class="small">No</span>

</div>

<div class="flex gap-3">

</div>

</div>

</div>

</div>

<div id="pagination"
class="px-0.5 flex items-center text-sm font-semibold text-gray-700 dark:text-gray-200">

<a href="https://code.claude.com/docs/en/common-workflows"
class="flex items-center space-x-3 group"><img
src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMyA2IiBjbGFzcz0iaC0xLjUgc3Ryb2tlLWdyYXktNDAwIG92ZXJmbG93LXZpc2libGUgZ3JvdXAtaG92ZXI6c3Ryb2tlLWdyYXktNjAwIGRhcms6Z3JvdXAtaG92ZXI6c3Ryb2tlLWdyYXktMzAwIj48cGF0aCBkPSJNMyAwTDAgM0wzIDYiIGZpbGw9Im5vbmUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg=="
class="h-1.5 stroke-gray-400 overflow-visible group-hover:stroke-gray-600 dark:group-hover:stroke-gray-300" /><span
class="group-hover:text-gray-900 dark:group-hover:text-white">Common
workflows</span></a><a href="https://code.claude.com/docs/en/platforms"
class="flex items-center ml-auto space-x-3 group"><span
class="group-hover:text-gray-900 dark:group-hover:text-white">Overview</span><img
src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMyA2IiBjbGFzcz0icm90YXRlLTE4MCBoLTEuNSBzdHJva2UtZ3JheS00MDAgb3ZlcmZsb3ctdmlzaWJsZSBncm91cC1ob3ZlcjpzdHJva2UtZ3JheS02MDAgZGFyazpncm91cC1ob3ZlcjpzdHJva2UtZ3JheS0zMDAiPjxwYXRoIGQ9Ik0zIDBMMCAzTDMgNiIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="rotate-180 h-1.5 stroke-gray-400 overflow-visible group-hover:stroke-gray-600 dark:group-hover:stroke-gray-300" /></a>

</div>

<div class="left-0 right-0 sticky bottom-0 w-full overflow-hidden z-20 pointer-events-none print:hidden">

<div class="chat-assistant-floating-input w-full group/assistant-bar relative before:content-[""] before:absolute before:left-0 before:right-0 before:top-1/2 before:h-[200px] before:bg-background-light before:dark:bg-background-dark translate-y-[100px] opacity-0">

<div class="relative pb-4 sm:pb-6">

<div class="flex flex-col w-full rounded-2xl pointer-events-auto bg-background-light/90 dark:bg-background-dark/90 backdrop-blur-xl border border-gray-200 dark:border-white/30 focus-within:border-primary dark:focus-within:border-primary-light transition-colors">

<div class="relative flex items-end">

<span class="absolute right-11 bottom-3 text-xs font-medium text-gray-400 dark:text-gray-500 select-none pointer-events-none peer-focus/input:hidden hidden sm:inline">⌘I</span>

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWFycm93LXVwIHRleHQtd2hpdGUgZGFyazp0ZXh0LXdoaXRlIHNpemUtMy41Ij48cGF0aCBkPSJtNSAxMiA3LTcgNyA3IiAvPjxwYXRoIGQ9Ik0xMiAxOVY1IiAvPjwvc3ZnPg=="
class="lucide lucide-arrow-up text-white dark:text-white size-3.5" />

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="flex w-full flex-col gap-12 justify-between px-8 py-16 md:py-20 lg:py-28 max-w-[984px] z-20">

<div class="flex flex-col md:flex-row gap-8 justify-between min-h-[76px]">

<div class="flex md:flex-col justify-between items-center md:items-start min-w-16 md:min-w-20 lg:min-w-48 md:gap-y-24">

<a href="https://code.claude.com/docs/en/overview" class="select-none"
data-state="closed" data-slot="context-menu-trigger"
style="-webkit-touch-callout:none"><span class="sr-only">Claude Code
Docs home page</span><img
src="https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&amp;auto=format&amp;n=c5r9_6tjPMzFdDDT&amp;q=85&amp;s=78fd01ff4f4340295a4f66e2ea54903c"
class="nav-logo w-auto relative object-contain shrink-0 block dark:hidden max-w-48 h-[26px]"
alt="light logo" /><img
src="https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&amp;auto=format&amp;n=c5r9_6tjPMzFdDDT&amp;q=85&amp;s=1298a0c3b3a1da603b190d0de0e31712"
class="nav-logo w-auto relative object-contain shrink-0 hidden dark:block max-w-48 h-[26px]"
alt="dark logo" /></a>

<div class="gap-4 min-w-[140px] max-w-[492px] flex-wrap h-fit flex justify-end md:justify-start">

<a href="https://x.com/AnthropicAI" class="h-fit" target="_blank"><span
class="sr-only">x</span><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBiZy1ncmF5LTUwMCBkYXJrOmJnLWdyYXktNjAwIGhvdmVyOmJnLWdyYXktNjAwIGRhcms6aG92ZXI6YmctZ3JheS01MDAiIHN0eWxlPSItd2Via2l0LW1hc2staW1hZ2U6dXJsKGh0dHBzOi8vZDNnazJjNXhpbTFqZTIuY2xvdWRmcm9udC5uZXQvdjcuMS4wL2JyYW5kcy94LXR3aXR0ZXIuc3ZnKTstd2Via2l0LW1hc2stcmVwZWF0Om5vLXJlcGVhdDstd2Via2l0LW1hc2stcG9zaXRpb246Y2VudGVyO21hc2staW1hZ2U6dXJsKGh0dHBzOi8vZDNnazJjNXhpbTFqZTIuY2xvdWRmcm9udC5uZXQvdjcuMS4wL2JyYW5kcy94LXR3aXR0ZXIuc3ZnKTttYXNrLXJlcGVhdDpuby1yZXBlYXQ7bWFzay1wb3NpdGlvbjpjZW50ZXIiPjwvc3ZnPg=="
class="w-5 h-5 bg-gray-500 dark:bg-gray-600 hover:bg-gray-600 dark:hover:bg-gray-500" /></a><a href="https://www.linkedin.com/company/anthropicresearch"
class="h-fit" target="_blank"><span class="sr-only">linkedin</span><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBiZy1ncmF5LTUwMCBkYXJrOmJnLWdyYXktNjAwIGhvdmVyOmJnLWdyYXktNjAwIGRhcms6aG92ZXI6YmctZ3JheS01MDAiIHN0eWxlPSItd2Via2l0LW1hc2staW1hZ2U6dXJsKGh0dHBzOi8vZDNnazJjNXhpbTFqZTIuY2xvdWRmcm9udC5uZXQvdjcuMS4wL2JyYW5kcy9saW5rZWRpbi5zdmcpOy13ZWJraXQtbWFzay1yZXBlYXQ6bm8tcmVwZWF0Oy13ZWJraXQtbWFzay1wb3NpdGlvbjpjZW50ZXI7bWFzay1pbWFnZTp1cmwoaHR0cHM6Ly9kM2drMmM1eGltMWplMi5jbG91ZGZyb250Lm5ldC92Ny4xLjAvYnJhbmRzL2xpbmtlZGluLnN2Zyk7bWFzay1yZXBlYXQ6bm8tcmVwZWF0O21hc2stcG9zaXRpb246Y2VudGVyIj48L3N2Zz4="
class="w-5 h-5 bg-gray-500 dark:bg-gray-600 hover:bg-gray-600 dark:hover:bg-gray-500" /></a>

</div>

</div>

<div class="flex flex-col sm:grid max-md:!grid-cols-2 gap-8 flex-1"
style="grid-template-columns:repeat(4, minmax(0, 1fr))">

<div class="flex flex-col gap-4 flex-1 whitespace-nowrap w-full md:items-center">

<div class="flex gap-4 flex-col">

Company

<a href="https://www.anthropic.com/company"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Anthropic</a><a href="https://www.anthropic.com/careers"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Careers</a><a href="https://www.anthropic.com/economic-futures"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Economic Futures</a><a href="https://www.anthropic.com/research"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Research</a><a href="https://www.anthropic.com/news"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">News</a><a href="https://trust.anthropic.com/"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Trust center</a><a href="https://www.anthropic.com/transparency"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Transparency</a>

</div>

</div>

<div class="flex flex-col gap-4 flex-1 whitespace-nowrap w-full md:items-center">

<div class="flex gap-4 flex-col">

Help and security

<a href="https://www.anthropic.com/supported-countries"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Availability</a><a href="https://status.anthropic.com/"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Status</a><a href="https://support.claude.com/"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Support center</a>

</div>

</div>

<div class="flex flex-col gap-4 flex-1 whitespace-nowrap w-full md:items-center">

<div class="flex gap-4 flex-col">

Learn

<a href="https://www.anthropic.com/learn"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Courses</a><a href="https://claude.com/partners/mcp"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">MCP connectors</a><a href="https://www.claude.com/customers"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Customer stories</a><a href="../engineering.html"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Engineering blog</a><a href="https://www.anthropic.com/events"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Events</a><a href="https://claude.com/partners/powered-by-claude"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Powered by Claude</a><a href="https://claude.com/partners/services"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Service partners</a><a href="https://claude.com/programs/startups"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Startups program</a>

</div>

</div>

<div class="flex flex-col gap-4 flex-1 whitespace-nowrap w-full md:items-center">

<div class="flex gap-4 flex-col">

Terms and policies

<a href="claude-code-best-practices.html#"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_self" rel="noreferrer">Privacy choices</a><a href="https://www.anthropic.com/legal/privacy"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Privacy policy</a><a href="https://www.anthropic.com/responsible-disclosure-policy"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Disclosure policy</a><a href="https://www.anthropic.com/legal/aup"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Usage policy</a><a href="https://www.anthropic.com/legal/commercial-terms"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Commercial terms</a><a href="https://www.anthropic.com/legal/consumer-terms"
class="text-sm max-w-36 whitespace-normal md:truncate text-gray-950/50 dark:text-white/50 hover:text-gray-950/70 dark:hover:text-white/70"
target="_blank" rel="noreferrer">Consumer terms</a>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="sticky shrink-0 z-[22] bg-background-light dark:bg-background-dark mt-[var(--banner-height,0px)] top-[var(--banner-height,0px)] h-[calc(100vh-var(--banner-height,0px))] max-lg:hidden print:hidden"
style="width:var(--assistant-sheet-width, 0px);overflow:hidden">

<div class="absolute left-0 top-0 bottom-0 w-px z-10 cursor-col-resize after:content-[""] after:absolute after:inset-y-0 after:-inset-x-2 after:select-none bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700">

</div>

<div id="chat-assistant-sheet"
class="flex flex-col overflow-hidden shrink-0 relative h-full bg-background-light dark:bg-background-dark chat-assistant-sheet"
aria-hidden="true">

<div class="w-full flex flex-col flex-1 min-h-0 lg:pt-3">

<div class="chat-assistant-sheet-header flex items-center justify-between pb-3 px-4">

<div class="flex items-center gap-2">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9InNpemUtNSB0ZXh0LXByaW1hcnkgZGFyazp0ZXh0LXByaW1hcnktbGlnaHQiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJNNS42NTc5OSAyLjk5TDQuMzk0OTkgMi41NjlMMy45NzM5OSAxLjMwNkMzLjgzNjk5IDAuODk4IDMuMTYxOTkgMC44OTggMy4wMjQ5OSAxLjMwNkwyLjYwMzk5IDIuNTY5TDEuMzQwOTkgMi45OUMxLjEzNjk5IDMuMDU4IDAuOTk4OTkzIDMuMjQ5IDAuOTk4OTkzIDMuNDY0QzAuOTk4OTkzIDMuNjc5IDEuMTM2OTkgMy44NyAxLjM0MDk5IDMuOTM4TDIuNjAzOTkgNC4zNTlMMy4wMjQ5OSA1LjYyMkMzLjA5Mjk5IDUuODI2IDMuMjg0OTkgNS45NjQgMy40OTk5OSA1Ljk2NEMzLjcxNDk5IDUuOTY0IDMuOTA1OTkgNS44MjYgMy45NzQ5OSA1LjYyMkw0LjM5NTk5IDQuMzU5TDUuNjU4OTkgMy45MzhDNS44NjI5OSAzLjg3IDYuMDAwOTkgMy42NzkgNi4wMDA5OSAzLjQ2NEM2LjAwMDk5IDMuMjQ5IDUuODYxOTkgMy4wNTggNS42NTc5OSAyLjk5WiIgZmlsbD0iY3VycmVudENvbG9yIiBzdHJva2U9Im5vbmUiIC8+PHBhdGggZD0iTTkuNSAyLjc1TDExLjQxMiA3LjU4N0wxNi4yNSA5LjVMMTEuNDEyIDExLjQxM0w5LjUgMTYuMjVMNy41ODcgMTEuNDEzTDIuNzUgOS41TDcuNTg3IDcuNTg3TDkuNSAyLjc1WiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHdpZHRoPSIxLjUiIGxpbmVjYXA9InJvdW5kIiBsaW5lam9pbj0icm91bmQiIC8+PC9zdmc+"
class="size-5 text-primary dark:text-primary-light" /><span class="font-medium text-gray-900 dark:text-gray-100">Assistant</span>

</div>

<div class="flex items-center gap-1">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLW1heGltaXplMiBzaXplLTQgc206c2l6ZS0zLjUgdGV4dC1ncmF5LTUwMCBncm91cC1ob3Zlcjp0ZXh0LWdyYXktNzAwIGRhcms6Z3JvdXAtaG92ZXI6dGV4dC1ncmF5LTMwMCI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg=="
class="lucide lucide-maximize2 size-4 sm:size-3.5 text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-300" />

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXggc2l6ZS1bMjBweF0gc206c2l6ZS00IHRleHQtZ3JheS01MDAgZ3JvdXAtaG92ZXI6dGV4dC1ncmF5LTcwMCBkYXJrOmdyb3VwLWhvdmVyOnRleHQtZ3JheS0zMDAiPjxwYXRoIGQ9Ik0xOCA2IDYgMTgiIC8+PHBhdGggZD0ibTYgNiAxMiAxMiIgLz48L3N2Zz4="
class="lucide lucide-x size-[20px] sm:size-4 text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-300" />

</div>

</div>

<div id="chat-content"
class="chat-assistant-sheet-content flex flex-col-reverse flex-1 overflow-y-auto relative px-5 min-h-0">

<div class="flex-grow">

</div>

<div class="h-full flex flex-col justify-between">

<div class="mt-4 flex flex-col items-center text-sm">

<div class="mx-8 text-center text-gray-400 dark:text-gray-600 text-xs chat-assistant-disclaimer-text">

Responses are generated using AI and may contain mistakes.

</div>

</div>

</div>

<div class="h-px w-full shrink-0">

</div>

</div>

<div class="px-4 pb-4 shrink-0">

<div>

<div class="flex flex-col w-full rounded-2xl pointer-events-auto bg-background-light/90 dark:bg-background-dark/90 backdrop-blur-xl border border-gray-200 dark:border-white/30 focus-within:border-primary dark:focus-within:border-primary-light transition-colors">

<div class="relative flex items-end">

</div>

<div class="flex items-center justify-between px-2 pb-2">

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld2JveD0iMCAwIDE4IDE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9InNpemUtMy41Ij48cGF0aCBkPSJNNy43NSA1VjExLjc1QzcuNzUgMTIuNTc4IDguNDIyIDEzLjI1IDkuMjUgMTMuMjVDMTAuMDc4IDEzLjI1IDEwLjc1IDEyLjU3OCAxMC43NSAxMS43NVY0Ljc1QzEwLjc1IDMuMDkzIDkuNDA3IDEuNzUgNy43NSAxLjc1QzYuMDkzIDEuNzUgNC43NSAzLjA5MyA0Ljc1IDQuNzVWMTEuNzVDNC43NSAxNC4yMzUgNi43NjUgMTYuMjUgOS4yNSAxNi4yNUMxMS43MzUgMTYuMjUgMTMuNzUgMTQuMjM1IDEzLjc1IDExLjc1VjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB3aWR0aD0iMS41IiBsaW5lY2FwPSJyb3VuZCIgbGluZWpvaW49InJvdW5kIiAvPjwvc3ZnPg=="
class="size-3.5" />

<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWFycm93LXVwIHRleHQtd2hpdGUgZGFyazp0ZXh0LXdoaXRlIHNpemUtMy41Ij48cGF0aCBkPSJtNSAxMiA3LTcgNyA3IiAvPjxwYXRoIGQ9Ik0xMiAxOVY1IiAvPjwvc3ZnPg=="
class="lucide lucide-arrow-up text-white dark:text-white size-3.5" />

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>