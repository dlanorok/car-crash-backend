from django.db import models

from api.cars.models import Car
from api.common.models.base import RevisionModel


class Insurance(RevisionModel):
    policy_number = models.CharField(max_length=256, null=True)
    agent = models.CharField(max_length=256, null=True)
    green_card = models.CharField(max_length=256, null=True)
    valid_until = models.DateTimeField(null=True)
    damage_insured = models.BooleanField(null=True)

    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True, related_name='insurances')
