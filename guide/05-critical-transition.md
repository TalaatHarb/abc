# 5. The critical transition: IUT III, Theorem 3.11 → Corollary 3.12

## 5.0 Reading map: the contested inference, both sides, what remains open

**Read this section first.** Everything from §5.1 onward is backing detail —
exact quotes, page numbers, and each side's argument in full — for the
claims made here. This file does not adjudicate who is right (no sentence
below is a verdict), does not re-derive the ~150 pages of IUT III
construction that precede Theorem 3.11 (term scope:
[07-dictionary.md](07-dictionary.md); claim graph: [00-map.md](00-map.md)),
and does not audit the Lean formalization effort in depth (see
[06-lean-boundary.md](06-lean-boundary.md) and §5.9; that cross-reference
sits in a shared, actively-edited directory — §5.12, flag 7).
For the later, bounded source-and-inference test of the native-$q$
output membership, see [XI-001](10-xi-001.md).

**The precise contested inference.** Corollary 3.12 ("Log-volume Estimates
for Θ-Pilot Objects," hosted-PDF pp.173–174 — citation note in §5.3) is
derived from Theorem 3.11 ("the main theorem of the present series," p.153)
through a proof labeled (i)–(xii). The dispute concerns the numerical
inference in **Step (xi)** (pp. 181–185), not the final Step (xii), where
the discussion continues with global Frobenioids (pp. 185–186).
Scholze–Stix ("SS," SS report p.9) and Mochizuki (Cmt2018-08 pp.3–4)
agree that Step (xi) turns on identifying
several a priori distinct copies of the real numbers (arising from objects
relative to different "arithmetic holomorphic structures" linked by the
Θ-link), mediated by indeterminacies the paper calls (Ind1), (Ind2), (Ind3),
while tracking a scalar factor of $j^2$.

**Side-by-side** (full citations: §5.4–§5.6):

| | Scholze–Stix | Mochizuki |
| --- | --- | --- |
| The Step (xi) map | Must effectively be linear for the diagram to stay consistent; keeping the $j^2$ scalar then forces an "empty inequality" | The raw $\Theta$-link can be linear; the *hull/indeterminacy-subject* volume comparison is not a scalar isomorphism. Mochizuki calls the generalized "(Lin)" premise "completely false"; "(Lin)" is his label |
| Effect on Theorem 3.11 | Under SS's reading, Thm. 3.11 itself "does not become false, but trivial" | Under SS's reading, Thm. 3.11's multiradial algorithms no longer apply at all — inapplicable, not trivialized |
| Overall verdict | "There is no proof"; not fixable by small modifications | Reflects "a fundamental misunderstanding" of what IUTch's objects are |

**What remains open** (full list: §5.11):
- whether Mochizuki's "(Lin)" label fairly restates what SS's own diagram
  assumes, or recharacterizes it;
- whether SS's quoted Step-(xi) conclusion and IUT III's own boxed
  Corollary 3.12 use the same normalized real quantities, as the
  [conditional algebraic reduction](09-critical-mechanism.md) requires;
- whether the two maps proposed in [Project LANA's report](09-critical-mechanism.md)
  can be shown to agree for a suitable admissible $S$ (its equation
  (9-1)); the report explicitly has no proof of this compatibility;
- no public, dated SS reply specifically to Mochizuki's Sept. 2018
  Cmt2018-08 was located;
- whether SS's quoted Step-(xi) sentence appeared verbatim in an earlier
  edition: its *inequality* appears on hosted PDF p. 184 but the
  surrounding sentence differs; SS's separate p. 16 citation matches the
  hosted Introduction's description of Corollary 3.12 (§5.3).

Evidence labels follow [00-map.md](00-map.md): `STANDARD`,
`ASSERTED_IN_IUT`, `DISPUTED`, `CONDITIONAL_FORMALIZATION`, `UNVERIFIED`.
Source-check labels follow [sources.md](sources.md): `PDF_SECTION`,
`SECONDARY`; `(CHECKED, 2026-10-05)` marks a passage read directly in this
research. PDF page is distinguished from printed page throughout (per
[08-work-queue.md](08-work-queue.md)).

---

## 5.1 Sources consulted, and live access status (checked 2026-10-05)

| # | Document | Self-declared date | URL | Access status (checked 2026-10-05) |
| --- | --- | --- | --- | --- |
| 1 | Scholze & Stix, *Why abc is still a conjecture* | Title page: **"July 16, 2018"** | <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf> | Fetched and extracted in full earlier in this research pass (`CHECKED`). A later re-check hit a transient TLS/connection failure on this one server; since full text was already obtained and is internally consistent (page numbers, footnotes, references all resolve), this is flagged as a possible transient outage, **not** asserted as a permanent access loss |
| 1a | — same document, as hosted by Mochizuki, labelled **"[SS2018-08] August 2018 Report"** | n/a | <https://www.kurims.kyoto-u.ac.jp/~motizuki/protectedpdf-2018-08/SS2018-08.pdf> | **HTTP 403** (access-restricted), confirmed live |
| 1b | — the URL originally linked by Quanta Magazine in Sept. 2018 for the same document | n/a | `http://www.kurims.kyoto-u.ac.jp/~motizuki/SS2018-08.pdf` (no `protectedpdf-` folder) | **HTTP 404** today. Confirmed: this exact URL is quoted live in Peter Woit's Sept. 2018 blog post (§5.9 below) as "[their write-up]... is now available here", so the file was freely reachable at this path in 2018 and has since been moved/restricted. The Bonn mirror (row 1) is the only copy this research could read |
| 1c | Earlier draft, "[SS2018-05] May 2018 Report" | n/a | <https://www.kurims.kyoto-u.ac.jp/~motizuki/protectedpdf-2018-05/SS2018-05.pdf> | **HTTP 403**. Not independently obtained; its content is known here only through Mochizuki's quotations of it in Cmt2018-05 |
| 2 | Mochizuki, *Report on Discussions, held during the period March 15–20, 2018, concerning Inter-universal Teichmüller Theory (IUTch)* ("Rpt2018"), with the cooperation of Yuichiro Hoshi | Title page: **"February 2019"**; hub page says "updated on 2019-02-01" | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Rpt2018.pdf> | **HTTP 200**, fetched and extracted in full (45 pp.) (`CHECKED`) |
| 3 | Mochizuki, *Comments on the Manuscript by Scholze–Stix...* ("Cmt2018-05") | Title page: **"July 2018"** (PDF container metadata separately shows Sept. 2018 — a minor, unresolved discrepancy, not pursued further here) | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-05.pdf> | **HTTP 200**, fetched and extracted in full (`CHECKED`) |
| 4 | Mochizuki, *Comments on the Manuscript (2018-08 version) by Scholze–Stix...* ("Cmt2018-08") | Title page: **"September 2018"**; opens by saying it supplements Cmt2018-05 and responds to "the August 2018 version of the manuscript [SS2018-08]" | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf> | **HTTP 200**, fetched and extracted in full (`CHECKED`) |
| 5 | Mochizuki's hub page for the whole exchange | n/a | <https://www.kurims.kyoto-u.ac.jp/~motizuki/IUTch-discussions-2018-03.html> | **HTTP 200** (redirects `http→https`), fetched in full (`CHECKED`) |
| 6 | Mochizuki, *Inter-universal Teichmüller Theory III: Canonical Splittings of the Log-theta-lattice* — currently hosted preprint PDF | Publications list marks this file **"NEW!! (2020-05-18)"** | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf> | **HTTP 200**, fetched and extracted in full (199 pp. in this extraction) (`CHECKED`) |
| 7 | IUT I–IV, journal version | Special issue dated **2021-03-05** | PRIMS 57 (1/2), DOIs `10.4171/PRIMS/57-1-1`…`-4`, pp. 3–207, 209–401, 403–626, 627–723 | Issue page and bibliographic listing resolved; DOI `-3` individually resolved with matching abstract in earlier research. `-1`,`-2`,`-4` confirmed via the publisher's own issue listing, not each individually re-fetched article-by-article in this pass |
| 8 | Klarreich, "Titans of Mathematics Clash Over Epic Proof of ABC Conjecture," *Quanta Magazine* | **2018-09-20** (date in URL slug, confirmed) | <https://www.quantamagazine.org/titans-of-mathematics-clash-over-epic-proof-of-abc-conjecture-20180920/> | **HTTP 200** (`CHECKED`) |
| 9 | Woit, "Scholze and Stix on the Mochizuki Proof," *Not Even Wrong* | Undated in the fetched text; contemporaneous with, and links to, the Quanta piece (so ≈ Sept. 2018) | <https://www.math.columbia.edu/~woit/wordpress/?p=10560> | **HTTP 200** (`CHECKED`) |
| 10 | Woit, "Million Dollar Prize for Scholze and Stix," *Not Even Wrong* | ≈ **July 2023** (references a Tokyo news conference "today" and links a Nikkei piece from that period) | <https://www.math.columbia.edu/~woit/wordpress/?p=13573> | **HTTP 200** (`CHECKED`) |
| 11 | Castelvecchi, "Maths proof that rocked number theory will be published," *Nature* 580, p.177 | **2020-04-09**; reports a press conference **2020-04-03** | <https://www.nature.com/articles/d41586-020-00998-2>, DOI `10.1038/d41586-020-00998-2` | The canonical URL returns **HTTP 406** to this session's text-fetching tool specifically (a header/content-negotiation issue, since a plain HEAD request to the same URL succeeds with HTTP 200); full text obtained instead from a Nature-hosted PDF mirror and extracted (`CHECKED`) |
| 12 | New Scientist, "Decade-long struggle over maths proof could be decided by \$1m prize" | **≈ July 2023** | <https://www.newscientist.com/article/2381521-decade-long-struggle-over-maths-proof-could-be-decided-by-1m-prize/> | **HTTP 200** (`CHECKED`) |
| 13 | New Scientist, article 2424640 (Joshi/Scholze/Mochizuki/Fesenko) | **2024-03-28** | newscientist.com/article/2424640 | **HTTP 200** (`CHECKED` earlier in this research) |
| 14 | New Scientist, article 2522687 (LANA "stuck point," Topaz, Buzzard) | **2026-04-10** (print issue 2026-04-18) | newscientist.com/article/2522687 | **HTTP 200** (`CHECKED` earlier in this research) |
| 15 | ZEN University / IUGC press releases on the IUT Innovator/Challenger Prizes | **2023-07-07** (prize creation); first award reported ≈ April 2024 | zen.ac.jp/news/0ul6zqed9-0; zen.ac.jp/news/d-5ye560_l | **HTTP 200** (`CHECKED`) |
| 16 | LANA (`lana-agents/iut`) GitHub README | n/a | raw.githubusercontent.com/lana-agents/iut/... | **HTTP 200**. Full depth already audited in [06-lean-boundary.md](06-lean-boundary.md); used here only for the one-paragraph cross-reference in §5.9 |
| 17 | Project LANA, *Interim Report on IUT Theory* | July 2026 (pinned PDF at `b8e4636`) | [Report PDF](https://github.com/katobungen/LANA_report_202607/blob/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/LANA_report_202607.pdf) and [ZEN University announcement](https://zen.ac.jp/news/zmcpostevent0717e) | **HTTP 200**. PDF pp. 40–43 and 45–49 read directly (`CHECKED`, 2026-10-05); the team's technical description and explicit unsolved compatibility (9-1) are summarized in [09](09-critical-mechanism.md) |

No claim below relies on a source this research could not actually open. Where
a source could not be opened (rows 1a, 1b, 1c), that fact is reported, not
papered over.

---

## 5.2 Established-fact timeline

These are dated, source-confirmed events, not characterizations of who is
right. Dated public commentary (who said what) is collected in §5.9, not
repeated here.

| Date | Event | Source |
| --- | --- | --- |
| 2012 | Mochizuki posts four IUT preprints online | Nature 2020 (row 11); Mochizuki's publications page |
| 2018-03-15 to 2018-03-19 | Scholze and Stix spend a week at RIMS, Kyoto, discussing the proof with Mochizuki and Hoshi | Rpt2018 title page (p.1); SS report p.1 |
| 2018-05 | SS circulate a first manuscript ("[SS2018-05]") | Hub page (row 5); Cmt2018-05 |
| 2018-07-16 (self-dated) / called "August 2018" by Mochizuki's site | SS circulate/finalize the manuscript still hosted today ("[SS2018-08]"), *Why abc is still a conjecture* | SS report title page; Cmt2018-08 p.1 — **the July/August discrepancy is unresolved; see §5.12** |
| 2018-07 and 2018-09 | Mochizuki posts Cmt2018-05 and Cmt2018-08, responding point-by-point | Title pages of each document |
| 2018-09 | Quanta (Klarreich) publishes an account with direct quotes from both sides; Woit's blog independently summarizes the dispute | Rows 8–9 |
| 2019-02 (self-dated) | Mochizuki finalizes/updates Rpt2018 | Rpt2018 title page; hub page |
| 2020-04-03 | Kyoto press conference announces PRIMS's acceptance of IUT I–IV, given by Kashiwara and Tamagawa (not Mochizuki) | Nature 2020, p.1 |
| 2020-04-09 | Nature publishes Castelvecchi's report, including that **Mochizuki is PRIMS's chief editor** | Row 11 |
| 2020-05-18 | The IUT III preprint PDF used throughout this file is last marked "NEW!!" on Mochizuki's publications list — after the 2018 SS exchange, hence the pagination gap (§5.12) | Mochizuki's publications-list page (row 6) |
| 2021-03-05 | IUT I–IV appear in print, PRIMS vol. 57 no. 1/2 | DOIs (row 7) |
| 2022–2024 | A Mochizuki-coauthored extension paper appears (*Kodai Math. J.* 45); IUGC (ZEN University, est. 2023-06-06) announces IUT-related prizes on 2023-07-07, including a USD 1,000,000 award for a published disproof; a separate, smaller prize is first awarded ≈2024-04 for the 2022 paper — detail in §5.9 | Rows 10, 12, 15 |
| 2023–2026 | Two separate Lean-formalization efforts proceed (Mochizuki's own; LANA, Kato/Topaz); LANA reports in 2026-04 reaching a point its lead calls "closely related" to SS's objection | Row 14; [06-lean-boundary.md](06-lean-boundary.md) |

---

## 5.3 What Theorem 3.11 and Corollary 3.12 assert, and the exact relation between them `ASSERTED_IN_IUT`

**Citation and edition note.** Scholze–Stix cite "[IUTT-3, page 16,
Corollary 3.12]" (SS p. 4). Page 16 of the **currently hosted** IUT III
contains the Introduction's description of Corollary 3.12 and its
quantities; the *formal, boxed statement* is at PDF pp. 173–174. Thus
their page-16 citation matches the current Introduction and **does not
by itself show a version change**, contrary to an earlier reading of
this file. SS also quote a Step-(xi) sentence (SS p. 9) whose numerical
inequality agrees with the current Step (xi-f), PDF p. 184, but whose
surrounding prose is not verbatim there. Whether this reflects a
different revision or a paraphrase needs the exact 2018 text; it
cannot be decided from the page-16 citation. Page numbers below refer
to the currently hosted PDF listed in source row 6.

**Theorem 3.11** ("Multiradial Algorithms via LGP-Monoids/Frobenioids,"
IUT III p.153) is introduced by the paper's own text, one sentence before its
statement, as *"the main theorem of the present series of papers"* (p.153).
Fixing a collection of Hodge theaters arising from a log-theta-lattice, part
(i) is labelled "Multiradial Representation." Per the paper's own summary in
Remark 3.11.1(i) (pp.159–160), the theorem gives an algorithm for describing
the LGP-monoids of one node of the log-theta-lattice in terms of the
"*a priori* alien arithmetic holomorphic structure" of a different,
Θ-link-linked node — up to three explicitly named indeterminacies,
**(Ind1), (Ind2), (Ind3)**.

**Corollary 3.12** ("Log-volume Estimates for Θ-Pilot Objects," IUT III
pp.173–174) is introduced, one sentence before its statement, as

> "a relatively concrete consequence of the somewhat abstract content of
> Theorem 3.11" (p.173).

Its statement opens "Suppose that we are in the situation of Theorem 3.11"
(p.173) — i.e. it does not stand on its own; it shares Theorem 3.11's
hypotheses and directly consumes Theorem 3.11's "multiradial representation"
as an ingredient. Its headline conclusion, quoted exactly from the PDF
(p.174):

> "$C_\Theta \ge -1$ for any real number $C_\Theta \in \mathbb{R}$ such that
> $-|\log(\Theta)| \le C_\Theta \cdot |\log(q)|$."

**The exact relation between the two** (per IUT III's own proof structure,
not a paraphrase): Corollary 3.12's proof is a named multi-step argument
(Steps (i) through (xii), per the paper's own labels, spanning
pp. 174–186 of the hosted PDF). The quantities "$-|\log(\Theta)|$" and
"$-|\log(q)|$" are **procession-normalized mono-analytic log-volumes** of
specific regions ("holomorphic hulls" of pilot-object images) defined using
Theorem 3.11's apparatus (p.173). The multiradial algorithm from Theorem 3.11
is explicitly invoked again inside this proof — SS's own report cites this
as "the multiradial algorithm [IUTT-3, Theorem 3.11]" being applied "so... it
is argued in [IUTT-3, Corollary 3.12]" (SS report p.9) — and the disputed
derivation step is specifically **Step (xi)**, the disputed step, where the
abstract multiradial comparison is converted into the numerical log-volume
inequality above. Both SS and Mochizuki agree on this locus: SS's report
says the issue arises "towards the end of Step (xi) in the proof of [IUTT-3,
Corollary 3.12]" (SS report p.9), and Mochizuki's replies repeatedly cite the
same Step (xi) (Cmt2018-08 (C12)–(C14), pp.3–4).

**A more nuanced point, worth stating precisely rather than compressing into
"Cor 3.12 follows from Thm 3.11":** SS's own footnote to their critique (SS
report, p.9, footnote 12) states that under the identification they say
consistency forces,

> "the critical [IUTT-3, Theorem 3.11] does not become false, but trivial."

That is, SS's objection is not confined to "the step from 3.11 to 3.12 has a
gap"; part of their claim is that, *under a specific reading of how objects
must be identified*, Theorem 3.11 itself would carry no content. Mochizuki's
response is not that this reading is a valid simplification that happens to
trivialize a true theorem; it is that the reading is illegitimate for 3.11 in
the first place — once SS's simplification is made, "one can no longer apply
the multiradial algorithms of [IUTchIII], Theorem 3.11" at all (Cmt2018-08
p.4, comment (C13)). So the disagreement is one level more structural than a
simple missing-step claim: **the two sides disagree about what operation
(identifying copies of the real numbers that arise relative to different
arithmetic holomorphic structures) is legitimate to perform at all in Step
(xi), and therefore about whether SS's simplified setting is a faithful
reduction of the real argument or a different, inapplicable one.** §5.6–5.7
develop this precisely.

---

## 5.4 The Scholze–Stix objection, in their own terms `DISPUTED`

Source: SS report (row 1), §2.2, "Proof of [IUTT-3, Corollary 3.12]," pp.9–10,
unless noted.

1. SS set up two Hodge theaters $HT_1, HT_2$ linked by a Θ-link, under which
   "the abstract Θ-pilot object from $HT_1$ is mapped to the abstract
   $q$-pilot object belonging to $HT_2$" (p.9).
2. They identify that the derivation of the headline inequality requires
   comparing **several distinct copies of 1-dimensional ordered
   $\mathbb{R}$-vector spaces** that arise in the construction — they list
   three families: (1) spaces where "abstract" pilot elements live,
   (2) spaces where "concrete" pilot elements live (one per index
   $j=1,\dots,\ell^\star$ on the Θ-side, one on the $q$-side), (3) two
   further copies of the standard reals $\mathbb{R}^\Theta, \mathbb{R}^q$
   where "arithmetic degrees" live (p.9). They draw this out as an explicit
   diagram (p.9–10) of maps between these copies.
3. They state that reaching the headline inequality additionally requires
   rescaling by a factor of **$j^2$** for each index $j$ (p.4, their
   equation (1.5); p.9, "it was necessary to change the isomorphism
   $\mathbb{R}\cong\mathbb{R}^{\odot,\Theta}$ by the scalar $j^2$"), in order
   for the abstract Θ-pilot object to "encode the arithmetic degree of the
   ($j$-th) concrete Θ-pilot object" (p.9).
4. Their central claim: if one insists on **consistently** identifying all
   the copies of $\mathbb{R}$ in the diagram using the natural isomorphisms
   they describe, introducing the $j^2$ scalars "strictly speaking leads to
   inconsistencies, i.e. monodromy" (p.10) — and the only way to keep the
   diagram consistent is to **omit** the $j^2$ scalars, "which leads to an
   empty inequality" (p.10, their emphasis).
5. They report that, in the March 2018 discussions, Mochizuki responded that
   the diagram commutes only "up to the 'blurring' given by certain
   indeterminacies"; SS's own gloss on this response is: "it seems to us
   that this statement means that the blurring must be by a factor of at
   least $O(\ell^2)$ rendering the inequality thus obtained useless" (p.10).
6. As noted in §5.3, their footnote 12 (p.9) separately records that, under
   the "identifying identical copies of objects along the identity"
   simplification, Theorem 3.11 itself "does not become false, but trivial."
7. SS's own overall verdict, stated on p.1, before any of the technical
   argument: "We, the authors of this note, came to the conclusion that
   there is no proof," calling the problem "so severe that in our opinion
   small modifications will not rescue the proof strategy" (p.1). They
   explicitly flag that they "supplement our report by mentioning dissenting
   views from Prof. Mochizuki and Prof. Hoshi" (p.1).

All of the above is SS's own claim, in SS's own terms, as published by SS.
It is reported here as a claim, not re-derived or checked line-by-line
against the full IUT III apparatus in this file (see §5.10 for what that
independent check would require).

---

## 5.5 Mochizuki's counter-interpretation, in his own terms `DISPUTED`

Source: primarily Cmt2018-08 (row 4), comments (C12)–(C14), pp.3–4; Rpt2018
(row 2), §§10–12 and the compact summary (Smm), p.2.

1. Mochizuki frames the dispute as turning on "the issue of distinguishing
   the *abstract category-theoretic* versions of pilot objects... from
   their *concrete (multiradial!) representations*," which he calls "one of
   the most central aspects of IUTch," citing Theorem 3.11 and the proof of
   Corollary 3.12 by name (Cmt2018-08, (C12), p.3).
2. He states that SS's simplifications (identifying objects "along the
   identity") correspond to what he calls the **"id-version"** of the
   construction, discussed at length in Rpt2018 §10, and that once this
   simplification is made, "one can no longer apply the multiradial
   algorithms of [IUTchIII], Theorem 3.11" (Cmt2018-08, (C13), p.4) — i.e.
   in his account the simplified setting SS analyze is not a faithful,
   trivialized restriction of the real argument, but a setting in which the
   real argument's tools no longer apply at all.
3. He isolates what he presents as SS's governing assumption and labels it
   **(Lin)** — his own term, not SS's: any two such copies of $\mathbb{R}$
   are related simply by multiplication by some scalar (Cmt2018-08, (C14),
   p.4).
4. His response: assumption (Lin) "is completely false" — where
   indeterminacies are involved, the relationship between log-volumes is
   geometry-dependent and **"highly non-linear"** (Cmt2018-08, (C14), p.4),
   illustrated by the worked example (LVEx) in §5.8.
5. His short, compact version of this whole disagreement (Rpt2018, (Smm),
   p.2) models the structure of the argument as: positive reals $A,B$ with
   $-2B=-A$ (standing for the Θ-link), a theorem $-2B\le -2A+1$ (standing
   for the multiradial representation of Theorem 3.11), jointly implying
   $A\le 1$ (standing for Corollary 3.12). He states that SS's
   misunderstanding, on this model, amounts to assuming "the theory remains
   essentially unaffected even if one takes $A=B$" — which forces $A=B=0$,
   a contradiction — and states explicitly that "the essential content...
   of IUTch fail(s) to hold under the assumption 'A=B'," so the
   contradiction "does not imply the existence of any flaws whatsoever in
   IUTch" (Rpt2018, p.2).
6. He asserts, as a matter of process, that "IUTch has been checked,
   verified, read and reread, and orally exposed in detail in seminars in
   its entirety countless times" since 2012 by a group of mathematicians,
   citing Fesenko's estimate ("verified at least 30 times") (Rpt2018, (Vrf1),
   pp.42–43), and that there is "no substantive mathematical reason
   whatsoever to suspect the existence of any oversights" (Rpt2018, (Vrf2),
   p.43).
7. His own diagnosis: the dispute may arise because the mathematics SS
   understand by "IUTch" differs substantially from the mathematics he and
   colleagues understand by that name (Rpt2018, (DfMth), p.44).

All of the above is Mochizuki's own claim, in his own terms, as published by
him. Like §5.4, it is reported, not independently re-derived here.

---

## 5.6 Side-by-side table

| Point at issue | Scholze–Stix (SS report, §2.2 unless noted) | Mochizuki (Cmt2018-08 / Rpt2018 unless noted) |
| --- | --- | --- |
| Where is the disputed step located? | "Towards the end of Step (xi) in the proof of [IUTT-3, Corollary 3.12]" (p.9) | Same locus, repeatedly cited: Step (xi) (Cmt2018-08 (C12)–(C14), pp.3–4) |
| What operation is at stake? | Consistently identifying several copies of $\mathbb{R}$ (abstract pilot, concrete pilot ×$\ell^\star$, arithmetic-degree copies) across the Θ-link (p.9) | Same operation, but described as subject to indeterminacies (Ind1)–(Ind3) belonging to the multiradial representation of Thm. 3.11 (Cmt2018-08 (C14), p.4) |
| What is the relationship between these copies, in each side's account? | A "simple, straightforward linear relationship... multiplication by some positive real number" is implicitly required for a meaningful inequality (this phrase, "(Lin)," is Mochizuki's label for SS's assumption, not SS's own words) | Labels the above assumption "(Lin)" and states it is "completely false"; the real relationship (once indeterminacies are accounted for) is "highly non-linear" (Cmt2018-08 (C14), p.4) |
| What happens to the disputed $j^2$ scalar? | Consistent identification forces it to be dropped, "which leads to an empty inequality" (p.10) | Does not address the $j^2$ computation on SS's own terms; reframes the whole computation as illegitimate once SS's "id-version" identifications are made (Cmt2018-08 (C13), p.4) |
| What did Mochizuki say in the March 2018 discussions themselves, per SS? | He said the diagram commutes "up to the 'blurring' given by certain indeterminacies"; SS gloss this as implying a useless bound, "at least $O(\ell^2)$" (p.10) | Not separately re-stated in these terms in the later written comments; the later comments instead refer to Rpt2018's own worked analogy (LVEx) as the general explanation |
| Does the objection bear only on Cor. 3.12, or on Thm. 3.11 too? | Footnote 12 (p.9): under their reading, "the critical [IUTT-3, Theorem 3.11] does not become false, but trivial" | (C13), p.4: under SS's simplification, "one can no longer apply the multiradial algorithms of [IUTchIII], Theorem 3.11" at all — i.e., not a trivialization of the real theorem, but inapplicability of it |
| What does each side conclude about the proof overall? | "We, the authors of this note, came to the conclusion that there is no proof" (p.1); "a problem so severe that... small modifications will not rescue the proof strategy" (p.1) | The objection reflects "a fundamental misunderstanding" (Cmt2018-08 (C11)–(C12), p.3) stemming from SS using a different, non-equivalent mathematical setting than the one IUTch actually defines (Rpt2018 (DfMth), p.44) |
| What does each side say about the state of outside verification? | Not a topic of the SS report itself, which is a mathematical note, not a survey of community opinion | Cites the testimony of "colleagues involved" and Fesenko's "verified at least 30 times" estimate as evidence against the existence of a flaw (Rpt2018 (Vrf1)–(Vrf2), pp.42–43) |

---

## 5.7 Locus of unresolved disagreement (neutral synthesis)

This section states, as precisely as the two primary documents allow, where
the live disagreement sits — without deciding it.

Both sides agree on:
- the location (Step (xi) of the proof of Corollary 3.12);
- that the step requires comparing several a priori distinct copies of the
  real numbers, arising from objects relative to different "arithmetic
  holomorphic structures" linked by the Θ-link;
- that the comparison is mediated by indeterminacies the paper calls
  (Ind1), (Ind2), (Ind3) and that these indeterminacies are not optional —
  SS's own report acknowledges they are present ("up to certain
  indeterminacies, e.g. (Ind1,2,3) (without which the conclusion would be
  obviously false)", SS report p.9).

The documents diverge on:
- **whether the specific comparison performed in Step (xi) is linear or
  non-linear in the relevant sense**, and consequently whether the $j^2$
  scalar can be consistently retained;
- **what follows if one insists on the "consistent identification" reading
  SS use**: SS read it as revealing an empty/useless inequality in Cor. 3.12
  (and triviality in Thm. 3.11 under the same reading); Mochizuki reads the
  insistence on that reading itself as the error, because, in his account,
  it is not a special/simplified case of the multiradial representation but
  a different construction to which Theorem 3.11 does not apply;
- **whether the disagreement is a checkable local computation or a
  disagreement about which mathematical object the words denote**:
  Mochizuki's own diagnosis (Rpt2018 (DfMth), p.44) explicitly frames it as
  the latter — that SS's "IUTch" and his "IUTch" denote different
  mathematical content — which, if accurate, would mean the dispute cannot
  be settled merely by checking arithmetic inside a single shared
  formalism, because the two sides would not (on this account) agree on
  what is being formalized. SS's report does not address this particular
  framing; it presents its criticism purely as an internal computation
  within IUT III's own stated objects and definitions.

Neither primary document, read on its own, resolves this. Each gives a
self-consistent account of why the other side is mistaken. Readers wanting
to go further than this file should inspect the
[six-node/paper-side object ledger](09b-object-identity-ledger.md),
attempt the checklist in §5.10, and note the asymmetry in
available independent (non-participant)
secondary commentary recorded in §5.9 and flagged again in §5.12.

---

## 5.8 A worked schematic analogy

> **⚠ This is explicitly NOT part of IUT.** It is Mochizuki's own
> illustrative toy model, offered by him as an elementary analogy for one
> qualitative phenomenon (indeterminacies producing a non-linear relation
> between log-volumes), not as a proof, derivation, or substitute for any
> part of IUT III. Mochizuki himself appends an explicit limiting caveat,
> quoted at the end of this section, that the analogy's internal
> consistency is special to the specific numbers/regions chosen and does
> **not** generalize to arbitrary regions and constants. Source: Rpt2018
> (row 2), item **(LVEx)**, pp.24–26 (preceded by (LbLV), p.23, and (MlLV),
> p.24). All arithmetic below was independently recomputed for this file by
> direct area calculation; the parameter experiment below is our own
> calculation on the illustrative model, not a claim in the source.

**The construction, exactly as given.** Let $V=\mathbb{R}^2$ and let
$\sigma: V\to V$ be $\sigma(x,y)=(-x,y)$, an order-2 automorphism. Let $W$ be
the stack-theoretic quotient of $V$ by the group $G=\{1,\sigma\}$, giving a
degree-2 finite étale map of orbispaces $\varphi: V\to W$. For positive
reals $a,b$, define two regions of $V$:

$$
R_{a,b} = \{(x,y): |x|\le 1,\ 0\le |y|\le a\}\ \cup\ \{(x,y): 0\le x\le 1,\ a\le|y|\le a+b\},
$$
$$
S_{a,b} = R_{a,b}\cup\sigma(R_{a,b}).
$$

$R_{a,b}$ is an inner band of width $2$ and total height $2a$, plus two
outer strips of width $1$ and height $b$ each; $S_{a,b}$ reflects (doubles)
only the asymmetric outer strips. Writing $\mu_{\log}$ for the natural log
of ordinary Euclidean area:

$$
\mu_{\log}(S_{a,b}) = \log(4a+4b) \;>\; \mu_{\log}(R_{a,b}) = \log(4a+2b).
$$

(Independently checked: area of $R_{a,b}$ is
$2\cdot(2a) + 1\cdot(2b) = 4a+2b$; $S_{a,b}$ doubles only the outer band to
full width, giving $4a+2(2b)=4a+4b$. The source's own stated inequality is
confirmed exactly.)

Since $\sigma(S_{a,b})=S_{a,b}$, $S_{a,b}$ is "defined over $W$" (label $W$);
since $\sigma(R_{a,b})\ne R_{a,b}$, $R_{a,b}$ is only "defined over $V$"
(label $V$) — i.e. $R_{a,b}$ is pictured as an "incomplete portion" of the
$G$-symmetric object whose log-volume is read off from $S_{a,b}$.

Now pick $\lambda\in\mathbb{R}$ with
$\mu_{\log}(S_{a,b}) > 0 > \lambda > \mu_{\log}(R_{a,b})$
(the source states that such values exist but gives **no numerical
triple**; our independently chosen $a=0.1,b=0.2$ gives
$\mu_{\log}(R_{a,b})=\log(0.8)\approx-0.223$, so any
$\lambda\in(\log(0.8),0)$ works, with
$\mu_{\log}(S_{a,b})=\log(1.2)\approx0.182>0$).
This makes $\rho:=\mu_{\log}(R_{a,b})/\lambda > 1$ well-defined, and $\lambda$
is read as the log-volume of a region $R_\lambda$ "defined over $W$."

**The correspondence table, exactly as the source states it** (Rpt2018 p.25):

| Toy-model object | Corresponds to (per Mochizuki) |
| --- | --- |
| $R_{a,b}$ | the Θ-pilot object, relative to the Θ-holomorphic structure |
| $S_{a,b}$ | the holomorphic hull, relative to the $q$-holomorphic structure, of the multiradial representation of the Θ-pilot, with "indeterminacies" given by the action of $G$ |
| $R_\lambda$ | the $q$-pilot object |
| the assignment $\mu_{\log}(R_{a,b})_V \mapsto \lambda_W$ | an $\mathbb{R}$-linear gluing isomorphism $\mathbb{R}_V\xrightarrow{\sim}\mathbb{R}_W$ (dividing by $\rho$), corresponding to the Θ-link |
| the chain $\mu_{\log}(S_{a,b})_W > \mu_{\log}(R_{a,b})_V \mapsto \lambda_W$ | the chain of log-volume relationships in the argument of Step (xi) of the proof of Corollary 3.12 |

**The point Mochizuki draws from it:**
$\mu_{\log}(S_{a,b})_W > \mu_{\log}(R_{a,b})_V$ follows from the geometry of
$R_{a,b}\subseteq S_{a,b}$ and the stack-quotient construction of $W$ — not
from the linear gluing map — yet stays "entirely logically consistent" with
that gluing (Rpt2018, pp.25–26). The model is built so a non-linear,
geometry-dependent fact and a linear isomorphism coexist without
contradiction, illustrating how assuming only linearity (as in (Lin)) could
wrongly predict a contradiction or a vacuous inequality.

**Mochizuki's own explicit limit on the analogy:** he states directly that
this consistency property does **not** hold "by arbitrary regions of $W$,
$V$ and an arbitrary real number $\lambda$" (Rpt2018, p.26) — the example's
internal consistency depends on the specific geometry and numeric
inequalities chosen; it is one existence example of a qualitative phenomenon
(non-linearity compatible with logical consistency), not a general theorem,
and not a model of IUT III's actual objects beyond that one point. His own
closing line calls Step (xi) "precisely the sort of situation" illustrated
here (Rpt2018, p.26) — an analogy claim, not an identity claim.

### 5.8.1 Exact parameter test (our calculation, not an IUT result)

The strict sign pattern used in (LVEx) is **not automatic** for
$a,b>0$. Set $r=4a+2b$ and $s=4a+4b$. Since $r<s$,
there exists a $\lambda$ with
$\log s>0>\lambda>\log r$ **if and only if**

$$
r<1<s
\quad\Longleftrightarrow\quad
0<a<\tfrac14,\qquad
\frac{1-4a}{4}<b<\frac{1-4a}{2}.
$$

For every such pair, the permitted values are exactly
$\lambda\in(\log r,0)$, and
$\rho=\log r/\lambda>1$. The equivalence follows by taking
exponentials, then solving $4a+2b<1<4a+4b$ for $b$.
It is an **existence criterion for this example**, not a theorem
about IUT's admissible indeterminacies.

| $(a,b)$ | $(r,s)$ | $\lambda=-1/10$? | What the calculation tests |
| --- | --- | --- | --- |
| $(1/10,1/5)$ | $(4/5,6/5)$ | Yes | Corrected numerical example above |
| $(1/20,3/10)$ | $(4/5,7/5)$ | Yes | Same $\log r$ and same gluing scale $\lambda/\log r$, **different** hull log-volume |
| $(3/20,1/10)$ | $(4/5,1)$ | No | Boundary $\log s=0$ breaks the strict sign pattern |
| $(1/10,7/20)$ | $(11/10,9/5)$ | No | $\log r>0$, so no allowed negative $\lambda$ |

Indeed, the hull's increase is

$$
\log s-\log r
=\log\left(1+\frac{2b}{4a+2b}\right),
\qquad 0<\log s-\log r<\log 2
\quad(a,b>0).
$$

The two admissible rows have the **same input log-area and the same
linear gluing map** but different outputs after symmetrization.
Therefore no rule depending *only* on the input log-area and this
chosen gluing map determines the hull's log-area: the shape parameter
$b$ matters. This is a concrete, falsifiable distinction between a
linear transport and a geometry-dependent set operation. The gain is
bounded by $\log 2$ in **this toy model**, while $\rho$ can be made
arbitrarily large by letting $\lambda\uparrow0$ for fixed $a,b$ in the
allowed region. Neither observation supplies a $j^2$ estimate,
an IUT comparison, or a justification for the native $q$-pilot
membership in Step (xi).

A second, much more compact version of the same rhetorical move appears
earlier in the same report as **(Smm)** (Rpt2018, p.2, quoted in §5.5, point
5, above): positive reals $A, B$ with $-2B=-A$, a theorem $-2B\le-2A+1$, giving
$A\le1$; Mochizuki states SS's implicit error, on this model, is equivalent
to assuming the theory is unaffected by setting $A=B$ (which is false on his
account and forces a contradiction $A=B=0$ that he says reflects the
invalidity of that assumption, not a flaw). This is an even smaller,
purely-algebraic schematic and is likewise explicitly marked by Mochizuki as
a "very rough" summary (Rpt2018, p.2), not a derivation.

---

## 5.9 Subsequent status: publication versus community acceptance

**Established, dated facts** (not characterizations):

- IUT I–IV were accepted for publication in PRIMS, announced at a Kyoto
  press conference on **2020-04-03** by Masaki Kashiwara and Akio Tamagawa
  (Mochizuki did not attend) (Nature 2020, p.1).
- **Mochizuki is PRIMS's chief editor**; PRIMS is published by RIMS, Kyoto
  University, where he works (Nature 2020, p.1). A secondary source (New
  Scientist, row 12) paraphrases Nature as reporting he had no personal
  role in the editorial decision on his own paper; this file could not
  independently confirm that specific sentence in the Nature text it
  obtained, so it is reported as New Scientist's characterization, not as
  independently verified primary text.
- IUT I–IV were published in print in PRIMS **2021-03-05** (special issue
  57(1/2)) — roughly eleven months after the acceptance announcement. Some
  secondary sources (e.g. New Scientist, row 12) describe the paper as
  "published in 2020," conflating the acceptance announcement with the
  later print date; this file keeps the two dates distinct.
- A 2022 *Kodai Math. J.* paper by Mochizuki and four coauthors applies IUT
  to obtain explicit abc-type inequalities and a conditional new proof of
  Fermat's Last Theorem; it is an application/extension, not an
  independent proof addressing the Scholze–Stix objection. It was later
  recognized by an IUGC prize (≈2024) — IUGC being an institution
  dedicated to promoting IUT theory, not an independent mathematical
  society (ZEN press release, row 15).
- A separately announced USD 1,000,000 "IUT Challenger Prize" requires a
  peer-reviewed paper meeting stated bibliographic eligibility rules (Woit,
  row 10) that an unpublished note such as the Scholze–Stix report does not
  on its face meet, independent of its mathematical content.
- Two distinct Lean formalization efforts exist: LANA (Kato/Topaz, ZEN
  Mathematics Center, started late 2023, announced 2026-03-31) and a
  separate effort run by Mochizuki himself, which per New Scientist (row
  14) is explicitly not aimed at independent verification. **Full
  technical detail on either Lean effort is out of scope for this file —
  see [06-lean-boundary.md](06-lean-boundary.md).**

**Characterizations by named individuals (dated, attributed, not adopted as
fact by this file):** immediately after the 2018 exchange, Stix described
the proof as having a "serious, unfixable gap" while Scholze maintained abc
"is still open" (both via Quanta, row 8). Woit, a self-described non-expert
commentator, wrote in 2018 that Mochizuki's responses did not seem to
"effectively address" the specific SS objection (row 9), and by 2023
characterized it as "generally accepted by experts" that the SS paper
"conclusively shows" a flaw — a stronger, unhedged version of his earlier
post (row 10). At the April 2020 acceptance announcement, Kedlaya said
community opinion had not much changed and Tamagawa said review found "no
fundamental alteration" needed (both row 11). In March 2024, Scholze
reiterated the work "falls far short of giving a proof of ABC," while
Mochizuki called Kirti Joshi's unrelated alternative work "mathematically
meaningless" (row 13). In April 2026, LANA's lead Adam Topaz reported its
formalization stuck at a point "closely related" to the SS objection (row
14). The team's July 2026 [interim report](09-critical-mechanism.md)
(row 17) then proposed the concrete two-map compatibility (9-1) as a
possible way to account for the disputed numerical comparison; it
explicitly has **no proof** of that compatibility and reports no
complete internal agreement on the original argument's proof status.
Separately, Fesenko's own survey (cited in Rpt2018, p.42, not
independently checked by this file) estimates IUTch has been "verified at
least 30 times" (row 2).

**This research located substantially more independent (non-IUT-affiliated)
commentary characterizing the objection as unresolved or credible than
comparably independent commentary asserting it has been rebutted.** This
may reflect the actual state of published commentary, or gaps in this
research; it is flagged, not treated as a finding about mathematical
correctness. Most "verification" claims on the pro-IUTch side available to
this research (Fesenko's count, the IUGC prize panel) come from parties
actively involved in promoting or extending IUT — a fact about provenance,
not a basis for discounting their content.

---

## 5.10 Reproduction checklist for a mathematical reader

To form an independent view (which this file deliberately does not do), a
reader would need to, at minimum:

1. Read IUT III's definitions of **Θ-pilot object** and **$q$-pilot object**
   (Definition 3.8, cited by both sides) and write down, in one's own
   notation, exactly which category each lives in and what data specifies
   an isomorphism between two instances.
2. Read the full statement of **Theorem 3.11**, parts (i)–(iii) (IUT III
   pp.153–159 in the hosted version), and write down the precise scope of
   each of **(Ind1), (Ind2), (Ind3)** — what group, or what range of
   choices, each permits — not just their names.
3. Read **Corollary 3.12**'s full proof, Steps (i)–(xii) (pp. 174–186 in the
   hosted version), and independently identify every point at which a
   "copy of $\mathbb{R}$" (in SS's language) or an "arithmetic holomorphic
   structure" (in Mochizuki's) is introduced, and what map/isomorphism is
   asserted to relate it to the others.
4. At Step (xi) specifically, write out explicitly whether the map used to
   pass between the Θ-side and $q$-side log-volume is asserted to be: (a)
   literally linear everywhere it is used, (b) linear only outside the
   region affected by (Ind1)–(Ind3) and non-linear/indeterminate within it,
   or (c) some other relationship — and locate the exact sentence(s) of IUT
   III that settle this, rather than inferring it from either side's
   commentary.
5. Independently verify the arithmetic of SS's equation (1.5) (SS report
   p.4) — the weighted sum over $j=1,\dots,\ell^\star$ with coefficients
   involving $j$ and $j^2$ — and check whether dropping the $j^2$ term, as
   SS say consistency requires, actually yields the "empty inequality" they
   describe, by the reader's own calculation rather than by trusting either
   side's characterization of the result.
6. Reconcile SS's quoted intermediate conclusion from Step (xi),
   $-|\log(q)|\le-|\log(\Theta)|$ (SS report p.9), with the parametrized
   statement of Corollary 3.12 (IUT III p.174). The
   [elementary reduction in 09](09-critical-mechanism.md) shows their
   **algebraic** equivalence if both use the same normalized real
   quantities $T=|\log(\Theta)|$ and $Q=|\log(q)|$ and $Q>0$. What remains
   open is confirming that the *two texts' numerical copies* and
   normalizations match and that Step (xi)'s comparison is legitimate.
   IUT III's own proof, p. 173, explicitly states $|\log(q)|>0$.
7. Obtain, if possible, the exact 2018 IUT III text quoted by SS
   in their Step-(xi) discussion (SS p. 9) and compare its wording with
   hosted Step (xi-f), p. 184. Their separate p. 16 citation matches
   the hosted Introduction and alone supplies **no** evidence of a
   substantive revision (§5.3 and §5.12).
8. Only after 1–7, read §5.4 and §5.5 above again and check which, if
   either, side's characterization matches what was found.

---

## 5.11 Open questions / unanswered concrete verification obligations

These are stated as questions, not rhetorical ones with an implied answer:

1. Is the map used at the disputed point of Step (xi) linear, non-linear, or
   does the dispute itself partly consist in the two sides describing
   *different* maps as "the" map at that point? (§5.10.4 is the precise
   version of this question.)
2. Does SS's "(Lin)" characterization (Mochizuki's label for their alleged
   assumption, not their own phrase) accurately represent what SS's own
   diagram and equations (SS report pp.9–10) actually assume, or does it
   simplify/recharacterize their argument in translation? Neither document
   read for this file settles this from the other side's perspective in a
   way phrased in common, shared notation.
3. Is the "id-version"/simplified setting that Mochizuki says is the real
   content of SS's argument (Cmt2018-08 (C13), p.4) in fact what SS's
   report performs, or is this itself a disputed characterization of SS's
   argument? This file found no passage in which SS respond, in writing,
   specifically to the "id-version" label or to (Lin) by name (both are
   Mochizuki's post hoc labels for SS's argument, introduced in Mochizuki's
   replies) — i.e., **no public, dated SS rebuttal of Mochizuki's Sept. 2018
   Cmt2018-08 was located by this research.** If one exists, it would bear
   directly on this file's open questions and was not found.
4. Does SS's quoted Step-(xi) sentence (SS p. 9) occur verbatim in the
   edition available in 2018, and did the mathematical content change?
   The current (xi-f), p. 184, has the same inequality but different
   prose. SS's p. 16 citation fits the hosted Introduction (§5.3);
   neither fact alone establishes a change in mathematical content.
5. Does either side's account change if the "indeterminacies" (Ind1)-(Ind3)
   are given a fully explicit, independent (non-IUT) group-theoretic or
   measure-theoretic description, rather than only a name and a citation to
   where they are defined?
6. What is the current (as of this writing) status of any written, public,
   dated response by Scholze or Stix to Mochizuki's Sept. 2018 Cmt2018-08 —
   this file located none specifically targeting Cmt2018-08's (C12)-(C14)
   and (Lin) framing, only later, general restatements of their original
   2018 position (e.g. Scholze's 2024 remark, row 13) that do not engage
   the (Lin)/"id-version" labels by name.
7. Project LANA's July 2026 [interim report](09-critical-mechanism.md)
   **does** now provide a public technical formulation: section 9.2,
   PDF p. 46, asks for a suitable $S$ making its two maps
   $\eta_q$ and $\eta^{\mathrm{anab}}_S$ agree; section 10.5, p. 49,
   says the team has no proof. The report accepts that the SS hexagon
   does not commute, but argues that the intended same-side comparison
   might avoid that hexagon (pp. 47–49). The open task is to show from
   IUT III whether the claimed Step-(xi) transport yields this *specific*
   compatibility, and whether the SS hexagon is actually unavoidable.
   This replaces this file's earlier assertion that no public technical
   description had been found; it does **not** settle either objection.

---

## 5.12 Explicit flags (do not silently resolve any of these)

1. **Edition comparison still open, but no demonstrated page-16
   mismatch.** SS's "page 16" agrees with the hosted PDF's Introduction,
   which already describes Corollary 3.12; the formal statement is on
   p. 173 (§5.3). SS's quoted closing Step-(xi) sentence has the same
   inequality as hosted (xi-f), p. 184, but not its surrounding wording.
   This file cites named results plus hosted-PDF pages without assuming
   that the earlier edition was textually identical or substantively
   different.
2. **Dating ambiguity on the SS report itself.** The publicly-readable Bonn
   copy is self-dated "July 16, 2018" on its own title page; Mochizuki's
   hub page and his own Cmt2018-08 both call the same document the "August
   2018" version/report. This file could not resolve which date is
   authoritative, or whether a mid-2018 revision explains the gap, and does
   not guess.
3. **Access-restriction change over time.** The exact URL Quanta linked in
   Sept. 2018 for the SS report (`.../~motizuki/SS2018-08.pdf`, no
   `protectedpdf-` folder) returns HTTP 404 today; both of Mochizuki's
   currently-listed copies (`protectedpdf-2018-05/`, `protectedpdf-2018-08/`)
   return HTTP 403. The only publicly readable copy found by this research
   is the Bonn-hosted mirror (row 1). This is reported as an observed
   change in public accessibility, not as an inference about intent.
4. **Evidentiary asymmetry in secondary commentary**, as detailed in §5.9:
   more independent commentary located by this research treats the
   objection as live/credible than treats it as rebutted, and this
   imbalance is flagged rather than treated as a tally of correctness.
5. **No direct, dated, public SS rebuttal of Cmt2018-08 was located.** If
   later rounds of written exchange exist beyond what is listed in §5.1,
   they were not found by the searches performed for this file.
6. **One PDF's internal metadata date and title-page date disagree**
   (Cmt2018-05: title page "July 2018," container metadata showing
   September 2018); noted but not pursued further, as it does not bear on
   the mathematical content.
7. **This guide's file set is assembled by several concurrent, independent
   research strands in one shared working directory, and that directory
   was observed to change, file-by-file, within minutes during this
   file's own drafting and review** (e.g. `guide/04-claim-dependencies.md`,
   `guide/03-iut-route.md`, and `guide/06-lean-boundary.md` were each
   observed present, then absent, then present again — the last with
   revised wording — inside the single checking session on 2026-10-05 that
   produced this file). At the final check reported here, all of this
   file's cross-references — [00-map.md](00-map.md),
   [07-dictionary.md](07-dictionary.md), [08-work-queue.md](08-work-queue.md),
   and [06-lean-boundary.md](06-lean-boundary.md) — resolved, and
   `06-lean-boundary.md`'s own statement of its scope (that it does not
   itself evaluate the Scholze–Stix dispute) was checked against its
   then-current text, though §5.0 now states this only in paraphrase, not
   verbatim, to keep this file's opening section brief. None of this
   file's own factual claims about LANA depend on that sibling file's
   content regardless:
   the LANA-related claims here cite the New Scientist article (row 14),
   the LANA GitHub README (row 16), or the pinned July 2026 report
   (row 17) directly. Given the demonstrated
   volatility, a reader opening this guide later should still treat every
   cross-reference link above as liable to have moved again since this
   paragraph was written, and should not assume the sibling files' exact
   wording is frozen.

---

## 5.13 Final disclaimer

This file reports what two identified parties said, in writing, on specific
dates, at specific cited locations, about one specific step of one specific
document — and what has and has not been said about it since. It is not a
proof, not a refutation, not an endorsement of either side's characterization
of the other's argument, and not a claim that the matter is settled by
publication, by a prize, or by any formalization effort referenced above or
in [06-lean-boundary.md](06-lean-boundary.md). Where this research could not
read a source, that is stated in §5.1 and §5.12, not silently filled in.
