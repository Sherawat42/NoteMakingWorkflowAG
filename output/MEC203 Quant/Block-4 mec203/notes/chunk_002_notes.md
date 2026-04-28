# Chunk 002 — Unit 13: Real Analysis (Intro & Sequences Setup)
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

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
- Continues into: A.P. examples and Geometric Progression (Chunk 003).
