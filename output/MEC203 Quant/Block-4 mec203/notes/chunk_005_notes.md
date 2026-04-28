# Chunk 005 — Unit 13: Extreme Value Theorem, Summary, Exercises
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt -->

## Section: 13.5.4(C) Limit and Continuity of `f: R^n → R^m` 🔴
<!-- Reason: Generalises limit/continuity to vector-valued multi-variable functions. Listed in unit objectives. -->

### Core Idea
The definitions of limit and continuity for `f: D → R^m` (with `D ⊆ R^n`) are identical in *form* to those for `f: R^n → R` — the only change is that the absolute value `|·|` is replaced by the **norm** `||·||` on the output side too (since `f(x)` and `l` are now vectors in `R^m`).

### Definitions
- **Limit of `f: D → R^m`** (with `D ⊆ R^n`, `a ∈ R^n`): `lim_{x → a} f(x)` exists and equals `l ∈ R^m` iff for every `ε > 0`, ∃ `δ > 0` such that whenever `||x − a|| < δ`, then `||f(x) − l|| < ε`.
  *(Note: both `f(x)` and `l` are now members of `R^m`, not real numbers.)* ⭐
- **Continuity of `f: D → R^m` at `a ∈ R^n`**: `f` is continuous at `x = a` if (i) `lim_{x → a} f(x)` exists, AND (ii) `lim_{x → a} f(x) = f(a)`. ⭐

### Key Concepts

#### What changes between `f: R^n → R` and `f: R^n → R^m`
| Object | `f: R^n → R` | `f: R^n → R^m` |
|---|---|---|
| Input distance | `||x − a||` (norm in R^n) | `||x − a||` (norm in R^n) |
| Output distance | `|f(x) − l|` (absolute value in R) | `||f(x) − l||` (norm in R^m) |
| `l` lives in | `R` | `R^m` |

> **Quick Recall:**
> - Limit definition is the same ε-δ shape; only the type of `||·||` on the output side changes.

### Connections
- Builds on: Limit / continuity for `f: R^n → R` (Chunk 004).
- Continues into: Extreme Value Theorem (next).

---

## Section: 13.5.4(D) Extreme Value Theorem 🔴
<!-- Reason: Named theorem; foundational for optimization (Block 5). Both single-variable and multivariable versions stated. -->

### Core Idea
The **Extreme Value Theorem (EVT)** says: a continuous function on a "compact-like" domain (closed interval in R; closed disc in R^n) attains both an absolute maximum and an absolute minimum value on that domain. Setup requires precise definitions of *local minima/maxima*, *local extremum*, and *global/absolute minimum/maximum*. A subtle point: a global extremum on the boundary may not be a local extremum.

> **In Simple Terms:** If a function has no jumps and is defined on a closed (and bounded) chunk of space, it must hit a highest value and a lowest value somewhere on that chunk. No "tending to infinity" allowed, no "approaching but never reaching" allowed.

### Definitions (single variable, `z = f(x)` on subset `S ⊆ R`)
- **Local Minima**: a value that `z = f(x)` attains at some point `p` such that for some `ε > 0`, `f(x) ≥ f(p)` for all `x ∈ ]p − ε, p + ε[ ⊆ S`. The value `f(p)` is the local minimum (a local minima is a *value*, not a point — `p` is the *point of* local minima). ⭐
- **Local Maxima**: a value that `z = f(x)` attains at some point `p` such that for some `ε > 0`, `f(x) ≤ f(p)` for all `x ∈ ]p − ε, p + ε[ ⊆ S`. (Same point/value distinction.) ⭐
- **Local Extremum (plural: extrema)**: a local minimum or a local maximum. ⭐
- **Global / Absolute Minimum**: a value `m` of `f(x)` over `S` such that `m ≤ f(x)` for all `x ∈ S`. (The term "minima" is generally not used here.) ⭐
- **Global / Absolute Maximum**: a value `M` of `f(x)` over `S` such that `f(x) ≤ M` for all `x ∈ S`. ⭐

### Definitions (several variables, `z = f(x)` on subset `S ⊆ R^n`)
For `x = (x_1, ..., x_n) ∈ S`:
- **Local Minima**: value `f(p)` at some `p ∈ R^n` such that for some `ε > 0`, `f(x) ≥ f(p)` for all `x ∈ ` open disc centered at `p` of radius `ε`, contained in `S`. ⭐
- **Local Maxima**: value `f(p)` at some `p ∈ R^n` such that for some `ε > 0`, `f(x) ≤ f(p)` for all `x ∈ ` open disc centered at `p` of radius `ε`, contained in `S`. ⭐
- **Global / Absolute Minimum**: a value `m` of `f(x)` over `S ⊆ R^n` such that `m ≤ f(x)` for all `x ∈ S`. ⭐
- **Global / Absolute Maximum**: a value `M` of `f(x)` over `S ⊆ R^n` such that `f(x) ≤ M` for all `x ∈ S`. ⭐

### Key Concepts

#### "Local" = immediate neighbourhood
For a real number `p`, "local" means the open interval `]p − ε, p + ε[`. For `p ∈ R^n`, "local" means the open disc of radius `ε > 0` centered at `p`.

#### Point vs. Value
The source emphasises: `x = x_3` is a *point of* local minima, but it is NOT itself a local minima — the *local minima* is the *value* `f(x_3)`. Similarly for maxima. There may be more than one local minima and more than one local maxima.

#### Extreme Value Theorem (single variable)
**Statement:** If `f` is continuous on a closed interval `[a, b]`, then `f` has an absolute maximum value and an absolute minimum value in `[a, b]`.

#### Extreme Value Theorem (several variables)
**Statement:** If `f` is continuous on a closed disc `D ⊆ R^n`, then `f` has an absolute maximum value and an absolute minimum value in `D`. *(Source as printed says "for a function f of one variable" — clearly an OCR/printing error; context makes clear this is the multivariable version.)*

#### Global extremum on a boundary need not be local
The global maximum (or global minimum), particularly at boundary points, may not be a local maximum (or local minimum). The reason: at a boundary point, the "neighbourhood" `]p − ε, p + ε[` extends outside `S`, where the function may take larger / smaller values. Source illustrates with Fig 13.2: at `x_4` (right boundary), points just to the right of `x_4` may exceed `f(x_4)`; at `x_1` (left boundary), points just to the left of `x_1` may be smaller than `f(x_1)`.

### ⚠️ Common Mistakes
- ❌ Calling the *point* `p` "a local minima" → ✅ The *value* `f(p)` is the local minima; `p` is the point at which it is attained.
- ❌ Assuming continuity alone implies an absolute max/min → ✅ EVT also requires the domain to be a closed interval (in R) or closed disc (in R^n) — i.e., compact.
- ❌ Assuming a global extremum is always a local one → ✅ Boundary global extrema may fail to be local.

### Edge Cases & Caveats
- The single-variable EVT requires `f` continuous on a *closed* interval. Open intervals don't suffice (e.g., `f(x) = 1/x` on `(0, 1)` has no maximum).

> **Quick Recall:**
> - Local minima = *value* `f(p)` smallest in some open neighbourhood; `p` is the point of attainment.
> - EVT (1-variable): continuous on `[a, b]` ⇒ attains absolute max and min.
> - EVT (n-variable): continuous on closed disc `D` ⇒ attains absolute max and min.

### Connections
- Builds on: Continuity in R^n; closed disc; bounded set (Chunk 004).
- Continues into: Optimization (Block 5, Units 16-19).

---

## Section: 13.5.4(E) Intermediate Value Theorem 🟡
<!-- Reason: Named theorem, briefly stated. Less detail than EVT in the source. -->

### Core Idea
**Statement (as in source):** "If `f` is a continuous function whose domain contains the interval `[a, b]`, then it takes on any given value between `f(a)` and `f(b)` at some point within the interval."

### Connections
- Builds on: Continuity (this unit and Block 3).

---

## Section: 13.6 Let Us Sum Up 🟢
<!-- Reason: Unit summary, restating what was covered. -->

### Core Idea
The unit covered:
- Concepts of sequences of real numbers and their special types (bounded, monotone).
- Concepts of limit of a sequence, convergence, divergence, Cauchy sequences, subsequences, sequences in `R^n`.
- For subsets of real numbers: open / closed / bounded / compact sets, the Bolzano-Weierstrass theorem, and economic applications.
- Under analysis of several real variables: n-dimensional real space, n-dimensional Euclidean space, functions between Euclidean spaces, functions from `R^n` to `R`, and functions from `R^k` to `R^m`.

---

## Section: 13.7 Key Words 🟢
<!-- Reason: Source-listed glossary. -->

### Definitions (verbatim glosses from source)
- **Real Analysis**: a branch of Mathematical Analysis.
- **Sequence**: an enumerated ordered set, in which repetition of elements is allowed. Enumerated means elements can be counted as first, second, etc. Elements of `[0, 1]` cannot be counted as first, second, ... A sequence uses parentheses `()`, unlike a set which uses braces `{}`.
- **Sequence of real numbers**: a function `f: S → R`, where `S` (the domain) is either `N` or an interval subset of `N`, and `R` (the codomain) is the set of real numbers. The main interest is in the range as an enumerated ordered set allowing repetitions.
- **Convergent Sequence**: `(S_n)` is convergent if ∃ a (finite) real `l` such that for given `ε > 0`, ∃ a natural `n_ε` with `|S_n − l| < ε` for all `n > n_ε`. Then `l` is the limit; we write `lim_{n→∞} S_n = l`.
- **Cauchy Sequence**: `(S_n)` is Cauchy if for given `ε > 0`, ∃ a natural `n_ε` such that `|S_n − S_m| < ε` for all `n, m > n_ε`.
- **Limit-point of a sequence**: real `LP` such that some subsequence of `(S_n)` converges to `LP`.
- **Open set**: `S` of reals is open if for each `a ∈ S`, ∃ `ε > 0` such that `]a − ε, a + ε[ ⊆ S`. Every member is well inside; no boundary points.
- **Closed set**: `S ⊆ R` is closed if `R − S = (−∞, +∞) − S` is open.
- **Compact set**: a subset of R is compact if it is both closed and bounded.
- **Limit point of a set**: `p` is a limit point of `S` if for every `ε > 0`, the open interval `]p − ε, p + ε[` contains a point of `S` different from `p`. Also called accumulation / condensation / cluster point.

---

## Section: 13.8 Answers / Hints to Check Your Progress Exercises 🟢
<!-- Reason: Solutions to in-text exercises; useful for revision. -->

### Check Your Progress 1 (subsequence test, first terms, general term, recursive defs)
1. From `S = (4, 6, 8, ...)`:
   - (a) `(6, 12, 16)` — IS a subsequence (each term in `S`, in order).
   - (b) `(12, 6, 16)` — NOT a subsequence (12 and 6 are out of order).
   - (c) `(8, 64, 243, ...)` — NOT a subsequence (243 is not in `S`).
2. First five terms (taking `S_1` as first):
   - (a) `S_n = [n + (−1)^n] / n` ⇒ `(0, 3/2, 2/3, 5/4, 4/5)`.
   - (b) `[1 − 1/(n+1)]^{n+½}` ⇒ `((1/2)^{1.5}, (2/3)^{2.5}, (3/4)^{3.5}, (4/5)^{4.5}, (5/6)^{5.5})`.
3. General term:
   - (a) `11/(6n − 4)` for `11/2, 11/8, 11/14, ...`
   - (b) `2^n − 3` for `−1, 1, 5, 13, ...`
4. Recursive definitions:
   - (a) `1, 4, 13, 40, ...`: `S_n = 3·S_{n−1} + 1`, `S_1 = 1`.
   - (b) `4, 9, 16, 25, ...`: `S_1 = 4`; since `S_n = (n+1)²`, `S_{n−1} = n²`, so `S_n − S_{n−1} = 2n + 1`. Hence `S_n = S_{n−1} + 2n + 1`.

### Check Your Progress 2 (A.P., G.P., H.P., Fibonacci, monotone-bounded examples)
1. A.P. `7, 4.5, 2, −0.5, −3, ...` (`a = 7`, `d = −2.5`):
   - (a) `t_25 = 7 + (25 − 1)·(−2.5) = 7 − 60 = −53`.
   - (b) Sum from 15th to 25th = `t_25 − t_14 = −53 − [7 + 13·(−2.5)] = −53 − (−25.5) = −27.5`. *(Source uses index 14 in the subtraction, consistent with sum of terms 15-25.)*
2. G.P.s:
   - (a) `6, 2, 2/3, ...` (`a = 6`, `r = 1/3`): `S_10 = 6·(1 − (1/3)^{10})/(1 − 1/3) = 9·(1 − (1/3)^{10})`.
   - (b) For G.P. `18, −6, 2, −2/3, ...` (`a = 18`, `r = −1/3`):
     - (i) `t_15 = 18·(−1/3)^{14} = 18·(1/3)^{14} = 2·(1/3)^{12}`.
     - (ii) Sum from 9th to 15th = `S_15 − S_8` (per source's working) = `(27/2)·(1/3)^9·(1 + 3^7)` = `(1/2)·(1/3)^7·(1 + 3^7)`.
3. A.P. with `a = 1/10`, `d = −1/15`: nth term = `(5 − 2n)/30`. So corresponding H.P. has nth term `30/(5 − 2n)`, i.e., `10, 30, −30, −10, −6, ...`
4. Fibonacci:
   - (a) First 12 terms: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89`.
   - (b) Sum from 6th to 10th = `(sum of first 10) − (sum of first 5) = (F_{12} − 1) − (F_7 − 1) = F_{12} − F_7 = 89 − 8 = 81`.
5. Examples:
   - (a) Strictly increasing: `(1, 2, 4, 8, ..., 2^{n−1}, ...)`.
   - (b) Strictly decreasing: `(−1, −2, −4, −8, ..., −2^{n−1}, ...)`.
   - (c) Neither: `(2, 3, 2, 3, ...)`; `t_n = 2` if `n` odd, `t_n = 3` if `n` even.
6. Mixed:
   - (a) Bounded but not monotonic: `(2, 3, 2, 3, ...)`.
   - (b) Monotonically increasing but not bounded: `(1, 2, 4, 8, ..., 2^{n−1}, ...)`.
   - (c) Both bounded and monotonic: `(3 − 1/n)` for `n ∈ N`.

### Check Your Progress 3 (oscillation, divergence, limit points, limit existence)
1. Examples:
   - (a) Finitely oscillatory: `(4, 3, 2, 1, 4, 3, 2, 1, ...)`.
   - (b) Divergent to +∞: `(1, 4, 9, 16, ...) = (n²)`.
   - (c) Divergent to −∞: `(−1, −4, −9, −16, ...) = (−n²)`.
   - (d) Infinitely oscillatory: `(1, −1, 4, −4, 9, −9, 16, −16, ...)`.
2. Limit points:
   - (a) `(4, 3, 2, 1, 4, 3, 2, 1, ...)`: four constant subsequences `t_n = 4` (`n = 4m − 3`), `t_n = 3` (`n = 4m − 2`), `t_n = 2` (`n = 4m − 1`), `t_n = 1` (`n = 4m`). Limit points: `4, 3, 2, 1`.
   - (b) `(2 + 1, 3 − 1, 2 + 1/2, 3 − 1/2, 2 + 1/3, 3 − 1/3, ...)`: two subsequences `(2 + 1/n) → 2` and `(3 − 1/n) → 3`. Limit points: `2` and `3`. (Convergence shown via Archimedean property.)
3. Show `lim n^{1/n} = 1`: Since `n^{1/n} > 1` for `n > 1`, write `n^{1/n} = 1 + h_n`, `h_n > 0`. Then `n = (1 + h_n)^n`. By binomial theorem, `n = 1 + n·h_n + n(n−1)/2 · (h_n)² + ...`. Dropping positive terms gives `n > [n(n−1)/2]·(h_n)²`, so `(h_n)² < 2/(n − 1)`, i.e., `h_n < √(2/(n − 1))` for `n > 2`. For given `ε > 0`, choose `n_ε > 2/ε² + 1`; then `|n^{1/n} − 1| < h_n < ε`. Hence `lim n^{1/n} = 1`.
4. Show `(n)` does not converge: Proof by contradiction. Suppose `lim (n) = l > 0`. Then for `ε = 1/2`, ∃ `n_ε` with `|n − l| < 1/2` for all `n > n_ε`, i.e., `l − 1/2 < n < l + 1/2`. But this interval contains at most one natural number — contradiction (it must contain infinitely many `n > n_ε`).

### Check Your Progress 4 (open / closed / bounded; limit points of sets)
1. Proofs:
   - (a) Closed interval `[a, b]` is not an open set: for any `ε > 0`, `]a − ε, a + ε[ ⊄ [a, b]` (it sticks out below `a`).
   - (b) Semi-closed interval `[a, b[` not open: as in (a) with the left endpoint. `]a, b]` not open: similarly with the right endpoint, `]b − ε, b + ε[ ⊄ ]a, b]`.
   - (c) `(−∞, 10)` not bounded below; `(100, ∞)` not bounded above.
   - (d) Every finite set is compact: shown to be closed (Example 13.19(ii)) and bounded ⇒ compact.
2. Limit points:
   - (a) `N = {1, 2, 3, ...}` has no limit points (cannot contain any open interval `]a − ε, a + ε[` of reals).
   - (b) Limit points of `(3, 5] ∪ {6, 7} ∪ [8, 9]` are `[3, 5] ∪ [8, 9]` (every point of an interval is its limit point; boundary points included; the finite set `{6, 7}` has no limit points).

### Check Your Progress 5 (multivariable function; norm/distance/dot product on 5-tuples)
1. `f(x, y, z) = 2 x²y² + 2 z² − 3xz`. Domain: `R³ = R × R × R`. Range: `R` (every real `u` achievable, e.g., `f(u/(−3), 0, 1) = u`).
   - (a) `f(−1, −2, 2)` — source prints `−16 − 64 + 6 = −74` (intermediate values reflect source as printed; verify against PDF).
   - (b) `f(1, 3, −2)` — source prints `−36 + 216 + 6 = 186`.
2. `x = (4, 2, −1, −2, −3)`, `y = (−1, 3, −3, −3, 2)`:
   - (a) `||x|| = √[16 + 4 + 1 + 4 + 9] = √34`; `||y|| = √[1 + 9 + 9 + 9 + 4] = √32`.
   - (b) `d(x, y) = √[(4−(−1))² + (2−3)² + (−1−(−3))² + (−2−(−3))² + (−3−2)²] = √[25 + 1 + 4 + 1 + 25] = √56`.
   - (c) `x · y = (4)(−1) + (2)(3) + (−1)(−3) + (−2)(−3) + (−3)(2) = −4 + 6 + 3 + 6 − 6 = 5`.

---

## Section: 13.10 Exercises and Answers (Q1-Q4) 🔴
<!-- Reason: Worked proofs of recursivity and boundedness for A.P., G.P., Fibonacci. Useful exam material. -->

### Q1 — A.P. is recursively definable
**Claim:** An Arithmetic Progression is recursively definable.

**Proof:** If `a` is the initial term and `d` the common difference, then nth term:
`t_n = a + (n − 1)d = a + [(n − 2)d + d] = [a + (n − 2)d] + d = t_{n−1} + d`.

So `t_n = t_{n−1} + d` — the nth term is given by a formula involving the (n−1)-th term. ∎

### Q2 — Non-trivial A.P. unboundedness
**Claim:** A non-trivial A.P. (`d ≠ 0`):
- (i) is not bounded above if `d > 0`,
- (ii) is not bounded below if `d < 0`.

**Proof of (i):** Let `M > 0`, `M > a`, be a real number, howsoever large. Given `M − a > 0` and `d > 0`, by the **Archimedean Property** ∃ a natural `n` such that `n·d > M − a`, i.e., `(a + n·d) > M`. So the `(n+1)`-th term exceeds `M`. Hence the A.P. cannot be bounded above. ∎

**Proof of (ii):** `d < 0` ⇒ `−d > 0`. Let `M > 0`, `M > |a|`. By Archimedean Property applied to `M + a` and `−d`, ∃ natural `n` with `n·(−d) > M + a`, i.e., `−a − nd > M`. Multiplying by −1 and reversing: `a + nd < −M`. So the A.P. cannot be bounded below. ∎

### Q3 — Non-trivial G.P. unboundedness
**Claim:** A non-trivial G.P. `(a r^{n−1})` (`a ≠ 0`, `1 ≠ r ≠ 0`):
- (i) not bounded above if `r > 1`, `a > 0`,
- (ii) not bounded below if `r > 1`, `a < 0`,
- (iii) bounded neither above nor below if `r < −1`.

**Proof of (i):** Let `r = 1 + ε`, with `ε > 0`. Let `M > 0` be as large as we like.
- (A) By Archimedean Property for `a·ε > 0`, ∃ natural `n` with `n·(a·ε) > M`.
- (B) `a·r^n = a·(1 + ε)^n = a·(1 + nε + ...) > a·n·ε` (binomial expansion; remaining terms are positive).
- From (A) and (B), ∃ `n` with `a·r^n > M`. Hence the G.P. with `r > 1` is not bounded above. ∎

**Proof of (ii):** `a < 0` ⇒ `−a > 0`; `r > 0`; let `r = 1 + ε`, `ε > 0`. By the same Archimedean argument applied to `(−a)·ε > 0`, ∃ `n` with `n·((−a)·ε) > M`. Then `(−a)·r^n > M`. Multiplying by −1: `a·r^n < −M`. Hence not bounded below. ∎

**Proof of (iii):** `r < −1` ⇒ `r² > 1`. Consider two sub-sequences:
- `(a · r^{2k})` (even indices): putting `R_1 = r² > 0`, this is the sequence `(a · R_1^k)`. Since `R_1 > 1` and `a > 0` (WLOG), this is unbounded above by part (i).
- `(a · r^{2k+1})` (odd indices): putting `R_2 = r² > 0` and `A_1 = a·r < 0` (since `a > 0`, `r < 0`), this becomes `(A_1 · R_2^{k})`. Since `R_2 > 1` and `A_1 < 0`, this is unbounded below by part (ii).

Hence the G.P. is bounded neither above nor below. ∎

### Q4 — Fibonacci unboundedness above; bounded below by 0
**Claim:** Fibonacci `(F_n) = (0, 1, 1, 2, 3, 5, 8, ...)` is not bounded above, but is bounded below by 0.

**Proof:** By definition, `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}` for `n ≥ 2`. ... (I)

By mathematical induction on `n`, for all `n ≥ 7`: `F_{n+1} > F_n > n`. ... (II)

Base case: `F_8 = 13 > 8 = F_7 > 7`. ✓ (II) holds for `n = 7`.

(Inductive step omitted in source but standard.) Hence `F_n` exceeds any natural number, i.e., is unbounded above.

`F_n ≥ 0` for all `n` (all terms are non-negative integers from the recurrence with `F_0 = 0`, `F_1 = 1`), so the sequence is bounded below by 0. ∎

> **Quick Recall:**
> - A.P. recursive: `t_n = t_{n−1} + d`.
> - A.P. unbounded above (d > 0) / below (d < 0); use Archimedean Property in proofs.
> - G.P. with `r > 1`: unbounded above if `a > 0`, unbounded below if `a < 0`; if `r < −1`, unbounded both ways.
> - Fibonacci: unbounded above; bounded below by 0.

### Connections
- Builds on: Boundedness results stated informally in 13.3.1 (Chunk 003); Archimedean Property used implicitly in 13.3.3 (Example 13.14).
- Continues into: Unit 14 (Calculus of Several Variables).
