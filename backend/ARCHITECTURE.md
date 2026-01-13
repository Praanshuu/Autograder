# Backend Architecture Overview (Django)

## System Architecture

The Autograder backend is built as a RESTful API using Django and Django REST Framework, following Django's app-based architecture.

## Directory Structure

```
backend/
├── autograder/          # Main project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL configuration
│   ├── wsgi.py          # WSGI application
│   └── asgi.py          # ASGI application
│
├── users/               # User management app
│   ├── models.py        # User model
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # ViewSets
│   ├── urls.py          # URL routing
│   └── admin.py         # Django admin
│
├── classes/             # Class management app
│   ├── models.py        # Class, Enrollment models
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── assignments/         # Assignment management app
│   ├── models.py        # Assignment, Question, TestCase models
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── submissions/          # Submission & grading app
│   ├── models.py        # Submission, TestResult models
│   ├── serializers.py
│   ├── views.py
│   ├── services.py      # Code execution service
│   ├── urls.py
│   └── admin.py
│
├── notifications/        # Notification system
│   ├── models.py        # Notification model
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Data Flow

### Authentication Flow
1. User registers/logs in → `POST /api/auth/register/` or `/login/`
2. Django validates credentials and generates JWT tokens
3. Client stores tokens and includes in subsequent requests
4. JWT Authentication middleware validates token on protected routes
5. Permission classes check user role for role-based access

### Class Management Flow
1. Teacher creates class → `POST /api/classes/`
2. System generates unique join code automatically
3. Students join using code → `POST /api/classes/{id}/join/`
4. Enrollment record created linking user to class
5. Class can be archived → `POST /api/classes/{id}/archive/`

### Assignment Flow
1. Teacher creates assignment → `POST /api/assignments/`
2. Assignment starts as `draft` status
3. Teacher publishes → `POST /api/assignments/{id}/publish/`
4. Students can view and submit code
5. After deadline, teacher can close → `POST /api/assignments/{id}/close/`

### Submission & Grading Flow
1. Student submits code → `POST /api/submissions/submissions/`
2. System validates submission (deadline, enrollment)
3. Code can be tested → `POST /api/code/run/` (before submission)
4. Teacher runs autograder → `POST /api/grading/grading/run-autograder/`
5. Teacher reviews and grades → `PUT /api/grading/submissions/{id}/grade/`
6. Teacher publishes grades → `POST /api/grading/submissions/{id}/publish/`
7. Student receives notification and can view results

## Database Schema Relationships

```
User (Custom Model)
  ├── One-to-Many → Enrollment
  ├── One-to-Many → Assignment (created_by)
  └── One-to-Many → Submission (student)

Class
  ├── One-to-Many → Enrollment
  ├── One-to-Many → Assignment
  └── Foreign Key → User (owner)

Assignment
  ├── Foreign Key → Class
  ├── Foreign Key → User (created_by)
  ├── Many-to-Many → Question
  └── One-to-Many → Submission

Question
  ├── Many-to-Many → TestCase
  └── Many-to-Many → Assignment

Submission
  ├── Foreign Key → Assignment
  ├── Foreign Key → Question
  ├── Foreign Key → User (student)
  └── Many-to-Many → TestResult
```

## Security Features

### Authentication
- JWT-based stateless authentication (djangorestframework-simplejwt)
- Password hashing with Django's built-in PBKDF2
- Token expiration (configurable, default 7 days access, 30 days refresh)

### Authorization
- Role-based access control (RBAC)
- Django REST Framework permission classes:
  - `IsAuthenticated` - Requires valid JWT
  - Custom checks for resource ownership
  - Role-based checks in views

### Input Validation
- Django REST Framework serializers for request validation
- Django model field validation
- Serializer field validation

### Code Execution Security
- Timeout limits prevent infinite loops
- File size limits prevent resource exhaustion
- Isolated temp directories
- Automatic cleanup of temp files
- No network access from executed code (sandboxed)

## API Design Principles

### RESTful Conventions
- Resource-based URLs (`/api/classes/`, `/api/assignments/`)
- HTTP methods: GET (read), POST (create), PUT (update), PATCH (partial update), DELETE (remove)
- Status codes: 200 (success), 201 (created), 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found), 500 (server error)

### Response Format
```json
{
  "success": true,
  "data": { ... },
  "message": "Optional message"
}
```

### Error Format
```json
{
  "message": "Error message",
  "errors": { ... } // Field errors
}
```

## Code Execution Service

### Supported Languages
- **Python 3**: Direct execution via `python3`
- **JavaScript**: Node.js runtime
- **Java**: Compile with `javac`, execute with `java`
- **C/C++**: Compile with `gcc`/`g++`, execute binary

### Execution Flow
1. Validate code and test cases
2. Create temporary files in isolated directory
3. Write code to language-specific file
4. Compile (if needed) or execute directly
5. Feed test case input via stdin
6. Capture stdout/stderr
7. Compare output with expected output
8. Return test results
9. Cleanup temp files

### Limitations
- Execution timeout (default 10 seconds)
- Memory limits (not enforced, but monitored)
- No file system access outside temp directory
- No network access
- Single-threaded execution

## Django-Specific Features

### Admin Panel
- Built-in Django admin at `/admin/`
- Custom admin interfaces for all models
- User-friendly management interface

### Migrations
- Database schema versioning
- Automatic migration generation
- Safe database updates

### ORM
- Django ORM for database operations
- Query optimization with `select_related` and `prefetch_related`
- Database-agnostic (SQLite, PostgreSQL, MySQL, etc.)

## Future Enhancements

### AI Grading Integration
- Placeholder endpoint exists: `POST /api/grading/grading/run-autograder/`
- Can integrate with:
  - OpenAI API for code review
  - Custom ML models for grading
  - Third-party code analysis services

### Real-time Features
- Django Channels for WebSocket support
- Real-time notifications
- Live collaboration features

### Advanced Features
- Code plagiarism detection
- Performance analytics
- Advanced code metrics
- Integration with version control (Git)

## Scalability Considerations

### Current Architecture
- Monolithic Django application
- SQLite for development, PostgreSQL for production
- File-based code execution

### Scaling Options
1. **Horizontal Scaling**: Load balancer + multiple Django instances
2. **Database**: PostgreSQL with connection pooling, read replicas
3. **Code Execution**: 
   - Docker containers for isolation
   - Celery for async task execution
   - Separate execution service/microservice
4. **Caching**: Redis for frequently accessed data
5. **CDN**: For static assets
6. **Database Optimization**: Indexes, query optimization

## Testing Strategy

### Unit Tests
- Django TestCase for model tests
- DRF APITestCase for API tests
- Mock external services

### Integration Tests
- Test complete API workflows
- Test authentication flows
- Test code execution service

### E2E Tests
- Test complete user workflows
- Test error scenarios

## Deployment

### Development
```bash
python manage.py runserver
```

### Production
```bash
# Using Gunicorn
gunicorn autograder.wsgi:application --bind 0.0.0.0:8000

# Using uWSGI
uwsgi --http :8000 --module autograder.wsgi
```

### Recommended Production Setup
- Process manager: systemd or supervisor
- WSGI server: Gunicorn or uWSGI
- Reverse proxy: Nginx
- Database: PostgreSQL
- Static files: Nginx or CDN
- Monitoring: Application monitoring (e.g., Sentry)
- Logging: Centralized logging (e.g., ELK stack)

## Environment Configuration

All configuration via environment variables (see `.env.example`):
- Database connection
- JWT secrets
- Service endpoints
- Feature flags

## Error Handling

- Django REST Framework exception handling
- Custom exception handlers
- Consistent error response format
- Error logging for debugging
- User-friendly error messages

## Performance Optimization

- Database indexes on frequently queried fields
- Pagination for large result sets
- Efficient queries with `select_related` and `prefetch_related`
- Database connection pooling
- Response compression (middleware)
- Caching (Redis/Memcached)
