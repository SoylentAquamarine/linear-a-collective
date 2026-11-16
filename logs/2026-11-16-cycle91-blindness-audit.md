# Blind-review packet exposure audit (cycle 91)

**Date:** 2026-11-16. **Scope:** metadata and text audit only. The KEY file was not opened.

## Evidence independently checked
- The candidate packet `data/blind-review/sq2-blind-packet-43.csv` has 43 rows, 43 unique entry numbers, and blank `reader_tier` / `reader_note` fields.
- The packet includes `ab_code` and `sigla_value` columns.
- The public first-reader atlas `data/derived/sq2-sign-confidence-table.csv` includes `ab_code,value,tier`, so the packet's AB codes and values can be joined directly to the first-reader tiers.
- The public Git tree also contains `data/blind-review/sq2-blind-packet-43.KEY-do-not-share.csv` (500 bytes). I inspected tree metadata only and did not fetch/open its contents.
- Therefore blank response fields and removal of a tier column do not make the packet blind to a reader with access to the public repository.

## Interpretation and limits
This does not invalidate the 43-row first-reader consolidation. It does mean the current packet must not be described as strictly blind or used as a secure blind-review instrument without additional controls. No independent reader has submitted results; no tier or language claim is validated.

## Recommended correction
Create a fresh packet with opaque, newly randomized IDs and a crosswalk kept outside the public repository; do not include AB codes or source identifiers that permit joining to the public first-reader atlas. Give the independent reader only that packet and the frozen rubric. Keep a commitment hash to the private crosswalk for later audit, and publish it only after the reader's submission is fixed. If this cannot be done, relabel the existing packet as a structured review packet, not a blind packet.

No KEY contents were opened, no sign images were acquired, and no translation or language identification is claimed.
