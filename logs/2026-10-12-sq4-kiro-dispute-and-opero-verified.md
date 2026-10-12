# SQ-4 — KI-RO's "deficit" reading is contested; Linear B's real debt term (o-pe-ro) verified

## Precommitment self-review (written before research)

**Known:** KI-RO specifically remained unverified at primary-source tier after last cycle's
SA-RA2/KU-RO work — the Phasis paper found didn't cover it. The existing Confirmed Finding
describes KI-RO as conventionally read "deficit/owed," sourced only via WebSearch synthesis,
without flagging any scholarly disagreement.

**Not done yet:** no search had specifically targeted KI-RO's own scholarly reception, or
checked whether "deficit/owed" is actually settled or contested.

**Design and why it's non-circular:** search for KI-RO's own literature directly, then attempt
to directly fetch the strongest-looking primary source found, reporting honestly whether it
actually supports the claim already on file or complicates it.

**Honesty precommitment:** if a genuine scholarly dispute is found, report it as a dispute —
don't pick whichever side was already on file and treat the search as confirming it.

## Findings

**A real scholarly dispute, not previously disclosed in this project's record**: Duccio
Chiapello (publishing under the contested "Minoan Greek" hypothesis, search-synthesis tier,
not independently fetched this cycle) reads KI-RO as "debt," pairing it in his analysis of
tablet HT 88 with A-DU ("payment"/"return") to argue the tablet records goods already repaid
alongside goods still owed. **Against this**: R. and E. Cash's analysis of tablet HT 123
(reported via an Aegeus Society abstract, search-synthesis tier) "strongly suggests that Linear
A ki-ro does not have the value of 'deficit' or similar." This is a genuine, live disagreement
between named scholars, not a settled reading — the existing Confirmed Finding's "deficit/owed"
framing should be read as the majority/conventional view, not an uncontested fact.

**Linear B's actual debt/deficit term, now directly verified at primary-source tier**: directly
fetched (curl + local `pypdf` extraction) R. J. E. Thompson, "Mycenaean qe-te-o and Greek
adjectives in -τέος and *-eyo-," *Ariadne* (DOI 10.26248/ariadne.vi.1869; originally presented
at the 15th International Mycenological Colloquium, 2021). The paper's own text, quoted
directly: "the term o-pe-ro and its abbreviation o, /ophelos/ 'debt, deficit,' ... clearly do
record shortfalls." Specific tablet examples given and confirmed in the extracted text:
- **PY Ma 222** (taxation record): assessed quantities equal the sum of payment (*a-pu-do-si*)
  entries plus *o-pe-ro* shortfall entries — e.g. 10 units paid + 13 units *o-pe-ro* = 23 units
  assessed.
- **PY Ac 1275** (personnel record): lists men present vs. missing, with *o-pe-ro* marking the
  missing count.
- **KN Do 927** (lambing record): *o-pe-ro* marks a shortfall against breeding targets.

**Disclosed limitation**: this paper is about Linear B's *qe-te-o*, contrasted against
*o-pe-ro* as a comparandum — it does not discuss Linear A's KI-RO at all. This verifies the
Linear B side of the comparison at primary-source tier; it does **not** independently verify
that KI-RO itself means "debt," which remains exactly as contested as the dispute above
describes.

## Outcome

This both advances and complicates the standing 2026-09-25 next action. Advances it: Linear B's
genuine debt/deficit term (*o-pe-ro*) is now primary-source-verified with three specific tablet
citations, a real comparandum for any future KI-RO check. Complicates it: KI-RO's own
"deficit/owed" reading, treated as settled in this project's existing Confirmed Finding, is
shown to be genuinely disputed in the current literature — a correction worth appending rather
than silently leaving the original framing unqualified.

## Decision

Append this dispute to the existing KU-RO/KI-RO Confirmed Finding in `knowledge-base/state.md`
rather than rewriting it — the original "conventionally read as... deficit/owed" framing is not
false (it is the majority view), but it should no longer stand unqualified.
