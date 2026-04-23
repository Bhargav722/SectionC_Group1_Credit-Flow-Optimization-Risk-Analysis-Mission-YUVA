# Data Cleaning Dictionary

This document summarizes the cleaning steps applied to the dataset in `notebooks/02_cleaning.ipynb`.

## 1. Initial Data Load
- Load the extracted dataset from `../data/interim/01_extraction.csv`.
- Print the initial shape and total number of missing values.

## 2. Remove Duplicates
- Drop duplicate rows from the dataset.
- Log the updated shape and missing value count.

## 3. Standardize Categorical Columns
- Clean `Gender`:
  - Strip whitespace and normalize capitalization.
  - Keep values `Male`, `Female`, `Other`; all other values become `Unknown`.
- Clean `Repayment_Status`:
  - Map a variety of labels like `late`, `Delayed`, `ONTIME`, and `On-time` to standardized values: `Late`, `On-Time`, `Default`.
  - Set unmapped values to `Unknown`.
- Clean other text fields:
  - `Sector`, `Residential Type`, `Enterprise Type`, `Specially Abled Type`, and `IFSC Code`.
  - Strip whitespace, normalize capitalization, and fill missing values with `Unknown`.
  - For `Residential Type`, restrict values to `Urban` and `Rural`; otherwise use `Unknown`.

## 4. Parse Currency Fields
- Convert the mixed-unit currency columns into numeric INR fields:
  - `Loan Amount (Mixed Units)` → `Loan_Amount_INR`
  - `Project Cost (Mixed Units)` → `Project_Cost_INR`
- Currency parsing rules:
  - Remove commas, currency symbols, and extra spaces.
  - Convert values like `k INR` into actual numbers (e.g. `20k INR` → `20000`).
  - If parsing fails, set the value to missing (`NaN`).
- Drop the original mixed-unit columns after conversion.

## 5. Convert Dates
- Convert `Application Date` to a proper datetime column.
- If conversion fails, the value becomes missing.
- Due to excessive missing values, drop the `Application Date` column entirely.

## 6. Impute Missing Numeric Values
- Use median imputation for the following columns:
  - `Loan_Amount_INR`
  - `Applicant_Monthly_Income`
  - `Risk_Score`
  - `Loan_Tenure_Months`
  - `Total_TAT_Days`
  - `Project_Cost_INR`
  - `Days_to_BHD_Verification`
  - `Days_to_SBDU_Verification`
  - `Days_to_DLIC_Approval`
  - `Days_to_Bank_Sanction`
  - `Days_to_Disbursement`
  - `Interest_Rate_%`
  - `EMI_Amount`
  - `EMI_to_Income_Ratio`
  - `Credit_Eligibility_Score`

## 7. Cap Outliers
- Apply an IQR-based cap to the same numeric columns used for imputation.
- Clip values outside the range `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]`.
- In addition, clip `Risk_Score` to the valid range `0` to `100`.

## 8. Save Cleaned Data
- Save the cleaned dataset to `../data/interim/02_cleaning.csv`.
- Log the final shape and total number of missing values.

## Notes
- The cleaning process focuses on preparing the dataset for analysis by removing duplicates, standardizing categories, converting currency fields, handling missing values, and reducing extreme outliers.
- This document is a high-level summary of the cleaning steps performed in the notebook.
