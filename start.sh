#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}=== Starting Autograder ===${NC}"

# Function to kill process on a specific port
kill_port() {
    PORT=$1
    # Check if any process is listening on the port
    PID=$(lsof -t -i:$PORT)
    if [ -n "$PID" ]; then
        echo -e "${RED}Killing existing process on port $PORT (PID: $PID)...${NC}"
        kill -9 $PID
    fi
}

# Cleanup function to kill all child processes
cleanup() {
    echo -e "\n${BLUE}Shutting down...${NC}"
    # Kill the process group (negative PID)
    if [ -n "$BACKEND_PID" ]; then kill $BACKEND_PID 2>/dev/null; fi
    if [ -n "$FRONTEND_PID" ]; then kill $FRONTEND_PID 2>/dev/null; fi
    exit
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT SIGTERM

# 1. Clean up ports 8000 and 5173
echo "Checking ports..."
kill_port 8000
kill_port 5173

# 2. Check Docker
echo "Checking Docker services..."
if ! docker compose ps | grep -q "Up"; then
    echo -e "${BLUE}Docker services not running. Starting...${NC}"
    docker compose up -d
else
    echo -e "${GREEN}Docker services are running.${NC}"
fi

# 3. Start Backend
echo -e "${GREEN}Starting Backend Server (Port 8000)...${NC}"
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo -e "${RED}Virtual environment not found!${NC}"
fi

python backend/manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!

# Wait a moment for backend to initialize
sleep 2

# 4. Start Frontend
echo -e "${GREEN}Starting Frontend Server (Port 5173)...${NC}"
cd frontend
npm run dev &
FRONTEND_PID=$!

# Wait for processes
wait
