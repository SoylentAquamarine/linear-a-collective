# SQ-4 — Libation-formula instance table

Central deliverable per `config/sidequests.md` SQ-4: every attested instance of the libation-formula
phrase across libation-table inscriptions, its exact published wording and variants, and whether it
generalizes to all attested instances or rests mainly on the exemplar most often quoted.

**Status: single-source compilation, not yet cross-checked against a second primary source.** Every row
below is drawn from one peer-reviewed paper — Rose Thomas, "Some reflections on morphology in the
language of the Linear A libation formula," *Kadmos* 59(1–2): 1–23 (2020), DOI 10.1515/kadmos-2020-0001
(freely hosted, downloaded and text-extracted 2026-09-27; see
`logs/2026-09-27-sq4-libation-formula-table-compilation.md` for the full method). Thomas's own paper cites
GORILA (the standard Linear A corpus edition) for each transliteration, so this is a second-hand
transcription of a primary corpus, not this project's own reading of the original inscriptions or GORILA
directly — a real, disclosed limitation, not silently upgraded to primary-source tier.

## The standard formula

`a-ta-i-*301-wa-ja   X   ja/a-sa-sa-ra-me   u-na-ka-na-si   i-pi-na-ma   si-ru-te`

Six sequences; **X** is the varying dedicant-name (or, once, place-name) slot. The final three sequences
(`u-na-ka-na-si i-pi-na-ma si-ru-te`) are reported as far less variable across inscriptions than the first
three, per Thomas's own account — this table focuses on the first three, where the documented variation
actually is.

## Opening sequence (`a-ta-i-*301-wa-ja` and variants)

| Inscription | Attested form | Notes |
|---|---|---|
| IO Za2.1 | `a-ta-i-*301-wa-ja` | one of 11 complete occurrences of the standard form |
| IO Za3 | `a-ta-i-*301-wa-ja` | ″ |
| IO Za7 | `a-ta-i-*301-wa-ja` | ″ |
| KO Za1 | `a-ta-i-*301-wa-ja` | ″ |
| PK Za12 | `a-ta-i-*301-wa-ja` | ″ |
| SY Za1 | `a-ta-i-*301-wa-ja` | ″ |
| SY Za2 | `a-ta-i-*301-wa-ja` | ″; this inscription also has the possible OLIV (olive) ideogram in the third-sequence slot |
| SY Za3 | `a-ta-i-*301-wa-ja` | ″ |
| SY Za4 | `a-ta-i-*301-wa-ja` | ″; third sequence here is the variant `pa3-ni-wi`, not `ja/a-sa-sa-ra-me` |
| SY Za8 | `a-ta-i-*301-wa-ja` | ″ |
| TL Za1 | `a-ta-i-*301-wa-ja` | ″ |
| PS Za2.2 | `ta-na-i-*301-ti` | distinct variant, unique occurrence |
| IO Za6 | `ta-na-i-*301-u-ti-nu` | distinct variant, unique occurrence; formula truncated to first three sequences only on this inscription |
| IO Za8 | `a-na-ti-*301-wa-ja` (transcribed with a dot under the first `a`, marking an uncertain reading) | distinct variant, unique occurrence |
| PK Za11 | `a-ta-i-*301-wa-e` | distinct variant, unique occurrence; third sequence here is `a-sa-sa-ra-me` (no `ja-` prefix) |
| ZA Zb3 | `a-ta-i-*301-de-ka` (dotted letters marking uncertain readings) | distinct variant, unique occurrence |
| AP Za1 | `ja-ta-i-*301-u-ja` | distinct variant, unique occurrence |

**Invariant core**: the sequence `-i-*301-` never varies across any attested form above — Thomas identifies
this as the word's root, with four possible prefixes (`a-/ja-`, `ta-`, `na-`, `t-`) and seven possible
suffixes (`-wa-/-u-`, `-ja-`, `-ti-`, `-nu-`, `-e-`, `-de-`, `-ka`) attaching to it across the attested
forms.

## Third sequence (`ja-/a-sa-sa-ra-me` and variants)

| Inscription | Attested form | Notes |
|---|---|---|
| (multiple, unspecified in the source paper's summary passage) | `ja-sa-sa-ra-me` | the more common of the two standard prefix forms |
| PK Za11, PR Za1 | `a-sa-sa-ra-me` (no `ja-` prefix) | the less common standard form |
| SY Za4 | `pa3-ni-wi` | non-standard substitution in this slot |
| KO Za12 | possibly `i-da-a` | non-standard substitution, reading itself uncertain per the source |
| SY Za2 | possibly the `OLIV` (olive) ideogram | substitution proposed by Davis (2013) and shown by Godart & Olivier (GORILA V) |

## What generalizes and what doesn't

**Generalizes across a real, multi-site set**: the opening sequence's root (`-i-*301-`) and its general
templatic shape (prefix + root + suffix) hold across all 17 individual inscriptions catalogued above,
spanning at least 6 distinct find-sites (IO, KO, PK, SY, TL, PS, ZA, AP, PR — abbreviations per the
source's own site-code convention, not expanded here since the paper's own site-name key was not extracted
in this pass). **Does not generalize word-for-word**: only 11 of the 17 listed inscriptions carry the
exact standard opening form; the remaining 6 each carry a distinct one-off variant. The third sequence
shows a similar pattern: a dominant standard form with a documented but shorter list of substitutions.

## Site-code key (partial — disclosed confidence levels, not all confirmed)

Attempted expansion of the site-code abbreviations via WebSearch and a direct fetch of Mnamon (Scuola
Normale Superiore's academic reference project on ancient writing systems), 2026-09-27:

| Code | Full site | Confidence |
|---|---|---|
| IO | Iouktas (Mount Iouktas) | **Confirmed** — directly stated in a search result quoting "IO Za 2 (a stone libation table from Mount Iouktas)" |
| KO | Kophinas | **Confirmed** — WebSearch-tier, not independently cross-checked against a second source |
| PK | Palaikastro | **Confirmed** — matches this project's own already-cited academia.edu paper title ("...Palaikastro (PK Za 27)") |
| SY | Kato Syme | **Confirmed** — WebSearch-tier, not independently cross-checked |
| PS | Petsophas | **Confirmed** — matches the same already-cited paper title pattern (Petsophas is where Palaikastro's libation tables were found) |
| ZA | Zakros (plausible) | **Unconfirmed, plausible pattern match only** — Zakros appears in Mnamon's site list and the code's first two letters match; no direct code-to-name pairing found |
| TL | Tylissos (plausible) | **Unconfirmed, plausible pattern match only** — same basis as ZA above |
| PR | Prassa (plausible) | **Unconfirmed, plausible pattern match only** — Prassa appears in this same paper's own citation list (Platon 1958, "Inscribed libation vessel from a Minoan house at Prassa, Heraklion") for a libation-formula-bearing object, making this a reasonable but not confirmed inference |
| AP | (not identified) | **Unresolved** — no plausible candidate found among the sites named in sources checked this cycle |

**Disclosed limitation**: only IO, KO, PK, SY, and PS are treated as confirmed; ZA, TL, and PR are pattern-based guesses, not verified pairings, and are marked as such rather than presented with false confidence; AP remains completely unidentified. GORILA's own published site-code key (not consulted directly this cycle) would resolve all of these definitively.

## What remains open

- The three "plausible, unconfirmed" and one "unresolved" site codes above would need GORILA's own
  published key, or a second independent source, to confirm or replace with a verified name.
- This table has not been cross-checked against GORILA directly or a second secondary source — a real
  limitation, disclosed per this project's own primary-source-verification discipline.
- The final three sequences (`u-na-ka-na-si i-pi-na-ma si-ru-te`) are asserted as "far less variable" but
  no instance-by-instance table for them was compiled in this pass, only for the first three sequences
  where Thomas's own account documents specific variation.

## Update (2026-10-04) — a genuine second-source cross-check, partially closing the open item above

Per SQ-4's own standing "cross-check against a second source" item, searched independently (not via
Thomas 2020) and found corroborating material, cited across two independent secondary sources (an
academia.edu paper, "Minoan Inscriptions on Libation Vessels," and search-synthesized context from
scholarly discussion of the formula's grammar — neither of these is GORILA itself, still disclosed at
secondary-source tier):

- **The "11 complete occurrences" figure independently confirmed**: a source independent of Thomas states
  the opening sequence appears "in 11 complete occurrences at various archaeological sites including
  Iouktas, Knossos, Palaikastro, Syme, and Trypiti" — matching Thomas's own count exactly, and the site
  list matches this table's own site codes (IO, KO, PK, SY, TL) without having consulted this table first.
- **The "X = varying dedicant-name (or, once, place-name) slot" caveat independently confirmed and made
  specific**: this project's own table already carried that parenthetical caveat (written before this
  cross-check). The independent source identifies the exact case: **`JA-DI-KI-TU` appears only in IO Za 2**
  and is "widely accepted as meaning 'Dikte (place name)'... 'of Dikte' or 'from Dikte'" — Mount Dikte, a
  sacred peak-sanctuary site in eastern Crete associated with Minoan ritual. This is not a contradiction of
  the existing table; it is the specific instance the existing caveat was already (correctly) anticipating,
  now independently sourced and named.
- **New structural detail, not in Thomas's table as extracted**: the same source describes the formula as
  parsed into "6 positional slots (verb, place-name, dedicant, object, subordinate verb, prepositional
  phrase)" — a grammatical-function breakdown worth checking against Thomas's own paper directly in a
  future pass, since it wasn't captured when the original table was compiled.

- **Update (2026-10-05) — checked directly against Thomas's own text, attribution corrected**: re-extracted
  Thomas 2020's primary text (see `logs/2026-10-05-sq4-libation-slot-breakdown-checked-against-thomas.md`
  for method) and confirmed the "6 positional slots" description in substance — verb (VSO, first
  sequence); subject/dedicant-or-place-name (second sequence, marked X); object noun phrase (third
  sequence, usually `ja-/a-sa-sa-ra-me`); and a three-part non-finite clause (final three sequences,
  "requesting divine favour"). **But Thomas's own text attributes this syntactic breakdown to Davis
  (2013/2014), citing his word-order analysis, not as her own original structural claim** — and Thomas's
  text never uses the term "subordinate verb"; the independent secondary source's phrasing was a loose
  paraphrase of Davis's "non-finite clause." No table content changes; this adds the correct named
  attribution the secondary source's wording obscured.

**Caution, disclosed**: this same search also surfaced several self-published, non-peer-reviewed
"decipherment" claims for Linear A (e.g., works classifying the underlying language as a Semitic branch) —
these are not relied upon here and should be treated with the same skepticism this project applies to
similar claims in sibling projects, not cited as if validated.

**Status change**: the "single-source, not yet cross-checked" caveat at the top of this file is now
partially addressed — the headline count and the one documented exception are independently corroborated,
though this is still secondary-source-tier corroboration, not a direct GORILA read.
