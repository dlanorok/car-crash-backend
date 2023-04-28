from django.urls import path, include
from rest_framework import routers

from api.drivers import views

router = routers.DefaultRouter()
router.register('drivers', views.DriversViewSet, basename='drivers')

urlpatterns = [
    path('', include(router.urls)),
]
