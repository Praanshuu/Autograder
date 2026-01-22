#!/bin/bash

# Autograder Sync Script
# Run this after pulling new code from git
# This handles all setup automatically

set -e  # Exit on error

echo "🔄 Syncing Autograder Project..."
echo "================================"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() {
    echo -e "${BLUE}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# 1. Pull latest code
print_step "Pulling latest code from git..."
git pull origin main || {
    print_warning "Git pull failed or no changes. Continuing anyway..."
}
print_success "Code updated"

# 2. Install frontend dependencies
print_step "Installing frontend dependencies..."
if [ -f "package.json" ]; then
    npm install
    print_success "Frontend dependencies installed"
else
    print_error "package.json not found!"
    exit 1
fi

# 3. Install backend dependencies
print_step "Installing backend dependencies..."
if [ -f "backend/requirements.txt" ]; then
    cd backend
    pip3 install -r requirements.txt --quiet
    cd ..
    print_success "Backend dependencies installed"
else
    print_error "backend/requirements.txt not found!"
    exit 1
fi

# 4. Run database migrations
print_step "Running database migrations..."
cd backend
python3 manage.py migrate --noinput
print_success "Database migrations applied"

# 5. Check if database needs population
print_step "Checking database..."
USER_COUNT=$(python3 -c "
import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
print(User.objects.count())
" 2>/dev/null)

if [ "$USER_COUNT" -lt 10 ]; then
    print_warning "Database seems empty. Populating with test data..."
    python3 setup_database.py
    print_success "Database populated"
else
    print_success "Database has $USER_COUNT users"
fi

cd ..

# 6. Check for hints in questions
print_step "Checking questions for hints..."
cd backend
QUESTIONS_WITHOUT_HINTS=$(python3 -c "
import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()
from assignments.models import Question
print(Question.objects.filter(hint='').count())
" 2>/dev/null)

if [ "$QUESTIONS_WITHOUT_HINTS" -gt 0 ]; then
    print_warning "Found $QUESTIONS_WITHOUT_HINTS questions without hints. Adding hints..."
    python3 add_hints_to_questions.py > /dev/null 2>&1 || print_warning "Hints script not found or failed"
    print_success "Hints added"
fi

cd ..

# 7. Build Docker image for code execution (optional)
print_step "Checking Docker availability..."
if command -v docker &> /dev/null; then
    if docker ps &> /dev/null; then
        print_step "Building Docker image for secure code execution..."
        cd backend/code_executor
        ./build_docker.sh > /dev/null 2>&1 && print_success "Docker image built" || print_warning "Docker build failed (optional)"
        cd ../..
    else
        print_warning "Docker is installed but not running. Skipping Docker build (optional)"
    fi
else
    print_warning "Docker not installed. Code execution will use subprocess (less secure)"
fi

# 8. Summary
echo ""
echo "================================"
echo -e "${GREEN}✓ Sync Complete!${NC}"
echo "================================"
echo ""
echo "Your project is ready to use:"
echo ""
echo "  Frontend: npm run dev"
echo "  Backend:  cd backend && python3 manage.py runserver"
echo ""
echo "Or use the quick start script:"
echo "  ./start.sh"
echo ""
