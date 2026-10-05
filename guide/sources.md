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
| I1 | [Mochizuki, *Inter-universal Teichmüller Theory I*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf) | PDF p. 61 (Definition 3.1), p. 87 (Definition 3.6), p. 88 (Corollary 3.7(i)); `CHECKED` by delegated source audit, 2026-10-05 | Initial data, Hodge theaters, theta-links in [03](03-iut-route.md) |
| I2 | [Mochizuki, *Inter-universal Teichmüller Theory II*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf) | PDF p. 137 (Corollary 4.6); `CHECKED` by delegated source audit, 2026-10-05 | Reconstruction input in [03](03-iut-route.md) and [04](04-claim-dependencies.md) |
| I3 | [Mochizuki, *Inter-universal Teichmüller Theory III*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf) | PDF p. 153 (Theorem 3.11), p. 173 (Corollary 3.12), pp. 181–183 (Step (xi)), and surrounding proof; `CHECKED` by delegated source audits, 2026-10-05 | Original statement and contested sub-step in [03](03-iut-route.md) and [05](05-critical-transition.md); older report page numbers differ |
| I4 | [Mochizuki, *Inter-universal Teichmüller Theory IV*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf) | PDF p. 22 (Theorem 1.10), p. 41 (Corollary 2.2), p. 54 (Corollary 2.3); `CHECKED` by delegated source audit, 2026-10-05 | Downstream estimates with extra hypotheses and an external input, mapped in [04](04-claim-dependencies.md) |
| X1 | [Mochizuki, *Arithmetic Elliptic Curves in General Position*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf) | Its **citation role** in IUT IV, including Theorem 2.1(i), was traced; its proofs were not independently re-derived | External `[GenEll]` input to IUT IV's Corollaries 2.2–2.3 in [04](04-claim-dependencies.md) |
| O1 | [Mochizuki, *Panoramic Overview of Inter-universal Teichmüller Theory*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf) | General orientation checked; **not** a proposition-level proof audit | Optional map to the primary-paper terminology in [03](03-iut-route.md) |
| D1 | [Scholze and Stix, *Why abc is still a conjecture*](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf) | PDF pp. 1, 4, 9–10 (§2.2, Step (xi)); `CHECKED` by delegated source audit, 2026-10-05 | Their objection and interpretation in [05](05-critical-transition.md) |
| D2 | [Mochizuki, 2018 comments (`Cmt2018-08.pdf`)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf) | PDF pp. 3–4, (C11)–(C14); `CHECKED` by delegated source audit, 2026-10-05 | Reply to the proposed identification in [05](05-critical-transition.md) |
| D3 | [Mochizuki, 2018 report (`Rpt2018.pdf`)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Rpt2018.pdf) | PDF p. 2, pp. 23–26 and 42–44; `CHECKED` by delegated source audit, 2026-10-05 | Mochizuki's explanatory analogy and account of the disagreement in [05](05-critical-transition.md) |
| L2 | [LANA `iut` at `d9465c111ec4073709f67e9fccec7e3eb374a816`](https://github.com/lana-agents/iut/tree/d9465c111ec4073709f67e9fccec7e3eb374a816) | [Variant statement, lines 78–91](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91) and [conditional abc capstone, lines 37–46](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46) (`CHECKED` by delegated source audit, 2026-10-05); external dependency sources unaudited | Downstream implication assumes an unproved Corollary 3.12 variant; see [06](06-lean-boundary.md) and the [pinned dependency ledger](06a-lean-dependencies.md). This is not a verification of IUT. |

The proof in [02a](02a-polynomial-abc.md) is written out here, not
transcribed from either source. The IUT I–IV entries cover the **listed
propositions**, not their entire proofs or all preparatory papers. The
2018 exchange has been read on both sides, **not adjudicated**. The LANA
audit checked a successful Lean build and repository-local
declarations/dependency pins, **not** every external dependency's source
or the mathematical faithfulness of its input statement.

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
