# Chunk 001 — Unit 9: Limit and Continuity (§9.0–§9.6)
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

## Section: Block 3 Roadmap & Unit 9 Front Matter 🟢

### Core Idea
Block 3 of MEC203 is *Calculus*. It is organised into four units that progress from limits, to single-variable derivatives, to multivariable derivatives, and finally to integration. Unit 9 lays the foundation: limits and continuity.

> **In Simple Terms:** Before you can do calculus, you must understand what it means for a function to "approach" a value (limit) and what it means for a function to be "smooth with no jumps" (continuity). Everything else — derivatives, integrals — is built on top of these two ideas.

### Key Concepts
- Block 3 contents: Unit 9 (Limit & Continuity), Unit 10 (Differential Calculus: One Variable), Unit 11 (Differential Calculus: Several Variables), Unit 12 (Integration).
- Unit 9 objectives: identify limit; evaluate left/right-hand limits; examine continuity; state properties of continuous functions; locate points of discontinuity.

---

## Section: Limit of a Function (§9.2) 🔴

### Core Idea
The limit captures the value a function "heads toward" as the input approaches a target — without requiring the function to be defined at that target. The phrase "x tends to a" means |x − a| can be made arbitrarily small. The limit `lim_{x→a} f(x) = t` exists when, for every preassigned ε > 0, there is a δ > 0 such that |f(x) − t| < ε whenever 0 < |x − a| < δ.

> **In Simple Terms:** Imagine walking toward a doorway. The limit is "what value the function would take if you arrived at the door". You don't need to actually walk through it — you just need to see where the path is heading.

### Key Concepts

#### One-sided approach
- Approach from the right: `x → a+` (also written `x → a + 0`), values strictly greater than a.
- Approach from the left: `x → a−` (also written `x → a − 0`), values strictly less than a.

#### ε–δ definition (analytical form)
The limit is t if, given any ε > 0 (no matter how small), we can choose δ > 0 such that `|f(x) − t| < ε` for all x with `0 < |x − a| < δ`. The notation `∀` reads "for all".

### Definitions
- **Limit of f(x) as x → a**: the unique number t (when it exists) such that f(x) can be made arbitrarily close to t by taking x sufficiently close to a (but not equal to a). ⭐ (exam-important)

### Examples
**Example 9.1(i): `lim_{x→1} (x² − 1)/(x − 1) = 2`**
At x = 1 + δ (δ small, ≠ 0): (x²−1)/(x−1) = 2 + δ. Taking δ → 0 makes this arbitrarily close to 2. The function itself is **not defined at x = 1** (0/0), yet the limit is 2.

**Example 9.1(ii): `lim_{x→1} (2x − 1) = 1`**
|f(x) − 1| = |2x − 2| = 2|x − 1|. For any ε > 0, choose δ = ε/2. Then |x − 1| < δ ⇒ |f(x) − 1| < ε.

> **Quick Recall:**
> - Limit answers "where is f(x) heading?" — does not require f(a) to exist.
> - ε–δ form: `∀ ε > 0, ∃ δ > 0 : 0 < |x − a| < δ ⇒ |f(x) − t| < ε`.

---

## Section: Right-Hand and Left-Hand Limits (§9.3) 🔴

### Core Idea
A two-sided limit exists only when both one-sided limits exist *and* are equal. They are written `f(a+0)` for the right-hand limit (RHL) and `f(a−0)` for the left-hand limit (LHL).

> **In Simple Terms:** Walk to the same door from two different sides of a hallway. If both directions lead you to the same spot, the "limit" exists. If they lead to different spots, there is no single limit.

### Key Concepts

#### Right-Hand Limit
For any ε > 0, ∃ δ > 0 such that |f(x) − t₁| < ε whenever `0 < x − a < δ` (i.e., `a < x < a + δ`). Denoted f(a + 0).

#### Left-Hand Limit
For any ε > 0, ∃ δ > 0 such that |f(x) − t₂| < ε whenever `0 < a − x < δ` (i.e., `a − δ < x < a`). Denoted f(a − 0).

#### Existence condition
`lim_{x→a} f(x)` exists ⟺ both `lim_{x→a+} f(x)` and `lim_{x→a−} f(x)` exist and are equal.

### Examples
**`lim_{x→0} |x|/x` does not exist.**
- RHL: for x > 0, |x|/x = +1, so `lim_{x→0+} = 1`.
- LHL: for x < 0, |x|/x = −1, so `lim_{x→0−} = −1`.
- Since 1 ≠ −1, the two-sided limit fails. Note also f(0) is undefined.

> **Quick Recall:**
> - Two-sided limit exists ⟺ RHL = LHL.
> - One-sided limits use only one approach direction.

---

## Section: Functions Tending to Infinity (§9.4) 🟡

### Core Idea
We say `lim_{x→a} f(x) = ∞` when, for any preassigned N (however large), there is a δ such that f(x) > N whenever 0 < |x − a| < δ. Symmetric definitions for −∞ and for x → ∞.

### Definitions
- **Limit at infinity**: `lim_{x→∞} f(x) = t` when, for every ε > 0, ∃ M > 0 such that |f(x) − t| < ε for all x > M.

### Examples
**Example 9.2(i):**
- `lim_{x→0+} 1/x = ∞` and `lim_{x→0−} 1/x = −∞`. Hence `lim_{x→0} 1/x` does **not** exist.

**Example 9.3:**
- `lim_{x→∞} 1/x = 0`; `lim_{x→−∞} 1/x = 0`.
- `lim_{x→∞} eˣ = ∞`; `lim_{x→−∞} x³ = −∞`.

> **Quick Recall:**
> - "Limit is ∞" is a *behaviour* statement, not a value — the limit technically does not exist as a finite number.

---

## Section: Fundamental Theorems on Limit (§9.5) 🔴

### Core Idea
If `lim f(x) = t₁` and `lim φ(x) = t₂` (both finite), the limit operator distributes over algebraic operations and many composite forms. Together with a small set of standard limits, these theorems mechanise most limit calculations.

### Key Concepts

#### Algebra of limits
1. `lim {f + φ} = t₁ + t₂` (sum)
2. `lim {f · φ} = t₁ · t₂` (product)
3. `lim {f / φ} = t₁ / t₂`, provided t₂ ≠ 0 (quotient)
4. `lim F[f(x)] = F[lim f(x)]` (continuous outer)
5. **Sandwich (squeeze) theorem**: if φ(x) ≤ f(x) ≤ ψ(x) near a, and `lim φ = lim ψ = t`, then `lim f = t`.
6. Order: if φ ≤ ψ near a, then t₁ ≤ t₂.

#### Standard limits to memorise
| Limit | Value |
|---|---|
| `lim_{x→0} sin x / x` | 1 (x in radians) |
| `lim_{x→∞} (1 + 1/x)^x` | e |
| `lim_{x→0} (1 + x)^{1/x}` | e |
| `lim_{x→0} log(1+x) / x` | 1 |
| `lim_{x→0} (eˣ − 1) / x` | 1 |
| `lim_{x→a} (xⁿ − aⁿ) / (x − a)` | n a^{n−1} (a > 0) |
| `lim_{x→0} ((1+x)ⁿ − 1) / x` | n |
| `lim_{n→∞} xⁿ / n!` | 0 |

### Examples
**Example 9.4(i): rational function with leading coefficients.**
`lim_{x→∞} (a₀ xⁿ + a₁ x^{n−1} + … + aₙ) / (b₀ xⁿ + b₁ x^{n−1} + … + bₙ) = a₀/b₀`
because every other term divided by xⁿ tends to 0.

**Example 9.4(ii): `lim_{x→π} sin x / (x − π)`**
Substitute z = x − π, so x = π + z; as x → π, z → 0.
`sin(π + z) = −sin z`. Then `lim_{z→0} −sin z / z = −1`.

**Example 9.4(iv): `lim_{n→∞} (1/n² + 2/n² + … + n/n²)`**
= `lim n(n+1) / (2n²) = (1/2) lim (1 + 1/n) = 1/2`.

**Example 9.4(v): `lim_{x→2−} √(x − 2)`** does not exist (square root undefined for x < 2 from the left).

> **Quick Recall:**
> - Quotient rule needs t₂ ≠ 0.
> - sin x / x → 1 only when x is in **radians**.
> - For polynomial-over-polynomial as x → ∞, ratio of leading coefficients wins.

### ⚠️ Common Mistakes
- ❌ Mistake: applying `lim f/g = lim f / lim g` when denominator limit is 0 → ✅ Correct: this is an indeterminate 0/0 (or ∞/∞) — needs algebraic simplification or L'Hôpital (Unit 10).
- ❌ Mistake: writing `lim sin x / x = 1` for x in degrees → ✅ Correct: only valid in radians.

---

## Section: Continuity (§9.6) 🔴

### Core Idea
A function is **continuous at x = a** if its graph has no "gap" at that point. Formally, `lim_{x→a} f(x)` exists, is finite, and equals f(a). Equivalently, both one-sided limits equal f(a). A function continuous at every point of its domain is **continuous on that domain**.

> **In Simple Terms:** Draw the function near x = a. If you can do it without lifting your pen, the function is continuous there. If you have to jump, leave a hole, or shoot off to infinity, it is discontinuous.

### Key Concepts

#### Three-part continuity test at x = a
1. f(a) exists.
2. `lim_{x→a} f(x)` exists (RHL = LHL).
3. The limit equals f(a).

#### Types of discontinuity
| Type | Characterisation | Example |
|---|---|---|
| **Ordinary** | RHL ≠ LHL | step function |
| **Removable** | RHL = LHL but ≠ f(a), or f(a) undefined | (x²−1)/(x−1) at x = 1 |
| **Infinite** | RHL or LHL is ±∞ | 1/x at x = 0 |
| **Oscillatory** | function oscillates without settling | (−1)^x at x → ∞ (finite or infinite oscillation) |

### Definitions
- **Continuous at x = a**: `lim_{x→a−} f(x) = lim_{x→a+} f(x) = f(a)`. ⭐ (exam-important)
- **Removable discontinuity**: a discontinuity that can be eliminated by redefining f(a) to equal the common one-sided limit. ⭐
- **Ordinary discontinuity**: f(a+0) ≠ f(a−0). ⭐

### Mechanisms / Processes
**Checking continuity at x = a:**
1. Compute f(a) — if undefined, it is at least a removable or essential discontinuity.
2. Compute LHL = `lim_{x→a−} f(x)`.
3. Compute RHL = `lim_{x→a+} f(x)`.
4. Compare: continuous ⟺ all three equal.

### Examples
**Example 9.5: `lim_{x→a} √(x − a)`** — for a removable case, f(a) may or may not exist.

**Example 9.6: f(x) = (x² − 1)/(x − 1).**
`lim_{x→1} f(x) = 2`, but f(1) is undefined (0/0). This is a *removable* discontinuity; defining f(1) = 2 makes f continuous.

**Example 9.7 (oscillatory):**
- (a) f(x) = (−1)^x oscillates finitely at infinity.
- (b) f(x) = (x²)^x oscillates infinitely.

### Properties of Continuous Functions (§9.6.1) — begins
- Sum, difference, and product of continuous functions are continuous (extends to any finite number of functions).
- Quotient is continuous wherever the denominator does not vanish.
- If f is continuous at a and f(a) ≠ 0, then f preserves sign in a neighbourhood of a.
<!-- Continues in chunk 002 -->

> **Quick Recall:**
> - Continuity at a needs three things: f(a) exists, the limit exists, the two are equal.
> - Removable: one redefinition fixes it. Ordinary: can't be fixed by redefining a single point.
> - Differentiability ⇒ continuity (proven in Unit 10), but continuous functions are not always differentiable.

### Connections
- Builds on: Limit (§9.2), One-sided limits (§9.3) — continuity is defined via limits.
- Is prerequisite for: Differentiability (Unit 10 §10.2) — you cannot have a derivative at a discontinuity (with rare infinite-derivative exceptions).

### Open Questions
1. Why does the |x| / x example fail to have a limit at 0 even though |x| and x are individually continuous?
2. Can a function be continuous at exactly one point? (yes — Dirichlet-type constructions, beyond syllabus.)
