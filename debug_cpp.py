
import subprocess
import os
import sys
import tempfile
import shutil

# Add Mingw to PATH
mingw_path = r"C:\msys64\mingw64\bin"
os.environ['PATH'] = mingw_path + os.pathsep + os.environ['PATH']
print(f"Added {mingw_path} to PATH")

# Test 3: Compile in temp dir
print("\n--- Test 3: Compile in temp directory ---")
temp_dir = tempfile.mkdtemp()
print(f"Temp dir: {temp_dir}")

try:
    code = '#include <iostream>\nint main() { std::cout << "Hello from Temp"; return 0; }'
    cpp_file = os.path.join(temp_dir, "program.cpp")
    exe_file = os.path.join(temp_dir, "program") # No .exe
    
    with open(cpp_file, "w") as f:
        f.write(code)
        
    res = subprocess.run(["g++", "-Wall", cpp_file, "-o", exe_file], 
                         capture_output=True, text=True, cwd=temp_dir)
                         
    if res.returncode == 0:
        print("Compilation success!")
        # Run it
        print("--- Running ---")
        run_res = subprocess.run([exe_file], capture_output=True, text=True, cwd=temp_dir)
        print("Output:", run_res.stdout)
    else:
        print("Compilation failed!")
        print("Stdout:", res.stdout)
        print("Stderr:", res.stderr)
        
except Exception as e:
    print(f"Failed: {e}")
finally:
    shutil.rmtree(temp_dir)
    print("Cleaned up temp dir")
