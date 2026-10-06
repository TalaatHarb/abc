# 7. Working dictionary: do not mistake names for identifications

This dictionary separates a **definition**, its role in the argument, and
the extra inference one must *not* make from the definition alone. Standard
terms have checked references. The IUT watchlist below consists of
**questions for the primary-paper audit**, not substitute definitions:
familiar-sounding names in IUT need their own exact source locators.

## Graduate-level walkthrough (intuition only)

For each unfamiliar term, write a **type signature** before an analogy:
what object enters, which map or construction acts, what exits, and
which numerical functions it preserves. An isomorphism need not
preserve an extra measurement that was never part of its structure.
As a toy example, $\phi:\mathbb R_A\to\mathbb R_B$,
$\phi(x)=2x$, is an ordered-additive isomorphism, but if both
copies have the independently assigned evaluation $v(x)=x$,
then $v_B(\phi(1))=2\ne v_A(1)=1$. This says **nothing**
about an actual IUT link; it explains why the next question is
always about the *specified* compatible evaluation.

Use the standard terms below to calculate, then treat the IUT rows
as prompts to inspect primary definitions rather than as invented
definitions of Hodge theaters or Frobenioids.

**Background, not source evidence:** the
[prerequisite route](02-prerequisites.md),
[Wikipedia on isomorphisms](https://en.wikipedia.org/wiki/Isomorphism),
and [Wikipedia on étale fundamental groups](https://en.wikipedia.org/wiki/%C3%89tale_fundamental_group).

## Standard terms and logical distinctions

| Term | Working definition or exact scope | Why we need it; a false shortcut to avoid |
| --- | --- | --- |
| Radical $R$ | $\operatorname{rad}(abc)=\prod_{p\mid abc}p$ for a primitive triple | Measures prime *support*, not the magnitude of $abc$; [01](01-abc-target.md), [G1](sources.md) |
| $p$-adic valuation $v_p(n)$ | The exponent of $p$ in the factorization of a nonzero integer $n$, extended to rationals by subtraction | $v_p(p^m)=m$, but the radical records only whether $m>0$; [01](01-abc-target.md) |
| Place | An equivalence class of archimedean or nonarchimedean absolute values on a number field; calculations choose normalized representatives | A numerical comparison valid at one place need not hold at another; [Goldfeld §2](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=5) |
| Height $H$ | For a primitive positive triple, $H([a:b:c])=\max(a,b,c)=c$; number-field heights combine *all* places | Do not replace a projective height with the size of one chosen coordinate in an arbitrary field; [01](01-abc-target.md), [G1](sources.md) |
| Weak abc | $(\lvert ABC\rvert)^{1/3}\ll_\varepsilon \operatorname{rad}(ABC)^{1+\varepsilon}$ for coprime nonzero $A+B+C=0$ | A geometric-mean bound is not literally the bound on $\max(\lvert A\rvert,\lvert B\rvert,\lvert C\rvert)$ in ordinary abc; [Goldfeld §1](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=1) |
| Model/minimal discriminant | A Weierstrass model has a discriminant; a local minimal model minimizes its $p$-adic valuation | A worked model calculation does not compute the minimal discriminant; [Goldfeld §3](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=6) |
| Conductor $N_E$ | A product $\prod_p p^{f_p}$ with exponents determined by reduction type of an elliptic curve $E$ | It is not literally $R=\operatorname{rad}(abc)$ for every Frey model; [Goldfeld §4](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=7) |
| Frey--Hellegouarch curve | For $a+b=c$, $y^2=x(x-a)(x+b)$ is an elliptic curve associated to the triple | Its invariants make a *conditional* bridge to abc, not a proof of Szpiro; [01](01-abc-target.md), [G1](sources.md) |
| Étale fundamental group | For connected $X$ and geometric base point $\bar x$, $\pi_1(X,\bar x)=\operatorname{Aut}(F_{\bar x})$ for the fiber functor on finite étale covers | Recovering a particular geometric object from group data requires additional hypotheses and reconstruction, not just this definition; [Stacks §58.6](https://stacks.math.columbia.edu/tag/0BQ8) |
| Implication $P\Rightarrow Q$ | A derivation of $Q$ from a stated input $P$ | A checked formal proof of this implication is not a checked proof of $P$ or necessarily a faithful translation of the paper's $P$; see the [project map](00-map.md) |
| Copy, isomorphism, label | A copy can carry corresponding structure without being literally the same object; a label names an object without prescribing its arithmetic value | Write the *specific map* and structures it preserves before comparing quantities in different copies; this is general logic, not a verdict on IUT |

## IUT-specific terms: source-audit questions

These are reading prompts until the actual definitions and allowed morphisms
are extracted from the primary papers. A quick analogy should always carry
this warning. Read the [primary-paper route](03-iut-route.md) for checked
locators; the [Lean vocabulary](06b-lean-vocabulary.md) describes typed
counterparts, not a replacement for the papers' definitions.

| Term | What the reader must determine from the cited paper | Dangerous unstated inference |
| --- | --- | --- |
| Initial $\Theta$-data | Which elliptic curve, base fields, primes, and auxiliary choices are fixed? | That a later theater automatically retains *every* original identification |
| Hodge theater | Which categories and arithmetic structures are present in a single theater? | That two theaters are the very same structured object |
| Frobenioid | What category is reconstructed, from what data, and up to what equivalence? | That an abstract reconstruction has fixed numerical coordinates |
| Theta-link / log-link | What is the domain, codomain, and exact preserved structure of each link? | That a transport preserves operations not included in its definition |
| Log-shell | What subset or object is being measured, at which places, with what normalization? | That it has the same value after an arbitrary relabeling |
| Log-theta-lattice | What are its nodes and the two sorts of connections? | That walking a diagram automatically yields a numerical inequality |
| Indeterminacy | Which group/action or range of choices is explicitly permitted? | That choosing one representative is canonical or comparison-safe |
| Mono-anabelian reconstruction | Which invariants recover which kind of arithmetic data? | That a recovered copy is identical to the source in all senses |

For every row, complete the seven-item definition gate in
[02](02-prerequisites.md), then cite a theorem that uses it in the
[claim graph](04-claim-dependencies.md). The open cells are deliberate:
learning the source's *permission to compare* is harder, and more important,
than memorizing its terminology.
