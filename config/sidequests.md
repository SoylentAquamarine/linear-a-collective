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

**Update (2026-09-25, third cycle — see
`logs/2026-09-25-sq1-sq4-lineara-explorer-and-kuro-kiro.md`):** a direct
read of `sigla.phis.me/paper.html` was attempted a third time and blocked
again, and this time the block was confirmed to be broad rather than
SigLA-specific — `en.wikipedia.org`, `arxiv.org`, `doi.org`,
`scholar.google.com`, `jstor.org`, `tandfonline.com`, `academic.oup.com`,
and `researchgate.net` were all also rejected by this session's egress
proxy. **This is now a three-cycle-confirmed environmental constraint —
future cycles running under this same proxy policy should not keep
re-attempting it; only a party/session with different network access can
resolve it.** Searching laterally instead surfaced a third candidate,
`github.com/mwenge/LinearA` + `github.com/mwenge/lineara.xyz` ("LinearA
Explorer"), citing GORILA and a named scholar George Douros as sources, with
1,684 catalogued document entries — but it has no `LICENSE` file at all
(rights status undetermined, weaker than SigLA or Navarre-AI on this axis),
and its claim that GORILA scans are hosted at `cefael.efa.gr` is itself
unverified (that domain is also egress-blocked from this session). SQ-1 is
now a three-way open field (SigLA / Navarre-AI / mwenge-LinearA); source
selection remains open pending a direct SigLA paper read from an unblocked
network.

**Update (2026-09-25, fourth cycle — see
`logs/2026-09-25-sq1-sigla-coverage-and-source-selection.md`): SQ-1 is now
provisionally resolved. SigLA is the provisionally selected working
source.** A direct read of `sigla.phis.me/paper.html` failed a fourth time
(egress-blocked), and three new adjacent domains tried for the first time
(`www.archaeology.wiki`, `www.repository.cam.ac.uk`, `site.unibo.it`) were
also blocked, further confirming the block is broad rather than
SigLA-specific. Instead of a fifth attempt at the same blocked read, three
independent `WebSearch` queries returned overlapping, mutually
corroborating figures: SigLA = 300 standard signs / 400 inscriptions /
3,000+ individual sign occurrences, explicitly "still under construction"
(not yet full-corpus coverage), with reading uncertainty and damage
(erasures) treated as a named design concern and a retained, displayed
feature rather than silently resolved — though the exact field-level
encoding scheme is still unconfirmed pending a direct paper/data read.

**Comparison and full reasoning are in the log; summary: SigLA beats
Navarre-AI/linear-a (non-institutional, disclosed a large 2026-09-18
claims/benchmark retraction) and mwenge/LinearA (no LICENSE file at all)
on institutional attribution and rights-clarity, at the cost of smaller
raw coverage (400 vs. 1,684–1,884 documents).** This selection is
provisional: it may need supplementing from a broader source once SQ-2
classification surfaces concrete coverage gaps, and it does **not**
authorize bulk retrieval of SigLA's per-sign dataset — any actual data
pull stays to the same narrow citation/count-spot-check scale as the
mwenge/LinearA precedent (Round 4), or needs explicit user authorization
for anything larger. **SQ-2 may now begin its first-pass classification
design against SigLA as the working source**, per this file's own
sequencing rule below.

**Update (2026-09-25, fifth cycle — ChatGPT Round 1, `comms/FromChatGPTToClaude.md`):**
the field-level encoding scheme gap flagged directly above is now closed,
via a direct read of SigLA's own help page (`sigla.phis.me/help.html`,
"Sign reading syntax" section) rather than another blocked paper-mirror
attempt. SigLA documents exactly **three** distinct, separately-encoded
uncertainty/damage states, which any normalization script must preserve
as three distinct fields, never collapsed into one generic "uncertain"
flag: (1) `?` or `unreadable` — an incomplete/broken sign; (2)
`unclassified` — a complete sign that has not been classified to a known
type; (3) an unsure-reading suffix `?` on an otherwise-classified sign
(e.g. `A01?`) — a confident-shape, unsure-value reading, structurally
distinct from (1) and (2). Erasures are separately marked in red in
SigLA's sign view (a fourth, display-level distinction, not yet confirmed
to have its own machine-readable export field). This closes the
uncertainty-preservation half of SQ-1's own evaluation criterion (line 25
above) at primary-source level for the documented user-facing syntax —
the underlying export schema's actual field names, and current corpus
coverage (SigLA's own paper describes an earlier, smaller administrative-
tablet-only snapshot; today's ~400-inscription figure should not be
assumed to carry the same coverage caveats without checking), remain
unconfirmed and are SQ-2's next concrete step before any broad
classification pass.

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

**Update (2026-09-25, fourth cycle):** SQ-1 has now provisionally selected
SigLA (see SQ-1 above) — this sidequest's blocking dependency is cleared.
**Still correctly not started this cycle:** no per-sign classification
exists yet, and none should begin without either (a) a narrow,
citation-scale data check (same precedent as the mwenge/LinearA single-file
spot-check, Round 4) or (b) explicit user authorization for a fuller
SigLA data pull — retrieving and parsing SigLA's actual 300-sign / 3,000+
occurrence dataset at working scale is more than a citation spot-check and
should not be treated as already authorized by the source-selection
decision alone. Next action for whichever cycle picks this up: get an
explicit scope decision on SigLA data retrieval (spot-check vs. full pull
with user authorization), then begin the first-pass borrowed-confident /
inferred / unknown classification design using a published Linear B sign
catalog as the comparison side.

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

**Status (2026-09-25, first catalog entry — see
`logs/2026-09-25-sq1-sq4-lineara-explorer-and-kuro-kiro.md`):** cataloged
the first administrative-term pair: **KU-RO** ("total") and **KI-RO**
("deficit"/"owed"), conventionally read this way in existing published
Linear A scholarship (cited across multiple independent sources, including
ones otherwise proposing rival language-family identifications) based on
their position at the end of numeral/commodity lists in accounting texts —
a functional/positional identification, not a phonetic or language-family
claim; see `knowledge-base/state.md` Confirmed Findings for the full
citation and disclosed limitations. A frequency spot-check against one
unverified candidate corpus file (mwenge/LinearA, see SQ-1) found 37
KU-RO / 16 KI-RO occurrences across 1,684 documents, consistent with (not
proof of) the literature description. Next action: extend to other
recurring administrative/numeral-ideogram conventions, and get a
primary-source-verified read of KU-RO/KI-RO (not just WebSearch synthesis)
once this session's egress restrictions allow it.

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

**Status as of 2026-09-25 (fourth cycle):** SQ-1 has provisionally
selected SigLA — the primary blocker is cleared. The new primary task is
SQ-2's first-pass classification, gated only on an explicit scope decision
for SigLA data retrieval (see SQ-2's update above). SQ-4 remains available
as a parallel-track sidequest.
