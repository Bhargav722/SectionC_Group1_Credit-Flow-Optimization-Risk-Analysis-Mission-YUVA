# NST DVA Capstone 2 - Project Repository

> **Newton School of Technology | Data Visualization & Analytics**
> A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

---

## Before You Start

1. Rename the repository using the format `SectionName_TeamID_ProjectName`.
2. Fill in the project details and team table below.
3. Add the raw dataset to `data/raw/`.
4. Complete the notebooks in order from `01` to `05`.
5. Publish the final dashboard and add the public link in `tableau/dashboard_links.md`.
6. Export the final report and presentation as PDFs into `reports/`.

### Quick Start

If you are working locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

If you are working in Google Colab:

- Upload or sync the notebooks from `notebooks/`
- Keep the final `.ipynb` files committed to GitHub
- Export any cleaned datasets into `data/processed/`

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Mission Yuva – Loan & Financial Analysis |
| **Sector** | Finance / Government Lending (J&K Youth Entrepreneurship) |
| **Team ID** | _To be filled by team_ |
| **Section** | _To be filled by team_ |
| **Faculty Mentor** | _To be filled by team_ |
| **Institute** | Newton School of Technology |
| **Submission Date** | _To be filled by team_ |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Bhargav Patil | [GitHub](https://github.com/Bhargav722) / [Portfolio](https://bhargav722.github.io/dva-portfolio/) |
| Data Lead | Hardik Hathwal | [GitHub](https://github.com/Kidrah-kun) |
| ETL Lead | Sibtain Ahmed Qureshi | [GitHub](https://github.com/Sibtain28) |
| Analysis Lead | Sibtain Ahmed Qureshi, Kabir Sharma | [Sibtain](https://github.com/Sibtain28), [Kabir](https://github.com/Kabir-glitch) |
| Visualization Lead | Bhargav Patil, Sibtain Ahmed Qureshi, Bhawana | [Bhargav](https://github.com/Bhargav722), [Sibtain](https://github.com/Sibtain28), [Bhawana](https://github.com/bhawanaydv) |
| Strategy Lead | Bhargav Patil | [GitHub](https://github.com/Bhargav722) |
| PPT and Quality Lead | Kabir, Rohan, Hardik | [Kabir](https://github.com/Kabir-glitch) |

---

## Business Problem

Mission Yuva is a government-backed youth entrepreneurship lending initiative operating across five districts of Jammu & Kashmir — Doda, Pulwama, Reasi, Samba, and Shopian. The scheme disburses loans across eight sectors (Agriculture, Healthcare, IT, Manufacturing, Retail, Services, Tourism) to young entrepreneurs, including women, rural applicants, and specially-abled individuals. Despite its scale, loan disbursement efficiency, repayment performance, and financial inclusion metrics require rigorous monitoring to ensure the programme achieves its socioeconomic goals.

**Core Business Question**

> Which districts and sectors exhibit the highest default risk, and how can loan appraisal and disbursement processes be optimised to improve repayment outcomes and inclusivity across Mission Yuva?

**Decision Supported**

> Programme administrators can use this analysis to prioritise risk-mitigation interventions by district and sector, streamline turnaround time, and target financial inclusion outreach to under-represented applicant groups.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Mission Yuva Government Loan Dataset |
| **Direct Access Link** | _Paste the direct download or access URL_ |
| **Row Count** | > 5,000 (2,610 verified applications in sample view) |
| **Column Count** | > 8 meaningful columns |
| **Time Period Covered** | _To be filled by team_ |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| Application ID | Unique loan application identifier | Primary key / count metric |
| District Name | One of five J&K districts (Doda, Pulwama, Reasi, Samba, Shopian) | Segmentation / geographic filter |
| Sector | Business sector of the applicant enterprise | Segmentation / KPI breakdown |
| Loan Amount INR | Sanctioned loan amount in Indian Rupees | KPI computation (Total Loan, Avg Loan) |
| Project Cost INR | Estimated project cost submitted by applicant | Correlation analysis (Loan vs Project Cost) |
| Repayment Status | On-Time / Late / Default / Unknown | KPI computation (Default Rate, Late Payments) |
| Risk Score | Applicant creditworthiness score (0–100) | KPI (Avg Risk Score), Risk Distribution |
| Gender | Female / Male / Other / Unknown | Inclusion analysis, Risk Score by Gender |
| Residential Type | Rural / Urban / Unknown | Inclusion KPI (Rural Count) |
| Enterprise Type | Existing Enterprise / MSME Sunrise Sector / Nano Entrepreneur / Unknown | Enterprise mix analysis |
| Specially Abled Type | Hearing / Locomotor / Multiple / Visual / Unknown | Inclusion KPI (Specially Abled Count) |
| Days to BHD Verification | TAT stage metric | Pipeline efficiency analysis |
| Days to SBDU Verification | TAT stage metric | Pipeline efficiency analysis |
| Days to DLIC Approval | TAT stage metric | Pipeline efficiency analysis |
| Days to Bank Sanction | TAT stage metric | Pipeline efficiency analysis |
| Days to Disbursement | TAT stage metric | Pipeline efficiency analysis |
| Monthly Income INR | Applicant's reported monthly income | Loan affordability / EMI ratio computation |
| EMI Amount INR | Estimated monthly EMI | KPI (Avg EMI Ratio) |
| Credit Score | Bureau credit score | KPI (Avg Credit Score) |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| KPI-1 Total Applications | Total number of loan applications received | `COUNT(Application ID)` → **2,610** |
| KPI-2 Total Loan Amount | Aggregate loan amount sanctioned across all applications | `SUM(Loan Amount INR)` → **₹546 Cr** |
| KPI-3 Avg Risk Score | Mean applicant risk score across all applications | `AVG(Risk Score)` → **51** |
| KPI-4 Avg TAT | Average total turnaround time from application to disbursement | `AVG(Days to BHD Verif. + Days to SBDU Verif. + Days to DLIC Approval + Days to Bank Sanction + Days to Disbursement)` → **188 days** |
| KPI-5 Late Payments Count | Number of applications with a Late repayment status | `COUNT(Application ID) WHERE Repayment Status = 'Late'` → **863** |
| KPI-6 Avg Credit Score | Mean credit bureau score across all applicants | `AVG(Credit Score)` → **50** |
| KPI-7 Total Defaulted Loans | Total loan amount associated with defaulted applications | `SUM(Loan Amount INR) WHERE Repayment Status = 'Default'` → **₹82 Cr** |
| KPI-8 Female Applicants | Count of female applicants | `COUNT(Application ID) WHERE Gender = 'Female'` → **2,610** |
| KPI-9 Specially Abled Count | Count of applicants with any specially-abled classification | `COUNT(Application ID) WHERE Specially Abled Type ≠ NULL` → **1,501** |
| KPI-10 Rural Count | Count of applicants with Rural residential type | `COUNT(Application ID) WHERE Residential Type = 'Rural'` → **2,610** |
| KPI-11 Avg EMI Ratio | Average ratio of EMI to monthly income (affordability indicator) | `AVG(EMI Amount INR / Monthly Income INR)` → **0.30** |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | 'https://public.tableau.com/views/Capstone2_17769441478690/Dasboard-4-LoanFinancialDeep-Dive?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link' |
| **Dashboard 1 – Loan Overview** | Top-level KPIs (Total Applications, Total Loan, Avg Risk Score, Avg TAT), Sector Breakdown heatmap by gender, Risk Score Distribution, TAT Analysis by district, District Overview loan amounts |
| **Dashboard 2 – Repayment & Risk** | Late Payments, Avg Credit Score, Total Defaulted Loans KPIs; Repayment by District, Default Rate by Sector, Repayment Status Split, Avg Risk Score by Gender & District heatmap |
| **Dashboard 3 – Applicant Profile & Inclusion** | Female Applicants, Specially Abled, Rural Count KPIs; Gender × Residential stacked bar, Specially Abled Breakdown pie, Enterprise Type by district, Sector × Enterprise type matrix |
| **Dashboard 4 – Loan & Financial Deep-Dive** | Avg EMI Ratio KPI; Loan Distribution histogram, Loan vs Project Cost scatter, Risk Score by Sector box plots, Avg Loan Amount by District, Income by Gender distribution |
| **Main Filters** | Sector, District Name, Gender, Residential Type, Enterprise Type, Repayment Status |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

1. **Total loan disbursement stands at ₹546 Cr across 2,610 applications**, with Doda district receiving the highest average loan amounts, suggesting it is the primary beneficiary district.
2. **The average turnaround time is 188 days**, indicating significant pipeline delays across verification and approval stages — Pulwama shows the widest TAT spread among districts.
3. **₹82 Cr (15% of total disbursement) is at default risk**, with Tourism and Healthcare sectors exhibiting the highest default rates (above 15%), requiring immediate risk monitoring.
4. **863 applications (33% of total) are in late repayment status**, concentrated across Doda and Pulwama, signalling localised repayment stress.
5. **Average credit score is 50 and average risk score is 51**, both around the midpoint scale, suggesting the applicant pool has moderate and relatively uniform credit risk — differentiation is sector- and district-driven.
6. **1,501 specially-abled applicants (57.5% of total) were served**, with Locomotor (350) and Visual (395) categories being most represented, demonstrating strong inclusion outreach.
7. **Nano Entrepreneur enterprise type dominates across most sectors**, particularly in IT and Services, while Retail has the highest share of Existing Enterprises — pointing to different maturity profiles by sector.
8. **Avg EMI Ratio of 0.30 indicates moderate affordability pressure**, with income distribution peaking in the ₹60K–₹70K monthly range, suggesting most borrowers are at or near recommended EMI-to-income thresholds.
9. **Loan amount closely tracks project cost in a near-linear relationship**, confirming that lending decisions are project-cost-driven with limited over- or under-financing.
10. **Risk score distributions are broadly similar across sectors**, but Agri and Tourism show the widest inter-quartile spread, implying greater applicant heterogeneity in these sectors.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Tourism and Healthcare have default rates above 15% | Introduce sector-specific post-disbursement monitoring and mandatory quarterly check-ins for Tourism and Healthcare loans above ₹10L | Reduce default rate by 3–5 percentage points within 12 months |
| 2 | Average TAT of 188 days creates pipeline bottlenecks | Digitise and parallel-process BHD and SBDU verification stages; set SLA targets of ≤ 30 days per stage | Reduce total TAT to under 120 days, improving applicant experience and reducing dropout |
| 3 | 863 late-payment applications concentrated in Doda and Pulwama | Deploy district-level loan counsellors and SMS-based repayment reminder campaigns in Doda and Pulwama | Reduce late-payment count by 20–25% within two repayment cycles |
| 4 | Avg EMI Ratio of 0.30 is near the 33% affordability ceiling | Cap loan sanctioning for applicants with projected EMI Ratio > 0.35; offer restructured repayment schedules for existing high-ratio borrowers | Reduce future default probability by pre-empting affordability stress |
| 5 | Nano Entrepreneurs dominate IT and Services but receive relatively smaller average loans | Design a dedicated Nano Entrepreneur loan tier with faster approval, lower documentation burden, and mentorship linkage | Increase formalisation and repayment rates among the fastest-growing enterprise segment |

---

## Repository Structure

```text
SectionName_TeamID_ProjectName/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- README.md
|   |-- project_report_template.md
|   `-- presentation_outline.md
|
|-- docs/
|   `-- data_dictionary.md
|
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and optionally `scripts/etl_pipeline.py`.
4. **Analyze** - EDA and statistical analysis performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - 3-5 data-backed business recommendations delivered.
7. **Report** - Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |
| SQL | Optional | Initial data extraction only, if documented |

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

---

## Evaluation Rubric

| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

> Marks are awarded for analytical thinking and decision relevance, not chart quantity, visual decoration, or code length.

---

## Submission Checklist

**GitHub Repository**

- [ ] Public repository created with the correct naming convention (`SectionName_TeamID_ProjectName`)
- [ ] All notebooks committed in `.ipynb` format
- [ ] `data/raw/` contains the original, unedited dataset
- [ ] `data/processed/` contains the cleaned pipeline output
- [ ] `tableau/screenshots/` contains dashboard screenshots
- [ ] `tableau/dashboard_links.md` contains the Tableau Public URL
- [ ] `docs/data_dictionary.md` is complete
- [ ] `README.md` explains the project, dataset, and team
- [ ] All members have visible commits and pull requests

**Tableau Dashboard**

- [ ] Published on Tableau Public and accessible via public URL
- [ ] At least one interactive filter included
- [ ] Dashboard directly addresses the business problem

**Project Report**

- [ ] Final report exported as PDF into `reports/`
- [ ] Cover page, executive summary, sector context, problem statement
- [ ] Data description, cleaning methodology, KPI framework
- [ ] EDA with written insights, statistical analysis results
- [ ] Dashboard screenshots and explanation
- [ ] 8-12 key insights in decision language
- [ ] 3-5 actionable recommendations with impact estimates
- [ ] Contribution matrix matches GitHub history

**Presentation Deck**

- [ ] Final presentation exported as PDF into `reports/`
- [ ] Title slide through recommendations, impact, limitations, and next steps

**Individual Assets**

- [x] DVA-oriented resume updated to include this capstone
- [x] Portfolio link or project case study added

---

## Contribution Matrix

This table must match evidence in GitHub Insights, PR history, and committed files.

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| Bhargav Patil | Support | Support | Owner | Owner | Owner | Owner | Support |
| Hardik Hathwal | Owner | Support | Support | Support | Support | Support | Owner |
| Sibtain Ahmed Qureshi | Support | Owner | Owner | Owner | Owner | Owner | Support |
| Kabir Sharma | Support | Support | Owner | Support | Support | Support | Owner |
| Bhawana | Support | Support | Support | Support | Owner | Support | Support |
| Rohan | Support | Support | Support | Support | Support | Owner | Owner |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Bhargav Patil

**Date:** _______________

---

## Academic Integrity

All analysis, code, and recommendations in this repository must be the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*
