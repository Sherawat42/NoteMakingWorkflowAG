# Chunk 008 — Put Options, Swaps, IRS, CDS, and Block 4 Wrap-Up
<!-- Pages: 73-78 -->
<!-- Source: chunk_008.txt -->

## Section: Put Option 🔴

<!-- See chunk 007 for start of "Options" section. -->

### Core Idea
A **put option** gives the buyer the right (not the obligation) to **sell** the underlying at a predetermined exercise price by expiry. It's the mirror image of a call: it's exercised only when the strike price exceeds the spot (E > S), and it pays off when prices fall — making it a hedging tool for protection against price declines.

> **In Simple Terms:** A put is insurance against a price drop. You pay a small premium to lock in a guaranteed selling price. If the market price drops below your guaranteed price, you exercise (sell at the high lock-in price). If prices rise instead, you let the put lapse and just sell at the higher market price.

### Key Concepts

#### Decision rule for a put option (Table 13.3)

| Situation | Decision | Market Term |
|-----------|----------|-------------|
| **E < S** at expiry (E − S < 0) | **Don't exercise** — profitable in market | **Out-of-the-money put** |
| **E > S** at expiry (E − S > 0) | **Exercise put** | **In-the-money put** (money flows to buyer) |

> Note: The source's wording on "decision" in the second row says "because it is not a profitable situation" — but the *exercise* decision is correct (E > S means it pays to sell to writer at E rather than market at S). It is profitable to exercise when E > S.

#### Formulas

**Exercise / intrinsic value of put, V_PO:**
$$V_{PO} = \begin{cases} E - S & \text{if } E > S \\ 0 & \text{if } E \le S \end{cases}$$

Equivalently:
$$V_{PO} = \max(E - S, 0)$$

**Net payoff:**
$$\text{Net Payoff} = V_{PO} - \text{Option premium}$$

#### Logical justification
- A put is exercised only when **E > S** because selling to the writer at E and replacing the asset (or transferring it) when market price is lower than E is a profit-making move.
- Exercising when E < S would mean buying in the market at S to sell to writer at E (lower) — irrational.

### Examples

**Example 13.3 — Put option on SBI:**
- Current price ₹7; possible prices at expiry (2 months): ₹5, ₹10, ₹15, ₹20, ₹25, ₹30.
- Siddhi buys a put: **strike E = ₹12**, premium = ₹2.

**Buyer's payoff (Siddhi):**

| Price S (₹) | Premium (₹) | Strike (₹) | Total Cost (₹) | Net Payoff (₹) | Exercise? |
|-------------|--------------|--------------|------------------|------------------|------------|
| 5 | 2 | 13 | 7 | 6 | Yes |
| 10 | 2 | 13 | 12 | 1 | Yes |
| 15 | 2 | — | 2 | −2 | No |
| 20 | 2 | — | 2 | −2 | No |
| 25 | 2 | — | 2 | −2 | No |
| 30 | 2 | — | 2 | −2 | No |

> Buyer's max loss = premium (₹2). Profit grows as S falls below E. (Note: source uses ₹13 in computations even though the strike is stated as ₹12 — preserving source's worked table.)

### Definitions
- **Put option** ⭐: Right (not obligation) of buyer to **sell** the underlying at a predetermined exercise price within a specified time, for a premium.
- **In-the-money put** ⭐: E > S at expiry.
- **Out-of-the-money put**: E < S at expiry.
- **Intrinsic value of put (V_PO)**: max(E − S, 0).

#### Call vs Put — comparison

| Aspect | Call option | Put option |
|--------|--------------|--------------|
| Right to | **Buy** the underlying | **Sell** the underlying |
| Exercise when | **S > E** | **E > S** |
| Intrinsic value | max(S − E, 0) | max(E − S, 0) |
| Buyer profits from | Rising prices | Falling prices |
| Used for | Hedging short positions / speculating on rises | Hedging long positions / speculating on falls |
| In-the-money | S > E | E > S |

#### Option vs Future — comparison
- **Future**: contract that **obligates** buyer to purchase / seller to sell at specified date and price.
- **Option**: gives the buyer the **right but not obligation** to buy or sell at specified price by date.

### ⚠️ Common Mistakes
- ❌ Mistake: A put option pays off when prices rise. → ✅ Correct: Put pays when **E > S** (price falls below strike).
- ❌ Mistake: Options are a type of futures. → ✅ Correct: Futures = obligation; Options = right (no obligation).

> **Quick Recall:**
> - Put exercised iff E > S.
> - V_PO = max(E − S, 0).
> - Buyer's max loss = premium.
> - Profits from falling prices.

---

## Section: Swaps — Concept, Features, IRS, CDS 🔴

### Core Idea
A **swap** is a financial contract for two parties to exchange cash flows or financial instruments under predetermined terms. Swaps are highly customised, OTC, often involve fixed-vs-floating rate exchanges, and are used to alter the nature of an asset/liability without liquidating it. The two most popular swaps are the **interest-rate swap (IRS)** and the **credit-default swap (CDS)**.

> **In Simple Terms:** A swap is like trading payment streams. Imagine two friends — one with a fixed-salary job that envies the bonuses of the other, who has a variable salary. They agree to swap paychecks each month. Neither changes employer; both get the income profile they wanted.

### Key Concepts

#### What swaps do
- Exchange cash flows or financial instruments based on predetermined terms.
- Encompass spot and forward transactions in a customised framework.
- Used by corporations, banks, individuals for **financing, lower borrowing costs, and managing interest-rate / FX risks**.
- Core objective: **alter the nature of an asset or liability without liquidation**.
  - Equity investor → can convert risky returns into fixed-income cash flows without selling equities.
  - Corporation with floating-rate debt → can convert it into fixed-rate without retiring/reissuing debt.

#### Ten features of swaps
1. **Customisability** — tailored to parties' specific needs.
2. **Counterparty risk** — depends on both parties fulfilling obligations.
3. **OTC trading** — through dealer networks, not standardised exchanges.
4. **Types** — interest-rate, currency, commodity swaps; different underlyings and cash-flow structures.
5. **Fixed and floating rates** — most swaps exchange fixed for floating (or vice versa).
6. **Maturity** — specified, ranges from months to several years.
7. **Notional principal** — total value on which cash flows are calculated; **principal itself is usually not exchanged**.
8. **Cash-flow exchange** — periodic (quarterly, semi-annual) per agreement.
9. **Purpose** — hedge risks, manage rate/currency exposure, speculate.
10. **Documentation** — swap agreement specifies notional, payment dates, calculation methods, default conditions.

### Definitions
- **Swap** ⭐: Derivative contract for two parties to exchange financial instruments or cash flows on agreed terms.
- **Notional principal** ⭐: Reference value on which cash flows are computed; not itself exchanged.
- **LIBOR (London Inter-Bank Offered Rate)** ⭐: Common floating-rate benchmark.
- **MIBOR (Mumbai Inter-Bank Offered Rate)** ⭐: Indian counterpart to LIBOR; used in Indian swaps.

### Mechanisms / Processes

#### a) Interest-rate swap (IRS)
- One party pays **fixed interest** on a notional amount and receives **floating interest** (commonly **LIBOR + base points**, or **MIBOR + base points** in India) on the same notional.
- No principal exchange; only periodic interest cash-flow netting.

**Example 13.5 — IRS between Companies A and B:**
- A pays B fixed at 7% p.a. on notional ₹10,00,000; A receives floating at LIBOR + 1% on same notional. (Note: source then uses fixed rate of 10% in its tables — preserving source figures.)
- Term: 3 years. LIBOR data:

| Year | LIBOR |
|------|-------|
| 0–1 | 8% |
| 1–2 | 6% |
| 2–3 | 10% |

**Step 1 — Floating interest receivable by A (LIBOR + 1%):**

| Year | Floating Rate | Floating Interest (₹) |
|------|----------------|------------------------|
| 1 | 9% | 90,000 |
| 2 | 7% | 70,000 |
| 3 | 11% | 1,10,000 |

**Step 2 — Fixed interest payable by A (10% in source's worked numbers):**

| Year | Fixed Rate | Fixed Interest (₹) |
|------|-------------|---------------------|
| 1 | 10% | 1,00,000 |
| 2 | 10% | 1,00,000 |
| 3 | 10% | 1,00,000 |

**Step 3 — Net cash flow to A:**

| Year | Net Cash Flow (₹) | Explanation |
|------|---------------------|--------------|
| 1 | −20,000 | Pays ₹1,00,000, receives ₹80,000 → pays net ₹20,000 |
| 2 | −30,000 | Pays ₹1,00,000, receives ₹70,000 → pays net ₹30,000 |
| 3 | +10,000 | Pays ₹1,00,000, receives ₹1,10,000 → receives net ₹10,000 |

> Note: Source rows show ₹80,000 for year 1's floating receipt (vs ₹90,000 in step 1); preserving source explanations as printed.

#### b) Credit Default Swap (CDS)
- Financial contract that provides **insurance against default risk** on a specific debt instrument.
- **Buyer of CDS** pays a premium to the **seller of CDS**.
- If borrower defaults, **seller pays buyer the face value** of the debt instrument.
- Effectively, the credit risk transfers from buyer to seller in exchange for premium.

**Example 13.6 — CDS on Company A's bond:**
- Company A issues ₹10 million bond, 5-year maturity.
- Investors buy bonds; Company A promises interest + principal repayment.
- If A defaults, investors lose interest and principal.
- Investor mitigates by buying CDS from a bank/hedge fund:
  - Pays a premium for protection.
  - If A defaults, the institution pays investor the **₹10 million face value**.
  - Risk transfers from investor to institution; institution earns the premium as compensation.

### ⚠️ Common Mistakes
- ❌ Mistake: In a swap, principal is exchanged. → ✅ Correct: **Notional principal is usually not exchanged**; only interest/cash flows are.
- ❌ Mistake: A CDS protects against any market loss. → ✅ Correct: A CDS specifically covers **default risk** on a particular debt instrument.

> **Quick Recall:**
> - Swap = exchange of cash flows; OTC; notional principal is **not** exchanged.
> - 2 most common swaps: **IRS** (fixed ↔ floating interest), **CDS** (default protection).
> - LIBOR / MIBOR — floating-rate benchmarks.
> - 10 features mnemonic: **C**ustomisable, **C**ounterparty risk, **O**TC, **T**ypes, **F**ixed/Floating, **M**aturity, **N**otional, **C**ash-flow exchange, **P**urpose, **D**ocumentation.

### Connections
- Builds on: Forward/futures discussion in Chunk 007.
- Cross-reference: Future Unit 21 — Pricing of Derivatives (Black-Scholes, binomial models).

---

## Section: Unit 13 Summary, Key Words, and Block 4 Wrap-Up 🟢

### Core Idea
Unit 13 covered derivatives — financial contracts deriving value from underlying assets. Their biggest advantage is **risk hedging**; the biggest disadvantage is **default (counterparty) risk**. Derivatives include futures, forwards, options, swaps. India's derivatives trading began **2000**; primary venues are **NSE and BSE**, with **SEBI** as regulator. Commodity derivatives trade on **MCX and NCDEX**; currency derivatives on **MSE**.

### Key Concepts

#### Block 4 Indian derivatives ecosystem

| Segment | Exchanges |
|---------|-----------|
| **Financial derivatives** | National Stock Exchange (NSE), Bombay Stock Exchange (BSE) |
| **Commodity derivatives** | Multi Commodity Exchange (MCX), National Commodity & Derivatives Exchange (NCDEX) |
| **Currency derivatives** | Metropolitan Stock Exchange (MSE) |
| **Regulator** | SEBI |

#### Key words (Unit 13)
- **Derivative** ⭐: Financial asset that derives value from an underlying. Includes futures, forwards, options, commodity derivatives, etc.
- **Futures** ⭐: Standardised contract obligating buyer to purchase / seller to sell at predetermined price and date.
- **Forwards** ⭐: Customised, OTC contract similar to futures.
- **Option** ⭐: Right (not obligation) to buy/sell underlying at strike/exercise price by expiry.
- **Swap** ⭐: Derivative contract exchanging financial instruments or cash flows on agreed terms; common: interest-rate swap and credit-default swap.

### Definitions
(See cumulative running_context.md and content_index.md for the full glossary across Block 4.)

### ⚠️ Common Mistakes
- ❌ Mistake: An option is a type of future. → ✅ Correct: They differ in obligation — futures bind both parties; options give the buyer a right.
- ❌ Mistake: SEBI regulates only equities. → ✅ Correct: SEBI regulates the broader **derivatives market** in India and is the apex securities regulator.

> **Quick Recall:**
> - Indian derivatives trading: **2000** at NSE/BSE.
> - Regulator: **SEBI**.
> - Commodity derivatives: **MCX, NCDEX**.
> - Currency derivatives: **MSE**.
> - Biggest pro: hedging. Biggest con: counterparty default.

### Connections
- Closes Block 4: Money Markets (Unit 10) → Capital Markets (Unit 11) → Bond Markets (Unit 12) → Derivatives (Unit 13).
- Forward link: Unit 21 (Pricing of Derivatives — Black-Scholes, binomial) referenced for advanced material.

### Open Questions
1. Why does the source use both LIBOR and MIBOR — is there a domestic-vs-cross-border practical difference?
2. Why might Indian retail participation in CDS markets remain limited despite their hedging potential?
