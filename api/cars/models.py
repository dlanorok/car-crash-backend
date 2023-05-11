from django.db import models
from multiselectfield import MultiSelectField

from api.common.enums import Enum
from api.common.models.base import RevisionModel
from api.crashes.models import Crash


class Car(RevisionModel):
    crash = models.ForeignKey(Crash, on_delete=models.CASCADE, related_name='cars')
    creator = models.CharField(max_length=128, blank=True)  # session_id

    make_type = models.CharField(max_length=128, blank=True)
    registration_plate = models.CharField(max_length=8, blank=True)

    damaged_parts = MultiSelectField(choices=Enum.DAMAGED_PARTS, max_length=3, blank=True)
    initial_impact = MultiSelectField(choices=Enum.INITIAL_IMPACT, max_length=3, blank=True)
