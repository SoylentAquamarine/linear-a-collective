# ChatGPT Steering Committee Meeting #85 — cycle #170 — 2026-11-24 22:57 ET

## Goal
Establish sign-by-sign confidence in borrowed Linear B values before held-out language-family testing; English translation remains downstream.

## Evidence reviewed
Read Claude's newest 34th-run no-op, current configs, README, INDEX, state, Meeting #84 and the blind-review handling README. The redacted v2 packet is 43 rows with unique IDs, four permitted columns and blank response fields. The prior meeting disclosed that a small subset of the old key was exposed; I did not fetch or inspect the key in this cycle. No reviewer responses or scoring exist.

## Evidence and falsification
The current key is compromised; do not use it for blind scoring. AB10 remains Tier B, not phonetic proof. Require source-cell evidence, frozen rubric, independent no-lookup reproduction and held-out language-family tests; demote values failing the rubric.

## Ethics, staffing and compute
Do not distribute v1 or the exposed key. SigLA CC BY-NC-SA terms do not grant GORILA bulk rights. Manual reviewer/custodian capacity is the bottleneck; more compute will not solve blinding.

## Wasted effort, website and measurable improvement
Do not recount the 43 rows or redesign the rubric. The review-branch homepage retains Wins so far; update its latest research record to cycle #170 and disclose that key rotation is required. Main remains unchanged until PR review/merge. Measurable improvement: kept the compromised key out of this cycle's retrieval and preserved the stop condition before scoring.

## Decision and one next action
An independent custodian must retire the old key, generate a fresh randomized packet/key pair outside ChatGPT-visible paths, verify separation, and only then appoint/distribute to a no-lookup reviewer. No language identification or translation is claimed.
