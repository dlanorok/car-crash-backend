from rest_framework import mixins

from api.circumstances.models import Circumstance
from api.circumstances.serializers import CircumstanceSerializer
from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView


class CircumstancesViewSet(SessionView,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           EventView):
    queryset = Circumstance.objects.all()
    serializer_class = CircumstanceSerializer

    def get_by_session(self, session_id):
        return Circumstance.objects.select_related('car').select_related('car__crash').filter(
            car__crash__session_id=session_id
        )

