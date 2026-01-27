#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Starting Autograder ===${NC}"

# Ensure Docker is up
echo "Checking Docker services..."
docker compose up -d

# Add MinGW to PATH for C/C++ support (Windows)
export PATH="/c/msys64/mingw64/bin:$PATH"

# Activate Virtual Env
source venv/bin/activate

# Function to kill background processes on exit
cleanup() {
    echo -e "\n${BLUE}Shutting down...${NC}"
    kill $BACKEND_PID
    exit
}

trap cleanup SIGINT

# Start Backend
echo -e "${GREEN}Starting Backend Server (Port 8000)...${NC}"
python backend/manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!

# Start Frontend
echo -e "${GREEN}Starting Frontend Server (Port 5173)...${NC}"
cd frontend
npm run dev

# Wait for backend (this line technically unreachable due to npm run dev blocking, but good practice)
wait $BACKEND_PID
