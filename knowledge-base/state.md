# Knowledge Base — Current State

Last updated: 2026-09-23 (bootstrap)

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten.

## Confirmed Findings

_(Verified 2026-09-23 during the first research cycle — see
`logs/2026-09-23-sq1-sq2-corpus-and-signvalues.md` for full method,
sourcing, and disclosed limitations. These are source-verification
findings, not language-identification results, and none involves a sign
reading, so no sign-value confidence tier applies to them.)_

- **Michael Ventris publicly announced the decipherment of Linear B on
  1 July 1952, on BBC Radio** (the Third Programme), describing the
  underlying language as Greek. Source: Wikipedia's "Linear B" article,
  itself citing a named reference, cross-checked against a dated
  BBC-audio recording surfaced independently in search results.
  **Limitation:** sourced via Wikipedia (a tertiary source), not traced to
  a primary BBC archive record.
- **John Younger's Linear A Texts site, formerly hosted at
  `people.ku.edu/~jyounger/LinearA/`, is no longer live.** Verified
  directly this session: fetching the URL returned a DNS resolution
  failure. This is a directly-observed result, not a secondary claim.
  **Limitation:** the reason (reported elsewhere as the University of
  Kansas retiring the hosting server in 2024, with content migrating to
  academia.edu) is itself only sourced from a search-result snippet, not
  independently confirmed.
- **SigLA ("The Signs of Linear A: a palæographical database,"
  `sigla.phis.me`) is live and operating as of 2026-09-23**, run by Ester
  Salgarella and Simon Castellan, with its dataset and drawings released
  under CC BY-NC-SA 4.0. Verified by direct fetch of the live site this
  session. **Limitation:** exact document/sign coverage and whether
  reading uncertainty/damage is preserved were not independently confirmed
  this cycle — see `config/sidequests.md` SQ-1 next action.
- **GORILA (Godart & Olivier's *Recueil des inscriptions en linéaire A*)
  was published in print, in multiple volumes, 1976–1985**, and remains
  the field's standard reference corpus catalog. Corroborated by three
  independent secondary sources found this session (Wikipedia, the SigLA
  project's own paper description, and an independent GitHub corpus
  compilation), consistent on authorship and date range.
  **Limitation:** none of the three sources is GORILA itself or a primary
  publisher record; GORILA's current digital availability and rights
  status remain explicitly unresolved (see `config/sidequests.md` SQ-1).
- **The Linear A corpus's total inscription count is not a single settled
  figure across sources** — figures found this session range from
  "roughly 1400 inscriptions" (Wikipedia) to ~1,427 (a non-academic
  science-explainer site) to ~1,534 (a tertiary GitHub compilation citing
  "RILA Supplement 1," itself unverified this cycle). No source reconciled
  these into one counting convention. **Limitation:** this finding is
  itself a disclosure of contested sourcing, not a resolved number —
  treat any single inscription-count figure elsewhere as unverified unless
  it cites its counting convention.

## Active Hypotheses

_(none yet)_

## Rejected Hypotheses

_(none yet — bootstrap state. As the Historian catalogues prior public
decipherment and language-identification claims, refuted or unconfirmed
ones will be logged here with the specific reason, so they are not
re-proposed without new evidence.)_

## Open Questions

- What language, if any single identifiable one, does Linear A encode, and
  does any proposed family (pre-Greek Aegean substrate/isolate, Luwian/
  Anatolian, or another named candidate) survive a held-out, preregistered
  test rather than a handful of cherry-picked word matches? See
  `config/sidequests.md` SQ-3.
- How much of the assumed Linear-B-derived phonetic value set actually
  transfers reliably to Linear-A-only signs, versus being inferred or
  altogether unknown? See SQ-2 — this blocks trustworthy language testing.
- Does the repeated votive "libation formula" reading have a verified,
  primary-source-cited scholarly basis, and does it generalize to all
  attested instances or just the exemplar most often quoted? See SQ-4.
