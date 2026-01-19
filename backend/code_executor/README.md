# Docker-Based Code Executor

Secure, isolated code execution using Docker containers.

## Features

- **Security**: Code runs in isolated Docker containers with resource limits
- **Resource Limits**: 
  - CPU: 5 seconds max execution time
  - Memory: 256 MB limit
  - File size: 1 MB limit
- **Restricted Environment**: No network access, read-only filesystem
- **Safe Builtins**: Only safe Python builtins are available (no os, subprocess, etc.)

## Setup

### 1. Install Docker

Make sure Docker is installed and running on your system:
- macOS: [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
- Linux: [Docker Engine](https://docs.docker.com/engine/install/)
- Windows: [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)

### 2. Build the Docker Image

```bash
cd backend/code_executor
./build_docker.sh
```

Or manually:
```bash
docker build -t autograder-executor:latest .
```

### 3. Install Python Dependencies

```bash
pip install docker
```

## Usage

The Docker executor is automatically used when available. The system will:
1. Try Docker execution first (more secure)
2. Fallback to subprocess execution if Docker is not available

### Testing the Docker Image

Test the Docker image directly:

```bash
echo '{"code": "print(\"Hello, World!\")", "input": ""}' | docker run --rm -i autograder-executor:latest python execute.py
```

Expected output:
```json
{"success": true, "output": "Hello, World!", "error": ""}
```

### Testing with Input

```bash
echo '{"code": "name = input()\nprint(f\"Hello, {name}!\")", "input": "Alice"}' | docker run --rm -i autograder-executor:latest python execute.py
```

## Architecture

### Files

- `Dockerfile` - Docker image definition
- `execute.py` - Code execution script with security restrictions
- `docker_service.py` - Django service wrapper for Docker execution
- `build_docker.sh` - Build script for Docker image

### Security Features

1. **Non-root User**: Code runs as non-root user `coderunner`
2. **Resource Limits**: CPU, memory, and file size limits enforced
3. **Network Disabled**: No network access from container
4. **Read-only Filesystem**: Container filesystem is read-only
5. **Restricted Builtins**: Only safe Python builtins available
6. **Timeout**: 5-second execution timeout

### Fallback Behavior

If Docker is not available, the system automatically falls back to subprocess execution. This ensures the application works even without Docker, though with reduced security.

## Troubleshooting

### Docker Not Available

If you see "Docker is not available" errors:
1. Check if Docker is running: `docker ps`
2. Check Docker permissions: `docker run hello-world`
3. On Linux, add user to docker group: `sudo usermod -aG docker $USER`

### Image Not Found

If you see "Docker image not found" errors:
1. Build the image: `./build_docker.sh`
2. Verify image exists: `docker images | grep autograder-executor`

### Permission Denied

On Linux, if you get permission errors:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

## Development

### Modifying Security Restrictions

Edit `execute.py` to modify:
- Resource limits (CPU, memory, file size)
- Available builtins
- Timeout duration

After changes, rebuild the image:
```bash
./build_docker.sh
```

### Adding Language Support

Currently only Python is supported via Docker. Other languages (JavaScript, Java, C++) use subprocess execution.

To add Docker support for other languages:
1. Create language-specific execution script
2. Add to Dockerfile
3. Update `docker_service.py` to handle the language
