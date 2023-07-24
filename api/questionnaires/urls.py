from django.urls import path, include
from rest_framework import routers

from api.questionnaires import views

router = routers.DefaultRouter()
router.register('questionnaires', views.QuestionnaireViewSet, basename='questionnaires')

urlpatterns = [
    path('', include(router.urls)),
]
