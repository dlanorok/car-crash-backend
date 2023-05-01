from rest_framework import serializers

from api.cars.models import Car
from api.crashes.models import Crash


class CrashSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True, required=False)

    class Meta:
        model = Crash
        fields = '__all__'


class CreateCrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crash
        fields = []
