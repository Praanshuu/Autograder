from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmissionAttemptViewSet, AssignmentProgressViewSet, GradebookViewSet

router = DefaultRouter()
router.register(r'attempts', SubmissionAttemptViewSet, basename='attempt')
router.register(r'progress', AssignmentProgressViewSet, basename='progress')
router.register(r'gradebook', GradebookViewSet, basename='gradebook')

urlpatterns = [
    path('', include(router.urls)),
]
