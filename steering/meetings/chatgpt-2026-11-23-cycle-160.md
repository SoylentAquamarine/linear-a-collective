# ChatGPT Steering Committee — cycle #160

**Date:** 2026-11-23 16:55 ET  
**Project:** Linear A Collective  
**Meeting:** #75

## Goal and evidence standard
Resolve sign-value confidence before language-family testing; source-language readings require independent no-lookup reproduction and held-out contexts. English translation is not yet justified.

## Evidence and falsification
Re-read Meißner & Steele (2017): Table 1's vowel-only row lists V=a/i; Table 2 lists V=a/e/i/o/u. This supports the table-tier distinction, not an AB10 phonetic value by itself. Independently checked the redacted v2 packet on PR #42: 43 rows, 43 unique AB IDs, four columns, zero nonblank response fields. Main still exposes v1 with batch_label; do not distribute v1. PR #42 is mergeable and contains v2; PR #43 carries the website correction.

## Ethics, permissions and capacity
Keep v1, the key and first-reader logs private for audit. SigLA CC BY-NC-SA and GORILA corpus rights are separate. No corpus acquisition or bulk download without item-specific permission. No independent reviewer is currently appointed.

## Wasted effort and website status
Further packet-format work is not useful; independent review is the bottleneck. The live homepage has Wins so far near the top and currently describes v2 as prepared/undistributed; this review branch links the cycle record. Nothing is deployed.

## Measurable improvement
Reproduced the source's Table 1/2 row distinction and rechecked all 43 v2 identifiers and blank response fields.

## Decision and next action
Director-review and merge PR #42 to replace the public v1 packet; then appoint an independent no-lookup reviewer and distribute only v2 plus the frozen rubric. Keep the key sealed.
