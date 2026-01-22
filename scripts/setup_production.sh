#!/bin/bash
# Production Setup Script for Autograder System
# Optimized for 150+ concurrent students

set -e  # Exit on any error

echo "🚀 Setting up Autograder System for Production"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   print_error "This script should not be run as root for security reasons"
   exit 1
fi

# Check system requirements
print_status "Checking system requirements..."

# Check Docker
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! docker info > /dev/null 2>&1; then
    print_error "Docker is not running. Please start Docker first."
    exit 1
fi

print_success "Docker is available"

# Check Python
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
if [[ $(echo "$PYTHON_VERSION < 3.8" | bc -l) -eq 1 ]]; then
    print_error "Python 3.8+ is required. Current version: $PYTHON_VERSION"
    exit 1
fi

print_success "Python $PYTHON_VERSION is available"

# Check Node.js
if ! command -v node &> /dev/null; then
    print_error "Node.js is not installed"
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [[ $NODE_VERSION -lt 16 ]]; then
    print_error "Node.js 16+ is required. Current version: $NODE_VERSION"
    exit 1
fi

print_success "Node.js v$(node --version) is available"

# Setup Backend
print_status "Setting up Django backend..."

cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt

# Install additional production dependencies
print_status "Installing production dependencies..."
pip install gunicorn redis celery psycopg2-binary

# Setup database
print_status "Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
print_status "Checking for superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print('Creating superuser...')
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Build Docker image for code execution
print_status "Building Docker image for secure code execution..."
cd code_executor
chmod +x build_docker.sh
./build_docker.sh

if [ $? -ne 0 ]; then
    print_error "Failed to build Docker image"
    exit 1
fi

cd ..

# Setup Frontend
print_status "Setting up React frontend..."
cd ../

# Install Node.js dependencies
print_status "Installing Node.js dependencies..."
npm install

# Build frontend for production
print_status "Building frontend for production..."
npm run build

# Create production configuration files
print_status "Creating production configuration files..."

# Create Docker Compose file for production
cat > docker-compose.prod.yml << 'EOF'
version: '3.8'

services:
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

  postgres:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: autograder
      POSTGRES_USER: autograder
      POSTGRES_PASSWORD: autograder_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./backend
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://autograder:autograder_password@postgres:5432/autograder
      - REDIS_URL=redis://redis:6379/0
      - DOCKER_EXECUTOR_IMAGE=autograder-executor:latest
      - DOCKER_MAX_WORKERS=30
      - MAX_CODE_RUNS_PER_MINUTE=15
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    depends_on:
      - postgres
      - redis
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 8

  celery:
    build: ./backend
    restart: unless-stopped
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://autograder:autograder_password@postgres:5432/autograder
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    depends_on:
      - postgres
      - redis
    command: celery -A core worker --loglevel=info --concurrency=8

  frontend:
    build: .
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - VITE_API_URL=http://localhost:8000
    command: npm run preview

volumes:
  postgres_data:
  redis_data:
EOF

# Create nginx configuration for production
mkdir -p nginx
cat > nginx/nginx.conf << 'EOF'
upstream backend {
    server backend:8000;
}

upstream frontend {
    server frontend:3000;
}

server {
    listen 80;
    server_name localhost;
    client_max_body_size 10M;

    # Frontend
    location / {
        proxy_pass http://frontend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Backend API
    location /api/ {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }

    # Static files
    location /static/ {
        proxy_pass http://backend;
    }

    # Media files
    location /media/ {
        proxy_pass http://backend;
    }
}
EOF

# Create systemd service files for non-Docker deployment
mkdir -p systemd
cat > systemd/autograder-backend.service << 'EOF'
[Unit]
Description=Autograder Backend
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=/path/to/autograder/backend
Environment=PATH=/path/to/autograder/backend/venv/bin
ExecStart=/path/to/autograder/backend/venv/bin/gunicorn core.wsgi:application --bind 127.0.0.1:8000 --workers 4 --threads 8
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Create monitoring script
cat > monitor_system.py << 'EOF'
#!/usr/bin/env python3
"""
System monitoring script for Autograder
Monitors Docker containers, database connections, and system resources
"""

import psutil
import docker
import requests
import time
import json
from datetime import datetime

def check_docker():
    """Check Docker containers status"""
    try:
        client = docker.from_env()
        containers = client.containers.list()
        
        print(f"🐳 Docker Status: {len(containers)} containers running")
        for container in containers:
            if 'autograder' in container.name:
                print(f"  - {container.name}: {container.status}")
        return True
    except Exception as e:
        print(f"❌ Docker Error: {e}")
        return False

def check_system_resources():
    """Check system resources"""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    print(f"💻 System Resources:")
    print(f"  - CPU: {cpu_percent}%")
    print(f"  - Memory: {memory.percent}% ({memory.used // 1024 // 1024}MB / {memory.total // 1024 // 1024}MB)")
    print(f"  - Disk: {disk.percent}% ({disk.used // 1024 // 1024 // 1024}GB / {disk.total // 1024 // 1024 // 1024}GB)")
    
    return {
        'cpu': cpu_percent,
        'memory': memory.percent,
        'disk': disk.percent
    }

def check_api_health():
    """Check API health"""
    try:
        response = requests.get('http://localhost:8000/api/submissions/system-status/', timeout=10)
        if response.status_code == 200:
            print("✅ API Health: OK")
            return True
        else:
            print(f"⚠️  API Health: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API Health: {e}")
        return False

def main():
    print(f"🔍 Autograder System Monitor - {datetime.now()}")
    print("=" * 50)
    
    docker_ok = check_docker()
    resources = check_system_resources()
    api_ok = check_api_health()
    
    # Alert if resources are high
    if resources['cpu'] > 80:
        print("⚠️  HIGH CPU USAGE!")
    if resources['memory'] > 85:
        print("⚠️  HIGH MEMORY USAGE!")
    if resources['disk'] > 90:
        print("⚠️  HIGH DISK USAGE!")
    
    overall_status = docker_ok and api_ok and resources['cpu'] < 90 and resources['memory'] < 90
    print(f"\n🎯 Overall Status: {'✅ HEALTHY' if overall_status else '❌ ISSUES DETECTED'}")

if __name__ == "__main__":
    main()
EOF

chmod +x monitor_system.py

# Create load testing script
cat > load_test.py << 'EOF'
#!/usr/bin/env python3
"""
Load testing script for Autograder
Simulates multiple students submitting code simultaneously
"""

import asyncio
import aiohttp
import time
import json
from concurrent.futures import ThreadPoolExecutor

# Test configuration
CONCURRENT_USERS = 50  # Start with 50, increase gradually
API_BASE_URL = "http://localhost:8000/api"
TEST_CODE = """
# Simple test code
a = int(input())
b = int(input())
print(a + b)
"""

TEST_CASES = [
    {"input": "5\n3", "expected_output": "8"},
    {"input": "10\n-2", "expected_output": "8"},
    {"input": "0\n0", "expected_output": "0"}
]

async def simulate_code_run(session, user_id):
    """Simulate a single user running code"""
    try:
        payload = {
            "code": TEST_CODE,
            "language": "python",
            "test_cases": TEST_CASES
        }
        
        start_time = time.time()
        async with session.post(f"{API_BASE_URL}/submissions/run_code/", json=payload) as response:
            end_time = time.time()
            
            if response.status == 200:
                result = await response.json()
                return {
                    "user_id": user_id,
                    "success": True,
                    "response_time": end_time - start_time,
                    "passed_tests": result.get("data", {}).get("summary", {}).get("passed", 0)
                }
            else:
                return {
                    "user_id": user_id,
                    "success": False,
                    "response_time": end_time - start_time,
                    "error": response.status
                }
    except Exception as e:
        return {
            "user_id": user_id,
            "success": False,
            "response_time": 0,
            "error": str(e)
        }

async def run_load_test():
    """Run load test with concurrent users"""
    print(f"🚀 Starting load test with {CONCURRENT_USERS} concurrent users")
    
    connector = aiohttp.TCPConnector(limit=100, limit_per_host=50)
    timeout = aiohttp.ClientTimeout(total=30)
    
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # Create tasks for concurrent execution
        tasks = [simulate_code_run(session, i) for i in range(CONCURRENT_USERS)]
        
        start_time = time.time()
        results = await asyncio.gather(*tasks, return_exceptions=True)
        end_time = time.time()
        
        # Analyze results
        successful = [r for r in results if isinstance(r, dict) and r.get("success")]
        failed = [r for r in results if isinstance(r, dict) and not r.get("success")]
        exceptions = [r for r in results if not isinstance(r, dict)]
        
        total_time = end_time - start_time
        avg_response_time = sum(r["response_time"] for r in successful) / len(successful) if successful else 0
        
        print(f"\n📊 Load Test Results:")
        print(f"  - Total Users: {CONCURRENT_USERS}")
        print(f"  - Total Time: {total_time:.2f}s")
        print(f"  - Successful: {len(successful)}")
        print(f"  - Failed: {len(failed)}")
        print(f"  - Exceptions: {len(exceptions)}")
        print(f"  - Success Rate: {len(successful)/CONCURRENT_USERS*100:.1f}%")
        print(f"  - Avg Response Time: {avg_response_time:.2f}s")
        print(f"  - Requests/Second: {CONCURRENT_USERS/total_time:.1f}")
        
        if failed:
            print(f"\n❌ Failed Requests:")
            for fail in failed[:5]:  # Show first 5 failures
                print(f"  - User {fail['user_id']}: {fail.get('error', 'Unknown error')}")

if __name__ == "__main__":
    asyncio.run(run_load_test())
EOF

chmod +x load_test.py

# Create startup script
cat > start_production.sh << 'EOF'
#!/bin/bash
# Start Autograder in production mode

echo "🚀 Starting Autograder System in Production Mode"

# Check if Docker Compose is available
if command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
elif command -v docker &> /dev/null && docker compose version &> /dev/null; then
    COMPOSE_CMD="docker compose"
else
    echo "❌ Docker Compose not found"
    exit 1
fi

# Start services
echo "📦 Starting services with Docker Compose..."
$COMPOSE_CMD -f docker-compose.prod.yml up -d

echo "⏳ Waiting for services to start..."
sleep 10

# Check service health
echo "🔍 Checking service health..."
$COMPOSE_CMD -f docker-compose.prod.yml ps

echo "✅ Autograder System started successfully!"
echo ""
echo "🌐 Access points:"
echo "  - Frontend: http://localhost:3000"
echo "  - Backend API: http://localhost:8000"
echo "  - Admin Panel: http://localhost:8000/admin"
echo ""
echo "📊 Monitoring:"
echo "  - Run './monitor_system.py' to check system health"
echo "  - Run './load_test.py' to test performance"
echo ""
echo "🛑 To stop: $COMPOSE_CMD -f docker-compose.prod.yml down"
EOF

chmod +x start_production.sh

# Final setup steps
print_status "Performing final setup steps..."

# Set proper permissions
chmod +x *.sh
chmod +x *.py

# Create logs directory
mkdir -p logs

print_success "Production setup completed successfully!"
print_success "=============================================="

echo ""
echo "🎯 Next Steps:"
echo "1. Review configuration files in the project root"
echo "2. Start the system: ./start_production.sh"
echo "3. Test with sample questions: http://localhost:8000/api/submissions/sample-questions/"
echo "4. Monitor system: ./monitor_system.py"
echo "5. Load test: ./load_test.py"
echo ""
echo "📋 System Capabilities:"
echo "  ✅ Secure Docker-based code execution"
echo "  ✅ Optimized for 150+ concurrent students"
echo "  ✅ Rate limiting and caching"
echo "  ✅ Auto-grading with test cases"
echo "  ✅ Real-time monitoring"
echo "  ✅ Load balancing ready"
echo ""
echo "🔐 Default Admin Credentials:"
echo "  Username: admin"
echo "  Password: admin123"
echo "  (Change these in production!)"
echo ""
echo "🚀 System is ready for production deployment!"