# SQ2 q/z sign batch completion — 2026-11-06

## Status

**Independent reproduction:** ChatGPT read the public official SigLA sign list and the published Cambridge source used by the frozen SQ2 rubric. This is a citation-scale classification result, not a Linear A reading or translation.

## Frozen rule

Per `logs/2026-09-28-sq2-confidence-rubric-freeze.md`:

- **Tier A:** the sign/value cell is present in Table 1.
- **Tier B:** absent from Table 1 but present in Table 2.
- **Tier C:** absent from both tables or otherwise contested.

Classification is per sign/value cell, not inferred from another cell in the same row.

## Sources and corpus permission

- SigLA, “Sign list”: https://sigla.phis.me/sign-list.html
- SigLA, “About”: https://sigla.phis.me/about.html — the site states a CC BY-NC-SA 4.0 licence.
- Ester Salgarella, *Aegean Linear Script(s): Rethinking the Relationship between Linear A and Linear B*, Cambridge repository PDF: https://api.repository.cam.ac.uk/server/api/core/bitstreams/7e3a97dd-5ae9-46e3-bab5-fdd644e45bec/content

The public pages/PDF were used for read-only research and short factual extraction. No restricted corpus material is reproduced here.

## Evidence

The SigLA sign list identifies the remaining q/z signs as AB21 **qi**, AB74 **ze**, and AB78 **qe**. In the Cambridge paper, the q and z rows are empty in Table 1, while Table 2 includes q-row **qa, qe, qi** and z-row **za, ze, zo**.

| Sign | SigLA value | Table 1 | Table 2 | Frozen tier |
|---|---|---:|---:|---|
| AB21 | qi | absent | present | B |
| AB74 | ze | absent | present | B |
| AB78 | qe | absent | present | B |

The earlier batch already classified AB16 **qa**, AB17 **za**, and AB20 **zo** as Tier B. This batch therefore completes every q/z sign currently listed on the cited SigLA sign list under the frozen table-membership rule.

## Measurable improvement

- Atlas coverage: **44/~300 → 47/~300** signs.
- q/z subset: **6/6 currently listed signs classified** under the frozen rule.
- Access blocker: resolved through a public official read route.

## Falsification and limits

Falsify or revise a row if a direct check of the cited edition shows that its sign/value cell is present in Table 1, absent from Table 2, or differs from SigLA’s current mapping. A future SigLA revision must be treated as a new source state rather than silently substituted.

These tiers measure confidence in a borrowed phonetic value only. They do **not** establish a Linear A language, source-language reading, word meaning, or English translation. The result was checked through accessible web renderings/text; it has not yet received a second human visual inspection of the table images.

## Visual-rendering cross-check — 2026-11-06 04:00 UTC

ChatGPT separately inspected rendered images of the official Cambridge PDF pages containing Tables 1 and 2, rather than relying only on extracted text. The rendering shows the q and z rows blank in Table 1 and shows **qa, qe, qi** and **za, ze, zo** in Table 2. This confirms the table-membership premise for AB21/qi, AB74/ze, and AB78/qe in the same model’s second modality; it is **not** an independent human reader and does not remove the Director review gate.

## Next action

Research Director: independently inspect the three table cells and, if confirmed, merge this batch; then freeze the next small sign subset before classification.
