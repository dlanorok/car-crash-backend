from django.db import models

from api.cars.models import Car
from api.common.models.base import RevisionModel


class Driver(RevisionModel):
    name = models.CharField(max_length=256, null=True)
    surname = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=256, null=True)
    date_of_birth = models.DateTimeField(null=True)
    driving_licence_number = models.CharField(max_length=256, null=True)
    driving_licence_category = models.CharField(max_length=256, null=True)
    driving_licence_valid_from = models.DateTimeField(null=True)
    driving_licence_valid_to = models.DateTimeField(null=True)

    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True, related_name='driver')

    def is_valid(self):
        return self.name and \
               self.surname and \
               self.address and \
               self.email and \
               self.phone_number and \
               self.driving_licence_number and \
               self.driving_licence_valid_to
