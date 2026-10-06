# 8. Research queue: turn the ten stages into checkable work

The [original plan](../Research-project-plan.md) proposes stages 0–10.
This queue makes the *prerequisites* and the *exit tests* explicit. "Started"
means a reader guide exists; it never means the corresponding mathematical
claim is proved. Work on independent rows may proceed in parallel, but their
results must meet the shared evidence rules in [00](00-map.md).

| Stage | Output and immediate task | Depends on | Exit test |
| --- | --- | --- | --- |
| 0 — target | [01](01-abc-target.md): exact quantifiers, radical, examples | None | Reader can reproduce both directions of the finite-exception equivalence |
| 1 — claim graph | [04](04-claim-dependencies.md): paper-side node-and-arrow ledger | Stage 0; primary PDFs | Every arrow has a theorem locator, hypotheses, and an explicit status |
| 2 — prerequisites | [02](02-prerequisites.md): shortest useful study route | Stage 0 | Reader can perform the three calculations and identify deferred subjects |
| 3 — dictionary | [03 §1.4](03-iut-route.md), [07](07-dictionary.md): source-located working terms and reader questions | Stages 1–2 | Every entry states allowed maps and what cannot yet be compared |
| 4 — IUT I | [03](03-iut-route.md): first-pass trace of data, theaters, and links | Stages 1–3 | Explain one concrete job of each construction using IUT I's own definitions |
| 5 — IUT II | [03](03-iut-route.md), [04](04-claim-dependencies.md): reconstruction and quantitative inputs | Stage 4 | State the quantity, normalization, theorem, and its downstream consumer |
| 6 — IUT III | [03](03-iut-route.md), [05](05-critical-transition.md): Theorem 3.11, Corollary 3.12, Step (xi) | Stages 4–5; primary IUT III | Independent expert can check each comparison or point to the exact gap |
| 7 — dispute | [05](05-critical-transition.md): Scholze–Stix objection and Mochizuki's answer | Stage 6; both sides' primary texts | Each disputed arrow has both interpretations and a testable obligation |
| 8 — IUT IV and Lean | [04](04-claim-dependencies.md), [06](06-lean-boundary.md), [06a](06a-lean-dependencies.md): downstream claims and conditional Lean assumptions | Stages 0–1; IUT IV; pinned Lean snapshot | Trace a formal declaration to abc without assuming its unproved input |
| 9 — adversarial review | [09](09-critical-mechanism.md), [09b](09b-object-identity-ledger.md), [09a](09a-adversarial-trial.md), and the [XI-001 gate report](10-xi-001.md): typed comparison, exact six-node/Step-(xi) arrow crosswalk, independent readings, and a bounded first unknown | First-pass locators from stages 6–8; checked [Project LANA report](sources.md) | Type the native-$q$ to bounded-output comparison under the paper's quantified choices; record a source-level map, a countermodel satisfying its actual premises, or the first precise missing premise. Agreement or a vote is not a proof |
| 10 — exposition | Connected reader guide and diagrams from checked edges | Stages 0–9 | Each explanation links back to the exact node, arrow, source, and remaining gaps |

## Next bounded investigations

1. Check the **full hypotheses and quantified objects** in IUT III
   Theorem 3.11, Corollary 3.12, and especially Step (xi) against the
   first-pass [claim ledger](04-claim-dependencies.md). Compare each
   transport with Project LANA's proposed two-map compatibility
   (9-1); an independent expert must validate the actual domains,
   admissible choices, and indeterminacies.
2. Reconstruct IUT IV Propositions 1.1–1.8 and the separate
   `[GenEll]` Theorem 2.1(i) input behind Corollaries 2.2–2.3.
   Record which inequalities are for heights, conductors, or log-volumes,
   and the exact rule converting one to another.
3. Compare the pinned [Lean theorem types](06a-lean-dependencies.md) with
   the published Corollary 3.12 **and separately** with the report's
   compatibility (9-1). Supply and review each missing premise; audit
   external dependency sources instead of counting a successful
   conditional build as a proof of either premise.
4. Give the disagreement to two human experts in its strongest source-linked
   formulations; ask each to identify the first arrow they would accept or
   reject. Do not turn differing verdicts into an invented consensus.

For every investigation, capture: `node ID | source URL and PDF page/section
or code SHA/lines | exact hypotheses | mathematical operation | claimed
conclusion | objection if any | verification performed | unresolved item`.
PDF page numbers and printed page numbers can differ; record which is used.
Prioritize **stage 6**, then **stages 7 and 8**, before producing a polished
"IUT in 20 diagrams." A diagram is a deliverable only after its edges can be
audited.

**XI-001 checkpoint (2026-10-06):** The
[gated report](10-xi-001.md) records four independent one-arrow readings,
a separate source-fidelity check of the primary PDFs and pinned Lean
signatures, and an independently checked ordinary-mathematics bridge.
It preserves a rejected monodromy shortcut that omitted real-linearity
and a corrected attribution of Mochizuki's one-structure objection.
IUT III's pre-volume comparison loop and vertical hull-volume bijection
are positive source-stated operations, but the audited passages did
not independently establish the choice-compatible law bounding the
**fixed** native $q$ value. This is a precisely located request for
an expert, not Stage 9's proof-level exit test or a verdict on abc.

**Phase II object-and-arrow checkpoint (2026-10-06):** The
[six-node redraw and paper-side ledger](09b-object-identity-ledger.md)
separate SS's labelled top/bottom arrows from four unlabelled
diagonals, a $j^2$ rescaling in its **prose**, and IUT III's
visibly overlined hull. Step (xi-e) describes a link of
numerical values; (xi-f) first asserts the decisive membership.
Remark 3.9.5 (Ob8)/(Ob9), PDF pp. 137--139, gives a
**vertical** comparison and bijection of hull log-volumes, not
an explicitly selected native-$q$ output. This locates the
*proposed* crosswalk; it does **not** derive its missing
choice-compatible law or establish whether SS's loop is mandatory.
The [corrected toy experiment](05-critical-transition.md#581-exact-parameter-test-our-calculation-not-an-iut-result)
gives the exact $(a,b,\lambda)$ sign region and two equal-input
shapes with different hull outputs; [09](09-critical-mechanism.md)
gives a finite-set version and a weaker but also unproved
one-sided numerical test. Count verified arrows and exact remaining
premises, **not** subjective percentages of understanding or the
number of agents. The [repeatable experiment gates](09a-adversarial-trial.md)
keep additional AI rounds bounded to this edge.

**Phase II checkpoint (2026-10-05):** [09](09-critical-mechanism.md)
isolates a checkable algebraic consequence of the *stated* Corollary 3.12
inequality under an explicit positivity and normalization assumption, and
uses a two-copy model to expose an identification/quantifier hazard.
[09a](09a-adversarial-trial.md) records three independent source
readings and a dependent ordinary-mathematics formalizer. The
formalizer verified that SS's drawn hexagon has no hull arrow while
IUT III, Step (xi-c), has an image-checked, overlined hull
containing a distinct pre-hull object. The
[typed conditional bridge](09-critical-mechanism.md) requires a
specified map equality, admissible reconstructed output, and a
common numerical evaluation; mere isomorphism is insufficient.
Project LANA's checked [interim report](sources.md) explicitly
has no proof of its map equality (9-1), and the further output-region
bridge is not established here. These are tools for locating the
missing justification, not a verification of IUT III or a
resolution of abc.

**Stages 1 and 4–6 checkpoint (2026-10-05):** The [paper-side
route](03-iut-route.md) and [15-node graph](04-claim-dependencies.md)
locate IUT I–IV's named propositions. They correct the plan's straight
line: Theorem 1.10 specializes Corollary 3.12 with added hypotheses,
and IUT IV uses the separate `[GenEll]` input. Step (xi) in IUT III
remains `DISPUTED`; the `[GenEll]` proof and earlier reconstruction
machinery have **not** been independently re-derived here.

**Stage 7 checkpoint (2026-10-05):** The [source-paired dispute
guide](05-critical-transition.md) distinguishes Scholze–Stix's proposed
linear identification, under which they say the critical estimate loses
its force, from Mochizuki's reply that this identification is not an
allowed comparison and would make Theorem 3.11 inapplicable. This states
the disagreement; it does **not** decide whether the published comparison
is justified.

**Stage 8 checkpoint (2026-10-05):** A pinned [Lean source
audit](06-lean-boundary.md) identifies a machine-readable *conditional*
route toward classical abc. Its `Corollary312Variant` input is unproved
there; the repository distinguishes that variant from the published
Corollary 3.12. Auditing the missing premise, transcription,
and external package sources is still open. The
[dependency ledger](06a-lean-dependencies.md) records a successful build
at the pinned commit and separates unused challenge stubs from the
audited implication chain; neither fact proves the missing premise.
