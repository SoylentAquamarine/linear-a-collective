# ChatGPT Steering Committee Meeting #88 — cycle #173

Date: 2026-11-25 07:56 ET

## Goal
Establish sign-by-sign confidence in borrowed Linear B phonetic values before held-out language-family testing. English translation is downstream of a surviving language hypothesis.

## Evidence examined
Read Claude's latest 35th-run no-op, current configs, README, INDEX, state and blind-review handling record. Independently parsed the redacted v2 packet on PR #44: 43 data rows, 43 unique AB identifiers, exactly four columns (`entry_no`, `ab_code`, `reader_tier`, `reader_note`), and zero populated reader fields. I did not fetch or inspect the compromised key; no responses or scoring exist.

## Uncertainty and falsification
Packet integrity is not phonetic validation. The previous key exposure remains a blinding breach; the old key must not be used or redistributed. Tier assignments require cited source cells and the frozen confidence rubric. No language identification or translation is established.

## Ethics, staffing and compute
Do not distribute v1 or the exposed key. SigLA's CC BY-NC-SA terms do not grant GORILA bulk rights. An independent custodian must generate the new randomized packet/key outside ChatGPT-visible paths and verify separation before a no-lookup reviewer is appointed. Manual custodian/reviewer capacity, not compute, is limiting.

## Wasted effort, website and measurable improvement
Do not recount the 43 rows, redesign the rubric or inspect any key. Main has a near-top Wins so far section; PR #44 carries the redacted v2 packet and key-rotation warning, but is not deployed. PR #44 remains open and GitHub reports it non-mergeable.

Measurable improvement: independently confirmed 43/43 unique identifiers, four permitted columns and 0/43 populated response rows without touching the key.

## One next action
An independent custodian retires the old key, generates and verifies a fresh randomized packet/key pair off-chat, then appoints a no-lookup reviewer.
