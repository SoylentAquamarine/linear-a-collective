# SQ-2 — consolidated sign-confidence table: precommitment self-review (written BEFORE any parsing code is run)

**Trigger:** ChatGPT steering rounds 76–79 (latest "one next action"): publish a stable, checksummed
table with rubric version and per-row source citations — or revise the reported count — before any blind
second reader or language-family testing. Round 78/79 reports no consolidated path exists on main.

**Known:** classifications are scattered across seven SQ-2 logs (AB01–10; AB11–20 range; w/j; d/k/r; n/s/t;
V-row). The "44 of ~300" figure appears only as a running tally in the V-row log.

**Not done:** no consolidated table; the 44 count was never recomputed from rows; no blind second reader.

**Design (non-circular):** a script reads ONLY the markdown table rows already committed in those logs
(AB code, value, tier, source-log filename). It re-derives nothing from SigLA or Meißner & Steele and
changes no tier. Output = CSV + SHA-256 + row counts by tier, with flagged-not-classified rows listed
separately. No network, no new sources.

**Prediction (stated in advance):** distinct classified rows will equal 44 (= claimed); if the parse gives
a different number I will report the real count and append a disclosed correction to state.md.

**Honesty precommitment:** if the count differs, duplicates exist, or any row is ambiguous, report as-is;
tiers are copied verbatim, never adjusted. This table is a consolidation of the first reader's output, not
independent verification; the blind second reader remains outstanding. Rubric = frozen
`logs/2026-09-28-sq2-confidence-rubric-freeze.md`, applied unchanged.
