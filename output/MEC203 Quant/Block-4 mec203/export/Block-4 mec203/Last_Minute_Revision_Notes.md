# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Symbol | Name | Symbol | Name |
|---|---|---|---|
| α | Alpha | θ | Theta |
| β | Beta | λ | Lambda |
| γ | Gamma | π | Pi |
| δ | Delta | σ | Sigma |
| ε | Epsilon | χ | Chi |
| ψ | Psi | μ | Mu |
| ρ | Rho | ω | Omega |

**Quick Recall:**
- Volume 2 covers Blocks 4-6.
- Block 4 = Real Analysis = Units 13-15.
- Unit 13 begins on Volume 2 page 11.

### ⚠️ Common Mistakes
- ❌ Applying `S = 1 + r + r² + ...` ⇒ `S = 1/(1−r)` to any `r` → ✅ Only valid when `|r| < 1` (series converges).
- ❌ Manipulating `lim (y)^n` algebraically without checking it exists → ✅ The limit might not exist (e.g., `y = 2`), so the manipulation is invalid.

### 13.2 Sequences — Set & Function Conceptualisations 🔴

**Notation**

**Set-type conceptualisation**
1. It is **ordered**: `(E, V, I, L)` and `(V, I, L, E)` are *distinct* sequences from the same letter set `{E, I, V, L}`.
2. It is **enumerated**: all elements can be listed one after another (1st, 2nd, 3rd, ...). For example, `(0, 1, 4, 9, ...)` lists squares of integers in order. **R itself, or any sub-interval like [0, 1], cannot be represented as a sequence** under any relation, because `|R| > |N|` (R is uncountable).
3. It **allows repetition**: `(1, 2, 4, 2, 4)` is a valid sequence, even though `{1, 2, 4, 2, 4}` is not proper set notation.

**Sequence as a function**
- `S`, the domain, is either:
  - (a) the set N of natural numbers, or
  - (b) an interval subset of N, e.g. integers in [10, 20] or [10, ∞), or
  - (c) integers in finite extensions [−k, n] or [−k, ∞), for `k, n ∈ N`.
- The codomain may be R, or Q, Z, C, or any non-empty set.

**Indexing and rank**

**Length and finiteness**

**Subsequence**
1. it is obtained by deleting some terms of `(S_n)` — every term of the subsequence occurs somewhere in `(S_n)`, AND
2. the relative positions of remaining elements are preserved — if `S_p` and `S_q` are both kept and `S_p` precedes `S_q` in the original, then `S_p` precedes `S_q` in the subsequence.

**Recursively definable sequence**
- **Sequence (set view)**: an ordered, enumerated set that allows repetition of elements. ⭐
- **Sequence (function view)**: a function `f: S → R` where `S ⊆ Z` is N or an interval subset of integers; written `(f_n) = (f(1), f(2), ...)`. ⭐
- **Indexing set**: the domain `S` in the functional representation.
- **Term / element**: a constituent of the sequence.
- **Index (rank)**: for an element `r` in the sequence, the unique `s ∈ S` with `f(s) = r`.
- **Length**: number of occurrences of terms (may be infinite).
- **n-tuple**: a finite sequence of length `n`.
- **Subsequence**: a sequence formed by deleting some terms of a given sequence without disturbing the relative order of the remaining ones. ⭐
- **Recursively definable**: nth term is given by a formula involving previous term(s). ⭐

### ⚠️ Common Mistakes
- ❌ Treating `(4, 2, 6, ...)` as a subsequence of `(1, 2, 3, ...)` → ✅ Order must be preserved; this fails because 4 precedes 2 in the candidate but 2 precedes 4 in the original.
- ❌ Confusing "index" with "position in the listing" → ✅ Index is the input value `s ∈ S`; position is where it appears when listed.
- R cannot be represented as a sequence under any ordering relation, because `|R| > |N|`.
- Even an interval like [0, 1] cannot be enumerated as a sequence — there is no "next real number after 0" under `<`.
- Builds on: Sets and functions (Block 1, Unit 3 — Relations and Functions).
- Continues into: 13.2.4 Well-known Types (A.P., next).

### 13.2.4(A) Arithmetic Progression (A.P.) 🔴

**nth term formula**

**Sum of first n terms — formula and derivation**
1. Write `S_n = t_1 + t_2 + ... + t_{n−1} + t_n`.
2. Reverse the order: `S_n = t_n + t_{n−1} + ... + t_2 + t_1`.
3. Add corresponding terms: `2 S_n = (t_1 + t_n) + (t_2 + t_{n−1}) + ... + (t_n + t_1)`.
4. Each pair sums to `(t_1 + t_n)` — for instance, `(t_2 + t_{n−1}) = [(t_1 + d) + (t_n − d)] = (t_1 + t_n)`.
5. Therefore `2 S_n = n (t_1 + t_n)`, so `S_n = (n/2)(t_1 + t_n)`.
6. Substituting `t_n = a + (n−1)d`: `S_n = (n/2)[2a + (n−1)d]`.
- **Arithmetic Progression (A.P.)**: a sequence `a, a+d, a+2d, a+3d, ...` for constants `a, d`. ⭐
- **Initial term `a`**: the first term `t_1`. ⭐
- **Common difference `d`**: the constant difference between consecutive terms `t_{n+1} − t_n`. ⭐
- (i) `3, 7, 11, 15, ...` is an A.P. with `a = 3`, `d = 4`. The 40th term is `t_40 = 3 + (40 − 1) × 4 = 3 + 156 = 159`.
- (ii) `5, 3.5, 2, 0.5, −1, −2.5, ...` is an A.P. with `a = 5`, `d = −1.5`. The 21st term is `t_21 = 5 + (21 − 1) × (−1.5) = 5 − 30 = −25`.

### ⚠️ Common Mistakes
- ❌ Using `t_n = a + n · d` → ✅ Correct formula is `t_n = a + (n − 1) · d` (because `t_1 = a` requires the offset of 1).
- ❌ Forgetting that `d` can be negative (decreasing A.P.) → ✅ A.P.s with `d < 0` are perfectly valid (e.g., Example 13.6(ii)).

**Quick Recall:**
- A.P. nth term: `t_n = a + (n − 1)d`
- A.P. sum: `S_n = (n/2)[2a + (n−1)d] = (n/2)(t_1 + t_n)`
- Builds on: Sequences as functions (13.2.2, this chunk).
- Continues into: A.P. examples and Geometric Progression (Chunk 003).

### 13.2.4(A continued) A.P. Worked Sums 🔴
- `S_10 = (10/2)[2(5) + (10 − 1)(−1.5)] = 5 · [10 − 9 · 1.5] = 5 · (10 − 13.5) = 5 · (−3.5) = −17.5`
- (Source writes: `5[10 − 9(1.5)] = −17.5`.)
- Required sum = `S_20 − S_10`.
- `S_20 = (20/2)[2(5) + (20 − 1)(−1.5)] = 10 · [10 − 19 · 1.5] = 10 · (10 − 28.5) = −185`.
- Required sum = `−185 − (−17.5) = −167.5`.

**Quick Recall:**
- To get a "slice" sum from term `m+1` to term `n` of an A.P.: compute `S_n − S_m`.
- Builds on: A.P. sum formula (Chunk 002).
- Continues into: G.P. (next).

### 13.2.4(B) Geometric Progression (G.P.) 🔴

**nth term of a G.P.**

**Sum of first n terms of a G.P.**

**Trivial cases excluded**
- `a = 0` → trivial sequence `0, 0, 0, ...`
- `r = 0` → trivial sequence `a, 0, 0, ...`
- `r = 1` → trivial sequence `a, a, a, ...`
- **Geometric Progression (G.P.)**: a sequence `a, ar, ar², ar³, ...` for constants `a, r`. ⭐
- **Common ratio `r`**: the multiplicative factor between consecutive terms `t_{n+1} / t_n`. ⭐
- **Scale factor `a`**: the initial term `t_1`. ⭐
- (i) `3, 6, 12, 24, ...` is a G.P. with `a = 3`, `r = 2`.
- (ii) `3, −6, 12, −24, ...` is a G.P. with `a = 3`, `r = −2`.
- (iii) `6, 2, 2/3, 2/9, 2/27, ...` is a G.P. with `a = 6`, `r = 1/3`.
- Sequence (i): `t_40 = 3 · (2)^{39} = 3 · 2^{39}`.
- Sequence (ii): `t_40 = 3 · (−2)^{39} = −3 · 2^{39}`.
- 39th terms of (i) and (ii) are equal: both `3 · 2^{38}` (because the exponent on `(−2)` is even, `(−2)^{38} = 2^{38}`).
- `S_10 = 3 · [(−2)^{10} − 1] / [(−2) − 1] = 3 · [2^{10} − 1] / (−3) = −[2^{10} − 1]`.
- `S_11 = 3 · [(−2)^{11} − 1] / (−3) = −[(−2)^{11} − 1] = −[−2^{11} − 1] = 2^{11} + 1`.
- (Source writes the result as `2^{11} + 1`.)
- Required = `S_20 − S_10`.
- `S_20 = 3[(−2)^{20} − 1] / (−3) = −[2^{20} − 1]`.
- Required = `−[2^{20} − 1] − {−[2^{10} − 1]} = −2^{20} + 1 + 2^{10} − 1 = 2^{10} − 2^{20}`.

### ⚠️ Common Mistakes
- ❌ Using `t_n = a · r^n` → ✅ Correct is `t_n = a · r^{n−1}`.
- ❌ Forgetting to exclude `r = 1` from the sum formula → ✅ The formula `S_n = a(r^n − 1)/(r − 1)` has division by zero when `r = 1`; for `r = 1` the trivial sequence has `S_n = na` directly.
- ❌ Treating `(−2)^{40}` as negative → ✅ Even powers of a negative number are positive.

**Quick Recall:**
- G.P. nth term: `t_n = a · r^{n−1}`
- G.P. sum: `S_n = a(r^n − 1)/(r − 1)` (or `a(1 − r^n)/(1 − r)` when `|r| < 1`)
- Builds on: A.P. (analogous structure with × in place of +).
- Continues into: H.P. (built from A.P.).

### 13.2.4(C) Harmonic Progression (H.P.) 🔴

**nth term of an H.P.**
- **Harmonic Progression (H.P.)**: the sequence `1/a, 1/(a+d), 1/(a+2d), ...` of reciprocals of an A.P. (with no zero terms). ⭐
- (i) For the A.P. `1, 2, 3, 4, ...` (a = 1, d = 1), the corresponding H.P. is `1, 1/2, 1/3, ..., 1/n, ...`. This is also known as the **Harmonic Sequence**.
- (ii) For the A.P. with `a = 1/16`, `d = 1/16` — that is, `1/16, 2/16, 3/16, 4/16, 5/16, 6/16, ...` — the corresponding H.P. is `16, 8, 16/3, 4, 16/5, ...`.
- The condition `a + n·d ≠ 0` for any `n` is essential: if any A.P. term is 0, its reciprocal is undefined.
- Builds on: A.P. (Chunk 002 / this chunk).

### 13.2.4(D) Fibonacci Sequence 🔴

**Recursive definition**

**Closed-form (Binet) formula**

**Sum of first n terms**
- **Fibonacci sequence**: the sequence `(F_n)` defined by `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}` for `n ≥ 2`. ⭐
- `Σ_{n=1}^{6} F_n = F_8 − 1 = 13 − 1 = 12`.

**Quick Recall:**
- Fibonacci recurrence: `F_n = F_{n−1} + F_{n−2}`, with `F_0 = 0`, `F_1 = 1`.
- Sum formula: `Σ_{i=1}^{n} F_i = F_{n+2} − 1`.
- Builds on: Recursively definable sequences (Chunk 002).
- Continues into: Boundedness of Fibonacci (next section).

### 13.3 Properties of Sequences — Bounded Sequence 🔴
- **Bounded above**: ∃ real `C` such that `S_n ≤ C` ∀ `n ∈ N`. ⭐
- **Bounded below**: ∃ real `D` such that `D ≤ S_n` ∀ `n ∈ N`. ⭐
- **Bounded**: bounded both above and below. ⭐
- (i) `(..., −10, −8, −6, ..., 0, 2, 4, 6)` — bounded above (by 6) but not bounded below.
- (ii) `(−10, −8, −6, ..., 0, 2, 4, 6, ...)` — bounded below (by −10) but not bounded above.
- (iii) `(−10, −8, −6, ..., 0, 2, 4, 6)` — bounded both above and below (it is finite).

**Boundedness of well-known sequences (proofs in Exercises)**
- **A.P.** `(a + (n−1)d)`, non-trivial (`d ≠ 0`):
  - (i) not bounded above if `d > 0`,
  - (ii) not bounded below if `d < 0`.
- **G.P.** `(a · r^{n−1})`, non-trivial (`a ≠ 0`, `1 ≠ r ≠ 0`):
  - (i) not bounded above if `r > 1` and `a > 0`,
  - (ii) not bounded below if `r > 1` and `a < 0`,
  - (iii) bounded neither above nor below if `r < −1`.
- **Fibonacci** `(F_n) = (0, 1, 1, 2, 3, 5, 8, ...)`: not bounded above, but bounded below by 0.
- Builds on: A.P., G.P., Fibonacci (this chunk).
- Continues into: Monotone sequences (next).

### 13.3.2 Monotone Sequence 🔴
- **monotonically increasing** if `S_n ≤ S_{n+1}` for all `n ∈ N`; **strictly** monotonically increasing if `S_n < S_{n+1}`.
- **monotonically decreasing** if `S_{n+1} ≤ S_n` for all `n ∈ N`; **strictly** monotonically decreasing if `S_{n+1} < S_n`.
- **monotonic** if it is either monotonically increasing or monotonically decreasing.
- **alternating** if successive terms change sign from plus to minus to plus, e.g., `(1, −3, 5, −7, ...)` or `(−1, 3, −5, 7, ...)`.
- **Monotonically increasing**: `S_n ≤ S_{n+1}` ∀ `n ∈ N`. ⭐
- **Strictly monotonically increasing**: `S_n < S_{n+1}` ∀ `n ∈ N`. ⭐
- **Monotonically decreasing**: `S_{n+1} ≤ S_n` ∀ `n ∈ N`. ⭐
- **Strictly monotonically decreasing**: `S_{n+1} < S_n` ∀ `n ∈ N`. ⭐
- **Monotonic**: monotonically increasing OR monotonically decreasing. ⭐
- **Alternating sequence**: terms alternate in sign.
- (i) `(1, 3, 5, 7, ...)` — strictly monotonically increasing.
- (ii) `(−1, −3, −5, −7, ...)` — strictly monotonically decreasing.
- (iii) `(1, 1/3, 1/5, 1/7, ...)` — strictly monotonically decreasing.
- (iv) `(−1, −1/3, −1/5, −1/7, ...)` — strictly monotonically increasing.
- (v) `(−1, 1, −3, 3, −5, 5, ...)` — neither monotonically increasing nor decreasing.

**Bounded vs Monotonic — independence**
- (i) A bounded sequence may not be monotonic, e.g., `(1, 2, 1, 2, ...)`.
- (ii) A monotonic sequence may not be bounded, e.g., `(1, 2, 3, ...)`.
- (iii) But there are sequences which are both, e.g., `(1 + 1/n)`, `n ∈ N`, is bounded (above by 2, below by 1) and monotonic.

### ⚠️ Common Mistakes
- ❌ Treating "alternating" as a kind of monotonic → ✅ Alternating sequences are explicitly *not* monotonic in general.
- ❌ Equating boundedness with monotonicity → ✅ The two are independent properties.
- Builds on: Bounded sequence (above).
- Continues into: Convergence (next).

### 13.3.3 Convergent / Divergent / Oscillatory Sequences 🔴

**Formalising "closer and closer" (the ε–`n_ε` machinery)**
1. "Terms `S_n` get as close to `l` as we wish" → "let `ε > 0` be as small as we like, so that `|S_n − l| ≤ ε`".
2. "Except for some initial terms" → "for all `n > n_ε`", where `n_ε` indicates we may set aside `n_ε` initial terms. Smaller `ε` → larger `n_ε` (the closer you want to be to the limit, the more early terms you may need to discard).

**Convergent Sequence — formal definition**

**Uniqueness of limit**

**Cauchy Sequence**

**Non-convergent sequences — four categories**
1. **Finitely oscillatory**: `(S_n)` is bounded but not convergent.
   - Examples: `((−1)^n) = (−1, 1, −1, 1, ...)`; `(1 + (−1)^n) = (0, 2, 0, 2, ...)`.
2. **Divergent to +∞**: for every real `Δ` (delta), howsoever large and positive, ∃ `n_Δ` such that `S_n > Δ` for all `n > n_Δ`. (Successive terms become unboundedly large.)
3. **Divergent to −∞**: for every real `Δ` > 0, ∃ `n_Δ` such that `S_n < (−Δ)` for all `n > n_Δ`. (Successive terms become unboundedly large in magnitude with negative sign.)
4. **Infinitely oscillatory**: unbounded, and diverges neither to +∞ nor to −∞.

**Limit Point of a sequence**
- For a convergent sequence, its limit is also a limit point (the sequence is its own subsequence).
- A limit point need not be a limit. E.g., `((−1)^n) = (−1, 1, −1, 1, ...)` has two limit points (1 and −1) but no limit (it isn't convergent).

**Bolzano-Weierstrass Theorem for sequences**
- **Convergent sequence**: ∃ real `l` such that ∀ `ε > 0`, ∃ `n_ε ∈ N` with `|S_n − l| < ε` for all `n > n_ε`. ⭐
- **Limit of a sequence**: the unique `l` in the convergence definition; written `lim_{n→∞} S_n = l`. ⭐
- **Cauchy sequence**: ∀ `ε > 0`, ∃ `n_ε ∈ N` with `|S_n − S_m| < ε` for all `n, m > n_ε`. ⭐
- **Finitely oscillatory**: bounded but non-convergent. ⭐
- **Divergent to +∞**: ∀ `Δ > 0`, ∃ `n_Δ` with `S_n > Δ` for all `n > n_Δ`. ⭐
- **Divergent to −∞**: ∀ `Δ > 0`, ∃ `n_Δ` with `S_n < −Δ` for all `n > n_Δ`. ⭐
- **Infinitely oscillatory**: unbounded; not divergent to ±∞. ⭐
- **Limit point of a sequence**: real number to which some subsequence converges. ⭐
- (a) `(S_n) = (2n − 1) = (1, 3, 5, ...)`.
- (b) `(S_n) = (a r^n)` with `r > 1`, `a > 0` (a G.P. with ratio > 1 and positive scale factor).
- (a) `(S_n) = (1 − 2n) = (−1, −3, −5, ...)`.
- (b) `(S_n) = (a r^n)` with `r > 1`, `a < 0`.
- (a) `(S_n) = ((−1)^n · n²) = (−1, 4, −9, 16, −25, ...)` (source writes it as `(−1, 5, −5, 9, ...)` due to OCR; intent is alternating-sign powers).
- (b) `(S_n) = (a · (−r)^n)` with `r > 1`, `a > 0` — the subsequence `(−ar, −ar³, −ar⁵, ...)` tends to −∞ while the subsequence `(ar², ar⁴, ar⁶, ...)` tends to +∞.
- `S_n = [√(n+1) − √n] · [√(n+1) + √n] / [√(n+1) + √n]`
- `   = [(n+1) − n] / [√(n+1) + √n]`
- `   = 1 / [√(n+1) + √n]`
- `   < 1 / [√n + √n] = 1 / (2√n)` (denominator decreases ⇒ value increases).
- `(n² + 5n − 7)/(3n² + 12n + 14) − 1/3`
- `= [3(n² + 5n − 7) − (3n² + 12n + 14)] / [3(3n² + 12n + 14)]`
- `= (3n − 35) / [3(3n² + 12n + 14)] < 3n / [3(3n² + 12n + 14)] < 3n / (9n²) = 1/(3n) < 1/n`.

### ⚠️ Common Mistakes
- ❌ Saying "limit point" and "limit" are the same → ✅ Every limit is a limit point, but a sequence may have many limit points and yet have no limit (it's then non-convergent).
- ❌ Forgetting `n_ε` depends on `ε` → ✅ Smaller `ε` typically requires larger `n_ε`.
- ❌ Using a single `n` to verify convergence → ✅ Must show "for all `n > n_ε`".
- A bounded non-convergent sequence is **finitely oscillatory** (by definition).
- The Bolzano-Weierstrass corollary only guarantees a *convergent subsequence* — the original sequence itself need not converge.

**Quick Recall:**
- Convergence: ∀ `ε > 0` ∃ `n_ε`: `|S_n − l| < ε` ∀ `n > n_ε`.
- Cauchy: ∀ `ε > 0` ∃ `n_ε`: `|S_n − S_m| < ε` ∀ `n, m > n_ε`.
- Convergent ⇔ Cauchy.
- Limit (if exists) is unique.
- Bolzano-Weierstrass (sequences): every bounded sequence has a limit point ⇒ has a convergent subsequence.
- Builds on: Bounded sequences, monotone sequences (this chunk).
- Continues into: Bolzano-Weierstrass for sets and economic applications (Chunk 004).

### 13.4.1 Open Set, Closed Set, Bounded Set, Compact Set 🔴
- **Open**: every member has a small open interval around it that is contained in the set ⇒ no member is a boundary point.
- **Closed**: complement (in R) is open.
- **Bounded**: set is sandwiched between two real numbers (one upper bound, one lower bound).
- **Compact**: closed AND bounded.
- **Open set**: A set `S ⊆ R` is **open** if for each `a ∈ S`, ∃ `ε > 0` such that the open interval `]a − ε, a + ε[ ⊆ S`. Equivalently, every member of `S` is well inside `S` and no member is a boundary point. ⭐
- **Closed set**: A set `S ⊆ R` is **closed** if `R − S = (−∞, +∞) − S` is open. ⭐
- **Bounded set**: `S` is **bounded** if it is both bounded above (∃ real `M`: `x ≤ M` ∀ `x ∈ S`) and bounded below (∃ real `M'`: `M' ≤ x` ∀ `x ∈ S`). ⭐
- **Compact set**: A subset of R is **compact** if it is both closed and bounded. ⭐
- (i) `[3, 10^{10}]` — bounds 3 (lower) and `10^{11}` (one upper bound, among others).
- (ii) `[−10^{10}, 1000]` — bounds −10^{10} and 1000.
- (iii) `{1, 2, 10, 10000} ∪ [−10^{10}, 1000]` — bounds −10^{10} and 10000.
- (i) `(−∞, 10)` — bounded above (e.g., by 10) but not below.
- (ii) `(100, ∞)` — bounded below (by 100) but not above.

**Only ∅ and R are both open and closed**

**Compact = Closed + Bounded**

### ⚠️ Common Mistakes
- ❌ Treating "not open" as equivalent to "closed" → ✅ Many sets are neither open nor closed (e.g., the half-open interval `[a, b[`); the only sets that are both are `∅` and `R`.
- ❌ Saying every bounded set is compact → ✅ Need *closed* AND bounded (e.g., `(0, 1)` is bounded but not closed, hence not compact).

**Quick Recall:**
- Open: every point has an ε-ball inside the set.
- Closed: complement is open.
- Bounded: fits between two reals.
- Compact: closed AND bounded.
- Both open and closed: only `∅` and `R`.
- Builds on: Bounded sequence (Chunk 003 — same idea, generalised).
- Continues into: Bolzano-Weierstrass for sets (next).

### 13.4.2 Bolzano-Weierstrass Theorem for Sets & Economic Applications 🔴

**Bolzano-Weierstrass for sets**

**Equivalent characterisation**

**Synonyms for "limit point of a set"**

**Economic application — Pareto-efficient allocation**
- **Limit point of a set `S`**: a real number `p` such that for every `ε > 0`, the open interval `]p − ε, p + ε[` contains a point of `S` different from `p`. Equivalently: contains infinitely many points of `S`. Also called accumulation / condensation / cluster point. ⭐
- Source theorem assumes **infinite** AND bounded — a finite bounded set has no limit point (e.g., `{1, 2, 3, 4}` has none).
- `N = {1, 2, 3, ...}` is infinite but unbounded, so the theorem doesn't apply — and indeed, N has no limit points.

**Quick Recall:**
- Bolzano-Weierstrass (sets): infinite + bounded ⇒ has a limit point.
- Limit point ↔ accumulation / cluster / condensation point.
- Used in economics to prove existence of Pareto-efficient allocations.
- Builds on: Limit point of a sequence (Chunk 003); compact sets (this chunk).
- Continues into: Section 13.5 — Analysis of Several Variables.

### 13.5.2 R^n and Euclidean Space 🔴
- **R^n**: `R^n = {(a_1, a_2, ..., a_n) : a_i ∈ R}`. Elements are called **n-tuples**. ⭐
- **Vector addition**: For `x = (x_1, ..., x_n)`, `y = (y_1, ..., y_n)`: `x + y = (x_1 + y_1, x_2 + y_2, ..., x_n + y_n)`. ... (13.3) ⭐
- **Scalar multiplication**: For `r ∈ R`, `r·x = (r x_1, r x_2, ..., r x_n)`. ... (13.4) ⭐
- **Zero vector**: `0 = (0, 0, ..., 0)`.
- **Additive inverse**: `−x = (−x_1, −x_2, ..., −x_n)`.
- **Euclidean distance**: `d(x, y) = √[(x_1 − y_1)² + (x_2 − y_2)² + ... + (x_n − y_n)²]`. ... (13.5) ⭐
- **Euclidean norm**: `||x|| = √[(x_1)² + (x_2)² + ... + (x_n)²] = d(x, 0)`. ... (13.6) ⭐

**From R² to R^n**

**Norm and distance are linked**

**Quick Recall:**
- `R^n = {(a_1, ..., a_n) : a_i ∈ R}`.
- `d(x, y) = √Σ (x_i − y_i)²`.
- `||x|| = √Σ x_i² = d(x, 0)`.
- `||x − y|| = d(x, y)`.
- Builds on: Cross product of two sets (Block 1, Unit 3).
- Continues into: 13.5.3 Functions over Euclidean spaces.

### 13.5.3 Functions over Euclidean Spaces 🔴
- **Vector addition function** `+: R^n × R^n → R^n`: `+((x_1, ..., x_n), (y_1, ..., y_n)) = (x_1 + y_1, ..., x_n + y_n)`. ... (13.8)
- **Scalar multiplication function** `·: R × R^n → R^n`: `r · (x_1, ..., x_n) = (r x_1, ..., r x_n)`. ... (13.9)
- **Distance function** `d: R^n × R^n → R`: `d(x, y) = √Σ (x_i − y_i)²`. ... (13.10)
- **Norm function** `||·||: R^n → R`: `||x|| = √Σ x_i²`. ... (13.11)
- **Scalar (dot) product function** `Scalar: R^n × R^n → R`: `Scalar((x_1, ..., x_n), (y_1, ..., y_n)) = x_1 y_1 + x_2 y_2 + ... + x_n y_n`. ⭐
- **Projection function** `R^k → R^m` (for `m < k`): drops some coordinates. E.g., `R_{1,2,3}: R^4 → R^3` with `R_{1,2,3}(x_1, x_2, x_3, x_4) = (x_1, x_2, x_3)`; `R_{2,3,4}(x_1, x_2, x_3, x_4) = (x_2, x_3, x_4)`; `R_{1,2}: R^5 → R^2`; `R_{3,5}(x_1, x_2, x_3, x_4, x_5) = (x_3, x_5)`.
- `||x|| = √[2² + (−1)² + (−3)² + 4² + (−2)²] = √[4 + 1 + 9 + 16 + 4] = √34`.
- `||y|| = √[3² + (−1)² + (−3)² + 2² + (−3)²] = √[9 + 1 + 9 + 4 + 9] = √32`.
- `d(x, y) = √[(2−3)² + (−1−(−1))² + (−3−(−3))² + (4−2)² + (−2−(−3))²]`
- `= √[1 + 0 + 0 + 4 + 1] = √6`.
- `x · y = (2)(3) + (−1)(−1) + (−3)(−3) + (4)(2) + (−2)(−3) = 6 + 1 + 9 + 8 + 6 = 30`.
- Builds on: 13.5.2 R^n and Euclidean Space.
- Continues into: 13.5.4 Concepts of Analysis in R^n.

### 13.5.4 Concepts of Analysis in R^n — Open Disc, Closed Disc, etc. 🔴
- A **sequence in R^n** has elements `s_i ∈ R^n`, i.e., each `s_i = (s_{i1}, s_{i2}, ..., s_{in})` with `s_{ij} ∈ R`.
- For limits, continuity, derivability: replace single real `x` with vector `x ∈ R^n`; replace `|x|` (absolute value) with `||x||` (norm); replace `|x − a|` (distance) with `d(x, a) = ||x − a||` (Euclidean distance).
- The notion of a "small open interval" `]a − ε, a + ε[` around a point becomes an **open disc** of radius ε.

**Open / closed disc**
- **Open Rectangle in R²**: `{(x_1, x_2) : a_1 < x_1 < b_1 and a_2 < x_2 < b_2}` with `a_i < b_i`. (Generalises to a "boundaryless cuboid" in `R^n`.)
- **Open Rectangle in R^n**: `{x = (x_1, ..., x_n) : a_i < x_i < b_i, i = 1, ..., n}` for fixed `a, b ∈ R^n`.
- **Open Disc of radius ε centered at `a`** in R^n: `{x = (x_1, ..., x_n) : ||x − a|| < ε}` for `ε > 0`. A "boundaryless sphere" in n-dimensional hyper-space. ⭐
- **Closed Disc of radius ε centered at `a`**: `{x ∈ R^n : ||x − a|| ≤ ε}`. Includes boundary points. ⭐

**Open, closed, bounded, compact sets in R^n**
- **Open set in R^n**: `S ⊆ R^n` is open if for each `a ∈ S`, ∃ an open disc of some radius `ε > 0` centered at `a` contained in `S`. Every member of `S` is well inside `S`. ⭐
- **Closed set in R^n**: `S ⊆ R^n` is closed if `R^n − S` is open. ⭐
- **Bounded subset of R^n**: `S` is bounded if it is bounded above and bounded below componentwise — i.e., ∃ reals `M, M'` such that `M' ≤ x_i ≤ M` for all `x = (x_1, ..., x_n) ∈ S` and for `1 ≤ i ≤ n`. ⭐
- **Compact set in R^n**: closed AND bounded. ⭐
- **Limit point of a subset of R^n**: `p = (p_1, ..., p_n) ∈ R^n` is a limit point of `S ⊆ R^n` if every open disc of radius `ε > 0` around `p` contains a point of `S` different from `p`. Also called accumulation / condensation / cluster point. ⭐

**Limit and continuity for `f: R^n → R` (real-valued)**
- **Limit:** `lim_{x → a} f(x)` exists and equals real number `l` iff for every `ε > 0`, ∃ `δ > 0` such that whenever `||x − a|| < δ`, then `|f(x) − l| < ε`.
- **Continuity at `a`:** `f` is continuous at `x = a` if (i) `lim_{x → a} f(x)` exists, AND (ii) `lim_{x → a} f(x) = f(a)`.

**Open disc replaces interval, norm replaces absolute value**

**Quick Recall:**
- Open disc: `{x : ||x − a|| < ε}`.
- Open set in R^n: every point has an open disc inside the set.
- Compact in R^n: closed + bounded.
- Limit `f: R^n → R`: ∀ε ∃δ such that `||x − a|| < δ ⇒ |f(x) − l| < ε`.
- Builds on: Open / closed / bounded / compact in R (Section 13.4.1, this chunk); norm and distance (13.5.2).
- Continues into: Limit / continuity for `f: R^n → R^m`, Extreme Value Theorem (Chunk 005).

### 13.5.4(C) Limit and Continuity of `f: R^n → R^m` 🔴
- **Limit of `f: D → R^m`** (with `D ⊆ R^n`, `a ∈ R^n`): `lim_{x → a} f(x)` exists and equals `l ∈ R^m` iff for every `ε > 0`, ∃ `δ > 0` such that whenever `||x − a|| < δ`, then `||f(x) − l|| < ε`.
- *(Note: both `f(x)` and `l` are now members of `R^m`, not real numbers.)* ⭐
- **Continuity of `f: D → R^m` at `a ∈ R^n`**: `f` is continuous at `x = a` if (i) `lim_{x → a} f(x)` exists, AND (ii) `lim_{x → a} f(x) = f(a)`. ⭐

**What changes between `f: R^n → R` and `f: R^n → R^m`**
| Object | `f: R^n → R` | `f: R^n → R^m` |
|---|---|---|
| Input distance | `||x − a||` (norm in R^n) | `||x − a||` (norm in R^n) |
| Output distance | `|f(x) − l|` (absolute value in R) | `||f(x) − l||` (norm in R^m) |
| `l` lives in | `R` | `R^m` |

**Quick Recall:**
- Limit definition is the same ε-δ shape; only the type of `||·||` on the output side changes.
- Builds on: Limit / continuity for `f: R^n → R` (Chunk 004).
- Continues into: Extreme Value Theorem (next).

### 13.5.4(D) Extreme Value Theorem 🔴
- **Local Minima**: a value that `z = f(x)` attains at some point `p` such that for some `ε > 0`, `f(x) ≥ f(p)` for all `x ∈ ]p − ε, p + ε[ ⊆ S`. The value `f(p)` is the local minimum (a local minima is a *value*, not a point — `p` is the *point of* local minima). ⭐
- **Local Maxima**: a value that `z = f(x)` attains at some point `p` such that for some `ε > 0`, `f(x) ≤ f(p)` for all `x ∈ ]p − ε, p + ε[ ⊆ S`. (Same point/value distinction.) ⭐
- **Local Extremum (plural: extrema)**: a local minimum or a local maximum. ⭐
- **Global / Absolute Minimum**: a value `m` of `f(x)` over `S` such that `m ≤ f(x)` for all `x ∈ S`. (The term "minima" is generally not used here.) ⭐
- **Global / Absolute Maximum**: a value `M` of `f(x)` over `S` such that `f(x) ≤ M` for all `x ∈ S`. ⭐
- **Local Minima**: value `f(p)` at some `p ∈ R^n` such that for some `ε > 0`, `f(x) ≥ f(p)` for all `x ∈ ` open disc centered at `p` of radius `ε`, contained in `S`. ⭐
- **Local Maxima**: value `f(p)` at some `p ∈ R^n` such that for some `ε > 0`, `f(x) ≤ f(p)` for all `x ∈ ` open disc centered at `p` of radius `ε`, contained in `S`. ⭐
- **Global / Absolute Minimum**: a value `m` of `f(x)` over `S ⊆ R^n` such that `m ≤ f(x)` for all `x ∈ S`. ⭐
- **Global / Absolute Maximum**: a value `M` of `f(x)` over `S ⊆ R^n` such that `f(x) ≤ M` for all `x ∈ S`. ⭐

**"Local" = immediate neighbourhood**

**Point vs. Value**

**Extreme Value Theorem (single variable)**

**Extreme Value Theorem (several variables)**

**Global extremum on a boundary need not be local**

### ⚠️ Common Mistakes
- ❌ Calling the *point* `p` "a local minima" → ✅ The *value* `f(p)` is the local minima; `p` is the point at which it is attained.
- ❌ Assuming continuity alone implies an absolute max/min → ✅ EVT also requires the domain to be a closed interval (in R) or closed disc (in R^n) — i.e., compact.
- ❌ Assuming a global extremum is always a local one → ✅ Boundary global extrema may fail to be local.
- The single-variable EVT requires `f` continuous on a *closed* interval. Open intervals don't suffice (e.g., `f(x) = 1/x` on `(0, 1)` has no maximum).

**Quick Recall:**
- Local minima = *value* `f(p)` smallest in some open neighbourhood; `p` is the point of attainment.
- EVT (1-variable): continuous on `[a, b]` ⇒ attains absolute max and min.
- EVT (n-variable): continuous on closed disc `D` ⇒ attains absolute max and min.
- Builds on: Continuity in R^n; closed disc; bounded set (Chunk 004).
- Continues into: Optimization (Block 5, Units 16-19).

### 13.10 Exercises and Answers (Q1-Q4) 🔴
- (i) is not bounded above if `d > 0`,
- (ii) is not bounded below if `d < 0`.
- (i) not bounded above if `r > 1`, `a > 0`,
- (ii) not bounded below if `r > 1`, `a < 0`,
- (iii) bounded neither above nor below if `r < −1`.
- (A) By Archimedean Property for `a·ε > 0`, ∃ natural `n` with `n·(a·ε) > M`.
- (B) `a·r^n = a·(1 + ε)^n = a·(1 + nε + ...) > a·n·ε` (binomial expansion; remaining terms are positive).
- From (A) and (B), ∃ `n` with `a·r^n > M`. Hence the G.P. with `r > 1` is not bounded above. ∎
- `(a · r^{2k})` (even indices): putting `R_1 = r² > 0`, this is the sequence `(a · R_1^k)`. Since `R_1 > 1` and `a > 0` (WLOG), this is unbounded above by part (i).
- `(a · r^{2k+1})` (odd indices): putting `R_2 = r² > 0` and `A_1 = a·r < 0` (since `a > 0`, `r < 0`), this becomes `(A_1 · R_2^{k})`. Since `R_2 > 1` and `A_1 < 0`, this is unbounded below by part (ii).

**Quick Recall:**
- A.P. recursive: `t_n = t_{n−1} + d`.
- A.P. unbounded above (d > 0) / below (d < 0); use Archimedean Property in proofs.
- G.P. with `r > 1`: unbounded above if `a > 0`, unbounded below if `a < 0`; if `r < −1`, unbounded both ways.
- Fibonacci: unbounded above; bounded below by 0.
- Builds on: Boundedness results stated informally in 13.3.1 (Chunk 003); Archimedean Property used implicitly in 13.3.3 (Example 13.14).
- Continues into: Unit 14 (Calculus of Several Variables).

### 14.2 The Concept of 'Limit' [🔴]

**Why limits are defined**

**Single-variable: two directions only**
- Case (i): `lim_{x→0} 1/x²` — both `1/(+ε)²` and `1/(−ε)²` blow up to `+∞`, agree → limit `= +∞`.
- Case (ii): `lim_{x→0} 1/x` — RHS goes to `+∞`, LHS goes to `−∞`, disagree → limit does not exist.

**Two-variable case: infinitely many directions**
- **Limit (multivariable, intuitive)**: a value consistent with values at all neighbouring points along every direction of approach. ⭐
- **Notation**: `lim_{(x,y)→(a,b)} f(x,y)` (preferred) or `lim_{x→a, y→b} f(x,y)`.
- Builds on: Unit 9 (Functions, Limits, Continuity, Block 3) and partial derivative limit definitions from Unit 11.
- Continues into: Computing limits (14.3) and limit-based derivatives (14.4).

### 14.3 Computing Limit for Functions of Two or More Variables [🔴]

**Continuity shortcut**

**Problematic conditions**

**Removable problematic condition**

**Path-testing for non-existence**
1. Check continuity (continuous → plug in).
2. If discontinuous, look for removable problematic conditions (factor and cancel).
3. If non-removable, test paths (`x=0`, `y=0`, `x=y`, etc.) — disagreement proves non-existence.
- Path `x=0`: limit `= 0/y² = 0`. (14.1)
- Path `y=0`: limit `= 0/(3x²) = 0`. (14.2)
- Path `x=y`: `x·x/(3x²+x²) = 1/4`. (14.3)

### ⚠️ Common Mistakes
- ❌ Concluding the limit exists because two paths agree → ✅ Two-path agreement is necessary, not sufficient. Always try a non-trivial path (like `x=y` or `y=x²`) to attempt to break agreement.
- ❌ Plugging in directly when the denominator is zero → ✅ First check whether the singular factor can be cancelled.
- Only the **value at the point itself is excluded** when computing the limit, so cancelling factors zero on the limit line/locus is legitimate.
- Continuity in each variable separately does not by itself guarantee continuity as a function of two variables; use the third bullet rule (continuous when one variable held constant **or** when `x=y`).

**Quick Recall:**
- Continuous → plug in.
- Removable problematic condition → cancel and plug in.
- Two paths disagree → limit DNE.
- Two paths agree → inconclusive; try more.
- Builds on: Section 14.2 (Chunk 006) Concept of Limit.
- Continues into: Section 14.4 Partial Derivatives (Chunk 007), where partial derivatives are themselves one-variable limits.
1. Are there algorithmic / non-path-based criteria for proving existence of multivariable limits (e.g. polar-coordinate squeeze)? (Not covered here.)

### 14.4.1 Partial Derivative of Function with Explicit Representation [🔴]
- **Partial derivative `f_x`**: `lim_{h→0} [f(x+h, y) − f(x, y)] / h`. ⭐
- **Partial derivative `f_y`**: `lim_{h→0} [f(x, y+h) − f(x, y)] / h`. ⭐
- **Alternative notations for `f_x`**: `∂f/∂x`, `∂U/∂x`, `D_x f`, `D_x f(x, y)`.
- `g_x(x, y) = ∂g/∂x = 5y⁴ · (3x²) = 15 y⁴ x²`
- `g_y(x, y) = (5x³)(4y³) = 20 x³ y³`
- `∂v/∂x = 2x cos(y)/w`
- `∂v/∂y = (x²/w)(−sin(y)) = −(x² sin(y)/w)`
- `∂v/∂w = x² cos(y) · (−w⁻²) = −2 x² cos(y)/w³` *(source has minor OCR ambiguity but states "= −2 {x² cos(y)/w³}")*
- Builds on: Section 14.2 limit concept.
- Continues into: implicit (14.4.2), composite (14.4.3), higher-order (14.4.4) cases.

### ⚠️ Common Mistakes
- ❌ Forgetting product rule on terms like `x⁴ z²` when differentiating w.r.t. `x` (since `z` depends on `x`) → ✅ Use `(4x³)z² + x⁴(2z)(∂z/∂x)`.

### 14.4.3 Chain Rule & Composite Functions [🔴]

**14.4.3.1 Chain rule for single independent variable**

**14.4.3.2 Chain rule for partial derivatives**

### ⚠️ Common Mistakes
- ❌ Treating `dy/dx` as a fraction and "cancelling" `dz` with `dz` → ✅ The chain rule is a proved theorem; the notation is suggestive but not algebraic.
- Builds on: 14.4.1 explicit derivatives.
- Continues into: total differentials (14.4.6) and Taylor multivariate (Chunk 009).

### 14.4.4 Higher Order Partial Derivatives [🔴]
- **Second-order partial `f_{xx}`**: `∂²f/∂x² = ∂/∂x (∂f/∂x)`. ⭐
- **Mixed partial `f_{xy}`**: `∂/∂y(∂f/∂x) = ∂²f/(∂y ∂x)`. ⭐
1. Compute first-order partial `f_x`.
2. Treat it as a new function and partial-differentiate w.r.t. `x` or `y`.
3. Continue for third- and higher-order derivatives.
- `f_x = 15 y⁴ x²`, `f_y = 20 x³ y³`
- `z_{xx} = ∂²f/∂x² = 30 y⁴ x`
- `z_{xy} = ∂²f/(∂y ∂x) = 60 y³ x²`
- The text remarks that first-order partials always have explicit form regardless of how the original function was given (explicit/implicit/composite). So the method for higher-order derivatives is the **explicit-case method** of 14.4.1.
- Continues into: Hessian (14.6.3, Chunk 008), Taylor's theorem (14.8, Chunks 008–009).

### 14.4.6 Differential / Total Differential [🔴]
- **Total differential of `z = f(x, y)`**: `dz = f_x dx + f_y dy` (equivalently `df = f_x dx + f_y dy`). ⭐
- **Total differential of `w = h(x, y, z)`**: `dw = h_x dx + h_y dy + h_z dz`. ⭐

**Quick Recall:**
- 1 variable: `dy = f'(x) dx`
- 2 variables: `dz = f_x dx + f_y dy`
- 3 variables: `dw = h_x dx + h_y dy + h_z dz`
- Plays significant role in Integral Calculus and Differential Equations (per text).
- Builds on: 14.4.1.

### 14.5 Directional Derivatives (start) [🔴]
- **Directional derivative (formal)**: `D_A f(x, y) = lim_{|A|→0} [f(x + |A| cos θ, y + |A| sin θ) − f(x, y)] / |A|`. ⭐
- **Gradient `∇f`**: the vector `⟨f_x, f_y⟩`. ⭐
- **Formula (differentiable f)**: `D_Â f(x, y) = f_x cos θ + f_y sin θ = ⟨f_x, f_y⟩ · ⟨cos θ, cos(π/2 − θ)⟩ = ∇f · Â`. ⭐
- `Û = ⟨cos(2π/3), sin(2π/3)⟩ = ⟨−½, (√3)/2⟩`.
- `D_Û f(x, y) = −½ f_x + (√3/2) f_y`
- At `(0, 2)`: `D_Û f(0, 2) = −½ · 0 + (√3/2)(0 + 12) = 6√3`.
- Builds on: partial derivatives (14.4) and inner product (Section 6.4 of Unit 6).
- Continues into: 3-variable directional derivatives, Jacobian, Hessian (Chunk 008).
1. Why `cos(π/2 − θ)` for the second component of the unit vector — i.e. how is the same formula generalized to `n` axes via direction cosines? (Addressed in Chunk 008.)

### 14.5 Directional Derivatives (continued — three variables) [🔴]
- **Direction cosines**: `(cos α, cos β, cos γ)` — the angles a unit vector makes with the `x`, `y`, `z` axes. ⭐
- **Directional derivative (3 variables)**: `D_û f = f_x cos α + f_y cos β + f_z cos γ`. ⭐
1. Compute `‖V‖`.
2. Form unit vector `û = V/‖V‖`.
3. Compute partials `f_x, f_y, f_z`.
4. Take dot product `∇f · û`.
- `‖V‖ = √((−1)² + 0² + 3²) = √10`.
- `û = ⟨−1/√10, 0, 3/√10⟩`.
- `D_û f(x, y, z) = (−1/√10) f_x + 0 · f_y + (3/√10) f_z = (−1/√10){2z² − 2xyz} + (3/√10){4xz + 6yz − x²y}` *(per source)*.
- Builds on: 14.5 (Chunk 007) — 2-variable directional derivative.
- Continues into: Jacobian (14.6) — generalizes the gradient row-vector to a matrix.

### 14.6 Explicit Function from R^n to R^m, Jacobian Matrix, Hessian [🔴]

**14.6.1 Function from R^n to R^m**

**14.6.2 Jacobian / Jacobian matrix**

**Jacobian determinant**

**14.6.3 Hessian**
- **Jacobian of `f: R^n → R^m`**: the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`, `i = 1,…,m`, `j = 1,…,n`. ⭐
- **Jacobian determinant**: when `n = m`, the determinant `det(J_f)`; useful in multiple integrals. ⭐
- **Hessian of `f: R^n → R`**: the `n × n` matrix of second partials, `H_f[i,j] = ∂²f/(∂x_i ∂x_j)`. ⭐
- `f_1(x, y) = e^{xy²}`, `f_2(x, y) = 2x² + 3y²`.
- `J_f = [[ y² e^{xy²},  2xy e^{xy²} ], [ 4x, 6y ]]`. *(per source: ∂f₁/∂x = y²e^{xy²}; ∂f₁/∂y = 2xy e^{xy²}; ∂f₂/∂x = 4x; ∂f₂/∂y = 6y)*
- At `(2, 1)`: `J_f(2, 1) = [[ e², 4e² ], [ 8, 6 ]]`. *(per source: 2e⁴ in first row, but transcript shows `[2e^4 4e^4 / 8 6]` — keep per source)*
- First partials: `∂f/∂x = y² e^{xy²}`, `∂f/∂y = 2xy e^{xy²}`.
- Second partials:
  - `∂²f/∂x² = y⁴ e^{xy²}`
  - `∂²f/(∂x ∂y) = (2y + 4xy³) e^{xy²} = 2y(1 + 2xy²) e^{xy²}` (source written as `(2 + 4xy) e^{xy²}` after simplification of OCR: rendered as `(2 + 4xy)`)
  - `∂²f/∂y² = (2x + 4x²y²) e^{xy²} = 4x²·… e^{xy²}` (per source `4x²·e^{xy²}` plus mixed term)
- `H_f(2, 1)` per source `= [[ 4e², 10e² ], [ 10e², 16 e² ]]`.
- Builds on: gradient (14.5).
- Continues into: Hessian's role in second-order Taylor expansion (Chunk 009) and in optimization (Unit 15).

### 14.7 Mean Value Theorem [🔴]

**History**

**14.7.1 MVT for single variable**

**14.7.2 MVT for several variables (optional reading)**
- **Mean Value Theorem (single variable)**: continuous on `[a, b]`, differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`. ⭐
- **MVT (several variables)**: differentiable on open `G ⊆ R^n`; for `x, y ∈ G`, `∃ c ∈ (0,1)`: `f(y) − f(x) = ∇f((1 − c)x + c y) · (y − x)`. ⭐
- Polynomial → continuous and differentiable everywhere → MVT applies.
- `f'(y) = 4y + 3`; at the MVT point `c`: `4c + 3 = (f(2) − f(1))/(2 − 1) = (18 − 9)/1 = 9`.
- `4c = 6` ⇒ `c = 3/2 ∈ (1, 2)`. ✓

### ⚠️ Common Mistakes
- ❌ Applying MVT to a function with a discontinuity in `[a, b]` → ✅ Continuity on closed interval is required.
- Continues into: Taylor's theorem (14.8) — Lagrange-form remainder uses MVT.
- Used in Exercises 7 & 8 (Chunk 010): `f' ≡ 0 ⇒ f` constant; `f' > 0 ⇒ f` strictly increasing.

### 14.8 Polynomial Approximation: Taylor's Theorem, Linear & Quadratic Approximations [🔴]

**Why polynomials?**

**14.8.1 Taylor's polynomial of order `k`**

**Forms of the remainder (mentioned, may be skipped)**
- **Peano's form**: `R_{k,a}(x) = h_{k,a}(x)·(x − a)^k`, with `lim_{x → a} h_{k,a}(x) = 0`.
- **Lagrange mean-value form**: `R_k(x) = (f^{(k+1)}(c)/(k+1)!)·(x − a)^{k+1}` for some `c` between `a` and `x`.
- **Cauchy's form**: `R_k(x) = (f^{(k+1)}(c)/k!)·(x − c)^k(x − a)`.

**14.8.2 Taylor's theorem (statement, no proof)**

**14.8.3 Taylor's series / expansion**
- **Taylor polynomial `P_{k, a}`**: `Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j`. ⭐
- **Taylor's formula**: `f(x) = P_{k,a}(x) + R_{k,a}(x)`. ⭐
- **Remainder term `R_{k,a}(x)`**: error of polynomial approximation; depends on `k`, `a`, `f`. ⭐
- **Taylor's series**: infinite version of Taylor's polynomial when `f` has all derivatives at `a` and `R_k → 0`. ⭐

**Quick Recall:**
- `P_{k,a}(x) = Σ_{j=0}^k f^{(j)}(a)·(x − a)^j / j!`
- `f(x) = P_{k,a}(x) + R_{k,a}(x)`
- For nice `f`, `R_{k,a}(x) → 0` as `x → a`.
- Builds on: MVT (14.7) — supplies the Lagrange remainder.
- Continues into: Maclaurin series (14.8.4), linear/quadratic approximation (14.8.5), and multivariate Taylor (14.9) — all in Chunk 009.
1. The remainder forms (Peano, Lagrange, Cauchy) are stated but not used; under what conditions is each preferred? (Beyond scope of the unit.)

### 14.8.4 Maclaurin's Series [🔴]
- **Maclaurin series**: Taylor's series with expansion point `a = 0`. ⭐
- Special case of: Taylor's series (14.8.3, Chunk 008).

### 14.8.5 Linear / Quadratic Approximation [🔴]
- **Linear approximation `P_{1, a}`**: `f(a) + f'(a)(x − a)`. (14.15) ⭐
- **Quadratic approximation `P_{2, a}`**: `f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)²`. (14.17) ⭐
- **Taylor's formula (linear)**: `f(x) = P_{1,a} + R_1(x, a)`, with `lim_{x→a} R_1 = 0`. (14.16)
- **Taylor's formula (quadratic)**: `f(x) = P_{2,a} + R_2(x, a)`, with `lim_{x→a} R_2 = 0`. (14.18)
1. Compute `f(a)`.
2. Compute `f'(a)` (and `f''(a)` for quadratic).
3. Plug into the polynomial template.
4. Error of approximation is `R_k(x)`.

### ⚠️ Common Mistakes
- ❌ Forgetting that the quadratic approximation includes the linear part → ✅ `P_{2,a} = P_{1,a} + (f''(a)/2!)(x − a)²`.

**Quick Recall:**
- `sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + …`
- `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + …` (derived in Chunk 010 CYP4 Q3)
- `log(x)` around `x = 1`: `(x − 1) − (x − 1)²/2 + (x − 1)³/3 − …` (Chunk 010 CYP4 Q4)
- Builds on: 14.8.1–14.8.3 (Chunk 008).
- Continues into: multivariate linear/quadratic approximation (14.9.1, 14.9.2).

### 14.9 Multivariate Polynomial Approximation: Taylor's Theorem, Linear Approximation [🔴]

**14.9.1 Linear approximation in two variables (order 1)**

**14.9.2 Quadratic approximation in two variables (order 2)**

**14.9.3 General Taylor's theorem (n variables, order k) — optional**

**14.9.3.1 Multivariate Taylor's series expansion**
- **Linear (Taylor) approximation 2 variables**: `P_{1, (a,b)} = f(a,b) + (x−a) f_x(a,b) + (y−b) f_y(a,b)`. ⭐
- **Quadratic (Taylor) approximation 2 variables**: as in (14.22). ⭐
- **General Taylor polynomial of order `k` in `n` variables**: as in (14.24).
1. Compute `f(a)` and all required partials of order ≤ `k` at `a`.
2. Substitute into the order-`k` Taylor polynomial.
3. The remainder term provides the error.
- `f(1, 1, 1) = 1`.
- First partials: `f_x = yz`, `f_y = xz`, `f_z = xy`; each `= 1` at `(1, 1, 1)`.
- Pure second partials all zero (`f_{xx} = f_{yy} = f_{zz} = 0`); mixed second partials: `f_{xy} = z`, `f_{xz} = y`, `f_{yz} = x`; each `= 1` at `(1, 1, 1)`.
- Third partial: only `f_{xyz} = 1` is non-zero; all others zero.
- Fourth and higher: all zero.

### ⚠️ Common Mistakes
- ❌ Forgetting the cross term `(x − a)(y − b) f_{xy}(a, b)` in the quadratic 2-variable Taylor → ✅ Always include it.
- ❌ Using the wrong factor `1/2!` for cross-terms — note the source formula uses `(x − a)(y − b) f_{xy}` with no `1/2!` because both off-diagonal entries `f_{xy}` and `f_{yx}` are summed.

**Quick Recall:**
- Linear: `f(a,b) + f_x(a,b)(x − a) + f_y(a,b)(y − b)`
- Quadratic adds: `½ f_{xx}(a,b)(x − a)² + f_{xy}(a,b)(x − a)(y − b) + ½ f_{yy}(a,b)(y − b)²`
- Builds on: 14.4 partials, 14.4.4 higher-order partials, 14.8.5 single-variable approximations.
- Continues into: optimization (Unit 15) — second-order conditions use Hessian and quadratic Taylor.

### 14.11 Key Words [🔴]
- **Partial derivative**: derivative of a dependent variable `z` w.r.t. one or more of the variables `x, y, w, …` while treating at least one of them as a constant. ⭐
- **Unit vector specification (in `n`-D)**: `(cos θ_1, cos θ_2, …, cos θ_n)`, where `θ_i` is the angle the vector makes with the `i`-th axis. For `n = 2`, with `θ` the angle with `x`-axis, the unit vector is `(cos θ, cos(π/2 − θ))`. ⭐
- **Gradient `∇f`**: for `f` of `n` variables `x_1, …, x_n`, `∇f = ⟨f_{x_1}, …, f_{x_n}⟩`. ⭐
- **Directional derivative**: in multivariate calculus, the derivative along a chosen direction at a point. If `û = (cos θ_1, …, cos θ_n)` and `∇f = ⟨f_{x_1}, …, f_{x_n}⟩`, then `D_û f = ∇f · û`. ⭐
- **Jacobian**: for `f: R^n → R^m`, the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`. ⭐
- **Hessian**: for `f: R^n → R`, the `n × n` matrix of second partials. ⭐
- **Mean Value Theorem**: continuous on `[a, b]`, differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`. ⭐
- **Taylor's formula**: `f(x) = P_{k, a}(x) + R_{k, a}(x)`, where `P_{k, a} = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k`. ⭐

**Quick Recall:**
- `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + …`
- `log(x) at a=1 = (x−1) − (x−1)²/2 + (x−1)³/3 − …`

### ⚠️ Common Mistakes
- ❌ Concluding existence of a 2-variable limit from agreement of two paths → ✅ As Q1 shows, even three paths agreeing isn't enough; non-existence requires only a single disagreement.
- ❌ Forgetting MVT requires both continuity on `[a, b]` AND differentiability on `(a, b)` (only interior).
| Metric | Formula (between x, y in R^n) | Where used |
|---|---|---|
| Euclidean d_E | √[ Σ (x_i − y_i)^2 ] | Geometry, "straight-line" distance |
| Taxicab / Manhattan d_T | Σ |x_i − y_i| | Urban planning, grid streets |
| Minkowski d_p | ( Σ |x_i − y_i|^p )^{1/p} | Generalisation; statistics, optimisation |
| (Chebyshev d_∞ — implicit limit case; not formula-defined here) | — | — |

**Quick Recall:**
- Manhattan = Minkowski with p = 1
- Euclidean = Minkowski with p = 2

### 15.2.1 Metrics — The Formalised Distances (Axioms) [🔴]
- **Metric on a set**: For a non-empty set S, a function d : S × S → R is called a **metric** if for all x, y, z in S it satisfies: ⭐
  - **(i) Non-negativity**: d(x, y) ≥ 0. (The cost of going from any point to any point is non-negative.)
  - **(ii) Identity of indiscernibles**: d(x, y) = 0 iff x = y. Equivalently:
    - (a) d(x, x) = 0 for any x in S (it does not cost to remain at the same point), and
    - (b) d(x, y) > 0 if x ≠ y (the cost of going to a different point is positive).
  - **(iii) Symmetry**: d(x, y) = d(y, x). (Cost of going from x to y equals cost of going back.)
  - **(iv) Triangle inequality** ("transitive property" in the source): d(x, z) ≤ d(x, y) + d(y, z). (Going directly from x to z does not exceed going from x via y to z.)

**Quick Recall:**
1. d(x, y) ≥ 0
2. d(x, y) = 0 ⇔ x = y
3. d(x, y) = d(y, x)
4. d(x, z) ≤ d(x, y) + d(y, z)
- Leads to: Definition of metric space (15.2.2)

### 15.2.2 Metric Space — Definition & Examples [🔴]
- **Metric Space**: The ordered pair (S, d), where S ≠ ∅ and d is a metric on S, is called a **metric space**. ⭐
- Mod(x) = |x| = −x if x < 0, and = x if x ≥ 0.
- (i) Non-negativity. Since x − y ∈ R, by definition of mod, d(x, y) = |x − y| ≥ 0.
- (ii) Identity. We know |x| = 0 iff x = 0. So d(x, y) = |x − y| = 0 iff x − y = 0 iff x = y.
- (iii) Symmetry. d(x, y) = |x − y| = |y − x| (by the mod function) = d(y, x).
- (iv) Triangle inequality. For x, y, z ∈ R:
- d(x, y) = 0 if x = y, and 1 if x ≠ y.
- (i) d(x, y) ∈ {0, 1}, hence d(x, y) ≥ 0.
- (ii) If d(x, y) = 0 then x = y (otherwise d would be 1).
- (iii) Symmetry. If d(x, y) = 0 then x = y, so d(x, y) = d(x, x) = d(y, x). If d(x, y) = 1 then y ≠ x, so d(y, x) = 1. Either way d(x, y) = d(y, x).
- (iv) Triangle inequality.
  - Case (a): if x = z, then d(x, z) = 0 = 0 + 0 ≤ d(x, y) + d(y, z).
  - Case (b): if x ≠ z, then d(x, z) = 1. For any y in S, y is unequal to at least one of x, z. Say x ≠ y; then d(x, y) = 1, so d(x, z) = 1 ≤ 1 + 0 ≤ d(x, y) + d(y, z) (since d(y, z) ≥ 0).
1. Show (R^2, d_T) is a metric space, where R^2 = R × R, and the Taxicab distance is d_T(x, y) = |x_1 − y_1| + |x_2 − y_2|.
2. Show (R^2, d_E) is a metric space, where the Euclidean distance is d_E(x, y) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2].
- Builds on: |·| function (Unit 1), Euclidean distance (Unit 14)
- Leads to: Open/closed sphere; open/closed sets (15.2.3)

### ⚠️ Common Mistakes
- ❌ Treating "ball" and "sphere" as different objects in this text. ✅ Here they're used interchangeably (the unit explicitly says the term "ball" is also used for "sphere").
- ❌ Thinking S^c is a standard notation. ✅ The text explicitly notes B^c and S^c are **not standard notations** for closed ball/sphere — they are local notation only.

### 15.2.3.1.1 Open & Closed Sphere of an Arbitrary Metric Space [🔴]
- **Open sphere with centre a and radius r** ⭐:
- **Closed sphere with centre a and radius r** ⭐:

**Quick Recall:**
- Open sphere uses strict < ; closed uses ≤.
- In (R, |·|), an open sphere is just an open interval centred at a.
- Builds on: Metric space definition (15.2.2.2)
- Leads to: Open set in metric space (15.2.3.1.2, chunk 012)
1. What does an "open sphere" look like under the **discrete metric** (Example 15.2)? — Pursued in chunk 012's Check Your Progress 2.

**Quick Recall:**
- In (R, |·|), the open sphere is an open interval.
- In (R^2, d_E), the open sphere is an open disk.

### 15.2.3.1.2 Open Set & Closed Set of a Metric Space [🔴]
- **Open set of (X, d)** ⭐: A subset T of X is **open** if for each x ∈ T, there is an open sphere S(x, ε) with ε > 0 such that S(x, ε) ⊆ T. Equivalently, every member of T is well inside T; no member is a boundary point.
- **Closed set of (X, d)** ⭐: A set T ⊆ X is **closed** if its complement X − T is an open set in X.
1. **]1, 3[ ∪ ]5, 7[ is open**, because (a) every open interval is an open set, and (b) union of open sets is open. (Both will be proved in the theorem below.)
2. **[1, 3[ is NOT open**: no open sphere ]1 − ε, 1 + ε[ with ε > 0 fits inside [1, 3[. Similarly **[1, 3] is not open**.
3. For a real number a:
   - **]−∞, a[ is open**. Proof: Let x ∈ ]−∞, a[, so x < a. Let ε = a − x > 0. Then S(x, ε) ⊆ ]−∞, a[.
   - **]a, ∞[ is open**. Proof: Let x ∈ ]a, ∞[, so a < x. Let ε = x − a > 0. Then S(x, ε) ⊆ ]a, ∞[.
- **(i) Union of an arbitrary number of open sets is open.**
- **(ii) Intersection of a finite number of open sets is open.**
- **(iii) The universal set X is open.**
- **(iv) The empty set ∅ is open.**
- **(v) Every open sphere S(a, r) is an open set.**

**Proof of (i): Union of arbitrary open sets is open**
- Let x ∈ ⋃_{i ∈ I} X_i, so x ∈ X_j for some particular j.
- Since X_j is open, there exists ε > 0 with S(x, ε) ⊆ X_j.
- And X_j ⊆ ⋃_i X_i.
- Hence S(x, ε) ⊆ ⋃_i X_i. ⬛

**Proof of (ii): Finite intersection of open sets is open**
- If the intersection is ∅, by (iv) it is open.
- Else, let x ∈ ⋂_{i=1..n} X_i; then x ∈ X_i for each i.
- Since each X_i is open, ∃ ε_i > 0 with S(x, ε_i) ⊆ X_i.
- Let ε = min{ε_i : i = 1, …, n}. Then ε > 0 and S(x, ε) ⊆ S(x, ε_i) ⊆ X_i for each i.
- So S(x, ε) ⊆ ⋂_{i=1..n} X_i. ⬛

### ⚠️ Common Mistake
- ❌ "Intersection of arbitrary open sets is open." ✅ Only **finite** intersections are guaranteed open. (For arbitrary intersection, the analogous result holds for **closed** sets.)
- **(i) Union of a finite number of closed sets is closed.**
- **(ii) Arbitrary intersection of closed sets is closed.** (The source text says "arbitrary intersection of closed sets is open" but the proof clearly establishes closed; this is a typo in the source.)
- **(iii) The universal set X is closed.**
- **(iv) The empty set ∅ is closed.**

**Proof of (i): Finite union of closed sets is closed**

**Proof of (ii): Arbitrary intersection of closed sets is closed**
1. **[1, 3] ∪ [5, 7] is closed**: every closed interval is closed, and union of finitely many closed sets is closed.
2. **[1, 3[ is NOT closed**: its complement ]−∞, 1[ ∪ [3, ∞[ is not open — no sphere S(3, ε) = ]3 − ε, 3 + ε[ fits inside the complement.
3. **]−∞, a] is closed**: complement ]a, ∞[ is open. **[a, ∞[ is closed**: complement ]−∞, a[ is open.
- Builds on: Open sphere of metric space (15.2.3.1.1, Chunk 011)
- Leads to: Convergence, continuity (15.2.4); topology (15.3)

### 15.2.4.1 Convergence of a Sequence in a Metric Space [🔴]
- **Convergent sequence in (X, d)** ⭐: Let (X, d) be a metric space, X ≠ ∅, with (x_n) = (x_1, x_2, …, x_n, …) an infinite sequence in X. We say (x_n) is **convergent** if there exists x ∈ X such that for each ε > 0, there exists a positive integer k such that d(x_n, x) < ε for all n > k.

**Quick Recall:**
- Convergence "ε-style": d(x_n, x) < ε eventually.
- Convergence "open-sphere style": x_n eventually inside S(x, ε).
- Builds on: Convergence in R (Unit 9), R^n (Unit 12)
- Leads to: Sequence-based characterisation of continuity (Theorem 15.2.4.2.3)

### 15.2.4.2 Continuity of a Function in Metric Space [🔴]
- **Continuity at x = x_0** ⭐: Let (X_1, d_1), (X_2, d_2) be metric spaces and f : X_1 → X_2. Then f is **continuous at x_0 ∈ X_1** if for each ε > 0 there exists δ > 0 such that for all x ∈ X_1, d_1(x, x_0) < δ implies d_2(f(x), f(x_0)) < ε. (Note f(x), f(x_0) ∈ X_2.)

**Quick Recall:**
1. ε–δ: d_1 small ⟹ d_2 small.
2. Open spheres / open sets: pre-image of "small region" contains a "small region."
3. Sequential: convergent sequences map to convergent sequences.
- Builds on: Continuity in R (Unit 9)
- Leads to: Continuity in topological space (15.3.2.1)

### 15.2.4.3 Connectedness in a Metric Space [🔴]
- **Connected set in (X, d)** ⭐: A set S in (X, d) is **connected** if it cannot be represented as the union of two or more disjoint non-empty open sets in the metric space.
- **Theorem 15.2.4.3.1**: S in (X, d) is connected iff it cannot be represented as the union of two or more disjoint non-empty closed sets.
- **Theorem 15.2.4.3.2**: A subset of R, equipped with Euclidean metric, is connected iff it is an interval (open, semi-open, or closed).
- **Example 15.6**: In (R, d_E), each of ]3, 7[, [3, 7[, [3, 7] is a connected set. In general, any interval — open, semi-open, or closed — is connected.
- **Example 15.7**: S = ]3, 7[ ∪ ]10, 16[ is **not** connected in (R, d_E). In general, the union of two non-overlapping intervals is not connected.
- Leads to: Connectedness in topology (15.3.2.2)

### 15.2.4.4 Compactness in a Metric Space; Bounded Sets [🔴]
- **Bounded set in (X, d)** ⭐: S ⊆ X is **bounded** if there exists r > 0 such that for all s, t ∈ S, d(s, t) < r.
- **Bounded metric space**: (X, d) is bounded if X itself is bounded as a subset of itself.
- **Boundedness.** Let M = max{ d(a_i, a_j) : i, j = 1, …, n }. Then for every pair (a_i, a_j), d(a_i, a_j) ≤ M. So A is bounded.
- **Closedness.** Show X − A is open. The universal set X is open. We can write
- Builds on: Compactness in R (previous unit; Bolzano-Weierstrass)
- Leads to: Compactness via open covers in topology (15.3.2.3, Chunk 013)

### 15.3.1 Topology — Basic Definitions [🔴]
- **Topology / Topological Space** ⭐: For X non-empty, a **topology on X** is the ordered pair (X, T), where T ⊆ P(X) is a collection of subsets of X satisfying:
  - (i) X ∈ T,
  - (ii) ∅ ∈ T,
  - (iii) the union of any number of sets in T is in T,
  - (iv) the intersection of any **finite** number of sets in T is in T.
- **Open Set** (in topology) ⭐: Each set in T is an **open set** of (X, T). A set is open iff it belongs to T. So X and ∅ are always open.
- **Closed Set** (in topology) ⭐: A subset S ⊆ X is **closed** if its complement X − S ∈ T. So X and ∅ are always closed too.
- **Neighbourhood of a point x (or a set S)** ⭐: A neighbourhood of x (or of S) is an open set (member of T) which contains the point x (or the set S).
- (i) X ∈ T, (ii) ∅ ∈ T — obvious.
- (iii) Only union is X ∪ ∅ = X ∈ T. ✓
- (iv) Only intersection is X ∩ ∅ = ∅ ∈ T. ✓
- (i) X ∈ P(X). (ii) ∅ ∈ P(X). ✓
- (iii) Any union of subsets of X is itself a subset of X, hence in P(X). ✓
- (iv) Any intersection of subsets of X is itself a subset of X, hence in P(X). ✓
- X, ∅ are always open in any metric space, so both ∈ T.
- (iii), (iv) follow from Theorem 15.2.3.1.2.1: arbitrary unions of open sets are open; finite intersections of open sets are open.

**Quick Recall:**
- **Indiscrete topology** = { ∅, X }. Smallest possible.
- **Discrete topology** = P(X). Largest possible.
- **Metric-induced topology** = open sets of (X, d).
| Setting | Open set defined as | Notes |
|---|---|---|
| (R, |·|) | every point has surrounding open interval inside the set | Recap from earlier unit |
| Metric space (X, d) | every point has surrounding open sphere inside the set | 15.2.3.1.2 |
| Topology (X, T) | being a member of the chosen collection T | 15.3.1 — most general |
- Builds on: Open sets in metric space (15.2.3.1.2)
- Leads to: Continuity / connectedness / compactness in topological space (15.3.2)

### 15.3.2.1 Continuity of a Function in Topological Space [🔴]
- Let (X_i, T_i), i = 1, 2, be topological spaces, and f : X_1 → X_2. Then f is **continuous at x_0 ∈ X_1** ⭐ if for each neighbourhood H of f(x_0) in X_2, there exists a neighbourhood G of x_0 in X_1 such that f(G) ⊆ H.

**Quick Recall:**
- Metric-space continuity (ε–δ) ⟹ this when T comes from d.
- Topological continuity is just "neighbourhood of image has a neighbourhood of pre-image inside."
- Builds on: Theorem 15.2.4.2.2 (open-set characterisation of continuity in metric spaces)
- Leads to: Connectedness, compactness (15.3.2.2, .3 — Chunk 013)

### 15.3.2.2 Connectedness of a Set in a Topological Space [🔴]
- **Connected set in topology (X, T)** ⭐: A set S ∈ T is **connected** if whenever S = A ∪ B with A, B ∈ T (i.e., open in X) and A ∩ B = ∅, then either A = ∅ or B = ∅.
- Builds on: Connectedness in metric space (15.2.4.3, Chunk 012)

### 15.3.2.3 Compactness of a Set in a Topological Space [🔴]
- **Cover**: In a topological space (X, T), for a set S, a **cover** of S is a family F of subsets of X with S ⊆ ⋃_{B ∈ F} B.
- **Open cover** ⭐: A cover F is an **open cover** if every B ∈ F is open, i.e., F ⊆ T.
- **Subcover / Finite subcover** ⭐: For a cover F of S, a **subcover** F′ is a sub-family F′ ⊆ F that is also a cover of S. If F′ contains only finitely many sets, it is a **finite subcover**.
- **Compact Set / Space** ⭐: A set S in (X, T) is **compact** if every open cover of S has a finite subcover. If X itself is compact, X is a **compact space**.

**Quick Recall:**
- Compact = "every open cover has a finite subcover."
- In metric/Euclidean space, this is equivalent to "closed and bounded."
- Builds on: Compactness in metric space (15.2.4.4, Chunk 012)

### 15.5 Key Words — Glossary [🔴]
- **Euclidean Distance d_E** in 2-D space R^2: For P(x_1, y_1), Q(x_2, y_2),
- d_E(P, Q) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]. ⭐
- **Taxicab / Manhattan Distance d_T** between P(x_1, y_1) and Q(x_2, y_2):
- d_T(x, y) = |x_1 − x_2| + |y_1 − y_2|. ⭐
- **Minkowski Distance of order p** in R^n:
- **Metric on a Set** (4 axioms): a function d : S × S → R with (i) d(x, y) ≥ 0, (ii) d(x, y) = 0 ⇔ x = y (i.e., d(x, x) = 0; d(x, y) > 0 if x ≠ y), (iii) d(x, y) = d(y, x), (iv) d(x, z) ≤ d(x, y) + d(y, z). ⭐
- **Metric Space**: ordered pair (S, d), S ≠ ∅, d a metric on S. ⭐
- **Open ball / sphere in R^n**: For a ∈ R^n, r > 0, S(a, r) = { x ∈ R^n : d_E(x, a) < r }.
- **Closed ball / sphere in R^n**: S^c(a, r) = { x ∈ R^n : d_E(x, a) ≤ r }. (S^c not standard notation.)
- **Open Set in R**: S ⊆ R is open if for each a ∈ S, there exists ε > 0 such that ]a − ε, a + ε[ ⊆ S.
- **Closed Set in R**: S ⊆ R is closed if R − S is open in R.
- **Open Sphere in (X, d)**: S(a, r) = { x ∈ X : d(a, x) < r }. ⭐
- **Closed Sphere in (X, d)**: S^c(a, r) = { x ∈ X : d(a, x) ≤ r }. ⭐
- **Open Set in (X, d)**: T ⊆ X is open if for each x ∈ T there is an open sphere S(x, ε), ε > 0, with S(x, ε) ⊆ T. ⭐
- **Closed Set in (X, d)**: T ⊆ X is closed if X − T is open in X. ⭐
- **Convergence in (X, d)**: (x_n) → x if for every ε > 0 there exists positive integer k with d(x_n, x) < ε for all n > k. ⭐
- **Continuity at x_0 in metric space**: For (X_i, d_i), i = 1, 2, f : X_1 → X_2 is continuous at x_0 if for every ε > 0 there exists δ > 0 such that d_1(x, x_0) < δ ⟹ d_2(f(x), f(x_0)) < ε. ⭐
- **Connected Set (metric space)**: S ⊆ X is connected if it cannot be represented as a union of two or more disjoint non-empty open sets in (X, d). ⭐
- **Bounded Set / Bounded Metric Space**: S ⊆ X bounded if ∃ r > 0 with d(s, t) < r for all s, t ∈ S. (X, d) bounded if X is bounded as a subset of itself. ⭐
- **Topology / Topological Space (X, T)**: For X ≠ ∅, T ⊆ P(X) with (i) X ∈ T, (ii) ∅ ∈ T, (iii) T closed under arbitrary unions, (iv) T closed under finite intersections. ⭐
- **Open Set in (X, T)**: any element of T.
- **Closed Set in (X, T)**: S ⊆ X with X − S ∈ T.
- **Neighbourhood of x (or set S) in (X, T)**: an open set (member of T) containing x (or S). ⭐
- **Continuity in topology**: f : X_1 → X_2 continuous at x_0 if for each neighbourhood H of f(x_0) in X_2, there is a neighbourhood G of x_0 in X_1 with f(G) ⊆ H. ⭐
- **Connectedness in topology**: S ∈ T is connected if it cannot be written as a disjoint union of two or more non-empty open sets. ⭐
- **Cover**: family F of subsets of X with S ⊆ ⋃_{B ∈ F} B.
- **Open Cover**: cover with F ⊆ T (every B is open). ⭐
- **Subcover / Finite subcover**: F′ ⊆ F that is itself a cover; finite if F′ has finitely many sets. ⭐
- **Compact Set / Space**: S in (X, T) compact if every open cover has a finite subcover. (X, T) compact if X is compact. ⭐

### Answer — Exercise 1: (R^n, d_T) is a metric space [🔴]
- **(i) Non-negativity.** Each |x_i − y_i| ≥ 0, so d_T(x, y) ≥ 0 + 0 + … + 0 = 0.
- **(ii) Identity.** d_T(x, y) = 0 iff |x_i − y_i| = 0 for each i = 1, …, n iff x_i − y_i = 0 (since |x| = 0 ⇔ x = 0) iff x_i = y_i for each i iff x = y.
- **(iii) Symmetry.** d_T(x, y) = Σ |x_i − y_i| = Σ |y_i − x_i| (by definition of mod) = d_T(y, x).
- **(iv) Triangle Inequality.** For x, y, z ∈ R^n,
- Builds on: Check Your Progress 1 (R^2 case) (Chunk 013)

### Answer — Exercise 2: (R^n, d_E) is a metric space [🔴]
- **(i) Non-negativity.** (x_i − y_i)^2 ≥ 0 for each i, so d_E(x, y) ≥ 0.
- **(ii) Identity.** d_E(x, y) = 0 iff (x_i − y_i)^2 = 0 for each i iff x_i = y_i for each i iff x = y.
- **(iii) Symmetry.** d_E(x, y) = √[ Σ (x_i − y_i)^2 ] = √[ Σ (y_i − x_i)^2 ] = d_E(y, x).
- **(iv) Triangle Inequality.** For x, y, z ∈ R^n,

### ⚠️ Note on the Source's Argument
The source justifies the triangle inequality via "the generalised Pythagorean theorem," writing (a_1 + … + a_n)^2 ≤ a_1^2 + … + a_n^2. This stated inequality is **not generally true** as written (e.g., (1+1)^2 = 4 > 1+1 = 2). The correct underlying tool is the **Minkowski inequality** (or Cauchy-Schwarz). We reproduce the source's proof structure as the question requires faithfulness, but the careful proof of the Euclidean triangle inequality uses Minkowski, not "(a + b)^2 ≤ a^2 + b^2."
- Builds on: Check Your Progress 1(2) (R^2 case) (Chunk 013)

**Quick Recall:**
- Euclidean unit ball in R^2 = open disk.
- Taxicab unit ball in R^2 = open diamond (tilted square).

### Answer — Exercise 4: Every Open Sphere S(a, r) is an Open Set [🔴]
- **Case 1: x = a.** Then S(x, r) = S(a, r) ⊆ S(a, r). ✓
- **Case 2: x ≠ a.** Then d(x, a) > 0, and d(a, x) < r.
  - Let ε = d(x, a) > 0. Then ε < r, i.e., r − ε > 0.
  - We show ]x − (r − ε), x + (r − ε)[ ⊆ S(a, r). (More precisely, the *open sphere* S(x, r − ε), which the source writes as the interval ]x − (r − ε), x + (r − ε)[ — appropriate for the R case.)
  - Let y ∈ S(x, r − ε), i.e., d(x, y) < r − ε.
  - Then by the triangle inequality, d(a, y) ≤ d(a, x) + d(x, y) < ε + (r − ε) = r.
  - Hence y ∈ S(a, r).
  - So S(x, r − ε) ⊆ S(a, r). ⬛
- Completes: Theorem 15.2.3.1.2.1(v) (Chunk 012)
- Builds on: Triangle inequality (15.2.1, Chunk 011)
