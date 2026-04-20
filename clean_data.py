import pandas as pd
import numpy as np
import re


#  Load Dataset

INPUT_FILE  = "data/raw/mission_yuva_credit_flow.csv"
OUTPUT_FILE = "clean/cleaned_mission_yuva.csv"

df = pd.read_csv(INPUT_FILE)
print(f"✅ STEP 0 — Loaded dataset: {df.shape[0]} rows × {df.shape[1]} columns")



# Select 8 Most Meaningful Columns

cols = [
    'Application ID',           # Unique identifier
    'District Name',            # Geographic dimension
    'Gender',                   # Demographic
    'Sector',                   # Loan sector
    'Loan Amount (Mixed Units)',# Core financial metric (needs cleaning)
    'Applicant_Monthly_Income', # Repayment capacity
    'Risk_Score',               # Creditworthiness
    'Repayment_Status'          # Target / outcome variable
]

df = df[cols].copy()
print(f"✅ STEP 1 — Columns reduced to 8: {list(df.columns)}")



#  Remove Duplicates

before = len(df)
df = df.drop_duplicates()
print(f"✅ STEP 2 — Duplicates removed: {before - len(df)} | Rows remaining: {len(df)}")



# Standardise Gender
#   Raw values: 'male', 'Male', 'Female', 'FEMALE', 'Other', NaN
#   Clean to  : 'Male', 'Female', 'Other', 'Unknown'

df['Gender'] = df['Gender'].str.strip().str.title()
df['Gender'] = df['Gender'].where(
    df['Gender'].isin(['Male', 'Female', 'Other']),
    other='Unknown'
)
print(f"✅ STEP 3 — Gender standardised | Unique values: {df['Gender'].unique().tolist()}")



#  Standardise Repayment_Status
#   Raw values: 'late', 'Delayed', 'ONTIME', 'On-time', 'Default', NaN
#   Clean to  : 'Late', 'On-Time', 'Default', 'Unknown'

status_map = {
    'late'    : 'Late',
    'Late'    : 'Late',
    'Delayed' : 'Late',
    'ONTIME'  : 'On-Time',
    'On-time' : 'On-Time',
    'Default' : 'Default'
}
df['Repayment_Status'] = df['Repayment_Status'].map(status_map).fillna('Unknown')
print(f"✅ STEP 4 — Repayment_Status standardised | Unique: {df['Repayment_Status'].unique().tolist()}")



# Standardise Sector


df['Sector'] = df['Sector'].str.strip().str.title().fillna('Unknown')
print(f"✅ STEP 5 — Sector standardised | Missing after fill: {df['Sector'].isnull().sum()}")



# Clean Loan Amount → unified numeric INR


def parse_loan_amount(val):
    """Convert mixed-format loan strings to a single float (INR)."""
    if pd.isna(val):
        return np.nan
    val = str(val).strip().replace(',', '')
    val = val.replace('₹', '').replace('$', '').strip()

    # Handle "k INR" notation e.g. "3029k INR" → 3,029,000
    if re.search(r'k\s*inr', val, re.IGNORECASE):
        num = re.sub(r'[^\d.]', '', val)
        return float(num) * 1000 if num else np.nan

    try:
        return float(val)
    except ValueError:
        return np.nan

df['Loan_Amount_INR'] = df['Loan Amount (Mixed Units)'].apply(parse_loan_amount)
df = df.drop(columns=['Loan Amount (Mixed Units)'])
print(f"✅ STEP 6 — Loan Amount parsed to INR | Missing: {df['Loan_Amount_INR'].isnull().sum()}")



# Handle Missing Values (Median Imputation)


df['Loan_Amount_INR']         = df['Loan_Amount_INR'].fillna(df['Loan_Amount_INR'].median())
df['Applicant_Monthly_Income']= df['Applicant_Monthly_Income'].fillna(df['Applicant_Monthly_Income'].median())
df['Risk_Score']              = df['Risk_Score'].fillna(df['Risk_Score'].median())

print(f"✅ STEP 7 — Missing values after imputation:")
print(df.isnull().sum().to_string())



# Outlier Detection & Capping (IQR Method)


def cap_iqr_outliers(series: pd.Series) -> pd.Series:
    """Cap outliers using the IQR method."""
    Q1  = series.quantile(0.25)
    Q3  = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    capped = ((series < lower) | (series > upper)).sum()
    print(f"   → {series.name}: bounds [{lower:.2f}, {upper:.2f}] | {capped} values capped")
    return series.clip(lower=lower, upper=upper)

print("✅ STEP 8 — Outlier capping (IQR):")
df['Loan_Amount_INR']          = cap_iqr_outliers(df['Loan_Amount_INR'])
df['Applicant_Monthly_Income'] = cap_iqr_outliers(df['Applicant_Monthly_Income'])
# Risk score has a logical range [0, 100]
df['Risk_Score'] = df['Risk_Score'].clip(0, 100)
print(f"   → Risk_Score: clipped to logical range [0, 100]")



# Rename Columns & Fix Data Types

df = df.rename(columns={
    'Application ID'         : 'Application_ID',
    'District Name'          : 'District_Name',
    'Applicant_Monthly_Income': 'Monthly_Income_INR'
})

df['Application_ID']    = df['Application_ID'].astype(int)
df['Monthly_Income_INR']= df['Monthly_Income_INR'].round(2)
df['Loan_Amount_INR']   = df['Loan_Amount_INR'].round(2)
df['Risk_Score']        = df['Risk_Score'].round(2)

print(f"✅ STEP 9 — Columns renamed & types fixed")
print(df.dtypes.to_string())



# Save Cleaned Dataset

df.to_csv(OUTPUT_FILE, index=False)

print(f"\n{'='*55}")
print(f"  ✅ Cleaning Complete!")
print(f"  Final shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"  Missing vals: {df.isnull().sum().sum()}")
print(f"  Saved to    : {OUTPUT_FILE}")
print(f"{'='*55}")
print("\nPreview:")
print(df.head(5).to_string(index=False))