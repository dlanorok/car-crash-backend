from django.db import models

from api.cars.models import Car
from api.common.models.base import RevisionModel


class Circumstance(RevisionModel):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True, related_name='circumstances')

    parked_stopped = models.BooleanField(default=False) # 1
    leaving_parking_opening_door = models.BooleanField(default=False) # 2
    entering_parking = models.BooleanField(default=False) # 3
    emerging_from_car_park = models.BooleanField(default=False) # 4
    entering_car_park = models.BooleanField(default=False) # 5
    entering_roundabout = models.BooleanField(default=False) # 6
    circulating_roundabout = models.BooleanField(default=False) # 7
    rear_same_direction = models.BooleanField(default=False) # 8
    straight = models.BooleanField(default=False)
    same_direction_different_lane = models.BooleanField(default=False) # 9
    changing_lanes = models.BooleanField(default=False) # 10
    overtaking = models.BooleanField(default=False) # 11
    turning_right = models.BooleanField(default=False) # 12
    turning_left = models.BooleanField(default=False) # 13
    reversing = models.BooleanField(default=False) # 14
    driving_on_opposite_lane = models.BooleanField(default=False) # 15
    from_right_crossing = models.BooleanField(default=False) # 16
    disregarding_right_of_way_red_light = models.BooleanField(default=False) # 17

    def is_valid(self):
        return True
        # return self.parked_stopped or \
        #        self.leaving_parking_opening_door or \
        #        self.entering_parking or \
        #        self.emerging_from_car_park or \
        #        self.entering_car_park or \
        #        self.entering_roundabout or \
        #        self.circulating_roundabout or \
        #        self.rear_same_direction or \
        #        self.same_direction_different_lane or \
        #        self.changing_lanes or \
        #        self.overtaking or \
        #        self.turning_right or \
        #        self.turning_left or \
        #        self.reversing or \
        #        self.driving_on_opposite_lane or \
        #        self.from_right_crossing or \
        #        self.disregarding_right_of_way_red_light or \
        #        self.straight
