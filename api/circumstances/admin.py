from django.contrib import admin

# Register your models here.
from api.circumstances.models import Circumstance

admin.site.register(Circumstance)
