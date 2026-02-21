from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'', AssignmentViewSet, basename='assignment')

# Must be before router: else /ai-analysis-tasks/ is matched as detail {pk} and 404s
urlpatterns = [
    path('ai-analysis-tasks/', AssignmentViewSet.as_view(actions={'get': 'list_ai_analysis_tasks'})),
    path('', include(router.urls)),
]
