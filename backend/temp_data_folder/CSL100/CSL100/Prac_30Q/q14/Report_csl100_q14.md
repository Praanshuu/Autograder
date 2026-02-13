# Autograder - Aggregated Feedback Report
## Assignment: csl100_q14



--- Feedback Report for: {B25MM017}_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that some values in the input dictionary are not unique, causing a KeyError when trying to swap them as keys. To fix this, ensure that all values in the input dictionary have unique elements before inverting it.
</output>
```

================================================================================



--- Feedback Report for: B25EE043_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each value in the original dictionary is unique, as this is a crucial aspect of inverting a dictionary with unique values.</output>
```

================================================================================



--- Feedback Report for: B25CS016_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the assumption that all values are unique and hashable, but this is not guaranteed by the problem statement; instead, consider using a dictionary comprehension with the `dict.get()` method to handle duplicate keys.
</output>
```

================================================================================



--- Feedback Report for: B25DS025_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the key exists in the new dictionary before trying to assign its value, as using a non-existent key can raise a KeyError.
</output>
```

================================================================================



--- Feedback Report for: B25EE053_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap the order of key and value when assigning to rev in the line `rev[value] = key`, so that keys become values and vice versa.</output>
```

================================================================================



--- Feedback Report for: B25CS030_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if a value exists in the original dictionary before using it as a key in the inverted dictionary, e.g., `if value in d:`.</output>
```

================================================================================



--- Feedback Report for: B25ME056_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the value is present in the original dictionary before using it as a key in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25MT021_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the value as a new key, which can lead to collisions and incorrect assignments. Instead, check if each value already exists in the new dictionary before assigning it a key.
</output>
```

================================================================================



--- Feedback Report for: B25CS035_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The issue lies in the fact that you're using `values` as a key, which is likely not unique and may lead to collisions when trying to access or assign dictionary values. Consider checking if a key exists before trying to use it, such as with the `in` operator or the `.get()` method.
```

================================================================================



--- Feedback Report for: B25DS030_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each value in the original dictionary is unique, as this is a crucial step in inverting a dictionary with unique values.</output>
```

================================================================================



--- Feedback Report for: S25MA002_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `dict.get()` method or checking if a key exists with `k in inverted` before assigning a value, as your current implementation overwrites existing keys without a clear indication of their original values.
</output>
```

================================================================================



--- Feedback Report for: B25CS056_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the key exists in the original dictionary before trying to assign its value to the inverted dictionary, as the current implementation may result in a KeyError when a new key is added that doesn't exist in the values.
</output>
```

================================================================================



--- Feedback Report for: Q14 B25MM007 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the value is present in the inverted dictionary before attempting to assign the key, as this could lead to KeyError.</output>
```

================================================================================



--- Feedback Report for: B25EE031_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the dictionary before trying to assign a value to it.</output>
```

================================================================================



--- Feedback Report for: B25DS035_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if your code is correctly handling duplicate values in the original dictionary, as swapping keys and values may not work as expected when there are duplicates.</output>
```

================================================================================



--- Feedback Report for: B25MM027_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the value is in the original dictionary before using it as a key in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25MM018_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding error handling to ensure that the inverted dictionary doesn't contain keys with duplicate values, as this could lead to unexpected behavior.</output>
```

================================================================================



--- Feedback Report for: B25CS038-Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS038-Q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS038-Q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS038-Q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS038-Q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS038-Q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The issue lies in the fact that you are using a variable name (`dict`) that shadows the built-in Python dictionary class, which is causing the function to be named `invert_dict` instead of `inverted_dict`.
```

================================================================================



--- Feedback Report for: B25CS029_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that the student's code is attempting to create an inverted dictionary, but it's not handling cases where keys are missing from the original dictionary. Consider adding a check to ensure that both key and value exist in the original dictionary before swapping them.</output>
```

================================================================================



--- Feedback Report for: B25MT029_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the dictionary comprehension where you're using `k` and `v` as keys and values, but you should be swapping them. Try changing `{v: k for k, v in dic.items()}` to `{k: v for k, v in dic.items()}`.
</output>
```

================================================================================



--- Feedback Report for: B25EE027_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `d2[val] = i`, where you're using the value as a key, but the problem statement assumes all values are unique and hashable. Instead, consider checking if the value already exists in `d2` before assigning it.
</output>
```

================================================================================



--- Feedback Report for: B25EE006.Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE006'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `in` operator to check if a value exists in the dictionary before trying to assign it as a key, e.g., `if values not in di:`</output>
```

================================================================================



--- Feedback Report for: B25ME016_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b', 3: 'c'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the inverted key-value pairs are added to the new dictionary only when both the original key and value exist in the input dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC018_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure the value exists in the dictionary before using it as a key, as your current implementation may lead to unexpected behavior or errors when dealing with non-existent values.</output>
```

================================================================================



--- Feedback Report for: B25EE012_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the inverted dictionary does not contain duplicate keys, as the current implementation will overwrite existing keys with new ones.</output>
```

================================================================================



--- Feedback Report for: B25DS036_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `i[values] = key`, where you're using the value as a key, which might not be unique. Consider adding a check to ensure that each value is used as a key only once.
</output>
```

================================================================================



--- Feedback Report for: B25MM009(q14) ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM009(q14)'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM009(q14)'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM009(q14)'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM009(q14)'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM009(q14)'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are correctly iterating over the values of the dictionary instead of its keys.</output>
```

================================================================================



--- Feedback Report for: B25MT007_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows providing a default value if the key is not present in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25ME043_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary has duplicate keys, as this could lead to overwriting existing key-value pairs.</output>
```

================================================================================



--- Feedback Report for: B25DS033_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Use the `inverted` dictionary's `get()` method to access its values, and consider using the `.setdefault()` method to avoid KeyError.</output>
```

================================================================================



--- Feedback Report for: B25EC032_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using dictionary comprehension to create a new dictionary with swapped key-value pairs, and handle cases where values are not unique.</output>
```

================================================================================



--- Feedback Report for: B25MT003_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue with your code is that you're iterating over the dictionary items, but when inverting the dictionary, you should be using the values as keys and vice versa. You need to check if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25CS007_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try iterating over the dictionary items using `for k, v in d.items():` instead of just `d.items`, which is a method call that needs parentheses.</output>
```

================================================================================



--- Feedback Report for: B25EE018_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the value (v) is not None before using it as a key in the new dictionary, i.e., `return {k: v for k, v in d.items() if v is not None};</output>
```

================================================================================



--- Feedback Report for: B25CS014_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary is being populated correctly by ensuring that each value (which should be unique) is used as a key and vice versa, without any duplicate keys.</output>
```

================================================================================



--- Feedback Report for: B25ME050_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Ensure that you're using the correct data type for the keys in the original dictionary, as they might not be hashable.</output>
```

================================================================================



--- Feedback Report for: B25EC042_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the value as the key and vice versa, which is causing the incorrect assignment of keys and values. Consider adding a check to ensure that each unique value exists as a key before assigning it.
</output>
```

================================================================================



--- Feedback Report for: B25ME032_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which returns `None` by default if the key is not found, instead of attempting to assign a value to a non-existent key.</output>
```

================================================================================



--- Feedback Report for: B25CS046_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the value of each key-value pair in the original dictionary is unique, as per the problem's requirement.</output>
```

================================================================================



--- Feedback Report for: B25EE059_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check if the key exists in the original dictionary before using it as a value, as your code will raise a KeyError when the key is not present.
</output>
```

================================================================================



--- Feedback Report for: B25EE038_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as a key, which is likely not unique in the original dictionary, causing collisions and incorrect assignments. Try using each value as a separate key instead.
</output>
```

================================================================================



--- Feedback Report for: B25DS010_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
To avoid the KeyError, consider using the `get()` method or a dictionary comprehension with an initial value to ensure that each key exists in the reversed dictionary before attempting to assign its value.
</output>
```

================================================================================



--- Feedback Report for: B25EE037_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try swapping `value` and `key` when assigning to `D`, as Python treats keys and values differently.</output>
```

================================================================================



--- Feedback Report for: B25EC001_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check for duplicate values in the original dictionary, as this could lead to incorrect key-value assignments in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25ME052_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that when using dictionary comprehension, you're iterating over the items in the order they were inserted, not by their unique values. To fix this, consider using a set to get unique keys and then iterate over them.
</output>
```

================================================================================



--- Feedback Report for: B25ME004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap the keys and values in the dictionary using a conditional statement to check for uniqueness of values, e.g., `result[value] = key` should be `if value not in result: result[value] = key`. </output>
```

================================================================================



--- Feedback Report for: B25MT010_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'c'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'c'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'c'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'c'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'c'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as both a key and a value, which is not unique in your dictionary. You should be using a different data structure or approach to invert a dictionary with unique values.
</output>
```

================================================================================



--- Feedback Report for: B25CS039_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `dict[value]` which is not a valid way to access or assign dictionary values, as dictionaries are inherently unordered. Instead, consider using `d.get(value)` or `d.setdefault(value, key)`.
</output>
```

================================================================================



--- Feedback Report for: B25DS012_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which returns `None` by default if the key is not found, instead of relying on indexing with square brackets (`[]`).</output>
```

================================================================================



--- Feedback Report for: B25CS025_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `e[values] = key`, where you're trying to use a value as a key. Instead, consider using the `.get()` method or an if-else statement to safely access dictionary keys.
</output>
```

================================================================================



--- Feedback Report for: B25CS055_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure the value exists in the dictionary before using it as a key, e.g., `d_[d[i]] = i` should be `i in d_ and not d_[d[i]]`, to avoid potential issues with duplicate values.
</output>
```

================================================================================



--- Feedback Report for: B25EC024_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the value as the new key, which can lead to duplicate keys in the resulting dictionary. You should be using the original key instead.
</output>
```

================================================================================



--- Feedback Report for: B25MM015_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that the code checks if a value exists in the original dictionary before using it as a key in the inverted dictionary, as the current implementation will result in a KeyError when a duplicate value is encountered.</output>
```

================================================================================



--- Feedback Report for: B25DS018_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each key in the original dictionary is unique before inverting it, as your current implementation may overwrite existing keys.</output>
```

================================================================================



--- Feedback Report for: B25CS008_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in using `d.values()` and `d.keys()` directly, which returns views of the original dictionary's values and keys. Instead, you should pass the actual values and keys as separate arguments to the `zip` function.
</output>
```

================================================================================



--- Feedback Report for: B25EE054_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by iterating over its items and using the value as the new key, but be cautious when accessing or assigning dictionary values, as the current logic may lead to unexpected behavior if a duplicate value exists.
</output>
```

================================================================================



--- Feedback Report for: B25MM004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows you to specify a default value if the key does not exist.</output>
```

================================================================================



--- Feedback Report for: B25EE060_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `swap[d[i]] = i`, where you're using the value from the original dictionary as a key in the new dictionary, which is causing the problem. Instead, try using the key-value pairs directly, like this: `swap[i] = d[i]`.
</output>
```

================================================================================



--- Feedback Report for: B25MM023_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b', 'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b', 10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b', 'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check if the key exists in the dictionary before trying to access its value, as `d[x]` may raise a KeyError if `x` is not present in `d`.
</output>
```

================================================================================



--- Feedback Report for: B25EC004_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: ['a'], 2: ['b']}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'v1': ['k1']}`
- Test 'empty': PASS
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{10: ['x'], 20: ['y'], 30: ['z']}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'a': [1], 'b': [2], 'c': [3]}`

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the key exists in the dictionary before trying to access its value using `d[key]`, e.g., `if key in d:`.</output>
```

================================================================================



--- Feedback Report for: B25DS003_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which returns `None` if the key is not found, instead of directly assigning a value to a non-existent key.</output>
```

================================================================================



--- Feedback Report for: B25DS031_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the value is present in the new dictionary (`z`) before using it as a key, as this could lead to unexpected behavior or errors.</output>
```

================================================================================



--- Feedback Report for: B25EC019_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if a key exists in the original dictionary before using its value as a key in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC037_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using a dictionary comprehension to create the new inverted dictionary, which can simplify and improve the code's readability.</output>
```

================================================================================



--- Feedback Report for: B25DS011_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows you to specify a default value if the key does not exist.</output>
```

================================================================================



--- Feedback Report for: B25ME034_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you are swapping keys and values correctly, as in `d_new[key] = value`, not `d_new[value] = key`.
</output>
```

================================================================================



--- Feedback Report for: B25CS002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values in the original dictionary by using a conditional statement to check for uniqueness of each value.</output>
```

================================================================================



--- Feedback Report for: B25DS014_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values in the dictionary using a dictionary comprehension instead of iterating over its keys.</output>
```

================================================================================



--- Feedback Report for: B25EE052_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Reversing dictionary keys and values requires checking for duplicate values, which is missing in your implementation. Ensure that you handle cases where multiple keys map to the same value.
</output>
```

================================================================================



--- Feedback Report for: B25CS028_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `invert_d[j] = i`, where you're trying to assign the value of `i` (an integer) as the key and then try to access it using its original value `j` later. This approach won't work for dictionaries with unique values, which is what your task requires.
</output>
```

================================================================================



--- Feedback Report for: B25EC002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each unique value in the original dictionary is used as a key in the new inverted dictionary, and vice versa.</output>
```

================================================================================



--- Feedback Report for: B25CS051_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values in the original dictionary, but ensure that each new key-value pair is unique.</output>
```

================================================================================



--- Feedback Report for: B25ME033_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the value exists in the new dictionary before trying to assign it as a key, as this could lead to unexpected behavior.</output>
```

================================================================================



--- Feedback Report for: B25ME003_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the value exists in the dictionary before using it as a key, as the current implementation will result in a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25ME026_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `inverted[value] = key`, where you're using the value as a key, potentially causing collisions and incorrect assignments. Instead, consider using the original key-value pair to construct the inverted dictionary, like so: `inverted[key] = value`.
</output>
```

================================================================================



--- Feedback Report for: B25ME037_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the value as the new key and vice versa, but in Python, dictionaries cannot have duplicate keys. You should check if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25ME024_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary is being populated correctly by verifying that each unique value in the original dictionary corresponds to only one key in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25CS033_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the value is present in the original dictionary before using it as a key, e.g., `if d[key] not in d`, to handle cases where values are not unique.</output>
```

================================================================================



--- Feedback Report for: B25EC022_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the inverted dictionary does not contain duplicate keys, which could lead to data loss.</output>
```

================================================================================



--- Feedback Report for: B25ME023 q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which allows you to specify a default value if the key does not exist.</output>
```

================================================================================



--- Feedback Report for: B25CS041_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure the value (i.e., d[i]) is present in the original dictionary `d` before using it as a key in the inverted dictionary `y`.
</output>
```

================================================================================



--- Feedback Report for: B25EE045_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] NameError: name 'a' is not defined
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] NameError: name 'a' is not defined
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] NameError: name 'a' is not defined
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] NameError: name 'a' is not defined
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] NameError: name 'a' is not defined
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try iterating over the dictionary items with `for key, value in d.items():` instead of `for key, value in d:` to access both keys and values.</output>
```

================================================================================



--- Feedback Report for: B25MM020_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] EOFError: EOF when reading a line
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] EOFError: EOF when reading a line
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] EOFError: EOF when reading a line
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] EOFError: EOF when reading a line
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] EOFError: EOF when reading a line
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider using a set to keep track of unique values, as your current approach with `v.index(i)` will raise an EOFError when the value is not found in the list of keys. This could be improved by checking if the value exists in the key's list before attempting to find its index.
</output>
```

================================================================================



--- Feedback Report for: B25MT005_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
When swapping keys and values, ensure that the new key is present in the inverted dictionary before assigning its value to avoid KeyError.
</output>
```

================================================================================



--- Feedback Report for: S25MA011_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the same variable name 'd' for both the original dictionary and the new inverted dictionary, causing confusion between the two. Try renaming one of them to avoid this ambiguity.
</output>
```

================================================================================



--- Feedback Report for: B25MT020_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{'yaswanth': 'first_name', 'ramala': 'last_name'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'yaswanth': 'first_name', 'ramala': 'last_name'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{'yaswanth': 'first_name', 'ramala': 'last_name'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{'yaswanth': 'first_name', 'ramala': 'last_name'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'yaswanth': 'first_name', 'ramala': 'last_name'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using a dictionary comprehension to create the inverted dictionary, as it can simplify the code and ensure that each value is mapped to its corresponding key.</output>
```

================================================================================



--- Feedback Report for: B25EE058_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `inverted[d[i]] = i`, where you're using the value (`d[i]`) as a key, but dictionary keys must be unique. Instead, consider using `i` as the key and `d[i]` as the value.
</output>
```

================================================================================



--- Feedback Report for: B25DS020_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS020_Q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS020_Q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS020_Q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS020_Q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS020_Q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the key exists in the dictionary before trying to access or assign its value, as this could be causing the function 'invert_dict' not found error due to incorrect usage of dictionary keys and values.
</output>
```

================================================================================



--- Feedback Report for: B25CS022_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Try using the `get()` method to access dictionary values, which allows you to specify a default value if the key does not exist.
</output>
```

================================================================================



--- Feedback Report for: B25EE046_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The loop construct in your code is iterating over each key in the dictionary `d`, but it should be iterating over each value instead, to correctly swap keys and values.
```

================================================================================



--- Feedback Report for: B25EC025_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{2: 'chi', 4: 'ntu'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{2: 'chi', 4: 'ntu'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{2: 'chi', 4: 'ntu'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{2: 'chi', 4: 'ntu'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{2: 'chi', 4: 'ntu'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as a key, which is a duplicate value from the original dictionary, not the unique values. You should be using each unique value as a key instead.
</output>
```

================================================================================



--- Feedback Report for: B25ME035_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'b', 2: 'b'}
{1: 'b', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'b', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'b', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'b', 2: 'b'}
{10: 'z', 20: 'z', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'b', 2: 'b'}
{'a': 3, 'b': 3, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the inner loop where you're iterating over the dictionary's values, which are unique and not iterable. You should iterate over the keys instead, as they represent the original dictionary values that need to be swapped.
</output>
```

================================================================================



--- Feedback Report for: <B25CS024>_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try iterating over the dictionary's items using `.items()` instead of just `d.items`, as `.items` is a method, not an attribute.</output>
```

================================================================================



--- Feedback Report for: B25EE020_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using the `get()` method to access dictionary values, which allows specifying a default value to return if the key is not found.</output>
```

================================================================================



--- Feedback Report for: B25EC017_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows you to specify a default value to return if the key does not exist.</output>
```

================================================================================



--- Feedback Report for: B25CS009_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the original dictionary before using its value as a new key, as the current implementation will raise a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25EE035_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `if` statement to check if each value is unique before assigning it a new key, as using a dictionary with duplicate values will overwrite previous assignments.
</output>
```

================================================================================



--- Feedback Report for: B25ME006_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `d.items()` which returns an iterator over the dictionary's keys and values, but when you iterate over this iterator, you should unpack each key-value pair into two separate variables (e.g., `key` and `value`). This is why you need to check if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25CS026_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the value is in the dictionary's keys before using it as a new key, as this could lead to unexpected behavior and incorrect results.</output>
```

================================================================================



--- Feedback Report for: B25ME028_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: ['a'], 2: ['b']}
{'v1': ['k1']}
{1: ['a'], 2: ['b']}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: ['a'], 2: ['b']}
{'v1': ['k1']}
{'v1': ['k1']}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: ['a'], 2: ['b']}
{'v1': ['k1']}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: ['a'], 2: ['b']}
{'v1': ['k1']}
{10: ['x'], 20: ['y'], 30: ['z']}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: ['a'], 2: ['b']}
{'v1': ['k1']}
{'a': [1], 'b': [2], 'c': [3]}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
To avoid the KeyError when accessing dictionary values that don't exist yet, consider initializing the value with an empty list instead of trying to append to it directly. For instance, use `result[value] = result.get(value, []) + [key]`.
</output>
```

================================================================================



--- Feedback Report for: S25MA004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>

The issue lies in the assumption that all values are unique and hashable, which may not be the case for dictionaries with duplicate values or non-hashable types.
```

================================================================================



--- Feedback Report for: B25ME060_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to handle duplicate values correctly by using a data structure that can store multiple keys for each value, such as a dictionary or a set.
</output>
```

================================================================================



--- Feedback Report for: q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values, but consider using a dictionary comprehension for conciseness.</output>
```

================================================================================



--- Feedback Report for: B25EE009_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `p[d[i]] = i`, where you're using the value as a key, but later trying to access it with its original key (`i`), which is not present in the inverted dictionary. You should use the original key to assign values instead.
</output>
```

================================================================================



--- Feedback Report for: B25EC036_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that keys and values are unique, as this is a crucial aspect of inverting a dictionary with unique values.</output>
```

================================================================================



--- Feedback Report for: B25ME030_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{'a': 1, 'b': 2, 'c': 3}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'a': 1, 'b': 2, 'c': 3}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{'a': 1, 'b': 2, 'c': 3}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{'a': 1, 'b': 2, 'c': 3}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
To avoid the KeyError, use the `in` operator or the `.get()` method to check if a key exists in the dictionary before trying to access its corresponding value.
</output>
```

================================================================================



--- Feedback Report for: b25me058_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict` method `.get()` instead of direct assignment, e.g., `p[v] = k`, which allows you to specify a default value if the key doesn't exist.</output>
```

================================================================================



--- Feedback Report for: B25DS038_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that when you iterate over `d.items()`, the keys and values are swapped, but the resulting dictionary still has the original order of the items. To fix this, use the `dict.fromkeys()` method or ensure that the order of items is preserved by using an OrderedDict.
</output>
```

================================================================================



--- Feedback Report for: B25CS019_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that the issue lies in the fact that you're using the value as a key, which can lead to duplicate keys in the resulting dictionary. Consider using a different approach, such as checking if a key exists before trying to use it.</output>
```

================================================================================



--- Feedback Report for: B25MT027_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the condition `c = d[i]` is correctly assigning the value to a variable, and consider using a different approach, such as iterating over the dictionary's values instead of its keys.</output>
```

================================================================================



--- Feedback Report for: B25MM030_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by iterating over its items and using each value as a key, but ensure that you're using the correct data structure for this purpose, such as a set or list, to avoid issues with duplicate keys.
</output>
```

================================================================================



--- Feedback Report for: B25DS023_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The loop iterates over `keys1` but assigns values from `vals1`, which might be empty if the original dictionary had only unique keys. Ensure that the loop iterates over both key and value pairs simultaneously using `.items()` instead of separate lists for keys and values.
</output>
```

================================================================================



--- Feedback Report for: B25EC039_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Re-examine your loop construct; consider using enumerate instead of range to iterate over both index and value simultaneously, ensuring you're correctly swapping key-value pairs.</output>
```

================================================================================



--- Feedback Report for: B25MT017_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you are trying to invert a dictionary with unique values, but your current implementation assumes all keys and values will always be present. You should add a check to ensure each key exists in the original dictionary before using it as a value.
</output>
```

================================================================================



--- Feedback Report for: B25CS017_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `d.items()` which returns an iterator over the dictionary's keys and values, but when iterating over this iterator, you're directly assigning the key to the value and vice versa without checking if the key already exists in the new dictionary. This can lead to duplicate values in the inverted dictionary.
</output>
```

================================================================================



--- Feedback Report for: B25ME027_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by iterating over its unique values, using each value as a new key and the original key as the corresponding value in the inverted dictionary. For example, if the input dictionary is {'a': 1, 'b': 2}, the output should be {1: 'a', 2: 'b'}. 
</output>
```

================================================================================



--- Feedback Report for: B25MT004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding error handling to ensure that keys and values are not swapped when a key is present in the original dictionary more than once, as this could lead to data loss.</output>
```

================================================================================



--- Feedback Report for: b25me047_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary is being populated correctly by ensuring each unique value in the original dictionary corresponds to exactly one key in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25DS026.q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS026'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the function name 'd' not matching the module name 'B25DS026'. Rename the function to match the module, e.g., `invert_dict()` becomes `B25DS026.invert_dict()`.
</output>
```

================================================================================



--- Feedback Report for: B25ME013_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the original dictionary before trying to access its value.</output>
```

================================================================================



--- Feedback Report for: B25CS059_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swapping keys and values in a dictionary requires using the `dict` constructor with key-value pairs as arguments, not iterating over the dictionary's items.</output>
```

================================================================================



--- Feedback Report for: B25DS002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method of dictionaries, which allows you to specify a default value to return if the key is not found in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25MM013_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using a conditional statement to check if the value is unique, and only add it to the new dictionary if it is not already present.
</output>
```

================================================================================



--- Feedback Report for: B24DS035_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the value as a key, but dictionaries in Python cannot have duplicate keys. You should be using each unique value as a separate key instead of trying to assign it back to its original key.
</output>
```

================================================================================



--- Feedback Report for: {B25CS013}_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The function does not handle cases where the value in the original dictionary is also present as a key elsewhere. Consider adding checks to ensure that each unique value can be found as a key before attempting to invert it.</output>
```

================================================================================



--- Feedback Report for: B25MT015_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values in the original dictionary by using `result[k] = value` instead of `result[value] = k`, ensuring that unique values are used as keys.</output>
```

================================================================================



--- Feedback Report for: B25ME021_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you are using `value` as a key, which is likely to be a duplicate value from the original dictionary. You should instead use a unique identifier for each value, such as its hash or an incrementing counter.
</output>
```

================================================================================



--- Feedback Report for: B25EE007_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check for uniqueness of values in the original dictionary, as using a set to store unique keys might not be necessary and could lead to incorrect results when swapping key-value pairs.</output>
```

================================================================================



--- Feedback Report for: B25EC033_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by iterating over its items and using the `in` keyword to check if each value is present in the new inverted dictionary, ensuring you don't overwrite existing assignments.
</output>
```

================================================================================



--- Feedback Report for: B25CS023_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the inverted dictionary key exists in the original dictionary before using it as a value, as this could lead to a KeyError if the key is not present.
</output>
```

================================================================================



--- Feedback Report for: B25EE029_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to handle cases where a value is unique, as this would result in a key-value swap being repeated, effectively losing one of the original values. Consider adding an if condition to check for uniqueness before swapping the key and value.
</output>
```

================================================================================



--- Feedback Report for: S25MA016_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the inverted dictionary has any duplicate keys, which could result in data loss when swapping values with their original keys.</output>
```

================================================================================



--- Feedback Report for: B25DS024_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary is being populated correctly by iterating through each unique value in the original dictionary and assigning its corresponding key, but first ensure that the key exists in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC031_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which allows you to specify a default value to return if the key is not found in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25CS042_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each unique value in the input dictionary is also present in the original dictionary, as this would be necessary for an invert operation.</output>
```

================================================================================



--- Feedback Report for: B25CS010_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which returns `None` by default if the key is not found, instead of raising a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25MT022_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check if the key exists in the original dictionary before using it as a value in the inverted dictionary, as the keys and values are swapped.
</output>
```

================================================================================



--- Feedback Report for: B25EE042_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as keys, which are likely unique integers or strings, but dictionary keys must be hashable and unique. Consider checking if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25EE004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert_dict should check if the value already exists in the inverted dictionary before assigning a new key-value pair, as the current implementation overwrites existing keys with the same value.
</output>
```

================================================================================



--- Feedback Report for: B25DS037_Q14.py ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS037_Q14'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS037_Q14'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS037_Q14'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS037_Q14'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25DS037_Q14'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `new_dict[v] = k`, where you're assuming that every value in the original dictionary is unique, which isn't guaranteed. Consider adding a check to ensure each value exists before trying to assign it as a key.
</output>
```

================================================================================



--- Feedback Report for: B25MT009_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The loop iterates over a copy of the original dictionary `a`, but it should iterate over the original dictionary `d` instead to swap keys and values correctly.</output>
```

================================================================================



--- Feedback Report for: B25ME005_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Try using the `dict.setdefault()` method to ensure that each value in the list is used as a key in the new dictionary, avoiding potential KeyError exceptions.
</output>
```

================================================================================



--- Feedback Report for: B25EC014_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the original dictionary `d` before trying to access its value with `d.get(x)`.</output>
```

================================================================================



--- Feedback Report for: B25CS004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using the `dict.setdefault()` method to ensure that the value is present in the result dictionary before attempting to assign it, e.g., `ans.setdefault(value[i], key[i]) = key[i]`. This will prevent potential KeyError exceptions.</output>
```

================================================================================



--- Feedback Report for: B25ME002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method or a conditional statement to check if a key exists in the dictionary before trying to assign its value to another variable.</output>
```

================================================================================



--- Feedback Report for: B25CS005_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 0

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS005_q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS005_q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS005_q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS005_q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25CS005_q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

- Technical summary was not generated.

================================================================================



--- Feedback Report for: B25CS043-q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that the original dictionary `c` is not guaranteed to have unique values. To fix this, you should add a check to ensure that each value appears only once before attempting to invert it.
</output>
```

================================================================================



--- Feedback Report for: B25EE048_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap the indexing in your `for` loop from `i` to `key_list[i]`, as you're currently trying to access the dictionary value with the key, not the other way around.</output>
```

================================================================================



--- Feedback Report for: B25EC027_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary is empty and handle this case, as the current implementation will raise a KeyError when trying to access a non-existent value.</output>
```

================================================================================



--- Feedback Report for: B25DS022_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'X': 1, 'y': 2}
{}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'X': 1, 'y': 2}
{}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'X': 1, 'y': 2}
{}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'X': 1, 'y': 2}
{}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'X': 1, 'y': 2}
{}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which returns `None` if the key is not found, instead of relying on the `in` operator.</output>
```

================================================================================



--- Feedback Report for: B25CS050_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the keys and values are swapped correctly by verifying that each value is associated with its original key in the input dictionary.</output>
```

================================================================================



--- Feedback Report for: B25CS048_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `d.items()` which returns an iterator over the dictionary's keys and values, but then you're iterating over it again as if it were a list of tuples. Instead, use `dict.fromkeys()` to create a new dictionary with unique values.
</output>
```

================================================================================



--- Feedback Report for: B25DS007_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `dict` constructor and providing a function that takes two arguments, but you're currently assigning the values as keys and vice versa. Consider checking if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25MT006_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `1 a
2 b
{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `1 a
2 b
{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `1 a
2 b
{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `1 a
2 b
{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `1 a
2 b
{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Swap key and value assignments in the for loop to correctly invert the dictionary, e.g., `c[value] = key` instead of `c[key] = value`.
</output>
```

================================================================================



--- Feedback Report for: B25MM001_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1', 'v2': 'k2'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1', 'v2': 'k2'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1', 'v2': 'k2'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1', 'v2': 'k2'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1', 'v2': 'k2'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary has all unique keys and values, as dictionaries cannot have duplicate keys.</output>
```

================================================================================



--- Feedback Report for: B25EE002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method of dictionaries, which allows you to specify a default value to return if the key is not found in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EE011_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Reconsider the loop construct; currently, you are iterating over `lst_values` which contains values from the original dictionary, not keys. Ensure to iterate over `lst_keys` instead.</output>
```

================================================================================



--- Feedback Report for: B25DS013_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'vl': 'kl'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Reconsider the assignment of values to keys, ensuring that each unique value in the original dictionary is used as a key in the inverted dictionary, and handle potential KeyError exceptions when assigning values to keys.</output>
```

================================================================================



--- Feedback Report for: b25cs049_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary has all unique keys by ensuring that there are no duplicate values in the original dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EE039_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the dictionary keys exist in the original dictionary before using them as values, as some unique values might not be present in the dictionary.
</output>
```

================================================================================



--- Feedback Report for: B25ME059_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the new dictionary before trying to access its value, as using `value: key` might lead to incorrect results.</output>
```

================================================================================



--- Feedback Report for: B25CS061_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap the key-value pairs by using `word` as the new key and `d[word]` as the new value in each iteration of the loop.</output>
```

================================================================================



--- Feedback Report for: B25EE001_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding error handling to ensure that the inverted dictionary only includes unique values, and handle cases where a value is missing its corresponding key.</output>
```

================================================================================



--- Feedback Report for: B25ME007_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Use the `get()` method to access and assign dictionary values, ensuring that you handle potential `KeyError` exceptions.</output>
```

================================================================================



--- Feedback Report for: B25EC013_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Be cautious of off-by-one errors when iterating over dictionary values, as Python's dictionary iteration order may not be what you expect. Consider using the `.items()` method to iterate over key-value pairs directly instead.
</output>
```

================================================================================



--- Feedback Report for: B25CS018_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows you to specify a default value to return if the key is not found.</output>
```

================================================================================



--- Feedback Report for: B25EE036_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure the value is in the dictionary before using it as a key, e.g., `if value not in dict`, to avoid potential issues with duplicate values or incorrect assignments.
</output>
```

================================================================================



--- Feedback Report for: B25ME019_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access and assign dictionary values, which allows you to specify a default value if the key does not exist.</output>
```

================================================================================



--- Feedback Report for: B25EE023_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to swap keys and values correctly, using `k` for keys and `v` for values in the new dictionary, not the other way around.
</output>
```

================================================================================



--- Feedback Report for: B25ME031_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that the inverted key-value pair exists in both the original and new dictionaries to avoid potential KeyError.</output>
```

================================================================================



--- Feedback Report for: B25DS001_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS001_q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS001_q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS001_q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS001_q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS001_q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure the function name 'invert_dict' matches the one used in the problem statement, as the error suggests a mismatch between the function name and its location.</output>
```

================================================================================



--- Feedback Report for: B25CS032_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Be cautious of modifying the dictionary `d` directly within the loop, as this can cause unexpected behavior and incorrect results.</output>
```

================================================================================



--- Feedback Report for: S25MA008  Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which allows you to specify a default value to return if the key is not found.</output>
```

================================================================================



--- Feedback Report for: B25EE025_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as a key, which are unique and not present as keys in the original dictionary, causing an empty inverted dictionary.
</output>
```

================================================================================



--- Feedback Report for: B25MT008_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure that the key exists in the original dictionary before using it as a value in the inverted dictionary, e.g., `inverse_d.update({v[i]: k[i] if v[i] in d else None})`.
</output>
```

================================================================================



--- Feedback Report for: B25EE034_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider modifying your code to use dictionary comprehension, as it can simplify the process of swapping keys and values.</output>
```

================================================================================



--- Feedback Report for: B25CS060_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check for duplicate values in the original dictionary and handle them accordingly, as swapping keys with identical values could lead to ambiguity in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25ME057_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the value is not already a key in the new inverted dictionary before assigning it, e.g., `if value not in invert:`</output>
```

================================================================================



--- Feedback Report for: B25EE012_q14,py ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows you to specify a default value to return if the key is not found in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25MM012_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict` method `.get()` instead of direct assignment to access and assign dictionary values, e.g., `inverted[value] = key`, to avoid potential KeyError.</output>
```

================================================================================



--- Feedback Report for: B25ME046_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you are using `value` as keys, which are unique values from the original dictionary, instead of using the original keys. Try swapping the assignment order: `new_dict[key] = value`.
</output>
```

================================================================================



--- Feedback Report for: B25MT001_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `The reversed dictionary is {1: 'a', 2: 'b'}
The reversed dictionary is {1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `The reversed dictionary is {1: 'a', 2: 'b'}
The reversed dictionary is {'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `The reversed dictionary is {1: 'a', 2: 'b'}
The reversed dictionary is {}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `The reversed dictionary is {1: 'a', 2: 'b'}
The reversed dictionary is {10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `The reversed dictionary is {1: 'a', 2: 'b'}
The reversed dictionary is {'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding error handling to your function to ensure that keys exist in the original dictionary before trying to assign them as values in the reversed dictionary.</output>
```

================================================================================



--- Feedback Report for: B25ME011_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert_dict should iterate over the items in d using 'for key, value in d.items():', not 'for keys, values in d.items():'.</output>
```

================================================================================



--- Feedback Report for: B25EC015_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 3
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Be cautious of the order in which you're iterating and updating the dictionary, as this could result in unexpected key-value pairs.</output>
```

================================================================================



--- Feedback Report for: B25MT032_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `dict` constructor and providing a function that takes a value as a key and returns the corresponding original key, or raise a ValueError if no such key exists.
</output>
```

================================================================================



--- Feedback Report for: B25EE055_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `a[d[i]] = i`, where you're using the value from the original dictionary as a key in the inverted dictionary, potentially causing collisions and incorrect assignments. Consider adding a check to ensure that each value is unique before assigning it to the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25DS016_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using `dict.get()` method to access dictionary values instead of indexing with a variable, as this approach can lead to an off-by-one error.</output>
```

================================================================================



--- Feedback Report for: B25ME008_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `dict.get()` method or checking if a key exists before trying to assign a value, e.g., `inverted[key] = value`.
</output>
```

================================================================================



--- Feedback Report for: B25EE016_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values by using `key` for new key and `value` for new value in the dictionary comprehension.</output>
```

================================================================================



--- Feedback Report for: B25EE057_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows providing a default value if the key is not present.</output>
```

================================================================================



--- Feedback Report for: B25ME049_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `inverted[value] = key`, where you're using the value as a key, which might not exist in the inverted dictionary. Instead, consider using the `dict.setdefault()` method to assign a default value if the key doesn't exist.
</output>
```

================================================================================



--- Feedback Report for: B25EE019_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the assumption that all values are unique and hashable, which may not be the case for dictionaries with duplicate keys or non-hashable values. Always check if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25EE050_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're iterating over the items of the original dictionary (`d.items()`) and then using `key` as the value and vice versa, which is not what we want. Instead, you should use a conditional statement to check if the key exists before trying to access it.
</output>
```

================================================================================



--- Feedback Report for: B25MT019_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the incorrect initialization of the new dictionary `di`, which is initialized as an empty dictionary but assigned a value from the input dictionary `d` without checking for duplicate keys, leading to potential loss of data.
</output>
```

================================================================================



--- Feedback Report for: B25EC038_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values using dictionary comprehension instead of nested loops.</output>
```

================================================================================



--- Feedback Report for: B25DS028_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're iterating over the keys of the original dictionary `d`, but you should be iterating over its values instead, as per the problem's requirement to "swap keys and values". Try changing `for i in d:` to `for value in d.values():`.
</output>
```

================================================================================



--- Feedback Report for: B25DS029_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `inverted[v] = k`, where you're using the value (`v`) as a key, which is not unique and can lead to overwriting existing keys. Instead, use the key (`k`) as the value.
</output>
```

================================================================================



--- Feedback Report for: B25MT026_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as a key, which is a duplicate value from the original dictionary, causing collisions and incorrect assignments. Instead, consider using the original keys to access the values.
</output>
```

================================================================================



--- Feedback Report for: B25CS012_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the value exists in the inverted dictionary before using it as a key, as this could lead to a KeyError.
</output>
```

================================================================================



--- Feedback Report for: B25DS041_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swapping keys and values in the original dictionary without considering potential collisions (e.g., duplicate values) could lead to incorrect results, as the same value might be reassigned to different keys.</output>
```

================================================================================



--- Feedback Report for: B25MT023-Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each unique value in the original dictionary is present as a key in the inverted dictionary, to avoid potential KeyError.</output>
```

================================================================================



--- Feedback Report for: B25ME029_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're updating the new dictionary, as `values[i]` is being used as both a key and a value; instead, consider using the index `i` to access the corresponding values.
</output>
```

================================================================================



--- Feedback Report for: B25EE021_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `.items()` method, which returns a list-like object of tuples containing key-value pairs, and then use a dictionary comprehension to swap keys and values.
</output>
```

================================================================================



--- Feedback Report for: B25CS062_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as both a key and a value, which is causing duplicate keys in your new dictionary. Consider using a different approach, such as checking if a key exists before trying to use it.
</output>
```

================================================================================



--- Feedback Report for: B25MT025_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The student's code is swapping keys and values correctly, but it should also handle cases where the input dictionary has duplicate values. The advice hints at a potential issue with loop constructs, which in this case might be related to the use of `d.items()` instead of iterating over unique values.
</output>
```

================================================================================



--- Feedback Report for: B25DS021_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS021_q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS021_q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS021_q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS021_q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25DS021_q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using a set to keep track of unique values instead of relying on the dictionary's built-in uniqueness, as this approach assumes that all values are hashable.</output>
```

================================================================================



--- Feedback Report for: B25DS004_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the value exists in the new dictionary before using it as a key, as this could lead to unexpected behavior or errors when dealing with duplicate values.
</output>
```

================================================================================



--- Feedback Report for: B25MM016_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM016_Q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM016_Q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM016_Q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM016_Q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM016_Q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are correctly iterating over the dictionary's values instead of keys in the loop construct.
</output>
```

================================================================================



--- Feedback Report for: B25EE051_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the dictionary before using it, as the current implementation may raise a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25DS019_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you're correctly handling duplicate values by using a data structure like a set or dictionary to keep track of unique keys, and consider adding an if-else statement to handle such cases accurately.
</output>
```

================================================================================



--- Feedback Report for: B25ME041_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're iterating over keys, but when creating the inverted dictionary, you should be using values as keys and keys as values. Try swapping `key` and `value` in your assignment.
</output>
```

================================================================================



--- Feedback Report for: B25EC007_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The issue lies in the fact that you're using the value as the key, but dictionaries require unique keys; using a value that already exists will overwrite any previous assignment.
```

================================================================================



--- Feedback Report for: B25EC006_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if a key exists in the dictionary before trying to assign a value to it, as the current implementation will raise a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25EC026_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The loop iterates over each key in the dictionary, but it should also include values that have unique keys, not just keys. Consider using a set to keep track of unique keys and only update the reverse dictionary with those keys.
</output>
```

================================================================================



--- Feedback Report for: s25ma010_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try iterating over the dictionary's items instead of just its keys, and check if each value is present in the original dictionary before assigning it to the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC009_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `p.update({j: i})`, where you're updating the dictionary with keys that are actually values from the original dictionary. This is causing duplicate keys and incorrect assignments. Instead, use a conditional statement to check if the key already exists before assigning it.
</output>
```

================================================================================



--- Feedback Report for: B25EC034_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure that duplicate values are handled correctly in the inverted dictionary, as your current implementation may overwrite existing keys with new ones.</output>
```

================================================================================



--- Feedback Report for: (B25DS042)_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{2: 'a', 4: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{2: 'a', 4: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{2: 'a', 4: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{2: 'a', 4: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{2: 'a', 4: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the condition `d[keys]` is correctly accessing the value in the dictionary, as it should be `d.get(keys)` to avoid a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25EC012_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the value as the new key and the original key as the new value, but also consider handling duplicate values correctly to avoid overwriting existing keys in the new dictionary.
</output>
```

================================================================================



--- Feedback Report for: B25MM002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM002_q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM002_q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM002_q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM002_q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25MM002_q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if your function is correctly handling cases where a dictionary value appears more than once, and ensure that you're using the correct data structure to store the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC044_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each unique value in the original dictionary is used as a key in the inverted dictionary, and vice versa.</output>
```

================================================================================



--- Feedback Report for: B25ME018_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the assumption that all values are unique and hashable, which is not guaranteed by the problem statement. You should check if a key exists before trying to assign a value to it.</output>
```

================================================================================



--- Feedback Report for: B25DS027_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values in a dictionary using a conditional statement to handle unique values.</output>
```

================================================================================



--- Feedback Report for: B25EC011_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the assumption that all values are unique and hashable, which is not guaranteed by the problem statement, leading to potential errors when swapping keys and values.</output>
```

================================================================================



--- Feedback Report for: B25MM008_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Consider adding a check to ensure the value is present in the original dictionary before using it as a key in the inverted dictionary, e.g., `if value not in d: raise ValueError(f"Value '{value}' not found in original dictionary")`.
</output>
```

================================================================================



--- Feedback Report for: B25MT002_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Reversing the keys and values in the dictionary requires checking if each value already exists as a key in the new dictionary before assigning the corresponding key. Consider using the `get()` method or a set to ensure uniqueness.
</output>
```

================================================================================



--- Feedback Report for: B25MT011.q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25MT011'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're iterating over the dictionary's values and keys simultaneously, which causes unexpected behavior due to the modification of the dictionary during iteration. Consider using an iterator or a different approach to swap key-value pairs.
</output>
```

================================================================================



--- Feedback Report for: B25CS044_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which returns `None` if the key is not present, instead of directly assigning a value to a non-existent key.</output>
```

================================================================================



--- Feedback Report for: B25EE030-q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The function should use a conditional statement to check if each value is unique, and only add it to the new dictionary if no other key maps to it.
</output>
```

================================================================================



--- Feedback Report for: B25EE026_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're iterating over the keys and values, which is causing an incorrect assignment of values to keys. Consider using dictionary's built-in methods like `items()` or `get()` instead.
</output>
```

================================================================================



--- Feedback Report for: B25EE017_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: ['a'], 2: ['b']}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'v1': ['k1']}`
- Test 'empty': PASS
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{10: ['x'], 20: ['y'], 30: ['z']}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'a': [1], 'b': [2], 'c': [3]}`

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `h.setdefault(v, []).append(k)`, where you're appending keys to a list associated with values. Instead, consider using a dictionary comprehension to create a new inverted dictionary directly.
</output>
```

================================================================================



--- Feedback Report for: B25CS020_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that each unique value in the original dictionary is present as a key in the inverted dictionary, and handle cases where this condition is not met.</output>
```

================================================================================



--- Feedback Report for: B25DS005_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as a key, which might not exist in the original dictionary, causing an error. Instead, consider using `key` as the new value and `value` as the new key.
</output>
```

================================================================================



--- Feedback Report for: B25EE013_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `get()` method, which returns the value for a given key if it exists in the dictionary; otherwise, it returns None. This ensures that you don't try to use a non-existent key.
</output>
```

================================================================================



--- Feedback Report for: B25EC005_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[FUNC ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[FUNC ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[FUNC ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[FUNC ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[FUNC ERROR] TypeError: 'builtin_function_or_method' object is not iterable
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to iterate over the dictionary's values as individual elements, not as attributes of an object (d.items), which is why you're encountering a TypeError. Use `for v in d.values()` instead.
</output>
```

================================================================================



--- Feedback Report for: B25DS034_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by using the `dict` constructor and providing the key-value pairs as keyword arguments, ensuring that each value is unique.
</output>
```

================================================================================



--- Feedback Report for: B25MM026_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try swapping the assignment order in `inverted[value] = key` to `inverted[key] = value` to correctly invert the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC008_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as keys, which are likely unique values from the original dictionary, instead of using the actual keys. Try using `key` as the new key and `value` as the new value.
</output>
```

================================================================================



--- Feedback Report for: B25DS006_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap keys and values in the dictionary using a conditional statement to check for uniqueness of values.</output>
```

================================================================================



--- Feedback Report for: B25MT018_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the value exists in the dictionary before using it as a key, as in `dict.get(value)`, instead of directly assigning `key` to `value`.
</output>
```

================================================================================



--- Feedback Report for: B25MM028_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which allows you to specify a default value to return if the key does not exist.</output>
```

================================================================================



--- Feedback Report for: B25EE033_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you check if the inverted key exists in the new dictionary before using it, as the current implementation may result in a KeyError.
</output>
```

================================================================================



--- Feedback Report for: B25EC020_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25EC020_q14'.
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25EC020_q14'.
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25EC020_q14'.
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25EC020_q14'.
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Function 'invert_dict' not found in module 'B25EC020_q14'.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the key exists in the dictionary before trying to assign a value to it, as using a non-existent key may raise an AttributeError.
</output>
```

================================================================================



--- Feedback Report for: B25CS047_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the original dictionary before trying to swap it with its value.</output>
```

================================================================================



--- Feedback Report for: B25ME048_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the inverted dictionary's keys exist in the original dictionary before using them as keys, as this could lead to KeyError.
</output>
```

================================================================================



--- Feedback Report for: B25EE049_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check that the values in the input dictionary are hashable, as non-hashable types like lists or dictionaries cannot be used as keys in a dictionary.</output>
```

================================================================================



--- Feedback Report for: B25CS045_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you are correctly swapping key-value pairs, and consider using a conditional statement to handle cases where values might be duplicates or non-unique in the original dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC028_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a'}
{'v1': 'k1'}
{1: 'a'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a'}
{'v1': 'k1'}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a'}
{'v1': 'k1'}
{10: 'x'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a'}
{'v1': 'k1'}
{'a': 1}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which returns `None` by default if the key is not found.</output>
```

================================================================================



--- Feedback Report for: S25MA018_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert the dictionary by swapping keys and values, but also consider handling cases where duplicate values exist, as your current implementation will overwrite existing keys with the last encountered value.
</output>
```

================================================================================



--- Feedback Report for: b25cs040.q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'b25cs040'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Try using the `get()` method instead of direct assignment, e.g., `return {v: k for k, v in d.items() if k in d}`, to avoid a KeyError when swapping keys and values.</output>
```

================================================================================



--- Feedback Report for: B25ME051_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as a key, which might not be unique in your original dictionary. Try using a different approach, such as using a set to ensure uniqueness or handling cases where values are not present in the new dictionary.
</output>
```

================================================================================



--- Feedback Report for: B25ME012_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `val = d[i]`, where you're using the value as an index, but dictionaries are unordered data structures and do not guarantee unique values. You should be using a different approach to handle duplicate values.
</output>
```

================================================================================



--- Feedback Report for: B25CS011_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the inverted dictionary's keys are unique, as your current implementation may result in duplicate keys.</output>
```

================================================================================



--- Feedback Report for: S25MA001__q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{'value': 'key', 'tum': 'mai'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'value': 'key', 'tum': 'mai'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{'value': 'key', 'tum': 'mai'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{'value': 'key', 'tum': 'mai'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'value': 'key', 'tum': 'mai'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the keys and values are being swapped correctly by iterating over the dictionary items instead of directly using dictionary comprehension, which can lead to incorrect results when dealing with duplicate values.</output>
```

================================================================================



--- Feedback Report for: B25EE056_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `new_dict[d[item]] = item`, where you're using the value as a key, potentially causing duplicates and incorrect assignments. Consider checking if the key already exists before assigning a new value to it.
</output>
```

================================================================================



--- Feedback Report for: B25EE003_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the original dictionary before using it as a value in the inverted dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC043_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check if the value exists in the dictionary before using it as a key, as this could lead to unexpected behavior or errors when assigning keys that don't exist.
</output>
```

================================================================================



--- Feedback Report for: B25CS021_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Invert dictionary by iterating over unique values instead of keys, as the current implementation swaps keys with their corresponding indices in the original dictionary.
</output>
```

================================================================================



--- Feedback Report for: B25EC045_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `in` keyword to check if a key exists in the new dictionary before trying to assign its value, e.g., `if value not in dic: dic[value] = key`. This will prevent potential issues with duplicate keys.</output>
```

================================================================================



--- Feedback Report for: B25DS015_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap values and keys in the dictionary, but currently, you're using the value as the new key and the original key as the new value. Try swapping them instead.</output>
```

================================================================================



--- Feedback Report for: B25EC041_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Swap the order of key-value pairs in the dictionary comprehension.</output>
```

================================================================================



--- Feedback Report for: B25DS032_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The issue lies in the fact that you're using `values` as both the value and the key in your dictionary comprehension, which is causing the incorrect assignment of values. Instead, consider using a variable to store the unique values and then swap them with the keys.
```

================================================================================



--- Feedback Report for: B25EC021_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure the key exists in the original dictionary before using its value, as your current implementation may result in a KeyError.</output>
```

================================================================================



--- Feedback Report for: B25CS034_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the inverted dictionary has unique values by ensuring that each key is not duplicated and that no value is assigned more than once.</output>
```

================================================================================



--- Feedback Report for: B25MT014_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the inverted dictionary's keys exist in the original dictionary before using them as values, as this could lead to KeyError.
</output>
```

================================================================================



--- Feedback Report for: B25MM025_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're using `zip` on dictionary values and keys; instead, consider iterating over the dictionary's items directly with `.items()`, ensuring each key-value pair is processed correctly before swapping them.
</output>
```

================================================================================



--- Feedback Report for: B25DS043_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Try using the `get()` method of dictionaries, which allows you to specify a default value to return if the key is not present in the dictionary. For example: `inverted[value] = key or inverted.setdefault(value, key)`.
</output>
```

================================================================================



--- Feedback Report for: B25DS008_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `dd[v] = k`, where you're using the value (`v`) as a key, which might not exist in the dictionary. Instead, consider using the original key (`k`) to access the corresponding value.
</output>
```

================================================================================



--- Feedback Report for: B25DS039_Q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that the value is not already in the new dictionary before using it as a key, as this could lead to duplicate keys and incorrect results.</output>
```

================================================================================



--- Feedback Report for: B25ME017_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're iterating over the dictionary's items and using the values as keys in the new dictionary, which is not what we want. Instead, you should be using each unique value as a key and its corresponding original key as the value.
</output>
```

================================================================================



--- Feedback Report for: B25CS054_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're iterating over the dictionary items, where 'key' and 'val' are being swapped, instead of using the original key-value pairs directly. Try changing `for key, val` to `for key, val in key_val`.
</output>
```

================================================================================



--- Feedback Report for: B25MT024_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the value as a key, which is not unique, causing unexpected behavior when trying to invert the dictionary. Consider using a set to ensure uniqueness of values before proceeding with the inversion.
</output>
```

================================================================================



--- Feedback Report for: B25EE022_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that the value is not already a key in the new dictionary before using it as a key.</output>
```

================================================================================



--- Feedback Report for: B25ME009_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are correctly handling duplicate values in the input dictionary, as your current implementation will overwrite existing keys with new ones.</output>
```

================================================================================



--- Feedback Report for: B25CS037_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: ['a'], 2: ['b']}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'v1': ['k1']}`
- Test 'empty': PASS
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{10: ['x'], 20: ['y'], 30: ['z']}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'a': [1], 'b': [2], 'c': [3]}`

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `dict.get()` method to access dictionary values, which allows you to specify a default value to return if the key is not found in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25ME001_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method to access dictionary values, which allows you to specify a default value if the key is not present in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EC035_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Review your code and ensure that you are swapping keys and values correctly. Specifically, verify that you are using the original key to store the inverted value, rather than reusing the same value as a new key.</output>
```

================================================================================



--- Feedback Report for: B25ME014_q14.py ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25ME014_q14'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25ME014_q14'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25ME014_q14'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25ME014_q14'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25ME014_q14'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the dictionary before using it, as the current code will throw an error when trying to swap keys and values.</output>
```

================================================================================



--- Feedback Report for: B25ME010_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using the original keys as new values and vice versa, but when accessing or assigning dictionary values, you should check if the key exists before trying to use it. Consider using the `dict.get()` method or a conditional statement to handle this.
</output>
```

================================================================================



--- Feedback Report for: B25DS017_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{1: 'a', 2: 'b'}
{'v1': 'k1'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `value` as keys, which are unique, but not all values might be present in the original dictionary. You should instead use `key` as keys and store their corresponding values.
</output>
```

================================================================================



--- Feedback Report for: B25ME045_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try using the `get()` method instead of direct assignment, which allows you to specify a default value if the key does not exist in the dictionary.</output>
```

================================================================================



--- Feedback Report for: B25EE024_q14.py ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE024_q14'
```
- Test 'single_item': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE024_q14'
```
- Test 'empty': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE024_q14'
```
- Test 'multiple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE024_q14'
```
- Test 'numeric_keys': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER SETUP ERROR] ModuleNotFoundError: No module named 'B25EE024_q14'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the line `h[d[k]] = k`, where you're using the value from the original dictionary as a key in the inverted dictionary. Instead, try using the key itself as the new value.
</output>
```

================================================================================



--- Feedback Report for: B25EE028_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a check to ensure that the value is unique in the result dictionary before using it as a key, as this could lead to collisions and incorrect results.</output>
```

================================================================================



--- Feedback Report for: B25MM006_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you're correctly mapping values to keys, considering cases where a value might be unique and need to be mapped to all other keys.
</output>
```

================================================================================



--- Feedback Report for: B25ME039_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': FAIL
  - Expected: `{1: 'a', 2: 'b'}`
  - Your output: `{'s': 'a', 'r': 'b', 't': 'd'}
{1: 'a', 2: 'b'}`
- Test 'single_item': FAIL
  - Expected: `{'v1': 'k1'}`
  - Your output: `{'s': 'a', 'r': 'b', 't': 'd'}
{'v1': 'k1'}`
- Test 'empty': FAIL
  - Expected: `{}`
  - Your output: `{'s': 'a', 'r': 'b', 't': 'd'}
{}`
- Test 'multiple': FAIL
  - Expected: `{10: 'x', 20: 'y', 30: 'z'}`
  - Your output: `{'s': 'a', 'r': 'b', 't': 'd'}
{10: 'x', 20: 'y', 30: 'z'}`
- Test 'numeric_keys': FAIL
  - Expected: `{'a': 1, 'b': 2, 'c': 3}`
  - Your output: `{'s': 'a', 'r': 'b', 't': 'd'}
{'a': 1, 'b': 2, 'c': 3}`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Swap the assignment order in the for loop from 'm, n' to 'n, m', so that keys are assigned values and vice versa.
</output>
```

================================================================================



--- Feedback Report for: B25EE044_q14 ---
Assignment: csl100_q14

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'simple': PASS
- Test 'single_item': PASS
- Test 'empty': PASS
- Test 'multiple': PASS
- Test 'numeric_keys': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
You are likely missing the `.invert()` method in your code, which is necessary to swap keys and values correctly.
</output>
```

================================================================================
