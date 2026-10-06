# 04. Claim dependency table: IUT III → IUT IV → abc

**Scope of this file.** A precise, ID-tagged ledger of every claim this
guide's companion file, [`03-iut-route.md`](03-iut-route.md), relies on to
trace a path from IUT's basic constructions through IUT III Theorem
3.11/Corollary 3.12 and IUT IV's quantitative statements to the abc
conjecture — with status, exact reference (page/section of the actual PDF
checked), and declared dependencies. Read `03` for the narrative; read this
file for the audit trail. Nothing in either file should be read as a verdict
that abc has been proved or that the disputed step has been resolved — see
`03-iut-route.md` §9 ("What this route does not establish"), which applies
equally to this file.

## 0. Pagination and edition note

All page numbers below are **PDF page numbers of the freely downloadable
preprints** hosted at `kurims.kyoto-u.ac.jp/~motizuki/` (exact URLs in §7).
Each of these PDFs is independently paginated starting at page 1. This is
**different** from the continuous, cross-paper pagination used in the 2021
journal printing of IUT I–IV in *Publications of the Research Institute for
Mathematical Sciences (PRIMS)*, vol. 57, no. 1/2 (2021): IUT I pp. 3–207,
IUT II pp. 209–401, IUT III pp. 403–626, IUT IV pp. 627–723 (DOIs
`10.4171/PRIMS/57-1-1` through `-4`). If a page number quoted here does not
match a reader's copy, check whether that copy is the journal offprint
rather than the homepage PDF.

## 1. Status legend

This file uses the five-label vocabulary this strand was instructed to use,
which matches, label-for-label, the evidence labels already fixed project-wide
in [00-map.md](00-map.md) ("Evidence labels"); definitions below are
reproduced from there for self-containedness, with one addition (†) spelled
out explicitly because it recurs in §5 below.

| Status | Meaning |
| --- | --- |
| `STANDARD` | A standard result, or one independently reproducible here; a proof or source is given. Used below both for pre-IUT classical mathematics (unqualified) and for `[GenEll]` (qualified: published/peer-reviewed, but specific to Mochizuki's own pre-IUT program — see the `IUT-G1` row). |
| `ASSERTED_IN_IUT` | A statement appearing in the published IUT I–IV papers; its precise statement and page locator are recorded. This label says only that the text asserts it, not that it has been independently checked or accepted. |
| `DISPUTED` | A specific inference or interpretation publicly challenged in the 2018 Scholze–Stix/Mochizuki exchange and its aftermath; both parties' positions are cited. |
| `CONDITIONAL_FORMALIZATION` | A Lean development that checks an implication **given** a named, explicit, unproved input; the input's exact type/statement is recorded, and the input is not itself proved. |
| `UNVERIFIED` | †A claim, document, or diagram this research pass could not check against a checked primary locator, or could check only at the level of its stated existence/scope, not its technical content. (This file applies the label both to claims "inherited from the plan without a checked locator," as in [00-map.md](00-map.md)'s original sense, and — flagged explicitly where it occurs — to primary documents that *were* read in full but do not themselves constitute a claim, proof, or verification, e.g. a slide deck self-described as a communication aid. See the `IUT-F2` row for the one case this applies to.) |

## Graduate-level walkthrough (intuition only)

This ledger is a **dependency graph**, not a list of theorems whose proofs
we have reproduced. In its main branch, `IUT-N1` (a representation)
feeds `IUT-N2` (the disputed log-volume estimate); `IUT-N3` specializes
that estimate under **extra** elliptic-curve hypotheses. The route to
`IUT-N4`/`IUT-N5` also imports `[GenEll]`, which does not follow from
the IUT III estimate. A downstream implication can be perfectly valid
*conditional on its parent* while leaving that parent's proof open.

For a graduate-reader check, choose `IUT-N2 -> IUT-N3` below: write
the input statement, the extra hypotheses, and the changed output
quantity separately. Then compare the Lean row `IUT-F1`: a theorem
assuming a Corollary 3.12 **variant** cannot certify the original
`IUT-N2` edge. The status column labels *claims and arrows*, not
how confidently a reader feels about the whole proof.

**Further background, not evidence for any arrow:** the
[narrative route](03-iut-route.md), [abc overview](01-abc-target.md),
and [Wikipedia on elliptic curves](https://en.wikipedia.org/wiki/Elliptic_curve).

## 2. Claim dependency table

`ID` values are namespaced `IUT-*` to avoid collision with `sources.md`'s own
`G1`/`C1`/`S1`/`L1` source-register IDs, which index *documents*, not
*claims*. "Depends on" lists only dependencies tracked in this table — it is
not a full prerequisite list (e.g. every row also implicitly depends on
ordinary scheme theory, Galois theory, and Frobenioid theory, not itemized
here; see [02-prerequisites.md](02-prerequisites.md) and
[03-iut-route.md](03-iut-route.md) §1.4/[07-dictionary.md](07-dictionary.md)
for that layer).

| ID | Claim | Status | Reference | Depends on |
| --- | --- | --- | --- | --- |
| `IUT-B1` | Initial $\Theta$-data: number field $F \supseteq \sqrt{-1}$, elliptic curve $E_F$, prime $\ell \geq 5$, valuation set $V$, $V^{\mathrm{bad}}_{\mathrm{mod}}$, sign datum $\varepsilon$ | `ASSERTED_IN_IUT` | IUT I, Def. 3.1, p. 61 | — |
| `IUT-B2` | $\Theta$-Hodge theater: the package $(\{{}^{\dagger}F_v\},\ {}^{\dagger}F^{\Vdash}_{\mathrm{mod}})$ | `ASSERTED_IN_IUT` | IUT I, Def. 3.6, p. 87 | `IUT-B1` |
| `IUT-B3` | $\Theta$-link: Frobenioid-theoretic correspondence between $\Theta$-pilot and $q$-pilot objects of adjacent theaters; not a ring/scheme morphism | `ASSERTED_IN_IUT` | IUT I, Cor. 3.7(i), p. 88 | `IUT-B2` |
| `IUT-B4` | log-link: vertical lattice direction, via the $p$-adic logarithm on local units | `ASSERTED_IN_IUT` | IUT III, Prop. 1.2 p. 30 / Prop. 1.3 p. 41 | `IUT-B2` |
| `IUT-B5` | Reconstruction algorithm $\Psi_{\mathrm{cns}}$ (mono-anabelian style), well-defined up to ${}^{\ddagger}\Pi_v$-conjugacy | `ASSERTED_IN_IUT` | IUT II, Cor. 4.6, p. 137 | `IUT-B2` |
| `IUT-N1` | Theorem 3.11: multiradial representation of the LGP-monoid/Frobenioid data, up to (Ind1)/(Ind2)/(Ind3) | `ASSERTED_IN_IUT` | IUT III, Thm. 3.11, p. 153 (= Intro "Theorem A", p. 19) | `IUT-B1…B5`, Def. 3.8 p. 112 |
| `IUT-N2` | Corollary 3.12: log-volume estimate $C_{\Theta} \geq -1$ for $\Theta$-pilot vs. $q$-pilot objects | `ASSERTED_IN_IUT`; proof's Step (xi), pp. 181–185, is `DISPUTED` | IUT III, Cor. 3.12, p. 173 (= Intro "Theorem B", pp. 21–22) | `IUT-N1` |
| `IUT-N3` | Theorem 1.10: Corollary 3.12 specialized to one $E_F$ with explicit constants, under extra hypotheses (good reduction outside $2\ell$; 2/3/5-torsion rationality) | `ASSERTED_IN_IUT` | IUT IV, Thm. 1.10, p. 22 | `IUT-N2` (+ extra hypotheses, not part of `IUT-N2`) |
| `IUT-N4` | Corollary 2.2: suitable initial $\Theta$-data exist for every point of bounded degree in a compact $K_V$, outside a finite exceptional set $\mathrm{Exc}_d$ | `ASSERTED_IN_IUT` | IUT IV, Cor. 2.2, p. 41 | `IUT-N3`, `IUT-G1` |
| `IUT-N5` | Corollary 2.3: Diophantine inequality $\mathrm{ht}_{\omega_X(D)} \lesssim (1+\varepsilon)(\mathrm{log\text{-}diff}+\mathrm{log\text{-}cond})$ for arbitrary hyperbolic $U_X$; "coincides precisely" with `[GenEll]` Thm. 2.1(i) | `ASSERTED_IN_IUT` | IUT IV, Cor. 2.3, p. 54 (= Intro "Theorem A", p. 3) | `IUT-N4`, `IUT-G1` |
| `IUT-N6` | abc, Vojta (hyperbolic curves), and Szpiro conjectures "follow as special cases" of `IUT-N5`, via classical Frey-curve/Belyi-map reduction and `[Vjt]` | `STANDARD` (classical descent step itself; conclusion of the overall route is not thereby `STANDARD` — see `03-iut-route.md` §9) | IUT IV, pp. 1–2, citing `[Vjt]` = Vojta, *Diophantine approximations and value distribution theory*, LNM 1239 (1987) | `IUT-N5` |
| `IUT-G1` | `[GenEll]` Thm. 2.1: height/general-position results for elliptic curves, used by both `IUT-N4` and `IUT-N5` | `STANDARD` (qualified — see §1) | S. Mochizuki, *Arithmetic Elliptic Curves in General Position*, Math. J. Okayama Univ. 52 (2010), pp. 1–28 | — (pre-dates IUT I–IV; not itself part of the 2018 dispute) |
| `IUT-F1` | Pinned LANA Lean repository: the unproved proposition `Corollary312Variant X := X.qPilot.lhs ≤ X.rhsData.rhs` is an **assumption** of a conditional theorem concluding `ClassicalABC`; a different `Corollary312Input` is *sketched in a Markdown plan* | `CONDITIONAL_FORMALIZATION` | [`Statement.lean:78–91`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91), [`ClassicalAbcGenuineCanLift.lean:37–46`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46), [pinned plan](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Plans/Iut4Sec1Spec.md) | Assumes a stand-in for `IUT-N2`; neither the Lean variant nor the plan's distinct placeholder proves `IUT-U1` or the published Step (xi) |
| `IUT-F2` | Mochizuki/RIMS "Formalization of IUT" slide deck: skeletal Lean material targeting an informally-labeled step "3.11.5 ⟹ 3.12" | `UNVERIFIED` (read in full; self-described as a communication aid, not a verification — see §5) | `Formalization of IUT (2026-04).pdf`, kurims homepage (URL §7) | Related informally to `IUT-N1`→`IUT-N2`; not a checked derivation of either |
| `IUT-U1` | Project LANA's proposed compatibility: for a suitable admissible $S$, the native $q$-pilot map $\eta_q$ equals the reconstructed map $\eta^{\mathrm{anab}}_S$ | `UNVERIFIED` **compatibility**; the report itself was read directly | [Interim report](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf), §9.2, PDF p. 46, equation (9-1); authors explicitly report no proof in §10.5, p. 49 | Candidate link in the `IUT-N1`→`IUT-N2` dispute, **not** a consequence established by `IUT-F1`; see [09](09-critical-mechanism.md) |

---

## 3. The disputed edge in detail: `IUT-N2`, proof Step (xi)

This section gives the minimum needed to understand *what* is disputed and
*where*, with the exact citations. **The full ten-page technical exchange
(sources, dates, access status, and a line-by-line reading of both texts) is
carried in `guide/05-critical-transition.md`, confirmed present as of this
writing** (consult this directory's current index, e.g.
[00-map.md](00-map.md), if that filename has since changed). What follows
was independently checked against the primary texts during this research
pass and does not depend on that other file.

**The claim in dispute.** Corollary 3.12's proof (IUT III, pp. 173–186)
compares, in Step (xi) (pp. 181–185), the multiradial representation
constructed in Theorem 3.11 for one column of the log-theta-lattice against
the $q$-pilot object's representation in an adjacent column, via what Step (xi-a)
calls "a sort of gluing isomorphism" across the $\Theta$-link, and
asserts a log-volume inequality.

**Scholze–Stix's objection** (S. Scholze and J. Stix, *Why abc is still a
conjecture*, 2018; §2.2, "Proof of [IUTT-3, Corollary 3.12]", pp. 9–10 of
their own PDF pagination): they identify several distinct copies of
1-dimensional real vector spaces that appear in the construction (in their
own notation: $R_{\odot,\Theta}$, $R_{\odot,q}$, $R_{\odot c,\Theta_j}$, $R_{\odot c,q}$, $R_{\Theta}$, $R_q$)
and argue that making the identifications Mochizuki's argument requires
forces either (a) an inequality that is vacuously true ("empty"), or (b), if
Mochizuki's stated indeterminacies (Ind1)–(Ind3) are invoked to avoid
vacuity, a loss of precision they describe as "blurring … by a factor of at
least $O(\ell^2)$," which they say renders the inequality "useless" for the
intended Diophantine application. Their essay opens (p. 1) with the
assessment "there is no proof," characterizing the problem as "so severe
that … small modifications will not rescue the proof strategy."

**Mochizuki's response.** Across several documents — `Rpt2018` (February
2019 report on the March 2018 discussions), `Cmt2018-05`/`Cmt2018-08`
(2018 comments on Scholze–Stix's manuscript drafts), and *Essential Logical
Structure of IUT* (`EssLog`) — Mochizuki maintains that the identifications
in question are legitimate precisely because of how the indeterminacies
(Ind1)–(Ind3) are built into the multiradial representation, and that the
critics' reading effectively (if not explicitly) substitutes an illegitimate
"$\vee$"-style collapse of distinct objects for the theory's actual "$\wedge$"-style
construction (`EssLog`, Example 2.4.5, pp. 51–52, and pp. 112–113; see
`03-iut-route.md` §8.2 for the toy model, explicitly marked there as
non-proof illustration). He states that the critics' position "does not
imply the existence of any flaws whatsoever in IUTch" (`Rpt2018`, p. 2), and
(`EssLog`, §1.2, pp. 7–8) labels the critics' broader interpretive stance
"the redundant copies school [of thought]" ("RCS").

**What this guide does and does not conclude.** Both positions above are
reported, with page citations, as *assertions by their respective authors*.
This guide did not find a published, mutually-accepted resolution as of the
sources checked (through 2024–2025 status reports from Mochizuki's own
page); the matter is recorded as `DISPUTED` for exactly that reason, on
`IUT-N2`'s proof specifically, not on IUT III/IV as a whole. A reader who
wants to form their own view should read §2.2 of the Scholze–Stix essay and
pp. 181–185 of IUT III side by side (reading exercise 2 in
`03-iut-route.md` §10), not rely on either side's summary of the other.

---

## 4. A naming trap worth flagging once more here

IUT III's own Introduction uses "Theorem A" for a restatement of Theorem
3.11 (p. 19) and "Theorem B" for a restatement of Corollary 3.12 (pp.
21–22). IUT IV's own Introduction separately uses "Theorem A" for a
restatement of Corollary 2.3 (p. 3). These are three different statements.
This guide's `IUT-N*` IDs are used precisely to avoid this collision; when
consulting secondary commentary that says "Theorem A," always check which
paper's Introduction is meant.

---

## 5. Two distinct Lean efforts and a separate interim report

Two separate, independent 2026 Lean-related efforts exist. Conflating them
would misstate both. Project LANA's interim report is a further, distinct
source: reading its mathematical proposal does not imply that the Lean
repository verifies the proposal.

### 5.1 `IUT-F1` — the LANA project (`lana-agents/iut`), `CONDITIONAL_FORMALIZATION`

The repository's pinned [`README.md`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/README.md)
states that the project **"does not verify IUT."** Its actual
[`Statement.lean:78–91`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91)
defines `Corollary312Variant X : Prop` as the inequality
`X.qPilot.lhs ≤ X.rhsData.rhs`, without proving it. In the same pin,
[`classicalABC_of_variant_genuine'`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46)
is a theorem from a universally quantified **hypothesis** of that
variant to `ClassicalABC`. This is an implemented *conditional*
implication, not a Lean verification of Corollary 3.12 or Step (xi).
The [line-by-line audit](06-lean-boundary.md) explains its additional
dependencies and the distinct abstract and concrete downstream routes.

The similarly named `Corollary312Input` appears instead as a
**proposed structure in [`Plans/Iut4Sec1Spec.md`, §2.2](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Plans/Iut4Sec1Spec.md)**,
not as the proved input of the Lean theorem just cited. Its proposed
fields `CTheta : ℝ`, `neg_one_le_CTheta : -1 ≤ CTheta`, and
`cor312_relation` assume a numerical bound in a *different* planned
strand. The plan's 2026-07-20 banner says "paused after P6 —
awaiting external input" for that strand. Do not infer that pausing
this plan stops the separate, compiled variant-to-abc route, or that
either strand supplies a checked bridge to the published Corollary
3.12. These two artifacts have different carrier types; no theorem
connecting them was found in the pinned audit. The Lean repository
also depends on the separate `LANA-Project/genl` package for
`[GenEll]`-related content, as traced in [06a](06a-lean-dependencies.md).

### 5.2 `IUT-F2` — Mochizuki/RIMS's own "Formalization of IUT" material, `UNVERIFIED`

A separate, independently discovered Mochizuki/RIMS document, `Formalization
of IUT (2026-04).pdf` (URL in §7), is **not** the LANA project and is not
referenced by it. It explicitly self-describes (p. 2) as a "communication
tool," stating that verification "is not a central focal point of interest"
of the material. It targets an informally-invented step the document itself
labels "3.11.5 ⟹ 3.12" — confirmed (p. 11) **not** to correspond to any
official proposition numbering in IUT III itself; it is a label coined for
this slide deck. This guide assigns it `UNVERIFIED` rather than
`CONDITIONAL_FORMALIZATION` because, unlike LANA, no checked, named,
compiling conditional theorem with an explicit input type was found here —
the material is "skeletal" by its own description and does not present
itself as a verification artifact. This distinction (LeanForm ≠ LANA) was
not found stated elsewhere in the sources checked during this research pass
and is flagged here explicitly so the two are not merged in later
exposition.

### 5.3 `IUT-U1` — a checked report, with an unproved compatibility

The July 2026 [Project LANA interim report](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf)
is now available and was checked directly at the pinned PDF revision in
§7. In §9.2, PDF p. 46, it proposes finding a suitable $S$ such that
$\eta_q=\eta^{\mathrm{anab}}_S$ (its equation (9-1)); in §10.5, p. 49,
the authors state that they have **no proof** of this equality and have
not reached complete agreement on the original IUT argument's proof
status. The report's diagnosis is neither a proof of the equality nor a
formalization of it by the distinct, pinned Lean project (`IUT-F1`).
See [09-critical-mechanism.md](09-critical-mechanism.md) for the maps'
provisional types, why the equality would matter, and its remaining
obligations.

---

## 6. Gaps, uncertainties, and what was deliberately not re-derived

- **`[GenEll]`'s own proofs** (Math. J. Okayama Univ. 52 (2010)) were not
  independently re-derived; its role as an input is confirmed from its
  citations inside IUT IV (and corroborated independently by LANA's own
  dependency structure, §5.1), but its internal correctness is reported here
  as "not found disputed," not "independently verified."
- **IUT IV Propositions 1.1–1.8** and the absolute-anabelian-geometry papers
  underlying `IUT-B5`'s reconstruction algorithms were not read in this
  research pass beyond what IUT II Corollary 4.6 itself states; treat the
  `IUT-B5` row as resting on one citable instance, not a full audit of the
  reconstruction machinery.
- **`SS2018-05.pdf` and `SS2018-08.pdf`**, hosted at
  `kurims.kyoto-u.ac.jp/~motizuki/protectedpdf-2018-05/` and
  `…/protectedpdf-2018-08/`, returned **HTTP 403** on every check performed
  (access-restricted by the host, not a transient fault); their content, to
  the extent it differs from the essay otherwise cited here, was not
  obtained directly. The essay cited throughout §3 above was obtained from
  a Wayback Machine capture (archived 2021-08-03) of
  `math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf`, needed
  because that host failed TLS handshakes directly during this research
  pass; treat this as "as archived." This file's own extraction of the
  archived PDF text did not surface a self-declared date on the essay's
  cover page; a sibling file in this guide separately reports the title
  page reading "July 16, 2018" — noted here as a cross-check this file did
  not itself perform, not as an independent confirmation.
- **`ExplicitEstimates.pdf`, `AlienCopies.pdf`**, and some other secondary
  background papers on the kurims homepage were downloaded but not read in
  depth for this pass; they are not cited above beyond title-level
  awareness and nothing here depends on their content.
- **This guide's own IDs (`IUT-*`) are specific to these two files.** Other
  files in this guide use their own ID schemes (e.g. `sources.md`'s
  `G1`/`C1`/`C2`/`S1`/`L1` for documents, which index different objects than
  this file's `IUT-G1` for a claim). Do not cross-reference IDs across files
  without checking which file defines them.
- **Concurrent editing note.** During this research pass, other files in
  this `guide/` directory were observed being created, renamed, and removed
  by other strands while this work was in progress (for example,
  `06-lean-boundary.md` was briefly absent from the directory listing, and
  a new companion file `06b-lean-vocabulary.md` later appeared). By the end
  of this research pass both `guide/05-critical-transition.md` (full
  Scholze–Stix exchange) and `guide/06-lean-boundary.md` (Lean-repository
  audit) were confirmed present and are now cited by name above and in
  `03-iut-route.md`. If either has since been renamed again, consult the
  directory listing or [00-map.md](00-map.md) at read time.


---

## 7. References (direct URLs; all confirmed reachable during this research pass unless noted)

Primary Mochizuki papers (base: `https://www.kurims.kyoto-u.ac.jp/~motizuki/`):

- `[IUT-I]` Inter-universal Teichmüller Theory I: `Inter-universal%20Teichmuller%20Theory%20I.pdf`
- `[IUT-II]` Inter-universal Teichmüller Theory II: `Inter-universal%20Teichmuller%20Theory%20II.pdf`
- `[IUT-III]` Inter-universal Teichmüller Theory III: `Inter-universal%20Teichmuller%20Theory%20III.pdf`
- `[IUT-IV]` Inter-universal Teichmüller Theory IV: `Inter-universal%20Teichmuller%20Theory%20IV.pdf`
- `[Pano]` Panoramic Overview of Inter-universal Teichmüller Theory: `Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf`
- `[EssLog]` Essential Logical Structure of Inter-universal Teichmüller Theory: `Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf`
- `[GenEll]` Arithmetic Elliptic Curves in General Position: `Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf` (= Math. J. Okayama Univ. 52 (2010), pp. 1–28)
- `[Rpt2018]` Report on Discussions, March 15–20, 2018: `Rpt2018.pdf`
- `[Cmt2018-05]` Comments (July/Sept. 2018): `Cmt2018-05.pdf`
- `[Cmt2018-08]` Comments (2018): `Cmt2018-08.pdf`
- `[LeanForm]` Formalization of IUT (2026-04): `Formalization%20of%20IUT%20(2026-04).pdf`
- Index pages used to locate the above: `papers-english.html`, `research-english.html`

Access-restricted (checked, confirmed `HTTP 403`, not used as a source beyond what other documents quote from them):

- `protectedpdf-2018-05/SS2018-05.pdf`
- `protectedpdf-2018-08/SS2018-08.pdf`

Scholze–Stix essay (obtained via Wayback Machine after direct TLS failure on the origin host):

- `[SS2018]` `https://web.archive.org/web/20210803222351if_/https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf`

External classical reference (not fetched as a PDF; bibliographic identification only):

- `[Vjt]` P. Vojta, *Diophantine approximations and value distribution theory*, Lecture Notes in Mathematics 1239, Springer-Verlag (1987)

Journal publication record (metadata only, used for the pagination note in §0):

- IUT I–IV, *Publications of RIMS* 57(1/2) (2021): `https://doi.org/10.4171/PRIMS/57-1-1`, `-2`, `-3`, `-4`

LANA Lean variant and separate planning document (`IUT-F1`,
`d9465c111ec4073709f67e9fccec7e3eb374a816`):

- `https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91`
- `https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46`
- `https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Plans/Iut4Sec1Spec.md`

Project LANA's independently checked interim report (`IUT-U1`, source
register [D4](sources.md); PDF sections 8.2–8.3, 9.2, and 10.2–10.5):

- `https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf`

---

## 8. Primary-source reading exercises (table-verification specific)

1. Pick any three `ASSERTED_IN_IUT` rows above. Open the cited page in the
   actual PDF and confirm the theorem/definition number and title match
   this table exactly. Report any mismatch as a correction to this file (do
   not silently "fix" your own understanding to match a wrong citation).
2. For `IUT-N4` (Corollary 2.2), find the definition of $\mathrm{Exc}_d$ in IUT IV
   and write down what it depends on (it is not a fixed set independent of
   $K_V$, $d$, $\varepsilon_d$). This checks that "outside a finite exceptional set"
   in this table is not quietly dropping its own dependencies.
3. For `IUT-F1`, open the **Lean source**
   `Iut/Cor312/Statement.lean` and check that `Corollary312Variant`
   is a `Prop`, not a proved theorem. Then open the separate **Markdown
   plan** `Plans/Iut4Sec1Spec.md` and find its proposed
   `Corollary312Input` structure. Do not mistake structure fields
   *written in the plan* for compiled Lean declarations, or either
   artifact for a proof of the published Corollary 3.12.
4. Attempt to fetch `SS2018-05.pdf`/`SS2018-08.pdf` yourself at the URLs in
   §7. If you obtain a result other than `HTTP 403`, that is new
   information not available during this research pass and should be
   recorded as a correction.

---

*Owned file: `guide/04-claim-dependencies.md`. Narrative companion:
`guide/03-iut-route.md`. This file does not claim the abc conjecture is
proved, does not claim IUT III/IV's disputed step is resolved, and does not
claim any Lean project verifies IUT — see `03-iut-route.md` §9 for the
disclaimer this table is built to support.*
