#!/bin/bash

# Autograder Quick Start Script
# Starts both frontend and backend servers

set -e

echo "🚀 Starting Autograder..."
echo "========================="

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Check if servers are already running
if lsof -Pi :5173 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${BLUE}Frontend already running on port 5173${NC}"
else
    echo -e "${BLUE}Starting frontend server...${NC}"
    npm run dev > /dev/null 2>&1 &
    echo -e "${GREEN}✓ Frontend started on http://localhost:5173${NC}"
fi

if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${BLUE}Backend already running on port 8000${NC}"
else
    echo -e "${BLUE}Starting backend server...${NC}"
    cd backend
    python3 manage.py runserver > /dev/null 2>&1 &
    cd ..
    echo -e "${GREEN}✓ Backend started on http://localhost:8000${NC}"
fi

echo ""
echo "========================="
echo -e "${GREEN}✓ Autograder is running!${NC}"
echo "========================="
echo ""
echo "  Frontend: http://localhost:5173"
echo "  Backend:  http://localhost:8000"
echo "  Admin:    http://localhost:8000/admin"
echo ""
echo "Quick credentials:"
echo "  Teacher: teacher / password"
echo "  Student: student_315 / password"
echo ""
echo "To stop servers:"
echo "  ./stop.sh"
echo ""
