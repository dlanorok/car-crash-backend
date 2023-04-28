from django.urls import path, include
from rest_framework import routers

from api.cars import views

router = routers.DefaultRouter()
router.register('cars', views.CarsViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
]
