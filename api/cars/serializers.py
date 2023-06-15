from rest_framework.fields import MultipleChoiceField

from api.cars.models import Car
from api.circumstances.serializers import CircumstanceSerializer
from api.common.enums import Enum
from api.common.serializer import ValidationSerializer
from api.drivers.serializers import DriverSerializer
from api.insurances.serializers import InsuranceSerializer
from api.policy_holders.serializers import PolicyHolderSerializer


class CarSerializer(ValidationSerializer):
    damaged_parts = MultipleChoiceField(choices=Enum.DAMAGED_PARTS, required=False)
    initial_impact = MultipleChoiceField(choices=Enum.INITIAL_IMPACT, required=False)
    policy_holder = PolicyHolderSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)
    insurance = InsuranceSerializer(read_only=True)
    circumstances = CircumstanceSerializer(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['damaged_parts'] = list(representation['damaged_parts'])
        representation['initial_impact'] = list(representation['initial_impact'])
        return representation

