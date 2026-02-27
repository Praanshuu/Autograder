# Goal Description
The dynamic analyzer returns syntax and compilation errors with the `error_message` key instead of the `error` key. In `backend/submissions/services.py`, the `_execute_python_with_output` method expects the key `error` when the Batch Runner is used (`res.get('error', '')`). This causes syntax errors to be silently swallowed, resulting in empty error messages and the frontend displaying a generic "(no output)" and "❌ Output mismatch".
The objective is to fix the error key extraction so that the user actually sees the syntax error on the frontend.

## Proposed Changes

### Backend Submissions Service

#### [MODIFY] services.py(file:///home/anshul/Projects/Autograder/backend/submissions/services.py)
In `_execute_python_with_output` (around line 219), change how `err_msg` is extracted from the batch result.
It currently does:
```python
                 err_msg = res.get('error', '')
```
Change it to extract from both possible keys (`error_message` or `error`):
```python
                 err_msg = res.get('error_message', res.get('error', ''))
```

## Verification Plan

### Automated Tests
1. Run the `test_execution.py` script locally that intentionally feeds `SyntaxError` code to the executor.
2. Verify that the returned result contains `FINAL RESULT = [{'status': 'runtime_error', 'console_output': '', 'error_message': 'Traceback (...)'}]` with the traceback in `error_message`.

### Manual Verification
1. Navigate to the frontend Practice Workspace or Student Workspace.
2. Attempt to submit Python code with a deliberate syntax error (e.g. `for i in range n:\n  pass`).
3. Verify that the UI displays a red `❌ Error:` box containing the syntax error traceback instead of "(no output)".
