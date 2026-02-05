#!/usr/bin/env python3
"""
Debug tool to help students understand why their test cases are failing.
This shows the exact difference between expected and actual output.
"""

def debug_test_case(your_output, expected_output):
    """
    Compare your output with expected output and show differences
    """
    print("=== TEST CASE DEBUG ===")
    print(f"Your output: '{your_output}'")
    print(f"Expected:    '{expected_output}'")
    print(f"Your output length: {len(your_output)}")
    print(f"Expected length:    {len(expected_output)}")
    
    # Check if they match
    if your_output == expected_output:
        print("✅ MATCH! This test case should pass.")
        return True
    else:
        print("❌ NO MATCH! Here's why:")
        
        # Show character-by-character differences
        print("\nCharacter-by-character comparison:")
        max_len = max(len(your_output), len(expected_output))
        
        for i in range(max_len):
            your_char = your_output[i] if i < len(your_output) else '(missing)'
            expected_char = expected_output[i] if i < len(expected_output) else '(missing)'
            
            if your_char != expected_char:
                print(f"Position {i}: Your='{your_char}' Expected='{expected_char}' ❌")
            else:
                print(f"Position {i}: '{your_char}' ✅")
        
        # Common issues
        print("\n🔍 Common issues to check:")
        
        if your_output.strip() == expected_output.strip():
            print("- Extra whitespace/newlines at start or end")
        
        if your_output.lower() == expected_output.lower():
            print("- Case sensitivity (uppercase vs lowercase)")
        
        if your_output.replace(' ', '') == expected_output.replace(' ', ''):
            print("- Extra or missing spaces")
        
        if your_output.replace('\n', ' ') == expected_output.replace('\n', ' '):
            print("- Newline vs space differences")
        
        return False

# Example usage:
if __name__ == "__main__":
    # Example test case
    your_output = "Hello World "  # Note the extra space
    expected_output = "Hello World"
    
    debug_test_case(your_output, expected_output)