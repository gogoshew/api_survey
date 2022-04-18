from django.contrib import admin
from django.urls import path, include

from survey.views import SurveyViewSet, UserAnswerSet, UserSurveys, QuestionViewSet
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r'survey', SurveyViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', UserAnswerSet)
router.register(r'user_answers', UserSurveys, basename='user_answers')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/drf-auth/', include('rest_framework.urls')),
]

urlpatterns += doc_urls







