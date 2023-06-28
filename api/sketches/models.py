from django.db import models

# Create your models here.
from api.cars.models import Car
from api.common.models.base import RevisionModel
from api.crashes.models import Crash

class Sketch(RevisionModel):
    crash = models.ForeignKey(Crash, on_delete=models.CASCADE, related_name='sketches')
    creator = models.CharField(max_length=128, blank=True)
    polygons = models.JSONField(blank=True, null=True)

class SketchCar(models.Model):
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE, related_name='sketch_cars')
    car_id = models.IntegerField()
    position_south = models.FloatField()
    position_west = models.FloatField()
    position_north = models.FloatField()
    position_east = models.FloatField()
    rotation = models.FloatField()
