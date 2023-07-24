import json
import os

from jsonschema import validate, ValidationError
from rest_framework import serializers

from api.crashes.models import Crash
from api.questionnaires.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    crash = serializers.PrimaryKeyRelatedField(queryset=Crash.objects.all(), many=False)

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

    class Meta:
        model = Questionnaire
        fields = '__all__'
