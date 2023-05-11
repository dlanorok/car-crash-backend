from rest_framework import viewsets, mixins

from api.cars.models import Car
from api.cars.serializers import CarSerializer
from api.common.views.session_view import SessionView


class CarsViewSet(
                  SessionView,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        # Create session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer.validated_data['creator'] = self.request.session.session_key

        return super().perform_create(serializer)

    def get_by_session(self, session_id):
        return Car.objects.select_related('crash').filter(crash__session_id=session_id[1])
