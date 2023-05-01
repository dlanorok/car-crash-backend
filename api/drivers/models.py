from django.db import models

from api.common.models.base import RevisionModel


class Driver(RevisionModel):
    name = models.CharField(max_length=128, blank=True)
    surname = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=256, blank=True)
    post_number = models.CharField(max_length=256, blank=True)
    country_code = models.CharField(max_length=128, blank=True)
