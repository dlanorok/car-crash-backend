from rest_framework import mixins

from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView
from api.policy_holders.models import PolicyHolder
from api.policy_holders.serializers import PolicyHolderSerializer


class PolicyHoldersViewSet(SessionView,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           EventView):
    queryset = PolicyHolder.objects.all()
    serializer_class = PolicyHolderSerializer

    def get_by_session(self, session_id):
        return PolicyHolder.objects.select_related('car').select_related('car__crash').filter(
            car__crash__session_id=session_id
        )

