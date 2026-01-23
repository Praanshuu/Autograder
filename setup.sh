#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Autograder Local Setup ===${NC}"

# 1. Prerequisite Checks
echo -e "\n${BLUE}[1/5] Checking prerequisites...${NC}"
command -v docker >/dev/null 2>&1 || { echo >&2 "Docker is required but not installed. Aborting."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is required. Aborting."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo >&2 "NPM/Node is required. Aborting."; exit 1; }

# 2. Infrastructure (Docker)
echo -e "\n${BLUE}[2/5] Starting Docker services (Postgres, Redis, MinIO)...${NC}"
docker compose up -d
echo -e "${GREEN}Docker services started.${NC}"

# 3. Python Backend
echo -e "\n${BLUE}[3/5] Setting up Backend (Python/Django)...${NC}"
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
echo "Installing Python dependencies..."
pip install -r backend/requirements.txt

echo "Running Migrations..."
python backend/manage.py migrate

# 4. Frontend
echo -e "\n${BLUE}[4/5] Setting up Frontend (React/Vite)...${NC}"
cd frontend
npm install
cd ..

# 5. Final Message
echo -e "\n${GREEN}=== Setup Complete! ===${NC}"
echo -e "You can now run the project using: ${BLUE}./start.sh${NC}"
