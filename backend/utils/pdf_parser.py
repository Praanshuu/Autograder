import re

def parse_practice_sheet(file_path):
    """
    Parses the text file extracted from the Practice Sheet PDF.
    Returns a list of dictionaries with keys: 'title', 'difficulty', 'description', 'test_cases'.
    """
    with open(file_path, 'r') as f:
        text = f.read()

    questions = []
    # Regex to find Questions usually starting with "Q<number>."
    # Pattern looks for "Q" followed by digits, a dot, then the Title and Difficulty in parens
    # e.g., "Q1. FizzBuzz (Easy)"
    question_pattern = re.compile(r'(Q\d+\.\s+)(.*?)\s+\((Easy|Medium|Hard)\)', re.IGNORECASE)
    
    # Split text by "Q<number>."
    # This is a bit tricky because we want to keep the header. 
    # Let's verify the text structure first. 
    # Based on previous view_file, it looks like:
    # Q1. FizzBuzz (Easy)
    # Filename: ...
    # Function: ...
    # ...
    # Input: ...
    # Test Cases: ...
    
    # Let's find all start positions
    matches = list(question_pattern.finditer(text))
    
    for i, match in enumerate(matches):
        start_idx = match.start()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        
        q_text = text[start_idx:end_idx]
        
        # Extract details
        title_raw = match.group(2).strip()
        difficulty = match.group(3).strip()
        full_title = f"{match.group(1).strip()} {title_raw}"
        
        # Description is everything after the header until "Input:" or "Function:"
        # But looking at the file, the description is often inside docstrings """ ... """
        docstring_match = re.search(r'"""(.*?)"""', q_text, re.DOTALL)
        if docstring_match:
            description = docstring_match.group(1).strip()
            # Clean up newlines and excessive spaces
            description = re.sub(r'\s+', ' ', description)
        else:
            description = f"Implement {title_raw}"

        # Extract Test Cases
        # Look for lines after "Test Cases:"
        test_cases = []
        tc_section = re.search(r'Test Cases:(.*?)(?=\n\n|\Z)', q_text, re.DOTALL | re.IGNORECASE)
        if tc_section:
            # This is rough, as formatting varies. 
            # We will just store the raw text or try to find func calls
            # e.g. fizzbuzz(5)
            # # [1, 2, ...]
            lines = tc_section.group(1).strip().split('\n')
            for line in lines:
                if line.strip():
                    test_cases.append(line.strip())
        
        questions.append({
            'title': full_title,
            'difficulty': difficulty,
            'description': description,
            # We can infer function name from "Filename: <ID> q<num>.py" or "Function:\ndef foo..."
            'raw_text': q_text
        })
        
    return questions
