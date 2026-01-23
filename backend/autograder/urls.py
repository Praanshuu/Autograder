"""
URL configuration for autograder project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def api_root(request):
    """API root endpoint"""
    return JsonResponse({
        'message': 'Autograder API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'auth': {
                'register': '/api/auth/register/',
                'login': '/api/auth/login/',
                'me': '/api/users/me/'
            },
            'classes': '/api/classes/',
            'assignments': '/api/assignments/',
            'submissions': '/api/submissions/submissions/',
            'code_execution': '/api/code/run/',
            'grading': '/api/grading/',
            'notifications': '/api/notifications/'
        },
        'documentation': 'See README.md for API documentation'
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_urls')),
    path('api/users/', include('users.urls')),
    path('api/classes/', include('classes.urls')),
    path('api/assignments/', include('assignments.urls')),
    path('api/submissions/', include('submissions.urls')),
    # path('api/code/', include('submissions.urls')),
    # path('api/grading/', include('submissions.urls')),
    path('api/notifications/', include('notifications.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
