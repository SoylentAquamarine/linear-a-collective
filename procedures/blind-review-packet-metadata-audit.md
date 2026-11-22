# Blind-review packet metadata audit

Use this procedure before distributing any blinded packet, including packets assembled from multiple source batches.

## 1. Freeze the intended blinding boundary
- Name the information the reviewer may see and the information that must remain hidden.
- Freeze the rubric and reviewer task before creating the packet.
- Keep the key, proposed values, first-reader logs and adjudication material separate.

## 2. Minimize and inspect fields
- Retain only stable item identifiers and blank reviewer-response fields required by the task.
- Remove batch labels, source-log names, source paths, timestamps, filenames, confidence tiers, hidden comments, spreadsheet metadata and other fields not needed by the reviewer.
- Check row order and identifiers for accidental encoding of source, tier, confidence or chronology.

## 3. Test for indirect leakage
- Join every packet identifier against the source/key tables.
- Ask whether any retained field maps one-to-one to a first-reader log, batch, source group or known confidence distribution.
- Inspect filenames, headers and README instructions for references that reveal hidden material.
- Record the test, row count, unique-ID count, key-join result and packet SHA-256.

## 4. Separate release and audit copies
- Preserve the exposed/original packet for audit, clearly marked DO NOT DISTRIBUTE.
- Create a new redacted packet rather than silently overwriting the original.
- Give the reviewer only the redacted packet and frozen rubric; do not expose the key or first-reader logs.

## 5. Seal and adjudicate
- Record the exact packet checksum and delivery scope.
- Seal reviewer responses before opening the key or first-reader records.
- Report disagreements and adjudication decisions; do not erase dissent.

## 6. Stop conditions
Do not distribute if any field can reveal a proposed value, source batch, prior tier or first-reader record. Correct the packet, rerun this audit and record a new checksum first.

This procedure was added after the 2026-11-22 discovery that a batch label mapped one-to-one to a first-reader source log and exposed the previous tier composition. It prevents that specific provenance leak from recurring; it does not establish any phonetic value.
