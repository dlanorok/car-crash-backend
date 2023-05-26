from django.db import models

from api.cars.models import Car
from api.common.models.base import RevisionModel


class Driver(RevisionModel):
    name = models.CharField(max_length=256, null=True)
    surname = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
    driving_licence_number = models.CharField(max_length=256, null=True)
    driving_licence_valid_from = models.DateTimeField(null=True)
    driving_licence_valid_to = models.DateTimeField(null=True)

    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True, related_name='driver')
