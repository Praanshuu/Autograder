from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'', AssignmentViewSet, basename='assignment')

urlpatterns = [
    path('', include(router.urls)),
]
