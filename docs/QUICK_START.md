# Quick Start Guide

## First Time Setup (New Laptop)

```bash
# 1. Install dependencies
npm install
cd backend && pip3 install -r requirements.txt

# 2. Setup database
cd backend
python3 setup_database.py

# 3. Run servers (in separate terminals)
# Terminal 1 - Backend
cd backend
python3 manage.py runserver

# Terminal 2 - Frontend  
npm run dev
```

## Login Credentials

- **Teacher**: `teacher` / `password`
- **Teacher (Alt)**: `Sharingan` / `testpass123`
- **Student**: `student_315` / `password`

## Before Switching Laptops

```bash
# Update database dump
cd backend
python3 manage.py dumpdata --indent 2 > db_dump.json
git add db_dump.json
git commit -m "Update database dump"
git push
```

## Troubleshooting

**Database not loading?**
```bash
cd backend
python3 setup_database.py
```

**Port already in use?**
- Frontend will auto-switch to next port
- Backend: `python3 manage.py runserver 8001`

**Need to reset everything?**
```bash
cd backend
python3 setup_database.py  # Reloads from dump
```
