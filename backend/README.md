# Autograder Backend API (Django)

Backend API server for the Autograder LMS platform built with Django and Django REST Framework.

## Features

- 🔐 JWT Authentication & Authorization
- 👥 User Management (Admin, Teacher, TA, Student roles)
- 📚 Class Management (Create, Join, Archive)
- 📝 Assignment Management (Draft, Publish, Close)
- 💻 Code Execution Service (Python, JavaScript, Java, C/C++)
- ✅ Automated Grading
- 📊 Submission Tracking
- 🔔 Notification System

## Tech Stack

- **Framework**: Django 4.2
- **API**: Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (default) / PostgreSQL (production)
- **CORS**: django-cors-headers

## Prerequisites

- Python 3.8 or higher
- pip
- (Optional) PostgreSQL for production
- Python 3 (for code execution)
- Node.js (for JavaScript execution)
- Java JDK (for Java code execution)
- GCC/G++ (for C/C++ code execution)

## Installation

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the backend directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_ENGINE=django.db.backends.sqlite3
   DB_NAME=db.sqlite3
   CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional, for admin panel)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**
   ```bash
   python manage.py runserver
   ```

The server will run on `http://localhost:8000`

## Project Structure

```
backend/
├── autograder/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/               # User management app
├── classes/             # Class management app
├── assignments/          # Assignment management app
├── submissions/          # Submission & grading app
├── notifications/        # Notification system
├── manage.py
└── requirements.txt
```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user
- `GET /api/users/me/` - Get current user

### Classes
- `GET /api/classes/` - Get all classes
- `GET /api/classes/{id}/` - Get single class
- `POST /api/classes/` - Create class (Teacher/Admin)
- `PUT /api/classes/{id}/` - Update class
- `POST /api/classes/{id}/join/` - Join class
- `POST /api/classes/{id}/archive/` - Archive/unarchive class
- `GET /api/classes/{id}/people/` - Get class roster

### Assignments
- `GET /api/assignments/` - Get assignments
- `GET /api/assignments/{id}/` - Get single assignment
- `POST /api/assignments/` - Create assignment (Teacher/Admin)
- `PUT /api/assignments/{id}/` - Update assignment
- `POST /api/assignments/{id}/publish/` - Publish assignment
- `POST /api/assignments/{id}/close/` - Close assignment

### Submissions
- `GET /api/submissions/submissions/` - Get submissions
- `GET /api/submissions/submissions/{id}/` - Get single submission
- `POST /api/submissions/submissions/` - Create/update submission (Student)

### Code Execution
- `POST /api/code/run/` - Execute code against test cases

### Grading
- `PUT /api/grading/submissions/{id}/grade/` - Grade submission (Teacher/TA)
- `POST /api/grading/submissions/{id}/publish/` - Publish grade
- `POST /api/grading/grading/run-autograder/` - Run autograder

### Notifications
- `GET /api/notifications/` - Get notifications
- `PUT /api/notifications/{id}/mark_read/` - Mark as read
- `PUT /api/notifications/mark_all_read/` - Mark all as read

## Authentication

All protected endpoints require JWT authentication. Include the token in the Authorization header:

```
Authorization: Bearer <access_token>
```

To get a token:
1. Register: `POST /api/auth/register/`
2. Login: `POST /api/auth/login/`

Response includes:
```json
{
  "success": true,
  "user": {...},
  "tokens": {
    "access": "...",
    "refresh": "..."
  }
}
```

## Database Models

### User
- Custom user model with role-based access
- Roles: admin, teacher, ta, student
- Settings stored as JSON

### Class
- Class information and metadata
- Join codes for enrollment
- Archive status

### Enrollment
- Links users to classes
- Tracks role (teacher, ta, student)
- Enrollment status

### Assignment
- Assignment details and questions
- Test cases for each question
- Status (draft, published, closed)

### Submission
- Student code submissions
- Test results and auto-grading
- Manual grading and feedback

### Notification
- User notifications
- Read/unread status
- Notification types

## Code Execution

The code execution service supports:
- **Python 3** - Direct execution
- **JavaScript (Node.js)** - Node.js runtime
- **Java** - Compile and execute
- **C/C++** - Compile with GCC/G++ and execute

**Security Considerations:**
- Code execution runs in isolated temp directories
- Timeout limits prevent infinite loops
- File size limits prevent resource exhaustion
- Automatic cleanup of temp files

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin Panel
Access at `http://localhost:8000/admin/` (requires superuser)

## Production Deployment

1. Set `DEBUG=False` in `.env`
2. Set proper `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL:
   ```env
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=autograder
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
6. Use a production WSGI server (gunicorn, uwsgi)
7. Configure reverse proxy (nginx)
8. Enable HTTPS

## Environment Variables

See `.env.example` for all available environment variables.

## License

ISC
