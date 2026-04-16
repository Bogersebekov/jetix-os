---
type: batch-report
phase: step-2-alpha-2
date: 2026-04-16
---

# Phase α.2 — Rule-based ingest report

## Statistics

- Total sweep records: 260
- Already imported (dedup vs wiki/sources): 254
- NEW for classification: 6
  - RELEVANT: 5
  - IRRELEVANT: 0
  - UNCLEAR: 1

## Ingested

- Successfully: 5
- Skipped (slug conflict): 0
- Edges added: 10

## IRRELEVANT (not imported, stay in Notion)



## UNCLEAR (for manual review, not imported)

- [32824963-33bf-8047-8387-cbd87f6b3617] [ / Ключевая] (untitled)

## Ingested slugs

- wiki/ideas/vork-khata-vork-selo-idealnoe-rabochee-okruzhenie.md
- wiki/ideas/posle-100k-derevnya-v-germanii-lyutyy-fokus.md
- wiki/ideas/problem-framing-samyy-dorogoy-navyk-2030.md
- wiki/ideas/dekompozitsiya-zhizni-na-podproekty.md
- wiki/ideas/audit-deystviy-po-vykhlopu-chtoby-bylo-na-ladoni.md


## Notes

- Rule-based classification (not Notion-fetch for full content).
  Preview = 500-char `Суть` field. Full content fetch deferred to Phase γ.
- All RELEVANT tagged `topics: [system-design]`.
- Slug conflicts resolved with -2/-3 suffix.
