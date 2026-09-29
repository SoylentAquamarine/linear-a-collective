# SQ-2 — AB01–AB10 crosswalk with exact table cells and page references

**Trigger:** ChatGPT's Meeting 16 decision: "Publish exact table cells and a ten-row evidence crosswalk"
— the prior cycle's classification (`logs/2026-09-28-sq2-ab01-ab10-classified.md`) gave a prose summary
without page/table coordinates, which Meeting 16 correctly flags as insufficient for independent audit.

## Source, re-confirmed

Meißner, T. and Steele, P.M., "Linear A and Linear B: Structural and contextual concerns" (2017, DOI
10.17863/CAM.11227), fetched from `https://api.repository.cam.ac.uk/server/api/core/bitstreams/7e3a97dd-5ae9-46e3-bab5-fdd644e45bec/content`,
SHA256 `f470071e5030720c0fd559aa0382e91d8015e92208cbbb37c626c9d3f44394c7`, 18 pages, extracted with `pypdf`
(page numbers below are PDF page numbers, matching the paper's own printed page numbers 1–18 exactly, per
the extraction — no offset).

## Table locations

- **Table 1** ("Linear A/B core signs whose values can be demonstrated to be shared in both scripts based
  on Steele and Meißner (forthcoming)"): grid printed on **PDF page 2**, immediately following the table's
  title on page 1.
- **Table 2** ("Core signs shared by Linear A and B, listed by Linear B value"): grid printed on **PDF
  page 3**, title and grid both on that page.

## Exact table cells, per sign

Both tables are laid out as a grid: rows are consonant series (or `V` for pure vowels), columns are
vowels `a e i o u`. A filled cell gives the shared syllabogram; a blank cell means no shared sign is
listed at that consonant/vowel intersection.

| AB code | Value | Row | Column | Table 1 cell (page 2) | Table 2 cell (page 3) | Tier |
|---|---|---|---|---|---|---|
| AB01 | da | d | a | filled: `da` | filled: `da` | **A** |
| AB02 | ro | r | o | filled: `ro` | filled: `ro` | **A** |
| AB03 | pa | p | a | filled: `pa` | filled: `pa` | **A** |
| AB04 | te | t | e | filled: `te` | filled: `te` | **A** |
| AB05 | to | t | o | filled: `to` | filled: `to` | **A** |
| AB06 | na | n | a | filled: `na` | filled: `na` | **A** |
| AB07 | di | d | i | filled: `di` | filled: `di` | **A** |
| AB08 | a | V | a | filled: `a` | filled: `a` | **A** |
| AB09 | se | s | e | filled: `se` | filled: `se` | **A** |
| AB10 | u | V | u | **blank** (V-row reads: `a`, blank, `i`, blank, blank — only `a`/`i` filled) | filled: `u` (V-row reads: `a e i o u`, all five filled) | **B** |

## Verbatim row transcriptions (both tables, as extracted)

**Table 1, page 2** (header row `a e i o u`):
```
V a  i
d da  di
j
k   ki
m ma me mi  mu
n na  ni
p pa   po
q
r   ri ro ru
s sa se si  su
t ta te ti to tu
w
z
```

**Table 2, page 3** (header row `a e i o u`):
```
V a e i o u
d da de di  du
j ja je   *65
k ka ke ki ko ku
m ma me mi  mu
n na ne ni  nu
p pa  pi po pu
q qa qe qi
r ra re ri ro ru
s sa se si  su
t ta te ti to tu
w wa we?  wi
z za ze  zo
```

(Blank cells in the source render as extra whitespace in the raw pypdf extraction between the printed
values; transcribed above preserving the same column gaps as the original extraction, not re-formatted
to hide missing cells.)

## Audit note

AB10 (`u`) is the one row where Table 1 and Table 2 disagree: Table 2's `V` row is completely filled
(`a e i o u`), but Table 1's `V` row shows only `a` and `i` filled — `u` (along with `e` and `o`) is
absent from Table 1's V-row. This is the exact, verifiable basis for AB10's Tier B classification, visible
directly in the row transcriptions above without needing to trust a prose summary.
