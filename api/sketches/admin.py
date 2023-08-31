from django.contrib import admin

# Register your models here.
from api.sketches.models import Sketch

admin.site.register(Sketch)
