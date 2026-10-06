# 9b. Object identity: the real-line diagram and the hull

**The question in plain language.** The Scholze--Stix (SS) objection
compares numbers in several *distinct* real-line copies. IUT III also
forms a *containing set of possible outputs* by taking a hull. A change
of numerical coordinates and an inclusion of sets are different
operations. The fact that the hull is drawn in IUT III but not in
SS's hexagon does **not** tell us whether the hexagon is required
elsewhere in the proof, or whether the specific native $q$-value is
bounded by the hull's output.

**The logic without IUT vocabulary.** If $A\subseteq B$ and every
number in $B$ is at most $-T$, a separately supplied number $q_0$
is bounded only after a further premise, such as $q_0\in B$.
For example, $A=(-\infty,-2]$, $B=(-\infty,-1]$, $T=1$,
and $q_0=-1/2$ satisfy the strict inclusion and output bound,
but $q_0\notin B$. This is a countermodel to the **unlicensed
inference from set inclusion alone**, not a counterexample to
IUT: the latter may supply other hypotheses. The critical question
is which source-stated operation connects its native $q$-value to
the bounded output.

This is a source-audited **working ledger**, not a formal model of
either party's entire argument. It refines [09's provisional
`M1`--`M10` ledger](09-critical-mechanism.md). Citations refer to
the hosted versions in the [source register](sources.md), not an
unavailable 2018 edition of IUT III. The precise Step-(xi) dispute
remains `DISPUTED`; the checked drawings, elementary calculations,
and reported conjectures have *different* statuses.

## One key for reading every arrow

| Mark or kind | What it can mean | What it does **not** establish alone |
| --- | --- | --- |
| `=` | Literal equality in a specified context, or an equality **proposed by a diagram**; those are different claims | Identity of earlier structures just because their labels look alike |
| $\cong$ | A *specified* isomorphism of specified structures | Equality of elements in two numerical copies without that map and its normalization |
| Poly-isomorphism / correspondence | A family or relation of allowed transports between structured data | A unique real-valued map, or preservation of every operation not named by the source |
| $U\subseteq\overline U$ | Inclusion in a hull, generally non-invertible | That a particular external value belongs to the bounded output set |
| $x\in A$ | A membership **proposition** needing a proof | An arrow that is justified by drawing a path near $A$ |

The IDs below have **source prefixes**. An `SS-` real line, an `I-`
paper object, and an `R-` report model are not definitionally the
same object. `UNKNOWN` means this audit has no checked source-level
map with the claimed type, not that such a map cannot exist.

## SS's six nodes: their diagram, not IUT III's hull

[SS, section 2.2, PDF pp. 9--10](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf#page=10)
introduces three *kinds* of ordered real line in two columns.
Their diagram groups the indexed concrete $\Theta$ lines into **one
displayed family node**, not a single unindexed line. Subscripts
in the following table were checked against the rendered PDF image;
$\ell^\star$ is our notation for its raised star-like mark.

| ID | Notation in the SS figure | Role in SS's description | Attached to |
| --- | --- | --- | --- |
| `SS-A` | $\mathbb R_{\odot,\Theta}$ | Abstract $\Theta$-pilot line | $\Theta$ side, $HT_1$ |
| `SS-B` | $\mathbb R_{\odot,q}$ | Abstract $q$-pilot line | $q$ side, $HT_2$ |
| `SS-C_j` | $(\mathbb R_{\odot_c,\Theta_j})_{j=1,\ldots,\ell^\star}$ | **Family** of concrete $\Theta$-component lines | $\Theta$ side, indexed by $j$ |
| `SS-D` | $\mathbb R_{\odot_c,q}$ | Concrete $q$-pilot line | $q$ side |
| `SS-E` | $\mathbb R_\Theta$ | Arithmetic-degree line | $\Theta$ side |
| `SS-F` | $\mathbb R_q$ | Arithmetic-degree line | $q$ side |

Here is a *topological redrawing in our IDs*, with the arrowheads
of SS's unnumbered display on PDF p. 10. The four diagonals are
unlabelled in the source; downward arrowheads point along the
slanted edges. This is not a facsimile of the PDF.

```text
                SS-A --[Theta-link, isomorphism]--> SS-B
              /                                       \
             v                                         v
          SS-C_j                                     SS-D
             \                                         /
              v                                       v
                SS-E ----------[=]---------------> SS-F
```

| Edge | What the figure actually prints | What an agent must check next |
| --- | --- | --- |
| `SS-A -> SS-B` | Top $\Theta$-link with isomorphism sign | Whether this numerical real-line isomorphism is supplied, with the required normalization, by IUT's prime-strip *poly*-isomorphism |
| `SS-A -> SS-C_j`, `SS-B -> SS-D` | Two directed, **unlabelled** upper diagonals | The exact abstract-to-concrete maps and their effect on degrees for each $j$ |
| `SS-C_j -> SS-E`, `SS-D -> SS-F` | Two directed, **unlabelled** lower diagonals | How the indexed family is assembled/normalized into one degree line |
| `SS-E -> SS-F` | Bottom arrow labelled `=` | Whether the asserted identification of the *two previously distinguished copies* is licensed by the IUT construction |

**No arrow is labelled $j^2$ or "hull" in the printed hexagon.**
SS's *prose*, PDF pp. 9--10, says that encoding the $j$-th
concrete $\Theta$ degree requires inserting a $j^2$ rescaling
somewhere on the left; [equation (1.5), PDF p. 4](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf#page=4)
uses this factor. The text argues that enforcing all the proposed
identifications would then make the loop inconsistent or lose the
useful inequality. The figure does not specify **which** left
comparison is rescaled. Do not put $j^2$ on a guessed edge.
Comparing paths for a particular $j$ requires selecting that
component and the aggregation/normalization maps; calling the
entire family node one ordered real line would conceal this choice.

## IUT III's distinct, source-named operations

These rows describe what the [hosted IUT III, PDF
pp. 181--184](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=181)
*states* in Step (xi-a)--(xi-f). "Checked" means the specific
notation/statement was read; it does not certify the disputed
inference or the paper's cited earlier lemmas.

| Edge and distinct objects | Kind; paper locator | Source-stated content | Separate obligation |
| --- | --- | --- | --- |
| `I-1`: $\Theta$-pilot at $(0,0)$ to $q$-pilot at $(1,0)$ | Prime-strip poly-isomorphism; Def. 3.8(i--ii), pp. 112--113; (xi-a), p. 181 | Pilot objects correspond across the link | A log-volume identity **across theaters** is not stated by this pilot correspondence alone |
| `I-2`: multiradial representations at $(0,\circ)$ and $(1,\circ)$ | Different permutation-symmetry poly-isomorphism; Thm. 3.11(i), pp. 153--155; (xi-b), pp. 181--182 | Transports collections of possible representation outputs | Which admissible choices and numerical evaluation survive this transport? |
| `I-3`: $q$-pilot's representation among ${}^{1,\circ}\mathcal U^{\mathbb Q}$ possibilities to ${}^{1,\circ}\mathcal U$ | Linked via prime-strip isomorphisms; (xi-c), p. 182 | Related possibilities in the $(1,\circ)$ column | No particular valued-region map or log-volume law was extracted from this sentence |
| `I-4`: ${}^{1,\circ}\mathcal U$ to ${}^{1,\circ}\overline{\mathcal U}$ | **Hull inclusion**; Rem. 3.9.5(i--ii), p. 127; (xi-c), p. 182 | The paper visibly writes ${}^{1,\circ}\overline{\mathcal U}\supseteq{}^{1,\circ}\mathcal U$; the overline disappears from plain PDF text extraction | Inclusion is not a bijective real-line map and by itself says nothing about the native $q$-value |
| `I-5`: the overlined hull to its normalized determinant and an output half-line | Determinant/log-volume; Rem. 3.9.5(vii), (Ob1)--(Ob5), pp. 131--134; (xi-d), p. 183 | A rank-one output is formed and a half-line $\mathbb R_{\le-|\log(\Theta)|}$ is described | Check the determinant normalization, all needed indeterminacy hypotheses, and the claimed numerical bound on actual admissible outputs |
| `I-5v`: hull log-volumes on the two sides of a **vertical log-link**, after a shift | Log-Kummer comparison and a natural bijection of hull log-volumes via realified semi-simplification; Rem. 3.9.5(vii), (Ob8), PDF pp. 137--138, and (Ob9), pp. 138--139; cited in (xi-d), p. 183 | These statements give a meaningful **vertical** comparison even with log-link iterates; (Ob9-1) treats determinant and iterate indeterminacies as compatibility conditions | This bijection does **not itself select** the native $(1,0)$ $q$ value as a log-volume of a particular $(1,\circ)$ output hull, or give an (Ind1)--(Ind3)-uniform bound for it |
| `I-6`: the $(1,0)$ $q$-pilot to its native number $-|\log(q)|$ | $q$-pilot log-volume; Cor. 3.12, p. 174; (xi-d), p. 183 | An **input-side** number is given separately from the output half-line | Match its real copy and evaluation with `I-5` without replacing a correspondence by identity |
| `I-7`: native $-|\log(q)|$ to the output half-line | (xi-e)--(xi-f), p. 184: values described as linked via prime-strip isomorphisms, then **membership asserted** | The first explicit membership is in (xi-f): $-|\log(q)|\in\mathbb R_{\le-|\log(\Theta)|}$ | Show the *typed numerical* link and bound before invoking membership; membership is precisely the disputed comparison, not its independent proof |

Theorem 3.11(ii), PDF pp. 155--156, states compatibility for
particular **vertical** Kummer packets; its (Ind3) includes only
upper semi-compatibility as a vertical label varies. (Ob8)/(Ob9)
are **not** absent: `I-5v` records their vertical comparability and
bijection. The bounded source check did not find in them the
*additional selection and numerical law* carrying `I-6` through
`I-5v` to `I-7` for the allowed choices. Claiming that *no passage
anywhere* supplies this link would go beyond this audit.

## Crosswalk: which alleged equalities are still questions?

| Tempting match | What has actually been checked | What would make the match usable |
| --- | --- | --- |
| `SS-A -> SS-B` and `I-1` | The labels describe the corresponding pilots; SS draws a numeric isomorphism, IUT specifies a **prime-strip** poly-isomorphism | Type a chosen map on the particular numerical copies, including its preservation or scaling law |
| `SS-C_j -> SS-E` and `I-2`/`I-5` | The $j^2$ rescaling appears in SS's **prose**; IUT additionally forms an output hull and determinant | Match the actual $j$-indexed normalization and verify whether the paper's comparison must factor through SS's six-node loop |
| `SS-E = SS-F` and `I-5v`/`I-6` | Equality is printed in SS's drawing; IUT's (Ob9) instead states a **vertical bijection of hull log-volumes**, while Step (xi-d) separately produces the native input | Identify an authorized common real copy, select the native value among admissible outputs, and check (xi-e)'s relationship before (xi-f)'s membership |
| `I-4` and an SS diagram edge | The **overlined hull inclusion is visible in IUT III**; SS draws no corresponding inclusion | Establish which SS comparison, if any, the hull replaces or bypasses, without assuming the desired bound |
| `R-1`: Project LANA's $\eta_q,\eta^{\mathrm{anab}}_S:R_{\mathrm{val}}\to R_{\mathrm{ss}}$ and `I-7` | The [interim report, §9.2, equation (9-1), PDF p. 46](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf#page=46) proposes equality of these suitably identified maps for admissible $S$; §10.5, p. 49 says **no proof is known to its team** | Prove the map compatibility **and** its passage through reconstructed membership, output bound, and shared normalization; the report's maps are a later model, not named objects of Step (xi) |

Mochizuki's [2018 comments, (C12)--(C14), PDF
pp. 3--4](sources.md) call the all-scalar-identification
assumption `(Lin)` and reject it for indeterminacy-subject
log-volumes. `(Lin)` is **his label for SS's alleged assumption**,
not a term printed by SS. His [separate planar-region analogy,
(LVEx), PDF pp. 24--26](05-critical-transition.md) illustrates a
non-invertible set enlargement alongside a linear gluing map; it
does **not** supply a map from `I-6` to `I-5` in the IUT paper.

## Two small schemas, not rival formalizations of IUT

**All-isomorphism schema.** Fix a particular $j>1$ and a nonzero
ordered real-line input $v$. If two paths with the **same** typed
source and target must agree, but one is $j^2$ times the other,
their output on $v$ cannot both agree: for an isomorphism $f$,
$f(v)=j^2f(v)$ would force $j^2=1$. This is the elementary
monodromy test under the *specified* all-isomorphism and
commutativity hypotheses. It does not prove that IUT requires
this loop or dictate which SS diagonal gets $j^2$.

**Hull schema.** A set operation $H(A)=A\cup\sigma(A)$ need not
factor through a number $\log\mu(A)$; [09's finite four-point
example](09-critical-mechanism.md) gives equal-sized inputs with
different hull sizes. The [exact $(a,b,\lambda)$ experiment in
05](05-critical-transition.md#581-exact-parameter-test-our-calculation-not-an-iut-result)
shows the same effect in Mochizuki's illustrative region family
and corrects **this guide's** earlier numerical example, not
the source. A hull can therefore coexist
with a *separate* linear gluing without having to be an arrow in
SS's real-line diagram. This **does not** prove the IUT operation
has the needed compatibility: `I-7` remains the live obligation.
The [typed conditional bridge in 09](09-critical-mechanism.md)
states what source-level premises would yield the bound, including
a weaker **one-sided numerical** candidate whose quantifiers also
remain unproved.

The first independently checkable question for a mathematician is
thus **not** "which agent wins?" It is: *Does the published
Step (xi-a)--(xi-f), with all cited hypotheses, provide a typed
comparison that takes the particular native `I-6` value into the
bounded `I-5` output for the paper's allowed choices?* A proof of
that arrow would answer this local audit; a source-level
counterexample must satisfy the paper's **actual** hypotheses.
Until then, the two diagrams give distinct conditional tests,
not a proof, a refutation, or agreement about abc. The repeatable
experiment protocol is in [09a](09a-adversarial-trial.md); the
[XI-002 source trace](11-native-q-trace.md) tests `I-6 -> I-7`
with a separate normalization mini-audit.
