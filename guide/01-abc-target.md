# 1. The target: a precise abc inequality

Take positive integers \(a,b,c\) with \(a+b=c\) and \(\gcd(a,b)=1\).
The other pairwise gcds are then also 1:
\(\gcd(a,c)=\gcd(a,a+b)=1\) and similarly \(\gcd(b,c)=1\).
For any positive integer \(n\), define its **radical**

\[
\operatorname{rad}(n)=\prod_{\substack{p\text{ prime}\\p\mid n}}p,
\qquad \operatorname{rad}(1)=1.
\]

Write \(R=\operatorname{rad}(abc)\). The usual abc conjecture says

\[
\forall\varepsilon>0\ \exists K_\varepsilon>0\
\forall(a,b,c)\quad
c\leq K_\varepsilon R^{1+\varepsilon}.
\tag{ABC}
\]

The quantifiers matter: **one** constant works for *all* primitive positive
triples at a fixed \(\varepsilon\); it may depend on \(\varepsilon\), and this
statement does not give a way to compute it. The alternative symmetric
formulation uses coprime nonzero \(A+B+C=0\), with
\(\max(|A|,|B|,|C|)\) in place of \(c\)
([Goldfeld, §1, PDF p. 1](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=1)).

## Why count primes instead of their powers?

For \(n=\prod p^{v_p(n)}\), where \(v_p(n)\) is the exponent of \(p\),

\[
\log n=\sum_p v_p(n)\log p,\qquad
\log\operatorname{rad}(n)=\sum_{v_p(n)>0}\log p.
\]

Thus the radical remembers *which* primes occur and forgets *how many times*
they occur. For \(1+8=9\), the product is \(2^3 3^2\), so
\(R=2\cdot3=6\), not \(72\). The quality
\(q(a,b,c)=\log c/\log R\) is about \(1.226\). A sharper example is
\(3+125=128\): \(R=2\cdot3\cdot5=30\), and \(q\approx1.427\).
These finite examples do **not** disprove (ABC); the conjecture permits
exceptions to every fixed exponent \(1+\varepsilon\).

Taking logarithms expresses the proposed bound as
\(\log c\leq(1+\varepsilon)\log R+\log K_\varepsilon\). This is a
useful *target shape*, not permission to substitute another theory's
notion of "volume" for \(\log R\) without proof.

## Why "finitely many exceptions" means the same thing

A frequently used equivalent formulation is: for **every** \(\eta>0\)
only finitely many primitive positive triples satisfy
\(c>R^{1+\eta}\).

To get (ABC) from this form, fix \(\varepsilon\). Outside its finite
exceptional set, \(c\leq R^{1+\varepsilon}\); choose \(K_\varepsilon\)
larger than 1 and all the finitely many ratios
\(c/R^{1+\varepsilon}\) in that set.

Conversely, assume (ABC) holds for *every* positive exponent. Given
\(\eta>0\), apply it with \(\varepsilon=\eta/2\). If
\(c>R^{1+\eta}\), then
\(R^{\eta/2}<K_{\eta/2}\), so \(R\) is bounded. The same uniform
inequality now bounds \(c\); hence there are only finitely many possible
positive triples. Taking a smaller exponent is essential: (ABC) with
exponent \(\eta\) alone does not supply this argument.

## An elementary view of the elliptic-curve bridge

For an elliptic curve \(E/\mathbb Q\), the **minimal discriminant**
\(\Delta_E\) measures degeneration with multiplicities, while the
**conductor** \(N_E\) records the bad primes with reduction-dependent
exponents. The Szpiro-type estimate in
[Goldfeld, §4, PDF p. 7](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=7)
has the *conjectural* shape
\[
|\Delta_E|\leq C_\delta N_E^{6+\delta}\quad(\delta>0).
\]

For a primitive abc triple, the associated Frey--Hellegouarch curve is
\[
E_{a,b}:\quad y^2=x(x-a)(x+b).
\]
For \(1+8=9\), the three roots of the cubic are \(0,1,-8\).
The displayed **integral model** has discriminant
\(16(1\cdot8\cdot9)^2=82944=2^{10}3^4\), while its abc radical is
\(R=6\). This calculation explains why discriminant *exponents* and prime
*support* differ; it does **not** compute the minimal discriminant or
conductor.

Goldfeld explains that after passing to a minimal model its discriminant is
\((abc)^2\) times a bounded power of 2, and its conductor is \(R\) times a
bounded power of 2. **Conditionally on** the Szpiro-type estimate, this
yields
\[
(abc)^2\ \ll_\delta\ R^{6+\delta}
\quad\Longrightarrow\quad
(abc)^{1/3}\ \ll_\eta\ R^{1+\eta}
\quad(\eta=\delta/6).
\]

Goldfeld calls this last inequality **weak abc** ([§1, PDF p. 1](https://www.math.columbia.edu/~goldfeld/ABC-Conjecture.pdf#page=1)).
The usual (ABC) immediately implies weak abc because
\((abc)^{1/3}\leq c\); the reverse implication is **not derived here**.
For instance, when \(a=1,b=c-1\), the geometric mean
\((abc)^{1/3}\) grows like \(c^{2/3}\), not \(c\): a bound on that
mean does not *by itself* give the desired bound on \(c\) with the
same exponent.
Do not turn this schematic conditional bridge into "Szpiro has been proved,"
or silently identify the weak inequality with the target (ABC). Establishing
which *precise* inequality IUT IV claims is a separate task.

## Check your understanding

1. For \(3+125=128\), why does the factor \(5^3\) contribute only \(5\)
   to \(R\)? Because the radical discards the exponent \(v_5(125)=3\).
2. Why does a constant in (ABC) not rule out the example \(3+125=128\)?
   Because it can absorb any finite set of high-quality triples.
3. In the finite-exceptions argument, why use \(\eta/2\) rather than
   \(\eta\)? It forces \(R\) to be bounded before bounding \(c\).

Further elementary exercises: [Keith Conrad, *Analogies between
\(\mathbb Z\) and \(F[T]\)*, homework 5, PDF p. 1](https://kconrad.math.uconn.edu/ross2003/analogy5.pdf#page=1).
This chapter verifies the **target and elementary implications**, not IUT.
