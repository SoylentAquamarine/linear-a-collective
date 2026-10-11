# SQ-2 — a fourth citation-scale batch (d/k/r rows) finds real exceptions, correcting last cycle's own claim

**Trigger:** last cycle's own named next step: "the real remaining uncertainty is in rows not yet tested
at all (d, k, r — present in Table 1 — plus whatever's left)." This batch runs exactly that test.

## What's already known / not done yet

Already known: 4 rows tested across 3 prior batches (m, p — present in Table 1, landed Tier A; q, z, w, j —
entirely absent from Table 1, landed Tier B/C), with a stated working claim: "Table 1/Table 2 membership
operates at the whole-consonant-row level, not per-sign... zero exceptions found so far." Not done: testing
a row that is only *partially* represented in Table 1, which the prior four batches happened not to sample.

## Design and why it's non-circular

Fetched SigLA's sign-list page (citation-scale) for every AB-series sign with d-, k-, or r-initial values,
then classified each against the same already-on-file Meißner & Steele Table 1/Table 2 grids, exactly as
the frozen rubric specifies — no new reading of the source paper, no rubric changes.

## Honesty precommitment

If this batch's results contradict last cycle's own stated working claim, report that plainly as a
correction, not a quiet reframing.

## Result

12 new AB-codes classified (3 were already done in the first batch: AB01/da, AB02/ro, AB07/di — skipped
here, not re-counted).

| AB code | Value | In Table 1? | In Table 2? | Tier |
|---|---|---|---|---|
| AB67 | ki | **Yes** (k-row, i-column) | Yes | **A** |
| AB26 | ru | **Yes** (r-row, u-column) | Yes | **A** |
| AB53 | ri | **Yes** (r-row, i-column) | Yes | **A** |
| AB45 | de | No | Yes | **B** |
| AB51 | du | No | Yes | **B** |
| AB44 | ke | No | Yes | **B** |
| AB70 | ko | No | Yes | **B** |
| AB77 | ka | No | Yes | **B** |
| AB81 | ku | No | Yes | **B** |
| AB27 | re | No | Yes | **B** |
| AB60 | ra | No | Yes | **B** |
| AB76 | ra₂ | special case — not a plain "ra" cell in either grid | — | **flagged, not classified** |

**AB76 ("ra₂")**: SigLA labels this a secondary/variant reading, the conventional Linear B notation for a
homophone sign (e.g. representing a syllable like /rya/ or /lya/ conventionally transliterated "ra₂," not
a second instance of plain "ra"). This doesn't correspond to a simple cell in either frozen table, so it is
**not forced into Tier A/B/C** — flagged as a real edge case needing its own handling rule in a future
cycle, consistent with how AB65's `*65` case was handled two cycles ago.

## This directly corrects last cycle's own stated working claim

**The k-row and r-row are each *partially* represented in Table 1, not uniformly present or absent** — the
k-row has only `ki` in Table 1 (not ka/ke/ko/ku), and the r-row has `ri`/`ro`/`ru` in Table 1 but not
`ra`/`re`. This means **AB67 (ki) and AB53/AB26 (ri/ru) land in Tier A while other signs in the exact same
consonant row (AB44/70/77/81, AB27/60) land in Tier B** — a direct, real exception to last cycle's claim
that "Table 1/Table 2 membership operates at the whole-row level, not per-sign."

**What actually happened, disclosed plainly**: the first four rows tested (m, p, q, z, w, j) happened, by
chance of which ones got sampled first, to all be rows that are either fully present or fully absent in
Table 1 — not because row-level uniformity is a real structural property of the table, but because that's
what the early, small sample looked like. Testing two more rows (d was also only partially tested before —
da/di present, de/du never checked until this batch, and they land in Tier B, so d is partial too) shows
the correct picture: **Table 1 membership is determined per cell (specific consonant+vowel combination),
not per consonant row.** The "zero exceptions across 4 rows" claim is retracted as an overgeneralization
from a biased early sample, not as a result that was wrong on its own terms — it was an honest extrapolation
that didn't hold up under a bigger, more representative test, exactly the kind of thing broader sampling is
supposed to catch.

## Decision

Classified-sign count now 32 of ~300 (9A/1B/AB01-10; 2A/3B/AB11-20; 0A/4B/1C/w+j-rows; 3A/8B/1 flagged/
d+k+r-rows). `knowledge-base/state.md` and `config/sidequests.md` should both carry this correction
forward explicitly, not just update the running total silently — the per-cell (not per-row) framing is the
one to use from here on.
