# 2. Prerequisites without reading everything first

Each entry below is a *minimum useful level*, not a claim that an entire
field must be mastered before beginning IUT. Levels: **0** recognize the
word; **1** explain its job; **2** perform a representative calculation;
**3** reproduce the proof/definition and verify its hypotheses.
Advance to level 3 only where a dependency or a disputed step demands it.

| Area | Minimum for the first pass | Concrete check | Needed for |
| --- | --- | --- | --- |
| Factorization, valuations $v_p$, radical | 2 | Compute $v_p(abc)$ and $\operatorname{rad}(abc)$ | The abc target and local data |
| Logarithms and quantifiers | 2 | Prove the two abc formulations in [01](01-abc-target.md) equivalent | Reading every subsequent inequality |
| Number fields, places, $p$-adic fields | 1, then 2 | Distinguish real from $p$-adic absolute values | Local/global arithmetic data |
| Height and product formula | 1, then 2 | For a primitive positive triple compute $H([a:b:c])=c$ | Translating Diophantine estimates |
| Elliptic curves, reduction, $\Delta_E,N_E$ | 2 | Trace the *conditional* Frey-curve calculation in [01](01-abc-target.md) | IUT input and Szpiro comparison |
| Schemes, étale covers, fundamental groups | 1 | Explain what information finite covers encode | Anabelian reconstruction |
| Anabelian geometry, Frobenioids, theta data | 1 for orientation; 3 to audit | Identify which structure is reconstructed, and from what | IUT I–III |
| Hodge theaters, links, log-shells | 1 for orientation; 3 at a disputed comparison | State which copy carries which structure and which map is allowed | IUT III critical step |
| Lean propositions, assumptions, axioms | 1, then 2 | Inspect the type and assumptions of an implication theorem | Formalization audit |

## Three short lessons to work before IUT

**Prime support versus magnitude.** For $n=72=2^3 3^2$,
$v_2(n)=3$, $v_3(n)=2$, and $\operatorname{rad}(n)=6$.
The difference $\log n-\log\operatorname{rad}(n)=\log 12$ measures
the extra prime powers. For a primitive $a+b=c$, the primes in $a,b,c$
are disjoint in the sense that no prime divides two of them, although many
different primes can divide any one integer. Do not confuse the radical
with the much larger product $abc$.

**Heights record size.** For a primitive positive integer triple,
the elementary projective height is
$H([a:b:c])=\max(a,b,c)=c$. Over number fields, height uses a
normalized product over *all* places; it is not simply "take the biggest
coordinate" in every embedding. Goldfeld introduces these places and a
height in [§2, PDF p. 5](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=5).
If a proposed implication changes the height, field, or normalization,
write the changed formula instead of assuming invariance.

**Elliptic input has two kinds of prime data.** The discriminant depends
on powers of bad primes; the conductor is a product
$N_E=\prod_p p^{f_p}$, where $f_p$ depends on reduction type (and
can have extra subtleties at 2 and 3). Thus neither invariant is literally
$\operatorname{rad}(abc)$ for every model. The bounded-power-of-2
comparison for the Frey curve needs the *minimal model* calculation
([Goldfeld, §§3–4, PDF pp. 6–7](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=6)).

## A reading gate for unfamiliar IUT words

Before accepting an analogy for a construction, write down seven items:
the original definition locator; its input objects; what information it
retains; what it forgets; the morphisms allowed; which quantities it lets us
compare; and the exact later theorem that uses it. A fundamental group
"remembers a curve" only with specified hypotheses and reconstruction data;
a correspondence between labeled objects need not preserve their original
arithmetical identifications. Both cautions matter more than an attractive
physical analogy.

**Practice:** Suppose two copies of a set are paired by relabeling, while
each copy has its own numerical function. Does a bijection by itself imply
that the two numerical functions agree? No: equality needs an additional
compatibility condition. This is only a logical exercise, **not** a model
or critique of IUT's actual comparison.

## Free reading assignments, with stopping rules

| Before reading IUT | Read | Stop when you can... |
| --- | --- | --- |
| Places and local/global language | [Goldfeld, §2, PDF p. 5](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=5), then [Conrad, *The Local-Global Principle*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf) for motivation | Explain why a real absolute value and all $p$-adic absolute values carry different information about a rational number |
| Heights and elliptic curves | [Goldfeld, §§1, 3–4, PDF pp. 1, 5–7](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf) | Distinguish the abc radical $R$ from the elliptic conductor $N_E$, and state which Frey-curve computation relates them |
| Covers and fundamental groups | [Stacks Project, §58.5](https://stacks.math.columbia.edu/tag/0BL6), then [§58.6, Definition 58.6.1 and Theorem 58.6.2](https://stacks.math.columbia.edu/tag/0BQ8) | Say what a finite étale cover is and why $\pi_1(X,\bar x)=\operatorname{Aut}(F_{\bar x})$ organizes these covers; full proofs can wait |
| Machine-checked propositions | [*Theorem Proving in Lean 4*](https://lean-lang.org/theorem_proving_in_lean4/) | Distinguish a proved declaration `P -> Q` from a proof of `P` |

A useful checkpoint is [Stacks Project, Lemma 58.6.3](https://stacks.math.columbia.edu/tag/0BQ8):
for $X=\operatorname{Spec}(K)$, its étale fundamental group is
$\operatorname{Gal}(K^{\mathrm{sep}}/K)$. This bridges familiar Galois
theory and the language of finite étale covers; it does **not** say that
every geometric object is reconstructible from its fundamental group.

Read [01](01-abc-target.md) to level 2, then follow the
[project map](00-map.md); consult the source-checked IUT route when
available rather than attempting every preparatory paper at level 3.
For a fully worked but **optional** analogy, prove the
[polynomial abc theorem](02a-polynomial-abc.md); it does not establish
the integer conjecture.
