from rest_framework import serializers

from api.common.models.base import RevisionModel


class ValidationSerializer(serializers.ModelSerializer):
    validate = serializers.BooleanField()

    def should_validate(self):
        return self.initial_data.get('validate', False)


class CreateSerializerStateChange(serializers.ModelSerializer):
    def create(self, validated_data):
        if validated_data.get('state', RevisionModel.State.EMPTY) is not RevisionModel.State.VALIDATED:
            validated_data['state'] = RevisionModel.State.PARTIAL

        return super().create(validated_data)


class SmsSerializer(serializers.Serializer):
    recipient = serializers.CharField(max_length=255)
    content = serializers.CharField()

