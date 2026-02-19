import pandas as pd
import os

file_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'

try:
    xl = pd.ExcelFile(file_path)
    print(f"Sheet names: {xl.sheet_names}")
    
    target_sheet = "Copy of Total-CSL100-Intro_Prog"
    if target_sheet in xl.sheet_names:
        df = pd.read_excel(file_path, sheet_name=target_sheet, nrows=20)
        print(f"\nColumns in '{target_sheet}':")
        # print(df.columns.tolist())
        print("\nFirst 20 Rows (Name, ID, SIS Login ID):")
        print(df[['Name', 'ID', 'SIS Login ID']])
    else:
        print(f"\nSheet '{target_sheet}' not found!")
        
except Exception as e:
    print(f"Error: {e}")
