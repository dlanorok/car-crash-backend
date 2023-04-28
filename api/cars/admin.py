from django.contrib import admin

# Register your models here.
from api.cars.models import Car

admin.site.register(Car)
