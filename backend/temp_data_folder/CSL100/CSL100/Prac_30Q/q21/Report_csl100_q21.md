# Autograder - Aggregated Feedback Report
## Assignment: csl100_q21



--- Feedback Report for: B25MT030_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like the student forgot to include 'name' and 'roll_number' in the function arguments of average() method, which should be `average(self)` instead.</output>
```

================================================================================



--- Feedback Report for: B25CS002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing required positional arguments 'name', 'roll_number', and 'marks' in your `__init__` method. Please ensure these parameters are included when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25ME019_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Student class is missing required positional arguments 'name', 'roll_number', and 'marks' in its __init__ method, which should be passed when creating an instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EE013_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output> The issue lies in the `info()` method where you're calling `self.average()` instead of `self.marks` which is required by the `__init__` method. It should be `self.marks` instead of `self.average()`. </output>
```

================================================================================



--- Feedback Report for: B25MT029_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT029_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT029_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT029_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT029_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT029_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access the Student class before it's defined. Make sure your methods are inside the class definition.</output>
```

================================================================================



--- Feedback Report for: B25MM005_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()`, `grade()`) before initializing the object, which is causing a TypeError. You should first create an instance of the Student class and then call these methods.</output>
```

================================================================================



--- Feedback Report for: B25CS035_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access the instance variables `self.name`, `self.roll_number` and `self.marks` directly from the class methods `info()`, instead of using them. Try accessing these variables inside the methods, for example: `return f'{self.name} (Roll: {self.roll_number}) | Avg: {avg:.1f} | Grade: {grade}'</output>
```

================================================================================



--- Feedback Report for: S25MA001__q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you're calling the `__init__` method with the correct parameters and ensure it's a class method by prefixing `_` to its name.</output>
```

================================================================================



--- Feedback Report for: B25DS016_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if all required parameters are being passed to the __init__ method, specifically 'name', 'roll_number', and 'marks'.</output>
```

================================================================================



--- Feedback Report for: B25DS032_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like the `__init__` method is not being called before trying to access its attributes, which could be causing the TypeError. Make sure to call `self.__init__(name, roll_number, marks)` in the `info` method.</output>
```

================================================================================



--- Feedback Report for: B25MT009_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) directly within your methods, but they are not defined until the object is initialized with `__init__()`. You should use the instance variable names, not their values, in your methods.</output>
```

================================================================================



--- Feedback Report for: B25EE022_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE022_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE022_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE022_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE022_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE022_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are correctly calling methods with correct parameters, for example, `self.average()` instead of `self.average()`. Also, make sure that all class attributes are defined before using them.</output>
```

================================================================================



--- Feedback Report for: B25CS037_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is causing the TypeError. Make sure to include it when initializing the Student object.</output>
```

================================================================================



--- Feedback Report for: B25E049_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing required positional arguments 'name', 'roll_number', and 'marks'. Ensure that these parameters are passed when creating a new `Student` object.
</output>
```

================================================================================



--- Feedback Report for: B25MM028_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are correctly calling methods `average()` and `grade()`, but you forgot to pass required arguments 'name', 'roll_number', and 'marks' when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EC035_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) directly without initializing them using the constructor (__init__ method). Make sure to include all required arguments in the __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25EE057_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're creating an instance of the Student class without providing all required positional arguments, which is causing the TypeError. Make sure to pass 'name', 'roll_number', and 'marks' when initializing a Student object.</output>
```

================================================================================



--- Feedback Report for: B25ME060_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (average() and grade()) before initializing the object with name, roll_number, and marks. Try calling these methods after they've been called in your info() method.</output>
```

================================================================================



--- Feedback Report for: B25CS042_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies with the `info()` method where you're trying to access instance variables without using dot notation or referencing them as attributes. Instead, use `self.name`, `self.roll_number`, and `self.marks` in your return statement.
</output>
```

================================================================================



--- Feedback Report for: B25CS034_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the 'name', 'roll_number' and 'marks' arguments in your __init__ method. Make sure they are included when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EC044_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are passing `self.avg` instead of calling the `average()` method when constructing the string for `info()`. Try changing it to `self.average()`.</output>
```

================================================================================



--- Feedback Report for: B25EE027_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rnumber', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rnumber', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rnumber', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rnumber', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rnumber', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies with the order of arguments passed to the `__init__` method, which should be `name`, `roll`, and `marks` instead of `self.name`, `self.rnumber`, and `self.marks`.
</output>
```

================================================================================



--- Feedback Report for: B25EC013_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of operations within the `info()` method. Currently, it first calculates the average and grade using the `average()` and `grade()` methods, then attempts to return a string with the calculated values. However, these calculations should be performed before attempting to construct the string, as the student's code does not correctly utilize the calculated averages and grades in its output.
</output>
```

================================================================================



--- Feedback Report for: B25DS043_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are mixing up `self.roll_number` and `self.roll`. In your `__init__` method, you should initialize `roll_number` instead of just `roll`, to avoid the TypeError.</output>
```

================================================================================



--- Feedback Report for: B25EE037_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to pass all required arguments (name, roll_number, marks) to the __init__ method when creating an instance of the Student class.</output>
```

================================================================================



--- Feedback Report for: B25EE052_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you're missing the required positional arguments 'name', 'roll_number', and 'marks'. Ensure that these parameters are passed when creating a new Student instance.
</output>
```

================================================================================



--- Feedback Report for: B25EC034_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) directly instead of using function arguments, which is why you're missing three required positional arguments in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25MM026_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (average() and grade()) before initializing the object with required parameters. Make sure to pass name, roll_number, and marks when creating a Student object.</output>
```

================================================================================



--- Feedback Report for: B25EC031_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance methods (`average()` and `grade()`) directly from `__init__()`, which is incorrect. The `__init__` method should only be used for initialization, not for accessing other methods.</output>
```

================================================================================



--- Feedback Report for: B25DS035_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're using `self.roll_number` instead of `self.roll`, which is a different attribute. You should use `self.roll` consistently throughout the class.
</output>
```

================================================================================



--- Feedback Report for: B25MM002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're mixing up `roll_number` with `roll`. Make sure to use consistent variable names throughout your code.</output>
```

================================================================================



--- Feedback Report for: B25ME046_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to print student information but your `__init__` method is not being called anywhere, which means it's not setting the required attributes (`name`, `roll_number`, and `marks`) for the `info()` method to work with.</output>
```

================================================================================



--- Feedback Report for: B25EE042_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing `self.roll_number` and `self.marks`. Make sure to include all required arguments when initializing the object.</output>
```

================================================================================



--- Feedback Report for: B25EC019_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing required positional arguments 'name', 'roll_number', and 'marks'. Ensure these are passed when creating a new instance of the Student class.
</output>
```

================================================================================



--- Feedback Report for: q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (self.name, self.roll_number, etc.) directly without initializing them first. You need to assign values to these variables using the __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25DS041_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS041_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS041_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS041_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS041_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS041_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods on an instance before it's fully initialized. In your `__init__` method, you should calculate the average marks and grade inside the class itself, not in the `info()` method.</output>
```

================================================================================



--- Feedback Report for: B25DS024_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are passing parameters as `self.roll_number`, `self.average()`, and `self.grade()` instead of assigning them directly. Change it to `self.roll`, `self.marks` respectively.
</output>
```

================================================================================



--- Feedback Report for: B25MT027_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're calling `self.grade()` twice, whereas it should be using the calculated average marks for grading. Update the method to use `self.marks / len(self.marks)` instead of `self.grade()`.
</output>
```

================================================================================



--- Feedback Report for: B25MT032_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're trying to concatenate the student's attributes with their average and grade, which are calculated methods. You should call these methods separately, like this: `return f'{self.name}, {self.roll_number}, {self.average()}, {self.grade()}'</output>
```

================================================================================



--- Feedback Report for: B25MM018_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing the required positional arguments 'name', 'roll_number', and 'marks'. Ensure these are passed when creating a new Student object, e.g., `student = Student('John Doe', 12345, 85)`.
</output>
```

================================================================================



--- Feedback Report for: B25ME003_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) before initializing the object with its required parameters. You should calculate or determine these values inside the respective methods instead of calling them directly in the `info()` method.</output>
```

================================================================================



--- Feedback Report for: B25EE044_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are passing `self.average` and `self.grade` as arguments instead of accessing class attributes. You should use `self` to access these attributes, for example: `print(f'{self.name}(Roll:{self.roll_number}) | Avg:{self.marks.mean()} | Grade:{self.marks.mean()/10}')</output>
```

================================================================================



--- Feedback Report for: B25CS018_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are trying to calculate average and grade inside the `get_info` method, but these calculations should be done in the `__init__` method or a separate method that is called before `get_info`. Try moving `calculate_average` and `get_grade` methods outside of `get_info`.</output>
```

================================================================================



--- Feedback Report for: B25DS002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing `self.roll_number` and `self.marks`. Ensure that all required parameters are passed during object creation.
</output>
```

================================================================================



--- Feedback Report for: B25ME026_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 2

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`) before they are initialized. Make sure to assign values to these variables in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25CS025_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're calling methods (`average()` and `grade()`) before initializing the object with required parameters, which should be done inside the `__init__` method instead of directly within the `info` method.
</output>
```

================================================================================



--- Feedback Report for: B25EC010_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()`, `grade()`) before initializing the instance with required arguments, which is causing a TypeError. You need to ensure that all attributes are assigned values before using them.</output>
```

================================================================================



--- Feedback Report for: B25EC042_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing 'roll_number' and 'marks' arguments in your Student class __init__ method. Make sure to include them when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25CS023_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`) outside of any method, which is not allowed. You should call these methods inside your `info()` function.</output>
```

================================================================================



--- Feedback Report for: B25ME004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) before they are defined. You should define these methods inside the class definition, not after calling them.</output>
```

================================================================================



--- Feedback Report for: B25EC020_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 3

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check the initialization of the Student class by ensuring that 'name', 'roll_no', and 'marks' are passed as arguments in the __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25EC039_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate average marks, grade, and info, but your `__init__` method is not correctly defined. Make sure it accepts all required parameters ('name', 'roll_number', and 'marks') when initializing a Student object.</output>
```

================================================================================



--- Feedback Report for: B25EE059_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate the average, grade, and info of a student but your __init__ method is only taking two parameters (name and roll) instead of three. Make sure to include 'marks' in the __init__ method as well.</output>
```

================================================================================



--- Feedback Report for: B25ME041_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are not passing the required arguments 'name', 'roll_number', and 'marks'. Ensure that all these parameters are passed when creating a new instance of the Student class.
</output>
```

================================================================================



--- Feedback Report for: B25MM025_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're referencing `s1` which is not defined; instead, use `self` to access the student's attributes.
</output>
```

================================================================================



--- Feedback Report for: B25EC041_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're initializing `self.roll` instead of `self.rollno` in your `__init__` method, which is causing the TypeError. Make sure to use `rollno` consistently throughout the class.</output>
```

================================================================================



--- Feedback Report for: B25DS020_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS020_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS020_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS020_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS020_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25DS020_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method, where you are trying to access methods (`average()`, `grade()`) on an instance of a class (`student`) that does not exist. You should replace `student` with `self`.
</output>
```

================================================================================



--- Feedback Report for: B25EE007_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in how you're calling the methods `average()` and `grade()`. Since these are instance methods, they should be called using `self` followed by the method name. For example, instead of `self.average(0)`, it should be `self.average(self.marks)` and similarly for `self.grade(0)`.
</output>
```

================================================================================



--- Feedback Report for: S25MA008  Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to call `self.average()` and `self.grade()` methods correctly, using parentheses after the dot operator (e.g., `self.average()`, not just `average()`), as they are instance methods.</output>
```

================================================================================



--- Feedback Report for: B25MT001_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're trying to access `self.roll_number` instead of `self.roll`, which is a single character, not a number. You should use `roll` consistently throughout your methods.
</output>
```

================================================================================



--- Feedback Report for: B25EC002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) before initializing the object with required arguments (`name`, `roll_number`, and `marks`), which is causing a TypeError.</output>
```

================================================================================



--- Feedback Report for: B25ME047_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME047_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME047_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME047_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME047_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME047_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (self.name, self.roll_number, etc.) directly instead of using methods for them. Try changing `Average: {self.average_marks()}, Grade: {self.grade()}` to `Average: {self.calculate_average()}, Grade: {self.calculate_grade()}` in the `info()` method.</output>
```

================================================================================



--- Feedback Report for: B25ME048_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're mixing up the order of arguments in your `__init__` method. You should be passing `name`, `roll_number`, and `marks` as separate parameters, not trying to unpack them inside the function.</output>
```

================================================================================



--- Feedback Report for: B25EC033_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is why it's throwing a TypeError. Make sure to include `self` as the first parameter when defining your methods.</output>
```

================================================================================



--- Feedback Report for: B25EC014_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems that you're missing the `self` parameter in your `__init__` method, which is required for instance methods in Python classes.</output>
```

================================================================================



--- Feedback Report for: B25ME006_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access methods from an instance (`self`) before it's created. You should define `average()`, `grade()` as instance methods inside the `__init__` method, not outside.</output>
```

================================================================================



--- Feedback Report for: B25EC037_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are trying to call methods (`average()`, `grade()`) before they are defined, which is causing the TypeError. You should define these methods within the class definition or after the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25EE018_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE018_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE018_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE018_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE018_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE018_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try importing the class before using it, e.g., `from B25EE018_Q21 import Student` or `import B25EE018_Q21 as s`, and ensure that the file name matches exactly with the class name.</output>
```

================================================================================



--- Feedback Report for: B25MM020_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are missing the 'name', 'rollno', and 'marks' parameters in your __init__ method. Make sure to include them when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25MM015_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of operations within the info() method. The average() and grade() methods are being called before their respective instance variables (avg and grd) are initialized, causing a TypeError because they are trying to access 'self' outside of an instance's __init__ method.
</output>
```

================================================================================



--- Feedback Report for: B25MT005_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods before they are defined. The `average()` and `grade()` methods should be defined inside the class, not outside it.</output>
```

================================================================================



--- Feedback Report for: B25CS041_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're initializing `roll_number` instead of `roll`, which is causing the TypeError. Try changing `self.roll_number` to `self.roll` in your `info()` method.</output>
```

================================================================================



--- Feedback Report for: B25EE051_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access methods (`average()` and `grade()`) before they are defined. You should define these methods inside the class definition.</output>
```

================================================================================



--- Feedback Report for: B25CS036_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 3

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check the number and types of arguments in the `__init__` method to ensure they match the requirements specified in the problem description.</output>
```

================================================================================



--- Feedback Report for: B25DS008_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to call `self` when referencing instance variables in methods like `info()`.</output>
```

================================================================================



--- Feedback Report for: S25MA014_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate the average and grade directly from the `info()` method, but according to the problem description, these calculations should be done separately. Try calculating the average and grade in their respective methods (`average()` and `grade()`) instead of trying to combine them in `info()`.</output>
```

================================================================================



--- Feedback Report for: B25CS043-q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS043-q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS043-q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS043-q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS043-q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS043-q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies with the incorrect attribute names used in the `info()` method. The correct attributes are 'name', 'roll', and 'marks', not 'names', 'self.roll', and 'self.average()'. Ensure to use the correct attribute names when accessing instance variables.
</output>
```

================================================================================



--- Feedback Report for: b25cs040.q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'b25cs040'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'b25cs040'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're trying to call `self.average()` without defining it, and also incorrectly using `self.roll_number` instead of `self.roll`.
</output>
```

================================================================================



--- Feedback Report for: B25EE055_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods before they are defined. The `average()` and `grade()` methods should be implemented inside the class, not as standalone functions.</output>
```

================================================================================



--- Feedback Report for: {B25CS013}_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25CS013}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25CS013}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25CS013}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25CS013}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25CS013}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the incorrect method call for 'average' and 'grade', which should be `self.marks` instead, as these methods are not defined in the provided code snippet.</output>
```

================================================================================



--- Feedback Report for: B25CS038-Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS038-Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS038-Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS038-Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS038-Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS038-Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to access 'self.grade()' and 'self.avg()' correctly, as they are instance methods that need to be invoked using parentheses (i.e., self.grade() instead of self.grade).</output>
```

================================================================================



--- Feedback Report for: B25EE046_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're mixing up the name and roll_number attributes. In your __init__ method, you're passing 'roll' instead of 'roll_number'. Make sure to use the correct attribute names throughout the class.</output>
```

================================================================================



--- Feedback Report for: B25DS015_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of arguments passed to the `__init__` method. In Python, keyword arguments should be used instead of positional arguments for instance initialization, so change `self.roll_number` to `self.roll`.
</output>
```

================================================================================



--- Feedback Report for: B25CS011_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'rolln'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'rolln'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'rolln'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'rolln'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'rolln'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables directly instead of using the methods provided by the class, which is causing the TypeError. Try accessing `self.name`, `self.roll`, and `self.marks` within your `info()` method.</output>
```

================================================================================



--- Feedback Report for: B25MT017_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 3

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're iterating over the 'marks' list in your average_marks method without specifying that it's a read-only attribute, which could be causing the TypeError.</output>
```

================================================================================



--- Feedback Report for: B25EC028_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like the `__init__` method is missing required positional arguments 'name', 'roll_number', and 'marks'. Make sure these are included when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EE036_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) before they are initialized. Make sure to pass all required arguments when creating a new Student object, or define these as class attributes if they need to be accessible outside the constructor.</output>
```

================================================================================



--- Feedback Report for: B25ME008_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is causing the TypeError. You should pass `self` as the first argument to the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25EE006.Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE006'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access a method 'average' before it's defined. You should define the methods before they are used.</output>
```

================================================================================



--- Feedback Report for: B25ME010_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are correctly calling methods `average()` and `grade()` from the instance itself (`self`), not from the class. Use `self.average()` and `self.grade()` instead of `Student.average(self)` and `Student.grade(self)`.</output>
```

================================================================================



--- Feedback Report for: B25ME031_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are using `self.roll_number` instead of `self.roll`. Python is case-sensitive, so it treats 'roll' and 'Roll' as two different attributes. You should change `self.roll_number` to `self.roll`.
</output>
```

================================================================================



--- Feedback Report for: B25MM009(q21) ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method, where you're calling `self.average()` and `self.grade()`, but these methods don't exist yet because they haven't been implemented. You should call `self.marks` instead to calculate the average and grade.
</output>
```

================================================================================



--- Feedback Report for: S25MA004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Change the constructor name from `_init_` to `__init__` to match Python's conventional naming convention for constructors.</output>
```

================================================================================



--- Feedback Report for: B25EE034_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're using `self.roll_no` instead of `self.roll` and also not passing `marks` as an argument to the `__init__` method. Make sure to use the correct attribute names.</output>
```

================================================================================



--- Feedback Report for: B25EC004_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EC004_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EC004_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EC004_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EC004_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EC004_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the way you're calling methods within the `info()` function. In Python, when using f-strings, you need to access attributes (methods) of an object by prefixing them with a dot (`.`), not by concatenating them with colons.
</output>
```

================================================================================



--- Feedback Report for: B25ME016_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'Student' is not defined
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'Student' is not defined
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'Student' is not defined
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'Student' is not defined
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'Student' is not defined
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that you are trying to access class attributes (`self.name`, `self.roll_number`, etc.) as if they were instance variables, but since this is a class definition, these should be accessed using the `self` keyword.</output>
```

================================================================================



--- Feedback Report for: B25DS030_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of arguments passed to the `__init__` method. In Python, default argument values are evaluated at the point of function definition in the defining scope. This means that when you define `self.name`, `self.roll_number`, and `self.marks` with default values (e.g., `None`), these values are used when the function is defined, not when it's called. Therefore, you should remove the default argument values to ensure they're only evaluated when the object is instantiated.</output>
```

================================================================================



--- Feedback Report for: B25CS007_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is required for instance methods in Python classes.</output>
```

================================================================================



--- Feedback Report for: B25DS021_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you're calling `self.avg()` and `self.grade()` directly from the `__init__` method, and instead call these methods after initializing the instance with correct arguments.</output>
```

================================================================================



--- Feedback Report for: B25EE060_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you're using `self.roll_number` instead of `self.roll`. The correct initialization should be `self.roll_number = roll`.
</output>
```

================================================================================



--- Feedback Report for: B25MT021_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The missing arguments 'name', 'roll_number', and 'marks' in the __init__ method are not being passed when creating a new Student object, which is causing the TypeError.</output>
```

================================================================================



--- Feedback Report for: B25ME029_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which should be `def __init__(self, name, roll_number, marks)` instead of just `def __init__(self, name, roll, marks)`. Make sure to include all required parameters.</output>
```

================================================================================



--- Feedback Report for: B25ME028_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
You are trying to call the methods of the 'Student' class but it's not imported in your code. Make sure you import the class at the beginning of your function.
</output>
```

================================================================================



--- Feedback Report for: B25MT026_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of arguments passed to the `__init__` method, where you are passing `roll_number` instead of `roll`. In Python, instance variables are assigned from right to left. So, `self.roll_number` should be `self.roll`.
</output>
```

================================================================================



--- Feedback Report for: B25CS048_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) before initializing the object with required parameters. You need to call these methods inside the `__init__` method itself or pass them as arguments to the `info` method.</output>
```

================================================================================



--- Feedback Report for: S25MA018_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are missing `self.roll_number` and `self.marks`. Ensure that all required arguments are passed when initializing a new `Student` object, like so: `def __init__(self, name, roll_number, marks)`.
</output>
```

================================================================================



--- Feedback Report for: B24DS035_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of arguments passed to the `__init__` method, where you are passing `self.roll_number` instead of `self.roll`. Python's convention is to pass instance variables as keyword arguments (e.g., `self.name`, `self.roll`, and `self.marks`) rather than positional arguments.
</output>
```

================================================================================



--- Feedback Report for: B25ME051_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are missing the required positional arguments 'roll_number' and 'marks' in your Student class's __init__ method. Make sure to include them when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EC008_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Student class is missing positional arguments 'name', 'roll_number', and 'marks' in its __init__ method, which should be added as parameters.</output>
```

================================================================================



--- Feedback Report for: B25CS030_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables directly instead of calling methods. You should call `self.name`, `self.roll_number`, and `self.marks` inside your methods, not use them directly.</output>
```

================================================================================



--- Feedback Report for: B25ME011_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing `self.rolls_number` (typo) and not passing all required parameters when initializing a new Student object, which should be `self.name`, `self.roll_number`, and `self.marks`.
</output>
```

================================================================================



--- Feedback Report for: B25CS017_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()`, `grade()`) before they are defined, which is causing a TypeError. Make sure to define these methods inside the class definition.</output>
```

================================================================================



--- Feedback Report for: B25DS031_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) within the `info()` method, but these methods are not defined. You should define them before using them.</output>
```

================================================================================



--- Feedback Report for: B25EE016_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE016_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE016_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE016_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE016_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE016_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access class 'Student' but haven't imported it. You should add `from B25EE016_q21 import Student` at the top of your code to fix this issue.</output>
```

================================================================================



--- Feedback Report for: B25ME012_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're using `self.roll_number` instead of `self.roll`. Python is case-sensitive, so it's treating `roll_number` as a different attribute.
</output>
```

================================================================================



--- Feedback Report for: B25DS039_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're calling `self.grade()` before initializing it, which is causing the TypeError. You should call `self.average()` instead of `self.grade()`. Also, note that there's a typo in 'roll_no' and 'gd', it should be 'roll' and 'grade'.</output>
```

================================================================================



--- Feedback Report for: B25CS026_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables before they are initialized. In the `__init__` method, you should assign the values of 'name', 'roll_number' and 'marks' to instance variables using `self.name`, `self.roll_number` and `self.marks` respectively.</output>
```

================================================================================



--- Feedback Report for: B25EC015_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_num', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_num', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_num', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_num', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_num', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're assigning instance variables (`self.name`, `self.roll_num`, `self.average()`, etc.) instead of using function arguments, which is why you need to pass 'name', 'roll_num', and 'marks' as positional arguments.
</output>
```

================================================================================



--- Feedback Report for: B25CS021_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you are using `self.roll_number` instead of `self.roll`. This is causing a TypeError because Python does not recognize `roll_number` as an attribute of the class.
</output>
```

================================================================================



--- Feedback Report for: B25EE012_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE012_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE012_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE012_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE012_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE012_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you are calling methods (`average()`, `grade()`) on an object before it is fully defined, as these methods require `self` as their first parameter. You should define and call these methods within the `__init__` method or separately after initialization.
</output>
```

================================================================================



--- Feedback Report for: B25ME017_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that the `self.average()` method is being called before it is defined, which would cause a TypeError. The correct order should be to define `average()` inside the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25EC021_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are passing `self.average()` and `self.grade()` which don't exist yet. You should calculate these values inside the methods themselves.</output>
```

================================================================================



--- Feedback Report for: B25MT010_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing `self.roll` and `self.marks` parameters while calling `self.avg` and `self.grade` methods. Make sure to include all required arguments in your method calls.</output>
```

================================================================================



--- Feedback Report for: B25EC001_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the `__init__` method, where you are calling `self.average()` before it is defined. You should calculate the average inside the `average` method instead.</output>
```

================================================================================



--- Feedback Report for: B25CS045_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are trying to call methods (average() and grade()) before initializing the object with required arguments. You should first create an instance of Student class by calling its constructor (`__init__()`) and then call these methods.</output>
```

================================================================================



--- Feedback Report for: B25EE056_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of initialization in the `__init__` method; you should initialize `self.name`, `self.roll`, and `self.marks` before calling `self.average()` and `self.grade()`.
</output>
```

================================================================================



--- Feedback Report for: B25MT008_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're returning the `info()` method before it's fully defined. You need to move the return statement inside the function definition.</output>
```

================================================================================



--- Feedback Report for: <B25CS024>_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are missing the required positional arguments 'name', 'roll_number', and 'marks'. Ensure that these parameters are included when initializing a new Student object.
</output>
```

================================================================================



--- Feedback Report for: B25DS022_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate the average marks by calling the `average()` method, but this method doesn't exist yet. You should define it before using it.</output>
```

================================================================================



--- Feedback Report for: B25EE054_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The `__init__` method is missing required positional arguments 'name', 'roll_number', and 'marks'. Ensure these parameters are passed during object creation, e.g., `Student('John Doe', 1234, 85)`.
</output>
```

================================================================================



--- Feedback Report for: B25EC036_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance methods (`average()` and `grade()`) without initializing them first. Make sure to call these methods inside the `info()` method, or define them before using them.</output>
```

================================================================================



--- Feedback Report for: B25ME005_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `roll_number` and `marks` parameters in your `__init__` method. Make sure to include them when initializing a new `Student` object.</output>
```

================================================================================



--- Feedback Report for: B25CS059_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'r_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'r_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'r_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'r_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'r_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is a fundamental concept in Python classes. Make sure to include it when initializing the object.</output>
```

================================================================================



--- Feedback Report for: B25EE021_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the self parameter in your __init__ method, which is required for instance methods in Python. You should define it as `def __init__(self, name, roll, marks):` instead of just `def __init__(self, name, roll, marks)`. This will ensure that all required arguments are passed when creating a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EE015_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you've defined the `info()` method incorrectly. Instead of formatting the string inside the method, try creating the formatted string outside the method as a class variable or by returning it and then printing it in the main part of your code.</output>
```

================================================================================



--- Feedback Report for: B25EE002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE002_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE002_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE002_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE002_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE002_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure you are defining the Student class before trying to instantiate it, as Python looks for classes from top to bottom.</output>
```

================================================================================



--- Feedback Report for: B25ME039_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME039_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME039_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME039_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME039_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME039_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to create an instance of the `Student` class, but your code is not correctly referencing it. Make sure to use the correct capitalization for 'roll' and 'average' in the `info()` method.</output>
```

================================================================================



--- Feedback Report for: B25DS018_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of operations within the `info()` method. Currently, you're calculating the average before grading it, but according to the problem description, the grade should be calculated first based on the marks.
</output>
```

================================================================================



--- Feedback Report for: B25MT020_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'student' is not defined
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'student' is not defined
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'student' is not defined
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'student' is not defined
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] NameError: name 'student' is not defined
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Try accessing instance variables directly instead of calling methods on `self` within the `info()` method, as shown below.</output>
```

================================================================================



--- Feedback Report for: B25MT007_ q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT007_ q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT007_ q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT007_ q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT007_ q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT007_ q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are trying to access instance variables directly instead of calling methods, which is causing the 'Class Student not found' error.</output>
```

================================================================================



--- Feedback Report for: B25DS036_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The `__init__` method is missing required positional arguments 'name', 'roll_number', and 'marks'. Ensure these are passed when creating a new Student instance.</output>
```

================================================================================



--- Feedback Report for: B25MT022_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you're using the instance to initialize in the `__init__` method correctly by removing the leading underscore.</output>
```

================================================================================



--- Feedback Report for: B25EC017_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to print student information instead of returning it, which is why you're getting a TypeError. Instead of using `print()` inside the `info()` method, consider making it return a string with the desired format.</output>
```

================================================================================



--- Feedback Report for: B25EC027_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `roll_number` argument in the `__init__` method, which is required for calculating the average and grade. Make sure to include it when initializing a new `Student` object.</output>
```

================================================================================



--- Feedback Report for: B25ME035_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) before they are defined, which is causing the TypeError. You should define these methods inside the class definition.</output>
```

================================================================================



--- Feedback Report for: B25EC038_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods before they are initialized, as `self.name`, `self.roll_number`, `self.average()`, and `self.grade()` are not defined until the `__init__` method is called.</output>
```

================================================================================



--- Feedback Report for: B25EC026_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to concatenate strings with different data types. Make sure your `self.roll_number` and `self.marks` are integers, and handle them as such in your methods.</output>
```

================================================================================



--- Feedback Report for: B25MM030_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that you are calling methods before initializing the instance, as `self.roll_number` and `self.grade()` are called before `self.__init__()`. Make sure to call them after initialization.</output>
```

================================================================================



--- Feedback Report for: B25DS033_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies with the `__init__` method, where you're missing the positional arguments 'name', 'roll_number', and 'marks'. Ensure these are included when initializing a new `Student` object.
</output>
```

================================================================================



--- Feedback Report for: B25CS051_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS051_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS051_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS051_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS051_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS051_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're trying to access class methods (`average()` and `grade()`) directly on an instance, whereas they should be called using dot notation (e.g., `self.average()`).
</output>
```

================================================================================



--- Feedback Report for: B25DS003_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the __init__ method where you are using 'roll' instead of 'roll_number'. It should be 'self.roll_number' to access the instance variable correctly.</output>
```

================================================================================



--- Feedback Report for: B25EE023_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are missing the required positional arguments 'name', 'roll_number', and 'marks' in your __init__ method. Make sure these parameters are included when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25CS019_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The Student class is missing positional arguments 'name', 'roll_number', and 'marks' from its __init__ method, which should be passed when creating an instance of the class.</output>
```

================================================================================



--- Feedback Report for: B25EC024_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Change `self.roll_number` to `self.roll` to match the parameter name in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25CS022_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like the student has swapped the order of arguments in the `info()` method, which is calling `self.average()` before it's defined, resulting in a TypeError. The correct implementation should be `return f'{self.name} (Roll: {self.roll_number}) | Avg: {self.marks / len(self.marks_list):.1f} | Grade: self.grade()'.</output>
```

================================================================================



--- Feedback Report for: B25EE020_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (average(), grade()) before initializing the object with required parameters ('name', 'roll_number', 'marks'). Make sure to assign these values inside the __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25EE058_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`) before initializing them in the `__init__` method. Make sure to assign values to these variables during initialization.</output>
```

================================================================================



--- Feedback Report for: B25DS038_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure all required positional arguments are passed when initializing the Student object, as they are missing in your code.</output>
```

================================================================================



--- Feedback Report for: B25EC012_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are missing required positional arguments 'name', 'roll_number', and 'marks'. Ensure they are included when initializing a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25DS026.q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25DS026'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are trying to import 'B25DS026' which is not a valid Python module. Make sure to use the actual module name that corresponds to your class, or define it yourself.</output>
```

================================================================================



--- Feedback Report for: B25ME007_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) before they are initialized. Make sure to assign values to these variables inside the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25DS027_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) directly within your methods, but they are not defined until the object is initialized in the `__init__` method. Try accessing them through the class attributes instead.</output>
```

================================================================================



--- Feedback Report for: B25CS050_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS050_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS050_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS050_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS050_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS050_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure you are correctly calling methods from the class instance, not from the class itself. Use `self` instead of `Student` when accessing methods.</output>
```

================================================================================



--- Feedback Report for: B25ME030_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods before they are initialized. You should calculate 'avg' and 'grade' inside the info() method instead of calling them directly.</output>
```

================================================================================



--- Feedback Report for: B25MT025_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're calling methods (`grade()` and `average()`) before initializing the object, which is causing the TypeError. You should call these methods after the object has been initialized.</output>
```

================================================================================



--- Feedback Report for: B25MM001_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're using `self.name` instead of just `name`, `self.roll` instead of `roll`, and `student_avg` instead of `self.avg()`. Try changing the `info()` method to use these correct attribute names.</output>
```

================================================================================



--- Feedback Report for: B25DS001_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are calling `self.__init__()` correctly by providing all required arguments (`name`, `roll`, and `marks`), instead of directly using instance variables (`self.name`, `self.roll`, etc.) in the methods.</output>
```

================================================================================



--- Feedback Report for: {B25MM017}_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25MM017}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25MM017}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25MM017}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25MM017}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module '{B25MM017}_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the method calls `self.names`, `self.roll`, `self.average()`, and `self.grade()` which do not exist, as they should be `self.name`, `self.roll`, `self.marks` instead of using undefined instance variables.
</output>
```

================================================================================



--- Feedback Report for: B25EC006_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are passing roll_num instead of roll when initializing the Student object. Make sure to use 'roll' consistently.</output>
```

================================================================================



--- Feedback Report for: B25EE033_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of operations within the `info()` method. Currently, you're calculating the average and grade first, then returning their values as if they were strings. Instead, calculate the grade based on the average marks, which requires dividing by 4 (assuming 4 subjects) to get a percentage. Then return the calculated grade.
</output>
```

================================================================================



--- Feedback Report for: B25MT023-Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if the 'self' parameter in the __init__ method is correctly defined with all required positional arguments.</output>
```

================================================================================



--- Feedback Report for: B25EE053_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the required positional arguments 'name', 'roll_number', and 'marks' in your Student class's __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25MT015_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to create an instance of the Student class with only two arguments (name and roll), but your __init__ method requires three. You should modify the __init__ method to accept all required parameters.</output>
```

================================================================================



--- Feedback Report for: B25EE004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Ensure that all required positional arguments ('name', 'roll_number', and 'marks') are passed to the __init__ method when creating a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25DS028_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance methods (`average()` and `grade()`) without initializing the object first, which is causing a TypeError. Make sure to call these methods after creating an instance of the Student class.</output>
```

================================================================================



--- Feedback Report for: B25CS029_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods `average()` and `grade()` before initializing the object with required parameters, which is causing a TypeError. Make sure to provide all necessary arguments in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25MM004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to pass `name`, `roll_number` and `marks` as arguments when initializing the `Student` object, not as keyword arguments.</output>
```

================================================================================



--- Feedback Report for: B25EE019_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Change the function name from `_init_` to `__init__` in the Student class, as Python convention dictates that special methods like this should be written with double underscores.</output>
```

================================================================================



--- Feedback Report for: B25DS017_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Student class should accept 'name', 'roll_number' and 'marks' as keyword arguments in the __init__ method, not positional arguments.</output>
```

================================================================================



--- Feedback Report for: B25DS010_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'Marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'Marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'Marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'Marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'Marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're using `self.roll_number` instead of `self.roll`, which is a separate attribute. You should also handle the case when marks are not provided to avoid potential errors.</output>
```

================================================================================



--- Feedback Report for: B25EE030-q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate the average, grade, and info of a student without initializing the required attributes 'name', 'roll_number', and 'marks' in your __init__ method.</output>
```

================================================================================



--- Feedback Report for: b25cs049_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access the class attributes `average()` and `grade()` before they are defined. The correct approach would be to define these methods within the `__init__` method or separately, not inside the `info` method.</output>
```

================================================================================



--- Feedback Report for: B25EE031_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are using `self.rollno` instead of `self.roll`. This mismatch should be corrected by replacing `rollno` with `roll` to ensure consistency and proper attribute access.
</output>
```

================================================================================



--- Feedback Report for: B25CS004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies with the order of operations in the `info()` method. Currently, it calls `average()` and `grade()` before returning the result, but these methods should be called after the object is fully initialized, not while still being defined.</output>
```

================================================================================



--- Feedback Report for: B25EE028_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're using `self.roll_number` instead of `self.roll`, which is likely causing a typo. Ensure that the attribute names match exactly as defined in the class.
</output>
```

================================================================================



--- Feedback Report for: B25ME023 q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that you are passing only two arguments (name, roll) to the __init__ method instead of three required positional arguments 'name', 'roll_number', and 'marks'. Ensure that all necessary parameters are passed when initializing a Student object.</output>
```

================================================================================



--- Feedback Report for: B25CS047_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you forgot to pass arguments to the `__init__` method, which is why it's complaining about missing required positional arguments. Make sure to include `name`, `roll_number`, and `marks` when creating a new `Student` object.</output>
```

================================================================================



--- Feedback Report for: S25MA016_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate average marks but forgot to store them in an instance variable during initialization, so ensure that `self.marks` is assigned a value in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25EE026_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_num`, etc.) before they are initialized. Make sure to call `super().__init__(name, roll_number, marks)` in your `__init__` method.</output>
```

================================================================================



--- Feedback Report for: (B25DS042)_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 3

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
</output>
The issue lies in the fact that you're iterating over the `self.marks` list and modifying its contents by assigning a new value to `Average_marks`, which is not allowed when iterating over a sequence. Instead, calculate the average before the loop.
```

================================================================================



--- Feedback Report for: B25ME037_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to create an instance of the Student class with only two arguments (name and roll), but the class requires three: name, roll, and marks. Make sure to pass all required arguments when creating a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EC018_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has one or more Syntax Errors.
- Syntax Error: invalid syntax at line 13, offset 45

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EC018_Q21.py, line 13)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EC018_Q21.py, line 13)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EC018_Q21.py, line 13)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EC018_Q21.py, line 13)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] SyntaxError: invalid syntax (B25EC018_Q21.py, line 13)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
In the `average` method, ensure that you check if the divisor (i.e., the length of `self.marks`) is zero before performing the division to avoid a ZeroDivisionError. Use a conditional statement to handle this case.
</output>
```

================================================================================



--- Feedback Report for: B25EE003_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods before they are defined. You should define `average()`, `grade()`, and `__init__()` separately.</output>
```

================================================================================



--- Feedback Report for: B25CS039_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance methods (`average()`, `grade()`) before initializing the student object, which is causing a TypeError. Make sure to call these methods within the `__init__` method or after the object has been initialized.</output>
```

================================================================================



--- Feedback Report for: B25ME024_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you are using `self.roll_number` instead of `self.roll`. In Python, instance variables are typically accessed without underscores (e.g., `self.roll` instead of `self.roll_number`). This mismatch is causing the missing required positional arguments error.
</output>
```

================================================================================



--- Feedback Report for: B25EE029_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you are missing the required positional arguments 'name', 'roll_number', and 'marks'. Consider adding default values for these parameters to ensure they are always provided when creating a new Student object.
</output>
```

================================================================================



--- Feedback Report for: B25DS025_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you've used `self.roll_number` instead of `self.roll`. This inconsistency causes the `TypeError` because Python is case-sensitive, and `roll_number` is not a valid attribute for the class.
</output>
```

================================================================================



--- Feedback Report for: B25CS010_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that you are incorrectly calling methods (`average()`, `grade()`) within the `info()` method, which expects a string return value. Instead, consider returning the calculated values directly.</output>
```

================================================================================



--- Feedback Report for: B25DS023_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is causing the TypeError. Try adding `self` as an argument to the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25DS007_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Make sure to use `self` as the first parameter in your `__init__` method, not just `_init_`.
</output>
```

================================================================================



--- Feedback Report for: B25MT019_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to print information about yourself, but your `info()` method is calling itself incorrectly. Instead of `self.average()` and `self.grade()`, try using `self.marks` for average calculation and a separate method or formula for grade calculation.</output>
```

================================================================================



--- Feedback Report for: B25DS014_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in how you're calling methods within `info()`. Instead of calling `self.grade()` directly, you should call it as a method by adding parentheses at the end, like this: `return f'{self.name} (Roll: {self.roll_number}) | Avg: {self.avg} | Grade: {self.grade()}')`.
</output>
```

================================================================================



--- Feedback Report for: Q21 B25MM007 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing required positional arguments 'roll_number' and 'marks' in your __init__ method. You should add these parameters to the function definition.</output>
```

================================================================================



--- Feedback Report for: B25CS009_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (self.name, self.roll_number) directly inside the info() method instead of using them within the method. Try accessing and returning these values correctly.</output>
```

================================================================================



--- Feedback Report for: B25CS016_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (`average()` and `grade()`) before initializing the object, which is causing a TypeError. Make sure to assign values to `self.name`, `self.roll_number`, and `self.marks` in the `__init__` method.</output>
```

================================================================================



--- Feedback Report for: B25ME033_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollnumber', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output> The issue lies in the `info()` method, where you're calling `self.average()` and `self.grade()` before initializing the object with required attributes. You should call these methods after the object is initialized.</output>
```

================================================================================



--- Feedback Report for: B25CS044_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_num'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you are trying to use instance variables (`self.name`, `self.roll_number`, etc.) before they are initialized, as the `__init__` method does not return anything and only sets up the initial state of the object.
</output>
```

================================================================================



--- Feedback Report for: B25EC045_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method, where you're trying to access `s1` which is not defined within that scope. You should instead be accessing `self` (the instance of the class) and its attributes directly.
</output>
```

================================================================================



--- Feedback Report for: B25CS060_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are missing required positional arguments 'roll_number' and 'marks'. Make sure to include them in the method signature, like this: `def __init__(self, name, roll_number, marks)`.
</output>
```

================================================================================



--- Feedback Report for: B25EE017_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 5

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 5 required positional arguments: 'name', 'roll_number', 'marks', 'average', and 'grade'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 5 required positional arguments: 'name', 'roll_number', 'marks', 'average', and 'grade'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 5 required positional arguments: 'name', 'roll_number', 'marks', 'average', and 'grade'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 5 required positional arguments: 'name', 'roll_number', 'marks', 'average', and 'grade'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 5 required positional arguments: 'name', 'roll_number', 'marks', 'average', and 'grade'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the `grade()` method where you're trying to access `self.average` before it's initialized, as it's not calculated until the `average()` method is called.</output>
```

================================================================================



--- Feedback Report for: B25ME043_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are using `self.roll_number` instead of `self.roll` and `self.avg` instead of calling the `average()` method. Try changing it to `return (f'{self.name} (Roll : {self.roll} | Avg : {self.average()} | Grade : {self.grade()}')`. Also, you need to define `average()` and `grade()` methods in your class.</output>
```

================================================================================



--- Feedback Report for: B25ME009_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of operations within the `info()` method. Currently, you're calculating `avg` using `self.average()`, which doesn't exist. You should calculate it before calling `self.grade()`. Try rearranging the lines to first call `average()` and then use its result for both calculations.
</output>
```

================================================================================



--- Feedback Report for: B25EE050_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if all parameters are being passed correctly to the __init__ method, especially for roll_number and marks.</output>
```

================================================================================



--- Feedback Report for: B25EC011_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method. You should define it as `def __init__(self, name, roll_number, marks):` to correctly initialize the student's attributes.</output>
```

================================================================================



--- Feedback Report for: B25MT004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student() takes no arguments
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student() takes no arguments
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student() takes no arguments
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student() takes no arguments
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student() takes no arguments
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Change the function name from `_init_` to `__init__` to match Python's convention and fix the TypeError.</output>
```

================================================================================



--- Feedback Report for: B25CS054_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to pass all required arguments (name, roll_number, marks) in the __init__ method to avoid missing values when accessing them later.</output>
```

================================================================================



--- Feedback Report for: B25CS014_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance methods without initializing the object first. Make sure to call `self` before accessing its attributes, e.g., `return (f'{self.name} (Roll: {self.roll_number}) | Avg: {self.marks / len(self.marks)} | Grade: self.grade()'`. Also, ensure that you're passing all required arguments when creating a new instance of the `Student` class.</output>
```

================================================================================



--- Feedback Report for: B25ME045_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're passing separate arguments for roll_number instead of using the given roll attribute, which should be used instead.
</output>
```

================================================================================



--- Feedback Report for: B25EC022_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables before they are initialized. In your `__init__` method, you should assign values to `self.name`, `self.roll_number`, and `self.marks` instead of using them in the `info` method.</output>
```

================================================================================



--- Feedback Report for: B25DS029_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'roll_number'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing `roll` argument in your `__init__` method. You should modify it to accept `roll_number` as well, like this: `def __init__(self, name, roll_number, marks)`. Also, make sure to use the correct variable names when calling methods inside the string.</output>
```

================================================================================



--- Feedback Report for: B25MT018_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) directly within the `info` method instead of calling their corresponding methods (e.g., `name()`, `roll_number()`, `average()`, and `grade()`). Make sure to call these methods to get the desired output.</output>
```

================================================================================



--- Feedback Report for: B25CS033_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're using `roll_number` instead of `roll`. Change it to `self.roll` to fix the error.</output>
```

================================================================================



--- Feedback Report for: B25EE039_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're calling `self.average()` and `self.grade()`, but these methods don't exist yet because they haven't been defined. You need to define these methods before using them.
</output>
```

================================================================================



--- Feedback Report for: B25ME059_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance methods (`average()` and `grade()`) directly from the `__init__` method. The `__init__` method should only be used for initialization, not for accessing other methods.</output>
```

================================================================================



--- Feedback Report for: B25MT002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has one or more Syntax Errors.
- Syntax Error: expected an indented block after class definition on line 1 at line 2, offset 1

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndentationError: expected an indented block after class definition on line 1 (B25MT002_q21.py, line 2)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndentationError: expected an indented block after class definition on line 1 (B25MT002_q21.py, line 2)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndentationError: expected an indented block after class definition on line 1 (B25MT002_q21.py, line 2)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndentationError: expected an indented block after class definition on line 1 (B25MT002_q21.py, line 2)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] IndentationError: expected an indented block after class definition on line 1 (B25MT002_q21.py, line 2)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
Check that `self.marks` is not empty before calculating the average to avoid a ZeroDivisionError, and consider using a more robust data structure than a list for storing marks.
</output>
```

================================================================================



--- Feedback Report for: B25EC032_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (`self.name`, `self.roll_number`, etc.) before they are initialized. Make sure to assign values to these attributes in the constructor (`__init__` method).</output>
```

================================================================================



--- Feedback Report for: B25DS004_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate the average and grade, but you're calling these methods before initializing the instance with name, roll, and marks. You should call `self.__init__(name, roll, marks)` instead of `self.average()` and `self.grade()`. Try doing that.</output>
```

================================================================================



--- Feedback Report for: B25ME014_q21.py ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q21'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q21'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q21'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q21'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25ME014_q21'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in importing the required modules. The `B25ME014_q21` module is not imported, which is causing the ModuleNotFoundError. Make sure to import this module at the beginning of your code.
</output>
```

================================================================================



--- Feedback Report for: B25MM013_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are using `self.roll_number` instead of `self.roll`. It should be `self.roll` as per the class definition.
</output>
```

================================================================================



--- Feedback Report for: B25ME013_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are using `self.roll_num` instead of `self.roll` consistently throughout your methods.</output>
```

================================================================================



--- Feedback Report for: B25EE024_q21.py ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q21'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q21'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q21'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q21'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25EE024_q21'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you forgot to import the required modules, specifically 'B25EE024_q21'. Make sure to add `from B25EE024_q21 import *` at the beginning of your code.</output>
```

================================================================================



--- Feedback Report for: B25DS034_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Make sure to pass all required arguments (`name`, `roll_no`, and `marks`) when initializing the `Student` object with `__init__(self, name, roll, marks)`.</output>
```

================================================================================



--- Feedback Report for: B25EE025_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you are missing the required positional arguments 'name', 'roll_number', and 'marks'. Ensure that these parameters are included when initializing a new Student object.
</output>
```

================================================================================



--- Feedback Report for: B25MM008_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The Student class is missing positional arguments 'name', 'roll_number', and 'marks' in its __init__ method, which should be added as parameters to fix the TypeError.
</output>
```

================================================================================



--- Feedback Report for: B25ME018_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you forgot to pass 'roll_number' and 'marks' when initializing your Student object. Make sure to include these parameters in the __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25EC043_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're using `roll_number` instead of `roll`. In Python, instance variables are typically accessed using lowercase names. Try changing `self.roll_number` to `self.roll`.
</output>
```

================================================================================



--- Feedback Report for: B25DS006_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 1 required positional argument: 'name'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 1 required positional argument: 'name'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 1 required positional argument: 'name'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 1 required positional argument: 'name'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 1 required positional argument: 'name'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods before they are initialized. The `average()` and `grade()` methods require the roll and marks attributes, which are not set yet.</output>
```

================================================================================



--- Feedback Report for: B25EE011_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing the required positional arguments 'name', 'roll_number', and 'marks'. Ensure these are included when initializing a new Student object, like so: `Student('John Doe', 12345, 85)`.
</output>
```

================================================================================



--- Feedback Report for: B25MM023_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'mark'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'mark'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'mark'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'mark'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'mark'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the Student class's __init__ method, where 'marks' is misspelled as 'abg', causing a TypeError when trying to access 'self.abg'. Correct it by changing 'abg' to 'marks'.
</output>
```

================================================================================



--- Feedback Report for: B25CS008_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables before they are initialized. You should calculate `avg` and `grd` inside the `info()` method instead of calling them separately.</output>
```

================================================================================



--- Feedback Report for: S25MA011_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Pass the required arguments 'name', 'roll_number', and 'marks' to the __init__ method of the Student class.</output>
```

================================================================================



--- Feedback Report for: B25CS012_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access attributes (average() and grade()) before initializing them, which is causing the TypeError. You should calculate these values inside the methods themselves.</output>
```

================================================================================



--- Feedback Report for: B25EE048_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you are missing the required positional arguments 'name', 'roll_number', and 'marks'. Ensure they are included when initializing a new Student object, e.g., `Student('John Doe', 1234, 85)`.
</output>
```

================================================================================



--- Feedback Report for: B25ME034_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The Student class is missing the required positional arguments 'name', 'roll_number', and 'marks' in its __init__ method, which should be corrected to accept these parameters as follows: `def __init__(self, name, roll_number, marks)`.
</output>
```

================================================================================



--- Feedback Report for: B25DS005_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing `self.roll_number` and `self.marks` as parameters, instead of `roll` and `marks`. This is causing a TypeError when trying to access these attributes later.
</output>
```

================================================================================



--- Feedback Report for: B25CS046_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing self.roll_number and self.marks in your __init__ method. Try adding them as parameters, like this: def __init__(self, name, roll_number, marks).</output>
```

================================================================================



--- Feedback Report for: B25MT014_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Change `_init_` to `__init__` in your Student class definition.</output>
```

================================================================================



--- Feedback Report for: B25MM012_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() takes exactly one argument (the instance to initialize)
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Change the name of the function from `_init_` to `__init__` to match Python's convention for special methods.</output>
```

================================================================================



--- Feedback Report for: B25ME001_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to calculate the average marks, but your Student class is missing required positional arguments 'name', 'roll_number', and 'marks' in its __init__ method.</output>
```

================================================================================



--- Feedback Report for: B25CS056_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of initialization parameters in your `__init__` method; it should be `self.name, self.roll, self.marks` instead of `self.roll, self.name, self.marks`.
</output>
```

================================================================================



--- Feedback Report for: B25ME056_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method, where you're using positional arguments (`self.name`, `self.roll_no`, `self.marks`) instead of keyword-only arguments. In Python, when using default values for all arguments (as shown in the problem description), it's conventional to use keyword-only arguments.
</output>
```

================================================================================



--- Feedback Report for: B25DS011_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'rollno', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you forgot to pass 'marks' as an argument to the __init__ method, which is required by the Student class. Make sure to include it when creating a new Student object.</output>
```

================================================================================



--- Feedback Report for: B25EE031_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing `self.rollno` and `self.marks` parameters in your `__init__` method. Make sure to include them when initializing a new `Student` object.</output>
```

================================================================================



--- Feedback Report for: B25ME002_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you are trying to access attributes using camelCase (`self.rno` instead of `self.roll`). Ensure that attribute names match the instance variables defined in the `__init__()` method.
</output>
```

================================================================================



--- Feedback Report for: B25ME032_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME032_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME032_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME032_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME032_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25ME032_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that you are trying to access class methods (average() and grade()) directly on an instance, but these methods should be called using dot notation (e.g., `self.average()` instead of `self.average()`).</output>
```

================================================================================



--- Feedback Report for: B25CS055_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `roll_number` argument in your `__init__()` method. Try adding it as a parameter, like this: `def __init__(self, name, roll_number, marks)`. This should fix the TypeError and allow your code to run correctly.</output>
```

================================================================================



--- Feedback Report for: B25MT011.q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] ModuleNotFoundError: No module named 'B25MT011'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the fact that you're trying to access methods (`average()` and `grade()`) from an object (`self`) without defining them within the class, which is causing a ModuleNotFoundError. Make sure to define these methods inside the Student class.
</output>
```

================================================================================



--- Feedback Report for: B25CS062_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS062_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS062_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS062_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS062_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS062_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `info()` method where you're trying to access instance methods (`average()`, `grade()`) without calling them, which should be `self.average()` and `self.grade()`. This is because Python treats these as separate entities from the class itself.
</output>
```

================================================================================



--- Feedback Report for: B25EE043_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE043_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE043_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE043_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE043_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE043_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access instance variables (self.name, self.roll_no, self.mean, self.grades) directly from an instance method info() instead of returning them. Try modifying your code to return these values using f-strings or concatenation.</output>
```

================================================================================



--- Feedback Report for: B25ME021_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the `__init__` method where you're using `self.roll_number` instead of `self.roll`. Also, the order of arguments in the `__init__` method should be `name`, `roll`, and `marks` as per the problem description.</output>
```

================================================================================



--- Feedback Report for: B25MM027_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It appears that the `__init__` method is missing required positional arguments 'marks' for the Student class, which should be passed when initializing a new instance.</output>
```

================================================================================



--- Feedback Report for: B25DS019_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're missing `self.roll_number` and `self.marks`, which are required positional arguments according to the class definition, so ensure they're included when initializing a new Student object.
</output>
```

================================================================================



--- Feedback Report for: B25EE035_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of operations within the `info()` method. You are calling `self.average()` and `self.grade()` before assigning their values to `avg` and `grd`, which results in a TypeError because these methods do not return any value.
</output>
```

================================================================================



--- Feedback Report for: B25ME050_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The Student class is missing required positional arguments 'name', 'roll_number', and 'marks' in its __init__ method, which should be passed when creating a new instance of the class.</output>
```

================================================================================



--- Feedback Report for: b25me058_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're passing `self.roll_number` instead of just `roll` when calling `self.grade()` method. The correct call should be `avg = self.average() and gr = self.grade(roll)`, assuming the `grade()` method takes one argument.</output>
```

================================================================================



--- Feedback Report for: B25ME057_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're passing `self.roll_number` instead of just `roll` and `marks` when calling methods from `__init__()`.</output>
```

================================================================================



--- Feedback Report for: B25EC009_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're missing the `self` parameter in your `__init__` method, which is why it's throwing a TypeError. Make sure to include `self` as the first parameter when defining your class methods.</output>
```

================================================================================



--- Feedback Report for: B25CS028_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS028_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to access class methods (average() and grade()) on an instance of another object 'student', which is not defined anywhere in your code. You should call these methods on the current object using 'self'.</output>
```

================================================================================



--- Feedback Report for: B25MM006_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_no', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the order of method calls. The `grade()` method is called before `average()`, but it seems that `grade()` should be a function that takes the average marks as an argument, not one that calculates the grade based on the average marks.
</output>
```

================================================================================



--- Feedback Report for: B25EE038_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're initializing `self.roll_number` instead of `self.roll`, and also forgot to call `super().__init__()` in your `__init__` method. Make sure to correct these issues.</output>
```

================================================================================



--- Feedback Report for: B25CS061_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the order of operations within the `info` method. The average and grade calculations are being performed before the values are actually retrieved from the instance variables, which will result in a TypeError because `self.roll_number` and `self.marks` are not yet defined when trying to calculate the average.</output>
```

================================================================================



--- Feedback Report for: B25CS005_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>One potential issue with your code is that you're trying to call methods `average()` and `grade()` before they are defined, which would cause a `NameError` if the class was being used like this: `student = Student('John', 1, 90)`. You should define these methods in the `__init__` method where you initialize the object.</output>
```

================================================================================



--- Feedback Report for: B25EE001_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>The issue lies in the `info()` method where you are calling methods (`avg_marks()`, `grade()`) without passing any arguments, but these methods should be called on 'self'. You need to modify the method calls to use self instead of their original function names.</output>
```

================================================================================



--- Feedback Report for: B25CS020_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS020_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS020_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS020_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS020_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25CS020_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods on the class itself, but Python doesn't allow that. You should call them on an instance of the class instead.</output>
```

================================================================================



--- Feedback Report for: B25ME027_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'Name', 'Roll', and 'Marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'Name', 'Roll', and 'Marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'Name', 'Roll', and 'Marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'Name', 'Roll', and 'Marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'Name', 'Roll', and 'Marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you are trying to access instance variables (`self.Name`, `self.Roll`) directly in your `info()` method, but they should be accessed using dot notation. Try changing `f"{self.Name}"` to `f"{self.name}"` and similarly for the other variables.</output>
```

================================================================================



--- Feedback Report for: B25MT024_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 3

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check the order of operations in your average() method, as you're calculating the sum and average on each iteration of the loop.</output>
```

================================================================================



--- Feedback Report for: B25EE045_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 0

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE045_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE045_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE045_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE045_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25EE045_q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

- Technical summary was not generated.

================================================================================



--- Feedback Report for: B25DS013_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 1
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're calling methods before they are defined. In Python, you need to define your methods (like `average()`, `grade()`) before using them in other methods or functions.</output>
```

================================================================================



--- Feedback Report for: B25MT003_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods (average() and grade()) inside the info() method, but these methods are not defined anywhere in your class. Make sure to define them correctly.</output>
```

================================================================================



--- Feedback Report for: B25MM016_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>Check if you are returning the instance variables correctly in your `info()` method. Instead of calling `self.average()` and `self.grade()`, directly return `self.name`, `self.roll`, and `self.marks` respectively.</output>
```

================================================================================



--- Feedback Report for: B25EE049_q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER CLASS ERROR] TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'roll_number', and 'marks'
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>
The issue lies in the `__init__` method where you're trying to access `self.avg` and `self.grade` which are not defined anywhere, instead of using the calculated average and grade based on the marks.
</output>
```

================================================================================



--- Feedback Report for: B25MT006_Q21 ---
Assignment: csl100_q21

--- STATIC ANALYSIS (Code Structure & Potential Issues) ---

Your code has valid syntax.
- For Loops: 0
- Function Definitions: 4

--- DYNAMIC ANALYSIS (Test Results) ---

- Test 'alice': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'bob': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'no_marks': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_A': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```
- Test 'boundary_B': RUNTIME_ERROR
  - Error Details: 
```
[RUNNER ERROR] Class 'Student' not found in module 'B25MT006_Q21'.
[RUNNER CLASS ERROR] AttributeError: Class Student not found.
```

**Overall Score: 0 / 5 tests passed.**

--- AI-Generated Feedback ---

Technical Summary (for 'None'):
```
<output>It seems like you're trying to call methods that don't exist yet, so define them before calling `self.name`, `self.roll` or `self.avg()`.</output>
```

================================================================================
