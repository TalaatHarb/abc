# 6a. Lean dependency ledger — re-verified follow-up pass

**Scope.** Narrow follow-up to [06](06-lean-boundary.md) §6.5: restores the
per-edge evidence ledger lost there, re-derived today from a **fresh clone of
the same pinned commit** (not reconstructed from memory). Owns only this
file; `03*`/`04*`/`05*`/`06`/`06b`/`07`/`_sources` were not touched.

**Pin**: `lana-agents/iut` @ `d9465c111ec4073709f67e9fccec7e3eb374a816`
(2026-10-03T19:53:47Z). Re-cloned and re-grepped 2026-10-05 for this file
only; every permalink below was checked against that exact commit today.
Where a fact could not be re-checked this pass, it is marked `UNVERIFIED`
rather than carried over.

## 6a.1 Node ledger: ID, exact hypotheses, conclusion

All permalinks share the prefix `.../lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/`.

| # | Declaration | Exact explicit hypotheses | Conclusion | File : lines |
|---|---|---|---|---|
| 0 | `Corollary312Variant` | none — it *is* the assumption, over `X : Corollary312VariantData AG TG` | $X.\mathrm{qPilot.lhs} \le X.\mathrm{rhsData.rhs}$, i.e. informally $-\lvert\log(q)\rvert \le -\lvert\log(\Theta)\rvert$. Docstring, twice: "no proof of this proposition exists in this repository, and none is claimed." | [`Iut/Cor312/Statement.lean#L78-L91`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91) |
| 1 | `Theorem110Invariants.theorem110` | `cert : Theorem110Certificate inv`, `est : inv.LocalEstimate`, `pnt : PrimeCountingBound`, `h312 : Corollary312Variant X` | $\tfrac16 X.\mathrm{qPilot.logQ} \le (1+20\,X.\mathrm{dmod}/X.\ell)(\mathrm{inv.logDtpd}+\mathrm{inv.logFtpd})+20(\mathrm{inv.eStar}\cdot X.\ell+\mathrm{pnt}.\eta)$ | [`Iut/Implication/Theorem110.lean#L227-L238`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Implication/Theorem110.lean#L227-L238) |
| 2 | `Corollary22Inputs.c2` | `hd : 1 ≤ d`, `ex : ThetaDataExistence P I`, `cheb`, `pnt`, `h312 : ∀ X, P X → Corollary312Variant X`, `x : T.Pt T.tripod`, `hx : x ∈ cbsSet ∩ ptLE d`, `hxe : x ∉ excCore`, `hH : threshold ≤ I.h x` | 3-way conjunction: inequality (C2), $\epsilon_E \le 1$, nonnegativity side-bound | [`Iut/Implication/Corollary22.lean#L383-L394`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Implication/Corollary22.lean#L383-L394) |
| 3a | `cor312Variant_implies_abc`/`_abc'` | `A : T.ProofPackage`, `I : ∀ K d, Corollary22Inputs T K d`, `ex`, `cheb`, `pnt`, `h312 : ∀ X, P X → Corollary312Variant X` | `ABC T` — abstract, for any `T : Genl.HeightTheory` | [`Iut/Implication/Corollary23.lean#L114-L134`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Implication/Corollary23.lean#L114-L134) |
| 3b | `Tripod.abc_of_variant` | single `h312`, universally quantified over `(D, LT, TL, QI)` ⟹ `Corollary312Variant (concreteVariantData D LT TL QI)` | `tripodTheory.StatementII` (ABC on compactly-bounded subsets only) | [`Iut/Tripod/Main.lean#L128-L133`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/Main.lean#L128-L133) |
| 4 | `Tripod.statementI_of_statementII` | `h : tripodTheory.StatementII` — **no other hypothesis** | `tripodTheory.StatementI`, via external `Genl.Curves.statementII_implies_statementI` (noncritical Belyi maps) | [`Iut/Tripod/GeneralPosition.lean#L264-L271`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/GeneralPosition.lean#L264-L271) |
| 5 | `classicalABC_of_variant_of_statementII_imp_I` | `Pi1`, `Tp`, `hII_I : StatementII → StatementI`, `h312` (same shape as node 3b) | `ClassicalABC`. Docstring: `StatementII` alone does **not** suffice (archimedean counterexample sketched inline) | [`Iut/Tripod/ClassicalAbc.lean#L294-L314`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbc.lean#L294-L314) |
| 6 | `classicalABC_of_variant` | `Pi1`, `Tp`, `h312` — `hII_I` pre-filled with node 4 | `ClassicalABC` | [`Iut/Tripod/ClassicalAbcOfVariant.lean#L26-L36`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcOfVariant.lean#L26-L36) |
| 7 | `classicalABC_of_variant_genuine` | `h27 : AffOrbicurve.CanLift27`, `h312` instantiated at `genuinePi1Theory h27` / `temperedTheory (genuineEtaleData h27)` | `ClassicalABC` | [`Iut/Tripod/ClassicalAbcGenuine.lean#L27-L36`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuine.lean#L27-L36) |
| 8 | `Anabelian.canLift27` | none (0-ary) | `AffOrbicurve.CanLift27`, from `OrbicurveCores.U2.canLift27C` (external, over ℂ) + `AffOrbicurve.canLift27_of_complex` (external Lefschetz transport to char. 0) | [`Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L28-L29`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L28-L29) |
| 9 | `classicalABC_of_variant_genuine'` | `h312` only — node 7's `h27` pre-filled with node 8 | `ClassicalABC`, **sole remaining hypothesis is `h312`** | [`Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46) |
| 10 | `ClassicalABC` / `ClassicalABCInt` | — | $\forall\varepsilon>0\,\exists C\,\forall a,b,c{\in}\mathbb N,\ 0{<}a,0{<}b,\gcd(a,b){=}1,a{+}b{=}c \Rightarrow c\le C\cdot\mathrm{rad}(abc)^{1+\varepsilon}$; `ℤ`-form proved equivalent at `classicalABC_iff_int` | [`Iut/Abc/Classical.lean#L34-L48`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Abc/Classical.lean#L34-L48), equivalence [`:146`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Abc/Classical.lean#L146) |

Implicit section `variable`/`universe` context (e.g. `AG`, `TG`, `T`, `K`, `d`)
is declared once near each file's top and is **not** re-traced per node here —
`UNVERIFIED` whether any such section variable smuggles in an extra
assumption beyond what each row states explicitly.

## 6a.2 Axiom and `sorry` evidence (fresh sweep, this pass)

Case-sensitive `grep` for `^\s*(noncomputable\s+)?axiom\s` over every `.lean`
file in the checkout: **zero matches**. (An earlier case-*insensitive* pass
in this session falsely matched the word "Axiom" inside a comment — redone
correctly here.) `grep` for `\bsorry\b`: **exactly 10 matches, all in
`Comparator/Challenge.lean`** (lines 27, 39, 48, 60, 67, 73, 93, 98, 103,
133 — [permalink to the file](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Comparator/Challenge.lean)).
`Comparator/` is a top-level sibling of `Iut/`/`Iut4Sec1/`, not a
subdirectory; a `grep` for the literal string "Comparator" inside every
`Iut/**/*.lean` file returned **zero matches**, i.e. no node in §6a.1 is
reachable from it by any `import`. [`lakefile.toml`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/lakefile.toml#L8-L11)
confirms this is intentional: `warn.sorry = false # "sorry" is load-bearing
in Comparator/Challenge.lean`. Note that `Challenge`/`Solution`
(`srcDir = "Comparator"`) **are** both listed in `defaultTargets`
alongside `Iut`/`Iut4Sec1` (same file, line 4), so a plain `lake build`
does compile this module — it is excluded from the *dependency graph*, not
from the *build*.

## 6a.3 Repo-native self-audit script (new finding)

[`scripts/AuditIutAxioms.lean`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/scripts/AuditIutAxioms.lean)
is a genuine Lean meta-program: it uses `Lean.Util.CollectAxioms` to walk
every public declaration under the `Iut` root and fail if any transitively
depends on an axiom outside `{propext, Quot.sound, Classical.choice}` (the
three standard, Mathlib-wide classical axioms — `sorry` compiles to a
forbidden `sorryAx`, so this would also catch stray `sorry`s under `Iut`).
This is real, well-constructed tooling — **but I could not find it invoked
by any of this repo's 5 CI workflows** (`lean_action_ci.yml` only runs
`leanprover/lean-action@v1`'s default build; `comparator.yml`,
`create-release.yml`, `update.yml`, `verso-blueprint.yml` do not reference
it either). **Whether this script actually runs anywhere in CI, or is a
manual/local-only developer tool, is `UNVERIFIED`.**

## 6a.4 CI evidence for this exact commit (GitHub Checks API)

Queried `api.github.com/repos/lana-agents/iut/commits/d9465c111ec4073709f67e9fccec7e3eb374a816/check-runs`
directly (3 check runs, all `completed`):

| Check run | Conclusion | Duration | Permalink |
|---|---|---|---|
| `build` (from `lean_action_ci.yml`) | **success** | ~29 min | [run 37149551882](https://github.com/lana-agents/iut/actions/runs/37149551882/job/111280309249) |
| `Build blueprint site` (`verso-blueprint.yml`) | **failure** | 24 s | [run 37149551946](https://github.com/lana-agents/iut/actions/runs/37149551946/job/111280309984) |
| `Deploy to GitHub Pages (/verso-blueprint)` | skipped (depends on the failed job above) | — | [run 37149551946](https://github.com/lana-agents/iut/actions/runs/37149551946/job/111280387504) |

The `build` job's single annotation is a generic GitHub runner-image notice
(Ubuntu 26 migration), unrelated to proof content. The failing job builds a
documentation/"blueprint" site (`verso-blueprint`), **not** the Lean
library — I did not fetch its failure log this pass, so the *cause* of that
failure is `UNVERIFIED`, but it is evidently independent of the `build`
job's success (different check suite, 24 s vs 29 min). Net reading: the
actual Lean elaboration of the default build target succeeded for this
commit, per GitHub's own hosted run; docs-site generation did not.

## 6a.5 Seven-plus-one dependency audit (from `lake-manifest.json`, this pin)

Direct (`"inherited": false`) requires only — roles quoted/paraphrased from
[`lakefile.toml`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/lakefile.toml)'s own inline comments:

| Package | Pinned rev | Declared role (lakefile.toml comment) |
|---|---|---|
| `mathlib` (leanprover-community) | `81a5d257c8e4` (tag `v4.32.0`) | foundational library (no role comment; standard dependency) |
| `tate-curves-theta` | `ca6c2279d3ce` | Tate q-parameters/classical theta function (taxis #13/#37); feeds initial Θ-data + Cor312 variant |
| `genl` | `ea2846c877d1` | height formalism + Theorem 2.1 (`Genl.Curves`), feeds node 3a/4; branch `wp-height-theory` |
| `heights` | `721496ca4c15` | complex uniformization, archimedean torsion bound; branch `wp-integrate` |
| `pi1` | `ca7def953193` | étale π₁/orbicurve cores, Lefschetz transport for node 8; branch `wp-core-basechange` |
| `orbicurve-cores` | `61616dcd77fb` | `[CanLift]` Prop. 2.7 over ℂ (node 8's `canLift27C`); branch `wp-u2` |
| `oka` | `75dcdc3faadd` | shared ancestor pin for `belyi` + `orbicurve-cores` |
| `tempered-fundamental-groups` | `2006651f52b7` | tempered π₁ of model orbicurves (taxis #7), feeds `TemperedPi1Theory` |

Full 40-char revs are in [`lake-manifest.json`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/lake-manifest.json).
**I did not clone or grep any of these 7 repositories' own source this
pass** — my axiom/`sorry` sweep (§6a.2) covers only `lana-agents/iut`
itself. Whether `genl`, `orbicurve-cores`, `pi1`, etc. contain their own
axioms/`sorry`/placeholders feeding nodes 3a, 4, or 8 is **`UNVERIFIED`**.

## 6a.6 What remains open after this pass

1. **External dependencies' internal soundness** (§6a.5) — not audited.
2. **`AuditIutAxioms.lean`'s CI execution** (§6a.3) — not found wired into
   any workflow; may be manual-only.
3. **`Build blueprint site` failure cause** (§6a.4) — not investigated;
   appears unrelated to proof-checking but unconfirmed.
4. **Section-variable context per node** (§6a.1) — implicit hypotheses from
   `variable`/`universe` blocks not individually re-traced.
5. **Mathlib's own soundness** at `81a5d257` — assumed via the community's
   standard review process, not independently re-audited here.
6. Everything already flagged as `UNVERIFIED`/`CONDITIONAL_FORMALIZATION` in
   [06](06-lean-boundary.md) (mathematical fidelity of node 0's inequality
   to the published Corollary 3.12, the André/W10 boundary, etc.) stands
   unchanged — this file only adds code-level evidence, it resolves none of
   those caveats.

No axiom declarations and no `sorry` were found inside the audited chain
(nodes 0–10, all under `Iut/`) itself — that specific, narrow claim is
re-confirmed this pass with a fresh grep against the pinned commit.
