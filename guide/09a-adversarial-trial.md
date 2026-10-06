# 9a. A reproducible adversarial trial for the Step-(xi) edge

**Fixed question:** Under exactly which source-stated maps and
indeterminacies, if any, does IUT III, Theorem 3.11, justify the
Step-(xi) numerical comparison used for Corollary 3.12? The target is
an auditable proposition or a sharply located open obligation, **not**
an AI vote on whether abc is true.

## Freeze the evidence packet

Use the [source register](sources.md) for official links and edition
warnings: IUT I Definition 3.1/3.6 and Corollary 3.7(i); IUT II
Corollary 4.6; the **currently hosted** IUT III Definition 3.8,
Theorem 3.11, Corollary 3.12 and proof Step (xi); Scholze–Stix
section 2.2 and equation (1.5); Mochizuki's 2018 comments
(C12)–(C14) and 2019 report. The old IUT III edition referred to by
the critics may differ from the hosted one; a matching theorem number
does not demonstrate that the passages are textually identical.
After A–C have completed independent readings, introduce the
[Project LANA interim report, sections 8–10](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf#page=40)
as a *fourth, separate interpretation*, particularly the still-unproved
compatibility (9-1) on PDF p. 46. Do not retroactively rewrite the
independent reports to agree with it.
For the separate formalization boundary, use the immutable LANA
snapshot in [06](06-lean-boundary.md), not the tip of its default branch.
The [working model](09-critical-mechanism.md) and
[dispute guide](05-critical-transition.md) are orientation, not primary
authority. Private scratch PDFs or extracted texts are not publication
sources.

## Independent roles, then a dependent formalization

| Role | Bounded assignment | Must not assume |
| --- | --- | --- |
| A — faithful proponent reading | From IUT III and Mochizuki's response, reconstruct the strongest source-located transport and estimate, including the indeterminacies | That the response proves the contested comparison |
| B — critical reading | From Scholze–Stix's own diagram/equation and IUT III, locate the earliest type, scaling, or precision objection and attempt one independent calculation | That Mochizuki's label `(Lin)` is the critics' own wording |
| C — definitions-only reading | Independently extract objects, theaters, maps, and permitted comparisons from IUT I–III *before* reading either partisan explanation | That familiar names or matching labels identify objects |
| D — formalizer | After A–C, type-check a minimal claim for **each** incompatible interpretation, including whether report (9-1) is well-typed; prove a toy implication or give a countermodel and list the extra hypothesis needed | That LANA's unproved `Corollary312Variant` formalizes Step (xi) or proves (9-1) |

Give A–C the same fixed question and immutable source packet **without
sharing their draft conclusions**. D receives their three completed
reports and must not erase a disagreement by choosing one side's
types. Each role stops at the bounded edge; no broad "prove abc" prompt.

## Required output from each reading

| Field | Required content |
| --- | --- |
| Node/edge | `IUT-N1 -> IUT-N2`, or a smaller named sub-edge |
| Typed objects | Distinct source and target, theater/label, numerical copy, and exact scope of quantifiers |
| Operation | Identity, specified isomorphism, correspondence, or reconstruction; explicit preservation law or `UNKNOWN` |
| Numerical step | Quantity and sign, normalization, $j^2$ if applicable, and permitted indeterminacies |
| Evidence | Author, work, edition, theorem/step, PDF page (or pinned code SHA, file, lines); separate what the author asserts from what was checked independently |
| Test | A calculation, toy countermodel, alternative reading, or smallest premise whose proof would decide that edge |
| Status | `STANDARD`, `ASSERTED_IN_IUT`, `DISPUTED`, `CONDITIONAL_FORMALIZATION`, or `UNVERIFIED`, **per claim or arrow** |

Compare reports *by the maps they type and equations they justify*.
Agreement on the location of Step (xi) is a result; agreement that it is
valid requires an independent checked inference under the paper's
hypotheses. A majority of agents is not a mathematical argument.
Disagreements must name the first incompatible domain, codomain,
allowed transport, or numerical estimate and what evidence would settle
it. If the reports never reach a common typed claim, record that
failure rather than inventing a consensus. A human expert must review
any purported resolution before the status label changes.

## External checkpoint before our agents' first pass

This is the state reported by the published sources, **not a conclusion
reached by the AI roles above**:

| Checkable proposition | Evidence and present status |
| --- | --- |
| IUT III states Corollary 3.12 using Theorem 3.11 | [IUT III](sources.md): `ASSERTED_IN_IUT`; the Step-(xi) inference remains `DISPUTED`, not certified by publication |
| The Scholze–Stix hexagon commutes with its proposed scalings | [Project LANA report, section 10.2 and 10.5, PDF pp. 47–49](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf#page=47) confirms it does **not** commute, while disputing that the intended proof must factor through it; the latter claim needs a separate check |
| The report's two maps agree for a suitable admissible $S$ | Same report, section 9.2, PDF p. 46, equation (9-1); section 10.5, PDF p. 49 explicitly reports **no proof** of that compatibility, so its mathematical status here is `UNVERIFIED` |
| The displayed parametrized inequality matches $-Q\leq-T$ | [Elementary reduction](09-critical-mechanism.md) checks this if both texts use compatible real-number copies, the same normalization, and $Q>0$; IUT III explicitly invokes $Q>0$ in the proof on PDF p. 173, but the remaining compatibility is **not** established by the algebra |
| Lean verifies IUT's Step (xi) | The [pinned code audit](06-lean-boundary.md) finds only a `CONDITIONAL_FORMALIZATION` from an unproved Corollary 3.12 **variant** to abc, not a proof of Step (xi) or of (9-1) |

The report's authors also state that they have not reached complete
agreement among themselves about whether the original paper contains a
formalizable proof (section 10.5, PDF p. 49). This is a report about
their investigation, **not** a vote on the truth of abc or a claim about
every mathematician's opinion.

## Trial 1: three independent readings of the same edge

The A/B/C readings below checked primary PDF passages separately before
receiving each other's findings. They did not reproduce all preceding IUT
lemmas or obtain a human expert's agreement. [I1–I3 and
D1–D3](sources.md) identify the exact editions; PDF page numbers in
this table refer to those copies.

| Role | Source-located object and operation | Independently checked | First remaining obligation |
| --- | --- | --- | --- |
| **A, proponent** | IUT III, Definition 3.8(ii), pp. 112–113: the $\Theta^{\times\mu}_{\mathrm{LGP}}$-link corresponds between pilots; Theorem 3.11(i), pp. 154–155, and Step (xi-b), pp. 181–182, additionally use a permutation-symmetry poly-isomorphism across representation columns. Remark 3.9.5 (Ob1)–(Ob3), (Ob6), pp. 131–135, describes a hull followed by $\det^{\otimes M}$, potentially increasing volume. | The raw link may be linear while the *hull-based* volume operation is not an invertible scalar map. Mochizuki's (LVEx) region/area formulas in his [2018 report, pp. 24–26](sources.md) were recomputed; they are an **analogy**, not Step (xi). | Check the cross-referenced lemmas behind the poly-isomorphism and the then-unread (Ob8)/(Ob9) apparatus (now traced in Trial 2). In Step (xi-f), p. 184, verify rather than assume the asserted membership of the **native** $q$-value in the output region. |
| **B, critic** | Scholze–Stix, section 2.2, pp. 9–10: six diagram nodes (including an $\ell^\star$-member family) and literal equality of the arithmetic-degree lines at the bottom. Their **text** requires $j^2$ rescaling somewhere on the left; the figure does **not** label a $j^2$ arrow. | In an all-isomorphism loop of ordered one-dimensional real vector spaces, the text's required $j^2$ rescaling conflicts with the unscaled route for $j\ne1$ under SS's identifications. The $\sum j$ and $\sum j^2$ algebra in SS p. 4 checks. `(Lin)` and `id-version` are **Mochizuki's labels**, not terms used in the SS PDF. | Identify the source-level connection, if any, between a drawn arrow and IUT III's **separate**, non-invertible hull. A broken proposed isomorphism loop alone establishes neither the intended proof nor its failure. |
| **C, definitions-only** | IUT I, Definition 3.1, p. 61: initial data are fixed; Corollary 3.7, pp. 88–89: distinct theaters have a prime-strip poly-isomorphism but not a distinguished ring/scheme identification. IUT III, Theorem 3.11(i), pp. 154–155: a **different** cross-column representation poly-isomorphism; part (ii), pp. 155–156: stated vertical log-Kummer compatibility for a specified component. | Corollary 3.12, pp. 173–174, treats the $\Theta$-pilot as subject to (Ind1)–(Ind3) but the $q$-pilot as not subject to them. Step (xi-d)–(xi-f), pp. 183–184, asserts a one-sided region membership; an identity of the two pilot objects or two log-volume functions does not follow simply from matching labels. | Type the interaction of the *pilot correspondence*, *cross-column poly-isomorphism*, and *native $q$-volume*. The cited vertical compatibility alone does not establish the horizontal comparison. |

**First divergence, stated without a vote.** SS model each required
comparison (componentwise in the indexed family) through a proposed
loop of ordered real-line identifications.
The proponent reading instead invokes a prime-strip correspondence,
a *different* representation transport, and a hull-to-line operation
that yields a one-sided inclusion, not an invertible map. The neutral
reading confirms that these are distinct source-named operations but
does **not** establish that the last operation contains the *native*
$q$-value. If SS's loop is mandatory for the actual operations, its
$j^2$ incompatibility matters; if a genuinely different same-side
route is licensed, the loop alone does not decide that route.
Neither conditional has been discharged. Project LANA's separate,
unproved two-map compatibility (9-1) gives a candidate test at this
precise fork ([09](09-critical-mechanism.md)).

**Reproducible corrections and checks.** In the hosted IUT III,
Step (xi) has substeps (xi-a)–(xi-h) on PDF pp. 181–185, and
Step (xii) follows on pp. 185–186; Step (xi) is *not* the final
labeled step. SS's "page 16" citation agrees with the hosted
Introduction's discussion of Corollary 3.12, although the boxed
statement is on p. 173; their quoted closing sentence has the same
inequality as hosted Step (xi-f), p. 184, but different prose.
This does **not** demonstrate a substantive 2018-to-2020 revision.
IUT III, p. 173, states $|\log(q)|>0$ when relating the two
inequality forms. Finally, IUT I locates the "outside the framework
of ring theory/scheme theory" passage on **PDF p. 61**, not p. 59.

The arithmetic in each side's *toy calculation* is checkable,
but not an adjudication: for $a=b=1$, Mochizuki's region/hull
example has log-areas $\log 6<\log 8$, while SS's
$\sum_{j=1}^{\ell^\star}j$ and
$\sum_{j=1}^{\ell^\star}j^2$ equal
$\ell^\star(\ell^\star+1)/2$ and
$\ell^\star(\ell^\star+1)(2\ell^\star+1)/6$ respectively.
The inference "therefore IUT's native $q$-value satisfies the bound"
is **not** a consequence of either calculation.

**Status after A/B/C:** the named IUT statements are `ASSERTED_IN_IUT`,
the elementary area/sum/algebra checks are `STANDARD`, and the
Step-(xi) cross-object inference and the relevance of SS's diagram
remain `DISPUTED`. The report's map equality (9-1) is `UNVERIFIED`;
the Lean result remains only a
`CONDITIONAL_FORMALIZATION`. Agreement here is limited to a better
specified question, not the answer.

## Trial 1: dependent formalizer D

D received the three reports **after** A/B/C had stopped, then
compared their incompatible arrow types against IUT III, the pinned
[Project LANA report](sources.md), and the pinned
[Lean code](06-lean-boundary.md). D wrote an
[ordinary-mathematics conditional lemma and countermodel](09-critical-mechanism.md),
**not** a Lean proof of IUT.

One small but consequential **source check is resolved**: the SS
hexagon reproduced as Figure 7 in the Project LANA report (PDF
p. 47) labels a top isomorphism and a bottom equality, leaves the
four diagonal comparison arrows unlabelled, and draws **no**
hull-containment arrow. IUT III, Step (xi-c), PDF p. 182, visibly writes
${}^{1,\circ}\overline{\mathcal U}\supseteq{}^{1,\circ}\mathcal U$
before Step (xi-d)'s log-volume calculation. The overline is present
in the PDF image but **lost in plain-text extraction**, which can
misleadingly render this as $U\supseteq U$. A reader can check both
figures side by side without accepting either side's proof claim.
This establishes a difference in the *drawn operations*, **not**
that the SS loop is avoidable or that the containment proves the
desired bound.

For a specified input $x$, D's typed test distinguishes three
independent obligations: an admissible $S$ with the report's map
equality $\eta_q=\eta^{\mathrm{anab}}_S$; membership of the
*reconstructed* output in a bounded admissible set; and a shared
log-volume evaluation that both bounds that set and reads the
*native* $q$-value as $-Q$. Only with **all three** does substitution
give $-Q\le -T$. The report's section 9.3 *outlines* a link from
(9-1) to output-region membership but does not prove the full
bridge; section 10.5 explicitly has no proof of (9-1). The
[two-map countermodel](09-critical-mechanism.md) shows that the
mere existence of isomorphisms cannot replace equality of the
specified maps. The extra assumptions are listed, not silently
declared facts of IUT III.

The formalization boundary is also **type-level**, not merely a
missing citation:

| Artifact | Checked type/status | Missing bridge |
| --- | --- | --- |
| Project LANA report, §9.2, PDF pp. 45–46 | Proposed equality (9-1) of two maps $R_{\mathrm{val}}\to R_{\mathrm{ss}}$; `UNVERIFIED` | Connect these exact maps and a common input to IUT III's hull/output-region bound |
| [Pinned `Iut/Cor312/Statement.lean:78–91`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91) | `Corollary312Variant X : Prop` is the unproved inequality `X.qPilot.lhs ≤ X.rhsData.rhs` | Derive it **for the concrete Lean data** from faithfully modeled paper constructions; no term deriving it from (9-1) was found in the pinned code audit |
| [Pinned `Plans/Iut4Sec1Spec.md`, §2.2](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Plans/Iut4Sec1Spec.md) | `Corollary312Input` is a proposed structure in a **paused Markdown plan**, not the proved input of that Lean theorem | Do not identify its carriers or fields with the separate `Corollary312Variant` strand without a checked bridge |
| [Pinned conditional capstone, lines 37–46](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46) | `ClassicalABC` follows **if** the variant holds for the required data; `CONDITIONAL_FORMALIZATION` | The capstone does not prove its `h312` input or the report's (9-1) |

**Remaining human-review question:** Does the *published* Step
(xi-a)–(xi-f), together with all its cited earlier lemmas, establish
the same-input, same-output compatibility and region bound for the
native $q$-pilot, with its stated indeterminacies? If not, point to
the earliest arrow that fails to type or the exact extra premise;
if so, give a reviewed derivation. The four AI roles and the report
have not supplied that derivation, so `IUT-N2` remains `DISPUTED`.

## Trial 2: an object-and-arrow fork, not another vote

Two further **source-limited** audits were run independently on
2026-10-06. One read IUT III's definitions, Theorem 3.11, and
Step (xi-a)--(xi-f); the other read the original SS diagram and
Mochizuki's reply. Neither used the other's draft. Their
[shared-notation output](09b-object-identity-ledger.md) preserves
different `I-` and `SS-` objects instead of declaring them equal.
These are complementary readings, **not two independent proofs** of
the same mathematical claim.

| Test | Reproducible result | What it does not decide |
| --- | --- | --- |
| `T2-SS`: diagram image versus prose | [SS §2.2, PDF p. 10](sources.md) has six nodes (one an indexed family), a labelled top isomorphism, a bottom equality, and **four unlabelled diagonal arrows**. Its $j^2$ rescaling is required by the text, **not printed on an arrow**; no hull arrow is drawn. | Whether IUT III must factor its numerical calculation through those particular diagonals and bottom equality |
| `T2-IUT`: the earliest output claim | In [IUT III](sources.md), Step (xi-c), p. 182, visibly has $U\subseteq\overline U$. Rem. 3.9.5 (Ob8)/(Ob9), PDF pp. 137–139, provides a **vertical** log-Kummer comparison and bijection of hull log-volumes, cited in (xi-d); (xi-e), p. 184, relates input and output values; (xi-f) **first asserts** native $-|\log(q)|$ belongs to the bounded half-line. | Neither the hull inclusion nor that vertical bijection by itself selects the native $q$ value as an admissible output with the required normalization and bound for all stated choices; other cited hypotheses still require review |
| `T2-TOY`: independently checked arithmetic | [05 §5.8.1](05-critical-transition.md) corrects **this guide's** illustrative $a=1/10,b=1/5$ hull area to $6/5$ (the 2018 report itself gives no numerical triple), derives the exact $(a,b,\lambda)$ sign region, and gives two different hull outputs for the same input area and gluing scale; [09](09-critical-mechanism.md) proves a smaller finite-group hull lemma. | Neither toy construction is an IUT counterexample or proves the paper's native-$q$ membership |
| `T2-BOUND`: conditional test | [09](09-critical-mechanism.md) proves that a *one-sided* comparison of the **specified** evaluations, plus independently constructed output membership and bound, suffices for the numerical conclusion at a designated input. | The one-sided premise and its paper-stated quantifiers are unproved; map equality (9-1) is likewise explicitly unproved in the interim report |

**Gate for scaling agent experiments.** Freeze the source edition and
the [typed arrow IDs in 09b](09b-object-identity-ledger.md) before
varying roles or prompts. Keep the first proponent and critic readings
separate; give the formalizer both *only after* they stop. Require
each output to state `input object/copy | output object/copy |
specified operation and choices | quantifiers | numerical law |
source page or code SHA | independent check | first unknown`.
The next experiments have different falsifiers:

| ID | Bounded question for the next agent batch | Useful result or explicit stop |
| --- | --- | --- |
| `XI-LOOP` | Which *paper-stated* maps, if any, force the `SS-A -> SS-F` loop to commute for each $j$, including the indexed aggregation and $j^2$ normalization? | Exhibit exact IUT domains, arrows, and preservation laws **or** record the first unsupported match. The SS loop's noncommutativity alone is not a source-level counterexample. |
| `XI-NATIVE` | What takes the particular `I-6` native $q$ input through `I-3`/`I-5v`/`I-5` to the asserted `I-7` output, with (Ind1)--(Ind3), log-link iterates, and determinant powers? | A source-located, independently checked bound with the paper's quantifiers **or** a named missing premise. Merely showing $U\subseteq\overline U$ **or** a vertical hull-volume bijection does not pass. |
| `XI-COMPARE` | Can the report's two maps be reconstructed from paper-stated data, and is its admissible-$S$ equality (9-1), or a correctly typed one-sided inequality **in the needed direction**, derivable on precisely the required inputs? | State which comparison is derived, its normalization, whether $S$ depends on $x$, and how reconstructed membership is independently shown. Neither candidate may be assumed as a substitute for the conclusion. |
| `XI-EXPLAIN` | Can a reader unfamiliar with IUT follow `I-1`--`I-7` using only sets, maps, choices, and numerical bounds? | Produce a plain-language argument **with a back-map to every source arrow and quantifier**; reject any simplification that turns a copy into an identity or asserts `I-7` without a premise. |
| `XI-FORMAL` | Once those types are source-checked, what is the **smallest** proposition on which the two readings differ? | A checked toy theorem/countermodel with all assumptions exposed; only then attempt a Lean transcription. Do not identify it with the unproved `Corollary312Variant` or announce a verification of IUT. |

Count a **new source-checked arrow**, an exact independently proved
toy implication, a countermodel *meeting every asserted premise*,
or a precisely located missing lemma as progress. Do not count the
number of agents, agreement among them, subjective completion
percentages in the planning notes, or a proof of an **assumed**
statement. If repeated batches return only restated positions,
stop the loop and seek a human expert on the first unknown arrow
instead of generating more purported consensus.

## Relation to the status of abc

Keep three questions separate: whether abc is true; whether IUT I–IV
establish it; and whether a pinned Lean development checks a *conditional*
implication given an unproved substitute input. An elementary
[algebraic equivalence](09-critical-mechanism.md) or a successful toy
formalization answers neither of the first two questions. This trial
produced a more precise question for independent experts to test, not
agreement on its answer.

## XI-001: the first gated one-arrow run

The [XI-001 report](10-xi-001.md) freezes a dated source packet and
records four independent first readings of the native-$q$ output
question, followed by separate **source-fidelity** and
**mathematical-inference** checks. It preserves failed shortcuts and
a bounded source-specific repair rather than counting agreement
between agents. The tested conditional bridge is ordinary mathematics;
neither that lemma nor the reported source passages settle Step (xi).

## XI-002: the bounded fixed-native-value trace

The [XI-002 report](11-native-q-trace.md) followed the `XI-NATIVE`
question above with **three independent neutral readings** of the
same eight hashed PDFs, then a distinct source-fidelity review and
a separate mathematical-inference gate. A focused follow-up
checked the determinant exponent, local volume signs, and
structure-sheaf correction. The positive (Ob8)/(Ob9) volume
bijection and the pre-volume prime-strip loop are retained, but
neither alone places the **specific** native number in the
bounded output; that choice-compatible numerical bridge remains
`UNRESOLVED_OBLIGATION` in the inspected passages.

Claims that the weakened horizontal link itself preserves native
degrees, or that Ob9 selects the fixed $q$ as an output, are
`SOURCE-MISMATCH` **for those proposed attributions**. No
`COUNTEREXAMPLE` to the full IUT hypotheses was produced.
The next useful operation is a human-checkable numbered-lemma
request, not another round of agent agreement or premature Lean.
