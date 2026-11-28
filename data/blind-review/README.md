# Blind second-reader packet (SQ-2)

Use only `sq2-blind-packet-43-redacted-v2.csv` and the frozen rubric at `logs/2026-09-28-sq2-confidence-rubric-freeze.md`.

The v2 packet contains 43 unique sign IDs and blank reviewer-response fields only. It omits the old `batch_label` field because the previous audit found that batch labels mapped one-to-one to first-reader source logs and exposed the old confidence-tier composition. It contains no proposed phonetic values.

The v1 packet is retained on the earlier review branch [PR #41](https://github.com/SoylentAquamarine/linear-a-collective/pull/41) for audit only. **Do not distribute v1.** The v2 packet is prepared but has not been distributed to a reviewer.

The reviewer should:
1. Use only the v2 CSV and the frozen rubric.
2. Assign confidence tiers from independent evidence, never SigLA's proposed value alone.
3. Not access the key, original confidence table or first-reader logs before submitting.
4. Seal responses before adjudication and report disagreements rather than hiding them.

Respect SigLA CC BY-NC-SA 4.0 and GORILA restrictions separately. Permission to inspect a source is not permission to redistribute it. This packet audit does not establish any phonetic value, language identification or translation.
