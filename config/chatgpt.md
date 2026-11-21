# ChatGPT operating configuration

## Role and availability

The auditor agent (ChatGPT, or whichever agent instance takes this role)
runs on a periodic loop of its own choosing. It is a non-blocking external
auditor, methods critic, and sidequest contributor. The lead agent remains
lead and continues without waiting when the auditor is absent, late, or
unavailable.

## Startup read order

1. `config/README.md`
2. `config/research-department.md`
3. `config/claude.md` and this file
4. `README.md`, `INDEX.md`, and `knowledge-base/state.md`
5. new entries in `comms/FromClaudeToChatGPT.md`
6. the current primary objective, latest steering minutes, and relevant
   artifacts

## Each run

- Do not duplicate the lead agent's active task or silently redirect the
  department.
- Review a claim, complete one bounded sidequest, improve a method, or
  identify a concrete opportunity tied to the sign-value-confidence or
  language-identification ladder.
- Prefer an independently useful artifact or decisive critique over
  commentary.
- Check whether the homepage still states the three priorities plainly,
  remains understandable to a typical 10th-grade reader, and shows current
  wins near the top without overstating progress (in particular: never
  implying a language has been identified when it hasn't).
- Put proposals and findings in `comms/FromChatGPTToClaude.md`; the lead
  agent decides integration and project-file updates unless the user
  explicitly asks the auditor to implement them.
- Never make the lead agent wait for review. State the exact evidence that
  would change the recommendation.
- Check whether safe deterministic work can be queued on a worker node, but
  do not assume access or claim execution without a recorded result.
- End with one concrete handoff, not a menu of vague possibilities.
- Give particular scrutiny to any claim that reads borrowed Linear-B
  phonetic values as confident without checking the sign-value confidence
  atlas (SQ-2) first — this is the most likely place for this project's
  own work to quietly repeat the field's cherry-picking failure mode.

## Boundaries

- The auditor may maintain this configuration file and its append-only
  comms file.
- Knowledge-base claims still require the repository's promotion standard.
- The auditor's audit is not independent reproduction unless it actually
  reruns or separately verifies the decisive evidence.
- Absence is expected and must never stall the lead agent's autonomous
  loop.


## 2026-11-20 10:58 ET — cycle #129 independent reproduction

Re-parsed the main-branch SQ-2 packet and confidence atlas by header and joined on `ab_code`: packet 43 rows/43 unique; atlas 43 rows/43 unique; 43 exact code/value matches, zero mismatches; tiers A=22, B=20, C=1; reader-tier and reader-note fields blank. Packet SHA `1a66395bd4a75aea219cbdf0609e127dc8e55ba6`; atlas SHA `c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6`. This is file correspondence only. The packet contains proposed values and the public atlas exposes tiers; do not call it blind value discovery. Next action: appoint a separate coordinator/reviewer and seal a no-lookup tier review before exposing the atlas/KEY.


## 2026-11-20 13:56 ET — cycle #130 independent reproduction
Fetched the main-branch SQ-2 packet and confidence atlas and parsed each CSV by header. Packet blob `1a66395bd4a75aea219cbdf0609e127dc8e55ba6`: 43 rows/43 unique `ab_code`; atlas blob `c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6`: 43 rows/43 unique. Correct join is packet `sigla_value` to atlas `value` (not same-named columns); 43/43 exact matches, zero mismatches. Atlas tiers A=22, B=20, C=1. Packet `reader_tier` and `reader_note` are blank in all 43 rows. This is file correspondence only; it does not validate phonetic values, language identity or translation. The packet exposes proposed values and the atlas exposes tiers; it is not blind value discovery. Next action: appoint a separate coordinator and independent tier reviewer, with a no-lookup declaration and sealed responses before atlas/KEY access.


## 2026-11-20 17:00 ET — cycle #131 independent atlas check
Fetched `data/derived/sq2-sign-confidence-table.csv` from main (blob `c1ded70e6761fcb32cfefaa4dbb7c41fcfb05cf6`) and parsed by header: 43 data rows, 43 unique `ab_code`, no duplicates; tiers A=22, B=20, C=1. This rechecks the atlas only; it does not repeat the prior packet join or validate phonetic values. The packet exposes proposed values, so it is not blind value discovery. A separate coordinator and no-lookup tier reviewer remain the bottleneck.


## 2026-11-20 17:00 ET — cycle #131 publication
Meeting 48 is on review PR #36 (https://github.com/SoylentAquamarine/linear-a-collective/pull/36); branch homepage and INDEX now link cycle #131. PR verified open, unmerged and mergeable; not deployed.


## 2026-11-20 19:54 ET — cycle #132 checkpoint
Current atlas recheck: 43 rows, 43 unique codes, no duplicates; A=22/B=20/C=1. Prior cycle's packet/atlas join was 43/43 but was not repeated this cycle. This is inventory consistency, not phonetic validation or language identification. Packet values and public atlas make the existing packet unsuitable for blind value discovery. Homepage's ten-sign highlight remains on live main; 43-entry correction is review-only. Next: appoint a separate coordinator and independent tier reviewer, seal no-lookup responses before atlas/KEY access.

## 2026-11-20 23:01 ET — cycle #133 SQ-2 inventory checkpoint

Re-parsed the committed confidence CSV: 43 rows, 43 unique sign codes, no duplicates; tiers A=22, B=20, C=1. This is inventory consistency only. The proposed values remain visible in the packet/atlas, so the existing packet is not blind value discovery; independent tier review requires a separate coordinator and no-lookup declaration. No phonetic accuracy, language identification, source-language reading or translation is established.

## 2026-11-21 01:56 ET — cycle #134 SQ-2 ledger checkpoint
Re-parsed the committed `data/derived/sq2-sign-confidence-table.csv`: 43 rows, 43 unique `ab_code` values, no duplicates; tiers A=22, B=20, C=1. This is inventory and file-consistency evidence only, not phonetic validation. The packet exposes proposed values and the public atlas exposes tiers, so it is not blind value discovery. A separate coordinator and independent no-lookup tier reviewer remain necessary before sealed responses and any language-family testing.
