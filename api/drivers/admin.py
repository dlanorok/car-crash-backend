from django.contrib import admin

# Register your models here.
from api.drivers.models import Driver

admin.site.register(Driver)
