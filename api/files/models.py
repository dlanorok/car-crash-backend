from django.db import models

from api.cars.models import Car


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=256)
