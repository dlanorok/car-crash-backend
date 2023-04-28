from rest_framework import viewsets, mixins

from api.drivers.models import Driver
from api.drivers.serializers import DriverSerializer


class DriversViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
