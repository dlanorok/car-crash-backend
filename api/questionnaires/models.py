from django.db import models

from api.cars.models import Car
from api.circumstances.models import Circumstance
from api.common.models.base import RevisionModel
from api.crashes.models import Crash
from api.insurances.models import Insurance
from api.policy_holders.models import PolicyHolder


class Questionnaire(RevisionModel):
    data = models.JSONField()
    creator = models.CharField(max_length=128, blank=True)
    crash = models.ForeignKey(Crash, on_delete=models.CASCADE, related_name='questionnaires')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')
    crash_confirmed = models.BooleanField(default=False)
