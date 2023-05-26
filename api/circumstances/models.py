from django.db import models

from api.cars.models import Car
from api.common.models.base import RevisionModel


class Circumstance(RevisionModel):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True, related_name='circumstances')

    parked_stopped = models.BooleanField(default=False)
    leaving_parking_opening_door = models.BooleanField(default=False)
    entering_parking = models.BooleanField(default=False)
    emerging_from_car_park = models.BooleanField(default=False)
    entering_car_park = models.BooleanField(default=False)
    entering_roundabout = models.BooleanField(default=False)
    circulating_roundabout = models.BooleanField(default=False)
    rear_same_direction = models.BooleanField(default=False)
    same_direction_different_lane = models.BooleanField(default=False)
    changing_lanes = models.BooleanField(default=False)
    overtaking = models.BooleanField(default=False)
    turning_right = models.BooleanField(default=False)
    turning_left = models.BooleanField(default=False)
    reversing = models.BooleanField(default=False)
    driving_on_opposite_lane = models.BooleanField(default=False)
    from_right_crossing = models.BooleanField(default=False)
    disregarding_right_of_way_red_light = models.BooleanField(default=False)
