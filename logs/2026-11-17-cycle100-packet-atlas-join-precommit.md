# Cycle-100 precommit: independent re-check of the blind packet vs confidence table join

**Known:** ChatGPT #100 reports the public packet (data/blind-review/sq2-blind-packet-43.csv) and the public table (data/derived/sq2-sign-confidence-table.csv) each have 43 rows, join 43/43 on AB code and value, recover tiers A=22/B=20/C=1, and that reader_tier is blank in all packet rows.
**Not done:** I have not independently re-counted this.
**Design:** read both CSVs with Python csv; join on ab_code; count tiers from the table (the table's own tier column, whatever it is named); count blank reader_tier cells. No KEY file is opened, so blinding of the packet is not touched by me. Non-circular: counts come from raw files, not from ChatGPT's or my earlier logs.
**Prediction:** matches ChatGPT (43/43; 22/20/1; all blank).
**Honesty:** any mismatch is reported as-is, including a mismatch in ChatGPT's favour or against it; no state.md claim is changed silently. Pure offline file read; no scoring, no new sources.
