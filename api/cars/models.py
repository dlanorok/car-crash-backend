from django.db import models
from multiselectfield import MultiSelectField

from api.common.enums import Enum
from api.common.models.base import RevisionModel
from api.crashes.models import Crash
from api.drivers.models import Driver


class Car(RevisionModel):
    crash = models.ForeignKey(Crash, on_delete=models.CASCADE, related_name='cars')
    creator = models.CharField(max_length=128, blank=True)  # session_id
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)
    damaged_parts = MultiSelectField(choices=Enum.DAMAGED_PARTS, max_length=3, blank=True)
    initial_impact = MultiSelectField(choices=Enum.INITIAL_IMPACT, max_length=3, blank=True)

    name = models.CharField(max_length=128, default=False, blank=True)
    registration_plate = models.CharField(max_length=8, blank=True)
