# SQ-2 — a second citation-scale batch classified (AB11–AB20), same rubric, same sources

**Trigger:** actively searching for an unclaimed thread this cycle. SQ-2's own AB01–AB10 pilot log
explicitly named its own next step: "the same rubric and these same two tables can be applied to any
further sign whose Linear B phonetic value falls in this grid." A citation-scale extension (not a bulk
pull — explicitly the distinction `config/sidequests.md` itself draws, same precedent as the mwenge/
LinearA single-file spot-check and the AB01–AB10 batch) doesn't need the pending full-dataset
authorization decision; it's the same bounded method, run on five more signs.

## What's already known / not done yet

Already known: the frozen three-tier rubric (Tier A = Meißner & Steele Table 1 membership, value+shape
confirmed; Tier B = Table 2-only, shape confirmed but not value; Tier C = neither), and AB01–AB10's
classification (9A/1B). Not done: any sign beyond that first ten-sign pilot batch.

## Method and why it's non-circular

Fetched SigLA's own sign-list page directly for AB11–AB20's assigned phonetic values (citation-scale, not
a bulk pull of the full ~300-sign/3,000+-occurrence dataset — same restraint as the AB01–AB10 batch).
Re-fetched the Meißner & Steele paper (same bitstream URL and SHA256 as already on file:
`f470071e5030720c0fd559aa0382e91d8015e92208cbbb37c626c9d3f44394c7`, confirmed to match on re-download) and
extracted its Table 1 and Table 2 grids in full via local `pypdf` text extraction. Classified each sign
against the frozen rubric exactly as written, not adjusted after seeing results.

## Honesty precommitment

Report every sign's tier exactly as the tables give it, and disclose plainly which signs in the AB11–AB20
range had no retrievable phonetic value at all rather than silently skipping them.

## Result

**SigLA's sign-list page gives phonetic values for only 5 of the 10 codes in this range**: AB11=`po`,
AB13=`me`, AB16=`qa`, AB17=`za`, AB20=`zo`. AB12, AB14, AB15, AB18, and AB19 do not appear with an
assigned value on the fetched page — disclosed as a real gap, not pursued further this cycle (may require
the `database.js` route already used for AB01–AB10, or may reflect signs SigLA itself doesn't assign a
simple value to).

| AB code | Value | In Table 1 (value+shape)? | In Table 2 (shape only)? | Tier |
|---|---|---|---|---|
| AB11 | po | Yes (p-row, o-column) | Yes | **A** |
| AB13 | me | Yes (m-row, e-column) | Yes | **A** |
| AB16 | qa | No (q-row is empty in Table 1) | Yes (q-row, a-column) | **B** |
| AB17 | za | No (z-row is empty in Table 1) | Yes (z-row, a-column) | **B** |
| AB20 | zo | No (z-row is empty in Table 1) | Yes (z-row, o-column) | **B** |

**Three of five land in Tier B this batch** — a notably different mix than AB01–AB10's 9A/1B. This is
consistent with, not contradicted by, the paper's own stated finding that entire consonant rows (q, w, z)
have no Table 1 membership at all — the q- and z-series are structurally absent from the value-confirmed
grid regardless of which specific sign within them is tested, not a property of `qa`/`za`/`zo`
specifically. The m- and p-series, by contrast, are two of the rows the paper calls out as nearly complete
in Table 1 (along with s and t) — consistent with `po` and `me` both landing in Tier A.

## Decision

SQ-2's classified-sign count is now 15 of ~300 (9A/1B from the first batch, 2A/3B from this one). The
pattern across both batches is already informative on its own: **which signs land in Tier A looks like it
tracks whole consonant-series membership in Table 1 (m/p/s/t rows strong, q/w/z rows structurally absent)
rather than being scattered unpredictably** — worth stating as a working observation, not yet a formal
finding, since only 2 of the paper's 12 consonant rows (q, z) have been directly tested this way so far.
A natural next citation-scale batch would deliberately sample from the w-row (also structurally empty in
Table 1) and more of the k-row (present in Table 1, not yet tested) to check whether this pattern holds.
