from rest_framework import serializers

from api.cars.models import Car
from api.cars.serializers import CarSerializer, CarJsonSerializer
from api.common.models.base import RevisionModel
from api.common.serializer import ValidationSerializer
from api.crashes.models import Crash


class CrashSerializer(ValidationSerializer):
    cars = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True, required=False)
    sketch = serializers.PrimaryKeyRelatedField(read_only=True)
    my_cars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Crash
        fields = '__all__'
        read_only_fields = ['session_id', 'closed', 'revision', 'creator']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get('request', None)

        if not request:
            return representation

        session_key = request.session.session_key

        if session_key:
            cars = Car.objects.filter(creator=session_key, crash__session_id=instance.session_id)
            representation['my_cars'] = [car.id for car in cars]

        return representation

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


class CrashJSONSerializer(serializers.ModelSerializer):
    cars = CarJsonSerializer(many=True)

    class Meta:
        model = Crash
        fields = '__all__'
