from rest_framework import serializers

from api.files.models import File
from api.sketches.models import Sketch


class SketchSerializer(serializers.ModelSerializer):
    file = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())

    class Meta:
        model = Sketch
        fields = '__all__'
