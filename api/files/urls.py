from django.urls import path, include
from rest_framework import routers

from api.files import views

router = routers.DefaultRouter()
router.register('files', views.FileViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
]
