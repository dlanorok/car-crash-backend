import random
import string

from django.db import models

from api.common.models.base import RevisionModel


def generate_unique_code():
    length = 5
    while True:
        session_id = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Crash.objects.filter(session_id=session_id).count() == 0:
            break

    return session_id


class Crash(RevisionModel):
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=8, default=generate_unique_code, unique=True, null=True)
    closed = models.BooleanField(default=False)
    participants = models.IntegerField(default=2)
    creator = models.CharField(max_length=128, blank=True)

    date_of_accident = models.DateTimeField(null=True)
    country = models.CharField(max_length=256, null=True)
    place = models.CharField(max_length=256, null=True)
    injuries = models.BooleanField(null=True)
    vehicle_material_damage = models.BooleanField(null=True)
    other_material_damage = models.BooleanField(null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # If crash was sent and closed, free session_id
        if self.closed:
            self.session_id = None

        super().save(force_insert, force_update, using, update_fields)
