# SQ-2 packet/table structural audit — 2026-11-27

**Scope:** parse only the redacted packet and public confidence table. The exposed KEY file was not opened.

## Exact inputs
- data/blind-review/sq2-blind-packet-43.csv — blob 1a66395bd4a75aea219cbdf0609e127dc8e55ba6
- data/derived/sq2-sign-confidence-table.csv — blob c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6

## Reproduction
- Packet: 43 rows, 43 unique ab_code values.
- Confidence table: 43 rows, 43 unique ab_code values.
- Exact ab_code + proposed-value joins: 43/43, zero mismatches.
- Tiers: A=22, B=20, C=1.
- All 43 packet reader_tier and reader_note fields are blank.

This is structural consistency only. It does not validate phonetic values, establish a language, or constitute blind review. The public atlas exposes proposed values, so the current packet is not suitable for an independent no-lookup reading. Do not inspect or reuse the exposed key.

## Decision
A separate non-Claude custodian must retire the exposed key and generate a fresh randomized packet off-chat. Recruit a reviewer with a signed no-lookup declaration before any phonetic validation or language-family test. Keep SigLA licensing separate from GORILA/data permissions.