# Docker-Based Code Execution Setup

This guide explains how to set up and use Docker-based secure code execution in the Autograder system.

## Why Docker?

Docker provides:
- **Isolation**: Student code runs in isolated containers
- **Security**: Resource limits prevent malicious code from harming the system
- **Consistency**: Same execution environment for all students
- **Safety**: No access to host filesystem, network, or system resources

## Prerequisites

### Install Docker

#### macOS
1. Download [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
2. Install and start Docker Desktop
3. Verify installation: `docker --version`

#### Linux (Ubuntu/Debian)
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker ps
```

#### Windows
1. Download [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
2. Install and start Docker Desktop
3. Verify installation in PowerShell: `docker --version`

## Setup

### Automatic Setup (Recommended)

Run the sync script which includes Docker setup:

```bash
./sync.sh
```

This will:
1. Install all dependencies
2. Check if Docker is available
3. Build the Docker image automatically

### Manual Setup

If you prefer manual setup:

```bash
# 1. Install Python Docker package
cd backend
pip3 install docker

# 2. Build Docker image
cd code_executor
./build_docker.sh

# 3. Verify image
docker images | grep autograder-executor
```

## Testing

### Test Docker Image Directly

```bash
# Simple test
echo '{"code": "print(\"Hello, World!\")", "input": ""}' | \
  docker run --rm -i autograder-executor:latest python execute.py

# Test with input
echo '{"code": "name = input()\nprint(f\"Hello, {name}!\")", "input": "Alice"}' | \
  docker run --rm -i autograder-executor:latest python execute.py

# Test with multiple inputs
echo '{"code": "a = int(input())\nb = int(input())\nprint(a + b)", "input": "5\n3"}' | \
  docker run --rm -i autograder-executor:latest python execute.py
```

### Test Through API

1. Start the backend server:
```bash
cd backend
python3 manage.py runserver
```

2. Test the run_code endpoint:
```bash
curl -X POST http://localhost:8000/api/submissions/run_code/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "code": "print(\"Hello, World!\")",
    "language": "python",
    "test_cases": [
      {"input": "", "expected_output": "Hello, World!"}
    ]
  }'
```

## How It Works

### Architecture

```
Student Code → Django API → Docker Service → Docker Container → Execute.py → Result
```

1. **Student submits code** via the web interface
2. **Django API** receives the code and test cases
3. **Docker Service** (`docker_service.py`) prepares the execution
4. **Docker Container** runs with resource limits and security restrictions
5. **Execute.py** runs the code with restricted builtins
6. **Result** is returned to the student

### Security Features

#### Container Level
- **Non-root user**: Code runs as user `coderunner` (UID 1000)
- **Network disabled**: No internet access
- **Read-only filesystem**: Cannot modify container files
- **Resource limits**:
  - Memory: 256 MB
  - CPU: 50% of one core
  - Temp space: 10 MB

#### Code Level (execute.py)
- **CPU time limit**: 5 seconds
- **Memory limit**: 256 MB
- **File size limit**: 1 MB
- **Restricted builtins**: Only safe functions available
  - ✅ Allowed: print, input, len, range, int, str, list, dict, etc.
  - ❌ Blocked: os, subprocess, open, eval, exec, import, etc.

### Fallback Behavior

If Docker is not available, the system automatically falls back to subprocess execution:

```python
# In views.py
if docker_executor.is_available() and language == 'python':
    # Use Docker (secure)
    result = docker_executor.execute_test_cases(code, test_cases)
else:
    # Fallback to subprocess (less secure)
    results = execute_code(code, language, test_cases)
```

This ensures the application works even without Docker, though with reduced security.

## Usage in Student Workspace

Students don't need to know about Docker. The system handles it automatically:

1. Student writes code in the editor
2. Student clicks "Run Code"
3. Code is executed in Docker container
4. Results are displayed in the console

## Troubleshooting

### Docker Not Running

**Error**: "Docker is not available. Please ensure Docker is running."

**Solution**:
```bash
# Check if Docker is running
docker ps

# Start Docker Desktop (macOS/Windows)
# Or start Docker daemon (Linux)
sudo systemctl start docker
```

### Image Not Found

**Error**: "Docker image not found: autograder-executor:latest"

**Solution**:
```bash
cd backend/code_executor
./build_docker.sh
```

### Permission Denied (Linux)

**Error**: "Permission denied while trying to connect to Docker daemon"

**Solution**:
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Apply changes
newgrp docker

# Or logout and login again
```

### Container Timeout

**Error**: Container execution times out

**Possible causes**:
- Infinite loop in student code
- Very slow algorithm
- Waiting for input that never comes

**Solution**: The system automatically handles timeouts (5 seconds). The student will see a timeout error.

### Memory Limit Exceeded

**Error**: "Memory limit exceeded (256 MB)"

**Possible causes**:
- Creating very large data structures
- Memory leak in student code

**Solution**: Student needs to optimize their code to use less memory.

## Development

### Modifying Resource Limits

Edit `backend/code_executor/execute.py`:

```python
# CPU time limit
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))  # Change 5 to desired seconds

# Memory limit
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))  # Change 256 to desired MB
```

After changes:
```bash
cd backend/code_executor
./build_docker.sh
```

### Adding More Builtins

Edit `backend/code_executor/execute.py`:

```python
safe_globals = {
    '__builtins__': {
        'print': print,
        'input': input,
        # Add more here
        'open': open,  # Be careful with this!
    }
}
```

### Testing Security

Try malicious code to verify security:

```python
# Should fail - no os module
import os
os.system('ls')

# Should fail - no subprocess
import subprocess
subprocess.run(['ls'])

# Should fail - no file access
open('/etc/passwd', 'r')

# Should fail - timeout
while True:
    pass

# Should fail - memory limit
big_list = [0] * (1000 * 1000 * 1000)
```

## Performance

### Benchmarks

Typical execution times:
- Container startup: ~100-200ms
- Simple code (print): ~50-100ms
- Complex code (loops): ~100-500ms
- Total (including overhead): ~200-700ms

### Optimization Tips

1. **Reuse containers**: The current implementation creates a new container for each execution. For better performance, consider container pooling.

2. **Warm up**: Build the image during deployment, not on first use.

3. **Resource limits**: Adjust limits based on your hardware and requirements.

## Production Deployment

### Docker Compose (Recommended)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - DOCKER_EXECUTOR_IMAGE=autograder-executor:latest
```

### Kubernetes

For large-scale deployments, consider Kubernetes with:
- Horizontal Pod Autoscaling
- Resource quotas
- Network policies
- Pod security policies

See the reference links in the project for more details.

## References

- [Docker Python SDK](https://docker-py.readthedocs.io/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [Resource Limits in Python](https://docs.python.org/3/library/resource.html)
- [GitHub Coderunner Project](https://github.com/your-reference)
- [HowToDoInJava Python Editor Guide](https://howtodoinjava.com/python/online-python-editor/)
