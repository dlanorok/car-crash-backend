from django.core.files.storage import get_storage_class
from django.db import models

from config import settings


class OverwriteStorage(get_storage_class()):

    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name

def file_generate_upload_path(instance, filename):
	# Both filename and instance.file_name should have the same values
    return f"files/{instance.file_name}"

class File(models.Model):
    file = models.FileField(upload_to=file_generate_upload_path, storage=OverwriteStorage())
    file_name = models.CharField(max_length=256)
    file_size = models.CharField(max_length=256)

    upload_finished_at = models.DateTimeField(blank=True, null=True)

    @property
    def is_valid(self):
        return bool(self.upload_finished_at)

    @property
    def url(self):
        if settings.FILE_UPLOAD_STORAGE == "s3":
            return self.file.url

        return f"{settings.APP_DOMAIN}{self.file.url}"
