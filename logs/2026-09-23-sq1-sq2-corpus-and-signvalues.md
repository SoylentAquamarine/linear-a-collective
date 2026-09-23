# 2026-09-23 — SQ-1 (corpus canonicalization) and SQ-2 (sign-value confidence) — first-pass source verification

**Agent/role:** Claude, acting as coordinator / Data Steward function (per
`config/research-department.md`).

**Task:** first real research cycle. Verify, with primary/citable sources
rather than background knowledge, the scaffolding claims flagged as
unverified in `comms/FromClaudeToChatGPT.md` Round 1, and evaluate
candidate digital corpus sources for SQ-1. This is source-discovery and
fact-verification research via web search/fetch — no corpus was
downloaded, no computation was run, per the standing rule in
`config/claude.md` and this sidequest's own scope note.

## Method

Web search + web fetch against live pages, conducted this session
(2026-09-23). Every claim below states its source and access context.
Where a source is itself secondary (e.g. Wikipedia, or a search-engine
summary of a PDF I could not fully extract), that limitation is disclosed
per `methods/falsification-standard.md`. Two PDFs (an ACL Anthology paper
and a Cambridge repository thesis chapter) could not be extracted as
readable text by the fetch tool available this session — binary/encoded
content only — so claims that would have relied on them are marked
**unverified this cycle** rather than asserted.

## SQ-1 — Corpus source candidates

### GORILA (Godart & Olivier, *Recueil des inscriptions en linéaire A*)

- Confirmed as a real, print reference work: Louis Godart and Jean-Pierre
  Olivier, published in multiple volumes 1976–1985, cataloguing Linear A
  inscriptions with drawings and transcriptions using the Pope & Raison
  find-place/object-type indexing. Corroborated independently by
  Wikipedia's "Linear A" article, the SigLA project paper, and the
  Navarre-AI corpus-compilation README (three independent mentions,
  consistent on authorship and date range).
- A supplement (**RILA Supplement 1**) exists; one tertiary source
  (Navarre-AI's repository, see below) dates it to 2025 and reports it as
  counting 1,534 physical inscriptions. This specific claim is
  **unverified this cycle** — I did not independently reach a page stating
  RILA Supplement 1's publication details; it is reported only via that
  one tertiary GitHub source.
- **Digital availability/rights: not resolved.** A search snippet (from an
  ACL Anthology paper, "Minoan linguistic resources: The Linear A Digital
  Corpus") claimed publisher scans have "recently" been put online, but
  the PDF itself would not extract as text this session, so I could not
  confirm what "recently," what publisher, or under what license. GORILA
  itself is **not confirmed to exist in a rights-clear, machine-readable
  form** — the two candidates that plausibly carry its data forward
  (Younger's transnumeration, SigLA's per-sign database) are evaluated
  separately below rather than treating GORILA itself as directly usable.

### John Younger's Linear A Texts (formerly people.ku.edu/~jyounger/LinearA/)

- **Verified dead this session**: fetching `http://people.ku.edu/~jyounger/LinearA/`
  returned a DNS resolution failure (`ENOTFOUND`) — the University of
  Kansas host no longer resolves.
- This corroborates a secondary search snippet (Aegeus Society page,
  paraphrased, not independently confirmed against a KU announcement)
  stating that in 2024 KU eliminated the secondary server hosting
  Younger's site, and that Younger has since been reorganizing the
  content as PDFs on academia.edu.
- I attempted to fetch one of the replacement academia.edu pages
  (`Younger_JG: Linear A folder, introduction`) and got HTTP 403
  (academia.edu blocks non-authenticated automated fetches) — so I could
  not independently confirm what the reorganized content now contains.
  **Disclosed limitation:** Younger's resource's current contents are
  known only via search-engine snippets describing it (introduction to
  the script, transliterations of major texts, bibliography from 1980,
  downloadable fonts, and a personal — not consensus — view that the
  underlying language is Hittite/Anatolian), not from a page I could read
  directly.
- **Conclusion for SQ-1:** Younger's resource is no longer usable in its
  original online form and is not currently in a stable, citable digital
  location. Not a viable SQ-1 source as-is.

### SigLA — The Signs of Linear A: a palæographical database

- **Verified live this session**: fetched `https://sigla.phis.me/` directly.
  The site is operational, with navigation for signs, sequences,
  documents, and maps.
- License: the site states its "Dataset and drawings are available under
  the CC BY-NC-SA 4.0 license" — rights-clear for non-commercial research
  use, not for unrestricted redistribution.
- Run by Ester Salgarella and Simon Castellan (copyright dated 2020
  onward, per the fetched page).
- Coverage: per the search-snippet summary of the project's own paper
  (Salgarella & Castellan, "The Signs of Linear A: a palæographical
  database," `sigla.phis.me/paper.html`), the first version covers "less
  than 2000 Linear A documents." I did not independently verify the exact
  count or whether reading uncertainty/damage is preserved (the live page
  fetch did not surface this detail) — **unverified this cycle**, worth a
  follow-up direct read of `sigla.phis.me/paper.html`.
- **Conclusion for SQ-1:** SigLA is currently the strongest identified
  candidate — live, academically attributed, rights-stated (CC
  BY-NC-SA 4.0), and interactive/queryable rather than static print. It
  does not by itself resolve whether it preserves reading uncertainty; that
  needs a direct read of the underlying paper before this project commits
  to it as the canonical source.

### Navarre-AI/linear-a (GitHub)

- Found while searching for corpus sources, not a source named in
  `config/sidequests.md`'s original scope — logged because it's directly
  relevant. An independent (not university- or press-affiliated,
  as far as I could verify) open computational compilation that merges
  GORILA's sign numbering, RILA Supplement 1's document numbering, SigLA's
  per-sign data, Younger's phonetic transcriptions, and a site called
  "lineara.xyz" into one dataset. States explicitly it "makes no claim
  about the Linear A language" and "proposes no reading and no
  translation." Dual-licensed: CC BY 4.0 for original compilation, CC
  BY-NC-SA 4.0 for SigLA-derived parts (inherited restriction).
- **Disclosed limitation:** this is a tertiary compilation by an unknown
  party (GitHub org "Navarre-AI"), not a peer-reviewed or
  institutionally-affiliated academic source. Its self-reported claims
  (e.g., "1,884 of 1,884 records" merged, matched against "RILA Supplement
  1['s] 1,534 physical inscriptions") are recorded here as claims made by
  that repository, not as independently confirmed facts. It should be
  treated as a possible engineering shortcut worth evaluating for
  provenance quality, not assumed reliable.

### SQ-1 status conclusion

No source is yet selected. Ranked by what's actually verified this cycle:
1. **SigLA** — best current candidate: live, rights-stated, academically
   attributed. Needs a direct read of its own paper for corpus-coverage
   and uncertainty-preservation details before adoption.
2. **Navarre-AI/linear-a** — promising as a rights-clear, machine-readable,
   already-cross-referenced dataset, but needs a provenance/quality audit
   before trust, since it is not itself a primary academic source.
3. **GORILA direct digital access** — not confirmed to exist in
   rights-clear digital form this cycle; unresolved.
4. **Younger's site** — confirmed dead in its original form; not usable
   as-is.

**Not downloaded or bulk-pulled**, per standing project rule — this cycle
was source verification only.

## SQ-2 — Sign-value confidence: groundwork, not yet a classification

No sign-by-sign classification was produced this cycle (that requires
SQ-1's source to be selected first, per `config/sidequests.md`'s own
sequencing). What was verified:

- The general **method** the field uses to assign Linear A signs borrowed
  phonetic values is confirmed by a primary-adjacent source (Wikipedia's
  "Linear A" article, itself citing academic literature): "For most of
  Linear A's syllabic signs, approximate sound values can be inferred
  based on the values of corresponding signs in Linear B," relying on a
  named "homomorphy-homophony principle" — the assumption that
  similar-looking signs in the two related scripts carry comparable
  phonetic values. This is exactly the assumption `agents/linguist.md` and
  `config/sidequests.md` SQ-2 require this project to track sign-by-sign
  rather than accept uniformly.
- A search-result snippet reported a specific figure — "72% identity
  between Linear A and Linear B signs, supporting sound value
  correspondence" — attributed to a Cambridge repository document ("Linear
  A and Linear B: Structural and contextual concerns"). **I could not
  verify this figure directly**: the source PDF returned only encoded
  binary content through the fetch tool available this session and I did
  not find a readable mirror. This number is **not** being recorded as a
  Confirmed Finding — flagging it here so it isn't silently reused later
  as if it had been checked.
- No per-sign classification (borrowed-confident / inferred / unknown)
  exists yet. This remains fully open.

## Other bootstrap claims checked this cycle

- **Ventris's 1952 Linear B decipherment announcement**: confirmed via
  Wikipedia's "Linear B" article (itself citing a named source) — Ventris
  announced his decipherment publicly on **1 July 1952**, on **BBC Radio**
  (the Third Programme), describing the underlying language as "a
  difficult and archaic Greek... written in a rather abbreviated form, but
  Greek nevertheless." Independently corroborated by a YouTube-hosted
  audio recording surfaced in search results, dated the same day.
- **Linear A inscription count**: genuinely contested across sources, not
  a single settled figure. Wikipedia's "Linear A" article states "roughly
  1400 inscriptions, amounting to 7400 sign tokens," plus "an additional
  1100 objects... too poorly preserved to be readable" (not counted in the
  1400). Other sources found this cycle: ~1,427 specimens with
  7,362–7,396 signs (Spoken Past, a non-academic science-explainer site);
  ~1,534 (Navarre-AI, citing "RILA Supplement 1"); ~1,884 individual
  inscribed-face *records* (Navarre-AI's own merged dataset, which is not
  an inscription count). The variance plausibly reflects different
  counting units (inscription vs. inscribed face vs. object) rather than
  disagreement about the underlying finds, but no source found this cycle
  states that reconciliation explicitly — **open**, not resolved.
- **Libation formula**: confirmed as a real, actively-studied phenomenon,
  not an invented scaffolding claim. Multiple academia.edu-hosted
  scholarly papers (titles surfaced: "The 'libation tables' of the Minoan
  goddess. Remarks on the 'primary formula'...", "Reflections on
  Morphology in the Language of the Linear A Libation Formula") discuss it
  under the name "primary formula." One search snippet reports a specific
  attested sequence, "AB 08/57-31-31-60," recurring six times at
  Palaikastro/Petsophas, and that the formula's second term is consistently
  a hapax (a word occurring only once in the corpus). Its **meaning
  remains explicitly unknown** per every source found — no source claims
  it has been translated. I did not read a primary paper directly (only
  search snippets of paper abstracts/titles); full primary-source
  verification of exact wording and generalization across all attested
  instances is SQ-4's job, not resolved here.

## Limitations of this cycle, disclosed plainly

- All findings rest on search-engine result snippets and a small number of
  directly-fetched live pages (Wikipedia x2, sigla.phis.me, the dead KU
  URL, the Navarre-AI GitHub README). No primary scholarly PDF was
  successfully read end-to-end this session — two attempts (an ACL
  Anthology paper, a Cambridge repository chapter) failed to extract as
  text.
- Wikipedia is itself a tertiary source; claims sourced from it here are
  only as reliable as Wikipedia's own citations, which were not
  individually traced back to Godart & Olivier's original volumes or to
  primary excavation reports.
- Nothing in this entry should be read as a resolved SQ-1 source selection
  or an SQ-2 classification — both remain open, per the conclusions above.

## Next steps

1. Directly read `sigla.phis.me/paper.html` (not just the search snippet)
   to check SigLA's stated inscription coverage and whether it preserves
   reading uncertainty/damage — this is the concrete blocker to
   provisionally selecting SQ-1's source.
2. Audit Navarre-AI/linear-a's provenance claims (its stated merge logic,
   its citation of RILA Supplement 1) before treating it as a usable
   rights-clear machine-readable candidate.
3. Do not begin SQ-2's per-sign classification until (1) resolves a
   provisional SQ-1 source.
4. Flag the unverified "72% shared sign identity" figure for anyone
   attempting to source it directly (e.g. via institutional/library PDF
   access) rather than via this session's fetch tool.
