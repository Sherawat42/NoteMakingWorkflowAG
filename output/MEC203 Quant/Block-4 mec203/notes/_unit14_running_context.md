# Unit 14 — Calculus of Several Variables — Running Context (Chunks 006–010)

## Key Concepts Introduced
- End-of-Unit-13 Fibonacci sum identity `Σ F_i = F_{n+2} − 1` (chunk 006)
- Closed/open set verification via complements (chunk 006)
- Multivariate limit: existence requires consistency along all directions (chunk 006)
- Continuity-based shortcut for limit computation (chunk 006)
- Removable problematic conditions (factoring out singular factors) (chunk 006)
- Path testing for non-existence of limit (two paths disagree → DNE) (chunk 006)
- Three forms of dependent-variable specification: explicit, implicit, composite (chunk 007)
- Partial derivative as one-variable limit with other variables held constant (chunk 007)
- Implicit partial derivatives via product/chain rule on both sides of the implicit equation (chunk 007)
- Chain rule for one independent variable (composition layers) (chunk 007)
- Chain rule for partial derivatives, Case I (single parameter) and Case II (two parameters) (chunk 007)
- Higher-order partial derivatives and notation suffix order (chunk 007)
- Interpretation of partial derivatives as direction-specific rate of change (chunk 007)
- Total differential `dz = f_x dx + f_y dy` extended to many variables (chunk 007)
- Directional derivative as `∇f · û` (chunk 007 → 008)
- Direction cosines for `n`-D unit vectors (chunk 008)
- Function `R^n → R^m` as `m`-tuple of scalar functions (chunk 008)
- Jacobian matrix `(∂f_i/∂x_j)` (chunk 008)
- Jacobian determinant when `n = m`, applications to multiple integrals (chunk 008)
- Hessian as matrix of second partials encoding local curvature (chunk 008)
- Mean Value Theorem (single variable; geometric tangent-parallel-to-secant interpretation) (chunk 008)
- MVT extended to several variables via gradient and chord (chunk 008)
- Polynomial approximation idea: rational-evaluable approximations of irrational-valued elementary functions (chunk 008)
- Taylor polynomial of order `k`; Taylor formula `f = P_k + R_k` (chunk 008)
- Remainder forms: Peano, Lagrange, Cauchy (mentioned only) (chunk 008)
- Taylor's series expansion (chunk 008)
- Maclaurin's series (Taylor with `a = 0`) (chunk 009)
- Linear approximation `P_{1, a}` and quadratic approximation `P_{2, a}` (chunk 009)
- Multivariate linear approximation `P_{1, (a, b)}` (chunk 009)
- Multivariate quadratic approximation `P_{2, (a, b)}` with mixed-partial cross term (chunk 009)
- General `k`-th order multivariate Taylor polynomial in `n` variables (chunk 009)
- Multivariate Taylor series expansion (chunk 009)
- MVT corollaries: `f' ≡ 0 ⇒ f` constant; `f' > 0 ⇒ f` strictly increasing (chunk 010)

## ⭐ Definitions (exam-critical)
- **Limit (multivariable)**: value consistent with values at all neighbouring points along every direction of approach.
- **Notation**: `lim_{(x, y) → (a, b)} f(x, y)`.
- **Partial derivative `f_x`**: `lim_{h → 0} [f(x+h, y) − f(x, y)] / h` (treat `y` as constant).
- **Partial derivative `f_y`**: `lim_{h → 0} [f(x, y+h) − f(x, y)] / h` (treat `x` as constant).
- **Total differential**: `dz = f_x dx + f_y dy` (2 vars); `dw = h_x dx + h_y dy + h_z dz` (3 vars).
- **Directional derivative**: `D_A f(x, y) = lim_{|A| → 0} [f(x + |A| cos θ, y + |A| sin θ) − f(x, y)] / |A|`.
- **Gradient `∇f`**: row-vector `⟨f_{x_1}, …, f_{x_n}⟩`.
- **Direction cosines**: `(cos θ_1, …, cos θ_n)` specifying a unit vector in `R^n`.
- **Jacobian of `f: R^n → R^m`**: `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`.
- **Jacobian determinant**: `det(J_f)` when `n = m`; used in multiple integrals.
- **Hessian of `f: R^n → R`**: `n × n` matrix of second partials, `H_f[i, j] = ∂²f/(∂x_i ∂x_j)`; describes local curvature.
- **Mean Value Theorem (single)**: continuous on `[a, b]` and differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`.
- **Mean Value Theorem (several)**: `f` differentiable on open `G ⊆ R^n` and `x, y ∈ G` ⇒ `∃ c ∈ (0, 1)`: `f(y) − f(x) = ∇f((1 − c)x + c y) · (y − x)`.
- **Taylor polynomial `P_{k, a}`**: `Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j`.
- **Taylor's formula**: `f(x) = P_{k, a}(x) + R_{k, a}(x)`.
- **Remainder term `R_{k, a}(x)`**: error of polynomial approximation; `lim_{x → a} R_{k, a} = 0` for well-behaved `f`.
- **Maclaurin series**: Taylor's series with `a = 0`.
- **Linear approximation (1 var)**: `P_{1, a} = f(a) + f'(a)(x − a)`.
- **Quadratic approximation (1 var)**: `P_{2, a} = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)²`.
- **Linear approximation (2 vars)**: `P_{1, (a, b)} = f(a, b) + (x − a) f_x(a, b) + (y − b) f_y(a, b)`.
- **Quadratic approximation (2 vars)**: `P_{2, (a, b)} = f(a, b) + (x − a) f_x + (y − b) f_y + ((x − a)²/2!) f_{xx} + (x − a)(y − b) f_{xy} + ((y − b)²/2!) f_{yy}` (all partials at `(a, b)`).

## Named Theorems / Models
- **Mean Value Theorem (Lagrange's MVT)** — single variable (chunk 008) and several-variables version (chunk 008, optional).
- **Taylor's Theorem** — for `k`-times differentiable `f: R → R` (chunk 008).
- **General multivariate Taylor's theorem** — order `k` in `n` variables (chunk 009, optional).
- **Chain rule** — single independent variable and partial derivative versions (chunk 007); stated without proof.
- **Directional derivative formula** — `D_A f = ∇f · Â` (chunk 007); stated without proof.

## Key Formulas
- Multivariate limit existence test: agree along every path. Two-path disagreement ⇒ limit DNE.
- `f_x = lim_{h→0} [f(x + h, y) − f(x, y)]/h`; `f_y = lim_{h→0} [f(x, y + h) − f(x, y)]/h`.
- Chain rule (1 var): `dy/dx = (dy/dz)(dz/dw)(dw/dx)`.
- Chain rule (1 parameter): `dw/dt = (∂w/∂x)(dx/dt) + (∂w/∂y)(dy/dt)`.
- Chain rule (2 parameters): `∂w/∂r = (∂w/∂x)(∂x/∂r) + (∂w/∂y)(∂y/∂r)`; analogously for `s`.
- Total differential: `dz = f_x dx + f_y dy`; `dw = h_x dx + h_y dy + h_z dz`.
- Directional derivative (2 vars): `D_û f = f_x cos θ + f_y sin θ = ∇f · û`.
- Directional derivative (3 vars): `D_û f = f_x cos α + f_y cos β + f_z cos γ = ∇f · û`.
- For non-unit `V`: `û = V/‖V‖`.
- Jacobian: `J_f = (∂f_i/∂x_j)` (`m × n`).
- Hessian: `H_f[i, j] = ∂²f/(∂x_i ∂x_j)` (`n × n`).
- MVT: `f'(c) = (f(b) − f(a))/(b − a)` for some `c ∈ (a, b)`.
- Taylor polynomial: `P_{k, a}(x) = Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j`.
- Taylor formula: `f(x) = P_{k, a}(x) + R_{k, a}(x)` with `lim_{x→a} R_k = 0`.
- Maclaurin: same as Taylor with `a = 0`.
- 2-variable linear Taylor: `f(a, b) + f_x(a, b)(x − a) + f_y(a, b)(y − b)`.
- 2-variable quadratic Taylor: linear part `+ ½ f_{xx}(a,b)(x − a)² + f_{xy}(a,b)(x − a)(y − b) + ½ f_{yy}(a,b)(y − b)²`.
- General order-`k` `n`-variable Taylor polynomial: `Σ_{j=0}^k (1/j!) Σ_{i_1, …, i_j} F_{x_{i_1} … x_{i_j}}(a) (x_{i_1} − a_{i_1}) … (x_{i_j} − a_{i_j})`.

### Useful Maclaurin / Taylor expansions appearing in this unit
- `sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + …` (chunk 009, Example 14.14)
- `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + x⁸/8! − …` (chunk 010, CYP4 Q3)
- `log(x)` around `x = 1`: `(x − 1) − (x − 1)²/2 + (x − 1)³/3 − …` (chunk 010, CYP4 Q4)
- `e^{x_1 + x_2 + x_3} ≈ 1 + (x_1 + x_2 + x_3) + (1/2!)(x_1 + x_2 + x_3)² + (1/3!)(x_1 + x_2 + x_3)³` (chunk 009, Example 14.15)
- `xyz` around `(1, 1, 1)` finite Taylor (4th + higher derivatives all zero) (chunk 009, Example 14.16)
