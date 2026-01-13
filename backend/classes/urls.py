from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'', ClassViewSet, basename='class')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('join-by-code/', ClassViewSet.as_view({'post': 'join_by_code'}), name='class-join-by-code'),
    path('', include(router.urls)),
]
