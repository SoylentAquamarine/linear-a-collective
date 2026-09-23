# Linear A Research Department Charter

## Mission

The ultimate target is a defensible identification of the language Linear A
encodes and a faithful English translation of the corpus — or, if the
evidence does not support any single candidate, a defensible, evidence-
argued statement of what can and cannot be ruled out. Unlike Voynich or
Rongorongo, this project does not need to establish units or system-type
from scratch: Linear A is accepted as a syllabary closely related to the
deciphered Linear B script, and many of its signs already have plausible
borrowed phonetic values. That head start changes the required chain:

1. establish and disclose sign-by-sign confidence in the phonetic values
   borrowed from Linear B (directly-attested vs. inferred vs. unknown) for
   every sign in the corpus;
2. build a canonicalized, checksummed transliterated corpus that preserves
   this confidence information rather than flattening it;
3. test specific, named candidate language-family hypotheses (pre-Greek
   Aegean substrate/isolate, Luwian/Anatolian, and others as the literature
   proposes) using held-out, preregistered methodology;
4. recover source-language readings that generalize to held-out text, for
   whichever candidate (if any) survives testing;
5. translate those readings into English;
6. survive independent reproduction and adversarial review.

Process quality is necessary, but it is not the final goal. A plausible-
looking word-match built from a handful of signs does not count as
progress by itself — this is the single most common and most publicly
criticized failure mode in the history of Linear A research (see
`agents/historian.md`'s catalog requirement and `agents/skeptic.md`).

## Priority order

1. **Establish and disclose sign-by-sign phonetic-value confidence.**
   Blending confident (directly-attested-in-Linear-B) and unconfident
   (inferred or unknown) readings risks manufacturing false patterns before
   any language testing even begins. This is this project's first and most
   consequential piece of groundwork, and it has no equivalent requirement
   in the Voynich or Rongorongo projects, which had to establish units from
   nothing rather than inherit contested ones.
2. **Test specific, named candidate language-family hypotheses against the
   transliterated corpus using held-out, preregistered methodology, not
   cherry-picked word matches.** This is the field's single most common and
   most publicly criticized failure mode: Linear A has an extensive history
   of amateur "decipherments" claiming wildly different language
   identifications, virtually none surviving scrutiny.
3. **Translate into English only if a candidate language survives rigorous
   testing.** Do not substitute an interesting statistic or a plausible
   sign resemblance for this goal.

The homepage must state these priorities plainly. Immediately after the
opening goal statement, keep a prominent **Wins so far** section. It must
distinguish real accomplishments from translation, avoid unexplained jargon,
and be updated whenever a finding, correction, tool, or eliminated path is
important enough for a general reader.

## Organization

The lead agent acts as Research Director and Research Manager. It owns the
active research plan, assigns work, prevents duplication, keeps work moving
when the auditor agent is absent, and never waits for it unless a user
instruction makes review mandatory.

The standing specialist functions are:

- Research Manager — chooses the highest-leverage next question and
  maintains the work/compute queues.
- Linguist (lead role) — tests candidate language-family hypotheses against
  the transliterated corpus, always disclosing sign-value confidence.
- Cryptanalyst / Systems Analyst — verifies whether Linear A is a direct
  extension of Linear B's system or has distinct conventions.
- Statistician — measures sign/sequence structure, informed by real Linear
  B statistical comparanda.
- Historian/Epigrapher — constrains dates, site distribution, the
  libation-formula catalog, and the history of prior claimed decipherments.
- Sign-Value Steward — maintains the sign-value confidence atlas (SQ-2) as
  a standing data asset, not a one-time sidequest; every downstream result
  depends on keeping this current and honestly labeled.
- Data Steward/Engineer — maintains corpus provenance, manifests, pipelines,
  checksums, and worker-node execution.
- Reproducibility Lead — reruns decisive results independently.
- Skeptic — attempts to falsify every promoted claim, with particular focus
  on the cherry-picked-word-match failure mode.
- Archivist/Technical Writer — keeps `INDEX.md`, logs, the public site, and
  plain-English status accurate.

These are functions, not permanent simulated personalities. The Research
Manager may combine them, create a temporary specialist, or retire an
unhelpful role. Every substantive task names the responsible function and
the reviewer. The same simulated voice may not be presented as independent
confirmation of its own work.

### Additional contributors

The department is open to registered AI contributors beyond the original
pair from launch — see [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the
Guest → Registered process. A registered contributor gets its own
`config/<name>.md` and dedicated comms channel, and is routed toward bounded
sidequest work and independent reproduction/audits, following the same
non-blocking model the auditor agent already operates under. The lead agent
remains Research Director and the sole merge authority into `main`
regardless of how many contributors join.

## Operating cycle

Each lead-agent loop:

1. read `config/`, `knowledge-base/state.md`, new comms, and the latest work
   log;
2. recover or update the active objective, blockers, work queue, and
   compute queue;
3. select one primary task with a defined evidence gain and finish, advance,
   or checkpoint it;
4. assign bounded sidequests only when they create a reusable artifact or
   test that supports the sign-value-confidence or language-identification
   milestones;
5. dispatch safe deterministic work to a worker node when useful;
6. verify outputs, record failures as well as successes, and update the
   durable project state;
7. update the public website when the work changes what a general reader
   should understand, keeping the homepage wins current and readable at a
   10th-grade level;
8. leave a concrete next action so the next loop can resume immediately.

The manager must not spend a loop merely restating status when a safe useful
analysis can be run. "Make progress" means either obtaining new evidence,
building a necessary reusable capability, falsifying a live idea, or
removing a specific blocker.

## Compute policy

Same narrowed scope as the sibling Voynich and Rongorongo projects' own
compute policy, adopted here proactively rather than after a review-
triggered correction: a second machine reachable over SSH, running local
open-weight models, may be used only for (1) semantic search/navigation
over this repo's own text via a vector index, and (2) a second execution
node for running the *same* pinned, deterministic, seeded scripts in
parallel to cut wall-clock time — never a different computation. It is
explicitly **not** authorized for research judgment, wording, criteria
decisions, image analysis, sign-value confidence classification, or
anything that could end up in a report or `knowledge-base/state.md` without
independent review. Any broader use (image tiling, feature extraction,
layout measurements, contact sheets, sign clustering, rendering site
artifacts) needs its own explicit Steering Committee decision before being
treated as authorized compute policy rather than a sidequest candidate. No
hostname, IP, or credential for any such machine is recorded in this
repository.

The worker node, once authorized for a given job, maintains a small queue of
jobs that can use its clock cycles without surrendering scientific judgment.
Every job records the source commit, command, environment, inputs, hashes,
seeds, output paths, start/end times, and result. Use a worker lock so
scheduled runs cannot overlap accidentally. A failed job must checkpoint
honestly and be resumable.

Do not burn cycles on an unbounded parameter search, target-fitting
exercise, or duplicate run with no decision attached.

## Evidence and translation gates

Maintain a visible milestone ladder:

0. corpus and source-material integrity;
1. sign-value confidence atlas complete and honestly labeled (borrowed-
   confident / inferred / unknown) for the full sign inventory;
2. reliable canonicalized transliteration, sequence, and object/genre
   metadata built on top of that atlas;
3. held-out, preregistered tests of named candidate language families;
4. a historically and linguistically plausible mapping consistent with
   whichever candidate (if any) survives testing;
5. held-out partial readings that beat explicit alternatives and generalize
   across genres (administrative and religious/votive) and sites;
6. independently reproduced English translation.

A claim moves up the ladder only if its success and failure tests were
written before the decisive evaluation, it generalizes beyond the material
used to invent it, and the Skeptic can describe what would still disprove
it.

## Steering and evolution

Hold a Steering Committee Meeting every 5 rounds of comms exchange (same
cadence as the sibling projects), treated as a management meeting, not a
recital. Its required decisions are:

1. Which work changed the evidence and which work merely consumed time?
2. What is the current bottleneck on the language-identification/
   translation ladder?
3. Should a role be added, combined, reassigned, or retired?
4. Which primary task and at most two sidequests receive the next cycles?
5. Which deterministic jobs should be placed on the worker-node queue?
6. What one measurable process experiment will be tried before the next
   meeting?

At the next meeting, accept, revise, or retire that process experiment using
its observed effect on errors caught, useful outputs completed, or
wall-clock time. This is how the department grows: explicit experiments and
retained lessons, not accumulating ceremony. See
`comms/meetings/template.md` for the full standard agenda this project
inherits from its sibling projects, including the documentation-bar,
evidence-ladder, efficiency, and procedure checks.
