from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'', ClassViewSet, basename='class')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('', include(router.urls)),
]
