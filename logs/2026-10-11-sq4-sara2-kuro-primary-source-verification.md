# SQ-4 — primary-source verification of KU-RO and a new administrative term, SA-RA2

## Precommitment self-review (written before fetching)

**Known:** SQ-4's own 2026-09-25 status note named the concrete next action for its numeral/
ideogram half: "extend to other recurring administrative/numeral-ideogram conventions, and get
a primary-source-verified read of KU-RO/KI-RO (not just WebSearch synthesis)." Every subsequent
SQ-4 cycle went into the libation-formula half instead; this specific next action was never
picked up. The project's own prior frequency spot-check (mwenge/LinearA corpus, unverified
candidate source) found 37 KU-RO occurrences — a number from this project's own corpus scan, not
yet independently cross-checked against a scholarly source's own count.

**Not done yet:** no primary academic source has been directly fetched and read for KU-RO or
any other recurring administrative term beyond the WebSearch-synthesis tier.

**Design and why it's non-circular:** search for an academic (not Wikipedia-summary) source
discussing KU-RO/KI-RO directly, then download and locally extract its actual text (the
project's established `curl` + `pypdf` workaround for PDFs WebFetch can't extract) rather than
relying on a search engine's own synthesis of the source.

**Honesty precommitment:** report whatever the source actually says, including if it
corroborates, contradicts, or is simply silent on this project's own prior frequency count — and
disclose plainly if a term other than the one searched for turns out to be the more
substantively verifiable finding.

## Findings

**Source**: Lela Chotalishvili, "Minoan SA-RA2 and Mycenaean Texts (One Instance of Linguistic
Encounter)," *Phasis* 13-14 (2010-2011), pp. 155-166 — a peer-reviewed classical-studies journal
(Tbilisi State University). Directly downloaded (`curl`) and text-extracted locally (`pypdf`,
WebFetch's own extraction failed on the raw PDF binary — the same recurring tooling limitation
this project has worked around before).

**KU-RO, independently corroborated at primary-source tier**: the paper states KU-RO ("sum"/
"total") is "the most recurrent formative" in Linear A economic texts, "found 37 times" —
**an exact match to this project's own prior frequency count** from an independent corpus
(mwenge/LinearA), now corroborated by a named scholarly source rather than resting on this
project's own unverified corpus scan alone. The paper confirms KU-RO's functional role: closing
a list of goods, weapons, or manpower in Hagia Triada-style economic tablets.

**A new administrative term, not previously catalogued — SA-RA2**: the paper's actual subject is
a *different* term, SA-RA2, described as "the second most recurrent formative" in Linear A
economic texts (21 occurrences), cited across specific named tablets (HT 11b, HT 18, HT 28a,
HT 28b, HT 30, HT 32, HT 33, HT 34, HT 36a, HT 90, HT 93a, HT 94a, HT 99a, HT 100, HT 101, HT 102,
HT 105, HT 114a, HT 121, HT 125a, HT 130). SA-RA2 appears before specific commodity ideograms
(8 times before ideogram "120," conventionally "wheat"; 5 times before ideogram "303," which
Georgiev identifies with Linear B ideogram "125," "cypress"), and on two occasions directly
follows KU-RO itself (HT 94a.3, HT 100.4) — a real, tablet-cited structural relationship between
the two terms, not an assumption.

**A disclosed structural comparison to Linear B, from the paper itself**: the author compares
SA-RA2 to Linear B's pe-mo/pe-ma ("seed, grain"), which occupies the equivalent position before
the same commodity ideogram ("120") in Linear B economic texts — but notes the quantities
following SA-RA2 (e.g. 976, 58, 40, 41) are far larger than typical pe-mo figures (mainly small,
up to ~94), leading the author to suggest SA-RA2 likely does **not** indicate a plot-size
measure the way pe-mo sometimes does — a specific, sourced caution against over-mapping the
two systems onto each other.

## Outcome vs. the named next action

Partially fulfills the 2026-09-25 next action: KU-RO is now primary-source-verified (not just
WebSearch synthesis), and a genuinely new administrative/numeral-adjacent convention (SA-RA2)
is catalogued with full tablet citations — directly matching "extend to other recurring
administrative... conventions." **KI-RO specifically was not covered by this source** — this
paper doesn't discuss it at all; a primary-source-verified read of KI-RO remains open for a
future cycle, not resolved here.

## Limitation disclosed

This is one paper's own reading, not cross-checked yet against a second independent source the
way the libation-formula table was. The Georgiev ideogram-125/"cypress" identification is
reported as the paper's own citation, not independently verified against Georgiev's original
work this cycle.
