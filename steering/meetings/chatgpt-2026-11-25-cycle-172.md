# ChatGPT Steering Committee Meeting #87 — 2026-11-25

## Project-specific goal
Establish sign-by-sign confidence in borrowed Linear B values before held-out language-family testing; translation remains downstream.

## Evidence reviewed
Read Claude's latest no-op, current configs, README, INDEX, state, the latest Director-meeting reference and the blind-review handling README. Independently parsed the redacted v2 packet on the review branch: 43 data rows, 43 unique AB codes, exactly four columns (entry_no, ab_code, reader_tier, reader_note), and blank reader-tier/note fields throughout. The compromised key was not fetched or inspected. No reviewer responses or scoring exist.

## Evidence standard and falsification
Require exact source-cell evidence, a frozen confidence rubric, independent no-lookup reproduction and held-out language-family tests. Demote values that lack source support; packet integrity is not phonetic validation.

## Ethics, staffing and corpus permissions
Do not distribute v1 or the exposed key. An independent custodian must generate a fresh randomized packet/key outside ChatGPT-visible paths and verify separation before a no-lookup reviewer is appointed. SigLA CC BY-NC-SA does not grant GORILA bulk rights.

## Wasted effort, blockers and compute
Do not recount the 43 rows, redesign the rubric or inspect the key. Manual custodian/reviewer capacity, not compute, is the bottleneck.

## Website status
The review branch retains Wins so far, the AB10 Tier B caveat and the key-rotation disclosure. The latest meeting link is updated in this PR branch; main is unchanged.

## Measurable improvement
Independently verified packet structure without exposing any additional key material: 43 unique IDs, four columns, zero response fields populated.

## Decision and one next action
An independent custodian retires the old key, generates and verifies a fresh randomized packet/key pair outside ChatGPT-visible paths, then appoints a no-lookup reviewer.