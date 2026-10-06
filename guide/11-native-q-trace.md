# 11. XI-002: attempt to trace the fixed native $q$-value

**Bounded result (2026-10-06): `UNRESOLVED_OBLIGATION`.** The
currently hosted IUT III, Step (xi-f), **asserts** exact membership
of the native $q$-pilot value in an output half-line. Three independent
paper-native traces, a separate source-fidelity check, and a
mathematical-inference check did not derive that membership from the
preceding passages they inspected. This does **not** establish that
the published claim is false, that a lemma is absent from the full
literature, or that abc is true or false. This is a report on one
arrow, [the `I-6` to `I-7` obligation](09b-object-identity-ledger.md).

Fix initial $\Theta$-data satisfying the paper's hypotheses (IUT I
Definition 3.1 includes $\ell\ge5$ and nonempty bad places), and
write, in the paper's respective normalizations,

$$
r=-|\log(q)|<0,\qquad s=-|\log(\Theta)|,\qquad
B_s=\{t\in\mathbb R:t\le s\}.
$$

The claim at [IUT III (xi-f), PDF/printed p.
184](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=184)
is $r\in B_s$, equivalently $|\log(q)|\ge|\log(\Theta)|$.
The reference in (xi-e) to an *approximate construction of the
input log-volume* does not qualify away the exact membership printed
in (xi-f).

## Graduate-level walkthrough (intuition only)

The inequality in (xi-f) is $r\le s$ for **one fixed native $r$**,
not a claim that *some* output in a hull has value at most $s$.
Remark 3.9.5 (Ob8)/(Ob9) compares hull log-volumes **vertically**;
the (xi-c)--(xi-d) hull and determinant operations build an output
bound. The unresolved composition is a permitted, choice-compatible
**numerical** route from that fixed $r$ to an output governed by
the bound. The table below records where each candidate route
starts and stops without asserting that they compose.

Normalization matters even for elementary inequalities: if both
sides were multiplied by the **same positive** integer $M$, then
$Mr\le Ms$ would imply $r\le s$. But the paper's tensor/determinant
constructions require their *own* source-licensed identifications
before one may write such an inequality for the native input.
Likewise "approximate construction" in (xi-e) cannot simply replace
the **exact** membership asserted in (xi-f). For a row in the
trace, try naming its source, target, allowed choice, and numerical
effect before using it as a map.

**Background, not verification:** [the prerequisite route](02-prerequisites.md),
[the preceding XI-001 experiment](10-xi-001.md), and
[Arakelov theory on Wikipedia](https://en.wikipedia.org/wiki/Arakelov_theory)
for general degree/height motivation, not IUT's particular formulas.

## Corpus, procedure, and status words

The [XI-002 frozen packet](sources.md#xi-002-source-packet-2026-10-06)
records the eight PDF URLs, editions, and SHA-256 fingerprints
(`I1`--`I4`, `D1`--`D4`). All eight packet copies matched that
manifest; local IUT I, II, and the optional IV also matched freshly
downloaded official PDFs. Three readers received the **same neutral
question** and the same packet, without each other's drafts or the
earlier XI-001 interpretation. A distinct reader checked the
rendered glyphs, source attributions, and key page labels; a
mathematical referee checked only the source-vetted premises.
The PDF indices and printed folios coincide at the IUT passages
cited below.

The two newly named IUT III and Scholze--Stix files supplied locally
are byte-identical to the already pinned hosted copies; the supplied
`SS2018-08.pdf` is a one-page *Not Found* response, **not** the
August 2018 report cited in Mochizuki's comments. The historical
2018 SS revision and the contemporary IUT III text have not been
compared with these editions. None of these PDFs is copied into
this repository.

`SOURCE_VERIFIED` means a **specified source passage** says what
its cell reports; `STANDARD` is a mathematical consequence we can
check separately; `ASSERTED_IN_IUT` marks a printed conclusion,
not a separately checked inference; `SOURCE-MISMATCH` rejects a
proposed attribution to that passage; `UNRESOLVED_OBLIGATION`
means a needed link was not established **within the inspected
corpus**; `COUNTEREXAMPLE` would require an example satisfying
*all* the relevant paper hypotheses. None was produced.

## The two strands are not yet a composed map

In the table, $P_\beta$ is **our shorthand**, not a paper-defined
point: a possible $\Theta$-output region for an admissible combined
choice $\beta$ under (Ind1)--(Ind3). Let $H$ denote the
**one-column holomorphic hull** of the output possibilities. Write
$\mu$ for a normalized log-volume **only where the cited passage
licenses that evaluation**. The rows record possible construction
routes; their order does **not** assert that the fixed $q$-value
passes through every row. Unless otherwise indicated, locators are
one-based PDF **and** printed pages in [the primary source
register](sources.md).

| # / passage | Domain | Operation or map | Codomain | Allowed choices | Normalization | Quantitative consequence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 / `I-6`: I1 Def. 3.1, pp. 61--63, Ex. 3.2(iv), p. 71; I3 Def. 3.8(i), p. 112, Cor. 3.12, p. 174, (xi-c), p. 182 | Native $q$-pilot in the $(1,0)$ global realified Frobenioid | One-column log-Kummer representation and log-volume | Represented $q$ class in $(1,\circ)$ packets; its **fixed** number $r$ | Input is **not** subject to (Ind1)--(Ind3); local decorated $\mathbf q_v=q_{E,v}^{1/(2\ell)}$ up to roots of unity | Procession-normalized $r=-|\log(q)|<0$ | Defines the input value, not an output relation | `SOURCE_VERIFIED` |
| 2 / `I-1`: I2 Def. 4.9(viii), p. 158, Rem. 4.10.3(ii), p. 162; I3 Def. 3.8(ii), p. 113, Cor. 3.12(i), p. 175 | $\Theta$-pilot prime-strip at $(0,0)$ | Horizontal $\Theta^{\times\mu}_{\mathrm{LGP}}$ **poly-isomorphism of weakened prime-strips** | Corresponding $q$-pilot prime-strip at $(1,0)$ | Paper-specified link; no ring identification | I2 says its value-group portion is **not preserved**; it gives no native-degree preservation law | Abstract pilot correspondence; **not** $\mu(\Theta)=r$ | `SOURCE_VERIFIED`; attributing native-degree equality to this link is `SOURCE-MISMATCH` |
| 3 / `I-2`: I3 Thm. 3.11(i)--(iii), pp. 153--159, (xi-b/c), pp. 181--182 | $\Theta$ data in $(0,m)$ theaters | Kummer/mono-analytic construction and étale-picture permutation representation | Possible regions $P_\beta$ in $(1,\circ)$ packets | (Ind1) procession, (Ind2) independent local, (Ind3) upper-semi-compatible vertical log-link choices | Packet weights and procession average; bare $j^2$ powers are not final hull volumes | IPL links **prime-strips**, SHE permits one-column expressibility, APT is **not** set transport | `SOURCE_VERIFIED`; no native-volume equation here |
| 4 / `I-4`: I3 Rem. 3.9.5(i)--(iv), pp. 127--129, **rendered** (xi-c), p. 182 | One-column output possibilities $P_\beta$ | Holomorphic hulling of their union | ${}^{1,\circ}\overline{\mathcal U}=H\supseteq{}^{1,\circ}\mathcal U$ | All permitted output possibilities; hull may enlarge volume **strictly** | One-column log-volume | $\mu(P_\beta)\le\mu(H)$ for compatible evaluated regions | Hull inclusion `SOURCE_VERIFIED`; monotonicity `STANDARD`; reading it as $q\subseteq H$ is `SOURCE-MISMATCH` |
| 5 / `I-5`: I3 Rem. 3.9.5(vii), (Ob3)--(Ob5), pp. 131--135; (xi-d), p. 183 | Rank-$>1$ hull $H$ | Weighted, structure-sheaf-corrected $\det^{\otimes M}$ | Comparable one-column rank-one line-bundle class | Compatible local packets and weights | $M>0$ is defined for the **chosen weighted operation**; compare with the $q$-pilot's corresponding $M$-th power, not an unscaled degree | Gives comparability of Frobenioid objects; no source-checked **order** of these two pointed classes yet | Machinery `SOURCE_VERIFIED`; native order `UNRESOLVED_OBLIGATION` |
| 6 / `I-5v`: I3 Rem. 3.9.5(vii), (Ob8)/(Ob9), pp. 137--139 | Hull log-volume classes at vertical log-link levels | Log-Kummer adjustment; realified semi-simplification | **Bijection of hull log-volume classes** across the vertical shift | Arbitrary allowed log-link iterates and their compatibility conditions | Matched hull-volume normalization | A **positive numerical compatibility claim**, not merely object comparability; it does not name the fixed native $q$ as an output | `SOURCE_VERIFIED`; using it as a selected $q$-output identity is `SOURCE-MISMATCH` |
| 7 / pre-volume loop: I3 Rem. 3.9.5(ix), pp. 141--144 | Output and input **prime-strip** structures | Claimed closed loop **up to formal quotient indeterminacies** | Prime-strip comparison before taking volume | Formal quotients and permissible choices matter | Volume follows the loop, not an assumed equality of raw values | The passage says this will yield an inequality, but supplies no separately displayed, choice-indexed fixed-$q$/output degree law in the passages inspected | Loop `SOURCE_VERIFIED`; typed numerical step `UNRESOLVED_OBLIGATION` |
| 8 / `I-5`, `I-7`: I3 (xi-d)--(xi-f), pp. 183--184 | Hull value $s$ and separately fixed input $r$ | Form $B_s$, then assert input/output membership | Exact $r\in B_s$ in (xi-f) | Output includes (Ind1)--(Ind3); the native input does not | $r$ and $s$ must be on a common signed real scale; any approximation needs explicit limiting quantifiers | $r\le s$ is **stated**, not independently derived by rows 1--7 | Statement `ASSERTED_IN_IUT`; preceding numerical implication `UNRESOLVED_OBLIGATION` |

**Where the trace stops.** Output containment establishes bounds on
*output* regions; Ob8/Ob9 establishes a meaningful **vertical**
bijection of *hull* log-volumes. The horizontal link and the
pre-volume prime-strip loop are also source-stated. None alone
identifies or bounds the **separately fixed** input number $r$
against an admissible output under the same choices and signed
normalization. The first unaccounted numerical inference, in this
bounded reconstruction, is from the relationship described in
(xi-e) to (xi-f)'s exact membership. This statement concerns
our independent derivation, **not** the existence of a paper proof.
The readers also followed candidate repairs in IUT III Theorem 1.5,
Propositions 3.9--3.10, Remarks 2.4.2 and 3.12.2, and IUT II
Definition 4.9/Corollary 4.10; none yielded a separately checked
selection-and-degree law in their traces. Further cited foundations,
including `[FrdI]`, `[FrdII]`, `[AbsTopIII]`, and `[EtTh]`, are
**outside this packet**, not silently certified or ruled out.

## Normalization mini-audit

| Check | Source-located fact | What must not be silently inferred |
| --- | --- | --- |
| Local pilot versus Tate parameter | I1 Ex. 3.2(iv), p. 71, decorates $q_{E,v}^{1/(2\ell)}$; I3 Def. 3.8(i), p. 112, uses the global realified pilot | Replace the decorated pilot by an unqualified $q_{E,v}$ in a numerical comparison |
| Packet baseline and signs | I3 Prop. 3.9(i), pp. 115--116, puts the local integral structure at volume **zero**; multiplying a local region by $p_v$ changes its log-volume by $-\log p_v$, and by $e$ at an archimedean place changes it by $+1$; Prop. 3.9(iii), p. 117, identifies global log-volume with arithmetic degree **relative to a suitable normalization** | These signs and the procession average specify local/global scales, not an inequality comparing the two pilots |
| Local weights, not a universal determinant exponent | I3 Rem. 3.1.1(iv), pp. 96--97, has a $1/N_E$ factor with $N_E=\prod_vN_v$ for **direct-product regions**; (Ob3-1), p. 132, calls for positive determinant tensor exponents matching the packet weights | The direct-product identity does not state $M=N_E$ for general hulls, or give a $1/M$ formula comparing $q$ with $\Theta$ |
| Procession labels | I3 Rem. 3.11.1(i), p. 159, gives bare $q^{j^2}$ for $1\le j\le\ell^\star=(\ell-1)/2$; Prop. 3.9, pp. 115--117, sets positive packet weights and averaging | The arithmetic average $\ell^{\star-1}\sum_j j^2=\ell(\ell+1)/12$ is **not** the indeterminacy-subject, corrected hull volume |
| Hull direction | The overbar on the **first** $\mathcal U$ in I3 (xi-c), p. 182, is visible in the PDF image but lost in text extraction; I3 Rem. 3.9.5(iv), p. 129, allows strictly larger hull volume | Neither $H\subseteq U$ nor the native $q$ region's inclusion in $H$ follows |
| Corrected determinant and $M$ | I3 (Ob3-1)--(Ob3-3), pp. 131--133, weights each local determinant and tensors it with the **inverse weighted determinant of the structure sheaf**; $M$ is the uniquely determined positive integer **for that chosen operation**, characterized by sending $\mathcal O(-)\otimes L$ to $L^{\otimes M}$, and may be chosen sufficiently divisible | No general closed formula $M=N_E$ or displayed $1/M$-normalized $q$-versus-hull inequality was found there; (Ob3-3) says the degree represents the original volume with *suitable normalization factors*, without displaying those factors |
| $M$-th pilot power and twists | I3 (Ob4), pp. 133--134, compares the corrected determinant with Frobenioid objects for the **$M$-th** $q$-pilot power and states that tensor-power-twist indeterminacies have no substantive effect on log-volumes | Such asserted comparability and twist invariance do **not** themselves state $\deg(Q_M)\le\deg(\widehat H_M)$; cancellation of $M$ would first require a proven, properly signed degree law |
| Vertical versus horizontal | I3 (Ob8)/(Ob9), pp. 137--139, compares hull log-volumes across **vertical** log-links; I2 Rem. 4.10.3(ii), p. 162, distinguishes the horizontal link's value-group portions | A vertical hull-volume bijection is not the missing horizontal identification of the native value |

Here $\mathcal M(-)$ in Prop. 3.9 denotes admissible **regions**,
not the integer $M$ in (Ob3). The basic tensor-power identity
$\deg(L^{\otimes M})=M\deg(L)$ is mathematics; neither its use
to divide by $M$ nor an order relation between the **two different
pilot-related objects** is a printed formula in (Ob3)--(Ob4).
The bare $j^2$ sum, the corrected determinant and its $M$, and
the final hull volume are **different** operations. Optional
IUT IV, pp. 27--29, gives downstream corrected hull bounds;
they cannot be inserted as an unproved Step-(xi) pilot comparison.

## Distinct readings and independent gates

| Reading | Source path it probed | First numerical question it left open |
| --- | --- | --- |
| A (native-pilot first) | IUT I's decorated $q$ generator; IUT II's value-group warning; the one-column hull and its corrected determinant | Which order-preserving, **pointed** comparison connects $q^M$ to the corrected hull determinant after permitted choices? |
| B (representation first) | IUT III's IPL/SHE/APT and étale-picture permutation, then Ob8/Ob9 and the pre-volume loop | What makes the separately fixed one-column $q$ number a bounded output value rather than merely expressible in the same column? |
| C (vertical-compatibility first) | Prop. 3.9 and arbitrary log-link iterates, then Ob8/Ob9 and Rem. 3.12.2's within-column equalities | What supplies the **cross-object**, choice-compatible signed degree law at (xi-e)--(xi-f)? |

The source-fidelity gate confirmed the overbar, exact (xi-f)
membership, both the vertical *volume* bijection and the
pre-volume loop, and the IUT II warning that the horizontal link
does not preserve value-group portions. It corrected a tempting
attribution: the bare $j^2$ components occur in I3 Rem.
3.11.1(i), p. 159 (also p. 173), **not** as a final hull-volume
formula in Rem. 3.9.5(i)--(iv). Agreement among readings is not a
proof or a source-level refutation. [Scholze--Stix's critique,
Mochizuki's reply, and Project LANA's proposed compatibility
(9-1)](10-xi-001.md) remain different interpretations and
research directions, not substitutes for this paper-native arrow.

The mathematical referee checked only the preceding *explicitly
vetted* facts. They give $\mu(P_\beta)\le s$, **not**
$r\le\mu(P_\beta)$ or $r\le s$. For example, the reduced
abstract data $r=-1$, $\mu(P)=-3$, $s=-2$ satisfy the first bound
but fail $r\le s$. This is **not** an IUT counterexample: it does
not model all the paper's hypotheses. Likewise a bare
$j^2$ average or an abstract strip isomorphism supplies no
missing order law.

An error term would help only with stated quantifiers: for
the **same fixed** $r,s$, inequalities
$r\le s+\varepsilon$ for **every** $\varepsilon>0$ imply
$r\le s$; one unspecified approximation does not. If the
output bound is $s_\varepsilon$, a separate limit control on
those bounds is required. No such limiting law has been extracted
from (xi-e) in this bounded trace.

## The next expert-ready lemma, not a guessed proof

For initial data satisfying the paper's actual hypotheses, identify
the **numbered passage and admissible choices** that compares the
fixed native $q$ class with the corrected output hull in a *common
ordered, signed real-degree target*. Specify the allowed log-link
iterate, (Ind1)--(Ind3) permissions, local weights, any sheaf
correction, and the **same positive determinant power $M$** on
both sides. For example, if source-grounded maps really give
pointed classes $Q_M,\widehat H_M$ and an order-preserving
evaluation $\nu$ with

$$
\nu(Q_M)=Mr,\qquad
\nu(Q_M)\le\nu(\widehat H_M),\qquad
\nu(\widehat H_M)=Ms,\qquad M>0,
$$

then dividing by $M$ proves $r\le s$. These equalities and the
order relation are a **request for a justified bridge**, not claims
established by this audit. With the opposite signed degree
convention the ordering must reverse. Alternatively, source-proved
$r=\mu(P_\beta)$ for a compatible output, or the weaker
$r\le\sup_\beta\mu(P_\beta)\le s$, would suffice. Such output
realization is **sufficient, not necessary**; raw geometric
$q\subseteq H$ is stronger still. Simply restating $r\le s$ as
an unnamed degree inequality is circular.

If a cited lemma supplies this typed comparison, verify each
hypothesis and inference in a **new** source gate. If an alleged
bridge attributes a native numerical equality to the weakened
horizontal poly-isomorphism or sends $q$ through Ob9 without a
pointed selection, classify that particular proposal
`SOURCE-MISMATCH`; do not turn it into a claim that IUT is
refuted. A `COUNTEREXAMPLE` requires *all* the genuine paper
hypotheses, which this run has not met. Until the lemma is
identified and checked, defer Lean and wider adversarial agent
runs as specified in the [protocol](09a-adversarial-trial.md).
