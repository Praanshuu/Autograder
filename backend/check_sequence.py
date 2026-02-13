import os
import pandas as pd
import re
from collections import defaultdict

# Base path for Question Data
qs_base = '/home/anshul/Projects/Autograder/backend/temp_data_folder/CSL100/CSL100/Prac_30Q'

def check_sequence():
    all_raw_ids = set()
    
    # Iterate through all q1-q30 folders
    for i in range(1, 31):
        csv_path = os.path.join(qs_base, f'q{i}', f'Summary_csl100_q{i}.csv')
        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                ids = df.iloc[:, 0].astype(str).tolist()
                all_raw_ids.update(ids)
            except Exception:
                pass

    # Struct: Year -> Branch -> Set of Seq Numbers
    # e.g. '25' -> 'DS' -> {1, 2, 3, 5}
    data = defaultdict(lambda: defaultdict(set))
    
    id_pattern = re.compile(r'^([A-Z])(\d{2})([A-Z]{2})(\d{3})$', re.IGNORECASE)
    
    for raw_id in all_raw_ids:
        match = id_pattern.match(raw_id.strip().upper())
        if match:
            degree, year, branch, seq_str = match.groups()
            seq = int(seq_str)
            data[f"{degree}{year}"][branch].add(seq)

    print(f"Analyzing {len(all_raw_ids)} unique raw IDs across all sheets...")
    
    # Check for gaps
    for batch, branches in data.items():
        print(f"\n--- Batch {batch} ---")
        for branch, seqs in branches.items():
            if not seqs:
                continue
                
            min_seq = min(seqs)
            max_seq = max(seqs)
            
            # Expected set from min to max
            expected = set(range(min_seq, max_seq + 1))
            missing = expected - seqs
            
            # Also check if it starts at 1? Usually roll numbers start at 1.
            # If min_seq > 1, arguably 1..min_seq-1 are missing too, but maybe they joined late?
            # Let's just report gaps between min and max for now, and note start.
            
            status = "Complete"
            msg = ""
            if missing:
                status = "Gaps Found"
                missing_list = sorted(list(missing))
                # Format missing list nicely
                if len(missing_list) > 10:
                    msg = f"Missing {len(missing_list)} IDs: {missing_list[:10]}..."
                else:
                    msg = f"Missing: {missing_list}"
            
            print(f"  {branch}: Range {min_seq}-{max_seq} (Count: {len(seqs)}). {status}. {msg}")
            
            # Check for start gap (e.g. starts at 5)
            if min_seq > 1:
                print(f"     Note: Starts at {min_seq} (Missing 1-{min_seq-1}?)")

if __name__ == "__main__":
    check_sequence()
