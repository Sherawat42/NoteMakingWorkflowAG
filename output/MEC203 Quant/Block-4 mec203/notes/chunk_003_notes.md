# Chunk 003 — Unit 13: Well-known Sequences & Properties of Sequences
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

## Section: 13.2.4(A continued) A.P. Worked Sums 🔴
<!-- Reason: Worked example for A.P. sum formula (which is core exam content). -->

### Core Idea
Demonstrates how to use the A.P. sum formula `S_n = (n/2)[2a + (n−1)d]` to compute (a) the sum of the first 10 terms, and (b) the sum of a slice from the 11th to 20th terms by computing `S_20 − S_10`.

### Examples

**Example 13.7 — A.P. `5, 3.5, 2, 0.5, −1, −2.5, ...` (a = 5, d = −1.5)**

(i) Sum of the first 10 terms:
- `S_10 = (10/2)[2(5) + (10 − 1)(−1.5)] = 5 · [10 − 9 · 1.5] = 5 · (10 − 13.5) = 5 · (−3.5) = −17.5`
- (Source writes: `5[10 − 9(1.5)] = −17.5`.)

(ii) Sum of terms from the 11th to the 20th, both included:
- Required sum = `S_20 − S_10`.
- `S_20 = (20/2)[2(5) + (20 − 1)(−1.5)] = 10 · [10 − 19 · 1.5] = 10 · (10 − 28.5) = −185`.
- Required sum = `−185 − (−17.5) = −167.5`.

> **Quick Recall:**
> - To get a "slice" sum from term `m+1` to term `n` of an A.P.: compute `S_n − S_m`.

### Connections
- Builds on: A.P. sum formula (Chunk 002).
- Continues into: G.P. (next).

---

## Section: 13.2.4(B) Geometric Progression (G.P.) 🔴
<!-- Reason: Named sequence; nth term and sum formula are core exam content; sum of infinite G.P. requires |r|<1 — a key analysis result. -->

### Core Idea
For constants `a` and `r`, the sequence `a, ar, ar², ar³, ...` is a **Geometric Progression (G.P.)**. The constant `r` is the **common ratio** and `a` is the **scale factor**. Successive terms are obtained by multiplying by `r`. To avoid trivial cases, the source assumes `a ≠ 0`, `r ≠ 0`, and `r ≠ 1` (else the sequence becomes `0, 0, 0, ...` or `a, 0, 0, ...` or `a, a, a, ...`).

> **In Simple Terms:** Each step multiplies by the same factor `r`. Whereas A.P. *adds* a fixed amount, G.P. *scales* by a fixed amount — like compound interest.

### Key Concepts

#### nth term of a G.P.
For initial term `t_1 = a` and common ratio `r`:
```
t_n = a · r^{n−1}
```

#### Sum of first n terms of a G.P.
```
S_n = a · (r^n − 1) / (r − 1)        ... (II)
```

When `|r| < 1`, this can be rewritten in the more numerically convenient form:
```
S_n = a · (1 − r^n) / (1 − r)        ... (III)
```

#### Trivial cases excluded
- `a = 0` → trivial sequence `0, 0, 0, ...`
- `r = 0` → trivial sequence `a, 0, 0, ...`
- `r = 1` → trivial sequence `a, a, a, ...`

### Definitions
- **Geometric Progression (G.P.)**: a sequence `a, ar, ar², ar³, ...` for constants `a, r`. ⭐
- **Common ratio `r`**: the multiplicative factor between consecutive terms `t_{n+1} / t_n`. ⭐
- **Scale factor `a`**: the initial term `t_1`. ⭐

### Examples

**Example 13.8 — Three G.P.s and their specific terms**
- (i) `3, 6, 12, 24, ...` is a G.P. with `a = 3`, `r = 2`.
- (ii) `3, −6, 12, −24, ...` is a G.P. with `a = 3`, `r = −2`.
- (iii) `6, 2, 2/3, 2/9, 2/27, ...` is a G.P. with `a = 6`, `r = 1/3`.

40th terms:
- Sequence (i): `t_40 = 3 · (2)^{39} = 3 · 2^{39}`.
- Sequence (ii): `t_40 = 3 · (−2)^{39} = −3 · 2^{39}`.
- 39th terms of (i) and (ii) are equal: both `3 · 2^{38}` (because the exponent on `(−2)` is even, `(−2)^{38} = 2^{38}`).

21st term of sequence (iii): `t_21 = 6 · (1/3)^{20} = 2 · (1/3)^{19}`.

**Example 13.9 — G.P. `3, −6, 12, −24, ...` (a = 3, r = −2)**

(i) Sum of the first 10 terms (using formula II):
- `S_10 = 3 · [(−2)^{10} − 1] / [(−2) − 1] = 3 · [2^{10} − 1] / (−3) = −[2^{10} − 1]`.

(ii) Sum of the first 11 terms:
- `S_11 = 3 · [(−2)^{11} − 1] / (−3) = −[(−2)^{11} − 1] = −[−2^{11} − 1] = 2^{11} + 1`.
- (Source writes the result as `2^{11} + 1`.)

(iii) Sum of terms from 11th to 20th, both included:
- Required = `S_20 − S_10`.
- `S_20 = 3[(−2)^{20} − 1] / (−3) = −[2^{20} − 1]`.
- Required = `−[2^{20} − 1] − {−[2^{10} − 1]} = −2^{20} + 1 + 2^{10} − 1 = 2^{10} − 2^{20}`.

### ⚠️ Common Mistakes
- ❌ Using `t_n = a · r^n` → ✅ Correct is `t_n = a · r^{n−1}`.
- ❌ Forgetting to exclude `r = 1` from the sum formula → ✅ The formula `S_n = a(r^n − 1)/(r − 1)` has division by zero when `r = 1`; for `r = 1` the trivial sequence has `S_n = na` directly.
- ❌ Treating `(−2)^{40}` as negative → ✅ Even powers of a negative number are positive.

> **Quick Recall:**
> - G.P. nth term: `t_n = a · r^{n−1}`
> - G.P. sum: `S_n = a(r^n − 1)/(r − 1)` (or `a(1 − r^n)/(1 − r)` when `|r| < 1`)

### Connections
- Builds on: A.P. (analogous structure with × in place of +).
- Continues into: H.P. (built from A.P.).

---

## Section: 13.2.4(C) Harmonic Progression (H.P.) 🔴
<!-- Reason: Named sequence type listed in objectives. -->

### Core Idea
A **Harmonic Progression** (H.P.) is a sequence obtained by taking the **reciprocals** of an arithmetic progression `a, a+d, a+2d, ...`, with the proviso that none of the A.P. terms equal zero (i.e., `a + n·d ≠ 0` for `n = 0, 1, 2, ...`). Most facts about H.P. follow directly from the corresponding facts about A.P.

> **In Simple Terms:** Flip each term of an A.P. upside-down — that's an H.P.

### Key Concepts

#### nth term of an H.P.
Since the nth term of the underlying A.P. is `a + (n−1)d`, the nth term of the H.P. is its reciprocal:
```
t_n^{H.P.} = 1 / [a + (n − 1)d]
```

### Definitions
- **Harmonic Progression (H.P.)**: the sequence `1/a, 1/(a+d), 1/(a+2d), ...` of reciprocals of an A.P. (with no zero terms). ⭐

### Examples

**Example 13.10 — H.P.s from A.P.s**
- (i) For the A.P. `1, 2, 3, 4, ...` (a = 1, d = 1), the corresponding H.P. is `1, 1/2, 1/3, ..., 1/n, ...`. This is also known as the **Harmonic Sequence**.
- (ii) For the A.P. with `a = 1/16`, `d = 1/16` — that is, `1/16, 2/16, 3/16, 4/16, 5/16, 6/16, ...` — the corresponding H.P. is `16, 8, 16/3, 4, 16/5, ...`.

### Edge Cases & Caveats
- The condition `a + n·d ≠ 0` for any `n` is essential: if any A.P. term is 0, its reciprocal is undefined.

### Connections
- Builds on: A.P. (Chunk 002 / this chunk).

---

## Section: 13.2.4(D) Fibonacci Sequence 🔴
<!-- Reason: Named sequence type, recursive definition, sum formula, closed form. Listed in objectives. -->

### Core Idea
The **Fibonacci sequence** `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...` is recursively defined by `F_0 = 0`, `F_1 = 1`, and `F_n = F_{n−1} + F_{n−2}` for `n ≥ 2`. It also has a (cumbersome) closed-form expression and a clean formula for the sum of the first `n` terms.

> **In Simple Terms:** Each term is the sum of the previous two. Starts with 0 and 1.

### Key Concepts

#### Recursive definition
```
F_0 = 0,  F_1 = 1,  F_n = F_{n−1} + F_{n−2}  for n ≥ 2.        ... (13.2)
```

#### Closed-form (Binet) formula
```
F_n = [ {(1 + √5)/2}^n − {(1 − √5)/2}^n ] / √5
```
Source notes this formula is "quite a cumbersome one" but can be used to calculate the nth term directly.

#### Sum of first n terms
```
Σ_{i=1}^{n} F_i = F_{n+2} − 1     for all n.
```

### Definitions
- **Fibonacci sequence**: the sequence `(F_n)` defined by `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}` for `n ≥ 2`. ⭐

### Examples

**Example 13.11 — Fibonacci first terms and sum**
(a) First ten terms: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34`.

(b) Sum of the first six terms using `Σ F_n = F_{n+2} − 1` with `n = 6`:
- `Σ_{n=1}^{6} F_n = F_8 − 1 = 13 − 1 = 12`.

> **Quick Recall:**
> - Fibonacci recurrence: `F_n = F_{n−1} + F_{n−2}`, with `F_0 = 0`, `F_1 = 1`.
> - Sum formula: `Σ_{i=1}^{n} F_i = F_{n+2} − 1`.

### Connections
- Builds on: Recursively definable sequences (Chunk 002).
- Continues into: Boundedness of Fibonacci (next section).

---

## Section: 13.3 Properties of Sequences — Bounded Sequence 🔴
<!-- Reason: Definition appears in Key Words; foundational for later convergence and Bolzano-Weierstrass theorem. -->

### Core Idea
A sequence `(S_n)` is **bounded above** if there exists a real `C` such that `S_n ≤ C` for all `n ∈ N`. It is **bounded below** if there exists a real `D` such that `D ≤ S_n` for all `n`. It is **bounded** if both — i.e., there exist reals `D ≤ C` such that `D ≤ S_n ≤ C` for all `n ∈ N`.

> **In Simple Terms:** A bounded sequence "lives inside" some horizontal strip on the number line.

### Definitions
- **Bounded above**: ∃ real `C` such that `S_n ≤ C` ∀ `n ∈ N`. ⭐
- **Bounded below**: ∃ real `D` such that `D ≤ S_n` ∀ `n ∈ N`. ⭐
- **Bounded**: bounded both above and below. ⭐

### Examples

**Example 13.12 — Three bounded/unbounded sequences**
- (i) `(..., −10, −8, −6, ..., 0, 2, 4, 6)` — bounded above (by 6) but not bounded below.
- (ii) `(−10, −8, −6, ..., 0, 2, 4, 6, ...)` — bounded below (by −10) but not bounded above.
- (iii) `(−10, −8, −6, ..., 0, 2, 4, 6)` — bounded both above and below (it is finite).

### Key Concepts

#### Boundedness of well-known sequences (proofs in Exercises)
- **A.P.** `(a + (n−1)d)`, non-trivial (`d ≠ 0`):
  - (i) not bounded above if `d > 0`,
  - (ii) not bounded below if `d < 0`.
- **G.P.** `(a · r^{n−1})`, non-trivial (`a ≠ 0`, `1 ≠ r ≠ 0`):
  - (i) not bounded above if `r > 1` and `a > 0`,
  - (ii) not bounded below if `r > 1` and `a < 0`,
  - (iii) bounded neither above nor below if `r < −1`.
- **Fibonacci** `(F_n) = (0, 1, 1, 2, 3, 5, 8, ...)`: not bounded above, but bounded below by 0.

### Connections
- Builds on: A.P., G.P., Fibonacci (this chunk).
- Continues into: Monotone sequences (next).

---

## Section: 13.3.2 Monotone Sequence 🔴
<!-- Reason: Listed in objectives; pairs with boundedness for the Monotone-Bounded Convergence framework (introduced via the Bolzano-Weierstrass corollary). -->

### Core Idea
A sequence `(S_n)`, `n ∈ N`, is:
- **monotonically increasing** if `S_n ≤ S_{n+1}` for all `n ∈ N`; **strictly** monotonically increasing if `S_n < S_{n+1}`.
- **monotonically decreasing** if `S_{n+1} ≤ S_n` for all `n ∈ N`; **strictly** monotonically decreasing if `S_{n+1} < S_n`.
- **monotonic** if it is either monotonically increasing or monotonically decreasing.
- **alternating** if successive terms change sign from plus to minus to plus, e.g., `(1, −3, 5, −7, ...)` or `(−1, 3, −5, 7, ...)`.

> **In Simple Terms:** Monotonic = "always moving in one direction" (never reversing). Strict = no flat steps.

### Definitions
- **Monotonically increasing**: `S_n ≤ S_{n+1}` ∀ `n ∈ N`. ⭐
- **Strictly monotonically increasing**: `S_n < S_{n+1}` ∀ `n ∈ N`. ⭐
- **Monotonically decreasing**: `S_{n+1} ≤ S_n` ∀ `n ∈ N`. ⭐
- **Strictly monotonically decreasing**: `S_{n+1} < S_n` ∀ `n ∈ N`. ⭐
- **Monotonic**: monotonically increasing OR monotonically decreasing. ⭐
- **Alternating sequence**: terms alternate in sign.

### Examples

**Example 13.13 — Five sequences classified**
- (i) `(1, 3, 5, 7, ...)` — strictly monotonically increasing.
- (ii) `(−1, −3, −5, −7, ...)` — strictly monotonically decreasing.
- (iii) `(1, 1/3, 1/5, 1/7, ...)` — strictly monotonically decreasing.
- (iv) `(−1, −1/3, −1/5, −1/7, ...)` — strictly monotonically increasing.
- (v) `(−1, 1, −3, 3, −5, 5, ...)` — neither monotonically increasing nor decreasing.

### Key Concepts

#### Bounded vs Monotonic — independence
The two properties are independent:
- (i) A bounded sequence may not be monotonic, e.g., `(1, 2, 1, 2, ...)`.
- (ii) A monotonic sequence may not be bounded, e.g., `(1, 2, 3, ...)`.
- (iii) But there are sequences which are both, e.g., `(1 + 1/n)`, `n ∈ N`, is bounded (above by 2, below by 1) and monotonic.

### ⚠️ Common Mistakes
- ❌ Treating "alternating" as a kind of monotonic → ✅ Alternating sequences are explicitly *not* monotonic in general.
- ❌ Equating boundedness with monotonicity → ✅ The two are independent properties.

### Connections
- Builds on: Bounded sequence (above).
- Continues into: Convergence (next).

---

## Section: 13.3.3 Convergent / Divergent / Oscillatory Sequences 🔴
<!-- Reason: Convergence and Cauchy sequence are explicitly in Key Words. ε-n_ε definition is foundational and exam-critical. Also covers Bolzano-Weierstrass for sequences. -->

### Core Idea
A sequence "converges" if, beyond some initial terms, all later terms get arbitrarily close to a fixed real number `l` — its **limit**. Formally captured by the ε–`n_ε` definition. Sequences that don't converge fall into four categories: finitely oscillatory, divergent to +∞, divergent to −∞, infinitely oscillatory. The notion of *limit point* generalises *limit* — a sequence may have several limit points even when it has no limit.

> **In Simple Terms:** A sequence converges to `l` if you can make it stay as close to `l` as you wish, by chopping off enough early terms.

### Key Concepts

#### Formalising "closer and closer" (the ε–`n_ε` machinery)
Two informal notions need formalisation:
1. "Terms `S_n` get as close to `l` as we wish" → "let `ε > 0` be as small as we like, so that `|S_n − l| ≤ ε`".
2. "Except for some initial terms" → "for all `n > n_ε`", where `n_ε` indicates we may set aside `n_ε` initial terms. Smaller `ε` → larger `n_ε` (the closer you want to be to the limit, the more early terms you may need to discard).

#### Convergent Sequence — formal definition
A sequence `(S_n)` is **convergent** if there exists a (finite) real number `l` such that for every `ε > 0`, there exists a natural number `n_ε` with `|S_n − l| < ε` for all `n > n_ε`. Then `l` is the **limit** and we write `lim_{n→∞} S_n = l`.

#### Uniqueness of limit
If `lim_{n→∞} S_n = l`, then no `l' ≠ l` can also be a limit.
**Proof (sketch from source):** Let `|l − l'| = 2ε > 0`. Since `lim S_n = l`, for this `ε` there exists `n_ε` with `|S_n − l| < ε` for all `n > n_ε`. By the triangle inequality:
`|l − l'| ≤ |l − S_n| + |S_n − l'|`
so `|S_n − l'| ≥ |l − l'| − |S_n − l| > 2ε − ε = ε`.
Thus `|S_n − l'| > ε` for all sufficiently large `n`, so `l'` cannot be a limit.

#### Cauchy Sequence
A sequence `(S_n)` is a **Cauchy sequence** if for every `ε > 0`, there exists a natural number `n_ε` such that `|S_n − S_m| < ε` for all `n, m > n_ε`.

The Cauchy definition does *not* require guessing the limit in advance — it captures the same idea ("terms get close to each other") as convergence.

**Theorem (Convergence ⇔ Cauchy):** A sequence `(S_n)` is convergent if and only if it is a Cauchy sequence.

#### Non-convergent sequences — four categories
1. **Finitely oscillatory**: `(S_n)` is bounded but not convergent.
   - Examples: `((−1)^n) = (−1, 1, −1, 1, ...)`; `(1 + (−1)^n) = (0, 2, 0, 2, ...)`.
2. **Divergent to +∞**: for every real `Δ` (delta), howsoever large and positive, ∃ `n_Δ` such that `S_n > Δ` for all `n > n_Δ`. (Successive terms become unboundedly large.)
3. **Divergent to −∞**: for every real `Δ` > 0, ∃ `n_Δ` such that `S_n < (−Δ)` for all `n > n_Δ`. (Successive terms become unboundedly large in magnitude with negative sign.)
4. **Infinitely oscillatory**: unbounded, and diverges neither to +∞ nor to −∞.

#### Limit Point of a sequence
For a sequence `(S_n)`, a real number `LP` is a **limit point** if some subsequence of `(S_n)` converges to `LP`.

**Results:**
- For a convergent sequence, its limit is also a limit point (the sequence is its own subsequence).
- A limit point need not be a limit. E.g., `((−1)^n) = (−1, 1, −1, 1, ...)` has two limit points (1 and −1) but no limit (it isn't convergent).

#### Bolzano-Weierstrass Theorem for sequences
**Statement:** Every bounded sequence has a limit point.

**Corollary:** Every bounded sequence has a convergent subsequence.

### Definitions
- **Convergent sequence**: ∃ real `l` such that ∀ `ε > 0`, ∃ `n_ε ∈ N` with `|S_n − l| < ε` for all `n > n_ε`. ⭐
- **Limit of a sequence**: the unique `l` in the convergence definition; written `lim_{n→∞} S_n = l`. ⭐
- **Cauchy sequence**: ∀ `ε > 0`, ∃ `n_ε ∈ N` with `|S_n − S_m| < ε` for all `n, m > n_ε`. ⭐
- **Finitely oscillatory**: bounded but non-convergent. ⭐
- **Divergent to +∞**: ∀ `Δ > 0`, ∃ `n_Δ` with `S_n > Δ` for all `n > n_Δ`. ⭐
- **Divergent to −∞**: ∀ `Δ > 0`, ∃ `n_Δ` with `S_n < −Δ` for all `n > n_Δ`. ⭐
- **Infinitely oscillatory**: unbounded; not divergent to ±∞. ⭐
- **Limit point of a sequence**: real number to which some subsequence converges. ⭐

### Examples

**Example 13.14 — Show `(S_n) = (1 + 1/n)` converges to 1.**
By definition, the sequence converges to 1 iff for every `ε > 0`, ∃ `n_ε` with `|(1 + 1/n) − 1| = |1/n| = 1/n < ε` for all `n > n_ε`. ...(A)

By the **Archimedean property**, given positive reals `1` and `ε`, ∃ a natural number `M` such that `Mε > 1`. Then for all `n > M`, `nε > Mε > 1`, so `1/n < ε`. Take `n_ε = M`; the result is proved.

**Example 13.15 — Sequences divergent to +∞**
- (a) `(S_n) = (2n − 1) = (1, 3, 5, ...)`.
- (b) `(S_n) = (a r^n)` with `r > 1`, `a > 0` (a G.P. with ratio > 1 and positive scale factor).

**Example 13.16 — Sequences divergent to −∞**
- (a) `(S_n) = (1 − 2n) = (−1, −3, −5, ...)`.
- (b) `(S_n) = (a r^n)` with `r > 1`, `a < 0`.

**Example 13.17 — Infinitely oscillatory sequences**
- (a) `(S_n) = ((−1)^n · n²) = (−1, 4, −9, 16, −25, ...)` (source writes it as `(−1, 5, −5, 9, ...)` due to OCR; intent is alternating-sign powers).
- (b) `(S_n) = (a · (−r)^n)` with `r > 1`, `a > 0` — the subsequence `(−ar, −ar³, −ar⁵, ...)` tends to −∞ while the subsequence `(ar², ar⁴, ar⁶, ...)` tends to +∞.

**Examples F (page 30) — Working out convergence**

*F.1: Show that `(S_n)` with `S_n = √(n+1) − √n` converges (to 0).*
Multiply numerator and denominator by `√(n+1) + √n`:
- `S_n = [√(n+1) − √n] · [√(n+1) + √n] / [√(n+1) + √n]`
- `   = [(n+1) − n] / [√(n+1) + √n]`
- `   = 1 / [√(n+1) + √n]`
- `   < 1 / [√n + √n] = 1 / (2√n)` (denominator decreases ⇒ value increases).

For given `ε > 0`, find `n_ε` such that `|1/(2√n) − 0| < ε`. Squaring: `1/(4n) < ε²`, so `n > 1/(4ε²)`. Thus for all `n > 1/(4ε²)`, `|S_n − 0| < ε`. Hence `lim S_n = 0`.

*F.2: Show that `lim_{n→∞} (n² + 5n − 7) / (3n² + 12n + 14) = 1/3`.*
Consider:
- `(n² + 5n − 7)/(3n² + 12n + 14) − 1/3`
- `= [3(n² + 5n − 7) − (3n² + 12n + 14)] / [3(3n² + 12n + 14)]`
- `= (3n − 35) / [3(3n² + 12n + 14)] < 3n / [3(3n² + 12n + 14)] < 3n / (9n²) = 1/(3n) < 1/n`.

So `|(n² + 5n − 7)/(3n² + 12n + 14) − 1/3| < 1/n`. For given `ε > 0`, choose `n_ε > 1/ε`; then `1/n < ε` for all `n > n_ε`. Hence the limit is `1/3`.

### ⚠️ Common Mistakes
- ❌ Saying "limit point" and "limit" are the same → ✅ Every limit is a limit point, but a sequence may have many limit points and yet have no limit (it's then non-convergent).
- ❌ Forgetting `n_ε` depends on `ε` → ✅ Smaller `ε` typically requires larger `n_ε`.
- ❌ Using a single `n` to verify convergence → ✅ Must show "for all `n > n_ε`".

### Edge Cases & Caveats
- A bounded non-convergent sequence is **finitely oscillatory** (by definition).
- The Bolzano-Weierstrass corollary only guarantees a *convergent subsequence* — the original sequence itself need not converge.

> **Quick Recall:**
> - Convergence: ∀ `ε > 0` ∃ `n_ε`: `|S_n − l| < ε` ∀ `n > n_ε`.
> - Cauchy: ∀ `ε > 0` ∃ `n_ε`: `|S_n − S_m| < ε` ∀ `n, m > n_ε`.
> - Convergent ⇔ Cauchy.
> - Limit (if exists) is unique.
> - Bolzano-Weierstrass (sequences): every bounded sequence has a limit point ⇒ has a convergent subsequence.

### Connections
- Builds on: Bounded sequences, monotone sequences (this chunk).
- Continues into: Bolzano-Weierstrass for sets and economic applications (Chunk 004).
