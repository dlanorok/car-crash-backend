from django.db import models
from multiselectfield import MultiSelectField

from api.common.enums import Enum
from api.common.models.base import RevisionModel
from api.crashes.models import Crash
from django.apps import apps

from api.files.models import File


class Car(RevisionModel):
    crash = models.ForeignKey(Crash, on_delete=models.CASCADE, related_name='cars')
    creator = models.CharField(max_length=128, blank=True)
    participants_count = models.IntegerField(default=2)

    car_type = models.CharField(max_length=128, blank=True)
    make_type = models.CharField(max_length=128, blank=True)
    registration_country = models.CharField(max_length=256, blank=True)
    registration_plate = models.CharField(max_length=256, blank=True)

    damaged_parts = MultiSelectField(choices=Enum.DAMAGED_PARTS, max_length=200, blank=True)
    initial_impact = MultiSelectField(choices=Enum.INITIAL_IMPACT, max_length=200, blank=True)

    initial_impact_svg_file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='initial_impact_car', blank=True, null=True)
    damaged_parts_svg_file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='damaged_parts_car', blank=True, null=True)

    def save(self, *args, **kwargs):
        is_new_car = self.pk is None
        super(Car, self).save(args, kwargs)
        if is_new_car:
            apps.get_model('insurances', 'Insurance').objects.create(car=self)
            apps.get_model('drivers', 'Driver').objects.create(car=self)
            apps.get_model('circumstances', 'Circumstance').objects.create(car=self)
            apps.get_model('policy_holders', 'PolicyHolder').objects.create(car=self)
