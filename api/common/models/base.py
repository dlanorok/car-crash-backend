from django.db import models


class RevisionModel(models.Model):
    class State(models.TextChoices):
        EMPTY = 'E', 'Empty'
        PARTIAL = 'P', 'Partial'
        VALIDATED = 'V', 'Validated'

    revision = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.revision = self.revision + 1
        super().save()

    class Meta:
        abstract = True
