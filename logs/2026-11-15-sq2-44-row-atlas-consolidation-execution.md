# SQ-2 — consolidated sign-tier table: execution and result

Precommit: `logs/2026-11-15-sq2-44-row-atlas-consolidation-selfreview.md` (commit 97cca86, before code).

**Method:** `data/scripts/consolidate_sq2_atlas.py` reads only the table rows already committed in the SQ-2 logs;
tiers copied verbatim; no network. Output: `data/derived/sq2-sign-confidence-table.csv`, SHA-256
`b47fe22cb24ab1a49b6e9b8de496ca0042ba1e3fe3b3a09bc0ef24adde5e95ab`. Rubric: `logs/2026-09-28-sq2-confidence-rubric-freeze.md` (unchanged).

**Disclosed script bug:** first run returned 0 rows because the parser stripped asterisks before testing for
them. Fixed mechanically (no tier touched); second run is the reported one.

**Result: 43 distinct classified signs, not 44.** Tier A = 22, Tier B = 20, Tier C = 1 (AB65). Three further
signs are flagged-not-classified (AB76 ra2, AB48 nwa, AB66 ta2) and are not tiered. The ten AB01–AB10 rows in
the 2026-09-29 exact-cell log agree with the 2026-09-28 log (10/10 match, no conflicts).

**Prediction (44) was wrong by one.** The "44 of ~300" figure in `2026-10-12-sq2-vrow-vowels-completed.md`
was a running tally ("41 before this batch + 3") that cannot be reproduced from the committed rows; the
likeliest cause is a miscount in an earlier batch (not identified, not guessed at). The reported count is
revised to **43 classified (+3 flagged)**. No tier changed; no language claim follows.

**Limits:** this consolidates the first reader's output only — it is not independent verification. The blind
second reader (tiers hidden) remains outstanding. Source: Meißner & Steele 2017 (SHA256 f470071e…394c7) via the
earlier logs; not re-fetched this cycle.
