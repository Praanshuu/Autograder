import os
import pandas as pd
import re
from collections import defaultdict

qs_base = '/home/anshul/Projects/Autograder/backend/temp_data_folder/CSL100/CSL100/Prac_30Q'

def compare_branches():
    # Structure: Branch -> Question -> Count
    data = defaultdict(lambda: defaultdict(int))
    
    id_pattern = re.compile(r'^([A-Z])(\d{2})([A-Z]{2})(\d{3})$', re.IGNORECASE)
    
    for i in range(1, 31):
        csv_path = os.path.join(qs_base, f'q{i}', f'Summary_csl100_q{i}.csv')
        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                ids = df.iloc[:, 0].astype(str).tolist()
                
                for raw_id in ids:
                    match = id_pattern.match(raw_id.strip().upper())
                    if match:
                        _, year, branch, _ = match.groups()
                        if year == '25':
                            data[branch][f'q{i}'] += 1
            except Exception:
                pass

    print(f"{'Branch':<6} | {'Total Subs':<10} | {'Avg Subs/Q':<10} | {'Missed Qs':<10}")
    print("-" * 50)
    
    for branch, q_counts in sorted(data.items(), key=lambda x: sum(x[1].values()), reverse=True):
        total_subs = sum(q_counts.values())
        avg_subs = total_subs / 30
        missed_qs = 30 - len(q_counts)
        print(f"{branch:<6} | {total_subs:<10} | {avg_subs:<10.1f} | {missed_qs:<10}")

if __name__ == "__main__":
    compare_branches()
