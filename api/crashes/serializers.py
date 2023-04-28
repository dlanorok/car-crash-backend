from rest_framework import serializers

from api.crashes.models import Crash


class CrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crash
        fields = '__all__'


class CreateCrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crash
        fields = []
