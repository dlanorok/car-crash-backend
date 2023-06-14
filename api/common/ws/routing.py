from django.urls import re_path

from api.common.ws.consumers import ModelUpdateConsumer


websocket_urlpatterns = [
    re_path(r"ws/updates/(?P<session_id>\w+)/$", ModelUpdateConsumer.as_asgi()),
]
