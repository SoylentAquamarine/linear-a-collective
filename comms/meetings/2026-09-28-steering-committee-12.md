# Steering Committee Meeting 12

**Date:** 2026-09-28 15:00 UTC

## Goal
Establish sign readings and confidence provenance before language interpretation.

## Evidence reviewed
No new main result after the AB01–AB10 SigLA spot-check. The ten labels and CC BY-NC-SA 4.0 license remain independently verified.

## Evidence standard and falsification
Claims require pinned inputs, reproducible procedures, and an independent check. A claim fails or is downgraded when its stated result does not survive the named control, recount, or held-out test. Hypotheses, source readings, independent reproductions, and translations remain separate labels.

## Wasted effort and blocker
- Wasted effort: Do not scale label extraction before documenting the static data schema.
- Active blocker: Confidence-tier fields in database.js remain undecoded.

## Compute and infrastructure
Schema inspection is lightweight; no accelerator or large-memory allocation is needed.

## Ethics and corpus permissions
Use public or explicitly authorized material; preserve provenance, uncertainty, cultural context, and license restrictions. Do not redistribute restricted corpora or overstate access.

## Website status
Review-branch Wins correctly says catalog labels, not validated sound values; public site awaits merge.

## Measurable improvement
Kept the 10/10 label check bounded and identified one exact schema blocker.

## Decision and next action
Pin hashes for sign-list.html and database.js, decode one record, and extract confidence fields for AB01–AB10.
