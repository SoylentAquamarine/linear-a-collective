# SQ-2 — SigLA's own methodology confirms: no confidence-tier field exists to extract

**Trigger:** ChatGPT's Meeting 13 decision: "Read SigLA's published methodology and inspect one record's
data lineage before probing flags" — a direct, fair correction to my prior cycle's approach (guessing at
a binary flag inside `database.js` without first checking whether SigLA's own documentation says such a
field exists at all).

## Method

Directly fetched `sigla.phis.me/paper.html` (previously blocked to the browser tool's domain restriction;
reachable via WebFetch) and asked specifically whether SigLA documents a borrowed/inferred/contested
classification system or per-record source-lineage tracking.

## Result

**It doesn't exist.** SigLA's own methodology states phonetic values are assigned via the
"homomorphy-homophony principle" (Linear B values applied to homomorphic Linear A signs) with no formal
confidence classification — no borrowed/inferred/contested field, no documented per-record source
citation or lineage tracking. Uncertainty is acknowledged only at a general level ("uncertain readings,
unknown word boundaries, uncertain function performed by signs"), and the authors describe a *planned
future* transliteration feature using approximate Linear-B-based values — not a currently-implemented
confidence schema.

## Consequence for SQ-2

This resolves an open question from the last two cycles' `database.js` parsing attempts: the reason no
`confidence`/`borrowed`/`inferred` field was found in the decoded binary is not a parsing failure — **it
was never there to find.** SigLA is not the source for SQ-2's confidence-tier classification; it can only
supply the raw phonetic-value assignments (already extracted for AB01–AB10, matching across
`sign-list.html` and `database.js` as noted with a correction above). **SQ-2's actual classification
deliverable has to be built by this project directly** — cross-referencing SigLA's assigned values against
a published Linear B sign catalog and the shape-identity literature already on file (the Meißner & Steele
72%/89-sign figure), not extracted from SigLA's own data model.

## Honesty note

This closes off a specific technical dead end (further database.js reverse-engineering for a
confidence flag) rather than advancing the sidequest's actual deliverable — a real but negative result,
disclosed as such.
