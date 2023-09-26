from django.db import models

from api.cars.models import Car
from api.common.models.base import RevisionModel


class PolicyHolder(RevisionModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    email_phone_number = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    country_code = models.CharField(max_length=128, blank=True, null=True)

    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True, related_name='policy_holder')

    def is_valid(self):
        return self.name and self.email_phone_number and self.address and self.country_code
