from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmissionViewSet, get_sample_questions, system_status

router = DefaultRouter()
router.register(r'submissions', SubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
    path('run/', SubmissionViewSet.as_view({'post': 'run_code'}), name='run-code'),
    path('simple-run/', SubmissionViewSet.as_view({'post': 'simple_run_code'}), name='simple-run-code'),
    path('start-timer/', SubmissionViewSet.as_view({'post': 'start_timer'}), name='start-timer'),
    path('update-timer/', SubmissionViewSet.as_view({'post': 'update_timer'}), name='update-timer'),
    path('get-timer/', SubmissionViewSet.as_view({'get': 'get_timer'}), name='get-timer'),
    path('grading/run-autograder/', SubmissionViewSet.as_view({'post': 'run_autograder'}), name='run-autograder'),
    path('sample-questions/', get_sample_questions, name='sample-questions'),
    path('system-status/', system_status, name='system-status'),
]
