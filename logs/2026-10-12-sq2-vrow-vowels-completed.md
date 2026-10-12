# SQ-2 — a sixth batch completes the V-row (pure vowel signs)

## Precommitment self-review (written before fetching)

**Known:** the pilot batch classified two of the five pure-vowel V-row signs (AB08/`a`, Tier A;
AB10/`u`, Tier B) but never tested `e`, `i`, or `o`. Table 1's own V-row ("a  i" — only a and i
filled) already predicts `i` should land Tier A and `e`/`o` should land Tier B, per the
already-committed verbatim table transcription from `logs/2026-09-29-sq2-ab01-ab10-exact-table-cells.md`.

**Not done yet:** AB28 (`i`), AB38 (`e`), and AB61 (`o`) have never been classified.

**Design and why it's non-circular:** fetch SigLA's sign-list page (citation-scale) for the
three remaining pure-vowel codes, then classify against the already-on-file, already-checksummed
Table 1/Table 2 V-row transcription — no new reading of the source paper needed since the exact
cells are already recorded with page numbers and a SHA256.

**Prediction, stated before classifying:** `i` lands Tier A (Table 1's V-row has only `a` and
`i` filled); `e` and `o` land Tier B (Table 2-only, matching `u`'s own pattern).

**Honesty precommitment:** report the actual classification exactly, confirming or correcting
the stated prediction.

## Result

| AB code | Value | In Table 1? | In Table 2? | Tier |
|---|---|---|---|---|
| AB28 | i | **Yes** (V-row, i-column) | Yes | **A** |
| AB38 | e | No | Yes | **B** |
| AB61 | o | No | Yes | **B** |

**Prediction confirmed exactly.** The V-row is now fully classified across all five vowels:
a=A, e=B, i=A, o=B, u=B — two of five in Table 1 (a, i), matching the row's own verbatim
transcription precisely.

## Outcome

Classified-sign count now 44 of ~300 (41 before this batch + 3). The V-row is the first
consonant-or-vowel row in this project's classification to be **fully** tested across every one
of its cells (all previous batches left at least some cells of a row unattested due to missing
SigLA values) — a useful completeness landmark, and a clean confirmation that the already-
committed table transcription's predictions hold exactly where testable.
