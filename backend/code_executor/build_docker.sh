#!/bin/bash
# Build Docker image for code execution

echo "Building Docker image for secure code execution..."

# Navigate to code_executor directory
cd "$(dirname "$0")"

# Build the image
docker build -t autograder-executor:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo "Image name: autograder-executor:latest"
    echo ""
    echo "To test the image, run:"
    echo "  docker run --rm -i autograder-executor:latest python execute.py"
else
    echo "❌ Failed to build Docker image"
    exit 1
fi
