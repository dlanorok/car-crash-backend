from rest_framework import serializers

from api.cars.models import Car
from api.insurances.models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=False)

    class Meta:
        model = Insurance
        fields = '__all__'
