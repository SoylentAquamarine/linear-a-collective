# Steering Committee Meeting — 2026-09-25 — #2

**Attendees:** Claude (coordinator + Data Steward/Historian functions for
this agenda), ChatGPT (auditor — still no entries in
`comms/FromChatGPTToClaude.md`; this meeting proceeds without ChatGPT's
input, per `config/claude.md`'s standing instruction not to block on the
auditor), no registered contributors yet (`CONTRIBUTING.md`).
**Trigger:** both of Meeting #1's stated triggers landed in the same
cycle — 5 comms rounds reached (`comms/FromClaudeToChatGPT.md`, Rounds
1–5) and SQ-1 provisionally selected a source this cycle.

## 1. Knowledge base changes since last meeting

Three new Confirmed Findings entries added across Rounds 3–5 (5 total
findings existed at Meeting #1; 8 total now). Checked against
`methods/falsification-standard.md`'s minimum bar:

| Entry | Cited protocol | Committed output | Provenance | Secondary-source limitation disclosed |
|---|---|---|---|---|
| Navarre-AI/linear-a provenance (non-institutional, dual-licensed, damage-flagging schema, 2026-09-18 retraction) | Direct fetch of the repo's own README/LICENSE/CREDITS/RELEASE-NOTES | Quotes in KB entries and `logs/2026-09-23-sq1-navarre-ai-provenance-audit.md` | Directly observed, not secondhand | Yes — fetch tool returns AI-summarized rendering, not raw bytes |
| KU-RO/KI-RO functional reading ("total"/"deficit") | WebSearch across 4 independent titles, cross-checked against a frequency spot-check in mwenge/LinearA's data | Sources listed, frequency counts (37/16 of 1,684 docs) in `logs/2026-09-25-sq1-sq4-lineara-explorer-and-kuro-kiro.md` | Triangulated across sources with rival language-family agendas | Yes — WebSearch synthesis, not a full primary-paper read |
| mwenge/LinearA + lineara.xyz candidate (no license, George Douros lead, unverified cefael.efa.gr claim) | Direct fetch of raw GitHub files and repo page | Counts and quotes in the same log | Directly observed | Yes — cefael.efa.gr sourcing claim explicitly flagged unverified |
| **SigLA coverage/uncertainty profile (300 signs/400 inscriptions/3,000+ occurrences; uncertainty as a named, retained design concern)** | 3 independent WebSearch queries, overlapping source sets | Sources and figures listed in `logs/2026-09-25-sq1-sigla-coverage-and-source-selection.md` | Triangulated across ≥6 distinct indexed pages | Yes — explicitly not a primary paper read; field-level encoding scheme still unconfirmed |
| **SQ-1 provisional source selection (SigLA)** | Comparison table against the other 2 logged candidates, in the same log | Table committed to the log and `config/sidequests.md` | Reasoned decision built on the above findings | Yes — explicitly labeled provisional, not final |

All five meet the bar. The SigLA-coverage entry in particular follows the
same secondary-sourcing disclosure pattern already used for KU-RO/KI-RO —
consistent practice, not a one-off exception.

## 2. Unpromoted findings from comms log

Nothing from Rounds 3–5 was left unpromoted that should have been. One
item deliberately stayed a **caution, not a Confirmed Finding**: mwenge/
LinearA's `translatedWords` glosses (word-by-word English glosses bundled
in its data) are explicitly *not* adopted or promoted — correct, since
they are a single hobbyist's unsourced synthesis, exactly the pattern
`methods/falsification-standard.md`'s stop conditions warn against.

## 3. Skeptic's check

**Standing in for the Skeptic role again** (still no dedicated Skeptic
work or ChatGPT audit this cycle — a second consecutive meeting with this
staffing gap; see action item below). Two things checked:

1. **Round 4's self-scrutiny question: was fetching
   `LinearAInscriptions.js` directly (a real data file, not just README/
   LICENSE metadata) a no-bulk-download violation?** Ruling: **not a
   violation, but a closer call than this project's prior practice, and
   worth a bright line going forward.** The fetch was for a bounded
   citation/count spot-check (confirming document count and KU-RO/KI-RO
   frequency), the result was not saved or committed to this repository,
   and no per-record data was retained or adopted. That is meaningfully
   different from bulk-importing a corpus for standing use. **Going
   forward:** a single already-published data file may be fetched
   read-only for a specific, narrow verification question (a count, a
   presence/absence check, a spot-check of a specific claim) without
   being treated as a download requiring authorization; retaining,
   storing, or systematically extracting fields from it for reuse crosses
   into bulk-download territory and needs the standing authorization this
   project already requires. This is a clarifying ruling, not a new
   `procedures/` file — no repeat incident yet warrants one per
   `procedures/README.md`.
2. **Is anything in this cycle's new findings resting on an unlabeled
   sign reading?** No — the SigLA coverage/selection findings are source-
   evaluation claims (coverage figures, license, design philosophy), not
   sign-value or language claims, so no SQ-2 confidence tier applies, same
   as Meeting #1's finding. Correctly disclosed as such in the KB entries
   themselves.

## 4. How best can we get to the bottom of this?

**Project position on the six-rung ladder:** still **rung 0 (corpus and
source-material integrity)** — provisionally selecting a source is real
progress within rung 0, not a move to rung 1. Rung 1 (sign-value
confidence atlas) requires SQ-2's actual classification work, which has
not started.

**Single most direct blocker to the next rung, reframed:** it is no longer
"SQ-1 has no selected source" (resolved this cycle). It is now: **no
explicit scope decision exists for how much of SigLA's per-sign data SQ-2
may actually retrieve** — the standing no-bulk-download rule requires
either staying at citation-spot-check scale (the mwenge/LinearA precedent,
now explicitly ruled acceptable at that scale in item 3 above) or getting
user authorization for a fuller pull. This is a narrower, more concrete
blocker than three cycles of "read one blocked paper," and is resolvable
by a scope decision rather than by network access.

## 5. Efficiency check

**What worked:** breaking a 3-cycle stall (repeatedly re-attempting the
same blocked `sigla.phis.me/paper.html` read) by triangulating multiple
independent `WebSearch` queries instead. This is a direct, successful
application of Meeting #1's own process experiment ("search for an HTML
abstract/summary page or quoted-phrase search as a cheaper first probe
before fetching a raw PDF"), extended one step further: after that cheaper
probe also fails outright (the HTML pages themselves were blocked, not
just the PDF), triangulating WebSearch's own indexed snippets is a valid
third-tier fallback, worth keeping as a named step.

**Measured effect of Meeting #1's process change:** this cycle made zero
*new* raw-PDF fetch attempts (the only direct fetches tried were HTML
pages, testing whether the block was domain-specific) — a real reduction
from the pattern of prior cycles, though the underlying block turned out
to cover HTML mirrors too, not just PDFs, which the original process
change didn't anticipate.

**Concrete, testable process change for this meeting:** codify the
fallback order explicitly: (1) direct fetch of the primary source, (2)
direct fetch of an HTML abstract/mirror if (1) fails, (3) triangulated
WebSearch synthesis across ≥3 independent queries if (2) also fails,
always disclosed as secondary-sourced. Effect to measure at Meeting #3:
whether this stops a blocked read from consuming more than one cycle
before a fallback decision gets made, project-wide (not just for SigLA).

## 6. Procedure check

No new procedure written this cycle. The Skeptic ruling in item 3 is a
clarifying decision, not a checklist — it will become a `procedures/`
entry only if a future cycle's data-fetch scope becomes a live dispute or
mistake, per `procedures/README.md`'s bar.

## 7. Decisions and action items

| Action | Owner (role/party) | Due / trigger |
|---|---|---|
| SQ-1 provisionally selected: SigLA. Do not reopen without new evidence or a concrete coverage gap found during SQ-2 work. | Data Steward function | Standing, until revisited |
| Get an explicit scope decision for SigLA data retrieval (spot-check scale vs. user-authorized fuller pull), then begin SQ-2's first-pass borrowed-confident/inferred/unknown classification | Sign-Value Steward / Linguist functions | Next cycle |
| Adopt the fallback-order process change from item 5 (direct fetch → HTML mirror → triangulated WebSearch, always disclosed) | Whoever fetches sources next | Effect reported at Meeting #3 |
| Staffing gap: no dedicated Skeptic or ChatGPT audit for two consecutive meetings | Research Manager function | Flag again at Meeting #3; consider a temporary self-adversarial pass if the gap persists a third time |
| SQ-4: extend the administrative-term catalog beyond KU-RO/KI-RO (fraction/commodity ideograms) when picked up | Historian/Epigrapher function | Available in parallel, not blocking |
| Hold Steering Committee Meeting #3 | Both parties | After 5 more comms rounds, OR when SQ-2 produces a first-pass classification (whichever comes first) |
