import json
import os

from django.utils.translation import gettext as _
from jsonschema import validate, ValidationError
from rest_framework import serializers

from api.cars.serializers import CarSerializer
from api.crashes.serializers import CrashSerializer
from api.questionnaires.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    crash = CrashSerializer()
    car = CarSerializer()

    def validate_data(self, value):
        try:
            current_directory = os.path.dirname(os.path.realpath(__file__))
            schema_file_path = os.path.join(current_directory, 'data/questionnaire_schema.json')

            with open(schema_file_path, 'r') as schema_file:
                schema = json.load(schema_file)
            validate(value, schema)
        except (ValidationError, FileNotFoundError) as e:
            raise serializers.ValidationError(str(e))
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for id, section in enumerate(data.get('data').get('sections', [])):
            data['data']['sections'][id]['name'] = _(section['name'])

        for id, step in enumerate(data.get('data').get('steps', [])):
            data['data']['steps'][id]['question'] = _(step['question'])

        for input_id, input in data.get('data').get('inputs', {}).items():
            data['data']['inputs'][input_id].update(placeholder=_(input.get('placeholder'))) if input.get('placeholder') else None
            for option_index, option in enumerate(input.get('options', [])):
                data['data']['inputs'][input_id]['options'][option_index].update(
                    label= _(option['label']) if option.get('label') else None
                )

        return data

    class Meta:
        model = Questionnaire
        fields = '__all__'
