
import pandas as pd

file_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'

try:
    # Read without headers to see the raw layout
    df = pd.read_excel(file_path, sheet_name='LetterGrades-CSL100-Intro_Progr', header=None)
    
    print("\nFirst 10 rows:")
    print(df.head(10))
    
    # helper to print non-null values in a row to identify headers
    print("\nPotential Header Rows:")
    for i in range(5):
        row = df.iloc[i]
        print(f"Row {i}: {row.dropna().tolist()}")

except Exception as e:
    print(f"Error reading excel file: {e}")
