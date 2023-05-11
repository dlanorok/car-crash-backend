from django.urls import path, include
from rest_framework import routers

from api.policy_holders import views

router = routers.DefaultRouter()
router.register('policy_holders', views.PolicyHoldersViewSet, basename='policy_holders')

urlpatterns = [
    path('', include(router.urls)),
]
