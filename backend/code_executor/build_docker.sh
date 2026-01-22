#!/bin/bash
# Build Docker image for code execution - Enhanced for production

echo "🐳 Building Docker image for secure code execution..."
echo "Optimized for high concurrency (150+ students)"

# Navigate to code_executor directory
cd "$(dirname "$0")"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Remove old image if exists
echo "🧹 Cleaning up old images..."
docker rmi autograder-executor:latest 2>/dev/null || true

# Build the image with optimizations
echo "🔨 Building optimized Docker image..."
docker build \
    --no-cache \
    --tag autograder-executor:latest \
    --label "build-date=$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
    --label "version=2.0" \
    .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo "📊 Image details:"
    docker images autograder-executor:latest
    echo ""
    echo "🧪 Testing the image..."
    
    # Test the image
    test_result=$(echo '{"code": "print(\"Docker test successful!\")", "input": ""}' | \
        docker run --rm -i autograder-executor:latest python execute.py 2>/dev/null)
    
    if echo "$test_result" | grep -q "Docker test successful"; then
        echo "✅ Image test passed!"
        echo "🚀 Ready for production use with 150+ concurrent students"
        echo ""
        echo "📋 Usage examples:"
        echo "  # Basic test:"
        echo "  echo '{\"code\": \"print(\\\"Hello, World!\\\")\", \"input\": \"\"}' | docker run --rm -i autograder-executor:latest python execute.py"
        echo ""
        echo "  # Test with input:"
        echo "  echo '{\"code\": \"name = input()\\nprint(f\\\"Hello, {name}!\\\")\", \"input\": \"Alice\"}' | docker run --rm -i autograder-executor:latest python execute.py"
        echo ""
        echo "🔧 System integration:"
        echo "  The Django backend will automatically use this image for secure code execution."
        echo "  Fallback to subprocess execution if Docker is unavailable."
    else
        echo "⚠️  Image built but test failed. Check the image manually."
        echo "Test result: $test_result"
    fi
else
    echo "❌ Failed to build Docker image"
    echo "💡 Troubleshooting tips:"
    echo "  1. Make sure Docker is running: docker ps"
    echo "  2. Check Docker permissions: docker run hello-world"
    echo "  3. On Linux, add user to docker group: sudo usermod -aG docker \$USER"
    exit 1
fi
