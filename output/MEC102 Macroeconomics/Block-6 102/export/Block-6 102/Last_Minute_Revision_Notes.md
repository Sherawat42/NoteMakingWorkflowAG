# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics


**Quick Recall:**
- Barter fails because of the **double coincidence of wants** problem.
- Money's three functions: **unit of account, medium of exchange, store of value**.
- Fiat money = no intrinsic value; commodity money = intrinsic value.

### Measures of Money Supply 🔴

**Why money supply has multiple definitions**

**What is excluded from money supply**
- Money held as **CRR (Cash Reserve Ratio)** with the RBI.
- Money held as **SLR (Statutory Liquidity Ratio)** with commercial banks.
- Money held by the government.

**History of monetary aggregate working groups**
| Year | Body | Role |
|------|------|------|
| 1961 | First Working Group on Money Supply (FWG) | First framework |
| 1977 | Second Working Group (SWG) | Revision |
| 1998 | Working Group on Money Supply: Analytics and Methodology of Compilation (WGMS) | Introduced NM0–NM3 and L1–L3 aggregates |
| Aggregate | Components | Nickname |
|-----------|-----------|----------|
| **M0** | Currency in circulation + Bankers' deposits with RBI + 'Other deposits' with RBI | Reserve money / monetary base / high-powered money / central bank money |
| **M1** | Currency with the public + Demand deposits with banks + 'Other deposits' with RBI | Narrow money |
| **M2** | M1 + Savings deposits of post office savings banks | — |
| **M3** | M1 + Time deposits with the banking system | Broad money |
| **M4** | M3 + All deposits with post office savings banks (excl. National Savings Certificates) | — |
| Aggregate | Components |
|-----------|-----------|
| **NM0** | Monetary base = Currency in circulation + Bankers' deposits with RBI + 'other deposits' with RBI |
| **NM1** | Currency with the public + Demand deposits with the banking system + 'Other deposits' with RBI (non-interest-bearing monetary liabilities of the banking sector) |
| **NM2** | NM1 + Short-term time deposits of residents (≤ 1 year contractual maturity) — represents transactions balances |
| **NM3** | NM2 + Long-term time deposits of residents + Call/Term funding from financial institutions |
| | Components |
|---|-----------|
| **L1** | NM3 + All deposits with the post office savings banks (excl. NSCs) |
| **L2** | L1 + Term deposits with term lending and refinancing institutions (FIs) + Term borrowing by FIs + Certificates of deposit issued by FIs |
| **L3** | L2 + Public deposits of non-banking financial companies |

**Why NM2/NM3 cover *residents* only**
- **Total stock of money** = money with public + money with RBI + money with government.
- **Money supply** = first component only (money held with the public).
- **Narrow money** = M0, M1 (easily converted into cash).
- **Broad money** = M3 (less liquid, includes time deposits).

### ⚠️ Common Mistakes
- ❌ Including CRR/SLR balances in money supply → ✅ They are excluded; they are out of circulation.
- ❌ Treating "currency in circulation" as the entire money supply → ✅ Currency is just one component; demand deposits and other deposits also count.
- ❌ Conflating M0 with M1 → ✅ M0 is reserve money (central-bank money); M1 adds demand deposits at commercial banks.

**Quick Recall:**
- M0 = Reserve / high-powered money. M3 = Broad money.
- M1 includes demand deposits; M3 adds time deposits.
- Money supply = money held by the **public only** (excludes RBI, government, CRR, SLR).
- Sole authority compiling monetary stats since **July 1935**: RBI.
- WGMS (1998) introduced NM0–NM3 and L1–L3.
---

### Money Multiplier 🔴

**Numerical illustration (from text, India 2022)**
- Deposit: ₹1,000.
- CRR = 4.5% → ₹45 to RBI.
- SLR = 18% → ₹180 in cash, gold, government securities.
- Available for lending: **₹775**.

**Mathematical Derivation**
- C = currency held by general public
- D = demand deposits held by general public
- R = bank reserves (cash held by banks + their demand deposits at central bank)
- $cd = C/D$ → desired **currency–deposit ratio** (chosen by the non-bank public)
- $rd = R/D$ → required **reserve ratio** (set by central bank via CRR + bank's excess reserves)

**Four Implications of equation (15.3)**
| # | Implication |
|---|---|
| (a) | Multiplier is **higher** for broader money measures (e.g. M3 > M1) |
| (b) | $m$ depends on $cd$ and $rd$; both vary with expected returns, liquidity, and risk on alternative assets |
| (c) | $\Delta M1 = m \cdot \Delta M0$ — knowing $m$ lets the central bank target $M1$ via $M0$ |
| (d) | Higher $rd$ → lower $m$ → less money supply (this is how raising **CRR/SLR** tightens monetary policy) |

**Alternative Interpretation — Currency-Money Ratio**
- **Great Depression (1929–1933, US):** money multiplier fell sharply. Depositors panicked and withdrew, raising $cd$; banks held more reserves, raising $rd$ — both pulled $m$ down. *Lesson:* multiplier is stable in normal times but breaks during banking crises.

### ⚠️ Common Mistakes
- ❌ Using $m = 1/rd$ as the universal formula → ✅ That ignores currency holdings; the full formula is $m = (cd+1)/(cd+rd)$.
- ❌ Treating $cd$ and $rd$ as constants → ✅ They shift with risk perception, liquidity preference, and crises.
- ❌ Thinking the multiplier creates *real* wealth → ✅ It creates deposit *money*, not goods.
- $rd$ includes both required CRR and any **excess reserves** banks voluntarily hold for liquidity/lending-risk reasons.
- The multiplier assumes leakages (cash withdrawals) are stable; in crises this assumption fails.

**Quick Recall:**
- **Money multiplier formula**: $m = \dfrac{cd + 1}{cd + rd}$.
- $\Delta M1 = m \cdot \Delta M0$.
- $cd$ chosen by **public**; $rd$ set by **central bank** (CRR) + bank's excess reserves.
- Higher CRR/SLR → lower $m$ → tighter money supply.
- Multiplier collapses in banking panics (Great Depression example).
- Builds on: Measures of Money Supply (Chunk 001) — uses M0, M1 definitions.
- Is prerequisite for: Open Market Operations (Chunk 001) — OMO works *through* the multiplier.

### Open Market Operations (OMO) — Introduction 🔴

**Four Functions of a Central Bank**
1. **Banker's bank / lender of last resort** — maintains solvency and liquidity of commercial banks.
2. **Promotes stable economic growth.**
3. **Stabiliser of purchasing power** — maintains stable inflation.
4. **Manages exchange rate** — reduces volatility.

**Expansionary vs Contractionary OMO**
| | Expansionary | Contractionary |
|---|---|---|
| Action | Central bank **buys** government securities | Central bank **sells** government securities |
| Effect on monetary base | Increases | Decreases |
| Bank balance sheet | Shifts from income-producing securities → non-income-producing excess reserves | Reverse |
| Bank response | Convert excess reserves to new loans by **lowering interest rate** | Reduces lending |
| Used when | Higher demand for liquidity; rates need to be kept in check | Money supply needs to be shrunk |
- **Open Market Operations (OMO)** ⭐: process of increasing or reducing the monetary base by buying (expansionary) or selling (contractionary) government securities in the open market.
- **Expansionary monetary policy**: central-bank stance that increases monetary base / lowers interest rates to stimulate the economy.
- **Contractionary monetary policy**: stance that reduces monetary base / raises interest rates to curb demand.

### ⚠️ Common Mistakes
- ❌ "OMO = printing money" → ✅ OMO swaps central-bank reserves for securities; it changes M0's *composition* and effective supply, not raw note printing.
- ❌ Thinking OMO directly determines lending rates → ✅ It changes reserves; *banks* then choose to lower lending rates to deploy them.

**Quick Recall:**
- **Buy bonds = expansion**; **sell bonds = contraction**.
- OMO works *through* the money multiplier — small ΔM0 → larger ΔM1.
- Four central-bank functions: lender of last resort, growth, price stability, exchange-rate management.
- Builds on: Money Multiplier (Chunk 001).
- Continues into: Box 15.1 on Repo/Bank Rate and sterilisation (Chunk 002).
1. How do liquidity preferences (cd) shift in a digital-payment economy where less currency is held?
2. Why might banks *not* lend out new reserves even when OMO injects them (e.g. liquidity trap)?

### Repo Rate, Reverse Repo Rate, Bank Rate (Box 15.1) 🔴

**Comparison Table ⭐**
| Rate | Borrower | Lender | Securities? | Repurchase agreement? |
|------|---------|--------|-------------|------------------------|
| **Repo Rate** | Commercial bank | RBI | Yes | Yes |
| **Reverse Repo Rate** | RBI | Commercial bank | (Bank parks cash with RBI) | — |
| **Bank Rate / Discount Rate** | Commercial bank | RBI | No | No |
| **Overnight Rate** | Commercial bank | Another commercial bank | — | — |

**How RBI uses Repo Rate to Manage Liquidity**
- To **increase liquidity**: RBI **reduces** the repo rate → banks find borrowing cheaper → they sell securities to RBI and borrow more.
- To **decrease liquidity / supply of money**: RBI **raises** the repo rate → discourages banks from borrowing.

**How Bank Rate Affects Money Supply**
- **Repo Rate**: rate of interest charged by RBI on cash borrowed by commercial banks against the sale of securities or bonds with an agreement to repurchase those securities at a predetermined price on a future date.
- **Reverse Repo Rate**: rate at which RBI pays interest on the excess funds commercial banks deposit with RBI.
- **Bank Rate (Discount Rate)**: rate of interest charged by RBI on loans extended to commercial banks and other financial institutions, with **no repurchase agreement, no securities sold, no collateral**.
- **Overnight Rate**: rate at which commercial banks borrow funds among themselves (bank-to-bank).
- Repo example: Commercial bank borrows ₹100,000 from RBI at repo rate 5% → interest at maturity = **₹5,000**.
- Reverse repo example: Commercial bank deposits ₹100,000 with RBI at reverse repo rate 4% → interest received = **₹4,000**.

### ⚠️ Common Mistakes
- ❌ Confusing repo rate with bank rate → ✅ Repo involves securities + repurchase; bank rate does not.
- ❌ Thinking reverse repo means RBI borrowing externally → ✅ It means banks parking cash with RBI for interest.

**Quick Recall:**
- **Repo = banks borrow from RBI against securities (with repurchase).**
- **Reverse repo = banks lend to RBI / park cash at RBI.**
- **Bank rate = RBI lends without collateral; bank rate > repo rate.**
- **Overnight rate = inter-bank borrowing.**
---
- **Sterilisation** ⭐: the process of neutralising the impact of changes in foreign exchange reserves on domestic money supply through Open Market Operations (selling government securities to absorb the extra money supply created by forex purchases).

**Quick Recall:**
- Sterilisation = **OMO used to offset money-supply effects of forex intervention**.
- Buying foreign currency injects rupees → sell securities to mop up.

**Quick Recall:**
- $M_d = f(Y, i)$ — increasing in Y, decreasing in i.
- Expansionary OMO shifts $M_s$ right → interest rate falls → AD rises.
- Selling securities = contractionary; raises interest rate, cuts AD, controls inflation.
| School | Money Neutrality? | Policy Recommendation |
|--------|-------------------|----------------------|
| **Classical** | Yes — money does not affect prices or growth; "duality" between monetary and real variables | Minimal intervention |
| **Keynesian** | No — ↑M → ↓i → ↑investment → ↑output via multiplier | Active, countercyclical policy |
| **New Classical** | Yes (rationally) — anticipated policy is ineffective | Stick to fixed **policy rules** |

**Quick Recall:**
- **Classical / New Classical**: money neutral → rules.
- **Keynesian**: money matters → countercyclical (active) policy.
- Note: **Unit 5** of the course already established that with flexible exchange rates, monetary policy is effective.

### Types of Monetary Policy 🔴

**Expansionary vs Contractionary**
| | Expansionary | Contractionary |
|---|---|---|
| **Aim** | Stimulate economy, boost investment/output | Control inflation, cool overheated economy |
| **Interest rate** | Lower than usual | Higher than usual |
| **Money supply** | Abnormally increased | Abnormally low |
| **Mechanism** | Cheaper credit → ↑ investment → ↑ employment, output | Costlier credit → ↓ investment, consumption |
| **Risk** | Currency depreciation (forex deterioration); higher inflation | Recession (↓ production, ↑ unemployment, ↓ AD) |
- **Monetary Policy**: macroeconomic policy set by the central bank or monetary authority of a country, concerned with the management of money supply in the economy.
- **Expansionary monetary policy** ⭐: policy that lowers interest rates or increases money supply to stimulate investment and growth.
- **Contractionary monetary policy** ⭐: policy that raises interest rates or restricts money supply to control inflation.

**Objective of Monetary Policy**

**Quick Recall:**
- **Expansionary** = ↑M / ↓i → ↑output, ↑employment, but risks ↑inflation and currency depreciation.
- **Contractionary** = ↓M / ↑i → controls inflation, but risks recession.

### Goals vs Targets of Monetary Policy 🔴

**Goals — Six Objectives ⭐**
| Goal | Why it matters |
|------|----------------|
| **Price stability** (containing inflation) | Foremost in developing economies; high inflation hurts growth and distribution |
| **Economic growth** | Real national income must rise; needs higher saving + investment |
| **Exchange-rate stability** | Critical under floating exchange rates |
| **Full employment** | Maximises social welfare |
| **Balance of Payments (BoP) equilibrium** | Avoids unsustainable CAD |
| **Reduction of economic inequality** | Equitable income/wealth distribution via priority-sector credit |

**Targets — Three Parameters**
1. **Supply of money / credit** — regulate.
2. **Rate of interest / cost of money** — keep at reasonable level.
3. **Availability of credit** — convenient access.

**Goal-by-goal details**
- "Relative" price stability — does not mean *zero* inflation. A modest rate gives producers incentive to expand.
- Ideal rate varies: **US ≈ 2%**; **India = 4% with ±2% tolerance band** (i.e., 2%–6%).
- Examples (2019): Venezuela ≈ **10 million % per year**; Argentina, Iran, Sudan ≈ **above 25%/year**.
- Abnormally high inflation: ↑ cost of living for poor; ↑ export prices; ↓ savings → ↓ growth; encourages unproductive investment (jewelry, real estate).
- Stage matched: high inflation → contractionary; stable inflation → balanced growth-employment policy.
- Needs higher saving + investment rates.
- Tools: priority-sector lending, interest-rate adjustments to incentivise saving.
- **Trade-off**: Growth target conflicts with **exchange-rate stability**. To prevent currency depreciation, tight monetary policy is needed — but high rates cut liquidity, raise lending costs, reduce production, raise unemployment.
- Under flexible exchange rates, exchange rate determined by demand/supply of forex.
- Domestic investors demand foreign currency when foreign investments are profitable; demand home currency when domestic investments are profitable.
- Central-bank tools to prevent rupee depreciation:
  1. Release foreign currency from forex reserves.
  2. Increase short-term lending rates.
  3. Increase **CRR** to reduce demand for foreign currency.
- All workers employed at prevailing wage rate.
- Conflicts with **tight monetary policy**.
- Achieved via expansionary monetary policy.

### ⚠️ Common Mistakes
- ❌ Treating "goals" and "targets" as synonyms → ✅ Goals are end-objectives; targets are intermediate operational variables.
- ❌ Assuming all goals are pursued equally → ✅ Priorities differ across countries and over time.
- ❌ Thinking price stability means zero inflation → ✅ Means a stable, *modest* rate (2–6% in India).

**Quick Recall:**
- **Goals** = price stability, growth, exchange-rate stability, full employment, BoP equilibrium, reduced inequality.
- **Targets** = money supply, interest rate, credit availability.
- **India inflation target**: 4% ± 2% (band 2%–6%).
- **US inflation target**: ≈ 2%.
- Goals **conflict**: growth vs exchange stability; full employment vs tight policy.
- Builds on: Types of Monetary Policy (Chunk 002).
- Continues into: Monetary Policy Instruments (Chunk 003) — the *tools* used to hit these targets.
1. Why does the trade-off between growth and exchange-rate stability matter more for developing economies?
2. Is reducing inequality a *legitimate* monetary-policy goal, or should it stay with fiscal policy?
| Cycle phase | Rate stance | Reason |
|-------------|-------------|--------|
| **Inflationary boom** | Higher than usual | Curb money supply |
| **Recession** | Lower than usual | Incentivise production, employment, growth |

**Quick Recall:**
- Three targets: money supply, cost (interest rate), availability of credit.
- Discriminatory rates: priority-sector lending = MSME, agriculture get lower rates.
- Inflation → ↑rates; recession → ↓rates.

### Monetary Policy Instruments — Quantitative Credit Control 🔴

**Quantitative vs Qualitative — Comparison ⭐**
| Aspect | Quantitative | Qualitative / Selective |
|--------|-------------|------------------------|
| Scope | Apply uniformly to whole banking system | Target specific sectors / borrowers |
| Discrimination | Non-discriminatory | Discriminatory |
| Examples | Bank rate, OMO, CRR, SLR | Margin requirements, credit rationing, direct action |

**The Four Quantitative Instruments**
- Definition: rate at which central bank lends to commercial banks and other financial institutions.
- ↑ Bank rate → ↑ economy-wide interest rates → ↓ credit creation → ↓ AD → ↓ prices.
- ↓ Bank rate → ↓ interest rates → ↑ credit (used in recession).
- Short-term borrowing from RBI uses **repo rate**; banks deposit excess at **reverse repo rate**.
- **Sell securities** → contract credit → ↓ AD → ↓ prices.
- **Buy securities** → expand credit → ↑ money supply → ↑ AD → ↑ output.
- Banks must keep a fixed % of total deposits as cash with the central bank.
- ↑ CRR → less left for lending → ↓ money supply.
- ↓ CRR → more available for lending → ↑ credit creation.
- Banks must keep a % of total deposits as **liquid (or near-liquid) assets** (cash, gold, government securities).
- ↑ SLR → ↓ credit; ↓ SLR → ↑ credit.
- **Quantitative credit control measures**: non-discriminatory monetary instruments that affect the entire banking system uniformly.
- **Qualitative / Selective credit control measures**: discriminatory monetary instruments targeting specific sectors or borrowers.
- **Bank Rate** (instrument view): rate of interest at which the central bank provides loans to commercial banks and other financial institutions.

**Quick Recall:**
- **4 quantitative tools**: Bank Rate, OMO, CRR, SLR.
- **3 qualitative tools**: Margin requirements, Credit rationing, Direct action.
- ↑CRR / ↑SLR / ↑Bank Rate / Sell-OMO → contractionary.
- ↓CRR / ↓SLR / ↓Bank Rate / Buy-OMO → expansionary.
- Builds on: OMO (Chunk 001), CRR/SLR (Chunk 001), Bank Rate (Chunk 002).

**Quick Recall:**
- 3 qualitative tools: margin requirements, credit rationing, direct action.
- Used to target *specific* sectors or borrowers — discriminatory by design.

### Monetary Policy in India 🔴

**16.5.1 Early Years of Monetary Policy (1950–mid-1980s)**
- **1950–1970**: RBI supported government's plan expenditure via **deficit financing** (industrialisation phase; large public-sector investment financed by RBI borrowing).
- Focus: **selective credit control** + flow of credit to priority sectors.
- **1971 to mid-1980s**: government relied more on fiscal policy; SLR and CRR were *increased*.
- **1985**: high inflation in 1980s → adoption of **monetary targeting framework** on the **Sukhamoy Chakravarty Committee** recommendations.

**Post-1991 Reforms**
- RBI's role changed significantly after 1991.
- **By 1997**: ad-hoc treasury bills completely phased out (curbed monetisation of fiscal deficit).
- Monetisation continued via primary issue of public debt.
- **Since April 2006**: RBI is **not allowed** to subscribe to the primary issue of public debt.

**16.5.2 Liquidity Adjustment Facility (1998 onwards)**
| Year | Event | Significance |
|------|-------|--------------|
| **1998** | RBI adopted **multiple indicator approach** | Tracked high-frequency financial-market rates + monthly indicators alongside output |
| **April 1999** | **Interim Liquidity Adjustment Facility (ILAF)** introduced | On Narasimham Committee (II) recommendations; repo and reverse repo emerged as primary policy rates; CRR/SLR significance reduced |
| **May 2011** | **Revised Liquidity Adjustment Framework (RLAF)** | **Repo rate became the only independently varying rate** — fixing the ILAF's flaws (no ceiling, no unique policy rate) |
| **Sep 2014** | RLAF fine-tuned | On Urjit Patel Committee recommendations |
| **May 2016** | **Monetary Policy Framework Agreement (MPFA)** signed between GOI and RBI | Inflation target: below 4% in FY 2016-17; RBI accountable to GOI on failure |
| **Feb 2019** | RBI started **accommodative monetary policy** | To stimulate ailing economy |
| **Aug 2019** | Formal linkage of repo rate to bank lending rates | Because Scheduled Commercial Banks (SCBs) were not transmitting rate cuts to public |
- **Liquidity Adjustment Facility (LAF)**: framework introduced 1999 (interim, ILAF) and revised 2011 (RLAF) under which repo and reverse repo became RBI's primary policy rates for managing liquidity.
- **Monetary Policy Framework Agreement (MPFA)** ⭐: 2016 GOI-RBI agreement formalising inflation targeting; RBI must report reasons and remedies if it misses the target.
- **Sukhamoy Chakravarty Committee (1985)**: recommended adoption of monetary targeting framework in India.
- **Narasimham Committee (Second, 1999)**: recommended introduction of ILAF.
- **Urjit Patel Committee (2014)**: recommended fine-tuning of RLAF.

### ⚠️ Common Mistakes
- ❌ Thinking RBI can subscribe directly to government debt → ✅ Banned since April 2006.
- ❌ Confusing RLAF (2011) with ILAF (1999) → ✅ RLAF made repo the *single* policy rate; ILAF lacked a ceiling.

**Quick Recall:**
- **1985**: Sukhamoy Chakravarty Committee → monetary targeting.
- **1998**: Multiple indicator approach.
- **April 1999**: ILAF (Narasimham II).
- **April 2006**: RBI barred from primary public-debt subscription.
- **May 2011**: RLAF — repo as sole varying rate.
- **Sep 2014**: Urjit Patel Committee fine-tunes RLAF.
- **May 2016**: MPFA signed; **inflation target = 4% (band 2–6%)**.
- **Feb 2019**: accommodative stance.
- **Aug 2019**: repo-rate-to-bank-lending-rate linkage formalised.
- Builds on: Goals of Monetary Policy (Chunk 002).
- Continues into: Transmission Mechanism (next section).

### Transmission Mechanism of Monetary Policy 🔴

**Master Table: Channels and Causation Chains ⭐**
| Channel | Causation chain |
|---------|-----------------|
| **Interest Rate (Nominal)** | Money ↑ → Interest Rate ↓ → Investment ↑ → Aggregate Demand ↑ |
| **Interest Rate (Real)** | Money ↑ → Expected Price ↑ → Expected Inflation ↑ → Real Interest Rate ↓ → Investment ↑ → AD ↑ |
| **Exchange Rate (Open Economy)** | Money ↑ → Interest Rate ↓ → Exchange Rate ↑ (Depreciates) → Exports ↑ → Net Exports ↑ → AD ↑ |
| **Bank Lending (Credit)** | Money ↑ → Deposits ↑ → Bank Loans ↑ → Investment ↑ → AD ↑ |
| **Balance Sheet (Credit)** | Money ↑ → Stock Prices (Net Worth) ↑ → Adverse Selection ↓ → Moral Hazard ↓ → Lending ↑ → Investment ↑ → AD ↑ |
| **Cash Flow (Credit)** | Money ↑ → Interest Rate ↓ → Cash Flow ↑ → Adverse Selection ↓ → Moral Hazard ↓ → Lending ↑ → Investment ↑ → AD ↑ |
| **Unanticipated Price Level (Credit)** | Money ↑ → Unanticipated Stock Prices ↑ → Adverse Selection ↓ → Moral Hazard ↓ → Lending ↑ → Investment ↑ → AD ↑ |
| **Liquidity Effects (Credit)** | Money ↑ → Stock Prices ↑ → Value of Financial Assets ↑ → Likelihood of Financial Distress ↓ → Consumer Durables/Housing Spending ↑ → AD ↑ |
| **Wealth Effect (Other)** | Money ↑ → Stock Prices ↑ → Wealth ↑ → Consumption ↑ → AD ↑ |
| **Tobin's q (Other)** | Money ↑ → Stock Prices ↑ → Tobin's q ↑ → Investment ↑ → AD ↑ |
| **Expectations (Other)** | Money ↑ → Expected Inflation ↑ → Consumption/Investment ↑ → AD ↑ |

**Channel-by-channel detail**
- **Nominal variant**: ↑M → ↓nominal i → ↑investment → ↑AD.
- **Real variant**: ↑M → ↑expected price → ↑expected inflation → ↓real i → ↑investment + ↑production incentive → ↑AD.
- **India weakness**: under-developed bond market, less banking competition, large informal credit sector → transmission via this channel is *weak* in developing economies. Long-term deposit base means short-term funding costs do not fall quickly.
- **Rational expectations link**: average of short-term rates = long-term rate, so transmission from short to long rates is essential.
- ↑M → ↓i → outflow of funds (investors prefer abroad) → ↓ supply of foreign currency → **depreciation** of domestic currency → ↑ net exports → ↑AD.
- **India**: importance has *risen* since the 1990s reforms opened the economy.
- **Bank Lending**: ↑M → ↑deposits → ↑bank lending → ↑investment → ↑AD. Effective in countries (like India) with under-developed financial markets where borrowers depend on banks.
  - Caveat: banks may be reluctant to lend in depressed conditions despite rising reserves; borrowers must be bank-dependent.
- **Balance Sheet**: ↑M → ↑stock prices → reduces asymmetric-information drawbacks → boosts confidence of lenders/borrowers → ↑lending → ↑investment → ↑AD.
- **Cash Flow**: ↑M → ↓i → ↑cash flow → reduces asymmetric-information drawbacks → ↑investment → ↑AD.
- **Unanticipated Price Level**: ↑M → unexpected stock-price rise → reduces asymmetric-information drawbacks → ↑lending → ↑investment → ↑AD.
- **Liquidity Effects**: ↑M → ↑stock prices and other financial-asset values → ↓ risk of financial distress → ↑ consumer durables/housing spending → ↑AD.
- **Wealth Effect**: ↑M → ↑stock prices → ↑wealth → ↑consumption → ↑AD.
- **Tobin's q**: 'q' = ratio of *market value of firm's existing shares* to *replacement cost of firm's physical assets*. ↑M → ↑stock prices → ↑q → ↑investment → ↑AD.
- **Expectations**: ↑M → ↑expected inflation → ↑present consumption + investment → ↑AD.

**Properties of Transmission**
1. List of affected variables is hard to pin down completely.
2. Impact is **non-uniform** — some variables strongly affected, others negligibly.
3. Effects appear with **lags** — some immediate, some delayed.
4. **Developed countries**: dominant channel = traditional **interest rate channel**.
5. **Developing countries**: **exchange rate** and **bank lending** channels play a significant role.
- **Transmission Mechanism**: the process or set of channels through which monetary policy affects economic variables.
- **Tobin's q**: ratio of the market value of a firm's existing shares (share capital) to the replacement cost of the firm's physical assets.
- **Asymmetric information**: lender/borrower information mismatch (basis of adverse selection and moral hazard problems).

### ⚠️ Common Mistakes
- ❌ Treating all transmission channels as equally important → ✅ Importance varies by economy and context.
- ❌ Assuming transmission is instantaneous → ✅ Lags vary (immediate vs delayed).
- ❌ Forgetting that ↑M ultimately raises AD (not output one-to-one) → ✅ Every channel ends in **↑AD**.

**Quick Recall:**
- **All channels end in ↑ Aggregate Demand.**
- Developed economies: **Interest Rate channel dominates**.
- Developing economies (incl. India): **Exchange Rate + Bank Lending channels** matter most.
- Tobin's q = market value of shares / replacement cost of physical assets.
- References: **Mishkin (1995), Taylor (1995), Boivin et al. (2010)**.
- Builds on: Money Supply effects on interest rate (Chunk 002, Fig 15.1).
- Builds on: Goals of monetary policy (Chunk 002).
- Is prerequisite for: Theory of monetary policy (Unit 17, Chunk 004) — uses IS curve, Phillips curve, AD curve which are all transmission outcomes.
1. Why do banks sometimes fail to transmit rate cuts (e.g. India 2019 led to August linkage decision)?
2. Why might a central bank prefer the interest-rate channel over direct money-supply targeting?
| Author / school | Rule |
|-----------------|------|
| **Friedman** | Constant rate of growth of money supply over time |
| **Robert Barro** | Commitment to zero/low inflation policy |
| **New-Keynesians** | Equations linking the central bank's policy rate to deviations from inflation and output targets |
| Theme | Key claim |
|-------|-----------|
| **Rules vs discretion** | Rules superior; but suffer from **dynamic inconsistency** |
| **Consensus view** | Monetary policy fixes inflation; cannot influence output (fixed at natural level) |
| **Criticism (path dependence)** | Natural output is endogenous; high AD raises both actual and natural output |

**Quick Recall:**
- Discretion has 3 lags: **identification, decision, implementation**.
- Rules: Friedman = constant money growth; Barro = zero inflation; new-Keynesian = policy-rate equations.
- Consensus view = money is *neutral* (Friedman idea revived); critics counter with path dependence.

**Quick Recall:**
- **Friedman**: no long-run trade-off + constant money-growth rule.
- Mainstream: keeps **rules > discretion** but uses inflation targeting, not money growth.

### Loss Function of the Central Bank 🔴

**The Loss Function**
| Symbol | Meaning |
|--------|---------|
| $x$ | Actual inflation rate |
| $y$ | Actual output |
| $y''$ | Output **target** of the central bank |
| $y'$ | Natural output level (full-employment output) |

**The Phillips Curve**
- $x^e$ = expected inflation.
- $e$ > 0 (slope parameter).
- Actual inflation exceeds expected inflation when actual output exceeds natural output.

**The Optimisation Problem**
- Central bank minimises L subject to the Phillips Curve.
- Achieved by varying money supply or interest rate.
- Analogy: like a consumer's utility maximisation. Just as a consumer reaches the highest indifference curve given a budget constraint, the central bank reaches the **lowest loss function** given the Phillips Curve.

**Geometric Interpretation (Fig. 17.1)**
- Loss-function contours = **concentric circles centred at B (the "bliss point")**.
  - Bliss point B: zero inflation **and** output at target $y''$.
  - Larger circle = greater welfare cost.
- On the vertical axis: output is at natural level → actual = expected inflation.
- Phillips Curve is upward-sloping (output rises with inflation).

**First-Order Condition at Optimum**
- **Loss function (of central bank)**: $L = x^2 + (y - y'')^2$ — welfare cost rising with inflation and with deviation of output from target.
- **Natural output ($y'$)**: output produced when labour force is fully employed.
- **Output target ($y''$)**: output level the central bank aims for; assumed > $y'$.
- **Bliss point (B)**: combination of zero inflation and output at $y''$ — minimum possible loss.

### ⚠️ Common Mistakes
- ❌ Treating $y''$ as equal to $y'$ → ✅ Model assumes $y'' > y'$ — that gap is the source of inflationary bias.
- ❌ Forgetting that the optimisation is *constrained* by the Phillips Curve → ✅ The central bank cannot arbitrarily pick (x, y).

**Quick Recall:**
- Loss function: $L = x^2 + (y - y'')^2$.
- Phillips Curve: $x = x^e + e(y - y')$.
- Optimum condition: $ex = y'' - y$.
- **Bliss point** = (0 inflation, $y''$). Loss-contours = concentric circles around B.
---

### Rules vs Discretion (Discretionary Outcome) 🔴

**Endogenising Expectations (Rational Expectations)**

**Discretionary Outcome — Key Features**
- Inflation rate is **endogenous** under discretion.
- Higher output target ($y''$) → higher inflation.
- Output is **NOT** stepped above its natural level.
- Reason: output rises only via *inflation surprise*; with rational expectations, no surprise possible.
- The discretionary outcome is point **A** in Fig. 17.1, where:
  1. Slope of loss function = slope of Phillips Curve.
  2. Actual inflation = expected inflation.

**Quick Recall:**
- Discretionary inflation: $x = (y'' - y')/e$.
- Output stays at natural level; only inflation rises.
- Rational expectations + minimisation → discretion produces **inflation bias**.

### Rules-Based Solution and Dynamic Inconsistency 🔴

**The Zero Inflation Rule (Rules Solution)**

**Comparison: Rule vs Discretion**
| Aspect | Discretion | Rule (zero-inflation) |
|--------|-----------|----------------------|
| Inflation | $(y'' - y')/e > 0$ | 0 |
| Output | Natural level $y'$ | Natural level $y'$ |
| Welfare cost | Higher | Lower |
| Position in Fig. 17.1 | Point A | Point O (origin) |

**Cheating Solution**

**Dynamic Inconsistency — The Core Insight**
- Rules superior to discretion.
- BUT once the rule is announced, the central bank has *incentive to violate it*.
- If it cheats, public learns the bank applies discretion → bank is forced back to the discretionary outcome (point A).
- **Final state after cheating**: inflation with no gain in output. Worst of both worlds.
- Therefore: such a shift in policy must be avoided.

**Solution: Delegation to a Conservative Central Banker**
1. Banker's loss function must place a higher weight on inflation than the government's.
2. **Banker must be independent of government control**.
3. If government is equally inflation-averse, nothing is gained.
- **Dynamic Inconsistency**: a policy is dynamically inconsistent if, having announced a rule, the central bank subsequently finds it optimal to violate the rule.
- **Cheating outcome**: violating an announced rule to exploit anchored expectations.
- **Delegation to a conservative central banker**: assigning monetary policy to an independent agent who places more weight on inflation control than the government does (Rogoff).

### ⚠️ Common Mistakes
- ❌ Thinking dynamic inconsistency means the rule is bad → ✅ The rule is *optimal*; the bank's incentive to deviate is the problem.
- ❌ Believing delegation works regardless of independence → ✅ Without independence, government's preferences seep through and gains are lost.
- ❌ Confusing the cheating outcome (C) with the long-run equilibrium → ✅ Once trust is lost, economy lands at A (discretionary outcome).
- Public's belief in the rule is fragile: a single break can reset expectations to discretion.
- Welfare ranking: **Rule (O) > Cheating (C) > Discretion (A)**.

**Quick Recall:**
- Rules-based: $x_r = x^e = 0$ → point O.
- Cheating: $x_c = e(y'' - y')/(1 + e^2) > 0$ → point C.
- Discretion: $x = (y'' - y')/e$ → point A.
- **Welfare**: O (best) > C > A (worst).
- Solution to dynamic inconsistency: **delegate to independent conservative banker** (Rogoff).
- With $\alpha > 1$ in loss function, inflation under delegation = $(y'' - y')/(e\alpha)$ — strictly lower.
- Builds on: Money Neutrality / Policy Ineffectiveness (Chunk 002).
- Builds on: Friedman's prescriptions (Chunk 004).
1. Is the RBI fully "independent" enough for the Rogoff prescription to bite? (Open question linking to MPFA — Chunk 003.)
2. What happens when the public's expectations adjust slowly (adaptive rather than rational)?

### Consensus View of Monetary Policy 🔴

**Old vs New Consensus**
| | Old textbook view | New consensus |
|---|---|---|
| **Main instrument** | Money supply | **Interest rate** |
| **Endogenous variable** | Interest rate | Money supply |
| **Mechanism** | Money demand × supply → interest rate | Central bank fixes policy rate; money supply adjusts |

**Taylor's Rule ⭐**
|--------|---------|
| $r$ | Real rate of interest (set by central bank) |
| $r'$ | Neutral / natural rate of interest |
| $x'$ | Inflation target |
| $y'$ | Natural output |
| $a, b$ | Both positive |
- Rate is positively related to **inflation gap** ($x - x'$) and **output gap** ($y - y'$).
- When both gaps are zero, $r = r'$.
- **You can verify this in RBI Monetary Policy Committee decisions.**

**IS Curve**
- Output gap responds **negatively** to real interest rate.
- $c$ captures other factors: fiscal policy and external demand.
- $c, d > 0$.
- **Neutral rate of interest**: rate at which output gap = 0, i.e. $r = c/d$.

**Accelerationist Phillips Curve**
- $\Delta$ is the difference operator (change between two periods).
- Inflation **accelerates** when output is above natural level (demand-pull).
- $e > 0$.
- **Origin**: equation (17.13) is the **adaptive expectations** version of equation (17.2) — i.e., public expects last year's inflation rate.

**The AD Curve (Aggregate Demand Schedule)**
- AD slopes downward (negative coefficient on x).
- Equilibrium: at the point on AD where output and inflation hit their respective targets.

**Equilibrium Condition**

**Off-Equilibrium Dynamics (Fig. 17.2, AD line)**
- **Left of $(y', x')$** (point B): $y < y'$ → inflation falling → bank cuts $r$ → AD expands → economy moves south-east toward $(y', x')$. Note: at B, *actual* $r >$ neutral $r$.
- **Right of $(y', x')$**: $y > y'$ → inflation rising → bank raises $r$ → economy moves north-west toward $(y', x')$. Actual $r <$ neutral $r$.
- **Taylor's Rule** ⭐: $r = r' + a(x - x') + b(y - y')$ — the policy rule linking the central bank's interest rate to inflation and output gaps.
- **Neutral rate of interest** ⭐: the rate at which the output gap is zero; $r' = c/d$ from the IS curve.
- **Accelerationist Phillips Curve**: $\Delta x = e(y - y')$ — inflation *accelerates* (rather than just exceeds expectations) when output is above natural level. Adaptive-expectations version of the original PC.
- **Aggregate Demand (AD) curve** (consensus model): the locus of $(y, x)$ combinations consistent with the IS curve and the Taylor-rule reaction function (eq. 17.14).
- **Nominal anchor**: monetary policy's role of providing a credible inflation target around which expectations form.

### ⚠️ Common Mistakes
- ❌ Treating the central bank as a money-supply-setter → ✅ In the consensus, it sets the **interest rate**.
- ❌ Confusing $r'$ (parameter chosen by bank) with $c/d$ (neutral rate from IS) → ✅ At equilibrium they must equal; if not, $x \ne x'$.
- ❌ Confusing the Phillips Curve in (17.2) with (17.13) → ✅ (17.13) is the *adaptive-expectations / accelerationist* version.
- The bank may not know the true IS-curve parameters → may misset $r'$ → economy lands on $AD'$ rather than AD.
- Under accelerationist PC, even small persistent output gaps drive ongoing inflation acceleration/deceleration.

**Quick Recall:**
- **Taylor rule**: $r = r' + a(x - x') + b(y - y')$.
- **IS curve**: $y - y' = c - dr$.
- **Accelerationist PC**: $\Delta x = e(y - y')$.
- **Neutral rate**: $r' = c/d$ (output gap zero).
- At equilibrium: $y = y'$, $x = x'$, $r = r' = c/d$.
- Modern view: interest rate is exogenous, money supply is endogenous.
- Builds on: Loss Function and Phillips Curve (Chunk 004).
- Builds on: Transmission Mechanism — Interest Rate Channel (Chunk 003).
- Continues into: Policy experiments — higher inflation target and expansionary fiscal policy (Chunk 005).
1. How can a central bank reliably estimate the neutral rate of interest in a developing economy?
2. Under accelerationist PC, why is even a temporary positive output gap so dangerous?

### Impact of a Higher Inflation Target 🔴

**What Stays Constant, What Changes**
| Variable | Change |
|----------|--------|
| Inflation target | $x' \to x''$ (higher) |
| Long-run output | $y'$ (unchanged) |
| Long-run inflation | Higher (= new target) |
| Neutral rate of interest | Unchanged |
| Long-run interest rate | Unchanged ($r' = c/d$) |
| Short-run interest rate | Temporarily lower |
| Short-run output | Temporarily higher |

**Quick Recall:**
- Higher inflation target → AD shifts up → short-run output gain.
- Long run: output back at $y'$; only inflation is permanently higher.
- Neutral rate $r' = c/d$ is unchanged.
- Builds on: Taylor's Rule, IS curve, AD curve (Chunk 004).
- Builds on: Friedman's no-long-run-trade-off claim (Chunk 004).

### Impact of Expansionary Fiscal Policy 🔴

**Net Result**
| Variable | Long-run change |
|----------|-----------------|
| Output | Unchanged ($y'$) |
| Inflation | Unchanged ($x'$) |
| Neutral interest rate | **Higher** (because c is higher) |
| Private expenditure | **Crowded out** by higher rate |

**Crowding Out — Two Versions Compared**
| | Standard analysis | New consensus |
|---|------------------|---------------|
| **Mechanism** | Higher public investment → excess of total investment demand over savings → interest rate rises to clear loanable-funds market | Central bank fixes interest rate; expansionary fiscal policy raises inflation → bank pushes up rate to keep inflation at target |
| **Common conclusion** | Private spending crowded out by higher rate | Same |
- **Crowding out (consensus version)**: an expansionary fiscal policy displaces private expenditure because the central bank, forced to maintain the inflation target, raises the interest rate.

### ⚠️ Common Mistakes
- ❌ Thinking expansionary fiscal policy boosts output → ✅ Long run, output and inflation unchanged in this model.
- ❌ Confusing the consensus crowding-out mechanism with the loanable-funds version → ✅ In the consensus, the central bank *chooses* to raise the rate to defend the target; in the standard view the market clears via savings-investment.
- **The Keynesian view (from Unit 2) sharply contradicts this**: in Keynes' framework fiscal policy boosts output via the multiplier.
- This model assumes the central bank is committed to inflation targeting and reacts mechanically to defend $x'$.

**Quick Recall:**
- Fiscal expansion: **no long-run effect on output or inflation**.
- Only effect: **higher neutral interest rate** → **crowding out** of private expenditure.
- Sharply contradicts Keynesian view from Unit 2.
- Builds on: Taylor's Rule and AD curve (Chunk 004).
- Contrasts with: Keynesian fiscal multiplier (referenced as Unit 2 of course).

**Quick Recall:**
- Consensus = **monetary policy is neutral** in the long run.
- Activist fiscal policy has **no space** in the framework.
- Stabilisation around natural level, *not* improvement of natural level.

### Path Dependence (Hysteresis) — The Critique 🔴

**Three Reasons Natural Output May Depend on Demand**
1. **Learning-by-doing**: high actual output improves labour productivity / reduces per-unit labour cost.
2. **Capital formation**: higher output induces more investment → higher capital stock → improved labour productivity → lower labour costs.
3. **Labour-force expansion**: higher AD encourages potential workers to enter the labour force, augmenting labour supply.

**Extending the Model**

**Path Dependence Illustrated (Fig. 17.5)**
- Initial equilibrium: B (on $y = y'$ line).
- Central bank raises inflation target → $\Delta x' > 0$ → $\Delta y > 0$.
- Economy temporarily shifts B → **D**.
- Higher inflation target → lower interest rate → AD stimulus → output rises.
- At D, $y > y'$. Although $\Delta y$ may turn negative (if the bracketed term in 17.19 is negative), the economy will *not* return to B because $y > y'$ also makes $y'$ rise (by 17.17).
- Economy moves north-west to a **new equilibrium E**, with both $y$ and $y'$ permanently higher.

**Caveat — Speed of Response**

**Empirical Evidence**
- **Most studies show** unemployment can stay below natural for extended periods with only **mild** inflation increases.
- The **short-run Phillips Curve is concave** — there *is* a trade-off between unemployment and inflation in the short run.
- In the long run, Phillips Curve is **vertical** at the natural rate of unemployment (consensus position).
- **Conclusion**: unemployment can be driven below its natural rate at *low cost* in inflation terms.

**Implications — How Hysteresis Overturns the Consensus**
| | Consensus / Monetarist / New-Classical | With path dependence |
|---|---|---|
| **Natural output** | Exogenously given | Endogenous to AD |
| **Activist policy** | Cannot raise output | Can permanently raise both $y$ and $y'$ |
| **Equilibrium** | Unique | Path-dependent — depends on starting point |
| **Long-run Phillips Curve** | Vertical | Effectively concave / not vertical |
- **Path dependence (hysteresis)** ⭐: macroeconomic outcome where the long-run equilibrium depends on the starting point and the path taken — typically because natural output (or natural unemployment) depends on actual output (or unemployment).
- **Knife-edge property of natural unemployment** (Friedman): the claim that any deviation from natural unemployment triggers rapidly accelerating or decelerating inflation.
- **Learning-by-doing**: productivity improvement that arises from cumulative experience of producing.

### ⚠️ Common Mistakes
- ❌ Treating natural output as fixed by technology and labour endowments alone → ✅ It can depend on AD via learning, investment, and labour-force expansion.
- ❌ Believing the long-run Phillips Curve is *always* vertical → ✅ Empirically, the short-run PC is concave, and persistent low-unemployment periods don't always trigger runaway inflation.
- ❌ Assuming policy can only stabilise around an exogenous target → ✅ Under hysteresis, policy can shift the target itself.
- High values of $e$ (Phillips-curve sensitivity) shorten how long output can deviate from natural — restoring the consensus result.
- Hysteresis effects take time to materialise; rapid inflation may force the bank to act before they appear.

**Quick Recall:**
- **Three sources of hysteresis**: learning-by-doing, capital formation, labour-force expansion.
- $\Delta y' = f(y - y')$ — natural output rises when actual output exceeds it.
- Under hysteresis, **no unique equilibrium** — depends on initial point (Fig. 17.5: B → D → E).
- **Short-run PC is concave**, not vertical.
- **Lavoie**, among others, championed this critique.
- Builds on: Consensus model and AD curve (Chunk 004).
- Contradicts: Friedman's knife-edge view (Chunk 004).
- Contradicts: Higher inflation target conclusion (Chunk 005, prior section).
1. How can policy makers tell whether the economy is in a "knife-edge" or "hysteresis" regime?
2. Empirically, are the productivity / labour-force responses to demand strong enough to validate hysteresis as a policy guide?

**Quick Recall:**
- **Three big debates** in monetary theory: rules vs discretion, neutrality, exogeneity of natural output.
- **Mainstream prefers rules** but disagrees on what "rule" means.
- **Hysteresis critique**: capacity depends on what you actually produce.
