# Independent reproduction: Linear A packet-to-atlas crosswalk — ChatGPT cycle 104

**Date:** 2026-11-17. The KEY file was not opened.

## Pinned inputs
- Packet: `data/blind-review/sq2-blind-packet-43.csv`, blob SHA `1a66395bd4a75aea219cbdf0609e127dc8e55ba6`
- Atlas: `data/derived/sq2-sign-confidence-table.csv`, blob SHA `c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6`

## Independent join
Parsed both CSVs independently. Packet rows = 43; atlas rows = 43. Joined on `ab_code` plus proposed value (`sigla_value` in the packet, `value` in the atlas): **43/43 matches**. All packet `reader_tier` cells are blank. Atlas tier counts are A=22, B=20, C=1.

## Interpretation
The public packet is not technically blind to a reader who can inspect the public repository/atlas. A packet-only external reader can still be blind if a separate coordinator distributes only the packet and frozen rubric, without repository/atlas access. This check verifies the join and tier leakage; it does not verify the phonetic values or establish a language. The KEY was not opened.
