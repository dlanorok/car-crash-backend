from rest_framework import serializers

from api.sketches.models import Sketch,SketchCar


class SketchCarSerializer(serializers.ModelSerializer):
    sketch = serializers.PrimaryKeyRelatedField(queryset=Sketch.objects.all(), many=False)

    class Meta:
        model = SketchCar
        fields = ['id', 'sketch', 'car_id', 'position_south', 'position_west', 'position_north', 'position_east', 'rotation']


class SketchSerializer(serializers.ModelSerializer):
    sketch_cars = SketchCarSerializer(many=True, required=False)

    class Meta:
        model = Sketch
        fields = '__all__'

    def create(self, validated_data):
        cars_data = validated_data.pop('sketch_cars')
        sketch = Sketch.objects.create(**validated_data)

        self.update_cars(sketch, cars_data)

        return sketch

    def update(self, instance, validated_data):
        cars_data = validated_data.pop('sketch_cars')
        super().update(instance, validated_data)

        self.update_cars(instance, cars_data)

        return instance


    def update_cars(self, sketch, cars_data):
        if cars_data:
            SketchCar.objects.filter(sketch=sketch).delete()
            for car_data in cars_data:
                SketchCar.objects.create(sketch=sketch, **car_data)
