from rest_framework import viewsets, mixins

from api.cars.models import Car
from api.cars.serializers import CarSerializer


class CarsViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    def perform_create(self, serializer):
        # Create session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer.validated_data['creator'] = self.request.session.session_key

        return super().perform_create(serializer)
