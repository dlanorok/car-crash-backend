from rest_framework import serializers

from api.cars.models import Car
from api.circumstances.models import Circumstance


class CircumstanceSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=False)

    class Meta:
        model = Circumstance
        fields = '__all__'
