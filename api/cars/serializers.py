from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from api.cars.models import Car
from api.common.enums import Enum


class CarSerializer(serializers.ModelSerializer):
    damaged_parts = MultipleChoiceField(choices=Enum.DAMAGED_PARTS)
    initial_impact = MultipleChoiceField(choices=Enum.INITIAL_IMPACT)

    class Meta:
        model = Car
        fields = '__all__'
