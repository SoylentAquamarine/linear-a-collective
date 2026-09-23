# Language-identification-oriented sidequest queue

Sidequests are bounded, achievable pieces of work. Each must produce a
reusable artifact, answer a decision, or remove a named blocker. The lead
agent may reprioritize them, but should record why.

## SQ-1 — Corpus canonicalization (blocking, start here)

**Purpose:** establish a rights-clear, machine-readable, checksummed source
corpus that preserves reading uncertainty, the same first step the sibling
Voynich and Rongorongo projects each took. This sidequest is not optional
groundwork — it blocks every other sidequest and the entire Statistician/
Linguist/Cryptanalyst track.

**Scope:** evaluate candidate digital transcriptions/corpora of Linear A.
The standard published reference is commonly cited as GORILA (Godart &
Olivier's *Recueil des inscriptions en linéaire A*) — verify its current
digital availability and rights status before assuming it as the canonical
source. Also evaluate any modern open digital sign-list or corpus resource,
e.g. work associated with John Younger's Linear A materials — verify
current availability, since online academic resources move or go stale.
For each candidate, record: source, license/rights, retrieval method,
coverage (how many of the several-hundred-to-~1,400 attested inscriptions
it transcribes, at what completeness — the exact figure and counting
convention need verification), whether it preserves reading uncertainty/
damage rather than silently resolving it, and a checksum once pulled. Do
not bulk-download anything without explicit user authorization — this is a
standing rule across all sibling projects.

**Deliverables:** a source-comparison writeup (mirroring the sibling
projects' own source-discovery-candidates format), a provenance file once a
source is selected, and a normalization script with a full ambiguity-audit
trail once normalization begins.

**Stepping-stone value:** nothing downstream (sign-value confidence
classification, frequency analysis, language-family testing) is
reproducible or falsifiable without this.

**Laptop/worker-node work:** none yet — this stage is source discovery and
licensing/provenance research, not computation.

**Status (2026-09-23, first-pass source verification — see
`logs/2026-09-23-sq1-sq2-corpus-and-signvalues.md`):** no source selected
yet. Verified this cycle: John Younger's KU-hosted site
(`people.ku.edu/~jyounger/LinearA/`) is confirmed dead (DNS failure);
SigLA (`sigla.phis.me`) is confirmed live, academically attributed (Ester
Salgarella & Simon Castellan), and rights-stated (CC BY-NC-SA 4.0) —
currently the leading candidate, pending a direct read of its own paper
for coverage/uncertainty-preservation details. An independent tertiary
compilation, Navarre-AI/linear-a (GitHub), merges GORILA numbering, RILA
Supplement 1, SigLA, and Younger's transcriptions under a rights-clear
dual license, but is not itself a peer-reviewed source and needs a
provenance audit before use. GORILA's own digital/rights status remains
unresolved — a claim that "scans have recently been put online by
publishers" could not be independently verified this cycle (source PDF
unreadable by available tooling). Next action: read `sigla.phis.me/paper.html`
directly.

**Update (2026-09-23, second cycle — see
`logs/2026-09-23-sq1-navarre-ai-provenance-audit.md`):** the direct read of
`sigla.phis.me/paper.html` was attempted and blocked outright by this
session's network egress policy (`EGRESS_BLOCKED`), as were every academic
mirror tried (Cambridge repository, Semantic Scholar, academia.edu,
fluxus-editions.fr, huggingface.co, an inscribercproject.com mirror) — a
new, environment-level blocker, distinct from the "PDF unreadable" tooling
issue logged last cycle. `github.com`/`raw.githubusercontent.com` were
reachable. **Reading `sigla.phis.me/paper.html` directly is still the next
action, for whichever party/session has unblocked network access.**
Instead, this cycle completed the provenance audit of Navarre-AI/linear-a
that Meeting #1 also called for, via direct reads of that repo's own
`README.md`/`LICENSE`/`CREDITS.md`/`RELEASE-NOTES-2026-09-18.md` (not the
bundled corpus data itself, per the no-bulk-download rule). Verdict: a
disciplined, rights-aware, non-peer-reviewed single-maintainer compilation
(1,884 records / 1,665 objects, 4,936 sign occurrences, a self-reported
damage-flagging schema covering 358 of them) that also disclosed and
withdrew a large body of prior claims/benchmarks after a data-import defect
and an external audit disagreed with most of what it checked.
**Recommendation: do not adopt its word/reading-level fields without an
independent spot-check; its structural metadata and damage-flagging
convention are lower-risk and can inform SQ-2's schema design regardless of
which corpus is ultimately selected.** SQ-1 source selection remains open.

## SQ-2 — Sign-value confidence atlas

**Purpose:** this is the piece of groundwork that makes Linear A a
genuinely different starting position than Voynich or Rongorongo — and also
its sharpest risk of a false start. Because many Linear A signs share forms
with Linear B signs of known phonetic value, it's tempting to treat the
whole sign inventory as "already readable." It isn't. This sidequest builds
the data layer that keeps confident and unconfident readings from being
blended together and manufacturing false patterns.

**Scope:** using SQ-1's canonicalized corpus, for every Linear A sign
record whether it has (a) a directly-borrowed Linear-B phonetic value —
the sign shape is attested in deciphered Linear B with a known reading,
(b) an inferred value — extrapolated by shape-similarity, positional
analogy, or partial context, but not directly attested, or (c) no
confident value — a Linear-A-only sign, or one whose Linear B
correspondence is itself contested. Track how this classification affects
any downstream result: which analyses depend on borrowed-confident signs
only, which include inferred values (and how sensitive the result is to
excluding them), and which cannot proceed at all without unknown-value
signs.

**Deliverables:** a checksummed sign-value confidence table (sign id,
confidence tier, basis/citation for the tier), a sensitivity-analysis
convention that downstream sidequests (especially SQ-3) must follow, and a
missing-data report.

**Stepping-stone value:** every subsequent language-identification test is
only as trustworthy as this classification — an unlabeled mix of confident
and unconfident readings is exactly how a plausible-looking false pattern
gets manufactured.

**Laptop/worker-node work:** sign-shape comparison/clustering against
published Linear B sign catalogs, cross-referencing.

**Status (2026-09-23, groundwork only — see
`logs/2026-09-23-sq1-sq2-corpus-and-signvalues.md`):** no per-sign
classification exists yet; this correctly waits on SQ-1 selecting a
source. Verified this cycle: the field's general method for assigning
borrowed values — the "homomorphy-homophony principle" (similar sign shape
across the two scripts implies comparable phonetic value) — is
real and citable (Wikipedia's "Linear A" article, itself citing the
academic literature), confirming this is the correct axis SQ-2 must
classify sign-by-sign rather than accept uniformly. A specific figure
found in search results ("72% identity between Linear A and Linear B
signs") could **not** be verified — its source PDF (a Cambridge repository
document) was not extractable by available tooling this cycle — and is
explicitly not being treated as confirmed. Next action: once SQ-1 selects
a source, begin a first-pass classification using SigLA's per-sign data
(if adopted) cross-referenced against a published Linear B sign catalog.

## SQ-3 — Language-family discriminant tests

**Purpose:** Linear A's central open question is not "what kind of system
is this" (accepted as a syllabary related to Linear B) but "what language
does it encode." This sidequest designs falsifiable, held-out tests of
specific named candidate language families, rather than the pattern-
matching approach responsible for virtually every past claimed Linear A
decipherment failing to survive scrutiny.

**Scope:** using SQ-1's corpus and SQ-2's confidence atlas, test named
candidate families the literature has proposed — a pre-Greek Aegean
substrate/isolate (often called "Minoan"), Luwian/Anatolian, and any other
family with a serious scholarly proposal behind it — against the
transliterated sign-sequences. Freeze each test's design and decision rule
before looking at results, the same discipline the sibling projects use for
their own mechanism tests. Every test must report which sign-value
confidence tiers it relied on and how the result changes when inferred or
unknown-value signs are excluded.

**Deliverables:** preregistration per test, held-out scores, comparison
against typologically appropriate baselines, sensitivity results by
sign-value confidence tier, and a plain-English interpretation.

**Stepping-stone value:** this is the project's actual central deliverable
at the hypothesis-testing stage — the single most consequential place a
shortcut (skipping preregistration, skipping the confidence-tier
sensitivity check) would repeat the field's dominant failure mode.

**Laptop/worker-node work:** n-gram/co-occurrence analysis against
candidate-language phonotactic and morphological baselines, permutation
controls, comparison-corpus assembly.

## SQ-4 — Genre/formula catalog

**Purpose:** catalog the most information-dense, partially-understood
subset of the corpus — administrative numeral/ideogram conventions and the
recurring votive "libation formula" — with primary-source verification
before treating any existing scholarly partial reading as ground truth.

**Scope:** compile every attested instance of the libation-formula phrase
across libation-table inscriptions, its exact published wording and
variants, and whether it actually generalizes to all attested instances or
rests mainly on the exemplar most often quoted in secondary sources.
Separately, catalog Linear A's numeral and fraction/ideogram conventions as
used in the administrative/accounting texts (heavily represented in
archives such as Haghia Triada), cross-checked against
`agents/cryptanalyst.md`'s systems-level comparison to Linear B's numeral
notation.

**Deliverables:** a checksummed libation-formula instance table with
primary-source citations, a numeral/ideogram convention reference, and an
explicit statement of what remains unverified vs. what has been checked
against a primary source.

**Stepping-stone value:** if the libation formula genuinely recurs with
verified consistent wording, it is this project's best available candidate
for a held-out sanity check, the way Voynich's zodiac-page labels and
Rongorongo's lunar-calendar-like sequence serve their own projects.

**Laptop/worker-node work:** none required beyond ordinary text
comparison; this is primarily source-verification research.

## Initial priority

Start SQ-1 first — a canonicalized corpus is a hard blocker for everything
else. SQ-2 (sign-value confidence atlas) should begin as soon as SQ-1 has a
provisionally selected source, and is this project's most consequential
piece of early groundwork — do not let SQ-3 substantively begin before
SQ-2 has at least a first-pass classification, since testing a language
hypothesis against unlabeled sign confidence is exactly the failure mode
this project exists to avoid repeating. SQ-4 can begin in parallel with
SQ-1/SQ-2 (it is primarily source-verification research, not dependent on
full corpus canonicalization) without competing with the primary task.
