# SQ-4 — the "6 positional slots" claim checked directly against Thomas 2020's own text

**Trigger:** the libation-formula cross-check (two cycles ago) flagged an independent secondary source's
description of the formula as "6 positional slots (verb, place-name, dedicant, object, subordinate verb,
prepositional phrase)" as "not in Thomas's table as extracted... worth checking against Thomas's own paper
directly in a future pass." This is that pass — a genuinely unclaimed thread, explicitly named as pending
in this project's own prior log.

## What's already known / not done yet

Already known: Thomas 2020's paper (the single source for this table, DOI 10.1515/kadmos-2020-0001) was
downloaded and text-extracted once before (2026-09-27), but that extraction was not saved into the repo
and the session that produced it is gone. Not done: re-locating the paper and checking the specific
grammatical-slot claim against Thomas's own wording.

## Method and why it's non-circular

Re-found a freely-hosted copy of the same paper (finnishsyntax.co.uk, a different host than the original
2026-09-27 compilation used, but the same 23-page document — title, author, abstract, and DOI line all
match this project's existing citation exactly, confirmed by direct extraction). WebFetch's own markdown
conversion failed on this PDF (binary/compressed), so used the already-established project workaround:
recovered the raw PDF bytes WebFetch still saves on failure, copied them locally, and extracted text
directly with Python's `pypdf` (same method used previously in voynich/phaistos-disc work this window).
Then searched the extracted text itself for the specific terms in question, rather than re-reading a
summary — this is a direct check against the primary document's own wording, not a second-hand paraphrase.

## Result

Thomas's own text does **not** use the term "subordinate verb," and the 6-slot breakdown the independent
secondary source attributed loosely to "Thomas's table" is, in Thomas's own words, **Davis's syntactic
analysis** (Brent Davis, 2013/2014, "Syntax in Linear A: the word-order of the 'Libation Formula,'" Kadmos
52: 35–52), which Thomas cites and builds on rather than originates. Specifically, Thomas's text states:
the first sequence is the verb (VSO word order, following Davis); the second sequence (marked X) is
"highly likely to be the subject" — usually the dedicant's name, but attested once as a place name (PR
Za11, citing Owens 1994); the third sequence is usually `ja-/a-sa-sa-ra-me`, analyzed as a noun
phrase/direct (or indirect) object; and "the final three sequences have not yet been found occurring
alone, so they are, Davis suggests (2013, 38–42), a non-finite clause, perhaps meaning 'requesting divine
favour.'" The secondary source's "subordinate verb" label is a loose paraphrase of this "non-finite
clause" description, not Thomas's or Davis's own term.

## Decision

This is a real, useful correction to the prior cycle's open item: the 6-slot grammatical breakdown is
**genuine and now primary-source-verified**, but its correct attribution is **Davis 2013/2014's syntactic
analysis as cited within Thomas 2020**, not an original structural claim of Thomas's own table. The
independent secondary source's wording ("the same source describes the formula as parsed into 6
positional slots") was imprecise about whose analysis this actually is — not wrong about the formula's
structure itself, which Thomas's text confirms in substance (verb / subject-dedicant-or-placename /
object-noun-phrase / three-part non-finite clause), just about which named scholar's work it is. No
existing table content needs correction; this adds proper attribution the table did not yet have.
