# 03. The IUT route: theater, link, reconstruction, and the path to abc

**Scope of this file.** A first-pass, human-accessible narrative of the
information flow Mochizuki's papers assert runs from the basic gadgets of
inter-universal Teichmüller theory (IUT) through IUT III, Theorem 3.11 /
Corollary 3.12, through IUT IV's quantitative statements, to the classical
abc conjecture. **It is not a verdict on whether that flow is correct.** The
companion file [`04-claim-dependencies.md`](04-claim-dependencies.md) holds
the ID-tagged claim table, status labels, and the full reference list with
direct URLs; this file tells the story and points back to those IDs (e.g.
`IUT-N2`) rather than repeating every citation in full. Where the plan's
own linear chain is an oversimplification, that is corrected explicitly in
§7. This file is restricted to primary Mochizuki sources (IUT I–IV and his
orientation/response material); the full ten-page technical case for each
side of the Scholze–Stix dispute is carried in
`guide/05-critical-transition.md`, confirmed present as of this writing (see
§7 and the References list in [04](04-claim-dependencies.md) if that
filename has since changed), not reproduced here in full.

**What "verified" means here.** Every theorem/corollary/definition cited
below was opened in the actual PDF at the page given and checked against the
printed text. Page numbers refer to the PDF page as rendered by the
paper itself — these homepage preprints are each self-paginated starting at
1, which is **not** the same as their continuous cross-paper pagination in
the 2021 journal printing, *Publications of RIMS* 57(1/2); see
[04](04-claim-dependencies.md) §0 for that distinction and the exact DOIs.
Nothing here should be read as "the mathematical community accepts this step
as correct"; it records what the cited document **asserts** or
**constructs**, and separately flags what is disputed, conditionally
formalized, or unverified, using the status vocabulary fixed in
[04](04-claim-dependencies.md) §1 (`STANDARD`, `ASSERTED_IN_IUT`,
`DISPUTED`, `CONDITIONAL_FORMALIZATION`, `UNVERIFIED`).

---

## 1. Three building blocks: theater, link, reconstruction

IUT's architecture is easiest to narrate in terms of three kinds of object.
These are Mochizuki's own technical terms — not an analogy. The analogy
comes later (§8) and is marked as such.

### 1.1 Theater

A **$\Theta$-Hodge theater** is the basic self-contained unit of the construction: a
package of categories and Frobenioid-theoretic data built from a fixed choice
of **initial $\Theta$-data** — a number field $F \supseteq \sqrt{-1}$, a once-punctured elliptic
curve $X_F$ of type (1,1), an elliptic curve $E_F$, a prime $\ell \geq 5$, a set of
valuations $V$, a non-empty set of "bad" valuations $V^{\mathrm{bad}}_{\mathrm{mod}}$, and an
auxiliary sign/root-of-unity datum $\varepsilon$ (IUT I, **Definition 3.1**, p. 61;
`IUT-B1`). The theater itself is defined at IUT I, **Definition 3.6** (p. 87;
`IUT-B2`), as a collection of data $(\{{}^{\dagger}F_v\}_{v \in V},\ {}^{\dagger}F^{\Vdash}_{\mathrm{mod}})$ satisfying
listed compatibility conditions. Mochizuki describes each theater, in brief,
as a kind of "miniature model" of ordinary scheme-theoretic arithmetic
geometry built around the theta function (IUT I, p. 61, paraphrased here;
only the two-word phrase is quoted). Informally: one self-consistent,
internally ordinary copy of arithmetic geometry, built around one elliptic
curve.

### 1.2 Link

Two kinds of arrow connect theaters, and they behave very differently:

- The **$\Theta$-link**, IUT I, **Corollary 3.7(i)** (p. 88; `IUT-B3`), is
  explicitly **not** a morphism of schemes or rings — IUT I states that it
  "lies outside the framework of ring theory/scheme theory" (p. 61). It is a
  Frobenioid-theoretic correspondence identifying a $\Theta$-pilot object in one
  theater with a $q$-pilot object in the next. Chained copies, indexed by
  $n \in \mathbb{Z}$, give the log-theta-lattice's horizontal direction; the
  "LGP-Gaussian" version used from IUT III §3 onward is fixed at IUT III,
  **Definition 3.8** (p. 112).
- The **log-link**, built from the $p$-adic logarithm on local units, is the
  lattice's vertical direction: IUT III, **Proposition 1.2** (p. 30) and
  **Proposition 1.3** (p. 41) (`IUT-B4`).

Together these produce the **log-theta-lattice**: a two-dimensional,
non-commutative diagram of theaters in which neither direction preserves
ring/scheme structure. That non-commutativity is the point of the
construction — it is what lets the theory compare "alien" arithmetic
holomorphic structures at all — and it is also the reason everything that
crosses a link has to be reconstructed rather than read off directly.

### 1.3 Reconstruction

Because a link does not preserve ring/scheme structure, anything compared
across it must be **re-derived** on the other side from data the link does
preserve (Galois/fundamental-group-theoretic data), via explicit,
step-by-step functorial algorithms — the "mono-anabelian" style of argument
(building on Mochizuki's earlier, separately published absolute anabelian
geometry papers, not analyzed in this file). The citable instance used
downstream is IUT II, **Corollary 4.6** ("Frobenioid-theoretic Monoids
Associated to $\Theta^{\pm\mathrm{ell}}$-Hodge Theaters", p. 137; `IUT-B5`): a functorial
algorithm constructing, in an F-prime-strip ${}^{\ddagger}F$, an assignment
$\Psi_{\mathrm{cns}}({}^{\ddagger}F)$, well-defined only up to a ${}^{\ddagger}\Pi_v$-conjugacy indeterminacy.
Reconstruction in IUT always comes with an explicit, named indeterminacy —
never an exact value — and tracking which indeterminacy attaches to which
reconstruction is the technical heart of the theory.

### 1.4 Compact working vocabulary (quick reference)

A source-located summary of the six terms most load-bearing for the route
traced in this file. "Permitted comparison" records what the cited text
itself licenses crossing a construction — not what a reader might assume by
analogy with ordinary scheme theory.

| Term | Purpose | Permitted comparison (or explicit unknown) | Primary reference |
| --- | --- | --- | --- |
| **$\Theta$-Hodge theater** | Self-contained "miniature model" of ordinary scheme-theoretic arithmetic geometry, built around one elliptic curve $E_F$; the basic unit linked/compared across the lattice. | Not compared to another theater as rings/schemes directly; only its **reconstructed** Galois-theoretic data (via §1.3) may be compared across a link. | IUT I, **Def. 3.6**, p. 87 (`IUT-B2`) |
| **$\Theta$-link** | The log-theta-lattice's horizontal arrow: identifies a $\Theta$-pilot object in one theater with a $q$-pilot object in the next, via Hodge–Arakelov-theoretic evaluation (constructed in IUT II). | Explicitly **not** a ring/scheme morphism — IUT I states it "lies outside the framework of ring theory/scheme theory" (p. 61); only the one named Frobenioid-theoretic correspondence is licensed. | IUT I, **Cor. 3.7(i)**, p. 88 (`IUT-B3`) |
| **log-link** | The lattice's vertical arrow: applies the $p$-adic logarithm to local units, passing from a Frobenius-like monoid to its "log" (additive) image. | At the level of elements, explicitly **not** compatible with the Kummer isomorphisms used elsewhere in the construction (IUT III, p. 26, paraphrased) — this stated incompatibility is exactly why log-shells (next row), not raw log-links, carry the comparison. | Constructed in IUT III, **Def. 1.1** (pp. 23–29); key compatibility properties in **Prop. 1.2**, p. 30 / **Prop. 1.3**, p. 41 (`IUT-B4`) |
| **log-shell** | A canonically-constructed compact ("bounded") topological module $I_{{}^{\dagger}F_v} \subseteq \Psi^{\sim}_{{}^{\dagger}F_v}$ attached to each valuation, serving — in the source's own words — as a "multiradial container" (IUT III, p. 115, paraphrased) on which log-volumes are measured. | Log-volumes **on log-shells and their tensor packets** are the specific licensed comparison device: IUT III's own Introduction states this "will play a crucial role in deriving the explicit estimates…obtained in Corollary 3.12" (p. 15, paraphrased apart from the quoted clause). Tensor-packet Kummer isomorphisms varying over $m \in \mathbb{Z}$ are subject to the **(Ind3)** indeterminacy specifically. **Unverified by this guide**: the deeper justification of log-shells' defining properties rests on Mochizuki's earlier paper "Topics in Absolute Anabelian Geometry III" (`[AbsTopIII]`), which is **not** in this guide's checked corpus and was **not** independently read here. | Defined (as "pre-log-shell" → "log-shell") in IUT III, **Def. 1.1**, p. 24; previewed in general form in IUT II, **Example 1.8(ix)**, p. 41 (itself citing `[AbsTopIII]`, Prop. 5.8(ii), unverified) |
| **log-theta-lattice** | The full two-dimensional, non-commutative diagram/grid of $\Theta$-Hodge theaters: $\Theta$-links as horizontal arrows, log-links as vertical arrows — the structure underlying Theorem 3.11 and Corollary 3.12. | Non-commutativity is explicit and intentional (stated as "the point of the construction" by this guide's §1.2, paraphrasing IUT III); nothing beyond the stated horizontal/vertical arrow structure is asserted to commute. | IUT III's own title and abstract, **p. 1** ("…Canonical Splittings of the Log-Theta-Lattice…") |
| **indeterminacy** | Tracks the structural non-uniqueness attached to every reconstruction or gluing step; because links do not preserve ring/scheme structure, nothing crosses one except up to an explicitly named indeterminacy. | Exactly **three** named indeterminacies license comparison in Theorem 3.11's multiradial representation — (Ind1) label-set permutations, (Ind2) $\mathbb{Z}^{\times}$-indeterminacies on local units via the $\Theta/\Theta^{\times\mu}$-link, (Ind3) "upper semi-compatibility" of log-Kummer correspondences — plus a separate ${}^{\ddagger}\Pi_v$-conjugacy indeterminacy on the $\Psi_{\mathrm{cns}}$ reconstruction (§1.3). Whether Step (xi) legitimately uses (Ind1)–(Ind3) for the comparison it performs is exactly the disputed question (`IUT-N2`, **DISPUTED**) — not resolved here. | IUT III, pp. 12–13 (Theorem 3.11's indeterminacy statement); IUT II, **Cor. 4.6**, p. 137 (`IUT-B5`, reconstruction-specific) |

---

## 2. The hinge: Theorem 3.11 and Corollary 3.12 (IUT III)

The reconstruction algorithms are assembled, for a whole lattice of theaters
at once, into the **multiradial representation** — IUT III, **Theorem 3.11**
("Multiradial Algorithms via LGP-Monoids/Frobenioids", p. 153; `IUT-N1`;
restated in the Introduction as "**Theorem A**", p. 19). "Multiradial"
means the representation is built to make sense simultaneously from the
point of view of *every* theater in the lattice, not only the one the data
came from. It is well-defined only up to three named indeterminacies, stated
at IUT III pp. 12–13 and invoked throughout Theorem 3.11:

- **(Ind1)** — automorphisms of processions of $D^{\vdash}$-prime-strips (label-set
  permutations);
- **(Ind2)** — automorphisms of $F^{\vdash\times\mu}$-prime-strips along the
  $\Theta/\Theta^{\times\mu}/\Theta^{\times\mu}_{\mathrm{lgp}}$-link ($\mathbb{Z}^{\times}$-indeterminacies on local copies of $O^{\times\mu}$);
- **(Ind3)** — the indeterminacy from the "upper semi-compatibility" of
  log-Kummer correspondences along one vertical line of the lattice.

**Corollary 3.12** ("Log-volume Estimates for $\Theta$-Pilot Objects", IUT III,
p. 173; `IUT-N2`; restated as "**Theorem B**" in the Introduction, pp.
21–22) is stated "in the situation of Theorem 3.11" and concludes, for the
procession-normalized mono-analytic log-volumes of a $\Theta$-pilot and a $q$-pilot
object, an inequality of the shape $-\lvert\log(\Theta)\rvert \geq -\lvert\log(q)\rvert$, i.e. $C_{\Theta} \geq -1$
for any real $C_{\Theta}$ with $-\lvert\log(\Theta)\rvert \leq C_{\Theta}\cdot\lvert\log(q)\rvert$. The proof runs pp.
173–186 in labeled steps (i)–(xii). **Step (xi)** (pp. 181–185) is where the
multiradial algorithm's output — built relative to one arithmetic
holomorphic structure, i.e. one column of the lattice — is compared, via a
gluing isomorphism across the $\Theta$-link, against the adjacent column's
representation of the $q$-pilot object, upgrading local isomorphisms of
prime-strips to a log-volume inequality by passing to determinants of
localized arithmetic vector bundles of rank $>1$ (IUT III, p. 183, contrasts
these with the rank-1 arithmetic line bundle underlying the $q$-pilot
object). **This is the exact passage
Scholze and Stix dispute**, and the passage Mochizuki's own responses
repeatedly identify as the locus of the disagreement. The full technical
back-and-forth is carried in `guide/05-critical-transition.md` (ID
`IUT-N2` in [04](04-claim-dependencies.md) links to it); the summary needed
to keep this route legible is in §7 below.

A precision worth stating plainly: Mochizuki writes, in *Essential Logical
Structure of IUT* (p. 112), that the passage from Theorem 3.11 to Corollary
3.12 is, in his word, **"relatively straightforward,"** and frames the
construction as preserving a logical "AND" relation ($\wedge$) rather than a
chain of intermediate inequalities (p. 113; see the non-proof toy model in
§8.2). Read in context, this is a claim about logical *shape*, conditional
on the legitimacy of the comparison performed in Step (xi) — it is not a
claim that Step (xi) is uncontested. The two things that are true at once:
(a) the disputed content is concentrated at one joint (Step (xi) of
Corollary 3.12's own proof), not spread across a long derivation, and (b)
that one joint is exactly what remains contested. Do not read
"straightforward" as "undisputed."

---

## 3. From Corollary 3.12 to an explicit number: IUT IV, Theorem 1.10

IUT IV's Introduction states that it takes the log-volume estimates obtained
in IUT III and applies them "to verify various diophantine results" (pp.
1–2). The first is **Theorem 1.10** — note the title, "Log-volume Estimates
for $\Theta$-Pilot Objects," is *word-for-word identical* to Corollary 3.12's title
(IUT IV, p. 22; `IUT-N3`). Its statement opens by fixing a collection of
initial $\Theta$-data as in IUT I, Definition 3.1, and then — in words close to
Mochizuki's own — "suppose that we are in the situation of [IUTchIII],
Corollary 3.12" (IUT IV, p. 22), before adding further conditions on $E_F$
(paraphrased, not quoted, below).

Theorem 1.10 is **not** an independent new derivation; it is Corollary 3.12
specialized and made numerically explicit for one fixed $E_F$, under
additional hypotheses absent from Corollary 3.12 itself: good reduction
outside $2\ell$, plus a rationality assumption on 2-, 3- and 5-torsion fields
(defining the "tripodal" field $F_{\mathrm{tpd}}$). Given these, Theorem 1.10 states an
inequality with fully explicit constants ($d^{*}_{\mathrm{mod}} = 2^{12}\cdot3^3\cdot5\cdot d_{\mathrm{mod}}$,
$e^{*}_{\mathrm{mod}}$, etc.) in place of Corollary 3.12's abstract $C_{\Theta}$. **This is the
first place a single arrow needs a qualifying label rather than a bare
arrowhead** — see §7.

---

## 4. From one curve to every curve: Corollary 2.2 and the external import `[GenEll]`

Theorem 1.10 concerns one elliptic curve $E_F$ meeting the stated hypotheses.
**Corollary 2.2** ("Construction of Suitable Initial $\Theta$-Data," IUT IV, p. 41;
`IUT-N4`) is the bridge to arbitrary elliptic curves: starting from the
"$\lambda$-line" $X = \mathbb{P}^1_{\mathbb{Q}} \setminus \{0,1,\infty\}$ and a compactly bounded set $K_V \subseteq U_X(\mathbb{Q})$, it
shows that for any degree bound $d$ and any point $x_E \in U_X(\mathbb{Q})$ of degree
$\leq d$ in $K_V$, **outside a finite exceptional set $\mathrm{Exc}_d$**, the
corresponding $E_F$/$F_{\mathrm{mod}}$ can be equipped with initial $\Theta$-data satisfying
Theorem 1.10's hypotheses, with explicit inequalities relating $\log(q)$ to a
height function. The mechanism licensing this — relating $E_F$'s height to
the canonical height $\mathrm{ht}_{\omega_X(D)}$ on the general curve $X$ — is not proved
in IUT IV: it is imported from **`[GenEll]`** = S. Mochizuki, *Arithmetic
Elliptic Curves in General Position*, Math. J. Okayama Univ. 52 (2010), pp.
1–28 (`IUT-G1`), a paper published **eight years before IUT I–IV were first
posted**, with no connection to the 2018 dispute. IUT IV cites `[GenEll]`,
Example 1.3(ii), Remark 3.3.1, and Definition 1.2(ii) directly inside
Corollary 2.2's own statement and proof (pp. 41–42). **The plan's
dependency chain nowhere mentions `[GenEll]`** — see §7.

---

## 5. The general inequality and the classical descent: Corollary 2.3

**Corollary 2.3** ("Diophantine Inequalities," IUT IV, p. 54; `IUT-N5`)
states, for an arbitrary smooth proper geometrically connected curve $X$
over a number field, reduced divisor $D$, $U_X = X \setminus D$ hyperbolic, degree
bound $d$, and $\varepsilon > 0$, a bounded-discrepancy inequality of the shape
$\mathrm{ht}_{\omega_X(D)} \lesssim (1+\varepsilon)(\mathrm{log\text{-}diff}_X + \mathrm{log\text{-}cond}_D)$ on $U_X(\mathbb{Q})_{\leq d}$. Its proof is
two sentences, stating in substance that Corollary 2.3's content
**"coincides precisely"** with `[GenEll]`, Theorem 2.1(i) (p. 54,
paraphrased apart from the quoted clause), with the remainder reducing to
`[GenEll]`, Theorem 2.1(ii), using Corollary 2.2 to supply the needed
bounded-discrepancy-class equality. This statement is **verbatim** IUT IV's
own Introduction-level "**Theorem A**" (p. 3) — confirmed by direct
comparison of the two statements' opening clauses.

**Naming trap, stated explicitly**: IUT III's Introduction *also* has its
own "Theorem A" (a restatement of Theorem 3.11, p. 19) and its own "Theorem
B" (a restatement of Corollary 3.12, pp. 21–22). "Theorem A" names three
*different* statements depending on which paper's Introduction is open.
Always check which paper is being cited before trusting an informal
reference to "Theorem A."

IUT IV's Introduction then states, immediately after its Theorem A, that
the Vojta conjecture for hyperbolic curves, the abc conjecture, and the
Szpiro conjecture for elliptic curves all **"follow as special cases"** of
Theorem A, citing `[Vjt]` for the detailed reduction (p. 2, paraphrased
apart from the quoted clause), where `[Vjt]` = P. Vojta, *Diophantine
approximations and value distribution theory*, Lecture Notes in Mathematics
1239, Springer (1987) (`IUT-N6`). This
final descent — writing abc via Frey curves and Belyi maps as a statement
about $\mathbb{P}^1 \setminus \{0,1,\infty\}$-valued points, matching $\mathrm{ht}_{\omega_X(D)}$/$\mathrm{log\text{-}diff}$/
$\mathrm{log\text{-}cond}$ against the classical height/radical formulation — is **pre-IUT,
classical** mathematics, not reproved inside IUT IV, and it is **not** part
of the Scholze–Stix dispute: their own essay independently walks the same
classical Belyi-map reduction in its §1 without objection, before turning to
their actual criticism. Both sides of the dispute treat this final step as
settled.

---

## 6. The chain, assembled

```
[IUT-B1] initial Θ-data (IUT I, Def. 3.1, p.61)
      |
      v
[IUT-B2] Theta-Hodge theater (IUT I, Def. 3.6, p.87)
      |
      +--> [IUT-B3] Theta-link (IUT I, Cor. 3.7, p.88)        -+
      +--> [IUT-B4] log-link (IUT III, Prop. 1.2/1.3)          |  together: the
      +--> [IUT-B5] reconstruction Psi_cns (IUT II, Cor. 4.6)  |  log-theta-lattice
                                                               v
                                             [IUT-N1] Theorem 3.11 -- multiradial
                                             representation + (Ind1)(Ind2)(Ind3)
                                             (IUT III, p.153)
                                                               |
                                    DISPUTED: Step (xi), pp.181-185 (see sec.7, sec.4 of 04)
                                                               v
                                             [IUT-N2] Corollary 3.12 -- C_Theta >= -1
                                             (IUT III, p.173)
                                                               |
                              + extra hypotheses on E_F (good reduction outside 2l,
                                torsion-field conditions; IUT IV p.22)
                                                               v
                                             [IUT-N3] Theorem 1.10 -- explicit
                                             inequality, ONE E_F (IUT IV, p.22)
                                                               |
      [IUT-G1] [GenEll] (2010, external, ------------------->  |  imported, not
               pre-IUT, not disputed)                          |  reproved here
                                                               v
                                             [IUT-N4] Corollary 2.2 -- suitable
                                             initial Theta-data for ALL points outside
                                             a finite Exc_d (IUT IV, p.41)
                                                               |
      [IUT-G1] [GenEll] Thm 2.1(i) ("coincides precisely") -->  |
                                                               v
                                             [IUT-N5] Corollary 2.3 = "Theorem A"
                                             of IUT IV's own Introduction (p.54 / p.3)
                                                               |
      classical: Frey curves, Belyi maps, [Vjt] = Vojta 1987 ->|  classical,
               (pre-IUT; both sides of the dispute agree here) |  not IUT-specific
                                                               v
                                             [IUT-N6] abc / Vojta / Szpiro
                                             "follow as special cases" (IUT IV, p.1-2)
```

---

## 7. Why this is a graph, not a line — correcting the plan's chain

`Research-project-plan.md` draws a single chain (its Stage-1 diagram: IUT
I → II → III (Cor. 3.12) → IV → abc/Szpiro/Vojta; and, modeled on Lean
declaration names elsewhere, `Corollary 3.12 variant ⇒ Theorem 1.10 ⇒
Corollary 2.2 ⇒ Corollary 2.3 ⇒ ABC`). Having traced the primary sources
directly, three corrections are warranted. None is a criticism of the
plan's overall strategy, which explicitly calls for expanding every arrow
and recording prerequisites per node (see `Research-project-plan.md` and
this guide's [08-work-queue.md](08-work-queue.md), Stage 6) — this section
is that expansion, for the primary-paper half of the route.

1. **A missing external input.** `[GenEll]` (2010) feeds into **both**
   Corollary 2.2 and Corollary 2.3 as an explicit, named, load-bearing
   citation — Corollary 2.3's entire proof is a two-line reduction to it. A
   text search of `Research-project-plan.md` for "GenEll", "General
   Position", or "Okayama" returns no matches. Any chain omitting it is
   missing a real edge: the generalization from "one curve in sufficiently
   general position" (Theorem 1.10) to "the Diophantine inequality for an
   arbitrary hyperbolic curve" (Corollary 2.3) is `[GenEll]`'s work,
   imported, not IUT III/IV's.
2. **"Corollary 3.12 ⇒ Theorem 1.10" is a specialization, not a bare
   implication.** Theorem 1.10 requires hypotheses on $E_F$ absent from
   Corollary 3.12 (good reduction outside $2\ell$; 2/3/5-torsion rationality).
   A single arrowhead invites reading Theorem 1.10 as unconditionally
   downstream of Corollary 3.12 the way a corollary follows a lemma; it is
   closer to "Corollary 3.12, under a further restriction of scope, made
   numerically explicit."
3. **The single arrow "Theorem 3.11 ⟹ Corollary 3.12" hides exactly where
   the risk is concentrated.** The transition is correctly flagged by the
   plan as central, but a reader could still conclude the whole transition
   is uniformly contested. It is not: both Mochizuki's own account (§2
   above) and the Scholze–Stix essay locate the entire weight on Step (xi)
   of Corollary 3.12's *own* proof — a single comparison, not a long
   derivation. The useful unit of dispute is "Step (xi)," not "everything
   between 3.11 and 3.12."

**Unresolved edges, stated explicitly** (status IDs refer to
[04-claim-dependencies.md](04-claim-dependencies.md)):

- `IUT-N1 → IUT-N2` (Step (xi) specifically): **DISPUTED**. Not resolved by
  this guide and not resolved in the public literature as of the sources
  checked here (2018 exchange through the 2024/2025 status reports).
- `IUT-N2 → IUT-N3`: asserted in IUT IV under extra hypotheses; no published
  rebuttal specific to this step was found, but it **inherits** `IUT-N2`'s
  disputed status as an upstream premise. An implication can be internally
  valid while its premise remains contested; this guide does not collapse
  the two.
- `IUT-N3 → IUT-N4 → IUT-N5`: asserted, conditional on `[GenEll]`, which was
  not itself found to be disputed by any source checked — but this guide
  did not independently re-derive `[GenEll]`'s own proofs, so treat "no
  dispute found" as exactly that, not as independent re-verification.
- `IUT-N5 → IUT-N6`: classical; both sides of the 2018 dispute treat it as
  unproblematic.

---

## 8. A non-proof analogy (clearly marked)

**Everything in this section is illustration, not derivation. It
establishes nothing.** It is included only to build intuition for how a
multiradial representation plus an "AND-relation" could plausibly produce a
single inequality, and for what Scholze–Stix say goes wrong. Two parts below
are Mochizuki's own simplified models (explicitly labeled by him as
rough/elementary); the third is this file's own plain-language framing,
written for this guide and not sourced to Mochizuki.

### 8.1 Mochizuki's own "A, B" toy model (his words: "very rough")

In his February 2019 report on the March 2018 discussions (`Rpt2018`, §2,
pp. 1–2), Mochizuki offers a deliberately "very rough" schematic, to
characterize what he believes is the critics' misreading, using two positive
reals $A, B$:

- $\Theta$-link ↔ a defining relation $-2B = -A$;
- Theorem 3.11 ↔ a proved inequality $-2B \leq -2A + 1$;
- combined ↔ Corollary 3.12: $-A \leq -2A + 1$, i.e. $A \leq 1$.

He states that an *additional* simplifying assumption "$A = B$" — which he
attributes to the critics' reading — forces $A = B = 0$, contradicting
positivity, and superficially looks like a proof the theory is
inconsistent; he argues the theory's own content already fails under that
extra assumption, so the apparent contradiction is an artifact of an
illegitimate simplification, not a flaw in IUT (p. 2). **This is Mochizuki's
own characterization of the disagreement, not a neutral description of
Scholze–Stix's actual argument** — their own technical objection is more
specific than "set $A = B$"; see §4 of [04](04-claim-dependencies.md) and
`guide/05-critical-transition.md` for their own wording.

### 8.2 Mochizuki's "$\wedge$ vs $\vee$" elementary model

In *Essential Logical Structure of IUT* (Example 2.4.5, pp. 51–52),
Mochizuki gives a second, more refined toy model with reals $A, B > 0$,
$0 \leq \varepsilon \leq 1$, and a symbol $N$: an "$\wedge$" reading ($\Theta$-link: $(N=-2B)\wedge(N=-A)$;
multiradial representation: $(N=-2A+\varepsilon)\wedge(N=-A)$; final estimate:
$-2A+\varepsilon=-A$, i.e. $A=\varepsilon\leq1$) versus an "$\vee$" reading of the same substitutions,
in which using two distinct reals $A, B$ becomes, in his words,
"superfluous" — which he says is precisely what tempts one toward
identifying $A = B$, invalidating the "$\wedge$" reading. His conclusion (pp.
112–113) is that IUT's logical structure is "a chain of AND relations," not
"a chain of concatenated inequalities," and that the argument's validity
turns on whether the "$\wedge$" (not "$\vee$") reading of the $\Theta$-link is legitimate —
restated, more technically, as whether distinct "copies" of certain objects
may be identified. **This is exactly the question Scholze–Stix raise**, but
where this toy model treats their objection as resting on an invalid
"$\vee$"-style identification, their own essay argues the issue is forced by
needing *consistent* identifications among several specifically-named
copies of one-dimensional real vector spaces in the actual construction, not
introduced by any simplification of their own. Reading only one side's toy
model gives a one-sided picture — see the dispute file for both sides
stated in their own terms.

### 8.3 This guide's own plain-language framing (not Mochizuki's; illustrative only)

> Picture each $\Theta$-Hodge theater as a sealed room containing one complete,
> self-consistent copy of ordinary number theory, built around one elliptic
> curve. The **$\Theta$-link** is a pass-through hatch between two adjacent rooms —
> but the hatch does not let ring-theoretic structure through, only a
> specific correspondence between two designated objects (a "$\Theta$-pilot" on one
> side, a "$q$-pilot" on the other). **Reconstruction** is the instruction
> manual for redescribing anything in one room using only what is visible
> through the hatch — Galois-theoretic data — so that observers in *every*
> room can agree on a description ("multiradiality"). The final estimate
> (Corollary 3.12) is a receipt comparing the redescribed size of the
> $\Theta$-pilot against the $q$-pilot's own size, with a small, explicitly bounded
> "handling fee" (the indeterminacies (Ind1)–(Ind3)) built in. The 2018
> dispute is about whether that receipt double-counts something — whether
> two quantities the construction treats as "the same resized object, seen
> from two rooms" are in fact independent copies that have been silently
> identified.

This paragraph is an aid to intuition only. It does not appear in, and is
not attributed to, any primary source, and it resolves nothing about
whether the comparison in Step (xi) is sound.

---

## 9. What this route does **not** establish

- It does not establish that IUT III Theorem 3.11 or Corollary 3.12 are
  correct. Their status is `ASSERTED_IN_IUT`, and Corollary 3.12's proof
  specifically carries an additional `DISPUTED` flag — see
  [04-claim-dependencies.md](04-claim-dependencies.md).
- It does not establish that the abc conjecture has been proved. As of the
  sources checked for this guide, abc is not treated as proved by
  mathematical consensus; this file reports what Mochizuki's papers assert
  and what has and has not been independently corroborated, not a verdict.
- The existence of a Lean formalization of parts of the IUT IV → abc route
  (see [04](04-claim-dependencies.md) §5) does **not** mean any part of IUT
  I–III has been formally verified. That project's own documentation says
  so explicitly, and this guide preserves the caveat rather than smoothing
  it over.
- This file does not re-derive or independently check `[GenEll]`'s own
  proofs, IUT IV Propositions 1.1–1.8, or the absolute-anabelian-geometry
  papers behind `IUT-B5`. These are recorded as gaps, not silently assumed.

---

## 10. Primary-source reading exercises

Do these with the PDFs open; URLs are in
[04-claim-dependencies.md](04-claim-dependencies.md) §7.

1. Open **IUT III at p. 173** and read Corollary 3.12's statement, then the
   proof through Step (iv) only. In your own words: what is a "$\Theta$-pilot
   object" and a "$q$-pilot object" (Definition 3.8, p. 112), and what does
   $-\lvert\log(\Theta)\rvert$ measure? Do not read Step (xi) yet.
2. Open **IUT III at p. 181 (Step (xi))** next to the Scholze–Stix essay's
   technical section (see [04](04-claim-dependencies.md) §4 for the exact
   pinpoint and URL). List the distinct copies of 1-dimensional real vector
   spaces Scholze–Stix say are in play, and find the corresponding objects
   in Mochizuki's own text of Step (xi). Can you locate the specific
   isomorphism they say is used inconsistently?
3. Open **IUT IV at p. 22 (Theorem 1.10)** and underline every hypothesis
   not already part of Corollary 3.12's statement (IUT III, p. 173). This
   directly checks §3 above.
4. Open **IUT IV at p. 54 (Corollary 2.3)** and `[GenEll]`'s Theorem 2.1 side
   by side (URL in [04](04-claim-dependencies.md) §7). Confirm for yourself
   whether the two statements "coincide precisely," as IUT IV's proof
   claims.
5. Find this project's own treatment of the LANA Lean repository (see
   [04-claim-dependencies.md](04-claim-dependencies.md) §5 and its
   references) and locate the Lean structure encoding a "Corollary 3.12"
   hypothesis. Identify which field is assumed versus derived, and compare
   it to Corollary 3.12's actual conclusion in IUT III. Are they the same
   statement?

---

*Owned file: `guide/03-iut-route.md`. Companion claim table, status legend,
full reference URLs, and gap list: `guide/04-claim-dependencies.md`. For the
abc conjecture's own precise statement, see
[01-abc-target.md](01-abc-target.md); for the project's shared evidence
framework, see [00-map.md](00-map.md); for the full Scholze–Stix technical
exchange, see `guide/05-critical-transition.md`, and for a commit-pinned
line-by-line Lean audit of the LANA repository, see
`guide/06-lean-boundary.md` (both maintained by other strands of this
project, confirmed present as of this writing, and not re-verified in full
by this file — check the guide's directory listing or
[00-map.md](00-map.md) if either filename has since changed).*
