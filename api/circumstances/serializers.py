from rest_framework import serializers

from api.cars.models import Car
from api.circumstances.models import Circumstance
from api.common.models.base import RevisionModel


class CircumstanceSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=False)

    class Meta:
        model = Circumstance
        fields = '__all__'

    def create(self, validated_data):
        validated_data['state'] = RevisionModel.State.VALIDATED
        return super().create(validated_data)
