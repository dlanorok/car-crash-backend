from rest_framework import serializers

from api.cars.models import Car
from api.policy_holders.models import PolicyHolder


class PolicyHolderSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=False)

    class Meta:
        model = PolicyHolder
        fields = '__all__'
