import pandas as pd
import os

excel_path = 'temp_data_folder/End Sem - CSL100 copy.xlsx'
csv_path = 'temp_data_folder/CSL100/CSL100/Prac_30Q/merged_output/merged_q1_q30.csv'

print(f"--- Inspecting {excel_path} ---")
try:
    if os.path.exists(excel_path):
        df_excel = pd.read_excel(excel_path)
        print("Columns:", list(df_excel.columns))
        print("First 3 rows:")
        print(df_excel.head(3).to_string())
    else:
        print("File not found.")
except Exception as e:
    print(f"Error reading Excel: {e}")

print(f"\n--- Inspecting {csv_path} ---")
try:
    if os.path.exists(csv_path):
        df_csv = pd.read_csv(csv_path)
        print("Columns:", list(df_csv.columns))
        print("First 3 rows:")
        print(df_csv.iloc[:3, :10].to_string()) # Show first 10 cols
    else:
        print("File not found.")
except Exception as e:
    print(f"Error reading CSV: {e}")
