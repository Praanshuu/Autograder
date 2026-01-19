#!/bin/bash

# Autograder Stop Script
# Stops both frontend and backend servers

echo "🛑 Stopping Autograder..."
echo "========================="

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Stop frontend (port 5173)
if lsof -Pi :5173 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "Stopping frontend server..."
    kill $(lsof -t -i:5173) 2>/dev/null
    echo -e "${GREEN}✓ Frontend stopped${NC}"
else
    echo "Frontend not running"
fi

# Stop backend (port 8000)
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "Stopping backend server..."
    kill $(lsof -t -i:8000) 2>/dev/null
    echo -e "${GREEN}✓ Backend stopped${NC}"
else
    echo "Backend not running"
fi

echo ""
echo "========================="
echo -e "${GREEN}✓ All servers stopped${NC}"
echo "========================="
echo ""
