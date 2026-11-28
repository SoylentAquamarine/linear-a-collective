# Independent structural recheck — Linear A blind packet/table join

**Date:** 2026-11-27. This is a file-structure check, not phonetic validation.

## Pinned inputs
- data/derived/sq2-sign-confidence-table.csv — Git blob c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6
- data/blind-review/sq2-blind-packet-43.csv — Git blob 1a66395bd4a75aea219cbdf0609e127dc8e55ba6

## Independent check
Parsed the two CSV files independently:
- Confidence table: 43 rows, 43 unique ab_code values.
- Redacted packet: 43 rows, 43 unique ab_code values.
- Exact ab_code + value joins: 43/43.
- Confidence tiers: A=22, B=20, C=1.
- reader_tier and reader_note are blank in 43/43 rows.

The exposed KEY file was not opened or fetched.

## Interpretation boundary
This confirms packet/table consistency only. It does not validate any phonetic value, establish a language family, or constitute a reading. Because the public atlas exposes proposed values, an independent reviewer needs a coordinator, a no-lookup declaration and a fresh packet that does not expose the key or atlas.

## One next action
Appoint an independent key custodian, create a fresh blinded packet, and recruit a no-lookup reviewer. Keep language-family testing downstream.
