# Chunk 005 — Unit 11: Partial Derivatives, Total Differential/Derivative, Differentiation Cases, Implicit & MRTS, Elasticity of Substitution, Homogeneity
<!-- Pages: 41-50 -->
<!-- Continues from: §11.2 (chunk 004) -->
<!-- Continues into: §11.4.4 Property 3 / Euler's theorem (chunk 006) -->

## Section: §11.2.1 Partial Derivative Defined 🔴
<!-- See chunk 004 for intro -->
- Definition via difference quotient and limit; notation ∂U/∂x₁ or f₁.
- Marginal interpretation (marginal utility = ∂U/∂xᵢ).
- Worked Example 11.1: f = x₁³ + 2x₁²x₂ + 3x₁x₂² + 4x₂³ → f₁, f₂.

## Section: §11.2.2 Higher Order Partial Derivatives 🟡
- Repeat partial differentiation; once function ceases to depend on a variable, higher orders → 0.
- Worked: z = 6x² + 5x³ + 10xy → z_{xx}; e^{x₁+x₂} + 3x₁x₂.

## Section: §11.2.3 Cross-Partial Derivatives & Young's Theorem 🔴
- f₁₂ = ∂f₁/∂x₂; f₂₁ = ∂f₂/∂x₁.
- Young's theorem: f₁₂ = f₂₁ when both exist and one is continuous.
- Generalises to n-variable f.
- Worked Examples (polynomial; log(x₁²+x₂²)).

## Section: §11.3 Total Differential and Total Derivative 🔴
- §11.3.1 Total differential: dy = f₁ dx₁ + f₂ dx₂ (linear approximation).
- §11.3.2 Total derivative: when xᵢ = xᵢ(t), dy/dt = f₁ dx₁/dt + f₂ dx₂/dt.
- Generalises to n variables.
- Worked Example 11.5(i): q = 4x₁ + 3x₂ chain through t.

## Section: §11.4 Differentiation & Applications: Function-of-Functions Cases 🔴
- §11.4.1 four cases of chain rule: (I) z=f(u(x,y)); (II) z=f(x,y), x=φ(t), y=ψ(t); (III) z=f(x,y), y=y(x); (IV) z=f(x,y) with x,y functions of u,v.
- Differential rules: d(u+v), d(uv), d(u/v), d(log x), d(uv/w).

## Section: §11.4.2 Implicit Functions 🔴
- f(x,y) = 0; cannot always separate. Differentiate via dz = fx dx + fy dy = 0.
- ⇒ dy/dx = −fₓ/fᵧ.
- Second derivative formula: d²y/dx² = −[fₓₓfᵧ² − 2fₓᵧfₓfᵧ + fᵧᵧfₓ²] / fᵧ³ ... (eq. 11.1).
- Worked Example: f(x,y) = x³ + xy + y³ → derivatives.

## Section: §11.4.3 Applications: MRTS & Elasticity of Substitution 🔴
- MRTS = f_L / f_K (along isoquant dY = 0).
- Elasticity of substitution σ = % change in (x₁/x₂) / % change in (f₂/f₁).
- σ formula: σ = f₁ f₂ (f₁ x₁ + f₂ x₂) / [x₁ x₂ (2 f₁ f₂ f₁₂ − f₁² f₂₂ − f₂² f₁₁)].
- Convexity of isoquant ensures denominator > 0 ⇒ σ > 0.
- σ = 0 (Leontief), σ = ∞ (perfect substitutes); σ inversely proportional to convexity.
- Note for linear-homogeneous: σ = f₁ f₂ / (q f₁₂).

## Section: §11.4.4 Homogeneous Functions 🔴
- Definition: f(kx₁, kx₂) = kⁿ f(x₁, x₂); n is degree.
- Property 1: z = xⁿ φ(y/x) form.
- Property 2: first-order partials are homogeneous of degree n−1.
- (Property 3 / Euler's theorem continues in chunk 006).
