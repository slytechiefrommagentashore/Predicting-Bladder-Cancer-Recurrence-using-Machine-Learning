import pandas as pd

# Load folder names and normalize the ID column
folder_df = pd.read_excel('folder_names.xlsx')
valid_ids = folder_df['case_submitter_id'].astype(str).str.strip().unique()

# Load the clinical Excel file
clinical_xlsx = pd.ExcelFile('cleaned_clinical_details.xlsx')
sheet_names = clinical_xlsx.sheet_names

# Store cleaned sheets
cleaned_sheets = {}

for sheet in sheet_names:
    df = clinical_xlsx.parse(sheet)
    
    # Normalize column names: lowercase + strip spaces
    df.columns = df.columns.str.lower().str.strip()
    
    if 'case_submitter_id' in df.columns:
        # Normalize the data for comparison
        df['case_submitter_id'] = df['case_submitter_id'].astype(str).str.strip()
        
        # Filter only matching case_submitter_id
        filtered_df = df[df['case_submitter_id'].isin(valid_ids)].copy()
        
        cleaned_sheets[sheet] = filtered_df
        print(f"✅ {sheet}: {len(filtered_df)} rows kept")
    else:
        cleaned_sheets[sheet] = df
        print(f"⚠️ {sheet}: 'case_submitter_id' not found")

# Save the result
with pd.ExcelWriter('cleaned_clinical_details_filtered.xlsx', engine='openpyxl') as writer:
    for sheet, data in cleaned_sheets.items():
        data.to_excel(writer, sheet_name=sheet, index=False)

print("🎯 Done! Filtered Excel saved as 'cleaned_clinical_details_filtered.xlsx'")
