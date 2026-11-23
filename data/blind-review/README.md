# Blind second-reader packet (SQ-2)

Use only `sq2-blind-packet-43-redacted-v2.csv` plus the frozen rubric at `logs/2026-09-28-sq2-confidence-rubric-freeze.md`.

The v2 packet contains sign IDs and blank reviewer fields only. It deliberately omits the old `batch_label` field because an audit found that each label mapped one-to-one to a first-reader source log and exposed the old tier composition. The v1 packet is retained for auditability only and must **not** be distributed to a reviewer.

The reader assigns Tier A/B/C using independent evidence only (never SigLA's own value alone). Do not open the KEY file, first-reader logs, or the original confidence table before submitting. Row order is shuffled (seed 20261116). Seal responses before adjudication; report disagreements rather than hiding them. Three flagged-unclassified entries are outside this packet.

Respect SigLA CC BY-NC-SA 4.0 and GORILA restrictions separately. The key remains in-repo for append-only auditability; a strict-blind reviewer receives only the v2 CSV and frozen rubric.
