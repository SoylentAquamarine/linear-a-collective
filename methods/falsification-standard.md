# Falsification and Promotion Standard

This is the minimum bar for moving an interpretation into **Active
Hypotheses**. It is deliberately stricter than the bar for recording a
measurement in **Confirmed Findings**. A measurement can be reliable while
supporting several incompatible explanations.

## Minimum bar for Confirmed Findings

Confirmed Findings is a much lower bar than Active Hypotheses — a
measurement or result, not an interpretation, and it doesn't need
alternatives explicitly ruled out. But every entry should still be well
documented and reproducible, not left to habit. Before a PR adds a bullet
to `knowledge-base/state.md`'s Confirmed Findings, it should have:

- a script, a manifest, or a directly-read and cited image/text protocol
  that produced the number or claim — not a description of a result
  alone, with nothing behind it a reader could rerun;
- the actual output (a summary JSON, a report, or both) committed to the
  repo, not only quoted or paraphrased inline in the bullet;
- enough provenance (source commit, checksum, seed, sample definition)
  that a third party could rerun it and reasonably expect the same
  result;
- for any claim built on sign readings, the sign-value confidence tier
  (borrowed-confident, inferred, or unknown — see `config/sidequests.md`
  SQ-2) of every sign involved, disclosed plainly, not silently assumed
  uniform;
- for anything resting on an external secondary source (a search-engine
  summary, a paper or catalog not read directly), an explicit disclosure
  of that limitation in the same entry — never presented as if it were
  independently verified when it wasn't. This applies with particular force
  here: much of what is "commonly cited" about Linear A in casual secondary
  sources is itself contested or imprecise in the primary scholarly
  literature (inscription counts, GORILA's exact scope and availability,
  and specific decipherment or language-identification claims all vary by
  source), so a claim's provenance chain matters more than usual.

This does not require independent adversarial review the way Active
Hypotheses does — that remains the harder bar. It requires that a
Confirmed Finding always be *checkable*, even when no one has checked it
yet.

## Required hypothesis card

Before running its decisive test, the proponent must record:

1. **Claim** — one operational statement narrow enough to fail.
2. **Alternatives** — at least the strongest competing named language-
   family explanations (e.g. if proposing a pre-Greek Aegean substrate,
   the strongest Luwian/Anatolian and "no candidate currently supported"
   alternatives), or a reason one family is inapplicable.
3. **Discriminating prediction** — an outcome expected under the claim and
   not equally expected under the named alternatives.
4. **Failure condition** — a numerical threshold, held-out pattern, or
   catalog mismatch that would count against the claim. This may not be
   invented after seeing the result.
5. **Units and controls** — the inscriptions, sign sequences, genres
   (administrative vs. religious/votive), sites, comparison corpora,
   exclusions, and randomization unit.
6. **Dependencies** — transliteration, sign-value confidence tier
   assumptions, segmentation, and site/genre-attribution assumptions that
   could manufacture the result.

## Evidence required for promotion

A candidate can enter **Active Hypotheses** only when all of the following
are present:

- a reproducible script or a cited, inspectable image/catalog protocol;
- an effect size and uncertainty or an equally explicit qualitative
  decision rule, not only a p-value;
- a negative or shuffled control appropriate to the claim;
- sensitivity to at least the material transliteration/segmentation,
  sign-value confidence tier, and site/genre confounds identified in the
  hypothesis card — explicitly including a result recomputed using only
  borrowed-confident sign values, to check whether inferred or
  unknown-value signs are doing the work;
- a held-out or genuinely out-of-sample test when the claim was developed
  by exploring the same data;
- independent adversarial review by the other collaborator, including
  reproduction of the headline result or a documented reason reproduction
  is impossible;
- a statement of what the result does **not** distinguish.

Promotion means "worth sustained falsification," not "probably deciphered."
Confirmation requires surviving the Skeptic's targeted test and explaining
evidence that the strongest alternative does not explain equally well.

## Automatic stop conditions

Do not promote when any of these applies:

- the observation was selected after inspecting the same test set and has
  no holdout;
- the effect disappears under one reasonable transliteration or
  segmentation policy;
- the effect disappears, or is substantially weaker, when restricted to
  borrowed-confident sign values only;
- the comparison changes inscription, genre, site, or sampling unit at the
  same time as the claimed variable;
- the proposed mechanism has enough unconstrained choices to fit arbitrary
  sequences;
- the result only restates a known corpus property (e.g. Zipf-like
  frequency) without a prediction that separates language-family
  hypotheses;
- an upstream correction has not been propagated through the full dependent
  analysis chain;
- the claim rests on matching a handful of signs or words to a target
  language without corpus-wide, held-out validation — the specific,
  publicly documented failure mode of virtually every prior claimed Linear
  A decipherment.

## Current consequence

At launch, the repository has no Confirmed Findings and no Active
Hypotheses — this is a genuine bootstrap state, not a placeholder awaiting
cleanup. The first substantive work is corpus canonicalization and the
sign-value confidence atlas (`config/sidequests.md`, SQ-1 and SQ-2), which
are themselves infrastructure, not findings.
