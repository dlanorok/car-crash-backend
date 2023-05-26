from rest_framework import viewsets, mixins

from api.circumstances.models import Circumstance
from api.circumstances.serializers import CircumstanceSerializer
from api.common.views.session_view import SessionView


class CircumstancesViewSet(SessionView,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    queryset = Circumstance.objects.all()
    serializer_class = CircumstanceSerializer

    def get_by_session(self, session_id):
        return Circumstance.objects.select_related('car').select_related('car__crash').filter(
            car__crash__session_id=session_id[1]
        )

