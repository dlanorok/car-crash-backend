from django.urls import path, include
from rest_framework import routers

from api.sketches import views

router = routers.DefaultRouter()
router.register('sketches', views.SketchesViewSet, basename='sketches')

urlpatterns = [
    path('', include(router.urls)),
]
