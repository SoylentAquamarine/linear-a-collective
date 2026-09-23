# Data

Source material for the project, versioned so every finding is
reproducible.

## Present

Nothing yet. See `config/sidequests.md` SQ-1 (corpus canonicalization) and
SQ-2 (sign-value confidence atlas) — both are required first groundwork
before any statistical or linguistic analysis can begin.

## Needed

- **Canonical transliterated corpus** — a rights-clear, machine-readable
  source covering as much of the surviving corpus as possible (commonly
  cited as several hundred to roughly 1,400 inscriptions depending on
  counting convention), using a documented reference numbering, that
  preserves reading uncertainty rather than silently resolving it. GORILA
  (Godart & Olivier's *Recueil des inscriptions en linéaire A*) is the
  commonly cited standard reference; its digital availability and rights
  status are not yet verified. Not yet selected. Do not bulk-download
  candidate sources without explicit user authorization.
- **Sign-value confidence atlas** — for every Linear A sign, whether its
  Linear-B-derived phonetic value is directly-attested, inferred, or
  unknown, with the basis for each classification. This is a genuinely
  different data need than the sibling Voynich/Rongorongo projects have,
  since Linear A inherits a partially-reliable, partially-uncertain reading
  system from Linear B rather than needing one built from nothing.
- **Normalization script** — once a source is selected, a documented,
  reproducible script to turn it into a form the Statistician can run
  frequency/entropy analysis on, without losing or silently resolving
  ambiguity, and without losing sign-value confidence tagging.
- **Reference/comparator corpora** — Linear B statistical and phonotactic
  data (a genuine, directly relevant comparator unavailable to the sibling
  projects), plus natural-language and candidate-family baselines (pre-
  Greek Aegean, Luwian/Anatolian, others) for the Linguist and Cryptanalyst
  to compare against. To be added as specific hypotheses are tested, not
  bulk-loaded up front.

## Convention

Any file added here should note its source URL, retrieval date, and
version/checksum in a companion `.source.md` (or in this README) so
provenance is never lost.
