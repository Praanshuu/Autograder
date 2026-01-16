# Autograder

An automated grading system built with React (Vite) frontend and Django backend.

## Quick Start

**New to this project or setting up on a new laptop?** See [QUICK_START.md](QUICK_START.md)

**Detailed setup instructions:** See [SETUP.md](SETUP.md)

## Quick Setup

```bash
# 1. Install dependencies
npm install
cd backend && pip3 install -r requirements.txt

# 2. Setup database
cd backend
python3 setup_database.py

# 3. Run servers
# Terminal 1 - Backend
cd backend
python3 manage.py runserver

# Terminal 2 - Frontend
npm run dev
```

## Login Credentials

After setup, use these test accounts:
- **Teacher**: `teacher` / `password`
- **Teacher (Alt)**: `Sharingan` / `testpass123`
- **Student**: `student_315` / `password`

## Tech Stack

- **Frontend**: React + Vite + TailwindCSS
- **Backend**: Django + Django REST Framework
- **Database**: SQLite (development)
- **Authentication**: JWT (djangorestframework-simplejwt)

## Project Structure

```
Autograder/
├── src/                    # React frontend source
├── backend/                # Django backend
│   ├── autograder/        # Django project settings
│   ├── users/             # User management
│   ├── classes/           # Class management
│   ├── assignments/       # Assignment management
│   ├── submissions/       # Submission handling
│   └── db_dump.json       # Database backup
├── public/                # Static assets
└── docs/                  # Documentation
```

## Development

### Before Switching Laptops

Always backup your database before switching machines:

```bash
cd backend
python3 backup_database.py
git add db_dump.json
git commit -m "Update database dump"
git push
```

### Common Commands

```bash
# Backend
python3 manage.py migrate          # Run migrations
python3 manage.py createsuperuser  # Create admin user
python3 backup_database.py         # Backup database
python3 setup_database.py          # Restore database

# Frontend
npm run dev                        # Start dev server
npm run build                      # Build for production
npm run preview                    # Preview production build
```

## Documentation

- [Quick Start Guide](QUICK_START.md) - Get up and running fast
- [Setup Guide](SETUP.md) - Detailed setup instructions
- [API Documentation](backend/README.md) - Backend API reference
- [Architecture](backend/ARCHITECTURE.md) - System architecture

## Troubleshooting

**Database issues?**
```bash
cd backend
python3 setup_database.py
```

**Port conflicts?**
- Frontend: Vite auto-switches to next available port
- Backend: `python3 manage.py runserver 8001`

**Authentication failing?**
- Verify database is loaded: `python3 setup_database.py`
- Check credentials in QUICK_START.md

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Update database dump if needed: `python3 backend/backup_database.py`
5. Commit and push
