# Blind second-reader packet (SQ-2)
`sq2-sign-confidence-table`-derived, tiers removed. Reader assigns Tier A/B/C per `logs/2026-09-28-sq2-confidence-rubric-freeze.md` using independent evidence only (never SigLA's own value alone). Do not open the KEY file or the first-reader logs before submitting. Row order shuffled (seed 20261116). Adjudication under the unchanged rubric; disagreements reported, not hidden. Three flagged-unclassified entries are outside this packet. Respect SigLA CC BY-NC-SA 4.0 / GORILA restrictions.
The KEY file is in-repo for append-only auditability; a reader who wants strict blindness should be given only the packet CSV + rubric.


## Cycle #145 correction
The original sq2-blind-packet-43.csv contains the proposed sigla_value column and is **not suitable for strict-blind distribution**. A separate sq2-blind-packet-43-redacted.csv removes proposed values while preserving the shuffled row order and blank reader fields. For a strict-blind second reader, distribute only the redacted packet plus the frozen rubric; do not distribute the original packet or KEY. Keep the original files in-repository for append-only auditability. No review has been conducted yet.
