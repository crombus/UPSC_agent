# Economy Flashcards — Formulas and Important Topics

> Part A: every formula and identity (one card each, with a worked numeric example). Part B: high-yield topic cards (definition, breakdown, committees/schemes/data, trap, Mains hook, memory hook).
> **Verification status:** built from the repository Economy `basic/` owners plus standard economics; web verification was mostly not possible. Unverified details are marked ⚠️ inside the card. Time-varying numbers (rates, ratios, thresholds) carry an as-of date from the owner or are left out. Mnemonics are original.

---

## A. FORMULAS — Macroeconomics, Money and Banking

> Scope: formula and identity cards for Economy owners 01–08 (basic and advanced): national income, growth and development indices, inflation and price indices, money and banking, interest and bond arithmetic, equity and fund ratios, Basel capital and liquidity ratios, and asset-quality and bank-performance ratios.
> Currency: as of 2026-10-30. No current repo rate, CRR, SLR, GDP size, inflation print or MSF cap is quoted as fact. Where an owner gives a dated figure, the as-of date is kept. Illustrative numbers are labelled as illustrative.
> ⚠️ marks an item that is standard economics or from memory and must be checked against the official source before use (UNDP HDR technical notes, NITI Aayog MPI reports, RBI Master Directions and liquidity-framework notifications, RBI Handbook of Statistics for M1–M4).

### GROUP — National income accounts

### Flashcard F-001 — GDP at market prices (expenditure method)
**Front:** How is GDP computed by the expenditure method, and what does each term stand for?
**Formula:** GDP(mp) = C + I + G + (X − M), at market prices, for a period, for the domestic territory. C = private final consumption (PFCE); I = gross fixed capital formation plus change in stocks (and valuables); G = government final consumption (GFCE, not government capital spending); X and M = exports and imports of goods and services. Units: ₹ lakh crore (or ₹ crore), current or constant prices.
**Worked example:** Illustrative, ₹ lakh crore: C = 60, I = 25, G = 15, X = 12, M = 14. GDP = 60 + 25 + 15 + (12 − 14) = 98.
**Learn:**
- Intermediate purchases are excluded; imports are subtracted because C, I and G can contain foreign-made goods (owner 01).
- Government capital expenditure creates assets and enters I; GFCE measures current government services (owner 01, Section 4 trap).
- PFCE is the largest demand component; the Survey 2025-26 FY26 first advance estimate put PFCE at 61.5% of GDP (✅ owner 01 §9 and basic table, citing the Survey 2025-26 FY26 first advance estimate; Survey PDF not fetchable this pass).
- Series: MoSPI released a new GDP series with 2022-23 base on 27 February 2026, replacing 2011-12; a comparable back-series was pending at the owner's cutoff (owner 01 §9).
**Trap:** Resale of an existing asset and transfer payments do not add to GDP. C + I + G + (X − M) is an accounting identity, not a behavioural causal claim.
**Back:** *"Buy at home, add what the world buys from us, take out what we buy from the world."*

### Flashcard F-002 — GVA at basic prices (production method)
**Front:** How is gross value added measured for a producer or a sector?
**Formula:** GVA(bp) = Gross value of output − Intermediate consumption. Sum over sectors gives GVA at basic prices for the economy.
**Worked example:** Owner 01 chain (₹ units): farmer sells wheat 20, input 0 → VA 20; miller sells flour 35, input 20 → VA 15; baker sells bread 50, input 35 → VA 15. Total VA = 50 = final bread value, not the sum of all sales (105).
**Learn:**
- The production approach avoids double counting by adding each stage's own value added (owner 01 §5).
- GVA is the sector-level measure; GDP at market prices is GVA plus net product taxes (see F-003).
- Services and construction output are estimated largely through enterprise and administrative data; informal sector is estimated, not observed (owner 01 §6A).
**Trap:** Adding all sales in a supply chain counts intermediate goods more than once. GVA is not GDP; the difference is net product taxes.
**Back:** *"Value added is what each stage adds — never the whole sale, only the new work."*

### Flashcard F-003 — GDP at market prices from GVA (net product taxes bridge)
**Front:** How do you move from GVA at basic prices to GDP at market prices?
**Formula:** GDP(mp) = GVA(bp) + Product taxes − Product subsidies = GVA(bp) + Net product taxes. Equivalently GVA(bp) = GDP(mp) − Net product taxes.
**Worked example:** Illustrative: GVA(bp) = 180, product taxes = 22, product subsidies = 6. Net product taxes = 16. GDP(mp) = 196.
**Learn:**
- Product taxes (for example GST and customs duty on goods and services) attach to units of output; production taxes and subsidies (for example stamp duty, land-based levies) are already inside GVA(bp) (owner 01 §3 and advanced §3).
- Owner 01 warns that GDP and GVA growth can differ when net product taxes change sharply, so a tax cut can narrow GDP growth relative to GVA even with unchanged production.
**Trap:** "Production taxes" and "product taxes" are different. Only product taxes and product subsidies bridge GVA and GDP at market prices.
**Back:** *"Add the product tax, subtract the product subsidy — then value added becomes the market-price GDP."*

### Flashcard F-004 — GDP at factor cost (net indirect taxes)
**Front:** How is GDP at factor cost obtained from GDP at market prices?
**Formula:** GDP(fc) = GDP(mp) − NIT, where NIT (net indirect taxes) = (Product taxes + other taxes on production) − (Product subsidies + other subsidies on production).
**Worked example:** Illustrative: GDP(mp) = 196 (from F-003). Net product taxes 16, plus other production taxes 4 minus other production subsidies 1 gives NIT = 19. GDP(fc) = 196 − 19 = 177.
**Learn:**
- Factor cost values output at the incomes paid to factors of production, so it removes the government's tax and subsidy wedge.
- National income is NNP at factor cost (F-009). The official tables that show GDP at factor cost follow MoSPI's series in use, which changed with the 2022-23 base (⚠️ check the current release).
- When taxes exceed subsidies, market-price aggregates exceed factor-cost aggregates; with net subsidies the order reverses.
**Trap:** Do not compare a market-price aggregate with a factor-cost aggregate from another table; they differ by NIT.
**Back:** *"Factor cost strips out the tax wedge and leaves what the factors actually earn."*

### Flashcard F-005 — Net domestic product (NDP)
**Front:** How is net domestic product derived from gross measures?
**Formula:** NDP(mp) = GDP(mp) − Depreciation (consumption of fixed capital, CFC). NDP(fc) = GDP(fc) − CFC.
**Worked example:** Illustrative: GDP(mp) = 196, CFC = 25. NDP(mp) = 171.
**Learn:**
- Gross measures include depreciation; net measures deduct it (owner 01 §7).
- Depreciation is an accounting estimate of fixed-capital consumption, not a cash payment made during the year (owner 01 advanced §9).
- A rise in gross output can coexist with a fall in net output if depreciation rises faster.
**Trap:** Depreciation is not a cash outflow. Gross measures are not "wrong"; they answer a different question from net measures.
**Back:** *"Net means the wear and tear is written off — gross is the bill before the wear."*

### Flashcard F-006 — Net factor income from abroad (NFIA)
**Front:** How is net factor income from abroad calculated, and what does it exclude?
**Formula:** NFIA = Factor income received from abroad − Factor income paid abroad (compensation of employees, property and entrepreneurial income).
**Worked example:** Illustrative: received 9, paid 4 → NFIA = +5 (₹ thousand crore units, illustrative).
**Learn:**
- NFIA is the bridge from domestic to national aggregates (owner 01 §2 and advanced §2).
- Personal transfers such as remittances are recorded separately from factor income (owner 01 advanced §2). Do not treat every inward remittance as NFIA.
- The 1993 SNA revision renamed GNP as gross national income (GNI) (✅ corrected: was attributed to SNA 2008; Wikipedia 'Gross national income' says GNI is "formerly known as gross national product (GNP)" and that the 1993 revision renamed it). Check MoSPI terminology in the current series (⚠️).
**Trap:** NFIA equals all remittances (false, owner 01 advanced §9). A negative NFIA means GDP exceeds GNP.
**Back:** *"NFIA counts what residents earn abroad minus what foreigners earn here — transfers sent home are not factor income."*

### Flashcard F-007 — Gross national product (GNP) from GDP
**Front:** How is gross national product derived from GDP at market prices?
**Formula:** GNP(mp) = GDP(mp) + NFIA. Domestic concepts follow location of production; national concepts follow residence of income earners (owner 01 §1).
**Worked example:** Illustrative: GDP(mp) = 196. NFIA = +5 gives GNP = 201. NFIA = −5 gives GNP = 191.
**Learn:**
- GDP is territorial; GNP is resident-income based (owner 01 §7).
- GDP can exceed GNP when NFIA is negative (owner 01 §7).
- Current MoSPI practice uses GNI terminology (⚠️ verify in the 2022-23 series release).
**Trap:** GNP must always exceed GDP is false; the sign of NFIA decides (owner 01 §8).
**Back:** *"Add what our people earn abroad and subtract what foreigners earn here — GDP becomes GNP."*

### Flashcard F-008 — Net national product at market prices (NNP mp)
**Front:** How is net national product at market prices derived?
**Formula:** NNP(mp) = GNP(mp) − Depreciation = GDP(mp) + NFIA − CFC.
**Worked example:** Illustrative: GNP = 201, CFC = 25 → NNP(mp) = 176.
**Learn:**
- Owner 01 presents NNP as GNP minus depreciation.
- NNP(mp) is still at market prices; net indirect taxes are removed in F-009 to reach national income.
**Trap:** Do not compare NNP at market prices with national income, which is NNP at factor cost.
**Back:** *"Net national is residents' income after the wear and tear — still priced with taxes."*

### Flashcard F-009 — National income (NNP at factor cost)
**Front:** What is national income and how is it computed?
**Formula:** National income = NNP(fc) = NNP(mp) − NIT = GNP(mp) − CFC − NIT.
**Worked example:** Illustrative: NNP(mp) = 176, NIT = 19 → national income = 157.
**Learn:**
- National income is the official headline income measure in India; per capita income (F-013) is derived from it (owner 01 §2 uses the simpler NNP/income wording).
- Factor cost is the basis that matches what factors receive.
- ⚠️ Confirm the current MoSPI series, base year and vintage before quoting a figure. The base moved to 2022-23 in the 27 February 2026 release (✅ owner 01 §9 cites the MoSPI press note; the press-note PDF was not readable this pass, so the vintage check stays ⚠️).
**Trap:** National income is not GNP. NNP at market prices exceeds national income whenever net indirect taxes are positive.
**Back:** *"National income is what the factors really take home — net of wear and net of the tax wedge."*

### Flashcard F-010 — Income-method identity (three methods converge)
**Front:** How is national income computed by the income method, and why should the three methods agree?
**Formula:** National income = Compensation of employees + Operating surplus + Mixed income + NFIA. GDP(mp) = Compensation of employees + Operating surplus + Mixed income + CFC + NIT.
**Worked example:** Illustrative: compensation 90, operating surplus 40, mixed income 30 give domestic factor income (NDP at factor cost) = 160. Add NFIA = 5 gives national income = 165.
**Learn:**
- Production (value added), income and expenditure approaches should theoretically converge because one person's spending is another's income and corresponds to produced output (owner 01 §4).
- In practice the three use different data and timing, so a statistical discrepancy remains (advanced §1).
- The income method captures informal earnings poorly; it relies on estimates for mixed income.
**Trap:** Transfer payments such as pensions are not factor income for GDP. Adding them to the income method double counts.
**Back:** *"Pay to workers, profit to owners, mixed earnings to the self-employed — plus what crosses the border."*

### Flashcard F-011 — Personal income (PI)
**Front:** How is personal income derived from national income?
**Formula:** PI = National income − (Corporate income taxes + Undistributed corporate profits + Social-security contributions) + Transfer payments received by households.
**Worked example:** Illustrative: national income 157, corporate taxes 10, undistributed profits 8, social-security contributions 6, transfers received 12. PI = 157 − 24 + 12 = 145.
**Learn:**
- Personal income is what households actually receive before their own direct taxes (standard national-accounts identity; ⚠️ check MoSPI's exact definition in the current series).
- Transfers are excluded from GDP but included in personal income, which explains why GDP and household income diverge.
**Trap:** Personal income is not the same as personal disposable income (F-012).
**Back:** *"Personal income is what households receive: take out what firms keep and the state takes, add back the transfers."*

### Flashcard F-012 — Personal disposable income (PDI)
**Front:** How is personal disposable income derived?
**Formula:** PDI = Personal income − Direct personal taxes (personal income tax and other direct taxes on persons, plus non-tax payments).
**Worked example:** Illustrative: PI = 145, personal income tax = 18 → PDI = 127.
**Learn:**
- Disposable income is the base for household consumption and saving: Saving = PDI − Consumption.
- GST and other indirect taxes are already in consumer prices; they do not reduce disposable income by this identity.
**Trap:** Do not subtract GST from disposable income. Do not treat transfers as taxes.
**Back:** *"Disposable is what remains after tax on the person — the tax on purchases already sits in the price."*

### Flashcard F-013 — Per capita income
**Front:** How is per capita income calculated, and what is it used for?
**Formula:** Per capita income = National income (or per capita NNP at factor cost, the official measure) ÷ mid-year population. Units: ₹ per person per year. For growth, use real (constant-price) income per capita.
**Worked example:** Illustrative: national income ₹200 lakh crore = ₹2 × 10¹³; population 1.4 billion → per capita ≈ ₹14,286 per person.
**Learn:**
- Per capita income corrects for population size, not for distribution (owner 01 advanced §8).
- The population denominator must match the period; census-based projections change the figure.
- Per capita GDP is not a development measure: it hides distribution, unpaid work and ecological cost (owner 02 §2 and §7).
- ⚠️ Quote the official per capita figure only with its base year and vintage; no current figure is given here.
**Trap:** Nominal per capita income can rise purely because of inflation; compare real per capita income for welfare trends.
**Back:** *"Divide the national pie by the population — the average hides who got which slice."*

### Flashcard F-014 — Nominal GDP and real GDP
**Front:** How are nominal and real GDP defined and computed?
**Formula:** Nominal GDP(t) = Σ p(t) × q(t) (current prices). Real GDP(t) = Σ p(0) × q(t) (base-year prices). Real GDP is the constant-price volume measure.
**Worked example:** Base year 0: goods A (p = 10, q = 100), goods B (p = 20, q = 50). Nominal(0) = 2,000. Year t: A (p = 12, q = 110), B (p = 22, q = 60). Nominal(t) = 12 × 110 + 22 × 60 = 2,640. Real(t) = 10 × 110 + 20 × 60 = 2,300. Real growth = (2,300 − 2,000)/2,000 = 15%; nominal growth = (2,640 − 2,000)/2,000 = 32%.
**Learn:**
- Real GDP separates volume change from price change (owner 01 §5).
- Nominal GDP is the right basis for fiscal and debt ratios; real GDP is the right basis for volume growth (owner 01 §5 and advanced §6).
- Owner 01 notes that nominal GDP can rise without real welfare gains when prices rise.
- A new base year changes both levels and growth rates (owner 01 advanced §6).
**Trap:** Higher nominal GDP does not mean more output (owner 01 §8). A level is not a growth rate.
**Back:** *"Nominal prices the year at today's prices; real prices it at base-year prices — only real shows volume."*

### Flashcard F-015 — GDP deflator (implicit price deflator)
**Front:** How is the GDP deflator computed, and what does it cover?
**Formula:** GDP deflator = (Nominal GDP ÷ Real GDP) × 100. Price change over the base is (deflator − 100)%.
**Worked example:** From F-014: deflator = 2,640 ÷ 2,300 × 100 = 114.78; prices are about 14.8% above the base.
**Learn:**
- The deflator covers domestically produced final goods and services; imports are excluded as foreign output (owner 01 advanced §7).
- It is broader than CPI in output coverage but is not a cost-of-living index (owner 01 advanced §7).
- It uses current-year quantities (a Paasche-type index; see F-031).
- Derived from national accounts, so revised with data updates and less suited to monthly management (owner 03 §6A).
**Trap:** The GDP deflator includes imported production is false (owner 01 advanced §9).
**Back:** *"Nominal over real, times a hundred — domestic output only, never the import bill."*

### Flashcard F-016 — Growth rate (year-on-year)
**Front:** How is the growth rate of GDP or any series calculated?
**Formula:** g(t) = [X(t) − X(t−1)] ÷ X(t−1) × 100. Apply to real GDP for real growth; to nominal GDP for nominal growth.
**Worked example:** Real GDP 100 → 107 gives g = 7%. Real GDP growth FY26 estimates in the Survey 2025-26 were 7.4% (✅ owner 01 §9 and basic table, citing the Survey 2025-26 FY26 first advance estimate; Survey PDF not fetchable this pass).
**Learn:**
- Always state the series, estimate vintage (first advance, second revised, provisional) and reference period (owner 01 §9).
- A growth rate and a level are different statements; compare levels with levels and rates with rates.
- Growth rates across a base-year break are invalid without an official back-series (owner 01 §9).
**Trap:** Nominal growth minus inflation is approximately real growth, but the approximation is not the same as the deflated series; use the official real series.
**Back:** *"Growth is this year minus last, over last — compare real with real, and never across a broken series."*

### Flashcard F-017 — Compound annual growth rate (CAGR)
**Front:** How is the compound annual growth rate over several years calculated?
**Formula:** CAGR = (V(end) ÷ V(start))^(1/n) − 1, with n = number of years; express as a percentage by multiplying by 100.
**Worked example:** A series rises from 100 to 180 in 5 years: CAGR = 1.8^(1/5) − 1 = 0.1247, i.e. about 12.5% a year.
**Learn:**
- CAGR is the constant rate that would carry the start value to the end value.
- It smooths year-to-year volatility but hides the path; report it alongside the annual series.
- The series must be on the same price and base basis at both ends.
**Trap:** The arithmetic average of annual growth rates is not the CAGR; the two differ when rates vary.
**Back:** *"CAGR is the one steady rate that links the start to the end — not the average of the yearly rates."*

### Flashcard F-018 — Base-year revision and linking (splicing)
**Front:** How should a series be linked across a base-year change, and when must splicing be avoided?
**Formula:** Linking factor LF = Old-series value ÷ New-series value in the overlap year s. Linked value(t) for years before s = Old value(t) × (New value(s) ÷ Old value(s)).
**Worked example:** Overlap year s: old = 100, new = 110, so the factor is 1.10. Old-series year t = 95 gives linked value 95 × 1.10 = 104.5 in new-base terms.
**Learn:**
- A base-year revision updates prices, weights, databases, classifications and coverage (owner 01 advanced §6).
- MoSPI's 2015 revision moved to 2011-12; the 27 February 2026 release moved to 2022-23 with revised sources and methods (owner 01 §9).
- Use only an official back-series or an official linking method; the owner notes the back-series was pending at its cutoff (owner 01 §9).
- Index base changes for CPI (2012=100 to 2024=100 from January 2026) and WPI (2011-12 to 2022-23 from May 2026) follow the same rule (owner 03 §8).
**Trap:** A base break is a measurement update, not a price shock; never splice levels or weights across a break without an official back-series.
**Back:** *"Link only at the overlap year, and only with the official back-series — never across a break by hand."*

### Flashcard F-019 — Incremental capital-output ratio (ICOR)
**Front:** How is the incremental capital-output ratio computed, and what does it diagnose?
**Formula:** ICOR = Investment rate ÷ Growth rate = (I ÷ Y) ÷ (ΔY ÷ Y), equivalently ΔK ÷ ΔY (capital added per unit of extra output).
**Worked example:** Illustrative: investment is 30% of GDP and growth is 6%. ICOR = 0.30 ÷ 0.06 = 5.0. Each extra percentage point of output needs about 5% of GDP invested.
**Learn:**
- A rising ICOR means lower investment efficiency: high saving or investment effort does not translate into growth (owner 01 advanced §6A and §4).
- ICOR is an aggregate diagnostic and does not identify the sector or institutional cause (owner 01 §6A).
- Owner 01 cites the 2018 Prelims concept of a high-saving economy with low output and capital-output ratio.
**Trap:** A high ICOR is not the same as a low saving rate; it reflects project execution, productivity and capacity use.
**Back:** *"More investment per unit of growth means a higher ICOR — efficiency, not effort, sets the ratio."*

### Flashcard F-020 — Output gap and potential output
**Front:** How is the output gap defined and what does its sign signal?
**Formula:** Output gap (%) = [(Y − Y*) ÷ Y*] × 100, where Y = actual real output and Y* = potential output (sustainable capacity from labour, capital and productivity).
**Worked example:** Y = 98, Y* = 100 → output gap = −2%. A negative gap signals weak demand.
**Learn:**
- Owner 01 uses the 2020 GS-III PYQ on potential GDP and India's output gap as the anchor (owner 01 §6A and §10).
- A negative gap supports cyclical demand repair; a capacity constraint calls for supply-side investment (owner 01 §6A).
- Potential output is estimated, not observed, and varies by method (owner 01 §6A).
**Trap:** Potential output is not the same as the output of the previous year; the gap is a comparison with estimated capacity.
**Back:** *"Gap is actual minus capacity, over capacity — below zero, demand is short; above zero, supply is straining."*

### GROUP — Growth, development and welfare indices

### Flashcard F-021 — Human Development Index (HDI, geometric mean)
**Front:** How is the HDI computed, and why does the geometric mean matter?
**Formula:** HDI = (I(health) × I(education) × I(income))^(1/3). Each dimension index I = (actual − minimum) ÷ (maximum − minimum). Education index = average of mean years of schooling (MYS) index and expected years of schooling (EYS) index. Income index = [ln(GNIpc) − ln(100)] ÷ [ln(75,000) − ln(100)], GNIpc in PPP dollars. Goalposts used here (life expectancy 20–85 years; EYS 0–18; MYS 0–15; GNIpc $100–$75,000 PPP), the education-index and income-index formulas, and the geometric mean are confirmed by Wikipedia 'Human Development Index' (✅ Wikipedia HDI, "new method", 2010 onward). The UNDP technical-note edition behind them is still unverified: the UNDP PDFs (2021-22, 2023-24, 2025) returned undecodable binaries (⚠️).
**Worked example:** Illustrative (not India's actual data): life expectancy 70 → (70 − 20) ÷ 65 = 0.769; EYS 12 → 12 ÷ 18 = 0.667; MYS 6.5 → 6.5 ÷ 15 = 0.433; education = (0.667 + 0.433) ÷ 2 = 0.550; GNIpc $6,000 → (ln 6,000 − ln 100) ÷ (ln 75,000 − ln 100) = 4.0943 ÷ 6.6201 = 0.6185 (✅ corrected: was 0.619 at three decimals, which rounds the same value to 0.618 at three places; 0.6185 is the four-decimal value). HDI = (0.7692 × 0.5500 × 0.6185)^(1/3) = (0.2617)^(1/3) ≈ 0.640.
**Learn:**
- HDI uses life expectancy, education and GNI per capita, so it is not income-only (owner 02 §6).
- The geometric mean penalises imbalance: a very low score in one dimension pulls the whole index down more than an arithmetic mean would (owner 02 §2).
- HDI is an average; it can rise while gender, caste, tribal or district deprivation persists (owner 02 §6A).
- Published by UNDP in its Human Development Reports (owner 02 §4).
**Trap:** HDI does not directly measure political freedom (owner 02 §7). HDI values across different goalpost vintages are not comparable without recalculation.
**Back:** *"Three legs, multiplied, cube-rooted — a weak leg drags the whole index down."*

### Flashcard F-022 — Inequality-adjusted HDI (IHDI)
**Front:** How is the IHDI derived from HDI, and what does it measure?
**Formula:** IHDI = [I(h)·(1 − A(h)) × I(e)·(1 − A(e)) × I(i)·(1 − A(i))]^(1/3), where A = inequality within each dimension (Atkinson measure, 0 ≤ A ≤ 1). Overall loss (%) = (1 − IHDI ÷ HDI) × 100. Structure confirmed: Wikipedia 'Inequality-adjusted HDI' describes IHDI as a geometric mean of inequality-adjusted dimensional indices that "discounts" each dimension by its inequality, drawing on the Atkinson family (✅ Wikipedia IHDI; the Wikipedia IHDI summary cites ε = 1). The explicit per-dimension inequality formula and the overall-loss definition are not on that page and remain ⚠️ (UNDP technical notes not decodable).
**Worked example:** Illustrative: HDI = 0.640 with the same inequality A = 0.10 in every dimension → IHDI = 0.640 × (1 − 0.10) = 0.576, a loss of 10%.
**Learn:**
- IHDI equals HDI when there is no inequality and falls below HDI as inequality rises (owner 02 §6).
- The 2025 GS-III PYQ asked for the difference between HDI and IHDI and why IHDI better reflects inclusive growth (owner 02 §9).
- IHDI measures distributional inequality within the three dimensions; it is not a poverty headcount and does not capture overlapping deprivations, which is MPI's role (owner 02 §8).
**Trap:** IHDI is not a different set of outcomes; it adjusts each HDI dimension for inequality (owner 02 §7).
**Back:** *"Discount each leg by its inequality, then take the cube root — IHDI shows what the average hides."*

### Flashcard F-023 — Gender Development Index (GDI)
**Front:** How is the Gender Development Index computed?
**Formula:** GDI = HDI(female) ÷ HDI(male). Each HDI is computed with the same goalposts, using female and male values, except that the income component is estimated earned income by sex (✅ corrected: was "the same formula" with GNI per capita; the UNDP GDI page names "command over economic resources" measured by estimated earned income). The ratio form is consistent with the Wikipedia GDI table: Kuwait female 0.802242 ÷ male 0.802827 = 0.99927, equal to the listed GDI (✅ Wikipedia GDI, numerical check; the page does not state the ratio in words). A value of 1 means parity; below 1 means female human development is lower than male. Countries are grouped in five groups by absolute deviation from parity (✅ Wikipedia GDI); the numeric group bands remain ⚠️ unverified.
**Worked example:** Illustrative: HDI(female) = 0.600, HDI(male) = 0.660 → GDI = 0.600 ÷ 0.660 = 0.909.
**Learn:**
- GDI tracks gender gaps in health (female and male life expectancy), education (expected years of schooling for children and mean years for adults by sex) and command over economic resources (estimated earned income by sex) (✅ UNDP GDI page, hdr.undp.org/content/gender-development-index-gdi).
- It is distinct from UNDP's Gender Inequality Index (GII), which uses reproductive health, empowerment and labour market dimensions (✅ Wikipedia 'Gender Development Index': GII has three dimensions, Reproductive Health, Empowerment and Labour Market Participation; it was proposed in the 2010 HDR).
**Trap:** GDI is a ratio of female to male HDI, not a poverty measure; do not confuse it with GII or with the MPI.
**Back:** *"Women's HDI over men's HDI — one is parity, less than one is the gap."*

### Flashcard F-024 — Multidimensional poverty: headcount ratio (H)
**Front:** How is the incidence (headcount ratio) of multidimensional poverty computed?
**Formula:** H = q ÷ n × 100, where n = total population (or households) and q = number of people identified as multidimensionally poor. A person is poor when the weighted deprivation score c ≥ k, with cut-off k = one-third (33.3%).
**Worked example:** Illustrative: n = 1,000 people, q = 300 poor → H = 30%.
**Learn:**
- H answers "how many are poor" (owner 02 §5A).
- The one-third cut-off is the same in the global and NITI national MPI (owner 02 §5A).
- H depends on the chosen cut-off and weights; changing either changes H (owner 02 §5A).
**Trap:** H is not the income-poverty headcount; a household above the income line can still be multidimensionally poor (owner 02 advanced §5).
**Back:** *"H counts heads: how many are poor out of everyone counted."*

### Flashcard F-025 — Intensity (A) and MPI = H × A
**Front:** How is the intensity of poverty computed, and how do H and A combine into the MPI?
**Formula:** A = (Σ c(i) over the poor) ÷ (q × d), the average weighted deprivation share among the poor, where d = number of indicators and c(i) = weighted deprivation score of poor person i. MPI = H × A.
**Worked example:** Illustrative: H = 0.30, A = 0.45 → MPI = 0.30 × 0.45 = 0.135, i.e. 13.5%.
**Learn:**
- A is averaged only across the poor, so it measures how deep deprivation runs among those already poor (owner 02 §5A).
- H and A can move in different directions: fewer poor (lower H) but deeper deprivation among those left (higher A) (owner 02 §5A).
- This decomposition is the answer to the 2020 GS-II PYQ on incidence and intensity of poverty against income-based measurement (owner 02 §9).
**Trap:** MPI is not a monetary poverty line and cannot price transfers. MPI is not H alone.
**Back:** *"Multiply how many are poor by how deep their poverty runs — MPI needs both legs."*

### Flashcard F-026 — Global MPI: dimensions, indicators and weights
**Front:** What are the dimensions, indicators and weights in the global MPI (UNDP and OPHI)?
**Formula:** Weighted deprivation score c = Σ w(j) × d(j), where d(j) = 1 if deprived in indicator j. Dimensions carry equal weight (1/3 each). Health: child mortality 1/6, nutrition 1/6. Education: years of schooling 1/6, school attendance 1/6. Living standards: cooking fuel, sanitation, drinking water, electricity, housing, assets, each 1/18. Ten indicators in total. Poor if c ≥ 1/3.
**Worked example:** Household deprived in nutrition (1/6), years of schooling (1/6) and sanitation (1/18): c = 0.1667 + 0.1667 + 0.0556 = 0.389 ≥ 0.333 → poor.
**Learn:**
- Global MPI is associated with UNDP and OPHI; household indicators are drawn from surveys (owner 02 §7 and §4).
- The 2026 Prelims PYQ on MPI methodology, indicators and institutional comparison is routed here (owner 02, 2026 PYQ block; key provisional, answer not recorded here).
- Weights and cut-off are the same as the owner's stated structure; the detailed weight table is confirmed against OPHI's global MPI page (✅ OPHI, "What is the global MPI?": health 1/6 + 1/6, education 1/6 + 1/6, six living-standard indicators at 1/18 each, cut-off one-third). Wikipedia 'Multidimensional Poverty Index' lists the same ten indicators, equal dimension weights and the "MPI poor (≥ 33%)" cut-off (✅ Wikipedia MPI).
**Trap:** Global MPI and NITI Aayog's national MPI differ in indicators and weights (see F-027); do not transplant one to the other.
**Back:** *"Ten indicators, three equal dimensions, one-third line — deprivation is counted with weights."*

### Flashcard F-027 — NITI Aayog national MPI (12 indicators)
**Front:** What are the dimensions, indicators, weights and cut-off in India's national MPI?
**Formula:** Same structure: c = Σ w(j) × d(j); poor if c ≥ 1/3. ⚠️ Weights as recalled from NITI Aayog's national MPI baseline report (2021) and progress review (2023), NITI sources returned HTTP 403 or 404 in this pass; the Wikipedia pages 'Multidimensional Poverty Index', 'Poverty in India' and 'National Multidimensional Poverty Index (India)' give no NITI indicator list or weights (the India article cites OPHI's global-MPI 55.4% for a 2005 state table, a different method, so it cannot confirm 55.3%); the owners do not state these weights, so still unverified: health — nutrition, child and adolescent mortality, maternal health, each 1/9; education — years of schooling, school attendance, each 1/6; living standards — cooking fuel, sanitation, drinking water, electricity, housing, assets, bank account, each 1/21. Dimensions weight 1/3 each.
**Worked example:** Illustrative household deprived in maternal health (1/9), school attendance (1/6) and sanitation (1/21): c = 0.1111 + 0.1667 + 0.0476 = 0.325 < 0.333 → not multidimensionally poor, despite three deprivations.
**Learn:**
- NITI Aayog tracks India's national MPI for domestic policy and state and district comparison (owner 02 §4).
- India's national MPI (owner 02 §8, as reported in Survey 2025-26): 55.3% in 2005-06, 14.96% in 2019-21, 11.28% in 2022-23 (✅ owner 02 §8, as reported in Survey 2025-26; Survey not fetchable this pass; cite as Survey-reported).
- Owner 02 notes MPI depends on indicator selection and survey periodicity (owner 02 §6A).
**Trap:** Global MPI ≠ NITI national MPI; a headline MPI figure is only comparable within the same methodology and vintage.
**Back:** *"Twelve indicators, the same one-third line — India's count is its own, built for its own households."*

### GROUP — Inflation and price indices

### Flashcard F-028 — Inflation rate
**Front:** How is the inflation rate calculated from a price index?
**Formula:** π(t) = [P(t) − P(t−1)] ÷ P(t−1) × 100. Year-on-year (y/y) uses P(t) and P(t−12) for monthly data; month-on-month (m/m) uses P(t) and P(t−1).
**Worked example:** CPI rises from 130 to 135.2 in a year → inflation = (135.2 − 130) ÷ 130 × 100 = 4.0%.
**Learn:**
- Inflation is a sustained rise in the general price level; disinflation means prices rise more slowly; deflation is a sustained fall (owner 03 §2).
- Headline CPI is the RBI-MPC nominal anchor under India's flexible inflation-targeting framework; (✅ owner 04 §4 and §6 state a 4% target with a ±2 band; ✅ Wikipedia 'Inflation targeting' table: India's 4% target adopted 08/2016; ⚠️ the ±2 band, the current framework notification and its period are not verified).
**Trap:** Falling inflation is not falling prices; a fall in the inflation rate still leaves prices higher.
**Back:** *"Percent change in the index is inflation — and disinflation only slows the climb, it does not reverse it."*

### Flashcard F-029 — Consumer Price Index (CPI)
**Front:** How is the CPI computed, and what does it measure?
**Formula:** CPI(t) = [Σ w(i) × p(i,t) ÷ p(i,0)] × 100, with fixed base-period weights w(i) = base expenditure shares. Equivalent to Σ p(i,t) × q(i,0) ÷ Σ p(i,0) × q(i,0) × 100 (a Laspeyres-type index).
**Worked example:** Base basket costs 300: rice 2 kg at ₹40 = 80, oil 1 litre at ₹120 = 120, services ₹100. Now: rice ₹44 (2 kg = 88), oil ₹130 (= 130), services ₹110. Total = 328. CPI = 328 ÷ 300 × 100 = 109.3.
**Learn:**
- CPI is a retail consumer basket that includes services and has a larger food component than WPI (owner 03 §2 and §6).
- MoSPI compiles CPI; the owner records the 2024=100 base from January 2026 replacing 2012=100 for current releases (owner 03 §8).
- CPI-IW (industrial workers) is the variant used for dearness-allowance indexation (owner 03 §5). ⚠️ Confirm the current CPI-IW base.
- Headline CPI includes food and fuel; core excludes them conventionally (owner 03 §6).
**Trap:** Do not join index levels across 2012=100 and 2024=100 without an official link. CPI is not the same as WPI.
**Back:** *"Fix the basket, price it now, divide by its base cost — the household bill in index form."*

### Flashcard F-030 — Wholesale Price Index (WPI)
**Front:** How is the WPI computed, and what does it cover?
**Formula:** WPI(t) = [Σ w(i) × p(i,t) ÷ p(i,0)] × 100 over wholesale goods only (primary articles, fuel and power, manufactured products). Services are excluded. Laspeyres-type fixed-weight index.
**Worked example:** Illustrative wholesale basket costs 300 in the base; now costs 315. WPI = 315 ÷ 300 × 100 = 105.
**Learn:**
- The Office of the Economic Adviser, DPIIT compiles WPI (owner 03 §4).
- The owner records WPI with 2022-23 base for the May 2026 release onward, replacing 2011-12 (owner 03 §8).
- WPI is a producer-cost signal, not a household cost-of-living index (owner 03 §6A).
- The PPI framework launched in June 2026 with 2022-23 base runs alongside WPI for a planned five-year transition; PPI replaces WPI gradually, not CPI (owner 03 §8).
**Trap:** WPI is not India's consumer cost-of-living index (owner 03 §7). WPI excludes services.
**Back:** *"WPI prices the factory gate, not the kitchen — goods only, no services."*

### Flashcard F-031 — Laspeyres versus Paasche index
**Front:** How do Laspeyres and Paasche indices differ in their quantity weights, and which Indian index uses which?
**Formula:** Laspeyres L = Σ p(t) × q(0) ÷ Σ p(0) × q(0) × 100 (base-year quantities). Paasche P = Σ p(t) × q(t) ÷ Σ p(0) × q(t) × 100 (current-year quantities).
**Worked example:** Using F-014 data: Laspeyres = (12 × 100 + 22 × 50) ÷ (10 × 100 + 20 × 50) = 2,300 ÷ 2,000 × 100 = 115.0. Paasche = (12 × 110 + 22 × 60) ÷ (10 × 110 + 20 × 60) = 2,640 ÷ 2,300 × 100 = 114.8.
**Learn:**
- CPI and WPI are fixed-base (Laspeyres-type) indices; the GDP deflator is Paasche-type (F-015).
- A Laspeyres index tends to overstate inflation when consumers substitute away from goods whose prices rise; a Paasche index tends to understate it. The bias is the standard reason for periodic basket revision (✅ Wikipedia 'Laspeyres index': Laspeyres "often overstates inflation because it does not account for consumers reacting to price changes"; Paasche "understates inflation by assuming consumers instantly adjust to new quantities").
**Trap:** Mixing up which weight set each index uses; the GDP deflator and CPI can diverge sharply for this reason (owner 03 §5).
**Back:** *"Laspeyres keeps the old basket and runs high; Paasche keeps today's and runs low."*

### Flashcard F-032 — Base effect
**Front:** What is the base effect, and how does it change a year-on-year inflation reading?
**Formula:** y/y inflation(t) = [I(t) ÷ I(t−12) − 1] × 100. The base effect is the change in y/y that arises only because I(t−12) was unusually high or low, even when the month's m/m change is ordinary.
**Worked example:** Last June index = 100 (low). This June index = 110 → y/y = 10%. Next year's June index = 111 when this June was 110 → y/y = 0.9%, even though the m/m change was an ordinary 0.9%. The sharp fall in y/y reflects the high base, not a new price drop.
**Learn:**
- Base effects are arithmetic comparisons with an unusual prior base, not new price shocks (owner 03 §7).
- Read the base before interpreting a y/y reading; use m/m and momentum alongside it (owner 03 advanced §5).
**Trap:** A base effect is not a new supply shock or policy success.
**Back:** *"A low base makes a small month look large; a high base hides a real rise — read the base first."*

### Flashcard F-033 — Core inflation
**Front:** How is core inflation defined, and how does it relate to headline inflation?
**Formula:** Core inflation = inflation of the CPI excluding food and fuel (conventional definition). Headline = w(core) × π(core) + w(food and fuel) × π(food and fuel), with weights summing to 1.
**Worked example:** Illustrative: w(core) = 0.70, π(core) = 4.0%; w(food and fuel) = 0.30, π(food and fuel) = 10%. Headline = 0.70 × 4.0 + 0.30 × 10 = 5.8%.
**Learn:**
- Core strips out volatile food and fuel to show demand-driven and sticky price pressure (owner 03 §6).
- The Survey 2025-26 recorded core at 4.62% in December 2025 with a major precious-metals contribution (✅ figure: owner 03 §8, citing Survey 2025-26; ⚠️ series and component treatment still unverified). Precious metals show why core is not a clean demand signal.
**Trap:** Core is not always below headline; relative food, fuel and other price moves can reverse the order (owner 03 §7).
**Back:** *"Core is headline without the weather and fuel noise — but gold can make even core noisy."*

### Flashcard F-034 — Real interest rate (Fisher relation)
**Front:** How is the real interest rate computed from the nominal rate and expected inflation?
**Formula:** Fisher: i = r + π(e), so approximate real rate r ≈ i − π(e) (nominal rate minus expected inflation). Exact form: (1 + i) ÷ (1 + π(e)) − 1.
**Worked example:** Nominal rate 7%, expected inflation 4% → real rate ≈ 3%. Exact: 1.07 ÷ 1.04 − 1 = 2.88%.
**Learn:**
- The real rate uses expected inflation, not necessarily current inflation (owner 03 advanced §3).
- Real rates drive saving and investment incentives; a cut in the nominal rate can be a real tightening if expected inflation falls faster.
**Trap:** Subtracting current inflation rather than expected inflation gives a different real rate.
**Back:** *"Real rate is the nominal rate minus what people expect prices to do — expectations, not yesterday's index, drive it."*

### Flashcard F-035 — Phillips curve (expectations-augmented)
**Front:** What relation does the short-run Phillips curve describe, and when does it break down?
**Formula:** π(t) = π(e) − β(u(t) − u*) + s(t), with β > 0; u = unemployment rate, u* = natural rate, s = supply shock. Output-gap form: π(t) = π(e) + κ × output gap + s(t).
**Worked example:** Illustrative: π(e) = 4%, unemployment 1 percentage point below the natural rate, β = 0.5 → π = 4 − 0.5 × (−1) = 4.5%.
**Learn:**
- The short-run trade-off is a demand-management guide, not a mechanical law (owner 03 §6).
- It weakens when supply shocks, administered prices, imported commodities and informal labour markets dominate (owner 03 §6A).
- Stagflation (weak growth or unemployment with inflation) is the case where a supply shock moves both variables the wrong way (owner 03 §6).
**Trap:** The Phillips curve is not a long-run trade-off. Do not use it to explain a vegetable-supply shock.
**Back:** *"Tight labour lifts prices — until a supply shock breaks the link."*

### Flashcard F-036 — Purchasing power of money (real value)
**Front:** How is the real value or purchasing power of a rupee computed from a price index?
**Formula:** Real value of a nominal amount (in base-year prices) = Nominal amount × 100 ÷ P(t), where P(t) is the price index with base 100. Purchasing power of ₹1 = 100 ÷ P(t) rupees of base-year goods.
**Worked example:** CPI = 150. ₹100 today buys what ₹100 ÷ 1.5 = ₹66.67 bought in the base year.
**Learn:**
- Purchasing power of money is the reciprocal of the price level; it is not the same as purchasing power parity (PPP), which compares price levels across countries (owner 01 advanced and owner 01 §5A).
- Indexation through DA or CPI-IW protects some organised-sector earners more than informal workers or the poor (owner 03 §5).
**Trap:** Purchasing power parity (cross-country exchange conversion) is not purchasing power of money (domestic price level).
**Back:** *"A rupee's power is the reciprocal of the price index — double the prices, halve the buying."*

### GROUP — Money supply, reserves and the RBI liquidity framework

### Flashcard F-037 — High-powered money (reserve money base)
**Front:** How is high-powered money (H) built up from its components?
**Formula:** H = C + R + OCR, where C = currency with the public plus cash held by banks (currency in circulation), R = bankers' deposits (reserves) with RBI, and OCR = other deposits with RBI. Component definitions confirmed by Wikipedia 'Money supply', which quotes the RBI definition of M0 as "Currency in circulation, plus bankers' deposits with the RBI and 'other' deposits with the RBI" (✅ Wikipedia 'Money supply'; the RBI reserve-money table itself was not reached, ⚠️ for its current release).
**Worked example:** Illustrative, ₹ lakh crore: C = 35, R = 12, OCR = 3 → H = 50.
**Learn:**
- Currency notes are RBI liabilities; they are part of the monetary base (owner 04 §6).
- H is the base on which the money multiplier acts: M = m × H (F-038).
- The RBI influences H through LAF operations, OMOs and FX intervention; sterilisation offsets FX-driven liquidity (owner 04 §2).
**Trap:** High-powered money is not M3; M3 is a multiple of H through the banking system, not the same thing.
**Back:** *"Public cash, bank reserves, and other RBI deposits — the base that the multiplier multiplies."*

### Flashcard F-038 — Money multiplier (currency–deposit form)
**Front:** How does the money multiplier link reserve money to broad money?
**Formula:** M = m × H, with m = (c + 1) ÷ (c + r). c = currency-deposit ratio (C ÷ D), r = reserve-deposit ratio (cash reserves and excess reserves ÷ deposits). If c = 0: m = 1 ÷ r.
**Worked example:** Illustrative: c = 0.20, r = 0.10 → m = 1.20 ÷ 0.30 = 4.0. With H = 50, money supply M = 4.0 × 50 = 200.
**Learn:**
- The multiplier rises when reserve impounding and currency leakage fall and when banks lend rather than hold excess reserves (owner 04 §6).
- Raising CRR lowers the multiplier; so does a rising currency preference.
- The multiplier is an outcome ratio, not a policy instrument; policy works through H and reserve ratios (owner 04 §2).
**Trap:** The multiplier is not the same as the credit multiplier (F-039), which is a simpler reserve-based measure.
**Back:** *"Leakage into cash and reserves locked at the RBI — the multiplier is one plus leakage over leakage plus reserve."*

### Flashcard F-039 — Credit multiplier (1 ÷ CRR)
**Front:** What is the simple credit multiplier and what does it assume?
**Formula:** Credit multiplier = 1 ÷ CRR, with CRR as a fraction of deposits. Maximum theoretical credit from a new deposit = new deposit ÷ CRR.
**Worked example:** Illustrative CRR = 4% (fraction 0.04) → multiplier = 25. A new deposit of ₹1,000 could support up to ₹25,000 of credit in this simple model. Current RBI CRR is not quoted here (⚠️ verify).
**Learn:**
- The simple model ignores SLR holdings, excess reserves and currency leakage, so actual credit expansion is smaller (owner 04 §6A on CRR as a blunt tool).
- CRR is charged on NDTL, not on total liabilities (F-047).
**Trap:** The credit multiplier is an upper bound in the simple model, not an observed number.
**Back:** *"Each rupee of deposit could fund one over CRR rupees of loans — the reserve is the brake."*

### Flashcard F-040 — M0 (reserve money)
**Front:** What is M0 in the RBI money-stock hierarchy?
**Formula:** M0 = reserve money = currency in circulation + bankers' deposits with RBI + other deposits with RBI (equal to H in F-037). (✅ Wikipedia 'Money supply', RBI definition: currency in circulation + bankers' deposits with the RBI + other deposits with the RBI.)
**Worked example:** Using F-037 illustrative values: M0 = 35 + 12 + 3 = 50.
**Learn:**
- M0 is the narrowest RBI-controlled aggregate; it moves with LAF and OMO operations.
- It is the base for the money multiplier.
**Trap:** M0 is not cash alone; bank reserves with RBI form part of it.
**Back:** *"M0 is the RBI's own balance-sheet money — notes plus bank reserves, nothing more."*

### Flashcard F-041 — M1 (narrow money, revised definition)
**Front:** What is M1 in the revised RBI money-stock definition?
**Formula:** M1 = currency with the public + demand deposits of the public with banks + other deposits with RBI. Definition confirmed: Wikipedia 'Money supply' quotes the RBI as "Currency with the public plus deposit money of the public" (✅ Wikipedia 'Money supply'; the deposit money includes demand deposits and "other" deposits with the RBI). The year and content of any revision of the aggregates remain ⚠️ unverified (RBI Handbook not reached).
**Worked example:** Illustrative: currency with public 30 + demand deposits 15 + other deposits with RBI 2 = 47 (₹ lakh crore).
**Learn:**
- M1 is the transactional, spendable money stock.
- Whether a 2021 revision replaced an earlier definition is unverified; check the vintage before comparing with older series (⚠️).
**Trap:** Do not assume where savings deposits sit inside M1 or M3 without checking the current RBI table (⚠️).
**Back:** *"M1 is money you can spend on sight: notes, demand money and RBI's other deposits."*

### Flashcard F-042 — M2 (M1 plus post-office savings)
**Front:** What is M2 and what does it add to M1?
**Formula:** M2 = M1 + savings deposits with post office savings banks (✅ Wikipedia 'Money supply', RBI definition: "M1 plus savings deposits with post office savings banks").
**Worked example:** Illustrative: M1 = 47 + post-office savings deposits 4 = M2 = 51.
**Learn:**
- M2 extends M1 to the post-office savings channel.
- Post-office time deposits sit in the wider M4, not in M2 (✅ M4 = M3 + all deposits with post office savings banks, Wikipedia 'Money supply'; M2 takes only savings deposits).
**Trap:** M2 is not M3; M3 adds bank time deposits, not post-office savings.
**Back:** *"M2 is M1 plus the post office passbook savings."*

### Flashcard F-043 — M3 (broad money)
**Front:** What is M3 and how is it built?
**Formula:** M3 = M1 + time deposits with the banking system (✅ corrected: the "net" qualifier was dropped; Wikipedia 'Money supply' quotes the RBI as "M1 plus time deposits with the banking system").
**Worked example:** Illustrative: M1 = 47 + bank time deposits 120 = M3 = 167.
**Learn:**
- M3 is the RBI's broad money aggregate and the one most often cited in liquidity analysis.
- The Survey 2025-26 liquidity snapshot reported M3 growth of 12.1% year-on-year for FY26 (✅ owner 04 §8, citing the Survey 2025-26 liquidity snapshot; as of the owner's cutoff).
- Read broad-money growth beside credit, deposits and nominal activity rather than as a direct inflation signal (owner 04 advanced §9).
**Trap:** M3 growth is not inflation; M3 is not the same as reserve money (M0).
**Back:** *"M3 is the broad money: spendable money plus the time deposits banks hold."*

### Flashcard F-044 — M4 (widest RBI measure)
**Front:** What is M4 and how does it extend M3?
**Formula:** M4 = M3 + total deposits with post-office savings organisations (✅ Wikipedia 'Money supply', RBI definition: "M3 plus all deposits with post office savings banks"; National Savings Certificates are excluded).
**Worked example:** Illustrative: M3 = 167 + post-office deposits 10 = M4 = 177.
**Learn:**
- M4 is the widest aggregate, adding all post-office deposits rather than only savings.
- M1 ⊂ M2 ⊂ M3 ⊂ M4 nest as money-stock aggregates; M0 (reserve money) is a separate base aggregate, not a subset of M1, because bankers' reserves sit in M0 but not in M1 (✅ by the RBI definitions quoted in Wikipedia 'Money supply').
**Trap:** M4 is not M3 plus savings only; it adds all post-office deposits.
**Back:** *"M4 is the widest net: all of M3, plus every rupee in the post office."*

### Flashcard F-045 — Cash Reserve Ratio (CRR)
**Front:** What is the CRR, what base does it apply to, and where must the reserve be held?
**Formula:** Required CRR balance = CRR (%) × NDTL. The reserve is held as cash balance with RBI, not in bank vaults.
**Worked example:** Illustrative: NDTL = ₹1,00,000 crore, CRR = 4% → required balance = ₹4,000 crore. Current CRR not quoted (⚠️ verify the RBI notification). Wikipedia 'Cash reserve ratio' gives 4.50% for India dated 6 April 2023 (secondary, stale; not adopted).
**Learn:**
- CRR is a share of net demand and time liabilities maintained as cash with RBI (owner 04 §2).
- It impounds lendable resources broadly and is a blunt, powerful liquidity tool; repeated use can strain intermediation (owner 04 §6A).
- CRR changes affect lendable resources broadly; OMO changes durable liquidity through securities trades (owner 04 §7).
**Trap:** CRR is not SLR (owner 04 basic, semantic-completeness ledger). Cash in a bank's own vault does not count toward CRR.
**Back:** *"CRR is cash locked at the RBI — a slice of net deposit liabilities, never the vault."*

### Flashcard F-046 — Statutory Liquidity Ratio (SLR)
**Front:** What is the SLR and what assets satisfy it?
**Formula:** Required SLR holdings = SLR (%) × NDTL. Eligible holdings: cash, gold and unencumbered approved securities (government securities). Eligible assets confirmed in part: Wikipedia 'Statutory liquidity ratio' lists "cash, gold reserves, Govt. bonds and other central bank approved securities" (✅ Wikipedia; the word "unencumbered" is not in that source). The same article words the base as "total demand and time liabilities" (no "net"), which conflicts with the NDTL base here, so the base stays ⚠️. Its 18.00% is dated 11 April 2020 and is not a current figure (⚠️).
**Worked example:** Illustrative: NDTL = ₹1,00,000 crore, SLR = 18% → required eligible assets = ₹18,000 crore. Current SLR not quoted (⚠️ verify).
**Learn:**
- SLR is a liquid-asset requirement held by the bank; CRR is cash with RBI. They are different instruments with different purposes (owner 04 basic, semantic-completeness ledger).
- Holdings of government securities under SLR tie banks to sovereign debt and affect the flow of funds to government borrowing (⚠️ standard).
**Trap:** CRR and SLR are not interchangeable: CRR is cash with RBI and earns no market return; SLR assets are securities or cash the bank holds itself.
**Back:** *"CRR is cash at the RBI; SLR is the shelf of liquid securities the bank keeps for itself."*

### Flashcard F-047 — Net demand and time liabilities (NDTL)
**Front:** What is NDTL and why does it matter?
**Formula:** NDTL = Demand liabilities + Time liabilities − amounts due from banks (in India and abroad). ⚠️ Confirm the current RBI definition, which governs the base for CRR and SLR.
**Worked example:** Illustrative: demand liabilities 40,000 + time liabilities 80,000 − due from banks 5,000 = NDTL 1,15,000. CRR at 4% → required balance 4,600.
**Learn:**
- CRR and SLR both apply to NDTL, not total deposits (owner 04 §2 and §4 on CRR as a share of net demand and time liabilities).
- Net of inter-bank dues avoids double counting inside the banking system.
**Trap:** NDTL is not total deposits; an inter-bank deduction changes the base.
**Back:** *"NDTL is what the bank owes its depositors, less what other banks owe it — the base for reserves."*

### Flashcard F-048 — LAF corridor: repo, standing deposit facility and marginal standing facility
**Front:** How are the repo rate, the SDF rate and the MSF rate related in the liquidity adjustment facility (LAF) corridor?
**Formula:** SDF rate = Repo rate − 0.25 percentage point. MSF rate = Repo rate + 0.25 percentage point. Corridor width = MSF − SDF = 0.50 percentage point (50 basis points). SDF spread confirmed as of 7 October 2026: the Wikipedia 'Reserve Bank of India' infobox shows the policy repo rate at 5.50% and the SDF rate at 5.25%, a 25 bp gap (✅ Wikipedia RBI infobox, dated; a secondary source, not an RBI primary release). The MSF spread remains ⚠️ unverified: the Wikipedia RBI policy-rate table is dated 9 April 2025 (repo 6.0%, MSF 6.25%, a 25 bp spread, stale), and no RBI monetary-policy statement stating the MSF rate was found (RBI press-release listings reached for Sept–Oct 2026 show liquidity notices only).
**Worked example:** Illustrative repo of 6.00% (hypothetical, not current): SDF = 5.75%, MSF = 6.25%, corridor width = 0.50 percentage point.
**Learn:**
- Repo injects liquidity against collateral; SDF absorbs surplus liquidity without collateral; MSF is an overnight emergency borrowing window against eligible securities (owner 04 §2 and §6).
- The SDF is the floor for overnight rates in the corridor; the WACR is the operating target (owner 04 advanced §7).
- Owner 04 advanced: the repo is the policy signal; the WACR is the operating target; the headline CPI is the target (owner 04 advanced §3 and §7).
- The 2024 PYQ rejected the broad claim that NBFCs have routine LAF access; direct access is institution- and facility-specific (owner 04 §7 and owner 05 §9).
**Trap:** Every liquidity injection is a rate cut is false: liquidity quantity and the stance are distinct (owner 04 §7). A corridor spread is not a mechanical proof of current policy rates.
**Back:** *"Repo sits in the middle; SDF a quarter below, MSF a quarter above — a fifty-basis-point pipe."*

### Flashcard F-049 — MSF borrowing cap
**Front:** How is the marginal standing facility's borrowing cap defined?
**Formula:** Borrowing cap under MSF = a RBI-set percentage of a bank's NDTL (overnight limit). The percentage is not quoted here. ⚠️ The percentage has been revised over time; verify the current RBI notification before quoting any number. The Wikipedia 'Reserve Bank of India' article says "Banks can borrow up to 2.5%" of NDTL with no date and alongside conflicting rate tables, so it is not adopted (⚠️ still unverified).
**Worked example:** Illustrative only: if the cap were 1% of NDTL and NDTL were ₹1,00,000 crore, the cap would be ₹1,000 crore. This is an arithmetic illustration, not a current RBI cap.
**Learn:**
- MSF is an emergency overnight backstop for scheduled commercial banks against eligible securities (owner 04 §2).
- The cap limits how much of the backstop a bank can use; it is an NDTL-linked ceiling, not a fixed rupee amount.
**Trap:** MSF is not open to every financial entity; NBFCs do not have routine LAF access (owner 04 §7; owner 05 §6).
**Back:** *"MSF is the overnight lifeboat, sized to a share of the bank's deposit base — not a bottomless tap."*

### GROUP — Interest rates, bonds and equities

### Flashcard F-050 — Simple interest
**Front:** How is simple interest computed?
**Formula:** SI = P × R × T ÷ 100; amount A = P + SI. P = principal (₹), R = rate (% per year), T = time (years).
**Worked example:** ₹50,000 at 8% for 3 years: SI = 50,000 × 8 × 3 ÷ 100 = ₹12,000; A = ₹62,000.
**Learn:**
- Interest is paid only on the principal; no interest earns interest.
- Convert months to years before applying the formula.
**Trap:** Mixing per-month and per-year rates without conversion.
**Back:** *"Simple interest is principal, rate and time — nothing grows on the interest itself."*

### Flashcard F-051 — Compound interest
**Front:** How is compound interest computed, and how does compounding frequency change it?
**Formula:** A = P × (1 + r ÷ 100)^n for annual compounding. With m compoundings per year: A = P × (1 + r ÷ (100m))^(mn). Compound interest CI = A − P.
**Worked example:** ₹1,00,000 at 10% a year compounded annually for 2 years: A = 1,00,000 × 1.10² = ₹1,21,000; CI = ₹21,000 (simple interest would give ₹20,000).
**Learn:**
- Interest earns interest, so the growth accelerates over time.
- Compounding frequency raises the effective yield (F-053).
**Trap:** Using the simple-interest formula for compound-interest questions.
**Back:** *"Compound means interest earns interest — the base grows each period, so the total outruns the rate."*

### Flashcard F-052 — Equated monthly instalment (EMI)
**Front:** How is an EMI computed for a loan repaid in equal monthly instalments?
**Formula:** EMI = P × r × (1 + r)^n ÷ [(1 + r)^n − 1], where r = annual rate ÷ 12 ÷ 100 (monthly rate) and n = number of monthly instalments.
**Worked example:** P = ₹10,00,000, annual rate 9% (r = 0.0075), n = 240 months. (1.0075)^240 ≈ 6.0092 (✅ corrected: was 6.0090; recomputed). EMI = 10,00,000 × 0.0075 × 6.0092 ÷ 5.0092 ≈ ₹8,997 a month. Total repaid ≈ 8,997 × 240 ≈ ₹21.6 lakh.
**Learn:**
- Early instalments are mostly interest; later ones are mostly principal.
- Floating-rate EMIs change with rate transmission, which is uneven across loans (owner 04 §5 and §6A).
- Prepayment reduces the outstanding principal and total interest; check bank terms.
**Trap:** Using the annual rate directly in the monthly formula is a unit error.
**Back:** *"EMI is the level payment that clears the loan — heavy interest first, principal later."*

### Flashcard F-053 — Effective annual yield (effective rate)
**Front:** How is the effective annual yield computed for an instrument compounding m times a year?
**Formula:** Effective annual yield = (1 + r ÷ m)^m − 1, with r the nominal annual rate and m the number of compoundings per year. Express ×100 for %.
**Worked example:** 12% a year compounded quarterly: (1.03)^4 − 1 = 0.1255, i.e. 12.55%.
**Learn:**
- Effective yield exceeds nominal yield whenever compounding is more than annual.
- Compare instruments on effective rates, not on stated rates with different compounding.
**Trap:** A higher stated rate can be a lower effective return if it compounds less often.
**Back:** *"Effective yield is the true annual return after compounding — compare like with like."*

### Flashcard F-054 — Face value and coupon
**Front:** How are the coupon amount and cash flows of a bond determined by face value and coupon rate?
**Formula:** Annual coupon = coupon rate × face value (par). Semi-annual coupon = coupon ÷ 2. Total cash flow at maturity = last coupon + face value.
**Worked example:** Face value ₹1,000 with 8% coupon: coupon = ₹80 a year (₹40 each half-year).
**Learn:**
- Coupon is the contractual interest rate on the face value; it does not change with market price (owner 08 §6).
- Bondholders are creditors and rank ahead of equity shareholders in repayment (owner 08 §6).
- Yield is the market-based return, which equals coupon only when the price equals face value (owner 08 advanced §7).
**Trap:** Coupon is not yield; a bond bought at a discount has yield above coupon.
**Back:** *"Coupon is the promise written on the face; yield is what you actually earn at the price you pay."*

### Flashcard F-055 — Current yield
**Front:** How is the current yield computed, and what does it leave out?
**Formula:** Current yield (%) = Annual coupon ÷ Market price × 100.
**Worked example:** Face ₹1,000, coupon 8% → annual coupon ₹80. Market price ₹950 → current yield = 80 ÷ 950 × 100 = 8.42%.
**Learn:**
- Current yield is a quick income measure; it ignores the capital gain pulled to par at maturity.
- Use yield to maturity (F-057) for a complete return comparison.
**Trap:** Current yield is not YTM; it ignores the discount or premium to par.
**Back:** *"Current yield is the coupon over today's price — it ignores the pull back to par."*

### Flashcard F-056 — Bond price–yield relation (inverse)
**Front:** How is a bond's price determined by its yield, and how do price and yield move?
**Formula:** P = Σ(t = 1 to n) C ÷ (1 + y)^t + F ÷ (1 + y)^n, with C = periodic coupon, F = face value, y = yield per period, n = periods. For a plain fixed-coupon bond, price and yield move inversely.
**Worked example:** Two-year bond, F = 100, annual coupon 8%: at y = 8%, P = 8 ÷ 1.08 + 108 ÷ 1.08² = 100.00. At y = 10%, P = 8 ÷ 1.10 + 108 ÷ 1.21 = 7.27 + 89.26 = 96.53.
**Learn:**
- Yield up, price down; a bond trading below par has yield above coupon (owner 08 §7 and advanced §5).
- Duration measures price sensitivity to yield; convexity refines it (owner 08 advanced §3).
- Price risk is separate from credit risk: a safe bond still loses market value when yields rise (owner 08 §6A).
**Trap:** Bond prices do not rise with market yields for a plain bond (owner 08 §7).
**Back:** *"Yield up, price down — promised cash is worth less when the market rate rises."*

### Flashcard F-057 — Yield to maturity (YTM)
**Front:** What is yield to maturity and how is it found?
**Formula:** YTM = the rate y that solves Market price P = Σ C ÷ (1 + y)^t + F ÷ (1 + y)^n. Approximation: YTM ≈ [C + (F − P) ÷ n] ÷ [(F + P) ÷ 2].
**Worked example:** F = 1,000, coupon C = 80, price P = 950, n = 5. Approximation gives (80 + 50 ÷ 5) ÷ ((1,000 + 950) ÷ 2) = 90 ÷ 975 = 9.2%. Solving exactly gives about 9.3%.
**Learn:**
- YTM is the internal rate of return if the bond is held to maturity and coupons are reinvested at YTM.
- It combines coupon income and the gain or loss from buying below or above par.
**Trap:** YTM is not the coupon rate and not the current yield; YTM assumes reinvestment at the same rate.
**Back:** *"YTM is the one rate that makes today's price equal every promised rupee."*

### Flashcard F-058 — Earnings per share (EPS)
**Front:** How is EPS computed?
**Formula:** EPS = (Profit after tax − Preference dividends) ÷ Number of equity shares outstanding.
**Worked example:** Profit after tax ₹500 crore, no preference dividends, 100 crore equity shares → EPS = ₹5 per share.
**Learn:**
- EPS is the profit attributable to one equity share; it is not the dividend paid.
- Dividends are declared by the board from profit and are not contractual (owner 08 §7).
**Trap:** EPS is not dividend per share; a firm can have high EPS and pay no dividend.
**Back:** *"EPS is the year's profit for every share in issue — earned, not paid out."*

### Flashcard F-059 — Price–earnings ratio (P/E)
**Front:** How is the P/E ratio computed and how is it read?
**Formula:** P/E = Market price per share ÷ EPS (trailing or forward EPS, as stated).
**Worked example:** Market price ₹100, EPS ₹5 → P/E = 20 (₹20 paid per rupee of annual earnings).
**Learn:**
- Higher P/E reflects growth expectations, low risk, or overvaluation; compare within the same sector and period.
- P/E is not meaningful for loss-making firms; check the EPS basis.
**Trap:** P/E is not a return; a P/E of 20 does not mean 5% yield in the same sense as a bond.
**Back:** *"P/E is what you pay per rupee of yearly earnings — price over profit per share."*

### Flashcard F-060 — Market capitalisation
**Front:** How is market capitalisation computed, and what does it represent?
**Formula:** Market capitalisation = Share price × Number of shares outstanding (equity).
**Worked example:** Price ₹2,000 × 10 crore shares = ₹20,000 crore.
**Learn:**
- Market capitalisation is the market value of equity, not the capital raised or the book value.
- Listed-company size is usually read from market capitalisation; free-float variants are a separate measure (⚠️).
**Trap:** Market capitalisation is not the money a company raised in its IPO or its book equity.
**Back:** *"Market cap is price times every share in issue — what the market puts on the whole company."*

### Flashcard F-061 — Dividend yield
**Front:** How is dividend yield computed?
**Formula:** Dividend yield (%) = Dividend per share (DPS) ÷ Market price per share × 100.
**Worked example:** DPS ₹5, price ₹100 → dividend yield = 5%.
**Learn:**
- Dividends depend on declaration and profits; they are not contractual like bond interest (owner 08 §7).
- A high dividend yield can reflect a falling price as well as a generous payout.
**Trap:** Dividend is not bond interest; a dividend cut does not breach a legal obligation in the way a missed coupon does.
**Back:** *"Dividend yield is cash back per rupee of price — declared, never promised."*

### Flashcard F-062 — Net asset value (NAV) of a mutual fund
**Front:** How is the NAV per unit of a mutual fund computed?
**Formula:** NAV per unit = (Market value of assets − Liabilities) ÷ Number of units outstanding, struck at the day's valuation point. ⚠️ SEBI valuation timing rules to be checked.
**Worked example:** Assets ₹10,500 crore, liabilities ₹100 crore, units 500 crore → NAV = 10,400 ÷ 500 = ₹20.80.
**Learn:**
- Open-ended mutual-fund units transact with the fund at applicable NAV; ETF units trade intraday on the exchange at market price, which can deviate from NAV (owner 08 §5 and advanced §5).
- NAV does not guarantee return; a low NAV is not a cheap price.
**Trap:** NAV is not a guaranteed return and not the market price of an ETF unit.
**Back:** *"NAV is the pool's net assets per unit — no guarantee, just the day's value of the portfolio."*

### Flashcard F-063 — Expense ratio (total expense ratio)
**Front:** How is a fund's expense ratio computed, and how does it affect investors?
**Formula:** Expense ratio (%) = Total annual fund expenses ÷ Average net assets × 100.
**Worked example:** Expenses ₹30 crore, average net assets ₹3,000 crore → expense ratio = 1.0% a year.
**Learn:**
- The expense ratio is deducted from the fund's return; compare funds within the same category.
- Index-style and ETF products often carry lower expense ratios (⚠️ general pattern, not a rule).
**Trap:** Expense ratio is an annual deduction on average assets, not a one-time entry load.
**Back:** *"The expense ratio is the yearly toll on the pool, charged on average assets, not on what you put in."*

### GROUP — Bank capital, liquidity and asset-quality ratios

### Flashcard F-064 — Capital adequacy ratio (CAR or CRAR)
**Front:** How is the capital adequacy (CRAR) ratio computed, and what minima apply in India?
**Formula:** CRAR (%) = (Tier 1 capital + Tier 2 capital) ÷ Risk-weighted assets (RWA) × 100. RWA = Σ (exposure × risk weight). Basel III global minimum total capital = 8% of RWA. RBI's India-specific minima per owner 06: CET1 ≥ 5.5%, Tier 1 ≥ 7%, Total CRAR ≥ 9%, excluding the Capital Conservation Buffer; with the 2.5% CCB (in CET1), effective CET1 ≈ 8% and effective total CRAR = 11.5%. The owner-confirmed minima (✅ owner 06 §4 and §6) cite the RBI Basel III Master Circular last issued 1 April 2025; ⚠️ the latest version is not verified. The global Basel figures (total capital above 8%, Tier 1 at least 6%, CET1 4.5%, CCB 2.5% of RWA) are confirmed by Wikipedia 'Basel III' (✅ Wikipedia Basel III).
**Worked example:** Illustrative: total capital ₹10,000 crore, RWA ₹1,00,000 crore → CRAR = 10%, which is above the 9% minimum but below the 11.5% effective level including CCB.
**Learn:**
- Capital is measured against risk-weighted assets, not total assets; the same balance sheet can carry different requirements (owner 06 §6).
- India's floor is stricter than the Basel global floor (owner 06 §7 trap).
- Capital adequacy alone cannot substitute for credit-appraisal quality or governance reform (owner 06 §5).
**Trap:** The Basel global 8% is not India's 9% minimum; do not quote the global figure for an India-specific answer (owner 06 §7).
**Back:** *"Capital over risk-weighted assets — the risk, not the size, sets the buffer."*

### Flashcard F-065 — Common Equity Tier 1 (CET1) ratio
**Front:** How is the CET1 ratio computed, and what is its minimum in India?
**Formula:** CET1 ratio (%) = CET1 capital ÷ RWA × 100. CET1 = fully paid-up equity and reserves, net of regulatory deductions (excludes additional Tier 1 and Tier 2). India: CET1 minimum 5.5% plus CCB 2.5% gives an effective 8% (✅ owner 06 §4 and §6; ⚠️ latest Master Circular version not verified).
**Worked example:** Illustrative: CET1 ₹6,000 crore, RWA ₹1,00,000 crore → CET1 ratio = 6.0%. It clears the 5.5% minimum but sits inside the 8% effective level, which is the CCB zone.
**Learn:**
- CET1 is the highest-quality loss-absorbing capital; Basel's global CET1 floor is 4.5% (owner 06 §4; ✅ Wikipedia 'Basel III').
- Tier 1 = CET1 + Additional Tier 1; Total capital = Tier 1 + Tier 2 (owner 06 §4 and §6).
**Trap:** CET1 is not Tier 1; Tier 1 includes AT1 instruments.
**Back:** *"CET1 is the pure equity cushion — the first loss and the purest test of capital."*

### Flashcard F-066 — Leverage ratio
**Front:** How is the leverage ratio computed, and why is it not risk-weighted?
**Formula:** Leverage ratio (%) = Tier 1 capital ÷ Total exposure (on- and off-balance sheet, unweighted) × 100. Basel III reference minimum is 3%. Basel III reference minimum of 3% confirmed by Wikipedia 'Basel III' ("Basel III introduced a minimum leverage ratio of 3%", ✅). RBI's Eleventh Amendment Directions, 2026 (press release of 23 October 2026, prid=63854) issue guidelines on the "Leverage Ratio 2017 Standard" effective 1 April 2027 (✅ RBI press release). The RBI minimum and bank categories are in the linked directions, which were not reached, so the India minimum remains ⚠️.
**Worked example:** Illustrative: Tier 1 = 6, total exposure = 150 (₹ lakh crore) → leverage ratio = 4.0%.
**Learn:**
- The leverage ratio is a non-risk-weighted backstop to the CRAR, guarding against models that understate risk (⚠️ standard Basel purpose).
- It uses total exposure, not RWA.
**Trap:** Leverage ratio is not the same as CRAR; a bank can meet CRAR and still breach the leverage backstop if its risk weights are low.
**Back:** *"Leverage ratio ignores risk weights — it caps total exposure as a backstop when models mislead."*

### Flashcard F-067 — Liquidity Coverage Ratio (LCR)
**Front:** How is the LCR computed, and what horizon does it cover?
**Formula:** LCR (%) = Stock of High-Quality Liquid Assets (HQLA) ÷ Total net cash outflows over the next 30 calendar days × 100. Minimum 100%. Basel global minimum of 100% confirmed (✅ Wikipedia 'Basel III': LCR ≥ 100%); the 30-calendar-day horizon is confirmed by the BIS Basel Framework LCR40 description (✅ BIS). RBI's India minimum and HQLA definitions remain ⚠️ unverified.
**Worked example:** Illustrative: HQLA = 120, net 30-day outflows = 100 → LCR = 120%.
**Learn:**
- LCR is a 30-day stress liquidity test introduced in the Basel III liquidity framework after the global financial crisis (owner 06 advanced §7 notes liquidity standards added after the crisis).
- It tests whether the bank can survive a short-term run with liquid assets.
**Trap:** LCR measures liquidity, not solvency; a bank can have a high LCR and weak capital.
**Back:** *"LCR asks: can you survive thirty days of withdrawals with assets you can sell at once?"*

### Flashcard F-068 — Net Stable Funding Ratio (NSFR)
**Front:** How is the NSFR computed, and what horizon does it cover?
**Formula:** NSFR (%) = Available Stable Funding (ASF) ÷ Required Stable Funding (RSF) × 100. Minimum 100% over a one-year horizon. Basel global minimum above 100% over a one-year horizon confirmed (✅ Wikipedia 'Basel III': "ASF / RSF > 100%", "over a one-year period of extended stress"). RBI's India minimum and the ASF/RSF factor tables remain ⚠️ unverified.
**Worked example:** Illustrative: ASF = 1,050, RSF = 1,000 → NSFR = 105%.
**Learn:**
- NSFR tests structural funding: long-term assets should be funded by stable, long-term sources.
- It complements the LCR (30-day) with a one-year structural view.
**Trap:** NSFR is a one-year structural measure; LCR is a 30-day stress measure. Do not swap them.
**Back:** *"NSFR asks: is long-term lending funded by long-term money, not by overnight borrowing?"*

### Flashcard F-069 — Gross NPA ratio (GNPA ratio)
**Front:** How is the gross NPA ratio computed, and what is the NPA test for a term loan?
**Formula:** GNPA ratio (%) = Gross NPA ÷ Gross advances × 100. Standard NPA test for a term loan: interest or principal overdue for more than 90 days (owner 06 §2).
**Worked example:** Illustrative: GNPA ₹2,200 crore ÷ gross advances ₹1,00,000 crore × 100 = 2.2%.
**Learn:**
- The owner records scheduled commercial bank GNPA of 2.2% and NNPA of 0.5% by September 2025 (owner 05 §8; owner 06 §8). Vintage and series to be cited with the figure.
- Recognition under RBI prudential norms comes before provisioning and resolution (owner 06 §3).
**Trap:** NPA is a classification under prudential norms, not a legal default event; restructured accounts are a separate category (owner 06 §7).
**Back:** *"Gross NPA over gross loans — the bad share before any provision is set aside."*

### Flashcard F-070 — Net NPA ratio (NNPA ratio)
**Front:** How is the net NPA ratio computed?
**Formula:** NNPA ratio (%) = Net NPA ÷ Net advances × 100. Net NPA = Gross NPA − provisions held against NPAs (⚠️ RBI treatment of interest suspense to be verified). Net advances = gross advances − provisions held against advances (⚠️ to be verified).
**Worked example:** Illustrative: GNPA 2,200; provisions against NPAs 1,300 → NNPA = 900. Gross advances 1,00,000; provisions on advances 1,500 → net advances = 98,500. NNPA ratio = 900 ÷ 98,500 × 100 = 0.91%.
**Learn:**
- NNPA is the loss the bank has not yet covered by provisions; it is the residual exposure.
- The owner records a 0.5% scheduled-bank NNPA by September 2025 (✅ owner 05 §8, citing a September 2025 figure).
**Trap:** NNPA is not GNPA minus GNPA ratio; the denominator is net advances, not gross advances.
**Back:** *"Net NPA is what remains after provisions — the loss not yet put aside."*

### Flashcard F-071 — Provision coverage ratio (PCR)
**Front:** How is the provision coverage ratio computed, and what does a higher PCR signal?
**Formula:** PCR (%) = Provisions held against NPAs ÷ Gross NPA × 100.
**Worked example:** Illustrative: provisions 1,300 ÷ GNPA 2,200 × 100 = 59.1%.
**Learn:**
- A higher PCR means more of the bad-loan stock is already covered by provisions (loss absorption).
- Provisioning recognises expected loss; write-off removes an asset from active books but recovery rights may continue (owner 06 §6 and §7).
**Trap:** Provisioning is not the same as write-off; PCR measures provisions, not the recovery achieved.
**Back:** *"PCR is the provision set aside for each rupee of bad loan — the shock absorber in rupee terms."*

### Flashcard F-072 — Net interest margin (NIM)
**Front:** How is net interest margin computed?
**Formula:** NIM (%) = (Interest earned − Interest expended) ÷ Average earning assets × 100.
**Worked example:** Interest earned ₹900 crore, interest expended ₹600 crore, average earning assets ₹5,000 crore → NIM = 300 ÷ 5,000 × 100 = 6.0%.
**Learn:**
- NIM measures the spread from intermediation: asset yields minus funding cost, as a share of earning assets.
- A high share of CASA (F-074) lowers the cost of funds and supports NIM (⚠️ standard link).
- NPAs reduce interest income and therefore NIM.
**Trap:** NIM is not net profit; it is one step before operating costs and provisions.
**Back:** *"NIM is the spread between what the bank earns on loans and what it pays for deposits, over its earning assets."*

### Flashcard F-073 — Credit-deposit (CD) ratio
**Front:** How is the credit-deposit ratio computed, and what does it show?
**Formula:** CD ratio (%) = Total bank credit (gross advances) ÷ Total deposits × 100.
**Worked example:** Credit ₹80,000 crore ÷ deposits ₹1,00,000 crore × 100 = 80%.
**Learn:**
- The CD ratio shows how much of deposits a bank lends out; a rising ratio signals stronger credit intermediation and possibly tighter liquidity.
- It is an intermediation measure, not a reserve requirement; CRR and SLR apply on NDTL (F-045 and F-046).
**Trap:** CD ratio is not CRR or SLR; it is a balance-sheet ratio.
**Back:** *"CD ratio is how much of the deposit base is out on loan — the bank's lending appetite in one number."*

### Flashcard F-074 — CASA ratio
**Front:** How is the CASA ratio computed, and why do banks track it?
**Formula:** CASA ratio (%) = (Current account deposits + Savings account deposits) ÷ Total deposits × 100.
**Worked example:** Current account ₹15,000 crore + savings ₹35,000 crore = ₹50,000 crore; total deposits ₹1,00,000 crore → CASA ratio = 50%.
**Learn:**
- CASA deposits are low-cost funding; a higher CASA ratio supports net interest margin (F-072).
- Term deposits are costlier; their share rises when banks compete for funds.
**Trap:** CASA excludes term deposits; a high CASA ratio is not the same as a high deposit base.
**Back:** *"CASA is the cheap money banks keep — current and savings, the costless part of funding."*

## A. FORMULAS — Fiscal, External Sector, Poverty, Agriculture, Industry and Micro

> Build note: exact formulas are standard economics. Time-varying official values are taken only from the Economy owners with their as-of labels. Anything not in the owners, or not confirmed by a live fetch, is marked ⚠️ and must be verified before use. Illustrative numbers in worked examples are hypothetical, not official statistics.

### GROUP — Fiscal

### Flashcard F-101 — Revenue deficit
**Front:** Which gap measures current (non-asset-creating) overspending by the government, and how is it computed?
**Formula:** Revenue deficit (RD) = Revenue expenditure − Revenue receipts. Units: ₹ crore or lakh crore in a given fiscal year. Revenue receipts = tax revenue + non-tax revenue (excluding recoveries of loans and disinvestment proceeds).
**Worked example:** Illustrative: revenue expenditure ₹40 lakh crore, revenue receipts ₹32 lakh crore. RD = 40 − 32 = ₹8 lakh crore.
**Learn:**
- Revenue expenditure supports current services and transfers and does not create a durable asset. A positive RD means the government is borrowing to meet current spending.
- Measure it as a percentage of GDP for comparability across years (RD/GDP × 100). Use BE, RE or Actuals consistently; the owner stresses that BE is an authorisation, not a realised figure.
- Related: fiscal deficit (F-103) and effective revenue deficit (F-102).
**Trap:** Zero RD does not mean zero fiscal deficit, because capital expenditure can still require borrowing. Do not treat RD as the same thing as the fiscal deficit.
**Back:** *"Revenue deficit: spend today what tomorrow's taxes did not fund."*

### Flashcard F-102 — Effective revenue deficit
**Front:** How is the "genuinely unproductive" part of the revenue deficit isolated?
**Formula:** Effective revenue deficit (ERD) = Revenue deficit − Grants-in-aid given to states/UTs for creation of capital assets. Equivalently: ERD = (Revenue expenditure − Grants for capital-asset creation) − Revenue receipts.
**Worked example:** Illustrative: RD = ₹8 lakh crore; grants to states for capital assets = ₹2 lakh crore. ERD = 8 − 2 = ₹6 lakh crore.
**Learn:**
- The grant is booked as revenue expenditure by the Centre but finances a durable asset at the receiving end. ERD therefore nets it out.
- Owner 09 states that a lower ERD reclassifies the transfer; it does not prove that the grant was well used. Read it with actual asset-creation outcomes.
- Pair with **effective capital expenditure**: the Centre's own capex plus capital-asset grants. The owner reports effective capex at 4% of GDP in FY25 (Economic Survey 2025-26, as cited in owner 09).
**Trap:** ERD is not "revenue deficit minus capex". Only grants for capital-asset creation are netted.
**Back:** *"Effective RD nets the bricks the states build with Centre's grants."*

### Flashcard F-103 — Fiscal deficit (and the borrowing identity)
**Front:** What is the fiscal deficit, and how is it financed?
**Formula:** Fiscal deficit (FD) = Total expenditure − (Revenue receipts + Non-debt capital receipts). Non-debt capital receipts = recovery of loans + disinvestment proceeds + other non-debt capital receipts. Borrowing is excluded from non-debt receipts, so FD is the total borrowing requirement for the year.
Financing identity: FD = Net market borrowings (dated securities) + External borrowings (net) + Other liabilities (for example, small-savings and other borrowings) ± Drawdown of cash balances.
**Worked example:** Illustrative: total expenditure ₹50 lakh crore, revenue receipts ₹32 lakh crore, recovery of loans ₹1 lakh crore, disinvestment ₹0.5 lakh crore. FD = 50 − (32 + 1 + 0.5) = ₹16.5 lakh crore.
**Learn:**
- Fiscal deficit is a flow over one year, not total public debt (owner 09).
- Union budget 2026-27 BE: FD 4.3% of GDP; 2025-26 RE: 4.4% of GDP (owner 09, dated to Union Budget 2026-27; check later RE/Actuals).
- FD/GDP × 100 is the standard ratio. The Union figure does not describe general government (states, local bodies, PSU liabilities).
**Trap:** Fiscal deficit is not "printing money". Ordinarily it is financed by market and other borrowing. Monetisation is a separate, more inflationary route (owner 03).
**Back:** *"Fiscal deficit: all spending, minus everything except borrowing."*

### Flashcard F-104 — Primary deficit
**Front:** What is the fiscal gap after removing interest on past debt?
**Formula:** Primary deficit (PD) = Fiscal deficit − Interest payments. Ratio form: PD/GDP × 100.
**Worked example:** Illustrative: FD ₹16.5 lakh crore, interest payments ₹11 lakh crore. PD = 16.5 − 11 = ₹5.5 lakh crore. Interest payments are the cost of past borrowing, so PD isolates the current-year fiscal gap.
**Learn:**
- A primary surplus means the current-year budget covers its non-interest spending without new borrowing, but FD can still be positive because of interest.
- Owner 09 confirms: primary deficit = fiscal deficit − interest payments (2025 Prelims tested this identity).
- Related: a "gross primary deficit" variant is also tested in PYQs (owner 09, 2025 Prelims Q65); check the question stem for the exact variant.
**Trap:** Do not subtract revenue deficit from FD. Only interest is removed.
**Back:** *"Primary deficit: borrowing for today, with yesterday's interest subtracted."*

### Flashcard F-105 — Revenue receipts vs capital receipts (classification identity)
**Front:** Which receipts are "revenue" and which are "capital", and what is the total-receipts identity?
**Formula:** Total receipts = Revenue receipts + Capital receipts. Revenue receipt: neither creates a liability nor reduces a financial asset (tax and non-tax revenue). Capital receipt: creates a liability or reduces a financial asset (borrowings, recovery of loans, disinvestment).
**Worked example:** Illustrative: tax ₹26 lakh crore + non-tax ₹6 lakh crore = revenue receipts ₹32 lakh crore; borrowing ₹15 lakh crore + loan recovery ₹1 lakh crore + disinvestment ₹0.5 lakh crore = capital receipts ₹16.5 lakh crore.
**Learn:**
- A disinvestment receipt is a capital receipt because it reduces a financial asset (equity held by Government).
- Borrowing is a capital receipt because it creates a liability, even though it finances spending.
- Owner 09 (2025 Prelims Q10): capital-receipt classification was tested directly.
**Trap:** "Capital receipts are revenue for spending without future cost" is wrong: borrowing creates liabilities and disinvestment reduces assets (owner 09 trap).
**Back:** *"Revenue creates nothing owed; capital creates something owed or sold."*

### Flashcard F-106 — Tax buoyancy
**Front:** How responsive is tax revenue to GDP growth, after discretionary changes are removed?
**Formula:** Tax buoyancy (ε_B) = (% change in tax revenue) ÷ (% change in nominal GDP), adjusted for discretionary tax changes (rate changes, new taxes). Simple form: ε_B = (ΔT/T) ÷ (ΔY/Y). Units: a ratio (dimensionless).
**Worked example:** Illustrative: nominal GDP grows 10%; tax revenue grows 12% in a year with no rate change. Buoyancy = 12/10 = 1.2 (tax grows faster than GDP). If an adjusted tax growth of 8% is observed, buoyancy = 0.8.
**Learn:**
- Buoyancy > 1 means taxes rise faster than GDP without any rule change.
- Buoyancy captures the whole tax system including base growth and compliance; elasticity (F-107) captures the structural response only.
- Owner 10: "tax buoyancy is not tax rate", and the owner's 2018-2023 demand set is not about buoyancy as such, so cite the formula explicitly.
**Trap:** A high tax rate does not automatically raise buoyancy. Tax base, evasion and compliance matter.
**Back:** *"Buoyancy: taxes outrun GDP when the economy and compliance do the lifting."*

### Flashcard F-107 — Tax elasticity
**Front:** What is the structural response of tax to income, before discretionary changes?
**Formula:** Tax elasticity (ε_T) = (% change in tax revenue) ÷ (% change in income), where the change is measured with the tax system's own rules, i.e., with no discretionary change. Units: dimensionless.
**Worked example:** Illustrative: income grows 10%; tax revenue grows 9% under unchanged rules. Elasticity = 9/10 = 0.9 (less than unity: an inelastic tax system).
**Learn:**
- Buoyancy includes discretionary changes; elasticity removes them. The difference is why Budget tax-rate hikes raise buoyancy but not elasticity.
- Progressive tax systems have elasticity above 1; proportional taxes have elasticity around 1; regressive taxes below 1 (standard public-finance classification).
**Trap:** Do not confuse elasticity with the tax-GDP ratio (F-108), which is a level, not a response.
**Back:** *"Elasticity: how tax reacts when the rulebook stays still."*

### Flashcard F-108 — Tax-GDP ratio
**Front:** How is the overall tax burden measured against the economy?
**Formula:** Tax-GDP ratio = (Gross or net tax revenue ÷ GDP) × 100. Specify the level (Centre, states, general government), gross or net of devolution, and the GDP base year.
**Worked example:** Illustrative: tax revenue ₹30 lakh crore, GDP ₹300 lakh crore. Tax-GDP = 30/300 × 100 = 10%.
**Learn:**
- The owner (09, 10) uses revenue receipts as a share of GDP: Centre revenue receipts averaged 9.1% of GDP in FY22-FY25 versus 8.5% in FY16-FY20 (Economic Survey 2025-26, as cited).
- Always state the GDP denominator and base year. A rebasing of GDP changes the ratio without any change in tax revenue.
**Trap:** Revenue receipts/GDP is broader than tax/GDP (it includes non-tax revenue). Do not swap them in an answer.
**Back:** *"Tax-GDP: what share of the nation's output the state can claim by law."*

### Flashcard F-109 — Debt-GDP ratio
**Front:** How is the sustainability of public debt measured?
**Formula:** Debt-GDP ratio = (Outstanding debt stock ÷ Nominal GDP) × 100. Debt is a stock; fiscal deficit is a flow. Debt dynamics: Δ(D/Y) ≈ (d − g)·(D/Y) + primary deficit ratio, where d = effective interest rate on debt and g = nominal GDP growth rate (approximate standard identity).
**Worked example:** Illustrative: debt ₹150 lakh crore, GDP ₹300 lakh crore → debt-GDP = 50%. If d = 7%, g = 10%, then (d − g) = −3%, so debt-GDP falls by about 3 percentage points of (D/Y) per year before the primary deficit effect.
**Learn:**
- Debt sustainability depends on the gap between the interest rate and nominal growth, and on the primary balance (owner 09 "debt-dynamics" logic).
- Owner 09: the N.K. Singh FRBM Review Committee shifted attention to a debt anchor and glide path rather than a one-year deficit figure.
**Trap:** A stable debt-GDP ratio is not the same as a stable deficit. A deficit that is smaller than nominal growth times debt can still leave debt stable.
**Back:** *"Debt-GDP: stock over output, watched against growth and interest."*

### Flashcard F-110 — FRBM targets and the escape clause
**Front:** What fiscal targets does the FRBM framework set, and when may they be relaxed?
**Formula (original Act, 2003; ✅ Wikipedia 'Fiscal Responsibility and Budget Management Act, 2003', fetched 2026-10-30):** Fiscal deficit ceiling ≤ 3% of GDP by 31 March 2008, with an annual minimum reduction of 0.3% of GDP; revenue deficit elimination by 31 March 2008 (postponed to 31 March 2009 and then suspended in 2009 after the 2008 crisis, per Wikipedia), with an annual minimum reduction of 0.5% of GDP.
**Escape clause (original Act; ✅ corrected: was 'subject to laying the reasons before Parliament'; Wikipedia paraphrase, statutory text not fetched):** The Central Government may depart from targets on grounds such as national security, natural calamity or other exceptional grounds it specifies; both Houses of Parliament must approve the deviation as soon as possible after the targets are exceeded.
**Worked example:** Illustrative: GDP ₹300 lakh crore. A 3% FD ceiling = ₹9 lakh crore. A FD of ₹16.5 lakh crore (F-103) = 5.5% of GDP, which breaches the ceiling by 2.5 percentage points.
**Learn:**
- Owner 09: FRBM Act 2003 and the annual fiscal statements (including the Macro Economic Framework Statement) impose medium-term disclosure discipline.
- ✅ The N.K. Singh-led FRBM Review Committee submitted its report on 23 January 2017 (made public 14 April 2017; Wikipedia FRBM page) and recommended a debt anchor with a glide path. The debt-to-GDP anchor numbers and the current escape-clause conditions are ⚠️ not verified (Wikipedia gives no numbers; check the Department of Economic Affairs document before quoting).
- Owner 09: the Budget 2026-27 FD BE is 4.3% of GDP (dated).
**Trap:** Do not state the current numerical FRBM target from memory. The 3% ceiling is the original 2003-Act figure; later rules differ.
**Back:** *"FRBM: a dated ceiling, a glide path, and a valve for emergencies that must be explained."*

### Flashcard F-111 — Investment (simple) multiplier
**Front:** By how much does national income rise for each ₹1 of autonomous investment or government spending, in the simplest closed model?
**Formula:** k = 1 ÷ (1 − MPC) = 1 ÷ MPS, where MPC = marginal propensity to consume and MPS = 1 − MPC. Assumes no taxes, no imports, and a closed economy.
**Worked example:** Illustrative: MPC = 0.8 → k = 1/(1 − 0.8) = 5. A ₹10,000 crore capex injection raises income by ₹50,000 crore in this stylised model.
**Learn:**
- Owner 09 (Mains angle): fiscal evaluation must consider multiplier, distribution and sustainability.
- Realistic multiplier is smaller once taxes and imports are included (see F-112).
- Owner 09: capex multipliers are high in principle, but project selection and execution determine them.
**Trap:** Do not use 1/(1−MPC) for India's real multiplier without taxes and import leakages. It is a textbook ceiling.
**Back:** *"Investment multiplier: one over the share you did not save."*

### Flashcard F-112 — Fiscal (government-spending) multiplier with taxes and imports
**Front:** How do taxes and imports reduce the multiplier for government spending?
**Formula:** k_G = 1 ÷ [1 − c(1 − t) + m], where c = MPC out of disposable income, t = proportional tax rate, m = marginal propensity to import. The denominator is 1 − c(1 − t) + m.
**Worked example:** Illustrative: c = 0.8, t = 0.2, m = 0.2. Denominator = 1 − 0.8 × 0.8 + 0.2 = 1 − 0.64 + 0.2 = 0.56. k_G = 1/0.56 ≈ 1.79.
**Learn:**
- The multiplier falls as taxes and imports rise, because more income leaks out of each spending round.
- Owner 09: multipliers depend on execution quality and financing conditions; crowding-out through interest rates can offset expansion.
- Compare with the simple multiplier (F-111): here 1.79 vs 5 under the same MPC, showing how leakages matter.
**Trap:** Do not compare a multiplier with and without leakages as if they were the same. State the model.
**Back:** *"Taxes and imports are the leaks that shrink the spending ripple."*

### Flashcard F-113 — Balanced budget multiplier
**Front:** What is the effect on income of an equal rise in government spending and taxes?
**Formula:** k_B = ΔY/ΔG (with ΔT = ΔG) = 1 in the simple model with a lump-sum tax. In general, k_B = k_G + k_T where k_T = −c ÷ [1 − c(1 − t) + m] (tax multiplier, F-115). With a proportional tax the balanced-budget multiplier is positive but less than 1 when leakages exist.
**Worked example:** Illustrative (lump-sum tax, c = 0.8): k_G = 1/(1 − 0.8) = 5; k_T = −0.8/(1 − 0.8) = −4; k_B = 5 + (−4) = 1. An extra ₹10,000 crore of spending financed by ₹10,000 crore of taxes raises income by ₹10,000 crore.
**Learn:**
- Balanced budgets are neutral in the textbook model, but not neutral if the tax falls on high-saving groups.
- Use this card to explain why "balanced budget" does not mean "no macro effect".
**Trap:** Do not claim a balanced budget raises income by a fixed multiple. It depends on the tax base and leakages.
**Back:** *"Balanced budget: spend what you tax and income still rises one for one."*

### Flashcard F-114 — Tax multiplier
**Front:** How does a change in taxes affect national income?
**Formula:** k_T = ΔY/ΔT = −MPC ÷ (1 − MPC) (lump-sum tax, closed economy). With proportional tax and imports: k_T = −c ÷ [1 − c(1 − t) + m].
**Worked example:** Illustrative: MPC = 0.8, tax cut ₹10,000 crore. k_T = −0.8/0.2 = −4. Income rises by 4 × 10,000 = ₹40,000 crore (a tax cut is a positive shock; a tax rise is negative).
**Learn:**
- The tax multiplier is smaller in magnitude than the spending multiplier, because part of a tax change is saved.
- Owner 10 (Mains angle): tax design matters for demand as well as equity.
**Trap:** The sign is negative: a tax increase reduces income. Do not write the tax multiplier as a positive number.
**Back:** *"Tax multiplier: a tax hike shrinks income by fewer rupees than the spend it funds."*

### Flashcard F-115 — MPC, MPS and APC
**Front:** What do marginal and average propensities mean and how are they linked?
**Formula:** MPC = ΔC ÷ ΔY; MPS = ΔS ÷ ΔY = 1 − MPC; APC = C ÷ Y; APS = S ÷ Y = 1 − APC. Units: dimensionless ratios between 0 and 1 (for MPC/MPS).
**Worked example:** Illustrative: income rises by ₹100 and consumption rises by ₹75. MPC = 75/100 = 0.75; MPS = 0.25. If C = 800 and Y = 1,000, APC = 0.8.
**Learn:**
- The multiplier (F-111) uses MPC; a higher MPC gives a higher multiplier.
- APC can be above MPC in the long run; the short-run consumption function has MPC < APC (standard Keynesian result).
**Trap:** MPC is a change ratio (marginal). APC is a level ratio (average). Do not interchange them.
**Back:** *"Marginal is the next rupee; average is the whole pie."*

### Flashcard F-116 — Laffer curve concept
**Front:** Why can a higher tax rate fall short of raising more revenue?
**Formula:** Tax revenue R(t) = t × B(t), where B(t) is the tax base, which falls as the rate rises. Revenue is maximised where dR/dt = 0; at that point the elasticity of the base with respect to the rate equals −1 (standard result).
**Worked example:** Illustrative: base B(t) = 1,000 − 800t (₹ crore, t in decimal). R(t) = t(1,000 − 800t). R is maximised at t = 1000/1600 = 0.625 (62.5%); at t = 0.8, R = 0.8 × 360 = 288, which is less than R(0.625) = 312.5. This is a stylised example only.
**Learn:**
- The Laffer curve is an inverted-U concept. It shows that above a critical rate, lower base and avoidance reduce revenue.
- In India, the relevant lever is the base and compliance (owner 10: "a higher tax rate always raises revenue" is a trap).
**Trap:** Do not state that India is on the wrong side of the Laffer curve. That is an empirical claim requiring evidence.
**Back:** *"Laffer: squeeze the rate too far and the base runs away."*

### Flashcard F-117 — Horizontal devolution formula (Finance Commission)
**Front:** How is a state's share of the divisible pool computed once the vertical share is fixed?
**Formula:** State i's share S_i = Σ_k (w_k × x_ik ÷ Σ_j x_jk), where x_ik = state i's value on criterion k, Σ_j x_jk = all-state total on criterion k, and w_k = weight of criterion k (weights sum to 100%). Multiply by the state pool to get rupees.
**Criteria (owner 10):** The Fifteenth Finance Commission used income distance, population, area, forest and ecology, demographic performance and tax effort in horizontal devolution.
**Weights (⚠️ still unverified; ✅ Wikipedia 'Fifteenth Finance Commission', fetched 2026-10-30, confirms the 2011 Census data basis and the 2021-22 to 2025-26 award period but does not state the weights):** The Fifteenth Finance Commission weights are commonly cited as income distance 45%, area 15%, population 15% (2011 Census), forest and ecology 10%, demographic performance 12.5% and tax effort 2.5% (these sum to 100%). Owner 10 gives the criteria but not the weights, and the official FC site returned HTTP 403 in this pass; verify against the official 15th FC report before quoting.
**Worked example:** Illustrative two-state, one-criterion case: state A has 30% of population, state B has 70%; population weight 15%. Contribution = 0.15 × 0.30 = 4.5% of the pool from population for state A.
**Learn:**
- Owner 10: Finance Commission recommends vertical devolution, horizontal distribution and grants. The FC does not set GST rates.
- Owner 10: 15th FC kept vertical devolution at 41%. The 16th FC award covers 2026-27 to 2030-31 with the vertical share at 41% of the divisible pool (✅ owner 10, citing the official action-taken memorandum; the memorandum fetch returned 403 in this pass).
**Trap:** The 2025 Prelims Q66 tested 41% (not 45%) for the 15th FC, per owner 10. Do not confuse the vertical share with the horizontal weights.
**Back:** *"Horizontal: each criterion's share, weighted, adds to the state's cut."*

### Flashcard F-118 — Vertical devolution share
**Front:** What fraction of the divisible pool of Union tax revenue goes to states as a whole?
**Formula:** Devolution to states = Vertical share × Divisible pool. Divisible pool = Gross tax revenue of the Union − surcharges and cesses − cost of collection. Share is expressed as a percentage of the divisible pool.
**Worked example:** Illustrative: gross tax ₹40 lakh crore; cesses and surcharges ₹6 lakh crore; cost of collection ₹0.5 lakh crore. Divisible pool = 40 − 6 − 0.5 = ₹33.5 lakh crore. At 41%, devolution = 0.41 × 33.5 = ₹13.735 lakh crore.
**Learn:**
- Owner 10: cesses and surcharges are not in the divisible pool in the same way as ordinary taxes. Repeated reliance shrinks the pool.
- Owner 10: the 16th FC accepted vertical share = 41% (dated).
**Trap:** Gross tax revenue is not the divisible pool. Cess and surcharge are deducted first.
**Back:** *"Vertical: take the pool minus cesses, then give states their 41%."*

### Flashcard F-119 — GST: CGST, SGST and IGST apportionment
**Front:** How is GST on a supply split between the Centre and states?
**Formula:** Intra-state supply: GST = CGST + SGST, each = (GST rate ÷ 2) × taxable value. Inter-state supply: GST = IGST = GST rate × taxable value. Total GST = CGST + SGST + IGST. Units: ₹ per taxable value (rate in %).
**Worked example:** Illustrative: taxable value ₹1,00,000 at an 18% rate. Intra-state: CGST = 9% = ₹9,000; SGST = 9% = ₹9,000; total ₹18,000. Inter-state: IGST = 18% = ₹18,000.
**Learn:**
- Destination-based: IGST follows final consumption (owner 10; Article 279A GST Council framework).
- CGST goes to the Centre and SGST to the State where the supply is consumed; IGST is then settled between the Centre and the destination State.
- Owner 10 GST 2.0 anchor: from 22 Sep 2025 broad 5% and 18% rates plus a special 40% demerit rate for specified supplies. Use the dated rates only.
**Trap:** The CGST/SGST split is always equal in an intra-state supply. The rate is halved for the two components, but the formula must state this.
**Back:** *"Intra-state splits in two halves; inter-state goes whole to IGST."*

### Flashcard F-120 — Input tax credit (ITC) computation
**Front:** How much GST does a taxable person actually pay after input tax credit?
**Formula:** Net GST payable = Output tax (GST charged on sales) − Eligible input tax credit (GST paid on purchases used in the business), subject to restrictions. Cascading is reduced because each stage credits the tax already paid.
**Worked example:** Illustrative: sales GST ₹18,000 (output); purchase GST ₹12,000 (input, all eligible). Net GST payable = 18,000 − 12,000 = ₹6,000, which is the GST attributable to the value added at this stage.
**Learn:**
- Owner 10: input tax credit reduces cascading when compliant value-chain invoices are matched under law.
- Credit usage order follows the CGST/SGST/IGST rules (for example, IGST credit can be used across heads). Verify exact sequencing against the CGST/IGST Acts before quoting.
- Refund delays and invoice matching are the main limitations (owner 10).
**Trap:** ITC is not a cash refund and is not available for every expense (blocked credits apply). Do not treat it as an unconditional rebate.
**Back:** *"ITC: the tax already paid upstream is the credit you subtract downstream."*

### Flashcard F-121 — GST cess
**Front:** How is a GST cess computed and why is it outside the divisible pool?
**Formula:** Cess = Cess rate × value (ad valorem) or ₹ per unit (specific). Revenue from cess is in the Union's cesses and surcharges category, not the divisible pool (owner 10).
**Worked example:** Illustrative ad valorem cess of 10% on a taxable value of ₹50,000 → cess = ₹5,000 (in addition to GST).
**Learn:**
- Owner 10: the compensation cess was discontinued for most goods after the Sep 2025 GST 2.0 reform and continues only on specified items until COVID-loan repayment; treat the post-repayment future as unsettled.
- Owner 10 Health and Education Cess illustrates Union resource-raising outside the divisible pool.
**Trap:** Cess and surcharge are not "shareable taxes". Do not treat cess revenue as part of the pool used for vertical devolution.
**Back:** *"Cess: an extra tax that the states do not share in the pool."*

### GROUP — External sector

### Flashcard F-122 — Balance of payments identity
**Front:** What is the BoP identity and how do reserves enter it?
**Formula:** CA + KA + E&O = ΔR, where CA = current account, KA = capital plus financial account excluding reserve changes, E&O = net errors and omissions, ΔR = increase in official reserves (with a sign convention: positive = reserves rise). Equivalent restatement: CA + KA + E&O − ΔR = 0.
**Worked example:** Illustrative: CA = −₹10 lakh crore; KA (ex-reserves) = +₹5 lakh crore; E&O = 0. Then ΔR = −10 + 5 + 0 = −₹5 lakh crore, i.e., reserves fall by ₹5 lakh crore to finance the gap.
**Learn:**
- Owner 19: modern BoP separates the capital account from the much larger financial account.
- A current-account deficit must be financed by net financial inflows, reserve use or accounting adjustment (owner 19).
- Reserves are central-bank external assets, not government budget revenue.
**Trap:** A balanced BoP does not mean there is no pressure; the identity holds by construction. Do not treat the accounting identity as a behavioural statement.
**Back:** *"Current plus capital, plus errors, equals the reserve change."*

### Flashcard F-123 — Trade balance
**Front:** What is the merchandise trade balance?
**Formula:** Trade balance (TB) = Merchandise exports (FOB) − Merchandise imports (CIF or FOB, per data convention). A negative value is a trade deficit.
**Worked example:** Illustrative: exports ₹35 lakh crore, imports ₹55 lakh crore → TB = 35 − 55 = −₹20 lakh crore (trade deficit).
**Learn:**
- Owner 20: trade balance concerns goods; the current account is broader (services, income, transfers).
- Owner 20 Economic Survey anchor: total exports USD 825.3 billion in FY25 (dated).
**Trap:** Merchandise deficit is not the BoP deficit. Services, income and transfers can offset it (owner 20 trap).
**Back:** *"Trade balance: goods only; the rest sits in the current account."*

### Flashcard F-124 — Current account and its components
**Front:** How is the current account built from its four parts?
**Formula:** CA = Goods balance + Services balance + Primary income balance + Secondary income balance (transfers, including remittances). Net invisibles = Services + Primary income + Secondary income.
**Worked example:** Illustrative (₹ lakh crore): goods −20; services +12; primary income −3; secondary income (remittances) +11. CA = −20 + 12 − 3 + 11 = 0. Net invisibles = 12 − 3 + 11 = +20, which exactly offsets the goods deficit of −20.
**Learn:**
- Owner 19: current account = trade in goods and services plus primary and secondary income.
- Remittances are transfers in the current account, not merchandise exports (owner 19 trap).
**Trap:** Invisibles are not the same as services. They include income and transfers.
**Back:** *"Current account: goods, services, income and gifts-from-abroad."*

### Flashcard F-125 — Current account deficit as % of GDP
**Front:** How is the current account deficit (CAD) expressed for comparison?
**Formula:** CAD% = (|CA| ÷ Nominal GDP) × 100, applied only when CA is negative. Use the fiscal-year or half-year GDP denominator and state it.
**Worked example:** Illustrative: CA = −₹7 lakh crore, GDP = ₹350 lakh crore → CAD% = 7/350 × 100 = 2.0% of GDP.
**Learn:**
- Owner 19 (Economic Survey 2025-26): CAD was 0.8% of GDP in H1 FY26 versus 1.3% in H1 FY25. Use the dated half-year value.
- A CAD is judged by financing quality (FDI vs short-term debt), not size alone (owner 19).
**Trap:** Do not divide by half-year GDP while quoting a full-year base. Keep the period consistent.
**Back:** *"CAD% is the gap as a share of the whole economy's output."*

### Flashcard F-126 — Invisibles (net)
**Front:** What are "invisibles" and how do they offset the goods deficit?
**Formula:** Net invisibles = Net services receipts + Net primary income + Net secondary income (transfers). Gross invisibles = total credits and total debits.
**Worked example:** Illustrative: services ₹12, primary income −₹3, transfers ₹11 → net invisibles = ₹20 lakh crore (as in F-124), which can offset a goods deficit of ₹20.
**Learn:**
- Owner 19: merchandise deficit can coexist with a manageable current account when services and transfers offset it.
- Owner 19 Mains angle: services exports and remittances concentrate external resilience in IT services and Gulf-linked remittances, which carry demand-concentration risk.
**Trap:** Invisibles are not a single line in the BoP. They are three separate subtotals in current account.
**Back:** *"Invisibles: the services, income and transfers that shrink the goods gap."*

### Flashcard F-127 — Nominal effective exchange rate (NEER)
**Front:** How is the rupee's value against a basket of trading partners' currencies measured?
**Formula:** NEER = Σ_i (w_i × E_i) in weighted-average form, or as a geometric weighted index: NEER_index = Π_i (E_i/E_i0)^(w_i) × 100 (trade weights summing to 1). E_i = rupee value of partner currency i (or inverse, per convention). Index form: a rise means appreciation in the chosen convention.
**Worked example:** Illustrative: two currencies, weights 0.6 and 0.4; both index values at 100 in base; in period t, currency 1 index = 110 and currency 2 index = 95. Geometric NEER = (1.10^0.6) × (0.95^0.4) × 100 ≈ 1.0589 × 0.9797 × 100 ≈ 103.7.
**Learn:**
- Owner 19 (PYQ ownership): NEER and REER are routed to the 2022 Prelims objective item.
- Wikipedia (fetched): NEER is weighted with the inverse of trade weights; the home currency index is divided by the geometric average of the basket currencies' value indices (convention noted). ✅ Wikipedia 'Effective exchange rate' (fetched 2026-10-30): NEER is typically calculated with geometric weighting; BIS publishes a narrow set of 27 countries and a broad set of 61 economies (BIS basket, not RBI).
- ⚠️ Basket size: the 6-currency NEER and 40-currency REER figures are recalled, not confirmed. The owners do not state the basket, and the RBI effective-exchange-rate page fetched in this pass gave no basket size. Verify with RBI publications before quoting.
**Trap:** NEER is nominal. It ignores inflation differences, which REER corrects (F-128).
**Back:** *"NEER: the rupee's average price against trade partners, unadjusted for prices."*

### Flashcard F-128 — Real effective exchange rate (REER)
**Front:** How is competitiveness measured after adjusting for relative prices?
**Formula:** REER = NEER × (P_home ÷ P_foreign), where P_foreign is a trade-weighted average of trading partners' price levels. In index form, a rise in REER means real appreciation (home goods become costlier relative to partners). Units: index (base year = 100).
**Worked example:** Illustrative: NEER index = 104; home price index rises 5%, foreign 2%. Ratio = 1.05/1.02 ≈ 1.0294. REER = 104 × 1.0294 ≈ 107.1 → real appreciation of about 3%.
**Learn:**
- Owner 19: nominal and real effective exchange rates differ because the latter adjusts for relative prices.
- Owner 19 PYQ: REER and NEER are routed to the 2022 Prelims item.
- The base year and CPI/WPI deflator used must be stated; RBI's REER base year is ⚠️ not verified (the RBI page fetched in this pass gave no base year; Wikipedia 'Real effective exchange rate' returned 404 in this pass, and 'Effective exchange rate' gives only the BIS base period of the 2011–13 average).
**Trap:** A rising NEER does not always mean stronger competitiveness; REER adjusts for inflation. Check the convention before reading "appreciation".
**Back:** *"REER: NEER corrected for the price gap, so it reads competitiveness, not nominal moves."*

### Flashcard F-129 — Real bilateral exchange rate
**Front:** What is the real exchange rate between two countries?
**Formula:** q = e × (P_foreign ÷ P_home), where e = domestic-currency price of one unit of foreign currency. Real depreciation of the home currency means q rises.
**Worked example:** Illustrative: e = ₹85 per USD; US price index 100, India price index 110 (both base-normalised). q = 85 × (100/110) = 77.27. A fall in q indicates real appreciation of the rupee.
**Learn:**
- Standard convention: q is the relative price of foreign goods in home-currency terms.
- Use the bilateral form for specific trade partners; use REER (F-128) for a trade-weighted measure.
**Trap:** Quoting e alone is nominal. The "real" label requires the price ratio.
**Back:** *"Real rate: nominal rate scaled by the price gap, not the price tag alone."*

### Flashcard F-130 — Purchasing power parity (PPP)
**Front:** What exchange rate equalises the price of a common basket across two countries?
**Formula:** Absolute PPP: S_PPP = P_home ÷ P_foreign (domestic currency per unit of foreign currency). Relative PPP: %ΔS = %ΔP_home − %ΔP_foreign (approx.). Units: currency per unit of foreign currency.
**Worked example:** Illustrative: basket costs ₹4,200 in India and $50 in the US. S_PPP = 4,200/50 = ₹84 per USD. If the market rate is ₹85, the rupee is slightly weaker than PPP implies.
**Learn:**
- PPP is used to compare GDP across countries (see F-184 for GDP at PPP).
- Owner 09, 10, 20, 23 mention PPP conceptually; the owners do not give PPP conversion-factor values, which change yearly. Use World Bank or IMF data with a date.
**Trap:** Market exchange rates and PPP exchange rates answer different questions. Do not use PPP to forecast the market rate in the short run.
**Back:** *"PPP: the rate at which one basket costs the same in both countries."*

### Flashcard F-131 — Forex reserves import cover (months of imports)
**Front:** How many months of imports can the reserves finance?
**Formula:** Import cover (months) = Forex reserves ÷ (Total imports ÷ 12) = Forex reserves ÷ Average monthly imports. Use the same currency and period for both terms.
**Worked example:** Illustrative: reserves USD 700 billion; annual imports USD 760 billion → monthly imports = 760/12 ≈ 63.3 → cover = 700/63.3 ≈ 11.1 months.
**Learn:**
- Owner 19 Economic Survey anchor: import cover was 11.1 months as of 9 January 2026; forex reserves were USD 701.4 billion as of 16 January 2026 (dated).
- Owner 19: reserve adequacy is multidimensional — import cover, short-term debt, broad money and stress scenarios. Import cover alone misses currency and rollover risk (1991 and 2013 episodes).
**Trap:** Import cover is not the same as reserves divided by the current-account deficit. Use imports.
**Back:** *"Cover is reserves over a month's import bill, not over the deficit."*

### Flashcard F-132 — External debt ratios (external debt/GDP and debt service ratio)
**Front:** How are external debt burden and servicing capacity measured?
**Formula:** External debt-to-GDP = (External debt stock ÷ GDP) × 100. Debt service ratio (DSR) = [(Interest + Principal repayments on external debt) ÷ (Current receipts: exports of goods and services + primary and secondary income receipts)] × 100 (conventional RBI-style measure; verify definition in the current RBI external-debt publication before quoting).
**Worked example:** Illustrative: external debt ₹80 lakh crore, GDP ₹350 lakh crore → debt-GDP ≈ 22.9%. Debt service: interest + principal ₹10 lakh crore; current receipts ₹60 lakh crore → DSR ≈ 16.7%.
**Learn:**
- Owner 19 Economic Survey anchor: external debt was 19.2% of GDP at end-September 2025 (dated).
- Owner 19 ECB section: ECBs are commercial, market-priced external debt and carry currency-mismatch and rollover risk.
**Trap:** Quoting external debt in USD without a GDP in USD is a unit error. Use a consistent currency.
**Back:** *"External debt over GDP; debt service over current receipts."*

### Flashcard F-133 — Short-term debt to reserves (Greenspan–Guidotti guide)
**Front:** How is rollover risk in external debt flagged?
**Formula:** Short-term debt ratio = Short-term external debt (original maturity ≤ 1 year) ÷ Forex reserves. Greenspan–Guidotti guideline: reserves should cover short-term external debt, i.e., ratio ≤ 1 (100%). Units: ratio or %.
**Worked example:** Illustrative: short-term debt USD 150 billion; reserves USD 700 billion → ratio = 150/700 ≈ 0.21 (21%). The guideline is satisfied.
**Learn:**
- Owner 19: reserve adequacy depends on maturity and rollover composition, not just import cover.
- Use original maturity, not residual maturity, when reading short-term debt.
**Trap:** Residual and original maturity differ. Check the definition used in any published series.
**Back:** *"Greenspan–Guidotti: short debt should not outrun the reserve cushion."*

### Flashcard F-134 — Marshall–Lerner condition and J-curve (depreciation and the trade balance)
**Front:** When does a currency depreciation improve the trade balance, and why can it worsen it first?
**Formula:** Marshall–Lerner condition: a depreciation improves the trade balance if |ε_x| + |ε_m| > 1, where ε_x = export demand elasticity and ε_m = import demand elasticity (assuming elastic supply and zero initial trade balance). J-curve: trade balance (in domestic currency) first worsens after depreciation because volumes adjust with a lag, then improves.
**Worked example:** Illustrative: ε_x = 0.6, ε_m = 0.5. Sum = 1.1 > 1 → Marshall–Lerner holds in this stylised case. If ε_x = 0.3, ε_m = 0.4, sum = 0.7 < 1 → depreciation worsens the balance.
**Learn:**
- ✅ Wikipedia 'Marshall–Lerner condition' (fetched 2026-10-30): the condition is that the absolute sum of export and import demand elasticities exceeds one, derived from a zero starting trade balance; the short-run worsening followed by long-run improvement is the J-curve effect. The elastic-supply assumption is the standard textbook addition and is not on that page.
- The J-curve explains why an immediate improvement is not guaranteed (owner 19 trap: "Depreciation always improves the trade balance immediately").
**Trap:** The condition is about elasticities, not about the size of the depreciation. Note the assumption of elastic supply.
**Back:** *"Depreciation helps when the elasticities add up beyond one, after the J bends."*

### Flashcard F-135 — Terms of trade (net barter and income)
**Front:** Are export prices rising faster than import prices, and what does it mean for income?
**Formula:** Net barter terms of trade (NBTT) = (Export price index ÷ Import price index) × 100. Income terms of trade (ITT) = (Export price index ÷ Import price index) × Export volume index. Units: index (base = 100).
**Worked example:** Illustrative: export price index 120, import price index 150 → NBTT = 120/150 × 100 = 80 (deterioration: each unit of exports buys fewer imports). If export volume index = 130, ITT = 80 × 130/100 = 104 (higher purchasing power despite worse price terms).
**Learn:**
- ✅ NBTT: terms of trade = export price index ÷ import price index × 100 (Wikipedia 'Terms of trade', fetched 2026-10-30). ⚠️ The income-terms formula (ITT = NBTT × export volume index) is not on that page and remains an unverified standard definition; use official index series with dates.
- NBTT falling with rising ITT means volume gains offset price loss.
**Trap:** A fall in NBTT is not a fall in income if volumes rise. Use ITT for purchasing-power questions.
**Back:** *"Net barter tracks price; income terms add the volume."*

### Flashcard F-136 — Tariff duties: ad valorem and specific
**Front:** How is a customs duty computed in ad valorem and specific forms?
**Formula:** Ad valorem duty = Rate (%) × Assessable value (CIF or transaction value). Specific duty = ₹ (or US$) per unit × Quantity. Mixed (compound) duty = ad valorem + specific.
**Worked example:** Illustrative: CIF value of edible oil ₹1,00,000 at 10% ad valorem → duty ₹10,000. Specific duty ₹30 per litre on 1,000 litres → duty ₹30,000. Owner 20: duty on crude/refined edible oils has been raised and cut in different years, so use a dated CBIC/DGFT rate.
**Learn:**
- Owner 20: the edible-oil basic customs duty is a live policy lever; import dependence persists.
- Specific duties are unaffected by price changes; ad valorem duties rise with price. Choose the form to match the policy aim.
**Trap:** Do not quote a specific duty as a percentage without a price. The two forms respond differently to price shocks.
**Back:** *"Ad valorem scales with the price; specific scales with the litre."*

### Flashcard F-137 — Effective rate of protection (ERP)
**Front:** How much protection does a tariff give to value added, once input tariffs are considered?
**Formula:** ERP = (t_o − Σ a_i × t_i) ÷ (1 − Σ a_i), where t_o = tariff on final output, t_i = tariff on input i, and a_i = input i's share in the value of output (at world prices). Units: percent.
**Worked example:** Illustrative: output tariff 20%; one input with share a = 0.5 at tariff 10%. ERP = (20 − 0.5 × 10)/(1 − 0.5) = (20 − 5)/0.5 = 30%. The effective protection (30%) exceeds the nominal output tariff (20%) because input tariffs are low.
**Learn:**
- ✅ Wikipedia 'Effective rate of protection' (fetched 2026-10-30): ERP = (Tf − Ti) ÷ VAint, where Tf = tariff paid on the final product, Ti = tariffs on importable inputs and VAint = international value added. With inputs valued at world prices this equals (t_o − Σ a_i t_i) ÷ (1 − Σ a_i) used in the formula above.
- Owner 20 (Mains angle): protecting an upstream industry can reduce downstream competitiveness. ERP is the formula that makes this measurable.
**Trap:** Nominal protection (F-138) is not effective protection. Input tariffs change the effective figure.
**Back:** *"ERP: the protection that the value added actually receives, after the inputs' tariffs."*

### Flashcard F-138 — Nominal rate of protection
**Front:** What tariff rate is quoted on the final good alone?
**Formula:** Nominal rate of protection (NRP) = Tariff rate on the final product (%). Equivalent to t_o in F-137, ignoring input tariffs.
**Worked example:** Illustrative: tariff on imported steel product 15% → NRP = 15%, even if inputs are taxed at 10%.
**Learn:**
- NRP is the headline tariff; ERP (F-137) can be higher or lower.
- Owner 20: tariffs protect producers but raise input or consumer costs when imports are used domestically.
**Trap:** Do not present NRP as the total protection a domestic industry enjoys. Check the input structure.
**Back:** *"Nominal: the tariff on the box; effective: the tariff on the value inside it."*

### GROUP — Poverty and inequality

### Flashcard F-139 — Poverty headcount ratio
**Front:** What share of the population lies below the poverty line?
**Formula:** H = q ÷ n × 100, where q = number of persons below the poverty line z (income or consumption below z), n = total population. Units: percent of population (incidence).
**Worked example:** Illustrative: population 1,000 persons, 230 below the line → H = 230/1000 × 100 = 23%.
**Learn:**
- H measures incidence, not depth (owner 23: headcount measures incidence while poverty gap captures depth).
- The headcount depends entirely on the line z chosen: a higher z raises H with the same distribution.
- The 2022-23 extreme poverty figure of 5.3% in the owner 23 Survey anchor uses the World Bank USD 3/day line at 2021 PPP, so it is not directly comparable with India's domestic lines (owner 23 caution).
**Trap:** Headcount ratio is not the number of poor persons. It is a share. Do not confuse with the poverty gap.
**Back:** *"Headcount: how many are under the line, as a share of all."*

### Flashcard F-140 — Poverty gap index and the FGT family
**Front:** How deep is poverty among the poor?
**Formula:** Poverty gap index (P1) = (1/n) × Σ_{i: y_i < z} (z − y_i)/z. Equivalent: P1 = H × I, where I = average income shortfall of the poor as a share of z. Family of Foster–Greer–Thorbecke measures: P_α = (1/n) Σ_{poor} ((z − y_i)/z)^α. P0 = headcount ratio, P1 = poverty gap, P2 = severity (squared gap).
**Worked example:** Illustrative: z = ₹1,000 per month; 3 poor persons with incomes 800, 600, 900; n = 10. Shortfalls: 200, 400, 100 → ratios 0.2, 0.4, 0.1. Sum = 0.7. P1 = 0.7/10 = 0.07 = 7%. H = 3/10 = 30%.
**Learn:**
- Owner 23: headcount captures incidence; poverty gap captures depth.
- The FGT family is the standard measurement framework; P2 gives extra weight to the poorest.
**Trap:** P1 is not the share of the poor who are poor. It is the total shortfall as a share of the line over the whole population.
**Back:** *"Poverty gap: the total shortfall, measured across everyone, not just the poor."*

### Flashcard F-141 — Lorenz curve and the Gini coefficient
**Front:** How is income or consumption inequality measured from a Lorenz curve?
**Formula:** Gini G = A ÷ (A + B) = 2A (when A + B = 0.5), where A = area between the line of perfect equality and the Lorenz curve, and B = area under the Lorenz curve. Discrete form: G = 1 − Σ_k (X_k − X_{k−1})(Y_k + Y_{k−1}), where X = cumulative population share and Y = cumulative income share (trapezoid rule). Units: 0 (equality) to 1 (perfect inequality).
**Worked example:** Illustrative, 4 equal-population groups with cumulative income shares Y = 0.10, 0.30, 0.60, 1.00 and X = 0.25, 0.50, 0.75, 1.00 (with X_0 = Y_0 = 0). Terms: (0.25)(0.10+0) = 0.025; (0.25)(0.30+0.10) = 0.10; (0.25)(0.60+0.30) = 0.225; (0.25)(1.00+0.60) = 0.40. Sum = 0.75. G = 1 − 0.75 = 0.25.
**Learn:**
- Owner 23: Lorenz curve plots cumulative population share against cumulative income or consumption share; Gini equals twice the area between the Lorenz curve and the line of perfect equality.
- Gini is sensitive to data (income vs consumption) and to the top of the distribution; read it with complementary measures (owner 23).
**Trap:** Gini is an inequality measure, not a poverty measure. A poverty fall can coexist with a rising Gini (owner 23 trap).
**Back:** *"Gini: twice the bow between the curve and the diagonal."*

### Flashcard F-142 — Palma ratio
**Front:** How is the gap between the top and bottom of the distribution measured?
**Formula:** Palma ratio = (Income share of the top 10%) ÷ (Income share of the bottom 40%). Units: ratio (dimensionless). A value above 1 indicates the top 10% earns more than the bottom 40% combined.
**Worked example:** Illustrative: top 10% hold 35% of income; bottom 40% hold 15%. Palma = 35/15 ≈ 2.33.
**Learn:**
- ✅ Wikipedia 'Palma ratio' (fetched 2026-10-30): the richest 10%'s share of gross national income divided by the poorest 40%'s share, resting on Palma's finding that the middle class takes about half of national income.
- Palma focuses on the tails, complementing the Gini, which is most sensitive to the middle of the distribution.
**Trap:** Palma uses the top 10% and bottom 40%, not the top 10% and bottom 10%.
**Back:** *"Palma: the top tenth over the bottom four-tenths."*

### Flashcard F-143 — Kuznets curve
**Front:** What relation between growth and inequality did Simon Kuznets propose?
**Formula:** Inverted-U hypothesis: inequality I rises then falls with income y, I = f(y) with f′ > 0 at low y and f′ < 0 at high y. A common quadratic form: I = a + b·y − c·y² with b, c > 0 (illustrative).
**Worked example:** Illustrative: I = 20 + 0.4y − 0.002y². Peak at y = 0.4/(2 × 0.002) = 100 (in stylised income units).
**Learn:**
- ✅ Wikipedia 'Kuznets curve' (fetched 2026-10-30): the inverted-U hypothesis, proposed in the 1950s–60s (1955 paper cited), links inequality to workers moving from agriculture to industry and rural to urban jobs.
- Modern evidence is mixed; the curve is a hypothesis, not a law (✅ Wikipedia: the hypothesis 'remains highly contested'; Kuznets himself worried about the fragility of the data). Cite it as a hypothesis.
**Trap:** The Kuznets curve does not predict that growth always lowers inequality. It describes a path that depends on policy and structure.
**Back:** *"Kuznets: inequality climbs, peaks, then falls, if the story goes to plan."*

### Flashcard F-144 — Tendulkar and Rangarajan poverty lines (numbers with caution)
**Front:** What are the Tendulkar (2009) and Rangarajan (2014) poverty lines, and how do they differ?
**Method:** Tendulkar (2009) moved from a calorie anchor to a broader consumption basket including health and education (owner 23). Rangarajan (2014) proposed a higher line using updated consumption norms (owner 23). Neither is India's single official line today (owner 23).
**Reference values (✅ 2011-12 values confirmed by Wikipedia 'Poverty in India', fetched 2026-10-30, citing RBI 2011-12 table: Tendulkar rural ₹816, urban ₹1,000, headcount 21.9%; Rangarajan rural ₹972, urban ₹1,407, headcount 29.5%; Tendulkar report November 2009, Rangarajan report June 2014. ⚠️ The 2004-05 line is still unverified):**
- Tendulkar 2011-12 line: rural about ₹816 and urban about ₹1,000 per person per month; all-India headcount about 21.9% (2011-12).
- Rangarajan 2011-12 line: rural about ₹972 and urban about ₹1,407 per person per month; all-India headcount about 29.5% (2011-12).
- Tendulkar 2004-05 line (⚠️): rural about ₹447 and urban about ₹579 per month.
**Worked example:** Illustrative only: a household of 5 with per-capita monthly consumption ₹900 is poor under the Rangarajan rural line (₹972) but not under the Tendulkar rural line (₹816), showing why the line choice matters.
**Learn:**
- Owner 23: attribute any line to its committee and year. Do not cite it as a current official line.
- The World Bank USD 3/day line (2021 PPP) is a separate international benchmark (owner 23 Survey anchor).
**Trap:** Tendulkar vs Rangarajan vs the World Bank line are different measures. A "poverty rate" must name its line.
**Back:** *"Two lines, two years, no official successor: name the committee before the number."*

### Flashcard F-145 — Dependency ratio
**Front:** How heavy is the non-working population relative to the working-age population?
**Formula:** Total dependency ratio = [(P_0–14 + P_65+) ÷ P_15–64] × 100 (conventions vary: some use 60+ in place of 65+). Old-age dependency ratio = (P_65+ ÷ P_15–64) × 100. Child dependency = (P_0–14 ÷ P_15–64) × 100.
**Worked example:** Illustrative: P_0–14 = 300 million; P_15–64 = 900 million; P_65+ = 100 million. Total dependency = (300 + 100)/900 × 100 = 44.4.
**Learn:**
- Owner 22: the dependency ratio is the mechanism for the demographic dividend; the window is time-bound.
- Owner 22: India's working-age share is projected to peak and then decline (⚠️ check the current official projection date before quoting).
**Trap:** A young population is not a dividend by itself. The dividend depends on a falling dependency ratio plus jobs (owner 22 trap).
**Back:** *"Dependency: the young and old per hundred working hands."*

### Flashcard F-146 — Total fertility rate and replacement-level fertility
**Front:** How many children does an average woman bear, and what rate sustains the population?
**Formula:** TFR = Σ_{a=15}^{49} ASFR_a × 5, where ASFR_a = age-specific fertility rate for each 5-year age group (births per woman in that group, per year). Replacement-level fertility ≈ 2.1 children per woman (standard demographic benchmark; depends on mortality).
**Worked example:** Illustrative ASFRs per 1,000 women (for 5-year groups 15–19, 20–24, 25–29, 30–34, 35–39, 40–44, 45–49): 50, 150, 130, 80, 40, 10, 2. Sum = 462 per 1,000 women → per woman 0.462 per year → TFR = 0.462 × 5 = 2.31.
**Learn:**
- Owner 22 does not give a current TFR figure; use the NFHS or SRS value with its year.
- Replacement level above 2.0 because of child mortality and sex ratio at birth.
**Trap:** TFR is a period measure, not a cohort fertility rate. Do not interpret a below-replacement TFR as immediate population decline.
**Back:** *"TFR: five-year births per woman summed; 2.1 keeps the numbers level."*

### Flashcard F-147 — Sex ratio (females per 1,000 males)
**Front:** How is the sex ratio defined and what is the child sex ratio?
**Formula:** Sex ratio = (Number of females ÷ Number of males) × 1,000. Child sex ratio (0–6 years) = (Females aged 0–6 ÷ Males aged 0–6) × 1,000. Units: females per 1,000 males.
**Worked example:** Illustrative: 480 million females and 520 million males → sex ratio = 480/520 × 1,000 = 923.
**Learn:**
- Census 2011 reference values: national sex ratio 943 females per 1,000 males (✅ Wikipedia 'Demographics of India', fetched 2026-10-30); child sex ratio 0–6: 918 (⚠️ still unverified; the Wikipedia pages fetched give no child-ratio figure; verify in the Census 2011 tables before quoting).
- Sex ratio at birth (SRB) is a separate measure (male births per female births) and is not the same as the census sex ratio.
**Trap:** A low child sex ratio is not the same as the overall sex ratio. Read the age group and reference.
**Back:** *"Sex ratio: females per thousand males, counted by age group."*

### Flashcard F-148 — LFPR, WPR and unemployment rate (PLFS)
**Front:** How are LFPR, WPR and the unemployment rate defined?
**Formula:** LFPR = (Labour force ÷ Working-age population) × 100, where labour force = employed + unemployed (seeking or available for work). WPR = (Employed ÷ Working-age population) × 100. Unemployment rate (UR) = (Unemployed ÷ Labour force) × 100. Relation: UR = (LFPR − WPR) ÷ LFPR × 100.
**Worked example:** Illustrative: working-age population 100 million; labour force 60 million; employed 56 million; unemployed 4 million. LFPR = 60%; WPR = 56%; UR = 4/60 × 100 = 6.7%.
**Learn:**
- Owner 22: LFPR, worker-population ratio and unemployment rate are distinct; PLFS reports all three on usual-status and current-weekly-status bases.
- A fall in UR can come from people leaving the labour force, which lowers LFPR (owner 22 trap).
**Trap:** The unemployment rate's denominator is the labour force, not the population (owner 22 trap).
**Back:** *"LFPR and WPR share the population; UR shares only the labour force."*

### Flashcard F-149 — PLFS status definitions and unemployment rate by status
**Front:** How do UPS, UPSS and CWS differ, and which unemployment rate does each give?
**Formula:** UR (basis) = (Unemployed on basis ÷ Labour force on basis) × 100. Bases: UPS (usual principal status: 365-day reference, principal activity); UPSS (usual principal and subsidiary: includes subsidiary activity over 365 days); CWS (current weekly status: 7-day reference, employed if worked at least 1 hour in the week, with the employment rule applied in the reference week); CDS (current daily status: day-by-day). Units: percent.
**Worked example:** Illustrative: labour force 1,000 (UPSS); unemployed 40 on UPSS → UR_UPSS = 4.0%. On CWS, the same people may be employed for an hour of work, giving UR_CWS = 3.1% (= 31/1000 × 100). The difference is definitional, not a change in the labour market.
**Learn:**
- Owner 22: UPS/UPSS best capture structural and disguised unemployment (365-day reference); CWS best captures seasonal and frictional movement (7-day reference); CDS is most sensitive to partial and under-employment (owner 22).
- Owner 22: a low CWS-based rate can conceal underemployment; name the basis before quoting.
**Trap:** A "PLFS unemployment rate" is not one number. Name the status (UPS, UPSS, CWS, CDS) every time.
**Back:** *"Name the basis before the rate: 365 days, 7 days or day-by-day."*

### GROUP — Agriculture and industry

### Flashcard F-150 — CACP cost concepts (A2, A2+FL, C2) and the 1.5× MSP rule
**Front:** How are the three CACP cost concepts built, and how does the 1.5× rule set MSP?
**Formula:** A2 = paid-out costs (seed, fertiliser, manure, pesticide, hired labour, irrigation, fuel, interest on working capital, etc.). A2+FL = A2 + imputed value of unpaid family labour. C2 = A2+FL + imputed rent on owned land + imputed interest on owned fixed capital. The 1.5× rule (cost-plus policy): MSP = 1.5 × A2+FL (for the notified crops; ✅ corrected: was 'as announced from Kharif 2018-19'. Wikipedia 'Minimum support price', fetched 2026-10-30, records the pledge in the Union Budget of 1 February 2018 that MSP would be at least 1.5 times the production cost, and notes that the cost base is not defined there; ⚠️ the A2+FL base and the current notification remain unverified).
**Worked example:** Illustrative: A2 = ₹1,000; FL = ₹300; rent and capital interest = ₹400 per quintal. A2+FL = 1,300; C2 = 1,700. MSP = 1.5 × 1,300 = ₹1,950 per quintal. Against C2, the same MSP is 1,950/1,700 = 1.147, i.e., 14.7% above C2.
**Learn:**
- Owner 12: MSP is generally benchmarked to a margin over A2+FL; farmer bodies demand C2+50% (see F-151).
- ✅ Owner 12: CACP recommends; CCEA announces. Owner 12 lists 23 notified crops (7 cereals, 5 pulses, 7 oilseeds, 4 commercial crops; verify currency). Owner 12 states the A2+FL benchmark but not the 1.5× multiplier; the 1.5× pledge is confirmed as a 2018 budget announcement (Wikipedia), while the cost base it applies to stays ⚠️ in the formula above.
- The cost base decides whether MSP looks adequate: the same MSP can be "50% above cost" against A2+FL and "below C2+50%" against C2.
**Trap:** A2, A2+FL and C2 are not interchangeable. C2 is the widest base (owner 12 trap).
**Back:** *"A2 is paid, A2+FL adds family labour, C2 adds the land and capital you own; MSP rides 1.5× A2+FL."*

### Flashcard F-151 — "C2 plus 50 per cent" (farmers' demand)
**Front:** What MSP formula do farmer bodies demand, and how does it differ from the 1.5× rule?
**Formula:** Farmers' demand: MSP = C2 × 1.5 = C2 + 0.5 × C2 (i.e., a 50% margin over the wider C2 base). Government practice: MSP = A2+FL × 1.5. Compare: 1.5 × C2 ÷ 1.5 × (A2+FL) = C2 ÷ (A2+FL) ≥ 1.
**Worked example:** Using the F-150 illustration (C2 = 1,700; A2+FL = 1,300): C2+50% = 1.5 × 1,700 = ₹2,550 per quintal; 1.5× A2+FL = ₹1,950. The gap is ₹600 per quintal.
**Learn:**
- Owner 12: the farmer-movement demand for C2+50% makes sense only once the cost base is named.
- Owner 12 limit: a C2-based MSP would raise farmer remuneration but also raise fiscal and market-distortion cost.
**Trap:** "C2+50%" is a demand, not a notified government formula. Do not state it as current policy.
**Back:** *"C2+50 asks for half again on the widest cost; the 1.5× rule takes half again on the narrower one."*

### Flashcard F-152 — Price spread (marketing margin) and farmer's share
**Front:** How much of the consumer rupee reaches the farmer?
**Formula:** Price spread (₹) = Retail (consumer) price − Farm-gate price. Price spread (%) = (Retail − Farm-gate) ÷ Retail × 100. Farmer's share = (Farm-gate ÷ Retail) × 100 = 100 − price spread %.
**Worked example:** Illustrative: farm-gate price ₹20/kg, retail price ₹60/kg. Price spread = 40 → 40/60 × 100 = 66.7%. Farmer's share = 33.3%.
**Learn:**
- Price spread captures intermediaries' margins, transport, storage and processing (value-chain logic in owners 13 and 15, outside this scope).
- Use the same unit and time window for both prices; compare farm-gate and retail for the same product and period.
**Trap:** A high price spread is not proof of exploitation. Cost of storage, processing and spoilage raises spreads legitimately.
**Back:** *"Spread: the consumer's rupee minus the farmer's rupee, over the consumer's rupee."*

### Flashcard F-153 — Farmer's income (net farm income)
**Front:** How is a farmer's income measured for the purpose of MSP and income-support debate?
**Formula:** Net farm income = Gross value of output − Paid-out costs (A2) [or − (A2+FL) if family labour is valued]. Gross value of output = Yield × Price (for each crop, summed over crops). Units: ₹ per hectare or per year.
**Worked example:** Illustrative: yield 30 quintal/ha × price ₹1,950/quintal = gross value ₹58,500/ha. A2 = ₹35,000/ha. Net income (over A2) = 58,500 − 35,000 = ₹23,500/ha.
**Learn:**
- Owner 12 and 11 use cost concepts and the cropping pattern to explain farm incomes; the owners give no all-India income figure, so do not quote one without a dated source.
- Net income depends on yield risk, price volatility and the crop mix (owner 11 "cropping pattern" logic).
**Trap:** Gross income and net income are different. An MSP increase does not raise net income if the paid-out costs rise faster.
**Back:** *"Farm income is what the crop brings in, minus what you paid out."*

### Flashcard F-154 — Cropping intensity
**Front:** How intensively is cultivated land used during a year?
**Formula:** Cropping intensity (%) = (Gross cropped area ÷ Net sown area) × 100. Units: percent (100% = each sown hectare cropped once).
**Worked example:** Illustrative: net sown area 100 ha; gross cropped area 150 ha (kharif 100 + rabi 50). Cropping intensity = 150/100 × 100 = 150%.
**Learn:**
- Owner 11: cropping intensity = gross cropped area ÷ net sown area (exact owner definition).
- Higher intensity raises marketed surplus but can worsen groundwater depletion, salinity, residue burning and nutrient imbalance (owner 11, 6A).
**Trap:** Higher cropping intensity does not mean more sustainable. Owner 11 trap.
**Back:** *"Intensity: crops per hectare per year, over the land actually sown."*

### Flashcard F-155 — Irrigation intensity (⚠️ definition variant)
**Front:** How much of the sown area is irrigated, and what is the common variant?
**Formula:** Common Indian usage: irrigated area ratio = (Net irrigated area ÷ Net sown area) × 100. Irrigation intensity in some tables = (Gross irrigated area ÷ Net irrigated area) × 100. The two are different; state the variant.
**Worked example:** Illustrative: net sown area 100 ha; net irrigated area 60 ha; gross irrigated area 80 ha. Irrigated share = 60% of net sown; irrigation intensity (variant 2) = 80/60 × 100 = 133%.
**Learn:**
- Not in the Economy owners (owner 14 is outside this scope); ⚠️ the definitions are conventional and must be checked against the Land Use Statistics or Agricultural Statistics source before quoting. No source was reachable in this pass (Wikipedia 'Cropping intensity' returned 404).
**Trap:** Irrigation intensity is not the same as cropping intensity. Irrigation intensity uses irrigated areas only.
**Back:** *"Irrigated share is land under water; irrigation intensity is water-times-crops."*

### Flashcard F-156 — Net sown area and gross cropped area identity
**Front:** How do net sown area and gross cropped area relate?
**Formula:** Net sown area (NSA) = area sown at least once in the year. Gross cropped area (GCA) = Σ area sown over all seasons = NSA + area sown more than once. Identity: GCA = NSA + Area sown more than once; GCA ≥ NSA always.
**Worked example:** Illustrative: NSA = 100 ha; area sown twice = 40 ha; GCA = 100 + 40 = 140 ha; cropping intensity = 140%.
**Learn:**
- Owner 11 (cropping systems) uses the same identity.
- Multiple cropping counts a plot once for each season it is sown.
**Trap:** GCA is not the total land area, and NSA is not the total cultivable area.
**Back:** *"Net counts each acre once; gross counts every season."*

### Flashcard F-157 — Crop yield
**Front:** How productive is land or a crop?
**Formula:** Yield (kg/ha or quintal/ha) = Total production ÷ Area harvested. Units must match (for example, quintal per hectare).
**Worked example:** Illustrative: production 3,000 quintals from 100 ha → yield = 30 quintal/ha.
**Learn:**
- Owner 11: the Green Revolution raised yields in irrigated wheat-rice belts; the gains were regionally concentrated.
- Yield is a per-area measure; production is total. An increase in area can raise production without raising yield.
**Trap:** Yield and productivity are not the same: yield is one input-output ratio, productivity may include other factors.
**Back:** *"Yield is output per hectare, not output for the nation."*

### Flashcard F-158 — Stock-to-use ratio
**Front:** How comfortable is the stock position relative to consumption?
**Formula:** Stock-to-use ratio (%) = (Ending stocks ÷ Total use) × 100, where total use = domestic consumption + exports + wastage (per the commodity balance sheet). Units: percent.
**Worked example:** Illustrative: ending stocks 40 million tonnes; total use 200 million tonnes → stock-to-use = 20%.
**Learn:**
- Owner 12: buffer stock is publicly held inventory for distribution, emergencies and stabilisation. Buffer norms guide desirable levels; actual stocks may be higher or lower (owner 12).
- Stock-to-use is a commodity-balance measure, not the same as the FCI buffer norm.
**Trap:** Buffer norm is a target; the stock-to-use ratio is an outcome. Do not swap them.
**Back:** *"Stock-to-use: what is left, over what is eaten, sold or spoilt."*

### Flashcard F-159 — Economic cost of foodgrains (food subsidy base)
**Front:** What cost base does FCI use for foodgrains, and how does the food subsidy relate?
**Formula:** Economic cost (per quintal) = Procurement price (MSP-linked) + procurement incidentals + storage and carrying costs + movement and distribution-related costs (owner 12: broader than MSP alone). Food subsidy (for the TPDS) ≈ (Economic cost − Issue price) × quantity issued (illustrative logic; the official subsidy is budgeted and accounted per Union Budget).
**Worked example:** Illustrative: MSP-linked procurement price ₹2,000/quintal; incidentals and storage ₹300; movement and distribution ₹200. Economic cost = 2,500. Issue price to beneficiary ₹100. Subsidy per quintal = 2,500 − 100 = ₹2,400.
**Learn:**
- Owner 12: economic cost is broader than MSP; it includes procurement incidentals, storage, movement, carrying and distribution-related costs.
- Owner 09: food subsidy has been historically financed through off-budget routes such as NSSF borrowing (pre-FY2020-21 example, owner 09); cite the current accounting from a dated Budget document.
**Trap:** The economic cost is not the MSP. Do not equate the two in an answer about FCI costs (owner 12 trap).
**Back:** *"Economic cost is MSP plus everything it takes to store and move the grain."*

### Flashcard F-160 — PDS leakage
**Front:** What share of entitled grain fails to reach the intended household?
**Formula:** PDS leakage (%) = [(Grain allocated − Grain reaching beneficiaries) ÷ Grain allocated] × 100. Use the same unit (tonnes) and period for both terms.
**Worked example:** Illustrative: allocated 100,000 tonnes; delivered to beneficiaries 85,000 tonnes → leakage = 15,000/100,000 × 100 = 15%.
**Learn:**
- Owner 12: end-to-end computerisation (ePoS, Aadhaar authentication, IMPDS) reduces diversion, but authentication failures can also exclude genuine beneficiaries.
- Leakage must be measured by independent survey, not only by allocation records.
**Trap:** Leakage is not the same as exclusion error. A low leakage can coexist with high exclusion (owner 12 trap).
**Back:** *"Leakage: what was allocated, minus what the family actually received."*

### Flashcard F-161 — Index of Industrial Production (IIP)
**Front:** How is industrial output measured month to month?
**Formula:** IIP_t = Σ_i (w_i × I_{i,t}) ÷ Σ_i w_i × base = Σ_i w_i × I_{i,t} (with Σ w_i normalised to 100), where I_{i,t} = output index of sector i in month t (base year = 100), and w_i = fixed base-year weight. Laspeyres-type fixed-weight index.
**Worked example:** Illustrative three-sector example: weights 0.5, 0.3, 0.2 (sum 1.0) with indices 110, 90, 100. IIP = 0.5×110 + 0.3×90 + 0.2×100 = 55 + 27 + 20 = 102.
**Learn:**
- ✅ Wikipedia 'Index of Industrial Production' (fetched 2026-10-30): Laspeyres-type fixed-weight formula with weights proportional to base-year value added; compiled and published monthly by the National Statistics Office under MoSPI; current base year stated as 2022-23 (the same page also carries a 2011-12 revision footnote, so the base label is internally inconsistent). ⚠️ The sectoral weights for mining, manufacturing and electricity are not on the page and remain unverified; check the official release before quoting.
- IIP covers mining, manufacturing and electricity; use the official release for the base year and weights.
**Trap:** IIP is a volume index of output, not a value index, and is not GDP. Do not convert IIP growth into GDP growth without a bridge.
**Back:** *"IIP: weighted output indices, base year equals one hundred."*

### Flashcard F-162 — Index of Eight Core Industries
**Front:** How is the eight-core index built and what weights does it use?
**Formula:** Index = Σ_i (w_i × I_i) ÷ Σ_i w_i, a fixed-weight (Laspeyres-type) index with base year = 100, where w_i = weight of core industry i in the index (weights sum to 100). Eight core industries: refinery products, steel, electricity, coal, crude oil, natural gas, cement, fertilisers.
**Weights and base year (⚠️ from memory; eaindustry.nic.in fetch failed with a TLS certificate error, and both Wikipedia URLs returned 404 in this pass; the listed weights sum to 100.00):** Base 2011-12 = 100, with weights refinery 28.04, steel 17.92, electricity 19.85, coal 10.33, crude oil 8.98, natural gas 6.88, cement 5.37, fertilisers 2.63 (summing to 100). Verify against the latest official base-year release before quoting; a rebasing may have occurred.
**Worked example:** Illustrative: suppose all eight sector indices are 105 except steel 110 and electricity 100: index = Σ w_i I_i ÷ 100 with the stated weights. Base case (all 105) = 105.00. Steel effect = 17.92 × (110 − 105)/100 = +0.896; electricity effect = 19.85 × (100 − 105)/100 = −0.993; index = 105.00 + 0.896 − 0.993 = 104.903 ≈ 104.90. (✅ corrected arithmetic: the earlier text omitted the electricity effect and gave about 105.)
**Learn:**
- The eight-core index is compiled and published by the Office of the Economic Adviser (DPIIT) under the Ministry of Commerce and Industry (⚠️ standard publisher; verify).
- It is a leading indicator of industrial activity and is a subset of IIP coverage (✅ Wikipedia 'Index of Industrial Production': the eight core industries make up about 40.27% of the weight of items included in the IIP).
**Trap:** Do not state the weights with confidence in an exam answer without the official source. The steel and electricity weights are the largest-moving components.
**Back:** *"Eight core: refinery, steel and power carry most of the weight."*

### Flashcard F-163 — Capacity utilisation
**Front:** What share of potential output is an industry actually producing?
**Formula:** Capacity utilisation (%) = (Actual output ÷ Potential output) × 100. Potential output is the maximum sustainable output at existing capacity. Units: percent.
**Worked example:** Illustrative: actual output 720 units per month; potential output 900 units → utilisation = 720/900 × 100 = 80%.
**Learn:**
- Owner 01 (GDP/output gap) and owner 16 (industrial policy) use capacity logic for supply-side constraints; the owners give no current utilisation value.
- High utilisation signals investment need; low utilisation signals weak demand or capacity overhang.
**Trap:** Capacity utilisation is not the output gap in GDP. It is an industry-level ratio.
**Back:** *"Utilisation: what the plant makes, over what it could make."*

### Flashcard F-164 — Incremental capital-output ratio (ICOR)
**Front:** How much investment does a unit of extra growth require?
**Formula:** ICOR = Investment rate ÷ Growth rate = (I/Y) ÷ g, where I/Y = gross investment as a share of GDP and g = GDP growth rate. Equivalent: ICOR = ΔK ÷ ΔY. Units: ratio (dimensionless).
**Worked example:** Illustrative: investment 30% of GDP; growth 6% → ICOR = 30/6 = 5. Each ₹1 of growth requires ₹5 of investment. If efficiency improves so ICOR = 4, the same investment yields more growth.
**Learn:**
- Owner 01: ICOR rises when investment efficiency falls; saving or investment effort does not guarantee growth.
- ICOR is an aggregate diagnostic, not a sector diagnosis (owner 01 limitation).
**Trap:** ICOR is not the average capital-output ratio K/Y. It is the incremental ratio.
**Back:** *"ICOR: investment over growth; a rising number means the capital is working less hard."*

### Flashcard F-165 — Capital-output ratio
**Front:** How much capital is embodied in each unit of output?
**Formula:** Average capital-output ratio = K ÷ Y (capital stock over output). Incremental (ICOR, F-164) = ΔK ÷ ΔY. Units: ratio.
**Worked example:** Illustrative: capital stock ₹600 lakh crore; GDP ₹300 lakh crore → K/Y = 2.0.
**Learn:**
- Owner 01 uses ICOR in the saving-investment-growth chain; the average K/Y is not directly observed in India's accounts and must be estimated (⚠️ method-dependent).
**Trap:** Do not use K/Y and ICOR interchangeably. Their values differ and answer different questions.
**Back:** *"Average K/Y is the stock; ICOR is the marginal stock per growth."*

### Flashcard F-166 — PLI incentive basis (incremental sales over base year)
**Front:** On what base is a Production-Linked Incentive (PLI) computed?
**Formula:** PLI incentive = Incentive rate (%) × Incremental sales (or value added) over the base year, for the eligible period, subject to a cap. Incremental sales = Current-year sales − Base-year sales. Owner 16 and 17 describe PLI as sales-linked support.
**Worked example:** Illustrative: base-year sales ₹1,000 crore; current-year sales ₹1,400 crore. Incremental sales = 400. Incentive at 10% = ₹40 crore (subject to cap).
**Learn:**
- The incentive is tied to incremental production, not to outlay or investment. Sanctioned outlay, approved application and disbursed incentive are different stages (owner 17 trap).
- ⚠️ The exact rate, base year and cap differ by scheme sector and notification; verify from the scheme guidelines (Department for Promotion of Industry and Internal Trade). No source was reachable in this pass (Wikipedia 'Production-linked incentive scheme' returned 404 in two attempts).
**Trap:** Sanctioned outlay is not the amount paid out. The formula above applies only to the incremental-sales component.
**Back:** *"PLI pays on the extra you sell over last year, not on the plant you build."*

### Flashcard F-167 — MSME classification thresholds (1 April 2025)
**Front:** What are the current investment and turnover thresholds for micro, small and medium enterprises?
**Formula:** Classification: micro if investment in plant and machinery or equipment ≤ ₹2.5 crore AND turnover ≤ ₹10 crore; small if investment ≤ ₹25 crore AND turnover ≤ ₹100 crore; medium if investment ≤ ₹125 crore AND turnover ≤ ₹500 crore. Test: the enterprise must satisfy both limits to fall in a class (the higher of the two tests determines the class in the MSMED framework).
**Worked example:** Illustrative firm: investment ₹20 crore, turnover ₹80 crore → small (investment ≤ 25 and turnover ≤ 100). If turnover were ₹120 crore, it would move to medium (≤ 500 turnover and ≤ 125 investment).
**Learn:**
- Owner 17 (cross-owner, not in the assigned scope): thresholds revised under the notification S.O. 1364(E) dated 21 March 2025, effective 1 April 2025 (✅ owner 17, which cites the notification; the msme.gov.in fetch returned 403 in this pass). The 2020 limits (micro ₹1 crore/₹5 crore; small ₹10 crore/₹50 crore; medium ₹50 crore/₹250 crore) are superseded.
- Owner 17 trap: do not cite 2020 limits as current.
**Trap:** Using the wrong vintage of thresholds is the main error. Cite the notification and date.
**Back:** *"MSME: two tests, one class, dated 1 April 2025."*

### GROUP — Micro basics

### Flashcard F-168 — Price elasticity of demand (PED)
**Front:** How responsive is quantity demanded to a change in its own price?
**Formula:** PED (ε_d) = (% change in quantity demanded) ÷ (% change in price). Midpoint (arc) form: ε_d = [(Q2 − Q1)/((Q2 + Q1)/2)] ÷ [(P2 − P1)/((P2 + P1)/2)]. Reported as absolute value |ε_d|. Units: dimensionless.
**Worked example:** Illustrative: price rises from ₹100 to ₹120 (midpoint 110, change 20 → 18.2%); quantity falls from 50 to 40 (midpoint 45, change −10 → −22.2%). ε_d = −22.2/18.2 ≈ −1.22 → |ε_d| ≈ 1.22 (elastic).
**Learn:**
- |ε_d| > 1 elastic (total revenue falls when price rises); |ε_d| < 1 inelastic (revenue rises with price); = 1 unit elastic.
- Total revenue effect: TR = P × Q, and ΔTR ≈ Q(1 − |ε_d|)ΔP.
**Trap:** Elasticity is a ratio of percentage changes, not a slope. Do not use absolute changes.
**Back:** *"Elastic means the buyer walks away; inelastic means the buyer pays."*

### Flashcard F-169 — Income elasticity of demand (YED)
**Front:** How does demand respond to a change in income?
**Formula:** YED (ε_y) = (% change in quantity demanded) ÷ (% change in income). Sign: ε_y > 0 normal good; ε_y < 0 inferior good; ε_y > 1 luxury; 0 < ε_y < 1 necessity.
**Worked example:** Illustrative: income rises 10%; demand for a product rises 15% → ε_y = 1.5 (luxury, normal good).
**Learn:**
- Owner 03 (must-know): demand for an inferior good can rise when income falls; demand depends on income, tastes, expectations and substitute prices.
**Trap:** A "normal" good is not always a "necessity". The classification uses the value of ε_y.
**Back:** *"Income elasticity: above one is a luxury, below one is a need, negative is inferior."*

### Flashcard F-170 — Cross elasticity of demand (XED)
**Front:** How does demand for good X respond to a change in the price of another good Y?
**Formula:** XED (ε_xy) = (% change in quantity demanded of X) ÷ (% change in price of Y). Sign: ε_xy > 0 substitutes; ε_xy < 0 complements; = 0 unrelated.
**Worked example:** Illustrative: price of tea rises 10%; demand for coffee rises 8% → ε_xy = +0.8 (substitutes).
**Learn:**
- Owner 03 (must-know): consumer demand depends on prices of substitutes and complements.
**Trap:** Sign matters: a positive XED means substitutes, not that the goods are alike.
**Back:** *"Cross elasticity: a rival's price rises, my demand climbs means substitutes."*

### Flashcard F-171 — Price elasticity of supply (PES)
**Front:** How responsive is quantity supplied to a change in its own price?
**Formula:** PES (ε_s) = (% change in quantity supplied) ÷ (% change in price). Typically positive. Units: dimensionless.
**Worked example:** Illustrative: price rises 10%; supply rises 15% → ε_s = 1.5 (elastic supply).
**Learn:**
- Short-run supply is usually less elastic than long-run supply, because capacity and inputs adjust with lags (standard result).
- For agricultural supply, the crop cycle and procurement price signal shape response (owner 11, 12 logic).
**Trap:** Supply elasticity is not demand elasticity. Keep the sides of the market separate.
**Back:** *"Supply elasticity: how fast the field and factory answer the price."*

### Flashcard F-172 — Consumer surplus and producer surplus
**Front:** How is the welfare gain to buyers and sellers measured at market equilibrium?
**Formula:** Consumer surplus (CS) = ½ × (P_max − P*) × Q* (linear demand, P_max = choke price, P* = equilibrium price, Q* = equilibrium quantity). Producer surplus (PS) = ½ × (P* − P_min) × Q* (linear supply, P_min = supply intercept). Total surplus = CS + PS.
**Worked example:** Illustrative: P_max = 100, P* = 60, P_min = 20, Q* = 40 units. CS = ½ × (100 − 60) × 40 = ₹800. PS = ½ × (60 − 20) × 40 = ₹800. Total = ₹1,600.
**Learn:**
- A price ceiling below P* reduces both surpluses and creates a deadweight loss; a subsidy or MSP above P* transfers surplus and can create excess supply (standard welfare logic; owner 12 uses it qualitatively).
**Trap:** Surplus is a welfare measure, not a cash revenue. Do not add surpluses to GDP.
**Back:** *"Consumer surplus is what buyers save; producer surplus is what sellers keep above cost."*

### Flashcard F-173 — Marginal cost, marginal revenue and profit-maximising condition
**Front:** At what output does a firm maximise profit?
**Formula:** MR = ΔTR ÷ ΔQ; MC = ΔTC ÷ ΔQ. Profit-maximising condition: MR = MC (with MC rising and the second-order condition satisfied). For a price-taker, MR = P. For a price-setter, MR = P(1 − 1/|ε_d|).
**Worked example:** Illustrative: P = ₹50, MC = 2Q + 10 (₹). Price-taker: MR = 50 → 2Q + 10 = 50 → Q = 20. Profit at Q = 20 is computed in F-174.
**Learn:**
- For a monopolist, the MR formula above shows why MR < P when demand is elastic but finite.
- Owner 16 and 20 use the same profit logic at the firm level (qualitative).
**Trap:** MR = MC is the condition, not MR = P, except for a price-taker.
**Back:** *"Produce until the next unit's extra revenue equals its extra cost."*

### Flashcard F-174 — Profit, total revenue and total cost
**Front:** How is economic or accounting profit computed?
**Formula:** TR = P × Q. TC = FC + VC. Profit (π) = TR − TC = (P − ATC) × Q, where ATC = TC ÷ Q. Breakeven: P = ATC; shutdown: P < AVC (short run).
**Worked example:** Illustrative: P = ₹50, Q = 20, TC = FC 200 + VC 600 = 800. TR = 1,000. π = 1,000 − 800 = ₹200. ATC = 800/20 = ₹40 → (50 − 40) × 20 = 200 ✓.
**Learn:**
- Accounting profit excludes imputed opportunity costs; economic profit includes them (standard distinction).
**Trap:** Do not confuse profit with revenue or with markup per unit.
**Back:** *"Profit: revenue minus all costs, including the costs you did not write down."*

### Flashcard F-175 — GDP at purchasing power parity (PPP)
**Front:** How is GDP converted into international dollars using PPP?
**Formula:** GDP (PPP) = GDP (domestic currency) ÷ PPP conversion factor, where the conversion factor = domestic currency units per international dollar (price-level ratio: P_domestic ÷ P_US for a common basket). Equivalent: GDP (PPP, US$) = GDP (local) ÷ (local currency per int'l $).
**Worked example:** Illustrative (not India's official figure): GDP ₹300 trillion; PPP conversion factor 20 ₹ per international dollar → GDP (PPP, international $) = 300 ÷ 20 = $15 trillion.
**Learn:**
- Owner 09/10/20/23 refer to PPP only conceptually. Use IMF or World Bank series with the year.
- PPP GDP is larger than market-rate GDP for developing economies because local non-traded services are cheaper.
**Trap:** The PPP conversion factor is not the market exchange rate. Do not mix them in one calculation.
**Back:** *"PPP GDP: local output divided by the local price of an international dollar."*

### Flashcard F-176 — Comparative advantage and opportunity cost
**Front:** Which country has the comparative advantage in which good?
**Formula:** Opportunity cost of good X in terms of Y = (units of Y forgone) ÷ (units of X produced). A country has comparative advantage in X if its opportunity cost of X is lower than the other country's.
**Worked example:** Illustrative: India can produce 10 units of wheat or 20 units of cloth (hours fixed). Opportunity cost of 1 wheat = 2 cloth. Partner: 1 wheat = 4 cloth. India has comparative advantage in wheat (lower opportunity cost, 2 < 4).
**Learn:**
- Comparative advantage is about relative opportunity cost, not absolute productivity.
- Owner 20 Mains angle: trade gains depend on domestic capability and adjustment support, not on theory alone.
**Trap:** Absolute advantage is not comparative advantage. A country can be better at both goods and still gain from trade.
**Back:** *"Comparative advantage: give up the least to make it."*

### Flashcard F-177 — Herfindahl–Hirschman Index (HHI)
**Front:** How concentrated is a market, using firms' shares?
**Formula:** HHI = Σ_i s_i², where s_i = market share of firm i in percent (0 to 100). Range: 0 (atomistic) to 10,000 (single firm). Equal shares: HHI = 10,000 ÷ N for N identical firms.
**Worked example:** Illustrative market: shares 40%, 30%, 20%, 10%. HHI = 40² + 30² + 20² + 10² = 1600 + 900 + 400 + 100 = 3,000.
**Learn:**
- ✅ Wikipedia 'Herfindahl–Hirschman index' (fetched 2026-10-30): HHI is the sum of squared percentage shares (0 to 10,000 on the percent scale; equal shares give 10,000 ÷ N). Thresholds cited there from the US DOJ 2010 Horizontal Merger Guidelines: below 1,500 unconcentrated; 1,500 to 2,500 moderately concentrated; above 2,500 highly concentrated; a change of more than 100 generally provokes scrutiny. The Gini coefficient of market shares is an alternative concentration measure (not separately verified in this build).
- Thresholds are jurisdiction- and vintage-specific; the 1,000/1,800 cut-offs of later US guidelines are not on the fetched page and remain ⚠️ unverified. Cite the authority and year.
**Trap:** HHI uses squared shares, so it gives more weight to large firms. Do not compute with shares as fractions unless the 10,000 scale is changed.
**Back:** *"HHI: square each firm's share and add; ten thousand means one firm."*

## B. IMPORTANT TOPICS — Macro, Money, Banking, Markets, Fiscal and External

> Scope: Economy owners basic/advanced 01–10, 19–21 and 26 (plus cross-owner references where cited). Owner facts carry their as-of date. ⚠️ = standard economics/UPSC knowledge not verified against a repository owner, or a time-varying value to re-check before use. Figures from Survey 2025-26 are Jan-2026-vintage estimates unless stated.

### GROUP — National income, growth and welfare measurement

### Flashcard T-001 — GDP, GVA, GNP and NDP: the core aggregates
**Front:** How do GDP, GVA, GNP and NDP differ, and which adjustment converts one into another?
**Definition (learn):** GDP is the market value of final goods and services produced within the domestic territory in a period. GVA is output minus intermediate consumption, measured at basic prices. GNP is GDP adjusted for net factor income from abroad (NFIA). NDP is GDP after deducting consumption of fixed capital (depreciation).
**Breakdown:**
- GVA at basic prices + net product taxes (product taxes minus product subsidies) = GDP at market prices.
- GNP = GDP + NFIA; NNP = GNP minus depreciation.
- Domestic = location of production; national = income of normal residents.
- Three methods (production, income, expenditure) should converge: GDP = C + I + G + (X − M).
- Nominal GDP uses current prices; real GDP uses base-year prices; GDP deflator = (Nominal GDP ÷ Real GDP) × 100.
- Intangible spending on R&D, software/databases, mineral exploration and artistic originals is treated as capital formation under SNA rules; advertising, brand building and staff training are not capitalised ⚠️ see owner.
**Cases / Committees / Schemes / Data:** Survey 2025-26 (Jan-2026 vintage): FY26 First Advance Estimate real GDP growth 7.4%, real GVA 7.3%, PFCE 61.5% of GDP. [basic/01 §6A, §9; basic/01 §6A intangible limit]
**Trap:** GNP exceeds GDP only when NFIA is positive; GDP can exceed GNP when NFIA is negative. Pension payments and transfers are not GDP. Resale of an existing asset adds only the brokerage or service value. Higher nominal GDP can be pure inflation.
**Mains hook:** Why GDP growth is necessary but not sufficient for development; use GDP and GVA together, because product-tax changes can make the two diverge. Verdict: output is a measure of production, not of distribution, unpaid work or ecological cost.
**Back:** *"Territory makes GDP, residence makes GNP, and Net strips out the wear and tear."*

### Flashcard T-002 — New GDP series (2022-23 base) and the 2015 base revision
**Front:** What changed in India's national-accounts base year, and when can old and new growth rates be compared?
**Definition (learn):** The base year is the reference year whose prices are used to construct constant-price (real) estimates. A base revision changes weights, sources and methods.
**Breakdown:**
- The 2015 revision moved India from the 2004-05 base to 2011-12 and made greater use of corporate administrative data; sector weights and methods changed ⚠️ (2004-05 base is standard knowledge).
- MoSPI released a new GDP series with base year **2022-23** on **27 February 2026**, replacing 2011-12, with annual and quarterly estimates from 2022-23.
- A comparable back-series was still pending at the owner's cutoff of 19 July 2026. Do not splice old and new growth rates.
- Estimates move through advance estimates (FAE, SAE), provisional and final stages; always state the vintage.
**Cases / Committees / Schemes / Data:** MoSPI press note, 27 Feb 2026 (cited in owner). [basic/01 §9; advanced/01 §10]
**Trap:** A base-year change is a measurement update, not a real change in output. Quoting a 2011-12-series growth figure next to a 2022-23-series figure without an official bridge is an invalid comparison.
**Mains hook:** Base revisions improve relevance and coverage but disrupt historical comparison; the qualified stance is to adopt the new series and label every break until an official back-series exists.
**Back:** *"No official bridge, no splice."*

### Flashcard T-003 — Potential GDP, output gap and ICOR
**Front:** How do potential output, the output gap and ICOR tell you whether growth is demand-constrained or capacity-constrained?
**Definition (learn):** Potential growth is the sustainable output growth consistent with labour, capital, productivity and macro stability. The output gap is actual minus potential output; a negative gap signals weak demand. ICOR (incremental capital-output ratio) is the investment needed per unit of extra output; a rising ICOR means falling investment efficiency.
**Breakdown:**
- A negative output gap supports demand repair; a capacity constraint needs supply-side investment and productivity.
- High saving or investment does not automatically raise growth; ICOR shows whether capital is productive.
- Potential output is estimated, not observed, and is revised in real time.
- Survey 2025-26 (Jan-2026 vintage): FY27 real GDP projection 6.8–7.2%; medium-term potential growth around 7%.
**Cases / Committees / Schemes / Data:** 2020 GS-III PYQ on potential GDP determinants and India's output gap (routed to basic/01). [basic/01 §5, §9; basic/26 §8]
**Trap:** A level of output is not a growth rate. A projection is conditional and period-specific, not a permanent trend.
**Mains hook:** Growth should be judged against sustainable capacity; a positive gap with high inflation calls for supply repair, a negative gap calls for demand support.
**Back:** *"The gap says demand, ICOR says efficiency."*

### Flashcard T-004 — HDI and IHDI: average achievement versus inequality-adjusted achievement
**Front:** What do HDI and IHDI measure, and why is IHDI a better test of inclusive growth?
**Definition (learn):** HDI is the UNDP composite of health (life expectancy), education and standard of living (GNI per capita). IHDI is HDI discounted for inequality within each of its three dimensions.
**Breakdown:**
- HDI combines the three dimension indices by geometric mean (owner states "geometric").
- IHDI equals HDI when there is no inequality and falls below HDI as inequality rises.
- HDI records average achievement; IHDI reveals how unequally that achievement is spread.
- Publisher: UNDP Human Development Report office; HDI does not measure political freedom.
- India's current HDI rank and score are not recorded in the owners ⚠️; take them only from the latest UNDP release with its year.
**Cases / Committees / Schemes / Data:** 2025 GS-III PYQ (10 marks): distinguish HDI and IHDI and explain why IHDI better reflects inclusive growth. [basic/02 §9; advanced/02]
**Trap:** HDI and IHDI do not measure identical outcomes; a small HDI-to-IHDI gap means low inequality, not high human development.
**Mains hook:** Use IHDI to show that growth in averages can hide unequal health, schooling and income; conclude by pairing IHDI with MPI and sector data because composites depend on chosen weights.
**Back:** *"HDI counts the average; IHDI checks how fairly the average is shared."*

### Flashcard T-005 — Multidimensional Poverty Index (UNDP-OPHI global; NITI Aayog national)
**Front:** How is MPI built, and how do incidence (H) and intensity (A) relate?
**Definition (learn):** MPI = H × A. A household is multidimensionally poor if it is deprived in at least one-third of the weighted indicators. H (headcount ratio) is the share of population that is poor; A (intensity) is the average share of weighted deprivations among the poor.
**Breakdown:**
- Three dimensions: health, education and living standards.
- Standard indicators include nutrition, child mortality, years of schooling, school attendance, cooking fuel, sanitation, drinking water, electricity, housing and assets. [basic/02 §6]
- Global MPI: UNDP and Oxford Poverty and Human Development Initiative (OPHI). NITI Aayog publishes India's national MPI.
- H and A can move in different directions, so one headline number hides composition.
**Cases / Committees / Schemes / Data:** NITI national MPI: 55.3% (2005-06), 14.96% (2019-21), 11.28% (2022-23) [basic/02 §8, Survey 2025-26]. 2020 GS-II PYQ on incidence and intensity against income-based measurement; 2026 Prelims PYQ on MPI methodology (key provisional, not inferred).
**Trap:** MPI is not an income-poverty line; it does not price deprivation in rupees and cannot replace income-poverty analysis when a cash transfer must be sized.
**Mains hook:** Income poverty answers how many are poor; MPI answers how deprived the poor are; a complete answer uses both and checks dimension-wise decomposition.
**Back:** *"H counts the poor; A measures how deep their poverty runs."*

### Flashcard T-006 — PPP GDP versus market-exchange-rate GDP
**Front:** Why can India's rank differ on PPP and market-exchange-rate GDP, and which basis answers which question?
**Definition (learn):** Purchasing power parity (PPP) converts output using a common basket of goods and services price levels. Market-exchange-rate conversion uses the prevailing currency rate.
**Breakdown:**
- PPP suits living-standard and real-purchasing-power comparisons across countries.
- Market-exchange-rate GDP suits external-trade, debt and market-size comparisons.
- The same production produces two rankings when price levels differ.
- PPP conversion factors come from international price surveys (World Bank International Comparison Program) that are periodically rebased, so always state the reference year.
- Owner says India is "regularly cited" among the largest economies on PPP; no exact rank is recorded in the owner (✅ corrected/added: Wikipedia 'Economy of India', as of October 2026, lists India as 3rd by PPP (2026) and 6th by nominal GDP (2026); the ranks are time-varying, so quote them with the date).
**Cases / Committees / Schemes / Data:** 2019 Prelims PYQ on PPP and India's world economy size (key unavailable locally). [basic/01 §6A, §9]
**Trap:** PPP and nominal rankings are not always identical. A PPP-based GDP is not a measure of real growth.
**Mains hook:** Distinguish the two bases explicitly before quoting any rank; use PPP for welfare and nominal GDP for external-sector and fiscal ratios.
**Back:** *"Basket for living standards, exchange rate for trade and debt."*

### GROUP — Inflation, price indices and business cycles

### Flashcard T-007 — The CPI family: headline, core, combined, rural and urban (MoSPI) and CPI-IW/AL/RL (Labour Bureau)
**Front:** Which CPI series exist, who publishes them, and which one anchors monetary policy?
**Definition (learn):** CPI is a retail price index for a representative consumer basket that includes services. Headline CPI includes food and fuel; core inflation conventionally excludes them.
**Breakdown:**
- MoSPI publishes the all-India CPI (combined, rural, urban) ✅ owner names the CPI; series splits (rural/urban) ⚠️ verify in MoSPI metadata.
- From January 2026 MoSPI publishes CPI with base 2024=100, replacing 2012=100 for current releases.
- RBI's inflation target is set on headline CPI, not WPI or the GDP deflator.
- CPI-IW (industrial workers), CPI-AL (agricultural labourers) and CPI-RL (rural labourers) are compiled by the Labour Bureau under the Ministry of Labour and Employment ⚠️; they drive wage and dearness-allowance indexation (owner cites CPI-IW DA indexation).
- Base years of the Labour Bureau series ⚠️ not recorded in the owners; verify before quoting.
**Cases / Committees / Schemes / Data:** Survey 2025-26: headline CPI averaged 1.7% in Apr–Dec FY26 (old 2012=100 series); core inflation 4.62% in Dec 2025 (Survey, with a major precious-metals contribution). [basic/03 §8]
**Trap:** Do not join index levels across a base break without an official link. A basket revision is not a price shock. CPI-IW is not the national anchor.
**Mains hook:** Inflation is distributional; indexation protects organised workers more than informal workers. Use headline versus core to separate supply shocks from demand.
**Back:** *"The household basket sets the policy anchor; the labour indices set the pay."*

### Flashcard T-008 — WPI and PPI (Office of the Economic Adviser, DPIIT)
**Front:** How do WPI and the new PPI differ from CPI, and what is the transition plan?
**Definition (learn):** WPI is a wholesale goods price index that excludes services; it is compiled by the Office of the Economic Adviser, DPIIT. PPI measures producer prices: output PPI tracks prices received, input PPI tracks prices paid for inputs, and service PPIs cover selected producer services.
**Breakdown:**
- WPI moved to base 2022-23 for the May 2026 release onward, replacing 2011-12.
- PPI 2022-23 framework launched June 2026, running alongside WPI for a planned five-year transition before PPI replaces WPI.
- PPI does not replace CPI; headline CPI remains the RBI inflation anchor under the 2026-31 flexible inflation-targeting framework (owner statement).
- WPI is a poor cost-of-living guide because it excludes services.
**Cases / Committees / Schemes / Data:** Owner dates: WPI 2022-23 (May 2026 release), PPI launch June 2026. [basic/03 §8; advanced/03 §9]
**Trap:** "RBI introduced PPI to replace CPI" is false; DPIIT's OEA introduced PPI to replace WPI gradually.
**Mains hook:** Producer-price signals (WPI/PPI) and household-price signals (CPI) diverge; answer by stating which index serves which decision.
**Back:** *"WPI weighs the wholesale goods; PPI splits the price received from the price paid."*

### Flashcard T-009 — Inflation types: demand-pull, cost-push, base effect, disinflation, deflation and stagflation
**Front:** How do you classify an inflation episode before choosing a policy response?
**Definition (learn):** Demand-pull inflation arises from excess aggregate demand. Cost-push inflation arises from rising input costs or supply constraints. Disinflation is a fall in the inflation rate while prices still rise. Deflation is a sustained fall in the general price level. Stagflation is weak growth or unemployment combined with inflation.
**Breakdown:**
- Diagnose by source, breadth, persistence and expectations.
- A single commodity price spike is not inflation until it becomes broad and persistent.
- Second-round effects run through wages, margins and expectations.
- A base effect is arithmetic (comparison with an unusually high or low prior base), not a new shock.
- Monetary policy works on demand, credit and expectations; it cannot repair crop failure or logistics.
**Cases / Committees / Schemes / Data:** 2020 lockdown logistics shock; 2021-22 global commodity surge (owner examples). [basic/03 §5]
**Trap:** Disinflation means prices rising more slowly, not falling. A negative output gap does not guarantee low headline inflation when supply shocks dominate.
**Mains hook:** 2024 GS-III PYQ on causes of persistent food inflation and the limits of RBI policy. Answer: separate supply repair, fiscal action and expectation management.
**Back:** *"Pull is demand, push is cost; disinflation slows the rise, deflation is the fall."*

### Flashcard T-010 — Business cycle phases and the V-shaped versus K-shaped debate
**Front:** What are the stylised business-cycle phases, and how do you test a claimed recovery?
**Definition (learn):** The stylised cycle runs recovery → expansion → peak → slowdown or recession → trough. A recovery is V-shaped when a sharp fall is followed by a sharp rebound, and K-shaped when sectors or groups diverge.
**Breakdown:**
- FY21 quarterly real GDP path (owner): −23.9% (Q1), −7.5% (Q2), +0.5% (Q3), +1.6% (Q4).
- Provisional full-year FY21 contraction was 7.3% (NSO, May 2021); revised to 6.6% (NSO, January 2022) with fuller data.
- The low Q1 base inflated later year-on-year growth comparisons (base effect).
- Employment and informality evidence showed slower recovery for salaried, women and young workers; this is the K-shaped counter-evidence.
- Business cycles can be demand-led, financial-cycle-led, inventory-led or supply-led, and each calls for a different response [advanced/03 §3].
**Cases / Committees / Schemes / Data:** 2021 GS-III PYQ "Do you agree that India's economic recovery after COVID-19 was V-shaped?" (15 marks). [basic/26 §5, §9]
**Trap:** A V-shaped aggregate path does not mean every sector or worker recovered equally. Quote the FY21 contraction with its estimate vintage, not as a single fixed number.
**Mains hook:** Pair the GDP path and base-effect logic with the employment (K-shaped) evidence and sector unevenness, then give a qualified agree-or-disagree verdict.
**Back:** *"A V can hide a K: check the aggregate path against jobs before you clap."*

### GROUP — RBI, monetary policy and liquidity management

### Flashcard T-011 — RBI: legal status, functions and independence
**Front:** Is RBI a constitutional or statutory body, who appoints the Governor, and what are its core functions?
**Definition (learn):** RBI is a statutory body under the Reserve Bank of India Act, 1934; it is not a constitutional authority. The Governor is appointed by the Central Government.
**Breakdown:**
- Functions: monetary authority, currency issuer (currency notes are RBI liabilities, not income), banker to government and to banks, reserve manager, payment-system regulator and lender of last resort within statutory mandates. [basic/04 §6]
- RBI regulates scheduled commercial banks, the banking functions of cooperative banks and (under scale-based regulation) NBFCs. [basic/05 §4]
- Operational independence on monetary policy operates inside the statutory framework; the Central Government can issue directions in public interest under RBI Act s.7 ⚠️ (verify section wording; not confirmed in this pass).
- RBI's Financial Markets Operations Department runs liquidity operations and OMOs. [basic/04 §4]
**Cases / Committees / Schemes / Data:** 2021 Prelims PYQ on the Governor's appointment and RBI's statutory-not-constitutional status (key unavailable locally). 2025 Prelims PYQ on RBI's income sources (government securities and foreign-currency operations). [basic/04 §9]
**Trap:** RBI is not a constitutional body. Interest on government securities and foreign-currency assets is RBI income; the currency notes it issues are liabilities, not income.
**Mains hook:** Operational autonomy versus accountability: rule-based inflation targeting plus statutory checks is the defensible design; the verdict should name the accountability mechanisms.
**Back:** *"Statute, not Constitution: RBI runs money under its own Act."*

### Flashcard T-012 — Monetary Policy Committee: composition, decision rule and statutory basis
**Front:** Who decides the policy repo rate, how is the MPC composed, and what gives it legal force?
**Definition (learn):** The Monetary Policy Committee (MPC) is a six-member body that decides the policy repo rate. Its statutory basis is the RBI Act amendment of 2016 (✅ Wikipedia, 'Monetary Policy Committee (India)': the RBI Act, 1934 was amended by the Finance Act 2016 to constitute the MPC; ✅ Wikipedia, 'Reserve Bank of India') ⚠️ (section numbers still to verify).
**Breakdown:**
- Six members: RBI Governor (chair), Deputy Governor in charge of monetary policy, one RBI officer nominated by the Central Board, and three external members appointed by the Central Government. [basic/04 §4]
- Decisions are taken by majority vote; the Governor holds a casting vote (✅ Wikipedia, 'Reserve Bank of India': "the vote of the RBI governor is decisive" on ties).
- The MPC targets headline CPI; the inflation target itself is set by Government in consultation with RBI under the 2015 Monetary Policy Framework Agreement ⚠️.
- MPC came into force on 27 June 2016 (✅ corrected: was "began operation in October 2016"; Wikipedia 'Monetary Policy Committee (India)' gives the in-force date; the first-meeting month is not verified in this pass ⚠️).
**Cases / Committees / Schemes / Data:** The 2016 adoption of the MPC and flexible inflation targeting made the repo decision central to published rationale. [basic/04 §5; basic/03 §5]
**Trap:** The MPC decides the repo rate; it does not decide the CPI target. WACR is an operating target, not the policy rate.
**Mains hook:** Rule-based, collectively taken decisions reduce discretion but cannot neutralise supply shocks; this is the core of the answer on whether MPC design improves credibility.
**Back:** *"Six votes set the repo; three of them come from outside the RBI."*

### Flashcard T-013 — Flexible inflation targeting: 4% ± 2 on headline CPI
**Front:** What is India's inflation target, what does the band mean, and what is the nominal anchor?
**Definition (learn):** Flexible inflation targeting (FIT) sets a CPI inflation target with a tolerance band; the framework value cited for India is 4% with ±2 percentage points (2% to 6%) (✅ Wikipedia 'Monetary Policy Committee (India)': "maintain 4% annual inflation until 31 March 2026 with an upper tolerance of 6%", lower tolerance 2%), while the MPC also weighs growth. The value that applies for 2026-31 has NOT been verified in this pass (no RBI notification retrieved; the Wikipedia mandate runs only to 31 March 2026 and gives no 2026-31 figure) ⚠️ — confirm from the dated notification before quoting.
**Breakdown:**
- Nominal anchor: headline CPI, not WPI, PPI or the GDP deflator. [basic/04 §4; basic/03 §6]
- The band is a tolerance range around the target, not the target itself.
- Owner notes that RBI continues to target headline CPI under the **2026-31** FIT framework; the 2026-31 target numbers are not recorded in the owners ⚠️ verify the current notification before quoting.
- The framework addresses headline inflation; food and fuel shocks can push CPI outside the band without a monetary failure.
**Cases / Committees / Schemes / Data:** RBI FY26 inflation projection revised from 2.6% to 2.0% in December 2025 (Survey). [basic/03 §8]
**Trap:** The target is 4% and the band is ±2; a 6% print is inside the band, a 6.5% print is not. Repo rate is the instrument, not the target.
**Mains hook:** Diagnose the inflation source first; monetary tightening fits demand-led inflation, while food and logistics shocks need supply-side and fiscal action.
**Back:** *"Four is the aim, two is the band, headline CPI is the yardstick."*

### Flashcard T-014 — Monetary-framework committees: Hilton-Young, Tarapore and Urjit Patel
**Front:** Which committees shaped India's currency, capital-account and inflation-targeting frameworks?
**Definition (learn):** Committees are advisory bodies whose recommendations are implemented in phases; none is self-executing.
**Breakdown:**
- Hilton-Young Commission: examined colonial currency and central-banking reform, leading to the creation of RBI (✅ corrected/confirmed: the RBI was set up on the recommendations of the 1926 Royal Commission on Indian Currency and Finance, also called the Hilton Young Commission; Wikipedia 'Reserve Bank of India'; RBI established 1 April 1935 ✅).
- Tarapore Committee: on capital-account convertibility (owner names RBI-linked Tarapore committee; the 1997 report ⚠️ verify year; Wikipedia 'Tarapore Committee' returned 404, so unverified).
- Urjit Patel Committee (2014): expert committee to revise and strengthen the monetary policy framework; it is generally credited with recommending CPI-based inflation targeting with a 4% ±2 band and a monetary policy committee ⚠️ (softened: not in owners; Wikipedia 'Urjit Patel' does not mention the committee, so the report title and recommendation list are unverified).
- 2026 Prelims PYQ on Indian financial-sector reform committees and their institutional sponsors (provisional key, answer not inferred). [basic/04 §9]
**Cases / Committees / Schemes / Data:** Owner-listed institution-committee pairs: Hilton-Young with currency and central-banking reform; Narasimham with banking reform; Tarapore with capital-account convertibility. [basic/04 §6]
**Trap:** Tarapore is about capital-account convertibility, not inflation targets; Urjit Patel is about the monetary framework, not bank governance.
**Mains hook:** Trace the evolution from discretionary to rule-based monetary policy and show which committee each step traces to.
**Back:** *"Tarapore opens the capital door; Patel points the policy at prices."*

### Flashcard T-015 — Repo, reverse repo, SDF and MSF: the LAF corridor
**Front:** How do repo, reverse repo, the Standing Deposit Facility and the Marginal Standing Facility set the policy corridor?
**Definition (learn):** Repo is RBI lending to banks against collateral securities, which injects liquidity. Reverse repo is RBI borrowing from banks against securities, which absorbs liquidity. The Standing Deposit Facility (SDF) is an uncollateralised facility for absorbing surplus liquidity. The Marginal Standing Facility (MSF) is an overnight emergency borrowing window for scheduled commercial banks against eligible securities.
**Breakdown:**
- The Liquidity Adjustment Facility (LAF) corridor runs from the SDF (floor) to the MSF (ceiling), with the repo rate in between.
- SDF was introduced in 2022 and gives RBI a collateral-free absorption tool. [basic/04 §5]
- Operating target is WACR, aligned to the corridor through LAF operations. [basic/04 §2]
- Specific spreads of SDF and MSF relative to repo have been revised; verify the current spread in the latest RBI notification ⚠️ (not confirmed in this pass).
- NBFCs do not enjoy routine LAF access just because scheduled banks do. [basic/05 §6]
**Cases / Committees / Schemes / Data:** 2024 Prelims PYQ on whether NBFCs have direct LAF access (rejected the broad claim). [basic/04 §7, basic/05 §9]
**Trap:** Repo is collateralised, OMO is an outright purchase or sale; a liquidity injection is not a rate cut; MSF is not available to every institution.
**Mains hook:** Separate the policy-rate signal (repo) from liquidity implementation (corridor and WACR) before judging transmission.
**Back:** *"The floor takes in, the ceiling lends out, and WACR sits between."*

### Flashcard T-016 — Cash Reserve Ratio and Statutory Liquidity Ratio
**Front:** How do CRR and SLR differ in form, holder and effect on bank lending?
**Definition (learn):** CRR is the share of net demand and time liabilities (NDTL) that banks must hold as cash with RBI. SLR is the share of NDTL that banks must hold in approved liquid assets (government securities, cash, gold) (✅ Wikipedia 'Statutory liquidity ratio': cash, gold reserves, government bonds and other approved securities, as a percentage of total demand and time liabilities).
**Breakdown:**
- CRR affects lendable resources broadly; it is blunt and changes affect all banks at once. [basic/04 §6A]
- Statutory range: the CRR band is commonly cited as 3% to 20% of NDTL under RBI Act s.42 ⚠️ (not confirmed: Wikipedia 'Cash reserve ratio' gives no statutory band or section). The SLR maximum of 40% is ✅ confirmed (Wikipedia 'Statutory liquidity ratio': "The maximum limit of SLR is 40% and minimum limit of SLR is 0"; the 20.75% floor was removed in January 2017), but the Banking Regulation Act s.24 citation is still ⚠️. Verify the current Act text and prescribed ratios before quoting.
- SLR ties bank portfolios to government securities, creating captive demand for sovereign debt ⚠️.
- Survey 2025-26 links CRR changes, repo easing and OMOs with improved transmission. [basic/04 §8]
**Cases / Committees / Schemes / Data:** Pandemic-phase CRR cuts paired with repo cuts and OMO support (owner example). [basic/04 §5]
**Trap:** CRR is not SLR. CRR is cash parked with RBI; SLR is securities held by the bank. Repeated CRR use strains intermediation more than corridor operations.
**Mains hook:** Reserve requirements are powerful but blunt; a verdict should weigh their cost to lending against their precision.
**Back:** *"CRR is cash parked with RBI; SLR is securities parked with government."*

### Flashcard T-017 — Open Market Operations, Market Stabilisation Scheme, and variable-rate operations
**Front:** How do OMOs, the MSS and variable-rate repo and reverse-repo operations change liquidity?
**Definition (learn):** OMO is RBI's outright purchase or sale of government securities to alter durable liquidity. The MSS is a scheme under which the government issues securities whose proceeds RBI holds to sterilise surplus liquidity from forex intervention ⚠️ (introduced 2004 ⚠️). VRR and VRRR are variable-rate repo and reverse-repo auctions used for short-term liquidity fine-tuning ⚠️.
**Breakdown:**
- OMO purchases add durable liquidity; OMO sales absorb it; both affect yields across maturities. [basic/04 §5]
- Sterilisation offsets the domestic liquidity effect of forex intervention, often via OMOs or absorption operations. [basic/04 §2; basic/19 §5]
- Sterilisation carries a fiscal and quasi-fiscal cost (interest differential) and cannot be sustained indefinitely at large scale. [basic/19 §5]
- VRR/VRRR fine-tune overnight conditions and do not change the policy stance.
**Cases / Committees / Schemes / Data:** 2023 Prelims PYQ on sterilisation and OMO role (key unavailable locally). [basic/04 §9]
**Trap:** OMO is not a repo rate change. A variable-rate auction is not an MPC decision.
**Mains hook:** Sterilised forex intervention protects a managed float in the short run but has a carrying cost and can distort the yield curve.
**Back:** *"OMO buys durable liquidity; MSS parks forex money; variable rates tune the day."*

### Flashcard T-018 — Liquidity management framework and WACR
**Front:** What is RBI's liquidity management framework, and why is the weighted average call rate (WACR) the operating target?
**Definition (learn):** The liquidity framework uses LAF, OMOs and FX operations to keep overnight money-market rates aligned with the policy corridor. WACR is the weighted average call-money rate, the operating target.
**Breakdown:**
- Policy target, tolerance band, repo rate and operating target are distinct. [basic/04 §6]
- Surplus liquidity pushes WACR toward the SDF floor; deficit liquidity pushes it toward the MSF ceiling ⚠️ (standard mechanism).
- Survey FY26: WACR averaged 8 basis points below repo up to 8 January 2026; M3 grew 12.1% y/y in the Survey's liquidity snapshot. [basic/04 §8]
- A liquidity surplus is not solvency and does not guarantee credit uptake.
**Cases / Committees / Schemes / Data:** Survey 2025-26 liquidity snapshot (period and vintage as stated). [basic/04 §8]
**Trap:** Liquidity surplus is not a rate cut; "the repo sets WACR" is only partly right, because liquidity conditions also matter.
**Mains hook:** Explain why liquidity management is needed even after an MPC decision: the decision sets the signal, but liquidity makes money markets follow it.
**Back:** *"Policy sets the signal; liquidity makes WACR obey."*

### Flashcard T-019 — Monetary transmission: EBLR, MCLR and bank lending rates
**Front:** How do repo changes pass into bank deposit and lending rates in India, and why is transmission uneven?
**Definition (learn):** Transmission is the path from policy rate to money-market rates, to bank deposit and lending rates, to borrowing and demand. EBLR (external benchmark lending rate) links floating-rate loans to an external benchmark such as the repo rate. MCLR (marginal cost of funds-based lending rate) links loans to a bank's marginal funding cost.
**Breakdown:**
- EBLR linkage became mandatory for new floating-rate retail and MSME loans from 1 October 2019 ⚠️ (standard date, verify).
- MCLR replaced the base-rate system from April 2016 ⚠️ (standard, verify).
- RLLR is a bank-level label for repo-linked rates; the RBI-prescribed benchmark is EBLR ⚠️ verify before using RLLR in an answer.
- Repo hikes in the post-pandemic phase passed quickly into external-benchmark-linked rates and more slowly into deposit rates and legacy loans. [basic/04 §5]
- Pass-through is shaped by funding mix, small-savings competition, credit risk and bank balance sheets. [basic/04 §5, §6]
**Cases / Committees / Schemes / Data:** Post-2022 repo cycle transmission (owner example; no rate numbers recorded in owners). [basic/04 §5]
**Trap:** A repo cut does not guarantee an equal cut in lending rates; "repo-linked" and "MCLR-linked" loans transmit at different speeds.
**Mains hook:** Evaluate monetary effectiveness through pass-through speed, banking health and the mix of benchmark loans in the borrower base.
**Back:** *"Repo moves the EBLR loans fast, the MCLR and old books slowly."*

### GROUP — Banking structure, NBFCs and bank-reform committees

### Flashcard T-020 — Banking structure: scheduled, commercial, cooperative and rural banks
**Front:** How is India's banking system classified, and what does "scheduled" mean?
**Definition (learn):** A scheduled bank is one included in the Second Schedule of the RBI Act, subject to eligibility conditions. Commercial banks take deposits and provide payments and credit services; cooperative banks are member-based banks regulated under banking law and co-operative law.
**Breakdown:**
- Scheduled commercial banks (SCBs): public sector, private sector and foreign banks (foreign banks may operate as branches or wholly owned subsidiaries). [basic/05 §4, §6]
- Regional Rural Banks (RRBs): rural-mandate institutions with a 75% overall priority-sector target and a 15% weaker-sections sub-target. [basic/05 §5]
- Cooperative banks: urban cooperative banks (UCBs) and rural cooperative banks. Banking functions fall under RBI and banking law; co-operative governance falls under state and co-operative law ⚠️ (standard split).
- Owner-level institutional tools: the Lead Bank Scheme and the Service Area Approach linked branch expansion to district credit planning. [basic/05 §4]
- DICGC insures eligible deposits in covered banks up to ₹5 lakh per depositor per bank. [basic/05 §6]
**Cases / Committees / Schemes / Data:** 2021 Prelims PYQ on UCB regulation and features; 2019 Prelims PYQ on the Service Area Approach under the Lead Bank Scheme (keys not recorded). [basic/05 §9]
**Trap:** "All co-operatives are regulated only by states" is false for banking functions, which fall under RBI. A commercial bank's assets are loans, investments, cash and balances; deposits are liabilities.
**Mains hook:** Institutional diversity widens inclusion but increases supervisory complexity; answer by mapping each institution to its mandate and safety net.
**Back:** *"Scheduled means on the Second Schedule; co-operatives bank under RBI law and state law."*

### Flashcard T-021 — Small Finance Banks and Payments Banks: differentiated licences
**Front:** What can Small Finance Banks and Payments Banks do, and what can they not do?
**Definition (learn):** Small Finance Banks (SFBs) are differentiated banks focused on small-ticket lending and deposit mobilisation. Payments Banks are differentiated banks focused on deposits and payments; they cannot lend from their own balance sheet.
**Breakdown:**
- SFB priority-sector target from FY2025-26: 60% overall, with 12% weaker-sections sub-target (owner states the 40% prescribed sub-targets plus 20% in any eligible priority sector). [basic/05 §5]
- Payments Banks accept deposits and facilitate payments but do not provide full-service lending (✅ owner; ✅ Wikipedia 'Payments bank': not permitted to lend to any person, including directors).
- Payments Banks' per-customer deposit ceiling is ₹2 lakh (✅ Wikipedia 'Payments bank': initially ₹1 lakh, raised to ₹2 lakh in 2021). Payments Banks cannot issue loans or credit cards (✅ Wikipedia); they can issue ATM/debit cards.
- Both are differentiated-bank categories created by RBI licensing, not separate constitutional categories. [basic/05 §5]
**Cases / Committees / Schemes / Data:** Owner example: differentiated licensing for SFBs and Payments Banks as activity-based design. [basic/05 §5]
**Trap:** A Payments Bank can lend from its own balance sheet is false. An SFB is a bank, not an NBFC.
**Mains hook:** Activity-based licensing expands access without granting identical powers to every entrant; answer by weighing viability of narrow business models.
**Back:** *"Small finance lends small; payments banks move money but do not lend their own."*

### Flashcard T-022 — NBFCs and Scale Based Regulation
**Front:** How do NBFCs differ from banks, and how does RBI regulate them by size and risk?
**Definition (learn):** An NBFC is a company providing specified financial activities without being a bank. Scale Based Regulation (SBR) is RBI's framework that sets regulatory intensity by size, activity and perceived systemic risk ⚠️ (framework adopted 2021; layer names ⚠️ verify).
**Breakdown:**
- NBFC categories ⚠️ (verify current list): investment and credit companies, infrastructure finance companies, microfinance institutions, factors, core investment companies, infrastructure debt funds, peer-to-peer lending platforms, account aggregators.
- Ordinary NBFCs generally cannot issue cheques drawn on themselves and are not covered by DICGC. [basic/05 §6]
- RBI registration does not make an NBFC a bank. [basic/05 §6]
- Funding fragility, not legal label, drives systemic risk: IL&FS (2018) and DHFL stress transmitted to mutual funds, banks and credit markets. [basic/05 §5]
**Cases / Committees / Schemes / Data:** 2026 Prelims PYQ on NBFC deposits, RBI registration, payment systems and deposit insurance (provisional key). 2024 Prelims PYQ on NBFC access to LAF (rejected). [basic/05 §9]
**Trap:** Every NBFC is a bank without branches is false. A registered NBFC does not get bank-style payment or deposit privileges.
**Mains hook:** Regulate by function, leverage and interconnectedness; avoid regulatory arbitrage without suffocating specialised credit.
**Back:** *"An NBFC lends without the bank's cheques and deposit cover; its size sets its rulebook."*

### Flashcard T-023 — Bank nationalisation and state-led restructuring timeline
**Front:** What was the sequence of bank nationalisation and later state-led consolidation?
**Definition (learn):** Nationalisation is state acquisition of ownership in private commercial banks; consolidation is merger of public-sector banks (PSBs) into fewer, larger units.
**Breakdown:**
- 1955: Imperial Bank of India became the State Bank of India ✅ (Wikipedia, 'Nationalisation of banks in India'); the SBI Act reference is standard ⚠️ and not separately confirmed.
- 1969: 14 major private banks nationalised, effective midnight 19 July 1969 ✅ (Wikipedia, 'Nationalisation of banks in India'; ordinance "Banking Companies (Acquisition and Transfer of Undertakings) Ordinance, 1969"; presidential approval of the bill 9 August 1969 ✅); the 1970 Act reference ⚠️ not confirmed (the page cites the 1969 ordinance and bill only).
- 1980: six more commercial banks nationalised ✅ (Wikipedia, 'Nationalisation of banks in India': "A second round of nationalizations of six more commercial banks followed in 1980"; the page gives no day or month, so the exact date is ⚠️).
- 2017: five associate banks (Bikaner & Jaipur, Hyderabad, Mysore, Patiala, Travancore) merged into SBI effective 1 April 2017; Bharatiya Mahila Bank was part of the proposal ✅ (Wikipedia, 'Nationalisation of banks in India'; Cabinet approval 15 Feb 2017).
- 2019-20: six PSBs were absorbed into four acquirers effective 1 April 2020 (OBC and United Bank into PNB; Syndicate into Canara; Andhra and Corporation into Union Bank; Allahabad into Indian Bank) ✅ (Wikipedia, 'Nationalisation of banks in India'; Cabinet approval 4 March 2020).
- Banks Board Bureau (2016) was created to recommend PSB board appointments, with later successor arrangements. [basic/05 §5, §9]
**Cases / Committees / Schemes / Data:** 2018 Prelims PYQ on PSB governance, capital infusion and the SBI merger; 2019 Prelims PYQ on selection of PSB chairmen (keys not recorded). [basic/05 §9]
**Trap:** Nationalisation does not prove sound governance. Ownership, appointments, underwriting quality and supervision are separate issues. Capital infusion alone does not fix weak appraisal.
**Mains hook:** State ownership helps welfare delivery and crisis response, but it does not automatically secure efficient credit allocation; answer through governance reform, not ownership alone.
**Back:** *"Fourteen in 1969, six in 1980, then the merging began."*

### Flashcard T-024 — Narasimham Committees I and II: prudential and consolidation reforms
**Front:** What did the Narasimham Committees recommend for Indian banking?
**Definition (learn):** The Narasimham Committee I (1991) on the financial system and Narasimham Committee II (1998) on banking-sector reform are the anchors of India's prudential banking reform.
**Breakdown:**
- Narasimham I (1991; appointed 14 August 1991, report November 1991 ✅ Wikipedia 'Narasimham Committee'): it identified priority-sector lending as a drag on bank profitability and advised phasing it out ✅; the wider list (prudential norms, capital adequacy, asset classification, reduced pre-emptions) ⚠️ not confirmed from a fetched source.
- Narasimham II (1998; report April 1998 ✅ Wikipedia): three-tier consolidation (three large internationally active banks, eight to ten national banks, regional/local banks), NPA and autonomy recommendations ✅; the full recommendation list beyond these items ⚠️ not separately verified.
- Owner: Narasimham I and II pushed reform towards prudential norms, capital adequacy and resolution-oriented discipline; implementation was phased and politically mediated. [basic/06 §5]
- Framing: the committees provide the bridge between liberalisation-era reform and later NPA, Basel and resolution debates. [basic/06 §5]
**Cases / Committees / Schemes / Data:** 2026 Prelims PYQ on financial-sector reform committees and sponsors (provisional, answer not inferred). [basic/04 §9]
**Trap:** Narasimham II is not a 1991 committee; both concern banks, not NBFCs. Committee recommendations are advisory and phased.
**Mains hook:** Trace NPA and Basel discipline back to the Narasimham lineage; a balanced answer shows what was implemented and what remains.
**Back:** *"Narasimham one wrote the prudence rules; Narasimham two pushed for stronger, fewer banks."* (✅ consolidation emphasis confirmed, Wikipedia 'Narasimham Committee').

### Flashcard T-025 — Nachiket Mor Committee and financial inclusion ⚠️
**Front:** What did the Nachiket Mor Committee propose for financial inclusion?
**Definition (learn):** Nachiket Mor chaired the Committee on Comprehensive Financial Services for Small Businesses and Low Income Households, formed September 2013 ✅ (Wikipedia 'Nachiket Mor'); the report appeared by early 2014 (Mint commentary of 10 January 2014 cited by Wikipedia) ✅ partial. Its recommendations are not recorded in the owners or in the fetched source; verify the report before using it in an answer ⚠️.
**Breakdown:**
- Broad idea ⚠️ (unverified; committee recommendations not retrieved): every household should have access to basic payment and savings services, delivered through business correspondents and technology.
- Proposed institutional support for inclusion ⚠️ (verify the exact funds and channels named in the report).
- Its era preceded the PMJDY launch (2014) and the Jan-Dhan–Aadhaar–mobile architecture. [basic/06 §5 context]
**Cases / Committees / Schemes / Data:** Owner-level link: PMJDY and SHG-bank linkage as inclusion architecture. [basic/06 §4, §6]
**Trap:** Do not confuse Mor (inclusion) with PJ Nayak (bank governance) or Raghuram Rajan (2008 sector reform).
**Mains hook:** Inclusion must be judged by usage and quality, not account counts; use the committee only after verifying its recommendations.
**Back:** *"Mor wanted every household banked and served through partners."* ⚠️

### Flashcard T-026 — PJ Nayak Committee and the Bank Board Bureau ⚠️
**Front:** What did the PJ Nayak Committee recommend on bank governance, and what did it lead to?
**Definition (learn):** The Committee to Review Governance of Boards of Banks in India (PJ Nayak, 2014) ⚠️ examined bank boards and appointment processes; it recommended a Bank Board Bureau ⚠️ (verify).
**Breakdown:**
- Bank Board Bureau constituted in 2016 to recommend appointments to PSB boards ✅ owner (basic/05 §5, §9).
- Recommendations on separating chairman and chief executive roles, and on reducing government influence over boards ⚠️ (verify).
- Later public-financial-sector appointment arrangements replaced the Bureau ⚠️ (owner says "successor arrangements"; verify the successor body and date).
**Cases / Committees / Schemes / Data:** 2022 Prelims PYQ on the Banks Board Bureau's role and PSB appointments (key unavailable locally). [basic/05 §9]
**Trap:** PJ Nayak is about governance of boards; Narasimham is about prudential reform. The Bureau recommended appointments; it did not run the banks.
**Mains hook:** Governance and ownership both matter; a sound answer separates appointment process, supervision and credit appraisal.
**Back:** *"Nayak fixed the boardroom: a bureau, not a ministry, recommended bank heads."* ⚠️

### Flashcard T-027 — Raghuram Rajan Committee (2008) on financial-sector reform ⚠️
**Front:** What did the Raghuram Rajan Committee on financial-sector reform recommend (constituted 2007; report year as stated in the Definition)?
**Definition (learn):** The Committee on Financial Sector Reforms, chaired by Raghuram Rajan, whose report is titled "A Hundred Small Steps" ✅ (Wikipedia 'Raghuram Rajan': set up in 2007 at Montek Singh Ahluwalia's request, "take a hundred small steps in the same direction"; the page's reference list gives the publication year as 2009, so the "2008" in the card heading is ⚠️ and not confirmed), proposed incremental reforms to deepen financial markets, widen access and reduce state dominance ⚠️.
**Breakdown:**
- Incremental, sequenced reform rather than a single big-bang change ⚠️.
- Access and inclusion, competition in banking, and market deepening ⚠️ (verify exact recommendations).
- Do not confuse with Raghuram Rajan's later RBI Governorship (2013–16 ✅ Wikipedia: 4 Sept 2013 – 4 Sept 2016), when the Asset Quality Review was launched ⚠️ (AQR link not confirmed by the fetched page).
**Cases / Committees / Schemes / Data:** Owner-level: AQR as a recognition-first NPA step [basic/06 §5]. The 2008 committee itself is not cited in the owners.
**Trap:** The 2008 Rajan committee and Rajan as RBI Governor are different roles. Committee advice is not binding law.
**Mains hook:** Sequencing matters: recognition, competition and inclusion reforms reinforce each other; name which step the question asks about.
**Back:** *"Rajan's report asked for a hundred small steps, not one leap."* (title ✅; year ⚠️)

### Flashcard T-028 — Priority Sector Lending: targets, sub-targets and the 2025 Master Direction
**Front:** What are the PSL targets for domestic banks, and what do shortfalls trigger?
**Definition (learn):** Priority Sector Lending (PSL) is an RBI-mandated directed-credit requirement. Domestic commercial banks and foreign banks with 20 or more branches must direct 40% of Adjusted Net Bank Credit (ANBC) or credit-equivalent off-balance-sheet exposure, whichever is higher, to priority sectors (owner-based; Wikipedia 'Priority sector lending' gives no percentages and the RBI Master Direction was not reached in this pass, so the 40% and the 2025 Master Direction remain ⚠️ until checked against the notified text).
**Breakdown:**
- Agriculture sub-target 18% (of which 10% for small and marginal farmers); weaker sections 12% ✅ owner.
- RRBs: 75% overall with 15% for weaker sections; SFBs: 60% overall with 12% for weaker sections from FY2025-26 ✅ owner.
- Targets are revised through RBI Master Directions (effective 1 April 2025, with later updates per owner); cite the current notified ratio, not a permanent figure. [basic/05 §5]
- Shortfalls are typically routed to NABARD's RIDF rather than penalised as criminal default ✅ owner.
**Cases / Committees / Schemes / Data:** Owner-verified targets as above; "updated through 11 September 2026" per the owner's own note ⚠️ verify the date.
**Trap:** PSL is not voluntary CSR. PSL certificates and securitised portfolios can substitute for genuine last-mile lending; it is not a constitutional ratio.
**Mains hook:** A social mandate on credit improves access for MSEs and farmers, but compliance-driven lending can be poorly underwritten; propose underwriting-quality checks alongside targets.
**Back:** *"Forty on the book, eighteen to farmers, twelve to the weaker sections."*

### Flashcard T-029 — DICGC deposit insurance and the Prompt Corrective Action framework
**Front:** How do deposit insurance and PCA protect depositors and weak banks, and how do they differ?
**Definition (learn):** DICGC (Deposit Insurance and Credit Guarantee Corporation) is the statutory deposit insurer for eligible bank deposits. Prompt Corrective Action (PCA) is RBI's supervisory framework that triggers graduated restrictions on weak banks using capital, asset-quality and profitability thresholds.
**Breakdown:**
- DICGC cover: eligible deposits up to ₹5 lakh per depositor per bank, including principal and interest. [basic/05 §6]
- DICGC does not cover shares, bonds, mutual funds, insurance products or ordinary NBFC liabilities. [basic/05 §5, §7]
- PCA: early-intervention restrictions (for example on dividends, branch expansion and management pay ⚠️ verify list) and risk-based triggers ⚠️ (thresholds not in owners).
- PCA is not liquidation and not a deposit-insurance payout mechanism. [basic/06 §6]
**Cases / Committees / Schemes / Data:** Owner: PCA as a tool for weak banks, paired with recapitalisation and governance repair. [basic/05 §5; basic/06 §4]
**Trap:** PCA is not DICGC; a DICGC payout is not an RBI supervisory intervention.
**Mains hook:** Preventive supervision beats waiting for failure, but PCA can slow credit, so pair it with recapitalisation and business-model correction.
**Back:** *"DICGC pays the depositor; PCA stops the slide before anyone has to be paid."*

### GROUP — NPAs, insolvency, asset reconstruction and Basel capital norms

### Flashcard T-030 — NPA classification, SMA buckets, provisioning and write-off
**Front:** When does a loan become an NPA, and how do SMA buckets, provisioning and write-off differ?
**Definition (learn):** An NPA is a loan classified as non-performing under RBI prudential norms; for a term loan, interest or principal overdue for more than 90 days is the standard test. Provisioning is a charge against income to absorb expected loss. Write-off removes the loan from the active book but does not waive recovery rights.
**Breakdown:**
- Special Mention Account (SMA) buckets track early overdue stages (SMA-0, SMA-1, SMA-2 for overdue periods up to 30, 31–60 and 61–90 days) ⚠️ (standard RBI framework; verify).
- Gross NPA minus provisions = net NPA; provisions reduce the uncovered amount. [basic/06 §6]
- Provisioning recognises expected loss; a write-off removes the asset from books. [basic/06 §7]
- Survey 2025-26: scheduled commercial bank GNPA 2.2% and NNPA 0.5% by September 2025. [basic/06 §8]
**Cases / Committees / Schemes / Data:** 2018 Prelims PYQ on capital adequacy (routed); 2020 Prelims PYQ on interest coverage ratio (routed). Keys not recorded. [basic/06 §9]
**Trap:** Provisioning is not write-off; write-off is not a waiver of the borrower's liability. Restructuring is not fraud when viability is restored transparently. There is no universal job-loss EMI holiday under RBI norms.
**Mains hook:** Early recognition can initially worsen reported ratios but stabilises the system; answer with recognition, provisioning and resolution in sequence.
**Back:** *"Ninety days overdue makes an NPA; provisions cover the hole, write-offs clear the books."*

### Flashcard T-031 — Twin Balance Sheet problem, Asset Quality Review and the 4R strategy
**Front:** What is the Twin Balance Sheet (TBS) problem, and how did the AQR and 4R strategy respond?
**Definition (learn):** The TBS problem is simultaneous stress in corporate balance sheets (over-leveraged firms with weak debt-servicing capacity) and bank balance sheets (rising NPAs). It was named in the Economic Survey 2016-17. The 4R strategy comprises Recognition, Resolution, Recapitalisation and Reforms.
**Breakdown:**
- Over-leveraged corporates often had interest-coverage ratios below 1 (owner describes this as the problem signal) ✅ owner.
- Asset Quality Review pushed banks to recognise under-reported stress; recognition comes first in the sequence. [basic/06 §5]
- Cleaning one balance sheet alone leaves the other constrained; resolution needs corporate deleveraging (IBC) and bank recapitalisation together. [basic/06 §5]
- TBS is a diagnostic framing, not a law or scheme. [basic/06 §6]
**Cases / Committees / Schemes / Data:** Economic Survey 2016-17 (Arvind Subramanian as CEA, per owner). Old system GNPA around 9% at that time; not a current figure. [basic/06 §5]
**Trap:** TBS is not a legal instrument. The GNPA figure quoted at the time is historical, not current.
**Mains hook:** Use TBS to show why NPA resolution needs both IBC-style corporate resolution and bank recapitalisation plus governance reform.
**Back:** *"Recognise, resolve, recapitalise, reform: never clean just one balance sheet."*

### Flashcard T-032 — Insolvency and Bankruptcy Code, 2016: collective, time-bound resolution
**Front:** What does the IBC, 2016 do, and what are its main institutions?
**Definition (learn):** The Insolvency and Bankruptcy Code, 2016 is a collective, time-bound insolvency framework aimed at value-maximising resolution rather than lender-by-lender recovery.
**Breakdown:**
- Adjudicating authority for corporate insolvency: National Company Law Tribunal (NCLT) ✅ owner.
- Committee of Creditors (CoC) takes resolution decisions; a Resolution Professional runs the process ✅ owner.
- Insolvency and Bankruptcy Board of India (IBBI) as regulator ✅ (Wikipedia, 'Insolvency and Bankruptcy Code': the IBBI oversees the proceedings).
- Time limits (✅ corrected: was "overall outer cap ⚠️"): the corporate insolvency resolution process is to be completed in 180 days from admission, extendable by 90 days if a majority of creditors agree; the mandatory 330-day outer limit (including extension and litigation time) was struck down by the Supreme Court in *Committee of Creditors of Essar Steel India Ltd v Satish Kumar Gupta* (2019): Wikipedia 'Insolvency and Bankruptcy Code' says the Court "has struck down the upper limit of 330 days" and that the Adjudicating Authority or Appellate Tribunal may in some cases allow time beyond 330 days. The Ghanashyam Mishra (2021) holding, and whether it is prospective or retrospective, is not on the fetched page and remains ⚠️ (✅ Wikipedia, 'Insolvency and Bankruptcy Code'). The Code was enacted in 2016 and commenced 28 May 2016 ✅.
- Inter-creditor agreements are coordination tools, not tribunals. [basic/06 §6]
**Cases / Committees / Schemes / Data:** 2019 Prelims PYQ on inter-creditor agreement purpose (routed). [basic/06 §9]
**Trap:** IBC admission is not resolution. IBC is not SARFAESI; DRT is not NCLT. Litigation and capacity constraints reduce time-bound efficiency.
**Mains hook:** Multi-creditor distress needs a collective mechanism; evaluate it on value preserved, time taken and litigation load.
**Back:** *"IBC makes creditors act together, on a clock, before a tribunal."*

### Flashcard T-033 — SARFAESI Act 2002, Debt Recovery Tribunals and recovery versus resolution
**Front:** How do SARFAESI and DRT recovery differ from IBC resolution?
**Definition (learn):** The SARFAESI Act, 2002 (Securitisation and Reconstruction of Financial Assets and Enforcement of Security Interest Act) gives secured creditors enforcement powers over secured assets outside ordinary civil suits ✅ owner. Debt Recovery Tribunals (DRTs) are specialised forums for recovery disputes under the Recovery of Debts and Bankruptcy Act, 1993 ⚠️.
**Breakdown:**
- SARFAESI is a secured-asset recovery tool; it is not the whole insolvency system ✅ owner.
- DRTs are distinct from the NCLT route under IBC ✅ owner.
- Recovery tools work best when security exists and documentation is clear; they do not solve viability in multi-creditor cases ✅ owner.
- Aggressive recovery without viability assessment can destroy enterprise value ✅ owner.
**Cases / Committees / Schemes / Data:** 2023 Prelims PYQ on InvIT tax treatment and SARFAESI (key unavailable locally; owner notes InvITs are not recovery frameworks). [basic/08 §9]
**Trap:** SARFAESI and IBC are not identical. SARFAESI does not reorganise a whole company; IBC does.
**Mains hook:** Compare recovery (SARFAESI, DRT), collective resolution (IBC) and stressed-asset transfer (ARC or NARCL) by purpose, speed and value preservation.
**Back:** *"SARFAESI seizes the secured asset, DRT adjudicates the debt, IBC rescues the company."*

### Flashcard T-034 — Asset Reconstruction Companies, NARCL and the bad-bank concept
**Front:** What are ARCs and NARCL, and what does a bad bank do to losses?
**Definition (learn):** ARCs are asset reconstruction companies that acquire stressed loans for recovery or resolution. NARCL (National Asset Reconstruction Company Ltd) is India's bad-bank vehicle that aggregates stressed assets so that they can be resolved in a specialised track ✅ owner.
**Breakdown:**
- ARCs and NARCL separate impaired assets from fresh bank lending ✅ owner.
- A transfer does not erase loss; valuation, recovery prospects and buyer interest decide the outcome ✅ owner.
- IDRCL (India Debt Resolution Company) is a related 2021 vehicle ⚠️ not in owners; verify before use.
- ARCs are regulated under the SARFAESI framework ⚠️ (standard; verify).
**Cases / Committees / Schemes / Data:** 2019 Prelims PYQ on the Inter-Creditor Agreement is related but distinct (routed) [basic/06 §9].
**Trap:** A bad bank eliminates losses is false. It moves stressed assets to another resolution vehicle; valuation risk stays.
**Mains hook:** Specialised vehicles unclog balance sheets, but transfer pricing and recovery uncertainty remain the hard problems.
**Back:** *"ARCs buy the bad debt, NARCL gathers it, and neither erases the loss."*

### Flashcard T-035 — Basel I, II and III norms and India's CRAR requirements
**Front:** What do Basel I, II and III require, and what India-specific capital minima apply?
**Definition (learn):** The Basel Committee on Banking Supervision sets international bank capital standards. Basel I (1988 ✅ Wikipedia 'Basel III' intro) introduced risk-weighted capital (⚠️ the risk-weighting detail is standard, not fetched); Basel II (2004 ✅ Wikipedia 'Basel III' intro) set three pillars: minimum capital, supervisory review and market discipline ✅ owner; Basel III (standards published by the BCBS in September 2010 ✅ Wikipedia 'Basel III'; post-global-financial-crisis) raised the quality and quantity of capital and added buffers and liquidity standards ✅ (buffers) ⚠️ (liquidity standards).
**Breakdown:**
- Basel III global minima: CET1 ≥ 4.5%, Tier 1 ≥ 6%, Total capital ≥ 8% of risk-weighted assets ✅ owner.
- Capital Conservation Buffer 2.5% in CET1 ✅ owner (✅ Wikipedia 'Basel III': at least 2.5% of RWA); effective minimum CET1 becomes 8% and effective total CRAR 11.5% ✅ owner.
- RBI India-specific minima for Indian scheduled commercial banks: CET1 ≥ 5.5%, Tier 1 ≥ 7%, Total CRAR ≥ 9%, excluding the CCB ✅ owner, from the Basel III Master Circular last issued 1 April 2025 (verify the latest-dated circular).
- Countercyclical Capital Buffer up to 2.5% exists but was not activated per the owner's latest guidance ✅ owner (verify).
- Liquidity standards: LCR requires HQLA to cover total net cash outflows over 30 days under stress, with HQLA ÷ net outflows ≥ 100%; NSFR requires available stable funding to exceed required stable funding over one year, with ASF ÷ RSF > 100% (✅ Wikipedia 'Basel III'); RBI implementation ⚠️ verify.
**Cases / Committees / Schemes / Data:** 2018 Prelims PYQ on capital adequacy as a risk-weighted concept (routed, key not recorded). [basic/06 §9]
**Trap:** Basel fixes one ratio for every asset is false; capital is risk-weighted. For an India-focused answer, cite the India-specific minima, not only the Basel 8% floor.
**Mains hook:** Higher buffers strengthen resilience but raise the cost of capital for weakly capitalised banks; recapitalisation must keep pace.
**Back:** *"Global eight, India nine, and with the buffer the Indian bank holds eleven and a half."*

### GROUP — Financial inclusion and digital payment rails

### Flashcard T-036 — PMJDY, JAM trinity and the RBI FI-Index
**Front:** What is PMJDY, how does JAM fit in, and how is inclusion measured beyond account counts?
**Definition (learn):** Pradhan Mantri Jan Dhan Yojana (PMJDY) is a national bank-account access scheme for the unbanked (launched 28 August 2014 ✅ Wikipedia 'PMJDY'; the same page's History section gives 15 August 2014, the Independence Day announcement). JAM is the trinity of Jan Dhan accounts, Aadhaar and mobile numbers ✅ (Wikipedia 'PMJDY'). The RBI FI-Index is a composite index of Access, Usage and Quality of financial services, with no base year ✅ owner.
**Breakdown:**
- PMJDY linked accounts to payments, DBT receipts and formal credit entry ✅ owner.
- Critique: opened accounts and sustained use differ; dormant accounts weaken the claim of effective inclusion ✅ owner.
- SHG-bank linkage connects savings groups, often women-led, to formal banking; the SHG itself is not a bank ✅ owner.
- WaterCredit is a microfinance model for water and sanitation access ✅ owner.
- RBI publishes the FI-Index annually ✅ owner.
**Cases / Committees / Schemes / Data:** 2026 Prelims PYQ on FI-Index sub-indices (provisional key, answer not inferred); 2021 Prelims PYQ on WaterCredit (routed); 2023 Prelims PYQ on SHG origin and bank linkage (routed). [basic/05 §9; basic/06 §9]
**Trap:** Inclusion equals account opening is false. FI-Index is not a count of accounts or borrowers. SHG is not a bank.
**Mains hook:** Inclusion must show usage and welfare value; use PMJDY and FI-Index together to separate access, usage and quality.
**Back:** *"Open the account, verify the person, connect the phone, then count the use."*

### Flashcard T-037 — Payment rails: RTGS, NEFT, UPI and ONDC
**Front:** How do RTGS, NEFT, UPI and ONDC differ, and who runs them?
**Definition (learn):** RTGS (real-time gross settlement) settles each transfer individually in real time. NEFT (National Electronic Funds Transfer) settles in batches. UPI (Unified Payments Interface) is an instant mobile-based payment interface run by the National Payments Corporation of India (NPCI) ✅ (Wikipedia 'Unified Payments Interface'). ONDC (Open Network for Digital Commerce) is an open e-commerce protocol network promoted by government ⚠️ (not verified in this pass).
**Breakdown:**
- RTGS is real-time gross; NEFT settles in batches; both operate 24x7 and inward transfers are free. [basic/07 §9]
- RBI requires payment-system data for systems operated in India to be stored in India for supervisory access. [basic/04 §6]
- Payment systems are RBI-regulated under the Payment and Settlement Systems Act ⚠️ (verify).
- UPI launched in 2016 (✅ corrected/confirmed: pilot launch 11 April 2016, Wikipedia 'Unified Payments Interface'); ONDC was incorporated in 2021 ⚠️ (not verified; the fetched page did not cover ONDC).
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQ Q68 on RTGS versus NEFT (key available locally; answer not recorded here). [basic/07 §9]
**Trap:** RTGS is batch and NEFT is real-time is wrong. A payments bank can lend is wrong. UPI is not a bank.
**Mains hook:** Digital public infrastructure widens access, but data localisation, consumer protection and fintech conduct risk must follow the rail.
**Back:** *"RTGS settles one by one, NEFT in batches, and UPI pays in a tap."*

### GROUP — Money market, capital market and financial instruments

### Flashcard T-038 — Money-market instruments: T-bills, commercial paper, CDs, call money and TREPS
**Front:** How do T-bills, commercial paper, certificates of deposit, call money and TREPS differ by issuer, tenor and collateral?
**Definition (learn):** The money market finances short-term needs (up to one year) ✅ owner. T-bills are short-term government securities; commercial paper (CP) is unsecured short-term corporate debt; certificates of deposit (CDs) are short-term instruments issued by eligible banks and financial institutions; call money is the overnight interbank market ⚠️ (standard); TREPS is the tri-party repo platform.
**Breakdown:**
- T-bills are issued by the government and auctioned by RBI on its behalf; tenors are typically 91, 182 and 364 days ⚠️ (tenors standard; verify).
- CP is issued by eligible corporates and is unsecured; vulnerable to rollover stress when confidence weakens ✅ owner.
- CDs are issued by eligible banks and FIs ✅ owner.
- TREPS replaced the earlier CBLO mechanism; it is collateralised and settled through CCIL ✅ owner.
- Repo is collateralised borrowing; TREPS is the platform; call money is typically unsecured ⚠️.
**Cases / Committees / Schemes / Data:** 2024 Prelims PYQ on CBLO (CBLO treated as money-market instrument per owner). 2020 Prelims PYQ on money-market instruments (routed). [basic/07 §8–9]
**Trap:** T-bills are not issued by RBI; RBI auctions them for the government. Repo, TREPS and call money are not identical in collateral, platform or counterparty exposure.
**Mains hook:** Money-market instruments fund short-term needs, and their rates transmit policy; discuss rollover risk and collateral design.
**Back:** *"Treasury, Commercial, Certificate, Call, and TREPS is the collateral lane."*

### Flashcard T-039 — Government securities, State Development Loans and Sovereign Gold Bonds
**Front:** How do G-secs, SDLs and Sovereign Gold Bonds differ, and what moves G-sec yields?
**Definition (learn):** Government securities (G-secs) are dated central-government debt, a capital-market instrument ✅ owner. State Development Loans (SDLs) are bonds issued by state governments through the same market ⚠️ (standard). Sovereign Gold Bonds (SGBs) are gold-linked government securities issued by RBI on behalf of the Government of India, launched 2015 ✅ (Wikipedia 'Sovereign Gold Bond'; Cabinet 9 Sept 2015, launch 5 Nov 2015).
**Breakdown:**
- NDS-OM is the electronic platform for G-sec trading; CCIL supports settlement; CDSL holds securities in dematerialised form ✅ owner.
- Yields respond to inflation expectations, fiscal borrowing, liquidity, policy-rate expectations and risk perception ✅ owner.
- SGB issuance (✅ corrected: status was "may have been discontinued ⚠️"): the scheme was discontinued; the last tranche (2023-24 Series IV) was issued 21 February 2024 and no new series followed; in February 2025 the Finance Minister confirmed no further tranches are planned; existing bonds are honoured (✅ Wikipedia 'Sovereign Gold Bond'; secondary source, RBI/government notice not retrieved).
- FPI holdings of G-secs have their own limits and routes; separate instrument, investor category and trading venue ✅ owner.
**Cases / Committees / Schemes / Data:** 2021 Prelims PYQ on factors in government bond yields; 2021 Prelims PYQ on NDS-OM, T-bills and CDSL (routed). [basic/07 §9]
**Trap:** G-secs are not corporate bonds. A plain bond's price moves inversely to yield. Coupon is not yield.
**Mains hook:** Government borrowing and bond yields link to crowding out and to monetary transmission; explain the channels, not only the yield level.
**Back:** *"Central bonds, state bonds, gold-linked bonds: yields follow inflation and fiscal news."*

### Flashcard T-040 — Corporate bonds, green bonds and sustainability bonds
**Front:** How do corporate bonds, green bonds and sustainability bonds differ?
**Definition (learn):** A corporate bond is a contractual debt claim by a company with coupon and principal obligations ✅ owner. A green bond finances defined environmental projects ✅ owner. A sustainability bond combines environmental and social eligible projects ✅ owner.
**Breakdown:**
- Bondholders are creditors and rank ahead of equity shareholders in repayment ✅ owner.
- Sovereign green bonds were first issued from FY2022-23 to finance eligible public-sector green projects, tracked against a framework ✅ owner (basic/25, cross-owner).
- Label credibility depends on framework, use-of-proceeds tracking and reporting; a label alone does not guarantee environmental outcomes ✅ owner.
- A 2026 provisional PYQ key distinguishes green, social and sustainability bonds ✅ owner (key provisional).
**Cases / Committees / Schemes / Data:** Owner data: sovereign green bonds from FY2022-23 (basic/25). 2025 Prelims PYQ on bondholder priority (routed). [basic/08 §8–9]
**Trap:** "Sustainability bond means only green projects" is false; it also covers social projects. Greenwashing risk remains where tracking is weak.
**Mains hook:** Green finance deepens markets only with credible labelling, disclosure and monitoring.
**Back:** *"Green is the environment alone; sustainability adds the social side."*

### Flashcard T-041 — Equity, mutual funds and ETFs: claim, liquidity and pricing
**Front:** How do equity shares, mutual funds and ETFs differ in claim, pricing and liquidity?
**Definition (learn):** Equity is an ownership claim with residual return and voting rights where applicable ✅ owner. A mutual fund is a SEBI-regulated pooled vehicle that issues units under a mandate ✅ owner. An ETF is an exchange-traded pooled unit bought and sold intraday on the exchange ✅ owner.
**Breakdown:**
- Open-ended mutual-fund units transact with the fund at applicable NAV rules ✅ owner.
- ETF prices can deviate from NAV; exchange trading does not guarantee perfect liquidity ✅ owner.
- Dividends depend on declaration and profits and are not contractual like bond interest ✅ owner.
- Beta measures a stock's volatility relative to the market; it is not a return guarantee ✅ owner.
- Diversification reduces idiosyncratic risk, not economy-wide corrections ✅ owner.
**Cases / Committees / Schemes / Data:** 2024 Prelims PYQ on ETFs as financial instruments (routed key available locally; answer not recorded). 2023 Prelims PYQ on beta (routed). [basic/07 §9; basic/08 §9]
**Trap:** ETF and stock are not identical; an ETF is a basket. Dividends are not contractual interest.
**Mains hook:** Compare by claim, liquidity promise and disclosure burden to advise household investors.
**Back:** *"A stock is ownership, a fund is a basket, and an ETF trades like a stock."*

### Flashcard T-042 — Alternative Investment Funds (AIFs) and their categories
**Front:** What is an AIF, which vehicles qualify, and what are its risks?
**Definition (learn):** An AIF is a privately pooled investment vehicle under SEBI's category-based framework ✅ owner. Venture capital funds and hedge funds fall within AIF categories ✅ owner; direct stocks and bonds are not AIFs ✅ owner.
**Breakdown:**
- Category I (venture, SME, social, infrastructure funds), Category II (private equity and debt without leverage) and Category III (hedge funds that may use leverage) ⚠️ standard framing; verify SEBI AIF Regulations, 2012 ⚠️.
- AIFs are less liquid and less standardised than mutual funds ✅ owner.
- Valuation opacity and liquidity mismatch remain risks ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQ on which investment vehicles qualify as AIFs (key available locally; answer not recorded here). [basic/08 §9]
**Trap:** An AIF is not a mutual fund; investing in direct bonds does not make one an AIF.
**Mains hook:** Investor suitability and disclosure matter more for AIFs than for mutual funds; cite category rules, not only returns.
**Back:** *"Privately pooled, sector-focused, less liquid: that is an AIF."*

### Flashcard T-043 — FPI, FDI, participatory notes and the insurance FDI cap
**Front:** How do FPI, FDI and participatory notes (P-notes) differ, and what is the owner-verified insurance FDI cap?
**Definition (learn):** Foreign portfolio investment (FPI) is passive foreign investment in listed securities through the portfolio route ⚠️ (standard). FDI is investment with a lasting interest and control or significant influence ⚠️ (standard). P-notes (participatory notes) are offshore derivative instruments issued by registered FPIs to overseas investors, not direct domestic shareholding ✅ owner.
**Breakdown:**
- P-notes are not direct holding; the underlying exposure is held by the registered FPI ✅ owner.
- Private-insurance foreign investment: ✅ corrected: was "74% under the automatic route" (owner, 2024 IRDAI circular). The Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 raised the cap to 100% in December 2025 (✅ two sources: Wikipedia 'Insurance in India' ("increased the FDI limits in the sector to 100% from 74%"; "100% in December 2025"), and PRS India bill tracker: the bill proposed FDI "from 74% to 100% of the paid-up equity capital", passed by Lok Sabha on 16 December 2025 and Rajya Sabha on 17 December 2025). The presidential-assent date and gazette/IRDAI text were not reached, so cite the Act and its date before using the figure in a final answer ⚠️.
- The owner's "74% remains" statement is superseded by the December 2025 amendment as reported; the owner file should be re-dated.
- FDI caps and routes vary by sector; do not generalise one sector's cap to others ✅ owner.
**Cases / Committees / Schemes / Data:** 2019 Prelims PYQ on participatory notes (routed); 2021 Prelims PYQ on FDI eligible instruments (routed). [basic/08 §9; basic/19 §9 routing]
**Trap:** P-notes are not FDI. The insurance cap is not a single figure for every insurer or every route; always state the Act or notification date with the percentage.
**Mains hook:** Capital-flow volatility from portfolio flows differs from stickier FDI; discuss quality of inflows.
**Back:** *"P-notes are borrowed exposure, FDI is owned, FPI is portfolio."*

### Flashcard T-044 — InvITs and REITs: pooled vehicles on cash flows
**Front:** How do InvITs and REITs differ, and what cash flows back them?
**Definition (learn):** An InvIT (Infrastructure Investment Trust) is a SEBI-regulated pooled vehicle giving market access to infrastructure cash-flow assets ✅ owner. A REIT (Real Estate Investment Trust) is a SEBI-regulated pooled vehicle for rent-yielding real estate ✅ owner.
**Breakdown:**
- REIT cash flows depend on occupancy and rent; InvIT cash flows depend on tariffs, traffic or project execution ✅ owner.
- InvIT tax treatment follows investment-vehicle rules; SARFAESI is a creditor-recovery framework, so they should not be conflated ✅ owner.
- SEBI's 2025 reclassification allows mutual funds and specialised funds to hold REIT units as equity-related instruments ✅ owner (cited SEBI circular).
- Valuation opacity and liquidity mismatch remain ✅ owner.
**Cases / Committees / Schemes / Data:** 2023 Prelims PYQ on InvIT tax treatment (routed; key unavailable locally). [basic/08 §9]
**Trap:** REIT, InvIT and AIF are not interchangeable labels; each differs in asset class, liquidity structure, investor base and regulation.
**Mains hook:** Compare REITs, InvITs and AIFs as channels for household participation in illiquid assets.
**Back:** *"Rent for REITs, roads and power for InvITs: both trade on cash flows."*

### Flashcard T-045 — Derivatives: futures, options, swaps and hedging versus speculation
**Front:** How do futures, options and swaps differ, and when is a derivative a hedge rather than a speculation?
**Definition (learn):** A future is a standardised derivative creating symmetric obligations for buyer and seller ✅ owner. An option gives the buyer a right, not an obligation, against the writer's contingent obligation ✅ owner. A swap is an exchange of cash-flow streams linked to rates, currencies or other variables ✅ owner.
**Breakdown:**
- Hedging reduces a pre-existing exposure; speculation creates or enlarges exposure to profit from price moves ✅ owner.
- Exchange-traded equity derivatives in India are regulated by SEBI with clearing-corporation margins ✅ owner.
- Interest-rate and currency swaps are regulated under RBI's framework and carry OTC counterparty and collateral risks ✅ owner.
- Hedge effectiveness depends on basis risk, contract match and discipline; over-hedging can create losses ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQ on India's equity-options market growth and regulation (key available locally; answer not recorded). [basic/08 §9]
**Trap:** Every derivative reduces risk is false. The same contract can hedge or speculate depending on whether an underlying exposure exists.
**Mains hook:** Separate legitimate hedging from excessive retail leverage and conduct risk; propose disclosure, suitability and margin discipline.
**Back:** *"Futures bind both sides, options give a right, swaps trade cash streams."*

### Flashcard T-046 — SEBI: statutory basis and powers
**Front:** What is SEBI's statutory basis, and what does it regulate?
**Definition (learn):** The Securities and Exchange Board of India is the statutory regulator of securities markets, established under the SEBI Act, 1992 ✅ (Wikipedia 'SEBI': statutory powers from 30 January 1992 through the SEBI Act, 1992; SEBI was first set up as an executive body on 12 April 1988).
**Breakdown:**
- Regulates listed securities, stock exchanges, mutual funds, AIFs, REITs and InvITs, credit-rating agencies and market intermediaries ✅ owner.
- Investor grievance and protection: SCORES grievance-redress system and product disclosure ✅ owner.
- SEBI's quasi-legislative, quasi-judicial and quasi-executive powers ✅ (Wikipedia 'SEBI': "three powers rolled into one body"; appeals go to the Securities Appellate Tribunal, then the Supreme Court). Exact statutory wording of the Act still to verify ⚠️.
- SEBI does not regulate ordinary bank lending; RBI does ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQ on SEBI's investor-warning and registered-investment-adviser role (per owner). [basic/08 §8]
**Trap:** SEBI regulates bank lending is wrong. SEBI and RBI divide labour functionally; instruments, venues and settlement can overlap.
**Mains hook:** Financial deepening needs conduct, disclosure and default management, not only new products.
**Back:** *"SEBI makes the rules, judges the breaches and enforces them, for securities, not for bank loans."*

### GROUP — Union Budget, deficits and fiscal rules

### Flashcard T-047 — Union Budget cycle: Articles 112–117 and the public funds
**Front:** What is the constitutional sequence of the Union Budget, and which funds finance it?
**Definition (learn):** The Annual Financial Statement (AFS) is the Budget statement under Article 112 ✅ owner. It is presented with charged and voted expenditure distinguished ✅ owner.
**Breakdown:**
- Article 112: Annual Financial Statement ✅ owner.
- Article 113: demands for grants voted by the Lok Sabha; no demand may be made except on the President's recommendation ✅ owner (2024 Prelims PYQ route).
- Article 114: Appropriation Bill authorising withdrawal from the Consolidated Fund ⚠️ (standard; not confirmed: Wikipedia 'Money bill' and 'Consolidated Fund of India' do not reproduce Arts 114–116; Wikipedia 'Money bill' does not mention Art 114).
- Article 115: supplementary, additional and excess grants ⚠️ (standard; not confirmed from a fetched source).
- Article 116: vote on account, votes on credit and exceptional grants ⚠️ (standard; not confirmed from a fetched source); an interim authorisation until the full budget passes.
- Article 117: money and financial bills involving expenditure need the President's recommendation (✅ partial: Wikipedia 'Money bill' says "A money bill can only be introduced in parliament with prior permission of the President of India (Article 117)"; the sub-clause detail remains ⚠️).
- Funds: Consolidated Fund of India (Art 266 ✅ Wikipedia 'Consolidated Fund of India': Art 266(1) makes government revenues and borrowed money part of the Consolidated Fund), Contingency Fund of India (Art 267 ⚠️ not on the fetched page), and the Public Account ⚠️.
**Cases / Committees / Schemes / Data:** 2024 Prelims PYQ on the AFS and Articles 112–113 (key on local file; answer not recorded here). [basic/09 §9]
**Trap:** The AFS is laid on behalf of the President, but the Budget is not a presidential authorisation for spending; Parliament authorises. Charged expenditure is not voted.
**Mains hook:** Parliamentary control over money; evaluate budget transparency through the sequence of approval, vote on account and CAG audit.
**Back:** *"112 presents, 113 demands, 114 appropriates, 116 bridges the gap."* ⚠️ (article numbering beyond 112–113 standard; verify).

### Flashcard T-048 — Deficit architecture: fiscal, revenue, primary and effective revenue deficits
**Front:** How do the fiscal, revenue, primary and effective revenue deficits differ, and what does each diagnose?
**Definition (learn):** Fiscal deficit = total expenditure minus non-debt receipts, broadly the borrowing requirement ✅ owner. Revenue deficit = revenue expenditure minus revenue receipts ✅ owner. Primary deficit = fiscal deficit minus interest payments ✅ owner. Effective revenue deficit = revenue deficit minus grants to states and UTs for creating capital assets ✅ owner.
**Breakdown:**
- Borrowing is excluded from non-debt receipts; recovery of loans and disinvestment are non-debt capital receipts ✅ owner.
- Effective capital expenditure = the Centre's own capex plus grants used for capital-asset creation ✅ owner.
- Fiscal deficit is a flow in a period, not total public debt ✅ owner.
- A zero primary deficit means current borrowing is fully explained by interest payments, not that debt is zero ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQs on capital receipts (Q10), revenue, fiscal and primary deficit (Q61) and gross primary deficit (Q65) (keys on local file; answers not recorded). [basic/09 §9]
**Trap:** Zero revenue deficit does not mean zero fiscal deficit; capital expenditure can still require borrowing. Capital receipts are not automatically asset-creating.
**Mains hook:** Use effective revenue deficit and effective capex to separate unproductive current spending from grants that build durable assets.
**Back:** *"Fiscal is all you borrow, revenue is the current gap, primary sheds interest, effective frees capital grants."*

### Flashcard T-049 — FRBM Act, 2003, the N.K. Singh Committee and the glide path
**Front:** What does the FRBM framework require, and what did the N.K. Singh-led committee add?
**Definition (learn):** The Fiscal Responsibility and Budget Management (FRBM) Act, 2003 imposes medium-term fiscal discipline through disclosure and targets ✅ owner. The Macro Economic Framework Statement (MEFS) explains the macro assumptions behind Budget numbers ✅ owner.
**Breakdown:**
- The N.K. Singh-led FRBM Review Committee (report submitted 23 January 2017 and made public 14 April 2017 ✅ Wikipedia 'FRBM Act, 2003') articulated a debt anchor and an operational glide path rather than a single-year deficit target ✅ owner.
- Committee debt-to-GDP proposals (for the Centre and the states) ⚠️ verify exact ratios from the report; not recorded in owners.
- FRBM Act enacted 26 August 2003, commenced 5 July 2004 ✅ (Wikipedia). The Medium-term Expenditure Framework Statement was added by an amendment of 2012 ✅ (Wikipedia). Later targets and amendments that changed the deficit path ⚠️ (year and targets not verified in this pass).
- Escape clauses should be transparent and temporary; otherwise targets become procyclical ✅ owner.
- Committee recommendations are advisory, not self-executing ✅ owner.
**Cases / Committees / Schemes / Data:** 2018 Prelims PYQ on the FRBM Review Committee's debt-GDP recommendations (routed); 2020 Prelims PYQ on the MEFS legal mandate (routed; keys not recorded). [basic/09 §9]
**Trap:** The Act sets medium-term transparency, not an annual deficit obsession. The MEFS is a context document, not a Budget estimate.
**Mains hook:** A glide path with transparent escape clauses balances credibility and countercyclical support; name the escape clause in any fiscal-rule answer.
**Back:** *"Anchor the debt, glide the deficit, disclose the statement."*

### Flashcard T-050 — Off-budget borrowing and contingent liabilities
**Front:** Why can the headline fiscal deficit understate government risk?
**Definition (learn):** Off-budget borrowing is borrowing or expenditure kept outside the Budget's fiscal-deficit calculation. Contingent liabilities are guarantees and similar claims that may become payable.
**Breakdown:**
- Examples: PSU government-guaranteed borrowing, NSSF-routed loans (pre-FY2020-21 practice of financing the Food Corporation of India's food-subsidy bill through NSSF borrowing), and special-purpose or extra-budgetary financing ✅ owner.
- Several such items have since moved onto the explicit Budget from FY2021-22 ✅ owner.
- Current stock of guarantees and off-budget items must be taken from a dated CAG or Budget document ✅ owner.
- The Centre's deficit ratio does not describe the whole general government ✅ owner.
**Cases / Committees / Schemes / Data:** Owner-cited FCI–NSSF example (pre-FY2020-21). [basic/09 §5, §6]
**Trap:** The headline deficit captures the full public-sector risk is false. Off-budget is off the headline, not off the hook.
**Mains hook:** Critically examine India's fiscal transparency by checking guarantees and off-budget items alongside the deficit ratio.
**Back:** *"Off-budget is off the headline, not off the hook."*

### Flashcard T-051 — Union Budget 2026-27 numbers and how to cite them
**Front:** What are the Union Budget 2026-27 fiscal numbers, and how should BE, RE and actuals be distinguished?
**Definition (learn):** Budget Estimates (BE) are policy authorisations and projections. Revised Estimates (RE) revise the current year partway through. Actuals are realised outcomes published by the Controller General of Accounts (CGA) after the year closes ✅ owner.
**Breakdown:**
- Fiscal deficit 2026-27 BE: 4.3% of GDP ✅ owner (Union Budget 2026-27 FRBM statement).
- Fiscal deficit 2025-26 RE: 4.4% of GDP ✅ owner.
- Capital expenditure 2026-27 BE: ₹12.22 lakh crore ✅ owner.
- Survey 2025-26: Centre revenue receipts averaged 9.1% of GDP in FY22–FY25 versus 8.5% in FY16–FY20 ✅ owner.
- Survey 2025-26: Centre capex about 3% of GDP post-pandemic versus 1.7% pre-pandemic; effective capex 4% of GDP in FY25 ✅ owner.
**Cases / Committees / Schemes / Data:** Figures as recorded in the owners; verify against later Revised Estimates and Actuals before citing after a revision ✅ owner status caution.
**Trap:** BE is not the realised outcome. Survey trends and Budget accounts are different sources.
**Mains hook:** Judge a Budget by capex quality, revenue quality and the debt path, not by the deficit percentage alone.
**Back:** *"Budget estimates promise, revised estimates adjust, actuals settle."*

### Flashcard T-052 — Household savings, government borrowing and crowding out
**Front:** How does government borrowing affect private credit, and what role do household financial savings play?
**Definition (learn):** Crowding out occurs when public borrowing raises interest rates or absorbs savings that would otherwise finance private borrowers ✅ owner. Crowding in occurs when productive public capex raises private investment ✅ owner.
**Breakdown:**
- Household financial savings (deposits, insurance, pension, small savings through the National Small Savings Fund) finance domestic government borrowing ✅ owner.
- A shift from financial savings to physical assets or cash weakens the financial pool for borrowing ✅ owner.
- Strong capex execution can crowd in private investment; heavy borrowing in tight conditions can crowd out private credit ✅ owner.
- 2026 Prelims PYQ on fiscal crowding out through government borrowing and interest rates (provisional key; answer not inferred) ✅ owner.
**Cases / Committees / Schemes / Data:** 2022 Prelims PYQ on household savings and government internal debt (routed). [basic/09 §9]
**Trap:** Household savings and government debt are not unrelated; domestic savings condition the financing environment.
**Mains hook:** Link borrowing, savings and interest rates in the savings–investment identity; conclude with a crowding-in condition, such as productive capex with strong execution.
**Back:** *"Public borrowing takes the same savings that private borrowers need."*

### GROUP — Taxation, GST and tax-base integrity

### Flashcard T-053 — Direct and indirect taxes, progressivity and incidence
**Front:** How do direct and indirect taxes differ in incidence, and what does progressivity mean?
**Definition (learn):** A direct tax is imposed on income, profit or wealth, and its legal incidence falls on the taxpayer. An indirect tax is imposed on transactions or consumption, and its burden may be shifted through prices ✅ owner. A progressive tax has an average burden that rises with income or ability to pay ✅ owner.
**Breakdown:**
- CBDT administers Union direct taxes; CBIC and state GST authorities administer indirect taxes ✅ owner.
- The Income-tax Act, 2025 and Income-tax Rules, 2026 commenced from 1 April 2026; the 1961 Act remains relevant to earlier years ✅ owner.
- Equalisation Levy on specified non-resident digital services and indirect-transfer rules on offshore share transfers deriving value from Indian assets are cross-border examples ✅ owner.
- Direct taxes can be diluted by exemptions and evasion; indirect taxes can protect equity through lower rates on essentials ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQs on agricultural income and rural agricultural land under income tax (routed; keys on local file). 2022 Prelims PYQ on indirect transfer of shares (routed). [basic/10 §9]
**Trap:** Direct is always progressive is false. Commencement date of a tax law and its rate changes are separate questions.
**Mains hook:** Direct taxes debate progressivity; indirect taxes debate incidence on consumption and compliance. Give both sides before concluding.
**Back:** *"Direct lands on the taxpayer; indirect rides the price."*

### Flashcard T-054 — GST architecture: destination-based VAT with input tax credit
**Front:** How does GST work across the Centre and the states, and what makes it destination-based?
**Definition (learn):** GST is a destination-based value-added tax on supply, with input tax credit (ITC) that taxes value addition across the chain ✅ owner. Revenue is assigned mainly to the place of final consumption through the IGST settlement architecture ✅ owner.
**Breakdown:**
- Components: CGST (Centre), SGST (state), IGST (inter-state supply) and UTGST (union territories) ⚠️ standard components; verify.
- Article 279A (inserted by the 101st Constitutional Amendment, 2016) ⚠️ (article number not confirmed in the fetched Wikipedia page; 101st Amendment confirmed) establishes the GST Council ✅ owner.
- ITC reduces cascading only when compliant, matched invoices satisfy the law ✅ owner.
- GST came into force on 1 July 2017 ✅ (Wikipedia 'Goods and Services Tax (India)': took effect through the 101st Amendment, launched at midnight on 1 July 2017).
**Cases / Committees / Schemes / Data:** 2018 Prelims PYQ on GST exemptions (routed). [basic/10 §9]
**Trap:** GST is origin-based is false; GST is destination-based. Not every supply is taxed identically; exemptions and zero-rating differ in credit consequences.
**Mains hook:** GST creates a common market and removes tax-on-tax, but invoice matching, refund delays and small-business compliance costs remain.
**Back:** *"Tax where it is eaten; credit what was paid up the chain."*

### Flashcard T-055 — GST rate structure after the 22 September 2025 rationalisation
**Front:** What is the GST rate architecture after the 56th GST Council reform?
**Definition (learn):** The 56th GST Council reform took effect from 22 September 2025 with broad 5% and 18% rates and a special 40% rate for specified demerit supplies ✅ owner.
**Breakdown:**
- Pre-reform structure had slabs of 0%, 5%, 12%, 18% and 28% plus compensation cess (✅ Wikipedia 'Goods and Services Tax (India)': pre-reform slabs 0/5/12/18/28; compensation cess up to 22% on top of 28% GST). Reform: 12% and 28% replaced by 5% and 18%; special 40% rate for luxury and "sin" goods; Council approval 3 September 2025 (✅ Wikipedia).
- Compensation cess discontinued for most goods; for tobacco and pan masala it continues until COVID-era loan repayment ✅ owner.
- Separately notified tobacco and cess treatment must not be collapsed into the two-rate shorthand ✅ owner.
- Verify the latest GST notifications for specific goods and services before quoting a rate ⚠️.
**Cases / Committees / Schemes / Data:** Owner-dated reform of 22 September 2025 (basic/10 §8). [basic/10 §8; advanced/10]
**Trap:** GST has only two rates is false. The 40% rate applies to specified luxury and sin (demerit) goods, not everything; the 0% and other rates on essentials and the cess treatment still need the notification (✅ corrected: "demerit" supplemented by "luxury and sin goods" per Wikipedia).
**Mains hook:** Simplification improves compliance but can blunt targeting of merit and demerit goods; judge the reform on both counts.
**Back:** *"Five and eighteen carry the load; forty punishes the demerit goods."*

### Flashcard T-056 — GST Council: Article 279A, composition and voting rule
**Front:** What is the GST Council, how is it composed, and how do its votes work?
**Definition (learn):** The GST Council is a constitutional federal forum under Article 279A that recommends the GST framework ✅ owner. It is not the Finance Commission ✅ owner.
**Breakdown:**
- Centre has one-third of weighted votes; states together have two-thirds ✅ owner.
- A decision needs at least three-fourths of weighted votes ✅ owner.
- Chair: Union Finance Minister; members: Union Minister of State and state finance or taxation ministers ⚠️ (standard, verify Art 279A(2)).
- The Council recommends; legislatures and the executive implement through laws and notifications ✅ owner.
**Cases / Committees / Schemes / Data:** Owner-verified voting rule (basic/10 §6; the one-third/three-fourths split is not on the fetched Wikipedia GST pages, so it remains ⚠️ for the Act text). The 101st Amendment (2016): ✅ Wikipedia 'Goods and Services Tax (India)' cites "The Constitution (One Hundred and First Amendment) Act, 2016" with assent 8 September 2016; Article 279A's number is still ⚠️.
**Trap:** GST Council is not Parliament; the Finance Commission does not set GST rates ✅ owner.
**Mains hook:** The voting weights make cooperative federalism a design question: the Centre's one-third is a veto only when combined with states' split; explain the implications for consensus.
**Back:** *"Centre one-third, states two-thirds, and three-fourths to decide."*

### Flashcard T-057 — Taxes subsumed in GST and levies outside GST
**Front:** Which central and state taxes did GST subsume, and which remain outside GST?
**Definition (learn):** GST subsumed pre-GST indirect taxes on the Union and state sides, removing cascading tax-on-tax across the production and distribution chain ✅ owner.
**Breakdown:**
- Union side: Central Excise Duty (with exceptions), Service Tax, Additional Excise Duties, Countervailing Duty, Special Additional Duty on imports, and central cesses or surcharges on supply ✅ owner.
- State side: State VAT or sales tax, Central Sales Tax (as collected), Purchase Tax, Entertainment Tax (other than local-body levies), Octroi and entry tax, Luxury Tax, and taxes on lotteries, betting and gambling ✅ owner.
- Outside GST: basic customs duty, stamp duty, property tax, electricity duty, state excise on alcohol for human consumption, and petroleum products (outside GST per owner's latest position) ✅ owner; verify petroleum status before treating it as settled.
**Cases / Committees / Schemes / Data:** 2019 GS-III PYQ on indirect taxes subsumed in GST (routed); 2018 Prelims PYQ on GST exemptions (routed). [basic/10 §5, §9]
**Trap:** "One Nation One Tax" with no exceptions is false; several large levies remain outside GST.
**Mains hook:** Enumerate subsumed taxes to show what GST simplified, then name the exclusions that keep the claim qualified.
**Back:** *"Many levies folded in; alcohol, petrol, stamp and power duties stayed out."*

### Flashcard T-058 — GST compensation guarantee and compensation cess
**Front:** What was the GST compensation guarantee, how did COVID-era loans extend the cess, and what is its status now?
**Definition (learn):** The GST (Compensation to States) Act, 2017 guaranteed states 14% annual revenue growth over the 2015-16 base for five years (2017–22), funded by a compensation cess on luxury and sin goods ✅ owner.
**Breakdown:**
- COVID-19 shortfall: back-to-back Centre loans of roughly ₹1.1 lakh crore (FY21) and ₹1.59 lakh crore (FY22) ✅ owner.
- Compensation cess collection was extended beyond June 2022 solely to service these loans; the owner records the extension through March 2026 ✅ owner.
- After the September 2025 reform, the cess was discontinued for most goods and continues on tobacco and pan masala until repayment ✅ owner.
- Post-repayment future of the cess is unsettled; verify the latest GST Council decision ✅ owner.
**Cases / Committees / Schemes / Data:** 2020 GS-III PYQ on the Compensation Act and COVID-19 impact (routed). [basic/10 §5, §9]
**Trap:** The compensation guarantee was transitional, not a permanent constitutional entitlement.
**Mains hook:** Transition assurance and crisis borrowing show fiscal federalism is about trust, not just tax design.
**Back:** *"Five years of guarantee, then loans, then a cess that outlived its promise."*

### Flashcard T-059 — Black money and the fiscal tax base
**Front:** Why is black money a fiscal problem, and which law targets undisclosed foreign assets?
**Definition (learn):** The Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015 targets undisclosed foreign income and assets ✅ owner.
**Breakdown:**
- Undisclosed income narrows the declared tax base, distorts allocation and weakens transparent budgeting ✅ owner.
- Enforcement alone cannot end illicit flows; information systems and compliance architecture matter ✅ owner.
- 2021 Prelims PYQ on black-money creation impact on the economy (routed; key unavailable locally). [basic/09 §9]
**Cases / Committees / Schemes / Data:** Owner-cited Black Money Act, 2015 [basic/09 §5].
**Trap:** Black money is separate from fiscal analysis is false; it directly affects the tax base and capacity.
**Mains hook:** Connect black money, compliance quality and domestic savings to the state's fiscal room.
**Back:** *"Hidden income shrinks the tax base the budget stands on."*

### GROUP — Finance Commissions and fiscal federalism

### Flashcard T-060 — Finance Commission: vertical and horizontal devolution
**Front:** What does the Finance Commission do, and how do vertical and horizontal devolution differ?
**Definition (learn):** The Finance Commission is a constitutional body under Article 280 (✅ Wikipedia 'Finance Commission of India': the President sets it up "within two years from the commencement of the Constitution and thereafter at the end of every fifth year or earlier"; a chairman and four other members) that recommends the distribution of tax revenue between the Centre and states, and among states, plus grants. It does not set GST rates ✅ owner.
**Breakdown:**
- Vertical devolution: the share of the divisible pool passed from the Centre to the states as a whole ✅ owner.
- Horizontal devolution: distribution of the states' share among states by criteria ✅ owner.
- Grants (Art 275: ✅ Wikipedia 'Finance Commission of India' lists Art 275 among the articles that "specify ways and means of sharing resources between the Union and States"; the grants mechanism itself ⚠️ standard) supplement devolution for specific needs.
- Earlier shares: 14th Finance Commission vertical share 42% ✅ (Wikipedia '15th Finance Commission': the government asked the 15th FC to review the 14th FC's hike "from 32 per cent to 42 per cent"); 15th recommended 41% ✅ owner.
**Cases / Committees / Schemes / Data:** 2023 Prelims PYQ on 15th FC horizontal tax devolution criteria (routed; key unavailable locally). [basic/10 §9]
**Trap:** The Finance Commission sets GST rates is false. Devolution is not every transfer; scheme-specific grants are separate.
**Mains hook:** Equalisation and incentives pull in opposite directions; examine whether the formula balances them.
**Back:** *"The Commission divides the pot: vertically between tiers, horizontally among states."*

### Flashcard T-061 — Fifteenth Finance Commission (2021–26): key recommendations
**Front:** What were the key recommendations of the 15th Finance Commission?
**Definition (learn):** The 15th Finance Commission recommended tax devolution and grants for the award period 2021–22 to 2025–26 ✅ (Wikipedia '15th Finance Commission': final report covers 2021-22 to 2025-26; tabled 1 February 2021).
**Breakdown:**
- Vertical devolution kept at 41% of the divisible pool ✅ owner (42% figure for the 14th FC confirmed ✅ Wikipedia; 41% for the 15th not independently re-fetched).
- Horizontal criteria: income distance, population, area, forest and ecology, demographic performance and tax effort ✅ owner; the numeric weights are ⚠️ not recorded in owners (verify).
- Tax effort reintroduced as a horizontal criterion ✅ owner.
- Education and agriculture-performance grants ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims Q66 on the 15th FC propositions: 41% (not 45%), education and agriculture-performance grants, and reintroduced tax effort (key on local file). [basic/10 §9]
**Trap:** A 45% vertical share is wrong for the 15th FC; the 2025 PYQ rejected it.
**Mains hook:** Demographic performance and tax effort reward discipline, but equalisation still matters for income-poor states; judge the mix.
**Back:** *"Forty-one is the vertical share; tax effort and demography shape the horizontal split."*

### Flashcard T-062 — Sixteenth Finance Commission (2026–31): status and accepted share
**Front:** What is the 16th Finance Commission's award period, and what is the accepted vertical share?
**Definition (learn):** The 16th Finance Commission's award covers 2026-27 to 2030-31 ✅ owner (✅ Wikipedia 'Finance Commission of India': period "2026 - 31"; constituted 31 December 2023; chair Arvind Panagariya). The accepted vertical share remains 41% of the divisible pool ✅ owner, per the official action-taken memorandum cited (⚠️ the fetched Wikipedia pages give no share for the 16th FC; verify the report and memorandum before quoting).
**Breakdown:**
- Horizontal criteria and grants: consult the report and action-taken memorandum; they are not reproduced in the owners ✅ owner.
- Composition and timelines: use the official Finance Commission documents, not commentary ✅ owner.
- The 16th FC continues the principle that devolution is periodically recalibrated rather than settled once ✅ owner.
**Cases / Committees / Schemes / Data:** Official action-taken memorandum (fincomindia, cited in owner) [basic/10 §8].
**Trap:** Do not assume the 15th FC's criteria carry over unchanged; check the 16th FC's own report.
**Mains hook:** Periodic recalibration shows fiscal federalism is a negotiated, evolving settlement.
**Back:** *"Sixteen runs the next five years; forty-one holds; read the memorandum for the rest."*

### Flashcard T-063 — Divisible pool, cesses and surcharges, and vertical imbalance
**Front:** How do cesses and surcharges change the divisible pool and state fiscal space?
**Definition (learn):** The divisible pool is the Union tax revenue that is shared with states under Article 270 (✅ partial: Wikipedia 'Finance Commission of India' lists Art 270 among the sharing articles; the pool definition ⚠️ standard). Cesses and surcharges generally sit outside this pool and are not shared through devolution ✅ owner.
**Breakdown:**
- Health and Education Cess is an example of a levy outside the ordinary divisible pool ✅ owner; the current rate is ⚠️ verify.
- Gross tax growth does not translate into equal untied resources for states when more revenue comes through cesses ✅ owner.
- Vertical imbalance: the Centre has the stronger tax base while states deliver most public services ✅ owner.
- Repeated cess reliance narrows state fiscal space and strains federal trust ✅ owner.
**Cases / Committees / Schemes / Data:** Health and Education Cess (owner example). [basic/10 §5]
**Trap:** All Union tax receipts enter the divisible pool identically is false.
**Mains hook:** Should cess reliance fall if cooperative federalism is to deepen? Use the divisible-pool logic, then weigh Union priorities.
**Back:** *"Cesses sit outside the pool, so pool growth is not the same as state growth."*

### Flashcard T-064 — Fiscal Health Index (NITI Aayog)
**Front:** What is the Fiscal Health Index, and what dimensions does it compare?
**Definition (learn):** The Fiscal Health Index is NITI Aayog's analytical tool for comparing state fiscal performance across several dimensions ✅ owner.
**Breakdown:**
- Dimensions per owner: own revenue mobilisation, quality of expenditure, fiscal prudence and debt sustainability ✅ owner.
- Use the dimensions and purpose, not uncertain rank snippets; rankings vary by year, data period and method ✅ owner.
- Headline rankings can hide differences in tax capacity, demography and inherited debt ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 GS-III PYQ (15 marks) on the Fiscal Health Index as a tool for state fiscal performance. [basic/09 §9; basic/10 §9]
**Trap:** Citing a state's rank without the year and method is a factual error risk.
**Mains hook:** Competitive federalism is measured through a basket of fiscal capabilities, not a single deficit ratio; use it to argue for quality of spending.
**Back:** *"Four pillars of state fiscal health: revenue, spending quality, prudence, debt."*

### GROUP — External sector: balance of payments, exchange rate and reserves

### Flashcard T-065 — Balance of payments accounts: current, capital and financial
**Front:** What do the current, capital and financial accounts record, and which flows sit where?
**Definition (learn):** The balance of payments records transactions between residents and non-residents. The current account covers goods, services and primary and secondary income. The capital account covers capital transfers and acquisition or disposal of non-produced non-financial assets. The financial account covers cross-border investment and reserve-asset transactions ✅ owner.
**Breakdown:**
- FDI, portfolio flows, loans (including ECBs) and NRI deposits enter the financial account ✅ owner.
- Remittances are transfers in the current account, not merchandise exports ✅ owner.
- A current-account deficit must be financed by net financial inflows, reserve use or accounting adjustment ✅ owner.
- Survey 2025-26: current-account deficit 0.8% of GDP in H1 FY26, down from 1.3% in H1 FY25 ✅ owner.
**Cases / Committees / Schemes / Data:** 2019 and 2020 Prelims PYQs on external-debt composition and FDI (routed; keys unavailable locally). [basic/19 §9]
**Trap:** A merchandise deficit equals a BoP deficit is false. The capital account does not hold most FDI and portfolio flows in modern accounting.
**Mains hook:** Preserve the capital-versus-financial account distinction; judge external risk by financing quality, not the CAD size alone.
**Back:** *"Goods and services feed the current account; cross-border investment feeds the financial one."*

### Flashcard T-066 — Exchange-rate regime: managed float and the impossible trinity
**Front:** What exchange-rate regime does India follow, and what constraint does the impossible trinity impose?
**Definition (learn):** A managed float is a market-determined exchange rate with RBI intervention to smooth excessive volatility, without targeting a fixed level ✅ owner. The impossible trinity states that a country can choose at most two of: a fixed exchange rate, free capital mobility and an independent monetary policy ✅ owner.
**Breakdown:**
- RBI intervention in FX markets absorbs or injects rupee liquidity unless sterilised, typically through OMOs ✅ owner.
- Nominal effective exchange rate and real effective exchange rate differ; REER adjusts for relative prices ✅ owner.
- Depreciation and appreciation describe market moves; devaluation and revaluation describe official parity changes ✅ owner.
- India manages the trinity through a managed float and calibrated capital-account openness ✅ owner.
**Cases / Committees / Schemes / Data:** 2022 Prelims PYQ on NEER and REER concepts (routed). [basic/19 §9]
**Trap:** A managed float is not a fixed peg. Sterilisation has a fiscal cost and cannot be sustained indefinitely at large scale ✅ owner.
**Mains hook:** Explain why India does not peg the rupee or fully open the capital account; name the trade-off each choice creates.
**Back:** *"Pick two of fixed, free and independent; India manages the float."*

### Flashcard T-067 — Forex reserves: composition, cover and what the data show
**Front:** What do forex reserves hold, and what are the latest owner-recorded figures?
**Definition (learn):** Forex reserves are external reserve assets held by the monetary authority ✅ owner. They typically include foreign-currency assets, gold, SDRs and the IMF reserve tranche position ⚠️ (standard composition; the owner names the reserve tranche as part of quota).
**Breakdown:**
- Forex reserves were USD 701.4 billion as of 16 January 2026 ✅ owner (Survey vintage).
- Import cover: 11.1 months as of 9 January 2026 ✅ owner.
- Reserves are a buffer; they do not remove oil dependence, export concentration or private foreign-currency risk ✅ owner.
- A large reserve stock is not a substitute for competitiveness ✅ owner.
**Cases / Committees / Schemes / Data:** Survey 2025-26 figures with the dates above. [basic/19 §8]
**Trap:** Reserves are government budget revenue is false; they are central-bank external assets with balance-sheet counterparts ✅ owner. Switzerland's gold-trade hub status does not imply large official gold reserves ✅ owner (2023 PYQ route).
**Mains hook:** Judge reserve adequacy by financing quality, debt maturity and currency composition; cite the date of every figure.
**Back:** *"Reserves are insurance, not income, and no cure for competitiveness."*

### Flashcard T-068 — The 1991 balance-of-payments crisis and its reforms
**Front:** What caused the 1991 balance-of-payments crisis, and which reforms followed?
**Definition (learn):** The 1991 crisis was a balance-of-payments crisis in which foreign-exchange reserves fell to a level covering only a few weeks of imports, requiring emergency IMF and gold-pledge support ✅ owner.
**Breakdown:**
- IMF conditionality required trade liberalisation, industrial delicensing, fiscal correction and exchange-rate reform ✅ owner.
- The gold pledge involved 67 tonnes ✅ (Wikipedia '1991 Indian economic crisis': 47 tonnes flown to the Bank of England and 20 tonnes to UBS, raising about $600 million; the same page reports reserves covering roughly three weeks of imports).
- Financial-sector reform followed through the Narasimham Committee I (1991) ✅ owner.
- India has not required IMF financial assistance since 1991 ✅ owner (verify current position).
**Cases / Committees / Schemes / Data:** Owner historical episode [basic/19 §5; basic/21 §5].
**Trap:** The 1991 episode does not show that current reserves are similarly precarious; the owner warns against that overstatement.
**Mains hook:** Reserves buy time; structural reforms and competitiveness provide durable resilience.
**Back:** *"Weeks of imports, a gold pledge, then reforms: reserves buy time, not competitiveness."*

### Flashcard T-069 — Shock channels: 2013 taper tantrum, 2020 COVID and Fed tightening
**Front:** How did the 2013 taper tantrum and the 2020 COVID shock transmit to India's external position?
**Definition (learn):** A taper tantrum is a capital-outflow shock triggered by signals of reduced asset purchases by a major central bank. The 2013 episode is the owner's example of the financial-account channel of BoP vulnerability ✅ owner.
**Breakdown:**
- 2013: US Fed tapering signal triggered capital outflows, sharp rupee depreciation, and RBI and government measures including special swap facilities to attract NRI deposits ✅ owner.
- 2020: a global demand shock produced a temporary current-account surplus because imports fell faster than exports and remittances, while reserves rose ✅ owner.
- Shock type matters: trade, financial-account or demand shocks each call for a different response ✅ owner.
- Fed tightening transmits to ECB costs through benchmark rates, currency mismatch and rollover risk ✅ owner.
**Cases / Committees / Schemes / Data:** 2022 Prelims PYQ on US Fed tightening, capital flight and ECBs (routed; key unavailable locally). [basic/19 §5A, §9]
**Trap:** Every crisis depletes reserves is false; the 2020 surplus was a temporary demand-collapse anomaly, not a structural improvement.
**Mains hook:** Compare 1991, 2013 and 2020 by transmission channel to show why external resilience depends on the type of shock.
**Back:** *"Taper rattles the capital, COVID shrinks the trade, 1991 drained the reserves."*

### Flashcard T-070 — External commercial borrowings (ECB) framework
**Front:** What are ECBs, who can borrow, and what risks do they carry?
**Definition (learn):** External commercial borrowings are loans and other permitted debt instruments raised by eligible resident entities from recognised non-resident lenders, governed by RBI's ECB framework under FEMA ✅ owner.
**Breakdown:**
- Eligible borrowers: resident entities other than individuals; recognised lenders: non-resident persons other than individuals, including multilateral institutions and export-credit agencies ✅ owner.
- Minimum average maturity period and end-use restrictions apply; proceeds cannot fund real-estate speculation, capital-market or margin trading unless permitted ✅ owner.
- The MAMP years, USD limit and cost ceiling have been revised in RBI rounds; cite only the dated Master Direction ✅ owner (figures ⚠️ verify).
- ECBs are distinct from concessional official assistance and from FPI portfolio debt ✅ owner.
**Cases / Committees / Schemes / Data:** 2022 Prelims PYQ on ECBs and Fed tightening (routed). [basic/19 §5A]
**Trap:** ECBs can be used for any purpose is false; depreciation raises the rupee cost of unhedged ECB servicing.
**Mains hook:** Prudent foreign-currency borrowing needs hedging, maturity matching and end-use discipline.
**Back:** *"ECBs borrow in dollars; a weaker rupee makes the same debt heavier."*

### Flashcard T-071 — Trade remedies and Foreign Trade Policy 2023
**Front:** What are anti-dumping, countervailing and safeguard duties, and what did FTP 2023 change?
**Definition (learn):** Anti-dumping duty addresses injury from dumped imports; countervailing duty addresses injury from subsidised imports; a safeguard addresses serious injury from an import surge without a dumping finding ✅ owner.
**Breakdown:**
- DGTR investigates anti-dumping, countervailing and safeguard cases under trade-remedy law ✅ owner.
- DGTR recommendations take effect only after government notification; remedies are time-bound and reviewable ✅ owner.
- FTP 2023 (effective 1 April 2023) replaced FTP 2015–20 and emphasises procedural ease, digitalisation and remission-based, WTO-compatible support ✅ owner.
- Edible-oil customs duty has been raised to protect oilseed farmers and cut to ease consumer inflation within the same policy cycle ✅ owner.
**Cases / Committees / Schemes / Data:** 2018 Prelims PYQ on imported edible oils versus domestic production and customs duty (routed; key unavailable locally). [basic/20 §5A, §9]
**Trap:** Anti-dumping is not a general safeguard against all imports ✅ owner. A safeguard does not need a dumping finding.
**Mains hook:** Time-bound protection is justified only where learning or strategic spillovers are demonstrable; defend this in any protectionism answer.
**Back:** *"Dumping, subsidy, surge: three remedies, three different tests."*

### GROUP — WTO, trade agreements and climate-linked trade barriers

### Flashcard T-072 — WTO agreements: AoA, TRIPS, TRIMS, GATS, SPS/TBT and TFA
**Front:** Which WTO agreement governs which subject, and what does each prohibit or protect?
**Definition (learn):** The WTO (established 1 January 1995 ✅ Wikipedia) administers multilateral agreements on trade in goods, services and intellectual property, plus dispute settlement ✅ owner (structure). Named agreements below.
**Breakdown:**
- Agreement on Agriculture (AoA): disciplines domestic support (boxes, Aggregate Measurement of Support, de minimis) and export subsidies ✅ owner (cross-owner basic/28 §8).
- TRIPS: minimum intellectual-property standards; it does not itself grant a patent ✅ owner.
- TRIMS: GATT-linked; prohibits local-content and trade-balancing investment measures under GATT Articles III and XI; it does not ban FDI as such ✅ owner.
- GATS: services supplied across borders, through consumption abroad, commercial presence or movement of persons ✅ owner.
- SPS (sanitary and phytosanitary) and TBT (technical barriers to trade) govern standards and technical regulations ⚠️ (standard).
- Trade Facilitation Agreement (TFA): customs and border procedures; entered into force 22 February 2017 (✅ WTO TFA page: "entered into force on 22 February 2017 after two-thirds of the WTO membership completed their domestic ratification process"; the Bali adoption is ✅ Wikipedia).
**Cases / Committees / Schemes / Data:** 2020 Prelims PYQ on TRIMS (routed; key unavailable locally); 2024 GS-III PYQ on IPR in life materials and patent commercialisation (routed). [basic/20 §5A, §9]
**Trap:** TRIMS bans foreign investment is false. TRIPS grants patents is false. GATS is not an IP agreement; TRIMS is not a services agreement.
**Mains hook:** IP answers should separate TRIPS minimum standards from domestic commercialisation, which depends on research quality, finance and market discovery.
**Back:** *"Agriculture supports, IP minima, goods investment rules, services four ways, and the safety and customs add-ons."*

### Flashcard T-073 — WTO ministerial outcomes relevant to India
**Front:** What were the major WTO ministerial outcomes relevant to India's agriculture, food security and trade?
**Definition (learn):** Ministerial conferences adopt package decisions that complete or extend the WTO's rulebook. Only the outcomes below are relevant and their verification status is noted.
**Breakdown:**
- MC9, Bali (December 2013): Trade Facilitation Agreement adopted and the interim Peace Clause on public stockholding for food security ✅ owner (Peace Clause from Bali 2013); TFA adoption ✅ (Wikipedia 'Trade Facilitation Agreement': confirmed at the Ninth Ministerial Conference, Bali, December 2013). TFA entry-into-force date 22 February 2017 ✅ (WTO TFA page, see T-072).
- MC10, Nairobi (15–19 December 2015; ✅ WTO MC10 page): Nairobi Package with the Export Competition decision (WT/L/980): developed members "shall immediately eliminate their remaining scheduled export subsidy entitlements"; developing members "by the end of 2018", with a footnote-5 exception to the end of 2022 for certain products (✅ WTO decision text, paras 6–7 and footnote 5; corrected from an unsourced general statement).
- MC12, Geneva (12–17 June 2022; ✅ WTO MC12 page): Agreement on Fisheries Subsidies (WT/MIN(22)/33) adopted in the "Geneva package" (✅); its entry-into-force status is not on the fetched page ⚠️ verify. The e-commerce moratorium decision (WT/MIN(22)/32) is ✅ listed, but its terms are ⚠️ not retrieved.
- MC13, Abu Dhabi (26 February – 2 March 2024; ✅ WTO MC13 page dates): e-commerce moratorium extension and no permanent public-stockholding solution ⚠️ (the fetched WTO page gives dates only; outcome documents not reached); the owner confirms no permanent solution as of the latest confirmed ministerial outcome ✅ owner.
- MC14, Yaoundé (26–30 March 2026; ✅ WTO MC14 page body, whose header reads "26 - 29 March" and mislabels the page "Thirteenth"); the WTO page confirms the meeting in Yaoundé and that ministers "adopted decisions" (WTO news item, 30 March); the specific e-commerce, fisheries and public-stockholding outcomes were not retrieved ⚠️. Do not cite a substantive outcome without checking the official WTO record.
**Cases / Committees / Schemes / Data:** Owner statement: India and G-33 have sought a permanent public-stockholding solution; interim Peace Clause protection remains ✅ owner (basic/20 §5).
**Trap:** The Bali Peace Clause is an interim protection, not a permanent solution ✅ owner. A permanent solution is not concluded.
**Mains hook:** MSP-based procurement can conflict with AMS and external-reference-price methods; the answer must state the interim-protection status precisely.
**Back:** *"Bali gave a shield, Nairobi cut export subsidies, and public stockholding still waits for a permanent fix."*

### Flashcard T-074 — WTO dispute settlement: Appellate Body paralysis and the MPIA
**Front:** Why is WTO binding dispute settlement impaired, and what workaround do some members use?
**Definition (learn):** The Appellate Body has been unable to hear new appeals since December 2019 because appointments were blocked, leaving the appellate stage without quorum ✅ owner. The Multi-Party Interim Appeal Arbitration Arrangement (MPIA), established in 2020, is an alternative appeal route among participating members ✅ owner.
**Breakdown:**
- Panels still issue first-level rulings; only the binding appeal stage is removed ✅ owner.
- India has not joined the MPIA ✅ owner (verify current membership and reasons from a dated source).
- Disputes can therefore lack a binding appellate remedy, weakening enforcement predictability ✅ owner.
**Cases / Committees / Schemes / Data:** Owner-verified WTO appellate status (WTO appellate page, cited in owner) [basic/20 §5, §6A].
**Trap:** WTO dispute settlement has fully collapsed is false; first-level panels continue.
**Mains hook:** Bilateralism is a partial substitute for a functioning multilateral system; argue for reform rather than withdrawal.
**Back:** *"Panels still speak, appeals stall, and India stays out of the side-door court."*

### Flashcard T-075 — EU Carbon Border Adjustment Mechanism (CBAM)
**Front:** What is the EU CBAM, which sectors does it cover, and why does India contest it?
**Definition (learn):** The EU Carbon Border Adjustment Mechanism requires importers into the EU of specified carbon-intensive goods to account for the embedded emissions of those goods, through certificates priced against the EU Emissions Trading System ✅ owner.
**Breakdown:**
- Covered sectors: cement, iron and steel, aluminium, fertilisers, hydrogen and electricity ✅ owner.
- Definitive, financially enforceable regime from 1 January 2026 after a 2023–25 reporting-only transitional phase ✅ owner (✅ Wikipedia 'Carbon Border Adjustment Mechanism': reporting from 2023; regime took effect in 2026; exact 2023–25 phase years not restated on the fetched page).
- Omnibus simplifications (for example a 50-tonne annual de-minimis import exemption and deadline changes) per the owner ✅ owner; verify from the Commission's CBAM pages.
- India's objections: WTO non-discrimination concerns under GATT most-favoured-nation and national-treatment rules, and climate-equity objection under CBDR-RC ✅ owner. India raised WTO consultations in 2024 ✅ owner.
- CBAM cost is not a fixed tariff rate; it depends on product emissions intensity and the EU ETS price ✅ owner.
**Cases / Committees / Schemes / Data:** Owner status dated August 2026; verify current EU implementation ⚠️.
**Trap:** CBAM is a normal tariff with a fixed percentage is false. CBAM is not an Indian carbon-market instrument.
**Mains hook:** Treat CBAM as both a trade and a climate question: give the WTO-consistency and CBDR-equity tracks, then the limits of the evidence.
**Back:** *"Carbon is priced at the border; India argues the price breaks both the trade rules and the equity principle."*

### Flashcard T-076 — FTAs, rules of origin and India's RCEP exit
**Front:** How do FTAs differ, what do rules of origin do, and why did India leave RCEP negotiations?
**Definition (learn):** An FTA reduces trade barriers among members under agreed coverage and rules. Rules of origin define where a product originates to qualify for preferential treatment ✅ owner.
**Breakdown:**
- India–UAE CEPA: in force May 2022 ✅ owner.
- India–Australia ECTA: in force December 2022 ✅ owner.
- India–EFTA (Iceland, Liechtenstein, Norway, Switzerland) TEPA: in force 1 October 2025 ✅ owner.
- India withdrew from RCEP negotiations in November 2019, citing trade-deficit, goods and dairy access, and safeguard concerns ✅ owner.
- Naming: CEPA, CECA and ECTA are labels for different agreement types; verify each agreement's scope ⚠️.
- The "noodle-bowl" effect: many rules-of-origin regimes raise compliance costs for exporters ✅ owner.
**Cases / Committees / Schemes / Data:** Owner-dated agreements above [basic/20 §5].
**Trap:** An FTA means zero duty on every product immediately is false; coverage, schedules and exclusions vary. Rules of origin are not tariffs.
**Mains hook:** Selective bilateralism reduces exposure to contested concessions but forgoes regional value-chain integration; weigh both.
**Back:** *"FTAs are deals with origin rules; India walked away from RCEP in 2019."*

### Flashcard T-077 — India–UK CETA and India–EU FTA: dated status
**Front:** What is the status of India's UK and EU trade agreements, as recorded in the owners?
**Definition (learn):** A comprehensive economic and trade agreement (CETA) covers goods, services, investment and related rules ⚠️ standard. The India–UK CETA and India–EU FTA are the two most significant recent negotiations recorded in the owners ✅ owner.
**Breakdown:**
- India–UK CETA: signed 24 July 2025; entered into force 15 July 2026 after a delay linked to UK steel-safeguard concerns ✅ owner (status as of August 2026 per owner; ✅ entry-into-force date and signing date confirmed by Wikipedia 'India–United Kingdom CETA' citing Reuters, 17 June 2026; the steel-assurance link is reported by Reuters, not confirmed in full text).
- India–EU FTA: negotiations concluded on 27 January 2026 (✅ EU Commission trade page: "On 27 January 2026, the EU and India concluded negotiations for a Free Trade Agreement"; Wikipedia 'India–European Union Free Trade Agreement' gives the same date). On 11 September 2026 the Commission presented it to the Council "for signature" (✅ EU Commission page). The owner's "technical level" wording and the "signature targeted before end-2026" timing are not confirmed by these sources (⚠️); no signature or ratification is reported in the fetched pages.
- Separate Investment Protection Agreement and Geographical Indications agreement remained under negotiation ✅ owner.
- Verify any development after August 2026 from a dated official source ⚠️ (owner caution).
**Cases / Committees / Schemes / Data:** Owner-dated status [basic/20 §5].
**Trap:** Concluded technically is not signed; signed is not in force; in force is not utilised by exporters.
**Mains hook:** Bilateral diversification is an answer to protectionism only if utilisation and rules of origin are managed; examine both.
**Back:** *"Concluded is not signed; signed is not in force; in force is not yet used."*

### GROUP — International financial institutions and global governance

### Flashcard T-078 — IMF: quotas, SDRs, reserve tranche and lending facilities
**Front:** How do IMF quotas, SDRs, the reserve tranche and the Rapid Financing Instrument work?
**Definition (learn):** A quota is a member's subscription that determines its financial contribution, voting weight and access limits ✅ owner. The SDR is an IMF-created reserve asset valued from a currency basket; it is not a currency in circulation and not an IMF loan ✅ owner.
**Breakdown:**
- The reserve tranche position (RTP) is the same concept as the gold tranche under old and current names; drawing on it is a withdrawal of the member's own reserve contribution, not a new loan ✅ owner.
- RFI gives single, low-conditionality emergency disbursement; Stand-By and Extended Fund Facilities are phased, conditionality-linked programmes ✅ owner.
- Current SDR basket: US dollar, euro, Chinese renminbi, Japanese yen and pound sterling ✅ (Wikipedia 'Special Drawing Rights': five currencies; weights as of August 2023 were USD 43.38%, EUR 29.31%, CNY 12.28%, JPY 7.59%, GBP 7.44%; IMF reviews the basket every five years; the 2022 re-evaluation took effect 1 August 2022). These are the weights of the 2022–27 basket as stated on Wikipedia; the IMF's own current valuation was not reached, so quote them as "as of August 2023" ✅ and treat any later figure as ⚠️ unverified.
- Quota reviews have been contested in pace and adequacy ✅ owner; India's current quota share is not recorded in owners ⚠️ verify.
- India has no active IMF programme ✅ owner (verify).
**Cases / Committees / Schemes / Data:** 2020 Prelims PYQ on gold tranche and reserve tranche (routed); 2022 Prelims PYQ on RFI (routed). [basic/21 §5, §9]
**Trap:** Gold tranche and reserve tranche are two facilities is false; RTP is not IMF borrowing; the RFI is not a Stand-By.
**Mains hook:** Conditionality protects credibility and repayment but raises ownership and social-cost debates; distinguish programme types before judging.
**Back:** *"Quota pays in, SDR is the reserve asset, and the reserve tranche is your own money."*

### Flashcard T-079 — World Bank Group: IBRD, IDA, IFC and MIGA
**Front:** How do IBRD, IDA, IFC and MIGA differ in clients, terms and instruments?
**Definition (learn):** "World Bank" commonly refers to IBRD and IDA ✅ owner. IBRD lends to creditworthy middle-income and eligible sovereign borrowers on near-market terms. IDA gives concessional loans, credits and grants to the poorest eligible countries ✅ owner. IFC finances private-sector development. MIGA provides political-risk guarantees ✅ owner.
**Breakdown:**
- Eligibility for IBRD versus IDA depends on per-capita income and creditworthiness, which can change over time ✅ owner.
- IBRD is the anchor of the 2025 Prelims PYQ on the World Bank's lending arm ✅ owner (key on local file).
- The International Centre for Settlement of Investment Disputes is a fifth Bank Group body ⚠️ (standard).
- Multilateral guarantees mobilise private capital, but crowding-in is not automatic ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQ on IBRD (key on local file; answer not recorded here). [basic/21 §9]
**Trap:** IDA and IFC are identical is false. IDA lends to sovereigns on concessional terms; IFC lends to private firms.
**Mains hook:** Compare institutions through mandate, client, instrument and governance rather than as one generic "global finance" bucket.
**Back:** *"IBRD lends to governments, IDA gives soft money, IFC backs firms, MIGA insures risk."*

### Flashcard T-080 — ADB, AIIB and NDB: regional and BRICS development banks
**Front:** How do the Asian Development Bank, the Asian Infrastructure Investment Bank and the New Development Bank differ?
**Definition (learn):** ADB is a regional development bank focused on Asia and the Pacific, headquartered in Manila ✅ owner (India is a founding member ✅ owner). AIIB is an infrastructure-focused multilateral bank founded in 2016 and headquartered in Beijing ✅ owner. NDB is the BRICS-founded bank financing infrastructure and sustainable development, headquartered in Shanghai ✅ owner.
**Breakdown:**
- India is among the largest shareholders in AIIB ✅ owner; the five NDB founders have equal initial shareholding ✅ owner, and membership has since expanded ✅ owner.
- ADB launched the Nature Solutions Finance Hub for Asia and the Pacific at COP28 (December 2023) to mobilise blended finance for nature-based solutions ✅ owner.
- AIIB and NDB complement, rather than replace, the World Bank and ADB ✅ owner.
- Equal founding shareholding does not mean equal borrowing or influence ✅ owner.
**Cases / Committees / Schemes / Data:** 2025 Prelims PYQ on the launcher of the Nature Solutions Finance Hub (key on local file); 2019 Prelims PYQ on AIIB membership (routed). [basic/21 §9]
**Trap:** AIIB and NDB replace the World Bank is false. The Nature Solutions Hub is not a UN or government initiative ✅ owner.
**Mains hook:** Plural multilateral finance expands choice but can fragment standards; argue for reformed multilateralism rather than fragmentation.
**Back:** *"ADB is Asia's regional bank, AIIB its infrastructure partner, NDB the BRICS-founded bank."*

### Flashcard T-081 — G20 Common Framework versus the DSSI
**Front:** How does the G20 Common Framework for Debt Treatment differ from the Debt Service Suspension Initiative (DSSI)?
**Definition (learn):** The DSSI (2020) gave eligible low-income countries a temporary suspension of official bilateral debt-service payments and formally ended in December 2021 ✅ owner. The G20 Common Framework (agreed November 2020) aims at case-by-case debt restructuring for eligible low-income countries that request it ✅ owner.
**Breakdown:**
- The Common Framework coordinates official bilateral creditors, including non-Paris Club creditors such as China, and seeks comparable treatment from private creditors ✅ owner.
- Only a small number of countries have processed cases (owner cites Chad, Zambia, Ethiopia and Ghana as of the latest confirmed reporting) ✅ owner (verify current status).
- Implementation is slow and uneven, with transparency and creditor-coordination gaps ✅ owner.
**Cases / Committees / Schemes / Data:** 2022 Prelims PYQ on the Common Framework (routed; key unavailable locally). [basic/21 §5, §9]
**Trap:** The Common Framework is the same as the DSSI is false; the Common Framework has not resolved most eligible countries' debt distress.
**Mains hook:** Sovereign debt governance requires restructuring with creditor coordination; a suspension alone is temporary relief.
**Back:** *"Pause is the DSSI; restructure is the Common Framework."*

## B. IMPORTANT TOPICS — Agriculture, Industry, Infrastructure, Social Sector, Digital, Climate and Energy

Source key: ✅ = verified in repository owner (Economy basic/advanced 11–18, 22–25, 27–31); ⚠️ = general knowledge or outside the owner's as-of data; re-verify before quoting any figure or date. Status-sensitive figures carry their owner as-of date.

### GROUP — Land reform, cropping and agrarian technology

### Flashcard T-101 — Land reform package (zamindari abolition, tenancy, ceilings, consolidation)
**Front:** What are the components of India's post-Independence land reform, and why is land reform more than redistribution?
**Definition (learn):** Land reform is institutional change in ownership, tenancy, ceilings, consolidation of holdings and land records, aimed at tenure security, equity and farm productivity.
**Breakdown:**
- ✅ Abolition of intermediaries (zamindari, jagirdari, inamdari): removed rent-collecting layers between the state and the cultivator; implemented by state Acts from the 1950s.
- ✅ Tenancy reform: regulation of rent, security of tenure, and recording of actual cultivators (bhumidari/ownership conferral in some states ⚠️).
- ✅ Land ceilings: maximum holding per family, with surplus land vested in the state and redistributed; exemptions and benami transfers blunted outcomes.
- ✅ Consolidation of holdings: merging scattered plots into compact units to cut fragmentation and boost irrigation and mechanisation.
- ✅ Land records: determine whether rights on paper become enforceable titles.
- ✅ Land is a State subject (State List), so reform pace varied sharply across states ⚠️ (Entry 18, State List).
**Cases / Committees / Schemes / Data:** ✅ Kerala Land Reforms Act (tenancy and ceilings, comparatively thorough); ✅ J&K Big Landed Estates Abolition Act, 1950; ✅ Punjab-style consolidation and Kerala as contrasting outcomes; ⚠️ 1951 First Constitutional Amendment (Art. 31A/31B, Ninth Schedule) protected reform laws from judicial challenge.
**Trap:** Land reform is not only redistribution. Statutes do not equal outcomes: records, litigation, exemptions and administrative capacity decide the field result. Ceilings and tenancy are different instruments.
**Mains hook:** Why have land reforms underdelivered for tenants and small farmers despite strong statutes? Qualify: records-linked reform and secure leasing matter more than ceilings alone.
**Back:** *"Abolish, register, cap, consolidate — and only then is the land 'reformed'."*

### Flashcard T-102 — Bhoodan–Gramdan and Operation Barga (voluntary redistribution and tenancy registration)
**Front:** How do Bhoodan/Gramdan and Operation Barga differ as land-reform episodes?
**Definition (learn):** Bhoodan and Gramdan were voluntary land-gift movements led by Vinoba Bhave; Operation Barga was a state-driven drive to record and protect sharecroppers (bargadars).
**Breakdown:**
- ✅ Bhoodan (launched 1951 by Vinoba Bhave; first gift 18 April 1951 at Pochampally, Nalgonda district) sought voluntary donation of land by landowners; Gramdan (from 1952; first gramdan village Mangroth, Hamirpur district, UP) extended this to village-level common ownership (✅ Wikipedia, Bhoodan Movement).
- ✅ Operation Barga (West Bengal) focused on recording bargadars so that tenure security and bargaining power improved (✅ Wikipedia, Operation Barga: launched 1978; sharecroppers recorded, protected against eviction, with hereditary rights).
- ✅ Barga is a tenancy-registration example, not a Green Revolution technology example.
**Cases / Committees / Schemes / Data:** ⚠️ Bhoodan yields were largely poor-quality or contested land (Wikipedia reports encroachment on Bhoodan land but gives no quality assessment; unverified); ✅ Operation Barga is the standard named tenancy-security example in the owner.
**Trap:** Voluntary donation (Bhoodan) is not compulsory ceiling redistribution. Operation Barga is about recorded cultivators, not about buying or transferring land titles wholesale.
**Mains hook:** Compare voluntary and legal routes to redistribution; conclude that enforceable records, not goodwill, secure tenants.
**Back:** *"Vinoba asked, Barga recorded: one begs the owner, the other names the sharecropper."*

### Flashcard T-103 — Digital land records and DILRMP
**Front:** What is the Digital India Land Records Modernisation Programme, and why does it matter for agriculture?
**Definition (learn):** DILRMP is a central programme to digitise land records, computerise registration, and create a reliable, updated cadastral and title system.
**Breakdown:**
- ⚠️ Run by the Department of Land Resources (Ministry of Rural Development); launched 2008 and revamped later.
- ⚠️ Components: digitisation of textual records, cadastral survey/resurvey, computerisation of registration, and integrated title/parcel identifiers.
- ✅ Land-linked registries (AgriStack-style farmer IDs) depend on clean land records; tenants and sharecroppers are excluded when records are outdated.
**Cases / Committees / Schemes / Data:** ✅ Owner 27 places geo-referenced village maps as a building block of AgriStack; ⚠️ state portals (e.g., Bhulekh-type) are the citizen-facing layer.
**Trap:** Digitisation of records does not automatically give tenure security; legal title and the state's dispute-resolution system still decide it. DILRMP is not AgriStack itself.
**Mains hook:** Argue that land-record digitisation is a precondition for credit, insurance and PM-KISAN-type eligibility, with the caution that it can exclude unrecorded tenants.
**Back:** *"Scan the record, fix the parcel, then trust the title."*

### Flashcard T-104 — Green Revolution
**Front:** What was the Green Revolution, and what package made it work?
**Definition (learn):** A seed–water–fertiliser–credit–extension technology package (high-yielding semi-dwarf varieties) that sharply raised wheat and rice yields from the 1960s.
**Breakdown:**
- ✅ Semi-dwarf wheat derived from the Norin-10 line, used by Norman Borlaug in Mexico, and IR8 semi-dwarf rice from IRRI were adapted for Indian conditions at IARI under M.S. Swaminathan's leadership. ✅ Norin-10 itself was bred in Japan (Iwate Prefecture, by Gonjiro Inazuka) and Borlaug worked with it at CIMMYT in Mexico; the owner's phrasing 'bred by Borlaug' should be read as 'used/adapted by Borlaug' (✅ Wikipedia: Norin 10).
- ✅ Complementary inputs: irrigation, fertiliser, extension, credit and assured procurement; seed alone was insufficient.
- ✅ Gains concentrated in Punjab, Haryana and western Uttar Pradesh, in wheat and rice.
- ✅ Side effects: groundwater depletion, nutrient imbalance, regional and crop concentration.
**Cases / Committees / Schemes / Data:** ✅ Named scientist anchors: Swaminathan (adaptation at IARI), Borlaug and IRRI (parallel global role). ✅ Owner notes Visvesvaraya's irrigation engineering is a separate strand.
**Trap:** Green Revolution was not uniformly national or crop-neutral; it was not a seed-only story; and it did not credit one person alone. Do not confuse with the Second or Evergreen concept (T-105).
**Mains hook:** Credit the package, then qualify with regional inequality and water/soil stress; conclude that the next phase must be sustainability-led.
**Back:** *"Seed, water, fertiliser, credit: the four legs; drop one and the table tips."*

### Flashcard T-105 — Second Green Revolution and Evergreen Revolution
**Front:** How do the 'Second Green Revolution' and 'Evergreen Revolution' differ from the original Green Revolution?
**Definition (learn):** Both are post-Green-Revolution frames for raising productivity sustainably: yield growth without ecological exhaustion, extended to rainfed and eastern regions.
**Breakdown:**
- ⚠️ 'Second Green Revolution' is a policy-speech term for productivity growth in eastern and rainfed India (Bihar, West Bengal, Odisha, Assam, eastern UP) rather than only Punjab–Haryana. (Wikipedia's 'Second Green Revolution' section confirms declining yield rates and alternatives such as SRI, marker-assisted selection and agroecology, but gives no eastern/rainfed geography.)
- ✅ 'Evergreen Revolution' was coined by M.S. Swaminathan in 1990 (he dates the idea to 1968) for productivity in perpetuity without ecological harm (✅ Wikipedia, Evergreen Revolution).
- ✅ Owner 11: second-generation agrarian policy must move from output maximisation to sustainability and farm viability.
**Cases / Committees / Schemes / Data:** ✅ National Commission on Farmers (Swaminathan chair) as a named anchor for productivity-with-income-security; ⚠️ exact year and definition of these terms should be quoted from the source document used.
**Trap:** These are concepts or policy framings, not official schemes with an outlay. Do not present them as statutory categories.
**Mains hook:** Argue that a second-generation revolution must shift from water- and fertiliser-intensive yields to resource-use efficiency and farm income.
**Back:** *"Evergreen means yield that stays green for the next generation."*

### Flashcard T-106 — Cropping seasons, cropping intensity and cropping pattern
**Front:** What are India's crop seasons, and how is cropping intensity measured?
**Definition (learn):** Cropping pattern is the distribution of cultivated area among crops; cropping intensity is gross cropped area as a share of net sown area.
**Breakdown:**
- ✅ Kharif: monsoon-season crop (sown around June–July, harvested Sept–Oct; e.g., paddy, bajra, jowar, cotton, soybean, groundnut, tur).
- ✅ Rabi: winter crop (sown Oct–Nov, harvested Mar–Apr; e.g., wheat, gram, mustard, barley, masur).
- ⚠️ Zaid: summer crop on irrigated land (e.g., watermelon, cucumber, moong in some regions).
- ✅ Formula (⚠️ standard): Cropping intensity (%) = Gross cropped area ÷ Net sown area × 100. Worked example: GCA 150 lakh ha, NSA 100 lakh ha → intensity 150%.
- ✅ Black gram and green gram are commonly kharif pulses, with regional summer/irrigated exceptions.
**Cases / Committees / Schemes / Data:** ✅ Kharif area is monsoon-linked; use official seasonal estimates for year-specific acreage.
**Trap:** Cropping intensity above 100% means area sown more than once, not higher yield. Kharif/rabi are seasons, not crop categories. Paddy and sugarcane are water-intensive in policy debate, but not universally.
**Mains hook:** Link high cropping intensity to marketed surplus and to groundwater stress; conclude with a diversification route tied to procurement and water budgets.
**Back:** *"Kharif sows with the rain, rabi with the cold, zaid with the canal."*

### Flashcard T-107 — Millets, 'Shree Anna' and crop diversification
**Front:** Why are millets treated as a policy lever for crop diversification?
**Definition (learn):** Millets are small-seeded, dryland/rainfed, short-duration cereals (jowar, bajra, ragi and minor millets) that need little water and are nutritionally dense.
**Breakdown:**
- ✅ Traits: C4 photosynthesis, drought tolerance, roughly 60–100-day duration, low water and input needs; rich in fibre, protein, iron and calcium with a low glycemic index.
- ✅ Budget 2023 branded millets 'Shree Anna'; 2023 was the UN International Year of Millets (India-proposed).
- ✅ National Food Security Mission–Nutri-Cereals sub-mission is the production route (owner 12, as-of).
**Cases / Committees / Schemes / Data:** ✅ Minor millets named in owner: foxtail, kodo, little, proso, barnyard.
**Trap:** Millets are not automatically cheaper or higher-yielding; revival depends on MSP depth, processing and demand, not branding alone. Millets ≠ pulses.
**Mains hook:** Argue that millets serve nutrition, climate and groundwater goals at once, but qualify with the procurement and processing gap.
**Back:** *"Thirsty crop, big nutrition: millets are the diversification the rice-wheat belt needs."*

### GROUP — Minimum support price, procurement and food security

### Flashcard T-108 — Minimum support price: process, crop coverage and the 22+1 count
**Front:** How is MSP recommended and announced, and which crops does it cover?
**Definition (learn):** MSP is an announced price floor meant to give a price signal and downside protection; it is not a universal legal purchase guarantee.
**Breakdown:**
- ✅ Commission for Agricultural Costs and Prices (CACP) recommends; Cabinet Committee on Economic Affairs (CCEA) announces.
- ✅ Coverage per owner 12: 7 cereals, 5 pulses, 7 oilseeds and cotton, jute, copra; sugarcane's price is an FRP (T-111).
- ✅ Official count: MSP is notified for 22 crops plus sugarcane's FRP, giving 23 commodities (✅ Wikipedia, 'Minimum support price': "a total of 23 commodities are covered by MSP mechanism", including FRP for sugarcane). The split matches owner 12's list (7 cereals + 5 pulses + 7 oilseeds + 4 commercial crops incl. sugarcane). The current-season notification has not been checked.
- ✅ Actual procurement depends on crop, region, quality, arrivals and agency reach.
**Cases / Committees / Schemes / Data:** ✅ Owner 12 (as-of 2025-26 anchor; verify). Rabi and Kharif MSPs are announced separately.
**Trap:** 'MSP for 23 crops' is not 'MSP for all crops' and not 'a legal guarantee'. Most fruits, vegetables and many minor crops have no MSP. Sugarcane is FRP, not CACP MSP.
**Mains hook:** Evaluate MSP as a price signal backed by procurement; qualify by regional concentration and the water-intensive cereal bias it reinforces.
**Back:** *"Recommend by CACP, announce by CCEA, procure where the FCI reaches."*

### Flashcard T-109 — CACP cost concepts (A2, A2+FL, C2) and the C2+50% debate
**Front:** What do A2, A2+FL and C2 mean, and how do they relate to MSP?
**Definition (learn):** A2 = actual paid-out cost; A2+FL = A2 plus imputed value of unpaid family labour; C2 = A2+FL plus imputed rent on owned land and imputed interest on owned fixed capital.
**Breakdown:**
- ✅ A2: seed, fertiliser, hired labour, irrigation, fuel and similar cash costs.
- ✅ A2+FL: adds family labour at an imputed wage.
- ✅ C2: adds owned land rent and interest on owned capital; the most comprehensive base.
- ⚠️ Government MSP is generally pegged to a margin over A2+FL (the stated policy is 1.5 times A2+FL; Wikipedia, Minimum support price, records only the 2018 Union Budget announcement of MSP at 50% more than 'production cost' and does not define the cost base, so the A2+FL base is still unverified).
- ✅ Farmer bodies demand C2+50%, which uses the C2 base.
**Worked example (illustrative):** If A2+FL = ₹1,000/quintal, MSP at 1.5× = ₹1,500. If C2 = ₹1,300/quintal, C2+50% = ₹1,950. The gap (₹450) is the 'remuneration' dispute.
**Cases / Committees / Schemes / Data:** ✅ CACP surveys per crop and state; cost data are averages and vary by year.
**Trap:** A2, A2+FL and C2 are not interchangeable. Saying 'MSP gives 50% margin' and 'MSP under-compensates' can both be true depending on the base.
**Mains hook:** Name the cost base before judging adequacy; conclude that a C2-based MSP raises farmer income but raises fiscal and market-distortion costs.
**Back:** *"Paid, family, then owned: each C adds the costs the farmer never writes on a bill."*

### Flashcard T-110 — Swaminathan Commission (National Commission on Farmers)
**Front:** What was the Swaminathan Commission, and what did its farmer-welfare logic add to MSP debates?
**Definition (learn):** The National Commission on Farmers (NCF), chaired by M.S. Swaminathan, examined farm productivity, income security and sustainability for farmers.
**Breakdown:**
- ✅ NCF is named in the owner as a farmer-centred anchor linking productivity, income security and ecology.
- ✅ NCF submitted five reports between December 2004 and 4 October 2006 (✅ Wikipedia, National Commission on Farmers). ⚠️ NCF recommended MSP at a level of C2 plus 50% (i.e., at least 50% above the comprehensive cost), which became the farmer-movement benchmark; the Wikipedia page has no MSP recommendation, so this stays unverified.
- ✅ Owner 11 treats NCF as a bridge from productivity to viability; it is advisory.
**Cases / Committees / Schemes / Data:** ✅ NCF chairmanship; ✅ 2004–06 years; ⚠️ C2+50% recommendation (verify wording in the report).
**Trap:** NCF is advisory and its recommendations are not statutory. The 'C2+50%' demand is linked to NCF but is not identical to the government's policy (A2+FL based MSP).
**Mains hook:** Use NCF as the bridge from productivity to income security; qualify that advisory recommendations depend on fiscal and procurement capacity.
**Back:** *"NCF says C2 plus half: a commission's recommendation, not a government's policy."*

### Flashcard T-111 — Fair and Remunerative Price (FRP) for sugarcane
**Front:** What is FRP, and how does it differ from MSP?
**Definition (learn):** FRP is the minimum price payable by sugar mills to cane growers for sugarcane, fixed by the Union government on the recommendation of CACP.
**Breakdown:**
- ✅ FRP is a statutory-style price under the sugarcane control regime, not a CACP MSP. Owner 12 classifies it as FRP.
- ⚠️ Under the Sugarcane (Control) Order, mills must pay at least FRP; states may announce a higher State Advised Price (SAP).
- ✅ Sugarcane cannot be traded below FRP; sugar prices and mill recovery rates shape the sustainability of FRP.
**Cases / Committees / Schemes / Data:** ✅ Owner 12 (sugarcane counted among the 23 crops via FRP). ⚠️ Current FRP figures per quintal should be taken from the latest Union notification.
**Trap:** Sugarcane FRP is not an MSP; SAP is above FRP; and FRP is paid by mills, not by the government procurement agency.
**Mains hook:** FRP shows how a price floor can be enforced via a processing monopoly; qualify with mill arrears and the ethanol/sugar diversion question.
**Back:** *"Mill pays the FRP, the state may add SAP, and the Centre never buys the cane."*

### Flashcard T-112 — Procurement, buffer stocks, FCI and economic cost
**Front:** How do procurement, buffer norms and the FCI fit together in food management?
**Definition (learn):** Procurement is government purchase of eligible produce at MSP; buffer stock is publicly held inventory for distribution, emergencies and stabilisation; FCI handles procurement, storage, movement and release.
**Breakdown:**
- ✅ Food Corporation of India (FCI) and state agencies procure, store, move and release foodgrain.
- ✅ Buffer-stock norms are desirable operational stock levels; actual stocks can be higher or lower.
- ⚠️ Buffer norms are fixed for specific quarterly stock dates (1 Jan, 1 Apr, 1 Jul, 1 Oct) as per the Food Ministry's norms; verify the current table.
- ✅ Economic cost of foodgrain includes procurement incidentals, storage, movement, carrying and distribution costs, not only MSP.
- ✅ Shanta Kumar Committee (2015, ⚠️ year) is a named reform anchor on FCI efficiency and PDS targeting.
- ⚠️ Open Market Sale Scheme (OMSS) releases stock to stabilise prices.
**Cases / Committees / Schemes / Data:** ✅ Owner 12 as-of 2025-26 anchors. ⚠️ Buffer norm and OMSS details to be checked.
**Trap:** Higher buffer stock is not always better; it raises carrying, quality and fiscal costs. FCI and CACP have different functions. Economic cost is not the MSP.
**Mains hook:** Evaluate the FCI model on price assurance versus fiscal and storage burden; conclude that targeting, decentralised procurement and crop diversification are better than open-ended stocking.
**Back:** *"Buy at MSP, hold within norms, release by need: the FCI cycle has three brakes."*

### Flashcard T-113 — National Food Security Act, 2013 (NFSA): coverage and entitlements
**Front:** Who is entitled to subsidised foodgrain under the NFSA, and how much?
**Definition (learn):** NFSA 2013 gives a legal entitlement to subsidised foodgrain through the Targeted Public Distribution System (TPDS) to identified priority and Antyodaya households.
**Breakdown:**
- ✅ Priority Households: 5 kg per person per month.
- ✅ Antyodaya Anna Yojana (AAY) households: 35 kg per household per month.
- ✅ Coverage capped at up to 75% of the rural and 50% of the urban population (roughly two-thirds of national population).
- ✅ Original prices ₹3/₹2/₹1 per kg (rice/wheat/coarse grains); since January 2023 the NFSA quota has been supplied free through PMGKAY, continuing to December 2028 (✅ Wikipedia, Pradhan Mantri Garib Kalyan Anna Yojana).
- ✅ Maternity and child-nutrition entitlements exist alongside cereals.
**Cases / Committees / Schemes / Data:** ✅ Owner 12 and owner 23 (NFSA as legal entitlement); ✅ continuation of free supply to December 2028 confirmed (see Breakdown).
**Trap:** AAY is 35 kg per household, not per person. Coverage ceiling is not the same as actual enrolled beneficiaries. NFSA is not universal free food.
**Mains hook:** Argue that entitlement converts food access into a right, but qualify with exclusion errors from Census-based coverage.
**Back:** *"Five a head, thirty-five a household, seventy-five percent rural: the NFSA math is a cap, not a promise."*

### Flashcard T-114 — TPDS, One Nation One Ration Card, e-PoS and PMGKAY
**Front:** How does the TPDS deliver food, what did ONORC add, and what is PMGKAY?
**Definition (learn):** TPDS is the statutory delivery chain for subsidised food; ONORC lets beneficiaries draw their entitlement from any ePoS fair-price shop across states; PMGKAY is an extended free-foodgrain support layer on the same network.
**Breakdown:**
- ✅ ONORC now operates across all States/UTs; beneficiaries authenticate through Aadhaar-based ePoS transactions tracked on IMPDS/Annavitran portals.
- ✅ End-to-End Computerisation of TPDS digitised allocation-to-sale; nearly all fair-price shops are ePoS-enabled.
- ✅ Authentication failures (connectivity, device, worn fingerprints, seeding errors) can exclude genuine beneficiaries.
- ✅ Fortified rice supply through PDS/ICDS/mid-day meal channels continued through December 2028 (owner 12, as-of); FSSAI safety debate remains contested.
- ✅ PMGKAY: extended free-foodgrain support using the public-distribution architecture; ✅ announced 26 March 2020 during COVID; current status: continuing to December 2028 (✅ Wikipedia, Pradhan Mantri Garib Kalyan Anna Yojana).
- ✅ DBT/cash-transfer PDS pilots (Puducherry, Chandigarh, Dadra & Nagar Haveli) test cash in place of grain; a trade-off with price-inflation and diversion risk.
**Cases / Committees / Schemes / Data:** ✅ Owner 12 (ONORC, ePoS, fortified rice, DBT pilots).
**Trap:** ONORC is portability, not new entitlement. PMGKAY is not identical to NFSA. Digitisation reduces leakage but adds exclusion risk. DBT is not a proven nationwide replacement.
**Mains hook:** Assess PDS reform as a shift from quantity access to verifiable, portable delivery; qualify with exclusion from authentication failures.
**Back:** *"One card, any shop, a fingerprint to prove it: portability needs both the scanner and the shop."*

### GROUP — Agricultural markets, aggregation and trade

### Flashcard T-115 — APMC Acts, model reform and state experiments
**Front:** What do APMC Acts do, and why do state mandi reforms differ?
**Definition (learn):** APMC (Agricultural Produce Market Committee) Acts are state laws that notify agricultural produce and regulate mandi yards, fees and market practice.
**Breakdown:**
- ✅ Agricultural marketing is a State subject; each state's APMC Act regulates notified produce, mandi yards, market fees and licensing.
- ✅ Model APMC framework (✅ Model APMC Act, 2003: features include a contract-farming model, a special market for perishables and a single market fee; ✅ Wikipedia, Agricultural Produce Market Committee) offered a template for states to permit direct marketing, private markets and contract farming.
- ✅ Karnataka's Rashtriya e-Market Services (ReMS) model unified markets, assaying and electronic processes.
- ✅ Bihar repealed its APMC Act (⚠️ 2006) as a contrasting model; repeal did not automatically create competitive private markets.
- ✅ Fragmentation (multiple market fees, many licences) reduces price discovery; unified rules work better than digitising an unreformed structure.
**Cases / Committees / Schemes / Data:** ✅ Owner 13: Karnataka ReMS, Bihar repeal, Dalwai Committee as anchors.
**Trap:** APMC is a state Act, not a central law. Repeal of a mandi system is not the same as competition. e-NAM does not abolish APMC Acts.
**Mains hook:** Argue that marketing reform must combine legal freedom with assaying, logistics, payment and buyer depth; conclude with the state-led, phased approach.
**Back:** *"Mandi law is a state's law: unify it, assay it, then let buyers compete."*

### Flashcard T-116 — e-NAM, assaying and quality-linked trade
**Front:** What is e-NAM, and what must accompany an online bid for a completed sale?
**Definition (learn):** e-NAM (National Agriculture Market) is an electronic trading platform that links participating APMC mandis for transparent bidding and wider price discovery.
**Breakdown:**
- ✅ Launched in 2016; operated under the Ministry of Agriculture through SFAC (owner 27).
- ✅ Assaying results create trusted quality categories for electronic bidding.
- ✅ Completed sale requires: online bid + trusted assaying + physical aggregation + logistics + payment/settlement + dispute resolution (owner 27 chain).
- ✅ Participating mandis remain under state APMC frameworks; e-NAM is digital-plus-physical.
**Cases / Committees / Schemes / Data:** ✅ e-NAM covers participating mandis; exact mandi count should be verified from the latest official dashboard (owner 13 caution).
**Trap:** Digital bidding without assaying, grading and payment enforcement creates a screen-based illusion of integration. e-NAM is not a stand-alone national market.
**Mains hook:** Argue that digital discovery only widens choice if physical functions follow; qualify with logistics and buyer concentration.
**Back:** *"Bid online, but the sale closes only when the grader, the godown and the banker agree."*

### Flashcard T-117 — Negotiable Warehouse Receipts and WDRA
**Front:** How do negotiable warehouse receipts (NWRs) help farmers, and what regulates warehousing?
**Definition (learn):** An NWR is a document issued by an accredited warehouse certifying stored produce; it can be pledged to a bank for credit, letting farmers avoid distress sale.
**Breakdown:**
- ✅ Warehousing Development and Regulatory Authority (WDRA) regulates accredited warehouses and NWR issuance (⚠️ creation statute and year unverified: the Wikipedia page 404s; the statute usually cited is the Warehousing (Development and Regulation) Act, 2007 (from memory, not source-checked), not a 'WRDA Act, 2010').
- ✅ NWR works only where warehouses are accredited, grading is trusted and lenders have confidence.
- ✅ NWR separates sale timing from harvest-time cash pressure.
**Cases / Committees / Schemes / Data:** ✅ Owner 13 (NWR as inventory-finance tool).
**Trap:** NWR is not a credit rating. WDRA is the regulator for warehouses, not the warehouse operator. Storage without accreditation cannot produce a negotiable receipt.
**Mains hook:** Argue that post-harvest finance depends on credible inventory; conclude that accreditation and grading reforms precede credit expansion.
**Back:** *"A receipt you can bank is a crop you need not dump."*

### Flashcard T-118 — Farm laws 2020 and their repeal in 2021
**Front:** What did the 2020 farm laws do, and why were they repealed?
**Definition (learn):** The 2020 package created trade channels outside APMC mandis and changed contract and stock rules; the Farm Laws Repeal Act, 2021 repealed the three laws.
**Breakdown:**
- ✅ Farmers' Produce Trade and Commerce (Promotion and Facilitation) Act, 2020: created an outside-APMC trade channel.
- ✅ Companion Acts: Farmers (Empowerment and Protection) Agreement on Price Assurance and Farm Services Act, 2020 (contract farming) and a 2020 amendment of the Essential Commodities Act, 1955 (stock limits) (✅ Wikipedia, Farmers' Produce Trade and Commerce Act, 2020); the exact title 'Essential Commodities (Amendment) Act, 2020' is not on the page (⚠️).
- ✅ Farm Laws Repeal Act, 2021 repealed them.
- ✅ Repeal shows marketing reform is a question of consultation, state powers and farmer trust, not only efficiency.
**Cases / Committees / Schemes / Data:** ✅ Owner 13 names the 2020 Trade Act and its repeal; ✅ Trade Act passage per Wikipedia: Lok Sabha 17 Sep 2020, Rajya Sabha 20 Sep 2020, President 27 Sep 2020; ⚠️ the Repeal Act's exact assent date is not verified.
**Trap:** Repeal did not end the need for competition, logistics and non-distortionary market access. The 2020 Trade Act is distinct from the MSP question.
**Mains hook:** Trace the lesson: market liberalisation requires federal consultation, assured grading and price-protection design; conclude with a phased, state-tested approach.
**Back:** *"Three laws in, three laws out: reform without trust is a law that gets repealed."*

### Flashcard T-119 — Farmer Producer Organisations (FPOs) and aggregation
**Front:** What is an FPO, and why is aggregation central to raising farm income?
**Definition (learn):** An FPO is a farmer-owned producer organisation (often a producer company) that aggregates produce, inputs or services for members.
**Breakdown:**
- ✅ FPOs help members pool produce, buy inputs in bulk, access assaying and negotiate with buyers.
- ✅ Dalwai Committee (Doubling Farmers' Income) treated aggregation and post-harvest value chains as central.
- ✅ Promotion institutions: SFAC, NABARD-linked support and state agencies.
- ✅ Constraints: working capital, governance, management depth, storage access and reliable buyer linkage.
- ⚠️ FPOs are typically registered as producer companies under the Companies Act; a co-operative is a different legal form.
**Cases / Committees / Schemes / Data:** ✅ Owner 13; ⚠️ scheme target and count should be taken from the latest official dashboard.
**Trap:** FPO ≠ co-operative in every legal respect. Aggregation is not an automatic cure for bargaining power; governance and finance decide it.
**Mains hook:** Argue that aggregation solves the small-farm scale problem faster than consolidation; qualify with governance and working-capital gaps.
**Back:** *"Many small farmers, one company, one bargain: the FPO is scale without land consolidation."*

### Flashcard T-120 — Contract farming, organised retail and monopsony risk
**Front:** Do supermarkets and contract farming eliminate middlemen, and what is the bargaining-power risk?
**Definition (learn):** Contract farming is a pre-agreed buyer–farmer arrangement on price, quality and volume; organised retail backward-integrates into direct procurement.
**Breakdown:**
- ✅ Organised retail and agribusiness replace the traditional commission-agent layer with their own grading, procurement and logistics.
- ✅ Named examples in owner 13: Reliance Retail's direct sourcing from farmers/FPOs; ITC's e-Choupal (launched 2000) bypassing mandi agents; Mother Dairy's Safal fruit and vegetable procurement.
- ✅ Where a few large buyers dominate procurement in a locality, they can exercise monopsony-like power over dispersed farmers.
- ✅ Contract enforcement and quality disputes are rarely symmetric between a small farmer and a large buyer.
**Cases / Committees / Schemes / Data:** ✅ Owner 13 (2018 GS-III Q4 anchor). ⚠️ State contract-farming laws may apply (✅ the Model APMC Act, 2003 includes a contract-farming model; state Acts not checked).
**Trap:** 'Eliminating middlemen' is a misnomer: the aggregation function persists, only its performer changes. Contract farming reduces some price risk but creates enforcement risk.
**Mains hook:** Evaluate whether direct procurement raises farmer share; conclude that competition safeguards and FPO-based bargaining matter more than the buyer's identity.
**Back:** *"The middleman is replaced, not removed; watch who now sets the price."*

### GROUP — Irrigation, inputs, credit, insurance and sustainability

### Flashcard T-121 — PMKSY: Har Khet Ko Pani and Per Drop More Crop
**Front:** What is PMKSY, and what do its named components achieve?
**Definition (learn):** The Pradhan Mantri Krishi Sinchayee Yojana (PMKSY) is the umbrella irrigation-efficiency framework combining irrigation access, micro-irrigation and watershed development.
**Breakdown:**
- ✅ Har Khet Ko Pani: taking irrigation water to uncovered fields (access expansion).
- ✅ Per Drop More Crop: micro-irrigation (drip and sprinkler) for water-use efficiency and fertigation.
- ✅ Watershed Development Component (formerly IWMP) treats catchments ridge-to-valley.
- ⚠️ PMKSY was approved in 2015; component outlays and names have been revised across plan periods.
**Cases / Committees / Schemes / Data:** ✅ Owner 14 (as-of 2025-26 anchors); ⚠️ outlays to be verified from the Union scheme page.
**Trap:** Plot-level micro-irrigation efficiency can be offset by area expansion or water-intensive cropping. More irrigation does not automatically mean sustainability.
**Mains hook:** Distinguish access from efficiency; conclude with groundwater governance and crop-choice reform alongside micro-irrigation.
**Back:** *"Har Khet Ko Pani brings the canal, Per Drop More Crop makes every drop count."*

### Flashcard T-122 — Watershed development and the Jal Shakti Abhiyan (Catch the Rain)
**Front:** How does watershed development work, and how did the Jal Shakti Abhiyan evolve?
**Definition (learn):** A watershed is a geo-hydrological unit draining to a common outlet; watershed development treats it from the ridge down to the valley to conserve soil and water.
**Breakdown:**
- ✅ Treatments: contour and field bunding, check dams, afforestation, soil and moisture conservation, sequenced from highest point downward.
- ✅ Funding pattern: 60:40 Centre–State (higher Central share for hill, tribal and North-Eastern states).
- ✅ Jal Shakti Abhiyan, launched 2019 by the Ministry of Jal Shakti, targeted 256 water-stressed districts with five interventions: rainwater harvesting, traditional water bodies, reuse and recharge, watershed development, afforestation.
- ✅ From 2021, the campaign became 'Catch the Rain', extended to all blocks, adding de-silting and geo-tagging of water bodies.
**Cases / Committees / Schemes / Data:** ✅ Owner 14: 256 districts, five interventions, Catch the Rain.
**Trap:** Watershed development is not one pond or check dam; it is catchment-wide and institution-based. JSA was not a permanent single scheme unchanged since 2019.
**Mains hook:** Argue that structures decay without community ownership and maintenance funds; conclude with participatory institutions.
**Back:** *"Ridge to valley, five campaigns in one, then catch the rain on every block."*

### Flashcard T-123 — Fertiliser subsidy: urea versus Nutrient Based Subsidy (NBS)
**Front:** How do urea pricing and NBS differ, and how is the fertiliser subsidy paid?
**Definition (learn):** Urea is nitrogen fertiliser under a separate subsidy and pricing regime; NBS gives a per-nutrient subsidy on covered phosphatic and potassic fertilisers.
**Breakdown:**
- ✅ Subsidy is released to manufacturers and importers through DBT after eligible sales; the farmer buys at a lower price.
- ✅ NBS covers notified P and K grades and per-nutrient support for N, P, K and sulphur.
- ✅ Urea is outside NBS and has a controlled farm price, so relative underpricing encourages excessive nitrogen use and imbalanced N:P:K.
- ✅ Not the same mechanism as PM-KISAN: fertiliser subsidy is a price-linked support to the product, PM-KISAN is cash to the farmer.
- ⚠️ Owner 28 (Union Budget 2025-26) gives approx. ₹1.84 lakh crore as the total fertiliser subsidy (urea ~₹1.19 lakh crore; NBS ~₹0.49 lakh crore). ✅ corrected internal check: the components sum to ₹1.68 lakh crore, not ₹1.84 lakh crore (was: 'total ₹1.84 lakh crore' with no reconciliation); the ~₹0.16 lakh crore residual is unexplained in owner 28. Not reconcilable from accessible sources: Wikipedia (Union budget of India; Economy of India) gives no 2025-26 fertiliser figure, indiabudget.gov.in returned HTTP 403, and PRS (prsindia.org) returned 404. Neither the ₹1.84 nor the ₹1.68 lakh crore figure is confirmed; do not quote a total without the Budget document.
**Cases / Committees / Schemes / Data:** ✅ Owner 28 4.1; ⚠️ Rabi 2025-26 NBS approval of about ₹37,952 crore (owner).
**Trap:** Fertiliser subsidy ≠ farm income subsidy. Urea and NBS are not the same regime. Budget allocation is not expenditure.
**Mains hook:** Argue that input subsidy should be redesigned for nutrient balance and small farmers; qualify with import and fiscal exposure.
**Back:** *"Urea is priced, NBS is per nutrient: one protects the bag, the other protects the soil."*

### Flashcard T-124 — Agricultural credit: Kisan Credit Card, NABARD and co-operative channels
**Front:** How does institutional farm credit work, and what roles do KCC, NABARD and DCCBs play?
**Definition (learn):** Institutional agricultural credit supplies short-term working capital (crop and allied) and medium-term investment through banks and co-operatives, with NABARD refinancing.
**Breakdown:**
- ✅ KCC: a short-term credit instrument for crop and allied working-capital needs (seed, fertiliser, labour, utilities, fuel); broader than input purchase.
- ✅ NABARD (National Bank for Agriculture and Rural Development): refinances agricultural and rural credit.
- ✅ District Central Co-operative Banks (DCCBs) are part of the short-term co-operative credit chain.
- ✅ KCC was introduced in August 1998 by public sector banks (✅ corrected: was '1998–99'; Wikipedia, Kisan Credit Card). ⚠️ Interest subvention (e.g., Modified Interest Subvention Scheme) lowers the effective rate for prompt repayers; the rates are not on the Wikipedia page, so verify current subvention rates.
**Cases / Committees / Schemes / Data:** ✅ Owner 14 (KCC, NABARD, DCCBs); ✅ owner 14 flags title-linked access excludes tenant farmers.
**Trap:** KCC is not only for seed purchase. Formal credit access depends on land-title records, so tenants and sharecroppers are weakly covered. NABARD is a refinancing and development institution, not the direct lender to most farmers.
**Mains hook:** Argue that institutional credit reduces dependence on informal lenders; qualify with title-linked exclusion and tenancy recognition.
**Back:** *"KCC runs the season, NABARD refills the well, DCCB carries the local load."*

### Flashcard T-125 — Pradhan Mantri Fasal Bima Yojana (PMFBY)
**Front:** How does PMFBY work, and what risk does it cover?
**Definition (learn):** PMFBY is a subsidised crop-insurance scheme that pools specified production risks for notified crops, notified areas and insured farmers.
**Breakdown:**
- ✅ Farmer premium share: 2% of sum insured for Kharif, 1.5% for Rabi, 5% for commercial/horticultural crops (owner 14; the scheme page was not reachable); ⚠️ the balance premium subsidy shared Centre–State (90:10 for North-Eastern/Himalayan states; otherwise generally 50:50) is not verified.
- ✅ Yield loss is assessed mainly through Crop Cutting Experiments (CCEs), increasingly supplemented by satellite and drone data.
- ✅ Enrolment has been voluntary since the 2020 revamp; several states have exited or scaled back.
- ⚠️ PMFBY launched on 18 February 2016 (✅ Wikipedia, PMFBY); the 'Kharif 2016' first-season wording is not separately confirmed.
**Cases / Committees / Schemes / Data:** ✅ Owner 14 (premium shares, CCE, voluntary enrolment). ✅ Launch year 2016 confirmed (Wikipedia: 18 February 2016); enrolment 100% voluntary from Kharif 2020 (✅ Wikipedia).
**Trap:** PMFBY covers specified production risks, not every price or household-income loss. The premium is not the same across seasons. Enrolment is not compulsory since the 2020 revamp (as owner states).
**Mains hook:** Evaluate PMFBY as risk pooling; qualify with slow claims, basis risk and voluntary exits.
**Back:** *"Two for Kharif, one-and-a-half for Rabi, five for the cash crop: the farmer pays a sip, the state pays the sea."*

### Flashcard T-126 — PM-KISAN: direct income support
**Front:** What does PM-KISAN provide, and how is it paid?
**Definition (learn):** PM-KISAN is a central DBT income-support scheme giving eligible landholding farmer families a fixed annual payment.
**Breakdown:**
- ✅ ₹6,000 per year per eligible landholding farmer family, paid in three DBT instalments.
- ✅ Launched in February 2019: announced in the 1 February 2019 Interim Budget and formally launched on 24 February 2019 in Gorakhpur (✅ Wikipedia, PM-KISAN).
- ✅ Eligibility is land-record-based, so tenant farmers, sharecroppers and cultivators without records can be omitted.
- ✅ It is income support, not a price floor, not an input subsidy and not insurance.
**Cases / Committees / Schemes / Data:** ✅ Owner 28 (₹6,000 p.a.; three instalments; exclusion rules).
**Trap:** PM-KISAN is not a fertiliser subsidy; it does not depend on what is produced or sold. Land-record eligibility is a classic exclusion trap.
**Mains hook:** Compare cash income support with price support; qualify with exclusion and fiscal cost.
**Back:** *"Six thousand a year, three slips, one land record: income support that starts at the patta."*

### Flashcard T-127 — Soil health and conservation agriculture
**Front:** How does soil-health management link to sustainable productivity?
**Definition (learn):** Soil health is the soil's capacity to function as a living system for productivity; conservation agriculture minimises soil disturbance, retains residue and rotates crops.
**Breakdown:**
- ✅ Conservation agriculture: minimum soil disturbance, residue management, crop rotation.
- ✅ Zero tillage: sowing without ploughing, common in wheat-after-paddy; cuts turnaround time and fuel, but weed and residue management still matter.
- ✅ Biochar: soil amendment linked to microbes and water retention; outcomes are context-specific.
- ✅ Fertigation (fertiliser through irrigation water) improves nutrient-use efficiency in suitable systems.
- ✅ Soil Health Card scheme, launched 19 February 2015 (✅ Wikipedia, Soil Health Card Scheme), gives farmers crop-wise nutrient and fertiliser recommendations per soil test.
**Cases / Committees / Schemes / Data:** ✅ Owner 14 defs; ✅ scheme year 2015 (Wikipedia; the ministry is not named on that page).
**Trap:** Zero tillage is not automatically 'no residue'. Biochar is not a universal fix. Tensiometer measures soil moisture tension, not nutrient status.
**Mains hook:** Argue that soil health must be part of input-subsidy redesign; conclude with nutrient-balance and water-efficiency links.
**Back:** *"Disturb less, cover more, test the soil before you feed it."*

### Flashcard T-128 — Organic and natural farming: NPOP, Sikkim and PKVY/NMNF
**Front:** How is organic farming certified, and how does natural farming differ?
**Definition (learn):** Organic farming follows certified standards for inputs and processes; natural farming relies on on-farm, low-external-input practices.
**Breakdown:**
- ✅ National Programme for Organic Production (NPOP) is implemented under APEDA (owner 12); organic certification architecture is distinct from every form of low-chemical farming.
- ⚠️ Sikkim decided in 2003 to convert fully to organic farming; Wikipedia gives two dates for achieving it ('achieved in 2015'; 'between 2003 and 2016') (✅ corrected: card said 'declared ... in January 2016' and cited a '2003 Assembly resolution'; neither the resolution nor a January 2016 declaration is on the page). The 2014 sale ban and phased subsidy withdrawal are unverified.
- ⚠️ Paramparagat Krishi Vikas Yojana (PKVY, 2015) under NMSA promotes organic clusters with certification.
- ⚠️ National Mission on Natural Farming (approved 2024) is a separate, lower-input mission; verify its current status.
**Cases / Committees / Schemes / Data:** ✅ Owner 14 (Sikkim as the most-cited state transition; ~75,000 ha certified per owner, verify).
**Trap:** Organic ≠ natural ≠ permaculture. Sikkim's small-hill model is not directly replicable in intensive plains states.
**Mains hook:** Argue that organic and natural farming reduce input dependence but need market premiums and certification access; qualify with yield and scale risks.
**Back:** *"Certify the organic, practise the natural, and remember Sikkim had a decade to transition."*

### Flashcard T-129 — Agricultural technology missions and mission-mode policy
**Front:** How do India's agricultural missions (NHM→MIDH, NFSM→NFSNM, NMEO-OP/OS) show the mission model?
**Definition (learn):** A mission is a time-bound, outcome-linked programme combining research, transfer, adoption, infrastructure and markets for a specific crop or problem.
**Breakdown:**
- ✅ Technology Mission on Oilseeds (1986) → successor arrangements for oilseeds, pulses, maize and oil palm.
- ✅ National Horticulture Mission (2005–06) → Mission for Integrated Development of Horticulture (MIDH) from 2014–15.
- ✅ National Food Security Mission (2007–08) → renamed National Food Security and Nutrition Mission (NFSNM) in FY25.
- ✅ NMEO-OP (oil palm) and NMEO-OS (oilseeds) are distinct missions; oil palm is perennial with long gestation.
- ✅ Mission for Atmanirbharta in Pulses (approved 2025, owner 29).
- ✅ Krishonnati Yojana umbrella (owner 29 snapshot, as of Economic Survey 2025-26) lists eight schemes; verify before quoting names.
**Cases / Committees / Schemes / Data:** ✅ Owner 29 chronology; ✅ 'Mission for Cotton Productivity' replaced the Technology Mission on Cotton (2000).
**Trap:** Not every 'Mission' is a technology mission. Output does not equal farmer income; area does not equal yield. Current umbrella lists cannot be applied to all years.
**Mains hook:** Evaluate missions on output, yield and net farm income separately; qualify with predecessor-successor churn and delivery gaps.
**Back:** *"Missions get renamed, outcomes get measured: track yield, not just area or acronyms."*

### GROUP — Food processing, cold chain and livestock

### Flashcard T-130 — Food processing: PMKSY (SAMPADA), Mega Food Parks, PLISFPI and Operation Greens
**Front:** Which instruments move food processing, and what does each do?
**Definition (learn):** Food processing transforms, preserves or packages food to extend shelf life and add value; policy works on infrastructure, incentives and price stabilisation.
**Breakdown:**
- ✅ Pradhan Mantri Kisan Sampada Yojana (PMKSY/SAMPADA umbrella) finances mega food parks, cold chains, agro-processing clusters and quality infrastructure (names and outlays revised across plan periods).
- ✅ Mega Food Parks: common facilities (collection centres, primary and central processing centres) linking farms to markets; several parks faced land and occupancy problems.
- ✅ PLI for Food Processing (PLISFPI): incentives on eligible incremental sales (ready-to-eat/cook, marine, Indian brands abroad).
- ✅ Operation Greens (originally tomato-onion-potato, later extended): price-stabilisation for perishables.
- ✅ FSSAI sets food-safety standards; APEDA supports export and market access.
**Cases / Committees / Schemes / Data:** ✅ Owner 15 (2025 GS-III employment question anchor). ⚠️ Sanctioned vs disbursed figures must be dated.
**Trap:** Sanctioned outlay is not disbursed incentive. A warehouse is not a cold chain. FSSAI regulates food safety; APEDA does not replace it.
**Mains hook:** Argue that output-linked incentives buy additionality; qualify with small-processor exclusion and fragmented first-mile logistics.
**Back:** *"Parks build the room, PLI pays for the output, Greens steadies the price of tomatoes."*

### Flashcard T-131 — Cold chain and post-harvest management
**Front:** What does a genuine cold chain require beyond cold storage?
**Definition (learn):** A cold chain is temperature-controlled storage and transport from production to consumption, sustained from first mile to last mile.
**Breakdown:**
- ✅ Nodes: pre-cooling units at farm/collection, ambient and cold storage, reefer transport, pack-houses, quality testing and traceability.
- ✅ Warehousing without pre-cooling and reefer logistics only shifts the point of deterioration.
- ✅ Reliable power and coordinated first-mile and last-mile logistics are binding constraints.
- ✅ Processing-linked employment is spread across aggregation, grading, cold logistics and packaging, but much of it is seasonal and informal.
**Cases / Committees / Schemes / Data:** ✅ Owner 15 (cold-chain nodes and employment). ⚠️ Specific cold-storage grant schemes should be verified.
**Trap:** A warehouse is not automatically a cold chain. Large plants do not solve first-mile loss; aggregation does.
**Mains hook:** Argue that post-harvest losses are about volatility and market access as much as spoilage; conclude with first-mile distributed infrastructure.
**Back:** *"Cool it at the farm, carry it cold, check it at the shelf: a single cold room is not a chain."*

### Flashcard T-132 — Dairy economics, Operation Flood and NDDB
**Front:** What was Operation Flood, and how does the Anand-type cooperative model work?
**Definition (learn):** Operation Flood was a national dairy programme (from 1970, under NDDB) linking rural milk sheds to urban demand through collection, processing and marketing.
**Breakdown:**
- ✅ Operation Flood began in 1970 under NDDB and ran in three phases.
- ✅ Anand-type cooperative: village producer societies, district unions and state federations.
- ✅ Economic advantages: aggregation of small daily quantities, transparent quality testing and payment, feed and veterinary services, processing and brand value.
- ✅ Risks: governance, political capture, regional concentration, delayed payment, monopsony where producers lack buyer choice.
- ✅ Dairy is a primary-sector activity; dairy processing is secondary.
**Cases / Committees / Schemes / Data:** ✅ Owner 30; ✅ India's milk production 2023-24 about 239.30 million tonnes (Basic Animal Husbandry Statistics 2024, as-of).
**Trap:** 'White Revolution' is the popular name for Operation Flood; it is not a separate scheme. Dairy farming vs dairy processing is a sector classification trap.
**Mains hook:** Argue that cooperatives solve aggregation and bargaining; qualify with governance and remote-producer exclusion.
**Back:** *"Milk comes twice a day, the test happens at the village, the payment comes on time: that is the Anand model."*

### Flashcard T-133 — Livestock schemes: Rashtriya Gokul Mission, NLM, LHDCP and AHIDF
**Front:** Which livestock schemes work on genetics, entrepreneurship, disease control and processing finance?
**Definition (learn):** Livestock policy combines breeding, feed and fodder, disease control and infrastructure finance under DAHD.
**Breakdown:**
- ✅ Rashtriya Gokul Mission: bovine genetic improvement and breeding infrastructure.
- ✅ National Livestock Mission: entrepreneurship in poultry, small ruminants, piggery; feed and fodder; livestock insurance components.
- ✅ Livestock Health and Disease Control Programme: vaccination, surveillance, veterinary capacity, zoonotic control.
- ✅ Animal Husbandry Infrastructure Development Fund (AHIDF): finance for dairy and meat processing, feed, breed technology and waste-to-wealth.
- ✅ Kisan Credit Card for animal husbandry, dairy and fisheries: working capital.
- ✅ Institutions: DAHD (policy and statistics), NDDB, ICAR institutes, state departments, FSSAI for food safety.
**Cases / Committees / Schemes / Data:** ✅ Owner 30 (scheme functions; ⚠️ outlay not owner-verified). Latest released Livestock Census: 20th (2019), ~536.76 million livestock; the 21st Census was launched in October 2024, results not yet owner-verified.
**Trap:** Census gives stock; the Integrated Sample Survey gives annual flows; Basic Animal Husbandry Statistics is a publication. Do not conflate them.
**Mains hook:** Argue that livestock income depends on feed, health and market access together; qualify with the feed-cost binding constraint.
**Back:** *"Gokul breeds, NLM starts, LHDCP protects, AHIDF processes: four instruments, one animal economy."*

### Flashcard T-134 — Fisheries, aquaculture and the Blue Revolution (PMMSY)
**Front:** How do capture fisheries and aquaculture differ, and what does PMMSY do?
**Definition (learn):** Capture fisheries harvest wild stocks (common-pool resource); aquaculture is managed farming of aquatic species in ponds, cages or recirculating systems.
**Breakdown:**
- ✅ Classification: capture vs aquaculture; marine vs inland vs brackish; extensive, semi-intensive, intensive; pond, cage, biofloc, RAS.
- ✅ Pradhan Mantri Matsya Sampada Yojana (PMMSY): sustainable fisheries production plus value-chain modernisation, welfare and jobs.
- ✅ Fisheries Infrastructure Development Fund and PM-MKSSY (formalisation and finance/insurance access).
- ⚠️ 'Blue Revolution' is the popular term for fisheries and aquaculture growth; FAO's 'Blue Transformation' (2022–2030) is a separate global roadmap (owner 30).
**Cases / Committees / Schemes / Data:** ✅ Owner 30 (section 12 and FAO Blue Transformation, 27).
**Trap:** Blue Transformation ≠ Blue Revolution ≠ Blue Box (WTO). Capture fisheries are not 'managed farming'. Fishing income is primary-sector.
**Mains hook:** Argue that aquaculture scales protein supply but needs value-chain and water-quality governance; qualify with capture-fishery overharvest.
**Back:** *"Catch what the sea gives, farm what the pond can take, and PMMSY takes both to market."*

### GROUP — Digital agriculture and farm-support economics

### Flashcard T-135 — Digital agriculture: AgriStack, Digital Agriculture Mission and Krishi-DSS
**Front:** What are AgriStack, the Digital Agriculture Mission and Krishi-DSS, and how do they fit together?
**Definition (learn):** Digital agriculture is data-enabled management of the farm cycle through identity, records, sensing, analytics and service delivery; AgriStack is the public infrastructure layer.
**Breakdown:**
- ✅ Digital Agriculture Mission: approved by the Union Cabinet in September 2024 with an outlay of ₹2,817 crore (central share ₹1,940 crore).
- ✅ AgriStack: federated infrastructure built with states; building blocks are a Farmer Registry, geo-referenced village maps and crop-sown information (Digital Crop Survey).
- ✅ Krishi-DSS: geospatial decision-support platform for crop mapping, crop-weather monitoring and drought assessment.
- ✅ Namo Drone Didi: drone-based services for women SHGs (2023-24 to 2025-26 design).
- ✅ Sensing, analysis and control are different: IoT senses; AI analyses; automated control acts.
**Cases / Committees / Schemes / Data:** ✅ Owner 27 (as-of Economic Survey 2025-26 snapshot; verify current status).
**Trap:** The mission is enabling infrastructure, not one farmer app. Land-linked registries can exclude tenants without correction procedures. Krishi-DSS supports decisions; it does not replace field verification.
**Mains hook:** Argue that DPI-style farm registries improve delivery; qualify with data rights, exclusion and cyber-resilience.
**Back:** *"Map the village, register the farmer, record the crop: then the services can find the field."*

### Flashcard T-136 — Direct and indirect farm subsidies: a classification
**Front:** What are the main categories of farm support, and why does the classification matter?
**Definition (learn):** Farm support includes transfers, price support, input subsidies, credit and insurance support, capital grants and public services; each has different incidence and fiscal logic.
**Breakdown:**
- ✅ Income transfer (PM-KISAN); fertiliser price subsidy (urea, NBS); electricity subsidy; irrigation subsidy; credit support; insurance premium support; capital grants (micro-irrigation, machinery); MSP-backed procurement; price-deficiency payments; public services; consumer food subsidy (PDS/NFSA).
- ✅ Electricity subsidy and the water–energy–crop nexus: free power lowers pumping cost and encourages water-intensive crops.
- ✅ Tariffs are border measures, not domestic subsidies.
- ✅ Public investment in roads and research is public-good support, not a producer subsidy in fiscal analysis.
**Cases / Committees / Schemes / Data:** ✅ Owner 28 section 3 map.
**Trap:** Procurement support ≠ consumer food subsidy. Public investment ≠ subsidy. Free power is also a crop-choice and aquifer incentive.
**Mains hook:** Classify before judging; conclude that rebalancing from input price support toward public goods and direct income support is the defensible route.
**Back:** *"Income, price, input, power, credit, insurance, capital, public goods: name the channel before naming the cost."*

### Flashcard T-137 — WTO Agreement on Agriculture: boxes, AMS and de minimis
**Front:** How are farm supports classified under the WTO Agreement on Agriculture (AoA), and what is the de minimis rule?
**Definition (learn):** The AoA (1995) disciplines domestic support through a traffic-light box system: Amber (distorting), Green (minimal distortion), Blue (production-limiting direct payments), with a de minimis threshold.
**Breakdown:**
- ✅ Amber Box: distorting support subject to reduction commitments (includes market price support and production/input-linked support).
- ✅ De minimis: for developing countries, product-specific support up to 10% of the value of production of the concerned product and non-product-specific support up to 10% of total agricultural production are exempt.
- ✅ Green Box: government-funded, minimal distortion, no producer price support (research, extension, pest control, food security and decoupled payments meeting criteria).
- ✅ Blue Box: direct payments tied to production-limiting programmes (fixed area or yield, fixed livestock numbers, or 85% or less of base production).
- ✅ Article 6.2: developing-country flexibility for input and investment subsidies to low-income producers.
- ✅ AMS: (Applied administered price − fixed external reference price) × eligible production. Worked example (illustrative): (₹2,000 − ₹1,200) per quintal × 1 crore quintal = ₹800 crore.
**Cases / Committees / Schemes / Data:** ✅ Owner 28 8.2–8.3. ✅ India's 2024-25 WTO notification: rice support ~$7.6 billion, ~11.85% of rice production value (owner, as-of).
**Trap:** Green Box is not 'anything environmentally good'. Blue Box is not 'any irrigation subsidy'. AMS is not the government budget.
**Mains hook:** Argue that India's MSP-based support triggers AMS limits; qualify with the stockholding peace clause and redesign options.
**Back:** *"Amber warns, Green is clean, Blue limits, and de minimis tells you how much noise you can make."*

### Flashcard T-138 — Public stockholding and the peace clause (Bali 2013)
**Front:** What is India's public stockholding issue at the WTO, and what protection exists?
**Definition (learn):** Public stockholding is government procurement and storage of foodgrain for food security; WTO rules count administered procurement prices as market price support against an old fixed external reference price.
**Breakdown:**
- ✅ The 2013 Bali Ministerial decision created an interim peace clause (due restraint) for existing public-stockholding programmes for staple crops, subject to transparency and notification conditions.
- ✅ India invoked the peace clause for food-security procurement in preceding marketing years, including 2024-25 (owner 28, as-of).
- ✅ India seeks a permanent solution, arguing food-security procurement for large vulnerable populations requires fairer rules.
- ✅ The fixed external reference price is from the base period (1986–88 ⚠️), so current administered prices overstate AMS.
**Cases / Committees / Schemes / Data:** ✅ Owner 28 (8.4, 2024-25 notification).
**Trap:** The peace clause is interim, not a permanent exemption. The AMS number is not the fiscal outlay. Bali 2013 is not the same as the Nairobi or Doha outcome.
**Mains hook:** Argue that India's food-security stocks need a permanent WTO solution; qualify with the need for transparent notifications and a diversified support mix.
**Back:** *"Bali buys a pause, not a permanent pass: India's stocks need a permanent rule."*

### GROUP — Industrial policy, PSUs, MSMEs and manufacturing

### Flashcard T-139 — Industrial policy timeline: IPR 1948, IPR 1956 and the New Industrial Policy 1991
**Front:** How did India's industrial policy move from state-led planning to liberalisation?
**Definition (learn):** Industrial policy is the state framework that shapes entry, competition, technology, location and strategic capability; the three landmark resolutions mark its phases.
**Breakdown:**
- ✅ IPR 1948: mixed-economy role for the state; private sector allowed alongside public enterprise.
- ✅ IPR 1956: industries classified into Schedules A, B and C; commanding heights reserved for the public sector; Industries (Development and Regulation) Act, 1951 licensing governed entry and capacity.
- ✅ New Industrial Policy 1991: dismantled most licensing, opened trade and investment, and linked industry to BoP reform.
- ✅ Partial delicensing and trade liberalisation began in the 1980s, so 1991 is not a clean break.
- ✅ Five-Year Plans shifted thrust: Second Plan (heavy industry, state-led), Sixth and Seventh (modernisation, early delicensing), Eighth Plan (systemic financial-sector reform alongside NIP 1991).
**Cases / Committees / Schemes / Data:** ✅ Owner 16 (chronology and Plan-by-Plan thrust).
**Trap:** Schedule A/B/C (1956) ≠ 1991 'Negative list'. 1991 did not remove all regulation: competition, environment and sector regulators remain.
**Mains hook:** Argue that 1991 was a BoP-triggered package, not an ideology switch; qualify with the continued state role in regulation and strategic sectors.
**Back:** *"Forty-eight mixed, fifty-six reserved, ninety-one opened: the policy followed the crisis, not the other way round."*

### Flashcard T-140 — LPG reforms: liberalisation, privatisation and globalisation
**Front:** What do LPG reforms mean, and what did the 1991 package include?
**Definition (learn):** LPG reforms are liberalisation (less licensing and control), privatisation (more private ownership or control) and globalisation (greater openness to trade and capital).
**Breakdown:**
- ✅ Liberalisation: delicensing, reduced controls on capacity and entry, exchange-rate and financial reform.
- ✅ Privatisation: disinvestment and selective private participation; ownership change differs from minority sale (T-143).
- ✅ Globalisation: trade opening, foreign investment and integration into global value chains.
- ✅ The state's role shifted toward regulation, public goods and social protection; it did not end.
**Cases / Committees / Schemes / Data:** ✅ Owner 16 (1991 as an external-shock response).
**Trap:** LPG reforms did not mean the end of the state. Privatisation does not automatically mean competition.
**Mains hook:** Evaluate LPG reforms on growth and productivity gains, with the distributional and regional costs they imposed.
**Back:** *"Loosen the licence, sell some of the state, open the border: the state stays as referee, not as owner of everything."*

### Flashcard T-141 — Competition law: from the MRTP Act to the Competition Act, 2002
**Front:** Why did India replace the MRTP Act with the Competition Act, 2002, and what does the CCI do?
**Definition (learn):** Competition law prevents abuse of dominance, cartels and anti-competitive mergers; the Competition Act, 2002 replaced the Monopolies and Restrictive Trade Practices (MRTP) Act, 1969.
**Breakdown:**
- ✅ Competition Commission of India (CCI) enforces the Act; it preserves contestability after entry controls are removed (owner 16).
- ⚠️ The MRTP Act, 1969 focused on controlling monopoly size and restrictive practices (purpose not verified on the fetched pages); ✅ the Competition Act, 2002 prohibits abuse of dominance, anti-competitive agreements and anti-competitive combinations (Wikipedia, Competition Act, 2002), shifting the focus to conduct and effects.
- ✅ The Competition Act received assent on 13 January 2003 and commenced on 31 March 2003 (✅ Wikipedia, Competition Act, 2002 infobox; the CCI's establishment date is not on the page). The MRTP repeal in September 2009 is stated by Wikipedia but tagged 'citation needed' (⚠️), so the 2009 linkage is unconfirmed.
- ✅ Sector regulators (e.g., electricity, telecom) share contestability oversight with the CCI.
**Cases / Committees / Schemes / Data:** ✅ Owner 16 (CCI). ✅ Commencement years (Wikipedia); ⚠️ MRTP repeal year and CCI establishment date unverified.
**Trap:** The MRTP Act is not the Competition Act. The CCI is a competition regulator, not a sector regulator. Removing licences does not remove the need for competition law.
**Mains hook:** Argue that liberalisation needs a competition regulator; qualify with the concentration of digital platforms.
**Back:** *"MRTP counted the size; the Competition Act watches the conduct."*

### Flashcard T-142 — PSUs, Navratna, Maharatna and Miniratna
**Front:** What are public sector undertakings (PSUs), and what do the Navratna, Maharatna and Miniratna labels signal?
**Definition (learn):** PSUs are government-owned enterprises; the Department of Public Enterprises (DPE) grants status labels that give enhanced delegated powers to well-performing CPSEs.
**Breakdown:**
- ✅ PSUs can serve strategic or public objectives but need commercial accountability and governance.
- ✅ Not all PSUs are natural monopolies; only some sectors have strong network or strategic features.
- ✅ DPE status labels exist: Maharatna (created 2010), Navratna (from 1997), Miniratna (Category I/II) (✅ Wikipedia, Maharatna). ⚠️ Their thresholds are not reliably stated: the page's figures are internally inconsistent (enterprise counts and listed names differ), so quote no thresholds without the DPE guidelines.
- ✅ The labels grant delegated investment and expenditure powers (e.g. Navratna: up to ₹1,000 crore or 15% of net worth on a single project; Miniratna-I: up to ₹500 crore or net worth, whichever is lower; ✅ Wikipedia, Maharatna). Ownership is not changed by the label (not stated on the page).
**Cases / Committees / Schemes / Data:** ✅ Owner 16 (DPE as PSE policy framer); ⚠️ labels and criteria to verify from DPE.
**Trap:** Maharatna is not a privatisation or disinvestment category. A label does not imply control change. Navratna ≠ Maharatna.
**Mains hook:** Argue that PSU reform should be enterprise-by-enterprise; qualify with strategic-sector classification and governance.
**Back:** *"Mini, Navratna, Maharatna: the star shows the freedom, not the owner."*

### Flashcard T-143 — Disinvestment policy: DIPAM, strategic versus minority sale and Air India
**Front:** How does strategic disinvestment differ from a minority stake sale, and what did Air India show?
**Definition (learn):** Disinvestment is the sale of government equity in a public enterprise; strategic disinvestment transfers a substantial (typically controlling) stake with management control, whereas a minority sale keeps control with the state.
**Breakdown:**
- ✅ DIPAM (Department of Investment and Public Asset Management) manages Union disinvestment and asset-management transactions.
- ✅ Air India: government's shareholding transferred to Talace Private Limited (Tata Sons), completed January 2022 (✅ Wikipedia, Air India: sale announced 8 October 2021 for ₹180 billion; handover 27 January 2022; the page does not name Talace, so the entity name is ⚠️).
- ✅ Disinvestment proceeds are capital receipts from asset sale, not recurring revenue; they do not prove a durable fiscal improvement.
- ✅ Privatisation is the broader shift of ownership or control to private hands; strategic disinvestment is one route.
**Cases / Committees / Schemes / Data:** ✅ Owner 16 (Air India, DIPAM). ⚠️ Current disinvestment receipts to be taken from the latest DIPAM/Budget document.
**Trap:** Disinvestment ≠ privatisation (if control stays). Proceeds are capital receipts, not tax revenue. Announced sales are not always completed.
**Mains hook:** Argue that strategic sale is the clean privatisation route; qualify with case-by-case selectivity and fiscal dependence on one-off receipts.
**Back:** *"Minority sale keeps the keys; strategic sale hands them over: the Air India keys went to Tata in 2022."*

### Flashcard T-144 — New PSE Policy 2021 and asset monetisation (National Monetisation Pipeline)
**Front:** How does the New PSE Policy differ from asset monetisation, and what is the NMP?
**Definition (learn):** The New PSE Policy (announced in the 2021–22 Budget) sorts sectors into strategic and non-strategic; asset monetisation leases the revenue or operating rights of existing public assets to private parties while ownership remains public.
**Breakdown:**
- ✅ New PSE Policy: strategic sectors keep a minimal CPSE presence; non-strategic sectors are privatised or closed if not viable.
- ✅ National Monetisation Pipeline (NMP), launched August 2021: brownfield assets (roads, railways, power transmission) leased for a fixed period; ownership reverts to government.
- ✅ Monetisation is a financing structure, not a change of ownership; it still transfers operating and collection risk.
- ⚠️ The number of strategic sectors and NMP's target value should be verified from the official policy text.
**Cases / Committees / Schemes / Data:** ✅ Owner 16 and owner 18 (NMP, Aug 2021).
**Trap:** Monetisation ≠ disinvestment: monetisation keeps ownership. NMP asset leases are not a privatisation of the asset.
**Mains hook:** Argue that monetisation recycles brownfield capital for new build; qualify with contingent liabilities and regulatory oversight.
**Back:** *"Lease the asset, keep the title: monetise what exists to build what does not."*

### Flashcard T-145 — MSME classification and Udyam Registration
**Front:** What are the current MSME investment and turnover thresholds, and what is Udyam?
**Definition (learn):** MSME classification under the MSMED framework uses plant-and-machinery/equipment investment and annual turnover; Udyam Registration is the self-declared online registration that gives access to MSME benefits.
**Breakdown:**
- ✅ Current limits (notified by S.O. 1364(E), dated 21 March 2025, effective 1 April 2025): Micro: investment up to ₹2.5 crore and turnover up to ₹10 crore; Small: ₹25 crore and ₹100 crore; Medium: ₹125 crore and ₹500 crore.
- ✅ Previous limits (July 2020): Micro ₹1 crore / ₹5 crore; Small ₹10 crore / ₹50 crore; Medium ₹50 crore / ₹250 crore (superseded).
- ✅ Udyam Registration (replacing Udyog Aadhaar): paperless, Aadhaar- and PAN-linked, self-declared.
- ✅ Registration is an eligibility gateway, not a growth guarantee.
**Cases / Committees / Schemes / Data:** ✅ Owner 17 (as-of 1 April 2025 limits; verify further revision).
**Trap:** The 2020 limits are superseded. An enterprise can be an MSME without being a startup. 'Micro' is by investment and turnover, not employment.
**Mains hook:** Argue that formal classification enables credit and procurement access; qualify with the constraint of scale and technology.
**Back:** *"Two-fifty lakh and ten crore for micro, and the 2025 notification rewrote the old numbers."*

### Flashcard T-146 — MSME finance: CGTMSE and TReDS
**Front:** How do CGTMSE and TReDS address different MSME finance constraints?
**Definition (learn):** CGTMSE is a credit guarantee trust that covers lenders against default on collateral-free MSME loans; TReDS (Trade Receivables Discounting System) is an RBI-regulated platform for discounting accepted buyer invoices.
**Breakdown:**
- ✅ CGTMSE (Credit Guarantee Fund Trust for Micro and Small Enterprises) reduces lender risk for collateral-free loans.
- ✅ TReDS platforms (e.g., RXIL, Invoicemart, M1xchange) let MSMEs discount accepted receivables to financiers.
- ✅ Delayed payment is a distinct constraint from term-credit access; invoice discounting solves a different problem.
- ✅ TReDS depends on buyer acceptance of the invoice; non-acceptance limits its reach.
**Cases / Committees / Schemes / Data:** ✅ Owner 17.
**Trap:** TReDS is not a credit-rating agency; it facilitates invoice discounting. CGTMSE guarantees loans; it does not disburse them.
**Mains hook:** Argue that MSME credit needs guarantee, receivables and collateral reform together; qualify with buyer-side payment discipline.
**Back:** *"Guarantee the loan, discount the invoice: one covers the missing collateral, the other the missing payment."*

### Flashcard T-147 — Production-Linked Incentive (PLI) schemes
**Front:** How do PLI schemes work, and what is their central design principle?
**Definition (learn):** PLI pays incentives on verified incremental production or sales over a base year, in notified sectors, rather than on announced capacity.
**Breakdown:**
- ✅ Incentive is paid against incremental output or sales (additionality), not announced investment.
- ✅ Eligibility conditions and base years define measurable additionality; sanctioned outlay ≠ disbursed incentive.
- ✅ PLI for Food Processing (PLISFPI) is an example (T-130).
- ⚠️ PLI was approved across about 14 key sectors in 2020–21 with an outlay of about ₹1.97 lakh crore; verify the current sector list and outlay from the Union notification.
**Cases / Committees / Schemes / Data:** ✅ Owner 17 design; ⚠️ sector list and outlay not owner-verified.
**Trap:** PLI is not an unconditional grant; headline outlay is not disbursement. Large firms may capture gains while small units fail eligibility.
**Mains hook:** Evaluate PLI on additionality and spillovers to domestic suppliers; qualify with base-year gaming and disbursal data.
**Back:** *"Pay for the output you add, not the plant you promise: PLI is additionality, not charity."*

### Flashcard T-148 — Semiconductors: the India Semiconductor Mission (ISM)
**Front:** What is the ISM, and why is semiconductor policy an ecosystem, not only a fab?
**Definition (learn):** The India Semiconductor Mission (under MeitY) coordinates support for design, fabrication, assembly, testing, marking and packaging (ATMP/OSAT) and the downstream electronics chain.
**Breakdown:**
- ✅ Value chain: design, materials, equipment, fabrication, assembly and testing, downstream products.
- ✅ Anchor projects in owner 17 include a fab with PSMC associated with Tata Electronics and Micron's ATMP facility in Gujarat (construction began September 2023 with a stated US$2.75 billion investment, ✅ Wikipedia; commissioning status still to be checked).
- ✅ Fab viability depends on uninterrupted power, ultra-pure water, vibration-free logistics and skilled workforce.
- ⚠️ ISM's outlay of about ₹76,000 crore is confirmed (✅ Wikipedia, 'Semiconductor industry in India'); the December 2021 approval date is not confirmed.
**Cases / Committees / Schemes / Data:** ✅ Owner 17 (ISM under MeitY; Semicon India programme).
**Trap:** Semiconductor policy is not only fabs. Chip design and packaging are distinct stages. Announced projects are not completed production.
**Mains hook:** Argue that resilience requires the whole ecosystem; qualify with power, water and talent constraints.
**Back:** *"Design, fab, pack, test: the mission is a chain, and every link must hold current."*

### Flashcard T-149 — Make in India and Atmanirbhar Bharat
**Front:** How do Make in India and Atmanirbhar Bharat differ as manufacturing strategies?
**Definition (learn):** Make in India (launched 2014) is a campaign to attract manufacturing investment and raise domestic production; Atmanirbhar Bharat (2020) is a self-reliance framing that adds supply-chain resilience and import substitution.
**Breakdown:**
- ✅ Make in India was launched on 25 September 2014 (✅ Wikipedia, Make in India).
- ✅ Atmanirbhar Bharat was announced in May 2020 in the COVID-era economic package (announced 12 May 2020; ✅ Wikipedia, Atmanirbhar Bharat; the page notes economists dispute the headline ₹20 lakh crore size).
- ✅ Owner 16: modern industrial policy targets capabilities, infrastructure, technology and supply-chain resilience rather than only subsidies.
- ✅ Import substitution and export promotion can both serve resilience; they are not opposites.
**Cases / Committees / Schemes / Data:** ✅ Owner 16 (resilience framing); ✅ launch dates (Make in India 25 September 2014; Atmanirbhar Bharat 12 May 2020; Wikipedia).
**Trap:** Atmanirbhar is not autarky. Domestic production is not automatically efficient; resilience must be weighed against cost and scale.
**Mains hook:** Argue for targeted self-reliance in strategic sectors; qualify with the efficiency cost of blanket import substitution.
**Back:** *"Make here invites the factory; Atmanirbhar asks the factory to make the parts too."*

### Flashcard T-150 — Startups, unicorns and the incubator–accelerator ladder
**Front:** How do startups, MSMEs and unicorns differ, and where do incubators and accelerators fit?
**Definition (learn):** A startup is an innovation-led, scalable young firm (DPIIT recognition has eligibility conditions); an MSME is classified by size; a unicorn is a privately held startup valued at ≥ US$1 billion.
**Breakdown:**
- ✅ Startup policy addresses innovation, uncertainty and rapid scaling; MSME policy addresses credit, formalisation and market access.
- ✅ Incubators develop capability and networks; accelerators help more mature ventures grow rapidly.
- ✅ Venture finance stages: grants, seed equity, growth equity, venture debt, formal credit and exits; an exit recycles risk capital.
- ✅ A unicorn is a valuation label, not proof of profitability or employment.
**Cases / Committees / Schemes / Data:** ✅ Owner 17 (5A startup architecture).
**Trap:** Not every new business is a startup. Unicorn ≠ employment success. Venture capital does not finance every stage.
**Mains hook:** Argue that startup growth needs a finance ladder and exit routes; qualify with the valuation-versus-productivity gap.
**Back:** *"Incubate the idea, accelerate the scale, exit to recycle: the unicorn is a price, not a payroll."*

### GROUP — Infrastructure, logistics and public investment

### Flashcard T-151 — National Infrastructure Pipeline and PM GatiShakti
**Front:** What do the National Infrastructure Pipeline (NIP) and PM GatiShakti do for planning?
**Definition (learn):** NIP is a published project pipeline for infrastructure investment visibility across sectors; PM GatiShakti is a GIS-based National Master Plan for integrating multimodal planning.
**Breakdown:**
- ✅ corrected: NIP was first made public in the PM's 2019 Independence Day speech, with a five-year horizon of 2020–25 (✅ Wikipedia, National Infrastructure Pipeline; was: 'announced in December 2019 for the 2019–25 horizon'; the page gives no day). Outlay: the task force headed by Atanu Chakraborty projected about ₹111 lakh crore for 2020–25, submitted May 2020 (✅ Wikipedia). An undated 'initial sanctioned amount' of ₹102 lakh crore also appears on that page (⚠️ undated; quote with its source).
- ✅ PM GatiShakti (launched October 2021) is a digital platform integrating roads, railways, ports and other modes across ministries.
- ✅ National Logistics Policy (released September 2022) complements GatiShakti with standardisation, data-sharing and process reform.
- ✅ Fragmented sectoral planning was the problem that GatiShakti addresses.
**Cases / Committees / Schemes / Data:** ✅ Owner 18 (GatiShakti and NLP); ⚠️ The page's infobox 'sanctioned' figure is unexplained and is not used here.
**Trap:** A published pipeline is not spending; GatiShakti is planning infrastructure, not building it. National Logistics Policy ≠ National Logistics Plan.
**Mains hook:** Argue that planning silos cause logistics cost; qualify with execution bottlenecks (land, clearances, utility shifting).
**Back:** *"Pipeline shows the projects, GatiShakti shows the map, the logistics policy fixes the process."*

### Flashcard T-152 — PPP models: BOT, HAM, TOT, annuity and Viability Gap Funding
**Front:** How do PPP models allocate construction, demand and payment risk, and what is VGF?
**Definition (learn):** PPP allocates project functions and risks between public and private parties; models differ in who bears traffic/demand risk and how payment is made.
**Breakdown:**
- ✅ BOT (Build-Operate-Transfer): developer bears traffic/revenue risk; toll or annuity variants.
- ✅ HAM (Hybrid Annuity Model): from 2016, government funds about 40% of cost during construction and pays the rest as annuities (60%) with interest; government takes on traffic risk.
- ✅ TOT (Toll-Operate-Transfer): monetising completed toll roads for a concession fee.
- ✅ VGF: capital grant for socially useful but commercially sub-viable PPP projects, up to a notified ceiling.
- ✅ Post-2012 BOT stress (over-leveraged bids, optimistic traffic, land delays) led to HAM; Kelkar Committee (2015) recommended risk-sharing and independent dispute resolution.
**Cases / Committees / Schemes / Data:** ✅ Owner 18.
**Trap:** PPP is not free infrastructure. HAM shifts traffic risk to the government's fiscal commitment. VGF is not a general subsidy.
**Mains hook:** Critically examine PPP: allocate risk to the party best able to manage it; qualify with annuity liability and off-budget opacity.
**Back:** *"BOT takes the traffic risk, HAM hands it to the state, TOT sells the finished road, and VGF fills the gap."*

### Flashcard T-153 — Sagarmala and Vizhinjam: port-led development versus a trans-shipment hub
**Front:** How does Sagarmala differ from a single port project such as Vizhinjam?
**Definition (learn):** Sagarmala (2015) is the umbrella programme for port modernisation, port connectivity, port-led industrialisation and coastal-community development; Vizhinjam is a specific trans-shipment port.
**Breakdown:**
- ✅ Sagarmala (2015): four pillars: port modernisation, connectivity, port-led industrialisation (coastal economic zones), coastal-community development.
- ✅ Vizhinjam International Seaport (Kerala): deep-draft trans-shipment hub designed to capture container traffic currently routed via foreign ports.
- ✅ Container turnaround time fell from 43.44 hours (FY15) to 30.08 hours (FY25) (owner 18, 📰 as-of).
- ✅ Inland waterway cargo rose from 18 MMT (2013–14) to 146 MMT (2024–25) (owner 18, 📰 as-of).
**Cases / Committees / Schemes / Data:** ✅ Owner 18.
**Trap:** Sagarmala ≠ Vizhinjam. Trans-shipment ≠ port-led industrialisation. Port capacity does not equal throughput.
**Mains hook:** Argue that port-led growth depends on connectivity and industrial clusters; qualify with the hub's dependence on transshipment competition.
**Back:** *"Sagarmala is the sea-road; Vizhinjam is one lighthouse on it."*

### Flashcard T-154 — Bharatmala Pariyojana
**Front:** What is Bharatmala Pariyojana, and how does it relate to highway PPPs?
**Definition (learn):** Bharatmala Pariyojana is a national highway programme (approved in 2017–18) for economic corridors, border and coastal roads, and expressway connectivity.
**Breakdown:**
- ✅ Phase-I covers 2017–2022 under MoRTH (✅ Wikipedia, Bharatmala Pariyojana). ✅ corrected: the card said 'launched in 2017–18'; the page gives 31 July 2015 as the establishment date and no 2017–18 approval date.
- ✅ Highway awards shifted to HAM after 2016 (T-152); Bharatmala uses this model for many corridors.
- ✅ Components (✅ Wikipedia): economic corridors (26,200 km), inter-corridor and feeder routes (15,500 km), border and international connectivity roads (5,300 km), coastal and port connectivity roads (2,000 km), expressways (1,600 km).
**Cases / Committees / Schemes / Data:** ✅ Overall plan 83,677 km; Phase-I 34,800 km with a Phase-I budget of ₹692,324 crore for 2017–22; investment estimate ₹10.63 trillion as of March 2022 (✅ Wikipedia, Bharatmala Pariyojana; dated figures, not current MoRTH data).
**Trap:** Bharatmala is a road programme, not a railway or port programme. HAM is a contract model, not the programme name.
**Mains hook:** Evaluate highway expansion for logistics cost versus fiscal commitments in annuities.
**Back:** *"Bharat's roads, on corridors, paid in annuities."*

### Flashcard T-155 — Dedicated Freight Corridors (DFCs)
**Front:** What are Dedicated Freight Corridors, and why do they matter for logistics?
**Definition (learn):** DFCs are rail corridors reserved for freight to separate heavy goods traffic from passenger trains and raise speed and capacity.
**Breakdown:**
- ✅ corrected: the Eastern DFC runs from Ludhiana (Punjab) to Dankuni (West Bengal), 1,337 km (was: 'Ludhiana–Sonnagar'); the Western DFC runs from Dadri (UP) to JNPT (Mumbai), 1,504 km (✅ Wikipedia, Dedicated Freight Corridor). The page gives construction-completion statements (East: by February 2024; West: by March 2026) but no commissioning date; ⚠️ commissioning status to verify.
- ✅ DFCs address rail capacity, a logistics bottleneck, and integrate with GatiShakti planning.
- ✅ Rail-port and rail-freight connectivity is part of the multimodal chain (owner 18).
**Cases / Committees / Schemes / Data:** ⚠️ Corporation details not in the fetched text (DFCCIL page 404) and to be verified.
**Trap:** DFC is not a highway, and freight corridors do not replace road logistics.
**Mains hook:** Argue that modal shift to rail reduces logistics cost; qualify with last-mile road feeders.
**Back:** *"Freight on its own track: the corridor carries cargo, the passengers take the other line."*

### Flashcard T-156 — UDAN and the regional air connectivity scheme
**Front:** What is UDAN, and how is it funded?
**Definition (learn):** UDAN (Ude Desh ka Aam Nagrik) is the Regional Connectivity Scheme for under-served airports, supported by viability gap funding for airlines.
**Breakdown:**
- ✅ Launched 21 October 2016 under the Ministry of Civil Aviation (✅ Wikipedia, UDAN infobox; first regional flights flagged off 27 April 2017).
- ✅ Regional connectivity links under-served routes and airports, with capped fares on selected routes (✅ Wikipedia: fixed-wing cap of ₹2,500 per hour of flight on 50% of seats; distance-graded ceiling of ₹3,500 for 800 km or more; figures as stated on the page, verify current caps).
- ✅ Viability gap funding supports airlines on routes that are not commercially viable alone.
**Cases / Committees / Schemes / Data:** ✅ Owner 18 (2024 GS-III UDAN anchor).
**Trap:** UDAN is a connectivity viability scheme, not a general airport investment programme.
**Mains hook:** Argue that regional air connectivity needs viability funding and airport infrastructure; qualify with fare sustainability.
**Back:** *"Fly the regional route, fund the thin route, and the small town gets a runway."*

### Flashcard T-157 — InvITs and REITs
**Front:** How do Infrastructure Investment Trusts (InvITs) and REITs mobilise infrastructure capital?
**Definition (learn):** InvITs and REITs are SEBI-regulated trusts that pool investor capital into infrastructure or real-estate assets, distributing cash flows to unitholders.
**Breakdown:**
- ⚠️ Regulated by SEBI (InvIT and REIT regulations, 2014): Wikipedia's REIT page confirms India approved REITs as of August 2014, but gives no InvIT or SEBI regulation year.
- ✅ Asset monetisation and InvITs can recycle capital from completed brownfield assets into new projects.
- ⚠️ InvITs distribute income from operating assets; they are not government budgets or guarantees.
**Cases / Committees / Schemes / Data:** ⚠️ Dated issuance and listing data to be verified.
**Trap:** InvITs are not a government guarantee. Monetisation through InvIT does not transfer control to a private owner in every case (depends on structure).
**Mains hook:** Argue that trusts broaden infrastructure capital; qualify with leverage and yield-risk exposure.
**Back:** *"Pool the cash flows, pass the income to the unit, and the state does not sign the cheque."*

### Flashcard T-158 — China–Pakistan Economic Corridor (CPEC)
**Front:** What is CPEC, and how should it be analysed in an economy answer?
**Definition (learn):** CPEC (announced 2015) is a China–Pakistan infrastructure and investment corridor from Gwadar to Kashgar, a flagship of China's Belt and Road Initiative.
**Breakdown:**
- ✅ Reported outlay in the range of US$46–62 billion (owner 18, as-of).
- ✅ India's objections: sovereignty over Gilgit-Baltistan (Pakistan-occupied territory India claims), consultation and transparency, debt sustainability, strategic significance of Gwadar.
- ✅ Analyse CPEC as an investment-and-infrastructure question, separate from the sovereignty objection.
**Cases / Committees / Schemes / Data:** ✅ Owner 18.
**Trap:** CPEC is not an Indian project. Its economic and sovereignty dimensions must be kept separate in an answer.
**Mains hook:** Evaluate CPEC's economic logic and its strategic risks for India's neighbourhood policy.
**Back:** *"Gwadar to Kashgar is an economic corridor with a sovereignty question attached."*

### GROUP — Employment, labour codes, skills and social sector

### Flashcard T-159 — Four Labour Codes, 2019–2020
**Front:** What are the four labour codes, what laws do they consolidate, and when did they take effect?
**Definition (learn):** The four codes consolidate 29 central labour laws into four frameworks covering wages, industrial relations, social security, and occupational safety, health and working conditions.
**Breakdown:**
- ✅ Code on Wages, 2019.
- ✅ Industrial Relations Code, 2020.
- ✅ Code on Social Security, 2020.
- ✅ Occupational Safety, Health and Working Conditions (OSH) Code, 2020.
- ✅ Labour is on the Concurrent List; Centre–state rules are needed.
- ✅ Four codes notified to come into force on 21 November 2025; central rules in May 2026; state rules and enforcement uneven (owner 22, as-of August 2026).
- ⚠️ Thresholds (verify the notified Rules): IR Code's lay-off/retrenchment threshold was raised from 100 to 300 workers and the Code was notified 21 November 2025 (✅ Wikipedia, Industrial Relations Code, 2020; the closure-permission threshold is not separately verified); OSH Code applies to establishments with 10 or more workers (20 for some); Code on Social Security defines gig-aggregator contributions of 1–2% of annual turnover, capped at 5% of payouts.
**Cases / Committees / Schemes / Data:** ✅ Second National Commission on Labour (2002) recommended simplification and stronger social security (owner 22).
**Trap:** Commencement date ≠ uniform enforcement. The 29 laws are not the same as 'all labour laws'. Unemployment rates alone do not show quality.
**Mains hook:** Evaluate the codes on flexibility versus worker protection; qualify with state readiness and threshold effects.
**Back:** *"Four codes, twenty-nine laws, one Concurrent List: the codes are written in Delhi and enforced in the states."*

### Flashcard T-160 — Gig and platform workers and the Social Security Code
**Front:** How does the Code on Social Security treat gig and platform workers, and how big is the gig workforce?
**Definition (learn):** Gig work is task-based, short-term work mediated by digital platforms; platform work includes location-based (ride-hailing, delivery) and web-based segments.
**Breakdown:**
- ✅ The Code on Social Security, 2020 explicitly defines gig and platform workers for social-security coverage.
- ✅ NITI Aayog (2022): ~7.7 million gig workers in 2020–21 (≈2.6% of the non-agricultural workforce), projected to reach ~23.5 million by 2029–30.
- ✅ Skill mix projection: roughly 47% medium-skilled, 31% low-skilled and 22% high-skilled (owner 24).
- ✅ Algorithmic matching produces volatile per-task earnings.
**Cases / Committees / Schemes / Data:** ✅ Owner 22 and owner 24; 2020–21 baseline and 2029–30 projection only.
**Trap:** Do not interpolate gig figures for unreported years. Platform-level transactions ≠ worker earnings. Gig ≠ self-employment in every legal sense.
**Mains hook:** Argue that gig work expands flexibility but needs portable social security; qualify with aggregator contribution design and data gaps.
**Back:** *"Seven-point-seven million in 2020-21, twenty-three-point-five million by 2029-30: anchor on the stated years, never the in-between."*

### Flashcard T-161 — Skilling: PMKVY, NSQF and the employability gap
**Front:** How does PMKVY link training to employment, and why is certification not employment?
**Definition (learn):** PMKVY is the Pradhan Mantri Kaushal Vikas Yojana under Skill India Mission, providing short-duration training with assessment and certification aligned to the National Skills Qualification Framework (NSQF).
**Breakdown:**
- ✅ PMKVY: short-duration skill training, assessment and certification.
- ✅ NSQF: competency levels linking training to recognised qualifications.
- ✅ Sector Skill Councils and employers connect training with occupational demand and apprenticeships.
- ✅ Certification does not guarantee placement or wage gains; employer recognition matters.
**Cases / Committees / Schemes / Data:** ✅ Owner 22.
**Trap:** Skill training ≠ employment. NSQF levels are not degrees.
**Mains hook:** Argue that skilling must be demand-led; qualify with placement and wage outcomes.
**Back:** *"Train, test, certify, then find the employer: the certificate is a ticket, not a seat."*

### Flashcard T-162 — Demographic dividend: window, dependency ratio and female labour force
**Front:** What makes a demographic dividend, and why does female labour-force participation matter?
**Definition (learn):** A demographic dividend is the potential growth gain from a favourable working-age population structure, which is time-bound.
**Breakdown:**
- ✅ Dependency ratio: non-working population (0–14 and 60+/65+) relative to working-age population.
- ✅ Dividend requires education, skills, jobs and productivity growth.
- ✅ Female LFPR rose between 2017–18 and 2023–24 but remains below male LFPR (owner 22); rising headline numbers may reflect survey changes.
- ✅ Unpaid care work: Time Use Survey 2019 shows women spend about 299 minutes a day versus 97 for men (owner 22); outside GDP's production boundary.
- ✅ 'Ageing before becoming rich' risk if the window closes before incomes rise.
**Cases / Committees / Schemes / Data:** ✅ Owner 22.
**Trap:** A young population is not a dividend automatically. The dividend is not permanent. Aggregate LFPR is not enough; quality matters.
**Mains hook:** Argue that India must convert working-age share into productive jobs and women's participation; qualify with care infrastructure and formal jobs.
**Back:** *"The window opens on age, but only skills, jobs and care decide whether it pays."*

### Flashcard T-163 — Unemployment types and PLFS measurement
**Front:** What types of unemployment exist, and how does PLFS measure them?
**Definition (learn):** Unemployment types: frictional (job transition), structural (skill–job mismatch from technological or sectoral change), cyclical (business downturn), seasonal (agricultural cycle), disguised (surplus labour that adds no output).
**Breakdown:**
- ✅ PLFS (Periodic Labour Force Survey, NSO) reports LFPR, worker-population ratio and unemployment rate on usual status and current weekly status bases.
- ✅ Unemployment rate = unemployed persons ÷ labour force; a person outside the labour force is not counted as unemployed.
- ✅ Usual Principal status (UPS) and UPSS for structural and disguised; CWS and CDS for seasonal, frictional and under-employment (owner 22).
- ✅ Falling unemployment can reflect discouraged workers leaving the labour force.
**Cases / Committees / Schemes / Data:** ✅ Owner 22; Q2 FY26 had 56.2 crore employed persons aged 15+ (owner 22, 📰 as-of).
**Trap:** Unemployment rate ≠ employment quality. Usual status and weekly status are different bases. Cyclical unemployment is historically muted in India.
**Mains hook:** Argue that a falling unemployment rate must be checked against LFPR and quality; qualify with survey basis.
**Back:** *"Count the job-hunter, not the discouraged; choose the reference period, then read the rate."*

### Flashcard T-164 — Poverty lines: Tendulkar (2009) and Rangarajan (2014)
**Front:** How did the Tendulkar and Rangarajan committees differ on the poverty line?
**Definition (learn):** The poverty line is the minimum consumption standard below which a household is classed as poor; India's expert-group lines differ in method and anchor.
**Breakdown:**
- ✅ Tendulkar Committee (2009): shifted the basis from a calorie-norm anchor to a broader consumption basket including health and education.
- ✅ Rangarajan Committee (2014): proposed a revised, generally higher line using updated consumption norms.
- ✅ India has not adopted a single official successor line since (owner 23); attribute any figure to its method and year.
- 📰 ✅ Extreme poverty was 5.3% in 2022–23 on the revised World Bank US$3/day line; lower-middle-income poverty 23.9% (owner 23, as-of).
**Cases / Committees / Schemes / Data:** ✅ Owner 23.
**Trap:** Poverty ≠ inequality (Gini). Tendulkar ≠ Rangarajan. A poverty decline on one line can coexist with rising inequality.
**Mains hook:** Argue that poverty measurement needs method, line and inequality checks; qualify with the lack of a current official line.
**Back:** *"Tendulkar counted the basket, Rangarajan raised the bar; neither is the single 'official' line today."*

### Flashcard T-165 — Multidimensional Poverty Index (NITI Aayog)
**Front:** What does the MPI measure, and what are the key NITI figures?
**Definition (learn):** The MPI (Alkire–Foster methodology) measures deprivation across health, education and living standards, identifying multidimensionally poor households.
**Breakdown:**
- ✅ National MPI fell to 14.96% in 2019–21; estimated at 11.28% in 2022–23 (owner 23, as-of; the latter is an estimate).
- ✅ Urban MPI fell from 8.65% to 5.27% between NFHS-4 (2015–16) and NFHS-5 (2019–21), faster than rural (owner 23).
- ⚠️ The NITI MPI 2023 reported the national MPI at about 25.01% in 2015–16 (verify against the NITI source; Wikipedia's MPI page has no national NITI figures and the NITI site was not reached).
- ✅ Indicator weights and thresholds are methodological choices.
**Cases / Committees / Schemes / Data:** ✅ Owner 23.
**Trap:** MPI is not an income poverty line. A falling national urban average can hide slum deprivation in housing, sanitation and water.
**Mains hook:** Argue that MPI complements income poverty; qualify with its indicator design and the estimate status of 2022–23.
**Back:** *"Count five dimensions of deprivation, and the average can hide the slum."*

### Flashcard T-166 — Inequality measures: Lorenz curve and Gini coefficient
**Front:** How is income or consumption inequality measured, and how does it differ from poverty?
**Definition (learn):** The Lorenz curve plots cumulative population share against cumulative income or consumption share; the Gini coefficient is the ratio of the area between the diagonal and the Lorenz curve to the total triangle under the diagonal (0 = perfect equality, 1 = perfect inequality).
**Breakdown:**
- ✅ Gini = area between line of equality and Lorenz curve ÷ total area under line of equality.
- ✅ Income, consumption, wealth and multidimensional inequality answer different questions.
- ✅ Gini is sensitive to the underlying distribution and survey data.
- ✅ Poverty can fall while inequality rises if growth favours upper deciles.
**Cases / Committees / Schemes / Data:** ✅ Owner 23 (Lorenz/Gini definitions).
**Trap:** Gini is not poverty. A high Gini does not equal a high poverty rate. Gini values vary by consumption vs income basis.
**Mains hook:** Argue that poverty and inequality require separate indicators; qualify with the data basis for each.
**Back:** *"Lorenz bends, Gini measures the bend: low Gini is closer to equality, not closer to zero poverty."*

### Flashcard T-167 — MGNREGA: the rural employment guarantee
**Front:** What does MGNREGA guarantee, and why is it a demand-driven safety net?
**Definition (learn):** MGNREGA (2005, now repealed; see Breakdown) guaranteed up to 100 days of unskilled manual employment per rural household per year, with wages paid if work is not provided.
**Breakdown:**
- ✅ Up to 100 days per rural household per year (owner 23).
- ✅ Demand-driven self-targeting: work is available to those who seek it at a set wage.
- ✅ Wage-payment delays or capped budgets can undermine the guarantee in high-demand periods.
- ✅ corrected: MGNREGA is no longer in force. Wikipedia (MGNREGA) lists its status as 'Repealed' and says Parliament repealed it in 2025 after both Houses passed the Viksit Bharat–Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, 2025 (VB-G RAM G); cited news is dated 18–19 December 2025, though the page gives no separate house dates (was: 'a replacement Bill was reported'). MGNREGA's own dates on the page: Lok Sabha 23 August 2005, Rajya Sabha 25 August 2005, assent 5 September 2005, commencement 2 February 2006. The successor's assent, commencement and day-guarantee are not verified (the 125-day figure is not on the page); the 100-day rule above describes MGNREGA as enacted.
**Cases / Committees / Schemes / Data:** ✅ Owner 23 (MGNREGA as demand-driven safety net).
**Trap:** MGNREGA is not an unemployment allowance; it is employment-linked. Self-targeting does not mean costless.
**Mains hook:** Argue that rural employment guarantees cushion shocks and rural demand; qualify with fund flow and asset quality.
**Back:** *"A hundred days if you ask, and the state pays even when it is late."*

### Flashcard T-168 — DAY-NRLM: rural livelihoods and self-help groups
**Front:** What is DAY-NRLM, and how does it work?
**Definition (learn):** The Deendayal Antyodaya Yojana–National Rural Livelihoods Mission (DAY-NRLM) builds self-help groups (SHGs) and federations to raise poor rural households' incomes.
**Breakdown:**
- ✅ SHG-based credit, skills and livelihood activities; community institutions as the delivery route.
- ⚠️ Launched in 2011 under Ministry of Rural Development.
- ✅ Community institutions link to bank credit and to scheme delivery.
**Cases / Committees / Schemes / Data:** ⚠️ Current coverage numbers to verify.
**Trap:** NRLM is not a credit scheme alone. SHG finance is not the same as KCC.
**Mains hook:** Argue that community institutions turn microfinance into livelihoods; qualify with repayment and sustainability risks.
**Back:** *"Self-help groups carry the loan, the livelihood and the voice."*

### Flashcard T-169 — Pradhan Mantri Awas Yojana (PMAY): housing for all
**Front:** What does PMAY deliver, and how does it differ between rural and urban strands?
**Definition (learn):** PMAY is a central housing scheme providing financial assistance for houses to eligible households, with rural (PMAY-G) and urban (PMAY-U) components.
**Breakdown:**
- ✅ PMAY-U launched 25 June 2015 (✅ Wikipedia, Pradhan Mantri Awas Yojana). ⚠️ PMAY-G's 2016 launch is not given on that page (it says IAY was merged into PMAY-G 'as of 2016').
- ✅ Assistance is targeted by eligibility criteria linked to socio-economic data.
- ✅ Housing is a capability and asset dimension of poverty measurement (MPI housing indicator).
**Cases / Committees / Schemes / Data:** ⚠️ Unit assistance amounts and completion targets to verify.
**Trap:** A house is not automatically an asset improvement; eligibility errors can exclude genuine households.
**Mains hook:** Argue housing is a multidimensional poverty dimension; qualify with eligibility and quality.
**Back:** *"Two strands, one roof: rural poor and urban poor, each with a checklist."*

### Flashcard T-170 — Ayushman Bharat PM-JAY: health insurance for vulnerable families
**Front:** How does PM-JAY work, and what does it not cover?
**Definition (learn):** PM-JAY (Pradhan Mantri Jan Arogya Yojana) is the insurance-based health cover for secondary and tertiary hospitalisation for identified vulnerable families.
**Breakdown:**
- ✅ Eligibility via SECC-based database (owner 23).
- ✅ Cover of ₹5 lakh per family per year (✅ Wikipedia, PM-JAY; the scheme's own text was not separately checked).
- ✅ Addresses catastrophic hospitalisation shocks.
- ✅ Does not fix primary-care access, outpatient spending or diagnostics gaps.
- ✅ Ayushman Bharat Health and Wellness Centres anchor primary care (owner 23).
**Cases / Committees / Schemes / Data:** ✅ Owner 23.
**Trap:** PM-JAY is not universal health insurance. SECC exclusion errors are a standing risk.
**Mains hook:** Argue that insurance protects against catastrophic spending; qualify with the primary-care and outpatient gap.
**Back:** *"Insurance for the big bill; the small bill still has to be fixed at the health centre."*

### Flashcard T-171 — PMJDY and the Financial Inclusion Index
**Front:** What did Jan Dhan achieve, and how does the RBI Financial Inclusion Index measure inclusion?
**Definition (learn):** Financial inclusion is the access and usage of formal financial services; PMJDY (2014) opened basic bank accounts, and the RBI Financial Inclusion Index aggregates access, usage and quality.
**Breakdown:**
- ✅ PMJDY launched in 2014 for near-universal basic bank accounts.
- ✅ RBI FI-Index (base 2021 = 53.9): 64.2 in March 2024; 67.0 in March 2025 (owner 23).
- ✅ Index measures access and usage, not income growth.
- ✅ Dormant accounts and deprivation in housing and sanitation can persist.
**Cases / Committees / Schemes / Data:** ✅ Owner 23 (FI-Index values as of March 2024 and March 2025).
**Trap:** Account ownership ≠ usage. FI-Index is not a poverty measure.
**Mains hook:** Argue that account access is necessary but not sufficient for inclusion; qualify with usage and quality.
**Back:** *"An account is a door, not a balance; the index counts the door, the use and the quality."*

### GROUP — Services, digital payments and data economy

### Flashcard T-172 — Unified Payments Interface (UPI)
**Front:** How does UPI move money, and what does its two-factor design protect?
**Definition (learn):** UPI is the real-time, interoperable bank-to-bank retail payment system built by the National Payments Corporation of India (NPCI); it transfers commercial-bank deposits instantly.
**Breakdown:**
- ✅ Authorisation: registered mobile or device (something held) plus UPI PIN/MPIN (something known); the PIN is entered on the payer's own device and is never supplied to the payee.
- ✅ UPI moves commercial-bank deposit money; it is not a central-bank liability (the digital rupee is).
- ✅ Merchant Discount Rate (MDR) is paid by the merchant, not the customer, and is shared among the acquiring bank, issuing bank and network; zero MDR for UPI person-to-merchant and RuPay debit cards since January 2020 (owner 24); reintroduction on select high-value transactions reported (verify).
- ✅ National Financial Switch (NFS) is the separate NPCI interbank ATM network.
**Cases / Committees / Schemes / Data:** ✅ Owner 24 (UPI, MDR, NFS). ✅ Owner 24 (Aadhaar-linked DBT as the earlier rail).
**Trap:** UPI ≠ digital rupee. MDR is merchant-paid. NFS is not UPI. UPI is not 'free' infrastructure in all cases; costs are shared.
**Mains hook:** Argue that UPI is digital public infrastructure lowering entry costs; qualify with cybersecurity, MDR design and platform concentration.
**Back:** *"Mobile for what you hold, PIN for what you know: the payee never sees the second key."*

### Flashcard T-173 — Fintech and digital lending: RBI's digital lending regulation
**Front:** How does RBI regulate digital lending, and what problem does it solve?
**Definition (learn):** Fintech uses technology to deliver or intermediate financial services; digital lending is loan origination and servicing through digital platforms, which RBI regulates through its Digital Lending Guidelines.
**Breakdown:**
- ✅ Digital Lending Guidelines (building on a Working Group report) require direct disbursal and repayment through the borrower's bank account, and standardised lending-service providers.
- ✅ Enforcement targets fully unregulated or offshore lending apps.
- ✅ Fintech can lower cost and expand access but does not remove credit or fraud risk.
- ⚠️ Guidelines issued 2022 (verify).
**Cases / Committees / Schemes / Data:** ✅ Owner 24.
**Trap:** Fintech is not automatically a bank or a licensed lender. Lending apps may be unlicensed or offshore. Digital lending does not reduce credit risk by itself.
**Mains hook:** Argue that digital lending widens access but needs regulated intermediation and consumer protection; qualify with over-indebtedness and fraud.
**Back:** *"Money goes to your bank, not the app, and every lender must hold a licence that the app can show."*

### Flashcard T-174 — Account Aggregator, ONDC and platform competition
**Front:** What do the Account Aggregator framework and ONDC add to digital public infrastructure?
**Definition (learn):** The Account Aggregator (AA) framework is an RBI-regulated consent-based data-sharing layer; ONDC (Open Network for Digital Commerce) is a government-backed open protocol that lets buyers and sellers transact across apps.
**Breakdown:**
- ✅ AA: consent-based sharing of financial data between regulated institutions through licensed NBFC account aggregators.
- ✅ ONDC: interoperability to prevent large platforms from becoming the sole gateway between buyers and sellers; it does not replace private apps.
- ✅ Platforms with network effects and data advantages can entrench dominance; regulation can weaken but rarely eliminate first-mover advantages.
- ✅ ONDC was incorporated on 31 December 2021 and its pilot launched on 29 April 2022 in five cities (✅ Wikipedia, Open Network for Digital Commerce). Dated figures on that page: over 370,000 vendors and service providers (February 2024) and 14 million transactions in October 2024; current volumes not verified.
**Cases / Committees / Schemes / Data:** ✅ Owner 24.
**Trap:** ONDC is not a separate e-commerce company. AA does not hold your data; it routes consented flows. Network effects are not automatically monopoly.
**Mains hook:** Argue that open protocols lower entry barriers; qualify with adoption depth and data-portability enforcement.
**Back:** *"Consent travels through the aggregator, the catalogue travels through the open network: neither owns the customer."*

### Flashcard T-175 — Digital Personal Data Protection Act, 2023 (DPDP)
**Front:** What is the DPDP framework, and what are its main design choices?
**Definition (learn):** The DPDP Act, 2023 governs digital personal data processing through consent or a listed 'legitimate use', creating the Data Protection Board of India.
**Breakdown:**
- ✅ Processing needs free, specific, informed consent (plain-language notice) or a legitimate use (e.g., voluntary provision for a specified purpose).
- ✅ Significant Data Fiduciaries face heavier obligations (Data Protection Impact Assessment, Data Protection Officer).
- ✅ Rules notified November 2025; obligations phased through 2027; Consent Manager registration and most rights obligations are phased (owner 24, as-of).
- ✅ Design trade-off: ease of compliance for small firms versus accountability for large platforms.
**Cases / Committees / Schemes / Data:** ✅ Owner 24 (Data Protection Board of India, Rules Nov 2025).
**Trap:** DPDP is not fully in force; treat it as enacted and partly in force. Consent is not the only lawful basis. Significant Data Fiduciaries are a notified category.
**Mains hook:** Discuss DPDP as a consent-and-accountability architecture; qualify with phased implementation and small-business compliance load.
**Back:** *"Consent or legitimate use, a board to enforce, and a phase-in calendar: privacy in three steps."*

### Flashcard T-176 — Virtual Digital Assets (VDA), crypto taxation and the digital rupee
**Front:** How is crypto (VDA) taxed in India, and what is the digital rupee?
**Definition (learn):** VDA covers crypto and similar digital assets; the digital rupee (e₹, CBDC) is a direct RBI liability, like sovereign currency, in a central bank digital currency pilot.
**Breakdown:**
- ✅ VDA transfers taxed at a flat 30% (Section 115BBH, Income-tax Act) with 1% TDS (Section 194S).
- ✅ VDA service providers must register with FIU-IND under PMLA.
- ✅ NFT: unique non-fungible token recording ownership/provenance; does not automatically confer copyright.
- ✅ Blockchain is distributed-ledger technology; cryptocurrency is one application.
- ✅ Digital rupee is an RBI liability; UPI is a commercial-bank deposit transfer.
**Cases / Committees / Schemes / Data:** ✅ Owner 24 (5A).
**Trap:** Crypto ≠ blockchain. Digital rupee ≠ UPI. NFT ≠ fungible crypto. Tax on VDA is not the same as regulation of issuance.
**Mains hook:** Argue that India has chosen taxation and AML-registration over outright crypto legality; qualify with the regulatory gap and the digital rupee's distinct role.
**Back:** *"Thirty percent on the gain, one percent at source, and the digital rupee is the RBI's own promise."*

### GROUP — Climate economics, green finance and circular economy

### Flashcard T-177 — Carbon pricing: PAT to the Carbon Credit Trading Scheme (CCTS)
**Front:** How has India moved from PAT to a compliance carbon market, and what is the Social Cost of Carbon?
**Definition (learn):** Carbon pricing applies a price signal to emissions via tax or trading; PAT (Perform, Achieve and Trade) and CCTS are India's trading instruments; Social Cost of Carbon (SCC) is a monetised damage estimate used in appraisal.
**Breakdown:**
- ✅ PAT (under the Energy Conservation Act): energy-intensity targets for large industrial units; over-achievers trade Energy Saving Certificates.
- ✅ CCTS (Energy Conservation (Amendment) Act, 2022; Bureau of Energy Efficiency administers): intensity-based baseline-and-credit; Carbon Credit Certificates trading from FY2026 onward.
- ✅ Obligated sectors include aluminium, cement, chlor-alkali, pulp and paper, petrochemicals; first compliance cycle ongoing (owner 25, as-of August 2026).
- ✅ Iron and steel: draft notification dated 26 June 2026 covering 255 plants (FY2023–24 baseline; reductions from about 2.1% to 9.3%, median about 5.5%; compliance intended from FY2026–27); public consultation, not final (owner 25).
- ✅ SCC: monetised damage per additional tonne of CO2 for policy appraisal; not a tax rate or a traded price.
**Cases / Committees / Schemes / Data:** ✅ Owner 25.
**Trap:** PAT targets energy intensity, not absolute emissions. CCTS is not a full economy-wide market. SCC ≠ carbon price. A draft notification is not an obligation.
**Mains hook:** Argue that intensity-based trading lets growth continue while cutting emissions per output; qualify with absolute-emission rises and sector coverage.
**Back:** *"Intensity first, credits next, SCC tells you what the damage is worth, not what the market charges."*

### Flashcard T-178 — National Green Hydrogen Mission
**Front:** What does the National Green Hydrogen Mission do, and where is it aimed?
**Definition (learn):** Green hydrogen is hydrogen produced by electrolysis powered by renewable electricity; the mission (approved January 2023) builds electrolyser manufacturing, production and demand in hard-to-abate sectors.
**Breakdown:**
- ✅ Demand targets: refining, fertiliser, steel and shipping; export potential.
- ✅ Distinct from renewable-electricity auctions: it builds a fuel pathway.
- ✅ Production cost and electrolyser capacity are early-stage; compare with grey and blue hydrogen.
**Cases / Committees / Schemes / Data:** ✅ Owner 25 (approved January 2023). ⚠️ Outlay and capacity targets to verify (Wikipedia's National Green Hydrogen Mission page 404s; the 'Hydrogen economy' page has no outlay).
**Trap:** Green ≠ blue (CCUS-linked) hydrogen. Electrolyser manufacturing is not hydrogen production.
**Mains hook:** Argue that hydrogen is a hard-to-abate decarbonisation route; qualify with cost and storage.
**Back:** *"Renewable power splits the water: green is the colour of the power, not of the pipe."*

### Flashcard T-179 — Green finance: green bonds, sovereign green bonds and disclosure
**Front:** How do green bonds and climate-risk disclosure finance the transition?
**Definition (learn):** Green bonds finance eligible environmental projects with use-of-proceeds tracking; sustainability bonds combine environmental and social uses; transition risk is the financial risk from decarbonisation policy or technology change.
**Breakdown:**
- ✅ India issued its first Sovereign Green Bonds from FY2022–23 to finance eligible public-sector green projects, tracked against a Sovereign Green Bond Framework.
- ✅ RBI has issued guidance and discussion papers on climate-related financial risk for regulated entities.
- ✅ SEBI requires Business Responsibility and Sustainability Reporting (BRSR) for the top listed companies by market capitalisation.
- ✅ Labelling depends on credible use-of-proceeds reporting.
**Cases / Committees / Schemes / Data:** ✅ Owner 25.
**Trap:** Green bond proceeds do not guarantee environmental results. BRSR is disclosure, not a tax. Transition risk ≠ physical risk.
**Mains hook:** Argue that green finance requires disclosure and credible tracking; qualify with greenwashing risk and the rollout across firms.
**Back:** *"Label the bond, track the use, disclose the risk: green money needs a paper trail."*

### Flashcard T-180 — Extended Producer Responsibility (EPR) and circular economy
**Front:** What is EPR, and how does it link to the circular economy?
**Definition (learn):** EPR makes producers or brand-owners responsible for the collection and recycling of their products at end of life; circular economy keeps materials in use through reduce, redesign, reuse, repair, refurbish, remanufacture and recycle.
**Breakdown:**
- ✅ EPR is notified for plastic packaging waste and e-waste under management rules; compliance is often traded via EPR certificates.
- ✅ Compliance needs monitoring and verification of actual collection and recycling.
- ✅ Informal waste processing is large in India and complicates measurement.
- ✅ Just transition considers workers, regions and consumers during structural change.
**Cases / Committees / Schemes / Data:** ✅ Owner 25.
**Trap:** EPR ≠ voluntary recycling. Circular economy is not only recycling; reduction and reuse come first in the logic.
**Mains hook:** Argue that EPR internalises end-of-life cost; qualify with verification and the informal sector.
**Back:** *"Whoever sells the bottle buys back the bottle: reduce, reuse, then recycle."*

### Flashcard T-181 — India's NDC commitments and the non-fossil capacity targets
**Front:** What did India commit to under the 2022 updated NDC and at COP26, and what is the progress marker?
**Definition (learn):** A Nationally Determined Contribution (NDC) is a country's Paris Agreement climate target; India's COP26 'Panchamrit' announcements included 500 GW of non-fossil capacity by 2030.
**Breakdown:**
- ✅ 2022 updated NDC: about 50% of cumulative installed electric-power capacity from non-fossil sources by 2030 (owner 25).
- ✅ COP26 (Glasgow, 2021): 500 GW non-fossil installed capacity by 2030, plus 50% of energy requirements from renewables by 2030, one billion tonnes less projected emissions, carbon intensity below 45% by 2030, net zero by 2070 (owner 31).
- ✅ Non-fossil share of installed capacity was 51.93% at end-December 2025 (owner 31, Survey as-of); this is capacity, not generation.
**Cases / Committees / Schemes / Data:** ✅ Owners 25 and 31.
**Trap:** The 500 GW target is installed capacity, not generation share or energy consumption. Non-fossil includes nuclear and large hydro, not only renewables. 'Energy independence by 2047' is a horizon, not a verified outcome.
**Mains hook:** Separate mitigation, adaptation and energy security; qualify with grid, storage, finance and just-transition constraints.
**Back:** *"Fifty percent capacity, five hundred gigawatts, net zero by seventy: the NDC is a power-plant promise."*

### Flashcard T-182 — Carbon Border Adjustment Mechanism (CBAM)
**Front:** What is the CBAM, and how does India's response differ from it?
**Definition (learn):** CBAM is the EU's border carbon adjustment: importers of carbon-intensive goods pay a charge reflecting the carbon price not paid in the country of origin.
**Breakdown:**
- ✅ CBAM is an EU trade instrument, not an Indian carbon market.
- ✅ India's responses: CCTS, MRV and domestic decarbonisation, reciprocal to external carbon-border pressure.
- ✅ CBAM-related exports require emissions data and verification.
**Cases / Committees / Schemes / Data:** ✅ Owner 25 (CBAM as external pressure).
**Trap:** CBAM is not part of India's carbon market. It is not a domestic carbon tax. India does not adopt the EU mechanism.
**Mains hook:** Argue that India must build MRV and domestic carbon pricing to protect export competitiveness; qualify with data costs.
**Back:** *"The EU charges the border, India builds the meter."*

### GROUP — Energy economics: power, distribution, fuels and security

### Flashcard T-183 — Electricity Act, 2003 and the power-sector institutions
**Front:** What does the Electricity Act, 2003 do, and which bodies regulate the power sector?
**Definition (learn):** The Electricity Act, 2003 consolidated the law on generation, transmission, distribution, trading and use; it delicensed most generation and allowed open access, while licensing transmission, distribution and trading.
**Breakdown:**
- ✅ Generation delicensed (subject to hydro and technical requirements); transmission, distribution and trading licensed.
- ✅ Institutions: Ministry of Power; Central Electricity Authority (planning, standards); CERC (inter-state tariffs); SERCs (intra-state tariffs and distribution licensing); APTEL (appeals); Grid-India (national/regional operation); CTU/STU; SLDC; BEE; EESL; PFC/REC.
- ✅ Electricity is on the Concurrent List; states own distribution and tariff roles.
- ✅ The Electricity (Amendment) Bill, 2025 is a Bill/proposal, not the Act.
**Cases / Committees / Schemes / Data:** ✅ Owner 31.
**Trap:** REC Ltd (finance company) ≠ REC (Renewable Energy Certificate). MW is capacity; MWh is energy. Electrified village ≠ reliable supply.
**Mains hook:** Argue that open access and independent regulators enable competition; qualify with state ownership of distribution and cross-subsidy.
**Back:** *"Generation opened, wires licensed, tariffs regulated, and the states still own the last mile."*

### Flashcard T-184 — DISCOM stress, UDAY and the RDSS
**Front:** What causes DISCOM losses, and what did UDAY and RDSS try to fix?
**Definition (learn):** DISCOMs are distribution utilities; their finance depends on AT&C losses (technical plus commercial) and the ACS-ARR gap (average cost of supply minus average revenue realised).
**Breakdown:**
- ✅ Operational causes: overloaded networks, technical losses, theft, defective metering, billing and collection failures.
- ✅ Financial causes: tariffs below cost, delayed tariff orders, delayed subsidy payments, expensive PPAs, debt.
- ✅ Vicious cycle: under-recovery → delayed generator payment → weak maintenance → worse losses → lower recovery.
- ✅ UDAY (historical): state takeover of legacy DISCOM debt; debt transfer without operational reform recurs.
- ✅ RDSS (Revamped Distribution Sector Scheme): approved outlay about ₹3,03,758 crore for FY2021–22 to FY2025–26, of which central GBS about ₹97,631 crore; funds smart prepaid metering and network upgrades (owner 31, as-of).
**Cases / Committees / Schemes / Data:** ✅ Owner 31.
**Trap:** AT&C ≠ ACS-ARR. Reducing theft may still leave a DISCOM loss-making if tariffs or subsidies are inadequate. A smart meter alone is not governance reform. RDSS outlay ≠ AT&C figure.
**Mains hook:** Argue that DISCOM reform needs tariffs, subsidy payments and governance together; qualify with the debt-transfer trap of UDAY.
**Back:** *"Losses are two beasts: theft and tariff; UDAY took the debt, RDSS takes the meters, and only governance closes the loop."*

### Flashcard T-185 — Renewable procurement: auctions, RPO and RECs
**Front:** How are renewable projects procured in India, and what do RPOs and RECs do?
**Definition (learn):** Renewable procurement uses competitive auctions (SECI and state utilities) to discover tariffs; RPO (Renewable Purchase Obligation) requires obligated entities to buy a prescribed renewable share; REC (Renewable Energy Certificate) is a tradable certificate for the renewable attribute of electricity.
**Breakdown:**
- ✅ Auctions have lowered discovered tariffs over successive rounds.
- ✅ RPO compliance can be met through electricity purchase or REC purchase.
- ✅ Very low bid tariffs have raised viability and discom payment-security concerns.
- ✅ Renewable capacity addition: 38.61 GW installed in FY2025–26 up to 31 December 2025 (owner 31, as-of; 📰).
- ✅ Storage, transmission and curtailment are the integration constraints.
**Cases / Committees / Schemes / Data:** ✅ Owner 25 (auctions) and owner 31 (RPO, REC, curtailment).
**Trap:** REC ≠ REC Ltd. Capacity share ≠ generation share. Auction tariff is not the all-in system cost (balancing and storage excluded).
**Mains hook:** Argue that auctions deliver cheap renewables; qualify with storage, transmission and discom payment security.
**Back:** *"Bid for the tariff, obligate for the share, certify the green attribute: three tools, one target."*

### Flashcard T-186 — Petroleum and natural gas economics: upstream, midstream, downstream and PNGRB
**Front:** Which bodies govern upstream versus midstream and downstream petroleum, and what does PNGRB regulate?
**Definition (learn):** Upstream = exploration and production (MoPNG and DGH); midstream and downstream = transport, storage, distribution and retailing, regulated by PNGRB within its statute.
**Breakdown:**
- ✅ PNGRB (Petroleum and Natural Gas Regulatory Board) regulates notified midstream and downstream petroleum and natural-gas activities.
- ✅ PNGRB does not regulate crude-oil or natural-gas production (upstream).
- ✅ ISPRL: strategic petroleum reserve infrastructure.
- ✅ Natural gas chain: production → transmission → city gas distribution → PNG/CNG end use.
- ✅ Petroleum prices and taxation: crude, refinery and product distinctions matter.
**Cases / Committees / Schemes / Data:** ✅ Owner 31 (2025 Prelims closure on PNGRB's boundary).
**Trap:** Crude import dependence ≠ product trade: India can import crude and export refined products. Resource ≠ reserve.
**Mains hook:** Argue that petroleum regulation is split by value-chain stage; qualify with price-control and tax linkages.
**Back:** *"Upstream is drilled by the ministry, downstream is regulated by the board: know which side the pipeline is on."*

### Flashcard T-187 — LPG, PNG and clean cooking: PM Ujjwala Yojana
**Front:** What does PM Ujjwala Yojana achieve, and what limits its economics?
**Definition (learn):** PM Ujjwala Yojana (PMUY) provides clean-cooking LPG connections to poor households, shifting cooking away from solid fuels.
**Breakdown:**
- ✅ Clean-cooking LPG access; sustained refill affordability still matters.
- ✅ PNG/CNG distribution is a city gas network regulated under PNGRB's midstream/downstream remit.
- ✅ Energy access includes connection, availability, reliability, affordability, quality and clean cooking.
**Cases / Committees / Schemes / Data:** ✅ Owner 31 (access ladder).
**Trap:** Connection ≠ consumption. An LPG connection is not clean cooking if refills are unaffordable. PNG is a pipeline network, not a cylinder.
**Mains hook:** Argue that clean cooking needs affordable refills as well as connections; qualify with usage gaps.
**Back:** *"A connection is a door, a refill is the meal."*

### Flashcard T-188 — Strategic petroleum reserves and energy security
**Front:** What are the five dimensions of energy security, and what do strategic stocks do?
**Definition (learn):** Energy security is reliable access to adequate energy at affordable prices, resilient to supply, price, geopolitical and climate shocks.
**Breakdown:**
- ✅ Five dimensions: availability, accessibility, affordability, acceptability and resilience.
- ✅ Import-shock transmission: global price shock → import bill and exchange rate → fuel, power and fertiliser cost → inflation and current-account pressure → household and firm margins.
- ✅ Security instruments: diversify countries and routes; strategic and commercial stocks; refining, LNG and storage capacity; efficiency; renewables and nuclear.
- ✅ Energy security does not require domestic production of every unit.
**Cases / Committees / Schemes / Data:** ✅ Owner 31 (13.1–13.3); ✅ ISPRL as SPR operator.
**Trap:** Energy self-sufficiency ≠ energy security. Strategic reserves are not the same as commercial stocks.
**Mains hook:** Argue that diversification and stocks beat autarky; qualify with price pass-through and low-income protection.
**Back:** *"Five doors to security: availability, access, affordability, acceptability, resilience: and the reserves are the backup key."*

### Flashcard T-189 — Ethanol Blended Petrol (EBP) and biofuel trade-offs
**Front:** What did the ethanol-blending programme achieve, and what feedstock trade-offs does it raise?
**Definition (learn):** EBP blends ethanol with petrol; India's programme aims to reduce import dependence and farm-linked income, using sugarcane juice/molasses and grain-based feedstock.
**Breakdown:**
- ✅ India reached 20% ethanol blending (E20) in 2025, about five years ahead of the 2030 target; up from about 1.5% in 2014 (owner 31, reported; verify latest release).
- ✅ Reported associated figures: foreign-exchange savings ~₹1.36 lakh crore; payments to distilleries ~₹1.96 lakh crore; to farmers ~₹1.18 lakh crore; ~698 lakh tonnes CO2 avoided (government-reported cumulative; re-verify).
- ✅ Feedstock trade-offs: sugarcane vs maize vs surplus rice; water and food-price effects.
**Cases / Committees / Schemes / Data:** ✅ Owner 31 (24.1–24.3).
**Trap:** E20 is a blend share, not a fuel standard for every vehicle. Sugarcane-based ethanol ≠ grain-based ethanol in economics.
**Mains hook:** Argue that blending reduces import dependence; qualify with food-price and water trade-offs.
**Back:** *"Twenty in the tank, but the feedstock decides whether it is energy or the food basket that pays."*

### Flashcard T-190 — Nuclear energy in India
**Front:** How is nuclear energy governed in India, and how does it fit the non-fossil target?
**Definition (learn):** Nuclear power is a non-fossil source counted in the non-fossil capacity target (not in 'renewables'), governed by atomic energy law and state-owned operators.
**Breakdown:**
- ✅ Atomic Energy Act, 1962 (in force September 1962; ✅ Wikipedia, Nuclear power in India). ⚠️ NPCIL's operation of most power reactors is not stated on the fetched text; verify.
- ✅ Non-fossil includes nuclear and large hydro; renewable does not mean every non-fossil source (owner 31).
- ✅ SHANTI Act, 2025 was passed by both Houses in the 2025 winter session and enables limited private participation under regulatory oversight (✅ Wikipedia, Nuclear power in India). ⚠️ The page is internally inconsistent: it says the SHANTI Act replaced and repealed the Atomic Energy Act, yet also refers to a 2026 budget proposal to amend that Act; verify the current status and commencement.
**Cases / Committees / Schemes / Data:** ✅ Owner 31 (non-fossil classification); ⚠️ operator and law details to verify.
**Trap:** Nuclear ≠ renewable. Non-fossil ≠ renewable. Nuclear capacity count is not generation share.
**Mains hook:** Argue that nuclear provides firm non-fossil power; qualify with capital cost, waste and liability.
**Back:** *"Non-fossil is the family; nuclear is in it, but not in the renewable clan."*

### GROUP — Macroeconomic dashboard and the Economic Survey

### Flashcard T-191 — The Economic Survey: what it is, who prepares it and how it differs from the Budget
**Front:** What is the Economic Survey, who prepares it, and how does it differ from the Union Budget?
**Definition (learn):** The Economic Survey is the Government of India's annual review of the economy's performance and outlook, prepared by the Ministry of Finance (✅ Wikipedia: presented by the Department of Economic Affairs; the Chief Economic Adviser guides its preparation) and tabled before the Budget.
**Breakdown:**
- ✅ Prepared by the Ministry of Finance; publishes analysis, projections and sector diagnosis (owner 26).
- ✅ Tabled 'just before the Union Budget' (✅ Wikipedia, Economic Survey; e.g. 31 January 2020 and 29 January 2021). ⚠️ 'The day before' is not stated on the page.
- ✅ The Budget is the Annual Financial Statement (Article 112 of the Constitution) with estimates, taxes and appropriations; the Survey is analytical and advisory.
- ✅ Survey projections are not Budget estimates; advance estimates are not final actuals.
- ✅ Budget Estimate (BE), Revised Estimate (RE) and actuals (CGA) are distinct fiscal vintages.
**Cases / Committees / Schemes / Data:** ✅ Owner 26; Economic Survey 2025-26 is a January 2026 vintage.
**Trap:** Survey ≠ Budget. Survey forecasts are not binding. FY26 advance estimate is not final actual.
**Mains hook:** Argue that the Survey is a diagnostic and policy-signal document, not an appropriation; qualify with its projection status.
**Back:** *"The Survey diagnoses the year, the Budget disburses the money, and the Constitution counts the difference."*

### Flashcard T-192 — Macro dashboard: growth, inflation, fiscal, external and vintage control
**Front:** What must a macro dashboard show, and what data-vintage traps must be avoided?
**Definition (learn):** A macro dashboard reconciles growth, inflation, employment, fiscal, monetary, external and sectoral indicators, each with source, unit, reference period and vintage (advance, provisional, final).
**Breakdown:**
- ✅ Growth: real GDP and GVA; flow vs share measures; PFCE (private final consumption expenditure).
- ✅ Inflation: CPI (lagging) vs RBI surveys and expectations (forward-looking).
- ✅ Fiscal: BE, RE and CGA actuals; deficit quality.
- ✅ External: CAD (flow), forex reserves and external debt (stocks).
- ✅ Survey 2025-26 (January 2026 vintage, owner 26): FY26 first advance estimate real GDP growth 7.4%; real GVA 7.3%; PFCE 61.5% of GDP; services growth 9.1%; FY27 real GDP projection 6.8–7.2%; CPI 1.7% in April–December FY26; current account deficit 0.8% of GDP in H1 FY26; forex reserves US$701.4 billion as of 16 January 2026 (all as-of owner dates).
**Cases / Committees / Schemes / Data:** ✅ Owner 26 (📰 anchors). Use later releases for updated figures.
**Trap:** Calendar year ≠ fiscal year. Nominal level ≠ real growth. A dashboard is diagnostic, not causal. Do not mix Survey and Budget editions.
**Mains hook:** Argue that a dashboard must show vintage and decomposition; qualify with data revisions.
**Back:** *"Every number needs its vintage: advance, provisional or final, and the year it describes."*

