from django.urls import path, include
from rest_framework import routers

from api.crashes import views

router = routers.DefaultRouter()
router.register('crashes', views.CrashViewSet, basename='crashes')

urlpatterns = [
    path('', include(router.urls)),
]
