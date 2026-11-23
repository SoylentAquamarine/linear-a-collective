# Blind-packet provenance-leak audit — 2026-11-22

## Scope and inputs
Joined the review-branch packet `data/blind-review/sq2-blind-packet-43-redacted.csv` to `data/derived/sq2-sign-confidence-table.csv` by `ab_code`. Both files contain 43 data rows; all packet codes are unique and all 43 match the confidence table.

## Finding
The packet's `batch_label` is not neutral metadata. Each batch label maps one-to-one to a first-reader source log, exposing the provenance group and its tier composition:

| Batch | Rows | Existing tier composition | First-reader source log |
|---|---:|---|---|
| batch-1 | 10 | A=9, B=1 | 2026-09-28-sq2-ab01-ab10-classified.md |
| batch-2 | 5 | A=2, B=3 | 2026-10-10-sq2-ab11-ab20-classified.md |
| batch-3 | 9 | A=7, B=2 | 2026-10-11-sq2-n-s-t-row-batch-classified.md |
| batch-4 | 11 | A=3, B=8 | 2026-10-11-sq2-d-k-r-row-batch-and-correction.md |
| batch-5 | 3 | A=1, B=2 | 2026-10-12-sq2-vrow-vowels-completed.md |
| batch-6 | 5 | B=4, C=1 | 2026-10-10-sq2-w-and-j-row-batch-classified.md |

This does not reveal the phonetic value directly, but it gives a no-lookup reviewer a provenance cue correlated with the original tier distribution. The v1 packet is therefore not suitable for strict blind review.

## Remediation
Created `sq2-blind-packet-43-redacted-v2.csv` by removing `batch_label` entirely. The v2 packet retains 43 unique AB codes, a shuffled row number, and blank `reader_tier` / `reader_note` fields. It contains no proposed phonetic-value field. The old v1 packet remains in the review branch for audit only and must not be distributed.

## Limits and decision
This is a structural/provenance audit, not a phonetic validation. It does not establish or reject any sign value or language-family hypothesis. Before distribution, the independent coordinator must receive only v2 plus the frozen rubric; no key or first-reader logs. Seal responses before adjudication and unblinding. SigLA CC BY-NC-SA 4.0 and GORILA restrictions remain separate.
