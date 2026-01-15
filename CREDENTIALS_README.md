# How to Access Test Credentials

## Important Security Note

⚠️ **The credentials file is intentionally excluded from git for security reasons.**

The `CREDENTIALS.md` file and user listing scripts are in `.gitignore` to prevent accidentally exposing user data.

## How to View Credentials Locally

### Option 1: Run the User Listing Script

```bash
cd backend
python3 list_all_users.py
```

This will display:
- All usernames
- Email addresses
- Full names
- Roles (student/teacher/admin)
- Account status

### Option 2: Check the Local CREDENTIALS.md File

If you have the file locally (not in git):
```bash
cat CREDENTIALS.md
```

### Option 3: Quick Reference

**Default Password for All Test Users**: `password`

**Quick Access Accounts:**
- Teacher: `teacher` / `password`
- Teacher: `Sharingan` / `testpass123`
- Student: `student_315` / `password`
- Student: `student_1` / `password`
- Admin: `testadmin` / `password`

**Total Users**: 320 (318 students, 2 teachers)

## For New Team Members

If you're setting up the project for the first time:

1. **Setup the database**:
   ```bash
   cd backend
   python3 setup_database.py
   ```

2. **View all users**:
   ```bash
   python3 list_all_users.py
   ```

3. **Create your own CREDENTIALS.md** (optional, local only):
   ```bash
   python3 list_all_users.py > ../CREDENTIALS.txt
   ```

## Creating New Test Users

### Via Django Shell
```bash
cd backend
python3 manage.py shell
```

```python
from django.contrib.auth import get_user_model
User = get_user_model()

# Create a new user
user = User.objects.create_user(
    username='newuser',
    email='newuser@example.com',
    password='password',
    first_name='New',
    last_name='User',
    role='student'  # or 'teacher', 'ta', 'admin'
)
print(f"Created user: {user.username}")
```

### Via Registration Page
1. Go to http://localhost:5173/register
2. Fill in the form
3. Submit

## Database Access

### Django Admin Panel
1. Go to http://localhost:8000/admin
2. Login with admin credentials
3. Navigate to Users section

### Direct Database Query
```bash
cd backend
python3 manage.py dbshell
```

```sql
SELECT username, email, first_name, last_name, role 
FROM users_user 
LIMIT 10;
```

## Security Best Practices

✅ **DO:**
- Keep credentials files in `.gitignore`
- Use environment variables for production
- Change all passwords before production deployment
- Use strong, unique passwords in production
- Regularly rotate credentials

❌ **DON'T:**
- Commit credentials to git
- Share credentials in public channels
- Use test credentials in production
- Hardcode passwords in source code
- Reuse passwords across environments

## Files Excluded from Git

The following files are in `.gitignore` for security:
- `CREDENTIALS.md` - Credentials documentation
- `backend/list_all_users.py` - User listing script
- `backend/db.sqlite3` - Database file (contains user data)
- `*.sqlite3` - All SQLite database files
- `db.sqlite3.backup` - Database backups

## Need Help?

If you need access to credentials:
1. Run `python3 backend/list_all_users.py`
2. Check this README for quick reference
3. Ask a team member who has local access
4. Check the project documentation

## Production Deployment

Before deploying to production:
1. Change all default passwords
2. Use environment variables for credentials
3. Enable proper authentication
4. Set up user management system
5. Implement password reset functionality
6. Enable 2FA for admin accounts
7. Regular security audits
