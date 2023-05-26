from django.urls import path, include
from rest_framework import routers

from api.circumstances import views

router = routers.DefaultRouter()
router.register('circumstances', views.CircumstancesViewSet, basename='circumstances')

urlpatterns = [
    path('', include(router.urls)),
]
