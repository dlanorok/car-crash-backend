from rest_framework import serializers

from api.cars.models import Car
from api.common.models.base import RevisionModel
from api.common.serializer import ValidationSerializer, UpdateSerializerStateChange
from api.crashes.models import Crash


class CrashSerializer(ValidationSerializer, UpdateSerializerStateChange):
    cars = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True, required=False)

    class Meta:
        model = Crash
        fields = '__all__'

    def validate(self, attrs):
        if not self.should_validate():
            return attrs

        date_of_accident = attrs.get('date_of_accident')
        country = attrs.get('country')
        place = attrs.get('place')
        errors = {}

        if not date_of_accident:
            errors['date_of_accident'] = 'Date cannot be null'
        if not country:
            errors['country'] = 'Country cannot be null'
        if not place:
            errors['place'] = 'Country cannot be null'

        if errors:
            raise serializers.ValidationError(errors)

        attrs['state'] = RevisionModel.State.VALIDATED
        self.initial_data['state'] = RevisionModel.State.VALIDATED

        return attrs


class CreateCrashSerializer(ValidationSerializer):
    class Meta:
        model = Crash
        fields = ['date_of_accident', 'country', 'place', 'injuries', 'vehicle_material_damage', 'other_material_damage']
