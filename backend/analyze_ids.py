import os
import pandas as pd
import re
from collections import Counter

# Base path for Question Data
qs_base = '/home/anshul/Projects/Autograder/backend/temp_data_folder/CSL100/CSL100/Prac_30Q'

def analyze_ids():
    all_raw_ids = []
    
    # Iterate through all q1-q30 folders
    for i in range(1, 31):
        csv_path = os.path.join(qs_base, f'q{i}', f'Summary_csl100_q{i}.csv')
        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                # Assume first col is ID
                ids = df.iloc[:, 0].astype(str).tolist()
                all_raw_ids.extend(ids)
            except Exception as e:
                print(f"Error reading Q{i}: {e}")

    print(f"Total raw submissions found: {len(all_raw_ids)}")
    
    # Regex for standard ID: Start with letter, then digits, then letters, then digits
    # User said: B25DS039 -> B (Prog), 25 (Year), DS (Branch), 039 (Seq)
    # Pattern: ^([A-Z])(\d{2})([A-Z]{2})(\d{3})
    
    valid_ids = set()
    batches = Counter()
    branches = Counter()
    noise = []
    
    # Loose regex to capture likely IDs even with suffix
    # Looks for [Letter][Digit][Digit][Letter][Letter][Digit]+
    id_pattern = re.compile(r'([A-Z])(\d{2})([A-Z]{2})(\d{3})', re.IGNORECASE)
    
    for raw_id in all_raw_ids:
        # standardizing
        clean_raw = raw_id.upper().strip()
        
        match = id_pattern.search(clean_raw)
        if match:
            # Extracted ID
            degree, year, branch, seq = match.groups()
            full_id = f"{degree}{year}{branch}{seq}"
            
            valid_ids.add(full_id)
            batches[year] += 1
            branches[branch] += 1
        else:
            noise.append(raw_id)
            
    print(f"\nUnique Valid IDs found: {len(valid_ids)}")
    print("\nBatch Distribution (Year):")
    for year, count in batches.most_common():
        print(f"  20{year}: {count} submissions")

    print("\nBranch Distribution:")
    for branch, count in branches.most_common():
        print(f"  {branch}: {count} submissions")
        
    print(f"\nNoise Examples (Total {len(noise)}):")
    print(noise[:20]) # Show first 20 noise items

    # Suggestion
    print("\n--- Recommendation ---")
    most_common_year = batches.most_common(1)[0][0]
    print(f"Focus on Batch 20{most_common_year}")

if __name__ == "__main__":
    analyze_ids()
