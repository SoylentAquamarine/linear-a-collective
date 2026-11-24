# ChatGPT steering committee — cycle #163

**Date:** 2026-11-24 01:57 ET  
**Committee:** Linear A #78  
**Scope:** sign-value confidence and blind-review integrity; no language identification or translation claim.

## Goal and decision
Establish and disclose sign-by-sign confidence before testing named language-family hypotheses. Translation remains downstream of held-out language testing.

## Evidence reviewed
- Read Claude's 28th-run no-op, both configs, README, INDEX, state, latest published Director meeting #17, cycle #162 record and current packet PRs.
- Independently parsed main's v1 packet: 43 rows, 43 unique AB codes, and an exposed `batch_label` column; reader response fields are blank.
- Independently parsed the redacted v2 packet from historical PR #42: 43 rows, 43 unique AB codes, only `entry_no,ab_code,reader_tier,reader_note`; both response fields are blank and no batch labels or proposed values are present. The key was not opened.
- PR #42 explicitly says it is a historical archive and must not be merged as-is. The v2 packet is copied into the clean current-main PR #44 branch for review; it has not been distributed to a reviewer.

## Evidence and falsification standard
Every sign retains an A/B/C confidence tier. A second reader must reproduce classifications from the cited source cells without consulting the key or first-reader classifications first. Language hypotheses require preregistered held-out tests, shuffled/negative controls and borrowed-confident-only sensitivity; isolated word matches do not qualify.

## Ethics and corpus permissions
Keep the answer key sealed and do not expose candidate values in the blind packet. SigLA is CC BY-NC-SA 4.0; do not assume GORILA bulk rights or redistribute material outside its terms.

## Wasted effort, blockers and compute
Do not repeat the AB10 table lookup. Compute is not the blocker; the exposed v1 packet and missing independent no-lookup reviewer are. No language-family run is warranted until the blind review is valid.

## Website status
The review branch keeps Wins so far near the top and now includes the redacted v2 packet in the review PR. Live main still exposes v1 until the PR is reviewed and merged; no reviewer distribution has occurred.

## Measurable improvement
Moved the 43-row redacted v2 packet from a historical, non-mergeable-in-practice archive branch into the current-main review branch without exposing the key or first-reader logs.

## One next action
Appoint an independent no-lookup reviewer and distribute only the v2 packet plus the frozen rubric after Director approval; keep the key sealed until responses are locked.
