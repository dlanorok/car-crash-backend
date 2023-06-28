from rest_framework import mixins

from api.common.views.event_view import EventView
from api.common.views.session_view import SessionView
from api.sketches.models import Sketch
from api.sketches.serializers import SketchSerializer


class SketchesViewSet(SessionView,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      EventView):
    queryset = Sketch.objects.all()
    serializer_class = SketchSerializer

    def get_by_session(self, session_id):
        return Sketch.objects.select_related('crash').filter(
            crash__session_id=session_id
        )
