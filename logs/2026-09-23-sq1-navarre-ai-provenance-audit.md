# 2026-09-23 — SQ-1: Navarre-AI/linear-a provenance audit; SigLA paper read attempt

**Agent/role:** Claude, acting as Data Steward function (per
`config/research-department.md`'s role list).
**Responding to:** Steering Committee Meeting #1
(`comms/meetings/2026-09-23-steering-committee-01.md`), action items
"Read `sigla.phis.me/paper.html` directly" and "Provenance-audit
Navarre-AI/linear-a's merge claims before adopting any of its bundled
data."

## What was attempted first: reading SigLA's own paper directly

Meeting #1's top action item was to read `sigla.phis.me/paper.html`
directly rather than via a search snippet. This was attempted this
session and **failed for a new reason, not the one logged last cycle**:
this session's network egress policy blocks the domain outright
(`EGRESS_BLOCKED`, not a content/parsing failure). The same block applied
to every other academic mirror tried:

- `sigla.phis.me` (paper.html and paper.pdf) — blocked
- `www.repository.cam.ac.uk` (Cambridge institutional repository record)
  — blocked
- `www.semanticscholar.org` — blocked
- `www.academia.edu` — blocked
- `www.fluxus-editions.fr` (paper PDF) — blocked
- `huggingface.co` (a dataset methodology page citing SigLA) — blocked
- `www.inscribercproject.com` (a paper mirror) — blocked

Per this session's own tooling documentation, an `EGRESS_BLOCKED` domain
means "not allowed by your organization's egress policy for this
session... do not retry or route around it." This is disclosed here as an
**environmental constraint for future cycles**, not something to keep
retrying: SigLA's own paper has still not been directly read by either
party as of this entry. `github.com` and `raw.githubusercontent.com` were
*not* blocked, so GitHub-hosted material remains reachable even when a
project's own academic-institution mirror isn't — worth trying first for
any future source-verification task.

What indirect evidence for SigLA's coverage/uncertainty-handling is
available (via search-result snippets, not a direct paper read — do not
promote as Confirmed): SigLA is described in multiple search snippets as
covering roughly 300 standard signs, ~400 hand-copied inscriptions, and
3,000+ individual searchable sign tokens, developed 2020– by Ester
Salgarella (Cambridge) with software by Simon Castellan (INRIA, Rennes).
This is consistent with, but does not upgrade, last cycle's finding that
SigLA is live and CC BY-NC-SA 4.0 licensed. **Still unresolved:** a direct
read of SigLA's uncertainty/damage-markup convention in its own words.

## What was completed instead: Navarre-AI/linear-a provenance audit

Meeting #1's second action item — audit Navarre-AI/linear-a's merge
claims before treating it as source-selection-worthy — was completed this
cycle via direct reads of that repository's own published files (fetched
from `raw.githubusercontent.com/Navarre-AI/linear-a/master/...` and the
repo's GitHub page; the default branch is `master`, not `main`). Per the
standing no-bulk-download rule, the underlying `corpus.json` dataset
itself was **not** fetched or parsed — only the repository's own
documentation files (`README.md`, `LICENSE`, `CREDITS.md`,
`RELEASE-NOTES-2026-09-18.md`), which describe the dataset's structure and
provenance without requiring the dataset itself to be pulled.

**Method limitation to disclose:** these files were read via this
session's `WebFetch` tool, which processes the fetched page through an
intermediate summarization model and returns paraphrase/quotes rather than
raw bytes. The quotes below are reproduced as that tool returned them and
have **not** been independently confirmed byte-for-byte against the raw
file. Treat this as a real but lower-fidelity read than a manual diff
would give — a materially different situation from a search-snippet-only
finding (this pulled the actual current file, not a cached/indexed
excerpt), but still a step short of the "committed output a third party
could rerun" ideal `methods/falsification-standard.md` asks for.

**Findings:**

- **Maintainer/authority:** the repo's `CREDITS.md` names a single
  individual maintainer, "Matt Navarre" ("Matt Navarre. Copyright 2026."),
  with no stated institutional affiliation and no claim of peer review.
  It self-describes as a "computational research project" that compiles
  and cites published scholarship (GORILA, SigLA, RILA Supplement 1,
  Younger's transcriptions) rather than as an academic publication itself.
- **License structure:** confirmed dual-license split, per `LICENSE`:
  CC BY 4.0 by default (code, text, project-generated data), with CC
  BY-NC-SA 4.0 carved out specifically for SigLA-derived content, flagged
  at the record level in `corpus.json` by a `sources` array containing
  `"sigla"`. The file states ShareAlike reaches derivative measurements
  computed from SigLA material, and that CC BY-NC-SA 4.0 material "cannot
  be relicensed as CC BY 4.0." This is a coherent, rights-aware structure,
  not a rights-washing shortcut, on its face.
- **Scale, per the repo's own README (as of the 2026-09-18 release):**
  1,884 records representing 1,665 physical objects (faces counted
  separately; some source IDs duplicate the same physical inscription);
  4,936 total sign occurrences broken down by role (syllabogram 3,287,
  logogram 1,175, fraction 313, erasure 100, transaction 61); 402 entries
  in the sign-reference file; word-field data present in 670 of the
  records (666 non-empty).
- **Uncertainty/damage handling — directly relevant to SQ-1's selection
  criterion:** the README states 358 of the 4,936 sign occurrences carry
  `type: null`, `reading: null`, and `certain: false`, explicitly marking
  a position where "the source reads damage, not a sign" — i.e., damage is
  flagged in the schema rather than silently resolved into a normal
  reading, at least for this subset and at least as self-reported. This
  has **not** been independently verified against the raw `corpus.json`
  (not fetched, per the no-bulk-download rule) — this is the compiler's
  own claim about its own data, not yet an independently confirmed
  property.
- **Self-disclosed correction event (important caution, not
  disqualification):** `RELEASE-NOTES-2026-09-18.md` documents that a
  prior release contained a data-import defect — the importer "read one
  page too many from each source document," fabricating concatenated
  words in 318 records, which dropped the unique multi-syllable word count
  from 1,211 to 979 once caught. The maintainer states an external audit
  of 544 documented claims disagreed with 331 of them, and that "a large
  body of claims, findings and benchmarks was withdrawn... because it was
  not supported by the data," including "the findings report and the
  success-criteria ladder" and all 14 benchmark folders. The repo now
  states it makes "no claim about the Linear A language... no reading and
  no translation," positioning itself purely as a sourced, concordance-
  level data publication going forward.

## Interpretation for SQ-1

This audit is a genuine mixed signal, and should be read as exactly that:

- **In favor:** disciplined, disclosed licensing that correctly respects
  SigLA's ShareAlike terms; a damage/uncertainty-preserving schema
  (self-reported); and — notably — a maintainer who, on discovering a real
  defect via reader feedback and an external audit, retracted a large
  body of claims rather than patching around them. That last point is
  itself evidence of a source willing to admit error, which is worth more
  than it costs.
- **Against / caution:** this is a single, non-institutional, non-peer-
  reviewed maintainer's compilation. The scale of what had to be
  withdrawn (an entire findings report, all 14 benchmarks, and an
  external audit disagreeing with the majority of documented claims) means
  its *word-level* and *reading-level* data should not be trusted without
  our own independent spot-check, even though the structural metadata
  (counts, license, damage-flagging schema) is lower-risk and easier to
  take at face value.

**Recommendation, not yet a decision:** do not provisionally select
Navarre-AI/linear-a for word/reading-level data. Its damage-flagging
schema convention and its GORILA/SigLA/RILA concordance mapping are
plausible reusable ideas regardless of source selection. SigLA itself
remains the leading candidate for sign-drawing and per-sign-occurrence
data, but its own paper still needs a direct read once this session's (or
a future session's) egress policy allows it, or via a party whose network
isn't blocked from `sigla.phis.me`.

## Next action

1. Either party: get a direct read of `sigla.phis.me/paper.html` from a
   network that isn't blocked from it (or ask the user whether the
   `sigla.phis.me` domain can be allowed for this project's sessions).
2. Do not adopt Navarre-AI/linear-a's word/reading fields without an
   independent spot-check against a small, explicitly-authorized sample —
   not a bulk pull — given the disclosed retraction history.
3. SQ-1 source selection remains open; this cycle narrowed the decision
   inputs but did not close them.
