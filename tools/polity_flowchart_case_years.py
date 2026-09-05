"""Explicit Polity flowchart case-year normalization and validation.

The registry is deliberately curated. It never infers a year from a case name.
"""

from __future__ import annotations

import copy
import re
import textwrap
from dataclasses import dataclass
from typing import Any, Iterable
from urllib.parse import quote_plus


YEAR_RE = r"(?:18|19|20)\d{2}"
MAX_ASCII_WIDTH = 100


@dataclass(frozen=True)
class CaseRule:
    case_id: str
    canonical: str
    year: int
    aliases: tuple[str, ...]
    source_title: str
    source_url: str


def _ik_search(case_name: str) -> str:
    return "https://indiankanoon.org/search/?formInput=" + quote_plus(case_name)


CASES: dict[str, CaseRule] = {
    rule.case_id: rule
    for rule in (
        CaseRule(
            "minerva-mills",
            "Minerva Mills",
            1980,
            ("Minerva Mills",),
            "Minerva Mills Ltd. v. Union of India, Supreme Court judgment",
            _ik_search("Minerva Mills v Union of India"),
        ),
        CaseRule(
            "rajendra-n-shah",
            "Union of India v. Rajendra N. Shah",
            2021,
            ("Union of India v. Rajendra N. Shah", "Rajendra N. Shah"),
            "Union of India v. Rajendra N. Shah, Supreme Court judgment",
            "https://indiankanoon.org/search/?formInput=Rajendra+N.+Shah+20+July+2021",
        ),
        CaseRule(
            "common-cause-lokpal",
            "Common Cause v. Union of India",
            2017,
            ("Common Cause v. Union of India", "Common Cause"),
            "Common Cause v. Union of India, judgment dated 27 April 2017",
            _ik_search("Common Cause v Union of India Lokpal 27 April 2017"),
        ),
        CaseRule(
            "lok-prahari",
            "Lok Prahari v. Union of India",
            2018,
            ("Lok Prahari v. Union of India", "Lok Prahari"),
            "Lok Prahari v. Union of India, judgment dated 16 February 2018",
            _ik_search("Lok Prahari v Union of India 16 February 2018"),
        ),
        CaseRule(
            "thalappalam",
            "Thalappalam Service Cooperative Bank",
            2013,
            (
                "Thalappalam Service Cooperative Bank Ltd. v. State of Kerala",
                "Thalappalam Service Cooperative Bank",
                "Thalappalam",
            ),
            "Thalappalam Service Cooperative Bank Ltd. v. State of Kerala, judgment dated 7 October 2013",
            _ik_search("Thalappalam Service Cooperative Bank 7 October 2013"),
        ),
        CaseRule(
            "gujarat-university-language",
            "Gujarat University v. Shri Krishna",
            1963,
            (
                "Gujarat University v. Shri Krishna",
                "Gujarat University",
            ),
            "Gujarat University v. Shri Krishna Ranganath Mudholkar, judgment dated 5 March 1963",
            _ik_search("Gujarat University Shri Krishna 5 March 1963"),
        ),
        CaseRule(
            "dav-college-language",
            "D.A.V. College v. State of Punjab",
            1971,
            ("D.A.V. College v. State of Punjab", "D.A.V. College"),
            "D.A.V. College v. State of Punjab, judgment dated 5 May 1971",
            _ik_search("DAV College State of Punjab 5 May 1971 language"),
        ),
        CaseRule(
            "karnataka-english-medium",
            "State of Karnataka v. Associated Management",
            2014,
            (
                "State of Karnataka v. Associated Management of English Medium Primary and Secondary Schools",
                "State of Karnataka v. Associated Management",
                "Associated Management of English Medium",
            ),
            "State of Karnataka v. Associated Management of English Medium Primary and Secondary Schools, judgment dated 6 May 2014",
            _ik_search("State Karnataka Associated Management English Medium 6 May 2014"),
        ),
        CaseRule(
            "article-370",
            "In Re: Article 370 of the Constitution",
            2023,
            ("In Re: Article 370 of the Constitution",),
            "In Re: Article 370 of the Constitution, Supreme Court judgment dated 11 December 2023",
            "https://api.sci.gov.in/supremecourt/2019/29796/29796_2019_1_1501_49019_Judgement_11-Dec-2023.pdf",
        ),
        CaseRule(
            "berubari-union",
            "Berubari Union",
            1960,
            ("In Re: Berubari Union", "Berubari Union", "Berubari"),
            "In Re: Berubari Union, Supreme Court advisory opinion",
            _ik_search("In Re Berubari Union 14 March 1960"),
        ),
        CaseRule(
            "kesavananda-bharati",
            "Kesavananda Bharati",
            1973,
            ("Kesavananda Bharati", "Kesavananda"),
            "Kesavananda Bharati v. State of Kerala, Supreme Court judgment",
            "https://indiankanoon.org/docfragment/257876/",
        ),
        CaseRule(
            "lic-consumer-education",
            "LIC of India",
            1995,
            (
                "L.I.C. of India v. Consumer Education and Research Centre",
                "LIC of India v. Consumer Education and Research Centre",
                "LIC of India",
                "LIC",
            ),
            "L.I.C. of India v. Consumer Education and Research Centre, judgment dated 10 May 1995",
            "https://indiankanoon.org/docfragment/1513693/",
        ),
        CaseRule(
            "ds-nakara",
            "D.S. Nakara",
            1982,
            ("D.S. Nakara", "Nakara"),
            "D.S. Nakara v. Union of India, judgment dated 17 December 1982",
            "https://indiankanoon.org/docfragment/1416283/",
        ),
        CaseRule(
            "gb-pant-university",
            "G.B. Pant University",
            2000,
            (
                "G.B. Pant University of Agriculture and Technology",
                "G.B. Pant University",
                "Pant University",
            ),
            "G.B. Pant University of Agriculture and Technology v. State of Uttar Pradesh, judgment dated 10 August 2000",
            "https://indiankanoon.org/docfragment/198698/",
        ),
        CaseRule(
            "excel-wear",
            "Excel Wear",
            1978,
            ("Excel Wear",),
            "Excel Wear v. Union of India, Supreme Court judgment",
            _ik_search("Excel Wear v Union of India 29 September 1978"),
        ),
        CaseRule(
            "maganbhai",
            "Maganbhai Ishwarbhai Patel",
            1969,
            ("Maganbhai Ishwarbhai Patel", "Maganbhai Ishwarbhai"),
            "Maganbhai Ishwarbhai Patel v. Union of India, Supreme Court judgment",
            _ik_search("Maganbhai Ishwarbhai Patel v Union of India 9 January 1969"),
        ),
        CaseRule(
            "section-6a",
            "In Re: Section 6A",
            2024,
            ("In Re: Section 6A",),
            "In Re: Section 6A of the Citizenship Act 1955, Supreme Court judgment dated 17 October 2024",
            _ik_search("In Re Section 6A Citizenship Act 17 October 2024"),
        ),
        CaseRule(
            "pradeep-kumar-biswas",
            "Pradeep Kumar Biswas",
            2002,
            ("Pradeep Kumar Biswas",),
            "Pradeep Kumar Biswas v. Indian Institute of Chemical Biology, Supreme Court judgment",
            _ik_search("Pradeep Kumar Biswas 16 February 2002"),
        ),
        CaseRule(
            "ep-royappa",
            "E.P. Royappa",
            1973,
            ("E.P. Royappa", "Royappa"),
            "E.P. Royappa v. State of Tamil Nadu, judgment dated 23 November 1973",
            "https://indiankanoon.org/docfragment/1327287/",
        ),
        CaseRule(
            "maneka-gandhi",
            "Maneka Gandhi",
            1978,
            ("Maneka Gandhi", "Maneka"),
            "Maneka Gandhi v. Union of India, Supreme Court judgment",
            _ik_search("Maneka Gandhi v Union of India 25 January 1978"),
        ),
        CaseRule(
            "champakam-dorairajan",
            "Champakam Dorairajan",
            1951,
            (
                "State of Madras v. Champakam Dorairajan",
                "Champakam Dorairajan",
                "Champakam",
            ),
            "State of Madras v. Champakam Dorairajan, Supreme Court judgment",
            _ik_search("State of Madras v Champakam Dorairajan 9 April 1951"),
        ),
        CaseRule(
            "indra-sawhney",
            "Indra Sawhney",
            1992,
            ("Indra Sawhney",),
            "Indra Sawhney v. Union of India, judgment dated 16 November 1992",
            "https://indiankanoon.org/docfragment/1363234/",
        ),
        CaseRule(
            "m-nagaraj",
            "M. Nagaraj",
            2006,
            ("M. Nagaraj", "Nagaraj"),
            "M. Nagaraj v. Union of India, Supreme Court judgment",
            _ik_search("M Nagaraj v Union of India 19 October 2006"),
        ),
        CaseRule(
            "jarnail-singh",
            "Jarnail Singh",
            2018,
            ("Jarnail Singh", "Jarnail"),
            "Jarnail Singh v. Lachhmi Narain Gupta, Supreme Court judgment",
            _ik_search("Jarnail Singh Lachhmi Narain Gupta 26 September 2018"),
        ),
        CaseRule(
            "janhit-abhiyan",
            "Janhit Abhiyan",
            2022,
            ("Janhit Abhiyan", "Janhit"),
            "Janhit Abhiyan v. Union of India, Supreme Court judgment",
            _ik_search("Janhit Abhiyan v Union of India 7 November 2022"),
        ),
        CaseRule(
            "davinder-singh",
            "Davinder Singh",
            2024,
            ("State of Punjab v. Davinder Singh", "Davinder Singh"),
            "State of Punjab v. Davinder Singh, Supreme Court judgment",
            _ik_search("State of Punjab v Davinder Singh 1 August 2024"),
        ),
        CaseRule(
            "shreya-singhal",
            "Shreya Singhal",
            2015,
            ("Shreya Singhal",),
            "Shreya Singhal v. Union of India, Supreme Court judgment",
            _ik_search("Shreya Singhal v Union of India 24 March 2015"),
        ),
        CaseRule(
            "anuradha-bhasin",
            "Anuradha Bhasin",
            2020,
            ("Anuradha Bhasin",),
            "Anuradha Bhasin v. Union of India, Supreme Court judgment",
            _ik_search("Anuradha Bhasin v Union of India 10 January 2020"),
        ),
        CaseRule(
            "kedar-nath-singh",
            "Kedar Nath Singh",
            1962,
            ("Kedar Nath Singh", "Kedar Nath"),
            "Kedar Nath Singh v. State of Bihar, Supreme Court judgment",
            _ik_search("Kedar Nath Singh v State of Bihar 20 January 1962"),
        ),
        CaseRule(
            "ak-gopalan",
            "A.K. Gopalan",
            1950,
            ("A.K. Gopalan", "Gopalan"),
            "A.K. Gopalan v. State of Madras, Supreme Court judgment",
            _ik_search("A K Gopalan v State of Madras 19 May 1950"),
        ),
        CaseRule(
            "rc-cooper",
            "R.C. Cooper",
            1970,
            ("R.C. Cooper",),
            "R.C. Cooper v. Union of India, Supreme Court judgment",
            _ik_search("R C Cooper v Union of India 10 February 1970"),
        ),
        CaseRule(
            "puttaswamy-privacy",
            "K.S. Puttaswamy",
            2017,
            ("K.S. Puttaswamy", "Puttaswamy"),
            "Justice K.S. Puttaswamy (Retd.) v. Union of India, privacy judgment dated 24 August 2017",
            "https://indiankanoon.org/docfragment/91938676/",
        ),
        CaseRule(
            "ir-coelho",
            "I.R. Coelho",
            2007,
            ("I.R. Coelho",),
            "I.R. Coelho v. State of Tamil Nadu, judgment dated 11 January 2007",
            "https://indiankanoon.org/docfragment/322504/",
        ),
        CaseRule(
            "property-owners",
            "Property Owners Association",
            2024,
            ("Property Owners Association", "Property Owners"),
            "Property Owners Association v. State of Maharashtra, judgment dated 5 November 2024",
            "https://indiankanoon.org/docfragment/114205571/",
        ),
        CaseRule(
            "vishaka",
            "Vishaka",
            1997,
            ("Vishaka",),
            "Vishaka v. State of Rajasthan, Supreme Court judgment",
            _ik_search("Vishaka v State of Rajasthan 13 August 1997"),
        ),
        CaseRule(
            "golaknath",
            "I.C. Golaknath",
            1967,
            ("I.C. Golaknath", "Golaknath"),
            "I.C. Golaknath v. State of Punjab, judgment dated 27 February 1967",
            "https://indiankanoon.org/docfragment/120358/",
        ),
        CaseRule(
            "bijoe-emmanuel",
            "Bijoe Emmanuel",
            1986,
            ("Bijoe Emmanuel", "Bijoe"),
            "Bijoe Emmanuel v. State of Kerala, Supreme Court judgment",
            _ik_search("Bijoe Emmanuel v State of Kerala 11 August 1986"),
        ),
        CaseRule(
            "naveen-jindal",
            "Naveen Jindal",
            2004,
            ("Union of India v. Naveen Jindal", "Naveen Jindal"),
            "Union of India v. Naveen Jindal, Supreme Court judgment",
            _ik_search("Union of India v Naveen Jindal 23 January 2004"),
        ),
        CaseRule(
            "shyam-narayan-chouksey",
            "Shyam Narayan Chouksey",
            2018,
            ("Shyam Narayan Chouksey",),
            "Shyam Narayan Chouksey v. Union of India, final order dated 9 January 2018",
            _ik_search("Shyam Narayan Chouksey 9 January 2018"),
        ),
        CaseRule(
            "shankari-prasad",
            "Shankari Prasad",
            1951,
            ("Shankari Prasad", "Sankari Prasad"),
            "Shankari Prasad Singh Deo v. Union of India, Supreme Court judgment",
            _ik_search("Shankari Prasad 5 October 1951"),
        ),
        CaseRule(
            "sajjan-singh",
            "Sajjan Singh",
            1964,
            ("Sajjan Singh",),
            "Sajjan Singh v. State of Rajasthan, judgment dated 30 October 1964",
            "https://indiankanoon.org/docfragment/1308308/",
        ),
        CaseRule(
            "indira-gandhi",
            "Indira Nehru Gandhi v. Raj Narain",
            1975,
            (
                "Indira Nehru Gandhi v. Raj Narain",
                "Indira Gandhi v. Raj Narain",
                "Indira Gandhi",
            ),
            "Indira Nehru Gandhi v. Raj Narain, judgment dated 7 November 1975",
            "https://indiankanoon.org/docfragment/936707/",
        ),
        CaseRule(
            "waman-rao",
            "Waman Rao",
            1980,
            ("Waman Rao",),
            "Waman Rao v. Union of India, judgment dated 13 November 1980",
            "https://indiankanoon.org/docfragment/1124708/",
        ),
        CaseRule(
            "anjum-kadari",
            "Anjum Kadari",
            2024,
            ("Anjum Kadari",),
            "Anjum Kadari v. Union of India, 2024 INSC 831",
            _ik_search("Anjum Kadari 2024 INSC 831"),
        ),
        CaseRule(
            "sr-bommai",
            "S.R. Bommai",
            1994,
            ("S.R. Bommai", "Bommai"),
            "S.R. Bommai v. Union of India, judgment dated 11 March 1994",
            "https://indiankanoon.org/docfragment/139734870/",
        ),
        CaseRule(
            "state-of-rajasthan",
            "State of Rajasthan v. Union of India",
            1977,
            ("State of Rajasthan v. Union of India", "State of Rajasthan"),
            "State of Rajasthan v. Union of India, Supreme Court judgment",
            _ik_search("State of Rajasthan v Union of India 6 May 1977"),
        ),
        CaseRule(
            "mohit-minerals",
            "Mohit Minerals",
            2022,
            ("Union of India v. Mohit Minerals", "Mohit Minerals"),
            "Union of India v. Mohit Minerals, Supreme Court judgment",
            _ik_search("Union of India v Mohit Minerals 19 May 2022"),
        ),
        CaseRule(
            "adm-jabalpur",
            "ADM Jabalpur",
            1976,
            ("A.D.M. Jabalpur", "ADM Jabalpur"),
            "ADM Jabalpur v. Shivkant Shukla, Supreme Court judgment",
            _ik_search("ADM Jabalpur v Shivkant Shukla 28 April 1976"),
        ),
        CaseRule(
            "rameshwar-prasad",
            "Rameshwar Prasad",
            2006,
            ("Rameshwar Prasad",),
            "Rameshwar Prasad v. Union of India, Supreme Court judgment",
            _ik_search("Rameshwar Prasad v Union of India 24 January 2006"),
        ),
        CaseRule(
            "shamsher-singh",
            "Shamsher Singh",
            1974,
            ("Shamsher Singh",),
            "Shamsher Singh v. State of Punjab, Supreme Court judgment",
            _ik_search("Shamsher Singh v State of Punjab 23 August 1974"),
        ),
        CaseRule(
            "parshotam-lal-dhingra",
            "Parshotam Lal Dhingra",
            1957,
            ("Parshotam Lal Dhingra", "P.L. Dhingra", "Dhingra"),
            "Parshotam Lal Dhingra v. Union of India, judgment dated 1 November 1957",
            _ik_search("Parshotam Lal Dhingra v Union of India 1958"),
        ),
        CaseRule(
            "khem-chand",
            "Khem Chand",
            1957,
            ("Khem Chand",),
            "Khem Chand v. Union of India, judgment dated 13 December 1957",
            _ik_search("Khem Chand v Union of India 13 December 1957"),
        ),
        CaseRule(
            "tulsiram-patel",
            "Union of India v. Tulsiram Patel",
            1985,
            (
                "Union of India v. Tulsiram Patel",
                "Union of India v Tulsiram Patel",
                "Tulsiram Patel",
            ),
            "Union of India v. Tulsiram Patel, judgment dated 11 July 1985",
            _ik_search("Union of India v Tulsiram Patel 11 July 1985"),
        ),
        CaseRule(
            "ecil-karunakar",
            "ECIL v. B. Karunakar",
            1993,
            (
                "Managing Director, ECIL v. B. Karunakar",
                "ECIL v. B. Karunakar",
                "B. Karunakar",
            ),
            "Managing Director, ECIL v. B. Karunakar, judgment dated 1 October 1993",
            _ik_search("Managing Director ECIL v B Karunakar 1 October 1993"),
        ),
        CaseRule(
            "tsr-subramanian",
            "T.S.R. Subramanian",
            2013,
            ("T.S.R. Subramanian", "TSR Subramanian"),
            "T.S.R. Subramanian v. Union of India, judgment dated 31 October 2013",
            _ik_search("TSR Subramanian v Union of India 31 October 2013"),
        ),
        CaseRule(
            "dc-wadhwa",
            "D.C. Wadhwa",
            1986,
            ("D.C. Wadhwa",),
            "D.C. Wadhwa v. State of Bihar, judgment dated 20 December 1986",
            "https://indiankanoon.org/docfragment/504006/",
        ),
        CaseRule(
            "krishna-kumar-singh",
            "Krishna Kumar Singh",
            2017,
            ("Krishna Kumar Singh",),
            "Krishna Kumar Singh v. State of Bihar, judgment dated 2 January 2017",
            "https://indiankanoon.org/docfragment/107225908/",
        ),
        CaseRule(
            "kehar-singh",
            "Kehar Singh",
            1988,
            ("Kehar Singh",),
            "Kehar Singh v. Union of India, judgment dated 16 December 1988",
            "https://indiankanoon.org/docfragment/1152284/",
        ),
        CaseRule(
            "maru-ram",
            "Maru Ram",
            1980,
            ("Maru Ram",),
            "Maru Ram v. Union of India, judgment dated 11 November 1980",
            "https://indiankanoon.org/docfragment/1222748/",
        ),
        CaseRule(
            "sr-chaudhuri",
            "S.R. Chaudhuri",
            2001,
            ("S.R. Chaudhuri",),
            "S.R. Chaudhuri v. State of Punjab, Supreme Court judgment",
            _ik_search("S R Chaudhuri v State of Punjab 17 August 2001"),
        ),
        CaseRule(
            "sita-soren",
            "Sita Soren",
            2024,
            ("Sita Soren",),
            "Sita Soren v. Union of India, Supreme Court judgment dated 4 March 2024",
            _ik_search("Sita Soren v Union of India 4 March 2024"),
        ),
        CaseRule(
            "puttaswamy-aadhaar",
            "K.S. Puttaswamy (Aadhaar)",
            2018,
            (
                "Justice K.S. Puttaswamy (Aadhaar)",
                "K.S. Puttaswamy (Aadhaar)",
            ),
            "Justice K.S. Puttaswamy (Retd.) v. Union of India, Aadhaar judgment dated 26 September 2018",
            "https://indiankanoon.org/docfragment/127517806/",
        ),
        CaseRule(
            "rojer-mathew",
            "Rojer Mathew v. South Indian Bank",
            2019,
            ("Rojer Mathew v. South Indian Bank", "Rojer Mathew"),
            "Rojer Mathew v. South Indian Bank, Supreme Court judgment",
            _ik_search("Rojer Mathew v South Indian Bank 13 November 2019"),
        ),
        CaseRule(
            "first-judges-case",
            "First Judges Case",
            1981,
            ("First Judges Case",),
            "S.P. Gupta v. Union of India, judgment dated 30 December 1981",
            _ik_search("S P Gupta v Union of India 30 December 1981"),
        ),
        CaseRule(
            "second-judges-case",
            "Second Judges Case",
            1993,
            ("Second Judges Case",),
            "Supreme Court Advocates-on-Record Association v. Union of India, judgment dated 6 October 1993",
            _ik_search("Second Judges Case 6 October 1993"),
        ),
        CaseRule(
            "third-judges-case",
            "Third Judges Case",
            1998,
            ("Third Judges Case",),
            "In re Special Reference No. 1 of 1998, advisory opinion dated 28 October 1998",
            _ik_search("Special Reference No 1 of 1998 Third Judges Case"),
        ),
        CaseRule(
            "fourth-judges-case",
            "Fourth Judges Case",
            2015,
            ("Fourth Judges Case", "NJAC Case"),
            "Supreme Court Advocates-on-Record Association v. Union of India, NJAC judgment dated 16 October 2015",
            _ik_search("NJAC judgment 16 October 2015"),
        ),
        CaseRule(
            "l-chandra-kumar",
            "L. Chandra Kumar",
            1997,
            ("L. Chandra Kumar",),
            "L. Chandra Kumar v. Union of India, judgment dated 18 March 1997",
            _ik_search("L Chandra Kumar v Union of India 18 March 1997"),
        ),
        CaseRule(
            "supreme-court-bar-association",
            "Supreme Court Bar Association",
            1998,
            ("Supreme Court Bar Association",),
            "Supreme Court Bar Association v. Union of India, judgment dated 17 April 1998",
            _ik_search("Supreme Court Bar Association v Union of India 17 April 1998"),
        ),
        CaseRule(
            "rupa-ashok-hurra",
            "Rupa Ashok Hurra",
            2002,
            ("Rupa Ashok Hurra",),
            "Rupa Ashok Hurra v. Ashok Hurra, judgment dated 10 April 2002",
            _ik_search("Rupa Ashok Hurra v Ashok Hurra 10 April 2002"),
        ),
        CaseRule(
            "hussainara-khatoon",
            "Hussainara Khatoon",
            1979,
            ("Hussainara Khatoon",),
            "Hussainara Khatoon v. State of Bihar, Supreme Court judgment",
            _ik_search("Hussainara Khatoon 9 March 1979"),
        ),
        CaseRule(
            "state-tamil-nadu-governor",
            "State of Tamil Nadu v. Governor of Tamil Nadu",
            2025,
            ("State of Tamil Nadu v. Governor of Tamil Nadu",),
            "State of Tamil Nadu v. Governor of Tamil Nadu, 2025 INSC 481, judgment dated 8 April 2025",
            "https://api.sci.gov.in/supremecourt/2023/44785/44785_2023_1_1501_61019_Judgement_08-Apr-2025.pdf",
        ),
        CaseRule(
            "assent-advisory-opinion",
            "In re Assent, Withholding or Reservation of Bills",
            2025,
            (
                "In re Assent, Withholding or Reservation of Bills",
                "Article 143 assent opinion",
            ),
            "In re Assent, Withholding or Reservation of Bills, advisory opinion dated 20 November 2025",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
        ),
        CaseRule(
            "nabam-rebia",
            "Nabam Rebia",
            2016,
            ("Nabam Rebia",),
            "Nabam Rebia v. Deputy Speaker, judgment dated 13 July 2016",
            _ik_search("Nabam Rebia v Deputy Speaker 13 July 2016"),
        ),
        CaseRule(
            "subhash-desai",
            "Subhash Desai",
            2023,
            ("Subhash Desai",),
            "Subhash Desai v. Principal Secretary, Governor of Maharashtra, judgment dated 11 May 2023",
            _ik_search("Subhash Desai Governor Maharashtra 11 May 2023"),
        ),
        CaseRule(
            "kihoto-hollohan",
            "Kihoto Hollohan",
            1992,
            ("Kihoto Hollohan",),
            "Kihoto Hollohan v. Zachillhu, judgment dated 18 February 1992",
            _ik_search("Kihoto Hollohan v Zachillhu 18 February 1992"),
        ),
        CaseRule(
            "ravi-s-naik",
            "Ravi S. Naik",
            1994,
            ("Ravi S. Naik", "Ravi Naik"),
            "Ravi S. Naik v. Union of India, judgment dated 9 February 1994",
            _ik_search("Ravi S Naik v Union of India 9 February 1994"),
        ),
        CaseRule(
            "shrimanth-balasaheb-patil",
            "Shrimanth Balasaheb Patil",
            2019,
            ("Shrimanth Balasaheb Patil", "Shrimanth Patil"),
            "Shrimanth Balasaheb Patil v. Karnataka Legislative Assembly, judgment dated 13 November 2019",
            _ik_search("Shrimanth Balasaheb Patil 13 November 2019"),
        ),
        CaseRule(
            "keisham-meghachandra",
            "Keisham Meghachandra Singh",
            2020,
            ("Keisham Meghachandra Singh", "Keisham Meghachandra", "Keisham"),
            "Keisham Meghachandra Singh v. Speaker, Manipur Legislative Assembly, judgment dated 21 January 2020",
            _ik_search("Keisham Meghachandra Singh 21 January 2020"),
        ),
        CaseRule(
            "raja-ram-pal",
            "Raja Ram Pal",
            2007,
            ("Raja Ram Pal",),
            "Raja Ram Pal v. Hon'ble Speaker, Lok Sabha, judgment dated 10 January 2007",
            _ik_search("Raja Ram Pal 10 January 2007"),
        ),
        CaseRule(
            "sankalchand-sheth",
            "Sankalchand Himmatlal Sheth",
            1977,
            ("Sankalchand Himmatlal Sheth", "Sankalchand Sheth"),
            "Union of India v. Sankalchand Himmatlal Sheth, judgment dated 19 September 1977",
            _ik_search("Sankalchand Himmatlal Sheth 19 September 1977"),
        ),
        CaseRule(
            "chandra-mohan",
            "Chandra Mohan",
            1966,
            ("Chandra Mohan",),
            "Chandra Mohan v. State of Uttar Pradesh, Supreme Court judgment",
            _ik_search("Chandra Mohan v State of Uttar Pradesh 1966"),
        ),
        CaseRule(
            "sampat-prakash",
            "Sampat Prakash",
            1968,
            ("Sampat Prakash",),
            "Sampat Prakash v. State of Jammu and Kashmir, judgment dated 10 October 1968",
            _ik_search("Sampat Prakash v State of Jammu and Kashmir 10 October 1968"),
        ),
        CaseRule(
            "kishansing-tomar",
            "Kishansing Tomar",
            2006,
            ("Kishansing Tomar",),
            "Kishansing Tomar v. Municipal Corporation of Ahmedabad, Supreme Court judgment",
            _ik_search(
                "Kishansing Tomar Municipal Corporation Ahmedabad 2006"
            ),
        ),
        CaseRule(
            "k-krishna-murthy",
            "K. Krishna Murthy",
            2010,
            ("K. Krishna Murthy", "Krishna Murthy"),
            "K. Krishna Murthy v. Union of India, judgment dated 11 May 2010",
            _ik_search("K Krishna Murthy Union of India 11 May 2010"),
        ),
        CaseRule(
            "vikas-gawali",
            "Vikas Kishanrao Gawali",
            2021,
            ("Vikas Kishanrao Gawali", "Vikas Gawali"),
            "Vikas Kishanrao Gawali v. State of Maharashtra, judgment dated 4 March 2021",
            _ik_search(
                "Vikas Kishanrao Gawali State of Maharashtra 4 March 2021"
            ),
        ),
        CaseRule(
            "fouziya-imtiaz-shaikh",
            "State of Goa v. Fouziya Imtiaz Shaikh",
            2021,
            ("State of Goa v. Fouziya Imtiaz Shaikh", "Fouziya Imtiaz Shaikh"),
            "State of Goa v. Fouziya Imtiaz Shaikh, judgment dated 12 March 2021",
            _ik_search(
                "State of Goa Fouziya Imtiaz Shaikh 12 March 2021"
            ),
        ),
        CaseRule(
            "gnctd-aid-advice",
            "GNCTD aid-and-advice judgment",
            2018,
            ("GNCTD aid-and-advice judgment",),
            "Government of NCT of Delhi v. Union of India, Constitution Bench judgment dated 4 July 2018",
            _ik_search(
                "Government of NCT Delhi Union of India 4 July 2018"
            ),
        ),
        CaseRule(
            "gnctd-services",
            "Delhi services judgment",
            2023,
            ("Delhi services judgment", "May 2023 services judgment"),
            "Government of NCT of Delhi v. Union of India, Constitution Bench services judgment dated 11 May 2023",
            _ik_search(
                "Government of NCT Delhi Union of India 11 May 2023 services"
            ),
        ),
        CaseRule(
            "k-lakshminarayanan",
            "K. Lakshminarayanan",
            2018,
            ("K. Lakshminarayanan", "K. Lakshiminarayanan"),
            "K. Lakshminarayanan v. Union of India, judgment dated 6 December 2018",
            _ik_search(
                "K Lakshminarayanan Union of India 6 December 2018"
            ),
        ),
        CaseRule(
            "samatha",
            "Samatha",
            1997,
            ("Samatha",),
            "Samatha v. State of Andhra Pradesh, judgment dated 11 July 1997",
            _ik_search("Samatha State of Andhra Pradesh 11 July 1997"),
        ),
        CaseRule(
            "orissa-mining-corporation",
            "Orissa Mining Corporation",
            2013,
            ("Orissa Mining Corporation",),
            "Orissa Mining Corporation Ltd. v. Ministry of Environment and Forest, judgment dated 18 April 2013",
            _ik_search(
                "Orissa Mining Corporation Ministry Environment Forest 18 April 2013"
            ),
        ),
        CaseRule(
            "mohinder-singh-gill",
            "Mohinder Singh Gill",
            1977,
            ("Mohinder Singh Gill",),
            "Mohinder Singh Gill v. Chief Election Commissioner, judgment dated 2 December 1977",
            _ik_search(
                "Mohinder Singh Gill Chief Election Commissioner 2 December 1977"
            ),
        ),
        CaseRule(
            "ac-jose",
            "A.C. Jose",
            1984,
            ("A.C. Jose", "A. C. Jose"),
            "A.C. Jose v. Sivan Pillai, judgment dated 5 March 1984",
            _ik_search("A C Jose Sivan Pillai 5 March 1984"),
        ),
        CaseRule(
            "tn-seshan",
            "T.N. Seshan",
            1995,
            ("T.N. Seshan", "T. N. Seshan"),
            "T.N. Seshan v. Union of India, judgment dated 14 July 1995",
            _ik_search("T N Seshan Union of India 14 July 1995"),
        ),
        CaseRule(
            "adr-candidate-disclosure",
            "Union of India v. Association for Democratic Reforms",
            2002,
            (
                "Union of India v. Association for Democratic Reforms",
                "Association for Democratic Reforms candidate disclosure",
            ),
            "Union of India v. Association for Democratic Reforms, judgment dated 2 May 2002",
            _ik_search(
                "Union of India Association for Democratic Reforms 2 May 2002"
            ),
        ),
        CaseRule(
            "pucl-nota",
            "People's Union for Civil Liberties",
            2013,
            ("People's Union for Civil Liberties", "PUCL NOTA"),
            "People's Union for Civil Liberties v. Union of India, NOTA judgment dated 27 September 2013",
            _ik_search(
                "People's Union for Civil Liberties Union of India 27 September 2013 NOTA"
            ),
        ),
        CaseRule(
            "anoop-baranwal",
            "Anoop Baranwal",
            2023,
            ("Anoop Baranwal",),
            "Anoop Baranwal v. Union of India, Constitution Bench judgment dated 2 March 2023",
            _ik_search("Anoop Baranwal Union of India 2 March 2023"),
        ),
        CaseRule(
            "adr-vvpat",
            "Association for Democratic Reforms v. Election Commission of India",
            2024,
            (
                "Association for Democratic Reforms v. Election Commission of India",
                "ADR VVPAT",
            ),
            "Association for Democratic Reforms v. Election Commission of India, judgment dated 26 April 2024",
            _ik_search(
                "Association for Democratic Reforms Election Commission India 26 April 2024 VVPAT"
            ),
        ),
        CaseRule(
            "manbodhan-lal-srivastava",
            "State of U.P. v. Manbodhan Lal Srivastava",
            1957,
            (
                "State of U.P. v. Manbodhan Lal Srivastava",
                "Manbodhan Lal Srivastava",
            ),
            "State of U.P. v. Manbodhan Lal Srivastava, Supreme Court judgment",
            _ik_search(
                "State of Uttar Pradesh v Manbodhan Lal Srivastava 1957"
            ),
        ),
        CaseRule(
            "ashok-kumar-yadav",
            "Ashok Kumar Yadav",
            1985,
            ("Ashok Kumar Yadav v. State of Haryana", "Ashok Kumar Yadav"),
            "Ashok Kumar Yadav v. State of Haryana, Supreme Court judgment",
            _ik_search("Ashok Kumar Yadav State of Haryana 10 May 1985"),
        ),
        CaseRule(
            "shankarsan-dash",
            "Shankarsan Dash",
            1991,
            ("Shankarsan Dash v. Union of India", "Shankarsan Dash"),
            "Shankarsan Dash v. Union of India, Supreme Court judgment",
            _ik_search("Shankarsan Dash Union of India 30 April 1991"),
        ),
        CaseRule(
            "mv-thimmaiah",
            "M.V. Thimmaiah",
            2007,
            ("M.V. Thimmaiah v. UPSC", "M.V. Thimmaiah"),
            "M.V. Thimmaiah v. Union Public Service Commission, Supreme Court judgment",
            _ik_search("M V Thimmaiah Union Public Service Commission 2007"),
        ),
        CaseRule(
            "k-manjusree",
            "K. Manjusree",
            2008,
            ("K. Manjusree v. State of Andhra Pradesh", "K. Manjusree"),
            "K. Manjusree v. State of Andhra Pradesh, Supreme Court judgment",
            _ik_search("K Manjusree State of Andhra Pradesh 15 February 2008"),
        ),
        CaseRule(
            "tej-prakash-pathak",
            "Tej Prakash Pathak",
            2024,
            (
                "Tej Prakash Pathak v. Rajasthan High Court",
                "Tej Prakash Pathak",
            ),
            "Tej Prakash Pathak v. Rajasthan High Court, 2024 INSC 847",
            _ik_search("Tej Prakash Pathak Rajasthan High Court 2024 INSC 847"),
        ),
        CaseRule(
            "bhim-singh-article-282",
            "Bhim Singh",
            2010,
            ("Bhim Singh v. Union of India", "Bhim Singh"),
            "Bhim Singh v. Union of India, Supreme Court judgment",
            _ik_search("Bhim Singh Union of India Article 282 2010"),
        ),
        CaseRule(
            "jaishri-laxmanrao-patil",
            "Jaishri Laxmanrao Patil",
            2021,
            (
                "Jaishri Laxmanrao Patil v. Chief Minister, Maharashtra",
                "Jaishri Laxmanrao Patil",
                "Jaishri Patil",
            ),
            "Jaishri Laxmanrao Patil v. Chief Minister, Maharashtra, judgment dated 5 May 2021",
            "https://api.sci.gov.in/supremecourt/2019/23618/23618_2019_35_1501_27992_Judgement_05-May-2021.pdf",
        ),
        CaseRule(
            "arvind-gupta-cag",
            "Arvind Gupta",
            2012,
            ("Arvind Gupta v. Union of India", "Arvind Gupta"),
            "Arvind Gupta v. Union of India, Supreme Court order on performance audit",
            _ik_search("Arvind Gupta Union of India CAG performance audit 2012"),
        ),
        CaseRule(
            "subramaniam-balaji",
            "S. Subramaniam Balaji",
            2013,
            (
                "S. Subramaniam Balaji v. State of Tamil Nadu",
                "S. Subramaniam Balaji",
            ),
            "S. Subramaniam Balaji v. State of Tamil Nadu, Supreme Court judgment",
            _ik_search("S Subramaniam Balaji State of Tamil Nadu 2013 CAG"),
        ),
        CaseRule(
            "arun-kumar-agrawal",
            "Arun Kumar Agrawal",
            2013,
            ("Arun Kumar Agrawal v. Union of India", "Arun Kumar Agrawal"),
            "Arun Kumar Agrawal v. Union of India, Supreme Court judgment",
            _ik_search("Arun Kumar Agrawal Union of India CAG report 2013"),
        ),
        CaseRule(
            "telecom-service-providers",
            "Association of Unified Telecom Service Providers of India v. Union of India",
            2014,
            (
                "Association of Unified Telecom Service Providers of India v. Union of India",
            ),
            "Association of Unified Telecom Service Providers of India v. Union of India, judgment dated 17 April 2014",
            "https://indiankanoon.org/doc/112886265/",
        ),
        CaseRule(
            "brijeshwar-singh-chahal",
            "State of Punjab v. Brijeshwar Singh Chahal",
            2016,
            (
                "State of Punjab v. Brijeshwar Singh Chahal",
                "Brijeshwar Singh Chahal",
            ),
            "State of Punjab v. Brijeshwar Singh Chahal, Supreme Court judgment",
            "https://api.sci.gov.in/jonew/bosir/orderpdf/2812218.pdf",
        ),
        CaseRule(
            "paramjit-kaur",
            "Paramjit Kaur v. State of Punjab",
            1999,
            ("Paramjit Kaur v. State of Punjab", "Paramjit Kaur"),
            "Paramjit Kaur v. State of Punjab, Supreme Court judgment",
            _ik_search("Paramjit Kaur State of Punjab NHRC 1999"),
        ),
        CaseRule(
            "nc-dhoundial",
            "N.C. Dhoundial v. Union of India",
            2003,
            (
                "N.C. Dhoundial v. Union of India",
                "N.C. Dhoundial",
                "Dhoundial",
            ),
            "N.C. Dhoundial v. Union of India, judgment dated 4 December 2003",
            "https://api.sci.gov.in/jonew/judis/25688.pdf",
        ),
        CaseRule(
            "eevfam",
            "EEVFAM",
            2016,
            (
                "Extra Judicial Execution Victim Families Association v. Union of India",
                "Extra Judicial Execution Victim Families Association",
                "EEVFAM",
            ),
            "Extra Judicial Execution Victim Families Association v. Union of India, judgment dated 8 July 2016",
            "https://api.sci.gov.in/jonew/judis/43775.pdf",
        ),
        CaseRule(
            "raj-narain",
            "State of U.P. v. Raj Narain",
            1975,
            ("State of U.P. v. Raj Narain", "Raj Narain"),
            "State of U.P. v. Raj Narain, Supreme Court judgment",
            _ik_search("State of UP v Raj Narain 24 January 1975"),
        ),
        CaseRule(
            "sp-gupta",
            "S.P. Gupta v. Union of India",
            1981,
            ("S.P. Gupta v. Union of India", "S.P. Gupta"),
            "S.P. Gupta v. Union of India, Supreme Court judgment",
            _ik_search("S P Gupta v Union of India 30 December 1981"),
        ),
        CaseRule(
            "cbse-aditya-bandopadhyay",
            "CBSE v. Aditya Bandopadhyay",
            2011,
            ("CBSE v. Aditya Bandopadhyay", "Aditya Bandopadhyay"),
            "CBSE v. Aditya Bandopadhyay, Supreme Court judgment",
            "https://api.sci.gov.in/jonew/judis/38344.pdf",
        ),
        CaseRule(
            "cic-state-manipur",
            "Chief Information Commissioner v. State of Manipur",
            2011,
            (
                "Chief Information Commissioner v. State of Manipur",
                "CIC v. State of Manipur",
                "State of Manipur",
            ),
            "Chief Information Commissioner v. State of Manipur, Supreme Court judgment",
            "https://api.sci.gov.in/jonew/judis/38918.pdf",
        ),
        CaseRule(
            "rbi-jayantilal-mistry",
            "RBI v. Jayantilal N. Mistry",
            2015,
            (
                "RBI v. Jayantilal N. Mistry",
                "Reserve Bank of India v. Jayantilal N. Mistry",
                "Jayantilal N. Mistry",
            ),
            "RBI v. Jayantilal N. Mistry, Supreme Court judgment",
            "https://api.sci.gov.in/jonew/judis/43192.pdf",
        ),
        CaseRule(
            "subhash-chandra-agarwal",
            "Subhash Chandra Agarwal",
            2019,
            (
                "CPIO, Supreme Court of India v. Subhash Chandra Agarwal",
                "CPIO v. Subhash Chandra Agarwal",
                "Subhash Chandra Agarwal",
            ),
            "CPIO, Supreme Court of India v. Subhash Chandra Agarwal, judgment dated 13 November 2019",
            "https://api.sci.gov.in/supremecourt/2009/36624/36624_2009_1_1502_18247_Judgement_13-Nov-2019.pdf",
        ),
        CaseRule(
            "anjali-bhardwaj",
            "Anjali Bhardwaj v. Union of India",
            2019,
            ("Anjali Bhardwaj v. Union of India", "Anjali Bhardwaj"),
            "Anjali Bhardwaj v. Union of India, judgment dated 15 February 2019",
            "https://api.sci.gov.in/supremecourt/2018/15968/15968_2018_Judgement_15-Feb-2019.pdf",
        ),
        CaseRule(
            "kazi-lhendup-dorji",
            "Kazi Lhendup Dorji v. CBI",
            1994,
            ("Kazi Lhendup Dorji v. CBI", "Kazi Lhendup Dorji"),
            "Kazi Lhendup Dorji v. CBI, Supreme Court judgment",
            _ik_search("Kazi Lhendup Dorji v CBI 1994"),
        ),
        CaseRule(
            "vineet-narain",
            "Vineet Narain v. Union of India",
            1997,
            ("Vineet Narain v. Union of India", "Vineet Narain"),
            "Vineet Narain v. Union of India, Supreme Court judgment",
            _ik_search("Vineet Narain v Union of India 18 December 1997"),
        ),
        CaseRule(
            "cpdr-west-bengal",
            "State of West Bengal v. Committee for Protection of Democratic Rights",
            2010,
            (
                "State of West Bengal v. Committee for Protection of Democratic Rights",
                "Committee for Protection of Democratic Rights",
                "CPDR",
            ),
            "State of West Bengal v. Committee for Protection of Democratic Rights, Constitution Bench judgment",
            _ik_search("State of West Bengal Committee for Protection of Democratic Rights 2010"),
        ),
        CaseRule(
            "alok-kumar-verma",
            "Alok Kumar Verma v. Union of India",
            2019,
            ("Alok Kumar Verma v. Union of India", "Alok Kumar Verma"),
            "Alok Kumar Verma v. Union of India, Supreme Court judgment",
            _ik_search("Alok Kumar Verma v Union of India 8 January 2019"),
        ),
        CaseRule(
            "fertico-marketing",
            "Fertico Marketing and Investment Pvt. Ltd. v. CBI",
            2020,
            (
                "Fertico Marketing and Investment Pvt. Ltd. v. CBI",
                "Fertico Marketing",
                "Fertico",
            ),
            "Fertico Marketing and Investment Pvt. Ltd. v. CBI, Supreme Court judgment",
            _ik_search("Fertico Marketing Investment Pvt Ltd v CBI 2020"),
        ),
        CaseRule(
            "thommandru-vijayalakshmi",
            "CBI v. Thommandru Hannah Vijayalakshmi",
            2021,
            (
                "CBI v. Thommandru Hannah Vijayalakshmi",
                "Thommandru Hannah Vijayalakshmi",
                "Thommandru",
            ),
            "CBI v. Thommandru Hannah Vijayalakshmi, Supreme Court judgment",
            _ik_search("CBI v Thommandru Hannah Vijayalakshmi 2021"),
        ),
        CaseRule(
            "jaya-thakur",
            "Dr Jaya Thakur v. Union of India",
            2023,
            ("Dr Jaya Thakur v. Union of India", "Dr Jaya Thakur", "Jaya Thakur"),
            "Dr Jaya Thakur v. Union of India, Supreme Court judgment",
            _ik_search("Dr Jaya Thakur v Union of India 2023 INSC 616"),
        ),
        CaseRule(
            "west-bengal-union-2024",
            "State of West Bengal v. Union of India",
            2024,
            (
                "State of West Bengal v. Union of India",
                "West Bengal v. Union",
            ),
            "State of West Bengal v. Union of India, 2024 INSC 502",
            _ik_search("State of West Bengal v Union of India 2024 INSC 502"),
        ),
        CaseRule(
            "sadiq-ali",
            "Sadiq Ali v. Election Commission of India",
            1972,
            ("Sadiq Ali v. Election Commission of India", "Sadiq Ali"),
            "Sadiq Ali v. Election Commission of India, Supreme Court decision reported in 1972",
            _ik_search("Sadiq Ali Election Commission of India 1972"),
        ),
        CaseRule(
            "inc-institute-social-welfare",
            "Indian National Congress v. Institute of Social Welfare",
            2002,
            (
                "Indian National Congress v. Institute of Social Welfare",
                "Indian National Congress v Institute of Social Welfare",
            ),
            "Indian National Congress (I) v. Institute of Social Welfare, Supreme Court judgment dated 10 May 2002",
            _ik_search("Indian National Congress Institute of Social Welfare 10 May 2002"),
        ),
        CaseRule(
            "adr-electoral-bonds",
            "Association for Democratic Reforms v. Union of India",
            2024,
            (
                "Association for Democratic Reforms v. Union of India",
                "ADR electoral bonds",
            ),
            "Association for Democratic Reforms v. Union of India, electoral-bonds judgment dated 15 February 2024",
            _ik_search("Association for Democratic Reforms Union of India electoral bonds 15 February 2024"),
        ),
        CaseRule(
            "lily-thomas",
            "Lily Thomas v. Union of India",
            2013,
            ("Lily Thomas v. Union of India", "Lily Thomas"),
            "Lily Thomas v. Union of India, Supreme Court judgment dated 10 July 2013",
            _ik_search("Lily Thomas Union of India 10 July 2013"),
        ),
        CaseRule(
            "rambabu-singh-thakur",
            "Rambabu Singh Thakur v. Sunil Arora",
            2020,
            ("Rambabu Singh Thakur v. Sunil Arora", "Rambabu Singh Thakur"),
            "Rambabu Singh Thakur v. Sunil Arora, Supreme Court order dated 13 February 2020",
            _ik_search("Rambabu Singh Thakur Sunil Arora 13 February 2020"),
        ),
        CaseRule(
            "damyanti-naranga",
            "Damyanti Naranga v. Union of India",
            1971,
            (
                "Damyanti Naranga v. Union of India",
                "Damayanti Naranga",
                "Damyanti Naranga",
            ),
            "Damyanti Naranga v. Union of India, Supreme Court judgment dated 6 May 1971",
            _ik_search("Damyanti Naranga Union of India 6 May 1971"),
        ),
        CaseRule(
            "ramlila-maidan",
            "Ramlila Maidan Incident",
            2012,
            ("Ramlila Maidan Incident", "Ramlila Maidan"),
            "In Re: Ramlila Maidan Incident, Supreme Court judgment dated 23 February 2012",
            _ik_search("Ramlila Maidan Incident 23 February 2012"),
        ),
        CaseRule(
            "mkss-protest",
            "Mazdoor Kisan Shakti Sangathan v. Union of India",
            2018,
            (
                "Mazdoor Kisan Shakti Sangathan v. Union of India",
                "Mazdoor Kisan Shakti Sangathan",
            ),
            "Mazdoor Kisan Shakti Sangathan v. Union of India, Supreme Court judgment dated 23 July 2018",
            _ik_search("Mazdoor Kisan Shakti Sangathan Union of India 23 July 2018"),
        ),
        CaseRule(
            "amit-sahni",
            "Amit Sahni v. Commissioner of Police",
            2020,
            ("Amit Sahni v. Commissioner of Police", "Amit Sahni"),
            "Amit Sahni v. Commissioner of Police, Supreme Court judgment dated 7 October 2020",
            _ik_search("Amit Sahni Commissioner of Police 7 October 2020"),
        ),
        CaseRule(
            "noel-harper",
            "Noel Harper v. Union of India",
            2022,
            ("Noel Harper v. Union of India", "Noel Harper"),
            "Noel Harper v. Union of India, Supreme Court judgment dated 8 April 2022",
            _ik_search("Noel Harper Union of India 8 April 2022"),
        ),
        CaseRule(
            "jolly-george",
            "Jolly George Varghese v. Bank of Cochin",
            1980,
            ("Jolly George Varghese v. Bank of Cochin", "Jolly George Varghese"),
            "Jolly George Varghese v. Bank of Cochin, Supreme Court judgment dated 4 February 1980",
            _ik_search("Jolly George Varghese Bank of Cochin 4 February 1980"),
        ),
        CaseRule(
            "gramophone-company",
            "Gramophone Company of India v. Birendra Bahadur Pandey",
            1984,
            (
                "Gramophone Company of India v. Birendra Bahadur Pandey",
                "Gramophone Company",
            ),
            "Gramophone Company of India Ltd. v. Birendra Bahadur Pandey, Supreme Court judgment dated 21 February 1984",
            _ik_search("Gramophone Company Birendra Bahadur Pandey 21 February 1984"),
        ),
        CaseRule(
            "r-gandhi",
            "Union of India v. R. Gandhi",
            2010,
            ("Union of India v. R. Gandhi", "R. Gandhi"),
            "Union of India v. R. Gandhi, President, Madras Bar Association, Supreme Court judgment dated 11 May 2010",
            _ik_search("Union of India R Gandhi Madras Bar Association 11 May 2010"),
        ),
        CaseRule(
            "madras-bar-ntt",
            "Madras Bar Association NTT",
            2014,
            ("Madras Bar Association NTT",),
            "Madras Bar Association v. Union of India, National Tax Tribunal judgment dated 25 September 2014",
            _ik_search("Madras Bar Association National Tax Tribunal 25 September 2014"),
        ),
        CaseRule(
            "madras-bar-iv",
            "Madras Bar Association IV",
            2020,
            ("Madras Bar Association IV",),
            "Madras Bar Association v. Union of India, tribunal-rules judgment dated 27 November 2020",
            _ik_search("Madras Bar Association tribunal rules 27 November 2020"),
        ),
        CaseRule(
            "madras-bar-v",
            "Madras Bar Association V",
            2021,
            ("Madras Bar Association V",),
            "Madras Bar Association v. Union of India, Tribunal Reforms Ordinance judgment dated 14 July 2021",
            _ik_search("Madras Bar Association Tribunal Reforms Ordinance 14 July 2021"),
        ),
        CaseRule(
            "madras-bar-2025",
            "Madras Bar Association tribunal reforms",
            2025,
            ("Madras Bar Association tribunal reforms",),
            "Madras Bar Association tribunal-reforms judgment reported as 2025 INSC 1330, dated 19 November 2025",
            _ik_search("Madras Bar Association 2025 INSC 1330 19 November 2025"),
        ),
        CaseRule(
            "delhi-laws-act",
            "In re Delhi Laws Act",
            1951,
            ("In re Delhi Laws Act", "Delhi Laws Act"),
            "In re Delhi Laws Act, 1912, Supreme Court decision dated 23 May 1951",
            _ik_search("In re Delhi Laws Act 23 May 1951"),
        ),
        CaseRule(
            "ak-kraipak",
            "A.K. Kraipak v. Union of India",
            1969,
            ("A.K. Kraipak v. Union of India", "A.K. Kraipak", "Kraipak"),
            "A.K. Kraipak v. Union of India, Supreme Court judgment dated 29 April 1969",
            _ik_search("A K Kraipak Union of India 29 April 1969"),
        ),
        CaseRule(
            "sn-mukherjee",
            "S.N. Mukherjee v. Union of India",
            1990,
            ("S.N. Mukherjee v. Union of India", "S.N. Mukherjee"),
            "S.N. Mukherjee v. Union of India, Supreme Court judgment dated 28 August 1990",
            _ik_search("S N Mukherjee Union of India 28 August 1990"),
        ),
        CaseRule(
            "cci-sail",
            "Competition Commission of India v. SAIL",
            2010,
            (
                "Competition Commission of India v. SAIL",
                "CCI v. SAIL",
                "CCI v SAIL",
            ),
            "Competition Commission of India v. Steel Authority of India Ltd., Supreme Court judgment dated 9 September 2010",
            _ik_search("Competition Commission India SAIL 9 September 2010"),
        ),
        CaseRule(
            "cellular-operators-trai",
            "Cellular Operators Association of India v. TRAI",
            2016,
            (
                "Cellular Operators Association of India v. TRAI",
                "Cellular Operators Association v. TRAI",
            ),
            "Cellular Operators Association of India v. TRAI, Supreme Court judgment dated 11 May 2016",
            _ik_search("Cellular Operators Association India TRAI 11 May 2016"),
        ),
        CaseRule(
            "navtej-singh-johar",
            "Navtej Singh Johar v. Union of India",
            2018,
            ("Navtej Singh Johar v. Union of India", "Navtej Singh Johar", "Navtej"),
            "Navtej Singh Johar v. Union of India, Supreme Court judgment dated 6 September 2018",
            _ik_search("Navtej Singh Johar Union of India 6 September 2018"),
        ),
        CaseRule(
            "p-and-o-steam-navigation",
            "P & O Steam Navigation",
            1861,
            (
                "P & O Steam Navigation Co. v. Secretary of State",
                "P & O Steam Navigation",
                "P&O Steam Navigation",
            ),
            "Peninsular and Oriental Steam Navigation Co. v. Secretary of State for India, Calcutta Supreme Court decision of 1861",
            _ik_search("Peninsular Oriental Steam Navigation Secretary State 1861"),
        ),
        CaseRule(
            "vidyawati",
            "State of Rajasthan v. Vidyawati",
            1962,
            ("State of Rajasthan v. Vidyawati", "Vidyawati"),
            "State of Rajasthan v. Vidyawati, Supreme Court judgment dated 2 February 1962",
            _ik_search("State Rajasthan Vidyawati 2 February 1962"),
        ),
        CaseRule(
            "kasturi-lal",
            "Kasturi Lal v. State of Uttar Pradesh",
            1964,
            (
                "Kasturi Lal v. State of Uttar Pradesh",
                "Kasturi Lal Ralia Ram Jain",
                "Kasturi Lal",
            ),
            "Kasturi Lal Ralia Ram Jain v. State of Uttar Pradesh, Supreme Court judgment dated 29 September 1964",
            _ik_search("Kasturi Lal Ralia Ram Jain 29 September 1964"),
        ),
        CaseRule(
            "bk-mondal",
            "B.K. Mondal & Sons",
            1961,
            (
                "State of West Bengal v. B.K. Mondal & Sons",
                "B.K. Mondal & Sons",
                "B.K. Mondal",
            ),
            "State of West Bengal v. B.K. Mondal & Sons, Supreme Court judgment dated 5 December 1961",
            _ik_search("State West Bengal B K Mondal Sons 5 December 1961"),
        ),
        CaseRule(
            "mulamchand",
            "Mulamchand v. State of Madhya Pradesh",
            1968,
            ("Mulamchand v. State of Madhya Pradesh", "Mulamchand"),
            "Mulamchand v. State of Madhya Pradesh, Supreme Court judgment dated 8 March 1968",
            _ik_search("Mulamchand State Madhya Pradesh 8 March 1968"),
        ),
        CaseRule(
            "nagendra-rao",
            "N. Nagendra Rao & Co.",
            1994,
            (
                "N. Nagendra Rao & Co. v. State of Andhra Pradesh",
                "N. Nagendra Rao & Co.",
                "N. Nagendra Rao",
            ),
            "N. Nagendra Rao & Co. v. State of Andhra Pradesh, Supreme Court judgment dated 6 September 1994",
            _ik_search("N Nagendra Rao State Andhra Pradesh 6 September 1994"),
        ),
        CaseRule(
            "nilabati-behera",
            "Nilabati Behera v. State of Orissa",
            1993,
            ("Nilabati Behera v. State of Orissa", "Nilabati Behera"),
            "Nilabati Behera v. State of Orissa, Supreme Court judgment dated 24 March 1993",
            _ik_search("Nilabati Behera State Orissa 24 March 1993"),
        ),
        CaseRule(
            "rudul-sah",
            "Rudul Sah v. State of Bihar",
            1983,
            ("Rudul Sah v. State of Bihar", "Rudul Sah"),
            "Rudul Sah v. State of Bihar, Supreme Court judgment dated 1 August 1983",
            _ik_search("Rudul Sah State Bihar 1 August 1983"),
        ),
        CaseRule(
            "challa-ramkrishna-reddy",
            "State of Andhra Pradesh v. Challa Ramkrishna Reddy",
            2000,
            (
                "State of Andhra Pradesh v. Challa Ramkrishna Reddy",
                "Challa Ramkrishna Reddy",
            ),
            "State of Andhra Pradesh v. Challa Ramkrishna Reddy, Supreme Court judgment dated 26 April 2000",
            _ik_search("Challa Ramkrishna Reddy 26 April 2000"),
        ),
        CaseRule(
            "ev-chinnaiah",
            "E.V. Chinnaiah v. State of Andhra Pradesh",
            2004,
            ("E.V. Chinnaiah v. State of Andhra Pradesh", "E.V. Chinnaiah"),
            "E.V. Chinnaiah v. State of Andhra Pradesh, Supreme Court judgment dated 5 November 2004",
            _ik_search("E V Chinnaiah State Andhra Pradesh 5 November 2004"),
        ),
        CaseRule(
            "jalour-singh",
            "State of Punjab v. Jalour Singh",
            2008,
            ("State of Punjab v. Jalour Singh", "Jalour Singh"),
            "State of Punjab v. Jalour Singh, Supreme Court judgment dated 18 January 2008",
            _ik_search("State Punjab Jalour Singh 18 January 2008"),
        ),
        CaseRule(
            "afcons-infrastructure",
            "Afcons Infrastructure v. Cherian Varkey Construction",
            2010,
            (
                "Afcons Infrastructure v. Cherian Varkey Construction",
                "Afcons Infrastructure",
            ),
            "Afcons Infrastructure Ltd. v. Cherian Varkey Construction Co., Supreme Court judgment dated 26 July 2010",
            _ik_search("Afcons Infrastructure Cherian Varkey 26 July 2010"),
        ),
        CaseRule(
            "interglobe-aviation",
            "InterGlobe Aviation v. N. Satchidanand",
            2011,
            ("InterGlobe Aviation v. N. Satchidanand", "InterGlobe Aviation"),
            "InterGlobe Aviation Ltd. v. N. Satchidanand, Supreme Court judgment dated 4 July 2011",
            _ik_search("InterGlobe Aviation Satchidanand 4 July 2011"),
        ),
        CaseRule(
            "bar-council-pla",
            "Bar Council of India v. Union of India",
            2012,
            ("Bar Council of India v. Union of India",),
            "Bar Council of India v. Union of India, Supreme Court judgment dated 28 August 2012",
            _ik_search("Bar Council India Union India Permanent Lok Adalat 28 August 2012"),
        ),
        CaseRule(
            "patil-automation",
            "Patil Automation v. Rakheja Engineers",
            2022,
            ("Patil Automation v. Rakheja Engineers", "Patil Automation"),
            "Patil Automation Pvt. Ltd. v. Rakheja Engineers Pvt. Ltd., Supreme Court judgment dated 17 August 2022",
            _ik_search("Patil Automation Rakheja Engineers 17 August 2022"),
        ),
        CaseRule(
            "canara-bank-jayarama",
            "Canara Bank v. G.S. Jayarama",
            2022,
            ("Canara Bank v. G.S. Jayarama", "Canara Bank v. G.S. Jayarama Shetty"),
            "Canara Bank v. G.S. Jayarama, Supreme Court judgment dated 19 May 2022",
            _ik_search("Canara Bank G S Jayarama Permanent Lok Adalat 19 May 2022"),
        ),
        CaseRule(
            "rmd-union",
            "R.M.D. Chamarbaugwala v. Union of India",
            1957,
            ("R.M.D. Chamarbaugwala v. Union of India",),
            "R.M.D. Chamarbaugwala v. Union of India, Supreme Court judgment dated 9 April 1957",
            _ik_search("R M D Chamarbaugwala Union of India 9 April 1957"),
        ),
        CaseRule(
            "bhikaji-narain",
            "Bhikaji Narain Dhakras",
            1955,
            ("Bhikaji Narain Dhakras", "Bhikaji Narain"),
            "Bhikaji Narain Dhakras v. State of Madhya Pradesh, Supreme Court judgment dated 29 September 1955",
            _ik_search("Bhikaji Narain Dhakras 29 September 1955"),
        ),
        CaseRule(
            "basheshar-nath",
            "Basheshar Nath",
            1958,
            ("Basheshar Nath v. CIT", "Basheshar Nath"),
            "Basheshar Nath v. Commissioner of Income Tax, Supreme Court judgment dated 19 November 1958",
            _ik_search("Basheshar Nath Commissioner Income Tax 1959"),
        ),
        CaseRule(
            "prafulla-kumar",
            "Prafulla Kumar Mukherjee",
            1947,
            (
                "Prafulla Kumar Mukherjee v. Bank of Commerce",
                "Prafulla Kumar Mukherjee",
            ),
            "Prafulla Kumar Mukherjee v. Bank of Commerce, Privy Council decision of 1947",
            _ik_search("Prafulla Kumar Mukherjee Bank of Commerce 1947"),
        ),
        CaseRule(
            "fn-balsara",
            "State of Bombay v. F.N. Balsara",
            1951,
            ("State of Bombay v. F.N. Balsara", "F.N. Balsara"),
            "State of Bombay v. F.N. Balsara, Supreme Court judgment dated 25 May 1951",
            _ik_search("State Bombay F N Balsara 25 May 1951"),
        ),
        CaseRule(
            "kc-gajapati",
            "K.C. Gajapati Narayan Deo",
            1953,
            (
                "K.C. Gajapati Narayan Deo v. State of Orissa",
                "K.C. Gajapati Narayan Deo",
            ),
            "K.C. Gajapati Narayan Deo v. State of Orissa, Supreme Court judgment dated 30 January 1953",
            _ik_search("K C Gajapati Narayan Deo 30 January 1953"),
        ),
        CaseRule(
            "rmd-state-bombay",
            "State of Bombay v. R.M.D. Chamarbaugwala",
            1957,
            ("State of Bombay v. R.M.D. Chamarbaugwala",),
            "State of Bombay v. R.M.D. Chamarbaugwala, Supreme Court judgment dated 4 April 1957",
            _ik_search("State Bombay R M D Chamarbaugwala 4 April 1957"),
        ),
        CaseRule(
            "deep-chand",
            "Deep Chand v. State of Uttar Pradesh",
            1959,
            ("Deep Chand v. State of Uttar Pradesh", "Deep Chand"),
            "Deep Chand v. State of Uttar Pradesh, Supreme Court judgment dated 15 January 1959",
            _ik_search("Deep Chand State Uttar Pradesh 15 January 1959"),
        ),
        CaseRule(
            "m-karunanidhi",
            "M. Karunanidhi v. Union of India",
            1979,
            ("M. Karunanidhi v. Union of India", "M. Karunanidhi"),
            "M. Karunanidhi v. Union of India, Supreme Court judgment dated 8 May 1979",
            _ik_search("M Karunanidhi Union India 8 May 1979"),
        ),
        CaseRule(
            "kerala-education-bill",
            "In re Kerala Education Bill",
            1958,
            ("In re Kerala Education Bill", "Kerala Education Bill"),
            "In re Kerala Education Bill, Supreme Court advisory opinion dated 22 May 1958",
            _ik_search("In re Kerala Education Bill 22 May 1958"),
        ),
        CaseRule(
            "ram-krishna-dalmia",
            "Ram Krishna Dalmia",
            1958,
            (
                "Ram Krishna Dalmia v. Justice S.R. Tendolkar",
                "Ram Krishna Dalmia",
            ),
            "Ram Krishna Dalmia v. Justice S.R. Tendolkar, Supreme Court judgment dated 28 March 1958",
            _ik_search("Ram Krishna Dalmia Justice Tendolkar 28 March 1958"),
        ),
        CaseRule(
            "shayara-bano",
            "Shayara Bano v. Union of India",
            2017,
            ("Shayara Bano v. Union of India", "Shayara Bano"),
            "Shayara Bano v. Union of India, Supreme Court judgment dated 22 August 2017",
            _ik_search("Shayara Bano Union India 22 August 2017"),
        ),
        CaseRule(
            "modern-dental-college",
            "Modern Dental College",
            2016,
            (
                "Modern Dental College v. State of Madhya Pradesh",
                "Modern Dental College",
            ),
            "Modern Dental College and Research Centre v. State of Madhya Pradesh, Supreme Court judgment dated 2 May 2016",
            _ik_search("Modern Dental College Madhya Pradesh 2 May 2016"),
        ),
        CaseRule(
            "shirur-mutt",
            "Shirur Mutt",
            1954,
            (
                "Commissioner, Hindu Religious Endowments v. Sri Lakshmindra Thirtha Swamiar of Shirur Mutt",
                "Shirur Mutt",
            ),
            "Commissioner, Hindu Religious Endowments v. Shirur Mutt, Supreme Court judgment dated 16 April 1954",
            _ik_search("Shirur Mutt 16 April 1954"),
        ),
        CaseRule(
            "indian-young-lawyers",
            "Indian Young Lawyers Association",
            2018,
            (
                "Indian Young Lawyers Association v. State of Kerala",
                "Indian Young Lawyers Association",
            ),
            "Indian Young Lawyers Association v. State of Kerala, Supreme Court judgment dated 28 September 2018",
            _ik_search("Indian Young Lawyers Association 28 September 2018"),
        ),
        CaseRule(
            "navjyoti-cooperative",
            "Navjyoti Cooperative Group Housing",
            1992,
            (
                "Navjyoti Cooperative Group Housing Society v. Union of India",
                "Navjyoti Cooperative Group Housing",
            ),
            "Navjyoti Cooperative Group Housing Society v. Union of India, Supreme Court judgment dated 17 December 1992",
            _ik_search("Navjyoti Cooperative Group Housing 17 December 1992"),
        ),
        CaseRule(
            "motilal-padampat",
            "Motilal Padampat Sugar Mills",
            1978,
            (
                "Motilal Padampat Sugar Mills v. State of Uttar Pradesh",
                "Motilal Padampat Sugar Mills",
            ),
            "Motilal Padampat Sugar Mills v. State of Uttar Pradesh, Supreme Court judgment dated 12 December 1978",
            _ik_search("Motilal Padampat Sugar Mills State Uttar Pradesh 1979"),
        ),
        CaseRule(
            "padma-sundara-rao",
            "Padma Sundara Rao",
            2002,
            (
                "Padma Sundara Rao v. State of Tamil Nadu",
                "Padma Sundara Rao",
            ),
            "Padma Sundara Rao v. State of Tamil Nadu, Supreme Court judgment dated 13 March 2002",
            _ik_search("Padma Sundara Rao Tamil Nadu 13 March 2002"),
        ),
    )
}


TOPIC_CASE_IDS: dict[str, tuple[str, ...]] = {
    "polity-01": (),
    "polity-02": (),
    "polity-03": ("minerva-mills", "article-370", "rajendra-n-shah"),
    "polity-04": (
        "berubari-union",
        "kesavananda-bharati",
        "lic-consumer-education",
        "ds-nakara",
        "gb-pant-university",
        "excel-wear",
    ),
    "polity-05": ("berubari-union", "maganbhai"),
    "polity-06": ("section-6a",),
    "polity-07": (
        "pradeep-kumar-biswas",
        "kesavananda-bharati",
        "ep-royappa",
        "maneka-gandhi",
        "champakam-dorairajan",
        "indra-sawhney",
        "m-nagaraj",
        "jarnail-singh",
        "janhit-abhiyan",
        "davinder-singh",
        "shreya-singhal",
        "anuradha-bhasin",
        "kedar-nath-singh",
        "ak-gopalan",
        "rc-cooper",
        "puttaswamy-privacy",
        "ir-coelho",
        "minerva-mills",
        "property-owners",
        "vishaka",
    ),
    "polity-08": (
        "champakam-dorairajan",
        "golaknath",
        "kesavananda-bharati",
        "minerva-mills",
        "property-owners",
    ),
    "polity-09": ("bijoe-emmanuel", "naveen-jindal", "shyam-narayan-chouksey"),
    "polity-10": (
        "shankari-prasad",
        "sajjan-singh",
        "golaknath",
        "kesavananda-bharati",
        "indira-gandhi",
        "minerva-mills",
        "waman-rao",
        "ir-coelho",
        "anjum-kadari",
    ),
    "polity-11": (),
    "polity-12": (
        "kesavananda-bharati",
        "sr-bommai",
        "state-of-rajasthan",
        "mohit-minerals",
    ),
    "polity-13": (),
    "polity-14": (
        "adm-jabalpur",
        "puttaswamy-privacy",
        "sr-bommai",
        "rameshwar-prasad",
    ),
    "polity-15": (
        "shamsher-singh",
        "dc-wadhwa",
        "krishna-kumar-singh",
        "kehar-singh",
        "maru-ram",
    ),
    "polity-16": ("shamsher-singh", "sr-chaudhuri"),
    "polity-17": ("sita-soren", "puttaswamy-aadhaar", "rojer-mathew"),
    "polity-18": (
        "first-judges-case",
        "second-judges-case",
        "third-judges-case",
        "fourth-judges-case",
        "kesavananda-bharati",
        "minerva-mills",
        "ir-coelho",
        "l-chandra-kumar",
        "supreme-court-bar-association",
        "rupa-ashok-hurra",
        "hussainara-khatoon",
        "vishaka",
        "state-tamil-nadu-governor",
        "assent-advisory-opinion",
    ),
    "polity-19": (
        "shamsher-singh",
        "sr-bommai",
        "rameshwar-prasad",
        "nabam-rebia",
        "subhash-desai",
        "dc-wadhwa",
        "krishna-kumar-singh",
        "state-tamil-nadu-governor",
        "assent-advisory-opinion",
    ),
    "polity-20": (
        "kihoto-hollohan",
        "raja-ram-pal",
        "sita-soren",
        "nabam-rebia",
        "state-tamil-nadu-governor",
        "assent-advisory-opinion",
    ),
    "polity-21": (
        "first-judges-case",
        "second-judges-case",
        "third-judges-case",
        "fourth-judges-case",
        "sankalchand-sheth",
        "l-chandra-kumar",
        "chandra-mohan",
    ),
    "polity-22": ("article-370", "sampat-prakash"),
    "polity-23": (
        "kishansing-tomar",
        "k-krishna-murthy",
        "vikas-gawali",
        "fouziya-imtiaz-shaikh",
    ),
    "polity-24": (
        "kishansing-tomar",
        "k-krishna-murthy",
        "vikas-gawali",
        "fouziya-imtiaz-shaikh",
    ),
    "polity-25": (
        "gnctd-aid-advice",
        "gnctd-services",
        "k-lakshminarayanan",
        "article-370",
    ),
    "polity-26": ("samatha", "orissa-mining-corporation"),
    "polity-27": (
        "mohinder-singh-gill",
        "ac-jose",
        "tn-seshan",
        "adr-candidate-disclosure",
        "pucl-nota",
        "anoop-baranwal",
        "adr-vvpat",
    ),
    "polity-28": (
        "manbodhan-lal-srivastava",
        "ashok-kumar-yadav",
        "shankarsan-dash",
        "mv-thimmaiah",
        "k-manjusree",
        "tej-prakash-pathak",
    ),
    "polity-29": ("bhim-singh-article-282", "mohit-minerals"),
    "polity-30": ("mohit-minerals",),
    "polity-31": (
        "indra-sawhney",
        "jaishri-laxmanrao-patil",
        "davinder-singh",
    ),
    "polity-32": (
        "arvind-gupta-cag",
        "subramaniam-balaji",
        "arun-kumar-agrawal",
        "telecom-service-providers",
    ),
    "polity-33": ("brijeshwar-singh-chahal",),
    "polity-34": (),
    "polity-35": ("paramjit-kaur", "nc-dhoundial", "eevfam"),
    "polity-36": (
        "raj-narain",
        "sp-gupta",
        "cbse-aditya-bandopadhyay",
        "cic-state-manipur",
        "rbi-jayantilal-mistry",
        "subhash-chandra-agarwal",
        "anjali-bhardwaj",
    ),
    "polity-37": (
        "kazi-lhendup-dorji",
        "vineet-narain",
        "cpdr-west-bengal",
        "alok-kumar-verma",
        "fertico-marketing",
        "thommandru-vijayalakshmi",
        "jaya-thakur",
        "west-bengal-union-2024",
    ),
    "polity-38": (
        "common-cause-lokpal",
        "lok-prahari",
        "sita-soren",
    ),
    "polity-39": (
        "rajendra-n-shah",
        "thalappalam",
    ),
    "polity-40": (
        "gujarat-university-language",
        "dav-college-language",
        "karnataka-english-medium",
    ),
    "polity-41": (
        "parshotam-lal-dhingra",
        "khem-chand",
        "shamsher-singh",
        "tulsiram-patel",
        "ecil-karunakar",
        "tsr-subramanian",
        "l-chandra-kumar",
    ),
    "polity-42": (
        "kihoto-hollohan",
        "ravi-s-naik",
        "shrimanth-balasaheb-patil",
        "keisham-meghachandra",
        "nabam-rebia",
        "subhash-desai",
    ),
    "polity-43": (
        "sadiq-ali",
        "inc-institute-social-welfare",
        "adr-candidate-disclosure",
        "adr-electoral-bonds",
        "lily-thomas",
        "rambabu-singh-thakur",
        "pucl-nota",
    ),
    "polity-44": (
        "damyanti-naranga",
        "ramlila-maidan",
        "mkss-protest",
        "amit-sahni",
        "noel-harper",
    ),
    "polity-45": (
        "berubari-union",
        "maganbhai",
        "jolly-george",
        "gramophone-company",
        "vishaka",
        "section-6a",
        "sr-bommai",
    ),
    "polity-46": (
        "l-chandra-kumar",
        "r-gandhi",
        "madras-bar-ntt",
        "madras-bar-iv",
        "madras-bar-v",
        "rojer-mathew",
        "madras-bar-2025",
    ),
    "polity-47": (
        "kesavananda-bharati",
        "minerva-mills",
        "maneka-gandhi",
        "ir-coelho",
        "sr-bommai",
        "first-judges-case",
        "second-judges-case",
        "third-judges-case",
        "fourth-judges-case",
    ),
    "polity-48": (),
    "polity-49": (
        "delhi-laws-act",
        "ak-kraipak",
        "maneka-gandhi",
        "sn-mukherjee",
        "cci-sail",
        "cellular-operators-trai",
        "l-chandra-kumar",
    ),
    "polity-50": (
        "kesavananda-bharati",
        "minerva-mills",
        "maneka-gandhi",
        "sr-bommai",
        "puttaswamy-privacy",
        "navtej-singh-johar",
    ),
    "polity-51": (
        "p-and-o-steam-navigation",
        "vidyawati",
        "kasturi-lal",
        "bk-mondal",
        "mulamchand",
        "nagendra-rao",
        "nilabati-behera",
        "rudul-sah",
        "challa-ramkrishna-reddy",
    ),
    "polity-52": (
        "kesavananda-bharati",
        "minerva-mills",
        "sr-bommai",
        "puttaswamy-privacy",
        "navtej-singh-johar",
    ),
    "polity-53": (
        "m-nagaraj",
        "jarnail-singh",
        "jaishri-laxmanrao-patil",
        "ev-chinnaiah",
        "davinder-singh",
    ),
    "polity-54": (
        "hussainara-khatoon",
        "jalour-singh",
        "afcons-infrastructure",
        "interglobe-aviation",
        "bar-council-pla",
        "patil-automation",
        "canara-bank-jayarama",
    ),
    "polity-55": (
        "rmd-union",
        "bhikaji-narain",
        "basheshar-nath",
        "prafulla-kumar",
        "fn-balsara",
        "kc-gajapati",
        "rmd-state-bombay",
        "deep-chand",
        "m-karunanidhi",
        "kerala-education-bill",
        "kedar-nath-singh",
        "golaknath",
        "kesavananda-bharati",
        "minerva-mills",
        "ram-krishna-dalmia",
        "ep-royappa",
        "shayara-bano",
        "modern-dental-college",
        "puttaswamy-privacy",
        "anuradha-bhasin",
        "navtej-singh-johar",
        "shirur-mutt",
        "indian-young-lawyers",
        "shamsher-singh",
        "navjyoti-cooperative",
        "motilal-padampat",
        "padma-sundara-rao",
        "supreme-court-bar-association",
    ),
}


ASCII_CASE_IDS: dict[str, tuple[str, ...]] = {
    key: tuple(
        case_id
        for case_id in case_ids
        if case_id
        not in {
            "article-370",
            "rajendra-n-shah",
            "ds-nakara",
            "gb-pant-university",
            "excel-wear",
            "vishaka",
            "puttaswamy-aadhaar",
            "rojer-mathew",
        }
    )
    for key, case_ids in TOPIC_CASE_IDS.items()
}

GRAPHICAL_CASE_IDS: dict[str, tuple[str, ...]] = {
    key: tuple(
        case_id
        for case_id in case_ids
        if not (key == "polity-12" and case_id == "state-of-rajasthan")
    )
    for key, case_ids in TOPIC_CASE_IDS.items()
}


def case_label(case_id: str, *, uppercase: bool = False) -> str:
    rule = CASES[case_id]
    canonical = rule.canonical.upper() if uppercase else rule.canonical
    return f"{canonical} ({rule.year})"


def _literal_pattern(value: str) -> str:
    return re.escape(value).replace(r"\ ", r"\s+")


def _case_pattern(rule: CaseRule) -> re.Pattern[str]:
    aliases = "|".join(
        _literal_pattern(alias)
        for alias in sorted(rule.aliases, key=len, reverse=True)
    )
    return re.compile(
        rf"(?<![\w])"
        rf"(?:(?P<prefix>{YEAR_RE})\s+)?"
        rf"(?P<label>{aliases})"
        rf"(?P<suffix>"
        rf"(?:\s*,\s*{YEAR_RE}|\s+\(?{YEAR_RE}\)?|\s*\({YEAR_RE}\))"
        rf")?"
        rf"(?![\w])",
        re.IGNORECASE,
    )


def _upper_style(value: str) -> bool:
    letters = "".join(character for character in value if character.isalpha())
    return bool(letters) and letters.isupper()


def normalize_text(
    topic_key: str,
    text: str,
    *,
    changes: list[dict[str, Any]] | None = None,
    field: str = "",
) -> str:
    result = text
    if topic_key == "polity-03":
        article_370_after = (
            "[FACT — CURRENT LINK] J&K: till 2019 J&K had its own Constitution "
            "(Article 370); In Re: Article 370 of the Constitution (2023) upheld "
            "the 2019 changes"
        )

        def replace_article_370(match: re.Match[str]) -> str:
            if changes is not None and match.group(0) != article_370_after:
                changes.append(
                    {
                        "case_id": "article-370",
                        "before": match.group(0),
                        "after": article_370_after,
                        "field": field,
                    }
                )
            return article_370_after

        result = re.sub(
            r"\[FACT\s*[—-]\s*CURRENT LINK]\s*J&K:\s*\[FACT]\s*note\s*[—-]\s*"
            r"till 2019 J&K had its own constitution \(Art 370\);\s*"
            r"abolished 2019;\s*SC upheld",
            replace_article_370,
            result,
            flags=re.IGNORECASE,
        )
    if topic_key == "polity-06":
        section_6a_after = "IN RE: SECTION 6A (2024) — 17 OCTOBER"

        def replace_section_6a(match: re.Match[str]) -> str:
            if changes is not None and match.group(0) != section_6a_after:
                changes.append(
                    {
                        "case_id": "section-6a",
                        "before": match.group(0),
                        "after": section_6a_after,
                        "field": field,
                    }
                )
            return section_6a_after

        result = re.sub(
            r"(?:IN RE:\s*)?SECTION 6A,\s*17 OCT(?:OBER)? 2024",
            replace_section_6a,
            result,
            flags=re.IGNORECASE,
        )
    for case_id in TOPIC_CASE_IDS.get(topic_key, ()):
        rule = CASES[case_id]
        pattern = _case_pattern(rule)

        def replace(match: re.Match[str]) -> str:
            before = match.group(0)
            matched_year = re.search(
                YEAR_RE,
                (match.group("prefix") or "") + (match.group("suffix") or ""),
            )
            if (
                "\n" in before
                and matched_year
                and int(matched_year.group(0)) == rule.year
            ):
                return before
            after = case_label(
                case_id,
                uppercase=_upper_style(match.group("label")),
            )
            if changes is not None and before != after:
                changes.append(
                    {
                        "case_id": case_id,
                        "before": before,
                        "after": after,
                        "field": field,
                    }
                )
            return after

        result = pattern.sub(replace, result)
    return result


def _wrap_changed_line(before: str, after: str) -> list[str]:
    if before == after or len(after) <= MAX_ASCII_WIDTH:
        return [after]
    indentation = re.match(r"\s*", after).group(0)
    content = after[len(indentation) :]
    return textwrap.wrap(
        content,
        width=96 - len(indentation),
        initial_indent=indentation,
        subsequent_indent=indentation + "  ",
        break_long_words=False,
        break_on_hyphens=False,
        replace_whitespace=False,
        drop_whitespace=True,
    )


def normalize_ascii_body(
    topic_key: str,
    body: str,
    *,
    changes: list[dict[str, Any]] | None = None,
    field: str = "",
) -> str:
    output: list[str] = []
    for line_number, line in enumerate(body.splitlines(), 1):
        normalized = normalize_text(
            topic_key,
            line,
            changes=changes,
            field=f"{field}:line-{line_number}",
        )
        output.extend(_wrap_changed_line(line, normalized))
    return "\n".join(output)


def normalize_ascii_document(
    data: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, list[dict[str, Any]]]]:
    normalized = copy.deepcopy(data)
    changes: dict[str, list[dict[str, Any]]] = {}
    raw_topics = normalized.get("topics")
    if isinstance(raw_topics, dict):
        topic_items: Iterable[tuple[str, Any]] = raw_topics.items()
    elif isinstance(raw_topics, list):
        topic_items = (
            (str(item.get("topic_key") or ""), item)
            for item in raw_topics
            if isinstance(item, dict)
        )
    else:
        return normalized, changes
    for mapping_key, topic in topic_items:
        if not isinstance(topic, dict):
            continue
        topic_key = str(topic.get("topic_key") or mapping_key)
        if topic_key not in TOPIC_CASE_IDS:
            continue
        topic_changes: list[dict[str, Any]] = []
        for index, panel in enumerate(topic.get("panels") or [], 1):
            if not isinstance(panel, dict):
                continue
            if isinstance(panel.get("title"), str):
                panel["title"] = normalize_text(
                    topic_key,
                    panel["title"],
                    changes=topic_changes,
                    field=f"panel-{index}:title",
                )
            for body_key in ("ascii_text", "full_text"):
                if isinstance(panel.get(body_key), str):
                    panel[body_key] = normalize_ascii_body(
                        topic_key,
                        panel[body_key],
                        changes=topic_changes,
                        field=f"panel-{index}:{body_key}",
                    )
        if topic_changes:
            changes[topic_key] = topic_changes
    return normalized, changes


def _normalize_renderable_graphical_value(
    topic_key: str,
    value: Any,
    *,
    changes: list[dict[str, Any]],
    field: str,
) -> Any:
    if isinstance(value, str):
        return normalize_text(
            topic_key,
            value,
            changes=changes,
            field=field,
        )
    if isinstance(value, list):
        return [
            _normalize_renderable_graphical_value(
                topic_key,
                item,
                changes=changes,
                field=f"{field}[{index}]",
            )
            for index, item in enumerate(value)
        ]
    if isinstance(value, dict):
        output: dict[str, Any] = {}
        for key, item in value.items():
            if key in {"source_references"}:
                output[key] = item
            else:
                output[key] = _normalize_renderable_graphical_value(
                    topic_key,
                    item,
                    changes=changes,
                    field=f"{field}.{key}" if field else key,
                )
        return output
    return value


def normalize_graphical_spec(
    spec: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    topic_key = str(spec.get("topic_key") or "")
    changes: list[dict[str, Any]] = []
    normalized = _normalize_renderable_graphical_value(
        topic_key,
        copy.deepcopy(spec),
        changes=changes,
        field="",
    )
    stages = normalized.get("stages")
    if isinstance(stages, list):
        extra = next(
            (
                stage
                for stage in stages
                if isinstance(stage, dict) and stage.get("role") == "extra"
            ),
            None,
        )
        if isinstance(extra, dict) and topic_key == "polity-04":
            groups = extra.get("groups")
            if isinstance(groups, list) and len(groups) >= 3:
                items = groups[2].get("items")
                if (
                    isinstance(items, list)
                    and len(items) >= 2
                    and str(items[0]).strip().casefold() == "g.b."
                ):
                    changes.append(
                        {
                            "case_id": "gb-pant-university",
                            "before": "G.B. / Pant University (2000)",
                            "after": case_label("gb-pant-university"),
                            "field": "stages[E].groups[2].items",
                        }
                    )
                    items[0] = case_label("gb-pant-university")
                    items[1] = re.sub(
                        r"^(?:G\.B\.\s+)?Pant University\s*\(2000\)\s*",
                        "",
                        str(items[1]),
                        flags=re.IGNORECASE,
                    )
        if isinstance(extra, dict) and topic_key == "polity-17":
            groups = extra.get("groups")
            if isinstance(groups, list) and len(groups) >= 3:
                items = groups[2].get("items")
                if isinstance(items, list) and len(items) >= 3:
                    if str(items[1]).strip().casefold().startswith("rojer mathew"):
                        changes.append(
                            {
                                "case_id": "rojer-mathew",
                                "before": (
                                    "Rojer Mathew v. / South Indian Bank (2019)"
                                ),
                                "after": case_label("rojer-mathew"),
                                "field": "stages[E].groups[2].items",
                            }
                        )
                        items[1] = (
                            f"{case_label('rojer-mathew')}, the Court doubted the "
                            "earlier Article 110 reasoning"
                        )
                        items[2] = re.sub(
                            r"^South Indian Bank\s*\(2019\),\s*",
                            "",
                            str(items[2]),
                            flags=re.IGNORECASE,
                        )
    return normalized, changes


def _iter_renderable_graphical_strings(spec: dict[str, Any]) -> Iterable[str]:
    for key in ("title", "short_route", "reading_note"):
        value = spec.get(key)
        if isinstance(value, str):
            yield value
    stages = spec.get("stages")
    if not isinstance(stages, list):
        return
    for stage in stages:
        if not isinstance(stage, dict):
            continue
        for key, value in stage.items():
            if key == "source_references":
                continue
            if isinstance(value, str):
                yield value
            elif isinstance(value, (dict, list)):
                yield from _iter_strings(value)


def _iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            if key != "source_references":
                yield from _iter_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_strings(item)


def _expected_label_present(text: str, case_id: str) -> bool:
    rule = CASES[case_id]
    return bool(
        re.search(
            _literal_pattern(rule.canonical)
            + rf"\s*\({rule.year}\)",
            text,
            re.IGNORECASE,
        )
    )


def _common_errors(topic_key: str, text: str, expected: Iterable[str]) -> list[str]:
    errors: list[str] = []
    if re.search(rf"\(({YEAR_RE})\)\s*\(\1\)", text):
        errors.append(f"{topic_key}: duplicate parenthesized case year")
    renormalized = normalize_text(topic_key, text)
    if renormalized != text:
        errors.append(f"{topic_key}: known case label is not normalized with its year")
    for case_id in expected:
        if not _expected_label_present(text, case_id):
            errors.append(
                f"{topic_key}: missing {case_label(case_id)}"
            )
    return errors


def ascii_topic_errors(topic_key: str, title_and_body: str) -> list[str]:
    errors = _common_errors(
        topic_key,
        title_and_body,
        ASCII_CASE_IDS.get(topic_key, ()),
    )
    for number, line in enumerate(title_and_body.splitlines(), 1):
        if len(line) > MAX_ASCII_WIDTH:
            errors.append(
                f"{topic_key}: ASCII line {number} exceeds {MAX_ASCII_WIDTH} characters"
            )
    if topic_key == "polity-06" and not re.search(
        r"IN RE:\s*SECTION 6A\s*\(2024\)\s*—\s*17 OCTOBER",
        title_and_body,
        re.IGNORECASE,
    ):
        errors.append("polity-06: Section 6A judgment date is not explicit")
    return errors


def graphical_spec_errors(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key") or "")
    if topic_key not in TOPIC_CASE_IDS:
        return []
    text = "\n".join(_iter_renderable_graphical_strings(spec))
    errors = _common_errors(
        topic_key,
        text,
        GRAPHICAL_CASE_IDS.get(topic_key, ()),
    )
    if topic_key == "polity-06" and not re.search(
        r"IN RE:\s*SECTION 6A\s*\(2024\)\s*—\s*17 OCTOBER",
        text,
        re.IGNORECASE,
    ):
        errors.append("polity-06: Section 6A graphical judgment date is not explicit")
    if topic_key == "polity-09":
        if "2023 Jallikattu ruling" not in text or "2014" not in text:
            errors.append("polity-09: dated Jallikattu comparison is incomplete")
    if topic_key == "polity-12" and "2024 West Bengal ruling" not in text:
        errors.append("polity-12: dated West Bengal ruling reference is incomplete")
    return errors


def source_record(case_id: str) -> dict[str, Any]:
    rule = CASES[case_id]
    return {
        "case_id": case_id,
        "canonical_label": case_label(case_id),
        "decision_year": rule.year,
        "source_title": rule.source_title,
        "source_url": rule.source_url,
    }


def distinct_case_ids(topic_keys: Iterable[str]) -> list[str]:
    return sorted(
        {
            case_id
            for topic_key in topic_keys
            for case_id in TOPIC_CASE_IDS.get(topic_key, ())
        }
    )
