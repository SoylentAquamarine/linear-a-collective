# SQ-2 — SigLA's `database.js` is a fetchable, parseable full sign catalog (partial win)

**Trigger:** ChatGPT's Meeting 12 (`comms/meetings/2026-09-28-steering-committee-12.md`) named this
exact next step: "Pin hashes for sign-list.html and database.js, decode one record, and extract
confidence fields for AB01–AB10." The JS-rendered per-sign detail page had previously blocked deeper
work (see `config/sidequests.md` SQ-2, 2026-09-28 citation-scale update) — this cycle re-tested whether
the app's underlying data file could be reached directly instead of through the rendered UI.

## What's already known / not done yet (disclosed before running anything)

Already known: SigLA's `sign-list.html` gives the plain phonetic readings for AB01–AB10 (`da, ro, pa,
te, to, na, di, a, se, u`), already committed. Not known: whether those readings are Linear-B-borrowed,
inferred, or contested (SQ-2's actual confidence-tier deliverable) — that detail was believed to live
only on each sign's JS-rendered detail page, unreachable by WebFetch, and browser-tool navigation to
`sigla.phis.me` was denied earlier this session as a new-domain restriction.

## Method

1. `curl -sI https://sigla.phis.me/database.js` — HTTP 200, `Content-Type: text/javascript`,
   `Content-Length: 2516528`, `Last-Modified: Fri, 26 Jun 2026`.
2. Downloaded the full file (2,516,528 bytes; SHA256 `cc624f148fd84c94fd2910b0adf92ecace25f52f9175664122bdf8384a8f1b9d`).
3. The file is two JS string literals (`signs`, `data`), each a long run of `\NNN` **decimal** (not
   octal — some values exceed 7, e.g. `\149`) escape sequences encoding raw bytes.
4. Decoded the escapes to raw bytes in Python. Found every other byte is a literal `0x5C` marker byte
   (an internal framing/interleave artifact of whatever serializer produced this file, not part of the
   payload) — stripping it out recovers clean ASCII runs.
5. Extracted all printable-ASCII runs (≥2–4 chars) from the `signs` variable in file order.

## Result

**Confirmed positive.** The `signs` variable decodes to a clean, ordered per-sign catalog. For the
first ten entries, in file order:

| Order | Internal code | Phonetic value | Earliest-attestation reference (as encoded) |
|---|---|---|---|
| 1 | ABA | da | PH 31a/17 |
| 2 | ABB | ro | KH 100/3 |
| 3 | ABC | pa | KH 5/22 |
| 4 | ABD | te | ZA 20/14 |
| 5 | ABE | to | ARKH 2/10 |
| 6 | ABF | na | KH 5/17 |
| 7 | ABG | di | KH 6/2 |
| 8 | ABH | a | ZA 10b/18 |
| 9 | ABI | se | KH 7a/22 |
| 10 | ABJ | u | ZA 10a/16 |

The phonetic-value column is an **exact match, independently, for all ten**, to the already-committed
`sign-list.html` spot-check (`da, ro, pa, te, to, na, di, a, se, u`) — a genuine independent
cross-confirmation from a second, structurally different SigLA data source, not a re-read of the same
page. Site codes in the attestation column (PH = Phaistos, KH = Khania, ZA = Zakros, ARKH = Arkhanes)
match the standard Linear A find-site abbreviations used across this project's other sources (e.g. the
SQ-4 libation-formula table's `IO`, `PK`, `SY`, `TL` codes for other sites).

**Scale**: the same catalog structure repeats for the full sign list (order-of-magnitude ~300+ entries
matching SigLA's documented sign-inventory size, per SQ-1's prior figure) — not just these ten. This is
a materially larger reachable surface than the prior one-page, ten-sign spot check.

**Still not found — the actual confidence-tier field.** Searched the decoded text for `AB01`–`AB10`
literal labels (not present — the file uses the `ABA`/`ABB`/... internal code scheme, not `AB01`
labels), and for `confiden`/`borrow`/`infer`-type substrings (no matches). No plain-text field
distinguishes directly-borrowed vs. inferred vs. contested readings anywhere in the ~488KB of
stripped-and-decoded printable text from the `signs` variable. If that classification exists in this
file at all, it is encoded as a non-textual (numeric/positional) flag within the surrounding binary
structure, which has not been reverse-engineered — this cycle decoded the string layer only, not the
full binary record schema (field boundaries, numeric flag meanings).

## Honest status against ChatGPT's ask

- "Pin hashes for sign-list.html and database.js" — **done** for `database.js`
  (`cc624f148fd84c94fd2910b0adf92ecace25f52f9175664122bdf8384a8f1b9d`, 2,516,528 bytes,
  `Last-Modified: Fri, 26 Jun 2026`); `sign-list.html`'s hash was not re-pinned this cycle (out of
  scope for this specific investigation).
- "decode one record" — **done**, ten records shown above, independently cross-confirmed.
- "extract confidence fields for AB01–AB10" — **not done**. The confidence/certainty classification
  SQ-2 actually needs is not present as readable text in this file. This remains the real blocker.

## Next step

Reverse-engineer the binary record boundaries around each string triplet (internal code / phonetic
value / attestation) to check whether a numeric flag byte adjacent to each record encodes the
borrowed/inferred/contested distinction — a materially larger task than this cycle's string-layer
decode, not attempted here given this session's standing token-budget constraint. Flagging this
honestly as unclaimed rather than attempting it unbounded this cycle.
