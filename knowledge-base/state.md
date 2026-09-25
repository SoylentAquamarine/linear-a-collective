# Knowledge Base — Current State

Last updated: 2026-09-25 (fourth research cycle)

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

_(Added 2026-09-23, second research cycle — see
`logs/2026-09-23-sq1-navarre-ai-provenance-audit.md` for full method,
sourcing, and disclosed limitations. These describe a *candidate data
source's* own self-published provenance/schema claims, not a Linear A
language or reading finding, so no sign-value confidence tier applies.
**Method limitation shared by all four bullets below:** read via this
session's `WebFetch` tool, which returns an AI-summarized/quoted rendering
of the fetched file rather than raw bytes — quotes are as that tool
returned them, not independently confirmed byte-for-byte. Also: a direct
read of SigLA's own paper (`sigla.phis.me/paper.html`), the leading
candidate source and the concrete next action from Steering Committee
Meeting #1, was attempted and blocked by this session's network egress
policy, along with every other academic mirror tried — still outstanding,
not resolved this cycle.)_

- **The Navarre-AI/linear-a GitHub compilation is a single-maintainer,
  non-institutional, non-peer-reviewed project** (its own `CREDITS.md`
  names the maintainer as "Matt Navarre," states no institutional
  affiliation, and does not claim peer review), that compiles GORILA
  numbering, RILA Supplement 1, SigLA data, and Younger's transcriptions.
  Verified by direct fetch of the repository's own `CREDITS.md` this
  session. **Limitation:** self-description, not independently audited by
  this project.
- **Navarre-AI/linear-a uses a disclosed dual license** — CC BY 4.0 by
  default, with CC BY-NC-SA 4.0 carved out specifically for SigLA-derived
  records (flagged in its data by a `sources` array containing `"sigla"`),
  correctly preserving SigLA's ShareAlike term on derived measurements.
  Verified by direct fetch of the repository's own `LICENSE` file this
  session. **Limitation:** the underlying data file was not fetched to
  confirm the flag is applied consistently record-by-record.
- **Navarre-AI/linear-a's schema, per its own README, flags 358 of 4,936
  total sign occurrences as `type: null` / `reading: null` /
  `certain: false` to mark a damaged, unreadable sign position rather than
  silently resolving it** — a real point in favor of SQ-1's "preserves
  reading uncertainty" selection criterion, if independently confirmed.
  Verified by direct fetch of the repository's own `README.md` this
  session. **Limitation:** this is the compiler's own claim about its own
  data; the underlying `corpus.json` was not fetched or independently
  checked, per the standing no-bulk-download rule.
- **Navarre-AI/linear-a self-disclosed and withdrew a large body of prior
  claims in a 2026-09-18 release**, after a data-import defect
  (concatenated words fabricated in 318 records) and an external audit
  that "disagreed with" 331 of 544 documented claims; the withdrawn
  material included an entire findings report and all 14 benchmark
  folders, and the repository now states it makes no claim about the
  Linear A language and proposes no reading or translation. Verified by
  direct fetch of the repository's own `RELEASE-NOTES-2026-09-18.md` this
  session. **This is a caution, not a disqualification** — see
  `config/sidequests.md` SQ-1: do not adopt this source's word/reading-
  level fields without an independent spot-check.

_(Added 2026-09-25, third research cycle — see
`logs/2026-09-25-sq1-sq4-lineara-explorer-and-kuro-kiro.md` for full method,
sourcing, and disclosed limitations.)_

- **In Linear A administrative/accounting texts, the word KU-RO is
  conventionally read in the published literature as meaning "total"
  (analogous to Linear B's accounting term to-so, "so much"), and KI-RO as
  "deficit"/"owed," based on their position at the end of numeral/commodity
  lists.** This is a report of existing, pre-dating-this-project field
  scholarship (corroborated across multiple independent sources found this
  session, including sources otherwise arguing for rival, contested
  language-family identifications, which cite the same base KU-RO/KI-RO
  reading regardless), not a novel test or translation by this project.
  **This is a functional/positional word identification, not a phonetic
  decipherment or a language-family claim** — it does not depend on, and
  should not be conflated with, any sign's SQ-2 phonetic-value confidence
  tier. **Limitation:** sourced via WebSearch-synthesized snippets of
  academia.edu/ResearchGate/World-History-Encyclopedia pages, not a full
  primary-paper read (this session's network egress policy blocks direct
  access to `sigla.phis.me`, `en.wikipedia.org`, `arxiv.org`, `doi.org`,
  `scholar.google.com`, `jstor.org`, `tandfonline.com`, `academic.oup.com`,
  `researchgate.net`, and other academic domains — see the log for the full
  list; this is now a three-cycle-confirmed environmental constraint, not
  a one-off failure). A frequency spot-check against one directly-fetched
  (not independently verified) candidate corpus file found 37 occurrences
  of `KU-RO` and 16 of `KI-RO` across 1,684 catalogued documents —
  consistent with, but not proof of, the literature's description.
- **A third SQ-1 corpus candidate exists beyond SigLA and Navarre-AI/
  linear-a: `github.com/mwenge/LinearA` (extraction scripts) and
  `github.com/mwenge/lineara.xyz` ("LinearA Explorer," the hosted app +
  bundled data), a single-maintainer project citing GORILA (Godart &
  Olivier) and a named scholar, George Douros, as its two principal
  sources.** Verified directly via `raw.githubusercontent.com` and the
  repo's own GitHub page this session. **Limitation:** no `LICENSE` file
  exists in the `lineara.xyz` repo (checked directly; 404 on `LICENSE`,
  `LICENSE.md`, `LICENSE.txt`), so its rights/reuse status is undetermined
  — a real mark against it relative to SigLA and Navarre-AI. Its claim that
  GORILA's digitized volumes are hosted at `cefael.efa.gr` could not be
  independently checked this session (`cefael.efa.gr` is itself blocked by
  this session's egress policy) and should be treated as an unverified
  secondary claim, not a confirmed fact about GORILA's availability.

_(Added 2026-09-25, fourth research cycle — see
`logs/2026-09-25-sq1-sigla-coverage-and-source-selection.md` for full
method, sourcing, and disclosed limitations. This is a source-evaluation
finding, not a language-identification result.)_

- **SigLA ("The Signs of Linear A: a palæographical database") comprises a
  list of 300 standard signs drawn from 400 Linear A inscriptions copied by
  hand, with more than 3,000 individual sign occurrences currently
  searchable, and is explicitly described (by its own project pages, as
  indexed) as "still under construction," aiming eventually to cover all
  known inscriptions.** Corroborated across three independent `WebSearch`
  queries returning overlapping but non-identical source sets (Semantic
  Scholar, academia.edu, the Cambridge Apollo repository record, two
  separate archaeology.wiki articles, the INSCRIBE project's own page, and
  a fluxus-editions.fr PDF mirror), all consistent on the 300/400/3,000+
  figures. **Limitation: this is a WebSearch-synthesized secondary
  reading, not a direct primary read of `sigla.phis.me/paper.html` itself
  — that direct read has now failed for four consecutive cycles due to a
  confirmed broad egress block on this session's network (also blocking
  en.wikipedia.org, arxiv.org, doi.org, scholar.google.com, jstor.org,
  tandfonline.com, academic.oup.com, researchgate.net, archaeology.wiki,
  repository.cam.ac.uk, and site.unibo.it, each independently confirmed
  this or a prior session).** 400 inscriptions is substantially smaller
  than this project's already-logged contested full-corpus range
  (~1,400–1,534); treat SigLA as a partial, expanding source, not a
  full-corpus one.
- **SigLA's own design treats reading uncertainty as a named concern and a
  retained, displayed feature rather than something silently resolved**
  — the indexed synthesis describes "uncertain readings, unknown word
  boundaries, uncertain function performed by signs in isolation, and
  ambiguous standard terminology" as an explicit challenge the database
  was built to address, and separately states damaged features such as
  erasures are included for display/analysis, alongside an explicit
  three-way distinction between a sign's standardised shape, a particular
  occurrence, and a graphic variant. **Limitation: same WebSearch-synthesis
  caveat as above — this confirms uncertainty/damage is a designed-for,
  retained concept in SigLA, but does not confirm the exact field-level
  encoding mechanism, which still needs a direct paper read or direct data
  inspection to pin down precisely.**
- **SQ-1 corpus-source selection: SigLA is now the project's provisionally
  selected working source**, chosen over Navarre-AI/linear-a (broader
  coverage and a self-reported damage-flagging schema, but non-
  institutional, non-peer-reviewed, and disclosed a large claims/benchmark
  retraction on 2026-09-18) and mwenge/LinearA (broader coverage, but no
  license file at all — undetermined rights status) on the strength of its
  institutional attribution, confirmed clean license (CC BY-NC-SA 4.0),
  and now-corroborated coverage/uncertainty-handling profile. **This
  selection is provisional, not final: it does not resolve whether SigLA's
  400-inscription coverage will need supplementing from a broader source
  once concrete gaps appear during SQ-2 classification, and it does not
  authorize any bulk retrieval of SigLA's per-sign dataset** — see
  `config/sidequests.md` SQ-1 for the full comparison table and reasoning,
  and the standing no-bulk-download rule in `README.md`/`config/claude.md`.

## Active Hypotheses

_(none yet — the KU-RO/KI-RO entry above is a Confirmed Finding about
existing scholarship, not an Active Hypothesis, per
`methods/falsification-standard.md`: it makes no language-family claim and
was not developed or tested by this project.)_

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
