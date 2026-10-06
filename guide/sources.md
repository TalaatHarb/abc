# Source register and citation policy

This is a **linked reading corpus**, not a repository of copied PDFs.
`CHECKED` means the specified passage was actually read; `TO_CHECK` means
a document is on the research list, not that its claimed contents have been
verified. The [original plan](../Research-project-plan.md) is a proposal and
its bibliographic claims are *not* themselves primary evidence.

| ID | Source | Passage checked | Used for |
| --- | --- | --- | --- |
| G1 | [Dorian Goldfeld, *Modular Forms, Elliptic Curves and the abc-Conjecture*](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf) | PDF pp. 1, 5–7 (`CHECKED`, 2026-10-05) | Strong/weak abc distinction; heights; discriminant, conductor, and conditional Szpiro/Frey comparison in [01](01-abc-target.md) and [02](02-prerequisites.md) |
| C1 | [Keith Conrad, *Analogies between Z and F[T]: Homework 5*](https://kconrad.math.uconn.edu/ross2003/analogy5.pdf) | PDF p. 1 (`CHECKED`, 2026-10-05) | Exercises on polynomial abc and the role of the exponent in [02a](02a-polynomial-abc.md) |
| C2 | [Keith Conrad, *The Local-Global Principle*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf) | PDF p. 1 (`CHECKED`, 2026-10-05); rest assigned, not audited here | Motivation for places and local/global study in [02](02-prerequisites.md) |
| S1 | [Stacks Project, §§58.5–58.6](https://stacks.math.columbia.edu/tag/0BL6) ([§58.6](https://stacks.math.columbia.edu/tag/0BQ8)) | Definitions, Theorem 58.6.2, and Lemma 58.6.3 on the linked pages (`CHECKED`, 2026-10-05) | Finite étale covers, the fundamental group, and its Galois-group example |
| L1 | [*Theorem Proving in Lean 4*](https://lean-lang.org/theorem_proving_in_lean4/) | Landing page (`CHECKED`, 2026-10-05); assigned chapters not audited here | Optional background for inspecting formal proof assumptions |
| I1 | [Mochizuki, *Inter-universal Teichmüller Theory I*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf) | PDF pp. 61–63 (Definition 3.1, including p. 61's "outside the framework of ring theory/scheme theory" warning), p. 71 (Example 3.2(iv), decorated $q$), pp. 87–91 (Definition 3.6, Corollary 3.7 and Remark 3.8.1); `CHECKED` by source audits, 2026-10-05/06 | Initial data, Hodge theaters, theta-links, limits of cross-theater identification, and local pilot normalization in [03](03-iut-route.md), [09](09-critical-mechanism.md), and [XI-002](11-native-q-trace.md) |
| I2 | [Mochizuki, *Inter-universal Teichmüller Theory II*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf) | PDF p. 137 (Corollary 4.6), pp. 158–162 (Definition 4.9(viii), Corollary 4.10, Remark 4.10.3(ii)); `CHECKED` by source audits, 2026-10-05/06 | Reconstruction input and the horizontal link's value-group limitation in [03](03-iut-route.md), [04](04-claim-dependencies.md), and [XI-002](11-native-q-trace.md) |
| I3 | [Mochizuki, *Inter-universal Teichmüller Theory III*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf) | PDF p. 16 (Introduction), pp. 96–97 (Remark 3.1.1(iv)), 112–118 (Definition 3.8, Proposition 3.9), 127–129, 131–135, 137–139, 141–144 (Remark 3.9.5, including **(Ob8)/(Ob9) on pp. 137–139** and part (ix) on pp. 141–144), 153–163 (Theorem 3.11 and Remark 3.11.1), 173–175 (Corollary 3.12), 181–185 (Step (xi), (xi-a)–(xi-h)), 185–186 (Step (xii)); the overline in (xi-c), p. 182, and the (xi-e)/(xi-f) distinction, p. 184, were checked against the rendered PDF (2026-10-05/06) | Original assertion, packet/determinant normalization, vertical hull-volume bijection, and bounded native-value trace in [03](03-iut-route.md), [05](05-critical-transition.md), [09](09-critical-mechanism.md), [09a](09a-adversarial-trial.md), [09b](09b-object-identity-ledger.md), and [XI-002](11-native-q-trace.md); older edition's exact wording still to compare |
| I4 | [Mochizuki, *Inter-universal Teichmüller Theory IV*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf) | PDF p. 22 (Theorem 1.10), pp. 27–29 (later corrected hull bounds), p. 41 (Corollary 2.2), p. 54 (Corollary 2.3); `CHECKED` by source audits, 2026-10-05/06 | Downstream estimates with extra hypotheses and an external input in [04](04-claim-dependencies.md); optional normalization cross-check, **not** a native-value bridge, in [XI-002](11-native-q-trace.md) |
| X1 | [Mochizuki, *Arithmetic Elliptic Curves in General Position*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf) | Its **citation role** in IUT IV, including Theorem 2.1(i), was traced; its proofs were not independently re-derived | External `[GenEll]` input to IUT IV's Corollaries 2.2–2.3 in [04](04-claim-dependencies.md) |
| O1 | [Mochizuki, *Panoramic Overview of Inter-universal Teichmüller Theory*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf) | General orientation checked; **not** a proposition-level proof audit | Optional map to the primary-paper terminology in [03](03-iut-route.md) |
| D1 | [Scholze and Stix, *Why abc is still a conjecture*](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf) | PDF pp. 1, 4, 7–10 (§2.2); diagram glyphs, directions, and absence of a printed $j^2$ or hull arrow checked against the rendered image on p. 10 (2026-10-06); `CHECKED` by delegated source audits | Their objection and interpretation in [05](05-critical-transition.md), [09a](09a-adversarial-trial.md), and the six-node [09b](09b-object-identity-ledger.md) |
| D2 | [Mochizuki, 2018 comments (`Cmt2018-08.pdf`)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf) | PDF pp. 3–4, (C11)–(C14); pp. 1, 5 on the cited August 2018 SS version; `CHECKED` by delegated source audits, 2026-10-05 and 2026-10-06 | Reply to the proposed identification in [05](05-critical-transition.md) and version caveat in [XI-001](10-xi-001.md) |
| D3 | [Mochizuki, 2018 report (`Rpt2018.pdf`)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Rpt2018.pdf) | PDF p. 2, pp. 15–20, 22–27, and 42–44; `CHECKED` by delegated source audits, 2026-10-05 | Mochizuki's explanatory analogy and account of the disagreement in [05](05-critical-transition.md) and [09](09-critical-mechanism.md) |
| D4 | [Project LANA, *Interim Report on IUT Theory* (July 2026, pinned PDF)](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf) ([ZEN University announcement](https://zen.ac.jp/news/zmcpostevent0717e)) | PDF pp. 40–49, especially condition (9-1) on p. 46 and provisional assessment on p. 49; `CHECKED`, 2026-10-05; `pdf` branch at commit `b8e4636` (2026-07-20) | The project's proposed two-map compatibility test and explicit lack of a proof of that test; this is an interim analysis, not a Lean theorem or a verdict on IUT |
| L2 | [LANA `iut` at `d9465c111ec4073709f67e9fccec7e3eb374a816`](https://github.com/lana-agents/iut/tree/d9465c111ec4073709f67e9fccec7e3eb374a816) | [Variant statement, lines 78–91](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91) and [conditional abc capstone, lines 37–46](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46) (`CHECKED` by delegated source audit, 2026-10-05); external dependency sources unaudited | Downstream implication assumes an unproved Corollary 3.12 variant; see [06](06-lean-boundary.md) and the [pinned dependency ledger](06a-lean-dependencies.md). This is not a verification of IUT. |
| L3 | [LANA `iut`, separate IUT IV §1 plan at the same SHA](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Plans/Iut4Sec1Spec.md) | Markdown §2.2's *proposed* `Corollary312Input` structure and the 2026-07-20 "paused after P6" banner; `CHECKED`, 2026-10-05 | Planning/specification placeholder, **not** the compiled Lean `Corollary312Variant` in `L2` and not a proof of the missing inequality |

The proof in [02a](02a-polynomial-abc.md) is written out here, not
transcribed from either source. The IUT I–IV entries cover the **listed
propositions**, not their entire proofs or all preparatory papers. The
2018 exchange has been read on both sides, **not adjudicated**. The LANA
audit checked a successful Lean build and repository-local
declarations/dependency pins, **not** every external dependency's source
or the mathematical faithfulness of its input statement. The July 2026
Project LANA report (`D4`) is a **different kind of evidence** from the
pinned code snapshot (`L2`) or its separate planning document (`L3`):
its proposed compatibility (9-1) is explicitly unproved there, and
neither a conditional Lean implication nor a proposed Markdown
structure supplies that missing argument.

## XI-001 source snapshot (2026-10-06)

The [publisher's record for IUT
III](https://doi.org/10.4171/PRIMS/57-1-3) gives *Publ. RIMS* 57
(2021), 403–626. Publication is not a verdict on the disputed inference.
The following fingerprints distinguish the copies actually read from
unexamined editions; these PDFs are not distributed with the guide.

| Source ID | Frozen copy and SHA-256 | Access limitation |
| --- | --- | --- |
| I3 | Currently hosted official PDF and the local reading copy both `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9` | Byte-identical on this date; the IUT III text cited in the 2018 exchange has not been separately matched to this edition |
| D1 | Local SS PDF `4ec276246a2a92d2e211a0dae5afd073b5eae7e2b37e9bbabe3cb82c7e0b34a0` | The official Bonn PDF is dated July 16, 2018 (p. 1); a fresh Playwright request returned 527,012 bytes with the same hash, without requesting a TLS-validation bypass. An earlier curl attempt failed TLS. The distinct August 2018 SS version cited in D2, pp. 1, 5, has not been compared |
| D2 | Official comments PDF `2fbd8deb2ca54c728191970bd5a06b81fe12bb68e656a8c684ad6bda86d83e6d` | Only the passages listed above were audited |
| D3 | Official report PDF `582e3f60e9461c127617844d92440dd60720ee9291da3a693270bcf195221882` | Only the passages listed above were audited |
| D4 | Report PDF at commit `b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676`: `aa53093aa8d69dbce5f8fb4f541069a418650260dee1ef532917aa8db89606c7` | Later report revisions, if any, require a separate check |
| L2 | Git commit `d9465c111ec4073709f67e9fccec7e3eb374a816` (2026-10-03) | This is a code revision, not a PDF fingerprint; external dependencies are not re-audited here |

## XI-002 source packet (2026-10-06)

Three independent native-$q$ trace readers received the **same** eight
PDFs, pinned by SHA-256 before their readings. Hashes identify an
edition; they do not establish any disputed mathematical inference.

| Source ID | Frozen SHA-256 | Edition and access |
| --- | --- | --- |
| I1 | `7360e3ed27c235b5497a0743d3ed1646fbb97688547d16b7c784fc7f127f1f03` | May 2020 PDF; local and freshly downloaded official IUT I copies match |
| I2 | `180bfa6aaddc4ae37af37acaad51f61e0a47b33b8255ad3169e28a970ae39b7c` | December 2020 PDF; local and freshly downloaded official IUT II copies match |
| I3 | `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9` | May 2020 hosted IUT III edition; official match checked in XI-001 |
| I4 | `5bf4b1e0a8c2686562a6859e5009d301335044cfb5efec5d3a9edf764e4af87f` | IUT IV PDF, used **only** for an optional normalization cross-check; local and freshly downloaded official copies match |
| D1 | `4ec276246a2a92d2e211a0dae5afd073b5eae7e2b37e9bbabe3cb82c7e0b34a0` | July 16, 2018 Bonn SS edition; official match checked in XI-001 |
| D2 | `2fbd8deb2ca54c728191970bd5a06b81fe12bb68e656a8c684ad6bda86d83e6d` | Official `Cmt2018-08.pdf`, freshly downloaded with the same fingerprint as XI-001 |
| D3 | `582e3f60e9461c127617844d92440dd60720ee9291da3a693270bcf195221882` | Official `Rpt2018.pdf`, freshly downloaded with the same fingerprint as XI-001 |
| D4 | `aa53093aa8d69dbce5f8fb4f541069a418650260dee1ef532917aa8db89606c7` | Project LANA's pinned July 2026 report at commit `b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676`, freshly matched |

The newly supplied `Inter-universal Teichmuller Theory III.pdf` and
`WhyABCisStillaConjecture.pdf` are byte-identical to the `I3` and
`D1` reading copies, **not** older editions. The local
`SS2018-08.pdf` is a 317-byte, one-page *Not Found* response, not a
Scholze--Stix paper, and was excluded. The August 2018 SS version
mentioned in D2 and the historical IUT III text cited in that
exchange remain **uncompared**.

## Minimum information for every future citation

1. **Paper:** author, title, stable official URL, publication or revision
   date where relevant, section/theorem, and *PDF page versus printed page*.
2. **Code:** upstream repository, immutable commit SHA, file and lines,
   exact declaration type, and a record of any axioms/assumed inputs.
3. **Inference:** identify *which* parts are in the source and *which* parts
   are our explanatory paraphrase or derivation. A citation to a paper's
   introduction cannot certify a later disputed comparison.
4. **Disagreement:** cite the objection and the reply independently; do
   not treat agreement about terminology as agreement about an inference.

Record access failures instead of inventing a locator. Links to PDFs or
source files let readers inspect the originals without distributing copies
or making a conditional calculation look like a new proof.
