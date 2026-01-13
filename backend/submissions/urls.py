from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmissionViewSet

router = DefaultRouter()
router.register(r'submissions', SubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
    path('run/', SubmissionViewSet.as_view({'post': 'run_code'}), name='run-code'),
    path('grading/run-autograder/', SubmissionViewSet.as_view({'post': 'run_autograder'}), name='run-autograder'),
]
