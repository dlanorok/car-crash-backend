from django.urls import path, include
from rest_framework import routers

from api.common.views.send_sms import SendSMSViewSet

router = routers.DefaultRouter()
router.register('send-sms', SendSMSViewSet, basename='send-sms')

urlpatterns = [
    path('', include(router.urls)),
]
