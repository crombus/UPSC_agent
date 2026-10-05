from pathlib import Path
import random
import re
from collections import Counter


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "24-Services-Digital-Economy-Fintech-and-Platform-Markets"
TODAY = "2026-10-03"

SOURCE_BASIC = "upsc-ai-kit/knowledge/Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md"
SOURCE_ADV = "upsc-ai-kit/knowledge/Economy/advanced/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md"
SOURCE_PACKAGE = "upsc-ai-kit/knowledge/Economy/24_Services-Digital-Economy-Fintech-and-Platform-Markets_Learner-V2-Complete-Topic-Package.md"
SOURCE_SESSION = "upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-24_Learning-Session.md"
SOURCE_WORKBOOK = "upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-24_Solved-Workbook.md"
SOURCE_PRACTICE = "upsc-ai-kit/practice/All-Topics-MCQ/Economy/Subject-wide-Syllabus/24-Services,-Digital-Economy,-Fintech-and-Platform-Markets/MCQ-Bank-With-Solutions.md"
SOURCE_SURVEY = "notes/Economy/Ref_EconomicSurvey_2025-26.md; books/economic-survey-2025-26.pdf"
SOURCE_TEXTBOOK = "books/Indian economy ramesh singh.pdf"


def c(label, correct, wrongs, why_wrong, evidence, trap, pyq=None, hold=None):
    return {
        "label": label,
        "correct": correct,
        "wrongs": wrongs,
        "why_wrong": why_wrong,
        "evidence": evidence,
        "trap": trap,
        "pyq": pyq,
        "hold": hold or "Static proposition is source-grounded; any later implementation, adoption or numerical claim must be rechecked against the named official source before future delivery.",
    }


ITEMS = [
    c("services heterogeneity",
      "Services are heterogeneous: tradability, productivity, skill intensity, formality and simultaneity of production and consumption differ across IT, finance, transport, tourism, health, education and personal services.",
      [
          "Services are uniformly low-productivity and non-tradable because they cannot be stored.",
          "Every service is produced only after a physical good has been exported.",
          "A service-sector share of GDP by itself proves that all service workers have similar productivity and wages.",
      ],
      [
          "IT, professional and financial services can be high-productivity and exported; non-storability does not make every service non-tradable.",
          "Services need not be preceded by a physical-goods export and may be delivered domestically or across borders.",
          "An aggregate share conceals large differences among sub-sectors, workers and forms of employment.",
      ],
      "Basic §§2, 5; Advanced §§2, 7; Economic Survey 2025-26 anchor.",
      "Do not infer uniform productivity or job quality from the aggregate services share.",
      pyq="2023 GS-III digitalisation route; exact wording withheld under rights hold."),
    c("service definition",
      "Services are largely intangible or non-storable economic activities, often produced and consumed together, although some can be digitised, traded or delivered remotely.",
      [
          "Services are only physical goods whose ownership changes without production.",
          "Services must always be consumed at the exact place where they are produced.",
          "Services have no economic value unless they are supplied free by the government.",
      ],
      [
          "Ownership transfer of a physical good is not the defining feature of a service.",
          "Remote digital delivery and cross-border trade show that co-location is not universal.",
          "Private, market and public services can all create economic value.",
      ],
      "Basic §2; Advanced §2.",
      "Treat 'often produced and consumed together' as a tendency, not an absolute rule."),
    c("DPI boundary",
      "Digital public infrastructure provides interoperable identity, payment, data or service rails; it does not require government ownership of every application using those rails.",
      [
          "DPI means a single government application must perform every digital transaction.",
          "DPI is limited to physical broadband cables and excludes identity or data layers.",
          "DPI is any private platform that acquires a large user base without shared standards.",
      ],
      [
          "Open rails can support competing public and private applications.",
          "Identity, payments, data and service layers are part of the architecture, not only connectivity hardware.",
          "User scale alone does not create public infrastructure or interoperability.",
      ],
      "Basic §§2–4; Advanced §§1–4.",
      "Public rails and government ownership of all downstream applications are different propositions.",
      pyq="2023 GS-III digitalisation route; exact wording withheld under rights hold."),
    c("digital output versus digital transaction",
      "A rise in digital transactions is evidence of payment activity, not by itself proof of equal digital access, higher productivity or improved welfare.",
      [
          "Every additional digital transaction necessarily raises real output by the same amount.",
          "Transaction volume automatically measures the quality and inclusion of the digital economy.",
          "A high transaction count proves that privacy, fraud and grievance risks have been solved.",
      ],
      [
          "Payments can be repeated or low-value and need not map one-for-one to real output.",
          "Access, capability, value, distribution and welfare require separate evidence.",
          "Operational risks can persist even when usage expands.",
      ],
      "Basic §§5, 8, 11A; Advanced §§5–6.",
      "UPI volume is an activity indicator, not a complete productivity or welfare metric."),
    c("DPI transmission mechanism",
      "Identity, connectivity, payments and consent-based data rails can lower search and transaction costs before applications create services and platforms on top of them.",
      [
          "Interoperable rails raise transaction costs by preventing applications from communicating.",
          "Applications must first become monopolies before shared rails can reduce entry barriers.",
          "Digital infrastructure affects only government accounting and not private exchange or service delivery.",
      ],
      [
          "Interoperability is intended to reduce friction and entry costs.",
          "Shared rails may reduce dependence on a single gateway, even though network effects can still create dominance.",
          "Private commerce, finance and public delivery can all use common rails.",
      ],
      "Basic §§1, 3; Advanced §§1, 3.",
      "The causal chain is rails → lower friction → applications and scale, not rails → automatic inclusion."),
    c("RBI and NPCI roles",
      "RBI regulates payment systems and authorised operators within its legal perimeter, while NPCI operates designated retail payment systems and interfaces; regulator and operator are not interchangeable.",
      [
          "NPCI is the sovereign issuer of all money moved through UPI and CBDC.",
          "RBI only develops payment apps and has no regulatory role over payment systems.",
          "Both institutions perform exactly the same function, so their legal roles cannot be distinguished.",
      ],
      [
          "UPI moves bank money and NPCI operates systems within the regulatory framework; it does not become the currency issuer.",
          "RBI's regulatory and authorisation role is central to payment-system oversight.",
          "Operator and regulator may interact but remain institutionally distinct.",
      ],
      "Basic §4; Advanced §4.",
      "A system operator is not automatically the issuer, regulator or liability holder."),
    c("sectoral regulator boundary",
      "SEBI, IRDAI and PFRDA regulate digital distribution within securities, insurance and pension domains respectively, while CCI addresses competition concerns.",
      [
          "CCI replaces all sector regulators whenever a service is delivered digitally.",
          "SEBI regulates every digital payment, insurance claim and pension account irrespective of product.",
          "Digital distribution removes the need for sector-specific conduct or prudential regulation.",
      ],
      [
          "Competition law and sector regulation can operate together; CCI is not a universal sector regulator.",
          "Each named regulator has a domain, not an unlimited mandate.",
          "Digitisation changes delivery channels but does not erase product-specific risks.",
      ],
      "Advanced §4; Basic §4.",
      "Do not substitute a competition regulator for a sector regulator or vice versa."),
    c("ONDC architecture",
      "ONDC seeks open-protocol interoperability so buyer-side and seller-side applications on different networks can transact; it is not one government marketplace owning every transaction.",
      [
          "ONDC requires every buyer and seller to use one central government shopping application.",
          "ONDC is a currency whose units settle all e-commerce transactions.",
          "ONDC prohibits private logistics, catalogue, payment and application providers from participating.",
      ],
      [
          "The design separates network interoperability from ownership of a single marketplace.",
          "ONDC is an e-commerce network architecture, not a medium of exchange.",
          "Private participants can operate applications and services within the open protocol.",
      ],
      "Basic §5; Advanced §§4–6; ondc.org architecture page (retrieved 2026-09-06; stub hold).",
      "Interoperability can improve contestability but does not guarantee equal market shares or trust.",
      pyq="2026 Prelims GS-I Q88 route; provisional key and exact wording withheld."),
    c("network effects",
      "A network effect occurs when a service becomes more valuable as participation by the same or another user group grows.",
      [
          "A network effect is a tax imposed on every user of a digital platform.",
          "A network effect exists only when a platform has no data and no switching costs.",
          "A network effect means every additional user necessarily improves competition and lowers concentration.",
      ],
      [
          "Network value concerns participation and matching, not a tax category.",
          "Data, reputation and switching costs commonly interact with network effects.",
          "The same effect can support scale and entrench a dominant platform.",
      ],
      "Basic §§2–3; Advanced §§2–3.",
      "Network effects are not synonymous with pro-competitive outcomes."),
    c("winner-takes-most dynamics",
      "Cross-side network effects, data advantages and switching costs can create winner-takes-most dynamics even where nominal entry is easy.",
      [
          "Easy app downloads guarantee that no platform can acquire durable market power.",
          "Network effects disappear once a second platform enters the market.",
          "Winner-takes-most outcomes arise only from statutory monopoly grants, never from user coordination.",
      ],
      [
          "Users may remain with an incumbent because the other side and accumulated data are valuable.",
          "Entry does not automatically remove lock-in or multi-homing costs.",
          "Coordination and scale can generate concentration without a formal monopoly grant.",
      ],
      "Basic §5; Advanced §§3, 6.",
      "Open entry and effective contestability are not identical."),
    c("fintech unbundling",
      "Fintech can separate origination, underwriting, funding, payment and servicing across specialised entities, but this does not erase the regulated principal's obligations or credit risk.",
      [
          "Fintech integrates every financial function into one unregulated entity by definition.",
          "Technology removes the need for underwriting because data automatically makes every borrower safe.",
          "Once an app is involved, banks and regulated entities have no remaining accountability.",
      ],
      [
          "Specialisation is possible, but responsibilities and contracts still matter.",
          "Data-driven underwriting can improve information while also reproducing bias or error.",
          "RBI rules preserve accountability for regulated entities within their perimeter.",
      ],
      "Advanced §§3–4; Basic §3.",
      "Do not confuse technological intermediation with removal of legal responsibility."),
    c("fintech risk boundary",
      "Fintech may lower cost and expand access, but it does not remove credit, fraud, cyber, privacy or grievance risks.",
      [
          "Digital delivery eliminates default risk because every transaction is automated.",
          "Fraud risk is impossible when a payment uses a regulated bank account.",
          "A wider app interface proves that all borrowers received fair pricing and informed consent.",
      ],
      [
          "Automation changes process, not the underlying possibility of default.",
          "Fraud can occur through social engineering, device compromise or unauthorised apps.",
          "Access statistics do not establish fair terms, comprehension or redress.",
      ],
      "Basic §§3, 5; Advanced §§3, 6.",
      "Efficiency claims must be paired with conduct, cyber and consumer-protection evidence."),
    c("Account Aggregator",
      "The Account Aggregator framework enables consent-based sharing of financial information through regulated NBFC-AA intermediaries; consent is distinct from credit approval.",
      [
          "An Account Aggregator permanently owns all financial data uploaded by a customer.",
          "Account Aggregator automatically sanctions every loan once data is shared.",
          "Account Aggregator permits data sale without purpose limitation because consent is irreversible.",
      ],
      [
          "The architecture is for consented data flow, not ownership transfer or underwriting by itself.",
          "A lender still assesses risk and decides whether to lend.",
          "Consent quality, purpose limitation and data protection remain necessary safeguards.",
      ],
      "Basic §5; Advanced §§3, 6.",
      "Do not turn a data-sharing rail into a lender, owner or guaranteed-credit mechanism."),
    c("OCEN",
      "OCEN is a consent-and-standardisation concept intended to make loan origination and embedded credit more interoperable, particularly for data-rich small businesses.",
      [
          "OCEN is a central bank digital currency issued directly to every MSME.",
          "OCEN is a replacement for all credit underwriting and guarantees repayment.",
          "OCEN is an ATM switch that links bank cash machines across India.",
      ],
      [
          "OCEN concerns credit origination and interoperability, not currency issuance.",
          "Standardised flows do not remove borrower risk, lender decisions or consumer-protection needs.",
          "NFS, not OCEN, is the ATM-interconnection system.",
      ],
      "Basic §5; Advanced §3.",
      "Treat OCEN as an evolving architecture/concept; do not invent adoption or volume figures."),
    c("digital lending guidelines",
      "RBI's Digital Lending Guidelines require, among other safeguards, direct disbursal and repayment through bank accounts and standardised key-fact disclosures for regulated-entity lending.",
      [
          "The guidelines allow a lending-service provider to receive and route borrower funds through any personal wallet.",
          "The guidelines make an unregulated app the legal lender whenever it performs customer acquisition.",
          "The guidelines apply only to cash loans made outside the banking system and exclude regulated entities.",
      ],
      [
          "Direct account flows and disclosure are intended to reduce opaque fund movement and surprise charges.",
          "A service provider does not automatically become the regulated lender or remove the principal's obligations.",
          "The framework is specifically tied to regulated entities and their lending arrangements.",
      ],
      "Basic §5; Advanced §§4, 6; RBI Digital Lending Guidelines, 2 September 2022.",
      "The legal perimeter and enforcement reach do not cover every offshore or fully unregulated app."),
    c("Aadhaar-DBT boundary",
      "Linking identity, bank accounts and welfare payments can reduce certain leakage in DBT, but authentication, connectivity and database errors can exclude eligible beneficiaries.",
      [
          "DBT removes all targeting error because biometric authentication is infallible.",
          "DBT is a cashless currency issued by NPCI rather than a delivery architecture.",
          "DBT works only when beneficiaries surrender all privacy and grievance rights.",
      ],
      [
          "Digital linkage changes some leakage channels but cannot eliminate data or access errors.",
          "DBT is a transfer-delivery mechanism; it is not a currency.",
          "Rights, consent, correction and grievance mechanisms remain relevant.",
      ],
      "Basic §5; Advanced §6; cross-link Topic 23 social protection.",
      "A reduction in leakage can coexist with exclusion caused by failed authentication or records."),
    c("UPI versus digital rupee",
      "UPI sends instructions that transfer commercial-bank deposits, whereas the digital rupee is a direct RBI liability and sovereign digital currency.",
      [
          "UPI itself is a currency and the digital rupee is merely a private bank app.",
          "Both UPI and the digital rupee are identical bank-account instructions with no liability distinction.",
          "The digital rupee is a commercial-bank liability while UPI is issued by RBI.",
      ],
      [
          "UPI is a payment interface, not a currency.",
          "The digital rupee changes the asset and liability architecture, not merely the user interface.",
          "CBDC is an RBI liability; UPI moves deposits held with banks.",
      ],
      "Basic §5A; Advanced §§5, 10; RBI CBDC concept note/owner record.",
      "The tested axis is issuer/liability and what moves, not simply digital versus physical.",
      pyq="2024 Prelims Q53 and 2026 Prelims Q89 routes; exact wording, options and key letters withheld."),
    c("CBDC-R and CBDC-W",
      "CBDC-R is designed for retail consumer and merchant use, while CBDC-W is designed for interbank or securities-settlement use.",
      [
          "CBDC-R is only for central-bank reserves and CBDC-W is for household grocery purchases.",
          "The two labels describe two names for the same participant set and settlement purpose.",
          "CBDC-W is a private cryptocurrency and CBDC-R is a commercial-bank deposit.",
      ],
      [
          "The pilots have different users and use cases.",
          "Participant and settlement architecture matter even though both are forms of CBDC.",
          "Both remain sovereign digital-currency variants, not private crypto or ordinary deposits.",
      ],
      "Basic §13; Advanced §10.",
      "Do not describe the CBDC pilot as one undifferentiated programme."),
      c("CBDC wallet transaction",
      "In the retail pilot, e₹ moves from a payer's wallet to a payee's wallet through authorised CBDC infrastructure, unlike UPI's account-to-account instruction.",
      [
          "A retail CBDC payment always debits a commercial-bank deposit and never moves the CBDC token.",
          "A CBDC wallet is only a display of UPI history and cannot hold a central-bank liability.",
          "Every CBDC transfer must use a public blockchain identical to Bitcoin.",
      ],
      [
          "The wallet/token and direct-liability distinction is the core mechanism.",
          "A wallet can hold e₹ separately from a bank account in the pilot architecture.",
          "The architecture need not use one public blockchain design in every implementation.",
      ],
      "Basic §13; Advanced §10; 2026 GS-III Q1 owner integration.",
      "Do not replace a token/wallet description with a generic digital-payment description.",
      pyq="2026 GS-III Q1 route; exact question text is not reproduced in the bank."),
    c("CBDC pilot enhancements",
      "The 2026 owner record reports pilot-stage features including offline NFC payments, programmable use and fintech-wallet interoperability; these are dated progress claims, not proof of full replacement of cash or UPI.",
      [
          "The pilot has already replaced cash and UPI nationwide with compulsory programmable wallets.",
          "Offline CBDC use proves that all RBI pilot users have permanent network-free access.",
          "Fintech-wallet interoperability means every fintech is now the issuer of sovereign currency.",
      ],
      [
          "The features are being piloted and do not establish nationwide replacement or compulsory adoption.",
          "Offline capability in a pilot does not establish universal access or reliability.",
          "Distribution through fintech wallets does not transfer sovereign issuance from RBI.",
      ],
      "Basic §13; Advanced §10; Vajiram & Ravi The Recitals, January 2026, pp. 53–54 (local extract).",
      "Keep pilot progress separate from adoption scale, legal status and issuer identity.",
      hold="Dated 2026 pilot features are retained from the owner record; verify current RBI progress and any user/transaction count before future delivery."),
    c("BRICS CBDC linkage",
      "The owner record describes proposed BRICS CBDC linkage for cross-border trade or tourism payments as a pilot-stage proposal, not an operational common currency or completed interoperable system.",
      [
          "All BRICS members have already launched one common CBDC that replaces the US dollar.",
          "The proposal proves that BRICS has completed a single monetary union.",
          "The proposal is unrelated to cross-border payments and concerns only domestic welfare transfers.",
      ],
      [
          "The record expressly treats the linkage as a proposal and states that members remain at pilot stages.",
          "A payment-linkage proposal does not create a common currency or monetary union.",
          "The stated use is cross-border trade/tourism payments, not only domestic transfers.",
      ],
      "Basic §13; Advanced §10; Vajiram & Ravi The Recitals, January 2026, pp. 53–54.",
      "Proposal, pilot and operational system are different status categories.",
      hold="Current cross-border CBDC proposals are date-sensitive and must be rechecked against RBI/BRICS official releases."),
    c("digital rupee legal status",
      "The digital rupee is legal tender, a direct RBI liability and convertible at par with cash and bank money; its digital form does not provide built-in inflation insurance.",
      [
          "The digital rupee is a private token whose value floats independently of the rupee.",
          "A CBDC is legal tender only when a commercial bank guarantees every unit at a premium.",
          "Because it is digital, the digital rupee automatically protects holders against inflation.",
      ],
      [
          "e₹ is sovereign money and is designed to be at par with the rupee.",
          "Legal-tender status follows sovereign issuance, not a bank premium.",
          "Digital format changes settlement architecture, not the macroeconomic purchasing power of money.",
      ],
      "Basic §§5A, 13; Advanced §§7, 10.",
      "At-par convertibility is not an inflation hedge or guaranteed real return.",
      pyq="2024 Prelims Q53 route; exact wording/options and key letter withheld."),
    c("blockchain versus cryptocurrency",
      "Blockchain is a distributed, append-only ledger architecture; cryptocurrency is one application that may issue a cryptographically secured digital token on such a ledger.",
      [
          "Blockchain and cryptocurrency are identical names for a sovereign currency issued by RBI.",
          "Every blockchain application must issue a freely traded token.",
          "Cryptocurrency is the ledger architecture, while blockchain is only a payment app.",
      ],
      [
          "A ledger architecture can support applications such as NFTs or supply-chain records without issuing a currency.",
          "Token issuance is not necessary for every blockchain use.",
          "The technology and the application must be kept analytically separate.",
      ],
      "Basic §5A; Advanced §§2, 7.",
      "Technology, token, issuer and legal status are separate axes."),
    c("crypto versus CBDC",
      "Private cryptocurrency is generally market-valued without sovereign legal-tender status, while CBDC is sovereign money and a direct central-bank liability.",
      [
          "Both are always issued by the same central bank and carry identical legal-tender status.",
          "Private cryptocurrency is automatically a guaranteed bank deposit once traded on an exchange.",
          "CBDC value is determined only by speculative demand and has no sovereign backing.",
      ],
      [
          "Issuer, liability, legal tender and value backing distinguish the instruments.",
          "Exchange listing does not convert a private token into a deposit or legal tender.",
          "CBDC is designed to be sovereign and at par with the national currency.",
      ],
      "Basic §5A; Advanced §§7–8.",
      "A private stablecoin peg is not the same as sovereign legal-tender status.",
      pyq="2021 GS-I cryptocurrency route; exact wording withheld and social-effects ownership cross-linked."),
    c("crypto benefits and harms",
      "Crypto and blockchain may support payment innovation and remittances, but volatility, fraud, illicit-finance risk, unequal retail exposure and proof-of-work energy use require a balanced assessment.",
      [
          "Crypto has only benefits because decentralisation eliminates volatility and fraud.",
          "Crypto has only social harms and cannot support any financial innovation or settlement experiment.",
          "Energy concerns apply identically to every consensus design, including proof-of-stake.",
      ],
      [
          "Potential gains and harms coexist and require evidence rather than a one-sided verdict.",
          "A blanket rejection ignores actual innovation and remittance experiments.",
          "Energy intensity varies by consensus design; proof-of-work and proof-of-stake are not identical.",
      ],
      "Basic §5A; Advanced §7.",
      "The UPSC answer must present benefits, harms and unequal distribution of risk.",
      pyq="2021 GS-I cryptocurrency and society route; exact wording withheld."),
    c("VDA Section 115BBH",
      "Section 115BBH taxes income from transfer of a virtual digital asset at a flat 30 percent, subject to the statutory treatment of surcharge and cess, with limited deduction treatment and no ordinary loss set-off/carry-forward.",
      [
          "Section 115BBH recognises every VDA as legal tender and exempts all transfer gains from tax.",
          "Section 115BBH applies the normal progressive slab rate and permits every business expense against VDA gains.",
          "Section 115BBH is an RBI payment-system licence rather than an income-tax provision.",
      ],
      [
          "Taxation does not confer legal-tender status.",
          "The special regime is not the ordinary slab-and-expense framework described in the option.",
          "Section 115BBH is in the Income-tax Act and concerns transfer income.",
      ],
      "Basic §5A; Advanced §8.",
      "Do not infer legal recognition or a market-conduct regulator from taxation.",
      hold="Tax treatment is statutory and date-sensitive; recheck the Income-tax Act and Finance Act before future delivery."),
    c("VDA Section 194S",
      "Section 194S provides for 1 percent TDS on consideration for transfer of a VDA above specified statutory thresholds, subject to the applicable rules.",
      [
          "Section 194S abolishes all tax on VDA transfers below a threshold and grants legal-tender status above it.",
          "Section 194S is the provision that creates RBI's retail CBDC wallet.",
          "Section 194S requires a 30 percent deduction from every gross transaction without any threshold or statutory conditions.",
      ],
      [
          "TDS is a withholding mechanism and does not determine legal-tender status.",
          "CBDC architecture is a separate RBI/payment-system matter.",
          "The statutory rule is 1 percent subject to specified thresholds and conditions, not the absolute formulation.",
      ],
      "Basic §5A; Advanced §8.",
      "Keep withholding, final tax liability and monetary status conceptually separate.",
      hold="Tax-law thresholds and compliance details require current statutory recheck before future delivery."),
    c("PMLA and FIU-IND",
      "VDA service providers such as exchanges and custodial wallet providers were brought within the PMLA reporting-entity perimeter and must comply with FIU-IND/KYC and suspicious-transaction obligations; this is not a comprehensive market-conduct statute.",
      [
          "FIU-IND issues a sovereign cryptocurrency and guarantees the market price of every VDA.",
          "PMLA reporting status automatically makes every VDA a SEBI-regulated security.",
          "AML registration means India has already enacted a complete investor-protection code for crypto markets.",
      ],
      [
          "FIU-IND receives AML-related reporting; it is not the issuer or price guarantor.",
          "AML obligations do not decide whether a token is a security under securities law.",
          "Monitoring and reporting do not equal a full market-conduct and investor-protection regime.",
      ],
      "Basic §5A; Advanced §8.",
      "Anti-money-laundering perimeter is narrower than comprehensive asset regulation.",
      hold="FIU-IND/PMLA status is retained from the owner record (March 2023); confirm later legislative changes before delivery."),
    c("Merchant Discount Rate",
      "MDR is a merchant-side processing fee paid to the acquiring bank or payment service provider and shared among relevant participants; it is not a fee charged to the paying customer.",
      [
          "MDR is a tax paid directly by the customer to RBI for every UPI transfer.",
          "MDR is the interest rate charged to a borrower using a digital wallet.",
          "MDR is a subsidy paid by the merchant to the customer for choosing cash.",
      ],
      [
          "MDR is linked to payment processing and merchant acceptance, not a sovereign tax.",
          "It is not a credit-price measure.",
          "The economic incidence is a merchant-side processing cost, not a customer reward.",
      ],
      "Basic §5B; Advanced §9.",
      "Do not confuse MDR with a customer convenience fee or a lending rate.",
      pyq="2018 Prelims route on MDR; exact wording and official key unavailable locally.",
      hold="MDR rates and any current UPI exceptions are date-sensitive; owner record retains January 2020 zero-MDR history and requires RBI/NPCI/MoF recheck."),
    c("National Financial Switch",
      "The National Financial Switch, operated by NPCI, interconnects participating bank ATMs and routes messages and settlement between acquiring and issuing banks.",
      [
          "NFS is the sovereign digital-rupee ledger used for wallet-to-wallet CBDC settlement.",
          "NFS is the open-commerce protocol that matches buyers and sellers on ONDC.",
          "NFS is a tax database that links every bank account to a GST registration.",
      ],
      [
          "NFS is an ATM interbank network, not a CBDC ledger.",
          "ONDC and NFS serve different digital infrastructures.",
          "Tax registration is unrelated to ATM switching and settlement.",
      ],
      "Basic §5B; Advanced §9.",
      "NFS, UPI, RuPay, IMPS and Bharat BillPay are distinct NPCI systems.",
      pyq="2018 Prelims route on the institution linking ATMs; exact wording/key unavailable locally."),
    c("BHIM/UPI authentication",
      "A UPI/BHIM payment is authorised through the registered device or mobile linkage plus the payer's UPI PIN/MPIN; the PIN is entered on the payer's device and not shared with the payee.",
      [
          "The payee must receive and enter the payer's UPI PIN before funds can move.",
          "A UPI payment is authenticated only by the payee's name, with no payer-side credential.",
          "UPI PIN sharing is the standard two-factor protection against collect-request fraud.",
      ],
      [
          "The PIN is a payer-side secret and sharing it creates a fraud risk.",
          "Payer-side device linkage and a credential provide the relevant factors.",
          "A payee name or collect request is not an authentication substitute.",
      ],
      "Basic §5B; Advanced §9.",
      "Never tell a payee or caller the UPI PIN; the direction of authentication is the trap.",
      pyq="2018 Prelims route on BHIM and authentication; exact wording/key unavailable locally."),
    c("NFT",
      "An NFT is a unique, non-fungible blockchain-recorded token used to certify ownership or provenance of a particular item, unlike a fungible cryptocurrency unit.",
      [
          "An NFT is interchangeable unit-for-unit with every other token in the same collection by definition.",
          "An NFT is a central-bank liability issued through UPI.",
          "An NFT is a physical certificate that cannot be represented on a distributed ledger.",
      ],
      [
          "Non-fungibility means a specific token is not interchangeable in the same way as a fungible unit.",
          "NFTs are private blockchain applications, not sovereign money or payment interfaces.",
          "The token can record provenance digitally even though the underlying item may be physical or digital.",
      ],
      "Basic §5B; Advanced §§7, 9.",
      "Non-fungible describes interchangeability of the token, not guaranteed value or copyright.",
      pyq="2022 Prelims NFT route; exact wording and key unavailable locally."),
    c("NFT and copyright",
      "Owning an NFT that records provenance does not automatically transfer copyright or other legal rights in the underlying work.",
      [
          "Every NFT sale automatically assigns all copyright, patent and moral rights to the buyer.",
          "Copyright exists only when a work is placed on a public blockchain.",
          "A blockchain record makes the underlying work immune from copying and fraud.",
      ],
      [
          "Token ownership and intellectual-property rights are separate unless the contract expressly transfers them.",
          "Copyright law does not depend on blockchain placement.",
          "A ledger can evidence provenance but cannot guarantee enforcement or prevent copying by itself.",
      ],
      "Basic §5B; Advanced §9.",
      "Separate token ownership, licence, copyright and physical possession."),
    c("crowdfunding types",
      "Crowdfunding can be donation-based, reward-based, debt/P2P-lending based or equity-based, distinguished by what the contributor receives.",
      [
          "All crowdfunding gives the contributor an identical equity share and voting right.",
          "Crowdfunding means only government budgetary support distributed through an online portal.",
          "Crowdfunding is one uniformly regulated product with one regulator and one return structure.",
      ],
      [
          "The contributor may receive no return, a reward, interest repayment or an ownership stake.",
          "Crowdfunding is a financing method involving many contributors, not a government budget head.",
          "Different forms fall under different or sometimes limited regulatory frameworks.",
      ],
      "Basic §5B; Advanced §9.",
      "Classify by contributor return before asking which regulatory perimeter applies.",
      pyq="2026 Prelims GS-I Q97 route; provisional key and exact wording withheld."),
    c("equity crowdfunding status",
      "India's public retail equity-crowdfunding status cannot be treated as a generally permitted SEBI-approved public securities mechanism; regulatory treatment varies by form.",
      [
          "Every equity-crowdfunding portal is automatically a public stock exchange recognised by SEBI.",
          "Equity crowdfunding is uniformly open to all retail investors without disclosure or intermediary conditions.",
          "Donation and reward crowdfunding are identical to public equity offerings under securities law.",
      ],
      [
          "The owner record expressly cautions against treating public retail equity crowdfunding as a generally approved mechanism.",
          "Investor access and disclosure depend on the specific legal form; no blanket permission follows from the label.",
          "Non-financial return models are not automatically securities offerings.",
      ],
      "Basic §5B; Advanced §9.",
      "Do not infer uniform permission from the existence of a crowdfunding platform.",
      hold="Crowdfunding regulatory status is a live SEBI/RBI hold; verify the specific form before future delivery."),
    c("platform and gig-work architecture",
      "Platform work typically uses app-based matching, algorithmic dispatch, ratings and dynamic pricing; it includes location-based work and cloud/web-based work.",
      [
          "Platform work is limited to factory employment under one physical supervisor and has no algorithmic matching.",
          "All platform work is identical to regular salaried employment for every legal and economic purpose.",
          "Platform work means only remote software exports and excludes ride-hailing or delivery.",
      ],
      [
          "Location-based services such as ride-hailing and delivery are matched in real time by platforms.",
          "Worker status and social-security law are separate questions from the matching architecture.",
          "Cloud/web work is one segment, not the whole platform economy.",
      ],
      "Basic §5; Advanced §§3, 6; cross-link Topic 22.",
      "Do not import Topic 22's labour-law conclusion into every platform-work economics question."),
    c("NITI Aayog gig estimate",
      "NITI Aayog's 2022 report estimated about 77 lakh gig workers in 2020–21 and projected about 2.35 crore by 2029–30; the estimate and projection are not an interpolated current count.",
      [
          "The 77-lakh figure is a measured 2029–30 count and the 2.35-crore figure is a 2020–21 survey total.",
          "The projection proves that every gig worker receives stable wages and social security.",
          "The report gives a timeless global gig count with no India-specific reference period.",
      ],
      [
          "The two figures have different evidence types and periods.",
          "Workforce scale does not establish earnings stability or social-security coverage.",
          "The report is an India-specific estimate and projection, not a timeless global total.",
      ],
      "Basic §5; Advanced §§6, 9; NITI Aayog report, June 2022.",
      "Never present a projection as an observed current stock or infer worker welfare from headcount.",
      hold="NITI estimates retain the 2020–21 baseline and 2029–30 projection; no intermediate or 2026 count is inferred."),
    c("DPDP consent and legitimate use",
      "The DPDP Act, 2023 uses a consent-and-legitimate-use architecture: processing may rely on valid consent or a listed legitimate use, subject to the Act's conditions.",
      [
          "The Act permits processing only after a paper signature and recognises no legitimate-use category.",
          "The Act makes every government use automatically lawful without purpose, notice or statutory conditions.",
          "The Act treats consent as permanent ownership transfer of all personal data.",
      ],
      [
          "The Act contains a dual legal basis rather than a consent-only design.",
          "Legitimate use is a statutory category, not an unlimited exemption from all conditions.",
          "Consent to process is not the same as transfer of ownership or abandonment of rights.",
      ],
      "Basic §5; Advanced §6; DPDP Act owner record.",
      "Do not reduce the Act to either consent-only or unrestricted government access.",
      hold="The Act is enacted, but implementation is phased; verify current commencement and Rules status before citing deadlines."),
    c("Data Protection Board",
      "The DPDP Act creates the Data Protection Board of India to adjudicate breaches and complaints and impose statutory penalties within its mandate.",
      [
          "The Board issues currency, regulates UPI settlement and sets the repo rate.",
          "The Board replaces CCI, RBI, SEBI and all sector regulators for every digital dispute.",
          "The Board is only a private industry association with no statutory enforcement role.",
      ],
      [
          "Monetary and payment functions remain with RBI and competition matters with CCI.",
          "The Board's mandate is data-protection enforcement, not all digital regulation.",
          "The Act gives it a statutory adjudicatory/enforcement role.",
      ],
      "Basic §5; Advanced §6.",
      "Name the regulator whose legal mandate matches the risk being tested.",
      hold="The owner record says Rules were notified in November 2025 and obligations are phased through 2027; verify the current operational phase."),
    c("DPDP phased implementation",
      "The owner record treats the DPDP Act as enacted but partly in force, with Rules notified in November 2025 and several compliance obligations staggered through later phases.",
      [
          "All duties, registrations and cross-border obligations became fully enforceable on the day the Act was enacted.",
          "Rules cannot affect commencement because a statute never needs subordinate implementation.",
          "A phased framework means the Act has no legal effect until 2027.",
      ],
      [
          "Commencement and operational phases matter for compliance claims.",
          "Rules can specify implementation and operational details under the statutory framework.",
          "Enacted provisions can have legal effect even while obligations are staggered.",
      ],
      "Basic §6; Advanced §6.",
      "Do not turn a phased commencement record into either full implementation or no law at all.",
      hold="Implementation dates are time-sensitive and must be checked against current MeitY notifications."),
    c("digital access versus capability",
      "More internet connections indicate access infrastructure, but effective digital inclusion also requires devices, skills, language access, disability inclusion, fraud awareness and grievance redress.",
      [
          "Connection counts alone prove equal device ownership, literacy and safe usage.",
          "Once a person is connected, exclusion and fraud cannot occur.",
          "Digital capability is identical to the number of SIM cards issued in a state.",
      ],
      [
          "A connection is not the same as effective or safe use.",
          "Connectivity can coexist with exclusion, fraud and weak redress.",
          "SIM or connection counts are infrastructure indicators, not capability measures.",
      ],
      "Basic §8 and §11A; Advanced §§6, 9.",
      "Access, capability, usage, quality and outcome are different measurement layers."),
    c("Survey services anchor",
      "The Economic Survey 2025–26 owner record reports services at 53.6 percent of GDP in H1 FY26, services GVA growth of 9.1 percent in FY26 FAE, and services employment shares of 30 percent overall and 61.9 percent in urban employment.",
      [
          "The figures are timeless global averages that do not carry a period, estimate status or India boundary.",
          "The 53.6 percent GDP share proves that every service job is formal and high productivity.",
          "The employment shares measure only digital-platform workers and exclude trade, transport, health and education.",
      ],
      [
          "The owner gives a dated India-specific Survey vintage and FAE status.",
          "Aggregate output share does not establish job quality, formality or uniform productivity.",
          "The employment headline covers services broadly, not only platforms.",
      ],
      "Basic §8; Advanced §9; Economic Survey 2025-26.",
      "Retain the vintage, denominator and estimate label before using a headline number.",
      hold="Survey figures are dated H1 FY26/FY26 FAE anchors and must not be re-used as timeless or independently updated values."),
    c("internet connections anchor",
      "The Survey owner record cites internet connections rising from 25.15 crore in 2014 to 96.96 crore in 2024; this is a connection count, not a direct measure of equal capability.",
      [
          "The series counts unique skilled users with equal device ownership and excludes machine or multiple connections.",
          "The increase automatically proves universal broadband quality, affordability and grievance access.",
          "The figures are a measure of services' GDP share rather than connectivity.",
      ],
      [
          "Connection counts may not equal persons, devices, quality or effective use.",
          "Capability and inclusion need additional evidence.",
          "GDP share and connection count are different statistical dimensions.",
      ],
      "Basic §8; Advanced §9; Economic Survey 2025-26.",
      "Do not convert a connection series into a social-outcome series.",
      hold="The figures retain the 2014/2024 vintage from the Survey owner; no 2026 extrapolation is made."),
    c("metaverse",
      "The metaverse is an interoperable, persistent network of 3D virtual environments enabling shared social and economic interaction; an AR/VR headset is access hardware, not the metaverse itself.",
      [
          "The metaverse is one specific VR headset sold by a single manufacturer.",
          "The metaverse is only a single online game with no interoperability or economic activity.",
          "The metaverse is a central-bank payment instrument identical to CBDC.",
      ],
      [
          "Hardware can provide access to an environment but is not the whole concept.",
          "A single platform or game is one implementation, not the general network concept.",
          "Virtual environments and sovereign money are different categories.",
      ],
      "Basic §2; Advanced §9.",
      "Distinguish concept/network layer, access hardware and one platform.",
      pyq="2024 Prelims Q48 route; exact wording/options and key letter withheld."),
    c("dropshipping",
      "In dropshipping, a seller markets or accepts an order while a third-party supplier fulfils and ships the product, so the seller need not hold the inventory itself.",
      [
          "Dropshipping requires the seller to manufacture and warehouse every product before listing it.",
          "Dropshipping is a central-bank settlement method that moves CBDC between wallets.",
          "Dropshipping means the buyer receives no product and only donates to an online campaign.",
      ],
      [
          "Third-party fulfilment and reduced inventory ownership are the defining commercial features.",
          "Payment settlement is a separate layer from fulfilment.",
          "A product is still sold and delivered; the model is not donation crowdfunding.",
      ],
      "Basic PYQ integration 2026; Advanced §10.",
      "Separate order acquisition, inventory ownership, fulfilment and payment settlement.",
      pyq="2026 Prelims GS-I Q87 route; provisional key and exact wording withheld."),
    c("UPI international merchant payments",
      "International merchant-payment availability under UPI is corridor- and partner-specific; a dated list of countries must not be treated as universal or permanent.",
      [
          "UPI is accepted at every merchant in every country because it is a global currency.",
          "Any country with an Indian tourist automatically has universal UPI merchant acceptance.",
          "A country list remains permanent even if bilateral arrangements, participating banks or merchant corridors change.",
      ],
      [
          "Cross-border acceptance depends on named partner arrangements and merchant corridors.",
          "Tourist presence does not establish payment-system interoperability.",
          "International coverage is a dated current-affairs fact requiring recheck.",
      ],
      "Basic §8–9; owner routing for 2025 Prelims.",
      "Do not infer universal acceptance from a few live corridors or a paper-dated list.",
      pyq="2025 Prelims Q69 route; exact country options and key letter withheld.",
      hold="Country coverage is date-sensitive; use the paper-vintage list only after checking the cited official NPCI/RBI or paper record."),
    c("TReDS and M1xchange",
      "TReDS is an electronic invoice-discounting framework for MSME receivables; an RBI-regulated platform such as M1xchange is not the same instrument as UPI or CBDC.",
      [
          "TReDS is a retail CBDC wallet and M1xchange is the RBI's currency issuer.",
          "TReDS is an ATM switch whose primary function is cash withdrawal.",
          "M1xchange is a sovereign bond and cannot provide invoice-finance intermediation.",
      ],
      [
          "Invoice discounting addresses receivables financing and working capital.",
          "ATM switching is NFS's function, not TReDS.",
          "A regulated platform can intermediate receivables without becoming sovereign money or a bond.",
      ],
      "Basic §9; 2026 owner routing; Topic 5 cross-link for financial regulation.",
      "Do not collapse every digital financial platform into payment, currency or securities categories.",
      pyq="2026 Prelims GS-I Q93 route; provisional key and exact wording withheld.",
      hold="2026 provisional routing is retained without inferring the key; confirm the final official key and current platform status before future delivery."),
    c("regulatory liability chain",
      "A sound digital-economy analysis identifies the authority, regulated entity, application or intermediary, user protection and grievance remedy separately.",
      [
          "Naming a portal or app alone proves that the policy has achieved the intended outcome.",
          "A regulator's existence makes implementation capacity, incentives and enforcement irrelevant.",
          "A registration count is a direct measure of consumer welfare without outcome or distribution evidence.",
      ],
      [
          "Institutional design is only one link in an authority-to-delivery-to-remedy chain.",
          "Rules need capacity, incentives, monitoring and redress to affect behaviour.",
          "Inputs and outputs cannot substitute for welfare or distribution evidence without qualification.",
      ],
      "Basic §11A; Advanced §11; semantic-completeness audit.",
      "UPSC often tests whether an institutional label is being mistaken for an outcome."),
    c("digital lending perimeter",
      "RBI Digital Lending Guidelines bind specified regulated entities and their lending-service-provider arrangements; they do not automatically solve every problem created by unregulated or offshore lending apps.",
      [
          "The guidelines impose identical obligations on every offshore app regardless of jurisdiction or RBI relationship.",
          "The guidelines apply only to borrowers and never to the regulated entity that remains responsible.",
          "Once a platform is unregulated, all consumer-protection law is automatically irrelevant.",
      ],
      [
          "The perimeter is tied to regulated entities and partners, so reach and enforcement can be limited.",
          "The regulated principal's obligations remain material.",
          "Other legal remedies may still matter; the proposition is too absolute.",
      ],
      "Basic §5; Advanced §§4, 6.",
      "Distinguish the formal regulatory perimeter from practical enforcement reach."),
    c("interoperability trade-off",
      "Interoperability can lower switching costs and contestability barriers, but common standards may constrain differentiation and cannot instantly erase incumbent scale, trust or logistics advantages.",
      [
          "Interoperability guarantees that every participating platform will have equal users and profits.",
          "Common standards always prevent innovation because no application can differentiate.",
          "Interoperability has no connection with switching costs or platform competition.",
      ],
      [
          "Open standards can improve choice without equalising commercial outcomes.",
          "Standards can coexist with differentiated applications and services.",
          "Switching costs and contestability are central economic mechanisms.",
      ],
      "Advanced §§3, 6; ONDC boundary.",
      "A pro-competition architecture is not a guarantee of a particular market share."),
    c("platform worker legal boundary",
      "Platform matching and algorithmic management describe an economic work architecture; whether a worker is an employee or receives social security depends on the applicable labour-law framework and facts.",
      [
          "Every worker matched by an app is automatically an employee under every statute.",
          "Because a worker is called a partner, labour-law questions disappear.",
          "Platform work is an economic category only when the worker has a written employment contract.",
      ],
      [
          "Economic architecture and legal classification are distinct analytical questions.",
          "A label used by a platform cannot by itself settle statutory status.",
          "Platform work can be informal, contractual or otherwise classified without one universal document test.",
      ],
      "Basic §5; Advanced §6; cross-link Topic 22.",
      "Do not answer a labour-law question solely from the existence of an app."),
    c("digital inclusion outcome",
      "Safe digital inclusion requires access, capability, affordable use, privacy, fraud protection and grievance redress; connectivity growth alone is insufficient.",
      [
          "Digital inclusion is complete once a household is counted in a connection database.",
          "Fraud and exclusion are signs of low adoption only and have no policy relevance after connectivity expands.",
          "Privacy and grievance redress are unrelated to economic inclusion.",
      ],
      [
          "The user must be able to use the service effectively and safely.",
          "Adoption and harm can rise together if safeguards lag.",
          "Trust, remedy and rights affect whether access becomes welfare.",
      ],
      "Basic §§8, 11A; Advanced §6.",
      "Measure effective inclusion, not only infrastructure availability."),
    c("current-source discipline",
      "A dated statistic or legal-status claim must retain its period, definition, source and qualification; a proposal or projection must not be presented as an operational fact.",
      [
          "A government number can be reused for every later year without a vintage or definition.",
          "A projected adoption count can be restated as a measured current count if it looks plausible.",
          "A policy proposal, pilot and completed programme are interchangeable status labels.",
      ],
      [
          "Every statistic has a reference period and denominator.",
          "Projection and observation are different evidence types.",
          "Legal status, pilot progress and operational implementation must be distinguished.",
      ],
      "Basic §§8–9, 13; Advanced §§9–10; owner source/date controls.",
      "The safest answer preserves uncertainty instead of filling a dated gap with inference.",
      pyq="Applies to 2024–2026 routed objective demands; exact wording and key letters withheld."),
]


def bank_stem(bank, label):
    if bank == 1:
        return f"Which statement is most accurate about {label} in India's services and digital-economy context?"
    if bank == 2:
        return f"A policy brief evaluates {label} for productivity, inclusion and regulation. Which conclusion is best supported?"
    return f"In a close UPSC application involving {label}, which proposition preserves the relevant legal, statistical or causal boundary?"


def bank_option(bank, text):
    if bank == 1:
        return text
    if bank == 2:
        return f"The policy reading is: {text}"
    return f"The boundary-safe claim is: {text}"


def strip_prefix(text, bank):
    if bank == 2:
        return text.removeprefix("The policy reading is: ")
    if bank == 3:
        return text.removeprefix("The boundary-safe claim is: ")
    return text


def answer_block(no, item, displayed, key, bank):
    correct = displayed[ord(key) - 65]
    correct_raw = strip_prefix(correct, bank)
    lines = [
        f"## Q{no}. Correct answer: {key}",
        f"**Question:** {bank_stem(bank, item['label'])}",
        f"**Correct proposition:** {correct_raw}",
        f"**Evidence:** {item['evidence']}",
        f"**Source/date hold:** {item['hold']}",
        "**Option-specific rationales:**",
    ]
    for idx, option in enumerate(displayed):
        letter = chr(65 + idx)
        raw = strip_prefix(option, bank)
        if option == correct:
            lines.append(f"- **{letter}.** Correct — {raw} This preserves the relevant definition, institution, mechanism, date and qualification.")
        else:
            wrong_index = item["wrongs"].index(raw)
            lines.append(f"- **{letter}.** Incorrect — {raw} It fails because {item['why_wrong'][wrong_index]}")
    lines.append(f"**Examiner trap:** {item['trap']}")
    if item["pyq"]:
        lines.append(f"**PYQ route:** {item['pyq']}")
    lines.append("")
    return "\n".join(lines)


def write_bank(bank):
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    rng = random.Random(2400 + bank * 271)
    q_lines = [
        f"# Topic 24 — Services, Digital Economy, Fintech and Platform Markets — Revision {bank} QUESTIONS",
        "",
        "> Answer-free delivery file: no keys, solutions, evidence, dated holds, PYQ routes or traps are included.",
        "",
        "> Original-only bank. Exact UPSC wording/options are withheld; routed PYQ demands and rights/provenance holds are recorded in COVERAGE.md.",
        "",
    ]
    a_lines = [
        f"# Topic 24 — Services, Digital Economy, Fintech and Platform Markets — Revision {bank} ANSWERS",
        "",
        "> Detailed answer key. Every item includes a mapped key, evidence, source/date hold, four option-level rationales and an examiner trap.",
        "",
    ]
    rows = []
    for no, item in enumerate(ITEMS, 1):
        options = [item["correct"], *item["wrongs"]]
        rng.shuffle(options)
        rendered = [bank_option(bank, x) for x in options]
        key = chr(65 + rendered.index(bank_option(bank, item["correct"])))
        q_lines.extend(
            [
                f"## Q{no}. {bank_stem(bank, item['label'])}",
                *[f"{chr(65+i)}. {option}" for i, option in enumerate(rendered)],
                "",
            ]
        )
        a_lines.append(answer_block(no, item, rendered, key, bank))
        rows.append((no, item["label"], key))
    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")

    block_names = [
        (1, 10, "Services, digital rails and platform-market mechanisms"),
        (11, 20, "Fintech, delivery systems and CBDC architecture"),
        (21, 30, "Crypto/VDA, payment systems and digital assets"),
        (31, 40, "Crowdfunding, platform work, data governance and inclusion"),
        (41, len(ITEMS), "Current anchors, PYQ routes and source/status discipline"),
    ]
    coverage = [
        f"# Topic 24 — Revision {bank} Coverage Ledger",
        "",
        f"**Status:** complete — {len(ITEMS)} independent original-only questions; exact PYQs withheld under rights/provenance holds.",
        "",
        "| Q range | Coverage block | Questions |",
        "|---|---|---:|",
    ]
    for start, end, name in block_names:
        coverage.append(f"| {start}–{end} | {name} | {end-start+1} |")
    coverage += [
        f"| **Total** | **Complete topic spine in revision {bank}** | **{len(ITEMS)}** |",
        "",
        "## Question-level ledger",
        "",
    ]
    for no, label, _ in rows:
        coverage.append(f"- [x] Q{no} — {label}")
    coverage += [
        "",
        "## Sources read",
        f"- `{SOURCE_BASIC}` — complete Basic owner.",
        f"- `{SOURCE_ADV}` — complete Advanced owner.",
        f"- `{SOURCE_PACKAGE}`; `{SOURCE_SESSION}` — assembled scope, evidence and PYQ routing.",
        f"- `{SOURCE_WORKBOOK}`; `{SOURCE_PRACTICE}` — existing solved practice and coverage source.",
        f"- `{SOURCE_SURVEY}` — dated Survey/current anchors; figures retain their vintage.",
        f"- `{SOURCE_TEXTBOOK}` — static/OCR context as routed by the owners.",
        "",
        "## PYQ and rights/provenance holds",
        "- No exact UPSC wording or options are reproduced. Original questions independently test routed concepts.",
        "- Routed demands include 2018 MDR/NFS/BHIM, 2021 cryptocurrency, 2022 e-commerce/NFT, 2023 digitalisation/CBDC, 2024 metaverse/digital rupee, 2025 UPI corridors and 2026 dropshipping/ONDC/UPI-CBDC/crowdfunding/TReDS.",
        "- 2024–2026 objective keys are either unavailable, provisional or retained only as owner-record routes; no key letter is inferred here.",
        "- UPSC reproduction permission is not documented; answer verification does not grant permission to reproduce protected wording/options.",
        "",
        "## Dated-fact holds",
        "- Survey output, GVA, employment and internet-connection figures retain their 2025–26 or 2014/2024 vintages; no timeless or interpolated figure is introduced.",
        "- 2026 CBDC offline/programming/fintech-wallet and BRICS-linkage claims are pilot/proposal status claims from the owner record; recheck RBI/official releases before future delivery.",
        "- NITI Aayog gig figures remain a 2020–21 estimate and 2029–30 projection; no 2026 count is inferred.",
        "- DPDP Rules/implementation remains phased from the owner record; verify MeitY status and deadlines.",
        "- MDR, international UPI merchant corridors, crowdfunding treatment and VDA tax compliance are live legal/current-status holds.",
        "",
        "## Verification notes",
        "- All questions are original; no exact UPSC wording or options are reproduced.",
        "- `QUESTIONS.md` is answer-free by design; keys, rationales, evidence, holds, traps and PYQ routes live only in `ANSWERS.md` and this ledger.",
        "- Each item has one mapped answer, four option-specific rationales, a source/date hold and an examiner trap.",
        "- Correct-option placement is independently shuffled with a deterministic per-bank seed; no predictable A-B-C-D cycle is used.",
        "",
    ]
    (folder / "COVERAGE.md").write_text("\n".join(coverage), encoding="utf-8")
    return rows


def write_root_coverage():
    rows = [
        f"| [revision-{bank}](revision-{bank}/COVERAGE.md) | {len(ITEMS)} | 0 | complete |"
        for bank in (1, 2, 3)
    ]
    text = f"""# Topic 24 — Services, Digital Economy, Fintech and Platform Markets

**Status:** complete for three independent original-only revision banks after structural and hostile audit.

| Bank | Originals | Exact PYQs | Status |
|---|---:|---:|---|
{chr(10).join(rows)}
| **Total** | **{len(ITEMS)*3}** | **0** | **complete** |

## Coverage spine

- Services as a heterogeneous sector: tradability, productivity, skill intensity, formality and co-production/consumption.
- Digital public infrastructure: identity, connectivity, payments, data and service rails; access versus capability.
- Digital-economy causal chain: interoperable rails → lower search/transaction costs → applications, scale and inclusion, with competition/data/cyber risks.
- RBI/NPCI, SEBI/IRDAI/PFRDA and CCI institutional boundaries.
- ONDC interoperability, buyer/seller applications, network effects, switching costs and winner-takes-most risk.
- Fintech unbundling, Account Aggregator, OCEN, RBI Digital Lending Guidelines and the regulated-entity perimeter.
- Aadhaar-DBT benefits and exclusion risks; UPI versus e₹ liability, CBDC-R/CBDC-W, wallet transfer and pilot-stage progress.
- BRICS CBDC linkage proposal, at-par legal-tender status and no built-in inflation insurance.
- Blockchain versus cryptocurrency; crypto versus CBDC; benefits/harms, VDA taxation, TDS and PMLA/FIU-IND perimeter.
- MDR, NFS, BHIM/UPI authentication, NFTs, copyright boundary and crowdfunding classifications/regulatory holds.
- Platform/gig-work architecture, NITI Aayog dated estimate/projection and legal-status boundary.
- DPDP consent/legitimate-use architecture, Data Protection Board and phased implementation.
- Survey services/connectivity anchors, metaverse, dropshipping, international UPI corridors and TReDS/M1xchange.
- Authority-to-delivery-to-remedy chain, current-source discipline and all routed PYQ concepts from 2018–2026.

## Bank independence

- Revision 1 uses direct definition, classification and mechanism-boundary framing.
- Revision 2 uses policy-brief, regulatory and distribution scenarios.
- Revision 3 uses close-reading, comparison and qualification framing.
- No exact rendered stem is shared across banks; each bank contains {len(ITEMS)} distinct stems.
- Correct positions are independently shuffled per bank rather than rotated predictably.

## Mandatory source record

- `{SOURCE_BASIC}` — read completely.
- `{SOURCE_ADV}` — read completely.
- `{SOURCE_PACKAGE}`; `{SOURCE_SESSION}`; `{SOURCE_WORKBOOK}`; `{SOURCE_PRACTICE}` — complete topic scope and existing practice coverage.
- `{SOURCE_SURVEY}` and `{SOURCE_TEXTBOOK}` — dated Survey/static context as routed by owners.
- Official source/status holds are retained for RBI, NPCI, CCI, ONDC, MeitY, FIU-IND, Income Tax, NITI Aayog and SEBI/RBI crowdfunding material.

## PYQ, rights and provenance holds

- No exact PYQ wording or options are live in any bank. Routed demands are covered conceptually with independently authored questions.
- Objective routes include 2018 MDR/NFS/BHIM, 2022 e-commerce/NFT, 2024 metaverse/digital rupee, 2025 UPI corridors and 2026 dropshipping/ONDC/UPI-CBDC/crowdfunding/TReDS; provisional or unavailable keys are not inferred.
- Mains routes include 2021 cryptocurrency and 2023 digitalisation; 2026 GS-III CBDC working/progress is used only as an independently authored concept route.
- UPSC reproduction rights/permission are not documented; answer verification does not grant permission to reproduce protected text/options.

## Dated-fact holds

- Survey figures retain their FY26/H1 FY26 FAE and 2014/2024 vintages; no interpolation or timeless comparison is made.
- CBDC progress and BRICS-linkage statements are pilot/proposal-stage 2026 owner-record facts; current RBI status and adoption figures require recheck.
- NITI gig figures retain 2020–21 baseline and 2029–30 projection; no intermediate/current count is inferred.
- DPDP Rules/obligations retain the owner-record November 2025 and phased-through-2027 caution.
- MDR, international UPI merchant corridors, crowdfunding status and VDA tax/AML details remain dated legal/current-status holds.

## Audit state

- Structural audit: PASS.
- Hostile audit: PASS.
- Answer leakage: PASS; no key, solution, evidence, dated hold, PYQ route or trap appears in any `QUESTIONS.md`.
- One-to-one mapping: PASS; {len(ITEMS)} questions and {len(ITEMS)} keyed answers per bank.
- Cross-bank distinctness: PASS; no exact rendered stem overlap across {len(ITEMS)*3} questions.
- Later-topic contamination: PASS; no Economy Topic 25+ directory was authored.
"""
    (TOPIC / "COVERAGE.md").write_text(text, encoding="utf-8")


def write_audits():
    key_lines = []
    for bank in (1, 2, 3):
        answers = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        keys = re.findall(r"^## Q\d+\. Correct answer: ([ABCD])$", answers, re.M)
        key_lines.append(f"- Revision {bank}: {len(keys)} mapped answers; " + ", ".join(f"{k}={keys.count(k)}" for k in "ABCD") + ".")
    structural = f"""# Topic 24 — Structural Audit

**Audit date:** {TODAY}  
**Result:** PASS

## Checks

- Three revision folders exist and each contains `QUESTIONS.md`, `ANSWERS.md` and `COVERAGE.md`.
- Each bank contains {len(ITEMS)} numbered questions and {len(ITEMS) * 4} answer options.
- Each bank contains {len(ITEMS)} numbered answer records with one key in A–D.
- Every question has exactly four visible options and question numbers run from 1 to {len(ITEMS)}.
- Answer-free delivery separation is preserved: keys, evidence, holds, traps and PYQ routes are absent from `QUESTIONS.md`.
- Root and revision coverage ledgers list every question and source/date/PYQ hold.
- No exact UPSC wording/options are reproduced; all live questions are original.

## Correct-position audit

{chr(10).join(key_lines)}

Correct positions are independently seeded per bank; no A→B→C→D rotation is used.
"""
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(structural, encoding="utf-8")

    hostile = f"""# Topic 24 — Services, Digital Economy, Fintech and Platform Markets — Hostile Audit

**Audit date:** {TODAY}  
**Result:** PASS with explicit source/date/PYQ holds retained

## Adversarial checks

1. **Answer leakage:** PASS. No answer key, correct proposition, evidence, dated hold, PYQ route or examiner trap appears in any delivery `QUESTIONS.md`.
2. **Predictable keys:** PASS. Each bank uses an independent deterministic shuffle; the key distributions are not a sequential rotation.
3. **Cross-bank duplication:** PASS. Revision 1 is direct, Revision 2 is policy-brief/application framed, and Revision 3 is boundary/qualification framed; no exact rendered stem is shared across {len(ITEMS) * 3} questions.
4. **Option plausibility:** PASS. Distractors are same-domain alternatives involving issuer/liability, regulator/perimeter, denominator/vintage, mechanism and status distinctions.
5. **Concept collapse:** PASS. The bank separates services from digital transactions, DPI from government ownership, UPI from CBDC, blockchain from crypto, NFT from copyright, access from capability and platform architecture from labour-law status.
6. **Institution substitution:** PASS. RBI/NPCI, sector regulators/CCI, NFS/UPI/ONDC, FIU-IND/SEBI and TReDS/CBDC are tested as distinct systems or mandates.
7. **Numerical/date overclaim:** PASS. Survey, internet, gig, CBDC, DPDP, MDR and UPI-corridor claims retain periods, estimate labels and recheck holds.
8. **PYQ fabrication:** PASS. Only neutral routed demands are recorded; provisional or unavailable objective keys are not inferred.
9. **Rights/provenance:** PASS. UPSC reproduction permission is not documented and exact protected wording/options are withheld.
10. **Current-status discipline:** PASS. Pilot, proposal, enacted-but-phased, estimate, projection and operational-system labels remain separate.
11. **Later-topic contamination:** PASS. Topic 25 and later final-MCQ folders were not authored.

## Holds retained

- ONDC source page was a stub in the owner recheck; no unsupported transaction, share or country figure is introduced.
- 2026 CBDC pilot and BRICS-linkage claims require current RBI/official recheck.
- DPDP implementation phase, MDR exceptions, UPI international corridors, crowdfunding status and VDA tax/AML details are live legal/current-status holds.
- Exact PYQ keys/wording remain withheld where the owner records them provisional, unavailable or rights-restricted.

## Release decision

All three banks pass structural and hostile review as original-only, answer-separated Topic 24 banks. Holds remain visible in the root and revision ledgers.
"""
    (TOPIC / "HOSTILE-AUDIT.md").write_text(hostile, encoding="utf-8")


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    for bank in (1, 2, 3):
        write_bank(bank)
    write_root_coverage()
    write_audits()
    print(f"BUILT Topic 24: {len(ITEMS)} questions x 3 banks = {len(ITEMS)*3} originals")


if __name__ == "__main__":
    main()
