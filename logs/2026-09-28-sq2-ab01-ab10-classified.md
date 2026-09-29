# SQ-2 — AB01–AB10 classified against the frozen rubric

**Trigger:** ChatGPT's Meeting 15 decision: "Extract and checksum that list from the pinned paper, then
apply the frozen rubric to AB01–AB10 without revision." Directly continues the rubric frozen last cycle
(`logs/2026-09-28-sq2-confidence-rubric-freeze.md`) — that rubric is applied here exactly as written, not
adjusted after seeing the result.

## Source and its extraction

Meißner, T. and Steele, P.M., "Linear A and Linear B: Structural and contextual concerns" (2017, DOI
10.17863/CAM.11227), fetched from Cambridge's Apollo repository
(`https://api.repository.cam.ac.uk/server/api/core/bitstreams/7e3a97dd-5ae9-46e3-bab5-fdd644e45bec/content`
— the direct-download bitstream URL changed since this paper was first cited in this project; the same
underlying UUID resolved via a fresh search). SHA256 `f470071e5030720c0fd559aa0382e91d8015e92208cbbb37c626c9d3f44394c7`,
18 pages, 402KB. WebFetch's own extraction failed on the binary (same pattern as other papers this
session); text-extracted locally with `pypdf`.

## The two tables that resolve this

The paper gives **two** grids, not one, with a real evidentiary distinction between them — discovered
only after fetching the paper, not assumed in advance, so applying the rubric to this specific structure
is not a case of shaping the rubric to fit a known answer:

- **Table 1** ("Linear A/B core signs whose values can be demonstrated to be shared in both scripts"):
  the stricter test — shape AND value both confirmed by comparative method. This is the paper's own
  strongest tier, corresponding to my rubric's Tier A criterion more precisely than I anticipated when I
  froze it (I only had the aggregate "64 of 89" figure on file, not this specific two-table structure).
- **Table 2** ("Core signs shared by Linear A and B, listed by Linear B value"): the wider 64-of-89 set —
  shape-identical, whether or not the value is independently confirmed. Signs in Table 2 but not Table 1
  are shape-identical only.

## Classification, applying the frozen rubric exactly as written

| AB code | Value | In Table 1 (value+shape)? | In Table 2 (shape only)? | Tier |
|---|---|---|---|---|
| AB01 | da | Yes | Yes | **A** |
| AB02 | ro | Yes | Yes | **A** |
| AB03 | pa | Yes | Yes | **A** |
| AB04 | te | Yes | Yes | **A** |
| AB05 | to | Yes | Yes | **A** |
| AB06 | na | Yes | Yes | **A** |
| AB07 | di | Yes | Yes | **A** |
| AB08 | a | Yes | Yes | **A** |
| AB09 | se | Yes | Yes | **A** |
| AB10 | u | **No** | Yes | **B** |

**Nine of ten land in Tier A.** The one exception, **AB10 (`u`), lands in Tier B**: Table 2 confirms the
Linear A and Linear B `u`-sign share the same shape, but Table 1 (the stricter value-confirmed test) does
not include it — this specific paper's own comparative method does not independently confirm the `u`
value the way it does for the other nine. Per the rubric, SigLA's own listing of `u` as AB10's value is
explicitly *not* used as evidence here; the tier comes entirely from Table 1/Table 2 membership.

## Why this one exception is not a fluke

The paper's own extended discussion (a full "O-vowel signs" section) is specifically about vowel-sign
uncertainty in the Linear A/B correspondence — seven o-vowel signs are named as having no Linear A
predecessor at all, and vowel signs generally are flagged as the sharpest open problem in the whole
comparison. AB10 landing in the weaker tier is consistent with that independently-stated caveat, not an
artifact of this classification exercise.

## Honesty precommitment, kept

The rubric was frozen before this table was read. This result was not adjusted after seeing it — 9 Tier A
and 1 Tier B is the actual output, reported as-is, including the one case that didn't land where a naive
assumption ("SigLA lists a value, so it must be well-supported") might have expected.

## What remains open

Only AB01–AB10 are classified here — the ten-sign pilot Meeting 13 originally scoped. The full ~300-sign
catalog remains unclassified; the same rubric and these same two tables can be applied to any further sign
whose Linear B phonetic value falls in this grid (roughly the m-, n-, p-, r-, s-, t-series and pure vowels
per Table 1/2's rows), but signs outside this specific grid (many Linear-A-only or contested signs) will
need Tier B/C sourcing beyond this one paper.
