from django.contrib import admin

# Register your models here.
from api.insurances.models import Insurance

admin.site.register(Insurance)
