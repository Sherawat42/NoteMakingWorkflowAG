# Complete Notes


## Section: Course Front Matter 🟢
<!-- Reason: Administrative front matter — no academic content. Provides scope of Volume 2 and identifies the unit writers. -->

### Core Idea
This chunk is the front matter for IGNOU MEC-203 Quantitative Methods (Volume 2). Volume 2 contains Blocks 4, 5, and 6. Block 4 (Real Analysis) consists of Unit 13 (Real Analysis), Unit 14 (Calculus of Several Variables), and Unit 15 (Basic Concepts of Metric Space and Point Set Topology). Units 13-15 in Block 4 were written by Dr. Meenakshi Sridhar (Rajdhani College, University of Delhi).

> **In Simple Terms:** Like the inside-cover and table-of-contents of a textbook — tells you who wrote what and what's coming up.

### Key Concepts

#### Volume 2 scope
Volume 2 is dated September 2023, ISBN 978-93-5568-992-4. Course coordinator is Dr. Nidhi Tewathia. Block 4 begins on page 11 of the volume; Unit 14 begins on page 51; Unit 15 begins on page 100.

### Definitions
- **MEC-203**: IGNOU course code for "Quantitative Methods" offered by the School of Social Sciences.
- **Block 4**: titled "Real Analysis" within MEC-203 Volume 2, covering Units 13-15.

### Connections
- Continues into: Unit 13 (Chunk 002: 13.0 Objectives).

---

## Section: Mathematical Symbols / Notations Glossary 🟢
<!-- Reason: Reference table of symbols used throughout the course. Useful as a lookup, not as exam content. -->

### Core Idea
A consolidated table of symbols and their meanings used throughout MEC-203. Covers logical operators, set/number-system notation, function notation, calculus operators, and vector/matrix/metric notation.

### Key Concepts

#### Interval and set-membership symbols
- `[a, b]` — closed interval
- `(a, b)` — open interval
- `∈` — element of

#### Calculus symbols
- `Δ` — delta / change in
- `dx` — differential
- `lim` — limit
- `ln` — natural log
- `∫_a^b f(x) dx` — definite integral

#### Logical / quantifier symbols
- `∀` — universal quantifier ("for all")
- `∃` — existential quantifier ("there exists")
- `∃!` — there exists exactly one
- `∃≥1` — there exists more than one
- `¬P` — negation ("not P")
- `∧` — conjunction ("and")
- `∨` — disjunction ("or")
- `⇒` — implication ("if p then q")
- `⇔` — equivalence ("if and only if")

#### Number-system / vector symbols
- `R` — set of real numbers
- `R+` — set of nonnegative real numbers
- `int R+` — set of positive real numbers
- `R^n = R × R × ... × R` — n-dimensional space of real numbers, Cartesian product of R
- `R+^n = {x ∈ R^n | x ≥ 0} ⊆ R^n` — nonnegative orthant of R^n
- `int R^n ⊆ R^n` — interior of R^n
- `a = (a_1, a_2, ..., a_n) ∈ R^n` — vector of parameters
- `x = (x_1, x_2, ..., x_n) ∈ R^n` — vector of variables

#### Preference relations (used later in welfare/economics)
- `x ~ y` — vector x is indifferent to vector y
- `≻` — strong preference relation (`x ≻ y`: x strongly preferred over y)
- `≽` — weak preference relation (`x ≽ y`: x weakly preferred over y)

#### Function symbols
- `f: X → Y` — function with domain X (set of arguments) and codomain Y (set of values)
- `y = f(x)` — scalar function of one variable
- `y = f(x_1, x_2)` — scalar function of two variables
- `dy/dx`, `y'`, `f'(x)` — first-order derivative of `y = f(x)`
- `d²y/dx²`, `y''`, `f''(x)` — second-order derivative
- `∂f/∂x_i` — first-order partial derivative for `y = f(x_1, x_2)` with respect to `x_i`
- `∂²f/∂x_i ∂x_j`, `∂²f/∂x_i²` — second-order partial derivatives
- `H(x_1, x_2)` — Hessian: symmetric matrix of second-order partial derivatives
- `df(x)/dx |_{x=x*}` — value of derivative at point `x*`

#### Vector / matrix / metric symbols
- `(p, x) = Σ p_i x_i` — scalar product of vectors `p, x ∈ R^n`
- `det(A)` or `|A|` — determinant of matrix A
- Euclidean / Non-Euclidean metric (distance)
- Euclidean / Non-Euclidean norm
- `t` — time as discrete variable; `t ∈ [0, +∞)` — time as continuous variable
- `∇f`, `grad f` — gradient of function f, where `∇f = (∂f/∂x_1, ..., ∂f/∂x_n)`

### Edge Cases & Caveats
- The codomain in `y = f(x)` is described in source as "Independent variable (value of function)" — context indicates this means the *dependent* output value (likely OCR/source phrasing artifact).

---

## Section: Greek Alphabet Reference 🟢
<!-- Reason: Reference table only. -->

### Core Idea
List of Greek letters likely to appear in the course. Source lists pairs of (lowercase symbol, name).

### Key Concepts

#### Greek letters listed
| Symbol | Name | Symbol | Name |
|---|---|---|---|
| α | Alpha | θ | Theta |
| β | Beta | λ | Lambda |
| γ | Gamma | π | Pi |
| δ | Delta | σ | Sigma |
| ε | Epsilon | χ | Chi |
| ψ | Psi | μ | Mu |
| ρ | Rho | ω | Omega |

### Connections
- Continues into: Block 4 title page; Unit 13 begins in Chunk 002.

> **Quick Recall:**
> - Volume 2 covers Blocks 4-6.
> - Block 4 = Real Analysis = Units 13-15.
> - Unit 13 begins on Volume 2 page 11.


---


## Section: 13.0 Objectives 🟢
<!-- Reason: Lists what the unit aims to teach; orients the reader. -->

### Core Idea
After completing Unit 13, the learner should be able to: explain real analysis as a discipline; explain the concept of a sequence and related concepts (term, length, subsequence); define and use well-known sequences (A.P., G.P., H.P.); characterise properties of sequences (boundedness, monotonicity, convergence, divergence, oscillation); define limit and limit point of a sequence; state and apply the Bolzano-Weierstrass theorem (for sequences and for sets) including in economic problem-solving; define open / closed / bounded / compact sets of reals; and apply function, limit and continuity ideas to several variables over `R^n`.

### Connections
- Builds on: Calculus (Block 3, Unit 9 — Limit and Continuity).
- Continues into: 13.1 Introduction (next).

---

## Section: 13.1 Introduction — What is Real Analysis 🟡
<!-- Reason: Conceptual framing; not exam-tested directly but defines the discipline and gives the two motivating "absurd result" examples (13.1, 13.2). -->

### Core Idea
Real Analysis is a branch of Mathematical Analysis restricted to the real numbers. It dominantly uses *analytical skills*: relating a hard problem to simpler sub-problems, solving the sub-problems, then reassembling the solution. Where Calculus *applies* rules (e.g., the Quotient Rule, the Fundamental Theorem of Calculus), Real Analysis *justifies* those rules — establishing when they are valid.

> **In Simple Terms:** Calculus is the "user manual" — it tells you which buttons to press. Real Analysis is the "engineering report" — it proves the buttons actually do what they claim, and warns you when the device will misbehave.

### Key Concepts

#### Analytical skills (recursive problem-solving)
The source describes three recursive steps:
1. Relate a hard problem to simpler problems and/or break it into sub-problems already solved.
2. Solve the simpler / sub-problems independently.
3. Reassemble the solutions of the sub-problems into a solution of the difficult problem.

Listed categories of analytical skills include logical reasoning, critical thinking, and data analysis.

#### Subject matter of Real Analysis
The study of behaviour and properties of:
- real numbers (R),
- sequences and series of real numbers, and
- real functions.

A function is called a **real function** if its domain is R or a subset of R containing an interval; it is **real-valued** if its codomain is R. Most studied functions are real-valued, but the codomain may be any non-empty set.

For sequences/series, the fundamental concept is **limit**, with **convergence** as another key notion. For functions, the fundamental concepts include limit, **continuity**, **differentiability**, and **integrability**.

#### Difference between Calculus and Real Analysis
Both share concepts (limit, continuity, derivative, integral), but they approach them differently:
- Calculus *applies* rules (e.g., Quotient Rule `d(u/v)/dx = (v du/dx − u dv/dx) / v²`, Fundamental Theorem of Calculus).
- Real Analysis *provides theoretical foundations and justifications* — for example, justifying that `d(u/v)/dx` exists and that the Quotient Rule is true; or proving the Fundamental Theorem of Calculus.

#### Application domains
Natural sciences, social sciences, engineering — anywhere the notion of continuous change is significant. In economics specifically: expected utility theory, welfare economics, financial economics, cooperative games (e.g., the Nash Bargaining Solution).

### Examples

**Example 13.1 — Why "trick" methods need theoretical conditions**
For the series `S = 1 + (1/2) + (1/2)² + (1/2)³ + ...`, the trick is:
- Let `S = 1 + (1/2) + (1/2)² + (1/2)³ + ...`
- Then `2S = 2 + [1 + (1/2) + (1/2)² + ...] = 2 + S`
- So `2S − S = 2`, giving `S = 2`. ✓ correct

Now apply the same method to `S' = 1 + 2 + 2² + 2³ + ...`:
- `2S' = 2[1 + 2 + 2² + ...] = 2 + 2² + 2³ + ... = S' − 1`
- So `S' = −1`, which is **completely absurd** (a sum of positive numbers cannot be negative).

**Lesson:** the method is valid only under certain conditions (in this case, |r| < 1). Determining those validity conditions is the job of Real Analysis; applying the method under those conditions is the job of Calculus.

**Example 13.2 — Limit of `(y)^n` argument**
Let `L = lim_{n→∞} (y)^n`. Letting `m = n+1`:
- `L = lim_{n→∞} (y)^{n+1} = lim_{n→∞} y · (y)^n = y · lim_{n→∞} (y)^n = y · L`.
- So `(y − 1) L = 0`, implying either `y = 1` or `L = 0`.

This argument apparently shows `lim_{n→∞} (y)^n = L = 0` for all `y ≠ 1`. **But** taking `y = 2` gives the limit of `2, 4, 8, 16, ...` as zero, which is absurd. Again, explaining the absurdity is the job of theory (Real Analysis).

### ⚠️ Common Mistakes
- ❌ Applying `S = 1 + r + r² + ...` ⇒ `S = 1/(1−r)` to any `r` → ✅ Only valid when `|r| < 1` (series converges).
- ❌ Manipulating `lim (y)^n` algebraically without checking it exists → ✅ The limit might not exist (e.g., `y = 2`), so the manipulation is invalid.

### Connections
- Builds on: Calculus rules (Block 3); requires `|r| < 1` condition that will be formalized via convergence (Section 13.3.3, Chunk 003).
- Continues into: 13.2 Sequences (next).

---

## Section: 13.2 Sequences — Set & Function Conceptualisations 🔴
<!-- Reason: Foundational definitions used throughout the unit. Notation, indexing set, subsequence, length, recursive definability are all listed in objectives. -->

### Core Idea
A *sequence* is an ordering of entities, one after another. It can be viewed in two equivalent ways: (i) as a special kind of (ordered, enumerated, repetition-allowing) set; or (ii) more formally as a function `f: S → R` whose domain `S` is some subset of the integers and whose codomain is R (or any non-empty set). The "values written in order" — `(f_1, f_2, f_3, ...)` — are what we usually refer to as the sequence.

> **In Simple Terms:** A sequence is a *list with a fixed order*. Whereas a set `{2, 4, 8}` doesn't care about order or duplicates, a sequence `(2, 4, 8, 4, 2)` does.

### Key Concepts

#### Notation
A sequence uses parentheses: `(1, 2, 4, 8, ...)`. A set uses braces: `{1, 2, 4, 8, ...}`. They are written similarly but the brackets distinguish them.

#### Set-type conceptualisation
A sequence is a sort of set, with three special properties:
1. It is **ordered**: `(E, V, I, L)` and `(V, I, L, E)` are *distinct* sequences from the same letter set `{E, I, V, L}`.
2. It is **enumerated**: all elements can be listed one after another (1st, 2nd, 3rd, ...). For example, `(0, 1, 4, 9, ...)` lists squares of integers in order. **R itself, or any sub-interval like [0, 1], cannot be represented as a sequence** under any relation, because `|R| > |N|` (R is uncountable).
3. It **allows repetition**: `(1, 2, 4, 2, 4)` is a valid sequence, even though `{1, 2, 4, 2, 4}` is not proper set notation.

#### Sequence as a function
A sequence of real numbers is a function `f: S → R` where:
- `S`, the domain, is either:
  - (a) the set N of natural numbers, or
  - (b) an interval subset of N, e.g. integers in [10, 20] or [10, ∞), or
  - (c) integers in finite extensions [−k, n] or [−k, ∞), for `k, n ∈ N`.
- The codomain may be R, or Q, Z, C, or any non-empty set.

We write `(f(1), f(2), f(3), ...) = (f_1, f_2, f_3, ...) = (f_n)_{n=1, 2, 3, ...}` or `(f_n)_{n ∈ N}`.

#### Indexing and rank
For `f: S → R`, the *indexing set* is `S`. The **index (or rank)** of an element `r ∈ R` is the `s ∈ S` with `f(s) = r`. *Index ≠ position in sequence*: e.g. for `ISQ_n = (2^{n²})` over `n ∈ [−10, 10]`, the element `2^{100}` has index `−10` (because `ISQ(−10) = 2^{(−10)²} = 2^{100}`), even though it appears 1st in the listing.

#### Length and finiteness
The **length** of a sequence is the number of occurrences of terms (counting repetitions). E.g., `(1, 0, 1, 0, 1, ...)` has *infinite* length even though the underlying set `{0, 1}` has only 2 elements. A sequence may be finite or infinite. A finite sequence with `n` elements is also called an **n-tuple**.

#### Subsequence
For a given sequence `(S_n)`, a sequence is its **subsequence** if:
1. it is obtained by deleting some terms of `(S_n)` — every term of the subsequence occurs somewhere in `(S_n)`, AND
2. the relative positions of remaining elements are preserved — if `S_p` and `S_q` are both kept and `S_p` precedes `S_q` in the original, then `S_p` precedes `S_q` in the subsequence.

Example: `(2, 4, 6, ...)` IS a subsequence of `(1, 2, 3, ...)`. But `(4, 2, 6, ...)` is NOT (order is disturbed).

#### Recursively definable sequence
A sequence `(a_n)` is **recursively definable** if the nth term can be obtained through a formula involving some or all of the previous terms.

Example: `(s_n) = (2^n)_{n ∈ N}`. Recursive definition: `s_1 = 2^1 = 2`, and `s_n = 2 · s_{n−1}` (since `2^n = 2 · 2^{n−1}`).

By default in this unit (unless stated otherwise), sequences `(S_n)` are indexed by `n ∈ N`, where 0 may be considered as belonging to N.

### Definitions
- **Sequence (set view)**: an ordered, enumerated set that allows repetition of elements. ⭐
- **Sequence (function view)**: a function `f: S → R` where `S ⊆ Z` is N or an interval subset of integers; written `(f_n) = (f(1), f(2), ...)`. ⭐
- **Indexing set**: the domain `S` in the functional representation.
- **Term / element**: a constituent of the sequence.
- **Index (rank)**: for an element `r` in the sequence, the unique `s ∈ S` with `f(s) = r`.
- **Length**: number of occurrences of terms (may be infinite).
- **n-tuple**: a finite sequence of length `n`.
- **Subsequence**: a sequence formed by deleting some terms of a given sequence without disturbing the relative order of the remaining ones. ⭐
- **Recursively definable**: nth term is given by a formula involving previous term(s). ⭐

### Examples

**Example 13.3 — Powers of 2 over all of N**
`ISQ: N → N`, with `ISQ(n) = 2^n` for all `n ∈ N`. Sequence is `(ISQ_1, ISQ_2, ISQ_3, ...) = (2, 4, 8, ...)`. Shorthand: `(2^n)_{n ∈ N}`.

**Example 13.4 — Powers of 2 that are two-digit integers**
`ISQ: [4, 9] → N`, `ISQ(n) = 2^n`. Images: `(2^4, 2^5, 2^6, 2^7, 2^8, 2^9) = (16, 32, 64, 128, 256, 512)`. Shorthand: `(2^n)_{4 ≤ n ≤ 9}`.

**Example 13.5 — Powers of 2 indexed on [−10, 10]**
`ISQ: [−10, 10] → N`, `ISQ(n) = 2^{n²}` for all `n ∈ [−10, 10]`. The images are `(2^{100}, 2^{81}, ..., 2^0, 2^1, 2^4, ..., 2^{100})`. Note that the element `2^{100}` appears twice (at `n = −10` and at `n = +10`) — illustrating that sequences allow repetition.

### ⚠️ Common Mistakes
- ❌ Treating `(4, 2, 6, ...)` as a subsequence of `(1, 2, 3, ...)` → ✅ Order must be preserved; this fails because 4 precedes 2 in the candidate but 2 precedes 4 in the original.
- ❌ Confusing "index" with "position in the listing" → ✅ Index is the input value `s ∈ S`; position is where it appears when listed.

### Edge Cases & Caveats
- R cannot be represented as a sequence under any ordering relation, because `|R| > |N|`.
- Even an interval like [0, 1] cannot be enumerated as a sequence — there is no "next real number after 0" under `<`.

### Connections
- Builds on: Sets and functions (Block 1, Unit 3 — Relations and Functions).
- Continues into: 13.2.4 Well-known Types (A.P., next).

---

## Section: 13.2.4(A) Arithmetic Progression (A.P.) 🔴
<!-- Reason: Named sequence type, formula listed in Key Words / objectives, used in Check Your Progress questions. -->

### Core Idea
For constants `a` and `d`, the sequence `a, a+d, a+2d, a+3d, ...` is called an **arithmetic progression** (A.P.). The constant `a` is the **initial term** and `d` is the **common difference**. Successive terms differ by exactly `d`. A.P.s are recursively definable: `t_n = t_{n−1} + d`.

> **In Simple Terms:** Climb a staircase where every step has the same height — that height is `d`, the starting step is `a`.

### Key Concepts

#### nth term formula
For an A.P. with initial term `t_1 = a` and common difference `d`:
```
t_n = a + (n − 1) · d
```

#### Sum of first n terms — formula and derivation
For an A.P. `(t_1, t_2, ..., t_n)`:
```
S_n = (n/2) · (t_1 + t_n)
```

For an A.P. with initial term `a` and common difference `d`:
```
S_n = (n/2) · [2a + (n − 1)d]      ... (I)
```

**Derivation (source argument):**
1. Write `S_n = t_1 + t_2 + ... + t_{n−1} + t_n`.
2. Reverse the order: `S_n = t_n + t_{n−1} + ... + t_2 + t_1`.
3. Add corresponding terms: `2 S_n = (t_1 + t_n) + (t_2 + t_{n−1}) + ... + (t_n + t_1)`.
4. Each pair sums to `(t_1 + t_n)` — for instance, `(t_2 + t_{n−1}) = [(t_1 + d) + (t_n − d)] = (t_1 + t_n)`.
5. Therefore `2 S_n = n (t_1 + t_n)`, so `S_n = (n/2)(t_1 + t_n)`.
6. Substituting `t_n = a + (n−1)d`: `S_n = (n/2)[2a + (n−1)d]`.

### Definitions
- **Arithmetic Progression (A.P.)**: a sequence `a, a+d, a+2d, a+3d, ...` for constants `a, d`. ⭐
- **Initial term `a`**: the first term `t_1`. ⭐
- **Common difference `d`**: the constant difference between consecutive terms `t_{n+1} − t_n`. ⭐

### Examples

**Example 13.6 — Two A.P.s and specific terms**
- (i) `3, 7, 11, 15, ...` is an A.P. with `a = 3`, `d = 4`. The 40th term is `t_40 = 3 + (40 − 1) × 4 = 3 + 156 = 159`.
- (ii) `5, 3.5, 2, 0.5, −1, −2.5, ...` is an A.P. with `a = 5`, `d = −1.5`. The 21st term is `t_21 = 5 + (21 − 1) × (−1.5) = 5 − 30 = −25`.

### ⚠️ Common Mistakes
- ❌ Using `t_n = a + n · d` → ✅ Correct formula is `t_n = a + (n − 1) · d` (because `t_1 = a` requires the offset of 1).
- ❌ Forgetting that `d` can be negative (decreasing A.P.) → ✅ A.P.s with `d < 0` are perfectly valid (e.g., Example 13.6(ii)).

> **Quick Recall:**
> - A.P. nth term: `t_n = a + (n − 1)d`
> - A.P. sum: `S_n = (n/2)[2a + (n−1)d] = (n/2)(t_1 + t_n)`

### Connections
- Builds on: Sequences as functions (13.2.2, this chunk).
- Continues into: A.P. examples and Geometric Progression (Chunk 003: 13.2.4(A continued) A.P. Worked Sums).


---


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
- Builds on: A.P. sum formula (Chunk 002: 13.0 Objectives).
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
- Builds on: Recursively definable sequences (Chunk 002: 13.0 Objectives).
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
- Continues into: Bolzano-Weierstrass for sets and economic applications (Chunk 004: 13.4 Properties of Sets of Real Numbers — Intro).


---


## Section: 13.4 Properties of Sets of Real Numbers — Intro 🟡
<!-- Reason: Bridge from interval notation to general open / closed sets. -->

### Core Idea
The familiar interval concepts — open `]a, b[ = {x : a < x < b}`, closed `[a, b] = {x : a ≤ x ≤ b}`, semi-open / semi-closed `]a, b] = {x : a < x ≤ b}` — are now generalised to *sets* of real numbers. An open interval is "open" in the sense that we cannot pinpoint its boundary elements (e.g., 2 ∉ ]2, 4[ and there is no "next greater number" we can name); a closed interval is "closed" because its boundary elements (2 and 4 in `[2, 4]`) are included.

> **In Simple Terms:** Open = no edge included; closed = both edges included. We're now lifting these ideas from intervals to general sets.

### Connections
- Builds on: Interval concepts from earlier units.
- Continues into: 13.4.1 Open / Closed / Bounded / Compact Sets (next).

---

## Section: 13.4.1 Open Set, Closed Set, Bounded Set, Compact Set 🔴
<!-- Reason: All four definitions are listed in Key Words and in Unit Objectives. Compact = closed + bounded is a foundational result in real analysis. -->

### Core Idea
Four key set-theoretic properties of subsets of R:
- **Open**: every member has a small open interval around it that is contained in the set ⇒ no member is a boundary point.
- **Closed**: complement (in R) is open.
- **Bounded**: set is sandwiched between two real numbers (one upper bound, one lower bound).
- **Compact**: closed AND bounded.

Crucially, **the only two sets that are both open and closed are ∅ and R itself.**

> **In Simple Terms:** Open = "every point sits comfortably inside, with elbow room". Closed = "the complement has elbow room everywhere". Bounded = "fits in a finite stretch". Compact = closed + bounded — the most well-behaved kind.

### Definitions
- **Open set**: A set `S ⊆ R` is **open** if for each `a ∈ S`, ∃ `ε > 0` such that the open interval `]a − ε, a + ε[ ⊆ S`. Equivalently, every member of `S` is well inside `S` and no member is a boundary point. ⭐
- **Closed set**: A set `S ⊆ R` is **closed** if `R − S = (−∞, +∞) − S` is open. ⭐
- **Bounded set**: `S` is **bounded** if it is both bounded above (∃ real `M`: `x ≤ M` ∀ `x ∈ S`) and bounded below (∃ real `M'`: `M' ≤ x` ∀ `x ∈ S`). ⭐
- **Compact set**: A subset of R is **compact** if it is both closed and bounded. ⭐

### Examples

**Example 13.18 — Open sets**
(i) Every open interval `A = ]a, b[` is an open set. *Proof sketch:* Let `x ∈ A`. Then `a < x < b`, so `(x − a) > 0` and `(b − x) > 0`. Let `ε = min((x − a), (b − x)) > 0`. Then `]x − ε, x + ε[ ⊆ ]a, b[`.

(ii) The union of open intervals is an open set. (Demonstrated for two intervals; argument extends to any number.) *Proof sketch:* Let `A = ]a_1, b_1[ ∪ ]a_2, b_2[` (assume `b_1 < a_2`, else they merge). For any `x ∈ A`, `x` is in one of the two intervals; apply (i) to that interval to get the required ε-ball.

**Example 13.19 — Closed sets**
(i) Every closed interval `A = [a, b]` is closed. *Proof:* `R − [a, b] = (−∞, a) ∪ (b, +∞)`. Each piece is an open interval (hence open), and the union of open sets is open. So the complement is open ⇒ `[a, b]` is closed.

(ii) Every finite set `{a_1, a_2, ..., a_n}` is closed. *Proof for `n = 3`:* `R − {a_1, a_2, a_3} = (−∞, a_1) ∪ (a_1, a_2) ∪ (a_2, a_3) ∪ (a_3, +∞)`. Each is open, union is open, so the finite set is closed. *(Source notation actually shows three intervals; the argument generalises straightforwardly.)*

**Example 13.20 — Bounded sets**
(1) Each of the following is bounded:
- (i) `[3, 10^{10}]` — bounds 3 (lower) and `10^{11}` (one upper bound, among others).
- (ii) `[−10^{10}, 1000]` — bounds −10^{10} and 1000.
- (iii) `{1, 2, 10, 10000} ∪ [−10^{10}, 1000]` — bounds −10^{10} and 10000.

(2) Neither of the following is bounded:
- (i) `(−∞, 10)` — bounded above (e.g., by 10) but not below.
- (ii) `(100, ∞)` — bounded below (by 100) but not above.

**Example 13.21 — Compact sets**
Each of `[3, 10^{10}]`, `[−10^{10}, 1000]`, and `{1, 2, 10, 10000} ∪ [−10^{10}, 1000]` is both closed and bounded — hence compact.

### Key Concepts

#### Only ∅ and R are both open and closed
The empty set `∅` and `R` itself are the only two subsets of R that are simultaneously open and closed.

#### Compact = Closed + Bounded
This is the working definition for "compact" in this unit (which is the Heine-Borel characterisation in R, although the source doesn't name it).

### ⚠️ Common Mistakes
- ❌ Treating "not open" as equivalent to "closed" → ✅ Many sets are neither open nor closed (e.g., the half-open interval `[a, b[`); the only sets that are both are `∅` and `R`.
- ❌ Saying every bounded set is compact → ✅ Need *closed* AND bounded (e.g., `(0, 1)` is bounded but not closed, hence not compact).

> **Quick Recall:**
> - Open: every point has an ε-ball inside the set.
> - Closed: complement is open.
> - Bounded: fits between two reals.
> - Compact: closed AND bounded.
> - Both open and closed: only `∅` and `R`.

### Connections
- Builds on: Bounded sequence (Chunk 003 — same idea, generalised).
- Continues into: Bolzano-Weierstrass for sets (next).

---

## Section: 13.4.2 Bolzano-Weierstrass Theorem for Sets & Economic Applications 🔴
<!-- Reason: Named theorem listed in objectives and Key Words. Economic application is explicitly highlighted in source. -->

### Core Idea
The Bolzano-Weierstrass theorem for sets says: **every infinite and bounded set has a limit point.** This generalises the limit-point concept from sequences to sets. A *limit point* of a set is a point such that every open interval around it contains a point of the set distinct from itself — equivalently, every open interval around it contains *infinitely many* points of the set. Variations of this theorem are used in economics to prove existence of equilibria — e.g., the existence of a Pareto-efficient allocation.

> **In Simple Terms:** If a set has infinitely many points crammed into a finite stretch, somewhere those points must be "piling up" — that pile-up location is a limit point.

### Key Concepts

#### Bolzano-Weierstrass for sets
**Statement:** Every infinite and bounded set has a limit point.

#### Equivalent characterisation
A point `p` is a limit point of `S` if and only if for every `ε > 0`, the open interval `]p − ε, p + ε[` contains **infinitely many** points of `S`.

#### Synonyms for "limit point of a set"
A limit point of a set is also called an **accumulation point**, **condensation point**, or **cluster point**.

#### Economic application — Pareto-efficient allocation
The source quotes (paraphrased): *"There are different important equilibrium concepts in economics, the proofs of the existence of which often require variations of the Bolzano-Weierstrass theorem. One example is the existence of a Pareto-efficient allocation. The Bolzano-Weierstrass theorem allows one to prove that if the set of allocations is compact and non-empty, then the system has a Pareto-efficient allocation."* (Wikipedia, as cited in source.)

### Definitions
- **Limit point of a set `S`**: a real number `p` such that for every `ε > 0`, the open interval `]p − ε, p + ε[` contains a point of `S` different from `p`. Equivalently: contains infinitely many points of `S`. Also called accumulation / condensation / cluster point. ⭐

### Examples

**Example 13.22 — Limit points of intervals**
(i) For an interval `]a, b[`, `[a, b]`, `]a, b]`, or `[a, b[` — whether open, closed, or semi-open — *every point of the interval is a limit point of the interval*.

(ii) For an open interval `]a, b[`, or a semi-open interval `]a, b]` or `[a, b[`, **both boundary points `a` and `b` are also limit points**, even though `a` (in the first two) and `b` (in the last) are not in the interval.

### Edge Cases & Caveats
- Source theorem assumes **infinite** AND bounded — a finite bounded set has no limit point (e.g., `{1, 2, 3, 4}` has none).
- `N = {1, 2, 3, ...}` is infinite but unbounded, so the theorem doesn't apply — and indeed, N has no limit points.

> **Quick Recall:**
> - Bolzano-Weierstrass (sets): infinite + bounded ⇒ has a limit point.
> - Limit point ↔ accumulation / cluster / condensation point.
> - Used in economics to prove existence of Pareto-efficient allocations.

### Connections
- Builds on: Limit point of a sequence (Chunk 003: 13.2.4(A continued) A.P. Worked Sums); compact sets (this chunk).
- Continues into: Section 13.5 — Analysis of Several Variables.

---

## Section: 13.5 Analysis of Several Variables — Setup 🟡
<!-- Reason: Transition section. Sets up generalisation from R to R^n. -->

### Core Idea
So far, sequences, limits, continuity, derivatives, and integrals have been discussed in `R`. Section 13.5 extends/generalises some of these to `R^n`, the set of n-tuples of real numbers. The starting point is the concept of a function of several variables.

### Connections
- Builds on: All of Sections 13.2-13.4.
- Continues into: 13.5.1 Multivariable functions (next).

---

## Section: 13.5.1 Introduction to Multivariable Functions 🟡
<!-- Reason: Examples-driven introduction; underlying concepts are core but presentation is illustrative. -->

### Core Idea
A multivariable function is one whose value depends on more than one independent variable. Familiar examples: area of a rectangle (depends on length and breadth) and the compound-interest formula (depends on principal, rate, and time). Functional evaluation extends straightforwardly: substitute each independent variable's value.

### Examples

**Example 13.23 — Three illustrations**
(i) Area of a rectangle: `A = L × B`. `A` is a function of two variables `L`, `B`.

(ii) Money due at maturity: `M = DD · (1 + r)^t`, where `DD` is the demand deposit (money deposited), `r` the annual rate of interest, `t` the number of years. `M` is a function of three variables `DD`, `r`, `t`.

(iii) Functional evaluation: For `f(x, y) = 2x²y + 2y² − 3x`, find domain, range, and value at given points.
- **Domain:** `R × R` (defined for every pair `(x, y)`).
- **Range:** `R` (every real `u` is achievable: take `x = u/(−3)`, `y = 0` ⇒ `f(x, y) = u`).
- (a) `f(2, 3) = 2(2)²(3) + 2(3)² − 3(2) = 24 + 18 − 6 = 36`. *(Source-printed value: −48 + 18 + 6 = 24, indicating an OCR/printing error — the formula expanded gives `2·4·3 = 24`, `2·9 = 18`, `−3·2 = −6`, sum = 36. We follow the source's intermediate writing as displayed: `−48 + 18 + 6 = 24` with the caveat that intermediate values appear off.)*
- (b) `f(3, −2) = 2(3)²(−2) + 2(−2)² − 3(3) = −36 + 8 − 9 = −37`. *(Source prints `−108 + 8 − 9 = −109`, which is inconsistent with the formula — likely a different power was intended in the OCR. Reproducing source as written.)*

### Edge Cases & Caveats
- The numerical evaluations in Example 13.23(iii) as printed in the OCR'd source contain arithmetic that does not match the stated formula `f(x, y) = 2x²y + 2y² − 3x`. The likely intended formula uses higher powers (e.g., `2x²y³`). Verify against the original PDF.

### Connections
- Continues into: 13.5.2 R^n and Euclidean Space (next).

---

## Section: 13.5.2 R^n and Euclidean Space 🔴
<!-- Reason: Foundational definitions: R^n, vector operations, Euclidean distance, norm. Used throughout the rest of Block 4 and beyond. -->

### Core Idea
`R^n` is the n-fold Cartesian product of `R` with itself — its elements are **n-tuples** `(a_1, a_2, ..., a_n)`. R^n is given vector-space structure (addition, scalar multiplication, zero vector, additive inverse) and a metric structure via **Euclidean distance** and **Euclidean norm**.

### Definitions
- **R^n**: `R^n = {(a_1, a_2, ..., a_n) : a_i ∈ R}`. Elements are called **n-tuples**. ⭐
- **Vector addition**: For `x = (x_1, ..., x_n)`, `y = (y_1, ..., y_n)`: `x + y = (x_1 + y_1, x_2 + y_2, ..., x_n + y_n)`. ... (13.3) ⭐
- **Scalar multiplication**: For `r ∈ R`, `r·x = (r x_1, r x_2, ..., r x_n)`. ... (13.4) ⭐
- **Zero vector**: `0 = (0, 0, ..., 0)`.
- **Additive inverse**: `−x = (−x_1, −x_2, ..., −x_n)`.
- **Euclidean distance**: `d(x, y) = √[(x_1 − y_1)² + (x_2 − y_2)² + ... + (x_n − y_n)²]`. ... (13.5) ⭐
- **Euclidean norm**: `||x|| = √[(x_1)² + (x_2)² + ... + (x_n)²] = d(x, 0)`. ... (13.6) ⭐

### Key Concepts

#### From R² to R^n
First introduced for `R²`: `d((x_1, x_2), (y_1, y_2)) = √[(x_1 − y_1)² + (x_2 − y_2)²]`, and `||(x_1, x_2)|| = √[(x_1)² + (x_2)²]`. Then extended to general `R^n` by adding more squared-difference terms inside the square root.

#### Norm and distance are linked
Since `x − y = (x_1 − y_1, ..., x_n − y_n)`, we have:
```
||x − y|| = d(x, y)              ... (13.7)
```
i.e., the norm of the difference vector equals the Euclidean distance.

> **Quick Recall:**
> - `R^n = {(a_1, ..., a_n) : a_i ∈ R}`.
> - `d(x, y) = √Σ (x_i − y_i)²`.
> - `||x|| = √Σ x_i² = d(x, 0)`.
> - `||x − y|| = d(x, y)`.

### Connections
- Builds on: Cross product of two sets (Block 1, Unit 3).
- Continues into: 13.5.3 Functions over Euclidean spaces.

---

## Section: 13.5.3 Functions over Euclidean Spaces 🔴
<!-- Reason: Defines the family of functions used throughout the unit (vector addition, scalar product, projections, distance, norm). -->

### Core Idea
The vector operations and metric concepts of 13.5.2 can themselves be viewed as *functions* between Euclidean spaces. Plus, there are additional important functions: **scalar (dot) product** and **projection functions** that drop coordinates.

### Definitions
- **Vector addition function** `+: R^n × R^n → R^n`: `+((x_1, ..., x_n), (y_1, ..., y_n)) = (x_1 + y_1, ..., x_n + y_n)`. ... (13.8)
- **Scalar multiplication function** `·: R × R^n → R^n`: `r · (x_1, ..., x_n) = (r x_1, ..., r x_n)`. ... (13.9)
- **Distance function** `d: R^n × R^n → R`: `d(x, y) = √Σ (x_i − y_i)²`. ... (13.10)
- **Norm function** `||·||: R^n → R`: `||x|| = √Σ x_i²`. ... (13.11)
- **Scalar (dot) product function** `Scalar: R^n × R^n → R`: `Scalar((x_1, ..., x_n), (y_1, ..., y_n)) = x_1 y_1 + x_2 y_2 + ... + x_n y_n`. ⭐
- **Projection function** `R^k → R^m` (for `m < k`): drops some coordinates. E.g., `R_{1,2,3}: R^4 → R^3` with `R_{1,2,3}(x_1, x_2, x_3, x_4) = (x_1, x_2, x_3)`; `R_{2,3,4}(x_1, x_2, x_3, x_4) = (x_2, x_3, x_4)`; `R_{1,2}: R^5 → R^2`; `R_{3,5}(x_1, x_2, x_3, x_4, x_5) = (x_3, x_5)`.

### Examples

**Example 13.24 — Norm, distance, and scalar product on two 5-tuples**
Let `x = (2, −1, −3, 4, −2)` and `y = (3, −1, −3, 2, −3)`.

(i) **Norm of each:**
- `||x|| = √[2² + (−1)² + (−3)² + 4² + (−2)²] = √[4 + 1 + 9 + 16 + 4] = √34`.
- `||y|| = √[3² + (−1)² + (−3)² + 2² + (−3)²] = √[9 + 1 + 9 + 4 + 9] = √32`.

(ii) **Euclidean distance:**
- `d(x, y) = √[(2−3)² + (−1−(−1))² + (−3−(−3))² + (4−2)² + (−2−(−3))²]`
- `= √[1 + 0 + 0 + 4 + 1] = √6`.

(iii) **Scalar product:**
- `x · y = (2)(3) + (−1)(−1) + (−3)(−3) + (4)(2) + (−2)(−3) = 6 + 1 + 9 + 8 + 6 = 30`.

### Connections
- Builds on: 13.5.2 R^n and Euclidean Space.
- Continues into: 13.5.4 Concepts of Analysis in R^n.

---

## Section: 13.5.4 Concepts of Analysis in R^n — Open Disc, Closed Disc, etc. 🔴
<!-- Reason: Generalises every set-theoretic and analytic concept from R to R^n. Foundational for Unit 14 (Calculus of Several Variables) and Unit 15 (Metric Spaces). -->

### Core Idea
Most (but not all) concepts from R — limits, continuity, derivability, integrability, sequences, the Bolzano-Weierstrass theorem — extend to `R^n`. The key generalisations:
- A **sequence in R^n** has elements `s_i ∈ R^n`, i.e., each `s_i = (s_{i1}, s_{i2}, ..., s_{in})` with `s_{ij} ∈ R`.
- For limits, continuity, derivability: replace single real `x` with vector `x ∈ R^n`; replace `|x|` (absolute value) with `||x||` (norm); replace `|x − a|` (distance) with `d(x, a) = ||x − a||` (Euclidean distance).
- The notion of a "small open interval" `]a − ε, a + ε[` around a point becomes an **open disc** of radius ε.

> **In Simple Terms:** Wherever the 1-D analysis used `|·|`, just swap in `||·||` and "interval" becomes "disc/ball". Almost everything carries over.

### Definitions

#### Open / closed disc
- **Open Rectangle in R²**: `{(x_1, x_2) : a_1 < x_1 < b_1 and a_2 < x_2 < b_2}` with `a_i < b_i`. (Generalises to a "boundaryless cuboid" in `R^n`.)
- **Open Rectangle in R^n**: `{x = (x_1, ..., x_n) : a_i < x_i < b_i, i = 1, ..., n}` for fixed `a, b ∈ R^n`.
- **Open Disc of radius ε centered at `a`** in R^n: `{x = (x_1, ..., x_n) : ||x − a|| < ε}` for `ε > 0`. A "boundaryless sphere" in n-dimensional hyper-space. ⭐
- **Closed Disc of radius ε centered at `a`**: `{x ∈ R^n : ||x − a|| ≤ ε}`. Includes boundary points. ⭐

#### Open, closed, bounded, compact sets in R^n
- **Open set in R^n**: `S ⊆ R^n` is open if for each `a ∈ S`, ∃ an open disc of some radius `ε > 0` centered at `a` contained in `S`. Every member of `S` is well inside `S`. ⭐
- **Closed set in R^n**: `S ⊆ R^n` is closed if `R^n − S` is open. ⭐
- **Bounded subset of R^n**: `S` is bounded if it is bounded above and bounded below componentwise — i.e., ∃ reals `M, M'` such that `M' ≤ x_i ≤ M` for all `x = (x_1, ..., x_n) ∈ S` and for `1 ≤ i ≤ n`. ⭐
- **Compact set in R^n**: closed AND bounded. ⭐
- **Limit point of a subset of R^n**: `p = (p_1, ..., p_n) ∈ R^n` is a limit point of `S ⊆ R^n` if every open disc of radius `ε > 0` around `p` contains a point of `S` different from `p`. Also called accumulation / condensation / cluster point. ⭐

### Key Concepts

#### Limit and continuity for `f: R^n → R` (real-valued)
For `f: D → R` with `D ⊆ R^n` and a point `a = (a_1, ..., a_n) ∈ R^n`:
- **Limit:** `lim_{x → a} f(x)` exists and equals real number `l` iff for every `ε > 0`, ∃ `δ > 0` such that whenever `||x − a|| < δ`, then `|f(x) − l| < ε`.
  *(Note: `f(x)` and `l` are real numbers, not members of R^n.)*
- **Continuity at `a`:** `f` is continuous at `x = a` if (i) `lim_{x → a} f(x)` exists, AND (ii) `lim_{x → a} f(x) = f(a)`.

#### Open disc replaces interval, norm replaces absolute value
The structural change going from R to R^n is purely notational — `|·|` becomes `||·||`, `]a − ε, a + ε[` becomes the open disc. The ε-δ definition is otherwise identical.

> **Quick Recall:**
> - Open disc: `{x : ||x − a|| < ε}`.
> - Open set in R^n: every point has an open disc inside the set.
> - Compact in R^n: closed + bounded.
> - Limit `f: R^n → R`: ∀ε ∃δ such that `||x − a|| < δ ⇒ |f(x) − l| < ε`.

### Connections
- Builds on: Open / closed / bounded / compact in R (Section 13.4.1, this chunk); norm and distance (13.5.2).
- Continues into: Limit / continuity for `f: R^n → R^m`, Extreme Value Theorem (Chunk 005: 13.5.4(C) Limit and Continuity of `f: R^n → R^m`).


---


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
- Builds on: Limit / continuity for `f: R^n → R` (Chunk 004: 13.4 Properties of Sets of Real Numbers — Intro).
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
- Builds on: Continuity in R^n; closed disc; bounded set (Chunk 004: 13.4 Properties of Sets of Real Numbers — Intro).
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
- Builds on: Boundedness results stated informally in 13.3.1 (Chunk 003: 13.2.4(A continued) A.P. Worked Sums); Archimedean Property used implicitly in 13.3.3 (Example 13.14).
- Continues into: Unit 14 (Calculus of Several Variables).


---


## Section: Unit 13 Exercises Q4–Q9 (Continued) [🟡]
<!-- Reason: end-of-unit proofs reinforce sequence/set concepts; Fibonacci sum is a classical identity worth retaining -->

### Core Idea
The first part of the chunk closes Unit 13 by completing inductive proofs that the Fibonacci sequence is unbounded above (continuing from chunk 005), proving the sum identity for Fibonacci numbers, and showing simple bounded/closed-set facts. These exercises consolidate the tools (induction, complements, Archimedean property) used throughout Unit 13.

> **In Simple Terms:** A wrap-up of small proof exercises before the unit officially ends — Fibonacci grows without bound, its partial sums have a tidy closed form, and standard set facts get verified by going through complements.

### Key Concepts

#### Fibonacci sum identity
For all `n`, `Σ_{i=1..n} F_i = F_{n+2} − 1`. Proved by induction: base case `n=1` gives `F_1 = 0` and `F_3 − 1 = 1 − 1 = 0`; the induction step uses the hypothesis `Σ_{i=1..k} F_i = F_{k+2} − 1` and the recursion `F_{k+3} = F_{k+2} + F_{k+1}`.

#### Closed sets via complements
A union of two closed intervals `[a₁,b₁] ∪ [a₂,b₂]` (with `b₁ < a₂`) is closed because its complement `(−∞, a₁) ∪ (b₁, a₂) ∪ (b₂, +∞)` is a union of open intervals (open). The same trick shows an open interval `(a,b)` is not closed (its complement is a union of semi-open intervals) and a semi-closed interval `(a,b]` is not closed.

### Definitions
- **Fibonacci sequence (recursive)**: `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}` for `n ≥ 2`.

### Mechanisms / Processes
1. To show `F_n` is unbounded: prove inductively `F_{n+1} > F_n > n` for `n ≥ 7` → for any `M`, pick `n > M` so `F_n > M`.
2. Sum identity proof flow: base case → assume true at `k` → expand `Σ_{i=1..k+1} F_i = (F_{k+2} − 1) + F_{k+1} = F_{k+3} − 1`.

### Examples
**Q5 — Sum of first n Fibonacci terms**
- Claim: `Σ_{i=1..n} F_i = F_{n+2} − 1`.
- Base case `n=1`: `F_1 = 0`, and `F_3 − 1 = 1 − 1 = 0`. ✓
- Induction step: `Σ_{i=1..k+1} F_i = (F_{k+2} − 1) + F_{k+1} = F_{k+3} − 1`. ✓

**Q6 — Every finite set {a₁,…,aₙ} is bounded**
Take `m = min{a_i}`, `M = max{a_i}`. Then `m ≤ a_i ≤ M` for every `i`.

**Q7 — Union of two closed intervals is closed**
`R − ([a₁,b₁] ∪ [a₂,b₂]) = (−∞,a₁) ∪ (b₁,a₂) ∪ (b₂,+∞)` (each piece open) → complement is open → original is closed.

### Connections
- Builds on: Bolzano-Weierstrass and bounded sequences (Chunk 005: 13.5.4(C) Limit and Continuity of `f: R^n → R^m`)
- Ends Unit 13; the next sections begin Unit 14.

---

## Section: 14.0 Objectives & 14.1 Introduction [🟢]
<!-- Reason: scope-setting context only -->

### Core Idea
"Calculus of Several Variables" (also "Multivariable" or "Multivariate calculus") extends the calculus of one variable to functions of several variables. The unit will define and compute limits, partial derivatives (explicit, implicit, composite), directional derivatives, Jacobians, Hessians, the Mean Value Theorem and Taylor's theorem (and series) for both single and several variables.

> **In Simple Terms:** A roadmap: the unit takes everything you know from one-variable calculus and lifts it to functions that depend on many variables at once.

### Key Concepts

#### Limit is foundational
The concept of limit underlies every other concept of continuous mathematics — continuity, convergence, differentiation, integration. Extension of the limit concept from one variable to two variables is "surprisingly, much more complicated" than further extension from two to any finite number of variables (50, 100). For this reason, limit is treated first.

### Connections
- Builds on: Block 3 Calculus and Unit 13 Real Analysis.
- Continues into: Section 14.4 Partial Derivatives (Chunk 007: 14.4 Overview of Partial Derivatives & Higher Order Partial Derivatives [🟢]).

---

## Section: 14.2 The Concept of 'Limit' [🔴]
<!-- Reason: foundational concept; defines criterion for existence of limit in several variables -->

### Core Idea
The idea of "limit" is to assign **some** value to a function at a point where it may not be defined, but not arbitrarily — the assigned value must be consistent with the values at **all** neighbouring points. For a function of one variable a point can be approached from only two directions (LHS and RHS); for a function of two variables, from infinitely many directions. The limit exists only when values along all approaches reconcile.

> **In Simple Terms:** A limit is the "agreed-on" value at a point: every road into the point must lead to the same number. On the real line there are only two roads. In the plane there are infinitely many roads, which is why two-variable limits are much harder.

### Key Concepts

#### Why limits are defined
Functions can be undefined at points (e.g. `f(x) = (x²−25)/(x−5)` is undefined at `x=5` because the denominator vanishes). The limit assigns a "consistent" value: at neighbours `5±ε` we get `10±ε`, which agrees as `ε → 0`.

#### Single-variable: two directions only
On the real line, neighbours of `a` are `(a−ε)` and `(a+ε)`. If LHS and RHS limits agree, the limit exists.

- Case (i): `lim_{x→0} 1/x²` — both `1/(+ε)²` and `1/(−ε)²` blow up to `+∞`, agree → limit `= +∞`.
- Case (ii): `lim_{x→0} 1/x` — RHS goes to `+∞`, LHS goes to `−∞`, disagree → limit does not exist.

#### Two-variable case: infinitely many directions
A point `(a, b)` in `R²` may be approached along infinitely many paths. The existence of the limit at `(a, b)` depends on **conciliation of values at neighbouring points along potentially infinitely many directions.** Extension from 2 variables to `n>2` variables is essentially straightforward.

### Definitions
- **Limit (multivariable, intuitive)**: a value consistent with values at all neighbouring points along every direction of approach. ⭐
- **Notation**: `lim_{(x,y)→(a,b)} f(x,y)` (preferred) or `lim_{x→a, y→b} f(x,y)`.

### Connections
- Builds on: Unit 9 (Functions, Limits, Continuity, Block 3) and partial derivative limit definitions from Unit 11.
- Continues into: Computing limits (14.3) and limit-based derivatives (14.4).

---

## Section: 14.3 Computing Limit for Functions of Two or More Variables [🔴]
<!-- Reason: practical algorithm for limit computation; prerequisites for partial-derivative limits -->

### Core Idea
For multivariate limits, instead of testing infinitely many directions, exploit continuity: if the function is continuous at the point, limit equals the value at the point. If continuity fails because of a "problematic condition" (zero denominator, negative root, log of zero/negative), try to remove the issue algebraically; otherwise, find two paths that yield different proposed limits — that proves the limit does not exist.

> **In Simple Terms:** First check if the function is continuous at the point — if yes, just plug in. If something blows up, try to cancel it. If you can't cancel, try two different paths — if they disagree, the limit doesn't exist.

### Key Concepts

#### Continuity shortcut
A function `f(x, y)` is continuous at `(a, b)` iff `lim_{(x,y)→(a,b)} f(x,y) = f(a,b)`. Polynomials, trig, exp, log and combinations are continuous when continuous as one-variable functions (by setting `x=y` or treating one as constant). For continuous functions, "the required LIMIT at a point equals the VALUE at that point."

#### Problematic conditions
Watch for: (i) division by zero, (ii) square-rooting negative numbers, (iii) log of zero or negative numbers.

#### Removable problematic condition
Algebraically simplify so the singular factor cancels. E.g. `(x²−2xy+y²)/(x−y) = (x−y)` everywhere except on the line `x = y`; for limit computation the value on that line is irrelevant.

#### Path-testing for non-existence
If a problematic condition cannot be removed, suspect non-existence. Try two paths (e.g. `x=0`, `y=0`, `x=y`, `y=x²`). If two paths give different limits → limit does not exist. **Agreement on two paths does NOT prove existence.**

### Mechanisms / Processes
1. Check continuity (continuous → plug in).
2. If discontinuous, look for removable problematic conditions (factor and cancel).
3. If non-removable, test paths (`x=0`, `y=0`, `x=y`, etc.) — disagreement proves non-existence.

### Examples
**Example 14.1 — Plug-in via continuity**
`lim_{(x,y)→(1,3)} sin((π/2)x) + 3y² + 7`. The function is continuous everywhere, so `= sin(π/2) + 3(9) + 7 = 1 + 27 + 7 = 35`.

**Example 14.2 — Removable singularity**
`lim_{(x,y)→(1,1)} (x² − 2xy + y²)/(x² − y²)`. Denominator zero at `(1,1)`. Factor: `(x²−2xy+y²)/(x²−y²) = (x−y)/(x+y)` everywhere off `x=y`. Limit `= 0/2 = 0`.

**Example 14.3 — Non-existence via paths**
`lim_{(x,y)→(0,0)} xy/(3x² + y²)`.
- Path `x=0`: limit `= 0/y² = 0`. (14.1)
- Path `y=0`: limit `= 0/(3x²) = 0`. (14.2)
- Path `x=y`: `x·x/(3x²+x²) = 1/4`. (14.3)
Since (14.1) and (14.3) disagree, the limit does not exist.

### ⚠️ Common Mistakes
- ❌ Concluding the limit exists because two paths agree → ✅ Two-path agreement is necessary, not sufficient. Always try a non-trivial path (like `x=y` or `y=x²`) to attempt to break agreement.
- ❌ Plugging in directly when the denominator is zero → ✅ First check whether the singular factor can be cancelled.

### Edge Cases & Caveats
- Only the **value at the point itself is excluded** when computing the limit, so cancelling factors zero on the limit line/locus is legitimate.
- Continuity in each variable separately does not by itself guarantee continuity as a function of two variables; use the third bullet rule (continuous when one variable held constant **or** when `x=y`).

> **Quick Recall:**
> - Continuous → plug in.
> - Removable problematic condition → cancel and plug in.
> - Two paths disagree → limit DNE.
> - Two paths agree → inconclusive; try more.

### Connections
- Builds on: Section 14.2 (Chunk 006: Unit 13 Exercises Q4–Q9 (Continued) [🟡]) Concept of Limit.
- Continues into: Section 14.4 Partial Derivatives (Chunk 007: 14.4 Overview of Partial Derivatives & Higher Order Partial Derivatives [🟢]), where partial derivatives are themselves one-variable limits.

### Open Questions
1. Are there algorithmic / non-path-based criteria for proving existence of multivariable limits (e.g. polar-coordinate squeeze)? (Not covered here.)


---


## Section: 14.4 Overview of Partial Derivatives & Higher Order Partial Derivatives [🟢]
<!-- Reason: framing/recap section; orients the reader to the three forms of dependent-variable specification -->

### Core Idea
A dependent variable can be specified in three forms: (i) **explicitly** as a single function of the independent variables; (ii) **implicitly** in an equation where neither side is a single variable; (iii) as a **composition** (a non-circular chain of functional definitions). Partial derivatives arise only when a variable depends, directly or indirectly, on two or more variables.

> **In Simple Terms:** Same idea as a one-variable derivative, but only one input is allowed to wiggle while the others stay frozen. The form (explicit / implicit / chain) just changes the bookkeeping.

### Key Concepts

#### Three issues for multivariate derivatives
For functions of two or more variables we must address: (a) how the calculation procedure is modified, (b) how notation is modified, and (c) how the idea of "rate of change" evolves.

### Connections
- Builds on: Unit 11 (single-variable derivatives) and Unit 13 (limits, several real variables).
- Continues into: explicit partial derivatives (14.4.1) and the rest of section 14.4.

---

## Section: 14.4.1 Partial Derivative of Function with Explicit Representation [🔴]
<!-- Reason: defines partial derivative formally; sets all notation used through unit -->

### Core Idea
For `U = f(x, y)`, `f_x(x, y)` is the derivative of `f` w.r.t. `x` treating `y` as a constant; defined as the one-variable limit `lim_{h→0} [f(x+h, y) − f(x, y)]/h`. Similarly `f_y(x, y) = lim_{h→0} [f(x, y+h) − f(x, y)]/h`.

> **In Simple Terms:** Pretend the other variables are numbers (constants), and differentiate with the usual one-variable rules.

### Definitions
- **Partial derivative `f_x`**: `lim_{h→0} [f(x+h, y) − f(x, y)] / h`. ⭐
- **Partial derivative `f_y`**: `lim_{h→0} [f(x, y+h) − f(x, y)] / h`. ⭐
- **Alternative notations for `f_x`**: `∂f/∂x`, `∂U/∂x`, `D_x f`, `D_x f(x, y)`.

### Examples
**Example 14.4**

(i) `z = g(x, y) = 5x³ y⁴`
- `g_x(x, y) = ∂g/∂x = 5y⁴ · (3x²) = 15 y⁴ x²`
- `g_y(x, y) = (5x³)(4y³) = 20 x³ y³`

(ii) `v = h(x, y, w) = x² cos(y)/w`
- `∂v/∂x = 2x cos(y)/w`
- `∂v/∂y = (x²/w)(−sin(y)) = −(x² sin(y)/w)`
- `∂v/∂w = x² cos(y) · (−w⁻²) = −2 x² cos(y)/w³` *(source has minor OCR ambiguity but states "= −2 {x² cos(y)/w³}")*

### Connections
- Builds on: Section 14.2 limit concept.
- Continues into: implicit (14.4.2), composite (14.4.3), higher-order (14.4.4) cases.

---

## Section: 14.4.2 Partial Derivative of Function with Implicit Representation [🟡]
<!-- Reason: secondary mechanism — same idea, applied to implicit equations -->

### Core Idea
For an implicit relation among ≥ 3 variables, e.g. `2x⁴y³z² − 7x²y⁵z = x⁴ + y³`, you must (i) name the dependent variable and (ii) differentiate both sides treating other variables as constants, then collect terms in `∂z/∂x` and solve.

> **In Simple Terms:** Treat `z` as a hidden function of `x` (with `y` frozen). Differentiate both sides, gather all `∂z/∂x` terms on one side, and isolate.

### Mechanisms / Processes
1. State which variable is dependent.
2. Differentiate both sides w.r.t. the chosen independent variable, treating other independent variables as constants and using product/chain rule on terms involving the dependent variable.
3. Move all terms with the partial on LHS, others on RHS, factor and divide.

### Examples
**Implicit example (eq. 14.6 / 14.7):** `2x⁴y³z² − 7x²y⁵z = x⁴ + y³`.

For `∂z/∂x` (y constant):
- `2y³ · {(4x³)z² + x⁴(3z²)(∂z/∂x)} − 7y⁵ · {(2x)z + x²(∂z/∂x)} = 4x³`
- Collect `∂z/∂x` on LHS, the rest on RHS:
- `x · (6x³z² − 7y⁵) · (∂z/∂x) = x³(4 − 8z²) + 14 y³ z`  *(using OCR-cleaned form)*
- `∂z/∂x = {x³(4 − 8z²) + 14 y³ z} / [x(6x³z² − 7y⁵)]`

For `∂z/∂y` (x constant):
- `(2x⁴)(3z²)(∂z/∂y) − (7x²){5y⁴ z + y⁵ (∂z/∂y)} = 3y²`
- `∂z/∂y = (y²/x²)·{3 + 35 x² y³ z} / [6x²z² − 7 y⁵]` (per source).

### ⚠️ Common Mistakes
- ❌ Forgetting product rule on terms like `x⁴ z²` when differentiating w.r.t. `x` (since `z` depends on `x`) → ✅ Use `(4x³)z² + x⁴(2z)(∂z/∂x)`.

### Connections
- Builds on: 14.4.1 (explicit case).

---

## Section: 14.4.3 Chain Rule & Composite Functions [🔴]
<!-- Reason: chain rule is universal; partial-derivative chain rule is exam-critical -->

### Core Idea
The chain rule lets you compute derivatives of nested compositions by multiplying derivatives along the chain. For one independent variable: `dy/dx = (dy/dz)(dz/dw)(dw/dx)`. For partials, contributions through every dependency path are summed.

> **In Simple Terms:** "Peel" the composition from outside in, multiplying derivatives at each layer. With several variables, sum the contributions from every path that connects the inputs to the output.

### Key Concepts

#### 14.4.3.1 Chain rule for single independent variable
For `y = log(sin(eˣ + 7x²))`, set `z = sin(eˣ + 7x²)`, `w = eˣ + 7x²`, so `y = log z`, `z = sin w`, `w = eˣ + 7x²`. Then:
`dy/dx = (dy/dz)(dz/dw)(dw/dx) = [1/sin w][cos w][eˣ + 14x] = (eˣ + 14x) cot(eˣ + 7x²)`.

**Caution:** `dy/dx` is a single symbol — the slash is *not* a fraction. It is a notational accident that the chain rule looks like cancellation. The chain rule has been **proved**; it is not just symbolic cancellation.

#### 14.4.3.2 Chain rule for partial derivatives
**Case I:** `w(x, y)` with `x = x(t)`, `y = y(t)` (single parameter).
`dw/dt = (∂w/∂x)(dx/dt) + (∂w/∂y)(dy/dt)`

**Case II:** `w(x, y)` with `x = x(r, s)`, `y = y(r, s)`.
`∂w/∂r = (∂w/∂x)(∂x/∂r) + (∂w/∂y)(∂y/∂r)`
`∂w/∂s = (∂w/∂x)(∂x/∂s) + (∂w/∂y)(∂y/∂s)`

### Examples
**Example 14.6 — Single parameter case**
`w(x, y) = (2x + 3y)²`, `x = (t+1)^{1/2}`, `y = t²`.
`dw/dt = [2(2x+3y)·2] · (½)(t+1)^{−1/2} + [2(2x+3y)·3] · (2t)`.

**Example 14.7 — Two-parameter case**
`w(x, y) = (2x + 3y)²`, `x = (2r + s)^{1/2}`, `y = (r − 2s)²`.
`∂w/∂r = [4(2x+3y)] · (½)(2r+s)^{−1/2}(2) + [6(2x+3y)] · [2(r−2s)·1]`
`∂w/∂s = [4(2x+3y)] · (½)(2r+s)^{−1/2}(1) + [6(2x+3y)] · [2(r−2s)·(−2)]`

### ⚠️ Common Mistakes
- ❌ Treating `dy/dx` as a fraction and "cancelling" `dz` with `dz` → ✅ The chain rule is a proved theorem; the notation is suggestive but not algebraic.

### Connections
- Builds on: 14.4.1 explicit derivatives.
- Continues into: total differentials (14.4.6) and Taylor multivariate (Chunk 009: 14.8.4 Maclaurin's Series [🔴]).

---

## Section: 14.4.4 Higher Order Partial Derivatives [🔴]
<!-- Reason: notation conventions are exam-critical; foundation for Hessian, Taylor, Young's theorem -->

### Core Idea
Partial derivatives are themselves functions; differentiating again gives second-order partials, and so on. Notation: in subscript form `f_xy` means "first `x`, then `y`"; in `∂` form `∂²f/(∂y ∂x)` means the same thing. **Suffix order rule:** later variables go on the **right** in `f_…` notation, on the **left** in `∂…` notation.

> **In Simple Terms:** Differentiate twice. The two notations read in opposite directions — be careful which one you use.

### Definitions
- **Second-order partial `f_{xx}`**: `∂²f/∂x² = ∂/∂x (∂f/∂x)`. ⭐
- **Mixed partial `f_{xy}`**: `∂/∂y(∂f/∂x) = ∂²f/(∂y ∂x)`. ⭐

### Mechanisms / Processes
1. Compute first-order partial `f_x`.
2. Treat it as a new function and partial-differentiate w.r.t. `x` or `y`.
3. Continue for third- and higher-order derivatives.

### Examples
For `z = f(x, y) = 5x³ y⁴`:
- `f_x = 15 y⁴ x²`, `f_y = 20 x³ y³`
- `z_{xx} = ∂²f/∂x² = 30 y⁴ x`
- `z_{xy} = ∂²f/(∂y ∂x) = 60 y³ x²`

### Edge Cases & Caveats
- The text remarks that first-order partials always have explicit form regardless of how the original function was given (explicit/implicit/composite). So the method for higher-order derivatives is the **explicit-case method** of 14.4.1.

### Connections
- Continues into: Hessian (14.6.3, Chunk 008), Taylor's theorem (14.8, Chunks 008–009).

---

## Section: 14.4.5 Interpretation of Partial Derivatives [🟡]
<!-- Reason: connects calculation to economic intuition (rate of change) -->

### Core Idea
`f_x(x, y)` is the rate of change of `f` as `x` changes with `y` held fixed; `f_y(x, y)` similarly with `y` varying. Sign indicates direction: positive → increasing in that variable, negative → decreasing. A function may simultaneously be increasing in one variable and decreasing in another at a point.

### Examples
**Example 14.8** — Is `f(x, y) = 2x³/(3y²)` increasing or decreasing at `(1, 3)`?
- `f_x = 4x²/(3y²)` ⇒ `f_x(1, 3) = (4/3)(1/9) > 0` → increasing in `x` (with `y` fixed).
- `f_y = −2 · (2x³/3) · y⁻³ = −2x³/y³` *(per source: `f_y = 6(2x³/3y²)/dy = [(2/3)·(−3)]/y³ = −2x³/y³`)*. Wait — but source uses `2x³/3 y²`. Let me re-state per source: `f_y(x, y) = −2x³/y³`. Then `f_y(1, 3) = −2/81 < 0` → decreasing in `y` (with `x` fixed).

### Connections
- Builds on: 14.4.1.
- Continues into: directional derivatives (14.5).

---

## Section: 14.4.6 Differential / Total Differential [🔴]
<!-- Reason: key formula appearing in Key Words list and used through optimization, integration, ODEs -->

### Core Idea
For one variable, `dy = f'(x) dx` (or `df = f'(x) dx`). For a function of several variables, the **total differential** sums each partial derivative times the corresponding variable's differential.

> **In Simple Terms:** Total change = sum of (rate of change in each direction) × (small step in that direction).

### Definitions
- **Total differential of `z = f(x, y)`**: `dz = f_x dx + f_y dy` (equivalently `df = f_x dx + f_y dy`). ⭐
- **Total differential of `w = h(x, y, z)`**: `dw = h_x dx + h_y dy + h_z dz`. ⭐

> **Quick Recall:**
> - 1 variable: `dy = f'(x) dx`
> - 2 variables: `dz = f_x dx + f_y dy`
> - 3 variables: `dw = h_x dx + h_y dy + h_z dz`

### Connections
- Plays significant role in Integral Calculus and Differential Equations (per text).
- Builds on: 14.4.1.

---

## Section: 14.5 Directional Derivatives (start) [🔴]
<!-- Reason: named formula, central to gradient and continued throughout unit -->

### Core Idea
Partial derivatives only measure change in axis-aligned directions. The **directional derivative** measures the rate of change of `f(x, y)` along an arbitrary unit direction `Â` making angle `θ` with the positive `x`-axis. By a stated (unproved) result, for a differentiable `f`, `D_Â f(x, y) = f_x cos θ + f_y sin θ`, which equals the dot product of the gradient `∇f = ⟨f_x, f_y⟩` with the unit vector `⟨cos θ, cos(π/2 − θ)⟩`.

> **In Simple Terms:** Pick a direction. The directional derivative is how fast the function changes if you walk one unit step in that direction. It's just the gradient dotted with the unit direction vector.

### Definitions
- **Directional derivative (formal)**: `D_A f(x, y) = lim_{|A|→0} [f(x + |A| cos θ, y + |A| sin θ) − f(x, y)] / |A|`. ⭐
- **Gradient `∇f`**: the vector `⟨f_x, f_y⟩`. ⭐
- **Formula (differentiable f)**: `D_Â f(x, y) = f_x cos θ + f_y sin θ = ⟨f_x, f_y⟩ · ⟨cos θ, cos(π/2 − θ)⟩ = ∇f · Â`. ⭐

### Examples
**Example 14.9 (start)** — `f(x, y) = x² e^{xy} + 3y²` at `(0, 2)` along unit vector `Û` in direction `θ = 2π/3`.
- `Û = ⟨cos(2π/3), sin(2π/3)⟩ = ⟨−½, (√3)/2⟩`.
- `D_Û f(x, y) = −½ f_x + (√3/2) f_y`
  `= −½ {2x e^{xy} + x²y e^{xy}} + (√3/2){x³ e^{xy} + 6y}` *(per source)*
- At `(0, 2)`: `D_Û f(0, 2) = −½ · 0 + (√3/2)(0 + 12) = 6√3`.

### Connections
- Builds on: partial derivatives (14.4) and inner product (Section 6.4 of Unit 6).
- Continues into: 3-variable directional derivatives, Jacobian, Hessian (Chunk 008: 14.5 Directional Derivatives (continued — three variables) [🔴]).

### Open Questions
1. Why `cos(π/2 − θ)` for the second component of the unit vector — i.e. how is the same formula generalized to `n` axes via direction cosines? (Addressed in Chunk 008.)


---


## Section: 14.5 Directional Derivatives (continued — three variables) [🔴]
<!-- Reason: extends gradient/dot-product formula to n variables; central exam fact -->

### Core Idea
For a differentiable `f(x, y, z)`, the directional derivative along a unit vector `û = ⟨cos α, cos β, cos γ⟩` is `D_û f = f_x cos α + f_y cos β + f_z cos γ = ⟨f_x, f_y, f_z⟩ · ⟨cos α, cos β, cos γ⟩`. The cosines are the direction cosines (one per coordinate axis). For a non-unit vector `V`, normalize to get `û = V/‖V‖`.

> **In Simple Terms:** Same gradient-dot-direction formula as 2D, just with more components. The direction is given by the cosines of the angles your arrow makes with each axis.

### Definitions
- **Direction cosines**: `(cos α, cos β, cos γ)` — the angles a unit vector makes with the `x`, `y`, `z` axes. ⭐
- **Directional derivative (3 variables)**: `D_û f = f_x cos α + f_y cos β + f_z cos γ`. ⭐

### Mechanisms / Processes
1. Compute `‖V‖`.
2. Form unit vector `û = V/‖V‖`.
3. Compute partials `f_x, f_y, f_z`.
4. Take dot product `∇f · û`.

### Examples
**Example 14.10** — `f(x, y, z) = 2xz² + 3y² z − x²yz` along `V = ⟨−1, 0, 3⟩`.
- `‖V‖ = √((−1)² + 0² + 3²) = √10`.
- `û = ⟨−1/√10, 0, 3/√10⟩`.
- `D_û f(x, y, z) = (−1/√10) f_x + 0 · f_y + (3/√10) f_z = (−1/√10){2z² − 2xyz} + (3/√10){4xz + 6yz − x²y}` *(per source)*.

### Connections
- Builds on: 14.5 (Chunk 007: 14.4 Overview of Partial Derivatives & Higher Order Partial Derivatives [🟢]) — 2-variable directional derivative.
- Continues into: Jacobian (14.6) — generalizes the gradient row-vector to a matrix.

---

## Section: 14.6 Explicit Function from R^n to R^m, Jacobian Matrix, Hessian [🔴]
<!-- Reason: named matrices/definitions appearing in Key Words; central to optimization in MEC203 -->

### Core Idea
A function `f: R^n → R^m` can be written as `f(x) = (f_1(x), …, f_m(x))` with each `f_j: R^n → R`. The **Jacobian** `J_f` is the `m × n` matrix of all first-order partials `∂f_i/∂x_j`. When `n = m`, its determinant is the **Jacobian determinant** (used in multiple integrals). The **Hessian** of a scalar function `f: R^n → R` is the `n × n` matrix of all second-order partials `∂²f/(∂x_i ∂x_j)` and describes local curvature.

> **In Simple Terms:** Stack all gradients of all output components → Jacobian. Stack all second derivatives of one scalar output → Hessian.

### Key Concepts

#### 14.6.1 Function from R^n to R^m
For `f: R² → R⁴` defined by `f(x, y) = (x + y², 3x² − 5, x·y, 3y⁴)`, set `f_1(x, y) = x + y²`, `f_2(x, y) = 3x² − 5`, `f_3(x, y) = x·y`, `f_4(x, y) = 3y⁴`. In general, `f(x) = (f_1(x), …, f_m(x))`, each component a real-valued function on `R^n`.

#### 14.6.2 Jacobian / Jacobian matrix
The `nm` partial derivatives `∂f_i/∂x_j` for `i = 1,…,m`, `j = 1,…,n` are assumed to exist. The **Jacobian** is the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`. The `i`-th row of `J_f` is `∇f_i = [∂f_i/∂x_1, …, ∂f_i/∂x_n]`. Alternative notations: `D f`, `J_f`, `∇f`, `∂(f_1,…,f_m)/∂(x_1,…,x_n)`.

#### Jacobian determinant
If `n = m`, the Jacobian matrix is square, so its determinant is defined and called the **Jacobian determinant** (or just "Jacobian"). It is useful in evaluating multiple integrals. The text notes the ambiguity that "Jacobian matrix" is also sometimes called just "Jacobian".

#### 14.6.3 Hessian
For `f: R^n → R` mapping `x = (x_1, …, x_n)` to `f(x) ∈ R`, the Hessian `H_f` is the `n × n` matrix with `(i, j)` entry `∂²f/(∂x_i ∂x_j)`. **Hessian matrix describes the local curvature of a function of many variables.**

### Definitions
- **Jacobian of `f: R^n → R^m`**: the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`, `i = 1,…,m`, `j = 1,…,n`. ⭐
- **Jacobian determinant**: when `n = m`, the determinant `det(J_f)`; useful in multiple integrals. ⭐
- **Hessian of `f: R^n → R`**: the `n × n` matrix of second partials, `H_f[i,j] = ∂²f/(∂x_i ∂x_j)`. ⭐

### Examples
**Example 14.11 — Jacobian**
`f: R² → R²`, `f(x, y) = (e^{xy²}, 2x² + 3y²)`.
- `f_1(x, y) = e^{xy²}`, `f_2(x, y) = 2x² + 3y²`.
- `J_f = [[ y² e^{xy²},  2xy e^{xy²} ], [ 4x, 6y ]]`. *(per source: ∂f₁/∂x = y²e^{xy²}; ∂f₁/∂y = 2xy e^{xy²}; ∂f₂/∂x = 4x; ∂f₂/∂y = 6y)*
- At `(2, 1)`: `J_f(2, 1) = [[ e², 4e² ], [ 8, 6 ]]`. *(per source: 2e⁴ in first row, but transcript shows `[2e^4 4e^4 / 8 6]` — keep per source)*

**Example 14.12 — Hessian**
`f: R² → R`, `f(x, y) = e^{xy²}`.
- First partials: `∂f/∂x = y² e^{xy²}`, `∂f/∂y = 2xy e^{xy²}`.
- Second partials:
  - `∂²f/∂x² = y⁴ e^{xy²}`
  - `∂²f/(∂x ∂y) = (2y + 4xy³) e^{xy²} = 2y(1 + 2xy²) e^{xy²}` (source written as `(2 + 4xy) e^{xy²}` after simplification of OCR: rendered as `(2 + 4xy)`)
  - `∂²f/∂y² = (2x + 4x²y²) e^{xy²} = 4x²·… e^{xy²}` (per source `4x²·e^{xy²}` plus mixed term)
- `H_f(2, 1)` per source `= [[ 4e², 10e² ], [ 10e², 16 e² ]]`.

### Connections
- Builds on: gradient (14.5).
- Continues into: Hessian's role in second-order Taylor expansion (Chunk 009: 14.8.4 Maclaurin's Series [🔴]) and in optimization (Unit 15).

---

## Section: 14.7 Mean Value Theorem [🔴]
<!-- Reason: classical named theorem in Key Words list; basis for Taylor's theorem -->

### Core Idea
The MVT relates the average rate of change of a function over an interval to the instantaneous rate of change at some interior point. Geometrically, the tangent at some interior point is parallel to the secant joining the endpoints.

> **In Simple Terms:** If you average 60 km/h on a road trip, at some moment your speedometer must have read exactly 60.

### Key Concepts

#### History
A special case for inverse interpolation of sine was first described by Parameshvara (1380–1460) of the Kerala School of Astronomy and Mathematics. Now also called **Lagrange's Mean Value Theorem**.

#### 14.7.1 MVT for single variable
**Statement:** For real `a < b`, if `f: [a, b] → R` is continuous on `[a, b]` and differentiable on `(a, b)`, then there exists `c ∈ (a, b)` such that
`f'(c) = (f(b) − f(a))/(b − a)`.

**Geometric interpretation:** A continuous and (interior-)differentiable curve has at least one interior point where the tangent is parallel to the chord joining `(a, f(a))` and `(b, f(b))`.

#### 14.7.2 MVT for several variables (optional reading)
For `f: G → R` differentiable on an open set `G ⊆ R^n`, and `x, y ∈ G`, there exists `c ∈ (0, 1)` such that
`f(y) − f(x) = ∇f((1 − c)x + c y) · (y − x)`.

The point `(1 − c)x + c y` lies on the line segment from `x` to `y`, and `∇f · (y − x)` is the directional derivative along the chord.

### Definitions
- **Mean Value Theorem (single variable)**: continuous on `[a, b]`, differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`. ⭐
- **MVT (several variables)**: differentiable on open `G ⊆ R^n`; for `x, y ∈ G`, `∃ c ∈ (0,1)`: `f(y) − f(x) = ∇f((1 − c)x + c y) · (y − x)`. ⭐

### Examples
**Example 14.13** — `f(y) = 2y² + 3y + 4` on `[1, 2]`.
- Polynomial → continuous and differentiable everywhere → MVT applies.
- `f'(y) = 4y + 3`; at the MVT point `c`: `4c + 3 = (f(2) − f(1))/(2 − 1) = (18 − 9)/1 = 9`.
- `4c = 6` ⇒ `c = 3/2 ∈ (1, 2)`. ✓

### ⚠️ Common Mistakes
- ❌ Applying MVT to a function with a discontinuity in `[a, b]` → ✅ Continuity on closed interval is required.

### Connections
- Continues into: Taylor's theorem (14.8) — Lagrange-form remainder uses MVT.
- Used in Exercises 7 & 8 (Chunk 010): `f' ≡ 0 ⇒ f` constant; `f' > 0 ⇒ f` strictly increasing.

---

## Section: 14.8 Polynomial Approximation: Taylor's Theorem, Linear & Quadratic Approximations [🔴]
<!-- Reason: named theorem; fundamental tool; explicit Taylor formula in Key Words list -->

### Core Idea
Many "elementary" functions (`√x`, `x^{2/3}`, `eˣ`, `log x`, `sin x`) cannot be evaluated as rational numbers exactly even at simple inputs. They can however be **approximated** by polynomials, which are easy to evaluate (since `xⁿ` is rational when `x` is rational, but `eˣ` and `log x` typically aren't). Taylor's approach builds the approximating polynomial out of values of `f` and its derivatives at a known point `a`.

> **In Simple Terms:** If you know the function and its slopes at one point, you can build a polynomial that closely matches the function nearby — that's a Taylor polynomial. Adding higher-order terms makes the match better.

### Key Concepts

#### Why polynomials?
Polynomial values are rational when inputs are rational, regardless of degree, so they are computable. Other elementary functions (`eˣ`, `log x`) generally produce irrational outputs even from rational inputs.

#### 14.8.1 Taylor's polynomial of order `k`
Given `f(a), f'(a), f''(a), …, f^{(k)}(a)`,
`P_{k,a}(x) = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k`. ... (14.11)

Then **Taylor's formula** is `f(x) = P_{k,a}(x) + R_{k,a}(x)`, where `R_{k,a}(x)` is the **remainder term** representing the error of approximation. ... (14.12)

For "well-behaved" `f`, `lim_{x → a} R_{k,a}(x) = 0`.

#### Forms of the remainder (mentioned, may be skipped)
- **Peano's form**: `R_{k,a}(x) = h_{k,a}(x)·(x − a)^k`, with `lim_{x → a} h_{k,a}(x) = 0`.
- **Lagrange mean-value form**: `R_k(x) = (f^{(k+1)}(c)/(k+1)!)·(x − a)^{k+1}` for some `c` between `a` and `x`.
- **Cauchy's form**: `R_k(x) = (f^{(k+1)}(c)/k!)·(x − c)^k(x − a)`.

#### 14.8.2 Taylor's theorem (statement, no proof)
For integer `k ≥ 1`, if `f: R → R` is `k`-times differentiable at `a`, then there exists a function `R_k(x, a)` such that
`f(x) = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k + R_k(x, a)`,
and `lim_{x → a} R_k(x, a) = 0`. The function `R_k(x, a)` depends on `x`, `a`, and `f`.

#### 14.8.3 Taylor's series / expansion
For functions infinitely differentiable at `a` (like `eˣ`, `sin x`),
`f(x) = Σ_{n=0}^∞ (f^{(n)}(a)/n!)(x − a)^n`,
where `0! = 1` and `(x − a)⁰ = 1`. ... (14.13)

### Definitions
- **Taylor polynomial `P_{k, a}`**: `Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j`. ⭐
- **Taylor's formula**: `f(x) = P_{k,a}(x) + R_{k,a}(x)`. ⭐
- **Remainder term `R_{k,a}(x)`**: error of polynomial approximation; depends on `k`, `a`, `f`. ⭐
- **Taylor's series**: infinite version of Taylor's polynomial when `f` has all derivatives at `a` and `R_k → 0`. ⭐

> **Quick Recall:**
> - `P_{k,a}(x) = Σ_{j=0}^k f^{(j)}(a)·(x − a)^j / j!`
> - `f(x) = P_{k,a}(x) + R_{k,a}(x)`
> - For nice `f`, `R_{k,a}(x) → 0` as `x → a`.

### Connections
- Builds on: MVT (14.7) — supplies the Lagrange remainder.
- Continues into: Maclaurin series (14.8.4), linear/quadratic approximation (14.8.5), and multivariate Taylor (14.9) — all in Chunk 009.

### Open Questions
1. The remainder forms (Peano, Lagrange, Cauchy) are stated but not used; under what conditions is each preferred? (Beyond scope of the unit.)


---


## Section: 14.8.4 Maclaurin's Series [🔴]
<!-- Reason: named special case; classical formula appearing in standard exam questions -->

### Core Idea
The **Maclaurin series** is the special case of Taylor's series with `a = 0`. Under the conditions of Taylor's theorem,
`f(x) = f(0) + f'(0) x + (f''(0)/2!) x² + (f'''(0)/3!) x³ + … + (f^{(n)}(0)/n!) xⁿ + …`. ... (14.14)

> **In Simple Terms:** Taylor expansion centred at 0.

### Definitions
- **Maclaurin series**: Taylor's series with expansion point `a = 0`. ⭐

### Connections
- Special case of: Taylor's series (14.8.3, Chunk 008).

---

## Section: 14.8.5 Linear / Quadratic Approximation [🔴]
<!-- Reason: directly used in optimization, regression, error analysis; explicit polynomials worth memorizing -->

### Core Idea
Truncating the Taylor polynomial at order 1 gives the **linear approximation** (a tangent-line approximation); truncating at order 2 gives the **quadratic approximation** (a parabolic approximation). Higher order → smaller expected error.

> **In Simple Terms:** Pick how many derivatives to use. Use 1 → straight-line approximation. Use 2 → parabolic approximation. The remainder shrinks as the order grows.

### Definitions
- **Linear approximation `P_{1, a}`**: `f(a) + f'(a)(x − a)`. (14.15) ⭐
- **Quadratic approximation `P_{2, a}`**: `f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)²`. (14.17) ⭐
- **Taylor's formula (linear)**: `f(x) = P_{1,a} + R_1(x, a)`, with `lim_{x→a} R_1 = 0`. (14.16)
- **Taylor's formula (quadratic)**: `f(x) = P_{2,a} + R_2(x, a)`, with `lim_{x→a} R_2 = 0`. (14.18)

### Mechanisms / Processes
1. Compute `f(a)`.
2. Compute `f'(a)` (and `f''(a)` for quadratic).
3. Plug into the polynomial template.
4. Error of approximation is `R_k(x)`.

### Examples
**Example 14.14 — `f(x) = sin(x)`**
Values at `x = 0`: `sin(0) = 0`, `f'(0) = cos(0) = 1`, `f''(0) = −sin(0) = 0`, `f'''(0) = −cos(0) = −1`. (14.19)

**Part (i) Linear approximation**: `P_{1, 0} = sin(0) + x · cos(0) = 0 + x = x`.

**Part (i) Quadratic approximation**: `P_{2, 0} = 0 + x·1 + (x²/2!)·0 = x`.

**Part (ii) Maclaurin expansion** — derivative values cycle `0, 1, 0, −1, 0, 1, …`. Substituting:
`sin(x) = 0 + x·1 + (x²/2!)·0 + (x³/3!)·(−1) + (x⁴/4!)·0 + (x⁵/5!)·1 + … = x − x³/3! + x⁵/5! − x⁷/7! + …`.

### ⚠️ Common Mistakes
- ❌ Forgetting that the quadratic approximation includes the linear part → ✅ `P_{2,a} = P_{1,a} + (f''(a)/2!)(x − a)²`.

> **Quick Recall:**
> - `sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + …`
> - `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + …` (derived in Chunk 010 CYP4 Q3)
> - `log(x)` around `x = 1`: `(x − 1) − (x − 1)²/2 + (x − 1)³/3 − …` (Chunk 010 CYP4 Q4)

### Connections
- Builds on: 14.8.1–14.8.3 (Chunk 008: 14.5 Directional Derivatives (continued — three variables) [🔴]).
- Continues into: multivariate linear/quadratic approximation (14.9.1, 14.9.2).

---

## Section: 14.9 Multivariate Polynomial Approximation: Taylor's Theorem, Linear Approximation [🔴]
<!-- Reason: multivariate Taylor is heavily used in optimization, econometrics, comparative statics -->

### Core Idea
Multivariate polynomial approximation generalizes Taylor's theorem to functions of two or more variables. Build-up is staged: first linear approximation in 2 variables, then quadratic, then arbitrary order in `n` variables.

### Key Concepts

#### 14.9.1 Linear approximation in two variables (order 1)
At point `(a, b)`:
`P_{1, (a, b)}(x, y) = f(a, b) + (x − a) f_x(a, b) + (y − b) f_y(a, b)`. ... (14.20)

Taylor's formula: `f(x, y) = P_{1, (a, b)} + R_1(x, y)`, provided `lim_{(x,y) → (a,b)} R_1(x, y) = 0`. ... (14.21)

Required: values of `f, f_x, f_y` at `(a, b)`. Approximation called "linear" because `P_1` is degree one.

#### 14.9.2 Quadratic approximation in two variables (order 2)
At point `(a, b)`:
`P_{2, (a, b)}(x, y) = f(a, b) + {(x − a) f_x(a, b) + (y − b) f_y(a, b)} + {((x − a)²/2!) f_{xx}(a, b) + (x − a)(y − b) f_{xy}(a, b) + ((y − b)²/2!) f_{yy}(a, b)}`. ... (14.22)

Taylor's formula: `f(x, y) = P_{2, (a, b)} + R_2(x, y)`, with `lim_{(x,y)→(a,b)} R_2 = 0`. ... (14.23)

**Necessary condition for (14.23):** `f` has continuous first- and second-order partials at `(a, b)`.

In practice, "generally we use at most quadratic approximation."

#### 14.9.3 General Taylor's theorem (n variables, order k) — optional
For `F: R^n → R` and points `x = (x_1, …, x_n)`, `a = (a_1, …, a_n)`,
`P_k(x, a) = F(a) + Σ_{i} F_{x_i}(a)(x_i − a_i) + (1/2!) Σ_{i, j} F_{x_i x_j}(a)(x_i − a_i)(x_j − a_j) + … + (1/k!) Σ_{i_1, …, i_k} F_{x_{i_1} … x_{i_k}}(a)(x_{i_1} − a_{i_1}) … (x_{i_k} − a_{i_k})`. ... (14.24)

**Theorem:** there exists `R_k(x, a)` such that `F(x) = P_k(x, a) + R_k(x, a)` and `lim_{x → a} R_k(x, a) = 0`. ... (14.25) Error of approximation is `R_k(x, a)`.

The argument extends straightforwardly to `f: R^n → R^m` componentwise: `f = (f_1, …, f_m)`.

#### 14.9.3.1 Multivariate Taylor's series expansion
For functions infinitely differentiable at `a` (like `e^{x+y+z}`),
`F(x) = Σ_{k=0}^∞ (1/k!) Σ_{i_1, …, i_k} F_{x_{i_1} … x_{i_k}}(a) · (x_{i_1} − a_{i_1}) … (x_{i_k} − a_{i_k})`.

### Definitions
- **Linear (Taylor) approximation 2 variables**: `P_{1, (a,b)} = f(a,b) + (x−a) f_x(a,b) + (y−b) f_y(a,b)`. ⭐
- **Quadratic (Taylor) approximation 2 variables**: as in (14.22). ⭐
- **General Taylor polynomial of order `k` in `n` variables**: as in (14.24).

### Mechanisms / Processes
1. Compute `f(a)` and all required partials of order ≤ `k` at `a`.
2. Substitute into the order-`k` Taylor polynomial.
3. The remainder term provides the error.

### Examples
**Example 14.15 — Order-3 Taylor polynomial of `F(x_1, x_2, x_3) = e^{x_1 + x_2 + x_3}` near (0, 0, 0).**

All partials of `F` equal `e^{x_1 + x_2 + x_3}`, so at `(0, 0, 0)` every value is `1`:
`F(0,0,0) = 1`, `F_{x_i}(0,0,0) = 1`, `F_{x_i x_j}(0,0,0) = 1`, `F_{x_i x_j x_k}(0,0,0) = 1` for all `i, j, k`.

Substituting in (14.24) with `n = 3, k = 3, a = (0, 0, 0)`:
`F(x) = 1 + (x_1 + x_2 + x_3) + (1/2!)(x_1 + x_2 + x_3)² + (1/3!)(x_1 + x_2 + x_3)³`.

**Example 14.16 — Taylor series for `f(x, y, z) = xyz` around `(1, 1, 1)`.**
- `f(1, 1, 1) = 1`.
- First partials: `f_x = yz`, `f_y = xz`, `f_z = xy`; each `= 1` at `(1, 1, 1)`.
- Pure second partials all zero (`f_{xx} = f_{yy} = f_{zz} = 0`); mixed second partials: `f_{xy} = z`, `f_{xz} = y`, `f_{yz} = x`; each `= 1` at `(1, 1, 1)`.
- Third partial: only `f_{xyz} = 1` is non-zero; all others zero.
- Fourth and higher: all zero.

Substituting:
`f(x, y, z) = 1 + {(x − 1) + (y − 1) + (z − 1)} + (1/2)·2·{(x − 1)(y − 1) + (y − 1)(z − 1) + (x − 1)(z − 1)} + (1/3!)·6·{(x − 1)(y − 1)(z − 1)} + 0 + …`
`= 1 + (x − 1) + (y − 1) + (z − 1) + {(x − 1)(y − 1) + (y − 1)(z − 1) + (x − 1)(z − 1)} + (x − 1)(y − 1)(z − 1)`.

### ⚠️ Common Mistakes
- ❌ Forgetting the cross term `(x − a)(y − b) f_{xy}(a, b)` in the quadratic 2-variable Taylor → ✅ Always include it.
- ❌ Using the wrong factor `1/2!` for cross-terms — note the source formula uses `(x − a)(y − b) f_{xy}` with no `1/2!` because both off-diagonal entries `f_{xy}` and `f_{yx}` are summed.

> **Quick Recall (2-variable):**
> - Linear: `f(a,b) + f_x(a,b)(x − a) + f_y(a,b)(y − b)`
> - Quadratic adds: `½ f_{xx}(a,b)(x − a)² + f_{xy}(a,b)(x − a)(y − b) + ½ f_{yy}(a,b)(y − b)²`

### Connections
- Builds on: 14.4 partials, 14.4.4 higher-order partials, 14.8.5 single-variable approximations.
- Continues into: optimization (Unit 15) — second-order conditions use Hessian and quadratic Taylor.

---

## Section: 14.10 Let Us Sum Up [🟢]
<!-- Reason: recap material -->

### Core Idea
The unit covered: limits of multivariate functions, partial derivatives (explicit, implicit, composite via chain rule), higher-order partials, directional derivatives, Jacobian, Hessian, Mean Value Theorem (one and several variables), Taylor's theorem and series for one and several variables, with applications to polynomial approximation.

### Connections
- Recap of all sections in Unit 14.

---

## Section: 14.11 Key Words [🔴]
<!-- Reason: official examination terminology -->

### Definitions
- **Partial derivative**: derivative of a dependent variable `z` w.r.t. one or more of the variables `x, y, w, …` while treating at least one of them as a constant. ⭐
- **Unit vector specification (in `n`-D)**: `(cos θ_1, cos θ_2, …, cos θ_n)`, where `θ_i` is the angle the vector makes with the `i`-th axis. For `n = 2`, with `θ` the angle with `x`-axis, the unit vector is `(cos θ, cos(π/2 − θ))`. ⭐
- **Gradient `∇f`**: for `f` of `n` variables `x_1, …, x_n`, `∇f = ⟨f_{x_1}, …, f_{x_n}⟩`. ⭐
- **Directional derivative**: in multivariate calculus, the derivative along a chosen direction at a point. If `û = (cos θ_1, …, cos θ_n)` and `∇f = ⟨f_{x_1}, …, f_{x_n}⟩`, then `D_û f = ∇f · û`. ⭐
- **Jacobian**: for `f: R^n → R^m`, the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`. ⭐
- **Hessian**: for `f: R^n → R`, the `n × n` matrix of second partials. ⭐
- **Mean Value Theorem**: continuous on `[a, b]`, differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`. ⭐
- **Taylor's formula**: `f(x) = P_{k, a}(x) + R_{k, a}(x)`, where `P_{k, a} = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k`. ⭐

---

## Section: 14.12 Answers — Check Your Progress 1, Q1 [🟡]
<!-- Reason: worked exercise solution -->

### Examples
**CYP1 Q1** — `lim_{(x, y) → (4, 1)} 3 x y² / (x + y)`.

The function fails continuity along `x + y = 0`, but `(4, 1)` does not lie on that line. On the rest of the domain (including `(4, 1)`) the function is continuous, so the limit equals the value:
`lim = 3·(4)·(1)² / (4 + 1) = 12/5`.

### Connections
- Builds on: 14.3 continuity-based limit shortcut.


---


## Section: Check Your Progress 1 — Limit Computation Answers [🟡]
<!-- Reason: continued worked examples cementing 14.3 limit techniques -->

### Examples

**CYP1 Q2** — `lim_{(x, y) → (1, −1)} (x² + 2xy + y²)/(x² + y²)`. *(Per source notation; treat as written.)*

Function not continuous at `(1, −1)`: denominator factor zero on the relevant line. But except on the line `x + y = 0`, the function `(x² + 2xy + y²)/(x² − xy + y²)` *(per source's algebraic simplification)* equals `(x + y)/(x² − xy + y²)`. Limit at `(1, −1)`:
`= (1 + (−1)) / (1² − (1)(−1) + (−1)²) = 0/3 = 0`.

The limit is computed by removing the problematic condition (cancelling the singular factor on the line where the limit is taken).

**CYP1 Q3** — `lim_{(x, y) → (1, 1)} [2(1 − y) + 3(x − 1)] / (x − y)`.

Denominator zero at `(1, 1)` and no cancelling factor — limit may not exist. Test paths:
- Path `x = 1`: numerator `= 2(1 − y)`, denominator `= 1 − y`, ratio `= 2`. So limit along `x = 1` is `2`.
- Path `y = 1`: numerator `= 3(x − 1)`, denominator `= x − 1`, ratio `= 3`. So limit along `y = 1` is `3`.

Two paths give different proposed limits, so the limit **does not exist**.

### Connections
- Builds on: 14.3 (Chunk 006: Unit 13 Exercises Q4–Q9 (Continued) [🟡]).

---

## Section: Check Your Progress 2 — Partial Derivatives Answers [🟡]
<!-- Reason: worked solutions for partial-derivative manipulations -->

### Examples

**CYP2 Q1** — `z = 8x/(x² + 5y)`.
- `∂z/∂x = [8(x² + 5y) − 8x(2x)]/(x² + 5y)² = (8x² + 40y − 16x²)/(x² + 5y)² = (40y − 8x²)/(x² + 5y)²`.
- `∂z/∂y = 8x · [(−1)(x² + 5y)^{−2}·5] = −40x/(x² + 5y)²`.

**CYP2 Q2** — `f(x, y, z) = x sin(y)/z²`.
- `∂f/∂x = sin(y)/z²`.
- `∂f/∂y = x cos(y)/z²`.
- `∂f/∂z = x sin(y) · (−2)/z³ = −2 x sin(y)/z³`.

**CYP2 Q3** — `z = √(x² + log(5x − 3y²))`.
- `∂z/∂x = ½ · (x² + log(5x − 3y²))^{−1/2} · {2x + 5/(5x − 3y²)}`.
- `∂z/∂y = ½ · (x² + log(5x − 3y²))^{−1/2} · {(−6y)/(5x − 3y²)} = −3y / [(5x − 3y²)·(x² + log(5x − 3y²))^{1/2}]`.

**CYP2 Q4** — Find `∂³f/(∂y ∂x²)` for `f(x, y) = e^{xy}`.
- `∂f/∂x = y e^{xy}`.
- `∂²f/∂x² = y² e^{xy}`.
- `∂³f/(∂y ∂x²) = ∂/∂y (y² e^{xy}) = (e^{xy}) · 2y + y² · x e^{xy} = (2y + x y²) e^{xy}`.

**CYP2 Q5** — `z = f(x, y) = 5x³ y³`. *(Note: source actually writes `5x³ y³` here, not `5x³ y⁴`.)*

From 14.4.4: `z_{xx} = 30 y³ x` *(per source: 30y⁴x — using earlier 5x³ y⁴ form)*. The source carries the worked example `z_{xx} = 30 y³ x`, `z_{xy} = 60 y² x²` (note: source mixes; reproduce literally):

Per source (matching 14.4.4 example with `5x³ y⁴`):
- `z_{xxx} = ∂/∂x(30 y⁴ x) = 30 y⁴`
- `z_{xxy} = ∂/∂y(30 y⁴ x) = 120 y³ x`
- `z_{xyx} = ∂/∂x(60 y³ x²) = 120 y³ x`
- `z_{xyy} = ∂/∂y(60 y³ x²) = 180 y² x²`
- For `z_{yyy}`: `z_y = 20 x³ y³`, `z_{yy} = 60 x³ y²`, `z_{yyy} = 120 x³ y`.

Note the equality `z_{xxy} = z_{xyx}` consistent with mixed-partials interchange.

**CYP2 Q6** — Directional derivative of `f(x, y) = x² tan(y) + 3x log(y)` at `(1, π/3)` along the unit vector `û` in direction `θ = π/4`.

`û = ⟨cos(π/4), sin(π/4)⟩ = ⟨1/√2, 1/√2⟩`.
`D_û f(x, y) = (1/√2) f_x + (1/√2) f_y = (1/√2)(f_x + f_y)`
`= (1/√2) [{2x tan(y) + 3 log(y)} + {x² sec²(y) + 3(x/y)}]`

At `(1, π/3)`:
`D_û f(1, π/3) = (1/√2) [2 tan(π/3) + 3 log(π/3) + sec²(π/3) + 9/π] = …`

### Connections
- Builds on: 14.4 (Chunk 007: 14.4 Overview of Partial Derivatives & Higher Order Partial Derivatives [🟢]).

---

## Section: Check Your Progress 3 — Jacobian & Hessian Answers [🟡]
<!-- Reason: worked solutions for matrix-of-partials -->

### Examples

**CYP3 Q1** — `f: R² → R³`, `f(x, y) = (sin x, 2xy, 3xy²)`.
- `J_f = [[cos x, 0], [2y, 2x], [3y², 6xy]]`.
- At `(1, π/2)`: `J_f(1, π/2) = [[cos 1, 0], [π, 2], [3π²/4, 3π]]`. *(per source's numeric forms)*

**CYP3 Q2** — `f: R³ → R³`, `f(x, y, z) = (2z + sin x, 2xy − z², 3xy² − 3z)`.
- `J_f = [[cos x, 0, 2], [2y, 2x, −2z], [3y², 6xy, −3]]`.
- At `(π, 1/2, 1)`: `J_f(π, 1/2, 1) = [[−1, 0, 2], [1, 2π, −2], [3/4, 3π, −3]]`. *(matches source values: cos π = −1; rows match the print)*

**CYP3 Q3** — `f: R² → R`, `f(x, y) = 3x² + 2y³`.
- First partials: `∂f/∂x = 6x`, `∂f/∂y = 6y²`.
- Hessian: `H_f = [[6, 0], [0, 12y]]`.
- At `(1, 2)`: `H_f(1, 2) = [[6, 0], [0, 24]]`.

### Connections
- Builds on: 14.6 (Chunk 008: 14.5 Directional Derivatives (continued — three variables) [🔴]).

---

## Section: Check Your Progress 4 — MVT, Linear/Quadratic Approximations & Maclaurin/Taylor Series [🟡]
<!-- Reason: capstone of Taylor section; classical formulas worth memorizing -->

### Examples

**CYP4 Q1 — MVT applied to `f(y) = y³ + 2y² − y` on `[−1, 2]`.**

Polynomial → conditions of MVT met. There exists `c ∈ (−1, 2)`:
`f'(c) = (f(2) − f(−1))/(2 − (−1)) = (14 − 2)/3 = 4`.
`f'(y) = 3y² + 4y − 1` ⇒ `3c² + 4c − 1 = 4` ⇒ `3c² + 4c − 5 = 0`.
Solutions: `c = (−4 ± √76)/6 = (−2 ± √19)/3`. Numerically `c_1 = 0.7863`, `c_2 = −2.1196`.
Only `c_1 ∈ (−1, 2)`, so `c = 0.7863`.

**CYP4 Q2 — MVT for `f(x) = x(x − 1)(x − 2)` on `[0, 1/2]`.**

Polynomial → conditions hold. `∃ c ∈ (0, 1/2)`:
`f'(c) = (f(1/2) − f(0))/(1/2) = (3/8 − 0)/(1/2) = 3/4`.
`f'(x) = (x − 1)(x − 2) + x(x − 2) + x(x − 1) = 3x² − 6x + 2`.
`3c² − 6c + 2 = 3/4` ⇒ `12c² − 24c + 5 = 0` ⇒ `c = (6 ± √21)/6`.
Only `c = 1 − √21/6` lies in `(0, 1/2)`. ✓

**CYP4 Q3 — `f(x) = cos(x)`: linear, quadratic, Maclaurin.**

Values at `x = 0`: `cos(0) = 1`, `f'(0) = −sin(0) = 0`, `f''(0) = −cos(0) = −1`, `f'''(0) = sin(0) = 0`.

- **Linear approximation**: `P_{1, 0} = cos(0) + x · (−sin 0) = 1 + 0 = 1`.
- **Quadratic approximation**: `P_{2, 0} = 1 − x²/2!`.
- **Maclaurin series**: derivative cycle `1, 0, −1, 0, 1, …`, so
  `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + x⁸/8! − …`.

**CYP4 Q4 — `f(x) = log x` around `x = 1`: linear, quadratic, Taylor series.**

(`log x` is undefined at `0` so Maclaurin fails — only Taylor at `a = 1` is defined.)

Values at `x = 1`: `log(1) = 0`, `f'(1) = 1/x|_{x=1} = 1`, `f''(1) = −1/x²|_{x=1} = −1`, `f'''(1) = 2/x³|_{x=1} = 2`.

- **Linear approximation**: `P_{1, 1} = 0 + (x − 1)·1 = (x − 1)`.
- **Quadratic approximation**: `P_{2, 1} = (x − 1) + ((x − 1)²/2!)·(−1) = (x − 1) − (x − 1)²/2`.
- **General `k`-th derivative**: `f^{(k)}(\log x) = (−1)^{k−1} (k − 1)!/x^k`, so `f^{(k)}(1) = (−1)^{k−1}(k − 1)!`.
- **Taylor series at `a = 1`**:
  `log(x) = (x − 1) − (x − 1)²/2 + (x − 1)³/3 − (x − 1)⁴/4 + … + (−1)^{k−1}(x − 1)^k/k + …`.

> **Quick Recall:**
> - `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + …`
> - `log(x) at a=1 = (x−1) − (x−1)²/2 + (x−1)³/3 − …`

### Connections
- Builds on: 14.7 MVT and 14.8 Taylor (Chunk 008–009).

---

## Section: 14.13 Exercises (Q1–Q8) and Answers [🟡]
<!-- Reason: end-of-unit consolidation exercises -->

### Examples

**Q1 — `lim_{(x,y)→(0,0)} x⁴ y / (x⁸ + y⁴)`.**

Discontinuous at `(0, 0)` and no cancellable factor. Try paths:
- Paths `x = 0`, `y = 0` give 0 (insufficient).
- Path `x = y` (per source `x = y`): limit `= lim x⁴·x/(x⁸ + x⁴) = lim x⁵/(x⁸ + x⁴) = lim x/(x⁴ + 1) = 0`. *(per source equation (i))*
- Path `y = x²`: `x⁴·x² / (x⁸ + x⁸) = x⁶/(2x⁸) = 1/(2x²)` — wait, source gives `1/2` after simplification. Reading source literally: along `y = x²`, the limit `= lim 1/2 = 1/2`. (Source eq. (ii)).

Since (i) gives `0` and (ii) gives `1/2`, the limit does **not** exist.

**Q2 — `y = log(sin(eˣ + 7x²))`. Find `d²y/dx²`.**

From 14.4.3.1 (Chunk 007): `dy/dx = (eˣ + 14x) cot(eˣ + 7x²)`. Then
`d²y/dx² = (eˣ + 14) cot(eˣ + 7x²) + (eˣ + 14x) · {−csc²(eˣ + 7x²)}·(eˣ + 14x)`
`= (eˣ + 14) cot(eˣ + 7x²) − (eˣ + 14x)² csc²(eˣ + 7x²)`.

**Q3 — Water tank `V(t) = 5t² − 64t + 45`** *(source has `Vy =5t- 64t +45` which OCR-renders the `t²` poorly; using interpretation consistent with `V'(t) = 10t − 64`).*

`V'(t) = 10t − 64`.
- (a) `V'(3) = 30 − 64 = −34 < 0` → volume **decreasing** at `t = 3`.
- (b) `V'(7) = 70 − 64 = 6 > 0` → volume **increasing** at `t = 7`.
- (c) Magnitude at `t = 3` is `34`, at `t = 7` is `6`. The volume is changing **faster at `t = 3`**.

**Q4 — Differentials.**
- (a) `y = x³ sin(5x)` *(per source `x sin(5x)` — but the answer key uses `3x²` so interpret as `x³ sin(5x)`)*: `dy = (3x² sin(5x) + 5x³ cos(5x)) dx`.
- (b) `f(w) = e^{w³}`: `df = (3w² e^{w³}) dw`. *(source: `df = 3 e^{w³} dw` — OCR drops `w²` superscript; interpret faithfully as `(3w² e^{w³}) dw`)*
- (c) `z = e^{x sin(y)}`: `dz = (sin(y) e^{x sin(y)}) dx + (x cos(y) e^{x sin(y)}) dy`.
- (d) `g(x, y, z) = x⁵ y³ / z⁴` *(per source's answer pattern)*: `dg = (5x⁴ y³/z⁴) dx + (3 y² x⁵ / z⁴) dy + (−4 x⁵ y³ / z⁵) dz`. *(Source displays `(5x*y'/z') dx + (3y' x/z') dy + (−2 x*y'/z') dz`; we follow the partial-derivative pattern faithfully.)*

**Q5 — Directional derivative of `f(x, y, z) = sin(yz) + log(x)` at `(1, 1, π)` along `V = ⟨1, 1, −1⟩`.**

`∇f = ⟨1/x, z cos(yz), y cos(yz)⟩`. *(per source)*
At `(1, 1, π)`: `∇f = ⟨1, π cos(π), cos(π)⟩ = ⟨1, −π, −1⟩`. *(source written as `<2, −2, −1>` due to OCR; the structure is gradient at the point)*
`‖V‖ = √3`. Unit vector `û = ⟨1/√3, 1/√3, −1/√3⟩`.
`D_û f = ∇f(1, 1, π) · û = (1 − π + 1)/√3 = (2 − π)/√3`. *(source-final form: `(−2)/(√3)` per its own numeric path; reproduce per source's algebra)*

Per source: `D_û f = (1/√3){2 − 2 + 1} = 1/√3`, but the displayed final answer is `(−2)/√3`. Reproduce per source: **final value = `(−2)/√3`** (source eq.).

**Q6 — Jacobian for `f(x, y) = (x log y, sin x, xy, y³)` at `(π/2, π/4)`.**

- `f_1 = x log y`: `∂_x = log y`, `∂_y = x/y`.
- `f_2 = sin x`: `∂_x = cos x`, `∂_y = 0`.
- `f_3 = xy`: `∂_x = y`, `∂_y = x`.
- `f_4 = y³`: `∂_x = 0`, `∂_y = 3y²`.

`J_f(π/2, π/4) = [[log(π/4), 2], [0, 0], [π/4, π/2], [0, 3π²/16]]` *(matching source's printed entries: `log(π/2)` row is `2`, `1/√2 0`, `π/4 π/16`, `0 3π²/4` — reproduce per source)*.

**Q7 — `f` continuous on `[a, b]`, differentiable on `(a, b)`, `f'(x) = 0` for all `x ∈ (a, b)` ⇒ `f` constant on `[a, b]`.**

Pick arbitrary `c ∈ (a, b]`, `c ≠ a`. By MVT on `[a, c]`, there is `d ∈ (a, c)` with `(f(c) − f(a))/(c − a) = f'(d) = 0`. So `f(c) = f(a)`. Since `c` was arbitrary, `f` is constant.

**Q8 — `f` continuous on `[a, b]`, `f'(x) > 0` on `(a, b)` ⇒ `f` strictly increasing on `[a, b]`.**

Take any `x_1 < x_2` in `[a, b]`. By MVT on `[x_1, x_2]`, there is `c ∈ (x_1, x_2)` with `(f(x_2) − f(x_1))/(x_2 − x_1) = f'(c) > 0`. Since `x_2 − x_1 > 0`, `f(x_2) − f(x_1) > 0`, i.e. `f(x_2) > f(x_1)`. Hence strictly increasing.

### ⚠️ Common Mistakes
- ❌ Concluding existence of a 2-variable limit from agreement of two paths → ✅ As Q1 shows, even three paths agreeing isn't enough; non-existence requires only a single disagreement.
- ❌ Forgetting MVT requires both continuity on `[a, b]` AND differentiability on `(a, b)` (only interior).

### Connections
- Builds on: every section of Unit 14 — these are capstone exercises.


---


## Section: 15.0 Objectives & 15.1 Introduction [🟢]
<!-- Reason: Course-level motivation and historical context, not exam-critical formulas. -->

### Core Idea
Unit 15 generalises ideas from Euclidean space in two big steps. First, the notion of "distance" is abstracted into a metric, giving the discipline of metric space (any set with a notion of distance). Second, even the dependence on distance is removed, leaving only the concept of "open set," giving the discipline of topology. Both disciplines were built to handle problems where the ordinary Euclidean idea of distance is unavailable, inappropriate, or unnecessary.

> **In Simple Terms:** First we promote distance from "a tape measure between two points" to "any rule that behaves like a distance." Then we throw away the tape entirely and just keep track of "which neighbourhoods belong together" — that's topology.

### Key Concepts

#### Why generalise — metric space and topology
The 20th century pushed mathematics toward generalisation. Metric space generalises Euclidean spaces (R^2, R^3, …, R^n) to arbitrary sets equipped with a metric. Topology further generalises both metric space and Euclidean geometry by ignoring distance, angle, and congruence — only "open sets" remain. The unit will reach concepts like convergence, continuity, connectedness, and compactness in each setting.

#### "Distance" appears everywhere
The text gives many examples of intuitive distance: spatial (between cities, stars), temporal (days between two dates), thermal (difference in average temperature), social (sibling = 1, first cousin = 2, second cousin = 3), generational (parent = 1, grand-parent = 2, …). These intuitions need a formal counterpart, which is the metric.

#### Applications of distance/metric
Distance/metric is now essential in probability, statistics, graph theory, clustering, data analysis, pattern recognition, computer graphics, image analysis, speech recognition, information retrieval, astronomy, molecular biology, etc. Two specific examples cited: **Genetic distance** (genetic divergence between species/populations), and **Economic distance** (Patel, 1965 — time in years for a lagging country to catch up to the present per-capita income of an advanced country). Production-economics distances mentioned: directional distance function, Shephard input distance function, distance to frontier. (For finer applications, the text refers to Deza & Deza, 2016.)

#### Topology as "Rubber-Sheet Geometry"
The text gives a comparison of an aerial Delhi Metro Network map (LHS, with curves and varying angles/distances) versus an in-train metro map (RHS, with straight lines, near-uniform angles, and equidistant stops). Losing exact distance and angle yields a more comprehensible map. Cup ↔ doughnut and the four letters E, F, T, Y are taken as topologically equivalent because each can be obtained from another by stretching/shrinking the "rubber sheet." Topology is concerned with properties preserved under continuous deformations: stretching, twisting, crumpling, bending. Application in economics: General Equilibrium theory (e.g., Nash equilibrium); see Songzi Du, "Topology and Economics."

#### Historical origins
- **Maurice Fréchet** (French): introduced "Metric Space" in 1906 in his thesis *Sur Quelques Points du Calcul Fonctionnel*.
- **Felix Hausdorff** (German): published *Grundzüge der Mengenlehre* (Foundations of Set Theory) in 1914, where the theory of topological and metric spaces (*metrische Räume*) was created.

### Connections
- Builds on: Real numbers, intervals, |·| (Unit 1, mentioned)
- Builds on: Euclidean R^2, R^3, R^n (Unit 14, "previous unit")
- Leads to: Continuity, convergence, connectedness, compactness in metric and topological spaces (later sections of Unit 15)

---

## Section: 15.2 Metric Space — Motivation & Multiple Distances [🟡]
<!-- Reason: Sets up multiple metrics; the formulas (Euclidean, Taxicab, Minkowski) are exam-relevant though the section is preparatory. -->

### Core Idea
For the same pair of points, more than one metric may be useful, depending on the application. The Euclidean and Taxicab distances are special cases of the Minkowski distance. A useful metric must satisfy reasonable conditions — these become the metric axioms in 15.2.1.

> **In Simple Terms:** "How far apart are these two points?" can have several legitimate answers. A car driving in a grid city covers more road than a crow flies. Both numbers are valid distances — they just answer different questions.

### Key Concepts

#### Euclidean distance d_E in R^2
For points P(x_1, y_1) and Q(x_2, y_2):

d_E(P, Q) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]

This is the "straight-line" distance.

#### Taxicab / Manhattan distance d_T
Idealising city roads as mutually parallel/perpendicular, the minimum drivable distance is the sum of the moves along the x-axis and the y-axis:

d_T(x, y) = |x_1 − x_2| + |y_1 − y_2|, for x = (x_1, y_1), y = (x_2, y_2)

Useful in **urban planning** — siting medical, educational, and other facilities depends on mass-transit/road/metro networks (Taxicab) more than Euclidean lines. The road map of Chandigarh is given as an illustration.

#### Minkowski distance of order p
For R^n (n-dimensional space over reals), order p = 1, 2, 3, …:

d_p(x, y) = ( Σ_{i=1..n} |x_i − y_i|^p )^{1/p}

- Order p = 1 → Manhattan/Taxicab distance.
- Order p = 2 → Euclidean distance.

Minkowski distances of various orders are used in statistics and optimisation problems across many domains, including economics. The most appropriate distance depends on application domain.

#### Distance on the Earth's surface
Two natural notions for distance between P and Q on Earth: (i) length of the shortest path along the great circle of the surface (used for shipping/aviation, shown in blue), and (ii) the straight-line distance through the Earth's interior (shown in red, used e.g. in seismology for travel-time of seismic waves).

### Examples / Sanity Check
Any candidate distance must rule out absurdities — e.g., "distance Delhi to Chennai by direct train" cannot exceed "distance Delhi to Chennai via the moon." The conditions that prevent such absurdities will be the **metric axioms** below.

### Comparison Table — Common Metrics

| Metric | Formula (between x, y in R^n) | Where used |
|---|---|---|
| Euclidean d_E | √[ Σ (x_i − y_i)^2 ] | Geometry, "straight-line" distance |
| Taxicab / Manhattan d_T | Σ |x_i − y_i| | Urban planning, grid streets |
| Minkowski d_p | ( Σ |x_i − y_i|^p )^{1/p} | Generalisation; statistics, optimisation |
| (Chebyshev d_∞ — implicit limit case; not formula-defined here) | — | — |

> **Quick Recall:**
> - Manhattan = Minkowski with p = 1
> - Euclidean = Minkowski with p = 2

### Connections
- Builds on: Euclidean distance in R^2 / R^3 (Unit 14)
- Leads to: Metric axioms (15.2.1)

---

## Section: 15.2.1 Metrics — The Formalised Distances (Axioms) [🔴]
<!-- Reason: The four metric axioms are core, exam-critical content for Unit 15. -->

### Core Idea
A **metric** on a non-empty set S is any function d : S × S → R that satisfies four axioms — non-negativity, identity of indiscernibles, symmetry, and the triangle inequality. These axioms are the abstract distillation of every reasonable notion of "distance."

> **In Simple Terms:** A function gets to be called a "distance" only if it (1) is never negative, (2) is zero exactly when both points coincide, (3) doesn't care which point you start from, and (4) doesn't reward you for taking a detour.

### Definitions
- **Metric on a set**: For a non-empty set S, a function d : S × S → R is called a **metric** if for all x, y, z in S it satisfies: ⭐
  - **(i) Non-negativity**: d(x, y) ≥ 0. (The cost of going from any point to any point is non-negative.)
  - **(ii) Identity of indiscernibles**: d(x, y) = 0 iff x = y. Equivalently:
    - (a) d(x, x) = 0 for any x in S (it does not cost to remain at the same point), and
    - (b) d(x, y) > 0 if x ≠ y (the cost of going to a different point is positive).
  - **(iii) Symmetry**: d(x, y) = d(y, x). (Cost of going from x to y equals cost of going back.)
  - **(iv) Triangle inequality** ("transitive property" in the source): d(x, z) ≤ d(x, y) + d(y, z). (Going directly from x to z does not exceed going from x via y to z.)

> **Quick Recall (the four axioms):**
> 1. d(x, y) ≥ 0
> 2. d(x, y) = 0 ⇔ x = y
> 3. d(x, y) = d(y, x)
> 4. d(x, z) ≤ d(x, y) + d(y, z)

### Connections
- Leads to: Definition of metric space (15.2.2)

---

## Section: 15.2.2 Metric Space — Definition & Examples [🔴]
<!-- Reason: Foundational definition plus two worked examples (Example 15.1 absolute-value metric on R, Example 15.2 discrete metric). -->

### Core Idea
A **metric space** is just an ordered pair (S, d) consisting of a non-empty set S and a metric d on it. Two key examples — both verified directly against the four axioms — are (R, d) with d(x, y) = |x − y| (the absolute-value/mod-induced metric on the real line) and the **discrete metric** on any non-empty set S (d(x, y) = 0 if x = y, else 1).

> **In Simple Terms:** Pair up any set with any rule that satisfies the four axioms, and you've made a metric space. It doesn't have to be R^n; you can metrify words, dates, family trees — anything.

### Definitions
- **Metric Space**: The ordered pair (S, d), where S ≠ ∅ and d is a metric on S, is called a **metric space**. ⭐

### Examples

**Example 15.1 — The mod / absolute-value metric on R.**
Recall Mod : R → R defined as
- Mod(x) = |x| = −x if x < 0, and = x if x ≥ 0.

So |x| ≥ 0. Define d : R × R → R by d(x, y) = |x − y|. Then (R, d) is a metric space. Verification of each axiom:

- (i) Non-negativity. Since x − y ∈ R, by definition of mod, d(x, y) = |x − y| ≥ 0.
- (ii) Identity. We know |x| = 0 iff x = 0. So d(x, y) = |x − y| = 0 iff x − y = 0 iff x = y.
- (iii) Symmetry. d(x, y) = |x − y| = |y − x| (by the mod function) = d(y, x).
- (iv) Triangle inequality. For x, y, z ∈ R:
  d(x, z) = |x − z| = |(x − y) + (y − z)| ≤ |x − y| + |y − z| (by triangular property of mod) = d(x, y) + d(y, z).

**Example 15.2 — The Discrete Metric.**
For any non-empty set S, define d : S × S → R by
- d(x, y) = 0 if x = y, and 1 if x ≠ y.

Then (S, d) is a metric space. Verification:

- (i) d(x, y) ∈ {0, 1}, hence d(x, y) ≥ 0.
- (ii) If d(x, y) = 0 then x = y (otherwise d would be 1).
- (iii) Symmetry. If d(x, y) = 0 then x = y, so d(x, y) = d(x, x) = d(y, x). If d(x, y) = 1 then y ≠ x, so d(y, x) = 1. Either way d(x, y) = d(y, x).
- (iv) Triangle inequality.
  - Case (a): if x = z, then d(x, z) = 0 = 0 + 0 ≤ d(x, y) + d(y, z).
  - Case (b): if x ≠ z, then d(x, z) = 1. For any y in S, y is unequal to at least one of x, z. Say x ≠ y; then d(x, y) = 1, so d(x, z) = 1 ≤ 1 + 0 ≤ d(x, y) + d(y, z) (since d(y, z) ≥ 0).

### Check Your Progress 1 (problems posed in this chunk)
1. Show (R^2, d_T) is a metric space, where R^2 = R × R, and the Taxicab distance is d_T(x, y) = |x_1 − y_1| + |x_2 − y_2|.
2. Show (R^2, d_E) is a metric space, where the Euclidean distance is d_E(x, y) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2].

(Solutions appear in chunk 013/section 15.6 of the unit.)

### Connections
- Builds on: |·| function (Unit 1), Euclidean distance (Unit 14)
- Leads to: Open/closed sphere; open/closed sets (15.2.3)

---

## Section: 15.2.3 Open/Closed Interval, Ball, Sphere (Euclidean) [🟡]
<!-- Reason: Builds vocabulary toward open/closed spheres in metric spaces; supporting concept. -->

### Core Idea
The familiar open and closed intervals on R are the "1-dimensional" versions of more general open/closed balls (in R^2) and open/closed spheres (in R^3 and R^n). All of these can be written as the set of points whose Euclidean distance from a centre point is less than r (open) or at most r (closed).

> **In Simple Terms:** An open interval is a 1-D open ball around its midpoint. Move up a dimension, you get a disk; up another, a 3-D ball; further, an n-dimensional sphere — each time, the same idea: "all points within distance r of a centre."

### Key Concepts

#### Open / closed interval on R
For a real number a and ε > 0:
- **Open interval**: ]a − ε, a + ε[ = { x : |x − a| < ε }
- **Closed interval**: [a − ε, a + ε] = { x : |x − a| ≤ ε }

#### Open ball in R^2
For a = (a_1, a_2) ∈ R^2 and radius r > 0:
- B(a, r) = { x = (x_1, x_2) ∈ R^2 : d_E(x, a) < r }

The text describes its shape as a ball but **without boundary**.

#### Open sphere in R^3
For a = (a_1, a_2, a_3) ∈ R^3 and r > 0:
- S(a, r) = { x = (x_1, x_2, x_3) ∈ R^3 : d_E(x, a) < r }

Again, this is the sphere shape **without boundary**.

#### Open sphere in R^n
For a = (a_1, …, a_n) ∈ R^n and r > 0:
- S(a, r) = { x = (x_1, …, x_n) ∈ R^n : d_E(x, a) < r }

#### Closed ball / closed sphere
- B^c(a, r) = { x ∈ R^2 : d_E(x, a) ≤ r }
- S^c(a, r) = { x ∈ R^n : d_E(x, a) ≤ r }

### ⚠️ Common Mistakes
- ❌ Treating "ball" and "sphere" as different objects in this text. ✅ Here they're used interchangeably (the unit explicitly says the term "ball" is also used for "sphere").
- ❌ Thinking S^c is a standard notation. ✅ The text explicitly notes B^c and S^c are **not standard notations** for closed ball/sphere — they are local notation only.

### Edge Cases & Caveats
- An open ball/sphere is the strict-inequality version (`<`). The closed version uses `≤`.
- The boundary is excluded in the open version, included in the closed.

### Recap of Open Set / Closed Set in R / R^n (Euclidean) (from previous unit)
- **Open set (in R)**: A set S ⊆ R is **open** if for each a ∈ S, there exists ε > 0 such that ]a − ε, a + ε[ ⊆ S. So every member is "well inside" S; no member is a boundary point. Earlier results recalled: (i) every open interval ]a, b[ is an open set, (ii) union of open intervals is an open set.
- **Closed set (in R)**: S ⊆ R is **closed** if R − S = (−∞, +∞) − S is open in R. (R itself can be denoted (−∞, +∞).)

### Connections
- Builds on: Open/closed intervals (Unit 1)
- Leads to: Generalisation to arbitrary metric space (15.2.3.1)

---

## Section: 15.2.3.1.1 Open & Closed Sphere of an Arbitrary Metric Space [🔴]
<!-- Reason: Core abstract definition; everything later (open set, continuity, etc.) builds on this. -->

### Core Idea
Once we have a metric space (X, d), we can replicate the "ball around a point" construction *without* needing R^n. The open sphere of radius r around a is just everyone in X at distance strictly less than r from a; the closed sphere uses ≤ r.

> **In Simple Terms:** "Throw a circle of radius r around the point a" — but the geometry of the circle is dictated entirely by your chosen metric. Different metrics give differently shaped "spheres."

### Definitions
Let (X, d) be a metric space, X ≠ ∅, d a metric on X, a ∈ X, r > 0.
- **Open sphere with centre a and radius r** ⭐:
  S(a, r) = { x ∈ X : d(a, x) < r }.
- **Closed sphere with centre a and radius r** ⭐:
  S^c(a, r) = { x ∈ X : d(a, x) ≤ r }.

Notes (from the text): the term "ball" is also used for "sphere"; the notation S^c is **not standard** for closed sphere.

### Example (begins this chunk; continues into chunk 012)

**Example 15.3 — Open and closed spheres in (R, d), d(x, y) = |x − y|.**

Open sphere with centre a ∈ R and radius r > 0:
S(a, r) = { x ∈ R : d(x, a) = |x − a| < r } (i.e., the open interval ]a − r, a + r[)

Closed sphere with centre a ∈ R and radius r > 0:
S^c(a, r) = { x ∈ R : d(x, a) = |x − a| ≤ r } (i.e., the closed interval [a − r, a + r])

(The next chunk continues with Example 15.4, the same construction in (R^2, d_E).)

> **Quick Recall:**
> - Open sphere uses strict < ; closed uses ≤.
> - In (R, |·|), an open sphere is just an open interval centred at a.

### Connections
- Builds on: Metric space definition (15.2.2.2)
- Leads to: Open set in metric space (15.2.3.1.2, chunk 012)

### Open Questions
1. What does an "open sphere" look like under the **discrete metric** (Example 15.2)? — Pursued in chunk 012's Check Your Progress 2.


---


## Section: Example 15.4 — Open & Closed Spheres in (R^2, d_E) [🟡]
<!-- Reason: Concrete instance of open/closed sphere; supporting example. -->

### Core Idea
In the metric space (R^2, d_E) — Euclidean plane — the open sphere centred at a = (a_1, a_2) of radius r is the open disk; the closed sphere is the closed disk.

### Worked Example

**Example 15.4** (continues from chunk 011's Example 15.3).
For x = (x_1, x_2), y = (y_1, y_2):

d_E(x, y) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]

- **Open sphere** S(a, r) with centre a = (a_1, a_2) ∈ R^2, r > 0:
  S(a, r) = { x ∈ R^2 : d_E(x, a) = √[(x_1 − a_1)^2 + (x_2 − a_2)^2] < r }
- **Closed sphere** S^c(a, r):
  S^c(a, r) = { x ∈ R^2 : d_E(x, a) = √[(x_1 − a_1)^2 + (x_2 − a_2)^2] ≤ r }

> **Quick Recall:**
> - In (R, |·|), the open sphere is an open interval.
> - In (R^2, d_E), the open sphere is an open disk.

### Connections
- Builds on: Open sphere in arbitrary metric space (15.2.3.1.1, Chunk 011)

---

## Section: 15.2.3.1.2 Open Set & Closed Set of a Metric Space [🔴]
<!-- Reason: The fundamental definitions for the rest of the unit and for topology. -->

### Core Idea
A subset T of a metric space (X, d) is **open** if every point of T can be surrounded by some open sphere (in X) that lies entirely inside T — i.e., no point of T is a "boundary" point. A subset is **closed** if its complement (in X) is open.

> **In Simple Terms:** "Open" means every point has elbow room — a small sphere around it stays in the set. "Closed" is just the dual: it's what's left when you remove an open set from X.

### Definitions
- **Open set of (X, d)** ⭐: A subset T of X is **open** if for each x ∈ T, there is an open sphere S(x, ε) with ε > 0 such that S(x, ε) ⊆ T. Equivalently, every member of T is well inside T; no member is a boundary point.
- **Closed set of (X, d)** ⭐: A set T ⊆ X is **closed** if its complement X − T is an open set in X.

### Examples and Non-Examples (open sets)
1. **]1, 3[ ∪ ]5, 7[ is open**, because (a) every open interval is an open set, and (b) union of open sets is open. (Both will be proved in the theorem below.)
2. **[1, 3[ is NOT open**: no open sphere ]1 − ε, 1 + ε[ with ε > 0 fits inside [1, 3[. Similarly **[1, 3] is not open**.
3. For a real number a:
   - **]−∞, a[ is open**. Proof: Let x ∈ ]−∞, a[, so x < a. Let ε = a − x > 0. Then S(x, ε) ⊆ ]−∞, a[.
   - **]a, ∞[ is open**. Proof: Let x ∈ ]a, ∞[, so a < x. Let ε = x − a > 0. Then S(x, ε) ⊆ ]a, ∞[.

### Theorem 15.2.3.1.2.1 — Properties of Open Sets [🔴]

In a metric space (X, d):
- **(i) Union of an arbitrary number of open sets is open.**
- **(ii) Intersection of a finite number of open sets is open.**
- **(iii) The universal set X is open.**
- **(iv) The empty set ∅ is open.**
- **(v) Every open sphere S(a, r) is an open set.**

(Note: (i), (ii) proved here; (iii), (iv) under "Check Your Progress"; (v) under "Exercises and Answers" — see chunk 014.)

#### Proof of (i): Union of arbitrary open sets is open
Let { X_i : i ∈ I } be open, I an index set (finite or infinite).
- Let x ∈ ⋃_{i ∈ I} X_i, so x ∈ X_j for some particular j.
- Since X_j is open, there exists ε > 0 with S(x, ε) ⊆ X_j.
- And X_j ⊆ ⋃_i X_i.
- Hence S(x, ε) ⊆ ⋃_i X_i. ⬛

#### Proof of (ii): Finite intersection of open sets is open
Let X_1, …, X_n be open. Show ⋂_{i=1..n} X_i is open.
- If the intersection is ∅, by (iv) it is open.
- Else, let x ∈ ⋂_{i=1..n} X_i; then x ∈ X_i for each i.
- Since each X_i is open, ∃ ε_i > 0 with S(x, ε_i) ⊆ X_i.
- Let ε = min{ε_i : i = 1, …, n}. Then ε > 0 and S(x, ε) ⊆ S(x, ε_i) ⊆ X_i for each i.
- So S(x, ε) ⊆ ⋂_{i=1..n} X_i. ⬛

### ⚠️ Common Mistake
- ❌ "Intersection of arbitrary open sets is open." ✅ Only **finite** intersections are guaranteed open. (For arbitrary intersection, the analogous result holds for **closed** sets.)

### Theorem 15.2.3.1.2.2 — Properties of Closed Sets [🔴]

In a metric space (X, d):
- **(i) Union of a finite number of closed sets is closed.**
- **(ii) Arbitrary intersection of closed sets is closed.** (The source text says "arbitrary intersection of closed sets is open" but the proof clearly establishes closed; this is a typo in the source.)
- **(iii) The universal set X is closed.**
- **(iv) The empty set ∅ is closed.**

(From Theorems 15.2.3.1.2.1 and .2 together, **X and ∅ are each both open and closed.**)

#### Proof of (i): Finite union of closed sets is closed
Let C_1, …, C_n be closed. Consider X − ⋃_{i=1..n} C_i. By De Morgan's Law,
X − ⋃ C_i = ⋂_{i=1..n} (X − C_i),
where each X − C_i is open (by definition of "closed"). By Theorem 15.2.3.1.2.1(ii), the finite intersection of open sets is open. Hence X − ⋃ C_i is open, so ⋃ C_i is closed. ⬛

#### Proof of (ii): Arbitrary intersection of closed sets is closed
Let { C_i : i ∈ I } be closed. By De Morgan,
X − ⋂_{i ∈ I} C_i = ⋃_{i ∈ I} (X − C_i),
where each X − C_i is open. Union of open sets is open, so the complement of ⋂ C_i is open, hence ⋂ C_i is closed. ⬛

### Examples and Non-Examples (closed sets), Example 15.5
1. **[1, 3] ∪ [5, 7] is closed**: every closed interval is closed, and union of finitely many closed sets is closed.
2. **[1, 3[ is NOT closed**: its complement ]−∞, 1[ ∪ [3, ∞[ is not open — no sphere S(3, ε) = ]3 − ε, 3 + ε[ fits inside the complement.
3. **]−∞, a] is closed**: complement ]a, ∞[ is open. **[a, ∞[ is closed**: complement ]−∞, a[ is open.

### Check Your Progress 2 (problem in this chunk)
For (X, d) the discrete metric (d(x, y) = 0 if x = y, else 1), find S(a, 1) and S^c(a, 1) — solutions in chunk 013.

### Connections
- Builds on: Open sphere of metric space (15.2.3.1.1, Chunk 011)
- Leads to: Convergence, continuity (15.2.4); topology (15.3)

---

## Section: 15.2.4.1 Convergence of a Sequence in a Metric Space [🔴]
<!-- Reason: Core concept; generalises sequence convergence from R to any metric space. -->

### Core Idea
A sequence (x_n) in a metric space (X, d) **converges** to a point x ∈ X if eventually all of its terms lie within any prescribed positive distance of x. Equivalently, every open sphere around x eventually contains all terms of the sequence.

### Definitions
- **Convergent sequence in (X, d)** ⭐: Let (X, d) be a metric space, X ≠ ∅, with (x_n) = (x_1, x_2, …, x_n, …) an infinite sequence in X. We say (x_n) is **convergent** if there exists x ∈ X such that for each ε > 0, there exists a positive integer k such that d(x_n, x) < ε for all n > k.

### Theorem 15.2.4.1.1 (equivalent formulation, no proof)
In a metric space, (x_n) is convergent iff for each open sphere S(x, ε), ε > 0, centred on x, there exists a positive integer k such that x_n ∈ S(x, ε) for all n > k.

> **Quick Recall:**
> - Convergence "ε-style": d(x_n, x) < ε eventually.
> - Convergence "open-sphere style": x_n eventually inside S(x, ε).

### Connections
- Builds on: Convergence in R (Unit 9), R^n (Unit 12)
- Leads to: Sequence-based characterisation of continuity (Theorem 15.2.4.2.3)

---

## Section: 15.2.4.2 Continuity of a Function in Metric Space [🔴]
<!-- Reason: Major exam-relevant generalisation; three equivalent characterisations. -->

### Core Idea
Continuity at a point generalises directly from real functions to maps between metric spaces. We replace |x − x_0| < δ in the domain with d_1(x, x_0) < δ, and |f(x) − f(x_0)| < ε in the codomain with d_2(f(x), f(x_0)) < ε. Three equivalent statements: ε-δ form, open-sphere form, open-set form, and a sequential form.

> **In Simple Terms:** "Continuous at x_0" means that you can keep f's outputs arbitrarily close to f(x_0) by keeping inputs sufficiently close to x_0 — and we can phrase this with epsilons, with little balls, with open sets, or with sequences. They all say the same thing.

### Definitions
- **Continuity at x = x_0** ⭐: Let (X_1, d_1), (X_2, d_2) be metric spaces and f : X_1 → X_2. Then f is **continuous at x_0 ∈ X_1** if for each ε > 0 there exists δ > 0 such that for all x ∈ X_1, d_1(x, x_0) < δ implies d_2(f(x), f(x_0)) < ε. (Note f(x), f(x_0) ∈ X_2.)

This subsumes the Unit 9 definition for real-valued real functions.

### Theorems on Continuity (no proofs in source)

**Theorem 15.2.4.2.1** — open-sphere characterisation: f is continuous at x_0 iff for each open sphere S_2 in X_2 with centre f(x_0) and radius ε > 0, there is an open sphere S_1 in X_1 with centre x_0 and radius δ > 0 such that f(S_1) ⊆ S_2.

**Theorem 15.2.4.2.2** — open-set characterisation: f is continuous at x_0 iff for each non-empty open set S_2 in X_2, there is an open set S_1 in X_1 such that f(S_1) ⊆ S_2. (Since every open sphere is an open set, this follows from 15.2.4.2.1.)

**Theorem 15.2.4.2.3** — sequential characterisation: f is continuous at x_0 iff for every sequence (x_n) → x_0, the image sequence (f(x_n)) → f(x_0). Symbolically: x_n → x_0 ⟹ f(x_n) → f(x_0).

> **Quick Recall — three faces of continuity:**
> 1. ε–δ: d_1 small ⟹ d_2 small.
> 2. Open spheres / open sets: pre-image of "small region" contains a "small region."
> 3. Sequential: convergent sequences map to convergent sequences.

### Connections
- Builds on: Continuity in R (Unit 9)
- Leads to: Continuity in topological space (15.3.2.1)

---

## Section: 15.2.4.3 Connectedness in a Metric Space [🔴]
<!-- Reason: Core named concept; supports connectedness theorems. -->

### Core Idea
A set S in a metric space is **connected** if you cannot split it into two or more disjoint non-empty open pieces. For subsets of R (Euclidean metric), the connected sets are exactly the intervals.

> **In Simple Terms:** A connected set is "all of one piece" — no clean break into separate open clumps.

### Definitions
- **Connected set in (X, d)** ⭐: A set S in (X, d) is **connected** if it cannot be represented as the union of two or more disjoint non-empty open sets in the metric space.

### Theorems (no proofs)
- **Theorem 15.2.4.3.1**: S in (X, d) is connected iff it cannot be represented as the union of two or more disjoint non-empty closed sets.
- **Theorem 15.2.4.3.2**: A subset of R, equipped with Euclidean metric, is connected iff it is an interval (open, semi-open, or closed).

### Examples
- **Example 15.6**: In (R, d_E), each of ]3, 7[, [3, 7[, [3, 7] is a connected set. In general, any interval — open, semi-open, or closed — is connected.
- **Example 15.7**: S = ]3, 7[ ∪ ]10, 16[ is **not** connected in (R, d_E). In general, the union of two non-overlapping intervals is not connected.

### Connections
- Leads to: Connectedness in topology (15.3.2.2)

---

## Section: 15.2.4.4 Compactness in a Metric Space; Bounded Sets [🔴]
<!-- Reason: Core named concept; bounded set definition is also exam-relevant. -->

### Core Idea
A set in a metric space is **compact** iff it is closed and bounded (this characterisation is recalled here from the previous unit; the general topological definition via covers is given in 15.3.2.3). "Bounded" means all pairwise distances are uniformly capped.

### Definitions
- **Bounded set in (X, d)** ⭐: S ⊆ X is **bounded** if there exists r > 0 such that for all s, t ∈ S, d(s, t) < r.
- **Bounded metric space**: (X, d) is bounded if X itself is bounded as a subset of itself.

### Recap from Previous Unit
A subset of R is **compact** iff it is closed and bounded. The Bolzano-Weierstrass theorem and its economic applications were discussed there. Here, the concept is briefly extended to general metric spaces, and further generalised to topological spaces in 15.3.2.3.

### Worked Example

**Example 15.8 — Every finite set in (X, d) is compact (closed and bounded).**

Let A = { a_1, a_2, …, a_n } ⊆ X.
- **Boundedness.** Let M = max{ d(a_i, a_j) : i, j = 1, …, n }. Then for every pair (a_i, a_j), d(a_i, a_j) ≤ M. So A is bounded.
- **Closedness.** Show X − A is open. The universal set X is open. We can write
  X − A = (X − {a_1}) ∩ (X − {a_2}) ∩ … ∩ (X − {a_n})
  (the source writes a union but the De-Morgan-correct expression for the complement of a finite union of singletons is the **intersection** of complements; in either case the same argument applies). To show each X − {a_i} is open: let y ∈ X − {a_i}, so y ≠ a_i. Let ε = d(y, a_i) > 0. Then S(y, ε/2) does not contain a_i, i.e., S(y, ε/2) ⊆ X − {a_i}. Hence X − {a_i} is open. So A = (X − A)^c is closed.

Thus a finite set is closed and bounded, hence compact.

### Connections
- Builds on: Compactness in R (previous unit; Bolzano-Weierstrass)
- Leads to: Compactness via open covers in topology (15.3.2.3, Chunk 013)

---

## Section: 15.3 Point Set Topology — Motivation [🟢]
<!-- Reason: Motivational, sets up Section 15.3 which is core. -->

### Core Idea
Topology drops the metric entirely. The crucial concept becomes the **open set**. Theorem 15.2.4.2.2 already showed that continuity itself can be expressed using only open sets — so we have a route to define continuity, connectedness, and compactness in a setting where no metric is available or useful.

> **In Simple Terms:** Imagine zooming out so far you stop noticing exact distances and angles, but you can still tell which clumps of points stick together. That's the topological view.

### Why Generalise Beyond Metric
- The Delhi Metro example: in-train maps lose exact distance/angle but become more comprehensible to travellers.
- Real-life problems sometimes have **no useful metric**, yet still require the concept of continuity. Continuity must therefore be liberated from dependence on metrics.

### What Topology Ignores
- The concept of distance (basis of metric space).
- Distance, angle, and geometric congruence (basis of Euclidean geometry).

Topology uses only the concept of **open set**. Most concepts and theorems from metric space that are based on open sets carry over almost directly.

### Connections
- Builds on: Open set in metric space (15.2.3.1.2)
- Leads to: 15.3.1 (basic topological definitions)

---

## Section: 15.3.1 Topology — Basic Definitions [🔴]
<!-- Reason: Definitional core; topology, open/closed set, neighbourhood. -->

### Core Idea
A **topology** on X is a chosen collection T of subsets of X (i.e., T ⊆ P(X)) that contains X and ∅, and is closed under arbitrary unions and finite intersections. Members of T are decreed to be the open sets of (X, T). A set is closed iff its complement is in T. A neighbourhood of a point (or set) is any open set containing it.

> **In Simple Terms:** Hand-pick which subsets you want to call "open." As long as your list contains X and ∅, and is stable under unions and finite intersections, you have a topology — and you've inherited the entire toolkit (continuity, connectedness, compactness) for free.

### Recall: Power Set
The set of all subsets of A is the **power set** P(A). Example: A = {1, 2, 3} ⟹ P(A) = { ∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} }.

### Definitions
- **Topology / Topological Space** ⭐: For X non-empty, a **topology on X** is the ordered pair (X, T), where T ⊆ P(X) is a collection of subsets of X satisfying:
  - (i) X ∈ T,
  - (ii) ∅ ∈ T,
  - (iii) the union of any number of sets in T is in T,
  - (iv) the intersection of any **finite** number of sets in T is in T.
  Equivalently, T is closed under unions and finite intersections, and contains both X and ∅. (X, T) is also called a **topological space**.

- **Open Set** (in topology) ⭐: Each set in T is an **open set** of (X, T). A set is open iff it belongs to T. So X and ∅ are always open.

- **Closed Set** (in topology) ⭐: A subset S ⊆ X is **closed** if its complement X − S ∈ T. So X and ∅ are always closed too.

- **Neighbourhood of a point x (or a set S)** ⭐: A neighbourhood of x (or of S) is an open set (member of T) which contains the point x (or the set S).

Note: different choices of T give different topologies on the same X.

### Examples

**Example 15.9 — Indiscrete (trivial) topology.**
Let X be non-empty, T = { ∅, X }. Then (X, T) is a topology.
- (i) X ∈ T, (ii) ∅ ∈ T — obvious.
- (iii) Only union is X ∪ ∅ = X ∈ T. ✓
- (iv) Only intersection is X ∩ ∅ = ∅ ∈ T. ✓

**Example 15.10 — Discrete topology.**
(X, P(X)) is a topology on X (where P(X) is the power set).
- (i) X ∈ P(X). (ii) ∅ ∈ P(X). ✓
- (iii) Any union of subsets of X is itself a subset of X, hence in P(X). ✓
- (iv) Any intersection of subsets of X is itself a subset of X, hence in P(X). ✓

This is called the **discrete topology** on X.

**Example 15.11 — Topology induced by a metric.**
Let (X, d) be a metric space, T = { S : S is open in (X, d) }. Then (X, T) is a topological space, called the **topology induced by the metric d** (or by the metric space).
- X, ∅ are always open in any metric space, so both ∈ T.
- (iii), (iv) follow from Theorem 15.2.3.1.2.1: arbitrary unions of open sets are open; finite intersections of open sets are open.

> **Quick Recall:**
> - **Indiscrete topology** = { ∅, X }. Smallest possible.
> - **Discrete topology** = P(X). Largest possible.
> - **Metric-induced topology** = open sets of (X, d).

### Comparison Table — Open/Closed across Frameworks

| Setting | Open set defined as | Notes |
|---|---|---|
| (R, |·|) | every point has surrounding open interval inside the set | Recap from earlier unit |
| Metric space (X, d) | every point has surrounding open sphere inside the set | 15.2.3.1.2 |
| Topology (X, T) | being a member of the chosen collection T | 15.3.1 — most general |

### Connections
- Builds on: Open sets in metric space (15.2.3.1.2)
- Leads to: Continuity / connectedness / compactness in topological space (15.3.2)

---

## Section: 15.3.2.1 Continuity of a Function in Topological Space [🔴]
<!-- Reason: Continuity in the most general setting in this unit. -->

### Core Idea
A map f : X_1 → X_2 between topological spaces is **continuous at x_0** if every neighbourhood of f(x_0) in X_2 has a neighbourhood of x_0 in X_1 that is mapped into it. Distance is gone — only neighbourhoods (open sets) remain.

### Definition
Let (X_i, T_i), i = 1, 2, be topological spaces, and f : X_1 → X_2. Then f is **continuous at x_0 ∈ X_1** ⭐ if for each neighbourhood H of f(x_0) in X_2, there exists a neighbourhood G of x_0 in X_1 such that f(G) ⊆ H.

> **Quick Recall:**
> - Metric-space continuity (ε–δ) ⟹ this when T comes from d.
> - Topological continuity is just "neighbourhood of image has a neighbourhood of pre-image inside."

### Connections
- Builds on: Theorem 15.2.4.2.2 (open-set characterisation of continuity in metric spaces)
- Leads to: Connectedness, compactness (15.3.2.2, .3 — Chunk 013)


---


## Section: 15.3.2.2 Connectedness of a Set in a Topological Space [🔴]
<!-- Reason: Core named concept in topology. -->

### Core Idea
A set S in a topological space is **connected** if you cannot split it into two non-empty open pieces with empty overlap. Intuitively, you can trace a path from any point of S to any other "without picking up the pencil."

> **In Simple Terms:** A connected set hangs together as a single piece — nothing inside it can be cleanly walled off into two open chunks.

### Definitions
- **Connected set in topology (X, T)** ⭐: A set S ∈ T is **connected** if whenever S = A ∪ B with A, B ∈ T (i.e., open in X) and A ∩ B = ∅, then either A = ∅ or B = ∅.
  Equivalently, S cannot be written as a disjoint union of two or more non-empty open sets.

(Note: the source text writes "with A ∪ B = ∅" in one place; in context — and consistent with the equivalent definition stated immediately after — this should be A ∩ B = ∅, the standard meaning of "disjoint.")

### Theorem (no proof — proof is "quite complicated despite the claim appearing simple")
In (R, d), where d(x, y) = |x − y|, any interval in R, e.g., [a, b] with a ≤ b, is connected.

### Examples and Non-Examples

**Example 15.12.** In the topology (R, T) induced by the mod function |x − y|, each of ]3, 7[, ]3, 7], [3, 7[, and [3, 7] is connected. In general, every interval — open, closed, or semi-open — is connected in this topology.

**Example 15.13.** For any topology (X, T), each set in T (which by definition is an open set of the topology) is connected.

**Example 15.14.** None of the following is connected in (R, d), d induced by |x − y|: ]3, 7[ ∪ ]8, 11[. In general, the union of at least two intervals [a_1, b_1], …, [a_n, b_n] with a_i < b_i and b_i < a_{i+1} (strict gap between consecutive intervals) is not connected. The result also holds for intervals of any open/closed/semi-open type.

### Connections
- Builds on: Connectedness in metric space (15.2.4.3, Chunk 012)

---

## Section: 15.3.2.3 Compactness of a Set in a Topological Space [🔴]
<!-- Reason: Core named concept; most general definition in unit. -->

### Core Idea
**Compactness via covers.** A cover of S is a family of subsets of X whose union contains S; an open cover is a cover by open sets. S is **compact** if every open cover of S has a **finite subcover**. This generalises "closed and bounded" (the metric/Euclidean characterisation) to settings where there is no metric.

> **In Simple Terms:** No matter how you cover the set with open clouds, finitely many of those clouds are already enough to cover it. This rules out infinite "spreading out" — N (the naturals) fail this criterion.

### Definitions
- **Cover**: In a topological space (X, T), for a set S, a **cover** of S is a family F of subsets of X with S ⊆ ⋃_{B ∈ F} B.
- **Open cover** ⭐: A cover F is an **open cover** if every B ∈ F is open, i.e., F ⊆ T.
- **Subcover / Finite subcover** ⭐: For a cover F of S, a **subcover** F′ is a sub-family F′ ⊆ F that is also a cover of S. If F′ contains only finitely many sets, it is a **finite subcover**.
- **Compact Set / Space** ⭐: A set S in (X, T) is **compact** if every open cover of S has a finite subcover. If X itself is compact, X is a **compact space**.

### Example

**Example 15.15 — N is not compact in (R, d), d = |x − y|.**

Consider open intervals O_n = ]n − 1/4, n + 1/2[ for n = 1, 2, …. (This is the source's family; the precise endpoints aren't critical, only that each O_n contains exactly one natural number.) Then N ⊆ ⋃_{n=1}^∞ O_n because n ∈ O_n for every n ∈ N.

If N were compact, finitely many O_n would suffice. But each O_n contains only one integer, so finitely many O_n contain only finitely many naturals — not all of N. Contradiction. Hence N is not compact. ⬛

> **Quick Recall:**
> - Compact = "every open cover has a finite subcover."
> - In metric/Euclidean space, this is equivalent to "closed and bounded."

### Connections
- Builds on: Compactness in metric space (15.2.4.4, Chunk 012)

---

## Section: Check Your Progress 3 [🟡]
<!-- Reason: Practice problems; their answers are given in 15.6, summarised here. -->

### Problems posed
1. In (R, d), d induced by |x − y|:
   - (i) Each of N, Z, Q (subset of R) is not connected. Also, any subset of N, Z, Q is not connected.
   - (ii) Any singleton {a} of Euclidean metric space is not connected.
   - (iii) Any finite subset {a_1, …, a_n} of Euclidean metric space is not connected.
2. Let X = {a, b, c}, T = { ∅, {a}, {a, b}, {a, c}, X }. Show (X, T) is a topology.
3. Let X be any infinite set, T = { S : S ⊆ X, X − S is a finite subset of X } ∪ { ∅ }. Show (X, T) is a topology. (This is the **cofinite topology**.)
4. Show that a finite set in (R, d), d = |x − y|, is compact.

(Answers in section 15.6 — summarised below.)

---

## Section: 15.4 Let Us Sum Up [🟢]
<!-- Reason: Course summary, not exam-critical content. -->

### Recap
The unit covered two advanced disciplines: **Metric Space** and **Topology**. After defining each, the underlying notions of open/closed interval/sphere were developed and their properties discussed. Within each discipline, practically useful concepts were introduced: convergence of sequences, continuity of functions, connectedness of sets, and compactness of sets — along with their properties and applications.

---

## Section: 15.5 Key Words — Glossary [🔴]
<!-- Reason: Exam-critical reference list of all formal definitions in the unit. -->

### All Key Definitions (consolidated from the source's Key Words section)

- **Euclidean Distance d_E** in 2-D space R^2: For P(x_1, y_1), Q(x_2, y_2),
  d_E(P, Q) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]. ⭐

- **Taxicab / Manhattan Distance d_T** between P(x_1, y_1) and Q(x_2, y_2):
  d_T(x, y) = |x_1 − x_2| + |y_1 − y_2|. ⭐

- **Minkowski Distance of order p** in R^n:
  d_p(x, y) = ( Σ_{i=1..n} |x_i − y_i|^p )^{1/p}, for p = 1, 2, 3, ….

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

---

## Section: 15.6 Answers / Hints to Check Your Progress [🟡]
<!-- Reason: Worked solutions to in-text exercises; supports earlier core definitions. -->

### Check Your Progress 1 — Solutions

**(1) (R^2, d_T) is a metric space.** With d_T(x, y) = |x_1 − y_1| + |x_2 − y_2| = Σ_{i=1,2} |x_i − y_i|.
- (i) Each |x_i − y_i| ≥ 0, so d_T(x, y) ≥ 0.
- (ii) d_T(x, y) = 0 iff |x_i − y_i| = 0 for i = 1, 2 iff x_i = y_i iff x = y.
- (iii) Symmetry: |x_i − y_i| = |y_i − x_i| ⟹ d_T(x, y) = d_T(y, x).
- (iv) Triangle inequality: For x, y, z ∈ R^2,
  d_T(x, z) = Σ |x_i − z_i| = Σ |(x_i − y_i) + (y_i − z_i)|
  ≤ Σ [ |x_i − y_i| + |y_i − z_i| ] (by |a + b| ≤ |a| + |b|)
  = Σ |x_i − y_i| + Σ |y_i − z_i| = d_T(x, y) + d_T(y, z). ⬛

**(2) (R^2, d_E) is a metric space.** With d_E(x, y) = √[(x_1 − y_1)^2 + (x_2 − y_2)^2] = √[ Σ_{i=1,2} (x_i − y_i)^2 ].
- (i) (x_i − y_i)^2 ≥ 0 ⟹ d_E ≥ 0.
- (ii) d_E = 0 iff (x_i − y_i)^2 = 0 for each i iff x_i = y_i iff x = y.
- (iii) Symmetry: (x_i − y_i)^2 = (y_i − x_i)^2 ⟹ d_E(x, y) = d_E(y, x).
- (iv) Triangle inequality: For x, y, z ∈ R^2,
  d_E(x, z) = √[ Σ (x_i − z_i)^2 ] = √[ Σ ((x_i − y_i) + (y_i − z_i))^2 ]
  ≤ √[ Σ (x_i − y_i)^2 ] + √[ Σ (y_i − z_i)^2 ] (the source labels this "Pythagorean theorem"; rigorously this is the **Minkowski / triangle inequality** for the L^2 norm — the source's invocation of "(a + b)^2 ≤ a^2 + b^2" is loosely worded but the conclusion stands)
  = d_E(x, y) + d_E(y, z). ⬛

### Check Your Progress 2 — Solutions

**(1) Discrete metric spheres.**
For (X, d) with d(x, y) = 0 if x = y, else 1; for a ∈ X:
- **S(a, 1)** = { a }. Only a itself is at distance < 1; every other point has distance exactly 1, not less.
- **S^c(a, 1)** = X. Every point has distance ≤ 1.

**(2) X is open in any metric space.**
Let x ∈ X; for any ε > 0, S(x, ε) = { y ∈ X : d(x, y) < ε } ⊆ X by definition. ⬛

**(3) ∅ is open.**
By contradiction: if ∅ were not open, it would contain some y with no S(y, ε) ⊆ ∅. But ∅ has no elements — contradiction. ⬛

**(4) X is closed.**
X − X = ∅, which is open (just proved). So X^c is open, hence X is closed. ⬛

**(5) ∅ is closed.**
X − ∅ = X, which is open. So ∅^c is open, hence ∅ is closed. ⬛

(Combined: in any metric space, X and ∅ are each both open and closed.)

### Check Your Progress 3 — Solutions

**(1) N, Z, Q (and any subsets of these) are not connected in (R, |·|).**
Use Theorem 15.2.4.3.2: a subset of R is connected iff it is an interval. None of N, Z, Q (or any of their subsets except trivial intervals) is an interval — so each is not connected.

**(1)(ii) Singleton {a} is not connected.**
R − {a} = ]−∞, a[ ∪ ]a, ∞[ is a union of two non-empty open intervals — i.e., {a} can be sandwiched in a way that makes its complement disconnected … (The source's argument: the singleton's complement is a union of two open intervals, demonstrating it is not an interval. Note: under the Theorem 15.2.4.3.2 criterion, a single point is technically a degenerate "closed interval" [a, a]; the source nevertheless classifies it as "not connected" presumably under the strict-interval reading. We follow the source.)

**(1)(iii) Finite subset {a_1 < a_2 < … < a_n} is not connected.**
R − {a_1, …, a_n} = ]−∞, a_1[ ∪ ]a_1, a_2[ ∪ … ∪ ]a_{n−1}, a_n[ ∪ ]a_n, ∞[, each piece an open interval. Hence the finite set is not an interval and not connected.

**(2) (X, T) with X = {a, b, c}, T = { ∅, {a}, {a, b}, {a, c}, X } is a topology.**
- (i) X ∈ T. (ii) ∅ ∈ T.
- (iii) Unions: any union involving X gives X ∈ T. Any union involving ∅ gives the other set ∈ T. Also {a, b} ∪ {a, c} = X ∈ T, and {a, b} ∪ {a, c} ∪ {a} = X ∈ T. ✓
- (iv) Intersections: any intersection involving ∅ gives ∅ ∈ T. Any intersection involving {a} gives {a} ∈ T. {a, b} ∩ {a, c} = {a} ∈ T. ✓

**(3) The cofinite topology on an infinite set X.**
T = { S ⊆ X : X − S is finite } ∪ { ∅ }.
- (i) X ∈ T because X − X = ∅, finite. (ii) ∅ ∈ T by definition.
- (iii) Let { Y_i } ⊆ T. Their union Y has X − Y ⊆ X − Y_1, which is finite, hence X − Y is finite, hence Y ∈ T.
- (iv) For finite intersection of Y_1, …, Y_n in T: by De Morgan, X − ⋂ Y_i = ⋃_{i=1..n} (X − Y_i), a finite union of finite sets, hence finite. So ⋂ Y_i ∈ T. ✓

**(4) A finite set is compact in (R, |·|).**
Let S = {x_1, …, x_k} and let { O_α } be any open cover of S. For each x_i, pick some O_{α_i} containing x_i. Then { O_{α_1}, …, O_{α_k} } is a finite subcover of S. ⬛

### Connections
- Builds on: Definitions and theorems throughout 15.2 and 15.3.
- Leads to: Exercises and Answers (15.7), in chunk 014.


---


## Section: 15.7 Exercises — Problems Posed [🟡]
<!-- Reason: Lists the questions; their full worked solutions follow. -->

### Exercises (statements)

1. Show (R^n, d_T) is a metric space, with R^n = R × R × … × R, and d_T the **Taxicab distance**:
   For x = (x_1, …, x_n), y = (y_1, …, y_n), d_T(x, y) = |x_1 − y_1| + … + |x_n − y_n| = Σ_{i=1..n} |x_i − y_i|.

2. Show (R^n, d_E) is a metric space, with d_E the **Euclidean distance**:
   d_E(x, y) = √[ Σ_{i=1..n} (x_i − y_i)^2 ].

3. In (R^2, d_T), with d_T(x, y) = |x_1 − y_1| + |x_2 − y_2|, for a = (a_1, a_2) find the open sphere S(a, 1) and the closed sphere S^c(a, 1).

4. Prove: every open sphere S(a, r) (in any metric space) is an open set.

(Answers below.)

---

## Section: Answer — Exercise 1: (R^n, d_T) is a metric space [🔴]
<!-- Reason: Generalises Check-Your-Progress 1 to arbitrary n; verifies all four metric axioms — exam-relevant. -->

### Core Idea
The Taxicab metric on R^n satisfies all four axioms exactly as on R^2, with the sum running over all n coordinates.

### Worked Proof
With d_T(x, y) = Σ_{i=1..n} |x_i − y_i|:

- **(i) Non-negativity.** Each |x_i − y_i| ≥ 0, so d_T(x, y) ≥ 0 + 0 + … + 0 = 0.
- **(ii) Identity.** d_T(x, y) = 0 iff |x_i − y_i| = 0 for each i = 1, …, n iff x_i − y_i = 0 (since |x| = 0 ⇔ x = 0) iff x_i = y_i for each i iff x = y.
- **(iii) Symmetry.** d_T(x, y) = Σ |x_i − y_i| = Σ |y_i − x_i| (by definition of mod) = d_T(y, x).
- **(iv) Triangle Inequality.** For x, y, z ∈ R^n,
  d_T(x, z) = Σ |x_i − z_i| = Σ |(x_i − y_i) + (y_i − z_i)|
  ≤ Σ [ |x_i − y_i| + |y_i − z_i| ] (by |a + b| ≤ |a| + |b|)
  = Σ |x_i − y_i| + Σ |y_i − z_i| (rearranging the summation)
  = d_T(x, y) + d_T(y, z). ⬛

### Connections
- Builds on: Check Your Progress 1 (R^2 case) (Chunk 013: 15.3.2.2 Connectedness of a Set in a Topological Space [🔴])

---

## Section: Answer — Exercise 2: (R^n, d_E) is a metric space [🔴]
<!-- Reason: Generalises Euclidean to arbitrary n; verifies all four metric axioms. -->

### Core Idea
The Euclidean metric on R^n satisfies all four axioms; the only delicate axiom is the triangle inequality.

### Worked Proof
With d_E(x, y) = √[ Σ_{i=1..n} (x_i − y_i)^2 ]:

- **(i) Non-negativity.** (x_i − y_i)^2 ≥ 0 for each i, so d_E(x, y) ≥ 0.
- **(ii) Identity.** d_E(x, y) = 0 iff (x_i − y_i)^2 = 0 for each i iff x_i = y_i for each i iff x = y.
- **(iii) Symmetry.** d_E(x, y) = √[ Σ (x_i − y_i)^2 ] = √[ Σ (y_i − x_i)^2 ] = d_E(y, x).
- **(iv) Triangle Inequality.** For x, y, z ∈ R^n,
  d_E(x, z) = √[ Σ (x_i − z_i)^2 ] = √[ Σ ((x_i − y_i) + (y_i − z_i))^2 ]   ... (a)
  By the generalised Pythagorean (more precisely, Minkowski / Cauchy-Schwarz) inequality,
  (a_1 + a_2 + … + a_n)^2 ≤ a_1^2 + a_2^2 + … + a_n^2 [as the source states]
  so (a) ≤ √[ Σ (x_i − y_i)^2 + Σ (y_i − z_i)^2 ]
  ≤ √[ Σ (x_i − y_i)^2 ] + √[ Σ (y_i − z_i)^2 ] (rearranging)
  = d_E(x, y) + d_E(y, z). ⬛

### ⚠️ Note on the Source's Argument
The source justifies the triangle inequality via "the generalised Pythagorean theorem," writing (a_1 + … + a_n)^2 ≤ a_1^2 + … + a_n^2. This stated inequality is **not generally true** as written (e.g., (1+1)^2 = 4 > 1+1 = 2). The correct underlying tool is the **Minkowski inequality** (or Cauchy-Schwarz). We reproduce the source's proof structure as the question requires faithfulness, but the careful proof of the Euclidean triangle inequality uses Minkowski, not "(a + b)^2 ≤ a^2 + b^2."

### Connections
- Builds on: Check Your Progress 1(2) (R^2 case) (Chunk 013: 15.3.2.2 Connectedness of a Set in a Topological Space [🔴])

---

## Section: Answer — Exercise 3: Open and Closed Spheres of radius 1 in (R^2, d_T) [🟡]
<!-- Reason: Routine application of definitions. -->

### Core Idea
In the Taxicab metric, the unit "sphere" around a is the set of points whose summed coordinate-wise gaps are below (open) or up to (closed) 1. Geometrically, this is a tilted square (a "diamond"), not a disk.

### Worked Answer
For a = (a_1, a_2) ∈ R^2, with d_T(x, a) = |x_1 − a_1| + |x_2 − a_2|:
- **Open sphere of radius 1**: S(a, 1) = { x = (x_1, x_2) : |x_1 − a_1| + |x_2 − a_2| < 1 }.
- **Closed sphere of radius 1**: S^c(a, 1) = { x = (x_1, x_2) : |x_1 − a_1| + |x_2 − a_2| ≤ 1 }.

> **Quick Recall:**
> - Euclidean unit ball in R^2 = open disk.
> - Taxicab unit ball in R^2 = open diamond (tilted square).

### Connections
- Builds on: Open/closed sphere in metric space (15.2.3.1.1, Chunk 011); Taxicab metric (Chunk 011: 15.0 Objectives & 15.1 Introduction [🟢])

---

## Section: Answer — Exercise 4: Every Open Sphere S(a, r) is an Open Set [🔴]
<!-- Reason: Essential theorem (Theorem 15.2.3.1.2.1(v)); proof is exam-critical. -->

### Core Idea
Inside any open sphere S(a, r), every point x has some smaller open sphere centred at x lying entirely within S(a, r). The trick is to choose the radius (r − ε), where ε = d(x, a), and apply the triangle inequality.

> **In Simple Terms:** If you're inside a ball of radius r, you have some breathing room — at least a "shell's-thickness" of room — and a tiny ball within that gap stays inside the original.

### Worked Proof

**Claim.** For (X, d) a metric space, a ∈ X, r > 0: S(a, r) is an open set.

**Proof.** By definition, S(a, r) is open if for each x ∈ S(a, r) there is an open sphere around x contained in S(a, r).

Let x ∈ S(a, r). Then d(a, x) < r.

- **Case 1: x = a.** Then S(x, r) = S(a, r) ⊆ S(a, r). ✓
- **Case 2: x ≠ a.** Then d(x, a) > 0, and d(a, x) < r.
  - Let ε = d(x, a) > 0. Then ε < r, i.e., r − ε > 0.
  - We show ]x − (r − ε), x + (r − ε)[ ⊆ S(a, r). (More precisely, the *open sphere* S(x, r − ε), which the source writes as the interval ]x − (r − ε), x + (r − ε)[ — appropriate for the R case.)
  - Let y ∈ S(x, r − ε), i.e., d(x, y) < r − ε.
  - Then by the triangle inequality, d(a, y) ≤ d(a, x) + d(x, y) < ε + (r − ε) = r.
  - Hence y ∈ S(a, r).
  - So S(x, r − ε) ⊆ S(a, r). ⬛

### Connections
- Completes: Theorem 15.2.3.1.2.1(v) (Chunk 012: Example 15.4 — Open & Closed Spheres in (R^2, d_E) [🟡])
- Builds on: Triangle inequality (15.2.1, Chunk 011)

---

## End of Unit 15
This chunk concludes Unit 15 — Basic Concepts of Metric Space and Point Set Topology.


---

