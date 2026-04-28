# Chunk 003 — Unit 14 Commercial Banking Part 2: Credit Creation, Asset Distribution & Recent Trends
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

## Section: Creation of Credit/Deposits (14.5) 🔴

### Core Idea
Commercial banks do not just store money — they multiply it. When a bank advances a loan, it does not hand out cash; it credits the borrower's account, thereby creating a new deposit. Because the banking system as a whole keeps only a fraction of deposits as cash reserves, an initial primary deposit can balloon into a much larger volume of derivative deposits across the system. The maximum expansion is governed by the deposit/money multiplier.

> **In Simple Terms:** Think of the banking system as a chain of leaky buckets where each bucket spills 90% of what it gets into the next. A single rupee of fresh cash poured into the first bucket can refill the whole chain, leaving 10× the original water sloshing around as deposits — even though only one rupee of "new" water ever entered.

### Key Concepts

#### Primary vs Derivative Deposits
A **primary (actual) deposit** is created when a customer hands genuine cash to the bank — the bank's reserves rise rupee-for-rupee. A **derivative (created) deposit** arises when the bank itself sanctions a loan and credits the borrower's account; no cash changes hands, but the community's stock of money has just grown. The famous shorthand is "every loan creates a deposit." Derivative deposits are the actual mechanism of credit creation.

| Aspect | Primary Deposit | Derivative Deposit |
|---|---|---|
| Origin | Cash brought in by depositor | Loan sanctioned & credited by bank |
| Effect on reserves | Cash reserves of bank rise | No new cash; only book entry |
| Effect on money stock | No net change (cash → deposit) | Net increase in money supply |
| Other name | Actual deposit | Created deposit / credit creation |

#### The Deposit/Money Multiplier
For the banking system as a whole, the relationship between an initial primary deposit and the total expansion of deposits is:

`Δd = Δa / r`  ⭐

Where Δd = increase in total deposits in the system, Δa = increase in initial primary deposit, r = required cash reserve ratio. With r = 1/10, an initial deposit of ₹100 can support up to ₹1,000 of total deposits — a 10× expansion.

#### Banking System as a Whole vs Single Bank
A single bank cannot expand credit by 10× on its own — when it lends, the borrower spends and the cash drains away through the clearing house to other banks. But for the system collectively, those drains are simply transfers between banks; reserves stay inside the system, and the multiple expansion plays out fully.

### Definitions
- **Primary Deposit**: A deposit account opened by a bank by accepting cash from the public. ⭐
- **Derivative Deposit**: A deposit created by the bank in the process of granting credit; the loan, once sanctioned, is credited to the borrower's account, increasing the total stock of money. Identical to "credit creation." ⭐
- **Cash Reserve Ratio (r)**: The fraction (percentage) of deposits that a bank keeps in cash form (or with the central bank). ⭐
- **Credit Creation**: The power of banks to multiply loans and advances by creating deposits.

### Mechanisms / Processes
1. Customer A deposits ₹100 cash → bank holds ₹10 reserve, lends ₹90 to Borrower B.
2. B spends ₹90 → recipient deposits ₹90 in (some) bank → that bank holds ₹9, lends ₹81.
3. Process repeats; geometric series sums to ₹100 / 0.10 = ₹1,000 in total deposits.
4. Total new credit created = ₹900 (= ₹1,000 − ₹100 initial).

### Examples
**Example: 9/10 Reserve, ₹100 Initial Deposit**
With r = 0.10, Δd = 100 / 0.10 = ₹1,000. The system as a whole can expand deposits to ten times the initial cash injection. The textbook notes that bank deposits in any country are "many times as great as the total amount of cash in existence" — direct evidence the system is expanding deposits without an equivalent cash backing.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing a single commercial bank can multiply deposits 10×. → ✅ Correct: Only the banking system as a whole can; an individual bank loses cash to other banks via the clearing house.
- ❌ Mistake: Thinking banks "create money out of thin air." → ✅ Correct: Crowther — "the bank does not create money out of thin air; it transmutes other forms of wealth into money." The income-yielding securities in the economy set the outer limit.
- ❌ Mistake: Confusing primary and derivative deposits. → ✅ Correct: Primary = cash in; derivative = loan out.

### Edge Cases & Caveats
- The multiplier `Δd = Δa / r` is a maximum, not an automatic outcome — actual expansion depends on willingness to lend and to borrow.
- The bank cannot let its cash reserve fall below the required percentage of total deposit liabilities (textbook example: 10%).

> **Quick Recall:**
> - Formula: **Δd = Δa / r** (deposit multiplier) ⭐
> - With r = 1/10, system can create up to 10× initial deposit
> - Crowther: banks "transmute other forms of wealth into money"
> - "Every loan creates a deposit"

### Connections
- Builds on: Functions of Commercial Banks (Section 14.3, Chunk 2) — loans/advances and deposit acceptance
- Contrasts with: NBFIs which only "purvey" credit (Section 15.2.1, Chunk 4) — banks "create" credit
- Connects to: Cash Reserve Ratio as a monetary policy tool (Block on monetary policy)

### Open Questions
1. How is the simple multiplier modified once we introduce currency drains and excess reserves (Phillips' "leaky multiplier")?

---

## Section: Limits to Credit Creation (14.5.1) 🔴

### Core Idea
Banks' power to create credit is real but bounded. Seven institutional, behavioural and policy limits keep the multiplier from running unchecked. They span the structure of the banking system, public habits, the borrower side of the market, the macro cycle and the central bank's discretion.

> **In Simple Terms:** The credit multiplier is like a pressure cooker — it can build pressure, but seven safety valves (clearing rules, liquidity rules, cash supply, public preferences, collateral, the business cycle, and RBI policy) keep it from exploding.

### Key Concepts

#### Seven Limits to Credit Creation
A complete listing of the limitations the textbook identifies:

| # | Limit | What it does |
|---|---|---|
| i | Clearing House Restriction on a Single Bank | One bank cannot expand alone — it would lose cash to others through clearing; banks must move in step. |
| ii | Liquidity Ratio | Bank must keep a prudent share of assets liquid; this caps how much it is willing to lend or invest. |
| iii | Amount of Cash in Existence | Government and central bank fix the supply of legal tender; total cash sets the base on which the multiplier works. |
| iv | Cash People Prefer to Hold | If the public hoards cash instead of depositing it, deposits cannot grow; greater cheque/digital use eases this. |
| v | Collateral Security Available | Banks lend against acceptable security (the more shift-able, the better); shortage of good security limits lending. |
| vi | State of the Economy | Loans are taken only when there are profitable ventures; in a downturn, demand for credit dries up. |
| vii | Monetary Policy of the Central Bank | RBI's tools (CRR, SLR, repo, OMO etc.) can directly throttle bank credit expansion. |

### Definitions
- **Collateral Security**: An asset pledged by the borrower that the bank can convert to cash if the loan is not repaid; the more liquid (shift-able) the security, the more acceptable it is.
- **Legal Tender Money**: Currency whose acceptance in payment of debt cannot be refused; supply is determined by the government and central bank.

### Mechanisms / Processes
1. Crowther's qualifying observation: banks do not create money "out of thin air" — they convert (transmute) other wealth (income-yielding securities) into money.
2. The total volume of income-yielding securities sets the overall ceiling on credit creation.
3. The bank must keep a minimum cash reserve (e.g., 10%) against deposit liabilities.

### Examples
**Example: Why a Single Bank Cannot Expand Alone**
If Bank A alone doubles its lending, borrowers spend the new deposits, and cheques drawn on Bank A are cleared in favour of Banks B, C, D… Bank A loses cash, breaches its liquidity ratio, and is forced to contract. Hence credit policy must be co-ordinated across banks.

### ⚠️ Common Mistakes
- ❌ Mistake: Listing only the central bank's monetary policy as the limit. → ✅ Correct: Six other limits (some structural, some behavioural) are equally binding.
- ❌ Mistake: Treating "collateral security" only as a borrower's problem. → ✅ Correct: It is also a system-level limit — economy-wide shortage of good security caps total bank lending.
- ❌ Mistake: Assuming character of borrower is irrelevant once collateral is given. → ✅ Correct: Textbook is explicit — "the first consideration is the character of the borrower"; the bank prefers the loan to be repaid and collateral to be a last resort.

### Edge Cases & Caveats
- Increasing public confidence in banks and wider cheque/digital use directly **relax** limit (iv).
- Limits (vi) and (vii) are pro-cyclical and policy-driven respectively — they vary in tightness over time.

> **Quick Recall:**
> - SEVEN limits: (i) clearing house, (ii) liquidity ratio, (iii) cash in existence, (iv) cash public prefers to hold, (v) collateral, (vi) state of economy, (vii) monetary policy of central bank
> - Crowther: banks transmute, not create from thin air
> - First consideration in lending = character of borrower; collateral is fallback

### Connections
- Builds on: Section 14.5 Credit Creation (this chunk)
- Connects forward to: Monetary policy tools (CRR, SLR, OMO) elsewhere in MEC-110
- Contrasts with: NBFIs which lend only out of resources placed with them (Section 15.2.1, Chunk 4)

### Open Questions
1. How would the seven limits look re-cast in a digital economy where cash holdings are minimal and clearing is real-time?

---

## Section: Principles Governing Distribution of Assets (14.6) 🟡

### Core Idea
A banker is "torn between two conflicting motives" — earning profit by lending, and preserving liquidity to meet depositor demands on cash. The actual distribution of bank assets is a compromise between these. Cash earns nothing, so banks "minimise" cash but keep enough near-cash assets to absorb shocks.

> **In Simple Terms:** A banker is like a shopkeeper who cannot let the till run dry but also cannot afford to keep the entire stock as cash. So they keep just enough cash, a stack of easy-to-sell items behind it, and the bulk of stock in higher-margin but slower-moving goods.

### Key Concepts

#### The Banker's Conflicting Motives
- Wants to expand loans → more profit.
- Wants to hold enough cash → meet depositors' demand for withdrawals on demand.
- Cash is barren (zero income), so banks **minimise** cash.
- Banks therefore hold **fairly liquid** assets that can be turned into cash quickly with little or no loss.
- The asset distribution is a **compromise** between desire for profit and desire for liquidity.

#### Four Most Liquid Items in a Bank's Balance Sheet
The textbook names the first four items of a clearing bank's balance sheet as the most liquid:
1. Notes and coins
2. Balances with the Central Bank (RBI)
3. Bills
4. Market loans

All four can be turned into cash quickly with little if any financial loss.

#### Shift-ability of Assets
"Shift-ability" is one aspect of liquidity — the ease with which an asset can be passed on to another institution (e.g., the central bank). Most bank assets are shift-able to varying degrees, **except** advances supported merely by the borrower's good name.

### Definitions
- **Shift-ability**: The ease with which an asset can be transferred to another institution (especially the central bank) without significant loss; a key dimension of liquidity beyond mere "cashability."

### Mechanisms / Processes
1. Identify obligation: must pay cash on demand to depositors.
2. Identify motive: must earn profit for shareholders.
3. Sort assets by liquidity: cash (most liquid, zero return) → near-cash (bills, market loans) → loans/investments → property (least liquid, highest return).
4. Distribute holdings so the liquidity buffer covers normal and abnormal cash demands while the bulk earns income.

### Examples
**Example: Why Pure Bad-Debt-Style Advances Sit Apart**
A clean loan supported only by the borrower's reputation cannot be sold to or rediscounted with another institution. It therefore sits outside the shift-able universe and counts as a low-liquidity asset, no matter how creditworthy the borrower.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating "liquidity" only as cash-on-hand. → ✅ Correct: Liquidity also includes shift-ability — convertibility through transfer to another institution.
- ❌ Mistake: Assuming banks would prefer to hold maximum cash. → ✅ Correct: Cash is barren; banks **minimise** cash and rely on near-cash buffers.

### Edge Cases & Caveats
- The compromise tilts according to the bank's risk appetite, regulator's directives and the macro environment.

> **Quick Recall:**
> - Four most liquid items: notes/coins, balances with RBI, bills, market loans
> - Two motives in conflict: profit vs liquidity
> - Shift-ability ≠ pure cashability; it is transfer to another institution
> - Cash = the most barren of all investments

### Connections
- Builds on: Functions of commercial banks (Section 14.3, Chunk 2)
- Leads into: Liquidity vs Profitability (Section 14.6.1, this chunk)

### Open Questions
1. How does the rise of secondary markets and securitisation change the "shift-ability" classification of long-dated loans?

---

## Section: Liquidity vs Profitability of Assets (14.6.1) 🔴

### Core Idea
Liquidity and income-yielding capacity are **two opposite criteria** that every bank must reconcile. The most liquid asset (money) earns nothing; the highest-earning asset (long-term loans, property) is illiquid. The "secret of success" is striking a sound balance. The traditional liquidity concept has progressively given way to **shift-ability** and then the **anticipated income** concept.

> **In Simple Terms:** Imagine ranking food in your kitchen by how quickly you can eat it versus how nutritious it is. Tap water is instant but offers nothing; a slow-cooked stew is rich but not ready when guests arrive. The bank must keep a meal at every stage of "readiness vs richness."

### Key Concepts

#### The Liquidity-Profitability Trade-off
The more liquid an asset, the less income it yields, and vice versa. A bank that pursued only liquidity would hold all assets as money — earning nothing. A bank that pursued only profit would lock everything into long-term loans and property — risking insolvency to depositors. Banks therefore array their assets along a spectrum of liquidity vs profitability.

| Aspect | Liquidity | Profitability |
|---|---|---|
| Goal | Meet depositors' cash demand on time | Maximise income for shareholders |
| Most extreme asset | Cash / money | Long-term loans, property |
| Income | Low or zero | High |
| Convertibility | Quick, without loss | Slow, possibly with loss |
| Risk to bank if neglected | Loss of public confidence, bank run | Loss of profitability, shareholder discontent |

#### Anticipated Income Concept
The textbook describes a third stage in the evolution of the liquidity idea. Term loans are "liquidated" not by sale or rediscounting but by the **anticipated future income** of the borrower — the borrower saves and repays out of future earnings. This justifies financing of durable consumer goods (cars, white goods), where the asset cannot be sold or shifted to fund repayment.

### Definitions
- **Anticipated Income Concept**: A liquidity doctrine under which loans are repaid out of the borrower's expected future income rather than by selling or shifting the asset; underpins consumer-durable and term lending.
- **Shift-ability Concept**: The doctrine that an asset is liquid if it can be transferred to another institution (especially the central bank); broader than pure cashability and enables longer-dated lending.

### Mechanisms / Processes
1. Traditional concept of liquidity → focus on cash/near-cash.
2. Replaced by shift-ability concept → liquidity through transferability to other institutions; allows longer-dated, broader lending.
3. Replaced/supplemented by anticipated income concept → liquidity through borrower's future income stream.

### Examples
**Example: Loan to Buy a Refrigerator**
A loan to purchase a durable consumer good cannot be sold off and cannot be rediscounted with the central bank. Yet the bank treats it as "liquid enough" because the borrower's anticipated wages over the loan tenor will repay it. This is the anticipated income concept in action.

### ⚠️ Common Mistakes
- ❌ Mistake: Saying liquidity and profitability are independent goals. → ✅ Correct: They are opposite criteria — one comes at the cost of the other.
- ❌ Mistake: Treating shift-ability and anticipated income as the same thing. → ✅ Correct: Shift-ability = transfer to another institution; anticipated income = repayment out of future earnings.

### Edge Cases & Caveats
- The "secret of success" depends on the macro environment; in stress, what was shift-able may suddenly become illiquid.
- For consumer-durable loans, only the anticipated income concept rationalises calling them "liquid."

> **Quick Recall:**
> - Liquidity ↔ profitability are **opposite** criteria
> - Three stages of liquidity thinking: traditional → shift-ability → anticipated income
> - Cash = most liquid, zero income
> - Long-term loans/property = highest income, lowest liquidity

### Connections
- Builds on: Section 14.6 Asset Distribution (this chunk)
- Anchored by: Crowther's view (Section 14.5.1)
- Connects to: Asset-liability management and Basel-style liquidity ratios (later units)

### Open Questions
1. How does the Liquidity Coverage Ratio (LCR) under Basel III formalise the trade-off discussed here?

---

## Section: Recent Trends and Performance of Banking Industry in India (14.7) 🟡

### Core Idea
Indian banking in the last decade has been reshaped by digital payments, fintech, new bank categories (SFBs, Payments banks, Neobanks), and improved prudential indicators. As of mid-2024, banks are well-capitalised with multi-year-low NPAs. The June 27, 2024 Financial Stability Report (FSR) confirms broad-based resilience.

> **In Simple Terms:** The Indian banking sector has been simultaneously going digital and going specialised — a stack of fintechs and new bank categories now sits on top of older commercial banks, while the foundations (capital, asset quality) are the strongest they have been in years.

### Key Concepts

#### Digital Payments & Fintech Growth
- April 2024: 581 banks active on UPI; 15.08 billion digital transactions worth US$ 25.27 billion (₹2.1 trillion) for the period.
- Digital lending: US$ 75 billion in FY18 → estimated US$ 1 trillion by FY23 (5× rise in disbursements).
- Indian fintech market: US$ 29 billion funding across 2,084 deals (Jan 2017–Jul 2022) = 14% of global funding (2nd by deal volume).
- By 2025: Indian fintech market projected at ₹6.2 trillion (US$ 83.48 billion).
- IMPS is the only system at level 5 in the Faster Payments Innovation Index (FPII) across 25 countries.

#### Innovative Banking Models
| Model | Key Facts |
|---|---|
| Small Finance Banks (SFBs) | Licensed since 2015; minimum capital ₹200 cr (vs ₹500 cr for commercial banks); offer **basic banking services only**; serve unbanked/underbanked. After Fincare SFB merged into AU SFB on **April 1, 2024**, total SFBs = **11**. |
| Payments Banks | **4** in operation. **Cannot lend** or issue **credit cards**. |
| Neobanks | Digital-only platforms; no physical presence. RBI does not allow fully digital establishments → operate via partnerships with physical banks. |
| IPPB (India Post Payments Bank) | Aadhaar-based access via Postman/Gramin Dak Sevak; reach into villages. |

Other reach-expanding initiatives: Pradhan Mantri Jan Dhan Yojana, India Post Payments Bank.

#### Banking Sector Resilience — FSR (June 27, 2024) Highlights
The 29th issue of the Financial Stability Report, released by RBI on June 27, 2024, summarises the assessment by the Sub-Committee of the FSDC. Key indicators (end-March 2024):

| Indicator | Value (end-March 2024) |
|---|---|
| CRAR (SCBs) | 16.8% |
| CET1 ratio (SCBs) | 13.9% |
| GNPA ratio (SCBs) | 2.8% (multi-year low) |
| NNPA ratio (SCBs) | 0.6% |
| NBFC CRAR | 26.6% |
| NBFC GNPA | 4.0% |
| NBFC RoA | 3.3% |
| Projected CRAR Mar 2025 (baseline / medium / severe stress) | 16.1% / 14.4% / 13.0% |

Trend since 2020-21: SCBs improved asset quality, capital buffers and profitability despite the pandemic; healthy balance-sheet growth in 2021-22 and 2022-23 with broad-based credit acceleration.

### Definitions
- **Small Finance Bank (SFB)**: A specialised banking entity that serves financially under-served sections of society; minimum capital ₹200 cr; limited to basic banking services. ⭐
- **Payments Bank**: A category of commercial bank that can accept deposits and provide payment services but **cannot lend or issue credit cards**. ⭐
- **Neobank**: A digital-only banking platform with no physical presence; in India, partners with physical banks since RBI does not yet permit fully digital establishments.
- **CRAR (Capital to Risk-weighted Assets Ratio)**: A bank's capital expressed as a percentage of its risk-weighted assets; a core prudential measure.
- **CET1 (Common Equity Tier 1)**: The highest-quality capital component (mainly equity and retained earnings) as a percentage of risk-weighted assets.
- **GNPA / NNPA**: Gross / Net Non-Performing Assets ratio — proportion of loans on which interest/principal is overdue (gross) and net of provisions.
- **Differentiated Banking**: A specialised banking identity that serves under-served segments efficiently (e.g., SFBs, Payments banks).

### Mechanisms / Processes
1. RBI grants differentiated bank licenses (SFBs from 2015; Payments banks).
2. Schemes such as PMJDY and IPPB push physical reach.
3. UPI/IMPS push digital reach; fintech lending channels widen.
4. Combined effect: financial inclusion deepens; credit cycle is supported.

### Examples
**Example: Fincare-AU Merger (April 1, 2024)**
Fincare SFB merged into AU SFB effective April 1, 2024. The post-merger SFB count is **11** (down from 12). This is the kind of consolidation update that frequently appears as a fill-in-the-blank/MCQ item.

### ⚠️ Common Mistakes
- ❌ Mistake: Saying Payments banks can lend. → ✅ Correct: They can neither lend nor issue credit cards.
- ❌ Mistake: Listing 12 SFBs (pre-merger figure). → ✅ Correct: 11 SFBs after Fincare-AU merger on April 1, 2024.
- ❌ Mistake: Confusing CRAR with CET1. → ✅ Correct: CRAR is total regulatory capital / RWA; CET1 is just the highest-quality slice / RWA.

### Edge Cases & Caveats
- Stress-test CRAR projections (16.1/14.4/13.0%) are conservative hypothetical scenarios, not forecasts.
- "Digital lending US$ 1 trillion by FY23" is a forward-looking estimate, not a confirmed actual.

> **Quick Recall:**
> - SFBs: **11** (post Fincare-AU merger, April 1, 2024); ₹200 cr min capital
> - Payments banks: **4**; cannot lend or issue credit cards
> - FSR June 27, 2024: CRAR **16.8%**, CET1 **13.9%**, GNPA **2.8%**, NNPA **0.6%** (end-March 2024)
> - NBFCs: CRAR **26.6%**, GNPA **4.0%**, RoA **3.3%**
> - IMPS = level 5 in FPII (only one of 25 countries)

### Connections
- Builds on: Structure of Commercial Banks (Section 14.4, Chunk 2)
- Connects to: NBFCs covered in Unit 15 (Chunk 4) — note NBFC CRAR figure
- Anchors policy units later in MEC-110

### Open Questions
1. Will neobanks in India ever be granted standalone licences, or will the partnership model harden?
2. How will the next Fincare-style consolidations reshape the SFB market?

---

## Section: Summary and Key Words (14.8-14.9) 🟢

### Core Idea
A consolidating recap: banks mobilise savings and channel them to productive users; act as efficient payment conduits; operate on **fractional reserves**; create credit through derivative deposits; balance liquidity vs profitability; and have lately diversified into digital and differentiated forms.

> **In Simple Terms:** Section 14.8 is the textbook's "exam revision cheat-sheet" for Unit 14 — every theme that mattered shows up here in one paragraph each.

### Key Concepts

#### Recap of Unit 14 Themes
1. Banks as unique financial intermediaries (savings mobilisation + payment conduits).
2. Three deposit types (current, savings, fixed) reclassified into demand vs time.
3. Loans, advances, bill discounting, open-market investment.
4. Fractional reserve banking is the basis of profitability.
5. Credit creation via primary → derivative deposits, with limits.
6. Asset distribution = compromise between paying cash on demand and earning profit.
7. Banks promote capital formation and economic development.
8. Digital payments, neo-banking, SFBs etc. are the new edges of the system.

### Definitions (all ⭐ — exam-important Key Words)
- **Banks**: Financial institutions that accept deposits and make loans. ⭐
- **Bill of Exchange (Draft)**: A negotiable instrument with three parties — the **drawer** (issues the order), the **drawee** (ordered to make payment) and the **payee** (receives payment). A commercial bank cheque is a draft on the bank by the depositor payable to a designated payee. ⭐
- **Cash Reserve Ratio (CRR)**: The fraction of deposits that the RBI requires banks to keep as reserves. ⭐
- **Central Bank**: The government agency that oversees the banking system and is responsible for the amount of money and credit supplied to the economy. In India, the **Reserve Bank of India**. ⭐
- **Credit Creation**: The power of banks to multiply loans and advances by creating deposits. ⭐
- **Derivative Deposits**: Deposits created by the bank in the process of granting credit; loan sanctions credited to borrowers' accounts increase the total stock of money. Identical to credit creation by commercial banks. ⭐
- **Differentiated Banking**: A specialised banking identity that serves the underserved segments of the economy/society efficiently. ⭐
- **Liquidity**: The relative ease and speed with which an asset can be converted into cash. ⭐
- **Primary Deposit**: A deposit account opened by a bank by accepting cash from the public. ⭐
- **Vault Cash**: Currency physically held by banks and stored in vaults overnight. ⭐

### Mechanisms / Processes
1. Acceptance of deposits (current/savings/fixed → demand/time).
2. Grant of credit (loans, advances, bill discounting, market investments).
3. Fractional reserve operation → credit creation via derivative deposits.
4. Asset distribution managed for liquidity vs profitability.
5. Channelling of savings into priority industries → capital formation → economic growth.

### Examples
**Example: Bill of Exchange Trio**
A bill drawn by Trader X on Buyer Y in favour of Bank Z has X = drawer, Y = drawee, Z = payee. A commercial bank cheque is structurally the same: depositor (drawer) orders the bank (drawee) to pay the named beneficiary (payee).

### ⚠️ Common Mistakes
- ❌ Mistake: Treating Vault Cash as part of CRR. → ✅ Correct: Vault cash is currency physically inside the bank's vaults, separate from CRR balances with the RBI.
- ❌ Mistake: Defining liquidity only as "cash on hand." → ✅ Correct: It is the **ease and speed** of converting an asset to cash — a continuum, not a binary.

### Edge Cases & Caveats
- The Useful Books list (14.10) is reference material; not exam-testable but flags Crowther, Gupta, Mishkin, Hubbard etc. as the canonical sources behind this unit.
- Check Your Progress 3 answers point readers to Sections 14.7 and 14.6.1 — i.e., the high-yield material above.

> **Quick Recall:**
> - 10 Key Words to memorise (all ⭐)
> - Banks = create credit; Crowther = "transmute, not create from thin air"
> - Liquidity = ease + speed of conversion to cash
> - Vault cash ≠ CRR
> - Differentiated banking = SFBs, Payments banks etc.

### Connections
- Recaps: All earlier sections of Unit 14 (Chunks 2 and 3)
- Sets up: Unit 15 NBFIs (Chunk 4) by emphasising banks' uniqueness as credit creators

### Open Questions
1. Which of the ten Key Words has been redefined or sharpened by post-2020 RBI circulars (e.g., the CRR/SLR framework changes)?
