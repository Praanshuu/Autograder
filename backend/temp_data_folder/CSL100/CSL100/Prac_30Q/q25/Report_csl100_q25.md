# Autograder - Aggregated Feedback Report
## Assignment: csl100_q25



--- Feedback Report for: B25EC042_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'L'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'L'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'L'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'L'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'L'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the implementation of the `pop` method, which is accessing the 'L' attribute without defining it as a list. The correct implementation should use the 'self.stack' attribute instead.
</output>
```

================================================================================



--- Feedback Report for: B25ME002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.lst` instead of just `lst` in your methods, as `self.lst` refers to the list attribute of the class instance, whereas `lst` is a local variable.</output>
```

================================================================================



--- Feedback Report for: B25EE045_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 0

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE045_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE045_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE045_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE045_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE045_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

- Technical summary was not generated.

================================================================================



--- Feedback Report for: B25DS041_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the instance of the class, not just a variable.</output>
```

================================================================================



--- Feedback Report for: B25DS014_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `pop` method, where you are trying to access `self.stack`, but it seems like `stack` is not a class attribute. Instead, consider using `self._elements` (assuming this is your internal stack data structure) and modify the method accordingly.
</output>
```

================================================================================



--- Feedback Report for: B25CS048_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in methods like `push`, `pop`, etc., as it's a part of the class and not a global variable.</output>
```

================================================================================



--- Feedback Report for: B25EE044_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25ME006_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are calling the pop operation on an empty list by adding a condition to check for the size of the stack before popping an item, e.g., `if self.size() > 0:`.
</output>
```

================================================================================



--- Feedback Report for: B25MM004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use 'self' when calling instance methods, as in `def push(self, item): self.items.append(item)` instead of just `def push(item): self.items.append(item)`, and similarly for other operations like pop, peek, is_empty, and size.</output>
```

================================================================================



--- Feedback Report for: B25DS017_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` as the first parameter when defining methods in your class, like so: `def __init__(self): self.L = []`. This ensures that methods are called on an instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25ME047_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the instance of the class. For example, instead of `s.push(item)`, use `self.s.push(item)`.</output>
```

================================================================================



--- Feedback Report for: B25MT003_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing and modifying the list within a class method, as it refers to the instance variable.</output>
```

================================================================================



--- Feedback Report for: B25EE004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using the `self` parameter when calling methods within the class, as it may be missing or incorrectly used in your code.</output>
```

================================================================================



--- Feedback Report for: B25EE009_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you're using 'none' as a type in Python; instead, use None (with a capital 'N').</output>
```

================================================================================



--- Feedback Report for: B25EE056_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[[1], 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Remember to add the `pop` method to your class by using `self.List.pop()` instead of just `self.List`, as lists in Python have a built-in `pop` method.</output>
```

================================================================================



--- Feedback Report for: B25EE050_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use 'self' when calling methods within your class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25DS030_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has one or more Syntax Errors.
- Syntax Error: invalid syntax at line 14, offset 36

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25DS030_q25.py, line 14)
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25DS030_q25.py, line 14)
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25DS030_q25.py, line 14)
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25DS030_q25.py, line 14)
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25DS030_q25.py, line 14)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `append` correctly in your `push` method and ensure it's not overwriting the entire list instead of just adding a new item.</output>
```

================================================================================



--- Feedback Report for: B25EE018_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'none' is not defined
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
When initializing the Stack class, you are checking for `None` instead of `None`, which should be lowercase. Change `self.items = []` to `self.items = None`.
</output>
```

================================================================================



--- Feedback Report for: B25EC006_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when accessing attributes of the class in a static method, as it's not directly passed to the method like in instance methods. Instead, access the class attribute using the class name.
</output>
```

================================================================================



--- Feedback Report for: B25DS005_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.lst` instead of just `lst` when accessing the list inside the methods, as it's a reference to the instance variable and not a local variable. For example, in your `push` method, use `self.lst.append(item)` instead of `lst.append(item)`.
</output>
```

================================================================================



--- Feedback Report for: B25ME034_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `items` is a built-in Python variable that can cause unexpected behavior.</output>
```

================================================================================



--- Feedback Report for: B25ME016_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `True
20
20
1
10
None
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `True
20
20
1
10
None
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `True
20
20
1
10
None
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `True
20
20
1
10
None
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `True
20
20
1
10
None
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your `push`, `pop`, and `peek` methods to access the list correctly.</output>
```

================================================================================



--- Feedback Report for: B25CS059_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25DS013_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try initializing the stack as an empty list instead of a default argument, which can lead to unexpected behavior when using a class method.</output>
```

================================================================================



--- Feedback Report for: B25DS018_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `self` correctly when implementing methods like `push`, `pop`, and `peek`. Ensure these methods modify or access the `items` list attribute of the class instance.</output>
```

================================================================================



--- Feedback Report for: B25CS042_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as `lst` should be accessed through the class context (`self`).</output>
```

================================================================================



--- Feedback Report for: B25MT007_ q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT007_ q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT007_ q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT007_ q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT007_ q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT007_ q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` as the first parameter when defining your class methods, like in a typical Python class implementation (e.g., `def push(self, item): self.L.append(item)`).
</output>
```

================================================================================



--- Feedback Report for: B25ME014_q25.py ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q25'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q25'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q25'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q25'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q25'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods on an instance of your Stack class, as it's a reference to the current object and necessary for accessing its attributes. For example, instead of `B25ME014_q25`, try using `self.items`.
</output>
```

================================================================================



--- Feedback Report for: B25MM009(q25) ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Stack class is missing a list to store elements, so it should initialize 'self.items' as an empty list.</output>
```

================================================================================



--- Feedback Report for: S25MA016_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `None
10
None
0
True
0
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `None
10
None
0
True
0
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `None
10
None
0
True
0
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `None
10
None
0
True
0
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
10
None
0
True
0
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in the `push`, `pop`, and `peek` methods, as they are class attributes that need to be accessed through the instance.</output>
```

================================================================================



--- Feedback Report for: B25EC013_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as Python looks for a local variable with that name by default.</output>
```

================================================================================



--- Feedback Report for: B25MT005_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.item` instead of just `item` in your methods, as you are referencing the class attribute inside a class method.</output>
```

================================================================================



--- Feedback Report for: B25ME051_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `items` is a built-in function in Python and will not be accessible within a class method.</output>
```

================================================================================



--- Feedback Report for: B25CS010_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that the `push` operation appends elements to the list instead of overwriting the existing data, as shown below: `self.data.append(element)`.
</output>
```

================================================================================



--- Feedback Report for: B25MM026_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your Stack class, as it refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25ME024_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `len(self.items)` instead of `self.size` in your implementation, as Python does not have a built-in `size` attribute for lists.</output>
```

================================================================================



--- Feedback Report for: B25EE021_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The `pop` method should return the top element without removing it, so consider changing `return self.L.pop()` to `self.L.pop()`.
</output>
```

================================================================================



--- Feedback Report for: B24DS035_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your Stack class's methods, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25ME012_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize the list with None, not an empty list, in your `__init__` method to avoid index errors when popping or peeking at elements.</output>
```

================================================================================



--- Feedback Report for: B25DS031_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider adding a `self` parameter to the `__init__` method to initialize the list as an attribute of the instance, not just a local variable.</output>
```

================================================================================



--- Feedback Report for: B25MM013_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize the list with a non-empty value in the __init__ method and also check if the list is not empty before popping an element.</output>
```

================================================================================



--- Feedback Report for: B25ME019_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `b
False
2
[null, null, null, null, 20, 2, false, null, null, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `b
False
2
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `b
False
2
The Stack is empty.
[null, null, 2, null, null, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `b
False
2
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
When initializing your Stack class, you should not directly access or modify the `self.stack` list within the `__init__` method. Instead, consider using a separate method to initialize the stack, such as `initialize_stack()`, and call it in the `__init__` method.
</output>
```

================================================================================



--- Feedback Report for: B25ME057_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE024_q25.py ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q25'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q25'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q25'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q25'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q25'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The issue lies in the incorrect usage of the `__init__` method, as it should be `self.item = []` instead of just `self.item`, and also ensure that the module name is correct, which seems to be a typo.
```

================================================================================



--- Feedback Report for: B25MM018_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
False
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
False
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
False
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
False
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as the `items` attribute is not automatically passed by default.</output>
```

================================================================================



--- Feedback Report for: {B25MM017}_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25MM017}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25MM017}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25MM017}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25MM017}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25MM017}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling the methods inside your `__init__` method, as it's a common gotcha in Python classes. For example, instead of `items = []`, try `self.items = []`.
</output>
```

================================================================================



--- Feedback Report for: B25CS005_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `[null, null, 2, 7, 5, "Stack is empty"]`
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're using `append` to add elements to the stack, which changes the order of the list, whereas a stack should maintain the LIFO (Last In First Out) order. You should use `insert(0, element)` instead.
</output>
```

================================================================================



--- Feedback Report for: B25MT027_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.l` instead of just `l` when accessing the list in your methods, as `self` refers to the instance of the class and should be used to access its attributes.</output>
```

================================================================================



--- Feedback Report for: B25EC001_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'isEmpty'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'isEmpty'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'isEmpty'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling class methods, such as `is_empty()` and `size()`, by prefixing them with `self.`</output>
```

================================================================================



--- Feedback Report for: B25ME031_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[null, null, null, null, 20, 2, false, null, null, true]`
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the stack with at least one element in the `__init__` method, so it's not empty when trying to pop from it.</output>
```

================================================================================



--- Feedback Report for: B25EC004_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling instance methods, as in `self.items.append(item)`, not just `items.append(item)`.</output>
```

================================================================================



--- Feedback Report for: B25ME008_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[null, null, null, null, 20, 2, false, null, null, true]`
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you are checking for an empty list before attempting to pop from it, as the IndexError suggests that the stack is indeed empty when trying to remove an element.</output>
```

================================================================================



--- Feedback Report for: B25MT026_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] UnboundLocalError: local variable 'item' referenced before assignment
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] UnboundLocalError: local variable 'item' referenced before assignment
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` as the first parameter when defining methods in a class, as it refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE001_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25MT002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self._items` instead of just `_items` in your `push`, `pop`, and `peek` methods to access the class attribute correctly.</output>
```

================================================================================



--- Feedback Report for: B25ME010_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the instance of the class. For example, instead of `stack.push(item)`, use `self.stack.push(item)`.</output>
```

================================================================================



--- Feedback Report for: B25CS004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` when accessing the list in your methods, as `self` refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS033_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when accessing class attributes, like `self.stack`, in a class method, as it refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE038_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when defining methods within your class, as it refers to the instance of the class itself.</output>
```

================================================================================



--- Feedback Report for: B25DS011_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when accessing the list inside the class methods, as it refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS014_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `items` is a built-in function in Python.</output>
```

================================================================================



--- Feedback Report for: B25DS033_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your push, pop, peek methods to access the list attribute correctly.</output>
```

================================================================================



--- Feedback Report for: B25DS039_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'list' object has no attribute 'is_empty'
```
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `[null, [1]]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'list' object has no attribute 'is_empty'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'list' object has no attribute 'is_empty'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `is_empty` as an attribute of the list directly, instead use a separate method to check for emptiness.</output>
```

================================================================================



--- Feedback Report for: B25CS021_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output> The issue lies in the default value of `stack` being a reference to an empty list (`[]`) instead of a new empty list (`[]`). This means that every time a new instance is created, it's actually referencing the same list as the previous instances. </output>
```

================================================================================



--- Feedback Report for: B25EE007_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
20
10
True
[null, null, null, null, null, null, null, null, null, null]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `1
[null, null]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Initialize the list with a single element instead of an empty list to avoid index out of range error.</output>
```

================================================================================



--- Feedback Report for: B25EE043_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has one or more Syntax Errors.
- Syntax Error: invalid syntax at line 17, offset 32

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EE043_q25.py, line 17)
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EE043_q25.py, line 17)
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EE043_q25.py, line 17)
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EE043_q25.py, line 17)
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EE043_q25.py, line 17)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you're using `+=` instead of `+` in your `size` method to correctly calculate the length of the list.</output>
```

================================================================================



--- Feedback Report for: B25CS041_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your `push`, `pop`, and other methods, as `items` is a variable that only exists within the scope of the class's initializer.</output>
```

================================================================================



--- Feedback Report for: B25CS043-q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS043-q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS043-q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS043-q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS043-q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS043-q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25ME028_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods from within the class, as it refers to the current instance of the class. For example, instead of `stack.pop()`, try using `self.items.pop()`.
</output>
```

================================================================================



--- Feedback Report for: B25EC038_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC038_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC038_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC038_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC038_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC038_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods within the class, as it refers to the instance of the class. For example, instead of `Stack.pop()`, try `self.pop()`.
</output>
```

================================================================================



--- Feedback Report for: b25me058_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as they are class attributes that need to be accessed through the instance (`self`).</output>
```

================================================================================



--- Feedback Report for: B25EC010_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE003_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.items` instead of just `items` when accessing and modifying the list in your methods, as `self` refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25MT025_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the usage of `push` operation, which seems to be missing in your implementation. Make sure to add a `push` method that takes an element as input and adds it to the stack.</output>
```

================================================================================



--- Feedback Report for: B25ME046_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the list with None or an empty string, not just an empty list, when creating a new Stack class.</output>
```

================================================================================



--- Feedback Report for: B25EC018_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25ME027_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
30
2
False
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
30
2
False
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
30
2
False
Stack empty
Stack empty
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
30
2
False
Stack empty
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
30
2
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the instance of the class, not just a generic list.</output>
```

================================================================================



--- Feedback Report for: B25MT020_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are using `self` when calling methods, as it seems to be missing in your implementation.</output>
```

================================================================================



--- Feedback Report for: B25EE019_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Stack class is missing a key attribute to store its elements, which is typically implemented as a list.</output>
```

================================================================================



--- Feedback Report for: B25EE012_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 2
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE012_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE012_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE012_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE012_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE012_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the key exists in the dictionary before trying to access its value.</output>
```

================================================================================



--- Feedback Report for: B25CS008_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your push, pop, and peek methods to access the class attribute.</output>
```

================================================================================



--- Feedback Report for: B25MT015_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are pushing elements onto the stack using `self.items.append()` instead of `self.items.insert(0, item)`, which is typically used for stacks.</output>
```

================================================================================



--- Feedback Report for: B25ME035_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as in `if not self.items:`, instead of just `if not items:`.</output>
```

================================================================================



--- Feedback Report for: B25MT019_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
20
10
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
20
10
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are checking for empty stack before popping an element, as this will prevent the "list index out of range" error.</output>
```

================================================================================



--- Feedback Report for: B25DS001_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider initializing an empty list for storing stack elements inside the `__init__` method, as you've done, but also ensure that the `push`, `pop`, and `peek` operations modify or access the internal data structure correctly.</output>
```

================================================================================



--- Feedback Report for: B25EC009_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use 'self' when calling methods on instances of your Stack class, as in `self.l = []` instead of just `l = []`. Also, ensure that you're using the correct syntax for accessing and modifying instance variables.</output>
```

================================================================================



--- Feedback Report for: B25ME048_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has one or more Syntax Errors.
- Syntax Error: cannot assign to function call here. Maybe you meant '==' instead of '='? at line 18, offset 12

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='? (B25ME048_q25.py, line 18)
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='? (B25ME048_q25.py, line 18)
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='? (B25ME048_q25.py, line 18)
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='? (B25ME048_q25.py, line 18)
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='? (B25ME048_q25.py, line 18)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `append` instead of `=` when pushing items onto the stack in the `push` method.
</output>
```

================================================================================



--- Feedback Report for: S25MA018_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The student's code initializes a list with an empty list as its argument, which leads to a mutable default argument. This causes the list to be created only once when the class is defined, and all instances share the same reference, resulting in the index error when trying to pop from an empty list.
</output>
```

================================================================================



--- Feedback Report for: B25DS002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the instance of the class. For example, instead of `print(items)`, use `print(self.items)`.</output>
```

================================================================================



--- Feedback Report for: B25MT014_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The 'pop' method should also return the top item when the stack is not empty, similar to the 'peek' and 'size' methods.
</output>
```

================================================================================



--- Feedback Report for: B25EE059_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `items` is a built-in Python list data type that can cause unexpected behavior.</output>
```

================================================================================



--- Feedback Report for: B25CS056_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as `lst` is a local variable and not accessible outside the scope of the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25CS002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `The stack is empty.
The stack is empty.
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `The stack is empty.
[null, null, 2, 7, 5, null]`
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as Python looks for a local variable with that name first.</output>
```

================================================================================



--- Feedback Report for: B25EE053_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `self` when calling methods on your Stack class, as it's likely that `peek()` should be accessing `self._items[-1]` instead of just `_items[-1]`. This would cause an IndexError because the index is out of range.</output>
```

================================================================================



--- Feedback Report for: B25ME032_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'list'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Stack.is_empty() takes 0 positional arguments but 1 was given
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'list'
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as `self` refers to the instance of the class and should be used when accessing its attributes.</output>
```

================================================================================



--- Feedback Report for: B25ME011_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are correctly using self to access the class attributes in your methods, especially in push, pop, and peek operations.</output>
```

================================================================================



--- Feedback Report for: B25EE029_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as `self` is a reference to the current instance of the class and should be used to access its attributes.</output>
```

================================================================================



--- Feedback Report for: B25ME018_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods.</output>
```

================================================================================



--- Feedback Report for: B25DS0004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'lis'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'lis'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'lis'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'lis'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to access the 'lis' attribute correctly in the `pop` method by using self.lis[-1] instead of self.lis[len(self.lis) - 1], as list indices in Python start at 0, not 1.
</output>
```

================================================================================



--- Feedback Report for: B25CS051_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the list with None instead of an empty list, so that the index error doesn't occur when popping from an empty stack.</output>
```

================================================================================



--- Feedback Report for: B25MM001_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM001_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM001_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM001_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM001_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM001_Q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to create an instance of the Stack class before calling any methods, as `Stack` is a class name and not a standalone function.</output>
```

================================================================================



--- Feedback Report for: B25EE013_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use 'self' when calling methods within your class, as it refers to the instance itself.</output>
```

================================================================================



--- Feedback Report for: B25EC028_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the stack with an empty list and also check if the list is not empty before popping an element from it in the pop operation.</output>
```

================================================================================



--- Feedback Report for: B25ME059_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're initializing and using the list in your `__init__` method; instead of creating a new empty list, consider using `self.list1 = []`.
</output>
```

================================================================================



--- Feedback Report for: B25EC032_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing and modifying the list in your methods.</output>
```

================================================================================



--- Feedback Report for: B25MM025_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 0

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM025_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM025_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM025_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM025_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM025_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

- Technical summary was not generated.

================================================================================



--- Feedback Report for: B25CS053_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `20
20
1
False
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `20
20
1
False
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `20
20
1
False
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `20
20
1
False
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `20
20
1
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25DS016_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as it's a reference to the instance variable.</output>
```

================================================================================



--- Feedback Report for: B25EE035_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25MT024_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as it's a reference to the instance variable and not a local variable within the method.</output>
```

================================================================================



--- Feedback Report for: B25EE054_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your push, pop, and peek methods to access the list correctly.</output>
```

================================================================================



--- Feedback Report for: B25CS016_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `[null, null, 2, 7, 5, "Stack is empty"]`
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `append()` instead of indexing directly when adding elements to the stack.</output>
```

================================================================================



--- Feedback Report for: B25MT004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT004_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT004_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT004_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT004_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MT004_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods inside the class definition, as shown in the corrected code: `def __init__(self): self.L = []`. This ensures that the method is being called on an instance of the class.
</output>
```

================================================================================



--- Feedback Report for: B25EE039_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your push, pop, and peek methods, as they need to access the instance variable.</output>
```

================================================================================



--- Feedback Report for: B25EC008_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to check if the list is empty before attempting to pop an element from it.</output>
```

================================================================================



--- Feedback Report for: B25MM023_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` as the first parameter when defining methods in your Stack class, like so: `def push(self, item): self.items.append(item)`, and similarly for other methods.</output>
```

================================================================================



--- Feedback Report for: B25CS017_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Ensure that you are using `self.lst` instead of just `lst` in your methods, as `self` refers to the instance of the class and should be used consistently throughout.</output>
```

================================================================================



--- Feedback Report for: B25DS032_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'push'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'push'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'push'
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
30
20
2
False
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__peek__` method, where you're trying to access the last item of the stack using `self.items[-1]`, but this is not a valid operation for a peek method. Instead, you should return the top element without removing it from the stack.
</output>
```

================================================================================



--- Feedback Report for: B25EE028_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize the list with None or an empty list in the __init__ method, so it's not empty when you try to pop from it.</output>
```

================================================================================



--- Feedback Report for: B25EC044_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Stack.__init__() missing 1 required positional argument: 'L'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Stack.__init__() missing 1 required positional argument: 'L'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Stack.__init__() missing 1 required positional argument: 'L'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Stack.__init__() missing 1 required positional argument: 'L'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Stack.__init__() missing 1 required positional argument: 'L'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems that 'L' should be an instance of a Stack class itself, not a list, to correctly initialize the stack.</output>
```

================================================================================



--- Feedback Report for: B25CS044_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.lst` instead of just `lst` in your class methods, as `lst` is a local variable that gets redefined on each method call, causing the index error.</output>
```

================================================================================



--- Feedback Report for: B25EE060_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'pop'
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to implement the `pop` method by removing and returning the last element from the `self.Stack_list`, not just accessing it.</output>
```

================================================================================



--- Feedback Report for: B25MT009_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you're checking if the list is empty before attempting to pop from it in the `pop` method.</output>
```

================================================================================



--- Feedback Report for: B25EE030-q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `self` to access the class attributes in your methods, as it seems like the student might be accessing a local variable instead.</output>
```

================================================================================



--- Feedback Report for: B25DS036_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._data` instead of just `_data` in your `push`, `pop`, and `peek` methods, as they should be accessing the class's own attribute.</output>
```

================================================================================



--- Feedback Report for: B25CS007_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize the list with None or an empty list instead of an empty list, as you're trying to pop from it immediately after initialization.</output>
```

================================================================================



--- Feedback Report for: B25CS025_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 4 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the stack with a top element when creating a new instance by calling `self.items.append(None)` in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25CS047_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `2
2
1
False
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `2
2
1
False
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `2
2
1
False
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `2
2
1
False
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `2
2
1
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using the pop() function to remove items from the stack, as it should be implemented by overloading this operator or providing a separate method like 'remove()'.</output>
```

================================================================================



--- Feedback Report for: B25ME056_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Pass by reference instead of pass by value when initializing the list in the __init__ method to avoid unexpected behavior.</output>
```

================================================================================



--- Feedback Report for: B25EE049_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The implementation of `pop` method does not remove the top element from the stack, as it only returns the last element in the list instead of removing and returning it.</output>
```

================================================================================



--- Feedback Report for: B25ME041_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as Python looks for attributes on instances of classes, not just the class itself.</output>
```

================================================================================



--- Feedback Report for: B25DS020_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the push operation, where you are trying to append to the list without using 'self', which should be used to access the class's attributes and methods.</output>
```

================================================================================



--- Feedback Report for: B25ME043_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing and modifying the list inside a class method.</output>
```

================================================================================



--- Feedback Report for: S25MA014_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as Python treats local variables and instance variables differently.</output>
```

================================================================================



--- Feedback Report for: B25EE022_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE022_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE022_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE022_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE022_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE022_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as in `def __init__(self): self.L = []`, not just `self.L = []`. This will ensure that you're creating an instance of the class and using its attributes correctly.</output>
```

================================================================================



--- Feedback Report for: B25EE037_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Ensure that you are using `self` to refer to the instance of the class in your methods, as this is a fundamental concept in object-oriented programming.</output>
```

================================================================================



--- Feedback Report for: B25EE011_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods inside your class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS018_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the list as a list of lists (e.g., `self.lst = []`) instead of a regular list (`self.lst = []`), since you're using Python and need to preserve the order of elements, which is not guaranteed for regular lists.
</output>
```

================================================================================



--- Feedback Report for: B25EC039_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: Pop from empty stack
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: Pop from empty stack
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the list with None or an empty data type in the __init__ method, not just an empty list. This ensures that the stack is initialized correctly and can handle pop operations without errors.</output>
```

================================================================================



--- Feedback Report for: S25MA008  Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the default value of the list in the `__init__` method, which creates a new local list on each instance creation. Instead, use `None` as the default value to ensure a fresh list is created for each instance.
</output>
```

================================================================================



--- Feedback Report for: B25CS055_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, such as in the `push` operation where you should do `self.items.append(item)` instead of just `items.append(item)`. This ensures that the changes made to the stack are stored within the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EC033_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` when accessing the list in your methods, as `self` refers to the instance of the class and is necessary for data encapsulation.</output>
```

================================================================================



--- Feedback Report for: B25CS062_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS062_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS062_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS062_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS062_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS062_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as it refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE046_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[20, 10]
2
[null, null, null, 30, null, null, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `[1]
[null, null]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you check if the stack is empty before attempting to pop an element, as this would prevent the IndexError from occurring.
</output>
```

================================================================================



--- Feedback Report for: B25ME007_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` when accessing the list in methods, as it should be a reference to the class's attribute.</output>
```

================================================================================



--- Feedback Report for: B25ME037_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling instance methods, as in `self.items.append(item)`, not just `items.append(item)`.
</output>
```

================================================================================



--- Feedback Report for: B25CS046_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when referencing the instance's attributes in methods, like `def pop(self): return self.l.pop()` instead of just `def pop(): return self.l.pop()`.</output>
```

================================================================================



--- Feedback Report for: S25MA011_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as `items` is a built-in Python function.</output>
```

================================================================================



--- Feedback Report for: B25CS012_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are calling the pop method without checking if the list is empty first, which would raise an IndexError.</output>
```

================================================================================



--- Feedback Report for: B25MM008_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your `push`, `pop`, and `peek` methods to access the list attribute correctly.</output>
```

================================================================================



--- Feedback Report for: B25MM002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.items` instead of just `items` in your methods, as `items` is a variable within the `__init__` method and not accessible outside it.</output>
```

================================================================================



--- Feedback Report for: B25EC014_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[null, null, null, 30, 30, 2, false, 20, null, true]`
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are calling the `pop` method before checking if the stack is empty, as in `stack.pop()` instead of `if not self.items: return None; self.items.pop()`.
</output>
```

================================================================================



--- Feedback Report for: B25EC034_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE027_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[[], [], [], 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `[[1], 1]`
- Test 'empty_ops': PASS
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `[[], [], 2, 7, 5, null]`
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.balance.append(element)` for push operation instead of just `self.balance = [element]`.</output>
```

================================================================================



--- Feedback Report for: B25CS035_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as it's a reference to the instance variable.</output>
```

================================================================================



--- Feedback Report for: B25EE051_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` as the first parameter when defining your methods, like in a typical class implementation.</output>
```

================================================================================



--- Feedback Report for: B25DS043_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the instance of the class, not a standalone object.</output>
```

================================================================================



--- Feedback Report for: B25EE042_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you are using `self` when calling methods within your Stack class, as it refers to the instance of the class. For example, instead of `class Stack:`, try `class Stack: def __init__(self): self._items = []`.
</output>
```

================================================================================



--- Feedback Report for: B25DS034_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as it refers to the current instance of the class. For example, instead of `items.append(value)`, try `self.items.append(value)`.</output>
```

================================================================================



--- Feedback Report for: B25EE058_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the `pop` operation is being performed without first checking if the stack is empty, which would prevent the IndexError from occurring.
</output>
```

================================================================================



--- Feedback Report for: B25MT017_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty stack
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty stack
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you're calling the pop method without checking if the stack is empty first, which can lead to an IndexError.</output>
```

================================================================================



--- Feedback Report for: B25DS008_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output> The issue lies in the default value of the list in the `__init__` method, which creates a new empty list on each instance creation. This leads to a new list being created every time an object is instantiated, causing the index to be out of bounds when trying to pop from it.</output>
```

================================================================================



--- Feedback Report for: B25MT011.q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` correctly when calling class methods, as in `self.items.append(item)`, not just `items.append(item)`.</output>
```

================================================================================



--- Feedback Report for: B25MM030_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in the push, pop, and peek methods to access the list attribute correctly.</output>
```

================================================================================



--- Feedback Report for: B25EE016_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you're calling the pop method on the list itself instead of using the 'self' keyword to access the class's attributes, as in `self.items.pop()`.
</output>
```

================================================================================



--- Feedback Report for: B25DS015_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[[], [], [], 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `[[1], 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as `self.lst` refers to the list attribute of the class instance.</output>
```

================================================================================



--- Feedback Report for: B25EC017_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Ensure that you are using the `append` method to add elements to the stack instead of directly modifying the underlying list in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25CS028_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `self` to access the class attributes in your methods, as it seems like you forgot to use `self` when calling the `push` method.</output>
```

================================================================================



--- Feedback Report for: B25ME021_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing and modifying the list within a class method, as `self` refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EC037_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` when accessing the list inside your methods, as `self.lst` refers to the instance variable and `lst` is a local variable.</output>
```

================================================================================



--- Feedback Report for: B25ME009_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `self` refers to the instance of the class and should be used when accessing its attributes.</output>
```

================================================================================



--- Feedback Report for: B25EC026_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to remove elements from the list using indexing (e.g., `self.l[self.size() - 1]`) instead of slicing (`self.l[0:self.size() - 1]`), as slicing creates a new list and can be inefficient for large datasets.</output>
```

================================================================================



--- Feedback Report for: B25DS021_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Implementing an `is_empty` method that checks if the stack is empty by verifying the length of the internal list (`self.data`) would resolve the error.</output>
```

================================================================================



--- Feedback Report for: B25DS026.q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use 'self' when calling methods within the class, as it refers to the current instance of the class. Instead of `B25DS026`, try using a different name for your module or import it correctly.
</output>
```

================================================================================



--- Feedback Report for: B25EC041_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
It seems like you're trying to access the list `l` without initializing it with a size, which can lead to an "index out of range" error. Make sure to set a default size for your stack or handle this case in the `__init__` method.
</output>
```

================================================================================



--- Feedback Report for: B25ME026_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as it refers to the current instance of the class. For example, instead of `print(items)`, use `self.print_items()` or define a separate method `def print_items(self): pass`.</output>
```

================================================================================



--- Feedback Report for: Q25 B25MM007 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25MT008_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the stack is empty before popping an element to avoid the IndexError.</output>
```

================================================================================



--- Feedback Report for: B25DS027_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS027_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS027_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS027_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS027_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS027_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to import the list data type using `from typing import List` at the beginning of your class definition.</output>
```

================================================================================



--- Feedback Report for: B25EC002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 0

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC002_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC002_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC002_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC002_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EC002_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

- Technical summary was not generated.

================================================================================



--- Feedback Report for: B25CS019_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the current instance of the class. For example, instead of `self._items.append(item)`, try `self._items.append(item)` without `self`. Similarly, in the `__init__` method, you should initialize `self._items` with an empty list, not just assign it a value.</output>
```

================================================================================



--- Feedback Report for: B25EE026_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'stack'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The 'stack' attribute is not defined within the class, so it should be accessed as an instance variable using 'self.stack'.
</output>
```

================================================================================



--- Feedback Report for: B25MM006_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
When calling the `pop()` method, make sure to check if the stack is not empty before attempting to remove an element from it. This can be achieved by adding a conditional statement to handle the case where the stack is empty.</output>
```

================================================================================



--- Feedback Report for: B25MM028_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, "False", 20, 10, "True"]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, "True", 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods on instances of your Stack class, as it's a convention in Python for referring to the current object.</output>
```

================================================================================



--- Feedback Report for: B25EC031_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are using `self` correctly when calling methods on your Stack class, as this might be causing the issue with the 'push' operation not modifying the size of the stack.</output>
```

================================================================================



--- Feedback Report for: B25CS054_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `The stack is empty.
The stack is empty.
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `The stack is empty.
[null, null, 2, 7, 5, null]`
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider modifying your `__init__` method to also initialize the `top` attribute, as it is not being set anywhere else in the class.</output>
```

================================================================================



--- Feedback Report for: B25ME003_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` when accessing and modifying the list in your methods, as Python looks for a `__dict__` attribute on objects to determine their attributes.</output>
```

================================================================================



--- Feedback Report for: b25cs049_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as you're trying to access a class attribute (`self`) within a method.</output>
```

================================================================================



--- Feedback Report for: B25CS037_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Use `None` as the default value for the stack parameter instead of an empty list, like this: `def __init__(self, stack=None): self.stack = stack`. This ensures that every instance of the class has its own separate stack.</output>
```

================================================================================



--- Feedback Report for: B25EE023_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE023_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE023_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE023_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE023_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE023_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` as the first parameter when defining your class methods, like in a typical Python class definition.</output>
```

================================================================================



--- Feedback Report for: B25DS035_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, null, 30, 20, 2, "False", 20, 10, "True"]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, "True", 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
None
None
30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're initializing and manipulating the list within the `__init__` method. Instead of using `l = []`, consider using `self.l = []` to correctly initialize an instance variable.</output>
```

================================================================================



--- Feedback Report for: <B25CS024>_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize the list with None as the default value, so you can safely pop from it without getting an IndexError.</output>
```

================================================================================



--- Feedback Report for: B25ME017_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'isEmpty'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'isEmpty'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'isEmpty'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'size'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The `is_empty` and `size` methods should use `len(self.stack)` instead of `self.stack.isEmpty()` (which doesn't exist) or `self.size()`, as these are not built-in methods for a Python list, which is being used to implement the stack.
</output>
```

================================================================================



--- Feedback Report for: B25EE034_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are popping from an empty list by adding a condition to check the size of the stack before attempting to pop an item, e.g., `if not self.is_empty():`.
</output>
```

================================================================================



--- Feedback Report for: B25MT023 - Q 25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `self` refers to the instance of the class and should be used when accessing its attributes.</output>
```

================================================================================



--- Feedback Report for: B25CS023_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the `push` operation is correctly adding elements to the stack by verifying that it's using a list and appending to it, rather than overwriting its contents.</output>
```

================================================================================



--- Feedback Report for: B25MM012_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The Stack class is missing a dictionary to store its elements, indicated by the AttributeError 'Stack' object has no attribute 'items', suggesting that the student should initialize an empty dictionary in the __init__ method to track the stack's contents.
</output>
```

================================================================================



--- Feedback Report for: B25EC015_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, "30", "20", "2", "False", "20", "10", "True"]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, "1"]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to check if you're popping from an empty list by adding a condition to check the length of the stack before calling pop() in your pop method.</output>
```

================================================================================



--- Feedback Report for: B25MT001_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in your methods, as `self` refers to the instance of the class and should be used when accessing its attributes.</output>
```

================================================================================



--- Feedback Report for: {B25CS013}_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25CS013}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25CS013}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25CS013}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25CS013}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module '{B25CS013}_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use the `self` parameter when calling a method in Python, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25DS028_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as in `def push(self, item): self.items.append(item)`, not just `self.items.append(item)`.</output>
```

================================================================================



--- Feedback Report for: B25EC035_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
1
10
This is Empty
True
[[], [], [], 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
1
10
This is Empty
True
[[1], 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
1
10
This is Empty
True
[[], [], 2, 7, 5, "This is Empty"]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
1
10
This is Empty
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
When popping an element from the stack, you should use `self.l.pop(0)` instead of `self.l.pop(-1)`, as it's a Last-In-First-Out (LIFO) data structure.
</output>
```

================================================================================



--- Feedback Report for: B25ME050_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Ensure that you are using `self` to refer to the instance of the class in your methods, as this is a fundamental concept in object-oriented programming.</output>
```

================================================================================



--- Feedback Report for: B25EE036_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if the `pop` operation is performed without verifying if the list is empty, which could lead to an IndexError. Make sure to add a condition to handle this scenario before attempting to remove an item from the list.</output>
```

================================================================================



--- Feedback Report for: B25EE055_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use 'self' when calling methods on instances of your class, as in `if not self.items:`, to access class attributes like 'is_empty'.
</output>
```

================================================================================



--- Feedback Report for: B25ME013_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are calling the pop method on an empty list, ensure that you are checking for emptiness before attempting to remove an element from the stack.</output>
```

================================================================================



--- Feedback Report for: B25ME049_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `None
None
None
20
2
True
None
None
None
20
2
True
[null, null, null, 30, 20, 2, null, 20, 10, null]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `None
None
None
20
2
True
None
1
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
None
None
20
2
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are calling the pop method on the entire list, not just the instance of the Stack class.</output>
```

================================================================================



--- Feedback Report for: B25DS024_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[[], [], [], 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `[[1], 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize the list with None or an empty list, not just an empty list, in the __init__ method to avoid index errors.</output>
```

================================================================================



--- Feedback Report for: B25ME060_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Remember to use 'self' when calling methods inside a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS061_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods within your class, as it refers to the current instance of the class. For example, instead of `items.append(item)`, use `self.items.append(item)`.</output>
```

================================================================================



--- Feedback Report for: B25ME033_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods inside a class, as it refers to the current instance of the class. For example, instead of `items = []`, consider using `def __init__(self): self.items = []`. Also, ensure that you are calling methods on an instance of the class, not just on the class itself.</output>
```

================================================================================



--- Feedback Report for: B25EE006.Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods within the class, as it refers to the instance of the class. For example, instead of `B25EE006`, use `self`.
</output>
```

================================================================================



--- Feedback Report for: B25CS022_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods inside the class, like `self._data.append(element)` instead of just `_data.append(element)`, and also ensure that you're checking if an instance of the class is being used when calling a method.</output>
```

================================================================================



--- Feedback Report for: B25CS026_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Use a single list to store all elements and avoid using two separate lists (list and list1) as this can lead to index out of range error.</output>
```

================================================================================



--- Feedback Report for: B25CS038-Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the instance of the class. For example, instead of just `items = []`, use `self.items = []`. This ensures that each instance of the Stack class has its own list.</output>
```

================================================================================



--- Feedback Report for: B25DS022_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
10
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
10
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
10
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
10
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as it's a reference to the current instance of the class. For example, instead of `self.items.append(item)`, use `self.items.append(self.item).</output>
```

================================================================================



--- Feedback Report for: B25EC043_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `None
None
None
30
20
2
False
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `None
None
None
30
20
2
False
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `None
None
None
30
20
2
False
["Add elements before popping!", "Add elements before peeking", true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `None
None
None
30
20
2
False
[null, null, 2, 7, 5, "Add elements before popping!"]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `None
None
None
30
20
2
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider using a linked list implementation to handle push and pop operations efficiently, as your current list-based approach may lead to inefficient time complexities.</output>
```

================================================================================



--- Feedback Report for: B25EC011_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self._data` instead of just `_data` when accessing the list within methods like `push`, `pop`, and `peek`. This ensures that each instance of the Stack class has its own separate data, rather than all instances sharing a single list.</output>
```

================================================================================



--- Feedback Report for: B25MT010_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `b
False
2
[null, null, null, null, 20, 2, false, null, null, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `b
False
2
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `b
False
2
The Stack is empty.
[null, null, 2, null, null, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `b
False
2
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The error occurs because the `pop` operation removes the last element from the stack, but your implementation does not handle this case when there's only one element left in the stack. You should add a check to return the single remaining element instead of trying to remove it.
</output>
```

================================================================================



--- Feedback Report for: B25MM016_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The Stack class is missing a key attribute to store the elements, which should be initialized with a list or other data structure during object creation.
</output>
```

================================================================================



--- Feedback Report for: B25CS030_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.items` instead of just `items` in the push, pop, peek methods to access the list attribute correctly.</output>
```

================================================================================



--- Feedback Report for: B25EC012_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `self` refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25MT006_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.items` instead of just `items` in your methods, as `items` is a variable within the class's scope and not an attribute of the class itself.</output>
```

================================================================================



--- Feedback Report for: B25EE020_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to initialize an empty list instead of a pre-initialized one, as it can lead to unexpected behavior when elements are added later.</output>
```

================================================================================



--- Feedback Report for: B25EE002_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `items` is a built-in Python list attribute and should not be overwritten.</output>
```

================================================================================



--- Feedback Report for: B25EC022_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `Pop: 30
Peek: 20
Size: 2
Is Empty: False
Is Empty after popping all: True
------------------------------------------------------------
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `Pop: 30
Peek: 20
Size: 2
Is Empty: False
Is Empty after popping all: True
------------------------------------------------------------
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `Pop: 30
Peek: 20
Size: 2
Is Empty: False
Is Empty after popping all: True
------------------------------------------------------------
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `Pop: 30
Peek: 20
Size: 2
Is Empty: False
Is Empty after popping all: True
------------------------------------------------------------
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `Pop: 30
Peek: 20
Size: 2
Is Empty: False
Is Empty after popping all: True
------------------------------------------------------------
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as in `self.items.append(item)`, not just `items.append(item)`.</output>
```

================================================================================



--- Feedback Report for: B25MM027_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
30
2
False
20
10
None
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
30
2
False
20
10
None
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
30
2
False
20
10
None
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
30
2
False
20
10
None
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
30
2
False
20
10
None
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `items` is a local variable in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25ME023 q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS039_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
20
10
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
20
10
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
20
10
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods inside the class, as it refers to the current instance of the class. For example, instead of `my_stack.append(data)`, it should be `self.my_stack.append(data)`.</output>
```

================================================================================



--- Feedback Report for: B25DS003_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The student's code initializes a list with an empty list as its default value, which may lead to unexpected behavior when pushing elements onto the stack.</output>
```

================================================================================



--- Feedback Report for: B25ME030_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
30
20
2
False
20
10
True
[null, null, null, null, null, null, null, null, null, null]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
1
[null, null]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
None
None
True
0
[null, null, null, null]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
2
7
5
None
[null, null, null, null, null, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Ensure that you are using a list data structure with push and pop operations to maintain the Last-In-First-Out (LIFO) property, rather than simply appending elements to the list.</output>
```

================================================================================



--- Feedback Report for: B25DS038_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS038_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS038_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS038_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS038_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS038_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Verify that you are using the correct methods for dictionary operations, as 'dict1' and 'dict2' are being treated as if they were lists, not dictionaries.</output>
```

================================================================================



--- Feedback Report for: B25ME001_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the `push` operation is actually adding elements to the stack, and verify that `pop` returns the correct element, not just removes it from the list.</output>
```

================================================================================



--- Feedback Report for: B25MT018_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `[null, null, null, 30, "20", "2", false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `[null, "1"]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you're calling the methods on the class itself instead of an instance of the class, as the error suggests that `self.items` is empty when trying to pop from it.</output>
```

================================================================================



--- Feedback Report for: B25EC024_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as `items` is a built-in Python function.</output>
```

================================================================================



--- Feedback Report for: B25EC019_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are correctly initializing the container in the `__init__` method by ensuring it's not empty before popping elements.</output>
```

================================================================================



--- Feedback Report for: B25EC027_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
When calling the `pop()` method, make sure to check if the list is not empty before attempting to remove an item from it. This can be achieved by adding a conditional statement to handle the case where the list is empty.</output>
```

================================================================================



--- Feedback Report for: B25EC020_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within the class, as it's a reference to the current instance, not just the function itself.</output>
```

================================================================================



--- Feedback Report for: B25EE031_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
20
10
True
30
20
10
[null, null, null, null, 20, 2, false, null, null, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use the `append` method instead of indexing to add elements to the list in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25ME045_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are using `self` when calling methods on your Stack class, as it's likely that you're missing the `self` parameter in your method definitions.</output>
```

================================================================================



--- Feedback Report for: B25CS045_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in the `push` method, as `items` is a built-in Python data structure.</output>
```

================================================================================



--- Feedback Report for: B25EC025_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'items'
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'stack' object has no attribute 'items'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try accessing the list using `self.item` instead of just `item`, as it's a class attribute, not an instance attribute.</output>
```

================================================================================



--- Feedback Report for: B25MM015_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as `self` refers to the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25MM005_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` in your methods, as Python looks for a `__getattribute__` method to handle attribute access. For example, when implementing the `push` operation, you should do `self._items.append(item)` instead of just `self._items.append(item).</output>
```

================================================================================



--- Feedback Report for: B25CS029_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The stack implementation seems correct, but the `size` operation only returns the length of the list without checking if it's empty, which is why you're getting an `IndexError` when trying to pop from an empty list.
</output>
```

================================================================================



--- Feedback Report for: B25MT022_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 7

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize the `_items` attribute before using it, as it is not automatically created when the `Stack` class is instantiated.</output>
```

================================================================================



--- Feedback Report for: B25EE031_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
20
10
True
30
20
10
[null, null, null, null, 20, 2, false, null, null, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
20
10
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
20
10
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the implementation of the `push` operation, where you're directly accessing and modifying the underlying list without using the provided `append` method.</output>
```

================================================================================



--- Feedback Report for: q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within your class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25DS025_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Verify that you are using `self` correctly when calling class methods, as this can impact how attributes like `items` are accessed.</output>
```

================================================================================



--- Feedback Report for: B25ME029_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` as the first parameter when defining your methods, like in a typical Python class.</output>
```

================================================================================



--- Feedback Report for: B25MT030_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self._items` instead of just `_items` when accessing the list in your methods, as it's a private attribute and should be accessed through the class instance.</output>
```

================================================================================



--- Feedback Report for: B25EE015_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when referencing the stack's attributes in methods, as it represents the instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE057_q25 (1) ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE057_q25 (1)'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE057_q25 (1)'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE057_q25 (1)'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE057_q25 (1)'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE057_q25 (1)'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` when calling methods within your class, as it refers to the current instance of the class. For example, instead of `Stack.push(self.items)`, use `self.push(self.items).`
</output>
```

================================================================================



--- Feedback Report for: B25MM020_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 0

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25MM020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

- Technical summary was not generated.

================================================================================



--- Feedback Report for: B25DS023_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 3 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you are using a list as an attribute of your Stack class, but you haven't initialized it with any elements in the constructor. You should create an empty list and add elements to it when the push operation is performed.
</output>
```

================================================================================



--- Feedback Report for: B25CS060_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Consider initializing the stack with a list instead of an optional parameter to avoid potential issues when `list` is not provided.</output>
```

================================================================================



--- Feedback Report for: B25CS036_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS036_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS036_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS036_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS036_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS036_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to initialize an empty list in the `__init__` method instead of passing it as a parameter with a default value, which can lead to unexpected behavior.</output>
```

================================================================================



--- Feedback Report for: (B25DS042)_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the implementation of `pop` and `is_empty` methods, as `self.stack_list.pop()` removes the last element without checking if the list is empty, causing an `IndexError`, and there's no direct attribute for `is_empty`.
</output>
```

================================================================================



--- Feedback Report for: B25DS010_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS010_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS010_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS010_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS010_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25DS010_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to import the list data structure by adding `import list` at the beginning of your code.</output>
```

================================================================================



--- Feedback Report for: S25MA004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute '_items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you forgot to initialize the `_items` attribute before using it, which is a crucial part of your Stack class.</output>
```

================================================================================



--- Feedback Report for: B25DS029_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.item` instead of just `item` when accessing the list in your methods, as it's a part of the class and should be accessed through the instance.</output>
```

================================================================================



--- Feedback Report for: B25EC036_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as you are trying to access a class attribute (`self`) within a method.</output>
```

================================================================================



--- Feedback Report for: B25EE052_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as you're trying to access an instance variable.</output>
```

================================================================================



--- Feedback Report for: B25EE017_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 7

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25EE017_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are trying to call the methods directly on the class, instead of using 'self' when accessing them inside the class. For example, try changing `Stack()` to `Stack().push(item)`.
</output>
```

================================================================================



--- Feedback Report for: B25EE033_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class. For example, instead of `stack.pop()`, use `self._items.pop()`. Also, ensure that you're using the correct method names for stack operations like `push`, `peek`, etc.</output>
```

================================================================================



--- Feedback Report for: B25MT021_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` when accessing the list in your methods, as `items` is a built-in Python function.</output>
```

================================================================================



--- Feedback Report for: B25CS009_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: list index out of range
```
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 4 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self.stack` instead of just `stack` when accessing or modifying the stack in your methods, as Python looks for attributes on instances of classes, not global variables.
</output>
```

================================================================================



--- Feedback Report for: B25ME039_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'st'
```
- Test 'simple': PASS
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `The stack is empty.
The stack is empty.
[null, null, true, 0]`
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'st'
```
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Stack class should have an attribute 'stack' instead of 'a', as it is typically represented as a list.</output>
```

================================================================================



--- Feedback Report for: B25EC021_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'simple': PASS
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'is_empty'
```
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `[null, null, 2, 7, 5, "Stack is empty"]`
- Test 'no_ops': PASS

**Overall Score: 2 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as in `if self.is_empty():`, not just `is_empty()`. This will ensure that you're accessing the method on an instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS034_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check if you are using `self` when calling methods on your Stack class, as this can lead to issues with instance variables not being accessed correctly.</output>
```

================================================================================



--- Feedback Report for: B25CS020_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```
- Test 'no_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Stack' not found in module 'B25CS020_q25'.
[RUNNER CLASS ERROR] AttributeError: Class Stack not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling class methods, as it's a reference to the current instance, not just a generic object.</output>
```

================================================================================



--- Feedback Report for: B25DS006_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `append()` instead of assigning a new list, e.g., `self.list1.append(element)` in the push operation.</output>
```

================================================================================



--- Feedback Report for: B25MT032_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `self` to access and modify the class attributes in your methods, as it's a crucial part of object-oriented programming.</output>
```

================================================================================



--- Feedback Report for: B25EE025_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self` when calling methods within a class, as it refers to the current instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25CS011_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': PASS
- Test 'simple': PASS
- Test 'empty_ops': PASS
- Test 'mixed': PASS
- Test 'no_ops': PASS

**Overall Score: 5 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.items` instead of just `items` in your methods, as `self` refers to the instance of the class and should be used when accessing its attributes.</output>
```

================================================================================



--- Feedback Report for: B25EC045_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndexError: pop from empty list
```
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to use `self.lst` instead of just `lst` in the `push`, `pop`, and `peek` methods, as these methods are intended for instance methods, not global variables.</output>
```

================================================================================



--- Feedback Report for: B25DS007_Q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'simple': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'empty_ops': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'mixed': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] AttributeError: 'Stack' object has no attribute 'items'
```
- Test 'no_ops': PASS

**Overall Score: 1 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The `pop` method is attempting to access and modify the internal data structure without checking if it's initialized with a list, leading to the AttributeError.
</output>
```

================================================================================



--- Feedback Report for: B25ME004_q25 ---
Assignment: csl100_q25

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 6

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'complex': FAIL
  - Expected: `[null, null, null, 30, 20, 2, false, 20, 10, true]`
  - Your output: `30
20
2
False
True
[null, null, null, 30, 20, 2, false, 20, 10, true]`
- Test 'simple': FAIL
  - Expected: `[null, 1]`
  - Your output: `30
20
2
False
True
[null, 1]`
- Test 'empty_ops': FAIL
  - Expected: `[null, null, true, 0]`
  - Your output: `30
20
2
False
True
[null, null, true, 0]`
- Test 'mixed': FAIL
  - Expected: `[null, null, 2, 7, 5, null]`
  - Your output: `30
20
2
False
True
[null, null, 2, 7, 5, null]`
- Test 'no_ops': FAIL
  - Expected: `[]`
  - Your output: `30
20
2
False
True
[]`

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the fact that your `push` operation does not modify the `items` list; it simply assigns a new reference to `self.items`. You should append elements to the list instead of reassigning it.</output>
```

================================================================================
