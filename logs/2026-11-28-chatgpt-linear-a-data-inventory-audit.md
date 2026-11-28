# Linear A SQ-2 data inventory audit — 2026-11-28

**Scope:** main-branch metadata/table inspection only. No key or first-reader log opened; no corpus bytes accessed.

## Confidence table

- Path: `data/derived/sq2-sign-confidence-table.csv`
- Git blob SHA: `c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6`
- Parsed data rows: 43
- Unique sign IDs: 43
- Confidence tiers: A=22, B=20, C=1

This is a structured confidence ledger, not phonetic validation.

## Inventory and blinding discrepancies

- `data/README.md` still says “Nothing yet” under Present, despite the committed confidence table.
- The live homepage describes a redacted 43-entry packet as containing no proposed phonetic values.
- The latest main-branch steering record states the packet exposes `sigla_value` and `batch_label`; it is therefore not blind. Blank response fields do not repair exposure of proposed values.

## Conclusion

Correct the data inventory and homepage. Do not distribute the exposed packet as a blind test. A non-Claude custodian must retire the exposed key and create a randomized value-hidden packet before an independent no-lookup reviewer is recruited.
