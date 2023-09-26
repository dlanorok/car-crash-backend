from django.db import models

# Create your models here.
from api.cars.models import Car
from api.common.models.base import RevisionModel
from api.crashes.models import Crash
from api.files.models import File


class Sketch(RevisionModel):
    crash = models.OneToOneField(Crash, on_delete=models.CASCADE, related_name='sketch', null=True, blank=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='sketch', blank=True, null=True)
    confirmed_editors = models.CharField(max_length=256, blank=True, null=True)

    def is_valid(self):
        return self.file and self.confirmed_editors and len(self.confirmed_editors.split(",")) >= 1
