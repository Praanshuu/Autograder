# Troubleshooting Guide

## Common Errors and Solutions

### ❌ Error: "ERR_CONNECTION_REFUSED" or "Network Error"

**What it means**: The backend server is not running.

**Solution**:
```bash
./start.sh
```

Or manually:
```bash
cd backend
python3 manage.py runserver
```

**How to check if backend is running**:
```bash
lsof -i :8000
```

If nothing shows up, the backend is not running.

---

### ❌ Error: "Failed to load resource: net::ERR_CONNECTION_REFUSED"

**What it means**: Either frontend or backend (or both) are not running.

**Solution**:
```bash
./stop.sh    # Stop any existing servers
./start.sh   # Start fresh
```

**Check what's running**:
```bash
# Check frontend (port 5173)
lsof -i :5173

# Check backend (port 8000)
lsof -i :8000
```

---

### ❌  "Module not found" or "ModuleNotFoundError"

**What it means**: Missing Python or npm dependencies.

**Solution**:
```bash
./sync.sh
```

Or manually:
```bash
# Frontend
npm install

# Backend
cd backend
pip3 install -r requirements.txt
```

---

### ❌ Error: "Migration not applied" or Database errors

**What it means**: Database schema is out of sync.

**Solution**:
```bash
cd backend
python3 manage.py migrate
```

Or use sync script:
```bash
./sync.sh
```

---

### ❌ Error: "Port already in use"

**What it means**: A server is already running on that port.

**Solution**:
```bash
./stop.sh
./start.sh
```

Or manually kill the process:
```bash
# Kill frontend (port 5173)
kill $(lsof -t -i:5173)

# Kill backend (port 8000)
kill $(lsof -t -i:8000)
```

---

### ❌ Error: "CORS error" or "Access-Control-Allow-Origin"

**What it means**: Frontend and backend are not communicating properly.

**Check**:
1. Is backend running on port 8000?
2. Is frontend running on port 5173?

**Solution**:
```bash
./stop.sh
./start.sh
```

---

### ❌ Error: "401 Unauthorized" or "Invalid credentials"

**What it means**: Wrong username/password or not logged in.

**Solution**:
Use correct credentials:
- Teacher: `teacher` / `password`
- Student: `student_315` / `password`

**View all users**:
```bash
cd backend
python3 list_all_users.py
```

---

### ❌ Error: "404 Not Found" on API endpoints

**What it means**: API endpoint doesn't exist or URL is wrong.

**Check**:
1. Is backend running?
2. Check the URL in browser console

**Common endpoints**:
- Login: `http://localhost:8000/api/auth/simple-login/`
- Users: `http://localhost:8000/api/users/me/`
- Classes: `http://localhost:8000/api/classes/`

---

### ❌ Frontend shows blank page

**What it means**: Frontend build error or not running.

**Solution**:
```bash
# Check browser console (F12)
# Look for errors

# Restart frontend
./stop.sh
npm install
./start.sh
```

---

### ❌ Backend shows "ModuleNotFoundError: No module named 'anymail'"

**What it means**: Missing django-anymail package.

**Solution**:
```bash
cd backend
pip3 install django-anymail
```

Or update requirements:
```bash
./sync.sh
```

---

## Quick Fixes

### Nuclear Option (When Nothing Works)

⚠️ **Warning**: This will reset everything. Backup your local changes first!

```bash
# 1. Stop everything
./stop.sh

# 2. Backup your changes
git stash

# 3. Clean everything
rm -rf node_modules
rm -rf backend/db.sqlite3

# 4. Fresh sync
./sync.sh

# 5. Start servers
./start.sh

# 6. Restore your changes (if needed)
git stash pop
```

---

## Checking Server Status

### Is Backend Running?
```bash
curl http://localhost:8000/api/
```

If you get a response, backend is running.

### Is Frontend Running?
Open browser: http://localhost:5173

If you see the app, frontend is running.

### Check Both Servers
```bash
# Backend
lsof -i :8000

# Frontend
lsof -i :5173
```

---

## Common Workflow Issues

### After Pulling Code from Git

**Problem**: Code doesn't work after pulling.

**Solution**:
```bash
./sync.sh
./start.sh
```

### After Teammate Pushes

**Problem**: Errors after teammate pushes new code.

**Solution**:
```bash
./stop.sh
./sync.sh
./start.sh
```

### Starting Work Each Day

**Problem**: Forgot what to run.

**Solution**:
```bash
cd Autograder
./sync.sh    # Get latest code
./start.sh   # Start servers
```

---

## Debug Mode

### Enable Verbose Logging

**Backend**:
Edit `backend/autograder/settings.py`:
```python
DEBUG = True
```

**Frontend**:
Check browser console (F12 → Console tab)

### Check Backend Logs

If using `./start.sh`, check terminal output.

Or run manually to see logs:
```bash
cd backend
python3 manage.py runserver
```

### Check Frontend Logs

Browser console (F12 → Console tab)

---

## Still Having Issues?

### 1. Check the Basics
- [ ] Is backend running? (`lsof -i :8000`)
- [ ] Is frontend running? (`lsof -i :5173`)
- [ ] Did you run `./sync.sh` after pulling?
- [ ] Are you on the correct branch?

### 2. Try Clean Restart
```bash
./stop.sh
./sync.sh
./start.sh
```

### 3. Check Browser Console
Press F12 → Console tab
Look for red error messages

### 4. Check Backend Terminal
Look for error messages in the terminal where backend is running

### 5. Ask for Help
Share:
- Error message (screenshot or copy-paste)
- What you were trying to do
- Browser console errors
- Backend terminal errors

---

## Prevention Tips

✅ **Always run `./sync.sh` after pulling code**

✅ **Use `./start.sh` to start servers** (not manual commands)

✅ **Use `./stop.sh` before closing terminal** (clean shutdown)

✅ **Check if servers are running** before reporting errors

✅ **Keep dependencies updated** (run `./sync.sh` regularly)

---

## Quick Reference

```bash
# Daily workflow
./sync.sh      # Sync everything
./start.sh     # Start servers
./stop.sh      # Stop servers

# Check status
lsof -i :8000  # Backend
lsof -i :5173  # Frontend

# View credentials
cd backend && python3 list_all_users.py

# Clean restart
./stop.sh && ./sync.sh && ./start.sh
```

---

**Remember**: Most errors are fixed by running `./sync.sh`! 🚀
