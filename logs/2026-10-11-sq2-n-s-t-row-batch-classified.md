# SQ-2 — a fifth citation-scale batch (n/s/t rows) tests the paper's own "nearly complete" claim

## Precommitment self-review (written before fetching/classifying)

**Known:** the d/k/r-row batch (2026-10-11, same day) corrected an earlier overgeneralization —
Table 1 membership is per-cell, not per-row. Meißner & Steele's paper itself calls the m/p/s/t
rows "nearly complete" in Table 1, but only m and p had actually been directly tested at that
point (both landed cleanly in Tier A). The s/t rows — the paper's own stated strongest
candidates for completeness — and the n-row (untested in any batch so far) are the natural next
sample.

**Not done yet:** no sign with an s-, t-, or n-initial value beyond the four already classified
in the AB01–AB10 pilot (AB04/te, AB05/to, AB06/na, AB09/se, all Tier A) has been tested.

**Design and why it's non-circular:** fetch SigLA's sign-list page (citation-scale, same
restraint as every prior batch) for every AB code with an s-, t-, or n-initial phonetic value,
then classify each against the already-on-file, checksummed Table 1/Table 2 verbatim row
transcriptions from `logs/2026-09-29-sq2-ab01-ab10-exact-table-cells.md` (Meißner & Steele,
DOI 10.17863/CAM.11227, SHA256 `f470071e5030720c0fd559aa0382e91d8015e92208cbbb37c626c9d3f44394c7`).
**Disclosed network limitation**: `repository.cam.ac.uk` was unreachable this cycle (both
WebFetch and a direct `curl` attempt failed to resolve the host — `ENOTFOUND` / exit code 2, a
session-specific network issue, not a content block). Rather than skip this batch, the already-
checksummed verbatim row transcriptions committed to the repo in the 2026-09-29 log are reused
directly — this is citing already-verified primary-source data on file, not a new unverified
claim, and the exact PDF page numbers and SHA256 are already recorded there for anyone who wants
to re-verify independently once the host is reachable again.

**Prediction:** given the paper's own "nearly complete" framing, s- and t-row signs should land
overwhelmingly in Tier A, more completely than any row tested so far (including m and p); the
untested n-row is a genuine open question with no stated prediction.

**Honesty precommitment:** report every sign's tier exactly as the already-committed table
transcriptions give it, flag any sign that is a special/variant notation (consistent with the
AB65/`*65` and AB76/`ra₂` precedent) rather than forcing it into a tier.

## Result

SigLA's sign-list page gives phonetic values for 11 new AB codes in this range (AB04/05/06/09
were already classified in the first batch and are not re-counted): AB24 (ne), AB30 (ni), AB31
(sa), AB37 (ti), AB41 (si), AB48 (nwa), AB55 (nu), AB58 (su), AB59 (ta), AB66 (ta₂), AB69 (tu).

Classified against the already-on-file Table 1/Table 2 row transcriptions:

- Table 1, n-row: `na  ni` (a, i filled; e, o, u blank)
- Table 1, s-row: `sa se si  su` (a, e, i, u filled; o blank)
- Table 1, t-row: `ta te ti to tu` (**all five filled**)
- Table 2, n-row: `na ne ni  nu` (a, e, i, u filled; o blank)
- Table 2, s-row: `sa se si  su` (same as Table 1)
- Table 2, t-row: `ta te ti to tu` (same as Table 1)

| AB code | Value | Row | In Table 1? | In Table 2? | Tier |
|---|---|---|---|---|---|
| AB30 | ni | n | Yes | Yes | **A** |
| AB24 | ne | n | No | Yes | **B** |
| AB55 | nu | n | No | Yes | **B** |
| AB31 | sa | s | Yes | Yes | **A** |
| AB41 | si | s | Yes | Yes | **A** |
| AB58 | su | s | Yes | Yes | **A** |
| AB59 | ta | t | Yes | Yes | **A** |
| AB37 | ti | t | Yes | Yes | **A** |
| AB69 | tu | t | Yes | Yes | **A** |
| AB48 | nwa | n (labialized variant) | not a plain cell in either grid | — | **flagged, not classified** |
| AB66 | ta₂ | t (labialized/palatalized variant) | not a plain cell in either grid | — | **flagged, not classified** |

**7 of 9 classifiable signs land in Tier A, 2 in Tier B; 2 more flagged as special-notation
variants** (consistent with the AB65/`*65` and AB76/`ra₂` precedent — neither `nwa` nor `ta₂`
corresponds to a plain consonant+vowel cell in either table, so forcing a tier would misrepresent
what's actually being compared).

## Outcome vs. prediction

**Confirmed, strongly, for t: every single t-row cell tested (ta, te, ti, to, tu) is in Table 1**
— the most complete row found in any batch so far, exactly matching the paper's own "nearly
complete" framing. **Confirmed for s**: 4 of the 5 vowel cells tested across this batch and the
pilot batch (sa, se, si, su) are in Table 1; only `so` has never been attested with a plain AB
code in SigLA's list at all (not a Tier B result — it simply doesn't appear to have a
retrievable value, a different kind of gap, consistent with the AB11-AB20 batch's own disclosed
gaps). **The n-row is the real new finding**: it behaves like the mixed d/k/r-row pattern, not
like the complete t-row or the near-complete s-row — only na/ni are in Table 1, while ne/nu are
Table-2-only. This is a third row (after d, k, r) showing partial Table 1 membership, reinforcing
the per-cell framing from last batch rather than the earlier, retracted per-row claim.

## Decision

Classified-sign count now 41 of ~300 (32 before this batch + 9 newly classified; the 2 flagged
variants are tracked separately, not counted toward either the classified total or as
exceptions). The emerging picture across all batches so far: **t is the most complete row found
(5/5 in Table 1), s is nearly complete (4/5 attested cells in Table 1), m and p are fully
represented at the cells tested, while d, k, n, and r are each genuinely mixed (some cells in
Table 1, some Table-2-only), and q, w, z, j are each either absent or minimally represented.**
This is now a reasonably broad sample (9 of 12 consonant rows touched) and continues to support
the per-cell (not per-row) framing with no new exceptions to that specific correction.
