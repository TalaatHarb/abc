# Source register and citation policy

This is a **linked reading corpus**, not a repository of copied PDFs.
`CHECKED` means the specified passage was actually read; `TO_CHECK` means
a document is on the research list, not that its claimed contents have been
verified. The [original plan](../Research-project-plan.md) is a proposal and
its bibliographic claims are *not* themselves primary evidence.

| ID | Source | Passage checked | Used for |
| --- | --- | --- | --- |
| G1 | [Dorian Goldfeld, *Modular Forms, Elliptic Curves and the abc-Conjecture*](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf) | PDF pp. 1, 5–7 (`CHECKED`, 2026-10-05) | Strong/weak abc distinction; heights; discriminant, conductor, and conditional Szpiro/Frey comparison in [01](01-abc-target.md) and [02](02-prerequisites.md) |
| C1 | [Keith Conrad, *Analogies between \(\mathbb Z\) and \(F[T]\): Homework 5*](https://kconrad.math.uconn.edu/ross2003/analogy5.pdf) | PDF p. 1 (`CHECKED`, 2026-10-05) | Exercises on polynomial abc and the role of the exponent in [02a](02a-polynomial-abc.md) |

The proof in [02a](02a-polynomial-abc.md) is written out here, not
transcribed from either source. The IUT I–IV publications, both sides of the
2018 exchange, and the LANA repository are separate source-audit tracks;
their proposition numbers and Lean theorem types must be checked before
they appear here as checked references.

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
