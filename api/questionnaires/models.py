from django.db import models

from api.common.models.base import RevisionModel
from api.crashes.models import Crash


class Questionnaire(RevisionModel):
    data = models.JSONField()
    creator = models.CharField(max_length=128, blank=True)
    crash = models.ForeignKey(Crash, on_delete=models.CASCADE, related_name='questionnaires')
