# Independent structural audit — Linear A confidence table and redacted packet
Date: 2026-11-26.

## Pinned files
- data/derived/sq2-sign-confidence-table.csv — Git blob c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6
- data/blind-review/sq2-blind-packet-43.csv — Git blob 1a66395bd4a75aea219cbdf0609e127dc8e55ba6

The exposed KEY file was not fetched or inspected.

## Independent checks
- Confidence table: 43 data rows, 43 unique AB IDs.
- Tier counts: A=22, B=20, C=1.
- Redacted packet: 43 data rows, 43 unique AB IDs.
- Exact ID overlap: 43/43.
- reader_tier blank: 43/43.
- reader_note blank: 43/43.

## Interpretation and limits
This verifies file structure and ID alignment only. It does not validate any phonetic value or establish that a sign's tier is correct. The public confidence atlas is a separate lookup risk for any purported no-lookup reviewer; the packet is not independent phonetic validation. No key was accessed, no reviewer response exists, and no language identification or translation is supported.

## Decision
Keep the exposed key retired-before-use. An independent custodian must create and verify a fresh randomized packet/key off-chat, then appoint a no-lookup reviewer who cannot consult the public tier/value atlas.
