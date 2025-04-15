import pandas as pd

# Load all sheets from the original Excel file
xls = pd.ExcelFile('EP_data_SFU.xlsx')
sheets = ['SFU 2013 - 2024', 'UBC 2013 - 2024', 'SFU 2024 Data', 'UBC']

# Create a new Excel writer to save the cleaned sheets
with pd.ExcelWriter('EP_data_SFU_cleaned.xlsx') as writer:
    for sheet in sheets:
        df = pd.read_excel('EP_data_SFU.xlsx', sheet_name=sheet)
        
        # Only filter if GPA exists
        if 'GPA' in df.columns:
            df = df[df['GPA'] >= 2.0]
            print(f"{sheet}: Filtered GPA < 2.0 | Remaining rows: {len(df)}")
        else:
            print(f"{sheet}: No GPA column found (skipped filtering)")

        # Save each cleaned sheet
        df.to_excel(writer, sheet_name=sheet, index=False)

print("✅ GPA filtering complete! New file saved as: EP_data_SFU_cleaned.xlsx")
