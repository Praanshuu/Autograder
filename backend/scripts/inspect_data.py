import pandas as pd
import os

file_path = r"d:\Programming\internshipiit\Autograder_UI_Proj\autograder\public\data\End Sem - CSL100 copy.xlsx"
try:
    # Read all sheets to see what we have
    xls = pd.ExcelFile(file_path)
    print(f"Sheet names: {xls.sheet_names}")
    
    for sheet in xls.sheet_names:
        print(f"\n--- Sheet: {sheet} ---")
        df = pd.read_excel(xls, sheet_name=sheet, nrows=5)
        print(df.columns.tolist())
        print(df.head(2))
except Exception as e:
    print(f"Error reading excel: {e}")
