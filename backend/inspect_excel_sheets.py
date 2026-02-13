import pandas as pd

file_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'

try:
    # Read the Excel file to get sheet names
    xls = pd.ExcelFile(file_path)
    print(f"Sheet Names: {xls.sheet_names}")
    
    # Inspect the first few rows of each sheet to understand content
    for sheet in xls.sheet_names:
        print(f"\n--- Sheet: {sheet} ---")
        df = pd.read_excel(file_path, sheet_name=sheet)
        print("Columns:")
        print(df.columns.tolist())
        print("First 3 rows:")
        print(df.head(3).to_string())
        
except Exception as e:
    print(f"Error reading Excel file: {e}")
