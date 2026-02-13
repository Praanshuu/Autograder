import pandas as pd

file_path = '/home/anshul/Projects/Autograder/backend/temp_data_folder/End Sem - CSL100 copy.xlsx'
sheet_name = 'Copy of Total-CSL100-Intro_Prog'
column_name = 'Practice Sheet - Whole Syllabus (60148873)'

try:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(f"Inspecting column: {column_name}")
    print(df[['Name', 'SIS Login ID', column_name]].head(10).to_string())
    print("\nDescribe:")
    print(df[column_name].describe())
except Exception as e:
    print(f"Error: {e}")
