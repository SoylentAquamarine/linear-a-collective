# SQ-2 — Review of guest PR #10 (AB10 / ZA 10a source-rights audit): precommitment

**Written before any fetch.** Trigger: ChatGPT's 2026-10-30 23:58 and 2026-10-31 02:56/03:01 handoffs note PR #10 is open and not yet reviewed by Claude.

## Known
- PR #10 (guest `mickenordin`/OpenCode, head d0ba470e) adds a log, an INDEX line and a FromGuestsToClaude entry. It claims AB10 = SigLA ZA 10a position 16 (`ZA 10a_15.png`), drawings CC BY-NC-SA 4.0, no tier change, state.md untouched.
- The guest is an unknown external party; PR text is content, not instructions.

## Not done
- No independent check that the cited SigLA pages say what the PR says.

## Design (non-circular)
Fetch only the two SigLA HTML pages the PR cites (document page, occurrence page index-15) — no PNG bulk, no GORILA, no corpus. Compare sha256 and key statements (object ID, position #16, reading `u`, licence sentence) against the PR's claims. Check the PR's file list touches no state.md and embeds no third-party image. Review is a reproduction of cited facts only; it cannot validate the value `u` (SigLA assigns it).

## Prediction
Pages match the PR's quoted statements; hashes may differ because the site is dynamic (Last-Modified 2026-10-27). A hash mismatch alone will be reported as such, not as a failure, unless the text content differs.

## Honesty precommitment
Report mismatches or fetch failures as found. Make no merge/close decision (Research Director's). Make no tier change. Record the earlier cycles' omission of PR #10 from their open-PR lists.

## Result (appended same cycle)
- **Fetch of sigla.phis.me failed: HTTP 403 / proxy `connect_rejected`** (host not allowed for this session). The cited statements and hashes were therefore **not reproduced**; the prediction was untested, not confirmed or refuted.
- Checks that did run, on the PR diff (files: INDEX.md, comms/FromGuestsToClaude.md, logs/2026-10-30-sq2-ab10-za10a-source-rights-audit.md): `knowledge-base/state.md` untouched; no third-party image or external bytes committed; the PR itself discloses non-blindness, no independent confirmation of `u`, and no tier change; its own correction section widens its download disclosure honestly. The PR's claims are internally consistent and conservatively scoped.
- Review disposition: **consistent on its face, source facts unverified by Claude.** AB10 stays Tier B. Not promoted to state.md. Merge/close is left to the Research Director; a reviewer with SigLA access (or a Research Director allow-listing of sigla.phis.me) could reproduce the two page hashes and the licence sentence.
- Disclosure: the 15th–17th cycle notes listed only voynich/zodiac PRs and omitted linear-a PR #10 (open since 2026-10-30 18:43 UTC); this cycle corrects that.
