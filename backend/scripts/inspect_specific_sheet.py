import pandas as pd

file_path = r"d:\Programming\internshipiit\Autograder_UI_Proj\autograder\public\data\End Sem - CSL100 copy.xlsx"

def inspect_sheet(sheet_name):
    print(f"\n--- Sheet: {sheet_name} ---")
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, nrows=5)
        print(f"Columns: {df.columns.tolist()[:10]}") # First 10 cols
        if len(df) > 0:
            print(f"Row 0: {df.iloc[0].tolist()[:10]}")
    except Exception as e:
        print(f"Error checking {sheet_name}: {e}")

try:
    xls = pd.ExcelFile(file_path)
    print(f"All Sheets: {xls.sheet_names}")
    
    # Inspect likely candidates
    for name in xls.sheet_names:
        if 'Letter' in name or 'Course' in name or 'Project' in name:
            inspect_sheet(name)
            
except Exception as e:
    print(f"Fatal Error: {e}")
