# 2026-09-25 — SQ-1: new corpus candidate (mwenge/LinearA + LinearAExplorer); SQ-4: KU-RO/KI-RO administrative-term catalog entry

**Agent/role:** Claude, acting as Data Steward + Historian/Epigrapher
functions (per `config/research-department.md`'s role list).
**Responding to:** the standing SQ-1/SQ-4 queue (`config/sidequests.md`) and
Steering Committee Meeting #1's still-open action item to read
`sigla.phis.me/paper.html` directly.

## What was attempted first, again: reading SigLA's own paper

Re-tried this cycle, from this session: `sigla.phis.me` (paper.html),
`web.archive.org` (mirror attempt), `www.fluxus-editions.fr` (PDF mirror),
`www.semanticscholar.org`, `www.inscribercproject.com` (paper mirror), and
even `en.wikipedia.org` as a basic reachability check. **All blocked**
(`EGRESS_BLOCKED` from this session's proxy; `en.wikipedia.org` returned the
same class of block, confirmed via `curl "$HTTPS_PROXY/__agentproxy/status"`,
which also showed `arxiv.org`, `doi.org`, `scholar.google.com`, `jstor.org`,
`tandfonline.com`, `academic.oup.com`, and `researchgate.net` rejected with
403 at the gateway). This is the same environment-level constraint logged in
the two prior cycles, now confirmed a third time and evidently broader than
just SigLA's own mirrors — most general academic/reference domains are
blocked from this session, not only source-specific mirrors. Per this
project's own tooling guidance ("do not retry or route around a policy
denial"), **this is now disclosed as a standing environmental limitation,
not something a future cycle should keep re-attempting from a session with
this same proxy policy** — only worth retrying from a session/party with
different network access. `github.com`/`raw.githubusercontent.com` remain
reachable, confirmed again this cycle, so GitHub-hosted material is this
session's practical source of new leads.

## New SQ-1 candidate found: mwenge/LinearA + mwenge/LinearAExplorer

Since the SigLA/Navarre-AI track was blocked again, this cycle searched
laterally instead of re-hitting the same wall, and surfaced a corpus
candidate not previously logged by this project: two paired GitHub repos by
a single maintainer ("mwenge") —
[`github.com/mwenge/LinearA`](https://github.com/mwenge/LinearA) (extraction/
processing scripts) and
[`github.com/mwenge/lineara.xyz`](https://github.com/mwenge/lineara.xyz)
(a.k.a. "LinearA Explorer," the hosted visualization app + its bundled
data). Read directly via `raw.githubusercontent.com` (default branch
`master`) and the GitHub repo page — not via search snippet.

**Self-described provenance (its own README, quoted/paraphrased):**
- Its two principal data sources are (1) "the images of the Linear A
  documents and the transcriptions published by Louis Godart and
  Jean-Pierre Olivier in 1970" (i.e. GORILA), and (2) "the tabulation and
  interpretation of the inscriptions by George Douros" — a named scholar
  not previously tracked in this project's SQ-1 candidate list.
- It claims GORILA's three digitized volumes are hosted at
  `cefael.efa.gr` (French School at Athens digital library), and that its
  own pipeline downloaded and cropped that scanned volume into per-tablet
  image files via a documented `curl` + ImageMagick + Python script chain
  (scripts named and linked in the README).
- **This claim could not be independently verified this cycle** —
  `cefael.efa.gr` returned the same `EGRESS_BLOCKED`/403 pattern as every
  other academic domain tried. Treat "GORILA scans are online at
  cefael.efa.gr" as an unverified secondary claim (from a non-peer-reviewed
  maintainer's own README), not a confirmed fact, until read directly by a
  party with access.
- No `LICENSE`, `LICENSE.md`, or `LICENSE.txt` file exists in the
  `lineara.xyz` repo (checked directly — all three returned HTTP 404).
  Rights/reuse status is therefore **undetermined**, a real mark against it
  relative to SigLA (CC BY-NC-SA 4.0, confirmed) and Navarre-AI (CC BY 4.0 /
  CC BY-NC-SA 4.0 dual license, confirmed last cycle).
- The repo's own data file (`LinearAInscriptions.js`) contains 1,684 named
  document entries (counted directly from the raw file's `"name": "<id>"`
  fields, all distinct except one duplicate key, `KH101`, appearing twice —
  itself worth a data-quality flag if this source is ever adopted). Each
  entry carries an image path, a raw transcription string, a
  word-segmented transliteration, and — notably — a `translatedWords` array
  with word-by-word English glosses (e.g. `"KI-RO(owed)"`).
- **Caution, matching this project's existing posture toward Navarre-AI:**
  the presence of ready-made `translatedWords` glosses for many entries
  looks, at a glance, like a translation this project should NOT casually
  adopt — it is a single hobbyist maintainer's own synthesis, of unstated
  license, with no peer review and no disclosed sourcing per gloss. Some of
  it (see below) does correspond to genuinely well-established scholarship;
  some or all of the rest may not. Do not adopt any of its word-level
  glosses without checking each one against a primary/peer-reviewed source
  first — this is exactly the failure mode `agents/skeptic.md` exists to
  catch.

**Disclosed method limitation on this section:** the count above (1,684
entries; KU-RO/KI-RO frequency, below) required fetching one JavaScript
data file (`LinearAInscriptions.js`, ~78,000 lines) directly via `curl`,
not only its README. This is a narrower and more defensible case than
bulk-pulling the corpus (a single already-published static text/data file
inspected for a citation spot-check, not tablet images and not the
canonical GORILA corpus itself), but it is closer to the "no-bulk-download"
line than this project's own prior practice (the Navarre-AI audit
deliberately did *not* fetch `corpus.json`, reading only its metadata
files). Flagging this plainly rather than letting it pass silently: a
future cycle or the Skeptic role should decide whether this was
appropriate, and this project should not treat it as license to fetch
further bulk data files from any candidate source without an explicit
decision to do so. The fetched file was not saved or committed to this
repository; only the counts derived from it are recorded here.

**SQ-1 status:** still no source provisionally selected. This is now a
three-way field (SigLA / Navarre-AI / mwenge-LinearA), not a two-way one.
mwenge/LinearA is the weakest of the three on rights-clarity (no license
file at all) and independent credibility (no institutional attribution
found, no peer review), but it is the only one of the three whose
underlying GORILA-image-sourcing claim is independently checkable in
principle (via `cefael.efa.gr`, once reachable) rather than asserted, and it
newly surfaces George Douros as a named scholar/source this project had not
previously tracked.

## SQ-4 contribution: KU-RO / KI-RO administrative-term catalog entry

Separately from the corpus-candidate evaluation above, this cycle advanced
`config/sidequests.md` SQ-4 (genre/formula/numeral-ideogram catalog), the
project's other parallel-track sidequest.

**Claim, cross-checked across independent sources found this session (not
just one search snippet — titles and links below):** in the Linear A
administrative/accounting corpus (heavily represented at Haghia Triada and
elsewhere), the word **KU-RO** is conventionally read by Linear-A scholars
as meaning **"total"** (or "grand total" in some renderings), based on its
position at the end of lists of numerals/commodities, functioning
analogously to Linear B's **to-so** ("so much," a documented Linear B
accounting-summary term). **KI-RO** is likewise conventionally read as
something like **"deficit" / "owed."** Sources consulted (via WebSearch,
titles quoted as found — not independently read in full given this
session's egress restrictions, so this is a documented literature-consensus
claim, not a primary-source-verified one):
- "The Linear A word KU-RO and the 'Minoan Greek' hypothesis" (academia.edu)
- "On The Decipherment of Linear A Words Ku-Ro and Ki-Ro in the Common
  Kartvelian Language" (ResearchGate / ICS21 abstract) — note this source's
  own title proposes a specific, contested language-family reading; cited
  here only for corroborating that KU-RO/KI-RO's *functional* reading
  ("total"/"owed") is treated as an accepted starting point across rival
  language-identification camps, not for its Kartvelian claim, which this
  project takes no position on.
- "Linear A po-to(-)ku-ro (HT 122b.6; HT 131b.4) = Hurrian puttu(-)kuru"
  (academia.edu) — again cited only for corroborating the base KU-RO
  reading, not for its own Hurrian proposal.
- World History Encyclopedia's "Linear A Script" overview.

**Cross-check against the mwenge/LinearA data file (see above):** grepping
the same directly-fetched `LinearAInscriptions.js` for exact-token matches
found **37 occurrences of `"KU-RO"`** and **16 of `"KI-RO"`** across the
1,684-entry file — consistent with (not proof of) the "recurring
administrative formula word" description in the literature above. This is
supporting frequency context from an unverified, unlicensed compilation, not
independent confirmation of the reading itself.

**Why this is a Confirmed Finding, not an Active Hypothesis, and not a
translation claim:** per `methods/falsification-standard.md`, this is a
report of existing, widely-cited field scholarship (predating this
project, like the already-logged Ventris 1952 finding), not a novel test
this project ran, and it makes no claim about the underlying language KU-RO
belongs to. It is a **functional/positional word identification**
(occurs at the tail of numeral lists, therefore glossed "total"), which is
a different and much weaker claim than a phonetic decipherment or a
language-family identification — it does not touch, and should not be
conflated with, SQ-2's sign-by-sign phonetic-value confidence tiers, since
no phonetic reading of KU-RO's signs is asserted or required for this
functional gloss to hold. Promoted to `knowledge-base/state.md` with this
distinction stated explicitly, and with the secondary-sourcing limitation
disclosed (read via WebSearch synthesis, not a full primary-paper read,
consistent with the egress constraint logged above).

## Next action

1. Either party, from an unblocked network: still need a direct read of
   `sigla.phis.me/paper.html` (three cycles running now) **and**, newly,
   of `cefael.efa.gr`'s claimed GORILA-scan hosting page, to check
   mwenge/LinearA's sourcing claim.
2. SQ-1: do not provisionally select mwenge/LinearA given its undetermined
   license; it is logged as a candidate and a source of the George Douros
   lead, not a selection.
3. SQ-4: extend this catalog entry with other recurring administrative
   terms (e.g. commodity ideograms, fraction signs) the next time this
   sidequest is picked up, and independently verify the KU-RO/KI-RO reading
   against a primary source (a GORILA-derived commentary or a peer-reviewed
   paper actually read in full) rather than resting on WebSearch synthesis
   indefinitely.
4. Skeptic role (next cycle or ChatGPT): review whether fetching
   `LinearAInscriptions.js` directly (rather than only README/LICENSE-type
   metadata, as the Navarre-AI audit deliberately restricted itself to) was
   appropriate under the standing no-bulk-download rule, and set a clearer
   line for future cycles if not.
