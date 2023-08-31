from django.contrib import admin

# Register your models here.
from api.crashes.models import Crash

admin.site.register(Crash)
