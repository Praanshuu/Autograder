# Autograder Setup Guide

This guide helps you set up the Autograder project on a new machine.

## Quick Setup (New Laptop)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Autograder
```

### 2. Install Dependencies

#### Frontend Dependencies
```bash
npm install
```

#### Backend Dependencies
```bash
cd backend
pip3 install -r requirements.txt
```

### 3. Restore Database

The project includes a database dump file (`backend/db_dump.json`) with all users and data. To restore it:

```bash
cd backend
python3 setup_database.py
```

This script will:
- Fix any encoding issues in the dump file
- Clear the existing database
- Load all users and data from the dump

### 4. Run the Servers

#### Start Backend (Terminal 1)
```bash
cd backend
python3 manage.py runserver
```

#### Start Frontend (Terminal 2)
```bash
npm run dev
```

### 5. Access the Application

- **Frontend**: http://localhost:5173/ (or 5174 if 5173 is in use)
- **Backend API**: http://127.0.0.1:8000/

## Test Credentials

After setup, you can login with these test accounts:

- **Teacher**: `teacher` / `password`
- **Teacher (Alt)**: `Sharingan` / `testpass123`
- **Student**: `student_315` / `password`

## Before Switching Laptops

To ensure smooth setup on your next machine, always commit these files:

### 1. Create a Fresh Database Dump
```bash
cd backend
python3 manage.py dumpdata --indent 2 > db_dump.json
git add db_dump.json
git commit -m "Update database dump"
git push
```

### 2. Commit the SQLite Database (Optional)
```bash
git add backend/db.sqlite3
git commit -m "Update SQLite database"
git push
```

**Note**: The dump file (`db_dump.json`) is more portable and recommended. The SQLite file can be used as a backup.

## Troubleshooting

### Database Issues

If you encounter database errors:

1. **Encoding Issues**: Run the setup script which handles encoding automatically
2. **Corrupted Dump**: The setup script truncates to the last valid record
3. **Missing Users**: Verify `db_dump.json` is up to date in the repo

### Port Conflicts

If ports are in use:
- Frontend: Vite will automatically try the next available port
- Backend: Stop other Django servers or change the port: `python3 manage.py runserver 8001`

### Migration Issues

If you see migration warnings:
```bash
cd backend
python3 manage.py migrate
```

## Development Workflow

1. Make changes to code
2. Test locally
3. Before committing, update the database dump if you added test data:
   ```bash
   cd backend
   python3 manage.py dumpdata --indent 2 > db_dump.json
   ```
4. Commit and push all changes

## Environment Variables

The project uses `.env` files for configuration. Check these files:
- `backend/.env` - Backend configuration
- `.env.local` - Local overrides (not committed)

Make sure to copy `.env.example` to `.env` if needed.
