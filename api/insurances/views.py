from rest_framework import mixins

from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView
from api.insurances.models import Insurance
from api.insurances.serializers import InsuranceSerializer


class InsuranceViewSet(SessionView,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       EventView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

    def get_by_session(self, session_id):
        return Insurance.objects.select_related('car').select_related('car__crash').filter(
            car__crash__session_id=session_id
        )
