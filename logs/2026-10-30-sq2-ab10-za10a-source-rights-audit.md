# SQ-2 — AB10 on ZA 10a: exact source and reuse audit

**Trigger:** the 2026-10-30 18:01:55 UTC ChatGPT handoff asks for one
disputed AB10 cell and its reuse status. This is a bounded guest contribution
by OpenCode's Daybreak Blue agent, operated by GitHub user `mickenordin`.
The operator authorized a citation-scale audit, not a bulk corpus or image
download.

## Scope and independence limitation

This audit identifies one exact occurrence and checks what may be reused. It
does **not** perform a blind second reading: the agent read the repository's
existing AB10 Tier B result before opening the source. It also does not treat
a source-assigned transcription as independent confirmation of itself.

## Exact attestation and context

SigLA's document page identifies the object as **ZA 10a**, a tablet found at
Zakros, dated **LM IB**, measuring **5.1 cm × 8.6 cm × 1.2 cm**, with 29 signs
grouped into seven words:

- document page: <https://sigla.phis.me/document/ZA%2010a/>
- exact occurrence page: <https://sigla.phis.me/document/ZA%2010a/index-15.html>
- exact occurrence drawing: <https://sigla.phis.me/document/ZA%2010a/ZA%2010a_15.png>

The occurrence page labels tablet position **#16** as a syllabogram, links it
to the `AB10` attestation search, and displays the reading `u`. The filename
suffix is `_15` because the image files are zero-indexed while the displayed
tablet positions are one-indexed. SigLA's word view places #16 as the fourth
and final sign of sequence #4, `a-mi-da-u`.

This agrees with the repository's earlier string-layer extraction, which
gave AB10's earliest encoded attestation as `ZA 10a/16`, but this is not an
independent source: both records come from SigLA.

## Exact bytes inspected

Only the single occurrence PNG and its two immediate HTML context pages were
downloaded to temporary storage. No GORILA scan, original-object photograph,
or bulk SigLA data was downloaded. Commands:

```sh
curl --fail --silent --show-error --location \
  --output /tmp/opencode/ZA_10a_15.png \
  'https://sigla.phis.me/document/ZA%2010a/ZA%2010a_15.png'
curl --fail --silent --show-error --location \
  --output /tmp/opencode/ZA_10a_index-15.html \
  'https://sigla.phis.me/document/ZA%2010a/index-15.html'
curl --fail --silent --show-error --location \
  --output /tmp/opencode/ZA_10a_document.html \
  'https://sigla.phis.me/document/ZA%2010a/'
sha256sum /tmp/opencode/ZA_10a_15.png \
  /tmp/opencode/ZA_10a_index-15.html \
  /tmp/opencode/ZA_10a_document.html
```

Observed on 2026-10-30:

| Resource | Size / format | SHA256 |
|---|---|---|
| `ZA 10a_15.png` | 14,266 bytes; PNG, 205 × 467, 8-bit RGBA | `19d37ba16536b7e61e9c1eaeb3257300c5e34b9bac4f0de01ccb259af615c220` |
| `index-15.html` | 7,483 bytes; UTF-8 HTML | `e3f1b9474188f76d71658e2a016846e04e75360de81127083f494508b540e298` |
| ZA 10a document page | 26,451 bytes; UTF-8 HTML | `65bd046cf49ad1bf48e0f07b43682e0d5cda0c269dc5e76ab7c4d80ad3bb9979` |

The image response was HTTP 200 with `Content-Type: image/png`, ETag
`"886685703"`, and `Last-Modified: Tue, 27 Oct 2026 05:47:51 GMT`.
External bytes were inspected but are deliberately not committed here.

## Provenance and reuse status

The exact occurrence page itself states: “Dataset and drawings are available
under the CC BY-NC-SA 4.0 license,” attributes the work to Ester Salgarella
and Simon Castellan, and links the licence deed. SigLA's methodology page
explains the provenance more precisely:

- the GORILA corpus contains photographs and drawings, but its images are
  “not free to use”;
- SigLA therefore made **its own drawings** of each document, based on the
  standard corpus, and generated per-document and per-attestation image files
  from those drawings;
- photographs of original objects remain contingent on copyright permission.

Source: <https://sigla.phis.me/paper.html>, especially sections 3.2 and 5.
The fetched HTML had SHA256
`f694cb696a4bda6b0f58b68085dd03615caf498a0f4032c3162435738b0f6202`.

The licence permits sharing and adaptation with attribution, non-commercial
use, and ShareAlike obligations:
<https://creativecommons.org/licenses/by-nc-sa/4.0/>. Therefore:

| Material | Reuse status |
|---|---|
| SigLA's `ZA 10a_15.png` occurrence drawing | Reusable under **CC BY-NC-SA 4.0**, with attribution to Ester Salgarella and Simon Castellan, a licence link, indication of changes, non-commercial use, and ShareAlike for adaptations. |
| GORILA scan / original-object photograph linked as corpus evidence | **Not covered by SigLA's drawing licence.** SigLA itself says those images are not free to use. No such image was downloaded or copied. |

Because this repository's own work is MIT-licensed, the CC BY-NC-SA drawing
is not embedded in this PR. Linking it and recording its checksum supplies an
auditable identifier without creating ambiguity about which licence governs
a copied third-party file.

## Evidentiary result

This closes the narrow **identifier and reuse** gap for one disputed cell:
`ZA 10a`, position 16, SigLA file `ZA 10a_15.png`, with a clear CC BY-NC-SA
4.0 reuse route for the drawing.

It does **not** close the primary-image or phonetic-value gap:

1. the permitted image is a modern SigLA tracing based on GORILA, not a
   photograph or scan of the original clay surface;
2. SigLA both selected/classified the occurrence as AB10 and supplied `u`,
   so the crop cannot independently validate that assignment;
3. visual identity alone would not establish phonetic value even if the
   original object image were available.

Accordingly, this audit supplies **no tier change**. AB10 remains Tier B under
the project's corrected operational rubric. A genuinely independent next
test would require a rights-cleared original-object image or authoritative
facsimile assessed by a reader blind to SigLA's label, followed separately by
contextual evidence capable of discriminating `u` from alternative values
across independent inscriptions.

## Reproducible next step

Seek item-level permission for an original ZA 10a photograph (or document an
already-open authoritative facsimile), then give the unlabeled target and
explicit alternatives to a reader who has not seen this audit or the current
Tier B label. Keep shape identification and phonetic-value adjudication as
two separate decisions.

## Correction — complete temporary-download disclosure

The sentence above saying “Only the single occurrence PNG and its two
immediate HTML context pages were downloaded” is too narrow. Those were the
only **attestation/data files**, but three supporting rights/provenance pages
were also downloaded to temporary storage for direct inspection:

| Supporting page | Purpose | SHA256 |
|---|---|---|
| <https://sigla.phis.me/paper.html> | SigLA drawing and photograph provenance | `f694cb696a4bda6b0f58b68085dd03615caf498a0f4032c3162435738b0f6202` |
| <https://sigla.phis.me/about.html> | authorship and site-wide drawing licence statement | `637da5530fde6b50dfe2e5a6454765e446b73191a8377a85e87c4764d87ad611` |
| <https://creativecommons.org/licenses/by-nc-sa/4.0/> | licence permissions and conditions | `ca0597fd98c6fb2417993e867b5cbc91ebdc55e24839c38e4674e8c78d817f17` |

All six files remained under `/tmp/opencode`; none was committed. No corpus,
database export, GORILA scan, or original-object photograph was downloaded.
This correction expands the disclosure but does not change the rights or
evidentiary result above.
