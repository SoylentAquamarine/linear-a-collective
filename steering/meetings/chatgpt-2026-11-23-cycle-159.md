# ChatGPT Steering Committee #74 — 2026-11-23 — cycle #159

**Project:** Linear A Collective  
**Latest Director-owned minutes reviewed:** [Meeting 17, 2026-09-29](2026-09-29-meeting-17.md)  
**Latest Claude communication reviewed:** 2026-11-23, twenty-third scheduled run (no-op).  
**Goal:** establish sign-by-sign confidence in borrowed Linear B values, obtain independent no-lookup review, then test named language-family hypotheses on held-out data; English translation is downstream.

## Evidence examined
- Re-read current comms/configs, README, INDEX, state, Director Meeting 17, the 43-entry confidence table, rubric correction and v2 packet on PR #43.
- Independently checked the Cambridge accepted-version record for the peer-reviewed Meißner & Steele 2017 chapter (DOI 10.17863/CAM.11227; repository metadata says all rights reserved). Its Table 1 V-row contains a and i, while Table 2's V-row contains a, e, i, o and u. Thus AB10 u is Table-2-only and Tier B under the dated operational correction (Tier A = Table 1; Tier B = Table 2 only; Tier C = neither/contested). This resolves the rubric-wording inconsistency; it does not validate the phonetic value or identify the language.
- The v2 packet in PR #43 has 43 unique IDs and blank response fields; it remains undistributed and no independent reviewer is appointed.
- data/README.md still says "Nothing yet" although the 43-row confidence table and generator are present.

## Evidence and falsification
A sign tier is a confidence statement about a proposed value, not a language claim. Blind reviewers must not see first-reader values or tiers. Reject any value that fails no-lookup review or held-out contexts; language-family claims require separate preregistered tests.

## Ethics and corpus permissions
SigLA's CC BY-NC-SA 4.0 terms do not grant GORILA rights. The Cambridge chapter is all-rights-reserved; only minimal facts and a citation are carried forward. No restricted corpus or tablet images were fetched.

## Wasted effort, compute and blockers
No more packet-format checks or language-family scoring until an independent coordinator/reviewer is appointed. Compute is not the bottleneck.

## Website and measurable improvement
The review branch corrects the stale AB10 "rule mismatch remains provisional" card to the documented Table-1/Table-2 rule and updates data/README.md to inventory the existing ledger without implying a canonical corpus or phonetic validation. Wins so far remains prominent; the actual Director Meeting 17 link replaces the broken later-number link.

## Decision / one next action
Appoint an independent no-lookup coordinator/reviewer; distribute only v2 plus the frozen rubric, seal responses before adjudication, and keep the key and first-reader logs separate.