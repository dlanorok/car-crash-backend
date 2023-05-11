from rest_framework import serializers

from api.cars.models import Car
from api.drivers.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=False)

    class Meta:
        model = Driver
        fields = '__all__'
