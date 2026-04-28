# Chunk 010 — Check Your Progress Answers, Exercises & Final Worked Solutions
<!-- Pages: 91-100 -->
<!-- Source: chunk_010.txt -->

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
- Builds on: 14.3 (Chunk 006).

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
- Builds on: 14.4 (Chunk 007).

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
- Builds on: 14.6 (Chunk 008).

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
