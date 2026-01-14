# Project Setup & Handoff Guide

## Overview
This is the Autograder project. It consists of:
- **Frontend**: React + Vite + Tailwind (`/`)
- **Backend**: Django Rest Framework + SQLite (`/backend`)

## Prerequisites
- Node.js (v18+)
- Python (3.10+)
- Git

## Setup Instructions

### 1. Backend Setup (Django)
```bash
cd backend
# Create virtual environment
python -m venv venv
# Activate venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Database
# The 'db.sqlite3' file is INCLUDED in the repo for this handoff.
# You do NOT need to run migrations or seed data.
# It contains all the test data (Classes, Students, Assignments) we just set up.

# Run Server
python manage.py runserver
```

### 2. Frontend Setup (React)
```bash
# Return to root
cd ..
# Install node modules
npm install
# Run Dev Server
npm run dev
```

## Testing Login
The database comes pre-loaded with these accounts:
- **Teacher**: `teacher@example.com` / `password`
- **Student**: `student@example.com` / `password`

## Current Status
- **Teacher Dashboard**: Fully functional analytics and class management.
- **Student Workspace**: UI is ready, Layout is fixed.
- **Autograding**: The `execution` app structure is planned but NOT implemented yet.
