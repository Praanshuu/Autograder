import pandas as pd
import os
import re

excel_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'
sheet_name = 'Copy of Total-CSL100-Intro_Prog'
csv_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/CSL100/CSL100/Prac_30Q/q1/Summary_csl100_q1.csv'

try:
    # Load Excel IDs
    df_excel = pd.read_excel(excel_path, sheet_name=sheet_name)
    excel_ids = set(df_excel['ID'].astype(str).str.strip().str.upper())
    print(f"Found {len(excel_ids)} IDs in Excel.")
    print(f"Sample Excel IDs: {list(excel_ids)[:5]}")

    # Load CSV IDs
    df_csv = pd.read_csv(csv_path)
    # CSV ID format: B25DS024_Q1
    # Extract just the student ID part. Assuming format ID_Q#
    csv_ids_raw = df_csv.iloc[:, 0] # First column seems to be ID
    
    csv_ids = set()
    for raw_id in csv_ids_raw:
        # distinct ID might be splittable by underscore or just take the first part
        # Regex to capture the ID part
        match = re.match(r"([A-Za-z0-9]+)_", raw_id)
        if match:
            csv_ids.add(match.group(1).upper())
        else:
            csv_ids.add(raw_id.upper())
            
    print(f"Found {len(csv_ids)} IDs in CSV (Q1).")
    print(f"Sample CSV IDs: {list(csv_ids)[:5]}")

    # Check Intersection
    intersection = excel_ids.intersection(csv_ids)
    print(f"Intersection count: {len(intersection)}")
    print(f"Sample Intersection: {list(intersection)[:5]}")
    
    # Check Missing
    missing_in_excel = csv_ids - excel_ids
    print(f"IDs in CSV but NOT in Excel: {len(missing_in_excel)}")
    if missing_in_excel:
        print(f"Sample missing: {list(missing_in_excel)[:5]}")

except Exception as e:
    print(f"Error: {e}")
