from rest_framework import mixins

from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView
from api.drivers.models import Driver
from api.drivers.serializers import DriverSerializer


class DriverViewSet(SessionView,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    EventView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_by_session(self, session_id):
        return Driver.objects.select_related('car').select_related('car__crash').filter(
            car__crash__session_id=session_id
        )
