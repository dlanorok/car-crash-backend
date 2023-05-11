from django.urls import path, include
from rest_framework import routers

from api.insurances import views

router = routers.DefaultRouter()
router.register('insurances', views.InsuranceViewSet, basename='insurances')

urlpatterns = [
    path('', include(router.urls)),
]
