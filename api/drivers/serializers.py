from rest_framework import serializers

from api.cars.models import Car
from api.common.models.base import RevisionModel
from api.common.serializer import ValidationSerializer, CreateSerializerStateChange
from api.drivers.models import Driver


class DriverSerializer(ValidationSerializer, CreateSerializerStateChange):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=False)

    class Meta:
        model = Driver
        fields = '__all__'

    def validate(self, attrs):
        if not self.should_validate():
            return attrs

        attrs['state'] = RevisionModel.State.VALIDATED
        self.initial_data['state'] = RevisionModel.State.VALIDATED

        return attrs
