# Chunk 016 — Final Exercises: Piecewise Graph Q5–Q6, Hyperbola Q7, Rational Q8
<!-- Pages: 151-153 -->
<!-- Source: chunk_016.txt -->
<!-- Continuity: Closes Block-1, Unit 4. Continues Section 4.12 Exercises started in chunk 015 (Q5 piecewise overlap, Q6 three-piece function, Q7 hyperbola 9x²−16y²=144, Q8 rational function graphing). End-of-block matter. -->

## Section: Q5 (Continued) — Piecewise Function with Open/Closed Dot Convention 🔴

### Core Idea
When a piecewise function's two branches give different values at the boundary x, the convention is to use a **closed dot** for the branch that genuinely takes that value and an **open dot** for the other. This visually communicates the jump and prevents ambiguity about which branch "owns" the boundary point.

> **In Simple Terms:** At the joining x, only one of the two formulas gets to claim the actual point. Mark the winner with a filled circle, the loser with a hollow circle. The graph shows a small visual gap.

### Examples

**Example: g(x) = { −x² + 4 if x ≤ 1 ; 2x − 1 if x > 1 }**

T-chart for −x² + 4 on x ≤ 1:

| x | f(x) = −x² + 4 | (x, y) |
|---|---|---|
| −2 | 0 | (−2, 0) |
| −1 | 3 | (−1, 3) |
| 0 | 4 | (0, 4) |
| 1 | 3 | (1, 3) |

T-chart for 2x − 1 on x > 1:

| x | f(x) = 2x − 1 | (x, y) |
|---|---|---|
| 1 | 1 | (1, 1) |
| 2 | 3 | (2, 3) |
| 3 | 5 | (3, 5) |

**Plotting convention:**
- Upper branch (−x² + 4) at x = 1: closed dot at (1, 3) — because x ≤ 1 includes 1.
- Lower branch (2x − 1) at x = 1: **open dot** at (1, 1) — because x > 1 excludes 1; the formula is only "approached" there.

**Note**: the two pieces do not meet at x = 1 (one ends at y = 3, the other approaches y = 1) → there is a **visual blank space / jump** at x = 1.

### ⚠️ Common Mistakes
- ❌ Using closed dots on both branches at a non-shared boundary → ✅ Only one branch can include the boundary; use open dot for the other.

> **Quick Recall:**
> - "≤" and "≥" → closed dot.
> - "<" and ">" → open dot.

---

## Section: Q6 — Three-Piece Piecewise Function 🔴

### Core Idea
Piecewise functions can have three or more branches. The graphing process scales: build a T-chart per branch, evaluate **both endpoints** of each interval (so we know where to place open or closed dots), then assemble the full graph.

### Examples

**Example: h(x) = { x + 3 if x ≤ −2 ; x² if −2 < x ≤ 1 ; −x + 2 if x > 1 }**

[OCR note: source text shows "x ≤ 2" for the first branch, "if -2 < x < 1" middle, and "if x = 1" last — these signs are OCR-garbled. Reconstructed reasonable boundaries above based on the answer's evaluation table.]

The two outer branches are lines (only need two points). The middle branch is a parabola, so include extra points.

| Branch | x | y | Point |
|---|---|---|---|
| x + 3 | −3 | 0 | (−3, 0) |
| x + 3 | −2 | 1 | (−2, 1) |
| x² | −2 | 4 | (−2, 4) |
| x² | −1 | 1 | (−1, 1) |
| x² | 0 | 0 | (0, 0) |
| x² | 1 | 1 | (1, 1) |
| −x + 2 | 1 | 1 | (1, 1) |
| −x + 2 | 2 | 0 | (2, 0) |

**Closed/open dots**: at x = −2, the branches give 1 and 4 (jump). At x = 1, both x² and −x + 2 give 1 (continuous).

### Mechanisms / Processes
1. Identify each branch and its sub-domain.
2. T-chart for each branch including endpoints.
3. Place closed/open dots based on which branch includes the boundary.
4. Sketch each piece, joining or leaving gaps as the values dictate.

---

## Section: Q7 — Hyperbola 9x² − 16y² = 144 🔴

### Core Idea
A hyperbola in non-standard form must first be normalised by dividing through to make the right-hand side equal to 1. Then identify a, b, the foci (via a² + b² = F²), and the asymptotes (slopes ±b/a or ±a/b depending on orientation). Use these to sketch the curve.

### Mechanisms / Processes — Solution

**Step 1**: Divide both sides by 144:
9x²/144 − 16y²/144 = 1
⇒ x²/16 − y²/9 = 1
⇒ x²/4² − y²/3² = 1

This is a **horizontal hyperbola** with **a = 4** and **b = 3**.

**Step 2 — Intercepts**:
- **x-intercept**: set y = 0 → x²/4² = 1 → **x = ±4**. Points (4, 0) and (−4, 0).
- **y-intercept**: set x = 0 → −y²/9 = 1 → no real solution → **no y-intercept**.

**Step 3 — Foci**: F² = a² + b² = 16 + 9 = 25 → **F = 5**.
Foci at **(5, 0) and (−5, 0)**.

**Step 4 — Asymptotes**: y = ±(b/a)·x = **±(3/4)x**.

**Step 5 — Sketch**:
1. Plot asymptotes y = (3/4)x and y = −(3/4)x.
2. Plot vertices (±4, 0).
3. Use additional point: at x = 6, 9(36) − 16y² = 144 → −16y² = 144 − 324 = −180 → y² = 45/4 → y = ±3√5/2.
4. Draw branches starting at vertices, hugging asymptotes outward.

### ⚠️ Common Mistakes
- ❌ Forgetting to divide by 144 first → ✅ Always normalise to "= 1" form before reading a, b.
- ❌ Confusing F² = a² + b² (hyperbola) with F² = a² − b² (ellipse).

> **Quick Recall:**
> - Horizontal hyperbola: x²/a² − y²/b² = 1 → vertices (±a, 0), foci (±F, 0), F² = a² + b².
> - Asymptotes through origin: y = ±(b/a)x.

---

## Section: Q8 — Rational Function y = (2x² − 18)/(x² − 4) 🔴

### Core Idea
For a rational function whose graph involves both vertical and horizontal asymptotes, the standard procedure is: (i) find vertical asymptotes from denominator zeros, (ii) determine horizontal asymptote from leading-coefficient ratio (when degrees match), (iii) find x- and y-intercepts, (iv) plot extra points between intercepts and asymptotes for shape.

> **In Simple Terms:** First find all the "walls" (asymptotes) and "anchors" (intercepts), then fill in points to see how the curve bends between them.

### Mechanisms / Processes — Solution

**Step 1 — Vertical asymptotes**: denominator x² − 4 = 0 → x = ±2. So **vertical asymptotes at x = 2 and x = −2**.

**Step 2 — Horizontal asymptote**: degrees of numerator and denominator both = 2; ratio of leading coefficients = 2/1 = 2. So **horizontal asymptote at y = 2**.

**Step 3 — x-intercepts**: numerator 2x² − 18 = 0 → x² = 9 → **x = ±3**. Points (3, 0) and (−3, 0).

**Step 4 — y-intercept**: x = 0 → y = (0 − 18)/(0 − 4) = (−18)/(−4) = **4.5**. Point (0, 4.5).

**Step 5 — Additional points** (between intercepts and asymptotes for shape):

| x | y = (2x² − 18)/(x² − 4) |
|---|---|
| −5 | 1.5 |
| −2.5 | −2.4 |
| −1 | 5.3 |
| 1 | 5.3 |
| 2.5 | −2.4 |
| 5 | 1.5 |

**Shape**: three "branches" — left of x = −2, between x = −2 and x = 2, right of x = 2. The middle branch passes through (0, 4.5) and the outer branches approach y = 2 from below as |x| → ∞.

### ⚠️ Common Mistakes
- ❌ Skipping the asymptote step and directly tabulating values → ✅ Always identify asymptotes first; pick test points strategically near them.
- ❌ Plugging x = ±2 into a T-chart (undefined) → ✅ Mark these as vertical asymptotes, not as plot points.

> **Quick Recall:**
> - Vertical asymptote: where denominator = 0.
> - Horizontal asymptote (when num/denom degrees match): ratio of leading coefficients.
> - x-intercept: where numerator = 0 (and denominator ≠ 0).

---

## Section: End-of-Block Recap 🟢

### Core Idea
Chunk 016 closes Unit 4 (and Block 1) of MEC-203. Across Block 1 the student moved from set-theoretic foundations and number systems → relations and functions → coordinate geometry and graphing. The exercise set in chunks 015–016 ties together every graphing technique covered: vertex of quadratic, polynomial of degree 4, piecewise functions (two and three pieces), hyperbolas in non-standard form, and rational functions with both asymptote types.

### Connections
- This chunk completes Unit 4 of Block 1.
- Block 2 of MEC-203 typically continues into single-variable calculus (limits, differentiation), where:
  - Continuous vs discontinuous classification (chunk 014) becomes essential.
  - Asymptotic behaviour (chunks 013, 014) is formalised via limits.
  - Vertex/extremum reasoning (chunk 013) connects to first-derivative theory.

### Open Questions
- For Q8's rational function, can polynomial long division simplify the form to make the horizontal asymptote y = 2 obvious?
- How does the multi-branch hyperbola behaviour from Q7 generalise to multi-asymptote rational functions like Q8?

> **Quick Recall — Block 1 closing checklist:**
> - Plot quadratics via vertex (x = −b/2a).
> - Identify three discontinuity types.
> - Hyperbola: F² = a² + b²; asymptotes are diagonals of the helper rectangle.
> - Rational function pipeline: asymptotes → intercepts → fill points.
> - Always normalise conics to "= 1" form first.
