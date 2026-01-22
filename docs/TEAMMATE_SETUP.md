# Easy Setup for Teammates

## The Problem You're Facing

When your teammate pushes new code, you get errors because:
- New dependencies were added (npm packages or Python packages)
- Database schema changed (new migrations)
- New features need database updates
- Configuration changed

## The Solution: One Command Setup

I've created automated scripts so you **never have to manually run setup commands again**!

## 🚀 Quick Start (First Time Setup)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Autograder
```

### 2. Run the Sync Script
```bash
./sync.sh
```

That's it! This will:
- ✅ Install all frontend dependencies (npm)
- ✅ Install all backend dependencies (pip)
- ✅ Run database migrations
- ✅ Populate test data if needed
- ✅ Add hints to questions
- ✅ Everything ready to go!

### 3. Start the Servers
```bash
./start.sh
```

Done! Both servers are running.

## 🔄 Every Time You Pull New Code

**Just run ONE command:**

```bash
./sync.sh
```

This automatically:
1. Pulls latest code from git
2. Installs any new dependencies
3. Runs new database migrations
4. Updates database if needed
5. Fixes any setup issues

**Then start the servers:**
```bash
./start.sh
```

## 📋 Available Scripts

### `./sync.sh` - Sync Everything
Run this after pulling new code. It handles all setup automatically.

```bash
./sync.sh
```

### `./start.sh` - Start Servers
Starts both frontend and backend servers.

```bash
./start.sh
```

### `./stop.sh` - Stop Servers
Stops both servers cleanly.

```bash
./stop.sh
```

## 🎯 Common Workflows

### Workflow 1: Starting Your Day
```bash
cd Autograder
./sync.sh      # Get latest code and setup
./start.sh     # Start servers
```

### Workflow 2: After Teammate Pushes
```bash
./sync.sh      # Sync everything
./start.sh     # Restart servers
```

### Workflow 3: Ending Your Day
```bash
./stop.sh      # Stop servers
```

## 🐛 Troubleshooting

### "Permission denied" Error
Make scripts executable:
```bash
chmod +x sync.sh start.sh stop.sh
```

### "Port already in use" Error
Stop existing servers first:
```bash
./stop.sh
./start.sh
```

Or manually:
```bash
# Kill frontend (port 5173)
kill $(lsof -t -i:5173)

# Kill backend (port 8000)
kill $(lsof -t -i:8000)
```

### Database Errors After Pull
Just run sync again:
```bash
./sync.sh
```

### "Module not found" Errors
The sync script should fix this, but if not:
```bash
# Frontend
npm install

# Backend
cd backend
pip3 install -r requirements.txt
```

### Migration Errors
```bash
cd backend
python3 manage.py migrate
cd ..
```

## 📝 What Each Script Does

### sync.sh
1. **Pulls latest code** from git
2. **Installs frontend dependencies** (npm install)
3. **Installs backend dependencies** (pip install)
4. **Runs database migrations** (python manage.py migrate)
5. **Checks database** and populates if empty
6. **Adds hints** to questions if missing
7. **Shows summary** of what was done

### start.sh
1. **Checks if servers are running**
2. **Starts frontend** on http://localhost:5173
3. **Starts backend** on http://localhost:8000
4. **Shows access URLs** and credentials

### stop.sh
1. **Finds running servers** on ports 5173 and 8000
2. **Stops them cleanly**
3. **Confirms shutdown**

## 🎓 For Your Teammate

Tell your teammate to add this to their commit messages when they make changes that need setup:

```
⚠️ Run ./sync.sh after pulling this commit
```

Or better yet, just **always run `./sync.sh` after pulling** - it's safe and fast!

## 💡 Pro Tips

### Tip 1: Create an Alias
Add to your `~/.zshrc` or `~/.bashrc`:
```bash
alias ag-sync='cd ~/path/to/Autograder && ./sync.sh'
alias ag-start='cd ~/path/to/Autograder && ./start.sh'
alias ag-stop='cd ~/path/to/Autograder && ./stop.sh'
```

Then from anywhere:
```bash
ag-sync   # Sync project
ag-start  # Start servers
ag-stop   # Stop servers
```

### Tip 2: Morning Routine
Create a single command for your morning routine:
```bash
./sync.sh && ./start.sh
```

### Tip 3: Check What's Running
```bash
# Check if servers are running
lsof -i :5173  # Frontend
lsof -i :8000  # Backend
```

## 🔐 Credentials

After running `./sync.sh`, you can access:

**Quick Login:**
- Teacher: `teacher` / `password`
- Student: `student_315` / `password`

**View All Users:**
```bash
cd backend
python3 list_all_users.py
```

## 📚 Manual Commands (If You Really Need Them)

### Frontend Setup
```bash
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

### Database Setup
```bash
cd backend
python3 setup_database.py
python3 add_hints_to_questions.py
```

## ✅ Checklist After Pulling Code

- [ ] Run `./sync.sh`
- [ ] Check for errors in output
- [ ] Run `./start.sh`
- [ ] Test login at http://localhost:5173
- [ ] If issues, run `./sync.sh` again

## 🆘 Still Having Issues?

1. **Stop everything:**
   ```bash
   ./stop.sh
   ```

2. **Clean sync:**
   ```bash
   ./sync.sh
   ```

3. **Start fresh:**
   ```bash
   ./start.sh
   ```

4. **Check logs:**
   - Frontend: Check terminal where you ran start.sh
   - Backend: Check terminal output
   - Browser console: F12 → Console tab

5. **Nuclear option (last resort):**
   ```bash
   # Backup your local changes first!
   git stash
   rm -rf node_modules backend/db.sqlite3
   ./sync.sh
   ```

## 🎉 Benefits

✅ **No more manual setup** - One command does everything
✅ **No more errors** - Automatic dependency installation
✅ **No more migration issues** - Auto-runs migrations
✅ **Faster workflow** - Start coding immediately
✅ **Less frustration** - Just works!

---

**Remember: After pulling code, just run `./sync.sh` and you're good to go!** 🚀
