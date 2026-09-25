# 2026-09-25 — SQ-1: SigLA coverage/uncertainty-handling evidence via triangulated WebSearch; provisional source selection

**Agent/role:** Claude, acting as Data Steward function (per
`config/research-department.md`'s role list).
**Responding to:** Steering Committee Meeting #1's action item ("read
`sigla.phis.me/paper.html` directly ... report SigLA's document/sign
coverage and uncertainty-preservation"), still open after three prior
cycles (`logs/2026-09-23-sq1-sq2-corpus-and-signvalues.md`,
`logs/2026-09-23-sq1-navarre-ai-provenance-audit.md`,
`logs/2026-09-25-sq1-sq4-lineara-explorer-and-kuro-kiro.md`), and Meeting
#1's own efficiency-check decision ("search for an HTML abstract/summary
page or a quoted-phrase search as a cheaper first probe before fetching a
raw PDF directly").

## What was NOT re-attempted, and why

Per the standing guidance already recorded in this project (three cycles
of direct fetches to `sigla.phis.me`, `en.wikipedia.org`, `arxiv.org`,
`doi.org`, `scholar.google.com`, `jstor.org`, `tandfonline.com`,
`academic.oup.com`, `researchgate.net`, and mirrors — all blocked, most
recently confirmed via `curl "$HTTPS_PROXY/__agentproxy/status"` showing
the same 403 policy-denial pattern for `en.wikipedia.org` and `arxiv.org`
again this session), this cycle did not re-attempt a direct fetch of
`sigla.phis.me/paper.html` itself. It did try two adjacent, previously
untried direct fetches to see whether the block is truly domain-general or
specific to a narrower list: `https://www.archaeology.wiki/...` and
`https://www.repository.cam.ac.uk/items/...` (Cambridge Apollo repository
record for the SigLA paper) and `https://site.unibo.it/inscribe/en/...`
(the INSCRIBE project's own page on SigLA). **All three were also
`EGRESS_BLOCKED`.** This further confirms the block is broad (most
academic/reference-adjacent domains), not a SigLA-specific policy —
consistent with, and now extending, the three-cycle-confirmed finding
already in `config/sidequests.md`.

## What was tried instead: triangulated WebSearch synthesis

Three separate `WebSearch` queries were run, each returning a different but
overlapping set of source links, with an AI-synthesized answer drawn from
their indexed snippets (not this session fetching the pages itself):

1. `SigLA "Signs of Linear A" Salgarella Castellan database paper coverage
   documents signs uncertainty damage`
2. `SigLA Linear A database "damaged" OR "uncertain" OR "ambiguous" sign
   reading encoding`
3. `"SigLA" Linear A "400 inscriptions" OR "300 signs" OR "3,000"
   occurrences database`

Source links returned across the three queries (title, URL, as returned by
the tool — not independently fetched this session, since each domain
tried directly above was blocked):
- Semantic Scholar paper pages for both the paper's title variants
- academia.edu paper page
- `www.repository.cam.ac.uk` (Cambridge Apollo repository record)
- `www.fluxus-editions.fr/gla5-salg.pdf` (a PDF mirror)
- `www.archaeology.wiki` — two separate blog posts (2021-01-27,
  2021-02-18)
- `www.inscribercproject.com/SigLA/paper.html` (another mirror)
- `site.unibo.it/inscribe/en/linear-a-sigla` (the INSCRIBE project's own
  page)
- `sigla.phis.me/` and `sigla.phis.me/paper.html`/`paper.pdf` themselves
- Three unrelated recent-news links (sci.news, greekreporter.com,
  historyback.com) — not used as sourcing, listed for completeness

**Consistent, corroborating figures across all three independent query
results (not from a single source or a single search):**
- SigLA comprises **a list of 300 standard signs**, drawn from
  **400 Linear A inscriptions copied by hand** by the researcher (Ester
  Salgarella), with **more than 3,000 individual sign occurrences**
  ("individual signs found within the inscriptions") currently searchable.
- The database is explicitly described as **"still under construction"**,
  with the stated aim of eventually covering "all inscriptions known to
  date" — i.e. it does **not** yet claim full-corpus coverage. 400
  inscriptions is well short of the ~1,400–1,534 total figure range this
  project already logged as contested (see `knowledge-base/state.md`).
- On uncertainty/damage handling: the synthesis (drawing specifically on
  the two archaeology.wiki posts and the paper's own abstract as indexed)
  describes "uncertain readings, unknown word boundaries, uncertain
  function performed by signs in isolation, and ambiguous standard
  terminology" as an explicit, named design challenge the database was
  built to address, and separately states the database includes
  "epigraphical features such as erasures" for display/analysis — i.e.
  damage is a first-class, retained feature, not silently dropped. It also
  explicitly distinguishes three senses of "sign" (standardised shape /
  a particular occurrence / a graphic variant) as part of its own
  classification scheme, which is exactly the kind of granularity SQ-1's
  selection criterion was looking for.

**Disclosed limitation, matching this project's established bar for
WebSearch-synthesized findings (see the KU-RO/KI-RO entry,
`logs/2026-09-25-sq1-sq4-lineara-explorer-and-kuro-kiro.md`):** this is a
secondary-sourced synthesis of indexed snippets from multiple independent
pages describing the same paper/database, not a primary read of
`sigla.phis.me/paper.html` itself (still blocked, four cycles running).
The exact data-format-level mechanism for flagging uncertain/damaged signs
(e.g. a specific field, symbol, or null convention) is still not confirmed
— only that uncertainty/damage is treated as a named design concern and a
retained, displayed feature, not that it is preserved in a fully specific,
implementation-verifiable way. That last, finer-grained confirmation still
requires either a direct paper read or direct inspection of SigLA's actual
per-sign data (not attempted this cycle — see Next action).

## Decision: SQ-1 provisional source selection

Given three cycles of confirmed environmental blockage on the single most
direct path to full certainty (reading the paper), and enough now-
triangulated evidence to compare the three logged candidates on their
existing merits, this cycle makes the provisional selection call rather
than leaving SQ-1 open a fourth+ cycle on the same blocked dependency:

| Candidate | Institutional attribution | License | Live | Coverage (as found) | Uncertainty handling |
|---|---|---|---|---|---|
| **SigLA** | Yes — Ester Salgarella (Cambridge-affiliated research) + Dr. Simon Castellan (Univ. of Rennes) | CC BY-NC-SA 4.0, confirmed | Yes, confirmed 2026-09-23 | 400 inscriptions / 300 signs / 3,000+ sign occurrences, partial, still-expanding | Named design concern; erasures retained; exact field-level scheme unconfirmed |
| Navarre-AI/linear-a | No — single maintainer, self-disclosed non-institutional | Dual CC BY 4.0 / CC BY-NC-SA 4.0, confirmed | Yes | 1,884 records / 1,665 objects / 4,936 sign occurrences (broader) | 358/4,936 occurrences flagged `certain: false` (self-reported) | Disclosed and withdrew an entire findings report + 14 benchmark folders after a data-import defect and an external audit disagreeing with 331/544 claims |
| mwenge/LinearA + lineara.xyz | Partial — cites GORILA + named scholar George Douros, but no clear institutional home for the compilation itself | **None** — no LICENSE file found | Yes | 1,684 documents (broader) | Not established this project |

**Provisional selection: SigLA**, for SQ-2's forthcoming sign-value
classification work to build on, on the strength of its institutional
attribution, clean and confirmed license, and now-triangulated coverage/
uncertainty-handling profile — the strongest combination of rights-clarity
and credibility of the three, even though its raw coverage (400
inscriptions) is smaller than the other two candidates and than the full
corpus. This is **provisional, not final**: it does not resolve whether
SigLA's 400-inscription coverage will need supplementing from a broader
source (most plausibly Navarre-AI's structural/damage-flagging metadata,
already flagged in Round 2/3 as reusable regardless of which corpus is
selected, or a future direct SigLA-paper read) once SQ-2 classification is
under way and coverage gaps become concrete rather than abstract.

**What this decision does NOT do:** it does not authorize retrieving
SigLA's per-sign dataset in bulk. Per the standing no-bulk-download rule
and this project's own Round 4 self-scrutiny flag about the mwenge/LinearA
single-file fetch, actually pulling SigLA's data for SQ-2 classification
work is a separate step that should either (a) stay to the same narrow,
citation/count-spot-check scale as the mwenge/LinearA precedent, or (b)
require explicit user authorization if a fuller pull is judged necessary
— a decision for the next cycle picking up SQ-2, not this one.

## Next action

1. SQ-2 (sign-value confidence atlas) may now begin its first-pass
   classification design against SigLA as the working source, per
   `config/sidequests.md`'s own sequencing rule ("SQ-2 should begin as soon
   as SQ-1 has a provisionally selected source").
2. Still worth a direct primary read of `sigla.phis.me/paper.html` from any
   party/session with unblocked network access, specifically to confirm the
   exact field-level uncertainty/damage-encoding scheme — this is now a
   refinement question, not a blocking one.
3. Do not treat SigLA's 400-inscription coverage as the eventual full
   corpus; flag the coverage gap explicitly wherever SQ-2/SQ-3 results are
   reported, and revisit supplementing from Navarre-AI or a future GORILA
   digital source once concrete gaps are identified.
