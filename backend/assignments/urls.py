from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, QuestionViewSet, TestCaseViewSet

router = DefaultRouter()
router.register(r'', AssignmentViewSet, basename='assignment')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'test-cases', TestCaseViewSet, basename='testcase')

urlpatterns = [
    path('', include(router.urls)),
]
